# 13 MVP Proposal

**決策：Hybrid。**

```
Collectors(GitHub issues via gh、Opire、Superteam、HN、Reddit、Freelancer 公開頁、PCC 標案[待驗])
 → SQLite(opportunity, evidence, decision, revenue)
 → verify.py（gate + 證據欄位人工補）
 → score.py（12 的 v0）
 → report.md（每日）
 → 人工 approve（CLI）
 → task.md 產生器（給 Codex/Claude）
 → submissions 追蹤 → revenue ledger
```
技術：Python + SQLite + CLI + Markdown/CSV。無 dashboard（先用 report.md）。
**重點**：MVP 的主要價值不是「找 bounty」（04 顯示 bounty 池極薄），而是**管理「Productized DB/Data 服務」的銷售漏斗與證據**（來源可擴到標案、論壇、HN Freelancer 等）。若 7 天內來源產出的「已驗證且可行」機會 < 門檻（見 15），停止。
