# 04 獨立顧問 / 小型工作室 AI 自動化「已交付案例」證據(Phase 2)

標籤:BASELINE = 先前 Phase 0/1A/1B 結論;NEW EVIDENCE = 本輪頁面直接讀到;INFERENCE = 我的推論。

## 方法與限制(先讀)

- **產出**:`04_SOLO_SUCCESS_CASES.csv` 共 **39 列**(SC001-SC039,SOLO_CASES schema),來源索引 `_sources/solo_cases.csv`(34 列,含 4 筆「未採用/失敗」)。達成目標 >=25,但品質不均,見下。
- **驗證分布**:VERIFIED 25 / PARTIALLY VERIFIED 13 / UNVERIFIED 1。證據等級:A 0、B 21、C 18。**沒有任何一列是等級 A**(沒有合約、發票、官方紀錄)。
- **規模分布(我逐列標註)**:明示 solo 或 <=9 人 21 列(含 1 列「likely solo」SC037);規模 UNKNOWN 8 列;**Clutch 上標示 10-49 人的 10 列(Axe Automation 8、Streamline Agency 2)超出 <=15 人範圍**,僅保留作為「客戶自述」對照,不計入 <=15 人結論。
- **台灣案例 0 列**。中文搜尋只得到廠商行銷與教學文,沒有可驗證的個人顧問台灣案例。台灣結論 = UNKNOWN。
- **「client-reported」嚴格定義**:客戶本人署名/以客戶身分在第三方平台(Clutch)或客戶自己的話被引用。39 列中 21 列有某種客戶自述(16 列 Clutch、3 列 Kevin Leary 站內 testimonial、A2B 1 列、n8n.io 代管案例 1 列),**其餘 18 列只有提供者自述**。數字多為提供者估算。
- **被我排除的**:terms.law 的 5 個客戶案例(頁面自述為 illustrative composites,不是真實交付)、Medium/TDS(403)、n8n 論壇徵才貼(404)、dgmh10uk dev.to(404)。racprojects Notion 頁 WebFetch 無法渲染,僅有搜尋摘要,標 UNVERIFIED。
- **偏誤**:案例由搜尋引擎抓到;會公開案例的賣家本來就是會做行銷的賣家。**不能得出成交率、轉換率或成功率**,本檔也不估計。價格欄中的 Clutch 價格是評論者勾選的「區間」,不是發票。
- 價格/金額一律標示來源是 client band、provider 自述還是 offer list。Provider list price != price paid(沿用 BASELINE 規則)。
- 本檔已用 Clutch、廠商頁面、社群貼文等「公開頁面」,**沒有**聯絡任何人、沒有登入。Upwork/Fiverr/PeoplePerHour 評價頁多為 403 或需登入,**未取得**(列為限制)。

## 1. 案例總覽(依證據強度分組)

**A. 第三方平台客戶評論(Clutch,共 16 列;client-reported)**

| id | 提供者(規模) | 客戶類型 | 範圍 | Clutch 價格區間 | 客戶自述結果 |
|---|---|---|---|---|---|
| SC001 | n8n Lab(2-9 人) | UK 數位代理商(服務保險客戶) | Claude+n8n PDF 處理 | Confidential | 準確率 95%、每週省 15+ 小時、3 天變當日(進行中,2026-03 起) |
| SC002 | n8n Lab | 塞爾維亞 GTM 公司 | RevOps/自動化基礎建設 | USD 10k-49,999 | 每日合格 leads 約 7 變 24(2025-11 至 2026-01) |
| SC003 | n8n Lab | B2B SaaS GTM(11-50 人) | SEO 營運 AI 流程 | Confidential | 定性:報表時間減少 |
| SC004 | n8n Lab | 行銷代理(1-10 人) | n8n onboarding/報表/CRM | < USD 10k | 人工作業減 40-60%、onboarding 由數天變數小時 |
| SC005 | n8n Lab | 拍賣/汽車公司(51-200 人) | outbound/lead qualification | Confidential | 準時交付,無數字 |
| SC006 | n8n Lab | 短租軟體公司(51-200 人) | AI 語音 bot | 10k-50k 或 50k-199k(評論自相矛盾) | 評論者歸因約 10% 成長 |
| SC007-SC014 | Axe Automation(**10-49 人,超出範圍**) | 8 個客戶(保險、律助、行銷、地產、製造等) | email 分類、客戶 intake、onboarding、chatbot、資料擷取等 | 6 列 < USD 10k;1 列 10k-49,999;1 列 50k-199,999;(SC012 未揭露) | SC010:onboarding 約 24 小時變數秒;其餘定性。**SC008 為 1.0 負評**(無可用成品、延遲、無 QA) |
| SC015-SC016 | Streamline Agency(**10-49 人,超出範圍**) | NY IT 公司、SD 行銷代理 | AI agents/MCP;n8n 擴充 Zapier | Confidential | 1,500+ 面試、5 人錄取;每週省 1-2 小時(進行中) |

**B. 具名客戶 + 提供者案例頁(client quote 在提供者站內或廠商站)**

| id | 提供者 | 具名客戶 | 範圍 | 價格 | 結果(誰報告) |
|---|---|---|---|---|---|
| SC017 | Kevin Leary(solo) | Northstar Travel Group(約 500 人) | BigQuery 倉儲 + OpenAI 問資料 | UNKNOWN | client:每日使用、"night and day"(無數字);provider:歸因 98%、省 20-40 小時/月 |
| SC018 | Kevin Leary | Honeyfund(約 30 人) | web/SEO + AI metadata 工具 | UNKNOWN | client:organic 流量「明顯」上升;provider:平均排名 18.5 到 8.6 |
| SC019 | Kevin Leary | CPC Scientific(50 人) | 基礎建設 + AI lead 分類 | UNKNOWN | client 只談主機遷移;provider:頻寬 -90%、每月省 5-10 業務小時(估) |
| SC020 | Kevin Leary | Bastille Networks | AI visibility tracker 外掛 | UNKNOWN | 無 client 數字;provider 45% share of voice |
| SC021 | The AI Architects(solo) | Exam Centre Birmingham | Claude Code 建置成績歸檔系統 | UNKNOWN(offer 價:build 起價 USD 10,000) | provider:每份約省 5 小時 |
| SC022 | System AI(規模 UNKNOWN,n8n.io 代管) | The Srama Group | WhatsApp 語音助理 + Zoho CRM | UNKNOWN | client 營運經理述:得到地產業獎;行政時間 4-5 分變 10-20 秒 |
| SC023 | Khairul Muhtadin(solo) | Highlane Partners | 盡調文件 RAG,2 天 | UNKNOWN | 無客戶自述 |
| SC024 | A2B AI Technologies(規模 UNKNOWN) | 一位自由工作者 SEO 顧問 | SEO 報表自動化 | UNKNOWN | client 引述:過去需 2-3 天(頁面自相矛盾) |
| SC039 | robertwinters(solo) | KNVB、Lepaya、RTL | 資料平台為主,後期加 agentic/Claude Code | UNKNOWN | 無 |

**C. audit/assessment 再 build(提供者自述,多為匿名)**:SC025 Gigabit(規模 UNKNOWN)、SC026 Innovatrix、SC027 GrossiWeb(非 solo)、SC028 4Spot、SC029 racprojects(UNVERIFIED)、SC033 prem_patel(僅 offer)、SC038 techconcepts(solo,3 個匿名微案例)。

**D. 其他提供者自述/社群貼文**:SC030 大學課程製作(USD 5,000)、SC031 Contra 行銷代理平台(價格自相矛盾 USD 54,000 vs 4,000,**不可用**)、SC032 Zendesk 工單、SC034 鋁業、SC035 Skool 外燴 USD 5,000(內文被截斷)、SC036 Skool 法律客戶「約 USD 100K」(自述、無法驗證)、SC037 Dubai 發票 agent。

## 2. 回答:沒有大品牌背書的獨立顧問,什麼成交結構有證據?(計數僅來自本檔 39 列)

### 2.1 Offer 結構(NEW EVIDENCE,計數)

- **直接做 implementation(標 direct_build)**:32 / 39 列。其中多為「單一工作流/一個子系統」,不是整套平台。
- **audit/assessment 為入口(標 audit_first)**:8 / 39 列。細分:
  - 1 列把 assessment 當獨立計價項目併入同一專案(SC025:USD 6,000 + build USD 38,000 + USD 2,500/月;**提供者自述、規模 UNKNOWN、客戶匿名**);
  - 3 列把「審視一週」放在固定專案內(SC026、SC027、SC028),並非獨立銷售;
  - 2 列只是 offer 文字,沒有案例顯示轉換(SC033、SC038;SC033 的「audit 可抵扣」只是 offer 文字,CSV 的 audit_credited_to_build 標籤共 2 列,即 SC029 未驗證 + SC033 offer-only);
  - 1 列是失敗案例(SC008,Axe 評論者 1.0 分);
  - 1 列聲稱 audit 費用抵扣後續 USD 22K 專案(SC029),**UNVERIFIED**。
- **「audit 費用抵扣 build」已交付的證據:已驗證 0 列;未驗證 1 列(SC029)**。這是對 BASELINE 的重要補充:BASELINE 的 4 個「抵扣」賣家(AS001/AS018/AS020/AS035)仍只是 offer,本輪沒有找到任何一個被實際走完的案例。
- **implementation-first 的實例**:SC036(客戶發需求貼文,自述在提案時同附第一個可跑的 workflow)、SC023(兩天交付超出 PoC 的 demo)、SC017-SC019(AI 附掛在既有資料/web 長期關係上)。
- **後續/進行中關係(有文字證據)**:9 列(SC001、SC006、SC010、SC013、SC015、SC016、SC018、SC039 與 SC025 的月營運費)。另有 SC030、SC022 為「客戶可能再做」的口頭意向,不計入。注意 Clutch 的「ongoing」只代表專案未結束,**不等於 retainer 合約**。

### 2.2 證明(proof)類型(計數)

- **具名客戶**:9 / 39 列。其中屬明示 solo/小型者 7 列(Leary 4、AI Architects 1、Muhtadin 1、Winters 1);其餘 2 列(System AI、A2B)規模不明。
- **客戶本人在第三方平台的評論**:16 列(全部是 Clutch;其中 <=9 人的 n8n Lab 6 列、10-49 人的 10 列)。**明示 solo 的 15 列(21 列扣掉 n8n Lab 的 6 列 2-9 人)中,第三方平台客戶評論 = 0 列**。
- **客戶引述在提供者自己網站**:Leary 3 列 + A2B 1 列;n8n.io 代管 1 列。
- **demo / 範例交付物當 proof**:2 列(SC023 demo 報告、SC036 先交第一個 workflow)。
- **GitHub/開源當 proof**:本輪 0 列(BASELINE 的 AS025/AS032 在 offer 層出現,本輪案例層沒有)。
- **平台徽章**:1 列(SC033 Make 認證)。匿名 testimonial:1 列(SC025)。
- INFERENCE:**有第三方、可歸因的客戶自述的案例,幾乎都來自 Clutch 這種「平台代客戶收評論」的機制,而不是來自 solo 個人自己的網站**。在 <=9 人樣本中,可歸因的正面評論集中在一家(n8n Lab 6 列),不是分散多家,不能視為通則。

### 2.3 範圍與票價(client band / provider 自述,不是發票)

- Clutch 區間 16 列中,**10 列有區間**:< USD 10k 共 6 列、10k-49,999 共 2 列、50k-199,999 共 1 列、1 列自相矛盾;**6 列為 Confidential/未揭露**。
- 有明確期間且結束的 Clutch 專案約 2-5 個月(SC002、003、004、005、008、009、011、014);**進行中**6 列。
- 提供者自述的金額:USD 5,000(SC030、SC035)、USD 4,500 成本(SC027)、USD 6,000 + 38,000(SC025)、INR 75,000(SC026,未換算)、USD 22K(SC029,UNVERIFIED)、約 USD 100K(SC036,自述不可驗證)。
- 提供者自述工期:2 天(SC023)、約 3.5 天(SC028)、約 4 週(SC027)、約 6 週(SC026)、8 週(SC025)。
- INFERENCE:**本樣本最常被客戶付費的範圍是「單一流程到少數流程、< USD 10k、2-3 個月內」**;>USD 10k 的案例少數,且大多不是 solo 或客戶匿名。

### 2.4 交付模式(INFERENCE,來自上列計數)

1. 有長期關係的 solo(Leary、Winters)是「AI 附掛在資料/網站/平台既有委託上」,AI 不是獨立賣點。Leary 的 38 則 testimonial 中只有 2 家客戶與 AI 有關(testimonials 頁)。這支持「先有信任、AI 後加」的路徑,**但這是我對單一賣家的觀察**。
2. 小而精(2-9 人)的 n8n Lab 以「開場通話 + 業務面框架」被評論者稱讚(評論引述),結果具體(leads、小時數)。**只有一家,不能一般化**。
3. 負評(SC008)指向 QA/測試缺口,代表「交付與驗收條款」是風險點;這是 1 筆,不是比率。
4. 價格自相矛盾、無法驗證的案例(SC031、SC036)佔 39 列中的 2 列,代表公開案例頁需要交叉檢查,不能直接當證據。

## 3. 對決策的含意

- NEW EVIDENCE:**公開可核實的「solo 客戶自述 + 價格」案例極少**。本輪 39 列中,明示 solo 者無一列同時具備「具名客戶 + 第三方平台評論 + 價格」。
- NEW EVIDENCE:audit 轉 build 的已驗證案例 = 0;implementation-first 有案例但多為提供者自述。BASELINE 的「audit-first 階梯」仍是供給端敘事。
- INFERENCE:若走 Assessment 入口,**要先備好一個可公開的樣本交付物與至少 1-2 個可歸因客戶引述**(最低門檻是 1 個平台評論或 1 則具名引述),否則與市場上多數 solo 賣家處於同一個「無第三方證據」狀態。
- INFERENCE:對台灣市場沒有任何可借鏡的公開案例(0 列);需另以台灣商業證據檔補。
- 未解:確切成交的機制(誰、何時、如何決定付款)在公開頁面幾乎不可見,屬 UNKNOWN。

## 4. 本檔 CSV 欄位用法

- `offer_structure` 與 `proof_used` 帶 `[tag]` 標籤(如 `[direct_build]`、`[audit_first]`、`[audit_credited_to_build]`、`[named_client]`、`[client_review_platform]`、`[client_quote]`),上列計數可由這兩欄重現。
- `url` 對同一 Clutch 檔案使用 `#review-N` 片段以去重;片段是我加的序號,不是 Clutch 的錨點。
- `outcome_client_reported` 以 `NONE` 開頭表示該列沒有客戶自述,提供者數字放在 notes 或該欄的「Provider-reported」字句。
