# 15 Gaps and Unknowns

## A. 證據缺口（會影響決策）
1. **MongoDB 專屬購買證據 = 0**：PCC 47 筆得標無一筆被證實為 MongoDB；UK 兩筆為 Atlas 訂閱；281 則 pain 文無人表明預算或要付費找顧問。
2. **個人顧問成交價 UNKNOWN**；list price 僅 provider 自述，且 22/39 獨立賣家列來自 search snippet。
3. **Upwork / Fiverr / Reddit / Contra 登入牆**：官方條款、費率、Taiwan eligibility 多為 UNVERIFIED；Upwork 23 列 freelance 樣本僅 snippet。
4. **Freelance 樣本時間窗**：Freelancer API 只回 active 專案（約 7 天，2026-11-09～16），未達 60–90 天窗；預算為平台級距。
5. **台灣民間市場**：104、1111、Yes123、CakeResume、Tasker 無可驗證列；PRO360 僅 4 列且為小案。
6. **PCC 標案可否由個人/遠端承接**：tender 文件未讀；廠商資格（通常需公司登記）UNKNOWN。
7. **沒有 Percona 公開範例報告**（NEW EVIDENCE，負面）；Mydbops 範例報告需填表未讀。
8. 自動化比例全部 UNKNOWN；未做本機實測（Docker 未啟動、無 mongod/mongosh）。
9. 各指令最小權限角色多為 UNVERIFIED（官方 built-in roles 表格未逐項抽取）。
10. 平台自動化條款：Upwork/Fiverr/Reddit 官方條款未取得；已讀者（Contra、Freelancer §33、LinkedIn §8.2、HN、GitHub）皆限制自動化/爬取。
11. 稅務：服務在台執行的所得類別、零稅率是否適用遠端評估、是否須行號登記 → UNKNOWN（需會計師）；健保署補充保費 2.11%/NT$20,000 僅來自 search 摘要。
12. 個人僱傭合約（兼職/利益衝突/NDA）：未見，UNKNOWN。
13. Pain 資料偏差：Reddit 0 列；MongoDB 論壇 429 限流致召回不全；Atlas cost 11 列來自同一 HN thread。
14. MongoDB / Percona partner 計畫個人可否加入：UNKNOWN。
15. 公司政策：WebComm 禁止客戶資料/個資進 Claude；LLM 輔助步驟須只處理去識別化 metadata。

## B. 資料品質聲明
- 多數 provider 頁面由 WebFetch（小模型摘要）讀取，非逐字文本；引用條款與日期需人工對照原頁。
- Pain 資料皆 level C，只能視為訊號。
- 所有 `productized_mapping`、`category=` 為分析者標註（INFERENCE）。

## C. 最能縮小不確定性的下一步（見 16）
1. 讀 3–5 件 PCC 相關標案文件（資格、是否可遠端、是否限公司）。
2. 以真實的 read-only 證據收集腳本在一個本機/測試 MongoDB 上做實測，填入自動化比例。
3. 取得雇主政策、稅務與收款確認。
4. 以 paid-pilot 方式（對暖關係，非群發）驗證有無人付費。
