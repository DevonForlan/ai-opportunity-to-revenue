# 09 Cost Model

**限制**：本階段未逐項查證官方價格。以下僅列結構；未引用官方頁面者一律 **UNKNOWN**，不補估算值。需於下一步查官方 pricing 後填入。

| 項目 | Minimal | Practical | Scale |
|---|---|---|---|
| Claude / ChatGPT(Codex) 訂閱 | 已持有（用戶現況 UNKNOWN） | UNKNOWN | UNKNOWN |
| GitHub / Actions | 免費層（用量限制未查）UNKNOWN | UNKNOWN | UNKNOWN |
| 資料庫 | SQLite 本機：$0（結構性事實） | 同左 | Postgres 託管 UNKNOWN |
| 排程 | 本機 Task Scheduler：$0 | GitHub Actions cron UNKNOWN | VPS UNKNOWN |
| LLM API | 用訂閱 CLI，API $0 | UNKNOWN | UNKNOWN |
| Search / Scraping / Proxy / Apify | 不用（只用官方 API、`gh`、RSS） | UNKNOWN | UNKNOWN |
| Domain/Email/Monitoring | 不需要 | UNKNOWN | UNKNOWN |

**結構性結論（非估價）**：Minimal 方案可做到近 $0 增量現金成本（SQLite + `gh` + 本機排程 + 既有訂閱）；主要成本是**人工時間**，不是基礎設施。Scale 方案無證據支持必要性。
