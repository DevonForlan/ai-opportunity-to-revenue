# 05 Freelance 市場取樣 (2026-11-11)

標籤：VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / UNKNOWN。資料表見 `data/freelance_samples.csv`，來源見 `_sources/freelance.md`。

## 1. 結論摘要

- 樣本共 30 筆 (目標上限 30)：VERIFIED 9 筆 (個別 job 頁，其中 Confluent 為 2026-04-30，超過 60 天)；PARTIALLY VERIFIED 21 筆 (19 筆 Freelancer 列表層級 + 2 筆 RemoteOK API 摘要；詳見 CSV `detail_level`)。
- 27 筆 Freelancer.com、2 筆 RemoteOK、1 筆 Confluent forum。平台覆蓋極窄 (見 §2)。
- 欄位大量 UNKNOWN：client 歷史、付款驗證、確切發佈日在多數頁面不可見。
- 重點發現：公開可讀的 Freelancer 專案，預算普遍極低 (多為 USD 4-50/hr 或單案 USD 100-700 avg bid)，bids 數常達 100-270；與 MongoDB/Kafka 專家顧問定位 (USD 90/hr，Confluent 貼文) 差距大。
- 唯一高價值樣本：Deploy Three Claude AI Agents (USD 5,000-10,000，payment verified，但描述僅一行，PARTIALLY 可行性)；Scalability architecture assessment (INR 75,000-150,000)；Confluent Kafka contract USD 90/hr (已 6 個月前)。

## 2. 平台可及性 (本身即為發現)

| 平台 | 結果 | 標籤 |
|---|---|---|
| Upwork 公開 job 頁 | 4 個 URL 皆 HTTP 403，無法讀取欄位；搜尋引擎 snippet 顯示有 Kafka/Data Engineer/MongoDB 職缺 (如 Junior Data Engineer $5-10/hr、Kafka fixed $100)，但未驗證，未納入 CSV | VERIFIED (403) / UNVERIFIED (snippet 內容) |
| Freelancer.com | 公開可讀，無登入牆；少數 "Private project" 需登入 (2 筆見於 api-integration 列表) | VERIFIED |
| RemoteOK | API 可讀，但職缺多為受僱；salary 多為 0 | VERIFIED |
| WeWorkRemotely | 可讀，DevOps 類別 34 筆全為 Full-Time，無 contract | VERIFIED |
| HN Ask HN: Freelancer? (2026-11-02, id 50338744) | thread 存在；comment 層級查詢 0 hits，未取得貼文 | VERIFIED (存在) / UNKNOWN (內容) |
| Contra / Arc / Lemon.io / Toptal / Wellfound / PeoplePerHour / Guru | 未嘗試 (時間限制) | UNKNOWN |
| 台灣平台 (104 外包、Cakeresume、PRO360 等) | 未嘗試 | UNKNOWN |
| Fiverr | 僅取得搜尋 snippet，未開 gig 頁 | UNVERIFIED |

## 3. 樣本品質注意

- Freelancer 頁面的 "Posted 1 minute ago" 與 "Active 57 yrs ago" 並存，疑為 cache/渲染假象；發佈日一律標註為約 2026-11-11 或 UNKNOWN。實際以 "ends in 6 days" 推估為近一週內刊登 (推論，非事實)。
- "Budget" 在列表為 average bid (競標均價)，不等於客戶預算；個別頁才有客戶預算區間。
- 內容經 WebFetch 摘要模型轉述，非原始 HTML，可能有轉述誤差。
- 本地化金額 (INR/EUR) 未換算。
- 多筆高風險或不宜接案之項目 (遊戲 API、政府入口網站自動填表、第三方信用卡開帳號) 已標示或排除。

## 4. 主題分布 (CSV 30 筆)

| 主題 | 約筆數 | 觀察 |
|---|---|---|
| AI agent / Claude / MCP / LLM / RAG | 11 | 數量最多，競爭最激烈 (bids 35-277) |
| Scraping / API integration / Python automation | 6 | 低價 USD 9-228，race-to-bottom |
| Kafka / ETL / data pipeline | 4 | Kafka BigQuery (INR 37,500-75,000)；OCR+ETL (USD 8-15/hr) |
| MongoDB (主技能) | 2 | 皆為 app build，非 MongoDB 專業服務 |
| DevOps / migration / architecture | 5 | Nexus to JFrog migration 僅 INR 1,500-12,500 |
| 其他 | 2 | 評估/紅隊類 |

## 5. Fit 評分意義

fit_score 1-5 為本研究主觀評估：預算合理度、範疇清晰度、Taiwan 可行性、AI 輔助比例、風險綜合。非客觀指標。Taiwan eligible：除明示美國工作授權者 (NO) 外，皆為 LIKELY (未見地區限制)，非已確認。

## 6. 典型預算範圍 (僅列有來源者)

| 範圍 | 來源 | 標籤 |
|---|---|---|
| Kafka/DB 顧問合約 USD 90/hr，6+ 個月 | Confluent forum 2026-04-30 | VERIFIED (單一樣本) |
| Data/OCR LLM pipeline USD 8-15/hr | Freelancer 個別頁 | VERIFIED |
| AI agent 部署 USD 5,000-10,000 | Freelancer 個別頁 | VERIFIED (單一樣本) |
| 架構評估 INR 75,000-150,000 | Freelancer 個別頁 | VERIFIED (單一樣本) |
| Scraper INR 12,500-37,500 | Freelancer 個別頁 | VERIFIED |
| 其他 avg bid 見 CSV | Freelancer 列表 | PARTIALLY VERIFIED |

樣本過小，不可推論為市場中位數。

## 7. Productized Service 證據

| 服務 | 賣家 | 價格 | 交付形式 | 時程 | 標籤 |
|---|---|---|---|---|---|
| Database Health Audit (含 MongoDB 單一 replica set 或 sharded cluster，1-5 servers) | Percona | "starting from $11,400" | PDF 報告 (health scorecard、configuration scorecard、依 impact/effort 排序建議) + live session；review-only | 啟動後 5-7 business days | VERIFIED (頁面無日期，(c) 2026)。頁面對 MongoDB 節點數 1-6 vs 1-5 不一致 |
| DB Health Check (非限 MongoDB) | AVP Consulting | USD 490 one-time (前 3 客戶免費) | PDF (exec summary + technical deep-dive)，Critical/Warning/Advisory 分級，30 分鐘 walkthrough | 2-3 business days | VERIFIED (價格頁)；賣家規模/可信度 UNKNOWN |
| Reliability Setup | AVP Consulting | from USD 3,500 | 評估+HA 設計+分階段實作+runbook | 1-2 週 | VERIFIED |
| DBA On-Demand | AVP Consulting | USD 1,200/mo 或 2,200/mo | 月度 retainer | 約 1 週 onboarding | VERIFIED |
| Kafka Health Check package | Instaclustr | 未公開 | 設定參數審查 + topic 擴展/效能稽核 | 1-2 週 | PARTIALLY VERIFIED (PDF 為 2020 / 2025 版，未開讀，僅搜尋摘要) |
| Kafka architecture review | Nextbrick | 需報價 | 固定範圍專案或月 retainer | 2-4 週 | UNVERIFIED (僅摘要) |
| MongoDB Health Check | Datavail / MongoDB 官方 / Delbridge | 未見價格 | 五階段流程 (Datavail) | UNKNOWN | UNVERIFIED |
| RAG chatbot gig | Fiverr 多位賣家 | 約 USD 50 以下至 USD 400；agency 方案 USD 2,000-3,000 / 3 週 | 部署 chatbot，依文件量報價 | 1 天至 3 週 | UNVERIFIED (價格取自搜尋摘要，未開頁) |
| DB migration assessment 專屬套餐 | -- | -- | -- | -- | UNKNOWN：AVP 明示無獨立 migration 套餐；未找到其他有公開價格者 |
| Data pipeline audit / AI workflow 套餐 | -- | -- | -- | -- | UNKNOWN (未在時間內搜尋；Freelancer 有 n8n workflow 賣家自薦，無價格) |

觀察：MongoDB health check 公開價格橫跨 USD 490 至 11,400+ (約 23 倍)，反映買方分眾 (小型 vs 企業)。固定價 audit 的共同交付形式為 PDF 報告 + walkthrough call，review-only，這與可 AI 輔助的產出形式相符 (推論)。

## 8. 風險與未解問題

1. 樣本偏差：以 Freelancer 為主，結論不代表 Upwork/Toptal/台灣市場。
2. Upwork 登入/反爬限制使最相關的 Kafka/MongoDB 職缺無法驗證。
3. 價格過低的案子 (USD 4-26/hr) 多，不應作為定價參考。
4. 合規：Org policy 禁止放入客戶個資；接案前須確認不處理受 PDPA 規範資料。
5. 未接觸任何客戶、未建立帳號、未投標。

## 9. 建議後續

- 補測 Contra、Arc、Lemon.io、Toptal 公開頁及台灣平台 (UNKNOWN 項目)。
- 手動 (人工登入) 檢視 Upwork 以補 client 歷史與付款驗證欄位。
- 開啟 Fiverr gig 頁與 Instaclustr PDF 驗證價格/範圍。
