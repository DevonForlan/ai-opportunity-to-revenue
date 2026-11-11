# 03 機會平台研究（Bounty 與 Freelance）

- 研究日期（access date）：2026-11-11
- 標籤僅使用：VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / UNKNOWN
- 證據等級：A = 官方文件/條款/說明頁；B = 較強第二手；C = 弱（部落格、聚合站、論壇）
- 本文件為研究整理，**不是法律、稅務或財務建議**，所有內容須由人工複核後才可使用。依公司政策，不得將其視為正式文件。
- 方法限制：Upwork、Fiverr 官方 help center 對本次抓取工具回 HTTP 403，無法讀取官方原文；相關數字僅能引用第二手並標 UNVERIFIED。未建立任何帳號、未聯絡任何人、未接受任何條款。
- 來源明細見 `research/_sources/platforms.md`（來源編號 S##）。

## 0. 先講結論（Key findings）

1. **Algora**：algora.io 首頁（2026-11-11 抓取）目前呈現為「工程師招募服務」，未提及 bounty、貢獻者 payout、費用（S01）。先前搜尋結果中的 `docs.algora.io/bounties/payments` 與 `/pricing` 抓取皆為 404 或轉址回首頁（S02）。bounty 產品是否仍運作：**UNKNOWN**；費用：**UNKNOWN**（第二手來源互相矛盾）。
2. **Opire**：官網與 docs 內容停留在 2024（S05、S06）；docs 明確寫「claim 不會自動產生付款，付款由雙方直接安排」。這意味著**沒有平台級付款保證**；Taiwan payout：**UNKNOWN**。
3. **IssueHunt**：首頁頁尾 © 2025 IssueHunt K.K.，寫「bank 或 PayPal 付款」，但無狀態、費用、日期（S07）。2026 是否活躍：**UNVERIFIED**。
4. **Gitcoin**：bounties/hackathons 已移交 Buidlbox（官方 support 頁，無日期，S09）；Gitcoin Grants 在 2026 提案 sunset 並改為 d/acc 計畫（S10）。**不是可預期的個人 bounty 收入來源**。
5. **Superteam Earn**：2026 官方 FAQ 仍在（S12）；Superteam/Solana 贊助的 listing 需 KYC，外部贊助以錢包付款；國家限制與 Taiwan 資格：**UNKNOWN**（FAQ 未載）。
6. **Bountysource**：2023 母公司破產、2024 站點下線（第二手 C，S14）；視為**不可用**（PARTIALLY VERIFIED）。
7. **Polar**：官方 payout 國家清單**含 Taiwan**（Stripe Connect Express，S15）；Polar 不是 bounty 市集而是變現工具（MoR）。
8. **Stripe 方面（Taiwan 付款關鍵）**：Stripe 官方 Global Payouts 收款國家清單**含 Taiwan（TWD）**（S03）；但 stripe.com/global 頁面未列 Taiwan（S04）；Stripe Connect cross-border payouts 文件只列 US/UK/EEA/CA/CH 平台間自助跨境（S16）。詳見 `06_TAIWAN_PAYMENT_FEASIBILITY.md`。
9. **Freelance 平台**：Taiwan 資格與提領的官方證據大多取不到；Contra 官方 help 頁（180+ 國、USDC/PayPal/Payoneer）是少數有 A 級證據者（S20）。

## 1. Bounty / 開源 / Web3 機會平台

| 平台 | 2026 活躍 | 機會類型 | Taiwan 可參與 | Taiwan 付款 | 幣別 | 付款方式 | KYC | 平台費 | claim / 驗收流程 | 付款保證 | API/RSS/公開資料 | ToS 自動化/爬取 | ToS 風險 | 證據 URL | 信心 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Algora | UNKNOWN（首頁目前為招募服務） | GitHub issue bounty（歷史）；現首頁為 recruiting | UNKNOWN | UNKNOWN | UNKNOWN（歷史資料為 USD，C） | 歷史：Stripe Connect（C）；現狀 UNKNOWN | UNKNOWN | UNKNOWN（第二手說法：9%、19%+4% 等互相矛盾） | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN（未取得 ToS 全文） | UNKNOWN | https://algora.io/ （S01） | 低 |
| Opire | UNVERIFIED（內容停在 2024） | GitHub issue bounty，最低 USD 20（bounty）、USD 1（tip） | UNKNOWN | UNKNOWN | USD（最低額以 USD 表示，VERIFIED A） | 官方 docs：「付款由當事人直接安排」；第二手稱走 Stripe（C） | UNKNOWN | docs 頁未列平台費；第二手稱 4% + Stripe $0.85+5.25%（C，UNVERIFIED） | PR 送出後 claim；建立者審核（VERIFIED A） | **無**：docs 明寫 claim 不產生自動付款（VERIFIED A） | UNKNOWN | UNKNOWN | UNKNOWN | https://docs.opire.dev/rewards/pricing （S05）、https://opire.dev （S06） | 中（對「無付款保證」）/低（其餘） |
| IssueHunt | UNVERIFIED（頁尾 © 2025） | 開源 bounty；公開 bug 計畫 | UNKNOWN | UNKNOWN | UNKNOWN | 首頁稱「bank 或 PayPal」（A，但僅出現於 bug 計畫段） | UNKNOWN | 首頁未列；舊第二手稱 10%、提領 3.6%（C，2020 前後，UNVERIFIED） | 公司「triage 或修復後付款」（A，bug 計畫） | UNKNOWN | UNKNOWN | UNKNOWN（/terms 未讀） | UNKNOWN | https://issuehunt.io （S07） | 低 |
| Gitcoin | Bounties：已移交 Buidlbox（PARTIALLY VERIFIED）；Grants：2026 年提案 sunset/重組（PARTIALLY VERIFIED） | 公共財 grants、hackathon | UNKNOWN | UNKNOWN | UNKNOWN（歷史為 crypto） | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | https://support.gitcoin.co/gitcoin-knowledge-base/misc/cgrants-bounties-and-hackathons-sunsetting-faq/whats-happening-to-the-hackathons-and-the-bounties-program （S09）、https://gov.gitcoin.co/t/proposal-gitcoin-d-acc-2026-funding-initiative-restructuring-the-grants-program/25157 （S10） | 中 |
| Superteam Earn | PARTIALLY VERIFIED（FAQ 在線；listing 數量未驗證） | Solana 生態 bounty / project / grant（Content、Design、Dev、Other） | UNKNOWN（FAQ 未列國家限制） | 以錢包付款，無 Taiwan 銀行問題；官方未提 USDC（USDC 為 UNKNOWN） | UNKNOWN（官方未載） | 外部贊助：付到 Earn 帳號關聯錢包；Superteam/Solana 贊助：付款表單，提交後約 7 天（VERIFIED A） | Superteam/Solana 贊助 listing 得獎者須 KYC；外部贊助依贊助方（VERIFIED A） | UNKNOWN（FAQ 未提） | 報名/提交 → 得獎者領取（VERIFIED A） | 各贊助方各自負責；平台級保證 UNKNOWN | UNKNOWN | UNKNOWN（Terms of Use 未取得；privacy policy 提及營運方 Ekstasis Private Limited，C/A 混合） | UNKNOWN | https://docs.superteam.fun/the-superteam-handbook/community/faqs/superteam-earn-faq （S12）、https://superteam.fun/earn （S13） | 中（付款/KYC）/低（資格） |
| Bountysource | 不可用（PARTIALLY VERIFIED） | 開源 bounty | — | — | — | — | — | — | — | 2023 母公司破產；2024 站點顯示暫時下線；有開源專案移除徽章（皆 C） | — | — | — | https://en.wikipedia.org/wiki/Bountysource （S14） | 中低 |
| Polar | VERIFIED（docs 在線，2026-11-11 可讀） | 開源/創作者變現工具（Merchant of Record），**非 bounty 市集** | 有條件：Taiwan 在 payout 國家清單內（VERIFIED A） | Stripe Connect Express 付款到 Taiwan 居民或企業（VERIFIED A）；到帳 TWD 或 USD UNKNOWN | UNKNOWN | Stripe Connect Express（A） | Stripe 驗證（細節見 06） | payout 頁未提費用；UNKNOWN | 不適用 | 不適用 | UNKNOWN | UNKNOWN | UNKNOWN | https://polar.sh/docs/documentation/polar-as-merchant-of-record/supported-countries （S15） | 中高（國家清單）/低（其餘） |
| Replit Bounties | 官方 docs 稱 deprecated（第二手摘要，PARTIALLY VERIFIED；本次直接抓取 FAQ 未見狀態文字，S17） | 付費 bounty（歷史） | UNKNOWN | 第二手稱 USD、email 申請、25% 提領費、最低 USD 350（C，來自競品文件，UNVERIFIED） | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | — | — | — | — | — | https://docs.replit.com/additional-resources/bounties/faq （S17） | 低 |
| Dework | UNVERIFIED（聚合站稱 2025-07 被 Thrive Protocol 收購、仍營運，C） | DAO 任務板 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | https://solanacompass.com/projects/dework （S18） | 低 |
| MergeFund、BountyHub、BountyClaim | UNVERIFIED（僅見部落格/Product Hunt 提及，2026） | 開源/鏈上 bounty | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | S19（搜尋結果，C） | 低 |

### 1.1 Bounty 類別補充觀察

- 「Opire 無付款保證」是少數可由官方 docs 直接 VERIFIED 的風險。其他 bounty 平台的付款保證（escrow、爭議處理）**全部 UNKNOWN**。
- 2026 年出現多篇「公開 bounty 市場品質差、AI 垃圾提交」的第二手文章（例如 DEV 文章標題「public bounty market is broken in 2026」，C，S19）；curl 於 2026-01-31 結束 HackerOne bug bounty（第二手，與本表平台無關）。這只能作為市場訊號，不能作為任何平台的證據。
- 所有 bounty 平台的 API/RSS/爬取是否被 ToS 允許：本次**皆未取得 ToS 全文**，一律 UNKNOWN。自動化蒐集前必須先讀 ToS 與 robots.txt，並優先用官方 API 或 GitHub 公開資料。

## 2. Freelance 平台

| 平台 | 2026 活躍 | 機會類型 | Taiwan 可參與 | Taiwan 提領方式 | 幣別 | KYC | 平台費（接案者側） | 接案/驗收 | 付款保證 | API/公開資料 | 自動化/爬取 ToS | ToS 風險 | 證據 URL | 信心 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Upwork | PARTIALLY VERIFIED（2026 年新聞與 Help 內容持續更新，皆為第二手） | 投標式接案 | UNKNOWN（官方受限未取得；多個第二手教學預設 Taiwan 可用，不算證據） | 第二手：Direct to Local Bank（$0.99，非 Taiwan 專屬數字）、Wire（約 $30）、PayPal、Payoneer（C，UNVERIFIED）；Taiwan 是否支援 TWD local bank：UNKNOWN | UNKNOWN（USD 計價為一般情況，未驗證） | 有（身分驗證，細節 UNKNOWN） | 第二手稱 0–15% 依合約，不再固定 10%（C，UNVERIFIED） | 投標 → 合約 → 里程碑/小時制 | UNKNOWN | API 需經核准（A/C 混合：help 文章 S21 經搜尋摘要轉述） | 第二手引用 Upwork help「Use bots and other automation properly」稱即使有 API key 也禁止 scrape（直接抓取 403，PARTIALLY VERIFIED） | **高**（bots/automation 受限，帳號停權風險） | https://support.upwork.com/hc/en-us/articles/43342677368467-Use-bots-and-other-automation-properly （S21） | 低中 |
| Freelancer.com | PARTIALLY VERIFIED | 投標式接案 | UNKNOWN | 官方 support（freelancer.co.uk，無日期）摘要：PayPal / Payoneer 最低 USD 50、提領費 USD 1；Wire 最低 USD 500、費用 USD 25 + 中介銀行費（PARTIALLY VERIFIED；第二手摘要，直接抓取只確認有 PayPal、Skrill、Express Withdrawals 標題）| USD | UNKNOWN | UNKNOWN（第二手稱約 10%，未驗證） | 投標 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | https://www.freelancer.co.uk/support/payments/how-to-withdraw-funds （S22） | 低 |
| Fiverr | PARTIALLY VERIFIED | 商品化 gig | UNKNOWN | 第二手：Payoneer（每筆 USD 1）、PayPal、bank（約 USD 3，美國為主）（C，UNVERIFIED） | USD | UNKNOWN | 第二手稱賣家抽 20%（C，UNVERIFIED） | 買家下單 → 交付 → 驗收 | 第二手稱結算期 7–14 天、每日提領上限 USD 5,000（C，UNVERIFIED） | UNKNOWN | UNKNOWN | UNKNOWN（官方頁 403） | https://help.fiverr.com/hc/en-us/articles/360010530058-Withdrawing-your-earnings-managing-payout-methods （S23，未能讀取） | 低 |
| Contra | PARTIALLY VERIFIED（官方 help 在線；2026 部落格） | 作品集 + 直接案源 | 官方：180+ 國可用，**不支援** Russia/Iran/North Korea/Cuba/Syria；Taiwan 不在排除清單（VERIFIED A，但「未排除」不等於「Taiwan 一定可用」→ PARTIALLY VERIFIED） | 官方：USDC（多數國家，費率 2% free / 1% Pro）、PayPal（2%，「有例外」）、bank transfer（$0–8 + 匯率費 0.4–1%）、Payoneer（每筆上限 $3）、debit card（僅美國）（VERIFIED A） | USDC / USD 等；Taiwan 到帳幣別 UNKNOWN | UNKNOWN | 接案者 0% 抽成（官方 FAQ 經搜尋摘要，PARTIALLY VERIFIED）；提領另有上述費用；Pro 約 $29/月為第二手（C） | 客戶發案或直接邀約 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | https://client-help.contra.com/en/articles/9708244-payout-options-for-contractors （S20） | 中 |
| Toptal | PARTIALLY VERIFIED（官方頁在線） | 精選人才網路（匹配制） | 官方頁未載國家；「絕大多數工作為遠端」（VERIFIED A）；Taiwan 資格 UNKNOWN。第二手稱 Taiwan 未被排除但匹配困難（C） | 官方：Toptal 負責開票與收款（A）；Taiwan 提領方式 UNKNOWN | UNKNOWN | UNKNOWN | 官方頁未列抽成（A）；「約 50% 客戶加價」為第二手（C，UNVERIFIED） | 審核數週：作品/線上測驗、live 解題、專案（A） | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | https://www.toptal.com/freelance-jobs （S24） | 中（流程）/低（其餘） |
| Lemon.io | PARTIALLY VERIFIED（官方頁在線） | 精選開發者匹配 | 官方頁未列可申請國家（A）；Taiwan UNKNOWN | 官方：直接匯入銀行，或經 Payoneer / Wise（A）；Taiwan 銀行是否支援 UNKNOWN | UNKNOWN | UNKNOWN（流程含 CV/LinkedIn、AI 面談、測驗、live 技術面試） | 官方未揭露（A） | 5 階段審核（A） | 官方：Lemon 處理合約與開票（A） | UNKNOWN | UNKNOWN | UNKNOWN | https://lemon.io/for-developers/ （S25） | 中（流程）/低（其餘） |
| Arc.dev | PARTIALLY VERIFIED（arc.dev/en-tw 與 /w/taiwan 頁面存在） | 遠端工作/自由接案匹配 | 有 Taiwan 在地化頁面（`/en-tw/`、`/w/taiwan`，搜尋結果可見，C/A 混合）；資格 UNKNOWN。母公司 Codementor 在 Taipei 有辦公室為第二手（C） | UNKNOWN | UNKNOWN | UNKNOWN | 第二手稱 0% 接案者費（C，UNVERIFIED） | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | https://arc.dev/w/taiwan （S26） | 低 |
| Braintrust | UNVERIFIED | 人才網路 | 第二手稱「Taiwan 不受限」（C，shareuhack，2026-04，文章自述未經人工審稿） | UNKNOWN | UNKNOWN | UNKNOWN | 第二手稱人才 0%、客戶 15%（C） | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | https://www.shareuhack.com/en/posts/remote-job-platforms-taiwan-guide-2026 （S27） | 低 |
| Wellfound | UNVERIFIED | 新創求職 | UNKNOWN | 不適用（求職非接案付款） | — | — | 第二手：雇主付費模式（C） | — | — | — | — | — | S28（搜尋結果） | 低 |
| PeoplePerHour | UNVERIFIED | 投標式接案 | UNKNOWN | 第二手：PayPal、Payoneer、bank，發票核准後 7 天（C） | UNKNOWN | UNKNOWN | 第二手 3.5%–20% 滑動（C） | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | S28（Upwork 資源頁，競品自述，C） | 低 |

## 3. Taiwan 本地平台

| 平台 | 驗證結果 |
|---|---|
| 104外包網 | 嘗試抓取 `case.104.com.tw` 失敗（DNS 無此主機）。該服務是否仍以此網域營運：**UNKNOWN**。104 官方部落格有「接案」主題文章（S29，C），但無平台費與提領資訊。 |
| PRO360 達人網 | 官網標題為「SOHO找案件接案、業主找外包的首選平台」（A，標題）；收費（點數/報價費）、提領：**UNKNOWN**。 |
| Tasker（出任務） | 第二手互相矛盾：uptogo 稱接案者 9% 服務費（另有金流手續費）；Yourator 稱接案會員 12%、案主 6%（C）。官方說明稱「不開放外籍人士註冊」（搜尋結果摘要，官方 help 頁抓取失敗 `Header overflow`，PARTIALLY VERIFIED）。2026-01-28 起官方 LINE 公告 TaskerGo 需購買 T Points（C/A 混合）。現行費率：**UNKNOWN**。 |
| ProCase | 搜尋無任何資料：**UNKNOWN**，不確認其存在。 |

> Taiwan 本地平台一般以 TWD 計價、對象為 Taiwan 居民，付款到 Taiwan 銀行，跨境問題較小；但本次**未取得任何一家的官方費率與提領條款**，不可引用數字。

## 4. 風險與未決事項（UNKNOWN 清單）

1. Algora 現狀、國家與費用。
2. Opire、IssueHunt、Superteam Earn 對 Taiwan 的資格。
3. 所有 bounty 平台的 ToS 對自動化/爬取的規定。
4. Upwork / Fiverr / Freelancer 官方現行費率與 Taiwan 提領選項（官方頁被擋或內容不全）。
5. Toptal / Lemon.io / Arc / Braintrust 對 Taiwan 的明確資格。
6. 各平台是否提供付款保證（escrow）。

## 5. 對「自動化蒐集機會」的含義

- Upwork 第二手與其 help 文章（經搜尋摘要）指向機器人/自動化受限，視為**高風險**，建議不做自動爬取，僅人工瀏覽（此為風險管理建議，不是對 ToS 的認定）。
- GitHub 公開 issue 與 label（例如 bounty 標籤）資料的取得，應走 GitHub 官方 API 與其 ToS；本次未研究 GitHub ToS，**UNKNOWN**。
