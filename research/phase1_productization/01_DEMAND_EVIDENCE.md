# 01 Demand Evidence（索引與合併摘要）

合併資料集：`02_DEMAND_DATASET.csv`（371 列 = hiring/purchase 90 + pain 281）。細節見：
- `01_DEMAND_EVIDENCE_hiring.md`（雇用/購買證據：90 列；52 purchase、38 hiring）
- `01_DEMAND_EVIDENCE_pain.md`（痛點訊號：281 列，皆 level C）

| evidence_type | 列數 | 說明 |
|---|---:|---|
| purchase | 52 | 台灣 PCC 得標 47（A 級，官方 API）＋ UK/聚合 5（snippet）；**無一筆被證實為 MongoDB 專屬** |
| hiring | 38 | LinkedIn 16、Freelancer 9、Dice 8、HN 3、Upwork 2（snippet） |
| pain | 281 | MongoDB 論壇 143、Percona 論壇 44、GitHub 40、StackExchange 37、HN 17、Reddit 0 |

Pain 類別（分析者標註，INFERENCE）：backup_restore 45、ha_oplog 40、kafka_cdc 39、upgrade_eol 37、performance 35、migration 21、security 19、sharding 17、memory_disk 12、cost_atlas 11（同一 HN thread）、pipeline_reliability 5。

重點：Pain 很多，但 **0 則 pain 文表明預算或要付費找人**；購買證據來自台灣公部門的非 MongoDB 資料庫服務。不可把論壇求助視為付費需求。
