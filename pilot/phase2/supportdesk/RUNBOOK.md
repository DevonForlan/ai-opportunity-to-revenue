# Runbook (operator)

| Situation | What to do |
|---|---|
| `run` prints `dead_letter` counts | Malformed rows are stored in `dead_letters` with a reason (never silently dropped). Fix the source feed. |
| Item is `escalated` | No draft exists. Read it via `review`, write the reply yourself in the real helpdesk. Reasons are listed (e.g. `prompt_injection_suspected`, `sensitive_data_present`, `multi_intent`). |
| Item is `pending_approval` with reason `missing_order_id` | The draft asks the customer for the order number — review then approve. |
| Item is `pending_approval` with `sensitive_data_present` | Customer sent card/ID/password. Approve only the safe-handling draft; ask support to delete the original email from the real mailbox. |
| `verify` says audit chain BROKEN | Stop. Someone modified the DB. Preserve `var/` for investigation; do not approve anything. |
| Transient DB errors | The pipeline retries 3x. A failed request can be re-sent safely (idempotent on completed result). |
| Change thresholds/keywords | Edit `config/config.json` / `supportdesk/classifier.py`, bump `config_version`, run tests + eval, and compare with `eval/baseline.json`. Never tune on HELDOUT. |
