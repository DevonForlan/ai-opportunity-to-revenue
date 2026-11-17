"""CLI:  python -m supportdesk.cli run FILE.jsonl | review | approve KEY WHO | reject KEY WHO WHY | verify"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .pipeline import ROOT, Pipeline
from .store import Store

DB = ROOT / "var" / "supportdesk.sqlite3"


def _pipeline() -> Pipeline:
    DB.parent.mkdir(exist_ok=True)
    return Pipeline(store=Store(str(DB)))


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="supportdesk")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run"); r.add_argument("file")
    sub.add_parser("review")
    a = sub.add_parser("approve"); a.add_argument("key"); a.add_argument("approver")
    j = sub.add_parser("reject"); j.add_argument("key"); j.add_argument("approver"); j.add_argument("reason")
    sub.add_parser("verify")
    args = p.parse_args(argv)
    pipe = _pipeline()

    if args.cmd == "run":
        counts: dict[str, int] = {}
        for line in Path(args.file).read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            try:
                raw = json.loads(line)
            except json.JSONDecodeError:
                raw = line
            out = pipe.process(raw)
            counts[out["outcome"]] = counts.get(out["outcome"], 0) + 1
        print(json.dumps(counts, ensure_ascii=False))
    elif args.cmd == "review":
        for item in pipe.store.pending():
            print(json.dumps({k: item[k] for k in ("idem_key", "category", "priority", "status",
                                                     "escalation_reasons", "draft_reply")}, ensure_ascii=False))
    elif args.cmd == "approve":
        print(pipe.approve(args.key, args.approver))
    elif args.cmd == "reject":
        pipe.reject(args.key, args.approver, args.reason); print("rejected")
    elif args.cmd == "verify":
        ok = pipe.store.verify_audit_chain()
        print("audit chain OK" if ok else "audit chain BROKEN")
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
