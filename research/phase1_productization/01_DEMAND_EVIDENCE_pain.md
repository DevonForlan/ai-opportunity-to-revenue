# 01 DEMAND EVIDENCE — Pain（公開痛點貼文）

> evidence_type = **pain**。每一列只證明「有人公開遇到 MongoDB / Data Platform 問題」，**不是付費意願證明**（forum complaint != willingness to pay）。

## 0. 方法與限制（method & limitations）

- 擷取日期 2026-11-16；唯讀。工具：HN Algolia API、MongoDB Community Forums（Discourse JSON）、Percona Community Forum（Discourse JSON）、StackExchange API（stackoverflow / dba）、GitHub Search API（未驗證身分，約 10 req/min）、WebSearch（僅作補充定位）。
- 篩選：以關鍵字搜尋後，**人工逐筆挑選**與 Health Check / Upgrade / Replication / Backup / Kafka / Pipeline 類服務相關者；排除版本公告、活動、純教學、與營運無關的 driver/連線新手問題。自動分類只作輔助，最後 category 由人工指定。
- 時間：以 2025-01 起為主（見下方年度分佈）；StackExchange 與 GitHub 皆限 2025 起。
- **Reddit：無法使用**。`www.reddit.com` / `old.reddit.com` 的 .json 回傳 HTML（被擋），WebSearch 對 reddit.com 網域回 400（不可存取）。依規則不繞過；r/mongodb、r/dataengineering、r/devops、r/sysadmin、r/ExperiencedDevs **0 筆**（UNKNOWN，未驗證）。
- **明確付費求助（explicit paid-help request）：0 筆**。HN Algolia（含 consultant / hire / DBA / paying 類查詢）、WebSearch 皆未找到 2025–2026 的「願意付費請顧問處理 MongoDB/Kafka」公開貼文；找到的皆為廠商行銷頁或人力市集頁（屬 provider_marketing / hiring，非本檔範圍）。這本身是**重要負面發現**：公開論壇上的痛點很多，但幾乎沒有直接標價/求聘的貼文。
- 各欄限制：`stated_budget_rate / pricing_model / remote_onsite / geography / customer_type` 幾乎全為 UNKNOWN（匿名公開貼文不揭露）。`requested_outcome` 為依貼文內容的**推論（INFERENCE）**。views/replies/likes 來自 API，僅供熱度參考，非需求量。
- MongoDB Community Forums 在密集查詢時回 429；改以放慢速度重試補齊，仍可能漏掉部分主題（recall 不完整）。
- GitHub 的 debezium/dbz repo 於 2025-12-11 批次匯入舊 [DBZ-xxxx] 議題，created_at 非原始日期，已排除該批。
- evidence_level 一律 **C**（社群/軼事）。HN comment 為個人敘述，GitHub 為開發者回報；皆未驗證其嚴重性或商業影響。

## 1. 筆數統計

**總列數：281**（dataset：`02_DEMAND_DATASET_pain.csv`，id P001…P281；已依 URL 去重）

### 1.1 依來源

| source | rows |
|---|---|
| MongoDB Community Forums | 143 |
| Percona Community Forum | 44 |
| GitHub Issues | 40 |
| StackExchange (stackoverflow.com) | 25 |
| Hacker News | 17 |
| StackExchange (dba.stackexchange.com) | 12 |

### 1.2 依 evidence_type

| evidence_type | rows |
|---|---|
| pain | 281 |
| hiring / purchase / provider_marketing | 0（本檔不含） |

### 1.3 依貼文年度

| year | rows |
|---|---|
| 2025 | 232 |
| 2026 | 49 |

## 2. 類別頻率表（由 CSV 實際列數計算）

| category | 說明 | rows | % | 對應可產品化服務（INFERENCE） |
|---|---|---|---|---|
| backup_restore | Backup / restore / recovery | 45 | 16.0% | Backup/Restore readiness |
| ha_oplog | HA / replica set / oplog / failover | 40 | 14.2% | Replication/Oplog risk |
| kafka_cdc | Kafka / Debezium / change stream / CDC connector | 39 | 13.9% | Kafka-MongoDB integration review |
| upgrade_eol | Upgrade / EOL / version compatibility | 37 | 13.2% | Upgrade readiness |
| performance | Performance / slow query / index | 35 | 12.5% | Performance/Index review |
| migration | Migration (RDBMS / DocumentDB / Cosmos / cross-cloud / mongosync) | 21 | 7.5% | Migration assessment |
| security | Security / auth / TLS / audit / CVE | 19 | 6.8% | Security/compliance review |
| sharding | Sharding / shard key / balancer | 17 | 6.0% | Production risk assessment |
| memory_disk | Memory (WiredTiger) / disk growth / capacity | 12 | 4.3% | Health check |
| cost_atlas | Atlas cost / sizing | 11 | 3.9% | Atlas cost review |
| pipeline_reliability | Data pipeline reliability (loss / duplicates / bulk writes) | 5 | 1.8% | Data pipeline reliability review |

### 2.1 類別 x 來源

| category | MongoDB Community Forums | Percona Community Forum | GitHub Issues | StackExchange (stackoverflow.com) | Hacker News | StackExchange (dba.stackexchange.com) |
|---|---|---|---|---|---|---|
| backup_restore | 15 | 18 | 10 | 1 | 1 | 0 |
| ha_oplog | 25 | 5 | 2 | 3 | 2 | 3 |
| kafka_cdc | 15 | 0 | 16 | 6 | 2 | 0 |
| upgrade_eol | 23 | 5 | 2 | 4 | 1 | 2 |
| performance | 31 | 1 | 2 | 1 | 0 | 0 |
| migration | 8 | 3 | 0 | 4 | 3 | 3 |
| security | 6 | 8 | 1 | 2 | 0 | 2 |
| sharding | 12 | 0 | 0 | 3 | 0 | 2 |
| memory_disk | 5 | 4 | 1 | 1 | 1 | 0 |
| cost_atlas | 2 | 0 | 2 | 0 | 7 | 0 |
| pipeline_reliability | 1 | 0 | 4 | 0 | 0 | 0 |

### 2.2 觸發情境（trigger，規則式推斷自標題關鍵字）

| trigger | rows |
|---|---|
| incident-driven | 83 |
| upgrade/migration | 47 |
| Kafka | 35 |
| performance | 34 |
| HA/oplog | 29 |
| proactive/unclear | 27 |
| security | 15 |
| proactive (cost) | 11 |

> trigger 為標題關鍵字規則推斷（urgent/crash/fail/lost 等 → incident-driven），粗略，僅供參考。

## 3. 高熱度樣本（views 為 API 數值，僅論壇類有）

| id | source | views | category | title | url |
|---|---|---|---|---|---|
| P067 | MongoDB Community Forums | 2956 | upgrade_eol | MongoDB Upgrade to version 8.0 | https://www.mongodb.com/community/forums/t/mongodb-upgrade-to-version-8-0/318478 |
| P057 | MongoDB Community Forums | 2764 | upgrade_eol | Mongodb version upgrade 3.4 to latest | https://www.mongodb.com/community/forums/t/mongodb-version-upgrade-3-4-to-latest/321443 |
| P226 | Percona Community Forum | 2426 | security | CVE-2025-14847 Patch for Percona MongoDB release | https://forums.percona.com/t/cve-2025-14847-patch-for-percona-mongodb-release/39945 |
| P006 | MongoDB Community Forums | 2266 | ha_oplog | Unending log messages about unable to select sync source | https://www.mongodb.com/community/forums/t/unending-log-messages-about-unable-to-select-sync-source/310483 |
| P066 | MongoDB Community Forums | 1611 | upgrade_eol | How migrate v6 to v7? | https://www.mongodb.com/community/forums/t/how-migrate-v6-to-v7/311910 |
| P234 | Percona Community Forum | 1608 | memory_disk | Percona Operator for MongoDB endlessly spawning connections until OOMKilled | https://forums.percona.com/t/percona-operator-for-mongodb-endlessly-spawning-connections-until-oomkilled/39634 |
| P221 | Percona Community Forum | 1516 | upgrade_eol | Pods restart after upgrade to Operator 1.21.0 | https://forums.percona.com/t/pods-restart-after-upgrade-to-operator-1-21-0/39627 |
| P216 | Percona Community Forum | 1237 | ha_oplog | MongoDB Sharded Cluster Stuck Initializing Due to Denylisted Sync Source | https://forums.percona.com/t/mongodb-sharded-cluster-stuck-initializing-due-to-denylisted-sync-source/38185 |
| P229 | Percona Community Forum | 1184 | security | Using CertManager and TLS with MongoDB Helm charts results in error? | https://forums.percona.com/t/using-certmanager-and-tls-with-mongodb-helm-charts-results-in-error/36326 |
| P090 | MongoDB Community Forums | 1147 | backup_restore | Mongo repair not working, data corrupted when server shutdown accidently | https://www.mongodb.com/community/forums/t/mongo-repair-not-working-data-corrupted-when-server-shutdown-accidently/314644 |
| P140 | MongoDB Community Forums | 1141 | migration | AWS DocumentDB TLS in .net environment | https://www.mongodb.com/community/forums/t/aws-documentdb-tls-in-net-environment/311087 |
| P068 | MongoDB Community Forums | 1100 | upgrade_eol | MongoDB Atlas Upgrade – Choosing Between 7.0 and 8.0 | https://www.mongodb.com/community/forums/t/mongodb-atlas-upgrade-choosing-between-7-0-and-8-0/315214 |
| P238 | Percona Community Forum | 1090 | migration | How to migrate from existing MongoDB data to Percona MongoDB | https://forums.percona.com/t/how-to-migrate-from-existing-mongodb-data-to-percona-mongodb/38677 |
| P222 | Percona Community Forum | 1089 | upgrade_eol | Error on secret not found upgrading to operator 1.19.0 | https://forums.percona.com/t/error-on-secret-not-found-upgrading-to-operator-1-19-0/36297 |
| P198 | Percona Community Forum | 1079 | backup_restore | Mongod-failure-after-restore | https://forums.percona.com/t/mongod-failure-after-restore/39588 |
| P072 | MongoDB Community Forums | 1004 | upgrade_eol | Mongo 6.0.20 to 8.0.4 update: Memory usage issues! | https://www.mongodb.com/community/forums/t/mongo-6-0-20-to-8-0-4-update-memory-usage-issues/310946 |
| P230 | Percona Community Forum | 992 | security | Installation of PSMDB resource failed with TLS error | https://forums.percona.com/t/installation-of-psmdb-resource-failed-with-tls-error/37281 |
| P040 | MongoDB Community Forums | 987 | performance | MongoDB query becomes unexpectedly slow and broken | https://www.mongodb.com/community/forums/t/mongodb-query-becomes-unexpectedly-slow-and-broken/310040 |
| P098 | MongoDB Community Forums | 977 | sharding | Sharding an existing collection: chunk not splitting after balancing is done | https://www.mongodb.com/community/forums/t/sharding-an-existing-collection-chunk-not-splitting-after-balancing-is-done/309385 |
| P069 | MongoDB Community Forums | 974 | upgrade_eol | Update mongo version from 4 to 8 | https://www.mongodb.com/community/forums/t/update-mongo-version-from-4-to-8/327309 |

## 4. 各類別代表樣本（每類最多 4 筆）

### backup_restore — Backup / restore / recovery

- P079 [MongoDB Community Forums] How can I disable PITR on my Atlas M30 cluster? — https://www.mongodb.com/community/forums/t/how-can-i-disable-pitr-on-my-atlas-m30-cluster/328565
- P080 [MongoDB Community Forums] Can I use periodic oplog backups to reduce MTTR in MongoDB for faster recovery from accidental deletes/updates — https://www.mongodb.com/community/forums/t/can-i-use-periodic-oplog-backups-to-reduce-mttr-in-mongodb-for-faster-recovery-from-accidental-deletes-updates/324743
- P081 [MongoDB Community Forums] Unable to start locally from Atlas backup files — https://www.mongodb.com/community/forums/t/unable-to-start-locally-from-atlas-backup-files/318733
- P082 [MongoDB Community Forums] I accidentally deleted my M0 cluster named Cluster0 today. It's still within the 7-day window. Is there any wa — https://www.mongodb.com/community/forums/t/i-accidentally-deleted-my-m0-cluster-named-cluster0-today-its-still-within-the-7-day-window-is-there-any-way-to-restore-the-cluster-or-recover-the-data/325845

### ha_oplog — HA / replica set / oplog / failover

- P001 [MongoDB Community Forums] Increasing Oplog size - one-shot or step-by-step? — https://www.mongodb.com/community/forums/t/increasing-oplog-size-one-shot-or-step-by-step/328499
- P002 [MongoDB Community Forums] Issues Converting Standalone MongoDB to Replica Set Without Downtime (EC2 Setup) — https://www.mongodb.com/community/forums/t/issues-converting-standalone-mongodb-to-replica-set-without-downtime-ec2-setup/321298
- P003 [MongoDB Community Forums] Disk Bloat on one node of a 5 node Replica set — https://www.mongodb.com/community/forums/t/disk-bloat-on-one-node-of-a-5-node-replica-set/327987
- P004 [MongoDB Community Forums] Snapshot cloned replica - lag increase issue — https://www.mongodb.com/community/forums/t/snapshot-cloned-replica-lag-increase-issue/324997

### kafka_cdc — Kafka / Debezium / change stream / CDC connector

- P117 [MongoDB Community Forums] Setting custom value of maxAwaitTimeMS for change streams in sharded replica set does not seem to take effect — https://www.mongodb.com/community/forums/t/setting-custom-value-of-maxawaittimems-for-change-streams-in-sharded-replica-set-does-not-seem-to-take-effect/319651
- P118 [MongoDB Community Forums] Performance issues with change streams and multiple collections on single cluster — https://www.mongodb.com/community/forums/t/performance-issues-with-change-streams-and-multiple-collections-on-single-cluster/312413
- P119 [MongoDB Community Forums] Change streams: Scanned Objects / Returned has gone above 1000 — https://www.mongodb.com/community/forums/t/change-streams-scanned-objects-returned-has-gone-above-1000/322230
- P120 [MongoDB Community Forums] updateLookup in Change Streams Causing Full Collection Scan — https://www.mongodb.com/community/forums/t/updatelookup-in-change-streams-causing-full-collection-scan/318816

### upgrade_eol — Upgrade / EOL / version compatibility

- P057 [MongoDB Community Forums] Mongodb version upgrade 3.4 to latest — https://www.mongodb.com/community/forums/t/mongodb-version-upgrade-3-4-to-latest/321443
- P058 [MongoDB Community Forums] Upgrade Mongo from V4.4 to V8.0 — https://www.mongodb.com/community/forums/t/upgrade-mongo-from-v4-4-to-v8-0/317655
- P059 [MongoDB Community Forums] Issue Restoring Data After Upgrading MongoDB — https://www.mongodb.com/community/forums/t/issue-restoring-data-after-upgrading-mongodb/314955
- P060 [MongoDB Community Forums] Issue Restoring Data After Upgrading MongoDB from 4.4.29 to 8.0.3 — https://www.mongodb.com/community/forums/t/issue-restoring-data-after-upgrading-mongodb-from-4-4-29-to-8-0-3/314777

### performance — Performance / slow query / index

- P026 [MongoDB Community Forums] Building a 4-field compound index on a 1.2B documents collection (MongoDB 7.0.20): expected impact on cluster? — https://www.mongodb.com/community/forums/t/building-a-4-field-compound-index-on-a-1-2b-documents-collection-mongodb-7-0-20-expected-impact-on-cluster/327950
- P027 [MongoDB Community Forums] How to reduce the maximum insert time to less than 1s — https://www.mongodb.com/community/forums/t/how-to-reduce-the-maximum-insert-time-to-less-than-1s/324597
- P028 [MongoDB Community Forums] Slow Queries due to wait for write concern — https://www.mongodb.com/community/forums/t/slow-queries-due-to-wait-for-write-concern/328512
- P029 [MongoDB Community Forums] Facing Slow Performance for Filtered Count Queries — https://www.mongodb.com/community/forums/t/facing-slow-performance-for-filtered-count-queries/327540

### migration — Migration (RDBMS / DocumentDB / Cosmos / cross-cloud / mongosync)

- P132 [MongoDB Community Forums] Help Needed: Zero Downtime Migration of 3TB Self-Hosted MongoDB Between Cloud Providers — https://www.mongodb.com/community/forums/t/help-needed-zero-downtime-migration-of-3tb-self-hosted-mongodb-between-cloud-providers/323887
- P133 [MongoDB Community Forums] Mongosync - community version/open source version — https://www.mongodb.com/community/forums/t/mongosync-community-version-open-source-version/314607
- P134 [MongoDB Community Forums] Investigating Daily MongoSync CPU and Disk I/O Spikes — https://www.mongodb.com/community/forums/t/investigating-daily-mongosync-cpu-and-disk-i-o-spikes/321190
- P135 [MongoDB Community Forums] Need guidance on migrating MongoDB Atlas from GCP to AWS while maintaining current IOPS and minimizing cost — https://www.mongodb.com/community/forums/t/need-guidance-on-migrating-mongodb-atlas-from-gcp-to-aws-while-maintaining-current-iops-and-minimizing-cost/340487

### security — Security / auth / TLS / audit / CVE

- P111 [MongoDB Community Forums] Atlas cli downloads an empty audit log but from ui i can download log with data inside it — https://www.mongodb.com/community/forums/t/atlas-cli-downloads-an-empty-audit-log-but-from-ui-i-can-download-log-with-data-inside-it/328370
- P112 [MongoDB Community Forums] Not encrypting data with Mongoose + CSFLE — https://www.mongodb.com/community/forums/t/not-encrypting-data-with-mongoose-csfle/322560
- P113 [MongoDB Community Forums] Member certificate not working with clusterAuthX509 parameter — https://www.mongodb.com/community/forums/t/member-certificate-not-working-with-clusterauthx509-parameter/322746
- P114 [MongoDB Community Forums] Atlas UI Data Explorer or Browse Collections do not follow Network restrictions — https://www.mongodb.com/community/forums/t/atlas-ui-data-explorer-or-browse-collections-do-not-follow-network-restrictions/323726

### sharding — Sharding / shard key / balancer

- P094 [MongoDB Community Forums] Unable to Reclaim Disk Space after Dropping Databases on Sharded Cluster (WiredTiger, v4.0.0) — https://www.mongodb.com/community/forums/t/unable-to-reclaim-disk-space-after-dropping-databases-on-sharded-cluster-wiredtiger-v4-0-0/323243
- P095 [MongoDB Community Forums] Sharding Empty Collection takes a long time — https://www.mongodb.com/community/forums/t/sharding-empty-collection-takes-a-long-time/314663
- P096 [MongoDB Community Forums] One shard still has all the data after equal balancing — https://www.mongodb.com/community/forums/t/one-shard-still-has-all-the-data-after-equal-balancing/321017
- P097 [MongoDB Community Forums] Single chunk per shard — https://www.mongodb.com/community/forums/t/single-chunk-per-shard/327174

### memory_disk — Memory (WiredTiger) / disk growth / capacity

- P106 [MongoDB Community Forums] Compact doesn't free all the space — https://www.mongodb.com/community/forums/t/compact-doesnt-free-all-the-space/325366
- P107 [MongoDB Community Forums] How to switch to secondary to run compact — https://www.mongodb.com/community/forums/t/how-to-switch-to-secondary-to-run-compact/324591
- P108 [MongoDB Community Forums] Compaction Issue in MongoDB Atlas Replica Set — https://www.mongodb.com/community/forums/t/compaction-issue-in-mongodb-atlas-replica-set/312056
- P109 [MongoDB Community Forums] Cache-resident configuration — https://www.mongodb.com/community/forums/t/cache-resident-configuration/324231

### cost_atlas — Atlas cost / sizing

- P141 [MongoDB Community Forums] Data transfer cost in google cloud — https://www.mongodb.com/community/forums/t/data-transfer-cost-in-google-cloud/310253
- P142 [MongoDB Community Forums] MongoDB Atlas storage pricing for chunks and shard — https://www.mongodb.com/community/forums/t/mongodb-atlas-storage-pricing-for-chunks-and-shard/309514
- P181 [Hacker News] We cut our Mongo DB costs by 90% by moving to Hetzner (HN story) — https://news.ycombinator.com/item?id=45915884
- P182 [Hacker News] HN comment: MongoDB Atlas was around 500% more expensive than in-house every time I evaluated it (at almost ev — https://news.ycombinator.com/item?id=45919356

### pipeline_reliability — Data pipeline reliability (loss / duplicates / bulk writes)

- P143 [MongoDB Community Forums] Throttling huge bulk upserts to reduce load on cluster — https://www.mongodb.com/community/forums/t/throttling-huge-bulk-upserts-to-reduce-load-on-cluster/312138
- P262 [GitHub Issues] source-MongoDB-v2 source discovery incorrectly includes views, causing aggregation memory and unsupported _id  — https://github.com/airbytehq/airbyte/issues/77674
- P264 [GitHub Issues] Java heapspace on source connector — https://github.com/airbytehq/airbyte/issues/51616
- P268 [GitHub Issues] Mongodb connector fails to refresh schema — https://github.com/airbytehq/airbyte/issues/53612

## 5. 關鍵觀察（標記：NEW EVIDENCE = 本批資料直接支持；INFERENCE = 推論）

1. **NEW EVIDENCE**：在 281 筆公開貼文中，前四大類別為 backup_restore（45）、ha_oplog（40）、kafka_cdc（39）、upgrade_eol（37）。
2. **NEW EVIDENCE**：升級/EOL 相關貼文包含 3.2/3.4/3.6/4.4 → 7.x/8.x 的跨多版升級、升級後效能退化（7.0→8.0 FETCH、v7 collation 變慢、8.0.15–8.0.20 CPU regression）、升級後無法 restore，顯示「Upgrade Readiness」有真實技術痛點（需看 upgrade_eol 列）。
3. **NEW EVIDENCE**：Percona Forum 與 GitHub（Percona Operator）有大量 backup/restore/PBM 卡住、restore 失敗、PITR 卡住的貼文，且 views 數百至逾一千；Backup/Restore readiness 的痛點可見度高於預期。
4. **NEW EVIDENCE**：Kafka/CDC 類（MongoDB Source/Sink connector、Debezium、Airbyte source-mongodb、change stream resume token）出現多筆「資料遺失 / 重複 / resume token 失效 / OOM」貼文；其中 GitHub 為開發者回報，企業買家需求 UNKNOWN。
5. **NEW EVIDENCE**：Atlas 成本議題主要來自 HN 2025-11 單一討論串（261 points；多則留言），屬同一事件的多則留言，**不應當作多個獨立客戶**。
6. **NEW EVIDENCE（負面）**：未找到任何明確「付費請顧問」貼文；沒有任何貼文揭露預算。痛點存在 != 有人願意付費。
7. **INFERENCE**：多數貼文者是個人/小團隊開發者或自架維運者（customer_type UNKNOWN），在論壇求免費協助；可能的付費買家（有 SLA 的企業）不會公開發文。需由 hiring / purchase 證據（其他檔案）交叉驗證。

## 6. 與 Phase 0 baseline 的關係
- BASELINE（research/17）：標準化 DB 審計有公開付費證據。**本檔不修正該結論**，僅補充「痛點在公開論壇確實常見、類別分佈如上」；付費意願仍 UNKNOWN。

## 7. 資料表
- `02_DEMAND_DATASET_pain.csv`（DEMAND schema，281 列）
- `_sources/demand_pain.csv`（來源清單）

