"""SQLite store: idempotent requests, results, mock CRM, dead letters, hash-chained audit log."""
from __future__ import annotations

import hashlib
import json
import sqlite3
import time
from typing import Callable, TypeVar

T = TypeVar("T")

SCHEMA = """
CREATE TABLE IF NOT EXISTS requests (
  idem_key TEXT PRIMARY KEY, message_id TEXT, channel TEXT, sender_hash TEXT,
  redacted_subject TEXT, redacted_body TEXT, received_at TEXT, created_at REAL);
CREATE TABLE IF NOT EXISTS results (
  idem_key TEXT PRIMARY KEY, payload TEXT, status TEXT, updated_at REAL);
CREATE TABLE IF NOT EXISTS crm_tickets (
  ticket_id INTEGER PRIMARY KEY AUTOINCREMENT, idem_key TEXT UNIQUE, category TEXT,
  priority TEXT, order_id TEXT, status TEXT);
CREATE TABLE IF NOT EXISTS dead_letters (
  id INTEGER PRIMARY KEY AUTOINCREMENT, reason TEXT, raw_preview TEXT, created_at REAL);
CREATE TABLE IF NOT EXISTS outbox (
  id INTEGER PRIMARY KEY AUTOINCREMENT, idem_key TEXT UNIQUE, draft TEXT, approved_by TEXT, sent_at REAL);
CREATE TABLE IF NOT EXISTS audit_log (
  seq INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, event TEXT, idem_key TEXT,
  detail TEXT, prev_hash TEXT, hash TEXT);
"""


class TransientStoreError(RuntimeError):
    pass


def with_retry(fn: Callable[[], T], attempts: int = 3, backoff: float = 0.0) -> T:
    last: Exception | None = None
    for i in range(attempts):
        try:
            return fn()
        except TransientStoreError as exc:
            last = exc
            if backoff:
                time.sleep(backoff * (2 ** i))
    assert last is not None
    raise last


def idem_key(channel: str, message_id: str) -> str:
    return hashlib.sha256(f"{channel}\x00{message_id}".encode()).hexdigest()[:24]


def sender_hash(sender: str) -> str:
    return hashlib.sha256(sender.lower().encode()).hexdigest()[:12]


class Store:
    def __init__(self, path: str = ":memory:"):
        self.db = sqlite3.connect(path)
        self.db.executescript(SCHEMA)
        self.fail_next_writes = 0  # test hook: simulate transient failures

    # -- audit -----------------------------------------------------------------
    def audit(self, event: str, key: str | None, detail: dict) -> str:
        row = self.db.execute("SELECT hash FROM audit_log ORDER BY seq DESC LIMIT 1").fetchone()
        prev = row[0] if row else "GENESIS"
        body = json.dumps(detail, sort_keys=True, ensure_ascii=False)
        digest = hashlib.sha256(f"{prev}|{event}|{key}|{body}".encode()).hexdigest()
        self.db.execute(
            "INSERT INTO audit_log(ts,event,idem_key,detail,prev_hash,hash) VALUES (?,?,?,?,?,?)",
            (time.time(), event, key, body, prev, digest),
        )
        self.db.commit()
        return digest

    def verify_audit_chain(self) -> bool:
        prev = "GENESIS"
        for event, key, detail, p, h in self.db.execute(
            "SELECT event,idem_key,detail,prev_hash,hash FROM audit_log ORDER BY seq"
        ):
            if p != prev:
                return False
            if hashlib.sha256(f"{p}|{event}|{key}|{detail}".encode()).hexdigest() != h:
                return False
            prev = h
        return True

    # -- requests / results ---------------------------------------------------
    def _maybe_fail(self) -> None:
        if self.fail_next_writes > 0:
            self.fail_next_writes -= 1
            raise TransientStoreError("simulated transient write failure")

    def has_result(self, key: str) -> bool:
        """Idempotency is decided by a COMPLETED result, not by the raw request row.
        FIX 2026-11-17: keying on the request row lost a ticket when the result write failed."""
        return self.db.execute("SELECT 1 FROM results WHERE idem_key=?", (key,)).fetchone() is not None

    def save_request(self, key, req, redacted_subject, redacted_body) -> None:
        self._maybe_fail()
        self.db.execute(
            "INSERT OR IGNORE INTO requests VALUES (?,?,?,?,?,?,?,?)",
            (key, req.message_id, req.channel, sender_hash(req.sender), redacted_subject,
             redacted_body, req.received_at, time.time()),
        )
        self.db.commit()

    def save_result(self, key: str, result) -> None:
        self._maybe_fail()
        self.db.execute(
            "INSERT OR REPLACE INTO results VALUES (?,?,?,?)",
            (key, json.dumps(result.to_dict(), ensure_ascii=False), result.status, time.time()),
        )
        self.db.commit()

    def get_result(self, key: str) -> dict | None:
        row = self.db.execute("SELECT payload FROM results WHERE idem_key=?", (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def set_status(self, key: str, status: str) -> None:
        res = self.get_result(key)
        if res is None:
            raise KeyError(key)
        res["status"] = status
        self.db.execute("UPDATE results SET payload=?, status=?, updated_at=? WHERE idem_key=?",
                        (json.dumps(res, ensure_ascii=False), status, time.time(), key))
        self.db.commit()

    def pending(self) -> list[dict]:
        rows = self.db.execute("SELECT idem_key,payload FROM results WHERE status IN ('pending_approval','escalated')")
        return [{"idem_key": k, **json.loads(p)} for k, p in rows]

    # -- mock CRM / outbox / dead letters --------------------------------------
    def upsert_ticket(self, key: str, category: str, priority: str, order_id, status: str) -> None:
        self._maybe_fail()
        self.db.execute(
            "INSERT INTO crm_tickets(idem_key,category,priority,order_id,status) VALUES (?,?,?,?,?) "
            "ON CONFLICT(idem_key) DO UPDATE SET status=excluded.status",
            (key, category, priority, order_id, status),
        )
        self.db.commit()

    def add_dead_letter(self, reason: str, raw) -> None:
        preview = json.dumps(raw, ensure_ascii=False, default=str)[:200]
        self.db.execute("INSERT INTO dead_letters(reason,raw_preview,created_at) VALUES (?,?,?)",
                        (reason, preview, time.time()))
        self.db.commit()

    def send(self, key: str, draft: str, approved_by: str) -> bool:
        cur = self.db.execute("INSERT OR IGNORE INTO outbox(idem_key,draft,approved_by,sent_at) VALUES (?,?,?,?)",
                              (key, draft, approved_by, time.time()))
        self.db.commit()
        return cur.rowcount == 1

    def count(self, table: str) -> int:
        assert table in {"requests", "results", "crm_tickets", "dead_letters", "outbox", "audit_log"}
        return self.db.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
