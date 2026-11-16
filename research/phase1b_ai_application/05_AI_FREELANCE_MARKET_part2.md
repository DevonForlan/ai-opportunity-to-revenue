# 05 AI Freelance 市場 part 2 (Upwork / Arc / PRO360 / n8n+Make 社群 / 其他平台，2026-11-16)

資料表：`06_AI_FREELANCE_SAMPLES_part2.csv`（66 列，AG001-AG066）。來源：`_sources/ai_freelance_part2.csv`。Freelancer.com 與 PeoplePerHour 由另一位 agent 負責，本檔不含。
標籤 VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / UNKNOWN；證據等級 A=一手/公開 API 原文，B=經摘要器讀取的頁面，C=搜尋 snippet 或聚合頁。結論標註 BASELINE / NEW EVIDENCE / INFERENCE。

## 0. 方法與限制

**方法**
- n8n Community「Jobs」分類、Make Community「Hire a Pro」分類：公開 Discourse JSON（無登入），讀第一篇原文 (A)。
- PRO360：WebFetch 讀公開案件列表頁 (B)，預算為列表帶狀值 (NTD)，未開個案頁。
- Arc：WebFetch 讀列表與 2 個詳情頁 (B)。
- Upwork、Dice、Wellfound、Braintrust 鏡像、Indeed、LinkedIn：只有搜尋 snippet (C)。Upwork 直接抓取全部 HTTP 403（BASELINE 已知，仍成立），未繞過。
- 只收「徵人/外包」貼文；job post != paid engagement；沒有任何 `purchase` 證據。

**重大限制**
1. 39/66 列為 UNVERIFIED（snippet）。Upwork 27 列的預算與日期來自搜尋引擎摘要，且多數預算偏低（USD 5/15/80/100），疑為佔位值，與其範疇明顯不符。
2. 活性（liveness）：Lemon.io 的 Working Nomads 頁面明示「已過期」，Remotive 頁 HTTP 404；Dice 4 頁與 Wellfound 3 頁回 HTTP 410（無法分辨「已下架」或「擋爬蟲」）。BASELINE（Phase 1A）已發現 snippet 會高估當前需求，本次再度成立 (NEW EVIDENCE)。
3. 不可用或空：HN「Freelancer? Seeking freelancer?」2026-01 至 11 共 11 串，全部讀過，**AI 相關買方貼文 0 則**（僅 2 則 SEEKING FREELANCER：Flutter、電子音樂平台），無列。Toptal（只有供給端行銷）、Contra、Codeable、Malt（皆只有自由工作者檔案，無需求列表）、CakeResume（HTTP 403）、104 外包網（搜尋無結果）、Tasker（抓取失敗）、OpenAI/LangChain/HuggingFace/Cursor 論壇（無 jobs 分類）、Zapier community（endpoint 404）。以上為 UNKNOWN，不是「沒有需求」。
4. 幣別不換算；NTD、USD、GBP 分開。預算 != 成交價。
5. n8n 社群貼文約半數是 for-hire（供給），已排除；僅取買方/招募貼文。1 列（328131 AutoMatch）是招募供給的市集，屬 provider_marketing。
6. 超出 90 天窗口：Upwork CRM 顧問（2026-06-01）、Make 社群 106584（2026-03-27）、Wellfound Precept Labs、Lemon.io 過期單。保留為價格/範疇參考，不計入近期需求。
7. 未收錄：Indeed/LinkedIn 的無穩定 URL snippet（US 1099 USD 40/hr、UK GBP 250-400/日 n8n+OpenAI、fractional USD 25-35/hr 等），只在 §3 作旁證。

## 1. 計數 (n = 66)

| 平台 | 列數 | 驗證層級 |
|---|---:|---|
| Upwork (snippet) | 27 | UNVERIFIED / C |
| n8n Community Jobs | 13 | VERIFIED / A |
| PRO360 (台灣) | 6 | PARTIALLY / B |
| Arc | 5 | PARTIALLY / B |
| Dice (snippet) | 4 | UNVERIFIED / C |
| Wellfound (snippet) | 3 | UNVERIFIED / C |
| Make Community | 2 | VERIFIED / A |
| Braintrust (鏡像) | 2 | UNVERIFIED / C |
| Lemon.io | 2 | 1 VERIFIED(過期) / B，1 UNVERIFIED(404) / C |
| Indeed / LinkedIn 聚合 | 2 | UNVERIFIED / C |
| **合計** | **66** | **VERIFIED 16；PARTIALLY 11；UNVERIFIED 39** |

evidence_level：A 15、B 12、C 39（依 CSV 計，表中 Lemon 兩列分屬 B/C）。
evidence_type（本檔界定，CSV schema 無此欄）：hiring 63；provider_marketing/邊界 3（n8n AutoMatch 市集、Lemon.io 兩列）；pain 0；purchase 0。

產品映射（單一主映射，INFERENCE）：workflow-automation 13、sales-backoffice 10、agent-integration 9、rag-knowledge 5、other 5、eval-guardrail 4、support-automation 4、none 4、assessment 3、ai-ready-data 3、ai-api-integration 2、internal-assistant 2、ops-copilot 2。
不同於買方詞彙的觀察 (INFERENCE)：買方幾乎不用「RAG/guardrail」命名需求，而是描述結果（lead 流程、客服 WhatsApp、發票、CRM 同步）；eval-guardrail 的 4 列全來自 Upwork/Arc 且偏人力型。

## 2. 預算 / 時薪（僅含有明確數字的列；不換算；非成交價）

**Upwork 固定價 USD（snippet，UNVERIFIED，n=12）**：5、5、5、15、15、30、80、100、100、150、500、500。中位數 55。
- 其中 5 元三筆疑為佔位值；30 元為人工標註工作（非服務）。扣除這 4 列 (n=8)：15、15、80、100、100、150、500、500，中位數 100。
- 「RAG agent」類範疇（資料匯入、向量檢索、引用、前端、部署）標價 USD 80-150，範疇與價格明顯不符，**不可當作市價**。結論：此子集的價格資訊力 = 低 (INFERENCE)。

**Upwork 時薪（n=5，UNVERIFIED）**：USD 20-35（agent+n8n+React，3-6 個月）、USD 20（Voice AI）、USD 10-20（LLM 評測工）、USD 50-100（AI 程式碼評審，標註型）、USD 70-120（LLM-ops：Langfuse/evals，6-8 週，>30 hr/週）。僅最後一列是「可產品化的 eval/observability」形狀，且是人力計時。

**n8n 社群（VERIFIED，poster 自稱）**：單一 agency 轉包價 USD 300-900/個 workflow（每月 2-4 個，要求處理錯誤/重試）；USD 35/hr 保證+分潤；全職 Close CRM + n8n USD 2,000-3,000/月（明言非 freelancer）。
**其他**：Wellfound W-2 合約 USD 4,000-6,000/月（美國工作授權，UNVERIFIED，已超 90 天）；Dice/Indeed 聚合 snippet 顯示美國 C2C/1099 USD 40-90/hr 與 UK GBP 250-400/日，無法對應到單一 URL。
**PRO360（NTD 列表帶狀值，6 列中 3 列有帶狀）**：AI 軟體設計 10,000-50,000；AI 3D 試衣 app 100,000-300,000；爬蟲 <10,000；3 列 AI 顧問案無預算。供給端頁面公告 AI 顧問時薪 NT$3,000 / 6,500 / 10,000（低/均/高），專案 NT$5,000-100,000（供給端標價，非成交價）。
**供給端旁證（C）**：Lemon.io 頁稱 USD 27-105/hr；Contra 單一檔案報價 audit USD 1,200 / n8n+AI 起 USD 2,500；shareuhack 部落格稱典型案 NT$15,000-80,000、Tasker 有 103 筆 AI/n8n 案（無引用、未驗證）。

## 3. 發現（含標籤）

1. NEW EVIDENCE：n8n 社群與 Make 社群的買方/供給比極度偏斜。Make Hire-a-Pro 讀到約 27 串，買方請求僅 2 串，其餘為接案宣傳；n8n Jobs 29 串約半數為 for-hire。公開社群上，AI/自動化服務供給遠多於可見買方需求 (INFERENCE：買方多在 Upwork、私訊、轉介等不可見通道)。
2. NEW EVIDENCE：「可見的小額買方預算」集中在 USD 15-150 固定價（Upwork snippet）與 USD 300-900/個 workflow（agency 轉包）。兩者差一個量級，且前者疑為佔位值。若以 Upwork 公開預算定價，會嚴重低估；轉包價是更可信的下限錨點，但對象是 agency 而非終端企業。
3. NEW EVIDENCE：Arc 的 AI 職缺實為「全職式 freelance」(40 hr/週，12-52 週)，且有地域限制（US、EMEA/LATAM/NA、Berlin/Abu Dhabi 時段），詳情頁無金額。此類是人力補充，不是固定範疇產品；亞洲（含台灣）未被列為可接。
4. NEW EVIDENCE：台灣 PRO360 在 2026-11-06 至 11-15 的 AI 相關案件為：3 件「AI 顧問」(AI 導入評估/流程優化/ERP 導入，皆無預算)、AI app/軟體設計 NTD 10k-300k、爬蟲 <10k。AI 顧問類案件的買方語言是「導入 AI／優化流程」（assessment 形狀），沒有指名 OpenAI/RAG/n8n。與 BASELINE（Phase 1A：PRO360 預算多為 10k-50k NTD）一致。
5. NEW EVIDENCE：有多個買方語言明確的「小而具體」需求：WhatsApp AI 客服 agent（含 Razorpay 查單、Sheets 記錄、Slack 轉人工）、lead 管理（AI 分類+去重+標記不完整資料）、行銷歸因（API 進 BigQuery + AI lead scoring）。這三者都含「診斷＋建置＋人工轉接」，但皆有語言/時區限制（印尼語 GMT+7、印地語），台灣可及性受限 (INFERENCE)。
6. INFERENCE：eval/observability 類（Langfuse、eval-gated deploy、guardrail）只在 Upwork（USD 70-120/hr，6-8 週）與 Arc（含 eval/tracing/handover 的 12 週案）出現，均為人力計時，沒有固定範疇的 eval 產品需求列。無法支持「eval-guardrail 可產品化」的結論。
7. BASELINE 修正/延伸：Phase 1A 的 Upwork 全 403 與 snippet 過期現象在本次重現；新增 Lemon.io 實證（單頁明示過期、另一頁 404）。

## 4. 後續（需人工，規則禁止代登入）
- 人工登入 Upwork 驗證 27 列 snippet 的預算、提案數、client 歷史，優先查 USD 5/15/80/100 是否為佔位值。
- 人工查 Tasker、104 外包網、CakeResume、Malt 任務頁，補 UNKNOWN。
- 持續每週快照 n8n Jobs 與 Make Hire-a-Pro 的買方貼文比例。
