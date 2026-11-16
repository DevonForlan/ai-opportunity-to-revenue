# 03 Competitor Matrix（索引與合併摘要）

合併資料集：`04_COMPETITOR_DATASET.csv`（73 列：公司 34 + 獨立/boutique 39；皆為 provider_marketing，非購買證據）。細節見 `03_COMPETITOR_MATRIX_companies.md`、`03_COMPETITOR_MATRIX_independent.md`。

- 公司 34 列：VERIFIED 27、PARTIALLY 5、UNVERIFIED 2；有數字公開價格 7/34，MongoDB 專屬僅 Percona（US$11,400 起）。
- 獨立/boutique 39 列（約 30 個不同賣家，約 9 個 solo 頁面實讀）：17 列 VERIFIED、22 列僅 snippet。
- 反覆出現的 MongoDB scope：replica set/oplog、indexes/queries、WiredTiger cache、shard key、security、backup；反覆出現的交付：PDF 報告＋嚴重度排序＋30/60/90 天 roadmap＋live walkthrough；少數明講 read-only、NDA。
- 缺口（樣本內）：未見獨立定價的 upgrade-readiness、Kafka–MongoDB 整合審查（公司層）、獨立顧問的 backup/oplog/replication 產品。台灣：僅 2 家且無健檢產品。
