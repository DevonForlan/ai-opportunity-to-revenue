# 13 Taiwan 收款通路與稅務（跨境固定範圍技術服務）

- access date：2026-11-16
- 標籤：VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / UNKNOWN；證據等級 A/B/C；結論標 BASELINE / NEW EVIDENCE / INFERENCE。
- **聲明：本文件不是法律、稅務或財務建議。** 稅務、外匯與營業登記請洽國稅局、承辦銀行或會計師；依 WebComm 政策須人工複核，不得視為正式文件。

## 0. Method & limitations

- 工具為 WebFetch（回傳為摘要，非原文；「」內引文為摘要引述的條文短句）與 WebSearch。**只有在頁面中讀到的數字才寫入；否則 UNKNOWN。**
- 無法讀取：PayPal 商業（收款）費率頁（403/404）、NHI 官方 PDF（socket hang up，僅搜尋摘要）、中央銀行「匯入匯款分類及編號」完整附件、`費用標準` 令文原文、Wise 帳戶開立資格細頁。均標 UNVERIFIED/UNKNOWN。
- 未取得用戶雇傭契約、身分（居住者 183 天等）、客戶所在國、預期金額 → 個案判斷全為 UNKNOWN。
- 不重做 Phase 0（06 與 platforms.md S01–S44）；僅重驗或補充。
- 計數：本檔引用官方（A）頁面 15 頁（含 law.moj.gov.tw 6 條/法規、etax 3 頁、cbc 2 頁、Stripe 2、Polar 1、Wise 3、PayPal 1、Payoneer 1、Contra 1 部分重疊）；B/C 為搜尋摘要。詳 `_sources/channels_payment_tax.csv`。

## 1. 收款通路

| 通路 | Taiwan 狀態 | 費用/限制（僅讀到者） | 標籤 | 新舊 |
|---|---|---|---|---|
| **PayPal（Taiwan 個人）** | 官方 TW 費用頁（更新 2026-05-28）：提領到玉山 TWD 帳戶「no fee, if no currency conversion」；到玉山 USD 帳戶、到美國帳戶 2.50%；**付款/退款幣別轉換（含 TWD）高於基準匯率 4.00%**；提領到本地銀行的轉換 2.50%（餘額幣別非主要幣別時）；其他轉換 3.00% | **收款（商業交易）費率與提領限額：該頁指向另一頁，未讀到 → UNKNOWN**。商業帳戶費率 UNKNOWN | PARTIALLY VERIFIED | NEW EVIDENCE（補 4.00% 付款轉換；BASELINE 僅有 2.50%/3.00%） |
| **Wise** | 官方 help：USD account details 開放對「address is in a country where they can open a currency account」；**列出不可用國家名單中沒有 Taiwan**（含 UAE、Türkiye、Pakistan 等），但**頁面未明說 Taiwan 可用**，需看「Why can't I open a currency account?」。第二手（C）：kkinvesting 稱 Taiwan 居民可開並取得 USD routing/account number（UNVERIFIED） | Wise AU 費率頁（非 Taiwan）：USD wire/Swift 收款固定 **USD 6.11**，國內 USD 轉帳免費；取得帳戶資訊 22 種幣別免費。**Taiwan 適用 UNKNOWN** | PARTIALLY VERIFIED（不在排除清單）/ Taiwan 費率 UNKNOWN | NEW EVIDENCE（修正 BASELINE「UNVERIFIED、無證據」：官方排除名單無 Taiwan，但仍未證實） |
| **Payoneer** | 官方定價頁**不含 Taiwan 專頁**；本地銀行 USD 1.50 同幣別提領「Taiwan is not in the list」；其他提領「1.2%–4%」，部分國家最低費最高 20 USD 等值；marketplace 收款「Varies by marketplace」；年費 USD 29.95（12 個月累計收款 < USD 6,000 時收）；頁面稱費用「prices are estimates」 | Taiwan 實際費率：註冊後登入才顯示 → UNKNOWN | PARTIALLY VERIFIED | BASELINE 重驗一致 |
| **Contra payout** | A：180+ 國可用；排除 Russia/Iran/North Korea/Cuba/Syria；**頁面未提 Taiwan**。USDC：Ethereum gas 通常 0%，加密提領費 2%（free）/1%（Pro）；PayPal 2%；bank $0–8 + 匯差 0.4–1%（「Fees vary depending on the account type and country location」）；Payoneer 每筆上限 $3；debit card 僅美國。ToS §11.2：可對 early payout、stablecoin 收費 | 保留期/最低額 UNKNOWN；Taiwan 到帳幣別 UNKNOWN | PARTIALLY VERIFIED | BASELINE 重驗一致 |
| **Polar** | 官方：「Polar uses Stripe Connect Express to issue payouts to residents or businesses in any of the countries below」，清單含 🇹🇼 Taiwan；**頁面無任何 payout 費用資訊** | 費用/到帳幣別 UNKNOWN | VERIFIED（國家清單）/ 其餘 UNKNOWN | BASELINE 重驗一致 |
| **Stripe（自行開帳號）** | `stripe.com/global` 本次讀取：**Taiwan 未列**為可建帳國；亞洲僅 Hong Kong、India（preview）、Indonesia（preview）、Japan、Malaysia、Singapore、Thailand、UAE | — | VERIFIED（頁面未列）；實際不可開 = INFERENCE | BASELINE 重驗一致 |
| **Stripe Global Payouts**（Stripe 客戶付錢給你） | 官方 recipient countries：**Taiwan `TW`，Currencies = TWD，Private preview currencies = USD**；sender 僅 US、UK；實際方法/到帳時間/限額依 sender、recipient、幣別，見 payout-methods 頁（未讀） | 此通路由**付款方（Stripe 客戶）**啟用，非你可自行選擇 | VERIFIED | BASELINE 重驗；補充：USD 僅為 private preview |
| **國際電匯（銀行 SWIFT）** | 一般可行；銀行端手續費、中間行費：Taiwan 各銀行官方費率**本次未讀 → UNKNOWN**；Phase 0 僅有論壇個案（CTBC TWD 400/600，C） | 見 §2 外匯申報 | UNKNOWN（費用）/ PARTIALLY VERIFIED（可行） | BASELINE |
| **加密/USDC** | 平台側有（Contra）；Taiwan 出金/稅務 UNKNOWN | — | UNKNOWN | BASELINE |

**INFERENCE**：對 Taiwan 個人，目前可由官方證據支撐的「不需要額外假設」路徑只有：(a) PayPal → 玉山 TWD（付款幣別若為 USD 需面對 PayPal 轉換加成，4.00%/2.50% 為官方數字；收款手續費 UNKNOWN）；(b) 客戶若用 Stripe Global Payouts（Taiwan/TWD）；(c) 電匯。Wise USD 收款可能可行但未被官方證實。

## 2. 國際電匯 / 外匯申報（中央銀行）

**來源**：全國法規資料庫「外匯收支或交易申報辦法」（A；頁面顯示最近修正 111-12-26，修正條文自 112-01-01 施行）；中央銀行函（A，104-09-16 台央外柒字第 1040041230 號，內容為傳真交易指示，已為舊函）。

| 項目 | 官方文字（摘要引文） | 標籤 |
|---|---|---|
| 申報門檻 | 第 2 條第 2 項：「中華民國境內新臺幣五十萬元以上等值外匯收支或交易之資金所有者或需求者」應依辦法申報 | VERIFIED（條文） |
| 申報書 | 第 2 條第 3 項：依相關合約等證明文件「誠實填妥『外匯收支或交易申報書』」，經銀行業向央行申報 | VERIFIED |
| 個人每年結匯額度 | 第 4 條第 1 項第 3 款：「團體、個人每年累積結購或結售金額未超過等值五百萬美元之匯款」可填妥申報書後逕行辦理；超過者依第 6 條第 1 項須先經央行核准 | VERIFIED（條文）；是否為現行有效版 = 條文頁顯示 111 年修正，PARTIALLY VERIFIED |
| 證明文件 | 第 5 條：部分匯款須檢附「與該筆外匯收支或交易有關合約、核准函或其他證明文件」；第 8 條第 2 項：銀行保存申報書及文件「至少為五年」 | VERIFIED |
| 小額免填 | 搜尋摘要（央行附件）：結匯人每筆結匯金額未達新臺幣五十萬元等值外幣者免填申報書 | UNVERIFIED（未讀全文）|
| 大額 | 央行函（2015）：個人每筆結匯達 US$500,000 以上，須在交易前審查文件（舊函）| PARTIALLY VERIFIED（時效不明）|
| 匯入匯款分類及編號（勞務收入對應代碼）| 央行有「匯入匯款分類及編號」附件，但摘錄未顯示個人接案對應代碼 | **UNKNOWN** |
| 銀行手續費/中間行費 | 各銀行官方費率未讀 | UNKNOWN |
| 結匯 vs 留存外幣 | 申報辦法依「結匯」；留存外幣帳戶（外幣存款）的申報細節本次未查 | UNKNOWN |

## 3. 稅務（個人 vs. 公司）

### 3.1 所得來源與類別

- **所得稅法 §8(3)**（BASELINE S40）：在中華民國境內提供勞務之報酬屬境內來源；因此人在 Taiwan 為外國客戶工作的收入**可能**屬境內來源所得而非「海外所得」→ BASELINE，結論 UNKNOWN（個案）。
- **海外所得 NT$100 萬門檻**（BASELINE，etax S37/S38）：僅適用「非中華民國來源」所得；對在 Taiwan 提供服務的所得不一定適用 → **INFERENCE**：不能用此門檻判定免稅。本次未重讀。
- **所得稅法 §14（A，本次讀取）**：十類所得；第二類「執行業務所得」（「凡執行業務者之業務或演技收入，減除…折舊及修理費…」）；第十類「其他所得」（「不屬於上列各類之所得，以其收入額減除成本及必要費用後之餘額為所得額」）。**稿費**：所讀摘要未提及，歸類 **UNKNOWN**。
- 個人技術顧問/assessment 歸「執行業務所得」或「其他所得」或「營利所得」：**UNKNOWN**，需國稅局/會計師判定。etax 網路交易 Q&A（A）：低於起徵點、僅在網路銷售者，年度利潤列「營利所得」（該答覆情境為團購平台商品/服務賣家，**是否適用個人顧問為 UNKNOWN**）。
- 財政部「個人於網路發表創作或分享資訊課徵綜合所得稅作業規範」（114-12-23 發布，搜尋摘要，C/B）：歸類平台收益為執行業務所得（表演人）— **與顧問服務類比 UNKNOWN**，原文未讀。
- 費用認列：核實或「費用標準率」；114 年度費用標準令（搜尋摘要稱 財政部 115.3.27 台財稅字第 11404667891 號令，經醫師公會文件轉述，C）**原文未讀；適用於「其他專門職業及技術人員」的費用率 UNKNOWN**。

### 3.2 營業稅（對境外客戶的服務）

| 項目 | 官方文字 | 標籤 |
|---|---|---|
| 零稅率 | 營業稅法 §7(2)：「與外銷有關之勞務，或在國內提供而在國外使用之勞務」稅率為零（law.moj.gov.tw，資料截止 115-11-06）| VERIFIED |
| 證明文件 | 施行細則 §11(2)：「取得外匯結售或存入政府指定之銀行者，為政府指定外匯銀行掣發之外匯證明文件；取得外匯未經結售或存入政府指定之銀行者，為原始外匯收入款憑證影本」 | VERIFIED |
| 實務（etax 賣家頁，範例為數位遊戲）| 對海外買家屬外銷勞務，可附外匯證明或原始外匯收入款憑證影本申請零稅率；外銷勞務依「收款日銀行買入匯率」折算 | PARTIALLY VERIFIED（範例情境，非顧問服務） |
| 「在國內提供而在國外使用」是否涵蓋遠端提供給外國公司、成果在國外使用的 MongoDB assessment | 條文文字可能涵蓋；**個案適用（含 AWS/客戶資料位置、使用地認定）UNKNOWN**，需稽徵機關/會計師 | UNKNOWN（INFERENCE：可能適用）|
| 營業人稅籍登記 | §28：「營業人之總機構及其他固定營業場所，應於開始營業前…向主管稽徵機關申請稅籍登記」；MOF 網路交易專區（舊公告，104-11-24 更新）：個人在網路銷售貨物/勞務亦須營業登記，未登記可補稅及罰（§51、稅捐稽徵法 §44），可依稅捐稽徵法 §48-1 自動補報 | VERIFIED（條文/公告） |
| 小規模營業人起徵點 | etax 網路交易 Q&A：自 114/1/1，「勞務5萬元」「貨物10萬元」（月銷售額）；低於起徵點「暫時可以免向國稅局辦理稅籍登記」，超過須「立即」登記報繳。**注意**：etax 另一頁（賣家 export-case 範例）寫「4萬」，與 Q&A 5 萬不一致，該頁範例可能未更新 → 以 Q&A（含明確生效日）為準，仍標 PARTIALLY VERIFIED | PARTIALLY VERIFIED |
| 稅率/發票 | etax export-case 範例：月銷售額低於 20 萬由稽徵機關核定 1%（查定課徵）；超過 20 萬經核准可用統一發票 5%；以雙月申報。**是否適用顧問業/個人：UNKNOWN** | PARTIALLY VERIFIED（範例）|
| 持續性接案是否須設行號/公司 | 條文未規定「個人須設公司」；是否需「商業登記」（商業登記法）本次**未查** | UNKNOWN |

### 3.3 二代健保補充保費

- 全民健康保險法 §31（A，資料截止 115-11-06）：執行業務收入屬補充保費給付項目，由「扣費義務人於給付時扣取」並於次月底前繳納；單次給付逾一千萬元的部分及「未達一定金額者」免扣；**費率與「一定金額」在法條頁未載**。
- 健保署文件（搜尋摘要，PDF 未能開啟，B）：單次給付達新臺幣 20,000 元、費率 2.11%、單次上限以 1,000 萬元計 → **PARTIALLY VERIFIED，未讀原文，不要引用為確定**。另有新聞稱曾討論改為年度累計（B/C，結果未驗證）。
- **關鍵缺口**：扣費義務人是 Taiwan 付款方；**境外客戶付款給你時是否有人扣費、你是否須自行處理：UNKNOWN**。

### 3.4 個人 vs 公司（結構選項；不做建議）

| 選項 | 官方依據 | 狀態 |
|---|---|---|
| 以個人接案，申報綜合所得稅 | 所得稅法 §14 分類 | 類別/費用率 UNKNOWN |
| 行號/小規模營業人 | 營業稅法 §28；起徵點 5 萬（勞務，Q&A）| 設立流程、商業登記、收費 **UNKNOWN（未查）** |
| 公司（Ltd） | — | 本次未查：設立成本、營所稅、股東盈餘分配稅 → UNKNOWN |
| 與雇主關係 | 見 §4 | UNKNOWN |

## 4. 雇主 / 兼職揭露（generic UNKNOWN，用戶契約未知）

以下皆為待查項，非結論：
1. 僱傭契約或工作規則是否禁止兼職或要求事前申報：UNKNOWN。
2. IP 歸屬/職務發明條款是否涵蓋下班後作品、與雇主業務重疊者：UNKNOWN。
3. 利益衝突/競業禁止約定是否成立：UNKNOWN（BASELINE 06 僅有第二手整理）。
4. 是否使用公司設備、帳號、時間、資料（不得）：待用戶自查。
5. 客戶資料與 WebComm 政策：**不得將客戶/個資/機密輸入 AI 工具**；assessment 流程設計時須避免取得客戶敏感資料（INFERENCE）。
6. 受僱薪資所得 + 兼職所得合併申報、勞健保投保身分變動：UNKNOWN。
7. 公務員/特定身分：UNKNOWN。

## 5. 發票、外幣收款與簿記（待查項）

- 統一發票 vs 收據：是否需開立取決於是否為營業人與其稅籍類別 → UNKNOWN。
- 外幣收入認列時點與匯率：etax 範例頁稱外銷勞務以「收款日銀行買入匯率」折算（營業稅，PARTIALLY VERIFIED）；**所得稅上的認列時點與匯率 UNKNOWN**。
- 外匯證明取得：結匯時由銀行出具外匯證明（施行細則 §11(2)）；若不結匯留存外幣則用「原始外匯收入款憑證影本」。對實務是否需「結匯」才能零稅率：UNKNOWN（細則兩種方式皆列）。

## 6. 可執行的下一步（人工）

1. 向國稅局（或會計師）以書面詢問：個人對境外企業提供遠端 MongoDB assessment 之所得類別、是否須營業登記、是否適用 §7(2) 零稅率、二代健保補充保費。
2. 向收款銀行詢問：SWIFT 入帳手續費、中間行費、匯入匯款分類編號、外幣帳戶申報流程。
3. 登入 Wise/PayPal/Payoneer（人工）確認 Taiwan 當前費率與開戶資格。
4. 取得並閱讀自己的雇傭契約。

## 7. 與 Phase 0 的修正

- Wise：BASELINE「無證據」→ NEW EVIDENCE：官方 USD 帳戶不可用國家清單**不含 Taiwan**，但未正面證實 → 仍 UNKNOWN/PARTIALLY VERIFIED。
- PayPal：BASELINE 有 2.50%/3.00%；補 **4.00% 付款轉換**；提領費同。收款費率仍缺。
- 營業稅：BASELINE 06 §4.2 標「持續性接案是否需營業登記/零稅率：UNKNOWN（未查）」→ NEW EVIDENCE：§7(2)、細則 §11(2)、起徵點（勞務 5 萬/貨物 10 萬，114/1/1）、§28 已讀；個案適用仍 UNKNOWN。
- 二代健保：BASELINE 未涵蓋 → 補 §31 與（未驗證的）2.11%/20,000。

## 8. UNKNOWN 清單（彙整）

PayPal 商業收款費率/限額；Wise Taiwan 資格與費率；Payoneer Taiwan 實際費率；Contra/Polar 到帳幣別與保留期；銀行端電匯費；匯入匯款分類編號；個案所得類別；費用標準率；是否須營業/商業登記；零稅率個案適用；NHI 對境外給付；外幣所得認列時點；公司設立選項；雇主條款；US 預扣/W-8BEN（BASELINE 06 §3，未重驗）。
