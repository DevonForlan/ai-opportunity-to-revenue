"""Sensitivity of the AI-candidate ranking to the assessor's own inputs (SYNTHETIC scenario).
Perturbs volume and automatable_share of EVERY process by independent factors from a fixed grid and
counts how often each AI-fit process ranks first. Exhaustive grid, no randomness."""
import itertools, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from score import load, score, ROOT

base = load(ROOT / "scenario" / "processes.csv")
vol_f = (0.5, 1.0, 1.5)
share_f = (0.7, 1.0, 1.3)
ai_ids = [r["process_id"] for r in base if r["ai_needed_assessment"].lower().startswith("yes")]
wins = {p: 0 for p in ai_ids}; total = 0
# every process gets its own (volume factor, share factor) -> 9^5 combinations
combos = list(itertools.product(itertools.product(vol_f, share_f), repeat=len(base)))
for combo in combos:
    rows = []
    for r, (vf, sf) in zip(base, combo):
        r = dict(r); r["volume_per_month"] = str(float(r["volume_per_month"]) * vf)
        r["automatable_share_estimate"] = str(min(1.0, float(r["automatable_share_estimate"]) * sf)); rows.append(r)
    top_ai = [x for x in score(rows) if x["fit"] == "AI"][0]["process_id"]
    wins[top_ai] += 1; total += 1
print("combinations:", total)
for p in ai_ids: print(p, f"{wins[p]}/{total} = {wins[p]/total:.1%}", next(r['process_name'] for r in base if r['process_id']==p))
