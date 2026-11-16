# 05 Freelance / Contract 市場深潛 (Phase 1A，2026-11-16)

資料表：`06_FREELANCE_SAMPLES.csv`（86 列，ID F001-F086）。來源：`_sources/freelance_deep.csv`。
標籤：VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / UNKNOWN。證據等級 A=平台官方/一手資料，B=高可信二手（經摘要器讀取的頁面），C=搜尋摘要/社群/弱證據。結論標註 BASELINE / NEW EVIDENCE / INFERENCE。

## 0. 方法與限制 (method & limitations)

**方法**
- Freelancer.com：使用其公開、未登入 REST API（`/api/projects/0.1/projects/active/`，依 skill id 與關鍵字列舉），直接讀 JSON。`posted_date` 取自 API `time_submitted`（比 Phase 0 的網頁 "Posted 1 minute ago" 可靠，NEW EVIDENCE，修正 BASELINE 的日期 UNKNOWN）。
- PeoplePerHour、PRO360、Arc、Remotive、Twine、Confluent forum：WebFetch 抓公開頁（經小模型摘要，可能有轉述誤差）。HN：Algolia API 直接讀原文。
- Upwork：公開 job 頁 HTTP 403（BASELINE 已知，仍成立）。23 列僅來自搜尋引擎 snippet，一律 UNVERIFIED / C。
- 每列皆為「徵才/外包貼文」(evidence_type = hiring)。依規則：job post != paid engagement；沒有任何 purchase 證據；Lemon.io 一列為人才市場廣告 (接近 provider_marketing)。

**重大限制**
1. Freelancer API 只回傳「進行中」專案，實際時間窗約 7 天 (2026-11-09 至 11-16)；已結案專案需 id 查詢，無法回溯 60-90 天。因此 Freelancer 33 列無法代表 90 天趨勢，只是「一週快照」。
2. Freelancer 預算是平台預設級距（如 USD 250-750、INR 12,500-37,500），不是客戶確切預算；hourly 專案顯示的是時薪帶。客戶歷史在公開 API 隱藏 (UNKNOWN)。
3. 無法取得：Reddit r/forhire、r/slavelabour（HTTP 403，未繞過；第三方鏡像 429）、Malt (403)、CakeResume (403)、104 外包網 (網域無法解析)、Contra (JS/登入牆)、Guru/Toptal/Wellfound/Braintrust/Codeable（只有供給端行銷頁，無職缺清單）、Fiverr buyer requests（不可用，依任務指示不列入）。這些皆為 UNKNOWN，不是「沒有需求」。
4. 搜尋 snippet 會過期：嘗試開啟 4 個 Dice/Insight Global/Zipdev snippet 連結，3 個回 404/410（NEW EVIDENCE，說明 snippet 會高估目前開放的需求）。
5. 各幣別不換算（無官方匯率引用）。所有分布僅列出現的原始數字。
6. 標註 "OUTSIDE window" 的列（>90 天）：Confluent (2026-04-30)、Insight Global (2026-04-01)、Zipdev (2026-06-12)、PPH 與 Freelancer 舊 MongoDB DBA 案 (數年前)。保留作為價格/範疇參考，不計入近期需求。
7. 去重：Atlas M20 優化貼文在 Upwork 有兩個 job id（同標題，疑為重貼），只計一列；3 列 Arc 與 3 列 PRO360 各共用一個頁面 URL（同一列表頁上的不同工作/案號），非重複。

## 1. 計數 (n = 86)

| 平台 | 列數 | 驗證層級 |
|---|---:|---|
| Freelancer.com (API) | 33 | VERIFIED / A |
| Freelancer 區域站舊案 | 1 | PARTIALLY / B |
| Upwork (snippet) | 23 | UNVERIFIED / C |
| PeoplePerHour | 10 | 7 PARTIALLY / B，3 UNVERIFIED / C |
| Dice / Insight Global / Zipdev (snippet) | 8 | UNVERIFIED / C |
| PRO360 (台灣) | 4 | PARTIALLY / B |
| Arc | 3 | PARTIALLY / B |
| Confluent forum | 1 | VERIFIED / A |
| HN Who is hiring | 2 | VERIFIED / A |
| Remotive (Lemon.io) | 1 | PARTIALLY / B |
| **合計** | **86** | **VERIFIED 36；PARTIALLY 16；UNVERIFIED 34** |

evidence_type：hiring 86 / pain 0 / purchase 0 / provider_marketing 0（Lemon.io 一列邊界案例，歸 hiring）。

近 90 天內有可見日期的列：Freelancer 33（皆為 11-09 至 11-16）、PPH 6、PRO360 3（另 1 列無日期）、Remotive 1、HN 2。Upwork 23 列與 Arc 3 列無確切日期 (UNKNOWN)。

**可見性結論 (NEW EVIDENCE)**：Freelancer 上「MongoDB」技能標籤的進行中專案在擷取時只有 4 件（全是 app 建置或網站搬遷，沒有 DBA/健檢類），「Apache Kafka」標籤 1 件（GCP Kafka BigQuery）。PPH `databases` 類別前 20 件無 MongoDB 件。HN Who is hiring 11 月 245 則留言中，符合 mongo/kafka/dba/data engineer 且含 contract/freelance 字樣者僅 1 則 (Juro，AI Engineer 正職，contract 字樣來自公司業務)，無個人外包需求。

## 2. 預算 / 時薪分布 (僅限有明確數字的列；幣別分開；不換算)

### 2.1 Freelancer.com 固定價專案 (n = 26，VERIFIED，為平台級距，非客戶確切預算)

| 幣別 | 級距 : 件數 |
|---|---|
| USD (n=12) | 10-30 : 2；30-250 : 2；250-750 : 3；1,500-3,000 : 3；3,000-5,000 : 1；5,000-10,000 : 1 |
| INR (n=10) | 600-1,500 : 2；12,500-37,500 : 3；37,500-75,000 : 3；75,000-150,000 : 1；5,000,000 起 : 1 (ORBIT SaaS，願景型) |
| AUD (n=1) | 250-750 : 1 |
| GBP (n=1) | 10-20 : 1 |
| SGD (n=1) | 750-1,500 : 1 (Oracle RAC 7 天診斷) |
| CAD (n=1) | 750-1,500 : 1 |

### 2.2 Freelancer.com 時薪帶 (n = 7，VERIFIED，平台時薪帶)

INR/hr (n=4)：100-400、400-750、750-1,250、850-1,200。USD/hr (n=2)：8-15、15-25。CAD/hr (n=1)：25-50。

### 2.3 其他平台已陳述的時薪 (未換算，各自標註層級)

| 來源 | 數字 | 層級 |
|---|---|---|
| Confluent forum (Kafka + MongoDB sync，40h/週，6 個月+) | USD 90/hr (n=1) | VERIFIED，但 2026-04-30 超過 90 天 |
| HN AssumeAI (AI 工程，僅 UK remote) | GBP 30/hr 與 GBP 50/hr | VERIFIED，區域限制 |
| PPH Cloud migration consultant / Azure Data Factory | $33/hr、$99/hr (頁面顯示幣別，viewer 本地化，是否為 USD UNKNOWN) | PARTIALLY |
| Upwork Firebase DB engineer (限 UAE) | USD 15-35/hr | UNVERIFIED (snippet) |
| Dice/Insight Global (W2 代理商) | USD 30-40、45-50、60-75、57-75.5 /hr | UNVERIFIED (snippet)；W2 與經紀商報價，不是自由工作者成交價 |

### 2.4 固定價 MongoDB 專屬樣本 (全為 UNVERIFIED 或過期)

PPH Onprem MongoDB indexing：$70 固定、Entry、已授標 (數年前，PARTIALLY)。Upwork Atlas M20 優化：snippet 顯示 USD 100 固定，但另一 snippet 稱約 100 小時工時，二者矛盾，預算疑為佔位值 (UNVERIFIED)。Upwork Kafka developer：USD 100 固定、Expert 級、20-50 proposals (UNVERIFIED)。

### 2.5 競標數 (Freelancer，n = 33，API，擷取時)

中位數 105，範圍 5-365。結論 (INFERENCE)：公開可見的個人接案市場競爭極為擁擠；唯一低競標列 (NiFi 5 bids、Snowflake 28 bids) 皆為低時薪帶。

### 2.6 供給端價格宣稱 (provider_marketing / C，不可當成交價)

Lemon.io MongoDB 頁：依資歷 GBP 35-55 / 60-90 / 95-140 每小時；另有 USD 55/hr 起、USD 57/hr 平均的計算器宣稱，且自我矛盾（"No juniors" vs 列出 junior）。搜尋 snippet 引用 ZipRecruiter：Kafka 平均時薪 USD 56.94 (2026-05-31)、remote database contract USD 53.12 (2026-06-05)，未開頁驗證 (UNVERIFIED)。

與 BASELINE 價格對照：BASELINE 的 Percona MongoDB health audit 起價 USD 11,400、AVP 單次 USD 490；本次 Freelancer/PPH 公開需求端中，沒有任何已驗證的 MongoDB 專屬固定價案接近 USD 490 以上 (最高的資料類：Freelancer USD 1,500-3,000 級距，皆為應用層審計或整合案，非 MongoDB 健檢)。INFERENCE：公開自由接案平台的需求端價格遠低於已公開的專業 audit 價格，買方分眾不同 (BASELINE 已指出)。

## 3. 可映射到候選產品的比例 (productized_mapping)

mapping 是本研究對「此工作若產品化，最接近哪個候選產品」的 INFERENCE，非客戶說的話。每列只取單一主映射。

| 映射 | 全部 86 列 | 占比 | 排除 UNVERIFIED 後 (n=52) | 占比 |
|---|---:|---:|---:|---:|
| none | 30 | 34.9% | 22 | 42.3% |
| pipeline-reliability | 15 | 17.4% | 8 | 15.4% |
| ai-automation | 14 | 16.3% | 13 | 25.0% |
| performance-index | 8 | 9.3% | 3 | 5.8% |
| health-check | 8 | 9.3% | 1 | 1.9% |
| kafka-mongo-review | 7 | 8.1% | 2 | 3.8% |
| upgrade-readiness | 2 | 2.3% | 1 | 1.9% |
| backup-restore | 2 | 2.3% | 2 | 3.8% |
| replication-oplog | 0 | 0% | 0 | 0% |

觀察：
- **replication-oplog 為 0 件**；唯一提及 oplog/replica set/WiredTiger 的是 Upwork Atlas M20 優化貼文 (UNVERIFIED)，我將其映射為 performance-index。
- 較高 MongoDB/Kafka 技能重疊 ("High" 與 "Medium-High") 共 19 列，其中僅 2 列為近期 VERIFIED (Freelancer NestJS MongoDB 效能審計、GCP Kafka BigQuery)，另 1 列 VERIFIED 但已過期 (Confluent)。
- 已驗證列中最大宗映射是 ai-automation (13)，但這些多為低價、高競標 (57-193 bids) 的 agent/n8n 件；其中 USD 3,000-5,000 的 AI Workflow Automation Specialist (F018) 是唯一含「顧問 + 建置」形態者。
- 「健檢/審計/檢視」形狀的買方文字確實存在 (Oracle RAC 7 天固定價診斷 SGD 750-1,500 級距；Upwork "Database Architecture & Code Review"；Freelancer "Senior Full-Stack App Reliability Review" 356 bids)，但引擎不是 MongoDB。INFERENCE：買方願意以固定範疇買「診斷並證明結果」，MongoDB 專屬需求在公開平台上稀薄。
- backup-restore：唯一接近的是 PostgreSQL 的「5 階段備份 + 隔離還原測試 runbook」 (INR 600-1,500 級距，極低價) — 範疇形狀吻合但預算與引擎不吻合。
- 區域/語言封鎖常見：美國工作授權 (HN Virtasant、Oracle DBA US-only、多數 W2 代理商)、UAE 駐地 (Upwork Firebase)、Abu Dhabi 時區重疊 (Arc)、西語/葡語/印尼語要求 (Freelancer)、UK remote (AssumeAI)。Arc 公開區域為 EMEA/LATAM/NA，未列亞洲。Lemon.io 明列 APAC。台灣可及性：多數 LIKELY 但需逐案確認 (INFERENCE)。

## 4. 台灣平台 (NEW EVIDENCE，BASELINE 為 UNKNOWN)

- PRO360 `Programmer 工作` 第 1 頁（共 22 件，只讀 10 件）：案件為桌面 app、後台管理系統、APP、AI 軟體，預算帶多為「10k-50k」「50k 以下」「100k-300k」NTD（頁面未印幣別符號，推定為 NTD）；無 MongoDB/資料庫效能/資料管線案件。唯一資料管線 + LLM 自動化案為 PRO360 案號 4573804（10k-50k，AI automation/back-end data engineer）。
- PRO360 `資料庫` 與 `MIS 工程師` 類別第 1 頁：全是程式家教、Office/Access 課程與個人儲存裝置資料救援，無 B2B DBA 需求。
- 104 外包網（網域無法解析）、Tasker（抓取失敗，snippet 僅見爬蟲案以 MongoDB/PostgreSQL 為技能項、案號推定為 2025 年）、CakeResume（403）、1111：UNKNOWN。104.com.tw 搜尋結果是正職，非外包。
- INFERENCE：台灣公開接案平台可見需求為 SMB/個人客戶，預算量級與 B2B 專業 audit 差距大；不代表企業端沒有，只代表公開頁看不到。

## 5. 主要發現摘要

1. NEW EVIDENCE：Freelancer 一週快照內，MongoDB 標籤進行中專案僅 4 件、Kafka 1 件，皆非健檢/升級/複寫/備份類 — 公開自由接案平台對「MongoDB 專屬服務」的可見需求極薄。
2. NEW EVIDENCE：MongoDB 專屬且範疇清楚的需求只出現在 Upwork snippet (Atlas M20 慢查詢優化、索引優化) 與數年前的 PPH 案，價格為 USD 70-100 固定價量級 (均為 UNVERIFIED 或過期)。
3. INFERENCE：買方確實會發固定價「診斷 + 證明結果」(Oracle RAC 7 天) 與「架構/程式碼審查」貼文，範疇形狀與可產品化的 review 相符，但引擎、價格不同；不能直接外推成 MongoDB 健檢的付費意願。
4. NEW EVIDENCE：Kafka 需求出現於 Upwork (DevOps Kafka，client 歷史顯示約 USD 114K spent，UNVERIFIED) 與 Confluent forum (USD 90/hr，已過期)；多為長期人力補充，不是固定範疇 review。
5. NEW EVIDENCE：代理商/W2 合約 (Dice、Insight Global) 的 MongoDB DBA 時薪 USD 30-75 (UNVERIFIED snippet) 為員工式人力派遣，不是個人可接的產品化服務，且 4 個連結中 3 個已失效。
6. 限制：無法驗證 Upwork、Reddit、Malt、104、Cake、Tasker 的實際需求；以上不可推論為整體自由接案市場結論。

## 6. 與 BASELINE 的差異

- BASELINE (30 列) 日期多為 UNKNOWN；本次 Freelancer 日期取自 API，實際範圍 2026-11-09 至 11-16 (7 天窗口)，較 BASELINE 的「約 11-11」更精確。
- BASELINE 重新驗證並保留：GCP Kafka BigQuery、OCR/LLM pipeline (本次對應不同 project id)、Claude 三 agent、Travel CRM、Confluent forum。未直接複製，皆用 API 或直接頁面重讀。
- BASELINE「Taiwan 平台未嘗試」已補：PRO360 已測，其餘仍 UNKNOWN。
- BASELINE「Upwork 403」仍成立；本次以 snippet 補 23 列 UNVERIFIED。

## 7. 建議後續 (需人工，因規則禁止代為登入)

- 人工登入 Upwork 搜尋 "MongoDB"、"Atlas"、"replica set"、"Kafka Connect" 並記錄 posted time、proposal 範圍、client 歷史、付款驗證，用以確認 snippet 列。
- 人工登入 Reddit r/forhire、Malt、104 外包、Tasker 補 UNKNOWN。
- 持續每週快照 Freelancer API (只含進行中專案) 以累積 60-90 天時間序列。
