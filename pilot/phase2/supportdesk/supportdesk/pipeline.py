"""Pipeline: validate -> redact -> classify/extract -> retrieve -> draft -> escalate/hold -> store.

Nothing is "sent" by the pipeline. Drafts stay `pending_approval` until a human approves
(see approve()/reject()); escalated items have NO draft and need a human to write.
"""
from __future__ import annotations

import json
import hashlib
from pathlib import Path

from . import guardrails
from .classifier import (CATEGORIES_REQUIRING_ORDER, RuleProvider, detect_language,
                         extract_fields)
from .drafter import build_draft
from .retrieval import KnowledgeBase
from .schemas import SupportRequest, TriageResult, ValidationError
from .store import Store, idem_key, with_retry

ROOT = Path(__file__).resolve().parent.parent


def load_config(path: Path | None = None) -> dict:
    return json.loads((path or ROOT / "config" / "config.json").read_text(encoding="utf-8"))


class Pipeline:
    def __init__(self, store: Store | None = None, kb: KnowledgeBase | None = None,
                 config: dict | None = None, provider=None):
        self.store = store or Store()
        self.kb = kb or KnowledgeBase.load(ROOT / "kb" / "articles.json")
        self.config = config or load_config()
        self.provider = provider or RuleProvider()
        self.config_hash = hashlib.sha256(json.dumps(self.config, sort_keys=True).encode()).hexdigest()[:10]

    # ------------------------------------------------------------------
    def process(self, raw) -> dict:
        """Process one raw request. Returns {'outcome': ..., 'idem_key': ..., 'result': ...}."""
        try:
            req = SupportRequest.from_raw(raw)
        except ValidationError as exc:
            self.store.add_dead_letter(str(exc), raw)
            self.store.audit("dead_letter", None, {"reason": str(exc)})
            return {"outcome": "dead_letter", "idem_key": None, "reason": str(exc)}

        key = idem_key(req.channel, req.message_id)
        if self.store.has_result(key):
            self.store.audit("duplicate_skipped", key, {})
            return {"outcome": "duplicate", "idem_key": key, "result": self.store.get_result(key)}

        text = f"{req.subject}\n{req.body}"
        red_subject, k1 = guardrails.redact(req.subject)
        red_body, k2 = guardrails.redact(req.body)
        kinds = sorted(set(k1 + k2))
        injection = guardrails.detect_injection(text)

        category, confidence, scores = self.provider.classify(req.subject, req.body)
        language = detect_language(text)
        # Extract from the redacted text so a card number can never end up in a field.
        extracted = extract_fields(f"{red_subject}\n{red_body}")

        reasons: list[str] = []
        flags: list[str] = []
        if injection:
            reasons.append("prompt_injection_suspected"); flags.append("injection")
        if guardrails.has_sensitive(kinds):
            reasons.append("sensitive_data_present"); flags.append("pii:" + ",".join(kinds))
        if category in self.config["always_escalate_categories"]:
            reasons.append("category_requires_human")
        # Multi-intent guard (added after HELDOUT H16 produced an auto-draft that answered only one of
        # two requests). Tuned with knowledge of H16 -> HELDOUT is no longer clean for this rule.
        ranked = sorted(scores.values(), reverse=True)
        if (category != "other" and len(ranked) > 1
                and ranked[1] >= self.config["multi_intent_min_second_score"]
                and ranked[1] >= self.config["multi_intent_ratio"] * ranked[0]):
            reasons.append("multi_intent")
        if category == "other":
            reasons.append("unclassified")
        elif confidence < self.config["min_confidence"]:
            reasons.append("low_confidence")
        needs_order = category in CATEGORIES_REQUIRING_ORDER
        if needs_order and not extracted["order_id"]:
            reasons.append("missing_order_id")

        hits = [] if (injection or category == "other") else self.kb.search(
            f"{red_subject} {red_body}", category=category)
        top_score = hits[0][1] if hits else 0.0
        if not hits or top_score < self.config["min_retrieval_score"]:
            hits = []
            if category != "other":
                reasons.append("no_kb_match")

        # A draft is produced only if the case is NOT an escalation for a hard reason.
        hard = {"prompt_injection_suspected", "category_requires_human", "unclassified",
                "low_confidence", "no_kb_match", "multi_intent"}
        # missing_order_id and sensitive_data_present still allow a *clarifying* draft but need review.
        draft = ""
        if not (set(reasons) & hard):
            draft = build_draft(language, hits, extracted["order_id"], needs_order,
                                sensitive_note="sensitive_data_present" in reasons)
        needs_human = bool(reasons)
        status = "pending_approval" if draft else "escalated"
        if not draft and not needs_human:  # defensive: never leave a silent no-reply
            reasons.append("no_draft_generated"); needs_human = True
        if needs_human and status == "pending_approval":
            flags.append("review_clarifying_draft")

        result = TriageResult(
            message_id=req.message_id, category=category,
            priority=self.config["priority_rules"].get(category, "low"),
            language=language, confidence=confidence, needs_human=needs_human,
            escalation_reasons=sorted(set(reasons)), extracted=extracted,
            kb_refs=[a["id"] for a, _ in hits], draft_reply=draft, flags=flags,
            config_version=f"{self.config['config_version']}+{self.config_hash}", status=status)

        attempts = self.config["retry"]["attempts"]; backoff = self.config["retry"]["backoff_seconds"]
        with_retry(lambda: self.store.save_request(key, req, red_subject, red_body), attempts, backoff)
        with_retry(lambda: self.store.save_result(key, result), attempts, backoff)
        with_retry(lambda: self.store.upsert_ticket(key, category, result.priority,
                                                    extracted["order_id"], status), attempts, backoff)
        self.store.audit("triaged", key, {
            "category": category, "confidence": confidence, "status": status,
            "reasons": result.escalation_reasons, "kb": result.kb_refs, "config": result.config_version,
            "provider": getattr(self.provider, "name", "?")})
        return {"outcome": status, "idem_key": key, "result": result.to_dict()}

    # ------------------------------------------------------------------
    def approve(self, key: str, approver: str) -> dict:
        res = self.store.get_result(key)
        if res is None:
            raise KeyError(key)
        if res["status"] != "pending_approval":
            hint = ("already sent" if res["status"] == "sent" else
                    "escalated items have no draft; a human must write the reply"
                    if res["status"] == "escalated" else "not awaiting approval")
            raise ValueError(f"cannot approve item in status {res['status']!r}: {hint}")
        if guardrails.violates_commitments(res["draft_reply"]):
            raise ValueError("draft violates commitment policy")
        sent = self.store.send(key, res["draft_reply"], approver)
        self.store.set_status(key, "sent")
        self.store.upsert_ticket(key, res["category"], res["priority"], res["extracted"].get("order_id"), "replied")
        self.store.audit("approved_and_sent", key, {"approver": approver, "first_send": sent})
        return {"sent": sent}

    def reject(self, key: str, approver: str, reason: str) -> None:
        self.store.set_status(key, "rejected")
        self.store.audit("rejected", key, {"approver": approver, "reason": reason})
