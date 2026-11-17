# 07 Final Offer Design（Entry / Revenue / Follow-on）

依據：01（修正後排名）、02（私人買家證據天花板）、04（solo 交付案例）、05（台灣）、06（PCC）、08/10/11（Pilot）。標籤：BASELINE / NEW EVIDENCE / INFERENCE。**所有價格為待驗證假說，非成交價。**

## 0. 為什麼與 Phase 1B 不同
`BASELINE`（Phase 1B）：以 Assessment 為 #1、assessment-first。
`NEW EVIDENCE`：已交付的 solo 案例中 **32/39 為直接實作**，**審計→建置的驗證轉換 = 0**（04）；purchase 證據中 assessment 僅 4、implementation 72（01）。→ **把 Revenue Offer 放在固定範圍的實作 PoC；Assessment 降為 PoC 內的「診斷週」或可選入口，不當獨立主力。**

## A. Revenue Offer（主）— 客服信件分流與草稿回覆 PoC（人工核准版）
- **Product name（以業務結果命名）**：「客服信件處理時間縮減 PoC — 每封回覆仍由你核准」
- **ICP**：有穩定客服信量（每日數十封以上）、回覆多為重複類型、知識文件已存在的中小型電商／服務業（約 10–200 人）。**不選**：需要法規認證、含大量敏感資料、或已有成熟客服平台＋內部 AI 團隊的公司。
- **Buyer role**：客服主管／營運負責人（預算持有者通常為營運或老闆；UNKNOWN，需在 discovery 驗證）。
- **Trigger event**：客服量上升、新增通路（LINE/Email）、客服人力離職、被要求「導入 AI」。
- **Problem**：重複性信件佔用人力；擔心 AI 亂答；不知道從哪個流程開始。
- **Promised outcome（不承諾節省比例）**：在客戶提供的去識別化樣本上，交付一套可運作的分流＋有依據草稿＋人工核准流程，附評估報告與已知限制。
- **Exact scope**：1 個渠道、≤N 個信件類別（N 於報價時固定，建議從 Pilot B 的 6 類起）、客戶提供的 KB（≤X 篇，報價時固定）、1 個 CRM/工單目標（PoC 使用 mock 或客戶沙盒）、評估集（客戶去識別化樣本＋合成補充）。
- **Out-of-scope**：正式上線、維運、多渠道、語音、訓練模型、對客戶 production 資料的寫入、無人核准的自動寄送。
- **Prerequisites / access**：去識別化樣本信件（客戶操作）、KB 文件、核准者指定、系統權限限最小（上線階段才需要，由客戶操作）。
- **Customer effort（假設）**：提供樣本與文件、1–2 次評審會議、核准者標註少量草稿；**時數 UNKNOWN**（需在首次 pilot 量測）。
- **Deliverables**：運作的程式碼與 runbook、評估集與結果（含 HELDOUT 與已知限制）、稽核機制、範圍外建議、上線前檢核表、交接簡報。
- **Acceptance criteria**：事先約定的測試案例集全數執行；**危險方向錯誤（該升級卻出草稿）= 0 為硬性驗收**（於客戶樣本上）；PII 洩漏 = 0；承諾違規 = 0；其餘指標以雙方事先書面約定的門檻為準（**不由我預設數字**）。
- **Delivery steps**：診斷（含於本 offer）→ KB 整理 → 規則/（可選）模型 provider → 評估 → 核准流程 → 交接。
- **Data/privacy boundary**：只處理去識別化資料；不要求卡號/身分證/密碼；任何外部模型使用須書面同意；顧問端依公司政策不將客戶資料送入 Claude（需先決策替代方案）。
- **Turnaround hypothesis**：UNKNOWN（供給端常見 2–5 週，Clutch 案 2–5 個月；皆為廠商自述）。
- **Pricing hypothesis**：見 14（三個假說，皆待驗證）。
- **Upgrade / follow-on path**：見 C。
- **Kill criteria（此 offer）**：見 §D。

## B. Entry Offer（可選，作為實驗臂）— 客服流程診斷週（固定價、可折抵 PoC）
- 內容：1 週內完成流程盤點、樣本檢視、KB 缺口、風險與資料邊界、PoC 規格與驗收案例；輸出＝縮小版 Pilot A 報告（真實客戶版）。
- **為何仍保留**：供給端 19/43 公司以 assessment 為主服務、3 家折抵建置費、PRO360 有 3/6 諮詢形狀需求，代表「先診斷」在買方端是可理解的入口。
- **為何不作主力**：購買證據 4、轉換驗證 0、價格兩極（solo 中位 US$624.5 vs boutique US$3,950）、獨立賣家入口審計擁擠。
- 角色：**降低成交摩擦的實驗臂**，在 14 的定價實驗中與「PoC 內含診斷」對照。

## C. Follow-on Offer（暫定義，證據弱）
- 上線輔導（連接客戶沙盒→production，客戶操作授權）、每月評估與規則/KB 調校（retainer）、第二流程擴充。
- **證據**：solo retainer 標價 US$1.8k–9k/月（標價；2 位賣家明確拒絕 retainer）；Zipify 型長期合作僅有供應商自述（04）。**成交證據：UNKNOWN。**

## D. Kill criteria（offer 層）
- 暖關係接觸中，**無任何一位**對固定範圍 PoC 給出書面付費意願（人數與期限由使用者在 15 中設定）。
- 首次真實 pilot 的**有效時薪**低於使用者設定底線（需先量測人工時間）。
- 客戶資料政策使 PoC 無法在去識別化資料上驗證。
- 危險方向錯誤在客戶樣本上無法降到 0（即使加上人工核准仍不可接受）。

## E. 與 Phase 1B Top-5 的關係
修正後排名：1 Support PoC（本 offer）、2 Workflow/Document（以規則/腳本為主，必要時才加 AI；可作為第二個 offer 或客戶擴充）、3 RAG、4 Assessment（併入本 offer 的診斷）、5 Eval（作為本 offer 的評估附加交付）。
