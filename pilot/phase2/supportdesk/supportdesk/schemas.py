"""Input / output schemas and validation. All data in this pilot is SYNTHETIC."""
from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict
from typing import Any, Optional

CATEGORIES = (
    "billing_invoice",
    "shipping_delivery",
    "returns_refund",
    "account_access",
    "product_question",
    "complaint_escalation",
    "other",
)
CHANNELS = ("email", "form")
MAX_BODY_CHARS = 5000
MAX_SUBJECT_CHARS = 300
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class ValidationError(ValueError):
    """Raised when an incoming request does not satisfy the input schema."""


@dataclass(frozen=True)
class SupportRequest:
    message_id: str
    channel: str
    sender: str
    subject: str
    body: str
    received_at: str

    @staticmethod
    def from_raw(raw: Any) -> "SupportRequest":
        if not isinstance(raw, dict):
            raise ValidationError("request must be an object")
        for key in ("message_id", "channel", "sender", "subject", "body", "received_at"):
            if key not in raw:
                raise ValidationError(f"missing field: {key}")
            if not isinstance(raw[key], str):
                raise ValidationError(f"field {key} must be a string")
        if not raw["message_id"].strip():
            raise ValidationError("message_id is empty")
        if raw["channel"] not in CHANNELS:
            raise ValidationError(f"unknown channel: {raw['channel']!r}")
        if not _EMAIL_RE.match(raw["sender"]):
            raise ValidationError("sender is not an email-like address")
        if not raw["body"].strip():
            raise ValidationError("body is empty")
        if len(raw["body"]) > MAX_BODY_CHARS:
            raise ValidationError("body too long")
        if len(raw["subject"]) > MAX_SUBJECT_CHARS:
            raise ValidationError("subject too long")
        return SupportRequest(
            message_id=raw["message_id"].strip(),
            channel=raw["channel"],
            sender=raw["sender"].strip(),
            subject=raw["subject"].strip(),
            body=raw["body"],
            received_at=raw["received_at"],
        )


@dataclass
class TriageResult:
    message_id: str
    category: str
    priority: str
    language: str
    confidence: float
    needs_human: bool
    escalation_reasons: list[str] = field(default_factory=list)
    extracted: dict[str, Optional[str]] = field(default_factory=dict)
    kb_refs: list[str] = field(default_factory=list)
    draft_reply: str = ""
    flags: list[str] = field(default_factory=list)
    config_version: str = ""
    status: str = "pending_approval"  # pending_approval | escalated | approved | rejected | sent

    def to_dict(self) -> dict:
        return asdict(self)
