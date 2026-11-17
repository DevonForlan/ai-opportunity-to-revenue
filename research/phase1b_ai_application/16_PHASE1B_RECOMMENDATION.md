> ⚠️ **PHASE 2 審計修正（2026-11-17）**：本檔的排名與若干計數已被 `research/phase2_validation/01_PHASE1B_DECISION_AUDIT.md` 修正（purchase 126 筆有 50% 被誤分類；Workflow 的 20 筆 purchase 為 RPA、非 AI；Internal assistant 33→4；Assessment 7→4；「個人可及規模」論證被削弱）。**下列內容保留供追溯，不再作為決策依據。**

# 16 Phase 1B Recommendation

## 判定：**CONDITIONAL GO — 先做「測試獲客 + 小型 pilot」；不做 product build、不放棄、不再做大規模 research**

標籤：BASELINE / NEW EVIDENCE / INFERENCE。

## Issue #6 §17 的 17 問

| # | 問題 | 回答 |
|---|---|---|
| 1 | Top 5 | ① AI Automation Assessment（assessment-first，折抵 PoC）② Support/Service Automation ③ Workflow Automation（含 Document automation）④ RAG/Knowledge Assistant ⑤ AI Eval/Guardrail/Reliability Review（見 08） |
| 2 | 第一名為何勝出 | 唯一同時具備「固定範圍、遠端、單人可交付、資料存取負擔低」與「購買證據落在個人可及規模」的候選：PCC 105 筆得標中 31 筆 ≤TWD 1.5M，assessment/PoC 類含 TWD 0.85–1.48M；供給端 19/43 公司以 assessment 為主服務、3 家折抵建置費；PRO360 AI 顧問需求為評估形狀。**這是「結構」勝出，不是「已證明有人付費給個人」**（INFERENCE） |
| 3 | Buyer / purchase 證據強度 | Pain/hiring/freelance 需求廣（295 + 137 列，但多為 C 級或摘要）；**purchase 126 列全為公部門**；**私人買家購買證據 = 0**；個人可否承接公部門案 UNKNOWN |
| 4 | 最適 ICP | 10–200 人、有明確重複性人工流程（客服、文件、名單、報表）但無 AI 工程師的 SMB（INFERENCE）；次選為需做 PoC/可行性研究的法人／公部門單位（資格 UNKNOWN） |
| 5 | 客戶真正買的 outcome | **流程結果**（減少人工處理、可靠且可稽核、帶人工轉接），不是「AI」；buyer 反覆要求錯誤處理與可靠性（155 列 pain 觀察，C 級） |
| 6 | Assessment-first 或 implementation-first | **需求端是 implementation 形狀**（市集貼文與公部門得標多為「建置某流程」：得標 63/105 為實作類、11 為評估類，依標題推論）；**供給端以 assessment 當入口**（公司 19/43；solo 約 18/39）。→ 建議「**以 assessment 作銷售結構、以固定範圍 PoC/建置作營收**」，費用折抵（INFERENCE） |
| 7 | 最可行的固定 scope / solo / remote | Assessment、Eval/Guardrail review、單一流程的 workflow/doc automation PoC |
| 8 | 最易 AI-assisted delivery | Discovery 整理、候選排序、文件/spec 生成、測試案例、eval 集建立；**比例 UNKNOWN**（見 10；n=1 實驗） |
| 9 | 人工需求高 | 需求訪談與信任建立、架構與風險判斷、客戶資料處理、驗收簽核、上線與維運 |
| 10 | 競爭/商品化過高 | 低價 n8n/Make 建置（Freelancer 投標中位 125）、入口審計（solo US$45–5,000）、一般 chatbot；Microsoft Copilot readiness 單一生態擁擠 |
| 11 | 與 Data/MongoDB/Kafka 結合後的差異化 | **無證據**：AI+DB 買家證據 = 0（PCC MongoDB 僅 1 筆 2022 訓練課；Freelancer 5 件 MongoDB 貼文無向量/RAG；pgvector/Elasticsearch/Kafka/Text-to-SQL 標案標題 0）→ 不加分；僅可作 ai-ready-data/assessment 的同分 tie-breaker（見 14） |
| 12 | Price clusters | solo 入口審計 US$45–5,000（asking，中位約 500–750）；boutique 評估 US$3.5k–12.5k；n8n/Make 建置 agency US$3k–10k、solo US$500–3,000、市集 US$130–1,450；retainer solo US$1.8k–9k/月；台灣公部門得標中位 TWD 3.68M（見 12） |
| 13 | 個人實際成交價是否足夠 | **不足，UNKNOWN** |
| 14 | 最適 acquisition channel | **既有專業網絡／台灣 B2B 的人工直接接觸 + 以流程結果命名的個人網站/技術內容**；Contra 可作檔案但需遵守條款（禁自動化外聯、免費試用服務受限）。**避免**市集為主通路（預算低、投標多）與自動化外聯。AWS Marketplace 付費賣家不含台灣；n8n Experts 封閉且地區不含台灣；Anthropic/OpenAI 夥伴計畫個人資格 UNKNOWN（見 13） |
| 15 | 台灣跨境收款 | 承襲 Phase 1A：部分可行（Stripe Global Payouts、Polar 列台灣；Wise/PayPal 部分驗證；央行申報門檻 NT$50 萬）；AI 服務稅務與 IP 歸屬 UNKNOWN（需專業意見） |
| 16 | 下一步 | **Test acquisition + build pilot（小）**；非 product build、非 abandon、非繼續擴大 research |
| 17 | 最終判斷 | **CONDITIONAL GO** |

## 為什麼不是 GO
- 私人買家購買證據 0；全部購買證據為公部門且多為限制性招標（47/96 僅 1 家投標）；個人可否承接 UNKNOWN。
- 市集預算極低、投標多；solo 入口審計擁擠且便宜。
- 個人成交價、成交率、自動化槓桿皆 UNKNOWN。

## 為什麼不是 NO-GO / 放棄
- 台灣與美國公部門確實持續購買 AI 客服、知識庫/RAG、流程自動化與 PoC，個人規模（≤TWD 1.5M）案件佔 31/105。
- 供給端有大量固定範圍、assessment-first 並折抵後續建置的提供者，代表此銷售結構存在。
- 需求描述以「流程結果」為主，適合以固定範圍 PoC 交付，且有高 AI 輔助交付潛力（待實測）。

## 相對 Phase 1A
`NEW EVIDENCE` 顯示 AI 應用的購買證據（126 列）多於 MongoDB 專屬（0 列），**但兩者證據都集中在公部門與同一類來源，不可推論私人市場**。MongoDB 降為次要能力；Phase 1A 的 read-only Risk Assessment 形態保留為 assessment 結構範本。Phase 1A 的結論不被刪除。

## Conditions（變 GO 的條件；二元、由人驗證）
- C1：雇主兼職／NDA、稅務、收款路線確認。
- C2：至少 1 位真實的暖關係潛在客戶對**固定範圍 assessment/PoC** 給出書面付費意願（外聯由使用者本人決定與送出）。
- C3：以公開或合成資料完成一次完整 pilot 交付並記錄人工時數，才能算自動化槓桿與有效時薪。
- C4：讀 3–5 件 PCC 標案文件確認個人/遠端/轉包資格（決定是否值得追公部門市場）。
- C5：客戶資料處理方案（去識別化、不將客戶資料餵 Claude，符合公司政策）。

## Kill criteria
- 暖關係外聯後無付費意願（人數與期限由使用者定）；
- pilot 實測有效時薪低於使用者底線，或自動化槓桿不顯著；
- 雇主政策／稅務／收款任一無法解決；
- 客戶資料政策使 LLM 步驟無法使用且腳本化不足；
- 公部門案經文件確認個人完全不可參與，且私人市場仍無人付費。

## Recommended next step
1. 你確認雇主兼職政策、稅務與收款（C1）。
2. 授權後我可用**公開/合成資料**建立一套 pilot 交付範本（Opportunity Map、Candidate Register、PoC 規格、eval 集），記錄人工時數（C3）。
3. （選擇）讓我讀 3–5 件 PCC 標案文件（C4，純讀取）。
4. 任何對外聯絡、proposal、合約、付款、開帳號、接受條款，都由你本人決定與送出；我只準備素材。
