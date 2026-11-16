# 03 AI 供給端競品矩陣:獨立 / 個人 / 精品(boutique)服務商

## 方法與限制(務必先讀)

- **範圍**:個人顧問、fractional AI engineer、個人或小團隊的 productized AI 服務。資料集見 `04_AI_COMPETITOR_DATASET_solo.csv`(AI_SUPPLY schema,ids AS001-AS053),來源清單見 `_sources/ai_competitors_solo.csv`,分析見 `11_SOLO_CONSULTANT_MODEL.md`。
- **擷取日期**:2026-11-16(系統日期;brief 寫 11-18 起,未改動)。唯讀研究:未聯絡任何人、未註冊、未繞過登入或反爬。
- **驗證標準**:VERIFIED = 我實際讀到該頁面本身或 API payload(含 n8n community 的 Discourse JSON);PARTIALLY VERIFIED = 只有搜尋摘要、標題或 403/404 頁面。Evidence level:A = 賣方自家官網(對「賣方如何定位與標價」是第一手,但成效宣稱仍是自述)、B = 平台頁/社群貼文/合作夥伴目錄、C = 摘要或弱訊號。
- **重要限制**:(1) 這是**供給端行銷證據(provider_marketing)**,不是買方需求,也不是成交價;公開標價 != 實際成交價。(2) 沒有任何一列是 purchase 證據;無法得知轉換率、成交量、營收。(3) 多個 `.pages.dev` / `vercel.app` 站點無法確認賣方真實存在或是否為模板站;其中案例數字一律視為自述。(4) Upwork/Fiverr 多數 403,只能留 2 列 snippet-only;Fiverr 未納入逐列分析。(5) 樣本由搜尋引擎排序挑出,偏向「會做 SEO 的賣家」,**不是**隨機樣本,不可推論市場比例。(6) 組織政策:僅記錄品牌、帳號 handle、公開營業資訊,不記個人傳記。
- **evidence_type**:全部 53 列皆為 provider_marketing(沒有 pain / hiring / purchase)。

## 計數

| 維度 | 數量 |
|---|---|
| 總列數 | 53 |
| company_or_independent | independent 43;boutique 10 |
| 真正個人/獨立且實際讀過頁面(independent + VERIFIED) | 39 |
| verification_status | VERIFIED 49;PARTIALLY VERIFIED 4 |
| evidence_level | A 27;B 22;C 4 |
| 來源類型 | 個人/品牌官網 27;Contra 11;n8n community 6;Zapier partner directory 2;Upwork(403)2;PeoplePerHour 1;ComeUp 1;Make community 1;Ragic community 1;PRO360 1 |
| 台灣(country=Taiwan) | 4(Contra x2、Ragic community、PRO360);另有 1 篇台灣市場指南列入 sources 但不是賣方 |

註:來源類型為依 URL 網域手算,可能有 ±1 的分類誤差(例如 pages.dev 站歸入官網)。

## 矩陣(精簡;完整欄位請看 CSV)

| id | provider | 類型 | 國家 | 主要服務 | 公開價格 | 最低承諾 | 信任訊號(節錄) | 驗證 |
|---|---|---|---|---|---|---|---|---|
| AS001 | Automation Engineer (solo; Zapier/n8n… | independent | UNKNOWN | Tiered Spark/Audit/Sprint/Build/Stack automation packages + Care reta… | UNKNOWN (no price tags; quote after free 30-min call) | Care retainer 3-month min; Au… | Free intro call; client owns code; NDA on request; 1-business-day reply; 50/50 … | V |
| AS002 | paul-okhrem.com (solo fractional Chie… | independent | Czechia (Prague) | Fractional CAIO/CTO seat; scoped consulting; AI Growth Readiness Audi… | USD 1000/h (80h min = 80000); 30000/mo (6-mo min); audit 80000; works… | 80h; 6-month retainer | Published fees w/ review date and change log; NDA/conflicts review; related-par… | V |
| AS003 | Contra: preston_cardwell (AI Automati… | independent | USA (Houston) | Monthly AI automation advisory+implementation subscription | USD 3400/month | UNKNOWN | Self-described CPA (unverified); booking link; 3 followers | V |
| AS004 | Contra: prateek_dev (Fractional CTO &… | independent | India (Mumbai) | Monthly technical partner retainer (up to 40h) | From USD 4000/mo (other listings: USD 50/h; MCP server USD 1500) | 30-day cancellation notice | Itemized scope; 2 followers | V |
| AS005 | Contra: jonathan_guez (n8n/Make/Zapie… | independent | Israel (Holon) | Automation Audit then Build | Audit USD 150 fixed; build typically USD 500-3000; lead-gen stack 150… | UNKNOWN | Claim '10-20 h/week saved' (unverified); cal.com booking; 1 follower | V |
| AS006 | Contra: cheyne_smith (AI agents workf… | independent | USA (Murrieta) | Bounded workflow consulting package | From USD 250; 60-min consult USD 95 | UNKNOWN | Explicit scope limits (no production apps/live integrations/account access with… | V |
| AS007 | Contra: adreespro (Fractional Senior … | independent | Pakistan (Lahor… | Embedded part-time AI engineering retainer | USD 5000/mo (20h/wk); USD 9000/mo (40h/wk) | 1 month | Free 30-min discovery; proposal within 48h; 2 followers | V |
| AS008 | Andrew Zoll (AI Efficiency Consultant… | independent | USA (Pueblo CO) | Productized AI Efficiency Audit (no implementation in this offer) | USD 997 flat | none | Pay-nothing guarantee if <5h/week automatable work found; LinkedIn; author also… | V |
| AS009 | negodiuk.ai (solo Fractional AI Offic… | independent | UNKNOWN | Paid AI Audit -> AI Sprint -> Full AI Operating System | UNKNOWN (market retainer benchmark 3000-5000/mo cited, not own price) | UNKNOWN | Free 6-question audit tool; free 30-min call; press page; 13 yrs distribution b… | V |
| AS010 | sagnikbhattacharya.com (solo educator… | independent | UNKNOWN | 1:1 AI implementation consultation + courses | UNKNOWN (no prices on page) | UNKNOWN | Public writing; YouTube/TikTok/Instagram; courses; content-led lead generation | V |
| AS011 | The AI Architects (Email Alchemy LLC;… | independent | UNKNOWN (US/UK … | Done-for-you AI builds + maintenance + Team Enablement/Embedded Advis… | Build from USD 10000; maintenance 500-1000/mo; Enablement 2500/mo; Ad… | 3-month retainer minimum | 69,000+ followers claimed; guarantee: does what brief says / month-2 free if no… | V |
| AS012 | techconcepts.org AI Ops Sprint (solo … | independent | Spain (Madrid) | AI Ops Sprint Lite/Standard/Plus | UNKNOWN (amounts not shown) | UNKNOWN | Scarcity claim 'taking 3 new clients'; ex-Yandex/EY claim; runs on client infra… | V |
| AS013 | unlocked-consulting (solo inferred) | independent | Germany (Munich) | AI Second Opinion; AI Opportunity Audit; Company Know-how build; Exec… | UNKNOWN (no amounts) | UNKNOWN | Free 30-min call; 1-page proposal within 48h; limits written in contract; clien… | V |
| AS014 | Outright Mental studio (solo-operated) | independent | UNKNOWN | Feasibility Read; AI Capability Sprint; Agentic SDLC Enablement; Frac… | Feasibility USD 4500; Sprint USD 9500; SDLC USD 18000; leadership USD… | UNKNOWN | 25 yrs claim; public open-source; fixed pricing; 1-day reply; go/no-go built in | V |
| AS015 | dialedops (Indiana; appears solo) | independent | USA (Westfield … | AI Operations Sprint for owner-operated service businesses | USD 7500 design-partner (testimonial+case study+2 intros in exchange)… | UNKNOWN | Fixed price/no change orders; written proposal listing permissions; no client p… | V |
| AS016 | Contra: Sarunas Simaitis (AI Audit 30… | independent | Lithuania (Viln… | 30-minute AI diagnostic session; AI Feasibility Study listed USD 900 | USD 75 session; feasibility study USD 900 (page ambiguous) | none | Contra profile only; no ratings/certs | V |
| AS017 | Contra: sobhan_bahrami (AI infra & au… | independent | Hungary (Budape… | Fixed-price AI Infrastructure & Automation Audit | From USD 350 | none | Audit fee credit asked in FAQ (answer not shown); 6 followers | V |
| AS018 | Tyler Willis (OARS standard author; s… | independent | UNKNOWN | AI Readiness + Revenue Infrastructure Audit (website AI-operability) | USD 2500 single-site to 5000 multi-property | none | Authors own standard; free scanner; NDA; read-only access; narrow niche (not ge… | V |
| AS019 | Graham Mann (solo; diagnostic audit +… | independent | UNKNOWN | Free fit call -> diagnostic audit -> implementation sprint | Audit USD 1500+; sprint USD 2500+; fit call free | none | Capacity cap 2 engagements/quarter; NDA before call; 2-business-day reply | V |
| AS020 | Contra: prem_patel / Nex Automations … | independent | UNKNOWN | Make.com AI automation builds + 5-day audit | From USD 50/h; 5-day audit USD 499 (credited); custom app USD 1200 | UNKNOWN | Make Level 5 cert (valid to 2028) with verification links; claims 210+ clients/… | V |
| AS021 | Zapier directory: Mike the Automator … | independent | Puerto Rico (Sa… | Zapier automations/fixes/custom integrations incl. AI bots | Budget bands USD 251-500 up to 10001-200000; minimum spend USD 200; p… | USD 200 min spend | Free discovery call; 8 yrs; client logos; partner directory badge | V |
| AS022 | Zapier directory: BizPilot (solo) | independent | USA (Denver) | Zapier build/fix/implementation/support | Budget bands USD 251-500 up to 10001-200000; minimum spend USD 250 | USD 250 min spend | Free discovery call; 12+ yrs ops background | V |
| AS023 | PeoplePerHour hourlie: Rashid A. (RAG… | independent | Germany | Fixed-price RAG chatbot on up to 20 docs | USD 250 base; WhatsApp +150 | none | Platform escrow/money-protection badge; 7+ yrs Python claim | V |
| AS024 | ComeUp: IliassWakkar (RAG chatbot) | independent | UNKNOWN | Micro-priced RAG chatbot gig with add-ons | EUR 39.39 base; add-ons EUR 9.85-34.46 | none | Escrow-style payment on validation; new account with no sales | V |
| AS025 | n8n Community post: ck_lu (n8n reliab… | independent | UNKNOWN | Free 3-finding triage then USD 45 workflow reliability audit | Audit USD 45; fixes USD 120-260; monitoring USD 99/mo | none | Public sample audit and code as proof; no instance access; post got 3 replies/1… | V |
| AS026 | n8n Community post: Thomas_Geoffroy (… | independent | France | Single-defect JS/Python data-mapping fix around n8n | USD 60 | none | PayPal within 3 days; fixture sample; 2 replies/110 views | V |
| AS027 | n8n Community post: TY18 (cautomation… | independent | Italy (Turin) | n8n builds for construction-trade businesses and agencies; white-label | UNKNOWN | UNKNOWN | Vertical niche (construction); portfolio site; 2 replies/111 views | V |
| AS028 | n8n Community post: Juan_Patak (small… | independent | UNKNOWN | Small n8n/AI automation projects | UNKNOWN | none | Early-stage; 1 reply/33 views | V |
| AS029 | n8n Community post: EdwinSamoz (Germa… | independent | Germany | Fixed-price n8n packages; self-hosted GDPR-friendly | UNKNOWN | small first project at cost o… | Admits no clients yet; discounted first project; GDPR positioning; 3 replies/10… | V |
| AS030 | Make community: ApexSystematic (apexs… | independent | UNKNOWN | Fixed-price AI automations for professional-services firms | UNKNOWN | none | Free workflow audit; claims pays back <3 months; profile bio read via Discourse… | PV |
| AS031 | kevinleary.net (solo senior engineer) | independent | USA (Boston) | AI consulting: LLM integration, RAG, agents/MCP, data Q&A, workflow a… | UNKNOWN | UNKNOWN | 18 yrs; GitHub; Clutch; Smashing Magazine author; security practices stated | V |
| AS032 | rohitraj.tech (solo forward-deployed … | independent | India (Bengalur… | Fractional FDE retainer or fixed-scope pilot; MCP integration; traini… | UNKNOWN | UNKNOWN | Free 30-min scoping; NDA; public GitHub; 'evals not vibes'; pilot framed as pro… | V |
| AS033 | jxnl.github.io (Jason Liu) | independent | UNKNOWN | Formerly consulting/cohort training; no longer taking engagements | UNKNOWN | n/a | Public-writing-led personal brand; stopped selling services (brand leverage -> … | V |
| AS034 | kunalganglani.com (solo senior staff … | independent | Canada (Toronto) | Architecture and production-readiness review of agent/RAG/LLM systems… | UNKNOWN | none | Free 20-min intro call; 220+ published technical articles; 4M+ search impressio… | V |
| AS035 | Contra: sergiunicoara (AI System Audi… | independent | Romania (Timiso… | 5-day audit of existing LLM/RAG/agent system | From USD 750 | none | 3 followers; technical sample write-ups | V |
| AS036 | robertwinters-website.pages.dev (solo… | independent | France | Fractional; Architecture Review; Sprint Project (data eng + AI/LLM in… | UNKNOWN | UNKNOWN | ~20 yrs; prior leadership roles; takes 2-3 clients at once; GitHub; (data-platf… | V |
| AS037 | Contra: ycintelligence (Taipei, Custo… | independent | Taiwan (Taipei) | Custom AI agent & RAG implementation | UNKNOWN | none | Pro label; booking link; 3 followers; LINE deploy = local-market fit | V |
| AS038 | Contra: Payne Chen (Taichung, RAG cha… | independent | Taiwan (Taichun… | AI chatbot with RAG on client documents | UNKNOWN | none | Security claim only; no certs/testimonials | V |
| AS039 | Ragic community: zxc02621948 (Taiwan … | independent | Taiwan | Ragic low-code developer/consultant with n8n, chatbots, LINE/ERP inte… | UNKNOWN | none | Community-forum availability post (Aug 2026); no reviews/portfolio | V |
| AS040 | PRO360 (Taiwan) AI consultant listing… | independent | Taiwan (Taipei) | AI consulting: customer-service AI flow, chatbot, AI tool training; p… | UNKNOWN (platform category range NT$30000-100000/mo consulting, NT$10… | none | Platform ID verification and payment protection; Google ads certification; AI c… | V |
| AS041 | Ridgeway AI LLC | boutique | USA | AI Opportunity Audit -> consulting plan -> contracting (build/run) ->… | UNKNOWN (page shows range label only) | Contracting 3-month min then … | Free mapping call; plan portable to any builder; data stays with client | V |
| AS042 | Penrose Development LLC | boutique | USA (Twin Falls… | Discovery Workshop; project builds; monthly retainer; hourly | Workshop USD 449 (4h) / 849 (8h); workflow USD 1800; multi-process US… | none | Free consult; code ownership; physical PO box; clear scoping before billing | V |
| AS043 | Vantage Point (Cockrum Consulting LLC) | boutique | USA/Bulgaria (D… | Fractional AI Architect retainer | USD 1800 / 3400 / 6400 per month (8/16/32h) | 3-month minimum | Partner badges; AppExchange/HubSpot Marketplace listings; scope last reviewed 2… | V |
| AS044 | Jester Studio Works LLC | boutique | USA (Florida) | Tiered audits + fixed build + retainer | Audit USD 50 / 100 / 300; build USD 3000-7500; retainer USD 1000-2000… | retainer 3-month min | LLC; privacy policy/terms; price-ladder entry audit at USD 50 | V |
| AS045 | Ascero AI | boutique | USA (Waltham MA) | 12-offer productized menu (audits, sprints, retainers, agents) | USD 500 audit; 1500 setup+750/mo; 2997 weekend sprint; 4997 mini-audi… | varies | 30-day fit guarantee; weekend sprint money-back; named co-founders; trust page;… | V |
| AS046 | getaiaudit.ai | boutique | UNKNOWN | USD 197 productized AI audit (48h) | USD 197 standard; USD 244 rush; optional implementation ~USD 1500-3000 | none | 5-hour-back guarantee or full refund; published sample PDFs; no certs; seller i… | V |
| AS047 | Main and Machine | boutique | USA (Denver; Ph… | AI Readiness Audit -> Implementation Sprint -> Managed Services | Audit USD 3500-8500 | none | Free 30-min assessment; free workflow plan; sample deliverable labelled fiction… | V |
| AS048 | genai-data-solutions (2-person EU) | boutique | EU (country UNK… | Paid Discovery; AI Opportunity Audit; LLM Cost and Quality Audit; eva… | UNKNOWN (no amounts) | none | Open-source MIT eval toolkit on GitHub; discovery fee credited if signed within… | V |
| AS049 | aw-site RAG Pipeline Audit (founder-l… | boutique | USA (Sheridan W… | RAG Pipeline Audit -> Fix Sprint -> Quality Retainer | UNKNOWN (search snippet claimed 3000-6000; not on page) | audit required first | Founder book; free RAG debug checklist (email-gated) | V |
| AS050 | Dan Cumberland Labs | boutique | USA | AI strategy/fractional AI officer positioning for engineering and con… | UNKNOWN (page lists market benchmarks only; own prices UNKNOWN) | UNKNOWN | OpenAI partner logo; ACEC member; AI-use disclosure page; content-led | V |
| AS051 | n8n Community: for-hire $1500 fixed o… | independent | UNKNOWN | One n8n workflow in 5 business days, signed scope to tested handover | USD 1500 fixed (search snippet) | none | Written scope + acceptance; page 404 on fetch; unverifiable beyond snippet | PV |
| AS052 | Upwork project catalog: AI Readiness … | independent | UNKNOWN | Productized AI readiness audit + roadmap on Upwork | UNKNOWN | none | Page 403; title/search snippet only; shows audit-as-catalog-product exists on U… | PV |
| AS053 | Upwork project catalog: n8n workflows… | independent | UNKNOWN | n8n workflow builds tiered by days | USD 130-1450 (from listing title) | none | Page 403; price range only from title | PV |

V = VERIFIED;PV = PARTIALLY VERIFIED。

## 觀察(INFERENCE,僅限本樣本)

1. 本樣本中,**以付費 audit / diagnostic / review 當入口**的獨立賣家最常見(見 `11_SOLO_CONSULTANT_MODEL.md` 的手動統計),但這同時也是搜尋關鍵字(我搜 audit / assessment)造成的偏誤。
2. 公開標價的 audit 區間很寬(USD 45 到 5,000 為主;另有 USD 80,000 的高階顧問離群值);便宜端多半是平台/論壇上無評價的新帳號。
3. 台灣獨立賣家(4 列)全部不公開價格(contact for price / 洽談後報價),且多數只有 Contra/社群頁面,沒有可驗證的案例。
4. 與 Phase 1A 的 BASELINE 對照:Phase 1A 已列出台灣收款與接案渠道;本檔只補充**供給端定位證據**,不重做渠道與稅務。
