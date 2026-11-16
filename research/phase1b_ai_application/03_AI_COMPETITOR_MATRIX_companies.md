# 03 AI 供給端競品矩陣 — 公司/顧問/代理商 (AI_SUPPLY, companies)

## 方法與限制

- 方法:WebSearch 找出公開提供 AI 評估/PoC/sprint/自動化/導入服務的供應商,再以 WebFetch 讀取供應商自己的頁面(evidence A)。每列的 url 皆為實際讀取或實際看到的頁面。日期 2026-11-16。所有統計由 `04_AI_COMPETITOR_DATASET_companies.csv` 的 43 列計算得出。
- 限制:(1) WebFetch 以小模型摘要頁面,非逐字原文,欄位寫 UNKNOWN 代表摘要未見,不代表頁面一定沒有;(2) 供應商牌價 != 成交價;供應商行銷 != 買方需求;評分、案例、ROI 皆為自述,未獨立驗證;(3) 搜尋結果含大量 *.pages.dev / lovable.app 的疑似低品質或模板站,已刻意排除;(4) 台灣在地供應商公開報價極少,台灣列只有 4 列(cacaFly、iKala、精誠、叡揚;另 GroundAI 國別 UNKNOWN 但為繁中台灣市場頁),其中 cacaFly 首頁未列 AI 範圍、精誠/叡揚為新聞稿,皆僅 PARTIALLY VERIFIED,且四列價格皆 UNKNOWN;(5) 樣本為方便取樣(搜尋可見者),偏向會公開價格的英語系小型供應商,不代表整體市場;(6) 未能讀取:Acropolium(403)、MojoTech(連線失敗)、vantagepoint.io(404),未列入;(7) 貨幣依頁面原文,XYZ 的 'BD' 未定義、SSW 的 AUD 為由 GST 推測。
- 本檔不含 MongoDB/資料庫能力加權;僅比較供應商公開服務型態。

## 計數

總列數:**43**

### 依 verification_status
| status | 數量 |
|---|---|
| VERIFIED | 38 |
| PARTIALLY VERIFIED | 5 |

### 依 evidence_level
| level | 數量 |
|---|---|
| A | 41 |
| B | 2 |

### 依 evidence_type
全部為 provider_marketing(供應商自家頁面或新聞稿);**0** 列為 purchase(沒有任何公開成交/合約資料)。

### 依國家(自 country 欄位粗分)
| country | 數量 |
|---|---|
| UNKNOWN | 17 |
| US | 9 |
| Taiwan | 4 |
| Poland | 3 |
| UK | 3 |
| India | 2 |
| Australia | 2 |
| Other(DACH) | 1 |
| Other(Netherlands) | 1 |
| Other(Canada) | 1 |

### 依主要服務類型(各列取一個主類型)
| type | 數量 |
|---|---|
| assessment / readiness audit / strategy workshop / discovery | 19 |
| PoC / sprint (fixed-scope build) | 9 |
| workflow-automation (n8n/Make/Zapier) | 5 |
| rag-knowledge / knowledge platform | 5 |
| eval-guardrail / AI governance / red teaming | 3 |
| agent-integration (embedded pods) | 1 |
| internal-assistant (ChatGPT/Copilot rollout) | 1 |

## 重複出現的服務型態與範圍

- **Assessment-first(評估/稽核/工作坊)**:19/43 (44%),為最大宗。典型範圍:流程盤點、use-case 評分、readiness 評估、roadmap。典型時程 1 天至 4 週(Main & Machine 2-4 週;WorkWise 1-2 週;Peerbits 7 個工作天;SourceOfTruth 5 天;SSW 3 天;DLabs 約 5 小時)。
- **PoC / 固定範圍 sprint**:9/43 (21%)。時程 2 週最常見(Just Think AI、XYZ、INSIDEA discovery、Outright Mental AI Capability Sprint、Pragma-Code AI Sprint 14 天),PoC 2-6 週(Symphony、Pixelfield)。
- **Workflow automation(n8n/Make/Zapier)**:5/43 (12%)。以固定價格 + 月 retainer 為主(Goodspeed、GrowwStacks、Hack'celeration、Pragma-Code)。
- **Microsoft 365 Copilot readiness**(歸入 assessment):IT Partner、EPC Group、Steadfast、ProArch、Copilot Consulting;範圍幾乎都是 tenant 權限/oversharing/DLP/labels,與「自建 RAG/automation」不同,屬 Microsoft 生態顧問市場。
- **Governance / eval**:3/43 (7%);ISO 42001 / NIST AI RMF gap assessment 有明確定價案例(IT Partner 起價 $7,500、4 週),red teaming 皆為報價制。
- **Embedded / retainer**:Caylent FDE pods(3/6/9 個月)、Just Think AI Embedded($18k-$45k/月、3 個月最低)、Outright Mental Fractional($6k/月起)、SpotDev Accelerator(£10k/月起、按季)。

### 常見 deliverables 出現頻率(自 deliverables 欄關鍵字比對,為粗略計算)

| deliverable 類型 | 出現列數 |
|---|---|
| Roadmap / prioritized use-case list | 21/43 (49%) |
| Readiness / maturity scorecard or report | 12/43 (28%) |
| ROI / business case / cost estimate | 9/43 (21%) |
| Working prototype / PoC / MVP | 10/43 (23%) |
| Production deployment of workflow/agent | 9/43 (21%) |
| Eval suite / monitoring / observability | 8/43 (19%) |
| Runbook / docs / training / handover | 9/43 (21%) |
| Governance policy / DLP / risk register | 10/43 (23%) |
| Go/no-go decision | 5/43 (12%) |

### 實施時程分布(自 implementation_time 欄)
| 時程 | 數量 |
|---|---|
| 1-4 weeks | 24 |
| UNKNOWN | 13 |
| <=1 week (days/hours) | 5 |
| longer / mixed / other | 1 |

## 價格可見度(自 public_price 欄計算)

- 公開具體金額或區間:**20/43 (47%)**;UNKNOWN/僅報價:**23/43 (53%)**。
- pricing_model 明確寫 fixed(固定價/固定範圍):27/43 (63%)。
- 評估費可抵扣後續建置(audit credit):3/43 (7%)(Main & Machine 最多抵 sprint 的 25%;WorkWise 全額抵 $25k+ 案;SourceOfTruth 100% 抵)。
- 已公開的價格點(原幣,僅供參考,牌價非成交價):

| 供應商 | 服務 | public_price |
|---|---|---|
| Main & Machine (M&M) | AI Readiness Audit + AI Implementation Sprint + Managed Serv | Audit $3,500-$8,500; Sprint $12,000-$45,000; Managed from $1,500/mo; Full Back Office from $95,000; audit credit up to 25% of sprint if signed within 60 days |
| Goodspeed | n8n automation build (audit -> architecture -> build -> depl | Fixed build from $5,000 for up to 4 workflows; team from $10,000/mo (blog snippet only) |
| Pragma-Code | AI Sprint (n8n) + fixed packages + Agent Operations retainer | AI Sprint (n8n) EUR 2,900; Website Assistant EUR 1,490-2,900; Phone Assistant EUR 1,490-2,490; Automation retainer EUR 590/mo; Agent Ops EUR 390-1,190/mo |
| Just Think AI | AI Sprint (2 weeks) / AI Strategy / Embedded AI Partner | Sprint $25k-$60k; Strategy $15k-$35k; Embedded $18k-$45k/mo |
| WorkWise Solutions | AI Readiness Sprint / Custom Build / AI Operating Partner | Sprint $12,500 fixed, credited toward $25,000+ engagement booked within 90 days; build/retainer UNKNOWN |
| XYZ (xyz.dev) | Discovery Sprint / MVP Build / Ongoing Partnership | Discovery BD 250; MVP BD 999; Partnership BD 400/mo (currency 'BD' not defined on page - possibly Bahraini dinar; UNVERIFIED) |
| INSIDEA | AI & Automation: Discovery sprint / Production AI agent / Mu | Discovery from $2,000; agent/multi-agent scoped at proposal; Managed AI ops from $2,000/mo; LLM API costs separate |
| Outright Mental | AI Capability Sprint / Feasibility Read / Agentic SDLC Enabl | AI Capability Sprint $9,500; Feasibility Read $4,500; Agentic SDLC $18,000; Fractional from $6,000/mo |
| Pixelfield | AI Proof of Concept (Light / Standard) | Light PoC from GBP 8,000; Standard GBP 15,000-30,000; production build from GBP 25,000+ |
| Alian Software (Alian AI) | Fixed-fee Sprint incl. paid Discovery (AI agents, RAG, chatb | Typical $40K-$150K; Discovery $8K-$20K; 'not for' engagements under $20K |
| IT Partner LLC - M365 Copilot Readiness Assessment | Microsoft 365 Copilot Readiness Assessment | $4,950 |
| IT Partner LLC - Copilot & AI Use-Case ROI Sprint | Microsoft 365 Copilot and AI Use-Case ROI Sprint | $3,950 |
| Steadfast Solutions | Microsoft Copilot Readiness Assessment | Assessment $1,700 ex GST (+ Copilot license $540/yr); promo expired 2024 |
| GrowwStacks | Make.com automation, AI agents, MCP, Zapier migration | Simple $3,000-$5,000; multi-step $5,000-$10,000; enterprise $10,000-$25,000+; Make platform $9-$99/mo extra; retainer UNKNOWN |
| Hack'celeration | Automation audit + n8n/Make/Zapier builds with AI steps | Budgets start from $2,000; audit price UNKNOWN (conflict) |
| VibeFactory.ai | RAG knowledge base, agent automation, AI strategy assessment | No price list; assessment $5K-15K (FAQ) |
| SourceOfTruth Labs | AI Readiness Audit (Full) | INR 25K-50K |
| IT Partner LLC - ISO 42001 Readiness Assessment | AI Governance and ISO/IEC 42001 Readiness Assessment | From $7,500 (scoped by AI footprint) |
| SSW | AI Discovery Workshop | AUD $12,000 + GST (currency inferred from GST/Australia) |
| SpotDev Services | ChatGPT and Codex Rollout (AI Starter/Foundations/Rollout/Ac | Starter GBP 3,500; Foundations GBP 8,000; Rollout from GBP 18,000; Accelerator from GBP 10,000/mo (ex VAT) |

- 觀察(INFERENCE,樣本偏誤見上):公開價格集中於 (a) 評估類 US$3.5k-12.5k(IT Partner $3,950/$4,950、Main & Machine $3,500-8,500、WorkWise $12,500、Outright Mental feasibility $4,500;SourceOfTruth 為 INR 25-50K 的低價端);(b) 2 週 sprint US$9.5k-60k 分布很寬;(c) n8n/Make 建置 US$3k-10k(Goodspeed $5k 起、GrowwStacks $3-10k);(d) 月 retainer US$1.5k-45k 分布極寬。

## 信任訊號出現頻率(自 trust_signals 欄關鍵字比對,43 列為分母)

| 訊號 | 列數 |
|---|---|
| Vendor/platform partner badge (Microsoft/AWS/Google/OpenAI/Anthropic/HubSpot/n8n/Make/Salesforce) | 19/43 (44%) |
| Third-party review rating (Clutch/Google/Trustpilot/G2/Upwork/GoodFirms/Sortlist) | 12/43 (28%) |
| Named client logos / named clients | 8/43 (19%) |
| Security/compliance cert or posture (ISO, SOC2, Cyber Essentials, GDPR, NDA) | 8/43 (19%) |
| Fixed-price / guarantee / no-ROI-guarantee transparency | 6/43 (14%) |
| Client owns IP/code | 5/43 (12%) |
| Years-in-business / project-count claim | 16/43 (37%) |

- 具名 testimonial 文字(testimonials 欄非 UNKNOWN):9/43 (21%);有具名案例(case_studies 非 UNKNOWN):23/43 (53%)。多數小型供應商兩者皆無,信任主要靠 partner badge、第三方評分與固定價格/保證條款。

## 對 Taiwan 單人技術顧問產品化的含意(標示 INFERENCE)

- INFERENCE:以『固定價評估 + 可抵扣建置』與『2 週固定範圍 sprint(單一 workflow)』是公開價格最清楚、重複出現最多的包裝;這兩類與遠端、固定範圍、可用 AI 輔助交付相容。
- INFERENCE:Microsoft Copilot readiness 與 ISO 42001 gap assessment 有明確低價固定價案例,但綁定 M365/合規專長,是否適合需另評。
- NEW EVIDENCE:台灣在地公開價格幾乎不存在於供應商頁面(本批 UNKNOWN),價格訊號需由 PRO360/Tasker 等平台與其他檔(freelance/demand)補足;本檔不能推論台灣成交價。
- 不得由本檔推論買方願付價格:以上皆為供應商牌價。

## 資料列(摘要;完整欄位見 CSV)

| id | provider | 類型 | 國家 | 服務 | 時程 | 公開價格 | status |
|---|---|---|---|---|---|---|---|
| AC001 | Main & Machine (M&M) | assessment | US (Denver/Phoenix; also remot | AI Readiness Audit + AI Implementation Sprint + Ma | Audit 2-4 wks; Sprint 4-12 wks; Full Bac | Audit $3,500-$8,500; Sprint $12,000-$45,000; Managed from $1 | VERIFIED |
| AC002 | Goodspeed | workflow-automation | UNKNOWN | n8n automation build (audit -> architecture -> bui | Simple: days; complex multi-system: 2-4  | Fixed build from $5,000 for up to 4 workflows; team from $10 | VERIFIED |
| AC003 | Pragma-Code | workflow-automation | DACH (Germany) | AI Sprint (n8n) + fixed packages + Agent Operation | AI Sprint 14 days; Website Assistant 2-4 | AI Sprint (n8n) EUR 2,900; Website Assistant EUR 1,490-2,900 | VERIFIED |
| AC004 | Copilot Consulting | assessment | UNKNOWN | Readiness Assessment / Governance & Deployment / E | Assessment 2 wks; Governance 4-8 wks; En | UNKNOWN (Contact for Quote) | VERIFIED |
| AC005 | Just Think AI | poc-sprint | UNKNOWN | AI Sprint (2 weeks) / AI Strategy / Embedded AI Pa | Sprint 2 wks (demo day 5, prod day 8, ha | Sprint $25k-$60k; Strategy $15k-$35k; Embedded $18k-$45k/mo | VERIFIED |
| AC006 | WorkWise Solutions | assessment | UNKNOWN | AI Readiness Sprint / Custom Build / AI Operating  | Sprint 1-2 wks; build 6-8 wks; first cal | Sprint $12,500 fixed, credited toward $25,000+ engagement bo | VERIFIED |
| AC007 | XYZ (xyz.dev) | poc-sprint | UNKNOWN | Discovery Sprint / MVP Build / Ongoing Partnership | Sprint 2 wks; MVP 6-8 wks | Discovery BD 250; MVP BD 999; Partnership BD 400/mo (currenc | VERIFIED |
| AC008 | GroundAI | assessment | UNKNOWN (page in Traditional C | AI 導入顧問 (顧問陪跑) / PoC-MVP / ongoing technical consu | UNKNOWN | UNKNOWN | VERIFIED |
| AC009 | INSIDEA | poc-sprint | UNKNOWN | AI & Automation: Discovery sprint / Production AI  | Discovery 2 wks; agent 60-90 days; multi | Discovery from $2,000; agent/multi-agent scoped at proposal; | VERIFIED |
| AC010 | Outright Mental | poc-sprint | UNKNOWN | AI Capability Sprint / Feasibility Read / Agentic  | Feasibility 1 wk; AI Capability Sprint 2 | AI Capability Sprint $9,500; Feasibility Read $4,500; Agenti | VERIFIED |
| AC011 | Future Processing | poc-sprint | Poland (HQ; UK, US, Ukraine, S | Value Prototype Sprint | 1-3 wks; follow-on 4-8 wk milestone | UNKNOWN | VERIFIED |
| AC012 | Symphony Solutions | poc-sprint | Netherlands (Amsterdam) | AI Proof of Concept | Full PoC 2-4 wks; low-code prototype 2-5 | UNKNOWN | VERIFIED |
| AC013 | Pixelfield | poc-sprint | UK (London) | AI Proof of Concept (Light / Standard) | Light 2-4 wks; Standard 4-6 wks | Light PoC from GBP 8,000; Standard GBP 15,000-30,000; produc | VERIFIED |
| AC014 | Alian Software (Alian AI) | poc-sprint | India (ships globally) | Fixed-fee Sprint incl. paid Discovery (AI agents,  | 2-8 wks; paid discovery 1-2 wks | Typical $40K-$150K; Discovery $8K-$20K; 'not for' engagement | VERIFIED |
| AC015 | IT Partner LLC - M365 Copilot Readiness Assessment | assessment | US (stated 'US Microsoft partn | Microsoft 365 Copilot Readiness Assessment | 1-2 wks | $4,950 | VERIFIED |
| AC016 | IT Partner LLC - Copilot & AI Use-Case ROI Sprint | assessment | US (stated) | Microsoft 365 Copilot and AI Use-Case ROI Sprint | 2 wks | $3,950 | VERIFIED |
| AC017 | EPC Group | assessment | US (Houston) | Copilot Readiness Assessment (TAR-8) | 4 wks single tenant; 6 wks multi/hybrid | UNKNOWN (does not publish ranges) | VERIFIED |
| AC018 | Steadfast Solutions | assessment | Australia (Melbourne/Brisbane/ | Microsoft Copilot Readiness Assessment | UNKNOWN | Assessment $1,700 ex GST (+ Copilot license $540/yr); promo  | PARTIALLY VERIFIED |
| AC019 | ProArch | assessment | UNKNOWN (US inferred from URLs | Microsoft Copilot JumpStart (Envisioning & PoC; De | UNKNOWN (per Microsoft program guideline | UNKNOWN (Microsoft funding subject to eligibility, excludes  | VERIFIED |
| AC020 | GrowwStacks | workflow-automation | UNKNOWN | Make.com automation, AI agents, MCP, Zapier migrat | Simple 1-2 wks; multi-step 2-3 wks; ente | Simple $3,000-$5,000; multi-step $5,000-$10,000; enterprise  | VERIFIED |
| AC021 | Hack'celeration | workflow-automation | UNKNOWN (fully remote) | Automation audit + n8n/Make/Zapier builds with AI  | Small ~1 wk; first workflow 3-5 wks from | Budgets start from $2,000; audit price UNKNOWN (conflict) | VERIFIED |
| AC022 | GRC Solutions | eval-guardrail | UK (inferred) | AI Red Teaming & ML/LLM Testing | UNKNOWN | UNKNOWN (Get a quote) | VERIFIED |
| AC023 | LOW/CODE Agency | workflow-automation | UNKNOWN | AI Implementation / Business Automation / AI agent | UNKNOWN | UNKNOWN | PARTIALLY VERIFIED |
| AC024 | Caylent - Generative AI Proof of Value | poc-sprint | US (AWS partner) | AWS Generative AI Proof of Value | UNKNOWN | UNKNOWN | VERIFIED |
| AC025 | Caylent - Generative AI Strategy | assessment | US (AWS partner) | Generative AI Strategy (Catalyst) | UNKNOWN | UNKNOWN | VERIFIED |
| AC026 | Caylent - Forward Deployed Engineering Pods | agent-integration | US (AWS partner) | Forward Deployed Engineering Pods | 3, 6 or 9 months | UNKNOWN | VERIFIED |
| AC027 | deepsense.ai | rag-knowledge | Poland (Warsaw HQ; Palo Alto) | Claude Partner Network Select services (agents, RA | UNKNOWN | UNKNOWN | VERIFIED |
| AC028 | cacaFly (聖洋科技) | assessment | Taiwan (Taipei HQ, Hsinchu; Ma | Cloud AI+ 雲端智能中心 (Google Cloud AI consulting) | UNKNOWN | UNKNOWN | PARTIALLY VERIFIED |
| AC029 | iKala | rag-knowledge | Taiwan | iKala Nexus (enterprise knowledge + AI agents) / f | UNKNOWN | UNKNOWN | VERIFIED |
| AC030 | Peerbits | assessment | UNKNOWN | AI Audit for SMBs (AI Readiness Review) | 7 business days from discovery call | UNKNOWN (free discovery call) | VERIFIED |
| AC031 | VibeFactory.ai | rag-knowledge | UNKNOWN | RAG knowledge base, agent automation, AI strategy  | RAG 4-8 wks; agents 3-6 wks; assessment  | No price list; assessment $5K-15K (FAQ) | VERIFIED |
| AC032 | SourceOfTruth Labs | assessment | India (Jodhpur) | AI Readiness Audit (Full) | Audit 5 days; build 2-3 wks | INR 25K-50K | VERIFIED |
| AC033 | IT Partner LLC - ISO 42001 Readiness Assessment | eval-guardrail | US (stated) | AI Governance and ISO/IEC 42001 Readiness Assessme | 4 wks | From $7,500 (scoped by AI footprint) | VERIFIED |
| AC034 | DeepInspect | eval-guardrail | UNKNOWN | AI Governance & Compliance | 3-5 wks | UNKNOWN | VERIFIED |
| AC035 | 精誠集團 Sincere Group | rag-knowledge | Taiwan | 生成式AI一條龍服務 | UNKNOWN | UNKNOWN | PARTIALLY VERIFIED |
| AC036 | 叡揚資訊 Vigor (GSS) | rag-knowledge | Taiwan | Vitals ESP knowledge management with LLM Q&A | UNKNOWN | UNKNOWN | PARTIALLY VERIFIED |
| AC037 | SSW | assessment | Australia | AI Discovery Workshop | 3 days on-site | AUD $12,000 + GST (currency inferred from GST/Australia) | VERIFIED |
| AC038 | Sherwen | assessment | UNKNOWN | 1 Day AI Strategy Workshop (AI Strategy Sprint) | 1 day (in person or remote) | UNKNOWN | VERIFIED |
| AC039 | SpotDev Services | internal-assistant | UK (Bath) | ChatGPT and Codex Rollout (AI Starter/Foundations/ | Starter 4 wks; Foundations 2-3 wks; Roll | Starter GBP 3,500; Foundations GBP 8,000; Rollout from GBP 1 | VERIFIED |
| AC040 | Vention | assessment | US (New York; UK, DACH sites) | AI Discovery Workshop (feasibility check) | 2-6 wks | UNKNOWN | VERIFIED |
| AC041 | Pythian | assessment | UNKNOWN | AI Workshops (AI/ML strategy session) | 1 day intensive or 2-3 day deep dive | UNKNOWN | VERIFIED |
| AC042 | CGI (OpenAI partner) | assessment | Canada (founded 1976) | Enterprise AI Value Discovery / Enterprise AI Solu | UNKNOWN | UNKNOWN | VERIFIED |
| AC043 | DLabs.AI | assessment | Poland (Gdansk inferred) | AI strategy workshop (AI Radar / Opportunity Canva | ~5 hrs session + calibration + results s | UNKNOWN | VERIFIED |
