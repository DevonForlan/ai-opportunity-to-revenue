# 04 真實 Bounty 樣本研究 (Real Bounty Samples)

存取日期: 2026-11-11。方法: `gh search issues`(read-only)+ `gh api` GET 逐一重新抓取 issue / comments / timeline / repo metadata;未留言、未 claim、未聯絡任何人。
證據等級: A=一手且可重現(GitHub API 原始資料);B=二手/單一來源;C=推論或第三方文章。

## 1. 結論(先看這裡)

1. **誠實計數**: 重新抓取並逐一檢查 28 個「open + 有明確金額」的 issue。其中 **0 個** 同時滿足「未被指派、未結算、sponsor/maintainer 近期仍有回應、競爭者少、付款可證」= **沒有任何一個可標為 VERIFIED-actionable**。(VERIFIED 標籤僅表示「狀態事實已驗證」,例如已指派/已結算。)
2. 「找不到 20 個可行 bounty」本身就是關鍵發現,原因:
   - **農場/垃圾 repo 淹沒搜尋**: `label:"💎 Bounty"` 的前 100 筆 open 結果中約 72 筆來自疑似 farm/spam repo(ClankerNation/OpenAgents、limitlessprojects/Go-Hybrid、UnsafeLabs/Bounty-Hunters、SecureBananaLabs/bug-bounty 等,大量重複 template issue);`label:bounty` 前 100 筆約 87 筆。GitHub 搜尋單次上限 100,故為「前 100 筆」樣本非母體(證據 A,分類為本人判斷)。
   - **Algora 實質萎縮**: algora.io/bounties 現為 404,首頁改為「recruiting」服務(WebFetch,證據 B);coolify#7642 有人留言稱 "Algora's bounty board has since gone offline"(證據 B)。以 `algora-pbc` 為 commenter 的 open issue 僅 33 筆,其中 2025-2026 新建的合法 repo 只有個位數。多數仍標 💎 的 issue 建立於 2023-2025。
   - **AI bot 灌水競爭**: 舊 Algora bounty(onyx、zio、revert、coolify、arakoodev…)下聚集同一批帳號(如 jeffrey-graham、almagas、granbellllc-png、mulak1)在 2026-11-07~11-10 密集留言 /attempt、/claim;onyx#2281 單一 issue 搜尋即見 10+ 個 open PR。對人類開發者,期望值近乎零。
   - **仍活躍的真官方計畫是「指派制」**: Tenstorrent tt-metal(USD 750 / 3000)issue 建立後同日即由 maintainer 指派,對外部申請者已關閉。
3. 本任務範圍內 **Python 且合法的 open bounty 僅 5 個**(onyx#2281、toingg-jarvis #11/#13、tt-metal 兩個已指派、glances 已結算),且金額或可得性都很差。**未找到任何 MongoDB / Kafka 專屬 bounty**(UNKNOWN: 不代表不存在,僅為本次搜尋未見)。
4. Gitcoin / Polar / IssueHunt: 本次搜尋僅在 IssueHunt 見到舊 issue(2025 以前為主,多半為歷史連結),**未驗證任何仍有效金額** → UNKNOWN。Opire 僅出現在農場 repo 文字中。Bountysource 已不在範圍。

## 2. 搜尋命中品質統計(誠實計數)

| 類別 | 數量 | 說明 |
|---|---|---|
| 疑似 farm/spam/scam-like(前100筆 💎 Bounty) | ~72 / 100 | 本人判斷:重複模板、`Solidity $3k/$5k` 大量複製、非真實 sponsor;證據 A(原始清單)+判斷 |
| 疑似 farm/spam(前100筆 label:bounty) | ~87 / 100 | 同上(bounty-plaza、rustchain-bounties、IES-BoilerRoom、agentswarm-examples 等) |
| 詳細檢查的合法性候選 | 28 | 見第3節 |
| 其中已指派 | 6 | tt-metal x3、revert#372/#551、sola#157 |
| 其中已結算(open 但已頒發) | 3 | glances#3485、scratchdata#126/#170(starbasedb#71 亦有 Rewarded 標籤) |
| 其中 repo 停滯(>12 個月無 push) | 6 | dozer x2、revert x2、scratchdata x2(另 pgstrap、flyde 約 5-17 個月) |
| 其中 sponsor 有效性遭質疑 | 5 | zio-schema#712、EdgeChains#273/#286、pgstrap#2、coolify#7642 |
| 其中 >=3 個競爭 PR / claim | 多數 | 見表 |
| 無法驗證金額/平台 | 3 | Qubes#10781(UNKNOWN)、lux#99、EdgeChains#286 |

「stale / closed / already-claimed」精確的逐項數字僅涵蓋上列 28 個詳查項,農場 repo 未逐一檢查(不計入,避免偽精確)。

## 3. 28 個候選逐項(依 Fit 降序)

Fit 公式: 十項子分數(0-10)加權: tech 15、effort(越低工時越高分) 10、AI leverage 10、reward 10、payment confidence 15、competition(越少競爭越高) 15、repo simplicity 5、testability 5、acceptance clarity 5、maintainer responsiveness 10。**子分數為本人主觀判斷(無法由來源量化)**;reward 子分數對金額設上限,且 **已指派/已結算者總分強制封頂 15**(可得性閘門)。高金額不會單獨提高分數。Taiwan eligibility 全部 UNKNOWN(沒有任何來源證明可付款到台灣;Algora 官方文件說明需檢查 eligibility,但本次未能存取其政策頁)。deadline 除 tt-metal#62681 外均 UNKNOWN。工時估計:無來源 → UNKNOWN(effort 子分數僅為主觀相對難度)。

完整欄位(claim rules、付款證據、maintainer responsiveness 等)見 `research/data/bounty_samples.csv`。

| # | Issue | 平台 / 金額 | 語言 | 標籤: 狀態 | 競爭 | Fit | 子分數 (tech,effort,AI,reward,pay,comp,repo,test,accept,maint) |
|---|---|---|---|---|---|---|---|
| 1 | onyx-dot-app/onyx#2281 Jira Service Management Connector | Algora / USD 250 | Python | PARTIALLY VERIFIED: open; label maintainer approved; 2024-08-30 /bounty 250 | 至少10個 open PR 同時競爭;多人 /attempt | 48 | 8,6,8,5,3,1,4,7,5,3 |
| 2 | PG-AGI/toingg-jarvis#11 Pipecat + Gemini real-time integration | Algora / USD 5 | Python | PARTIALLY VERIFIED: open; /bounty $5 | 查到的 PR 皆 closed | 46 | 7,4,8,0,3,5,6,5,5,3 |
| 3 | outerbase/starbasedb#72 Replicate data from external source to internal source via Plugin | Algora / USD 250 | TypeScript | PARTIALLY VERIFIED: open; /bounty $250 | 6+ open PR | 44 | 6,3,7,5,5,1,5,5,4,4 |
| 4 | tari-project/universe#3518 L2 menu opens PIN setup while wallet loading | Tari bounty label(自管) / 15000 XTM(USD 換算 UNKNOWN) | TypeScript/Rust | PARTIALLY VERIFIED: open; 2026-11-07 建立; Acceptance Criteria 明確 | 3+ 人宣告開工,6+ open PR | 41 | 3,6,6,3,3,0,4,7,9,7 |
| 5 | PG-AGI/toingg-jarvis#13 Cross-platform packaging & installers | Algora / USD 5 | Python | PARTIALLY VERIFIED: open; reward eligible/$5 | 3+ /claim,PR #101 #102 + /attempt | 40 | 6,5,8,0,3,1,6,6,6,3 |
| 6 | getdozer/dozer#1690 Sample: Dozer + LLM + Vector DB + Langchain | Algora / USD 250 | Rust/Python sample | PARTIALLY VERIFIED: open; repo 最後 push 2024-06-18 | 多個 open PR | 40 | 7,5,9,5,1,1,6,5,4,0 |
| 7 | zio/zio-http#3141 ClassCastException with HandlerAspect + path params | Algora / USD 150 | Scala | PARTIALLY VERIFIED: open; /bounty $150 | 查到 PR 多數 closed;AI bot 留言多 | 39 | 1,5,6,4,4,2,4,7,6,5 |
| 8 | arakoodev/EdgeChains#273 Qdrant vector DB support in JS SDK | Algora / USD 30 | JavaScript | PARTIALLY VERIFIED: open; 有人詢問 bounty 是否仍有效 | 5+ open PR | 39 | 5,5,8,1,3,1,6,6,5,3 |
| 9 | arakoodev/EdgeChains#290 AWS Comprehend PII redaction utility | Algora / USD 50 + USD 25 | JavaScript | PARTIALLY VERIFIED: open; 2 筆 bounty | 多個 open PR | 39 | 5,5,8,1,3,1,6,6,5,3 |
| 10 | coollabsio/coolify#7642 Add SurrealDB with/without TiKV | Algora / USD 50 | PHP/Docker compose | PARTIALLY VERIFIED: open; 留言者稱 Algora board offline 並詢問是否仍資助 | 3+ /attempt,已有 PR /claim | 39 | 5,6,8,2,1,2,5,6,5,3 |
| 11 | seveibar/pgstrap#2 Use pglite to avoid requiring postgres | Algora(tscircuit) / USD 30 | TypeScript | PARTIALLY VERIFIED: open; 留言者質疑 bounty 是否仍有效 | 6+ open PR | 38 | 5,5,7,1,3,1,7,6,5,2 |
| 12 | zio/zio-schema#511 Unable to convert to TypedValue | Algora / USD 200 | Scala | PARTIALLY VERIFIED: open; /bounty $200 | 多個 open PR | 36 | 1,5,6,5,3,1,4,7,5,4 |
| 13 | arakoodev/EdgeChains#286 Convert endpoints to smart router | 留言稱 USD 200 / USD 200(僅留言,無平台確認) | JavaScript | UNVERIFIED: open; 留言含 Payout~$0 字樣 | 1 open PR | 35 | 4,4,7,3,1,3,6,5,3,2 |
| 14 | microg/GmsCore#2843 WearOS Support | BountyHub 群募 / USD 2340(bot 留言累計) | Kotlin/Java | PARTIALLY VERIFIED: open; 2025-03 起 | UNKNOWN | 32 | 1,0,4,8,3,6,1,2,2,3 |
| 15 | QubesOS/qubes-issues#10781 File copy via clipboard | 非官方 bounty / UNKNOWN | Python/C | UNVERIFIED: open; label bounty | UNKNOWN | 32 | 3,2,5,0,1,7,2,3,3,5 |
| 16 | zio/zio-schema#712 JsonCodec decoder accepts malformed JSON | Algora(歷史) / USD 75(留言稱 label 已移除) | Scala | UNVERIFIED: open; bounty 可能已失效 | PR #1189 open 無回覆 | 30 | 1,5,6,2,1,2,4,8,6,2 |
| 17 | getdozer/dozer#1659 IN clause in streaming SQL | Algora / USD 600 | Rust | PARTIALLY VERIFIED: open; repo 停滯 | 多 PR | 28 | 3,2,6,6,1,1,2,6,5,0 |
| 18 | Spectral-Finance/lux#99 LLM Provider Abstraction Layer | bounty label(標題 $600) / USD 600 | Elixir | UNVERIFIED: open; 多個 PR 含 AI 生成 | 10+ | 28 | 1,2,8,6,1,0,3,6,5,2 |
| 19 | nicolargo/glances#3485 New version of WebUI | Algora($1k label) / USD 1000 label / Algora 實付 USD 1(據外部留言) | Python/JS | VERIFIED(已結算,不可領): open 但已 merge 並 rewarded; label inactive | 已完成 | 15 | 3,2,3,0,1,0,6,3,2,6 |
| 20 | tenstorrent/tt-metal#64575 Fix sharded softmax on offset core grids | Tenstorrent Bounty Program / USD 750 | C++/Python | VERIFIED(已指派): open; 已指派 singhharsh1708 | 已指派;另有 PR #64935 | 15 | 3,3,6,6,6,0,2,6,8,9 |
| 21 | tenstorrent/tt-metal#64647 Fix remaining sharded scale_mask_softmax mask issues | Tenstorrent Bounty Program / USD 750 | C++/Python | VERIFIED(已指派): open; 已指派 xevrion | 已指派;PR #64731 | 15 | 3,3,6,6,6,0,2,6,8,9 |
| 22 | tenstorrent/tt-metal#62681 Static checker for compute-kernel API ordering | Tenstorrent Bounty Program / USD 3000 | Python/C++ | VERIFIED(已指派): open; 2026-11-02 指派 ke1rro,2個月期限,逾期重開 | 已指派;另有人已做原型 | 15 | 5,1,6,9,6,0,2,7,8,9 |
| 23 | outerbase/starbasedb#71 Improve test coverage with Vitest | Algora / USD 250 | TypeScript | PARTIALLY VERIFIED: open 但已有 Rewarded label,USD 250 已頒發 varshith257 | 4+ open PR | 15 | 4,5,7,5,5,1,5,8,4,4 |
| 24 | revertinc/revert#372 Workday Integration | Algora / USD 100 | TypeScript | PARTIALLY VERIFIED: open; 已指派 ezhil56x | 多個 open PR | 15 | 3,3,6,3,2,1,5,4,3,1 |
| 25 | revertinc/revert#551 Workable Integration | Algora / USD 100 | TypeScript | PARTIALLY VERIFIED: open; 已指派 2 人 | 多個 open PR | 15 | 3,3,6,3,2,1,5,4,3,1 |
| 26 | TheSolaAI/sola-application#157 Make blinks interaction hands-free | Algora / USD 70 | TypeScript | PARTIALLY VERIFIED: open; 已指派 2 人 | 多個 open PR | 15 | 3,4,6,2,3,1,5,4,4,3 |
| 27 | scratchdata/scratchdata#170 UI for DB connection add/delete | Algora / USD 150(已頒發) | Go | VERIFIED(已結算): open 但已頒發 CodeMan99 | 已完成 | 15 | 1,3,5,0,5,0,5,5,4,0 |
| 28 | scratchdata/scratchdata#126 AWS Secret Manager for DB credentials | Algora / USD 150(已頒發) | Go | VERIFIED(已結算): open 但已頒發 mehulmathur16 | 已完成 | 15 | 1,3,5,0,5,0,5,5,4,0 |

## 4. 重點個案觀察

- **onyx-dot-app/onyx#2281 (Python, USD 250)**: 全場 Fit 最高(48),但仍是「低」: 10+ open PR 競爭,maintainer 自 2024-08-30 後無回覆紀錄,repo 本身活躍(2026-11-11 push)。需 PR 含 `/claim #2281`。若要碰,最大風險是被先 merge 或 sponsor 不再用已下線的 Algora 付款。
- **tenstorrent/tt-metal**: 唯一看起來仍有官方流程的計畫(Bounty T&C、assign、2 個月期限),但 issue 為 community-suggested 後由提案者領走;需硬體/Tenstorrent Cloud,C++/kernel 為主,不符 Python/data 背景。可追蹤未來 `bounty_candidate` 新 issue(證據 A)。
- **glances#3485**: 提供「付款風險」實例 — label 寫 $1k,Algora 實付 $1(僅為外部留言單一來源,證據 B)。
- **starbasedb#71/#72**: 同 repo 有明確頒發 USD 250 的紀錄(付款證據 A),但 #72 已有 6+ open PR。
- **coolify#7642**: 與 data/DB 部署相關(SurrealDB template),USD 50,但留言稱 Algora 下線且 sponsor 為個人。
- **tari-project/universe**: 自管 bounty(15,000 XTM),Acceptance Criteria 寫得最清楚,但 3 人以上已宣告開工,且 XTM 兌 USD、台灣收款均 UNKNOWN。

## 5. 對「Taiwan 開發者 + AI agent」的含義(僅限已驗證事實)

- 沒有任何來源證明 Algora / Tenstorrent / Tari 能付款給台灣個人(UNKNOWN)。tt-metal 條款註明「local tax requirements may apply」。
- AI 輔助並非優勢: 此類 bounty 已被大量 AI 自動提案帳號佔據(同一批帳號在 10+ issue 同時 /attempt),速度與數量不再稀缺。
- 建議(決策者自行判斷): 不應把 GitHub bounty 當作可預期收入來源;若要實測,先在 tt-metal 觀察新建 issue、或針對 Python repo 搜尋「新建 24 小時內、maintainer 親自 /bounty、無 PR」的 issue,並先在 Algora 確認 payout 國家支援。

## 6. 限制

- GitHub search 單次上限 100 筆,農場比例為前 100 筆的樣本。
- 搜尋未涵蓋 Gitcoin/Polar/Opire 的專屬平台頁面(無法以 gh 驗證),IssueHunt 只見舊項目。
- 各 PR 的 open/closed 以 issue timeline 前 100 筆事件中的 cross-reference 為準,可能少計。
- 所有主觀分數需人工複核;本文件不是財務/法律建議。
