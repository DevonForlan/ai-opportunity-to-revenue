# 11 Architecture Options

| 階段 | 現有覆蓋 | 建議 |
|---|---|---|
| Collectors / Normalization / Dedup | radar（12 collectors、Opportunity model、URL fingerprint，VERIFIED 見 02） | **Reuse/Fork** Reddit/HN/Opire/Superteam；剔除 LinkedIn/InfoJobs/Windows launcher |
| Evidence verification | 無（radar 無付款證據驗證；TIP 靠猜測） | **自建**，借 idea-hunt-skill 的 kill-gates / Proof-of-Wallet |
| Scoring | radar 為關鍵字式 | 自建（見 12） |
| Human approval | 無 | 自建（CLI 一個 approve/reject 指令即可） |
| Codex/Claude 任務產生 | Shipwright（重，Claude Code only） | 只參考 workflow；自寫 Markdown task template |
| Submission / Revenue ledger | 無 | 自建（SQLite 一張表） |
| 台灣來源 | 無 | 加 PCC 政府標案 API（openfunltd/pcc.g0v.ronny.tw，是否可用需實測 UNKNOWN） |

## 選項
- A. Fork radar 全盤改：Brazil 耦合約 1/3、單一作者 0 stars → 維護風險。
- B. 從零寫：重複造 collectors。
- **C. Hybrid（選）**：只複製 radar 的 model/collector base/少數 collector（MIT），其餘自建。

不需要：multi-agent、vector DB、K8s、事件匯流排、ML 排序。
