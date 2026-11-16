# 07 AI Product Candidates & Top-5 Service Design

排名依據與計數見 `08_AI_PRODUCT_SCORING.md`。以下設計皆為 **INFERENCE**，**尚未被任何付費客戶驗證**；不先套 Basic/Pro/Enterprise。命名以「業務結果」為主（買家描述的是流程結果而非「AI」：例如「帶人工轉接的 WhatsApp 客服 agent」、「名單篩選後寫進 CRM」、「發票擷取」，且反覆要求錯誤處理與可靠性 — 來自 155 列 pain 資料）。

## 候選全表（15 + 1 新增）
Assessment · Workflow Automation · Internal AI Assistant · Agent Integration · RAG/Knowledge Assistant · AI-ready Data Assessment · Ops/Process Copilot · AI+API Integration · Document/Knowledge Automation · Support/Service Automation · Sales/Back-office Automation · Eval/Guardrail/Reliability · RAG Data Quality · AI+DB/MongoDB/Kafka · **Microsoft Copilot Readiness（由供給端新增）**。

## Top 5 完整設計

### 1. AI Automation Assessment → Fixed-scope PoC（assessment-first）
- **ICP**：10–200 人、有明確重複性人工流程（客服信箱、發票/文件、名單處理、報表）但無內部 AI 工程師的公司；或需做可行性驗證的公部門／法人單位（台灣得標案中此類 PoC/研究案 TWD 0.85–1.48M，是否可由個人承接 UNKNOWN）。
- **Trigger**：老闆/部門被要求「導入 AI」但不知從何開始；試過 chatbot/n8n 後不可靠；預算需要先有依據。
- **Problem / Outcome**：把「想導入 AI」轉為「排序後的自動化候選、可行性與風險、可驗收的 PoC」。
- **In-scope**：流程盤點（≤N 個流程，N 於報價時固定）、Automation Candidate Register、資料就緒與整合點檢視、安全/隱私風險清單、架構建議、1 個流程的 PoC 規格與驗收標準、readout。
- **Out-of-scope**：正式上線、維運、取得客戶 production 資料的寫入權限、模型訓練。
- **Prerequisites / access**：訪談 2–3 小時、流程文件或螢幕錄影、**去識別化範例**（不提供個資／客戶資料）；API 文件。
- **Delivery workflow**：discovery → 流程拆解 → 候選評分 → PoC 規格 →（可選）PoC 實作。
- **Deliverables**：見 09（Opportunity Map、Candidate Register、Architecture Recommendation、Risk Register、PoC 規格與驗收案例）。
- **Acceptance**：每個候選有證據欄位（流程步驟、頻率、資料來源）；PoC 驗收案例事先約定。
- **Turnaround**：UNKNOWN（供給端常見 1–2 週，但屬廠商自述）。
- **邊界**：assessment 與實作分開報價；實作可折抵（供給端有 3 家公司與數個 solo 如此做）。
- **固定價可行性 / 遠端**：高 / 高。
- **風險**：入口審計在獨立賣家中擁擠且便宜（US$45–5,000）；私人買家購買證據 0；信任門檻。

### 2. Support / Service Automation（客服 chatbot＋人工轉接）
- **ICP**：有 LINE/WhatsApp/Email 客服量且回覆重複率高的 SMB／公部門單位。
- **Outcome**：降低重複詢問的人工處理，保留轉接與稽核紀錄。
- **In-scope**：FAQ/知識來源整理、chatbot 流程、人工轉接、成效報表；Out-of-scope：多語全渠道平台、語音。
- **Access**：客服知識文件（去識別）、渠道 API 權限（由客戶操作）。
- **Recurring**：維運/調校（PCC 21 筆為維運/擴充類得標；中位 TWD 2.93M；個人能否承接 UNKNOWN）。
- **風險**：客戶對話資料敏感度高；競爭激烈；平台依賴。

### 3. Workflow Automation（n8n/Make/API + LLM 步驟；以文件與銷售後台為最常見用例）
- **ICP**：用 CRM/Email/表單/試算表的 SMB，流程斷裂、需要整合。
- **Deliverables**：已測試的 workflow、錯誤處理、runbook、交接文件。
- **市場價位**：agency US$3k–10k；solo US$500–3,000；市集 US$130–1,450（皆為標價）。
- **風險**：市集預算低、投標多（Freelancer 中位 125）；n8n 轉包錨點 US$300–900/workflow。

### 4. RAG / Knowledge Assistant
- **ICP**：文件量大、員工常問重複問題的組織。
- **Deliverables**：知識攝取 pipeline、檢索與回答品質評估集、guardrails、交接。
- **預算線索**：市集 US$50+/hr、GBP 5–10k、US$1.5–3k（n=6，小樣本）。
- **風險**：資料敏感度與存取負擔最高；需先有 eval 才能驗收。

### 5. AI Evaluation / Guardrail / Reliability Review
- **ICP**：已上線或即將上線 LLM 功能、需要品質與風險證據的團隊。
- **Scope**：評估集建立、hallucination/regression 測試、OWASP LLM Top 10 對照、監控建議；read-only 為主。
- **公開結構最清楚**（OWASP LLM Top 10 2025、Ragas、TruLens、LangSmith、Langfuse；見 09）；驗收標準為統計式且事先約定。
- **風險**：**單獨付費證據 UNKNOWN**（pain 23；美國聯邦 3 筆 Arize/Lasso/Mobius；台灣弱）；OpenAI Evals 平台將於 2026-11-30 關閉，勿以其為基礎。較適合作為 #1–#4 的附加交付／品質保證。

## 未入 Top 5 但需觀察
Doc automation（pain 27，併入 #3）、Agent integration、Copilot Readiness（供給有標價 US$1.7k–7.5k，單一廠商生態）、AI-ready data（買家證據弱）、AI+DB（無買家證據）。
