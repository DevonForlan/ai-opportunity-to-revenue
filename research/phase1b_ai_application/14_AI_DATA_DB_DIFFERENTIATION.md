# 14 AI x Data/DB 差異化：是否構成「可賣」的市場差異（Phase 1B）

## 方法與限制（先讀）
- 擷取日 2026-11-16。資料集：`14_AI_DB_EVIDENCE.csv`（AI_DEMAND schema，AD001–AD081，81 列、URL 去重、無虛構列）；來源清單：`_sources/ai_db_differentiation.csv`。
- 方法：PCC 政府標案 API（title search）、Freelancer.com 公開 API（active projects）、HN Algolia（Who is hiring 2026-11）、供應端 provider 頁（WebFetch 實讀）、MongoDB 官方頁與 vendor 案例（標示 provider_marketing）、Gartner 新聞稿（經搜尋摘要）。
- 限制（重要）：
  1. PCC 只搜**標題**；標案內文未讀，因此「標題為 AI 知識庫/RAG/客服」≠「使用何種 DB / 向量庫」；DBMS、個人/遠端可否承接皆 UNKNOWN。PCC API 曾遇 429，已降速重試。
  2. Freelancer 為單日 active 快照；多詞查詢為 OR 語意、雜訊高，故只用「單一關鍵字」計數作跨技術比較；job post != paid engagement。
  3. HN 僅取回 245 則留言（Algolia 分頁可能截斷），其中混有求職者貼文；只能作方向性參考。Upwork/Fiverr/Acropolium 頁面 403 或未取得，未視為證據。
  4. Provider list price != 成交價；vendor 案例=provider_marketing，不等於買方需求；Gartner 為預測不是量測。
  5. 本文件全部內容須經人工覆核後才可使用（組織政策）。

## 資料集計數（AD001–AD081）
| 維度 | 計數 |
|---|---|
| evidence_type | purchase 51 · hiring 19 · provider_marketing 10 · pain 1 |
| 來源 | PCC 51 · Freelancer 16 · HN 3 · provider/vendor/analyst 頁 11 |
| evidence_level | A 53 · B 6 · C 22 |
| verification_status | VERIFIED 77 · PARTIALLY VERIFIED 2 · UNVERIFIED 2 |
| product_mapping | rag-knowledge 24 · support-automation 15 · ai-ready-data 13 · internal-assistant 11 · workflow-automation 7 · ai-db-integration 5 · agent-integration 2 · other 2 · sales-backoffice 1 · assessment 1 |

註：`ai-ready-data` 13 列中 10 列是「資料治理」標案（標題未必含 AI），已在 notes 標明；不可視為「AI-ready data」專屬購買。

## 結論先行
**判定（INFERENCE，建立在下列 NEW EVIDENCE 上）：Data/MongoDB/Kafka/DB 技能與 AI 的組合，目前沒有買方端證據顯示它本身是「可賣的差異化」；它不應提高任何候選產品的排名。**
它的合理角色是「交付品質與可信度的加分項」，而不是買方會指名購買的品項。唯一例外的弱訊號：`ai-ready-data` / `assessment` 這類「資料導向的評估」在供應端有明確價格錨點，可在同分時作為 tie-breaker（見下）。

## 1. 買方端證據（NEW EVIDENCE）
### 1.1 AI 知識庫 / RAG / AI 客服：購買證據強，但不指名 DB（A 級，VERIFIED 標題與金額）
- PCC 51 筆 2025-01 起的決標（已排除圖書館資料庫訂閱、GPU 設備、培訓）：決標額 NT$341k–45.3M，**中位數 NT$5.2M**。標題關鍵字命中：知識(庫) 13、客服 12、資料治理 10、助理 7、RAG 5、大型語言模型 5。
- 例：勞動部「人工智慧知識管理與增強智能搜尋生成建置(RAG)案」NT$5.5M；國立臺中教育大學「生成式AI結合RAG之智慧教學助理系統」NT$6.0M（2025）與 NT$4.215M（2026）；嘉義縣財稅局「財稅AI知識庫管理系統」NT$5.2M；金管會「金融監理大數據智能應用平台主題式智慧問答」NT$2.5M；經濟部商業發展署「導入生成式AI客服系統」NT$3.5M／3.3M；大林慈濟「AI非結構化資料整理工具」NT$3.1M。
- **關鍵限制**：這些是公部門、向有能力的廠商（平台/SI）採購，金額多為 NT$ 百萬級；個人/遠端可否承接 UNKNOWN。標題沒有任何一筆揭露使用 MongoDB/pgvector/Elasticsearch。
- 與 BASELINE 一致：Phase 1A 已證實台灣公部門確實購買資料庫健檢/升級（BASELINE）；本輪證明公部門更大量購買「AI 知識庫/客服」（NEW EVIDENCE），但買的是**應用結果**而非 DB 技術。

### 1.2 技術別買方證據的具體計數（NEW EVIDENCE，皆需看限制）
| 技術/主題 | PCC 標題搜尋 | Freelancer active 單詞計數 | 備註 |
|---|---|---|---|
| MongoDB | 1 筆（2022 年訓練課程，非 AI） | 5（無一與 vector/RAG 相關；1 筆為 fresher 開發「AI 求職平台」INR 750–1,250/hr） | **MongoDB+AI 的買方購買/付費證據 = 0** |
| pgvector / Pinecone / LlamaIndex | pgvector 0 | 各 1（皆為同一或同類 RAG 貼文） | 買方偶爾在 spec 寫出 vector DB，但多為「vector store of your choice」 |
| Elasticsearch / Kafka | 各 0 | 各 1（皆非 AI） | Kafka→AI 買方證據 0（只有 vendor 部落格） |
| Text-to-SQL | 0 | 未見 | 僅金管會「智慧問答」一筆近似 |
| RAG / 知識庫 | 5 筆含 RAG；13 筆含知識庫 | RAG 類 3 篇有實質預算 | 見下 |
| n8n / LangChain（泛 AI 自動化） | n/a | n8n 14、LangChain 5 | 見 §3 |

### 1.3 Freelancer 上最接近「AI + DB/資料整合」的貼文（C 級，VERIFIED API）
- AD052（40815067）LLM Q&A agent，從「既有 managed database + cloud bucket」取資料，US$1,500–3,000 fixed，235 bids。**這是樣本中唯一明確寫「現有資料庫」的 AI 貼文**；未指定 DB 引擎。
- AD051（40818160）RAG on Salesforce Cases/email/PDF，GBP 5,000–10,000，167 bids，客戶保留 Salesforce 整合、接受 white-label agency。
- AD053（40818973）RAG support assistant，US$50+/hr，84 bids，agency 轉包。
- 以上三篇預算高於泛自動化貼文，但 n=3，且 bid 數仍 84–235：**有付費意願的訊號，但競爭擁擠**。

### 1.4 HN Who is hiring（2026-11，C 級）
- 245 則留言中提及 AI/LLM 約 141、Postgres 36、MongoDB 6、vector/embedding 4、Kafka 3、Elasticsearch 2、text-to-SQL 0。我逐則檢視的 MongoDB 命中皆為求職者自介（非買方）。雇主貼文多為 full-time 員工職缺（如 Opsfleet、Juro、Alternative Payments），限地區，不是顧問採購。結論：**買方端沒有「AI+MongoDB 顧問」需求訊號**（方向性，樣本有限）。

## 2. 供應端（NEW EVIDENCE，皆 list price / marketing）
| 供應者 | 產品 | 價格 | 標籤 |
|---|---|---|---|
| Made In Tandem（美國，DevMynd 旗下） | Data Readiness Assessment，2–3 週，1 位資深 data engineer | US$40–60k（多落在約 US$50k） | provider_marketing, B, VERIFIED |
| Workwise Solutions | AI Readiness Sprint | US$12,500 固定；抵用 ≥US$25k 後續案（90 日內） | provider_marketing, B, VERIFIED |
| HQSoftware | Data & AI Readiness Audit（固定範圍固定價） | 未公開 | provider_marketing, B, VERIFIED |
| Kensink Labs | pgvector + PostgreSQL，8 週固定價 | 未公開 | provider_marketing, B, VERIFIED |
| Percona | PostgreSQL AI workload 固定範圍支援 | 未見 | C, UNVERIFIED（僅搜尋摘要） |
| Contra/Upwork/Fiverr RAG gigs | 約 20 個套裝 RAG 服務 | Fiverr 入門約 US$50（搜尋摘要） | C, UNVERIFIED |
- 結論：data/AI-ready 評估有清楚價格錨點（US$12.5k–60k），但**賣家多為有品牌的精品公司**；RAG 實作供給極度擁擠且低價化。
- 台灣：本輪未找到台灣獨立顧問公開賣「AI+DB」固定價產品（未做系統性供給搜尋，僅 UNKNOWN，不下「不存在」結論）。

### 2.1 MongoDB 官方方案（A/B 級，provider_marketing）
- MAAP 於 2024-05-01 發表（官方新聞稿，已讀）：提供策略/roadmap、RAG 參考架構、jump-start workshop；夥伴為 AWS、Google、Microsoft、Anthropic、LangChain、LlamaIndex、gravity9、PeerIslands、Pureinsights 等；2024-12 擴增 Capgemini、Confluent、IBM、QuantumBlack、Unstructured（搜尋結果，非直接讀官方頁）。**無定價；頁面未載明個人顧問加入途徑（UNKNOWN）**。MongoDB 本身也賣 GenAI Build consulting（A 級，頁面僅搜尋摘要）。
- Swisscom（官方案例，已讀）：3,500+ 文件、30 家銀行、原型 2024-02-15、約 2024-05 上線、自述 ~6 人天開發；Cisco（CaseStudies.com 標示 MongoDB Case Study）自述省約 US$10M 無方法。**皆為 vendor 行銷**，證明「MongoDB 原生 RAG 存在」，不證明「有人付錢請第三方做」。MongoDB 自己及大型 SI 佔據此利基，對獨立顧問是**競爭而非通路**（INFERENCE）。
- Gartner（2025-02-26）：預測至 2026 年組織將放棄 60% 缺乏 AI-ready data 支撐的 AI 專案（B 級，預測而非量測，經搜尋摘要）→ 支持「資料就緒」是 pain，不證明預算。

## 3. 與泛 AI 自動化的量與強度比較（NEW EVIDENCE + INFERENCE）
- Freelancer 同一快照：泛自動化/bot/n8n 類貼文 8 筆（AD054–AD066）預算多在 US$30–750，bids 119–311；少數例外 US$3–5k（AI Workflow Automation Specialist，119 bids）。AI+DB/RAG 類 3 筆預算較高（£5–10k、US$1.5–3k、US$50+/hr），bids 84–235。
- 量：AI+DB 類貼文 3 筆 vs 泛自動化 ≥8 筆（n 小，**不足以統計推論**）。
- 強度：PCC 公部門採購的主力是 AI 知識庫/RAG/AI 客服（51 筆），泛「workflow automation」未系統抽樣（UNKNOWN，非證據缺乏）。
- INFERENCE：RAG/知識庫/客服「應用層」的付費證據明顯強於「DB 專屬」的證據；AI+DB 組合讓你在 RAG 案中可信度較高（ingestion、資料品質、整合），但買方篩選條件是「能否做出知識庫/客服」。

## 4. 各候選產品是否因 DB 差異化而上調（誠實判定）
| 候選 | 是否上調 | 理由（標籤） |
|---|---|---|
| rag-knowledge | **不上調**（本身已有強購買證據，但非因 DB） | 買方買結果；DB 技能是品質因子（INFERENCE） |
| rag-data-quality / ai-ready-data | **僅 tie-breaker（弱上調）** | 供應端有 US$12.5k–60k 錨點、Gartner pain、台灣有資料治理/非結構化整理採購；但 PCC 資料治理標案為 NT$1.2M–45M 大案（個人承接 UNKNOWN）；定價錨點屬精品公司（INFERENCE） |
| assessment | 不上調 | 與 DB 無關，已有獨立錨點 |
| ai-db-integration（MongoDB/pgvector 專屬） | **不上調；建議降為備援** | MongoDB+AI 買方證據 0；MongoDB 自己與大 SI 供給；Kensink 類精品無價格（NEW EVIDENCE） |
| Kafka/CDC→AI | 不上調 | 買方證據 0，僅 vendor 部落格 |
| text-to-SQL / analytics assistant | 不上調 | PCC/Freelancer 幾乎無，金管會 1 筆近似 |
| agent-integration（LLM + legacy/API） | 不上調 | AD051/AD052/AD057 顯示整合需求，但 bid 擁擠；API/整合技能是通用能力 |
- 與 BASELINE 一致：Phase 1A 已記錄 MongoDB 專屬購買證據 0；本輪把範圍擴大到 AI+DB，結論相同（NEW EVIDENCE 延伸）。

## 5. 什麼證據會改變我的判斷
1. 找到 ≥3 件買方公開貼文/標案明確要求「MongoDB Atlas Vector Search / pgvector / 既有 DB 的資料整備」且附預算或決標價。
2. 讀 PCC 標案內文（RAG/知識庫類）發現規格書明列特定向量庫/資料庫、且個人/小公司/遠端可投標（驗證 C4 類分支）。
3. 取得 MAAP 官方夥伴頁，證實個人/小型顧問可加入並有轉介案源。
4. 暖關係訪談：≥1 位真實買方願為「AI-ready data 評估」付費（書面），且指名要資料工程背景。
5. 供給端出現台灣獨立顧問公開成交價（非 list price）。
6. 反向：若 Pilot 顯示 RAG 案中資料品質/ingestion 工時占比高且客戶願另付，則 ai-ready-data 應升為主要候選。

## 6. 與 Phase 1A 的關係
- BASELINE：CONDITIONAL GO，第一產品為 MongoDB Production Risk Assessment；MongoDB 專屬購買 0。
- NEW EVIDENCE：把 AI 加到 DB 技能上並未產生新的購買證據；AI 需求集中在應用層。
- INFERENCE：若用戶追求「最多買方付費證據」，主線應為 AI 應用（rag-knowledge / support-automation）或「資料導向評估」，DB 專長作為交付品質與信任訊號，而非主訴求。不得因用戶熟悉 MongoDB 而提高其排名。
