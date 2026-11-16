# AI Demand Evidence (Pain + 明確付費求助) — Phase 1B

## 方法與限制
- 方法: 以公開 Discourse JSON API (n8n / OpenAI / Make / LangChain 論壇)、n8n Jobs 分類、HN Algolia API 取得 2025-2026 貼文，先以關鍵字篩選，再人工挑選與「AI 自動化要解決的商業問題」相關者。capture_date 2026-11-16。
- 驗證: 12 筆 n8n Jobs 貼文為讀完第一則貼文全文 (VERIFIED)；其餘 143 筆僅讀到 API 回傳的標題與搜尋摘要，未讀完整串 (PARTIALLY VERIFIED)。
- 分類 (ai_use_case / outcome / product_mapping) 為依標題關鍵字的啟發式分類，未逐篇人工複核，可能有誤；需人工審閱。product_mapping 與 notes 的 category= 相同。
- 限制: (1) 論壇抱怨不等於付費意願 (BRIEF 規則)；多數貼文發文者身分 (企業買家 vs 開發者/愛好者) 為 UNKNOWN，故 buyer_type 未捏造。(2) 論壇以 n8n/Make 使用者為主，有選擇偏誤 (偏低預算、低代碼用戶)。(3) 預算僅 5 筆有數字，且為徵人預算不等於成交價。(4) Zapier 社群 404、Dify 連線失敗、Reddit / StackExchange / GitHub issues / Indie Hackers 本輪未嘗試 (網路中斷與時間)，為覆蓋缺口；LangChain 與 HN 偏開發者語氣，買家訊號弱。(5) 排序依瀏覽/回覆數，熱門度不等於商業價值。

## 計數
總列數 155（目標 >=120 達成）。
### 依來源
| source | rows |
|---|---|
| n8n community | 76 |
| Make community | 31 |
| Hacker News | 21 |
| n8n community (Jobs category) | 12 |
| OpenAI developer community | 10 |
| LangChain forum | 5 |
### 依 evidence_type
| type | rows |
|---|---|
| pain | 143 |
| hiring | 12 |
### 依 verification_status
| status | rows |
|---|---|
| PARTIALLY VERIFIED | 143 |
| VERIFIED | 12 |

明確付費求助 (notes 含 'explicit paid-help request'): 36 筆 (含 Jobs 12 筆；論壇貼文者依標題判斷，故可能漏計/誤計)。

## Outcome-category 頻率表 (由本資料列計算)
| category (product_mapping) | rows | 其中 paid-help | 佔比 |
|---|---|---|---|
| doc-automation | 27 | 3 | 17% |
| eval-guardrail | 23 | 1 | 15% |
| sales-backoffice | 20 | 9 | 13% |
| workflow-automation | 20 | 14 | 13% |
| support-automation | 20 | 4 | 13% |
| agent-integration | 19 | 2 | 12% |
| rag-knowledge | 13 | 0 | 8% |
| ai-api-integration | 11 | 2 | 7% |
| ai-db-integration | 2 | 1 | 1% |

## 觀察 (INFERENCE，僅限本樣本)
- doc-automation (發票/PDF 擷取)、eval-guardrail (agent 監控/可靠性)、sales-backoffice、workflow-automation、support-automation 為樣本中最常見的痛點；樣本非隨機，不代表市場佔比。
- Jobs 分類中可見的實際預算極少: 一則「每個 workflow $300–$900 固定價、每月 2–4 個」、一則 $35/hr、一則全職 $2,000–$3,000/月 (僱傭非專案)。皆為 C 級、徵人預算，非成交價。
- 買家多半描述「流程結果」(WhatsApp 客服 agent、lead 管理 + CRM 同步、行銷歸因管線)，且常要求 error handling / human handoff，暗示 reliability 與 guardrail 是賣點，但仍屬單一論壇的 UNVERIFIED 推論。
- ai-db-integration 僅 2 筆，本樣本未顯示資料庫相關需求特別突出 (避免能力偏誤)。

資料檔: 02_AI_DEMAND_DATASET_pain.csv；來源: _sources/ai_demand_pain.csv。
