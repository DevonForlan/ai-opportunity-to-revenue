# 05 AI 自由接案市場 part 1（Freelancer.com API + PeoplePerHour）

## 0. 方法與限制（先讀）

- 擷取日 2026-11-16。資料列在 `06_AI_FREELANCE_SAMPLES_part1.csv`（71 列，id AF001-AF071），來源清單在 `_sources/ai_freelance_part1.csv`。
- **Freelancer.com（45 列，VERIFIED / A）**：公開未登入 REST API `/api/projects/0.1/projects/active/`，約 42 組關鍵字（AI automation、OpenAI API、Claude API、LLM integration、RAG、chatbot、AI agent、n8n、Make.com、Zapier、workflow automation、document processing AI、CRM/email automation、knowledge base、LangChain、vector database、MCP 等），去重後人工篩出與 AI 應用/自動化服務相關者；約 200 件原始結果中，大部分被判為不相關（影片、設計、純網站、純銷售）而排除。`time_submitted` 取自 API，範圍 2026-11-13 至 11-16 的一週內。BASELINE（Phase 1A 05 文件）的 Freelancer API 方法在此重用。
- **PeoplePerHour（26 列，PARTIALLY VERIFIED / B）**：WebFetch 抓三個公開分類頁（AI、AI chatbot development、technology-programming），內容經小模型摘要，可能有轉述誤差。發佈日只有相對時間（"38 minutes ago"）。其中 13 列是 1 至 7 個月前的 "Past Projects"，只作價格與範疇參考。PPH 顯示 `$`，可能是依觀看者換算的幣別，基準幣別 UNKNOWN；本文把它標成 "USD (as displayed)"，不與其他幣別合併。
- **未取得（不是「沒有需求」）**：Guru 403；Reddit r/forhire 403（未繞過）；WeWorkRemotely 搜尋頁 403，RSS 只有全職職缺；Twine 列表被模型回傳為設計/演員/LinkedIn 轉貼職缺，沒有 AI 自動化案；Remotive API 的 search 參數似乎被忽略（每次同樣 16 筆，無合適 contract 案）；RemoteOK 全是受薪職缺（薪資多為空）；GitHub bounty 搜尋結果以疑似機器人/bounty farm 倉庫為主（標籤如 "Bot-Score"、"Stellar Wave"），不可信，未列入。Upwork 仍 403（BASELINE）。因此本檔實質只有兩個平台。
- 數字規則：只用有明示數字的列計算；幣別不換算；Freelancer 預算是平台**預設級距**，不是客戶精確預算，也不是成交價；競標數是擷取當下的快照，不是最終數。客戶國別與歷史在 Freelancer 公開 API 隱藏、PPH 頁面未顯示，一律 UNKNOWN。所有列的 evidence_type 都是 hiring（職缺貼文），沒有任何 purchase（沒有公開授標或付款）。
- 其他限制：一週快照，不代表 90 天趨勢；Freelancer 與 PPH 的客戶偏小額、低價；有少數貼文看起來是接案者自我推銷（AF 的 n8n 兩列已註記），需求訊號弱；部分貼文含個資/敏感領域（法律協助 WhatsApp、CV 解析、兒童之家），依組織政策只記公開商業資訊。

## 1. 計數

| 維度 | 計數 |
|---|---|
| 平台 | Freelancer.com 45；PeoplePerHour 26 |
| verification_status / evidence_level | VERIFIED / A 45；PARTIALLY VERIFIED / B 26 |
| evidence_type（皆為職缺貼文） | hiring 71；purchase 0 |
| fixed / hourly | Freelancer：固定價 33、時薪 12；PPH：固定價 23（頁面未標示，依篩選器推定）、時薪 3 |
| integration_complexity（我的判讀，INFERENCE） | low 17；medium 36；high 18 |

## 2. 預算分布（只計有數字的列，幣別分開）

### 2.1 Freelancer.com 固定價級距（n = 33；這是預設級距，不是精確預算）

| 幣別 | n | 級距（件數） |
|---|---|---|
| USD | 16 | 30-250 (3)；250-750 (10)；300-800 (1)；1,500-3,000 (1)；3,000-5,000 (1) |
| INR | 10 | 600-1,500 (2)；1,000-5,000 (1)；1,500-12,500 (1)；12,500-37,500 (3)；37,500-75,000 (1)；150,000-250,000 (1)；5,000,000+ (1) |
| AUD | 2 | 250-750 (1)；10,000-20,000 (1) |
| EUR | 2 | 30-250 (1)；750-1,500 (1) |
| CAD | 2 | 100-450 (1)；750-1,500 (1) |
| GBP | 1 | 5,000-10,000 (1) |

USD 固定價：16 件中有 14 件的級距上限在 USD 800 以下（30-250、250-750、300-800），佔 88%，中位數級距是 USD 250-750。大型級距（USD 3,000-5,000、AUD 10,000-20,000、GBP 5,000-10,000、INR 5,000,000+）都是「founding engineer」或整套 SaaS 建置，不是固定範疇的小型自動化服務。

### 2.2 Freelancer.com 時薪帶（n = 12）

USD 15-25/hr 4 件，USD 50+/hr 1 件（RAG 客服助理，senior）；INR 750-1,250/hr 2 件、750-1,500/hr 1 件、850-1,200/hr 1 件、200-300/hr 1 件；EUR 10-15/hr 1 件、12-18/hr 1 件。時薪專案的「每週 40 小時」承諾是平台預設值，不代表真實工時。

### 2.3 PeoplePerHour（USD as displayed）

- 固定價 n = 23：最小 93、中位數 198、最大 19,800（另有 2,600、1,000、926、660 等）；n=23 中 15 件在 USD 250 以下（65%）。19,800 是 CV 文件智能的分階段案，是離群值。
- 時薪 n = 3：19、20、28 /hr。
- 注意：PPH 預算常是「參考報價」，頁面不一定標示固定或時薪；一則貼文（AF 音樂科技 AI 匹配）標示 $660 但文字寫每月上限 £500，幣別基準不確定。

### 2.4 預算級距 vs 實際價格（caveat）

Freelancer 級距是發案時選的預設檔，不是出價或成交價；`bid_avg`（API 提供，已記入競標欄位）才較接近市場出價，例如 AF 的 "AI Email Support Assistant" 級距 USD 250-750、平均出價約 USD 431；"LLM-Based Customer Q&A Agent" 級距 USD 1,500-3,000。仍不是成交價。PPH 的 $93-$250 檔位與 AI 客製化工作的工時不對等，INFERENCE：這些買方在找低價或試水溫，不是企業採購。與 BASELINE（Phase 1A）的結論一致：公開接案平台價格遠低於專業固定範疇服務價。

## 3. 競爭（出價數，擷取當下快照）

| 平台 | n | 中位數 | 最小-最大 | 平均 |
|---|---|---|---|---|
| Freelancer.com | 45 | 125 bids | 9-315 | 141.7 |
| PeoplePerHour | 26 | 38 proposals | 8-80 | 39.7 |

- Freelancer 最高競爭：Claude Internal Task Automation 310、AI Bots for Business Automation 286、Founding Engineer（AI community）301、n8n Lead Email Automation 260、AI Email Support Assistant 255。小額、描述通用的 n8n/automation 案出價最擠；「RAG 客服助理（USD 50+/hr）」為 84，「RAG Development Project（GBP 5,000-10,000）」為 167。
- 不同平台的出價數不能直接相比（Freelancer 的免費出價與機器人式出價較多）。出價多寡不等於需求強，只表示進入門檻低、同質競爭多。

## 4. 依 product_mapping 與 use case 的分布（n = 71，我的人工分類，INFERENCE）

| product_mapping | 件數 | 占比 | 出價數中位數（兩平台合併） |
|---|---|---|---|
| other（SaaS 建置、訓練、founding engineer、交易/簽證工具等） | 13 | 18% | 53 |
| workflow-automation | 12 | 17% | 94.5 |
| support-automation | 11 | 15% | 50 |
| sales-backoffice | 8 | 11% | 141.5 |
| agent-integration | 6 | 8% | 100 |
| rag-knowledge | 6 | 8% | 82 |
| ai-api-integration | 4 | 6% | 76 |
| doc-automation | 3 | 4% | 58 |
| internal-assistant | 2 | 3% | 257 |
| ops-copilot | 2 | 3% | 83.5 |
| eval-guardrail | 2 | 3% | 27 |
| ai-ready-data | 1 | 1% | 57 |
| assessment | 1 | 1% | 36 |
| rag-data-quality / ai-db-integration / none | 0 | 0% | n/a |

觀察：
1. NEW EVIDENCE：此快照中最常見的需求形狀是「把 n8n/Make/WhatsApp/Gmail/CRM 串起來並加一個 LLM 步驟」（workflow-automation + sales-backoffice + support-automation 合計 31 件，44%）。其中 WhatsApp 作為通道出現頻率很高（多件，未精確計數），區域偏印度、非洲、東南亞、歐洲小型企業。
2. NEW EVIDENCE：RAG/知識庫助理有 6 件，其中 3 件較大（USD 50+/hr、GBP 5,000-10,000、USD 1,500-3,000），是此快照裡預算最高的 AI 服務類型之一，但樣本很少。
3. NEW EVIDENCE：只有 1 件接近 assessment（PPH "AI consultancy and Training"，USD 2.6K 顯示，36 proposals），eval-guardrail 2 件（chatbot 診斷修復 USD 145、AI 匹配精度改善 USD 660）。代表「評估/診斷」在小額平台可見度低，但這是平台特性，不能推論為整體市場沒有此需求。
4. NEW EVIDENCE：有 1 件是「私有本機 LLM（Ollama）業務助理」（INR 37,500-75,000、204 bids），顯示資料不外送的需求存在，但單件不足以構成趨勢。
5. 重複/長期：recurring 或 ongoing 約 15-18 件（約 20-25%，分類欄位文字不一致，未精確計數），其他皆 one-off（INFERENCE 自貼文用語，如 "long-term"、"ongoing"、"fractional advisory"）。

## 5. 區域與遠端

- 公開欄位中，Freelancer 客戶國別隱藏；僅能從貼文文字推得：美國限定（AF 小型 chatbot MVP、AI Agent Architect 矽谷）、印度（含現場 Azure 訓練，非遠端）、印尼語、法語、義大利語、UK/EU 時區（PPH 兒童之家案）、英國限定（ManyChat）。其餘 UNKNOWN。
- 台灣可及性：大多數案件寫遠端且不限地區（INFERENCE，需逐案確認），但有數件限制地區或時區。

## 6. 對 Phase 1B 的意義（INFERENCE，非結論）

- 這兩個平台反映的是「低價、同質、高競爭」的小額買方；AI workflow/chatbot 類需求量大，但單價低（USD 中位數級距 250-750；PPH 中位數 USD 198），與 BASELINE 對 Phase 1A MongoDB 的觀察一致：平台價不代表專業固定範疇服務的可成交價。
- 較有價值的信號是需求「形狀」而不是價格：Gmail/CRM/WhatsApp 串接、RAG 客服助理、文件擷取/報表生成、已有 bot 的修復與延伸。需要其他資料（part 2、買方端 RFP、供給端公開價）才能判斷哪個值得產品化。
- 未驗證：成交率、實際付款、客戶歷史、真實預算。

## 7. 與 BASELINE 的關係

- BASELINE：Phase 1A `05_FREELANCE_MARKET_DEEP_DIVE.md` 的結論（Freelancer 級距為預設檔、Upwork 403、一週窗口）全部仍成立；本檔未重做 MongoDB 部分。
- 與 Phase 1A 不同點：本次 AI 關鍵字在 Freelancer 一週內就有 70 件以上相關貼文（含雜訊），MongoDB 標籤只有 4 件，所以 AI 自動化需求的**可見度**遠高於 MongoDB（NEW EVIDENCE；但可見度高與付費意願高是兩回事）。
