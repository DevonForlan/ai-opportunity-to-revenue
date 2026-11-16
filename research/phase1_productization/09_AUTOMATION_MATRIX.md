# 09 Automation Matrix：21 步工作流拆解

日期：2026-11-16　標記：BASELINE / NEW EVIDENCE / INFERENCE

## 0. Method & Limitations

- 方法：以官方 MongoDB 文件（`.md` 版本逐頁確認 HTTP 200 與內容）確認每個命令存在與語意；分類（class）、AI usefulness、hallucination risk 等欄位為 **INFERENCE（作者判斷，非實測）**。
- 來源：`_sources/deliverables_automation.csv`（41 列；31 vendor_official、5 OSS repo、3 blog、2 其他 vendor docs）。無 pain/hiring/purchase 證據。
- **自動化百分比 = UNKNOWN**（未量測；本文件不給任何百分比）。
- **本地測試：not tested。** Docker daemon 未啟動（`failed to connect to the docker API ... dockerDesktopLinuxEngine`），本機無 `mongod` / `mongosh`（`which` 皆無）。依指示不啟動重量級環境，未碰任何真實資料庫。所有命令輸出格式、權限需求均來自文件而非實測。
- **權限限制**：內建角色頁成功取得角色一句話描述（clusterMonitor＝「對監控工具（Cloud/Ops Manager agent）的唯讀存取」；read＝所有非 system collection；readAnyDatabase＝除 local/config 外所有 DB 的 read + listDatabases；dbAdmin＝schema/索引/統計類管理，不含 user/role 管理），但**逐 action 權限表未擷取**。因此「最小角色」欄除頁面直接證實者外，皆為 **UNVERIFIED（文件待逐 action 核對）**。頁面直接證實：`$indexStats`→至少 clusterMonitor；`listIndexes`→內建 `read` 即足夠；`$currentOp` 看所有使用者→`inprog` 權限；`usersInfo` 看他人→`viewUser` action；`listDatabases` 依 `authorizedDatabases`/`listDatabases` action 回傳範圍不同。
- 官方文件基底 URL：`https://www.mongodb.com/docs/manual/`（以下簡寫 `M/`）。

## 1. 分類圖例

- **DS** deterministic script；**RE** rule engine（確定性規則 + 門檻）；**LLM** LLM-assisted（人覆核）；**HR** human review required；**HO** human-only high-risk。
- Hallucination risk：LLM 介入此步時產生不實內容的風險（INFERENCE）。Production risk：對客戶系統的影響風險。Auditability：輸出可被第三方重現/追溯的程度。

## 2. 主矩陣

| # | 步驟 | 主 class | 確定性可行度 | AI 有用度 | Hallucination 風險 | 所需人類專長 | Production 風險 | Auditability |
|---|---|---|---|---|---|---|---|---|
| 1 | Environment inventory | DS + HR | 高（命令）；部署型態/責任分界需訪談 | 低 | 低 | 判讀部署型態、取得授權 | 低（唯讀） | 高 |
| 2 | Evidence collection | DS | 高 | 低（僅協助撰寫腳本） | 低（腳本需人審） | 寫/審唯讀腳本、最小權限設計 | 低~中（見各命令；`explain executionStats`、`validate`、profiler 啟用除外） | 高（manifest+hash） |
| 3 | Log parsing | DS + LLM | 高（MongoDB 4.4+ 為結構化 JSON 日誌，`getLog` 範例可見 `t/s/c/id/ctx/msg/attr`） | 中（聚類、摘要慢查詢） | 中（摘要可能漏列/誤歸因） | 讀 log 判斷真偽 | 低（需客戶提供檔；`getLog` 受 RAM 緩衝限制） | 中高 |
| 4 | Metrics normalization | DS | 高 | 低 | 低 | 理解各指標單位/重置語意 | 低 | 高 |
| 5 | Config validation | RE | 高（官方 checklist 可轉規則；版本相依，如 THP 8.0 啟用 / 7.0 以下停用） | 低~中（說明規則來源） | 低（規則為確定性）；LLM 解釋時中 | 判斷規則適用情境 | 低 | 高 |
| 6 | Topology analysis | RE + HR | 中高（成員數/votes/priority 可規則化；容錯判斷需情境） | 中 | 中 | 高（HA 設計） | 低 | 高 |
| 7 | Replication analysis | RE | 高（member state、lag、optime 差） | 低~中 | 低~中 | 中高 | 低 | 高 |
| 8 | Oplog analysis | RE | 高（window = 時間差；需配合寫入速率） | 低 | 低 | 中（結合備份/還原時間、Debezium 停機容忍） | 低 | 高 |
| 9 | Index review | RE + HR | 中（未使用/重複/前綴冗餘可規則化；「可否刪除」需情境） | 中 | 中 | 高（刪索引風險、唯一/TTL/hidden index） | 低（讀）；建議落地為高風險 | 高 |
| 10 | Query/performance analysis | LLM + HR | 低~中（COLLSCAN、docsExamined/nReturned 可規則；因果判斷難） | 中高 | **高**（易編造因果與調校數字） | 高 | 中（`explain(executionStats)` 會實際執行查詢；profiler 啟用改變伺服器狀態） | 中 |
| 11 | Capacity analysis | DS + HR | 中（單點快照可算；預測需時序資料） | 低~中 | 中高（外推為「預測」時） | 高 | 低 | 中 |
| 12 | Backup review | HR | 低（備份檔存在可檢；可還原性需演練） | 低 | 中 | 高 | 低（讀）~**高**（還原演練需隔離環境） | 中 |
| 13 | Security review | RE + HR | 中（auth/bindIp/TLS/角色盤點可規則化） | 低~中 | 中 | 高（最小權限、合規判斷） | 低；**本身涉及敏感資訊（user/role 清單）** | 高 |
| 14 | Upgrade readiness | RE + HR | 中（版本/FCV/EOL 規則化；相容性影響需讀 release notes） | 中（彙整 release notes） | **中高**（相容性斷言須有官方出處） | 高 | 低（讀）；升級執行屬 HO | 中高 |
| 15 | Finding generation | RE + LLM | 中（規則命中即成 finding 草稿） | 中 | 中 | 高 | 無 | 高（若綁 rule_id + evidence） |
| 16 | Evidence citation | DS | 高（schema 強制 `evidence_refs`、檢查指標存在） | 低（LLM 僅排版） | **高**（LLM 生成引用易造假，須程式驗證） | 低 | 無 | 高 |
| 17 | Severity classification | RE + HR | 中（規則給初值；情境調整靠人） | 低~中 | 中 | 高 | 無 | 中高（需記錄 rationale） |
| 18 | Recommendation generation | LLM + HR | 低 | 中高 | 中高 | 高 | 間接：錯誤建議落地風險高 | 中 |
| 19 | Report generation | LLM + DS(模板) | 中高（模板 + 資料填充） | 高（敘述文字） | 中（敘述超出證據） | 中（審稿） | 無 | 中 |
| 20 | QA | HR + DS | 中（schema 驗證、引用存在、數字對帳可自動） | 中（輔助找矛盾） | 中 | 高（第二人覆核） | 無 | 高 |
| 21 | Customer presentation | HO | 低 | 低（簡報草稿） | 中 | 高（溝通、承擔判斷） | 無（但承諾/責任風險高） | 低 |

註：「AI 有用度」「hallucination」為 INFERENCE；未做 eval，不給數字。

## 3. 輸入、輸出、命令、來源、所需權限

| # | Input | Output | MongoDB 命令 / 資料源（官方文件） | 最小存取（已證實 vs UNVERIFIED） |
|---|---|---|---|---|
| 1 | 客戶訪談表、連線授權 | environment.json（部署型態、版本、成員、DB/collection 清單） | `listDatabases` `M/reference/command/listDatabases/`；`hello`；`buildInfo`；`rs.conf()` `M/reference/method/rs.conf/`；`sh.status()` `M/reference/method/sh.status/` | `listDatabases` 回傳受 `authorizedDatabases` 與使用者 `listDatabases` 權限影響（已證實）；其餘 UNVERIFIED（預期 clusterMonitor 足夠，待核） |
| 2 | 命令清單、唯讀帳號 | raw/ 輸出 + manifest（版本、角色、hash） | `connectionStatus` `M/reference/command/connectionStatus/`（先驗證帳號實際權限）；其餘見下 | 人工建立專用唯讀帳號（建議 clusterMonitor + read/readAnyDatabase）；**建立帳號是客戶端動作** |
| 3 | mongod 日誌檔 / `getLog` | 解析後事件表（慢查詢、連線、選舉、錯誤） | `getLog` `M/reference/command/getLog/`；日誌檔；`keyhole -loginfo`（Apache-2.0，B） | `getLog`：UNVERIFIED；日誌檔由客戶提供更安全（避免主機存取） |
| 4 | raw/ | metrics.json（統一單位、時間戳） | `serverStatus` `M/reference/command/serverStatus/`（巨大輸出）；FTDC（`mongo-health` 以 clusterMonitor 取 diagnostic data；B，blog） | serverStatus：UNVERIFIED（預期 clusterMonitor） |
| 5 | `getCmdLineOpts`、`getParameter`、OS 輸出 | config_findings 草稿（rule_id + 命中） | `getCmdLineOpts` `M/reference/command/getCmdLineOpts/`；`getParameter` `M/reference/command/getParameter/`；Operations/Security Checklist | UNVERIFIED；OS 層（THP、ulimit、filesystem）需主機 shell，**DB 帳號無法取得** |
| 6 | environment.json、rs.conf | topology 圖與規則命中（偶數投票、單 AZ、priority 異常） | `rs.conf()`；`replSetGetStatus` `M/reference/command/replSetGetStatus/`；`sh.status()` | UNVERIFIED（待核 clusterMonitor） |
| 7 | replSetGetStatus 多次取樣 | 成員狀態、lag（optime 差）、heartbeat 異常 | `replSetGetStatus`；`rs.printReplicationInfo()`/`db.printReplicationInfo()`（顯示 slave/secondary 落後） | UNVERIFIED |
| 8 | getReplicationInfo、寫入速率 | oplog window（小時）、size、與還原時間/connector 停機容忍比較 | `db.getReplicationInfo()` `M/reference/method/db.getReplicationInfo/`（腳本用，回傳 JSON）；`rs.printReplicationInfo()` `M/reference/method/rs.printReplicationInfo/`（不回傳 JSON，僅人看）；oplog 概念 `M/core/replica-set-oplog/` | 讀 `local.oplog.rs` 的權限 UNVERIFIED（clusterMonitor 描述含 config/local 存取之說見 built-in roles 頁交叉註記，待核） |
| 9 | listIndexes、$indexStats、查詢模式 | 索引清單；未使用/重複/冗餘候選（附觀察窗口） | `listIndexes` `M/reference/command/listIndexes/`；`$indexStats` `M/reference/operator/aggregation/indexStats/`；`explain` | `listIndexes`：內建 `read` 足夠（已證實）；`$indexStats`：至少 clusterMonitor（已證實，頁面所述） |
| 10 | 慢查詢日誌/profiler、query shapes | query shape 清單、COLLSCAN、docs examined/returned、候選索引（待驗證） | `db.collection.explain()` `M/reference/method/db.collection.explain/`；Database Profiler `M/reference/database-profiler/`；`$currentOp` `M/reference/operator/aggregation/currentOp/`；Atlas Performance Advisor（M10+，Impact 排序，Atlas 專用） | `$currentOp` 看全部使用者需 `inprog`（已證實）；explain 需對目標 collection 的 find 權限（read，UNVERIFIED）；profiler 需寫入權限/啟用屬變更 → **超出唯讀** |
| 11 | dbStats、collStats、serverStatus | 容量表、cache 壓力、成長（若有時序） | `dbStats` `M/reference/command/dbStats/`；`collStats` `M/reference/command/collStats/`；`db.collection.stats()` | read（dbStats/collStats 文件列於 read/dbAdmin 類，UNVERIFIED） |
| 12 | 備份政策、備份日誌、還原演練紀錄 | backup_readiness 表（方式/RPO/RTO 是否已量測） | `mongodump`/`mongorestore`（`M/reference/program/mongodump/`、`mongodb/mongo-tools`）；`validate` `M/reference/method/db.collection.validate/`；Backup Methods `M/core/backups/` | 備份角色 `backup`；還原驗證應在**客戶隔離環境**，我方不應連 production 還原 |
| 13 | usersInfo、getCmdLineOpts、TLS 設定 | 安全 findings（auth off、過寬角色、無 TLS、bindIp 0.0.0.0） | `usersInfo` `M/reference/command/usersInfo/`；`connectionStatus`；`getCmdLineOpts`；Security Checklist | 看他人 user 需 `viewUser`（已證實）→ 超出 clusterMonitor，需客戶額外授權或由客戶自行匯出（遮罩） |
| 14 | buildInfo、FCV、driver 版本清單、lifecycle 頁 | 升級 readiness 表（EOL、升級路徑、相容性風險） | `buildInfo`；`getParameter {featureCompatibilityVersion:1}`；`setFeatureCompatibilityVersion` 文件（僅讀，不執行）`M/reference/command/setFeatureCompatibilityVersion/`；EOL `https://www.mongodb.com/legal/support-policy/lifecycles` | UNVERIFIED（預期 clusterMonitor）；driver 版本需客戶應用端資訊 |
| 15 | 步驟 5–14 輸出 | findings.json 草稿 | 無（內部） | 無 |
| 16 | findings 草稿 + evidence bundle | 每個 finding 的 evidence_refs（檔案、命令、JSON pointer、sha256） | 無 | 無 |
| 17 | findings | severity + rationale（規則初值 + 人調整） | 無 | 無 |
| 18 | findings + 官方文件連結 | recommended_action、priority、complexity、rollback 說明 | 引用官方文件作為 source_basis | 無 |
| 19 | findings.json + 模板 | report.md / pdf | 無 | 無 |
| 20 | 全部 | QA 清單（schema 通過、引用可解析、數字對帳、敏感資訊掃描） | 無 | 無 |
| 21 | 報告 | readout 簡報、Q&A | 無 | 無 |

## 4. 需要「超出唯讀 clusterMonitor/read」的項目（彙整）

- `usersInfo` 他人（viewUser）、`$currentOp allUsers`（inprog）、啟用 profiler、`explain(executionStats)`（對資料 collection 的讀取＋實際執行負載）、還原演練（需隔離環境）、OS 層設定（主機 shell，非 DB 權限）、Atlas 層級（API key Project Read Only，來自 mongo-health 文件，B）。
- INFERENCE：**第一階段可只靠 clusterMonitor +（選配）read 完成 topology/replication/oplog/config/version 的 8–9 成證據面**這個說法**未驗證**（未實測、權限表未核對），僅作為待驗證假設。

## 5. Kafka / Data pipeline 擴充（步驟 6–8、14 的平行項）

- Debezium（A）：失敗模式—unexpected 終止重送、`ChangeStreamHistoryLost`(286) 因 oplog 已滾過 resume point；lag 指標 `MilliSecondsBehindSource`；所需權限依 `capture.scope` 的 read + `hello`（+ sharded 讀 `config.shards`）。→ 可規則化：oplog window ≥ 預期 connector 停機時間；connector task state（Kafka Connect REST，官方端點細節本輪未驗證）。
- MongoDB Kafka Connector（A）：resume token 存為 Kafka offset；token 與 oplog 對不上＝invalid resume token。
- Confluent 官方 review checklist：UNKNOWN（未找到）。

## 6. 對「可自動化範圍」的結論（INFERENCE，不含百分比）

- 適合 DS/RE 且低風險：1、2、4、5、7、8、16、20（部分）。
- 需 LLM 但必須人覆核：3、10、18、19。
- 必須人：6/9/13/14 的情境判斷、12 的還原演練、17 的最終 severity、21。
- **最大風險不是技術而是治理**：LLM 處理客戶 evidence 與 WebComm 政策衝突（見 08 §7）；LLM 生成引用/建議的 hallucination 須以 schema + 程式驗證擋下。
- 建議的第一個可實作原型（INFERENCE）：步驟 2+5+7+8+14 的唯讀蒐集器 + rule engine + evidence bundle schema，**先對自己架設的拋棄式本機實例測試**（目前環境無 Docker/mongod，需先由人安裝；本輪 not tested）。

## 7. 計數

來源 CSV 41 列：vendor_official 31、oss_repo 5、vendor_blog 3、vendor_education 1、vendor_docs 1；證據等級 A 31 / B 7 / C 2 / UNKNOWN 1。evidence_type：documentation/provider_marketing；pain/hiring/purchase = 0。
