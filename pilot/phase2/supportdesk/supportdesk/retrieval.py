"""Tiny lexical retrieval over the synthetic KB (stdlib only; EN words + CJK char bigrams)."""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path

_WORD_RE = re.compile(r"[a-z0-9]+")
_CJK_RE = re.compile(r"[一-鿿]+")
_STOP = {"the", "a", "an", "is", "are", "to", "of", "and", "or", "in", "my", "i", "it", "for", "you", "we", "please", "not"}


def tokenize(text: str) -> list[str]:
    low = text.lower()
    # FIX (DEV D25): naive plural stemming so 'invoice' matches 'Invoices'.
    toks = [w[:-1] if len(w) > 3 and w.endswith("s") else w
            for w in _WORD_RE.findall(low) if w not in _STOP and len(w) > 1]
    for run in _CJK_RE.findall(low):
        toks.extend(run[i : i + 2] for i in range(len(run) - 1))
    return toks


class KnowledgeBase:
    def __init__(self, articles: list[dict]):
        self.articles = articles
        self._docs = [Counter(tokenize(f"{a['title']} {a['text_en']} {a['text_zh']}")) for a in articles]
        n = len(self._docs)
        df: Counter = Counter()
        for d in self._docs:
            df.update(d.keys())
        self._idf = {t: math.log((n + 1) / (c + 0.5)) + 1 for t, c in df.items()}

    @classmethod
    def load(cls, path: Path) -> "KnowledgeBase":
        return cls(json.loads(Path(path).read_text(encoding="utf-8")))

    def search(self, query: str, category: str | None = None, k: int = 2) -> list[tuple[dict, float]]:
        q = Counter(tokenize(query))
        if not q:
            return []
        results = []
        for art, doc in zip(self.articles, self._docs):
            if category and art["category"] != category:
                continue
            num = sum(q[t] * doc[t] * self._idf.get(t, 0) ** 2 for t in q if t in doc)
            den = math.sqrt(sum((c * self._idf.get(t, 0)) ** 2 for t, c in q.items())) * math.sqrt(
                sum((c * self._idf.get(t, 0)) ** 2 for t, c in doc.items())
            )
            score = num / den if den else 0.0
            if score > 0:
                results.append((art, round(score, 4)))
        results.sort(key=lambda r: r[1], reverse=True)
        return results[:k]
