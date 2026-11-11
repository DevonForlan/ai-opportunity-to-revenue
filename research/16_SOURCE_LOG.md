# 16 Source Log

合併自 _sources/*.md（各研究線原始表，欄位：Source/URL/Type/Access date/Evidence level/Used for/Confidence/Notes）。存取日 2026-11-11。

## repos


Access date 全部為 2026-11-11。證據等級：A = 直接閱讀原始碼/檔案內容（本次下載 tarball 或 gh api 讀檔）；B = 僅 GitHub API metadata 或 README；C = 僅搜尋結果描述。未執行任何第三方程式碼、未執行 git、未對外發 issue/PR/comment。

| Source | URL | Type | Access date | Evidence level A/B/C | Used for | Confidence | Notes |
|---|---|---|---|---|---|---|---|
| global-builder-opportunity-radar | https://github.com/everton-soares1985/global-builder-opportunity-radar | Repo（tarball 本地讀碼 + gh api） | 2026-11-11 | A | 架構/collector/scoring/dedup/SQLite/CI/來源清單 | High | 0 star、MIT、15 commits（2026-08-14 至 09-08）、無 release；CI 最近 5 次 4 success 1 failure（API）；測試未自行執行 |
| aitippro/TIP | https://github.com/aitippro/TIP | Repo（tarball 本地讀碼） | 2026-11-11 | A | 判斷是否有付款證據 | High | 5 star、無 LICENSE、僅 prompt + shell + 8 份日報，無程式碼 |
| ANVEAI/idea-hunt-skill | https://github.com/ANVEAI/idea-hunt-skill | Repo（tarball 本地讀碼） | 2026-11-11 | A | workflow/kill-gate 評估 | High | 4 star、MIT、單一 SKILL.md（約 18KB）、4 commits |
| app-vitals/shipwright | https://github.com/app-vitals/shipwright | Repo（gh api tree/README/commits，未下載，倉庫 size 約 683MB） | 2026-11-11 | A（README、tree、commits）/ B（程式內容未逐檔讀） | 成熟度、與 Codex/Claude Code 重疊 | Medium-High | 16 star、MIT、contributors API 合計約 4,540 commits、最新 release shipwright-1.6.23（2026-06-24）、最近 100 commits 全在 2026-11；自報指標未驗證 |
| Sudiddii/build-DNA | https://github.com/Sudiddii/build-DNA | Repo（gh api tree/README） | 2026-11-11 | B | build-DNA 候選比對 | Low | 5 star、MIT、3 commits、2026-05-29 建立；是否為使用者所指「build-DNA」= UNKNOWN |
| RamvikasSV/BuilderDNA | https://github.com/RamvikasSV/BuilderDNA | Repo（gh api） | 2026-11-11 | B | 排除 build-DNA 候選 | High | 僅 71 bytes README，空殼，排除 |
| gh search repos "build-dna / build DNA / builddna" | gh CLI 搜尋 | Search | 2026-11-11 | C | build-DNA 搜尋 | Medium | 其餘結果皆為生物 DNA、Holochain、建築等不相關 |
| algora-io/algora | https://github.com/algora-io/algora | Repo（gh api tree/README） | 2026-11-11 | B | 補充 repo | Medium | 1542 star、AGPL-3.0、Elixir、pushed 2026-07-18 |
| NSPG13/agent-bounties | https://github.com/NSPG13/agent-bounties | Repo（gh api tree/README） | 2026-11-11 | B | 補充 repo | Low-Medium | 20 star、license NOASSERTION、Rust、2026-07-08 建立、1944 檔、353 open issues；加密貨幣（Base USDC）付款 |
| speedyapply/JobSpy | https://github.com/speedyapply/JobSpy | Repo（gh api tree + model.py 片段） | 2026-11-11 | B/A（Taiwan enum） | 補充 repo | Medium | 4695 star、MIT；model.py 含 TAIWAN="taiwan" enum，實際各站是否支援台灣 UNVERIFIED |
| MaxKmet/idea-validation-agents | https://github.com/MaxKmet/idea-validation-agents | Repo（gh api README） | 2026-11-11 | B | 補充 repo | Medium | 510 star、MIT、pushed 2026-06-16、純 prompt、支援 Claude Code/Codex/Cursor |
| mvanhorn/last30days-skill | https://github.com/mvanhorn/last30days-skill | Repo（gh api README/tree） | 2026-11-11 | B | 補充 repo | Medium | 67262 star（API）、MIT、2026-01-23 建立、pushed 當日 |
| datou202307-design/trend-opportunity-radar | https://github.com/datou202307-design/trend-opportunity-radar | Repo（gh api README/tree） | 2026-11-11 | B | 補充 repo | Medium | 16 star、MIT、2026-08-06 建立 |
| roperi/UpworkScraper | https://github.com/roperi/UpworkScraper | Repo（gh api README） | 2026-11-11 | B | 補充 repo | Medium | 72 star、MIT、Selenium + SQLite、登入抓取 Best Matches（ToS 風險） |
| D4Vinci/Scrapling | https://github.com/D4Vinci/Scrapling | Repo（gh api metadata） | 2026-11-11 | B | 補充 repo | Medium | 101285 star（API 回傳）、BSD-3-Clause、Python |
| DIYgod/RSSHub | https://github.com/DIYgod/RSSHub | Repo（gh api tree） | 2026-11-11 | B | 補充 repo；路由檢查 | Medium-High | 46922 star、AGPL-3.0；tree 內 lib/routes 未見 104、upwork、cakeresume、pcc 路由 |
| dgtlmoon/changedetection.io | https://github.com/dgtlmoon/changedetection.io | Repo（gh api metadata） | 2026-11-11 | B | 補充 repo | Medium | 35728 star、Apache-2.0、386 open issues |
| openfunltd/pcc.g0v.ronny.tw | https://github.com/openfunltd/pcc.g0v.ronny.tw | Repo（gh api README/tree） | 2026-11-11 | B | 台灣標案資料 API | Medium | 37 star、PHP、GitHub 未偵測 license（README 稱後端 BSD、資料另有授權）、2017 建立、pushed 2026-10-29；API 本身未呼叫 |
| polarsource/polar | https://github.com/polarsource/polar | Repo（gh api metadata） | 2026-11-11 | B | 收入追蹤/收款參考 | Medium | 10468 star、Apache-2.0、Python；台灣出款支援 UNKNOWN |
| midday-ai/midday | https://github.com/midday-ai/midday | Repo（gh api metadata） | 2026-11-11 | B | 收入追蹤參考 | Medium | 15122 star、AGPL-3.0、pushed 2026-06-13（偏舊） |
| huginn/huginn | https://github.com/huginn/huginn | Repo（gh api metadata） | 2026-11-11 | B | 補充 repo | Medium | 50494 star、MIT、Ruby、2013 建立、694 open issues |
| Sver0411/OpportunityRadar | https://github.com/Sver0411/OpportunityRadar | Repo（gh api README/tree） | 2026-11-11 | B | 補充 repo | Medium | 9 star、MIT、Agent Skill、2026-09-14 建立、聚焦學生/職涯/競賽/資助 |
| aiadminhq/Tender-AI、RaptorChin/PCC_Scraper、pipeworx-io/mcp-taiwan-procurement 等 | gh search 結果 | Search | 2026-11-11 | C | 台灣標案小型 repo 盤點 | Low | 皆 0-5 star，未深查，僅列為備註 |

## platforms


Evidence level: A = official doc/terms/help; B = strong secondary; C = weak. Confidence: High / Medium / Low.
Note: "Published/updated" is UNKNOWN when the page showed no date.

| ID | Source | URL | Type | Access date | Published/updated date | Evidence level | Used for | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|---|
| S01 | Algora homepage | https://algora.io/ | Official site | 2026-11-11 | UNKNOWN (footer/©not stated) | A | Algora current positioning | Medium | Page describes recruiting service; no bounty/payout/fee text. Terms at /terms not read |
| S02 | Algora docs/pricing/payments URLs | https://docs.algora.io/bounties/payments ; https://algora.io/bounties/payments ; https://algora.io/pricing ; https://algora.io/docs/payments | Official site | 2026-11-11 | UNKNOWN | A | Showing docs unreachable | Medium | 301 redirects then 404 via fetch tool. Search-snippet fee claims (9%, 19%+4%, "contributors get 100%") unverified and conflicting |
| S03 | Stripe Global Payouts supported recipient countries | https://docs.stripe.com/global-payouts/send-money/recipient-countries | Official doc | 2026-11-11 | UNKNOWN | A | Taiwan (TW) listed, currency TWD, preview USD; sender countries US/UK | High | Applies to Global Payouts only, not Connect account onboarding |
| S04 | Stripe supported countries | https://stripe.com/global | Official site | 2026-11-11 | UNKNOWN | A | Taiwan not in Stripe account country list | Medium | Result from fetch-tool summary; re-verify manually |
| S05 | Opire pricing docs | https://docs.opire.dev/rewards/pricing | Official doc | 2026-11-11 | UNKNOWN | A | Min bounty $20, tip $1; claim does not create auto payment; payment arranged between parties | High | Fees/countries not stated on page; search snippet claimed Stripe $0.85+5.25% + 4% (C) |
| S06 | Opire homepage | https://opire.dev | Official site | 2026-11-11 | 2024 (footer, testimonial "August 2024") | A | Process; staleness | Medium | Activity in 2026 unverified |
| S07 | IssueHunt homepage | https://issuehunt.io | Official site | 2026-11-11 | (c) 2025 | A | Bank/PayPal payment mention; no fees/status | Low | Terms not read. Older fees (10%, 3.6% withdraw) from C sources 2020-ish |
| S08 | ossfund directory (Algora/Opire/IssueHunt profiles) | https://ossfund.onrender.com/issue-hunt | Directory | 2026-11-11 | 2020-06-20 / 2024-09 per snippets | C | Historical fee claims | Low | Stale; not relied on |
| S09 | Gitcoin support: bounties program | https://support.gitcoin.co/gitcoin-knowledge-base/misc/cgrants-bounties-and-hackathons-sunsetting-faq/whats-happening-to-the-hackathons-and-the-bounties-program | Official help | 2026-11-11 | UNKNOWN | A | Bounties/hackathons handed to Buidlbox | Medium | Undated |
| S10 | Gitcoin d/acc 2026 proposal | https://gov.gitcoin.co/t/proposal-gitcoin-d-acc-2026-funding-initiative-restructuring-the-grants-program/25157 | Official governance forum | 2026-11-11 | 2026-03-06 (posted); comments to 2026-05-06 | A | Gitcoin Grants sunset/rebrand proposal | Medium | Proposal, not confirmed decision |
| S11 | The Block: Gitcoin winding down software division | https://www.theblock.co/news/markets/2025-04-25-ethereum-public-goods-funding-protocol-gitcoin-winding-down-its-software-division-352055 | News | 2026-11-11 | 2025-04-25 | B | Grants Stack/Allo wind-down | Medium | From search snippet |
| S12 | Superteam Earn FAQ | https://docs.superteam.fun/the-superteam-handbook/community/faqs/superteam-earn-faq | Official doc | 2026-11-11 | UNKNOWN | A | KYC for Superteam/Solana-sponsored; payment form ~7 days; external wallet payout | High | Countries/USDC/fees not stated |
| S13 | Superteam Earn landing | https://superteam.fun/earn | Official site | 2026-11-11 | UNKNOWN | A | Sections Bounties/Projects/Grants | Low | No listings/terms shown |
| S14 | Bountysource Wikipedia + openHAB thread | https://en.wikipedia.org/wiki/Bountysource ; https://community.openhab.org/t/remove-bountysource-links/150946 | Secondary/forum | 2026-11-11 | 2023-2024 events | C | Bankruptcy 2023, site down 2024 | Low-Medium | Via search summary; no 2026 evidence |
| S15 | Polar supported countries | https://polar.sh/docs/documentation/polar-as-merchant-of-record/supported-countries | Official doc | 2026-11-11 | UNKNOWN | A | Taiwan in payout list via Stripe Connect Express | High | Fees not on page; Polar is MoR tool not bounty market |
| S16 | Stripe Connect cross-border payouts | https://docs.stripe.com/connect/cross-border-payouts | Official doc | 2026-11-11 | UNKNOWN | A | Self-serve limited to US/UK/EEA/CA/CH; use Global Payouts otherwise | High | |
| S17 | Replit bounties docs | https://docs.replit.com/additional-resources/bounties/faq | Official doc | 2026-11-11 | UNKNOWN | A | Status check | Low | Fetch showed no Bounties text; "deprecated" claim from search summary; 25%/$350 from competitor doc (C) |
| S18 | Dework on Solana Compass | https://solanacompass.com/projects/dework | Aggregator | 2026-11-11 | UNKNOWN (page cites Sept 2026) | C | Acquisition by Thrive Protocol 2025-07; operational | Low | Unconfirmed independently |
| S19 | Search results: 2026 bounty landscape (MergeFund, BountyHub, BountyClaim; DEV posts) | https://dev.to/dyclgtm/i-scanned-1500-github-bounties-with-an-ai-agent-the-public-bounty-market-is-broken-in-2026-33pg | Blog | 2026-11-11 | 2026 | C | Market signal only | Low | Promotional/low quality |
| S20 | Contra payout options | https://client-help.contra.com/en/articles/9708244-payout-options-for-contractors | Official help | 2026-11-11 | UNKNOWN | A | 180+ countries; USDC 2%/1%; PayPal 2%; bank $0-8; Payoneer cap $3; unsupported countries | High | Taiwan not named either way |
| S21 | Upwork: Use bots and other automation properly | https://support.upwork.com/hc/en-us/articles/43342677368467-Use-bots-and-other-automation-properly | Official help | 2026-11-11 | UNKNOWN | A | Automation restrictions | Low | Direct fetch HTTP 403; content from search-result summary and a Zendesk mirror (C) |
| S22 | Freelancer.com withdrawal support | https://www.freelancer.co.uk/support/payments/how-to-withdraw-funds | Official help | 2026-11-11 | UNKNOWN | A | Withdrawal methods | Low | Fetch showed only titles; numbers (PayPal/Payoneer min $50 fee $1; wire min $500 fee $25) from search summary |
| S23 | Fiverr withdrawal help | https://help.fiverr.com/hc/en-us/articles/360010530058-Withdrawing-your-earnings-managing-payout-methods | Official help | 2026-11-11 | UNKNOWN | A | Not read (403) | Low | Fiverr figures from C sources (Vaultleap, Wise blog, xflowpay) |
| S24 | Toptal freelance jobs | https://www.toptal.com/freelance-jobs | Official site | 2026-11-11 | UNKNOWN | A | Screening process, billing handled by Toptal, mostly remote | Medium | No country/fee info |
| S25 | Lemon.io for developers | https://lemon.io/for-developers/ | Official site | 2026-11-11 | UNKNOWN | A | Vetting steps; payout via bank/Payoneer/Wise | Medium | No country/fee info |
| S26 | Arc.dev Taiwan page | https://arc.dev/w/taiwan | Official site | 2026-11-11 | UNKNOWN | C | Taiwan localized pages exist | Low | Appeared only in search results; /talent-signup 404 |
| S27 | Shareuhack: remote job platforms Taiwan guide 2026 | https://www.shareuhack.com/en/posts/remote-job-platforms-taiwan-guide-2026 | Blog | 2026-11-11 | 2026-04-01 | C | Platform eligibility, tax, W-8BEN claims | Low | Article states AI-written without per-article human review; claims unverified |
| S28 | Search results: Braintrust/Wellfound/PeoplePerHour | https://www.upwork.com/resources/best-freelance-websites | Competitor blog | 2026-11-11 | 2026 | C | PeoplePerHour fee 3.5-20%, payouts | Low | Competitor-authored |
| S29 | 104 blog freelance tag | https://blog.104.com.tw/tag/%E6%8E%A5%E6%A1%88/ | Official blog | 2026-11-11 | UNKNOWN | C | Existence of 104 freelance content | Low | No fees. case.104.com.tw DNS failed |
| S30 | Stripe: Payments in Taiwan | https://stripe.com/en-at/resources/more/payments-in-taiwan | Official guide | 2026-11-11 | UNKNOWN | A | Does not claim Taiwan accounts supported | Low | Absence of statement only |
| S31 | Shareuhack: Taiwan indie dev payments guide | https://www.shareuhack.com/en/posts/taiwan-indie-dev-global-payments-guide-2026 | Blog | 2026-11-11 | 2026-04-08 | C | Stripe individual onboarding / Taiwan bank payout limits | Low | AI-written, unreviewed |
| S32 | PayPal Taiwan consumer fees | https://securepayments.paypal.com/tw/digital-wallet/paypal-consumer-fees | Official | 2026-11-11 | UNKNOWN | A | TWD withdrawal to E.SUN no fee; 2.50% to US acct; conversion 2.50%/3.00% | Medium | Via fetch summary; seller rates on separate page not read |
| S33 | Payoneer pricing | https://www.payoneer.com/about/pricing/ | Official | 2026-11-11 | UNKNOWN | A | Local bank $1.50 (listed countries, Taiwan not listed); 1.2%-4%; 1% receive; $29.95 annual | Medium | No Taiwan-specific page |
| S34 | Search results: Wise Taiwan receiving | https://tw.forumosa.com/t/wise-formerly-transferwise/189759 | Forum | 2026-11-11 | UNKNOWN | C | No evidence of Taiwan receive accounts | Low | Anecdotal |
| S35 | Search results: Upwork withdrawal fees | https://www.skydo.com/blog/withdraw-funds-from-upwork ; https://www.selfemployed.com/news/upwork-direct-us-bank-withdrawal-fee-2026/ | Blog/news | 2026-11-11 | 2026 | C | Local bank $0.99, wire ~$30, $2.99 US-bank fee (from 2026-09-01) | Low | Upwork official pages 403 |
| S36 | IRS About Form W-8 BEN | https://www.irs.gov/forms-pubs/about-form-w-8-ben | Official | 2026-11-11 | UNKNOWN | A | Purpose of W-8BEN | High | Treaty/rate details not on page |
| S37 | etax: individual basic income tax (overseas income) | https://www.etax.nat.gov.tw/etwmain/alien-tax-service/individual-income-basic-tax/bovNZmM | Official (MOF) | 2026-11-11 | UNKNOWN | A | Overseas income definition; NT$1M threshold | High | |
| S38 | etax tax-saving manual: individual income tax | https://www.etax.nat.gov.tw/etwmain/tax-info/understanding/tax-saving-manual/national/individual-income-tax/6xKrvGR | Official (MOF) | 2026-11-11 | UNKNOWN | A | Residency test, NT$7.5M, 20%, timing, FTC, costs | High | Does not address foreign-payer services |
| S39 | Economic Daily News citing Kaohsiung NTB | https://udn.com/news/story/7243/9588797 | News | 2026-11-11 | 2026-06-26 | B | 750萬 is overall deduction; report whether remitted or not; voluntary correction | Medium | |
| S40 | Income Tax Act Art. 8 | https://law.moj.gov.tw/LawClass/LawSingle.aspx?pcode=G0340003&flno=8 | Official law database | 2026-11-11 | data through 2026-10-30 (per page) | A | Art 8(3) service income sourced where performed | High | Interpretation to freelance cases = UNKNOWN |
| S41 | KPMG Taiwan tax monthly: Art 8(3) 參與及協助 | https://kpmg.com/tw/zh/home/insights/2015/09/tcr-tax-monthly.html | Professional | 2026-11-11 | 2015-09 | B | Participation-and-assistance dispute | Low-Medium | Old; not about individuals |
| S42 | Taiwan side-job articles (104, managertoday, legis-pedia) | https://blog.104.com.tw/working-part-time-during-working-hours/ ; https://www.legis-pedia.com/QA/question/1947 | Blog/Q&A | 2026-11-11 | UNKNOWN | C | Side job norms; Labor Standards Act Art 12 case | Low | No primary law/MOL text read |
| S43 | Tasker (via search) | https://tasker.com.tw/help/article/4 ; https://uptogo.com.tw/?p=324922 ; https://www.yourator.co/articles/674 | Official/blog | 2026-11-11 | UNKNOWN | C | Fee conflict 9% vs 12%/6%; foreigners not allowed | Low | Official page fetch failed (Header overflow) |
| S44 | PRO360 | https://www.pro360.com.tw | Official site | 2026-11-11 | UNKNOWN | A | Platform title only | Low | No fee/payout info |

## bounties


| Source | URL | Type | Access date | Evidence level | Used for | Confidence | Notes |
|---|---|---|---|---|---|---|---|
| GitHub issue search (label 💎 Bounty / bounty) | https://github.com/search?q=label%3A%22%F0%9F%92%8E+Bounty%22+is%3Aopen&type=issues | API/search | 2026-11-11 | A | farm 比例、候選清單 | 高(原始清單)/中(農場判斷為本人分類) | 上限100筆 |
| GitHub search algora-pbc commenter | https://github.com/search?q=commenter%3Aalgora-pbc+is%3Aopen&type=issues | API/search | 2026-11-11 | A | Algora 新建 bounty 稀少 | 中 | 僅33筆 |
| onyx-dot-app/onyx#2281 | https://github.com/onyx-dot-app/onyx/issues/2281 | GitHub issue (gh api) | 2026-11-11 | A | USD250、競爭 PR | 高 | |
| PG-AGI/toingg-jarvis#13, #11 | https://github.com/PG-AGI/toingg-jarvis/issues/13 | GitHub issue | 2026-11-11 | A | USD5 | 高 | |
| nicolargo/glances#3485 | https://github.com/nicolargo/glances/issues/3485 | GitHub issue | 2026-11-11 | A/B | $1k label vs $1 實付 | 中 | 實付金額來自外部留言 |
| tenstorrent/tt-metal#64575 #64647 #62681 | https://github.com/tenstorrent/tt-metal/issues/62681 | GitHub issue | 2026-11-11 | A | 指派制、USD750/3000 | 高 | T&C: https://docs.tenstorrent.com/bounty_terms.html(未抓取) |
| outerbase/starbasedb#71 #72 | https://github.com/outerbase/starbasedb/issues/72 | GitHub issue | 2026-11-11 | A | 已頒發USD250 | 高 | |
| coollabsio/coolify#7642 | https://github.com/coollabsio/coolify/issues/7642 | GitHub issue | 2026-11-11 | A/B | Algora 下線傳聞 | 中 | 單一外部留言 |
| tari-project/universe#3518 | https://github.com/tari-project/universe/issues/3518 | GitHub issue | 2026-11-11 | A | 15000 XTM | 高 | USD 換算 UNKNOWN |
| microg/GmsCore#2843 | https://github.com/microg/GmsCore/issues/2843 | GitHub issue | 2026-11-11 | A/B | BountyHub USD2340 | 中 | |
| Spectral-Finance/lux#99; scratchdata#126/#170; revert#372/#551; zio*; EdgeChains*; dozer*; pgstrap#2; sola#157; QubesOS#10781 | https://github.com/<repo>/issues/<n> | GitHub issue | 2026-11-11 | A | 見 CSV | 中-高 | |
| algora.io home | https://algora.io/ | Web | 2026-11-11 | B | 首頁轉 recruiting;/bounties 404(curl) | 中 | |
| Web search "Algora shutting down 2026" | (WebSearch) | Web search | 2026-11-11 | C | 未找到 Algora 關閉公告 | 低 | 與 404 並存,關閉與否 UNKNOWN |
| Bot Farms and Dead Repos blog | https://marchantdev.github.io/blog/bot-farms.html | Blog | 2026-11-11 | C | 旁證(僅列於搜尋結果,未讀全文) | 低 | |

## freelance


| Source | URL | Type | Access date | Published/updated date | Evidence level | Used for | Confidence | Notes |
|---|---|---|---|---|---|---|---|---|
| Freelancer.com 個別 project 頁 (8 筆) | https://www.freelancer.com/projects/google-cloud-platform/gcp-kafka-bigquery-data-engineer (及 CSV id 1-8 之 URL) | 公開 job 頁 | 2026-11-11 | 頁面顯示 "Posted 1 minute ago" 等相對時間 (疑為 cache 假象) | A | job 欄位 | Medium | WebFetch 經 AI 摘要，非原始 HTML；部分欄位 (country/payment) 缺 |
| Freelancer.com category 列表 (python/apache-kafka/mongodb/etl/ai-agents/api-integration/data-migration/devops) | https://www.freelancer.com/jobs/ai-agents/ 等 | 公開列表 | 2026-11-11 | 即時列表 | B | 22 筆 listing-level 樣本、bids 數 | Medium | 僅 avg bid，非 client 預算 |
| Upwork public job pages | https://www.upwork.com/freelance-jobs/apply/DevOps-Engineer-Kafka-Streaming-Platform_~022074041868551510301/ | 公開 job 頁 | 2026-11-11 | UNKNOWN | C | 證明 403 | High | 4 個 URL 皆 HTTP 403；搜尋 snippet 有 listing 但無法驗證欄位，未納入 CSV |
| RemoteOK API | https://remoteok.com/api | Job board API | 2026-11-11 | 2026-11-07/09 | B | 2 筆 AI 職缺 | Low | 僅讀前 100k/654k 字元；多為受僱職缺，非 contract |
| WeWorkRemotely DevOps 類別 | https://weworkremotely.com/categories/remote-devops-sysadmin-jobs | Job board | 2026-11-11 | 2026-10 至 11 | B | 確認全為 Full-Time | Medium | 無 contract 標示，未納入 CSV |
| Confluent Community Forum | https://forum.confluent.io/t/freelance-role-kafka-developer/38359 | 論壇貼文 | 2026-11-11 | 2026-04-30 | A | Kafka contract $90/hr | Medium | 超過 60 天 |
| HN Algolia (Ask HN Freelancer? Nov 2026, id 50338744) | https://hn.algolia.com/api/v1/search_by_date?query=%22Ask%20HN%3A%20Freelancer%3F%20Seeking%20freelancer%3F%22&tags=story | API | 2026-11-11 | 2026-11-02 | A (存在) | 確認 thread 存在 | High | comment 內容查詢 0 hits，未能取得貼文 |
| Percona Database Health Audit | https://www.percona.com/services/database-health-audit/ | 廠商服務頁 | 2026-11-11 | 無日期 (c) 2026 | A | MongoDB health check 價格 | High | "starting from $11,400"; PDF + live session; 5-7 business days |
| AVP Consulting pricing | https://avp-consulting.pages.dev/pricing | 廠商價格頁 | 2026-11-11 | UNKNOWN | B | DB Health Check $490 | Medium | 小型獨立顧問，無 migration 專屬套餐 |
| Instaclustr Kafka Health Check PDF | https://www.instaclustr.com/wp-content/uploads/2020/08/Kafka-Health-Check_Consulting-Services-Package_August-2020.pdf | 廠商 PDF | 2026-11-11 | 2020-08 (另有 2025-03 版) | B | Kafka review 套餐，1-2 週 | Medium | 無公開價格 |
| Nextbrick Kafka consulting | https://nextbrick.com/apache-kafka-consulting | 廠商頁 | 2026-11-11 | UNKNOWN | C | 2-4 週 architecture review | Low | 僅搜尋摘要，未開頁 |
| Datavail MongoDB Health Check | https://www.datavail.com/service-overview/Datavail_SO-MongoDB_Health_Check_Services.pdf | 廠商 PDF | 2026-11-11 | UNKNOWN | C | 存在性 | Low | 僅搜尋結果，無價格 |
| Fiverr RAG chatbot gigs | https://www.fiverr.com/novatoresols/create-ai-chatbot-with-rag-and-custom-knowledge-base (及搜尋結果其他 gig) | Gig listing | 2026-11-11 | UNKNOWN | C | RAG 價格帶 | Low | 價格取自搜尋摘要，未開頁驗證 |
