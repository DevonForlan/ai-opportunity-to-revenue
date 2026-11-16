# 08 Deliverables Blueprint：MongoDB / Data Platform Assessment 到底交付什麼

日期：2026-11-16　標記：BASELINE / NEW EVIDENCE / INFERENCE　證據等級 A=官方 B=高可信二手 C=社群

## 0. Method & Limitations

- 方法：WebFetch 官方文件（含 `.md` 版本）、GitHub API（license / pushed_at）、WebSearch 摘要。來源清單見 `_sources/deliverables_automation.csv`（41 列：vendor_official 31、oss_repo 5、vendor_blog 3、vendor_education 1、vendor_docs 1；證據等級 A 31 / B 7 / C 2 / UNKNOWN 1（含 1 個 404 嘗試與 1 個負面搜尋結果）；evidence_type 全為 provider_marketing 或 documentation，**沒有任何 pain / hiring / purchase 類證據**，本文件不處理需求面）。
- **重要限制**：
  1. **找不到任何 Percona MongoDB 審計「樣本報告」公開檔**（搜尋只回傳 audit-logging 文件）。NEW EVIDENCE（負面結果）：公開市面上「付費審計 deliverable 的實際樣貌」無法由 vendor 樣本直接驗證，下列結構中凡標 INFERENCE 者是由官方 checklist + OSS 工具輸出 + 通用顧問實務推導，不是複製某家樣本。
  2. Studio3T、Hackolade、Ops Manager/Cloud Manager health check、Confluent 官方 review checklist：**本輪未研究 / 僅 snippet，UNKNOWN**。Atlas Schema Suggestions 文件 URL 404，內容 UNVERIFIED。
  3. WebFetch 由小模型摘要頁面，個別數字（EOL 日期）請在對客前回官方頁面重核。
  4. 內建角色的「逐 action 權限表」未成功擷取；每個 command 對應最小角色僅 `$indexStats→clusterMonitor`、`listIndexes→read`、`$currentOp allUsers→inprog`、`usersInfo 他人→viewUser` 為頁面直接證實，其餘標 UNVERIFIED（見 09）。
  5. 未做本地實測（見 09）。

## 1. 公開參考資料盤點

| 類別 | 來源 | 證據 | 可借用於 | 備註 |
|---|---|---|---|---|
| 官方 checklist | Operations Checklist `.../administration/production-checklist-operations/` | A VERIFIED | 設定盤點規則：XFS/ext4、避免 NFS、THP（8.0+ 啟用、7.0 以下停用）、oplog 需涵蓋維護窗口與還原時間、奇數投票成員、監控 replication lag / oplog window、定期演練還原 | 規則可寫成 rule engine |
| 官方 checklist | Security Checklist `.../administration/security-checklist/` | A VERIFIED | 啟用 auth、RBAC 最小權限、TLS、bindIp/防火牆、audit（Enterprise）、noscripting、追 CVE 與 EOL | |
| 官方 | Production Notes | A（內容未細讀） | 硬體/OS baseline | PARTIALLY VERIFIED |
| 官方 lifecycle | `https://www.mongodb.com/legal/support-policy/lifecycles` | A VERIFIED（摘要） | 版本風險：6.0 EOL 2025-07-31；7.0 2027-08-31；8.0 2029-10-31；8.2 2026-07-31；5.0/4.4 已 EOL。Atlas Auto-Upgrade track 日期與 Enterprise 表不同 | 以今日 2026-11-16：6.0 已過 EOL |
| 官方 | FCV `setFeatureCompatibilityVersion` | A | 升級後設 FCV 前先 burn-in，因啟用不可回退功能使降級複雜 | 讀 FCV 用 getParameter |
| 官方（Atlas） | Performance Advisor | A VERIFIED | 輸出範本：依 Impact（浪費讀取 bytes）排序的 suggested indexes、Query Targeting（docs read / returned）、慢查詢分組；僅 M10+；有角色限制 | 自管環境無此功能，需自行以 log+explain 近似 |
| 官方 | Atlas Schema Suggestions | UNVERIFIED | — | URL 404 |
| OSS | Percona `mongo-health`（blog；repo `zelmario/mongo-health`，Apache-2.0 依 blog） | B | 一份「單一結論 + 逐項 finding 卡片（起始時間、成員、圖表、次數、下一步）」的輸出形式；68 檢查；FTDC 為資料源；clusterMonitor 即可；僅 replica set；每小時檢查 | repo 本輪未 fetch，license/活躍度 UNVERIFIED；**不得對客戶環境執行未審查第三方碼** |
| OSS | `simagix/keyhole` | B | `-loginfo` 日誌分析、cluster info、FTDC、兩叢集比較 | GitHub API：Apache-2.0、最後 push 2026-01-06、392 stars；README 聲明非 MongoDB 官方支援 |
| OSS | `mongodb-js/mongodb-schema` | B | 以抽樣文件推斷 schema | Apache-2.0；pushed 2026-10-01；**會讀客戶文件資料** → 與資料最小化衝突 |
| OSS | `mongodb/mongo-tools` | A | mongodump/mongorestore 還原驗證 | license 欄 NOASSERTION，需查 LICENSE |
| OSS | `percona/percona-toolkit` | B | pt-style 「摘要+digest」報告風格參考 | GPL-2.0；MongoDB 專屬工具本輪未驗證 |
| Kafka | Debezium MongoDB docs | A VERIFIED | 失敗模式：unexpected 終止→從最後記錄 offset 重送（至少一次，需處理重複）；停機過久→`ChangeStreamHistoryLost`(286)；`snapshot.mode=when_needed`；事件上限 16MB；lag 指標 `MilliSecondsBehindSource`(+P50/P95/P99)、`MilliSecondsSinceLastEvent`、`QueueRemainingCapacity`；所需權限：依 `capture.scope` 的 read、`hello`、sharded 需讀 `config.shards` | 恢復：刪除重建 connector（不同名）或清 offset；預防：oplog 大小/min retention（4.4+） |
| Kafka | MongoDB Kafka Connector change streams | A VERIFIED | resume token 存為 Kafka offset topic；token 對不到 oplog＝invalid resume token | 恢復頁面未讀 |
| Kafka | Confluent / Redpanda 監控（snippet） | B/C，UNVERIFIED | connector/task status、failed task、consumer lag | 官方 Confluent review checklist 未找到，UNKNOWN |
| 部署範本 | Kestra oplog sentinel blueprint | C | 自動化 oplog window + lag 檢查的先例 | snippet |

## 2. 將公開材料拆成報告章節（每章：典型內容 / 可證據化來源 / 標記）

| # | 章節 | 典型內容 | 證據來源（命令/檔案） | 備註 |
|---|---|---|---|---|
| 1 | Executive summary | 一頁：整體風險燈號、Top 5 finding、建議順序、不確定處 | 由 finding register 衍生 | mongo-health 的「單一結論連到 finding」是可參考形式（B） |
| 2 | Topology snapshot | 部署型態（standalone/RS/sharded/Atlas）、成員角色、priority/votes、hidden/delayed、版本、跨 AZ | `rs.status()`、`rs.conf()`、`hello`、`sh.status()` | 官方 checklist 之奇數投票、≥3 資料中心 |
| 3 | Configuration inventory | mongod 啟動參數、storage engine、cache、bindIp、auth、TLS、OS（THP、readahead、ulimit、filesystem） | `getCmdLineOpts`、`getParameter`、OS 檔（需主機存取，**超出 DB 帳號**） | OS 層多需客戶提供指令輸出 |
| 4 | Finding register | 見 §4 欄位 | 全部 | 核心 deliverable |
| 5 | Capacity / performance observations | 資料/索引大小、成長、working set vs cache、連線、queue、慢查詢 | `dbStats`、`collStats`、`serverStatus`、FTDC、log | 單次快照無法證明趨勢；趨勢需 ≥數天指標，否則標 UNKNOWN |
| 6 | Index findings | 未使用索引、重複/前綴冗餘索引、缺索引（COLLSCAN、docsExamined/nReturned 高）、索引大小 | `$indexStats`、`listIndexes`、log/profiler、`explain` | `$indexStats` 計數於重啟後歸零，需註明觀察窗口（INFERENCE：以 serverStatus uptime 判斷） |
| 7 | Replication / oplog | 成員狀態、lag、oplog window（小時）、oplog 大小 vs 寫入速率、選舉歷史、w:majority 使用 | `replSetGetStatus`、`db.getReplicationInfo()`、`rs.conf()` | Debezium 文件明示 oplog 需長於預期停機時間 |
| 8 | Backup / restore readiness | 備份方式、頻率、保留、最近一次還原演練證明、RPO/RTO 是否已量測 | 客戶提供的備份排程/日誌；`mongodump`/還原演練（**需客戶環境中另起測試目標**） | 官方：定期測試備份還原以估計復原時間。**僅憑「有備份檔」不等於可還原** |
| 9 | Upgrade / compatibility | 現行版本 vs EOL、FCV、driver 版本、deprecated 功能使用、升級路徑（逐 major） | `buildInfo`、`getParameter featureCompatibilityVersion`、lifecycle 頁、release notes | driver 相容：lifecycle 頁註記 EOL 超過 3 年後 driver 不再相容（A，摘要） |
| 10 | Security / access control | auth 是否開啟、使用者/角色盤點、過度權限、TLS、bindIp、audit、noscripting | `getCmdLineOpts`、`usersInfo`、`connectionStatus`、`getParameter` | 盤點他人 user 需 viewUser（超過 clusterMonitor） |
| 11 | Operational risks | 單點、無監控/告警、磁碟水位、runbook 缺失、知識集中 | 訪談 + 上列證據 | 含大量人為判斷 |
| 12 | Technical appendix | 原始命令輸出（遮罩後）、查詢清單、方法與限制 | evidence bundle | |
| 13 | Remediation roadmap | 0–2 週 / 1–2 月 / 季度；依賴順序；變更風險與回退 | 由 finding 優先級衍生 | 實作屬額外 scope（INFERENCE） |
| 14 | Walkthrough | 60–90 分鐘 readout、Q&A | 人 | 非自動化 |
| 15 | Machine-readable evidence bundle | JSON/NDJSON 命令輸出 + manifest + hash | 蒐集器 | 見 §5 |

## 3. 公開材料沒有給的（缺口）

- 沒有任何公開來源給出「severity 評分標準」或「likelihood」的統一定義；這是服務提供者自訂。**INFERENCE：不要輸出機率數字**；likelihood 僅在有證據（例：oplog window 3 小時 < 備份還原時間 8 小時 → 已可證明的條件）時才給定性等級，否則欄位留 `not_assessed`。
- 沒有公開來源支持「報告頁數、交付天數」的市場標準；Phase 0 的 Percona 價格 anchor（BASELINE：$11,400 起 / AVP $490）屬 provider_marketing，非成交價。

## 4. Finding register 欄位與 JSON Schema（INFERENCE）

欄位設計原則：每個 finding 必須指向 ≥1 個 evidence item；severity 由規則 + 人覆核；不輸出無依據的 likelihood/金額。

欄位：`id`, `title`, `category`（topology/config/index/replication/oplog/backup/upgrade/security/capacity/ops）, `scope`（cluster/member/db/collection）, `observation`（事實陳述，不含推論）, `evidence_refs[]`, `evidence_status`（VERIFIED / PARTIALLY_VERIFIED / UNVERIFIED / UNKNOWN）, `source_basis`（官方文件 URL 或 rule id）, `severity`（critical/high/medium/low/info）, `severity_rationale`, `impact`（若 X 發生會怎樣，限可說明者）, `likelihood`（`not_assessed` 或 low/med/high + `likelihood_basis`）, `recommended_action`, `priority`（P0–P3）, `remediation_complexity`（S/M/L + `requires_downtime` bool + `rollback_note`）, `confidence`, `reviewed_by`（human id）, `review_status`（draft/reviewed/accepted_by_customer/disputed）, `detected_by`（rule_id 或 llm_assisted）, `limitations`。

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Finding",
  "type": "object",
  "required": ["id","title","category","observation","evidence_refs","evidence_status","severity","severity_rationale","recommended_action","priority","remediation_complexity","review_status","detected_by"],
  "properties": {
    "id": {"type": "string", "pattern": "^F-[0-9]{3}$"},
    "title": {"type": "string"},
    "category": {"enum": ["topology","config","index","replication","oplog","backup","upgrade","security","capacity","ops","integration"]},
    "scope": {"type": "object", "properties": {"level": {"enum": ["cluster","member","database","collection"]}, "name": {"type": "string"}}},
    "observation": {"type": "string"},
    "evidence_refs": {"type": "array", "minItems": 1, "items": {"type": "object",
      "required": ["bundle_file","command","captured_at_utc","sha256"],
      "properties": {"bundle_file": {"type": "string"}, "command": {"type": "string"}, "json_pointer": {"type": "string"}, "captured_at_utc": {"type": "string", "format": "date-time"}, "sha256": {"type": "string"}}}},
    "evidence_status": {"enum": ["VERIFIED","PARTIALLY_VERIFIED","UNVERIFIED","UNKNOWN"]},
    "source_basis": {"type": "array", "items": {"type": "string", "format": "uri"}},
    "severity": {"enum": ["critical","high","medium","low","info"]},
    "severity_rationale": {"type": "string"},
    "impact": {"type": "string"},
    "likelihood": {"type": "object", "properties": {"level": {"enum": ["not_assessed","low","medium","high"]}, "basis": {"type": "string"}}, "default": {"level": "not_assessed"}},
    "recommended_action": {"type": "string"},
    "priority": {"enum": ["P0","P1","P2","P3"]},
    "remediation_complexity": {"type": "object", "required": ["size"], "properties": {"size": {"enum": ["S","M","L"]}, "requires_downtime": {"type": "boolean"}, "rollback_note": {"type": "string"}}},
    "confidence": {"enum": ["high","medium","low"]},
    "detected_by": {"type": "string"},
    "review_status": {"enum": ["draft","reviewed","accepted_by_customer","disputed"]},
    "reviewed_by": {"type": "string"},
    "limitations": {"type": "string"}
  },
  "allOf": [{"if": {"properties": {"severity": {"enum": ["critical","high"]}}}, "then": {"required": ["reviewed_by"], "properties": {"review_status": {"not": {"const": "draft"}}}}}]
}
```

規則：`severity ∈ {critical, high}` 必須人工 reviewed 才可進報告（schema 以 allOf 強制）。

範例 finding（假想，非真實客戶）：F-003「oplog window 約 X 小時，小於客戶自述的還原所需時間」→ evidence_refs 指向 `db.getReplicationInfo()` 輸出；severity 由規則（window < 還原時間）給 high，人覆核；likelihood `not_assessed`。

## 5. 機器可讀 evidence bundle（INFERENCE）

```
bundle/
  manifest.json        # tool_version, collector_commands[], client_id(pseudonym), captured_at_utc, mongod version, role used, sha256 per file
  raw/<host>/<command>.json    # 原始輸出，遮罩 hostnames/IP/usernames 規則見 manifest.redaction
  derived/metrics.json         # 正規化後指標
  findings.json                # 通過 schema 驗證的 findings
  report.md / report.pdf
  limitations.json             # 未能蒐集的項目與原因（權限不足、客戶不提供）
```

關鍵：蒐集器只做**唯讀**命令；只存 metadata/統計，不存文件內容；`manifest` 記錄所用帳號角色，作為「我們沒有越權」的稽核證據。

## 6. 客戶面 deliverable set（INFERENCE，以「可信的最小集合」為準）

**Minimum credible deliverables（MCD）**——少於此就不足以稱為 assessment：
1. 執行摘要（1–2 頁）：結論、Top findings、**明確的範圍與限制**（只看到什麼）。
2. Finding register（表格 + JSON），每筆有 evidence 引用與覆核狀態。
3. 拓撲與設定快照（版本/EOL 對照官方 lifecycle 頁、replica set 結構、關鍵參數）。
4. 優先化 remediation roadmap（P0–P3、複雜度、風險/回退）。
5. Evidence bundle（遮罩後原始輸出 + manifest，客戶可自行重跑查驗）。
6. 一次 readout（walkthrough）。

**Extended（選配）**：索引/效能深度審查（需 log/profiler 或 FTDC）、備份還原演練（需客戶提供隔離目標）、Kafka–MongoDB 整合審查（connector 設定、offset/oplog 風險、lag 指標）、升級計畫、後續覆測。

**不應承諾**：效能提升百分比、停機時間保證、合規認證結論、法律/財務意見。（組織政策：AI 產出須人工覆核，不可作為正式法律/財務文件。）

## 7. 與組織政策的衝突點（重要）

WebComm 政策禁止輸入客戶個資、機密文件、憑證、連線字串，並限制處理受個資法管轄資料。**INFERENCE：此服務若以 Claude 處理客戶 evidence，必須先確認 bundle 僅含已遮罩的 metadata（無文件內容、無使用者名稱/主機名等識別資訊），並先向 IT/雇主確認；否則 LLM 步驟只能在不含客戶資料的合成/公開資料上開發與測試。** 雇主兼職/NDA 風險見 Phase 0（BASELINE，UNKNOWN）。

## 8. 結論標記

- NEW EVIDENCE：公開「審計樣本報告」難以取得（Percona 無公開樣本）；可用素材是官方 checklist、Atlas Performance Advisor 的輸出形式、mongo-health 的 finding 卡片形式、Debezium/Kafka Connector 的失敗模式文件。
- INFERENCE：以 finding register + evidence bundle 為產品核心，比「報告頁數」更能與廉價競品/純 AI 輸出區隔，因為可稽核；但是否有人願意為此付費 = UNKNOWN（本文件不含需求證據）。
