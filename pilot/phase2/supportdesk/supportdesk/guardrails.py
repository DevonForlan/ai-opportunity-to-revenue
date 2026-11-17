"""Guardrails: PII redaction, prompt-injection detection, forbidden commitments."""
from __future__ import annotations

import re

# Card-like numbers: 13-19 digits optionally separated by spaces/dashes.
_CARD_RE = re.compile(r"\b(?:\d[ -]?){13,19}\b")
_TW_ID_RE = re.compile(r"\b[A-Z][12]\d{8}\b")
_EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
_PHONE_RE = re.compile(r"(?<!\d)(?:\+?886[- ]?|0)9\d{2}[- ]?\d{3}[- ]?\d{3}(?!\d)")
_PASSWORD_RE = re.compile(r"(password|passwd|密碼)\s*(is|:|：|為|是)\s*\S+", re.I)

INJECTION_PATTERNS = [
    r"ignore (all |any |the )?(previous|above|prior|earlier) (instructions|rules|prompts?)",
    r"disregard (all |any |the )?(previous|above|prior) ",
    r"(reveal|show|print|repeat) (your |the )?(system )?(prompt|instructions)",
    r"you are now ",
    r"act as (an? )?(admin|developer|root|system)",
    r"developer mode",
    r"忽略(以上|之前|先前|上述)?(所有|全部)?(的)?(指示|指令|規則|提示)",
    r"(顯示|洩漏|透露|印出)(你的)?(系統)?(提示|指令|prompt)",
    r"你現在是",
    r"approve (this|the) (refund|request) automatically",
    r"自動(核准|批准|退款)",
]
_INJECTION_RE = re.compile("|".join(f"(?:{p})" for p in INJECTION_PATTERNS), re.I)

# Commitments an automatically drafted reply must never make.
FORBIDDEN_COMMITMENTS = [
    "guarantee",
    "full refund",
    "refund immediately",
    "we promise",
    "legal liability",
    "我們保證",
    "一定退款",
    "立即退款",
    "全額退費",
    "賠償",
]


def redact(text: str) -> tuple[str, list[str]]:
    """Return (redacted_text, kinds_found)."""
    kinds: list[str] = []

    def sub(rx: re.Pattern, label: str, s: str) -> str:
        if rx.search(s):
            kinds.append(label)
            return rx.sub(f"[REDACTED_{label.upper()}]", s)
        return s

    out = text
    out = sub(_PASSWORD_RE, "password", out)
    out = sub(_CARD_RE, "card", out)
    out = sub(_TW_ID_RE, "national_id", out)
    out = sub(_EMAIL_RE, "email", out)
    out = sub(_PHONE_RE, "phone", out)
    return out, kinds


SENSITIVE_KINDS = {"card", "national_id", "password"}


def has_sensitive(kinds: list[str]) -> bool:
    return any(k in SENSITIVE_KINDS for k in kinds)


def detect_injection(text: str) -> bool:
    return bool(_INJECTION_RE.search(text))


def violates_commitments(draft: str) -> list[str]:
    low = draft.lower()
    return [p for p in FORBIDDEN_COMMITMENTS if p.lower() in low]
