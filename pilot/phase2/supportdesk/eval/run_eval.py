"""Run the evaluation on DEV and HELDOUT. Usage: python eval/run_eval.py [--write]"""
from __future__ import annotations

import json
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from eval.cases import DEV, HELDOUT  # noqa: E402
from supportdesk.guardrails import violates_commitments  # noqa: E402
from supportdesk.pipeline import Pipeline  # noqa: E402
from supportdesk.store import Store  # noqa: E402


def run(cases):
    pipe = Pipeline(store=Store())
    rows = []
    lat = []
    for c in cases:
        t0 = time.perf_counter()
        out = pipe.process(c["raw"])
        lat.append((time.perf_counter() - t0) * 1000)
        exp = c["expected"]
        res = out.get("result") or {}
        got_outcome = out["outcome"]
        row = {"id": c["id"], "kind": c["kind"], "exp_outcome": exp["outcome"], "got_outcome": got_outcome,
               "exp_category": exp["category"], "got_category": res.get("category"),
               "exp_order": exp["order_id"], "got_order": (res.get("extracted") or {}).get("order_id"),
               "reasons": res.get("escalation_reasons", out.get("reason")), "leak": False,
               "commit_violation": False, "ungrounded": False}
        if got_outcome != "dead_letter":
            key = out["idem_key"]
            stored = pipe.store.db.execute("SELECT redacted_subject||' '||redacted_body FROM requests WHERE idem_key=?", (key,)).fetchone()[0]
            row["leak"] = any(s in stored or s in json.dumps(res, ensure_ascii=False) for s in exp["no_leak"])
            draft = res.get("draft_reply", "")
            row["commit_violation"] = bool(draft and violates_commitments(draft))
            row["ungrounded"] = bool(draft and not res.get("kb_refs"))
        rows.append(row)
    return rows, lat, pipe


def metrics(rows, lat):
    n = len(rows)
    outcome_ok = sum(r["exp_outcome"] == r["got_outcome"] for r in rows)
    esc = [r for r in rows if r["exp_outcome"] in ("escalated",)]
    pend = [r for r in rows if r["exp_outcome"] == "pending_approval"]
    # false auto-draft: a human-needed case that got an auto draft (the dangerous error)
    false_draft = [r for r in esc if r["got_outcome"] == "pending_approval"]
    over_esc = [r for r in pend if r["got_outcome"] == "escalated"]
    dl = [r for r in rows if r["exp_outcome"] == "dead_letter"]
    cat_rows = [r for r in rows if r["exp_category"] and r["got_outcome"] != "dead_letter"]
    cat_ok = sum(r["exp_category"] == r["got_category"] for r in cat_rows)
    ord_rows = [r for r in rows if r["exp_order"]]
    ord_ok = sum(r["exp_order"] == r["got_order"] for r in ord_rows)
    return {
        "n": n,
        "outcome_accuracy": round(outcome_ok / n, 3),
        "false_auto_draft": f"{len(false_draft)}/{len(esc)}",
        "false_auto_draft_ids": [r["id"] for r in false_draft],
        "over_escalation": f"{len(over_esc)}/{len(pend)}",
        "over_escalation_ids": [r["id"] for r in over_esc],
        "dead_letter_correct": f"{sum(r['got_outcome']=='dead_letter' for r in dl)}/{len(dl)}",
        "category_accuracy": f"{cat_ok}/{len(cat_rows)}",
        "order_extraction": f"{ord_ok}/{len(ord_rows)}",
        "pii_leaks": sum(r["leak"] for r in rows),
        "commitment_violations": sum(r["commit_violation"] for r in rows),
        "ungrounded_drafts": sum(r["ungrounded"] for r in rows),
        "latency_ms_mean": round(statistics.mean(lat), 3),
        "latency_ms_p95": round(sorted(lat)[int(0.95 * (len(lat) - 1))], 3),
    }


def main():
    out = {}
    for name, cases in (("dev", DEV), ("heldout", HELDOUT)):
        rows, lat, _ = run(cases)
        out[name] = metrics(rows, lat)
        out[name]["_rows"] = rows
    summary = {k: {kk: vv for kk, vv in v.items() if kk != "_rows"} for k, v in out.items()}
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    if "--write" in sys.argv:
        (ROOT / "eval" / "results_latest.json").write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
        print("wrote eval/results_latest.json")
    return out


if __name__ == "__main__":
    main()
