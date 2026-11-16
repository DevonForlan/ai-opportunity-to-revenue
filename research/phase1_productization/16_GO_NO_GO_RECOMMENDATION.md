# 16 Go / No-Go Recommendation（Phase 1A）

## 判定：**CONDITIONAL GO — 進入「Pilot 驗證」，不進入 product build，也不再擴大 research**

## 對 Issue #4 §13 的 19 問

| # | 問題 | 回答（標籤） |
|---|---|---|
| 1 | 值得商品化嗎？ | **有條件**。有價格錨點與可標準化範圍，但**MongoDB 專屬的付費需求證據為 0**（NEW EVIDENCE） |
| 2 | 第一個產品 | **MongoDB Production Risk Assessment（read-only：backup/restore + replication/oplog + upgrade/EOL）**（INFERENCE，見 07）；備選入口：Upgrade/EOL Readiness |
| 3 | 為何不是其他 | 三類最大 pain 合計 122/281；獨立顧問未見單獨產品化；read-only 可行；效能/索引被低價 gig 擠壓；Kafka 付費者不明；pipeline 與 MongoDB 專長關聯弱 |
| 4 | Demand evidence 強度 | **Pain：強（281 列，level C）；購買：MongoDB 專屬弱到無；泛 DB 健檢購買（台灣公部門）：強但非 MongoDB 且非個人規模**（VERIFIED 分項） |
| 5 | ICP | 無專職 DBA 的中小型 MongoDB 團隊，有近期事故／升級／EOL／稽核觸發（INFERENCE） |
| 6 | 客戶買的 outcome | 降低明確風險（能否還原、failover 是否安全、版本是否過期），不是「Health Check」名稱 |
| 7 | Scope | 見 07 P1；診斷＋roadmap，remediation 另售 |
| 8 | 可遠端交付 | 可（read-only 證據；或客戶自行執行唯讀腳本回傳）。台灣公部門案是否可遠端 UNKNOWN |
| 9 | 最小可信交付物 | 摘要、Finding Register（含 evidence_refs）、拓撲/設定快照、roadmap、證據包、readout（見 08） |
| 10 | 可 script / AI 輔助 | inventory、收集、config 驗證、replication/oplog、引用＝deterministic/rule；log 摘要、query 分析、建議、報告＝LLM 輔助且須覆核；**比例 UNKNOWN（未實測）**（見 09） |
| 11 | 一定要資深人工 | critical/high finding、升級相容性判斷、severity、客戶 readout、任何 write 操作 |
| 12 | 個人 trust signals | 見 10：樣本中 solo 賣家**幾乎無**認證/客戶案例（0/8 頁），僅少數有 sample report 與公開價格 → 可作差異化：公開範例（脫敏）報告、公開技術內容、固定價、read-only 保證、paid triage 折抵。**哪些足以讓客戶購買＝UNKNOWN**（無成交資料） |
| 13 | Price clusters | 獨立/小型固定價 audit US$1,200–5,000；Percona US$11,400 起；marketplace US$90–399（見 11） |
| 14 | 個人實際成交價 | **UNKNOWN** |
| 15 | 優先測試的通路 | **暖關係／既有專業網絡直接外聯（人工）＋ Contra 個人檔案（有官方 0% 佣金、180+ 國、含 USDC/PayPal/銀行）**；**避免**群發/自動化外聯與免費試用（Contra 條款禁止；LinkedIn、HN、GitHub 亦限制自動化）。Upwork 競爭與預算偏低（樣本中位 105 bids；MongoDB 貼文微預算） |
| 16 | 台灣收款可行 | **部分**：Stripe Global Payouts（TWD）、Polar 列台灣；Wise/PayPal 部分驗證；央行申報門檻 NT$50 萬（VERIFIED）；Contra 台灣是否被明列 UNKNOWN |
| 17 | 主要法務/稅務/平台限制 | 所得類別與是否需行號（UNKNOWN，需會計師）；兼職/NDA（UNKNOWN）；平台禁止自動化外聯；客戶資料不得進 Claude（公司政策） |
| 18 | 下一步 | **Pilot（人工驗證付費意願）+ 少量工具實測**；不做 product build；不再大規模 research |
| 19 | 最終判斷 | **CONDITIONAL GO** |

## 為什麼不是 GO
- MongoDB 專屬購買證據 0；pain 文 0 則表明預算；freelance MongoDB 需求稀薄且低價（USD 2–8/hr、固定 US$70–100，C 級）。
- 可觀察的價格皆為 list price；個人成交價未知。

## 為什麼不是 NO-GO
- 供給端確有人公開賣固定價 read-only audit（US$1,200–$5,000 群聚，含 solo 與 boutique），代表此產品形態在市場上存在。
- Pain 量大且集中在可標準化且可 read-only 評估的主題。
- 台灣公部門持續採購資料庫健檢/效能/升級服務（購買證據 A 級，雖非 MongoDB）。
- 獨立顧問在此範圍缺口明顯（樣本內推論）。

## Conditions（成為 GO 的條件，皆為二元、由人驗證）
- C1：取得雇主/稅務/收款確認（Day 0）。
- C2：至少 1 位真實的潛在客戶（暖關係）對固定範圍的 read-only assessment 給出書面付費意願或 paid pilot。
- C3：在本機/測試 MongoDB 上以腳本產出一份脫敏範例 Finding Register，並記錄人工覆核時數（才能計算自動化比例與時薪）。
- C4（選擇性分支）：讀 PCC 標案文件確認個人/遠端可否參與；若可，評估將產品由「MongoDB」放寬為「資料庫（含 Oracle/SQL Server）健檢」是否值得（需另研究，非本輪）。

## Kill criteria（Pilot 階段）
- 暖關係外聯後無任何付費意願（人數與期限由使用者定）；
- 範例報告實測顯示人工覆核時數過高，有效時薪低於使用者底線；
- 雇主政策／稅務／收款任一無法解決；
- 客戶資料政策使 LLM 步驟無法使用且腳本化不足以降低工時。

## Recommended next action（最小下一步）
1. 你確認雇主兼職政策與稅務／收款路線（C1）。
2. 我可在授權下做 C3：寫 read-only 證據收集腳本（只在 throwaway 本機實例測試，不碰任何真實 DB）。
3. 你決定是否要我讀 3–5 件 PCC 標案文件（C4），純讀取。
4. 外聯（C2）一律由你本人決定與送出；我只準備素材。
