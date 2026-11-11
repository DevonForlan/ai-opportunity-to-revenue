# 06 Taiwan 付款、稅務與兼職可行性

- 研究日期：2026-11-11
- 標籤僅使用：VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / UNKNOWN
- **聲明：本文件不是法律、稅務或財務建議。** 稅務判斷請洽國稅局或會計師；依公司政策，內容須人工複核後方可使用。
- 來源編號 S## 對應 `research/_sources/platforms.md`。

## 1. 收款通路總覽（Taiwan 個人）

| 通路 | Taiwan 可用？ | 證據 | 費用/限制 | 標籤 |
|---|---|---|---|---|
| Stripe Global Payouts（Stripe 作為付款方，匯給 Taiwan 收款人） | Taiwan（TW）在可收款國家清單，幣別 TWD（另有 private preview 的 USD） | Stripe 官方 docs（S03，A） | 寄件方國家僅 US、UK；收款需符合 recipient requirements | VERIFIED |
| Stripe Connect cross-border payouts（平台自助） | 官方只寫 US/UK/EEA/Canada/Switzerland 平台間自助跨境；其他國家須聯絡業務或用 Global Payouts | S16（A） | 費用依收款方所在地，見 Stripe Connect payout pricing | VERIFIED（限制本身） |
| Stripe 帳號（在 Taiwan 自行開設） | stripe.com/global 頁面抓取結果**未列 Taiwan**（S04，A）；Stripe 的 Taiwan 付款指南頁亦未宣稱支援 Taiwan 帳號（S30，A）；第二手稱個人「技術上可申請」但 payout 到 Taiwan 銀行有限制（S31，C，2026-04，文章自述未經人工審稿） | 互相衝突 | — | UNVERIFIED（不要假設可開） |
| Polar（Stripe Connect Express） | 官方 payout 國家清單含 Taiwan | S15（A） | payout 費用頁面未載 | PARTIALLY VERIFIED（Polar 側 VERIFIED；實際 KYC 流程、費用、到帳幣別 UNKNOWN） |
| Algora / Opire / IssueHunt 的 Stripe/PayPal 付款 | Taiwan 是否在其付款國家內 | — | — | UNKNOWN |
| PayPal Taiwan | Taiwan 個人帳戶可提領至本地銀行；TWD 提領至玉山銀行 TWD 帳戶無手續費（無匯兌時）；其他 TWD 銀行未列；提領至美國帳戶 2.50%；匯兌：提領至本地銀行 2.50%，其他 3.00% | PayPal TW 費用頁（S32，A；經 WebFetch 摘要） | 收款（商業交易）費率在另一頁，未讀 | PARTIALLY VERIFIED |
| Payoneer | 官方定價頁未提 Taiwan 專屬資訊：本地銀行固定 USD 1.50 僅適用於清單國家，**Taiwan 不在該清單**；未列國家的提領為 1.2%–4%；以非本地幣別收款 1%（最低 USD 1）；年費 USD 29.95（12 個月累計收款低於 USD 6,000 時收取）。官方註明「不同地區可能不同」 | S33（A） | 搜尋摘要曾提到「1% 適用 China/Taiwan/Korea/Hong Kong 非本地幣別提領」（C，與抓取頁不一致，UNVERIFIED） | PARTIALLY VERIFIED |
| Wise Taiwan 收款 | 搜尋結果**無任何**證據顯示 Wise 提供 Taiwan 居民收款帳戶；第二手論壇稱可匯入 Taiwan 但不能持有 TWD（C） | S34（C） | 匯入 USD 到 Taiwan 的 Wise 費率表有 USD 19.29（預測有中間行費時，搜尋摘要，C，UNVERIFIED） | UNVERIFIED |
| 電匯（bank wire） | 一般可行 | 第二手：Upwork 約 USD 30、Freelancer USD 25 + 中間行費（S22，PARTIALLY VERIFIED）；個案：Taiwan 論壇有使用者稱 CTBC 收 Wise 匯入時扣 TWD 400 或 600（C） | 每筆固定費高；金額小時不划算 | PARTIALLY VERIFIED |
| USDC / 鏈上 | Contra 官方：多數國家可選 USDC 付款，費率 2%（free）/1%（Pro）（S20，A）；Superteam Earn 以錢包付款（S12，A）。Taiwan 能否出金成 TWD（交易所、銀行政策）：**UNKNOWN**（本次未研究） | — | — | PARTIALLY VERIFIED（平台側）/ UNKNOWN（出金側） |

## 2. 各平台付款重點（與 03 對照）

| 平台 | Taiwan 付款 | 提領費/最低額/保留期 |
|---|---|---|
| Contra | USDC、PayPal、bank、Payoneer 皆列在官方 help（S20，A）。PayPal 提領費 2%；bank $0–8 + 匯率 0.4–1%；Payoneer 單筆最高 $3 | 保留期、最低額：UNKNOWN |
| Freelancer.com | PayPal / Payoneer 最低 USD 50、費 USD 1；Wire 最低 USD 500、費 USD 25 + 中間行費（S22，摘要來自搜尋結果，頁面直接抓取未見這些數字） | 保留期 UNKNOWN |
| Upwork | 官方頁受 403 擋。第二手：Local bank $0.99、Wire ~$30、PayPal/Payoneer 另計（S35，C）；另有 2026-09-01 起「Direct to U.S. bank」對稅務地址在美國以外的自由工作者收 USD 2.99（第二手，C） | Taiwan local bank 是否支援：UNKNOWN |
| Fiverr | 官方頁 403。第二手：Payoneer 每筆 USD 1；PayPal 無提領費但有匯兌；結算 7–14 天；每日提領上限 USD 5,000（C） | UNVERIFIED |
| Lemon.io | 官方：直接匯銀行 / Payoneer / Wise（S25，A） | 費用、最低額 UNKNOWN |
| Toptal / Arc / Braintrust | UNKNOWN | UNKNOWN |
| Superteam Earn | 官方：Superteam/Solana 贊助 listing 須 KYC，提交付款表單後約 7 天內付款；外部贊助付到錢包（S12，A） | 費用 UNKNOWN |
| Polar | Stripe Connect Express | UNKNOWN |

## 3. 稅務表單：W-8BEN

- IRS 官方頁（S36，A）：外國人（foreign person）作為應被預扣所得之 beneficial owner 時，應向扣繳義務人或付款方提供 Form W-8BEN；付款方要求時即使不主張減免也應提交。
- 若使用美國平台，可能被要求 W-8BEN；是否適用、如何填寫（例如是否主張條約優惠）：**UNKNOWN，須會計師確認**。
- 第二手（S27，C，2026-04）稱「W-8BEN 可避免 30% 美國預扣」與「截至 2026-04 US–Taiwan 無生效租稅協定」。**本次未以官方來源驗證，視為 UNVERIFIED。**
- 各平台是否實際要求 W-8BEN：UNKNOWN（Upwork、Fiverr 官方頁無法讀取）。

## 4. Taiwan 稅務（個人；官方來源 + 判讀）

> 以下僅整理官方文字，**不構成稅務意見**。

### 4.1 官方文字（財政部電子申報繳稅服務網 etax.nat.gov.tw，A）

- 海外所得定義：「未計入綜合所得總額之非中華民國來源所得及香港澳門地區來源所得」（S37）。
- 門檻：申報戶全年海外所得**未達 NT$100 萬者免予計入基本所得額；達 NT$100 萬以上者應全數計入**（S37、S38）。
- 適用對象：同時符合「在中華民國境內居住之個人」及「申報戶全年海外所得達 NT$100 萬」兩要件（S38）。
- 居住定義：境內有住所且經常居住；或無住所而一課稅年度內居留合計滿 183 天（S38）。
- 基本稅額：基本所得額在 NT$750 萬以下者可扣除 750 萬，無基本稅額；超過則 (基本所得額 − 750 萬) × 20%（S38）。750 萬是整體基本所得額的扣除額，不是海外所得專屬免稅額（S39，經濟日報引高雄國稅局，2026-06-26，B）。
- 海外所得依給付年度計入，不論是否匯回（S38、S39）。
- 外國已納稅額可抵繳但有上限（S38）。
- 成本：無法提供成本證明時，可適用財政部規定的同類所得費用標準（S38）。
- 海外所得類別包含營利所得、執行業務所得、薪資所得（S38）。

### 4.2 關鍵判讀問題：在 Taiwan 做的案，是否算「海外所得」？

- 所得稅法第 8 條第 3 款（全國法規資料庫，A，S40）：「在中華民國境內提供勞務之報酬」屬中華民國來源所得（例外：非居住個人一課稅年度境內居留合計不超過 90 天，且自境外雇主取得者）。
- 因此，**人在 Taiwan 為外國客戶做的接案**，依該條文字可能屬於**中華民國來源所得**（併入綜合所得稅），而**不是**「海外所得」；此時 NT$100 萬門檻不一定適用。官方網頁（S38）以「來源」而非「付款人」定義海外所得，與此一致。
- 第二手（shareuhack，S27，C，2026-04）稱「所得來源取決於勞務提供地，與付款人及付款地無關」並引用判決字號；**本次未驗證該判決**，UNVERIFIED。
- KPMG 文章（S41，B/C，2015）指稱：法院常認為境外公司的勞務若需境內個人參與協助即可能屬來源所得（第 8 條第 3 款的「參與及協助」爭點）。與本情境（個人自己在境內提供）的關係：UNKNOWN。
- 結論：**單憑 NT$100 萬海外所得門檻，不能判斷接案收入是否免課稅。** 該收入屬哪一類所得、如何申報（執行業務所得／其他所得／營利所得）、能否扣除費用：UNKNOWN，須洽國稅局或會計師。
- 外幣收入於何時認列、匯率如何折算：UNKNOWN（本次未查）。
- 若為 Web3/加密貨幣收入（USDC 等）的稅務處理：UNKNOWN（本次未查）。
- 持續性接案是否需要營業登記、營業稅（例如對境外客戶的勞務），或個人是否應設立工作室/公司：UNKNOWN（本次未查）。KPMG 提到財政部對個人在平台提供線上直播勞務有營業稅輔導期至 2026-06-30（C），與一般接案是否類比：UNKNOWN。

### 4.3 自動補報

- 經濟日報引高雄國稅局（S39，B）：未被檢舉或查獲前主動補報補繳，依稅捐稽徵法第 48 條之 1 可能免罰；細節與適用條件請以法條與國稅局為準，UNKNOWN。

## 5. 兼職與雇主風險（Taiwan）

> 非法律意見；以下為第二手整理（B/C），**未取得勞動部原文或法條原文**，整體 PARTIALLY VERIFIED。

- 第二手（S42，C）：勞動部立場為員工可在正常工作時間外兼職；若兼職影響勞動契約履行，雇主可依工作規則訂定處罰；是否影響依個案認定。
- 第二手（S42，C）：有判決案例中，員工隱瞞兼職且於上班時間工作，被認定違規情節重大，雇主依勞基法第 12 條不經預告解僱；但法院並非全面禁止兼職。
- 第二手（S42，C）：競業禁止需符合勞基法對競業禁止約定的 4 項要件，缺一即無效；一般兼職禁止條款的效力在實務上有限。
- 實務檢核清單（不是法律結論）：
  1. 檢查僱傭契約與公司工作規則是否有兼職、利益衝突、智慧財產權歸屬條款：UNKNOWN（需讀你自己的文件）。
  2. 不要在上班時間或使用公司設備、帳號、資料做接案/bounty。
  3. 避免與雇主有競業或客戶重疊。
  4. 不要把客戶/雇主的機密內容輸入 AI 工具（本公司 WebComm 政策亦禁止）。
  5. 若為公務員身分，適用另外規範：UNKNOWN（本次未查）。

## 6. 可行性結論（只含有證據者）

| 路徑 | 可行性判斷 | 標籤 |
|---|---|---|
| 經 Polar 以 Stripe Connect Express 收款（若有此需求） | 官方清單含 Taiwan | PARTIALLY VERIFIED |
| 經 Stripe Global Payouts 的平台付款 | Stripe 官方列 Taiwan（TWD） | VERIFIED（Stripe 側）；個別平台是否使用此通路 UNKNOWN |
| PayPal 提領到 TWD 銀行 | 官方 TW 頁提及玉山銀行 TWD 提領無費用（無匯兌時） | PARTIALLY VERIFIED |
| Payoneer 提領 | 官方頁說明費用依地區，Taiwan 不在固定 USD 1.50 清單 | PARTIALLY VERIFIED |
| Wise 收款 | 無證據 | UNVERIFIED |
| USDC 收款 | 平台側有（Contra、Superteam Earn）；Taiwan 出金 UNKNOWN | UNKNOWN |
| 自行開 Stripe 帳號 | 官方 Stripe 國家頁未列 Taiwan | UNVERIFIED（不要假設） |
| Algora / Opire / IssueHunt / Gitcoin | 無法判定 | UNKNOWN |

## 7. 後續待查（優先序）

1. 以人工登入方式（不由本研究代做）確認 Upwork、Fiverr、Freelancer 的 Taiwan 提領選項與費率。
2. 取得 Superteam Earn Terms of Use 與國家限制。
3. 向國稅局／會計師確認：在 Taiwan 為境外客戶接案的所得類別、申報方式、是否需營業登記。
4. 查證 W-8BEN 是否被各平台要求，以及租稅協定現況。
5. 確認 Taiwan 銀行對 USDC 出金與 Stripe/PayPal 入帳的政策。
6. 讀自己的僱傭契約與公司工作規則。
