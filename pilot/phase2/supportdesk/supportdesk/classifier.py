"""Deterministic rule-based classifier + field extractor.

A model provider interface is defined so an LLM-backed provider can replace the rules
later. In THIS pilot only RuleProvider exists: LLM-based quality is UNTESTED.
"""
from __future__ import annotations

import re
from typing import Protocol

from .schemas import CATEGORIES

# Keyword -> weight, per category (English + Traditional Chinese). Plain data on purpose:
# a reviewer can read and change it without touching code.
KEYWORDS: dict[str, dict[str, float]] = {
    "billing_invoice": {
        "invoice": 2, "receipt": 1.5, "billing": 2, "charged": 2, "double charge": 3,
        "tax id": 2, "vat": 1.5, "payment failed": 2, "統編": 3, "發票": 3, "收據": 2,
        "扣款": 2.5, "重複扣款": 3, "帳單": 2.5, "付款失敗": 2,
    },
    "shipping_delivery": {
        "shipping": 2, "delivery": 2, "tracking": 2.5, "not arrived": 3, "hasn't arrived": 3,
        "where is my order": 3, "courier": 1.5, "late": 1, "address": 1,
        "物流": 2.5, "配送": 2.5, "出貨": 2, "還沒收到": 3, "沒收到": 2.5, "追蹤": 2, "寄送": 2,
    },
    "returns_refund": {
        "refund": 3, "return": 2, "exchange": 2, "wrong item": 2.5, "damaged": 2,
        "broken": 2, "defective": 2.5, "退貨": 3, "退款": 3, "換貨": 2.5, "瑕疵": 2.5, "損壞": 2,
        "壞掉": 2, "寄錯": 2.5,
    },
    "account_access": {
        "password": 2.5, "login": 3, "log in": 3, "sign in": 2.5, "locked": 2.5,
        "two-factor": 2.5, "2fa": 2.5, "reset": 2, "can't access": 3, "verification code": 2,
        "登入": 3, "密碼": 2.5, "帳號": 2, "鎖定": 2.5, "驗證碼": 2.5, "重設": 2,
    },
    "product_question": {
        "does it support": 3, "compatible": 2.5, "specification": 2, "specs": 2, "warranty": 2,
        "how do i": 1.5, "which model": 2, "size": 1, "dimension": 1.5, "battery": 1.5,
        "支援": 2, "相容": 2.5, "規格": 2.5, "保固": 2.5, "尺寸": 2, "怎麼使用": 2, "請問": 1,
    },
    "complaint_escalation": {
        "lawyer": 4, "legal action": 4, "sue": 3.5, "consumer protection": 4, "unacceptable": 2,
        "furious": 2.5, "worst": 2, "complaint": 2, "media": 2, "scam": 3.5,
        "律師": 4, "提告": 4, "消保官": 4, "消基會": 4, "客訴": 3, "太過分": 2.5, "詐騙": 3.5, "投訴": 3,
    },
}

ORDER_RE = re.compile(r"\b(ORD-\d{6})\b", re.I)
INVOICE_RE = re.compile(r"\b(INV-\d{6})\b", re.I)
AMOUNT_RE = re.compile(r"(?:NT\$|TWD|USD|\$)\s?([\d,]+(?:\.\d+)?)", re.I)
_CJK_RE = re.compile(r"[一-鿿]")

CATEGORIES_REQUIRING_ORDER = {"shipping_delivery", "returns_refund"}


def detect_language(text: str) -> str:
    cjk = len(_CJK_RE.findall(text))
    return "zh-TW" if cjk >= max(3, 0.1 * max(len(text), 1)) else "en"


def extract_fields(text: str) -> dict[str, str | None]:
    order = ORDER_RE.search(text)
    inv = INVOICE_RE.search(text)
    amt = AMOUNT_RE.search(text)
    return {
        "order_id": order.group(1).upper() if order else None,
        "invoice_id": inv.group(1).upper() if inv else None,
        "amount": amt.group(1).replace(",", "") if amt else None,
    }


def _compile(kw: str) -> re.Pattern:
    """ASCII keywords match on word boundaries (+ simple inflections); CJK matches as substring.

    FIX 2026-11-17: plain substring matching made 'sue' fire inside 'reissue' (found by HELDOUT H01).
    """
    if re.search(r"[a-z]", kw):
        return re.compile(r"(?<![a-z0-9])" + re.escape(kw) + r"(?:s|es|ed|ing)?(?![a-z0-9])")
    return re.compile(re.escape(kw))


_COMPILED = {cat: {kw: (_compile(kw), w) for kw, w in words.items()} for cat, words in KEYWORDS.items()}


def score_categories(text: str) -> dict[str, float]:
    low = text.lower()
    scores = {c: 0.0 for c in CATEGORIES if c != "other"}
    for cat, words in _COMPILED.items():
        for _kw, (rx, w) in words.items():
            if rx.search(low):
                scores[cat] += w
    return scores


class ModelProvider(Protocol):
    name: str

    def classify(self, subject: str, body: str) -> tuple[str, float, dict[str, float]]:
        """Return (category, confidence 0..1, raw_scores)."""


class RuleProvider:
    name = "rules-v1"

    def classify(self, subject: str, body: str) -> tuple[str, float, dict[str, float]]:
        # Subject counts double: customers put the intent there.
        scores = score_categories(f"{subject} {subject} {body}")
        ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
        (top, s1), (_, s2) = ranked[0], ranked[1]
        if s1 <= 0:
            return "other", 0.0, scores
        confidence = round(s1 / (s1 + s2 + 1.0), 3)
        return top, confidence, scores
