# 01 AI 需求證據：招聘 + 採購（Phase 1B）

## 方法與限制
- 擷取日期 2026-11-16（簡報建議 11-18 以後，此為實際日期）。唯讀研究，未聯絡任何人、未註冊帳號。
- 資料集：`02_AI_DEMAND_DATASET_hiring.csv`（AH001-AH140，共 140 列，URL 無重複）。來源紀錄：`_sources/ai_demand_hiring.csv`。
- 來源：(1) 台灣 PCC 決標公告（pcc.g0v.ronny.tw 回 301，改用 openfun 鏡像 `pcc-api.openfun.app`，以 20 個關鍵字搜標題，取 2024-01 起、award_amount 非空者，剔除硬體/訓練班/醫療影像等，保留 105 列）；(2) USAspending API（21 列）；(3) HN Who is hiring / Seeking Freelancer（Algolia API，11 列）；RemoteOK（3 列）。
- **未涵蓋**：UK Contracts Finder（關鍵字參數未生效，結果不相關，已棄用）、TED、SAM.gov、AU、SG GeBIZ、LinkedIn/Dice/Wellfound/Arc（需登入或 JS，未取得）、企業案例（provider_marketing）僅 1 列，未系統收集。Remotive API 搜尋參數無效且僅 16 筆，無相關職缺。
- 標準：award 金額 = 決標公告上的 `award_amount`（TWD）；不等於實際付款。`assessment_vs_implementation` 為**依標案名稱推斷**（INFERENCE），未讀招標規格；`product_mapping` 由關鍵字規則 + 少量人工覆寫產生，需人工複核。決標資料中投標廠商清單含未得標者，故**未記錄得標者身分**，僅記家數。
- 職缺貼文 != 付費案；job budget != 成交價；標案預算 != 最終付款。

## 計數
| 維度 | 計數 |
|---|---|
| source | Taiwan PCC 105；USAspending 21；HN Who is hiring 8；HN Seeking Freelancer 3；RemoteOK 3 |
| evidence_type | purchase 126；hiring 13；provider_marketing 1 |
| evidence_level | A 126；C 14 |
| verification_status | VERIFIED 137；PARTIALLY VERIFIED 3（RemoteOK，未讀職缺內文） |
| product_mapping | internal-assistant 33；support-automation 28；workflow-automation 22；doc-automation 15；rag-knowledge 11；agent-integration 11；assessment 8；eval-guardrail 5；ai-api-integration 2；other 2；rag-data-quality 1；sales-backoffice 1；ops-copilot 1 |

## 台灣 PCC 105 列的結構（NEW EVIDENCE，皆 VERIFIED 為決標公告欄位）
- 決標年份：2026 年 53、2025 年 36、2024 年 16。
- 金額級距（TWD）：>=1,000 萬 9 筆；300-1,000 萬 51 筆；100-300 萬 24 筆；<100 萬 21 筆。即 45/105 筆 <=300 萬，個人顧問規模可觸及的範圍存在，但多數買方為政府/國營單位。
- 買方類型：中央政府 27、地方政府 21、醫療/衛生 18、國營事業/運輸 11、國營銀行保險 10、公共研究機構 10、大學 8。**沒有一筆是一般民營 SMB**（INFERENCE：PCC 天然只涵蓋公部門，不代表 SMB 無需求）。
- 投標家數已知 96 筆中：1 家 47 筆、2 家 13、3 家 14、4 家以上 22（家數欄位為各筆決標紀錄所載）。單一投標比例高，可能表示限制性招標/評選制或供應商鎖定；對新進者而言進入門檻（資格、實績、評選）不低。INFERENCE。
- 招標方式多為「公開評選或公開徵求之限制性招標」準用最有利標，須備標案文件、實績、委員評選，個人 solo 顧問多半需掛靠公司或當分包（INFERENCE，未逐筆驗證）。
- 各 mapping 的決標金額中位數（TWD，列數）：internal-assistant 499 萬（31）；support-automation 200 萬（21）；rag-knowledge 473 萬（10）；workflow-automation 164 萬（16）；doc-automation 293 萬（11）；agent-integration 303 萬（6）；assessment 270 萬（7）。樣本小、含大型 SI，僅供量級參考。

### 評估/PoC/規劃類標案（可對應 assessment 產品；INFERENCE 依標題）
- AH063 新竹市政府「地政業務流程規劃 AI 導入策略委託研究案」2.7M TWD（細查詳情看到得標者為大學，非民間顧問）。
- AH077 政大「社會發展政策知識庫(RAG) PoC 可行性驗證機制」研究 1.45M。
- AH089 公保會「AI 輔助生成保障事件決定書稿概念驗證服務案」845,500；約一年後同單位有 AH050 系統建置案 3,800,500（可見 PoC -> 建置路徑，NEW EVIDENCE；兩案關聯為 INFERENCE）。
- AH104 台中市地政局「實價登錄申報書與契約書 AI 輔助查核原型建置案」277,000（小額原型）。
- AH010/AH013/AH015 台電綜研的 AI 客服可行性研究、生成式 AI 知識管理引進規劃、AI 知識庫精進研究（約 8.6-9.4M，偏大）。
- AH075 中華郵政 GenAI 提升金融機構營運效率研究 1.48M；AH051/AH065 文化部 GenAI 風險管理指引/規範策略規劃 3.8M / 2.65M（治理/政策類，eval-guardrail 邊緣）。

### 小額 AI 客服/聊天機器人（<100 萬，可重複的標準化範圍，INFERENCE）
經貿資訊網 AI 客服（國貿署，2024 年 38 萬、2026 年 90 萬）、北市建管處智慧客服 42 萬、北市交通事件裁決所 AI 客服機器人 34 萬、婦產科客服 AI Agent 38 萬、桃園機場 chatbot 維運 144 萬 / 社群 chatbot 135 萬。多為年度續約，顯示**客服類 AI 有重複採購**（同一買方 2024 與 2026 皆有決標）。這是 NEW EVIDENCE，但規格、技術棧與得標者仍 UNKNOWN。

### 大型專案（誠實標註，非 solo 可得）
AH001 消防署 AI 輔助 119 派遣 485.5M；台鐵 AI 客服系統 28.4M；環境部智慧客服+知識庫 12M（3 年）；北市資訊局市民智慧客服 10M；台電、國營銀行多為數百萬至千萬級，通常為 SI 主導。

## 其他來源
- **USAspending（21 列，VERIFIED）**：小額聊天機器人決標存在（USAID/Colombia chatbot 24,179 美元；Peace Corps 75,750；Ask Sage/Platform One 300,250；CPSC 484,134），也有 DoD/DOJ 的生成式 AI 平台、PoC（HHS agentic AI PoC 1.25M；VA AI PoC pilot 5.0M）。eval/guardrail 類購買證據：Arize LLM evaluation 工具 1.2M（USAF）、Swish/Lasso AI gateway 1.5M（DHS）、Mobius Logic LLM 信任 2.0M（DoD R&D）。RPA 仍是聯邦大宗（IRS 18M 級授權/維運），但多為軟體授權。美國聯邦採購需 SAM 註冊，solo 海外顧問無法直接投標，只能視為市場存在證據（INFERENCE）。
- **HN（11 列，C 級）**：AI 顧問公司（AssumeAI、Quantum Rise、Catalyst-Wayfare、Opsfleet、Stratirus）在徵人以交付客戶專案，說明「先找出 AI 有 ROI 的地方再建置」（assessment-first）與「agent 專案含 retrieval + evals + monitoring」是供給端的標準包裝。這些是供給端招聘，**不是**買方付費證據。AI 相關的 SEEKING FREELANCER 僅 3 筆（文件處理/OCR + LLM API、LLM API 整合、AI 工程師契約轉正），2026-11 的串中 0 筆。Cocient 的 evals 時薪（美元 50-250/hr，依領域）是平台付給專家的人工評測報酬，非 eval 顧問報價。
- **RemoteOK（3 列）**：產品公司內部 AI 職位，與服務買方需求關聯弱，僅作對照。

## 重點發現（供彙整）
1. **PURCHASE 證據幾乎全部來自公部門**（NEW EVIDENCE）：台灣 105 列、美國 21 列；SMB/民營買家的付費證據在本來源集仍缺（HN 招聘為間接）。
2. **客服 chatbot 與 RAG/知識庫是公部門最常付費的 AI 應用**（support-automation 28、rag-knowledge 11 + internal-assistant 33 為最大類；mapping 為關鍵字推斷）。
3. **標案存在 PoC/概念驗證 -> 建置 的階梯**（公保會 84.6 萬 PoC，之後有 380 萬建置案；政大 RAG PoC 145 萬），支持 assessment/PoC 作為入口產品，但標案制度對 solo 顧問有資格與評選門檻（INFERENCE）。
4. 單一投標家數占比高（47/96），小額（<100 萬 TWD）案多為年度維運/續約；是否能被個人承接 UNKNOWN。
5. eval/guardrail 的實際採購證據在美國有（Arize、Lasso、Mobius），台灣 PCC 僅見「PM/QA 技術諮詢驗證」類（高雄市多模態 GenAI 專案品質管理 ~5M）；台灣市場對獨立 eval 服務的付費證據弱（UNKNOWN 而非 NO）。

## 限制再述
關鍵字標題搜尋會漏掉未用 AI 字眼的案子；award_amount 未區分含稅/分年；PCC 鏡像未與官方網站逐筆比對；mapping 與 assessment/implementation 為標題推斷，需人工複核；與 Phase 1A（MongoDB/資料平台）基線之比較留給彙整階段。
