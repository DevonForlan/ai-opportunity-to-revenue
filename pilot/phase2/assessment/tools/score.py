"""Automation-candidate scoring for the SYNTHETIC assessment pilot.

Transparent, no weights hidden: every number comes from scenario/processes.csv. Inputs marked
*_estimate are assessor judgements (INFERENCE), not measurements. No money values are computed
because labour cost is UNKNOWN for the synthetic client.

hours_per_month  = volume * minutes / 60
addressable_h    = hours_per_month * automatable_share_estimate
difficulty       = data_sensitivity + (6 - data_readiness) + integration_complexity     (range 3..15)
value_per_diff   = addressable_h / difficulty
ai_fit           = 'AI' if the process needs language/document understanding else 'DETERMINISTIC'
Rule: a process that does not need AI is routed to a script/rules (cheaper, more reliable) and
is NOT offered as an AI PoC even if it ranks high.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(path: Path):
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def score(rows):
    out = []
    for r in rows:
        vol, mins = float(r["volume_per_month"]), float(r["minutes_per_case"])
        hours = vol * mins / 60
        addr = hours * float(r["automatable_share_estimate"])
        diff = (int(r["data_sensitivity_1to5"]) + (6 - int(r["data_readiness_1to5"]))
                + int(r["integration_complexity_1to5"]))
        fit = "AI" if r["ai_needed_assessment"].lower().startswith("yes") else "DETERMINISTIC"
        out.append({**r, "hours_per_month": round(hours, 1), "addressable_hours": round(addr, 1),
                    "difficulty": diff, "value_per_difficulty": round(addr / diff, 2), "fit": fit})
    out.sort(key=lambda x: x["value_per_difficulty"], reverse=True)
    for i, r in enumerate(out, 1):
        r["rank_all"] = i
    ai_only = [r for r in out if r["fit"] == "AI"]
    for i, r in enumerate(ai_only, 1):
        r["rank_ai"] = i
    return out


def main():
    rows = score(load(ROOT / "scenario" / "processes.csv"))
    (ROOT / "out").mkdir(exist_ok=True)
    (ROOT / "out" / "candidate_register.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{'rank':<5}{'id':<4}{'fit':<14}{'h/mo':>7}{'addr_h':>8}{'diff':>6}{'val/diff':>9}  name")
    for r in rows:
        print(f"{r['rank_all']:<5}{r['process_id']:<4}{r['fit']:<14}{r['hours_per_month']:>7}{r['addressable_hours']:>8}"
              f"{r['difficulty']:>6}{r['value_per_difficulty']:>9}  {r['process_name']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
