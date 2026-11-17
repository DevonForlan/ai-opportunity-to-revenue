# 私有買家商業證據 Part A（Phase 2）

日期 2026-11-17。資料集：`03_PRIVATE_BUYER_DATASET_partA.csv`（56 列，id PA001-PA056）；來源表：`_sources/private_buyer_a.csv`。

## 方法與限制
- 方法：WebSearch 找線索，再用 WebFetch 實際讀頁面；僅記錄讀過的頁面（Ibexlabs 例外，只見 search snippet，標 UNVERIFIED）。
- 唯讀；403/404/410/TLS 錯誤頁面未繞過，已記錄於 `_sources`（supportyourapp 403、Microsoft partner 站 TLS、Zapier Premiere Property 404、4Spot 410）。
- 所有「成果」皆為來源自述（provider-reported 或 client-reported），未獨立查證。**沒有任何一列取得實際合約金額。**
- 評級：全部列最高為 PARTIALLY VERIFIED（來源為供應商或平台自行發布，非合約文件）。證據等級 B=平台代管或 Clutch Verified 評論（9 列），C=供應商自述或一般 Clutch 評論（47 列）。
- Clutch 評論者姓名依組織政策不記錄，只記企業名或類型。
- 日期欄多數 UNKNOWN：許多頁面無發布日（只有 2026 版權頁尾）。

## 計數（本檔結論）
| 指標 | 數量 |
|---|---|
| 總列數 | 56 |
| commercial_evidence_type：named_client_case_study | 15 |
| partner_story | 3 |
| provider_claim_only | 12 |
| marketplace_completed（Clutch 評論） | 26 |
| contract_value_public / testimonial_only | 0 / 0 |
| **真正「具名私有客戶 + 範圍 + 供應商」（計入商業參與）** | **13**（PA001-PA013） |
| 另有 1 列具名但買方是否私有 UNKNOWN（GO p.l.c.，AI audit） | 1（PA014，不計入） |
| 具名但非私有（非營利）| 1（Women First Digital） |
| 明示合約金額（contract_value_public） | **0** |
| 有任何價格資訊（皆為弱：Clutch 級距 16 列、供應商標價 2 列） | 18 列（含 1 列 Clutch 為 50k-199k） |

INFERENCE：13 列中絕大多數為 BotsCrew（7）與 Master of Code（2，另 GO p.l.c. 1 列身分不明）；兩家皆為中型 agency，非個人顧問。小型/solo 供應商的具名客戶證據幾乎只出現在 Clutch 評論（級距價格），且多為 <USD 10k。

## 主要發現
1. NEW EVIDENCE：13 筆具名私有客戶案例，涵蓋 support automation、RAG、內部知識助理，但**無一公開價格**。
2. NEW EVIDENCE：Clutch 評論提供唯一的價格訊號：Growwstacks（10 列）與 autoMEE（6 列）多為 <USD 10,000 級距；AI Automation Agency 360 為 USD 10k-49,999（4 列）、50k-199,999（1 列）。這些是級距，不是成交價。
3. NEW EVIDENCE：只有一個「AI assessment/audit」具名案例（Master of Code 對 GO p.l.c.），無價格；公開可見的 assessment 價格只有 Hammer 的 USD 25,000 標價（list price，非成交）。
4. NEW EVIDENCE：有重複合作證據的僅 Zipify（Master of Code 服務逾 2 年，頁面自述）與 Waggles（後續 workflows）。
5. NEW EVIDENCE：負面資料點：Growwstacks 一則雜貨店發票自動化評論回報準確率 <50%（目標 98%）且工期超出數倍（PA 對應列已標）。

## 解讀注意
- 平台故事（n8n Koralplay、Make Ascent Media、Microsoft Cassidy/RVezy）多為買方自建或 SaaS 使用，不是顧問採購，僅作需求訊號。
- Goodspeed 部落格列出的 StepStone/Musixmatch/Unbabel 未說明建置者，故為 provider_claim_only。
- 成果數字（如 S&B 250% ROI、Legendary.cx 節省 USD 20,919）皆為供應商自述，省下的金額不是價格。
- 最貼近目標產品（固定範圍 support-automation PoC）的列：S&B Filters（4 週，BotsCrew）、Zipify、LAQO（助理 2 週建置）。

## A. 具名客戶案例（named_client_case_study）
| id | 買方 | 私有 | 供應商 | 規模 | 範圍 | 價格 | 類型 | 成果(來源自述) |
|---|---|---|---|---|---|---|---|---|
| PA001 | Waggles Pet Resort | yes | Ridgeline Agency (Zapier Solution Partner) | boutique agency (size UNKNOWN) | Training-evaluation booking admin: outreach, scheduling, reminders, record updates | UNKNOWN | named_client_case_study | provider/platform-reported: '15-20 hours per week saved'; '75% reduction in admin time' |
| PA002 | El Ezaby (Egyptian pharmacy chain, 400+ branches) | yes | IT Visionary (AWS Partner, New Cairo) | SMB/mid-size partner (size UNKNOWN) | Generative AI chatbot giving pharmacists verified answers over academy knowledge base | UNKNOWN | named_client_case_study | provider/platform-reported (quote from client CTO on page): response time -70%, satisfaction +50%, resolution 3x, workload -25% |
| PA003 | LAQO Insurance (Croatia, digital insurer) | yes | Infobip (with Microsoft Azure OpenAI, Croatian Telekom delivery) | mid-large vendor | 24/7 GPT assistant for claims and general info on WhatsApp, handoff to agents | UNKNOWN | named_client_case_study | provider-reported: '30% of customer queries are resolved through the AI digital assistant' |
| PA004 | Game Room Shop (e-commerce retailer) | yes | Aissist.io (AI support vendor) | startup vendor (size UNKNOWN) | AI agent for pre-sales/support questions on inventory, pricing, shipping, order status | UNKNOWN | named_client_case_study | provider-reported: 'roughly 60% of inbound conversations get fully resolved without a human' |
| PA005 | GsmServer (telecom/electronics online retailer) | yes | BotsCrew | boutique-to-mid agency (size UNKNOWN) | Website chatbot for FAQs, order status, purchase help | UNKNOWN | named_client_case_study | provider-reported: '72.28% of all customer requests' automated |
| PA006 | Pluggi (cannabis e-commerce startup) | yes | BotsCrew | boutique-to-mid agency | White-label AI budtender for dispensaries | UNKNOWN | named_client_case_study | provider-reported: '$0 to over $10,000 MRR'; '15.6x average ROI'; cart value +28% |
| PA007 | Hill+Knowlton Strategies (communications firm) | yes | BotsCrew | boutique-to-mid agency | WhatsApp chatbot collecting user info and handling pitch bookings | UNKNOWN | named_client_case_study | provider-reported: 149 bookings vs target 100 |
| PA008 | Legendary.cx (customised hair/skin care brand) | yes | BotsCrew | boutique-to-mid agency | Automate routine subscription/order-change email requests using client templates | UNKNOWN | named_client_case_study | provider-reported: 'savings of $20,919 in just 30 days' (a saving, not a price) |
| PA009 | S&B Filters (US automotive air-filter maker) | yes | BotsCrew | boutique-to-mid agency | Rebuild CEO's MCP/NetSuite prototype for production; internal order data + customer site assistant | UNKNOWN | named_client_case_study | provider-reported: 50% of requests automated; 24x faster first response; '250% ROI first year'; '$140k annual cost savings' |
| PA010 | Kravet Inc (luxury home furnishings, ~1,000 staff) | yes | BotsCrew | boutique-to-mid agency | Custom internal AI assistant over messy/outdated data across departments | UNKNOWN | named_client_case_study | provider-reported: reply accuracy '<60% to nearly 90%' |
| PA011 | Cartland Law (Australian tax law firm; product 'Ailira') | yes | BotsCrew | boutique-to-mid agency | Chatbot combining legal research with automated drafting for B2B/B2C | UNKNOWN | named_client_case_study | provider-reported qualitative only ('automated key processes') |
| PA012 | Zipify (e-commerce software company) | yes | Master of Code Global | mid-size agency (size UNKNOWN) | AI co-pilot for support agents + dashboard + reports | UNKNOWN | named_client_case_study | provider-reported: '65% faster response time', '30% lower operating costs', 'CSAT 88%' |
| PA013 | BoomBeauty (beauty-sector brand) | yes | Master of Code Global | mid-size agency | AI SMS assistant for routine questions + proactive checkout recovery | UNKNOWN | named_client_case_study | provider-reported: '40-60% T1 Load Cut' (no baseline) |
| PA014 | GO p.l.c. (Malta telecom) | unknown | Master of Code Global | mid-size agency | Audit of existing web assistant and GenAI-readiness roadmap | UNKNOWN | named_client_case_study | none stated (deliverables only) |
| PA056 | Women First Digital (reproductive-health non-profit) | no | BotsCrew | boutique-to-mid agency | Migrate Ally chatbot, fix multilingual, add analytics, new GPT chatbot Myka | UNKNOWN | named_client_case_study | provider-reported: 52% annual cost saving |

## B. 平台/夥伴故事（不計入）
| id | 買方 | 私有 | 供應商 | 規模 | 範圍 | 價格 | 類型 | 成果(來源自述) |
|---|---|---|---|---|---|---|---|---|
| PA015 | Koralplay (gaming/betting software, ~85 staff) | yes | none (built in-house on n8n) | n/a | L2 payment ticket automation, reporting, release notes, QA steps | UNKNOWN | partner_story | provider-reported (n8n page): 70% of payment tickets automated in one market; '616 hours per week' |
| PA016 | RVezy (RV rental, via Cassidy platform) | yes | Cassidy (AI workflow SaaS) | startup | Centralised knowledge base and workflows for customer support | UNKNOWN | partner_story | provider-reported: 'over 10 hours per week' saved by support team |
| PA017 | Ascent Media (Munich social-media agency, now ARETI) | yes | none (self-built; Make certified partner) | n/a | Internal workflows, client onboarding automation, cross-system integration | UNKNOWN | partner_story | provider-reported (CEO quote): '500%' efficiency on one workflow |

## C. 供應商自述/匿名客戶/標價（不計入）
| id | 買方 | 私有 | 供應商 | 規模 | 範圍 | 價格 | 類型 | 成果(來源自述) |
|---|---|---|---|---|---|---|---|---|
| PA018 | StepStone (jobs platform) | yes | UNKNOWN (builder not stated) | UNKNOWN | 200+ production workflows for candidate data, job syndication, CRM/ATS sync | UNKNOWN | provider_claim_only | provider-reported: prototyping 'two weeks to two hours' |
| PA019 | Musixmatch (music data company) | yes | UNKNOWN (builder not stated) | UNKNOWN | Replace manual data pipelines, reporting scripts, integrations | UNKNOWN | provider_claim_only | provider-reported: '47 days of engineering time freed' |
| PA020 | Unbabel (translation company) | yes | UNKNOWN (builder not stated) | UNKNOWN | Task routing, QA checks, notifications, reporting around translation pipeline | UNKNOWN | provider_claim_only | provider-reported: '51% reduction in manual operational work' |
| PA021 | Anonymous US online store (3M+ shoppers) | yes | instinctools | mid-size software house | 6-agent triage/prioritise/route/draft/compliance pipeline for ~5,000 requests/day | UNKNOWN | provider_claim_only | provider-reported: processing 4x faster; first response -75%; accuracy 92% with RAG; CSAT +15% |
| PA022 | Anonymous US supermarket chain (280+ stores) | yes | Persistent Systems | large SI | Website RAG chatbot over 110+ PDFs (recipes/magazine) | UNKNOWN | provider_claim_only | provider-reported: search time -20%, order value +25% |
| PA023 | Anonymous 'one of Europe's largest software companies' | yes | deepsense.ai | mid-size AI consultancy | Governed ChatGPT Enterprise deployment for 1,500+ users | UNKNOWN | provider_claim_only | provider-reported: launched on schedule for 1,500+ users |
| PA024 | Anonymous 'leading financial company' | unknown | nClouds (AWS consulting partner) | boutique-to-mid | GenAI chatbot for customer queries replacing manual handling | UNKNOWN | provider_claim_only | provider-reported: response time -40%, CSAT +25% |
| PA025 | Anonymous US flexible-staffing company (NDA) | yes | BotsCrew | boutique-to-mid agency | Rebuild SEO article workflow as AI pipeline with WordPress publishing | UNKNOWN | provider_claim_only | provider-reported: 16h to 1.5h per article; inconsistent figures on page |
| PA026 | 10 anonymous industry-labelled clients | unknown | Achiya (solo/boutique automation builder) | solo/boutique | 10 builds e.g. WhatsApp order bot, RFQ quote drafting, policy extraction | UNKNOWN | provider_claim_only | mostly capabilities, not measured results |
| PA027 | no client named | unknown | Hammer | UNKNOWN | Fixed-fee AI opportunity assessment and roadmap | 25000 | provider_claim_only | n/a |
| PA028 | no client named | unknown | Growwstacks Automation (Make Platinum Partner) | boutique agency | Self-stated typical project band | 5000-10000 typical; from 3000; up to 15000+ | provider_claim_only | provider-reported aggregate: '2000+ projects', '$2.4M+ client savings' |
| PA029 | Rizz Wireless | unknown | Ibexlabs (AWS partner) | boutique-to-mid | RAG design, Bedrock model selection, deployment for customer support (per snippet) | UNKNOWN | provider_claim_only | none seen |

## D. Clutch 評論（marketplace_completed，級距價格，弱證據）
| id | 買方 | 私有 | 供應商 | 規模 | 範圍 | 價格 | 類型 | 成果(來源自述) |
|---|---|---|---|---|---|---|---|---|
| PA030 | International anti-poverty nonprofit | no | AI Automation Agency 360 | boutique agency | Predictive engagement model, automated content distribution, CRM-integrated dashboard | 50000-199999 (bracket) | marketplace_completed | client-reported (review): +35% campaign engagement; -60% manual data processing |
| PA031 | Physician-led women's health publisher (digital media) | yes | AI Automation Agency 360 | boutique agency | Real-time transaction monitoring, automated risk reporting, dashboard | confidential | marketplace_completed | client-reported qualitative only |
| PA032 | Opportunities Exchange (nonprofit) | no | AI Automation Agency 360 | boutique agency | Predictive funding analytics, automated reporting, provider interfaces | 10000-49999 (bracket) | marketplace_completed | client-reported: -30% admin overhead |
| PA033 | Enterprise WordPress company | yes | AI Automation Agency 360 | boutique agency | Content approval/publishing automation, predictive dashboard, support chatbot, AI strategy roadmap | 10000-49999 (bracket) | marketplace_completed | client-reported: -45% time to publish; '60% of support tickets handled autonomously' |
| PA034 | Shopify/e-commerce digital agency (Lithuania) | yes | AI Automation Agency 360 | boutique agency | Trend prediction model, product-description generation, Shopify analytics dashboard | 10000-49999 (bracket) | marketplace_completed | client-reported: +15% AOV; 30% shorter design-to-dev turnaround |
| PA035 | Scientific-instruments manufacturer (Denmark) | yes | AI Automation Agency 360 | boutique agency | NLP + recommendation + workflow generator + conversational UI inside client software | 10000-49999 (bracket) | marketplace_completed | client-reported: -63% onboarding support tickets |
| PA036 | SmartBran (business-process-automation platform) | yes | AI Automation Agency 360 | boutique agency | Compliance checks, data management, reporting dashboard (healthcare data) | confidential | marketplace_completed | client-reported qualitative only |
| PA037 | 1Strike.ai (risk-detection company, Poland) | yes | AI Automation Agency 360 | boutique agency | Extract scanned bills of lading into database + tracking dashboard | confidential | marketplace_completed | client-reported: hours to minutes (no figures) |
| PA038 | Stratwell Partners (business services, SF) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | Diagnostic tool, lead qualification, insights database | confidential | marketplace_completed | client-reported: +36% new leads; up to -55% BD time |
| PA039 | Destler Real Estate Group (NJ) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | Calls and recordings into real-estate CRM via API | <10000 (bracket) | marketplace_completed | client-reported: +15% appointment rate |
| PA040 | Grocery store (London; name not given) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | Extract invoice data, compare prices, build price DB | <10000 (bracket) | marketplace_completed | client-reported NEGATIVE: <50% accuracy vs 98% goal; ran 4+ months vs 2-week proposal |
| PA041 | Anonymous marketing company (Australia) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | POS integrations, custom CRM, AI/automation | confidential | marketplace_completed | client-reported qualitative only |
| PA042 | Roof AI Lead Recovery (Ohio) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | Website build and multi-platform automation | <10000 (bracket) | marketplace_completed | none yet |
| PA043 | Smile Pouches (e-commerce, Canada) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | Custom plug-in linking two websites | <10000 (bracket) | marketplace_completed | client-reported: ~30 min/day saved; more sales |
| PA044 | ZHK Tuition (education, England) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | Replit-built app enhancements | confidential | marketplace_completed | none yet |
| PA045 | Western States (hospitality, Utah) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | Automated extraction workflow | confidential | marketplace_completed | client-reported expectation: ~16 labour hours/month |
| PA046 | 6FDS (education, UAE) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | Automations + custom tracking sheet | confidential | marketplace_completed | client-reported estimate: ~5 hours/week |
| PA047 | nefsy (e-commerce, Dubai) | yes | Growwstacks Automation (Make Platinum Partner) | boutique agency | AI chatbot, social content creator, voice agents | <10000 (bracket) | marketplace_completed | client-reported: 'as expected' |
| PA048 | Property maintenance company (London) | yes | autoMEE | boutique agency | Voice bot matching trade partners to jobs; recruitment CRM work | <10000 (bracket) | marketplace_completed | client-reported: job allocation time -40%; acceptance +25% |
| PA049 | HORECA food service company (Poland) | yes | autoMEE | boutique agency | Chatbot for HORECA customers | <10000 (bracket) | marketplace_completed | none reported ('project moved') |
| PA050 | Crown Security Services Ltd (UK) | yes | autoMEE | boutique agency | Website bot and AI lead gen | <10000 (bracket) | marketplace_completed | none quantified |
| PA051 | Re Crew HR (construction staffing, Poland) | yes | autoMEE | boutique agency | Communication platform, social customer search, AI add-ons | confidential | marketplace_completed | none quantified |
| PA052 | KL Law Polska (insolvency law firm) | yes | autoMEE | boutique agency | Automation to cut marketing cost and raise sales | confidential | marketplace_completed | client-reported: 'Increase of income' (no figure) |
| PA053 | Anglotec Ltd (language/tech education, UK) | yes | autoMEE | boutique agency | 24/7 AI help-desk chatbots | <10000 (bracket) | marketplace_completed | none quantified |
| PA054 | GNOSIS Technologie (IT services, LA, 11-50 staff) | yes | newbrainsai | boutique/solo-scale (UNKNOWN) | AI chatbots for reviewer's hotel clients, scraping agent, outreach tool | <10000 (bracket) | marketplace_completed | client-reported: 'over 1,000 leads in a short period' |
| PA055 | StarTalers (financial services, Luxembourg) | yes | BotsCrew | boutique-to-mid agency | Messenger chatbot taken over from failed vendor | 10000-49999 (bracket) | marketplace_completed | client-reported: first version in ~3 weeks; ~350 users |

## 未完成/限制
- 未找到：具公開合約金額的私有買家案例（0）、Anthropic/OpenAI/Google Cloud 由顧問夥伴為 SMB 建置的具名故事（搜尋結果多為大型企業或供應商自身案例，如 Kodif/Tidio/Decagon，未列入）。
- 最低目標 30 列已達（56 列），但其中符合嚴格定義者僅 13 列。
