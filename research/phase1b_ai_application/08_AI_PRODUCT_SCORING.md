# 08 AI Product Scoring（evidence-backed ordinal ranking）

標籤：`BASELINE` / `NEW EVIDENCE` / `INFERENCE`。計數由我對合併資料集重算（`02_AI_DEMAND_DATASET.csv` 295 列、`06_AI_FREELANCE_SAMPLES.csv` 137 列、`04_AI_COMPETITOR_DATASET.csv` 96 列、`14_AI_DB_EVIDENCE.csv` 81 列）。**不使用數字加權分數**，避免假精準；等級 H/M/L 的門檻在下方公開，UNKNOWN 不補值。

## 1. 反 capability-bias 規則
MongoDB/DB 熟悉度**不是**評分項；僅「Data/DB 差異化」一欄依 14 號文件的買家證據評分（結果：無證據，不加分）。

## 2. 證據計數（product_mapping 為關鍵字啟發式，需人工覆核 — LIMITATION）

| 候選 | Purchase（公部門得標） | Hiring | Pain（C 級） | Freelance 樣本（137） |
|---|---:|---:|---:|---:|
| AI Automation Assessment | 7 | 1 | 0 | 4 |
| Workflow Automation | 20 | 7 | 14 | 25 |
| Support / Service Automation | 28 | 2 | 18 | 15 |
| Internal AI Assistant | 33* | 0 | 0 | 4 |
| RAG / Knowledge Assistant | 11 | 0 | 13 | 11 |
| Document / Knowledge Automation | 13 | 2 | 27 | 3 |
| Agent Integration | 7 | 4 | 19 | 15 |
| Sales / Back-office Automation | 0 | 5 | 16 | 18 |
| AI Eval / Guardrail / Reliability | 4 | 1 | 23 | 6 |
| AI + API / Enterprise Integration | 0 | 2 | 11 | 6 |
| Ops / Process Copilot | 0 | 1 | 0 | 4 |
| AI-ready Data Assessment | 0 | 0 | 0 | 4 |
| RAG Data Quality | 1 | 0 | 0 | 0 |
| AI + DB / MongoDB / Kafka | 0 | 0 | 2 | 0（14 號資料集 81 列亦為 0 AI+DB 買家證據） |
| Microsoft Copilot Readiness（新增候選，供給端出現） | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

*Internal-assistant 的 33 列全為台灣 PCC，關鍵字映射可能與 RAG／客服重疊。
所有 purchase 皆為**公部門**（台灣 PCC 105 + 美國 USAspending 21）；**私人買家購買證據 = 0**（NEW EVIDENCE，重要限制）。

## 3. 評分表（H/M/L；INFERENCE 欄標示為分析者判斷）

等級門檻（只用於有計數的欄）：Purchase H ≥25、M 8–24、L <8；Buyer（pain+hiring+freelance）H ≥45、M 15–44、L <15。

| 候選 | Purchase | Buyer 廣度 | 預算可見度 | Solo 可行（INF） | 固定 Scope（INF） | 遠端（INF） | 交付自動化潛力（INF，見 10） | 競爭/商品化（INF，越高越差） | Data/DB 差異化 | 資料敏感/存取負擔（INF） |
|---|---|---|---|---|---|---|---|---|---|---|
| Assessment | L(7) | L(5) | M（廠商 US$1.7k–12.5k 公開） | H | H | H | M–H | **H（獨立端 18/39 賣家以 US$45–5,000 審計為入口）** | 無 | 低 |
| Workflow Automation | M(20) | H(46) | M（agency US$3k–10k；市集 US$130–1,450） | H | M | H | H | **H（投標中位 125）** | 無 | 中 |
| Support Automation | **H(28)** | M(35) | L–M | M–H | M | H | M | H | 無 | 中–高（客戶對話資料） |
| Internal AI Assistant | H(33*) | L(4) | L | M | M | H | M | M | 無 | **高** |
| RAG / Knowledge | M(11) | M(24) | M（市集最高：US$50+/hr、GBP 5–10k；n=6） | M | M | H | M | M | 無 | **高** |
| Doc / Knowledge Automation | M(13) | M(32) | L | M–H | H | H | M–H | M | 無 | 中–高 |
| Agent Integration | L(7) | M(38) | L | M | L | H | M | H | 無 | 中–高 |
| Sales / Back-office | L(0) | M(39) | L | H | M | H | H | H | 無 | 中 |
| Eval / Guardrail | L(4) | M(30) | UNKNOWN | H | **H** | H | **H** | **L（供給 3/43 公司列）** | 無 | 低–中 |
| AI + API Integration | L | M(19) | L | H | L | H | M | H | 弱 | 中 |
| AI + DB / MongoDB / Kafka | L(0) | L(2) | UNKNOWN | H | M | H | M | M | **無證據** | 中 |
| Copilot Readiness | UNKNOWN | UNKNOWN | M（US$1.7k–7.5k 公開） | H | H | H | M | H（單一廠商生態，供給擁擠） | 無 | 低 |

## 4. 排名（INFERENCE，依上表）

**Top 5**
1. **AI Automation Assessment（assessment-first、費用可折抵後續 PoC/建置）**
2. **Support / Service Automation（客服 chatbot + 人工轉接）**
3. **Workflow Automation（含 Document automation 作為最常見用例）**
4. **RAG / Knowledge Assistant**
5. **AI Evaluation / Guardrail / Reliability Review**（作為評估與實作的附加／獨立 review）

與 #2/#3 近乎同級（#2 購買證據較強，#3 自由接案需求最大；兩者商品化程度皆高）。

### 為何 #1 勝出（對 Issue §17-2）
- **唯一同時滿足**「固定範圍、遠端、單人可交付、資料存取負擔低」且有購買證據落在**個人可及規模**者：PCC 105 筆得標中 31 筆 ≤TWD 1.5M，其中 assessment/PoC 類含 TWD 0.85M–1.45M（政大 RAG PoC 可行性驗證 TWD 1.45M；中華郵政 GenAI 研究案 TWD 1.48M）。
- 供給端：19/43 公司列主服務為 assessment/readiness；3 家評估費折抵建置費；PRO360 的 AI 顧問需求（2026-11-06～15）為「導入 AI」類**評估形狀**需求。
- **弱點（必須誠實列出）**：購買證據全為公部門且多為限制性招標（96 筆有投標家數者中 47 筆僅 1 家）；私人買家購買證據 = 0；solo 賣家入口審計**擁擠且便宜**（價格 US$45–5,000，約 18 個賣家）；個人能否參與標案 UNKNOWN。
- 因此 #1 的結論是**「結構」勝出**（assessment-first 作為銷售入口、PoC/建置作為營收），並非「市場已證明有人付費給個人」。

### 為何不是其他
- Workflow/Support/RAG：需求最大但 **freelance 市集預算極低且投標多**（Freelancer 固定價中位級距 US$250–750，投標中位 125），價值要靠「評估→實作」結構、特定垂直、或轉包才能站穩。
- Sales/back-office、Agent Integration：需求樣本多但無購買證據。
- Eval/Guardrail：結構清楚、自動化高、供給少，但**單獨付費證據 UNKNOWN**（pain 23、美國聯邦 3 筆 Arize/Lasso/Mobius；台灣弱）→ 作為 #1 的附加項較合理。
- AI+DB / MongoDB / Kafka：**買家證據 = 0**（NEW EVIDENCE，見 14）。不因個人能力熟悉而加分。
- Copilot Readiness：供給端有標價但單一廠商生態、需求 UNKNOWN。

## 5. 與 Phase 1A（MongoDB）的比較
- `BASELINE`：MongoDB 專屬購買證據 = 0（PCC 47 筆資料庫健檢為 Oracle/SQL Server 等）。
- `NEW EVIDENCE`：AI 應用的公部門購買證據較多（126 列，其中台灣 105），且多為客服 chatbot／知識庫／RAG／流程自動化。**兩者證據來源相同（PCC）、涵蓋範圍有限，不可據此推論私人市場。**
- `INFERENCE`：Phase 1A 的「Risk Assessment」形態（read-only、固定範圍）可保留為 AI Assessment 的**結構範本**，但 MongoDB 不再是第一產品。
