# 12 獲客管道研究（固定範圍 MongoDB assessment 的 acquisition channels）

- access date：2026-11-16（除另註明）
- 標籤：VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / UNKNOWN；證據等級 A=官方、B=高可信第二手、C=社群/弱；結論標 BASELINE（沿用 Phase 0 的 03/06/platforms.md）/ NEW EVIDENCE / INFERENCE。
- **不是法律、稅務或財務建議**；內容須人工複核。依 WebComm 政策不得視為正式文件。

## 0. Method & limitations

- 工具：WebFetch（其回傳為小模型對頁面的摘要，非原文逐字；引文以「」標示者為摘要中引述的條款短句，高風險引用上線前須人工對照原文）、WebSearch。未登入、未建帳號、未聯絡任何人、未接受條款、未繞過任何阻擋。
- 官方頁 403/無法讀取：Upwork（`upwork.com/legal`、`upwork.com/resources/is-upwork-free`）、Fiverr（Terms of Service）、Reddit（User Agreement 與 Reddit Rules，另一網域被工具拒絕）、PayPal 商業費率頁（403/404）。這些欄位只能用搜尋摘要/第二手，一律 UNVERIFIED。Wayback 本次工具無法使用，未嘗試成功。
- 「公開 MongoDB/database assessment 需求證據」欄**不在本檔重做**：需求量化屬 DEMAND dataset（其他 agent）；本檔只註明該管道是否有可觀測的公開需求面（job post = hiring，不等於購買）。多數欄為 UNKNOWN。
- 沒有任何轉換率、得標率、營收數字；平台費僅引官方文字，否則 UNKNOWN。
- 計數：來源列見 `_sources/channels_payment_tax.csv`（本檔與 13 共用）。本檔管道數 18；官方（A）ToS/政策條款實際讀到者：Contra、Freelancer、LinkedIn、HN（ToU + Guidelines）、GitHub = 5 個管道；其餘 ToS 為 UNVERIFIED/UNKNOWN。

## 1. 總表（A 級證據以「官」標示；INFERENCE 以 [INF] 標示）

欄位縮寫：TW = 是否允許 Taiwan 使用者；費 = 平台對接案者收費；ToS = 自動化/爬取/AI 提案條款。

| # | 管道 | TW 可用 | 客戶品質證據 | 價格可見度 | 平台費（官方） | 地理限制 | 付款/提領 | ToS（自動化/爬取/AI） | 適合固定範圍 assessment | 信任門檻 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Upwork | UNKNOWN（官方頁 403；無官方拒絕證據） | UNKNOWN；BASELINE：僅第二手 | 公開 job 預算（hiring，非成交）| 官方頁 403。第二手（C）：2025-05-01 起 0–15% 依合約（UNVERIFIED，且與 BASELINE 一致）| UNKNOWN | UNVERIFIED（見 13） | 官方 help「Use bots and other automation properly」存在（BASELINE S21）但本次 403，內容僅搜尋摘要，UNVERIFIED。AI 提案：搜尋顯示 Upwork 自家指引建議「若使用 generative AI 應告知客戶」（C/B 摘要），**無明文全面禁止**，UNVERIFIED | 高 [INF]：有 Fixed-price 與 Project Catalog 概念，但「assessment」類為低價 gig 競爭 | 新帳號 0 評價 → 高 |
| 2 | Contra | **PARTIALLY VERIFIED**：官方 help 稱 180+ 國，排除 Russia/Iran/NK/Cuba/Syria（A），Taiwan 未點名 | UNKNOWN | 依 profile/project，公開度 UNKNOWN | 官：「100% commission-free」不抽成；處理商費另計（help.contra.com 12642699，經搜尋摘要）。ToS §11.2：stablecoin/early payout 可能收費；Pro 方案價格僅第二手（C） | ToS §2：「business purposes only」；不得提供「gratis introductory or trial services」 | USDC 2%/1%、PayPal 2%、bank $0–8+匯差 0.4–1%、Payoneer ≤$3（A，NEW EVIDENCE 重驗） | **官方 ToS（A，經摘要）**：§10 禁止以「spiders, robots, crawlers, data mining tools」存取/下載內容；§8 禁止以「multiple accounts, automated tools」規避外聯上限；§6.9 AI 輸出「should not rely … as a sole source of truth」。未見禁止 AI 撰寫提案的條文 | 中 [INF]：標準化 service 可上架；但 ToS §2 禁免費試做 → 「免費 mini-audit 當 lead magnet」在 Contra 內可能違規 | 中高 |
| 3 | Freelancer.com | UNKNOWN；ToS §3 僅排除 <16 歲、被停權者、依澳洲或適用法被禁者（A） | UNKNOWN | job 預算公開（hiring） | ToS §6/7：對「introduction fees for Projects, listing upgrades and memberships」收費（A，確切費率 UNKNOWN）；BASELINE 第二手 ~10% | §18：付款到「we do not offer our Service」的國家可被限制 | ToS §20：每月提領上限 USD 10,000（A，NEW EVIDENCE）；BASELINE：PayPal/Payoneer 最低 $50、wire 最低 $500（摘要） | **官方 ToS（A）**：§33「will not use any robot, spider, scraper or other automated means」；§4 禁聚合 listings。AI 條款：可見文本未涵蓋（頁面讀到 §46，其後未讀） | 低 [INF]：低價競標文化 | 高 |
| 4 | Fiverr | UNKNOWN（官方 403） | UNKNOWN | gig 價格公開（provider_marketing）| 官方 403；第二手（C）賣家 20%（UNVERIFIED，BASELINE 同） | UNKNOWN | UNVERIFIED（BASELINE：Payoneer/PayPal/bank 第二手） | 官方 403；搜尋僅見爬蟲廠商宣稱「ToS 限制爬取」（C）。UNVERIFIED | 中低 [INF]：可做 productized gig，但買家多為小額 | 高 |
| 5 | Arc | UNKNOWN。`arc.dev/w/taiwan` 為「Remote jobs in Taiwan」職缺板，含 Taiwan filter（本次讀取），未列開發者資格/費用/付款（C/A 混合）；`/talent-faq` 404 | UNKNOWN | 職缺顯示 hourly 但無金額 | 頁面未載（UNKNOWN） | 部分職缺要求時區重疊（頁面） | UNKNOWN | UNKNOWN | 低 [INF]：職缺/長期派遣導向，非固定範圍 | 中（需審核，細節 UNKNOWN） |
| 6 | Toptal | UNKNOWN：頁面不列國家，稱「from around the world」，單一職缺限「US/Canada/UK Only」（A） | 官：客戶為何者 UNKNOWN | 費率由成員自訂，Toptal 開票/收款（A） | 頁面未列抽成（UNKNOWN） | 個別職缺有地區限制（A） | UNKNOWN | 「Website Terms」未讀 | 低 [INF]：按時薪/長期派遣，非 productized | 高：官方稱 screening「typically takes a few weeks」，要求「at least 2-3 years」經驗（A） |
| 7 | Lemon.io | UNKNOWN：官方頁不列限制國家，稱「from wherever you want to live」；客戶多為「U.S. and Western Europe」（A） | 官：客戶描述（provider_marketing） | 官：無開發者費率；「Senior engineers from $55/hr」未說明是客戶價或開發者收入（UNKNOWN 歸屬） | 官未揭露 | 無明列限制 | 官：直接銀行、Payoneer 或 Wise（A）；費用 UNKNOWN | UNKNOWN | 低 [INF]：長期合作 20h/週以上；非 assessment | 高：5 階段含 live 面試（A） |
| 8 | LinkedIn | 一般帳號開放（User Agreement 無國別限制於所讀段落）；VERIFIED 僅限「條款未見排除」→ PARTIALLY VERIFIED | B2B 決策者較多 [INF] | 無公開價 | 免費帳號；付費 Premium/Sales Navigator 費用 UNKNOWN | — | — | **官方（A）§8.2**：不得「use software, devices, scripts, robots … to scrape」；§13「Use bots or other unauthorized automated methods」；§1「create a false identity」→ **自動化外聯/爬取高風險**，只適合人工 | 中高 [INF]：以內容與人脈引流，再走合約 | 中：需公開 profile 與案例 |
| 9 | Reddit | 開放（UNKNOWN 條款，官方 403/被拒） | C（社群） | 無 | — | — | — | 官方 User Agreement 無法讀取；BASELINE 外：2024 搜尋顯示 Reddit 稱商業性爬取者需遵守其條款與 robots.txt（C，二手）。**UNVERIFIED** | 低 [INF]：硬推銷易被版規/spam 處理；只能當 pain 研究與內容發布 | 低-中 |
| 10 | Hacker News | 開放（無國別限制於所讀條款） | C | 無；但有 "Who is hiring / Freelancer? Seeking freelancer" 月度串（需另用 Algolia API 研究，屬 DEMAND） | — | — | — | **官方 ToU（A）**：「you will not engage in or use any data mining, robots, scraping or similar data gathering」；不得「harvest or collect email addresses or other contact information」。**Guidelines（A）**：「Please don't use HN primarily for promotion」「Please don't put generated text in HN posts」 | 低 [INF]：僅適合技術文章（Show HN 無證據）| 低（以文章品質建立信用）|
| 11 | MongoDB Community Forums | 開放（UNKNOWN 國別） | C | 無 | — | — | — | Forum 規則頁（A）僅見「Don't post spam」「Don't cross-post」「Don't post link-only discussion topics」；**未見**推銷/徵才專條（頁面內未載，UNKNOWN）| 低 [INF]：以回答問題累積可見度；直接推銷風險未知 | 中（官方社群，回答品質可見） |
| 12 | GitHub（含 OSS issues、Sponsors、README/Profile） | 開放 | B（可看到提交歷史） | 無 | 一般免費；Sponsors 費用 UNKNOWN（未讀） | — | — | **官方 ToS（A）§H**：「You may not use the API to download data or Content from GitHub for spamming purposes」；「selling GitHub users' personal information, such as to recruiters, headhunters, and job boards」被禁；濫用 API 可停權 | 中 [INF]：作為信任證據（公開工具/檢查腳本）而非直接獲客；**不得**用 API 批量抓聯絡人寄信 | 低-中 |
| 13 | 個人網站 / SEO | 不受限 | 自有 | 可自定公開價 | 網站成本 UNKNOWN | — | 自選 | 無平台 ToS；其他法規（個資、廣告）UNKNOWN | 高 [INF]：固定範圍產品頁 + 範例報告最貼近「productized」；但冷啟動慢，SEO 成效 UNKNOWN | 高（無第三方背書時）|
| 14 | 技術內容（部落格、教學、開源檢查清單） | 不受限 | 自有 | — | — | — | — | 發布平台各自條款（HN/Reddit/DEV 等）| 中高 [INF]：可建立 competence 證據；需遵守雇主 IP/機密（UNKNOWN 契約）| 中 |
| 15 | 轉介（referrals，含前同事/前客戶） | 不受限 | 取決於關係 | 自定 | 無 | — | 自選 | — | 高 [INF]：固定範圍小單最易靠信任成交；但**需先有可轉介的客戶/同事**（現況 UNKNOWN） | 低 |
| 16 | 合作/分包（MongoDB Partner Program、Percona 類） | 見 §3 | 官方夥伴頁（provider_marketing）| 無 | MongoDB：onboarded 夥伴可免費取得 SI 認證訓練（A） | 表單要求 company name、city、country、website（A）→ 以公司主體為前提 | 自議 | Partner Program Agreement：MongoDB 可「at any time without notice」變更計畫（搜尋摘要，B） | 中 [INF]：Percona/MinervaDB 類 channel 以公司資格 | 高（需法人與經驗） |
| 17 | Taiwan 本地 B2B 直接開發 | 是 | UNKNOWN | UNKNOWN | — | — | TWD 轉帳（跨境問題小）[INF] | 個資法等適用 UNKNOWN | 中 [INF]：付款/發票簡單，但是否有 MongoDB 需求 UNKNOWN；Phase 0 未取得任何 Taiwan 本地平台官方費率 | 中 |
| 18 | 專業人脈 / 社群（MUG、meetup） | 是 | 取決於 | — | — | — | — | — | 中 [INF] | 低-中 |

> 注意：表中「適合固定範圍 assessment」「信任門檻」若標 [INF]，為本研究依平台運作形態做的推論，非證據；沒有任何成交率或收入數字。

## 2. 條款關鍵句（供自動化風險判斷；皆為 WebFetch 摘要引文，上線前須人工核對原文）

| 管道 | 條款 | 關鍵句（短引） | 等級 |
|---|---|---|---|
| Contra ToS §10 | 爬取 | 「using any engine, software, tool, agent, device or mechanism (including spiders, robots, crawlers, data mining tools or the like)」不得存取/下載內容（Contra 自家工具與搜尋引擎例外）| A（摘要） |
| Contra ToS §8 | 外聯 | 「including through the use of multiple accounts, automated tools, or coordinated activity」規避上限屬違規 | A（摘要） |
| Contra ToS §2 | 免費試做 | 平台「is not for use by individuals or entities soliciting or providing gratis introductory or trial services」 | A（摘要） |
| Freelancer ToS §33 | 機器人 | 「will not use any robot, spider, scraper or other automated means to access the Website」 | A（摘要） |
| LinkedIn UA §8.2 | 機器人 | 「Use bots or other unauthorized automated methods to access the Services」；亦不得「scrape or copy the Services, including profiles」 | A（摘要） |
| HN ToU | 抓取 | 「you will not engage in or use any data mining, robots, scraping or similar data gathering or extraction methods」 | A（摘要） |
| HN Guidelines | 推廣/AI | 「Please don't use HN primarily for promotion」；「Please don't put generated text in HN posts」 | A（摘要） |
| GitHub ToS §H | spam | 「You may not use the API to download data or Content from GitHub for spamming purposes」 | A（摘要） |
| Upwork | 自動化 | 官方 help「Use bots and other automation properly」（標題，BASELINE S21）；直接抓取 403，內文 UNVERIFIED | UNVERIFIED |
| Upwork | AI 提案 | 官方未見全面禁止；指引建議揭露 AI 使用（搜尋摘要）| UNVERIFIED |
| Fiverr / Reddit | — | 官方頁無法讀取 | UNKNOWN |

**含義（INFERENCE）**：Upwork/Contra/Freelancer/LinkedIn/HN 的條款文字皆對機器人/爬取採禁止立場，對「AI 協助撰寫」除 HN（禁生成文字）外未見明文禁止。**AI 可用於整理、起草，但提案/貼文應人工改寫、逐則發出；不做自動抓取/批量外聯。**

## 3. 合作/分包（MongoDB / Percona）公開準則

- MongoDB Partner Program（A，`mongodb.com/company/partners`）：類別有 Technology、Certified by MongoDB DBaaS、Services and Solutions、Built with MongoDB、Cloud。頁面「doesn't list eligibility criteria beyond」互補性服務；申請需填公司名/城市/國家/網站/聯絡人/說明並同意 Partner Program Agreement；onboarded 夥伴可取得免費 SI Associate（約 12h）與 SI Architect（約 8h）認證課程（NEW EVIDENCE）。**個人接案者是否可申請：UNKNOWN**（表單以 company 為單位）。
- MongoDB Consulting（A，`mongodb.com/products/consulting`）：自家提供 Solution Delivery、Flex Consulting、Consulting Packages（Advisory / Application Development / Training）；價格不公開；頁面未說明夥伴如何參與。→ 官方自己提供類似 advisory，意味有直接競爭；**競品細節由其他 agent 處理**。
- Percona（A，`percona.com/blog/about/partners`）：Strategic / Channel / Technology 三類；Channel 含 Web Gain Soft（Thailand）、MinervaDB（APAC，Bangalore/Singapore）、Compu-Gen；頁面「doesn't list formal eligibility requirements」，申請以 email/Contact Us。→ APAC 已有 channel 夥伴 → 同區競爭或可分包對象皆為 UNKNOWN。
- 結論：分包可能是**取得信任與案源**的路徑，但公開準則不足，**必須主動聯絡才能知道**（本研究依規則不聯絡）。

## 4. 簡短分析：排名（依證據強度，非預期收益）

排序標準：(a) 官方條款讀到且不排除 Taiwan/自動化風險可控；(b) 與固定範圍 assessment 的結構契合（INFERENCE）；(c) 信任門檻。**無任何管道有成交/收入證據。**

1. **個人網站 + 技術內容 + 轉介/人脈（13/14/15/18）** — 結構契合最高 [INF]；不受平台條款或地理限制。弱點：冷啟動；現有轉介來源 UNKNOWN；需先確認雇主 IP/兼職條款（UNKNOWN）。
2. **Contra** — 唯一在本次取得官方 ToS、官方 payout 與 0% 抽成文字的 freelance 平台（A）；Taiwan 未被排除但未被明列（PARTIALLY VERIFIED）。弱點：ToS §2 禁免費試做；§10/§8 禁自動化；客戶來源與 MongoDB 需求 UNKNOWN。
3. **Upwork** — 有 hiring 面可觀測（DEMAND dataset），但官方條款/費率/Taiwan 資格皆 403 → UNVERIFIED；信任門檻高。僅建議**人工**操作。
4. **LinkedIn（人工）** — B2B 決策者觸及 [INF]；自動化明確被禁。
5. **MongoDB 夥伴/Percona 類分包** — 準則不足，需公司主體；UNKNOWN 最多。
6. **Fiverr / Freelancer** — Fiverr 官方全 403；Freelancer 官方條款讀到但競標文化與固定範圍定價不相容 [INF]。
7. **Toptal / Lemon.io / Arc** — 皆為人才匹配/時薪長期派遣，與 productized assessment 不同形態 [INF]；審核長（Toptal「a few weeks」；Lemon 5 階段）。
8. **HN / Reddit / MongoDB Forum** — 只適合技術貢獻與 pain 蒐集，不適合推銷（HN Guidelines 明文）；Reddit 官方條款未讀。
9. **Taiwan 本地 B2B** — 付款/發票最簡單 [INF]；但需求與管道皆缺證據（Phase 0 亦無官方費率），UNKNOWN。

## 5. 對 Phase 0 的修正/補充

- NEW EVIDENCE：Contra ToS 條文（§2 免費試做、§8/§10 自動化、§11.2 費用）、Freelancer ToS（§33、§20 每月 USD 10,000 提領上限、§18）、LinkedIn §8.2、HN ToU/Guidelines、GitHub §H、MongoDB/Percona 夥伴頁、Lemon 官方（$55/hr 字樣歸屬不明）。
- BASELINE 未變：Upwork/Fiverr 官方頁仍 403。
- 衝突點：Freelancer ToS 說明費用名目為 introduction fees/memberships，與第二手「約 10%」不一致 → 費率仍 UNKNOWN。

## 6. UNKNOWN 清單

Upwork/Fiverr/Reddit 官方條款全文；各平台對 Taiwan 的明確資格；Toptal/Arc/Lemon 抽成；MongoDB Forum 推廣/徵才規則；個人是否可成為 MongoDB 服務夥伴；Taiwan 本地 B2B 管道；所有轉換率。
