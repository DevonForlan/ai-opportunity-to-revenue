# 09 AI Deliverables Blueprint：AI Automation 服務到底交付什麼

日期：2026-11-16　標記：BASELINE / NEW EVIDENCE / INFERENCE　證據等級 A=官方 B=高可信二手 C=社群

## 0. Method & Limitations

- 方法：WebFetch 官方文件／標準機構頁面，WebSearch 補存在性確認；所有來源見 `_sources/ai_deliverables_automation.csv`（25 列）。風格與切分方式沿用 BASELINE `research/phase1_productization/08_DELIVERABLES_BLUEPRINT.md`，不重做 MongoDB 部分。
- 來源計數：source_type — vendor_official 9、vendor_docs 5、standards_body 4、oss_docs 4、vendor_blog 1、oss_template 1、local_experiment 1；evidence_level — A 24、B 1；verification_status — VERIFIED 15、PARTIALLY VERIFIED 5、UNVERIFIED 3、UNKNOWN/NEGATIVE 2（Google transform fetch 失敗；AWS Prescriptive Guidance 404）。evidence_type 全為 documentation / provider_marketing，**沒有任何 pain / hiring / purchase 證據**；本文件不處理需求面與價格。
- **核心限制（NEW EVIDENCE，負面結果）**：
  1. 沒有找到任何「付費 AI 顧問交付物的真實樣本檔」。公開的是各雲端/標準機構的**框架與方法論頁面**，不是成交交付物。下列「交付物長相」凡標 INFERENCE 者，是由框架步驟＋eval 工具文件＋通用顧問實務推導，不是複製某家樣本。
  2. 未研究 / 未取得：McKinsey / BCG 公開框架（本輪**未研究，UNKNOWN**）；Google AI Adoption Framework（gated，內容 UNVERIFIED，二手摘要不採信）；IBM（僅搜尋，找不到官方評分模板，UNVERIFIED）；OpenAI「practical guide to building agents」PDF（fetch 回傳二進位，僅確認存在，內容 UNVERIFIED）；AWS CAF-AI（fetch 實際回傳 ML Lens 頁，perspective 清單未確認）；ISO/IEC 42001（iso.org 403，僅搜尋摘要）；NIST AI RMF 頁面只列函數名，未解釋內容；process-mining 模板（Celonis / Power Automate process mining）**未研究**。
  3. WebFetch 由小模型摘要頁面；對客前請回原頁面重核。
  4. 時效警告（VERIFIED）：OpenAI Evals 平台頁面自述 2026-10-31 轉唯讀、2026-11-30 關閉（今日 2026-11-16）→ 不可把交付物綁在該平台；Anthropic「Building effective agents」頁面自述工具細節自 2024-12 已變動。
  5. 治理（組織政策）：WebComm 政策禁止客戶個資/合約/財務資料進 Claude。本文件所有「LLM 輔助」交付步驟，凡涉客戶材料者皆須事先取得許可或改用 masked-metadata（見 10 §4）。

## 1. 公開參考資料盤點

| 類別 | 來源 | 證據 | 可借用於 | 備註 |
|---|---|---|---|---|
| 評估框架 | Microsoft CAF「Plan for AI adoption」 | A VERIFIED | 最接近公開的 assessment 骨架：use case 辨識四步（從 business problem 開始→寫成 use case 句→分類「個人效率 vs 業務自動化」→選 generative / 非 generative）；maturity level 1–4（技能×資料就緒×可行 use case）；資料資產盤點；以「business impact／technical complexity／resource／alignment」打分排序；roadmap + success metrics；PoC 5 步；timeline 加 20–30% buffer | 偏 Azure 生態，但骨架廠商中立可用 |
| 評估框架 | Microsoft CAF「AI adoption strategy」 | A VERIFIED | 「選擇營運責任最小且滿足需求的方案」原則；SaaS（Copilot Studio）→PaaS→infra 的階梯；Plan/Ready/Govern/Secure/Manage 五階段 | 對 Architecture Recommendation 有用 |
| 評估框架 | AWS CAF-AI / ML Lens | A PARTIALLY | 「以最佳實踐逐題審查 workload」的 review 形式；ML Lens 有可匯入的 custom lens JSON（GitHub aws-samples，未開啟檔案） | CAF-AI perspective 清單未驗證 |
| 評估框架 | Google AI Adoption Framework | A UNVERIFIED | 僅確認存在 gated whitepaper | 不引用內容 |
| 評估框架 | IBM / McKinsey / BCG | B UNVERIFIED / UNKNOWN | IBM 僅標題；McKinsey/BCG 未研究 | 不引用內容 |
| 風險框架 | OWASP Top 10 for LLM Apps 2025（LLM01 Prompt Injection、02 Sensitive Info Disclosure、03 Supply Chain、04 Data & Model Poisoning、05 Improper Output Handling、06 Excessive Agency、07 System Prompt Leakage、08 Vector & Embedding Weaknesses、09 Misinformation、10 Unbounded Consumption） | A VERIFIED | Security/Privacy Risk Register 的現成列骨架（10 列起手） | |
| 風險框架 | OWASP LLM06 Excessive Agency | A VERIFIED | Agent 驗收條件：最小功能、最小權限、避免開放式工具（shell/URL）、以使用者身分執行、高影響動作需人工核准、下游系統自行授權、記錄與 rate limit | 可直接轉成 Guardrails 驗收清單 |
| 治理 | NIST AI RMF（Govern/Map/Measure/Manage）、Playbook、Generative AI Profile NIST-AI-600-1（2024-07-26） | A PARTIALLY | 風險登錄冊的治理對照欄；本輪未讀內文，**不得**宣稱「符合 AI RMF」 | |
| 治理 | ISO/IEC 42001:2023 | A PARTIALLY | AI management system 標準存在（2023-12）；SMB 小型專案**不應**承諾認證 | 僅摘要 |
| RAG eval | Ragas：Context Precision、Context Recall、Context Entities Recall、Noise Sensitivity、Response Relevancy、Faithfulness、（多模態版）；NVIDIA 系：Answer Accuracy、Context Relevance、Response Groundedness | A VERIFIED | RAG evaluation 報告的指標欄 | 頁面未述 test-set 生成，不主張 |
| RAG eval | TruLens RAG Triad（context relevance / groundedness / answer relevance） | A VERIFIED | 最小三指標組；頁面稱三項皆佳＝「在知識庫範圍內無 hallucination」——此為 vendor 主張，INFERENCE：不可對客保證零幻覺 | |
| RAG eval | LlamaIndex：response eval（Correctness、Semantic Similarity、Faithfulness、Context/Answer Relevancy、Guideline Adherence）+ retrieval eval（合成 question-context pairs；MRR、hit rate、precision）；question generation | A VERIFIED | 把「檢索」與「生成」分開評估的結構；Evaluation dataset 可由客戶文件合成 | 合成資料仍需人審 |
| LLM eval 實務 | Anthropic Develop tests：success criteria 要 Specific/Measurable/Achievable/Relevant；task-specific、含 edge case、能自動化就自動化、量大優於少量精品；code/LLM/human 三種 grading；LLM 評審建議用不同於生成的模型 | A PARTIALLY（讀 100000/152950 字元） | 驗收條件範式與 test case 設計 | |
| LLM eval 實務 | OpenAI Evals：eval = data schema + graders；JSONL；以人工驗證標註；模型/prompt 變更即重跑以抓 regression | A VERIFIED | 資料集格式與 regression 流程；**平台將關閉，只借概念** | |
| 觀測/評估平台 | LangSmith：datasets、reference-free / reference-based evaluators、offline vs online、regression test（新版須勝過 baseline）、annotation queues | A VERIFIED | Monitoring + regression 交付物對應 | 商業 SaaS，客戶資料出境需評估 |
| 觀測/評估平台 | Langfuse：tracing、datasets、experiments（可在 CI 以門檻阻擋部署）、LLM-as-judge、code evaluators、annotation queues、user feedback | A VERIFIED | 同上；有 self-host 選項（頁面本輪未驗，UNKNOWN） | |
| Agent 實務 | Anthropic Building effective agents：workflow vs agent；從最簡開始；工具介面（ACI）要寫範例/邊界；sandbox 測試；停止條件與人工 checkpoint | A VERIFIED（頁面自註 2024-12 時效） | Agent configuration + reliability 驗收 | |
| Agent 實務 | OpenAI practical guide to agents | A UNVERIFIED 內容 | 僅搜尋摘要：「條件不成立時，確定性方案可能就夠」 | 不引用細節 |
| 脫敏工具 | Microsoft Presidio | A VERIFIED | masked-metadata 流程的 PII 偵測/匿名化；頁面自述「不保證找出所有敏感資訊」→ 必須搭配人工抽查 | |
| 樣本 | n8n 公開 template API（workflow 2462，15 nodes） | A VERIFIED | Workflow implementation 的「真實樣貌」；本輪用於本地實驗（見 10） | 單一樣本，n=1 |

## 2. 交付物拆解：assessment vs implementation vs managed-recurring

階段欄：A=assessment、I=implementation、M=managed/recurring；● 主要、○ 可選。「公開樣本」= 本輪是否找到可借結構的公開文件。**輸出長相與驗收條件皆為 INFERENCE**（由第 1 節來源推導）。

| # | 交付物 | A | I | M | 公開樣本／可借結構 | 典型內容（INFERENCE） | 驗收條件範式（INFERENCE） |
|---|---|---|---|---|---|---|---|
| 1 | AI Opportunity Map | ● | | | MS CAF Plan（use case 辨識→分類→打分） | 一頁表：use case 句、流程、頻率、現行工時（客戶提供，非估算）、AI 類型、資料來源、價值/可行/風險三軸分數、建議排序 | 每個 use case 可追溯到一個 business problem；評分準則書面化且客戶確認；前 N 名附 go/no-go 理由 |
| 2 | Process Map | ● | ○ | | BPMN 為通用記法（Camunda 頁僅確認支援子集，低證據） | 現況 as-is 流程圖（角色、系統、輸入輸出、例外分支）+ 標出人工判斷點 | 客戶逐步走查簽核；例外路徑覆蓋客戶列舉的前 N 類案例 |
| 3 | Automation Candidate Register | ● | | ○ | 無公開 register 樣本；MS CAF 提供評分欄位 | 表格：流程步驟、頻率、量、規則明確度、資料可及性、錯誤成本、是否需人審、建議方案層級（規則/腳本/LLM/agent） | 每列有「方案層級＋理由」；高錯誤成本者強制標「人審」 |
| 4 | Architecture Recommendation | ● | ○ | | MS CAF：SaaS→PaaS→infra 階梯、最小營運責任原則；Anthropic：最簡優先、workflow vs agent | 1 張架構圖 + 選型表（build/buy/低程式碼）+ 營運責任與成本結構說明 | 至少比較 2 個替代方案；列出被排除方案與理由；客戶 IT 確認可行（網路/身分/資料位置） |
| 5 | Integration Map | ● | ● | | 無公開樣本 | 系統清單、API/auth 型式、速率限制、資料欄位對應、寫入權限、失敗處理 | 每個整合點有已確認的存取方式（不是假設）；寫入動作單獨標示 |
| 6 | Data Readiness Assessment | ● | | | MS CAF Plan：資料資產盤點（來源/格式/品質/可及性）、maturity level | 文件/資料來源清冊、格式與品質抽樣、授權與敏感度分級、更新頻率、缺口 | 清冊覆蓋客戶指定範圍；品質結論附抽樣方法與樣本數；敏感度分級經客戶確認 |
| 7 | Security/Privacy Risk Register | ● | ● | ○ | OWASP LLM Top 10（10 列骨架）；NIST AI RMF 對照（僅名稱）；ISO 42001（存在） | 列：風險、情境、現有控制、殘餘風險、負責人、處置；加台灣個資法與資料出境欄（法規內容本輪未研究，UNKNOWN） | 10 類全部「適用/不適用＋理由」；每個高風險有對應控制與測試案例 |
| 8 | Prototype / POC | ○ | ● | | MS CAF Plan：PoC 5 步、內部非面向客戶優先、記錄 lessons、20–30% buffer | 可跑的最小流程 + 範圍/成功指標書 + 結果報告（含失敗案例） | 在預先約定的評估集上達成預先約定的門檻；結果報告含失敗案例，不只成功 demo |
| 9 | Workflow implementation | | ● | ○ | n8n 公開 template（實例）；Anthropic：workflow 優先 | 工作流 JSON/程式碼、環境設定、憑證交接清單、版本控制 | 在客戶測試環境端到端跑通約定案例集；失敗有重試/告警；憑證不入版本庫 |
| 10 | Agent configuration | | ● | ○ | Anthropic（工具設計、停止條件、人工 checkpoint）；OWASP LLM06 | system prompt、工具清單與權限、停止條件、人工核准點、成本上限 | 權限最小化清單通過；高影響動作必須人工核准；sandbox 測試案例通過；有最大迭代/成本限制 |
| 11 | RAG evaluation | ○ | ● | ● | Ragas / TruLens / LlamaIndex 指標 | 檢索與生成分開評估報告（Context Precision/Recall、Faithfulness、Answer Relevancy 等）、誤差分類、改善建議 | 指標與門檻預先約定；使用客戶認可的評估集；報告含人工抽查的一致性（LLM 評審 vs 人） |
| 12 | Knowledge ingestion pipeline | | ● | ○ | LlamaIndex 等（切塊/索引為工程實務；本輪未驗官方細節） | 文件擷取→清洗→切塊→嵌入→索引→更新排程；來源與版本 metadata | 指定文件集全數可檢索；增量更新可重現；刪除/權限變更可傳遞到索引（OWASP LLM08 相關） |
| 13 | API integration | | ● | ○ | 無公開樣本 | 連接器程式碼、錯誤處理、冪等與重試、速率控管、金鑰管理 | 對測試環境通過合約測試；重複執行不產生重複寫入 |
| 14 | Test cases（功能/整合） | | ● | ● | 一般軟體測試實務 | 測試矩陣、前置資料、預期結果 | 全數通過或例外經客戶書面接受 |
| 15 | Evaluation dataset | ○ | ● | ● | Anthropic（量大、edge case）；OpenAI（人工驗證標註）；LangSmith/Langfuse datasets | 輸入＋參考答案（如適用）＋metadata；來源（客戶提供/合成/生產抽樣）；標註者與審核紀錄 | 規模與分層覆蓋事先約定；標註經客戶領域專家抽審；與訓練/提示範例分離 |
| 16 | Reliability / hallucination analysis | ○ | ● | ● | TruLens triad；LlamaIndex Faithfulness；Anthropic grading 方法 | 錯誤分類（檢索錯、生成偏離、拒答不當、格式錯）、頻率、代表案例、緩解 | 錯誤率以預先約定指標報告並附信賴說明；**不承諾零幻覺**；高風險類別有緩解措施 |
| 17 | Guardrails | | ● | ○ | OWASP LLM01/02/05/06/07/10；Presidio（輸入脫敏）；Anthropic 停止條件 | 輸入/輸出檢查、拒答策略、權限上限、成本上限、人工升級路徑 | 對一組對抗/越權測試案例達到約定攔截率；失敗模式有 fallback；測試集保存可重跑 |
| 18 | Runbook | | ● | ● | 一般 SRE 實務；LangSmith/Langfuse 觀測 | 告警→診斷→處置→升級；憑證輪替；回滾；已知失效模式 | 客戶人員按 runbook 完成至少一次演練（含回滾） |
| 19 | Monitoring / observability | | ● | ● | Langfuse tracing/online eval；LangSmith online eval | trace、成本/延遲/錯誤率儀表、抽樣人審佇列、漂移告警 | 約定指標在儀表可見；告警送達實測；trace 中的敏感資料處置符合約定 |
| 20 | Handover documentation | | ● | | 通用 | 架構、設定、憑證位置（非明文）、操作與限制、已知問題 | 客戶人員依文件可獨立完成指定操作（走查驗收） |
| 21 | Training | | ● | ○ | MS CAF：存取需搭配訓練 | 操作/審核/例外處理培訓與教材 | 出席與演練完成；客戶完成約定情境練習 |
| 22 | Post-launch support | | ○ | ● | 無公開範本 | 固定期間缺陷修復、回歸評估重跑、模型/Prompt 變更評估、月報 | SLA 為書面約定（本輪未查證任何市場 SLA 慣例，UNKNOWN）；每次變更前後跑同一評估集比較 |

## 3. 最小可信交付組（INFERENCE，非市場驗證）

### 3.1 Assessment-first offer（對應 product_mapping：assessment）
1. 範圍與成功定義書（客戶確認）
2. AI Opportunity Map（#1）＋ Automation Candidate Register（#3）
3. Process Map（只針對前 1–3 個候選，#2）
4. Data Readiness 摘要（#6，抽樣式）
5. Architecture Recommendation（#4）＋ Integration Map（#5，僅確認存取方式）
6. Security/Privacy Risk Register（#7，OWASP 10 列起手）
7. 建議路線圖＋ go/no-go 與下一步（含 PoC 範圍草案與預先約定的成功指標）
8. 簡報／走查會議（含簽核）
- 判準：客戶讀完後能**不依賴顧問**決定「做/不做/先做哪個」。若只交一份通用 AI 報告而無可追溯的 register 與風險表，可信度不足（INFERENCE）。
- 風險（INFERENCE）：BASELINE 的 MongoDB audit 可用唯讀命令＋規則引擎確定性產出；AI assessment 的核心輸入多是**訪談與流程知識**，確定性程度低、對人工專長依賴高，且客戶端資料常含個資（受政策限制）。

### 3.2 Implementation-first offer（對應：workflow-automation / support-automation / doc-automation / rag-knowledge 等，視案而定）
1. 需求與驗收書（含評估集規模與門檻）— **先於開發**
2. Process Map（目標態）＋ Integration Map（#5）
3. Workflow implementation（#9）或 RAG（#12 + #11）或 Agent（#10）
4. Evaluation dataset（#15）＋ Test cases（#14）＋ 評估報告（#11/#16）
5. Guardrails（#17）＋ 安全審查結果（#7 子集）
6. Runbook（#18）＋ Monitoring 基本版（#19）
7. Handover documentation（#20）＋ Training（#21）
8. 上線後保固期（#22 的有限版本）
- 判準：交付物不只是「能跑」，而是「有評估集證明在約定指標上達標、有人知道怎麼運維」。缺 #15/#16/#18 者屬 demo，非可驗收的 implementation（INFERENCE）。

## 4. 驗收條件範式（INFERENCE，借自 Anthropic/OpenAI eval 指南的原則）

1. **指標先於開發**：Specific / Measurable / Achievable / Relevant（Anthropic，VERIFIED）。門檻由客戶與顧問**共同書面約定**；顧問不得自行挑選對自己有利的評估集。
2. **統計式驗收取代「全部正確」**：LLM 輸出非確定性（MS CAF 明述 generative AI「同輸入可能不同輸出」）→ 驗收寫成「在 N 筆評估集上通過率 ≥ X%，且 Y 類高風險案例 0 個未處理」。X、N 為待約定值，**本文件不給建議數值**（UNKNOWN，無證據）。
3. **評估集由客戶領域專家抽審**；合成資料標註為合成。
4. **LLM-as-judge 需校準**：以人工抽樣檢驗評審一致性（Anthropic 建議以他模型評審、人工用於校準，VERIFIED）。
5. **Regression gate**：任何 prompt/模型/程式變更後重跑同一評估集，不得低於 baseline（LangSmith / Langfuse / OpenAI，VERIFIED）。
6. **權限與動作驗收**：寫入、寄信、刪除等動作需明列並經人工核准或限額（OWASP LLM06，VERIFIED）。
7. **負面驗收**：越權、注入、洩漏測試案例（OWASP LLM01/02/07）必須存在並可重跑。
8. **失敗案例必須披露**：報告含失敗與限制，不以單次成功 demo 驗收。
9. **範圍外聲明**：不保證零幻覺、不保證節省工時/ROI（無證據不可承諾）。

## 5. 對產品決策的含義（INFERENCE，非需求證據）

- 可標準化度：交付物 #6、#7、#11、#15–#19 有明確公開結構與工具，適合模板化；#1–#5 依賴訪談，模板只能給骨架。
- 「eval + guardrail」類交付物（product_mapping：eval-guardrail、rag-data-quality）在公開文件中結構最清晰、可確定性驗收，但**是否有人付費買獨立的 eval 服務，本輪無證據（UNKNOWN）**，需由需求面文件裁決。
- 避免能力偏差：MongoDB/資料庫整合（ai-db-integration）僅為整合點之一，本文件未因使用者熟悉而給予額外權重。
- 待補（建議下一輪）：McKinsey/BCG 公開框架、process-mining 模板、Taiwan 個資法對 LLM 流程的具體要求、真實成交交付物樣本（可能不公開，UNKNOWN）。
