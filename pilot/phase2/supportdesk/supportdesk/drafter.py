"""Grounded draft replies: text comes only from KB snippets + fixed templates."""
from __future__ import annotations

from .guardrails import violates_commitments

GREETING = {"en": "Hello,", "zh-TW": "您好，"}
CLOSING = {
    "en": "This reply is a draft reviewed by our support team before sending.",
    "zh-TW": "此為草稿，將由客服人員審核後才會寄出。",
}
ASK_ORDER = {
    "en": "To look into this, could you please reply with your order number (format ORD-123456)?",
    "zh-TW": "為了協助您查詢，請回覆您的訂單編號（格式如 ORD-123456）。",
}
NOTE_SENSITIVE = {
    "en": "For your security, please do not send full card numbers, ID numbers, or passwords by email.",
    "zh-TW": "為了您的安全，請勿透過信件提供完整卡號、身分證字號或密碼。",
}


def build_draft(language: str, kb_hits: list[tuple[dict, float]], order_id: str | None,
                needs_order: bool, sensitive_note: bool) -> str:
    """Return a draft reply, or "" if nothing safe can be drafted."""
    if not kb_hits:
        return ""
    lang = "zh-TW" if language == "zh-TW" else "en"
    key = "text_zh" if lang == "zh-TW" else "text_en"
    lines = [GREETING[lang]]
    if order_id:
        lines.append(f"Re: {order_id}" if lang == "en" else f"關於訂單 {order_id}：")
    for art, _score in kb_hits[:1]:
        lines.append(art[key])
    if needs_order and not order_id:
        lines.append(ASK_ORDER[lang])
    if sensitive_note:
        lines.append(NOTE_SENSITIVE[lang])
    lines.append(CLOSING[lang])
    draft = "\n".join(lines)
    if violates_commitments(draft):  # defensive: templates should never trigger this
        return ""
    return draft
