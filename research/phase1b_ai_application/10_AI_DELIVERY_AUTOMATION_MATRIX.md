# 10 AI Delivery Automation Matrix：交付一個 AI 自動化服務本身可以自動化多少

日期：2026-11-16　標記：BASELINE / NEW EVIDENCE / INFERENCE

## 0. Method & Limitations

- 方法：沿用 BASELINE `research/phase1_productization/09_AUTOMATION_MATRIX.md` 的圖例與欄位；工具與事實性陳述引自 `_sources/ai_deliverables_automation.csv`（25 列，A 24 / B 1；VERIFIED 15 / PARTIALLY 5 / UNVERIFIED 3 / UNKNOWN 2）。**class、AI usefulness、hallucination 風險、所需專長、production 風險、auditability 皆為 INFERENCE（作者判斷，非實測）**。
- **自動化百分比 = UNKNOWN**（未量測；全文不給任何百分比）。
- **本地實驗（有限）**：見 §3，僅 1 個公開 workflow 樣本（n=1），LLM-free、無帳號、無金鑰、無客戶資料；證明「可確定性地盤點 workflow JSON」，**不**證明其他 21 步的自動化程度。其餘步驟一律 **not tested**。
- 所有 LLM 步驟尚未實測品質；沒有任何 LLM 輸出被用於本文件。
- 治理：WebComm 政策禁止客戶個資/合約/財務資料進 Claude。凡「LLM」或「agent」欄且涉客戶材料者，**須先取得許可或走 §4 masked-metadata**，否則降為 HR/HO 並以人工完成。
- 圖例：DS deterministic script；LLM LLM-assisted（人覆核）；AG agent-assisted（多步工具使用，人覆核）；HR human review required；HO human-only high-risk。AI 有用度：高/中/低（INFERENCE）。

## 1. 主矩陣（22 步）

| # | 步驟 | Input | Output | 主 class | AI 有用度 | Hallucination / 錯誤風險 | 所需人類專長 | Client-access / production 風險 | Auditability | 工具（引文件處） |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Discovery（訪談、範圍） | 客戶訪談、現有文件 | 範圍書、利害關係人表 | HR（LLM 僅整理逐字稿，需許可） | 中 | 中：摘要遺漏/誤植 | 高（提問、談判範圍） | 低（無系統存取）；逐字稿含個資 | 中：保留原始紀錄即可回查 | 無特定；見 §4 |
| 2 | Requirement extraction | 訪談紀錄、SOP、工單樣本 | 需求清單＋驗收條件草稿 | LLM + HR | 中 | 中：憑空補需求 | 高 | 低；材料可能含客戶機密 | 中：每條需求須連回來源句 | Anthropic：success criteria 須 Specific/Measurable（A，VERIFIED） |
| 3 | Workflow mapping（as-is） | 步驟描述、螢幕錄影/日誌、既有 workflow JSON | Process Map、決策點 | LLM + HR；若有 workflow JSON 則 DS | 中 | 中高：LLM 易「補全」未說出的步驟 | 高（領域流程） | 低–中：截圖含個資 | 中 | BPMN 記法（Camunda 頁僅確認子集，低證據）；DS 部分見 §3 實驗 |
| 4 | Process analysis（頻率、例外、瓶頸） | 工單/日誌匯出（客戶資料） | 頻率表、例外分類 | DS（統計）+ HR | 中（LLM 僅對文字欄位分類） | 中：分類標籤漂移 | 中 | **中高：需讀客戶營運資料**；個資 | 高（DS 可重現） | process-mining 工具**未研究**，UNKNOWN |
| 5 | Opportunity identification（打分排序） | #2–#4 的輸出 | Opportunity Map、Candidate Register | LLM + HR | 中 | 中：分數看似精確實為主觀 | 高（價值判斷、客戶政治） | 低 | 中：評分準則須書面化 | MS CAF Plan 打分法（A，VERIFIED）；OpenAI agents guide：條件不符時確定性方案可能就夠（僅摘要，UNVERIFIED） |
| 6 | Architecture | 需求、約束、整合清單 | 架構建議、選型比較 | HR（LLM 作選項腦力激盪） | 中 | 中高：過時產品資訊、虛構功能 | 高 | 低 | 中：決策需記錄理由 | MS CAF 階梯（SaaS→PaaS→infra；A，VERIFIED）；Anthropic 最簡優先（A） |
| 7 | Connector/API discovery | 客戶系統清單、公開 API 文件、OpenAPI spec | 整合地圖、auth/限額/欄位對應 | DS（解析 OpenAPI）+ LLM（讀文件）+ HR | 高（讀文件、比對欄位） | 中：LLM 幻想不存在的 endpoint；須以官方 spec 驗證 | 中–高 | 中：需客戶測試帳號與權限；**勿用生產憑證探測** | 中–高 | OpenAPI 解析為通用做法（本輪未研究，UNKNOWN） |
| 8 | Prototype | 選定 use case、少量脫敏樣本 | 可跑的最小流程 | AG / LLM + HR | 高 | 中：原型成功≠生產可靠 | 中–高 | 低（在自有 sandbox 用合成/脫敏資料）；接客戶系統則升高 | 中：版本庫＋prompt 版本 | MS CAF PoC：先做內部、非面向客戶案例（A，VERIFIED） |
| 9 | Coding | 規格、整合地圖 | 工作流/連接器程式碼 | AG / LLM + HR | 高 | 中：看似可行的錯誤實作、過時 API 用法 | 中–高（審碼） | 中：若在客戶環境部署則高；**程式碼勿含客戶金鑰（組織政策）** | 高：git diff | n8n 公開 template 示範常見結構（A，VERIFIED，§3） |
| 10 | Testing（功能/整合） | 需求、程式碼、測試資料 | Test cases、結果 | LLM（生成案例）+ DS（執行）+ HR | 高 | 中：生成案例偏 happy path | 中 | 低–中：整合測試打到客戶測試環境 | 高 | 一般測試框架（本輪未研究具體工具） |
| 11 | Prompting | 需求、評估集、範例 | Prompt、系統指令、工具描述 | LLM + HR（以評估集迭代） | 高 | 中：無評估集時「感覺變好」不可驗證 | 中 | 低 | 中：prompt 版本化＋評估結果綁定 | Anthropic 工具/ACI 設計（A，VERIFIED）；OpenAI Evals：先定義期望行為（A，VERIFIED） |
| 12 | Evaluation（含 guardrail 測試） | 評估集、系統、指標 | 評估報告、regression 基線 | DS（code grader）+ LLM（judge）+ HR（校準） | 高 | 中高：LLM judge 偏誤；評估集不代表真實分佈 | 高（設計指標與解讀） | 低–中：用客戶資料作評估集則受政策限制 | 高：資料集＋評分器版本化 | Ragas 指標、TruLens triad、LlamaIndex eval、LangSmith/Langfuse（均 A，VERIFIED）；OpenAI Evals 平台將於 2026-11-30 關閉（A，VERIFIED）→ 勿依賴 |
| 13 | RAG dataset preparation | 客戶文件（常含機密/個資） | 清洗後語料、metadata、評估問答 | DS（解析/清洗/去重）+ LLM（合成問題）+ HR | 中–高 | 中：合成問題偏易；OCR/表格解析錯 | 中–高 | **高：需接觸客戶文件**；個資/機密 | 高（DS）/中（LLM 合成） | LlamaIndex 合成 question-context pairs（A，VERIFIED）；Presidio 脫敏（A，VERIFIED：不保證找出全部） |
| 14 | Document ingestion | 語料 | 向量索引、更新排程 | DS | 低（工程為主） | 低–中：切塊策略影響檢索 | 中 | 中–高：寫入索引、權限傳遞（OWASP LLM08） | 高 | OWASP LLM08 Vector & Embedding Weaknesses（A，VERIFIED） |
| 15 | Integration（上線接線） | 程式碼、客戶測試/生產憑證 | 已連線流程 | HR（AG 僅限測試環境） | 低–中 | 中：誤寫入 | 高 | **高：生產寫入權限**；憑證處理 | 高：變更紀錄需完整 | OWASP LLM06：最小權限、人工核准高影響動作、下游自行授權（A，VERIFIED） |
| 16 | QA | 全部產出 | QA 紀錄、缺陷清單 | DS + HR | 中 | 中 | 中 | 低–中 | 高 | 同 #10、#12 |
| 17 | Security review | 架構、prompt、權限、資料流 | Risk Register、發現清單 | HR（LLM 作清單提示；**不得**作為結論來源） | 中 | **高**：LLM 常漏報/誤報；責任不可轉嫁 | 高（資安） | 中：需看客戶架構 | 高（須附證據） | OWASP LLM Top 10 2025、LLM06（A，VERIFIED）；NIST AI RMF / ISO 42001 僅 PARTIALLY，不宣稱符合 |
| 18 | Documentation（交接文件） | 程式碼、設定、決策紀錄 | 架構/操作文件 | LLM + HR | 高 | 中：文件與實作不一致 | 低–中 | 低；勿寫入明文憑證 | 高：與 repo 同步 | 無特定 |
| 19 | Training material | 文件、系統 | 教材、練習情境 | LLM + HR | 高 | 中 | 中 | 低 | 中 | MS CAF：存取須搭配訓練（A，VERIFIED） |
| 20 | Deployment preparation | 程式碼、客戶環境規格 | 部署清單、回滾計畫 | DS（腳本）+ HR；實際部署 HO | 低–中 | 中：環境假設錯誤 | 高 | **高：生產部署**；AGENTS.md 規則 3 禁止未經授權 production deploy | 高 | 無特定 |
| 21 | Monitoring | trace、成本、品質抽樣 | 儀表、告警、人審佇列 | DS（設定）+ LLM（online judge）+ HR | 中 | 中：online judge 漂移 | 中 | 中：trace 內含客戶輸入（個資）→ 保存與存取需約定 | 高 | Langfuse online eval / LangSmith online eval / annotation queues（A，VERIFIED） |
| 22 | Maintenance（regression、模型/Prompt 更新） | 評估集、變更請求 | 變更評估報告 | DS（重跑評估）+ HR | 中–高 | 中：模型更新造成靜默退化 | 中–高 | 中：需持續存取 | 高 | LangSmith regression test、Langfuse CI 門檻（A，VERIFIED） |

## 2. 觀察（INFERENCE）

1. **高 AI 槓桿集中在「文字/程式碼生成與整理」類步驟**：#2、#7、#9、#10、#11、#18、#19。這些步驟的錯誤可由人審或測試在交付前攔截。
2. **高風險不在 AI 而在存取**：#4、#13、#15、#20 需接觸客戶資料或生產系統，風險來自政策/權限而非模型品質；這與 BASELINE（MongoDB 唯讀診斷）不同——BASELINE 的輸入是系統 metadata，這裡的輸入常是**客戶內容本身**。
3. **評估（#12）是可確定性執行但需人設計的關鍵步驟**；它也是把「LLM 不確定性」轉成可驗收條件的唯一手段（見 09 §4）。
4. **LLM 不應成為安全審查（#17）與架構決策（#6）的結論來源**，僅作提示。
5. 不可由本文件推出任何「可自動化 X%」或「工時下降 Y%」——**UNKNOWN**，需在真實案例中計時量測。

## 3. 本地安全實驗（LLM-free）：解析公開 n8n workflow JSON

- 目的：驗證矩陣 #3/#7/#9 的 DS 部分——能否不靠 LLM、不碰客戶資料，確定性地把 workflow 檔轉成盤點表。
- 輸入：n8n 公開 template API（`https://api.n8n.io/api/templates/workflows/2462`，GET，HTTP 200，35,128 bytes），下載到 session scratchpad 的獨立目錄；腳本放在另一目錄，以 `python -I` 執行（檔案視為不可信資料；僅 `json.load`，不執行）。未使用帳號、金鑰、付款。
- 腳本：`scratchpad/tools/n8n_inventory.py`（約 30 行，未納入 repo；若需要可另行提 PR）。
- 結果（VERIFIED，n=1）：15 nodes、14 個連線來源；1 個 trigger（Telegram）、4 個 LLM/agent 相關節點（含 1 個 agent、1 個 chat model、1 個 memory、1 個語音轉文字）、4 個 tool 節點（Baserow ×2、Google Calendar、Gmail）、4 個邏輯節點；偵測到 5 種憑證**型別**（telegramApi、openAiApi、baserowApi、googleCalendarOAuth2Api、gmailOAuth2），憑證 id 不輸出；標出 1 個 agent 節點「需 eval set + tool 權限審查」；列出無入邊節點（trigger 與 sub-node，屬預期）。
- 限制：
  - 「tool 節點含寫入/寄信動作」的規則**未觸發**——因 n8n 的操作多以 resource/operation 欄位或 expression 表示，簡單關鍵字比對不可靠；此規則需對 n8n 節點 schema 逐型別撰寫（未做）。→ 這也說明：Excessive-agency 審查**不能**只靠關鍵字腳本，仍需人審。
  - 只測 1 個樣本、1 個平台（n8n）；未測 Make/Zapier/LangGraph 等；未測任何 LLM 步驟；未量測節省時間（UNKNOWN）。
  - 該樣本是個人助理 demo，不代表客戶流程複雜度。
- 其餘 21 步：**not tested**。

## 4. 治理設計：masked-metadata 方法（INFERENCE，待 IT / 資安許可）

前提：WebComm 政策禁止客戶個資、合約、財務資料輸入 Claude；Presidio 官方頁自述「不保證找出所有敏感資訊」（A，VERIFIED）→ **自動脫敏不能單獨作為合規依據**。

建議分層（由低風險到高風險）：
1. **Level 0 — 零客戶內容**：僅用公開文件、廠商文件、合成資料或自建樣本訓練/測試流程與 prompt（矩陣 #8、#9、#11 的開發階段）。
2. **Level 1 — 只送結構性 metadata**：由 DS 腳本在客戶環境或本機產生，內容僅限：欄位名/型別、行數、缺失率、文件數量/副檔名/頁數/語言分佈、流程步驟的角色與系統名稱（不含人名）、錯誤類別計數。**不含任何自由文字內容**。LLM 只看這份 metadata 產出建議（例：#4、#5、#6、#13 的規劃）。
3. **Level 2 — 脫敏後文字樣本**：先經 Presidio 類工具＋**人工逐筆抽查**＋客戶書面同意，才可由人決定是否送 LLM；需事先取得公司許可（政策要求諮詢 IT）。預設**不啟用**。
4. **Level 3 — 客戶內容與 LLM 的互動由客戶自己的環境完成**（客戶自有 LLM 帳號/私有部署，顧問不接觸資料）：顧問只交付流程、prompt、評估集模板與驗收標準。此模式使 #12、#13 的客戶資料步驟移出顧問的 Claude 使用範圍。
5. 一律：金鑰與連線字串不入 prompt、不入 repo（組織政策）；觀測平台（LangSmith 等 SaaS）的資料出境與保存**未評估，UNKNOWN**，在對客提案前須確認。
- 對產品的含義（INFERENCE）：此約束使「以 LLM 加速客戶資料處理」不可預設；較安全的槓桿是「LLM 加速**我方產物**（程式碼、文件、教材、測試案例）」與「DS 腳本處理客戶資料」。

## 5. 未解與下一步

- 實測計時：在 Level 0 資料上完整走一遍 #7→#12，記錄人工與 AI 時間（目前 UNKNOWN）。
- process-mining 工具、OpenAPI 解析工具、n8n 節點 schema 規則庫：未研究。
- Langfuse self-host 與資料保存條款：頁面本輪未驗。
- 台灣個資法對 LLM 流程的具體要求：未研究，須諮詢 IT／法務。
