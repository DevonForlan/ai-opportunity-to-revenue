# Phase 2 Audit Part 1：Phase 1B purchase 126 列全檢 + demand 抽樣 50 列

審計日期 2026-11-17。獨立審計者；未假設 Phase 1B 映射正確。標記：BASELINE（Phase 1B 原結論）／NEW EVIDENCE（本審計重算）／INFERENCE（審計者判斷）。

## 1. 方法與限制（先讀）

- Task 1：`02_AI_DEMAND_DATASET.csv` 中 evidence_type=purchase 的 126 列（Taiwan PCC 105 + USAspending 21）逐列人工判讀 title_problem 與 notes，決定 new_mapping / new_type / is_AI。輸出 `01_purchase_remap.csv`（126 列，欄位依指定；is_double-countable 以 note 內 `DBL:` 標記，無獨立欄）。
- **限制 1**：未重抓 PCC/USAspending 原文。PCC 列的 notes 僅含招標方式／家數，明載 "tender spec not read"；因此 new_mapping 只能依**標題**判斷。標題不足以判斷用途者標為 `other-AI` 並於 note 寫 UNKNOWN（共 31 列），這是誠實的不確定，不是已證實的分類。
- **限制 2**：Phase 1B 的 `assessment_vs_implementation` 為 25 種自由文字，本審計先正規化為 5 類（assessment/research、PoC/pilot、implementation、maintenance/expansion、other）再比較；`orig_type` 欄為正規化後值。「建置暨維護」類混合標題一律記 implementation，混合判斷屬 INFERENCE。
- 金額使用 dataset 的 award amount（TWD 或 USD 分開，不換算）。得標金額 ≠ 實付；公部門 ≠ 私人 SMB 價格。
- Task 2：seed 42（`random.seed(42)`，`random.sample`）自 169 列非 purchase（pain 143、hiring 25、provider_marketing 1）抽 50 列。分層方式：11 個 product_mapping 類別各先 `random.sample(...,1)`（類別依字母序），其餘 39 列自剩餘全體 `random.sample`。11 類全部出現。只讀 dataset 已存的標題／notes／URL，**未重抓原文**（dataset 本身多數為 "title+snippet only, full thread not read"），故判斷基於標題層級，confidence 中。

## 2. Task 1 結果：purchase 126 列

### 2.1 誤分類統計（NEW EVIDENCE）

| 指標 | 數量 |
|---|---:|
| mapping 被改 | 56 / 126（44%） |
| type 被改（正規化後） | 19 / 126（15%） |
| 任一項被改 | 63 / 126（50%） |
| 非 AI（is_AI=n） | **20 / 126（16%）**，全為 RPA/流程自動化，20 列原標 workflow-automation |

主要誤分類清單（完整逐列見 CSV）：
- **internal-assistant → other-AI：26 列**（AH001, 005, 014, 017, 022, 025, 027, 028, 033, 034, 036, 038, 040, 044, 048, 049, 053, 066, 071, 083, 086, 091, 093, 094, 099, 106）。原因：關鍵字 "generative-AI assistant / LLM application" 套到所有 GenAI 標題；實為通用 GenAI 平台、數據分析、調查、研究或用途不明案，不是「員工用內部助理」。另 AH012、AH054 → doc-automation（病歷撰寫／語音病歷），AH011 → rag-knowledge。
- **workflow-automation → not-AI：20 列**（AH016, 019, 026, 031, 052, 060, 073, 074, 076, 085, 090, 092, 095, 101, 102, 105, 123–126）。標題僅有 RPA／流程自動化／UiPath，無 AI 證據。AH052、073、076 連 RPA 都未證實（標題只寫「流程自動化」），AI=n 但性質 UNVERIFIED。
- assessment → other-AI：AH051、AH065（AI 風險／規範的**政策規劃**，非 AI 應用導入評估）；AH077 assessment → rag-knowledge（政大公行系的**學術研究**案，非交付給企業的 PoC）。
- other → other-AI：AH003、AH006（警政 AI 偵查系統）；doc-automation → other-AI：AH045（網頁廣告稽查，屬分類／監測）；rag-data-quality → ai-ready-data：AH118。
- type 修正：maintenance → implementation（標題為「建置暨維護／建立與擴充」：AH012, 019, 026, 031, 064, 082）；implementation → other（授權採購、推動計畫、輔導：AH014, 016, 022, 038, 084, 087, 090）；PoC/pilot → assessment/research（AH051, AH077）；PoC/pilot → maintenance（AH057）；其餘見 CSV。
- 弱匹配但保留：AH039（高雄 PM/QA 與技術諮詢驗證，與 eval-guardrail 只是鬆散相關）、AH043（AI 開發工具，非 end-user 助理）、AH062 與 AH041（同機構同日，可能同一方案重複計入）。

### 2.2 校正後計數（NEW EVIDENCE）

| 映射 | 原（BASELINE） | 校正後 |
|---|---:|---:|
| internal-assistant | 33 | **4**（AH004, 042, 043, 112） |
| other-AI（通用 GenAI 平台／用途不明／研究／政策） | 0（"other" 2） | **31** |
| support-automation | 28 | 28 |
| workflow-automation（AI） | 20 | **0**；not-AI（RPA）20 |
| doc-automation | 13 | 14 |
| rag-knowledge | 11 | 13 |
| agent-integration | 7 | 7 |
| assessment | 7 | **4**（AH010, 013, 063, 075） |
| eval-guardrail | 4 | 4（TW 1、US 3，皆為產品／R&D／PM-QA，非服務） |
| ai-ready-data（原 rag-data-quality） | 1 | 1 |
| 合計 | 126 | 126 |

Double-count：note 內 `DBL:` 標記 9 列為「同時可歸他類」（support/RAG、assessment/support、doc/RAG、recruit chatbot/sales 等）。原 "internal-assistant 33 與 RAG／客服重疊" 的懷疑**成立**，且程度更大：33 列中只有 4 列確為助理型。

| 類型 | 原 | 校正後 | 其中 AI 列（106） |
|---|---:|---:|---:|
| implementation | 75 | 72 | 63 |
| maintenance/expansion | 21 | 18 | 10 |
| assessment/research | 11 | 13 | 13 |
| PoC/pilot | 11 | 8 | 8 |
| other（授權／R&D／PM-QA／輔導／推動計畫） | 8 | 15 | 12 |

AI 列 106 = TW 89 + US 17；assessment+PoC 合計 21（約 20%），仍為少數；implementation 約 59%。BASELINE 的「implementation 占多數、assessment/PoC 為少數」方向不變，但 assessment 11→13 是因把政策／研究案歸入「研究」，這 13 列中有 6 列為 R&D 機構／大學／政策規劃，**買家屬研究型而非業務型**（INFERENCE）。

### 2.3 得標金額統計（校正後類別；僅公部門；TWD、USD 分開不換算）

TWD（n=105）：

| 類別 | n | 中位數 | 最小 | 最大 | ≤1.5M |
|---|---:|---:|---:|---:|---:|
| support-automation | 21 | 2,000,000 | 285,000 | 28,376,800 | 10 |
| other-AI | 30 | 4,695,000 | 341,000 | 485,508,000 | 6 |
| not-AI (RPA) | 16 | 1,640,000 | 271,140 | 8,080,475 | 8 |
| doc-automation | 12 | 3,265,000 | 277,000 | 8,950,000 | 2 |
| rag-knowledge | 12 | 4,725,000 | 1,296,750 | 11,679,000 | 2 |
| agent-integration | 6 | 3,030,000 | 1,320,000 | 5,950,000 | 2 |
| assessment | 4 | 5,791,500 | 1,480,000 | 9,366,000 | 1 |
| internal-assistant | 3 | 4,800,000 | 4,450,000 | 16,740,000 | 0 |
| eval-guardrail | 1 | 4,998,876 | 4,998,876 | 4,998,876 | 0 |
| 合計 | 105 | | | | 31 |

USD（n=21）：support 7（中位數 484,134；最小 24,179；最大 5,992,707）；not-AI 4（中位數 12,085,108；4.9M–18.4M）；doc 2（794,930–4,998,353）；eval 3（中位數 1,500,596；1.2M–2.0M）；rag 1（74,233）；agent 1（1,246,551）；ai-ready-data 1（968,066）；other-AI 1（2,934,029）；internal-assistant 1（214,655）。USD 的 AI 17 列：中位數 1,196,635、最小 24,179、最大 5,992,707；≤US$100k 僅 3 列。

非 AI（not-AI）列：**20**。

### 2.4 「≤TWD 1.5M」重算

- 全部 TW 105 列中 ≤1.5M：31（BASELINE 同）。其中 8 列為 not-AI RPA（AH085, 092, 095, 101, 102, 105 等），**剔除後 AI 列 = 23 / 89（26%）**，TW AI 中位數 TWD 3.9M；≤3M 為 35/89（39%）。
- AI 且 ≤1.5M 的 23 列主要是：support-automation 10（多為機場 chatbot、經貿網、農科院、校園 agent 等小標案）、other-AI 6、rag 2、agent 2、doc 2、assessment 1。
- 其中 assessment/research + PoC/pilot 共 **8 列**：AH075（1.48M，**僅此一列為 assessment 類別**，限制性招標、1 家投標）、AH077（1.45M，學術研究）、AH079（1.39M，研究委託）、AH081（1.32M，PoC，水利署 AI Agent 試辦）、AH083（1.29M，BIM+LLM 研究）、AH086（0.95M，規劃設計）、AH089（0.85M，PoC，公開取得報價單、5 家投標）、AH104（0.277M，PoC，原型建置）。→ 8/23 = 35% 為 assessment/PoC（BASELINE 31 列中 8 列 = 26%，4+4 數量相同，但分母因剔除 RPA 改變）。
- 已知投標家數的 AI ≤1.5M 列：19 列中 11 列僅 1 家；全部 TW 已知家數 96 列中 47 列僅 1 家（與 BASELINE 一致）。
- 招標方式：TW 105 列中 `限制性招標`（含評選）69、公開取得報價單 16、公開招標 12、UNKNOWN 8。僅 AH089 等少數屬低門檻公開取得報價。

## 3. Task 2 結果：demand 抽樣 50 列

n=50（pain 39、hiring 10、provider_marketing 1）。逐列見 `01_audit_demand_sample.csv`。

| 判定 | 數量 | 比例 |
|---|---:|---:|
| supported = y（映射與 evidence_type 皆成立） | 21 | 42% |
| supported = partly | 23 | 46% |
| supported = n（明確不成立） | 6 | 12% |
| is_buyer = y | 12 | 24% |
| is_buyer = unclear | 16 | 32% |
| is_buyer = n | 22 | 44% |

- **嚴格誤分類（n）= 6/50（12%，Wilson 95% CI 約 6–24%）**：AH140（員工職缺）、AP018（「evaluation form」關鍵字誤中 eval-guardrail）、AP042（MindBody API，無 LLM）、AP051（agent 自我審計討論，非客服）、AP103（企業 GenAI 採用評論，非 sales-backoffice）、AP149（n8n SQLite timeouts，無 AI）。
- **映射需改 = 13/50（26%，CI 約 16–39%）**；含 partly 的不完全支持 = 29/50（58%）。
- **evidence_type 錯誤**：39 個 pain 中，7 列實為徵人／付費求助（AP032, 042, 050, 061, 082, 145, 149；text 為 "hire"，類型被低估，對需求證據反而有利），15 列為非需求文本（practitioner 討論／bug／功能請求／社群分享：AP015, 031, 040, 051, 060, 069, 081, 085, 086, 092, 102, 103, 109, 139, 148），1 列為員工職缺（AP048）。即 pain 類型在嚴格解讀下 **23/39（59%）不是「買家痛點」**。另 dataset notes 中 "explicit paid-help request (by title)" 標記在樣本內出現 13 次，至少 AP018、AP113、AP139 的標題並不支持該標記；AP050 標題含 US$1,200/mo，dataset 卻寫 budget not stated（漏抓）。
- hiring 10 列：5 列 supported=y；AH128（提供者徵人）、AH136（人類資料平台）、AH140、AP009（員工）4 列不是可承接的服務買家需求。
- 買家身分：只有 12/50（24%）能判斷為 y（多為 "hire" 文字或 agency／SaaS 的 contract 職缺）；多數無預算，沒有 Phase 2 所需的「付費」證據。pain 列 39 中買家 y 僅 7。

結論（NEW EVIDENCE）：pain 類（C 級）可作為「題材分布」參考，但**不應作買家廣度或預算證據**；Buyer 廣度（pain+hiring+freelance）在評分表中的 H/M 判定應下修信心。

## 4. 哪些 Phase 1B 結論改變

| 結論 | 判定 |
|---|---|
| Top-5 順序（assessment／support／workflow／RAG／eval） | **成員大致不變，但 purchase 欄支撐削弱（INFERENCE）**。#3 Workflow Automation 的 purchase 20 全為非 AI RPA，AI workflow 公部門 purchase = 0；其 H(46) buyer 廣度來自 pain/freelance C 級證據。#5 Eval 的 purchase 4 皆為產品／R&D／PM-QA，無服務型付費證據。doc-automation（purchase 14、pain 27）可能與 eval 競爭 #5；#2 support-automation 為購買證據最強（28 列，TW 21 + US 7），順位最穩。assessment 在 purchase 只有 4 列（仍屬 L），#1 仍是 "structure 勝出" 而非證據勝出，與 BASELINE 自述一致。 |
| "internal-assistant 33" | **推翻**：33 → 4。26 列改 other-AI，其餘改 doc／rag。該列在評分表的 H(33) 為關鍵字假象，應改 L(4)；同時須新增「通用 GenAI 平台／用途不明（other-AI 31）」，反映公部門需求常是「GenAI platform」而非單一產品線。 |
| 20 筆 workflow purchase | **不是 AI 案**。BASELINE 的 workflow-automation purchase M(20) 應為 0（AI）+ 20 RPA（鄰近非 AI 市場，可作為「流程自動化付費存在」的旁證，但不是 AI 應用付費）。 |
| assessment-vs-implementation 比例 | 方向不變（implementation 為主）。AI 列中 assessment/research 13、PoC 8、implementation 63、maintenance 10、other 12。assessment 類 13 列有 6 列買家為研究機構／大學／政策規劃。 |
| 「assessment/PoC 得標落在 ≤TWD 1.5M」 | **部分成立但需縮小**。≤1.5M 的 8 列 assessment/PoC 中：純 assessment 只有 AH075（1.48M，貼近 1.5M 上限，限制性招標、單一投標）；AH077 為學術研究（非業務 PoC）、AH079/083/086 為研究／規劃類；真正的 PoC/prototype 為 AH081（1.32M）、AH089（0.85M，公開取得報價）、AH104（0.277M，原型）。BASELINE 引用的「政大 RAG PoC 1.45M」性質為學術研究，不宜作為 solo 可承接的 PoC 價格代表。 |
| 「purchase 證據落在個人可及規模」 | **削弱**。校正後 AI TW 中位數 TWD 3.9M，只有 26%（23/89）≤1.5M，且其中 11/19（已知家數）為單一投標、多為限制性招標；US 17 列 AI 中位數 US$1.2M，≤US$100k 僅 3 列且需 SAM 註冊。「個人能否投標」仍 UNKNOWN。≤1.5M 區間的主體是 support-automation chatbot（10 列），不是 assessment。結論宜改為：「有一批 ≤1.5M 的公部門小案存在，但其類型以 chatbot 為主，assessment 僅 1 列，且是否對個人開放 UNKNOWN」。 |
| 零私人買家 purchase | 不變（本審計未新增私人買家證據）。 |

## 5. Confidence

- purchase 全檢：標題層級判讀，**中等信心**。not-AI 20 列、internal-assistant 33→4 的結論**高信心**（前者標題無 AI 字樣，後者依標題可明確判定）。other-AI 31 列內部細分為 UNKNOWN，不可用於細項排名。
- type 修正：中信心（混合標題、PCC spec 未讀）。
- demand 抽樣：n=50，12% 嚴格誤分類、26% 映射需改的信賴區間寬（約 ±12pp）；只用標題／snippet 判斷，confidence 中偏低。
- 未驗證項（UNVERIFIED）：個人是否可投 PCC/USAspending 標案；ChatTYM、病歷 LLM 等標題的實際用途；PCC 原文規格。
