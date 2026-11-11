# repos.md — 來源清單（Repo 研究）

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
