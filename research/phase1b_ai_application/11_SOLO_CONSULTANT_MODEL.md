# 11 獨立 / 個人 AI 顧問銷售模型分析

## 方法與限制

- **樣本**:`04_AI_COMPETITOR_DATASET_solo.csv` 共 53 列;其中 **39 列為 independent 且實際讀過頁面(n=39)**,另 4 列為 independent 但只有摘要/403(不入下方百分比),10 列為 boutique/小團隊(僅作對照)。
- **以下統計為我對這 39 列逐列手動計數**,為描述性次數,不是市場比例。樣本由搜尋關鍵字(audit、assessment、fixed price、fractional)挑出,**必然偏向會做 SEO、且以 audit 為賣點的賣家**;沒有隨機抽樣。
- **全部是 provider_marketing**:自家網站、Contra/PeoplePerHour/ComeUp/Zapier 目錄、n8n/Make/Ragic 社群貼文。**沒有任何 purchase 證據**。因此:**無法得出任何 win rate、轉換率、成交量或營收**;本檔也不做這類推論。標價 != 成交價。
- n8n 社群貼文僅 2-3 則回覆、約 30-110 瀏覽(Discourse API 數字),不能當作需求證據。
- 標籤:BASELINE = Phase 0/1A 既有結論;NEW EVIDENCE = 本批頁面直接讀到;INFERENCE = 我的推論。
- 這 39 列中有 1 列(jxnl.github.io)已停止接案,納入是因為它示範「公開寫作品牌 -> 退出顧問」,計入分母。
- 資料集中 Taiwan 賣家僅 4 列,且全部沒有公開價格,台灣結論的證據力最弱。

## 1. 銷售模型分類(n=39,可重疊)

| 模型 | 次數 | 代表(id) | 標籤 |
|---|---|---|---|
| 付費 audit / diagnostic / review 當入口(assessment-first) | 18 | AS001, AS002, AS005, AS006, AS008, AS009, AS012, AS013, AS014, AS016-AS019, AS020, AS025, AS034, AS035, AS036 | NEW EVIDENCE |
| 免費 audit / 免費小樣本當 lead magnet | 2 | AS030(free workflow audit)、AS025(免費 3 個發現,再收 USD 45) | NEW EVIDENCE |
| 固定價 sprint / POC(含 audit 後接 build) | 約 9 | AS001, AS005, AS009, AS011, AS012, AS014, AS015, AS019, AS036 | NEW EVIDENCE |
| 直接賣 implementation(單一 workflow / chatbot 微型套餐) | 約 12 | AS003, AS021-AS024, AS026-AS029, AS037-AS039 | NEW EVIDENCE |
| 月費 retainer / fractional 席位 | 約 15 | AS001, AS002, AS003, AS004, AS007, AS011, AS014, AS025, AS031, AS032, AS036 等 | NEW EVIDENCE |
| 明確拒絕 retainer(單次交付) | 2 | AS008(Zoll: no scoping retainer)、AS030(Apex: No retainers) | NEW EVIDENCE |

INFERENCE:賣家敘事多為「audit -> sprint -> retainer」階梯,但本資料無法證明買家真的依此階梯付款。

## 2. 價格錨點(僅自述標價,n=22 列有任何公開價格)

- **Audit / 診斷入口價**(非離群值 10 個):USD 45(論壇新帳號)、75(30 分鐘)、150、350、499、750、997、1,500+、2,500-5,000、4,500。中位數落在約 USD 500-750 之間,但**此為標價樣本中位數,不是市場價**。離群:Paul Okhrem(AS002)audit USD 80,000,屬企業/高階諮詢定位,不可作 SMB 獨立顧問參照。
- **單一 workflow / chatbot 微型套餐**:USD 60(單一缺陷修正)、USD 250(RAG chatbot,PeoplePerHour)、EUR 39(ComeUp 新帳號,0 筆銷售);forum 上的一個固定價範例為 USD 1,500/5 天(只有摘要,頁面已 404,PARTIALLY VERIFIED)。
- **Sprint**:USD 2,500+(Graham Mann)、USD 7,500-12,500(dialedops)、USD 9,500(Outright Mental);boutique 對照:Penrose USD 1,800 起、Jester USD 3,000-7,500。
- **Retainer / fractional**:USD 3,400/月(AS003)、4,000(AS004)、5,000 與 9,000(AS007)、6,000 起(AS014)、2,500 與 5,000(AS011);另有 USD 99/月的小型「watch」(AS025)。boutique 對照 Vantage Point 以 8/16/32 小時計為 USD 1,800/3,400/6,400。
- **台灣**:4 列獨立賣家 0 個公開 NT$ 價格。台灣價格區間只有 2 個二手來源(Shareuhack 指南,頁面自述由 AI agents 撰寫、未逐篇人工審核;PRO360 價格頁,為 snippet),**可信度低,不得當報價依據**。BASELINE(Phase 1A 12/13)已涵蓋台灣收款/稅務,此處不重複。

## 3. 信任訊號頻率(n=39 獨立賣家)

| 信任訊號 | 次數 | 說明 |
|---|---|---|
| 公開任何價格 | 22 | 17 列沒有任何價格(含 Taiwan 4 列) |
| 免費 intro / discovery / scoping call | 約 10 | 最普遍的低摩擦入口 |
| 案例或作品展示(含自述、匿名、自家 demo) | 約 19 | 其中第三方可歸因的命名客戶僅約 5 列(AS011, AS031, AS036, AS020, AS021) |
| 帶全文的客戶 testimonial | 約 2-3 | AS011(10 則)、AS031(2 則)、AS019(1 則,屬另一產品) |
| 平台評分/評價數 | 3 | PRO360 5.0/12 則(AS040)、PeoplePerHour 5.0(數量 UNKNOWN)、Make/Zapier 自述 5 星 |
| 廠商 partner / 認證徽章 | 約 4 | Make Level 5 + Zapier(AS020)、Zapier Silver partner x2(AS021, AS022)、Google ads 認證(AS040,非 AI 專屬) |
| 公開寫作 / GitHub / 開源 / 免費工具當信任來源 | 約 11 | AS010, AS014, AS018, AS025, AS031-AS034, AS035, AS036, AS008 |
| 已發布樣本交付物 | 2 | AS025(GitHub 上的樣本 audit)、AS035(技術文章) |
| 保證 / 退款 | 4 | Zoll「找不到 5 小時/週就不收費」、AI Architects(含 month-two-free)、Mike「終身維護」、PeoplePerHour 平台 money-back |
| audit 費用抵扣後續專案 | 4 | AS001, AS018, AS020, AS035(AS017 在 FAQ 提問,答案未顯示) |
| NDA 可提供 | 約 6 | |
| 交付後 7-30 天支援 | 約 7 | |

重點(INFERENCE):多數獨立賣家**沒有**可第三方驗證的客戶證據。最常見的是「免費通話 + 自述案例」。有 testimonial 或命名客戶的賣家都有長期內容/社群分發(例如 AS011 自述 69,000+ 追隨者、AS031 有多年作品與文章),不是「剛開業就有」。

## 4. 無品牌獨立顧問的最小可行組合(INFERENCE,來自本樣本的共同點與缺口)

本樣本中**幾乎每個**較完整的賣家都具備以下項目;缺任一項的賣家(新論壇帳號、0 銷售)都呈現沒有證據的狀態:

1. 一個**單一、命名、固定範圍**的入口(audit 或單一 workflow),附明確交付物清單(報告頁數、通話長度、交付天數)。
2. **明確的 scope 邊界**(AS006 最清楚:不含 production app、live integration、帳號存取)與書面驗收。
3. 一個可公開查證的**樣本交付物或作品**(樣本 audit、GitHub、技術文章)。本樣本只有 2 列做到,代表是差異化空缺,但我**沒有**證據顯示它能提高成交。
4. 一個低摩擦的聯繫路徑(免費 15-30 分鐘通話,或免費小樣本)。
5. 所有權/資料條款(客戶擁有程式碼與文件、NDA)。
6. 沒有客戶時的誠實做法也存在:AS029 明說「沒有 reference customers,首案可成本價」;AS015(dialedops)用 USD 7,500 vs 12,500 的 design-partner 折扣換 testimonial 與 case study。這是**賣家的做法**,不是已驗證有效。

台灣獨立賣家(AS037-AS040)目前連上述 1-3 都沒有公開,故針對台灣 SME 市場,**尚無可借鏡的公開成功樣板**(UNKNOWN,非「不存在」)。

## 5. 免費 vs 付費 discovery

- 免費:免費 call(約 10)、免費小樣本(AS025)、免費 audit 工具/掃描器(AS009, AS018)。boutique 對照:免費 workflow plan(Main and Machine)。
- 付費:audit 18 列,價格從 USD 45 到 5,000(+離群值)。其中 4 列明說可抵扣後續專案。
- INFERENCE(未驗證):免費通話解決「信任」,付費 audit 解決「範圍與認真度」;但本資料沒有任何轉換數字,**不能說哪個比較有效**。

## 6. Retainer 模式

- 型態:(a) 固定小時包(AS001 約 4/6-8/16 小時、AS004 40 小時、Penrose 5/15/30 小時);(b) 每週固定天數 fractional(AS032、AS036);(c) 無限制請求型訂閱(AS003);(d) 小額 monitoring(AS025)。
- 條款常見:3 個月最低、30 天通知取消、未用小時不 rollover(AS001, AS004, AS011)。
- 與 sprint 的銜接:多數把 retainer 放在 audit/sprint 之後(AS001, AS014, AS031 都寫得很明確)。
- 兩位賣家反向定位為「不要 retainer」(AS008, AS030),可能對應客戶對綁約的抗拒;這只是定位選擇,**無需求證據**。

## 7. 對 Phase 1B 決策的含意(INFERENCE)

1. 供給端證據顯示「AI audit / assessment 當入口」已經**擁擠且低價化**(USD 45-1,000 的入口並不少),單靠 audit 難以差異化。
2. 沒有品牌的新賣家若要像本樣本中較完整者那樣被信任,需要累積公開證據(樣本交付物、作品、命名客戶)。這是時間成本,不是技術成本。
3. 資料庫/MongoDB 相關差異化:本批 39 個獨立賣家中,僅 AS036(data platform 為主)與 AS031(BigQuery/資料問答)明顯以資料為賣點;**沒有看到以 MongoDB 為賣點的獨立 AI 賣家**。這只代表本搜尋未找到,不代表市場空缺,也不構成提高 MongoDB 排名的理由(避免能力偏誤)。
4. 需求面(買方是否付費)必須由其他 Phase 1B 檔案(AI_DEMAND、AI_FREELANCE)驗證;本檔不能單獨支持任何「值得產品化」的結論。

## 附:未納入或失敗項目

- Upwork 3 頁、PeoplePerHour 其餘、Fiverr 多數 403 或無法取得;僅保留 2 筆 Upwork 摘要列。
- raj.it.com(DNS 失敗)、manta-ai.pages.dev(DNS 失敗)、steazysolutions(施工中頁面)、wearegabba(404)、Tasker 價格頁(header overflow)未成列。
- Aurora TIC(醫藥合規 audit)與 getwidget 等非 AI 應用顧問或較大代理商未納入。
