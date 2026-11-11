# 02 — 既有開源專案評估（fork / reuse / rewrite）

調查日期：2026-11-11。方法：四個指定 repo 中，radar、TIP、idea-hunt-skill 以 `gh api` 下載 tarball 到 scratchpad 後用 Read/Grep 讀碼（未執行 git、未執行其程式碼、未對外互動）；Shipwright 倉庫約 683MB，改用 gh api 讀 tree/README/commits。來源清單見 `_sources/repos.md`。

標記規則：VERIFIED = 我直接讀到程式碼/檔案或 API 回傳；PARTIALLY VERIFIED = 有部分直接證據，其餘為推論；UNVERIFIED = 僅 README/自我宣稱或搜尋描述；UNKNOWN = 找不到證據。Star 數與日期皆為 2026-11-11 當日 GitHub API 數值。

---

## 0. 結論先行

| 問題 | 結論 | 標記 |
|---|---|---|
| radar 能否直接 fork 當主系統 | 不建議整包 fork；建議 Hybrid：借用 5 個模組與「source admission」流程，自寫 verification / approval / build / revenue 層 | VERIFIED（讀碼） |
| TIP 是否找得到有付款證據（A）的機會 | 否。屬 B/C：趨勢訊號 + 作者推估的變現路徑，無實際付款證據 | VERIFIED |
| idea-hunt-skill | 不直接使用；Convert（抽取 kill-gate 與 Proof-of-Wallet 改寫進自己的 verification skill）並保留 workflow 參考 | VERIFIED |
| Shipwright | 成熟度高但與原生 Claude Code 重疊大、僅支援 Claude Code、基礎設施重；僅作參考，不整合 | PARTIALLY VERIFIED |
| 正確的 build-DNA repo | UNKNOWN。最接近的 `Sudiddii/build-DNA` 名稱吻合，但無法確認就是你指的那個 | UNKNOWN |

---

## 1. everton-soares1985/global-builder-opportunity-radar

### 1.1 基本事實

| 項目 | 內容 | 標記 |
|---|---|---|
| Stars / 授權 / 語言 | 0 star / MIT / Python 3.12（另有 React+Vite dashboard） | VERIFIED |
| 建立 / 最後 push | 2026-08-14 / 2026-09-08（距今 64 天，無近兩個月更新） | VERIFIED |
| Commits | 15 個，全部單一作者（2026-08-14 九個、08-15 兩個、09-04、09-05、09-06、09-08 各一）；無 release；0 open issues | VERIFIED |
| 真實程式碼 vs README | 真實：`src/global_builder_radar/` 約 25 個模組，storage.py 約 22KB、cli.py 約 26KB，12 個 collector | VERIFIED |
| 測試 | `tests/` 共 151 個 `def test_`（grep 計數）、有 offline fixtures；CI（ruff + pytest + dashboard lint/typecheck/build）最近 5 次 run：4 success、1 failure（2026-08-15），最後兩次成功。我未自行執行測試 | VERIFIED（計數與 CI 狀態）/ UNVERIFIED（測試本身是否全綠於本機） |
| 開發方式 | 含 AGENTS.md、QWEN_HANDOFF.md、docs/current-work.md，明顯由 AI coding agent 依文件契約迭代開發 | PARTIALLY VERIFIED（推論自檔案） |
| 作者定位 | 巴西開發者（`R$`、Baixada Santista、InfoJobs Brasil、`brazil_eligibility` 欄位） | VERIFIED |
| 台灣相關內容 | grep "Taiwan/台灣" 於 repo 內無任何命中 | VERIFIED |

### 1.2 架構

流程（docs/architecture.md + pipeline.py，VERIFIED）：
`sources.yaml → Collector（RSS/API/Gmail alert/Scrapling/Apify，各自隔離）→ Opportunity 正規化（pydantic）→ classify_opportunity_kind → enrich_opportunity（正則抽取金額/截止日/資格）→ classify_service_domains → score_opportunity → SQLite upsert（fingerprint 去重）→ dashboard JSON → 本地 React UI（localhost action API 寫回 saved/applied/dismissed）`

- Collector 只讀、不寫 DB；`asyncio.gather` + `_safe_collect` 讓單一來源失敗不影響整體（pipeline.py）。VERIFIED
- 設計原則寫明「缺少證據就是 null，不猜」「來源需通過 source-admission 六階段 confidence lifecycle（candidate/experimental/verified/degraded/retired）」。VERIFIED（docs/source-admission.md）
- 無 LLM 評分；README/architecture 明說 AI enrichment 屬未來，且「不取代 deterministic validation」。VERIFIED

### 1.3 Collectors 與來源（config/sources.yaml、docs/sources.md）

| 來源 | 方法 | 狀態（repo 自述） | Taiwan 適用性 | 建議 |
|---|---|---|---|---|
| reddit r/slavelabour `[TASK]` | RSS | enabled，verified（2026-08-13 smoke 25 解析/9 接受；2026-08-14 凍結跑遇 429） | 英文、全球可接；單價低、品質參差 | 保留（低權重） |
| reddit r/forhire `[Hiring]` | RSS | enabled，verified | 全球 | 保留 |
| reddit r/jobbit | RSS | disabled（正職轉貼太多） | 是 | 丟棄 |
| HN Freelancer 月串 `SEEKING FREELANCER` | Algolia API | enabled，verified；8 月實測真實為 0 筆（15 解析/0 接受） | 全球，量少但品質高 | 保留 |
| HN Who is Hiring | Algolia API | disabled（無法分離正職與合約） | — | 丟棄 |
| Opire bounties | Scrapling + Next.js `initialRewards` | enabled，verified | 全球；付款地區限制 UNKNOWN | 保留，補驗 Taiwan 可領款 |
| Superteam Earn | Scrapling dynamic | enabled，verified（22 連結、USDC/USDG 金額） | Web3；加密貨幣付款與台灣稅務/合規需自行評估 | 保留但標 B-risk |
| Algora（GitHub keyword search） | GitHub Search API | retired（作者自己判定為脆弱代理） | — | 丟棄；改走官方 Algora API（repo 自列 backlog，UNVERIFIED 該 API 實際可用性） |
| Upwork（Apify actor） | Apify | experimental；每次約 US$0.10（repo 自述，我未驗證） | 全球；抓取有 ToS 風險 | 可選，預設關閉 |
| Upwork Gmail alerts | Gmail API 唯讀 | verified | 全球，不抓取、合規性較佳 | 保留（若你有 Upwork 帳號） |
| LinkedIn Apify / LinkedIn Gmail alerts | Apify / Gmail | experimental / verified | 地點白名單為 Brazil | 丟棄（正職 lane，且地理硬編） |
| InfoJobs (Playwright) | Playwright | verified（supervised） | 巴西站台 | 丟棄 |
| GitHub bounty search collector | GitHub API | 程式存在；`signal_repetitions > 25` 視為垃圾 | 全球 | 可借邏輯 |

### 1.4 Ranking（scoring.py，VERIFIED）

純關鍵字加權：`include_keywords`（python:10 等）+ `exclude_keywords`（unpaid:-20）+ `category_weights` + `source_weights` + bonuses（email_contact:8、compensation_visible:8、remote:4、deadline_visible:2）。`basic_quality()` 四項各 0.25（有報酬文字、描述≥80字、有聯絡方式、有日期證據），明說「僅供報告，不進入排序」。

評估：簡單、可解釋、可測，但**沒有「付款證據等級」維度**、沒有 effort/ROI、沒有勝率估計，不足以做你要的 scoring。

### 1.5 Dedup（models.py / storage.py，VERIFIED）

- `fingerprint = sha256(source|external_id or canonical_url)`；`canonicalize_url` 移除 utm/fbclid 等追蹤參數、去尾斜線、小寫 host。
- 跨管道去重僅限同「source family」（例如 LinkedIn Gmail 與 LinkedIn Apify，以 exact platform job ID 合併，並累積 `acquisition_sources`、保留較豐富證據）。
- **沒有**跨平台語意去重（同一案子貼在 Reddit 與 Upwork 不會合併）。VERIFIED（缺失）

### 1.6 SQLite 資料模型（VERIFIED）

三表：`collection_runs`（來源健康）、`opportunities`（fingerprint PK；含 compensation_*、deadline、deadline_evidence、effort_evidence、brazil_eligibility、application_method、service_domains_json、raw_payload_json、score、status、saved、applied_at、dismissed_at、first/last_seen_at）、`application_confirmations`。
- 優點：raw_payload 保留、collector upsert 不覆寫使用者 lifecycle 欄位、狀態（new/reviewed/discarded/actioned）+ 使用者動作分離。
- 缺點：無 evidence 子表（一個機會多條證據、證據等級、驗證時間）、無 approval/build/submission/revenue 實體；只有「申請」層級。

### 1.7 Evidence handling

- 正向：金額/截止日/努力量只擷取文字明示內容、保留原文證據欄位；零金額不當報酬；`verify-github-issues` 指令把已關閉/死連結的 GitHub issue 標 discarded、清掉 0 元 bounty 的報酬（CHANGELOG 自述首次跑隱藏 22 筆污染資料，UNVERIFIED 數字）。
- 不足：證據僅停在「文字上看起來有報酬」，沒有「付款方是否真的付過款」「平台託管（escrow）」之類的 A 級驗證。

### 1.8 模組分類

| 分類 | 模組 | 說明 |
|---|---|---|
| 可直接重用（改動小） | `models.py`（Opportunity、canonicalize_url、fingerprint）；`collectors/base.py` + `registry.py`（Collector 協定與來源隔離）；`collectors/reddit.py`、`hackernews.py`（freelancer 版）；`docs/source-admission.md` 流程 | 需把 `brazil_eligibility` 泛化為 `region_eligibility`，加 TWD/NT$ 解析 |
| 可 fork 後修改 | `extraction.py`（金額/單位/截止日正則；30 處 Brazil 相關需改）；`scoring.py` + `profile_rules.yaml`（換成你的 skills 與 Taiwan profile，加證據等級權重）；`opire.py`、`scrapling_links.py`、`github_bounties.py`、`github_issues.py` | |
| 建議重寫 | `storage.py`（若你要 MongoDB/Kafka 路線；至少要擴充 evidence/approval/build/revenue 表）；`pipeline.py`（加 verification、approval gate）；`briefing.py`/`cli.py`（耦合 Brazil 與正職 lane） | |
| 不適合台灣 | `linkedin_apify.py`、`linkedin_gmail.py`、`infojobs_playwright.py`、`gmail_applications.py`（巴西地點/平台）；`abrir-radar.ps1`、`atualizar-upwork.ps1`、`convert_n8n_gmail_credential.py`、Oracle SSH 啟動邏輯；`service_domains.py` 的行銷/CRM 偏重；葡文關鍵字 | |
| 完全缺失（需新建） | 付款證據驗證、人工 approval gate、Codex/Claude build handoff、submission 追蹤、revenue 追蹤與回饋校準、台灣來源（104 外包網、PCC 標案等）、TWD/稅務 | |

### 1.9 風險

單一維護者、0 star、2 個月無更新（推論：個人專案，維護延續性 UNKNOWN）；Scrapling 被釘在 0.4.1（Windows fingerprint 問題，作者自述）；Apify/Upwork 抓取成本與 ToS；加密貨幣類來源之合規。

---

## 2. aitippro/TIP

| 項目 | 內容 | 標記 |
|---|---|---|
| 規模 | 5 star；**無 LICENSE**（法律上預設保留所有權利，不宜複製）；Shell（僅 `run_daily.sh`）；2026-05-25 建立、最後 push 2026-05-31（距今 164 天，已停更）；2026-05-25 至 06-01 共 8 份日報 | VERIFIED |
| 架構 | cron 每日 00:03 → `cat prompts/daily.md \| claude --print --max-budget-usd 5 --allowedTools "Bash,Read,Write,Edit,WebSearch,WebFetch,Glob,Grep"` → 寫 markdown 日報並 git push。**沒有任何應用程式碼、DB、去重或評分程式**，只有一份約 7.8KB 的 prompt | VERIFIED |
| 來源 | Product Hunt、HN 首頁、GitHub Trending、PH newsletter，輔以 WebSearch | VERIFIED |
| 安全 | CLAUDE.md 與 prompt 內的「sandbox」只是文字規則，並非技術隔離；同時給了 Bash+Write 權限去處理未信任網頁內容，prompt injection 風險實質存在 | PARTIALLY VERIFIED（推論） |
| 付款證據 | 機會卡片格式為「賽道/為什麼是今天/所需技能/變現路徑/可行性星等/窗口期」。「變現路徑」是作者自擬定價（例如 `$19-49/月`、`$0.01-0.05/次`、`$5000-20000` 年訂閱），**不是**已存在買家付款的證據。日報中的金額多為公司層級（如 ClickHouse ARR）或文章標題的 MRR 案例，不是某個機會的付款憑證 | VERIFIED（2026-05-28 日報抽查） |
| 可信度 | 日報含若干我無法核實的敘述（如 Claude Code 年化營收數字、特定模型版本/發布計畫）；一律當 UNVERIFIED，不納入任何決策 | UNVERIFIED |

結論：TIP 產出的是 **B 級（看起來有訊號）至 C 級（趨勢敘事）**，沒有 A 級（有付款證據）。可借鏡的只有「反過擬合：先讀昨日報告再寫今日」與「每則訊號標注來源類型」兩個 prompt 技巧。**不建議 fork。**

---

## 3. ANVEAI/idea-hunt-skill

| 項目 | 內容 | 標記 |
|---|---|---|
| 規模 | 4 star、MIT；2026-07-14 建立、3 commits 同日 + 1 commit 2026-10-26（距今 16 天）；檔案僅 LICENSE、README.md、SKILL.md（約 18.5KB） | VERIFIED |
| 性質 | 純 prompt 型 Claude skill（version 2.0.0），無程式碼、無資料層 | VERIFIED |
| 流程 | Stage 0 框定 → 1 痛點挖掘（last30days + G2/Capterra 1–3 星 + Upwork/Fiverr gig 當「採購單」）→ 2 候選 5–8 個 → 3 六道 kill-gate（0–2 分，任一 0 或總分 <8/12 淘汰）→ 4 office-hours 六問 + Mom Test → 4.5 Proof of Wallet（預售/押金/smoke test/concierge/LOI，事先定 pass bar）→ 5 只選 1 個 → 6 建置藍圖 | VERIFIED |
| 優點 | 「證據先於想像」「現金 > 意見」「先寫 pass bar」與你的 verification/scoring 精神一致；Proof of Wallet 可直接成為你的「付款證據」A/B/C 分級定義 | VERIFIED |
| 限制 | (1) 目標是「發明/挑選 SaaS 創業題材」，不是找現成 bounty/外包案；(2) 依賴外部 skill `last30days` 與 `office-hours`；(3) 範例偏印度 D2C/Razorpay，GTM 假設 72 小時、50–100 次冷開發；(4) 內文引用統計（42% 因無市場需求失敗、60–70% AI wrapper 營收為 $0、約 90% 於 2026 年底前死亡）本身為 skill 自述，**未附可核對的出處連結** | VERIFIED（限制）/ UNVERIFIED（統計數字） |

決策：**不直接使用；Convert**。把 Stage 3 的 gate 與 Stage 4.5 改寫為你系統 verification 階段的 checklist（改為針對「具名買家已付款/已公告獎金」而非 SaaS 點子），並僅保留其 workflow 作為參考。授權為 MIT，改寫時註明出處即可。

---

## 4. app-vitals/shipwright（Shipwright Harness）

| 項目 | 內容 | 標記 |
|---|---|---|
| 規模/授權/語言 | 16 star、MIT、TypeScript（Bun）；2026-06-06 建立、最後 push 2026-11-11（當日）；7 open issues | VERIFIED |
| 開發強度 | contributors API 合計約 4,540 commits（3429/1013/65/33/2，含 renovate bot）；最近 100 筆 commits 全在 2026-11；30 個 release（回傳上限可能截斷），最新 tag shipwright-1.6.23 發佈於 2026-06-24（commits 持續而 release 不頻繁，原因 UNKNOWN） | VERIFIED |
| 內容 | tree 1,304 檔：plugin（`plugins/shipwright` 300 檔，commands：prd、plan-session、dev-task、review、patch、merge、test-*、entropy/error/prompt/consolidation scan 等；agents：code-reviewer、researcher 等；skills）、task-store（Prisma/Postgres）、admin UI、metrics dashboard、agent runner、Helm chart、Slack 整合；測試檔（`.test.`/`.spec.`）約 380 個 | VERIFIED（tree 名稱計數） |
| 工作流 | `/shipwright:prd → plan-session → dev-task → review → patch → merge`，以 GitHub PR 為載體，task queue 存 task-store | VERIFIED（README） |
| 自報成果 | 「近 30 天 300 tasks、CI first-pass 85.8%、平均週期約 1.4h」，來自作者自己公開 dashboard，我未開啟核對 | UNVERIFIED |
| 與 Codex 關係 | README 中 "codex" 出現 0 次；定位為「built on Claude Code」plugin | VERIFIED（README 層級） |

評估：
- **成熟度**：以此類 side project 而言屬高（高頻率提交、測試、CI、Helm、Slack）；但 16 star 顯示採用度低，自報指標未獨立驗證，且以 SaaS/design-partner 為商業目的（README 有 discovery call 招募）。
- **與原生工具重疊**：plan→build→review→PR 這條路在原生 Claude Code（skills、subagents、`/review`、`gh`）與 Codex CLI 已能完成；Shipwright 額外價值在 task-store 佇列與 metrics，但需 Postgres/Bun/go-task，完整堆疊需 tmux+Docker+Postgres+Slack，對單人 Python/資料工程師過重。
- **結論：僅作參考，不整合。** 可借鏡：PRD→任務佇列→逐 task 開 PR→獨立 reviewer agent 的分段、`finding-verifier` 概念（對 review 結論再驗證）、metrics 指標設計。你的系統若要同時支援 Codex 與 Claude，應自建薄的 handoff 層（把已核准機會轉成 spec 檔，再由 Codex/Claude 各自執行），不要引入 K8s/Prisma 層。

---

## 5. 正確的 build-DNA repo

- 搜尋 `gh search repos`：`build-dna`、`build DNA`、`builddna`、`build-dna opportunity` 等關鍵字。
- 最接近：**Sudiddii/build-DNA**（5 star、MIT、2026-05-29 建立、3 commits、純 skill：SKILL.md + references + examples）。功能為「依個人背景/技能/人脈產生商業點子與 GTM、72 小時行動計畫」，三階段 DNA Scan → 點子生成 → Build Brief。PARTIALLY VERIFIED（名稱與時間吻合，且為 Claude skill）。
- 其他同名候選：`RamvikasSV/BuilderDNA`（README 僅 71 bytes，空殼）、`Anas-Rehberlik/Build-DNA`（0 star，無描述）、`BuildingDNA/*`（建築資訊，不相關）、`Spolson7788/*BuildDNA`（0 star，未見描述）——皆不採。
- 判定：**UNKNOWN**。無法證明它就是你所指「目前正確的 build-DNA」；三個已讀 repo 與 CURRENT_STATUS.md 中沒有提供可對照的連結或 owner。請由你確認 owner/repo。
- 若確為 Sudiddii/build-DNA：它是「從自己出發發想」的點子生成器，與 idea-hunt 的「證據先於想像」方向相反，僅適合作為「你的 DNA profile（Python/MongoDB/Kafka/資料工程）」輸入欄位的參考，不適合作為機會發現來源。

---

## 6. 其他值得參考的 repo（15 個，均於 2026-11-11 以 `gh api` 取得 metadata）

「Active」定義：最後 push 距今 ≤ 30 天為 Yes，31–120 天為 Moderate，>120 天為 Stale。架構欄凡未讀碼者標 UNVERIFIED（僅依 README/語言/目錄推定）。

| # | Repository | Purpose | Stars | Last Update | Active | License | Language | Architecture | Revenue-related feature | Evidence quality | Reusable components | Risk | Recommendation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | algora-io/algora | OSS bounty/hiring 平台 | 1542 | 2026-07-18 | Moderate（116 天） | AGPL-3.0 | Elixir | Phoenix 單體（UNVERIFIED，由語言與 850 檔推定） | 有懸賞與合約撮合；實際付款機制/台灣出款 UNKNOWN | A 級潛力（平台公開金額+託管，PARTIALLY VERIFIED） | 不建議重用程式碼；當資料來源 | AGPL；Elixir 技術棧不合；是否有穩定公開 API UNVERIFIED | 作為來源（走官方 API/頁面），不 fork |
| 2 | NSPG13/agent-bounties | AI agent 懸賞市場 + 協定（A2A/MCP，Base USDC） | 20 | 2026-11-11 | Yes | NOASSERTION | Rust | API+MCP server+CLI+合約結算（依 README，UNVERIFIED） | README 聲明只有鏈上 `BountySettled` 事件才算付款證明（設計理念可借鏡） | C-B：實際成交量 UNKNOWN（我未開 metrics 頁） | 「付款需有不可偽造結算事件」的證據原則 | 2026-07 才建立卻有 1,944 檔、353 open issues，疑似大量自動生成；加密貨幣付款/合規；授權不明 | 僅觀察與借鏡原則，不整合 |
| 3 | speedyapply/JobSpy | 多站職缺爬取（LinkedIn/Indeed/Glassdoor/Google 等） | 4695 | 2026-10-27 | Yes | MIT | Python | 每站一個 scraper 模組 + CLI + `mcp.py`（tree 可見，VERIFIED） | 無（正職 lane） | B：model.py 有 `TAIWAN` country enum（VERIFIED），各站實際支援度 UNVERIFIED | 若你也想追正職 lane，可當 collector | 站台 ToS/封鎖；與外包主軸無關 | 可選 collector，不納入核心 |
| 4 | MaxKmet/idea-validation-agents | B2C 創業點子驗證 agent prompt 集（15 skills，Claude Code/Codex/Cursor） | 510 | 2026-06-16 | Stale（148 天） | MIT | 無（markdown prompts） | 純 prompt + CLAUDE.md/AGENTS.md 路由（README，UNVERIFIED 其他） | 無直接收入功能 | C：驗證方式為 LLM 分析，非實際付款證據 | prompt 結構可參考 Codex+Claude 雙支援 | 已停更；針對 B2C app | 僅參考 |
| 5 | mvanhorn/last30days-skill | 跨 Reddit/X/YouTube/HN 近 30 天研究 skill | 67262 | 2026-11-11 | Yes | MIT | Python | Agent skill + 多來源 pipeline（README，UNVERIFIED 內部） | 無 | B：以互動數/金額（Polymarket）排序，屬需求「訊號」 | 可作為 verification 階段的外部研究工具 | 需第三方 API key、平台 ToS；star 數含宣傳性質（含 Trendshift 徽章） | 可選用為外部 skill，不 fork |
| 6 | datou202307-design/trend-opportunity-radar | 單一主題+單一平台的證據導向社群研究 skill | 16 | 2026-08-26 | Moderate（77 天） | MIT | Python | Agent skill；輸出 HTML/MD/JSON（README） | 無 | B+：要求區分「平台事實/機器擷取/模型判斷」三類證據 | 證據三分類標籤法可借到你的 evidence 欄位 | 建立僅 3 個月；README 自述外部使用者驗證尚未完成 | 借鏡證據標籤法 |
| 7 | roperi/UpworkScraper | 登入後抓取 Upwork Best Matches 存 SQLite | 72 | 2026-11-09 | Yes | MIT | Python | Selenium + SQLite，單次執行 + cron（README） | 間接：職缺含預算 | B | 無（建議不用） | 帳號登入抓取，違反 Upwork ToS 並有封號風險 | 不採用；以官方 email alert 取代 |
| 8 | D4Vinci/Scrapling | Python 爬取框架（radar 的底層依賴） | 101285 | 2026-11-09 | Yes | BSD-3-Clause | Python | 單請求到動態頁（README 描述，UNVERIFIED 內部） | 無 | B | 作為 collector 底層 | radar 因 0.4.8 在 Windows fingerprint 失敗而釘 0.4.1（作者自述） | 可用，鎖版本 |
| 9 | DIYgod/RSSHub | 將各網站轉 RSS | 46922 | 2026-11-11 | Yes | AGPL-3.0 | TypeScript | 路由插件（`lib/routes/*`，tree 共 9462 檔） | 無 | B：tree 檢索未見 104、Upwork、CakeResume、PCC 路由（VERIFIED） | 自架後可為特定來源提供 RSS | AGPL；台灣外包來源覆蓋率低 | 可選基礎設施 |
| 10 | dgtlmoon/changedetection.io | 網頁變更監控與通知 | 35728 | 2026-11-10 | Yes | Apache-2.0 | Python | Web 應用 + fetcher（UNVERIFIED 內部） | 無 | B | 監控無 RSS 的補助/標案/獎金頁面 | 386 open issues；需自行維運 | 可選，用於「無 feed 的台灣頁面」 |
| 11 | openfunltd/pcc.g0v.ronny.tw | 台灣政府電子採購網（PCC）標案資料 API | 37 | 2026-10-29 | Yes | 無偵測（README 稱後端 BSD，資料授權另見網站，UNVERIFIED） | PHP | 資料 API（README，UNVERIFIED 內部） | 標案公告含預算/決標金額（機關公開資料，PARTIALLY VERIFIED：未呼叫 API） | A 級潛力（政府公告，非自稱） | 資料可當台灣在地來源 | 授權條款不明；PHP；標案多為公司/法人資格，個人接案門檻高 | 值得做 PoC 驗證可得資料 |
| 12 | polarsource/polar | 開發者收款/訂閱/billing（merchant of record） | 10468 | 2026-11-11 | Yes | Apache-2.0 | Python | FastAPI 類 Python 後端（UNVERIFIED，由語言推定） | 收款、訂閱、授權 | B（對收入追蹤端有參考價值） | revenue 記錄模型、webhook 設計 | 台灣出款與稅務支援 UNKNOWN | 收入端參考 |
| 13 | midday-ai/midday | 自由工作者財務：發票、時間追蹤、對帳 | 15122 | 2026-06-13 | Stale（151 天） | AGPL-3.0 | TypeScript | Web 應用（UNVERIFIED） | 發票與財務總覽 | B | 資料模型參考 | AGPL；不支援台灣統一發票（UNVERIFIED）；已有 5 個月未更新 | 僅參考 |
| 14 | Sver0411/OpportunityRadar | 學生/職涯新人的機會核實（工作/科研/競賽/開源/資助） | 9 | 2026-09-28 | Moderate（44 天） | MIT | Python | Agent Skill + scripts（303 檔，README） | 無（聚焦資格與時效核實） | B：流程強調「回官方核實、資格、時效、投入成本」 | 核實問題清單可借用 | 2026-09-14 才建立；中文為主；僅 9 star | 借鏡核實流程 |
| 15 | huginn/huginn | 自架「監控並行動」agent | 50494 | 2026-11-09 | Yes | MIT | Ruby | Rails + agent 圖（UNVERIFIED） | 無 | B | 概念參考 | Ruby 技術棧不符；694 open issues | 不採用 |

排除（不列入 15 個）：`digediao/opportunity-radar`（描述為「自动化赚钱」，無授權，屬 get-rich-quick 傾向，未深查，UNVERIFIED）；`Mr-Destroyer/ZIMREAPER`（bug bounty 自動化瀏覽器，涉及授權範圍與法律風險）；`archerthegoat/mars-research-assistant`（交易研究，非本題）；台灣小型標案爬蟲 `aiadminhq/Tender-AI`、`RaptorChin/PCC_Scraper`、`pipeworx-io/mcp-taiwan-procurement`（0–1 star，未深查）；`liangdabiao/reddit-business-idea-validator`（40 star、無授權，未深查）。

台灣在地來源缺口：104 外包網、Tasker、CakeResume 等平台於 GitHub 查無活躍且高品質的開源 collector（`104` 關鍵字僅找到 2020–2025 年、星數 ≤6 的個人爬蟲）。這代表台灣來源必須自建，且需先查各平台 ToS（UNKNOWN）。

---

## 7. 最終建議：Fork radar vs Build from scratch vs Hybrid

**建議：Hybrid（以 radar 為「參考實作 + 部分程式碼來源」，不做整包 fork；核心新建）。**

理由（依證據）：
1. radar 是目前所見最接近「opportunity → ledger → ranking」的真實、有測試的程式碼（VERIFIED：151 測試、CI 綠、offline fixtures、source-admission 流程），但它只覆蓋你流程的前 1–1.5 段（collect → dedup → deterministic score → 人工標記 saved/applied）。
2. 你要的後半段（付款證據驗證、approval gate、Codex/Claude build handoff、submission、revenue tracking 與回饋）在 radar 完全沒有（VERIFIED 缺失）。
3. 約三分之一的實作與巴西綁定（地點、InfoJobs、Gmail alert、Windows 啟動腳本、`brazil_eligibility` 擴散至 extraction/briefing/storage/dashboard），fork 後需大量拆除，且單一維護者、0 star、停更 64 天，上游合併不可期。
4. 你的技術棧（Python、MongoDB、Kafka）可直接承接 radar 的 pydantic `Opportunity` 與 Collector 協定；SQLite 當 MVP ledger 可行，後續再換 MongoDB。是否真需要 Kafka（來源每日只有數十至數百筆）= 沒有證據顯示需要，建議先不用。

具體路線：
- **複製（授權 MIT，保留版權聲明）**：`models.py` 概念、Collector 基類與來源隔離、reddit/HN/Opire/Superteam collectors、金額與截止日抽取（加 TWD/NT$）、source-admission lifecycle 文件、`verify-github-issues` 的存活性檢查邏輯。
- **新建**：`evidence` 子模型（證據等級 A/B/C、驗證時間、驗證者）、付款證據驗證步驟（改寫自 idea-hunt 的 Proof of Wallet 與 agent-bounties 的「結算事件才算付款」原則）、scoring（含證據等級、投入時數、台灣可領款/稅務）、approval 狀態機、build handoff（輸出 spec 給 Codex/Claude）、submission 與 revenue 表。
- **不採用**：TIP（無證據、無授權、已停更）、Shipwright（重、僅 Claude Code）、UpworkScraper（ToS）。
- **優先驗證（PoC，各 1–2 天）**：Opire/Superteam/Algora 的 Taiwan 可領款條件；PCC 標案 API 可得欄位與授權；Upwork Gmail alert 能否取得穩定 ID。

後續待你確認：build-DNA 的 owner/repo（UNKNOWN）；是否接受加密貨幣付款類來源（合規與稅務）；是否將正職 lane 納入範圍。
