# 03 競爭者矩陣：獨立 / 單人 / 精品型（independent / solo / boutique）

## Method & limitations（方法與限制）
- 日期：2026-11-16。唯讀研究；未聯絡任何人、未註冊帳號、未繞過登入或反爬機制。
- 來源：WebSearch 結果與 WebFetch 可讀頁面。Fiverr / Upwork / MentorCruise 對 fetch 回傳 403，這些列僅有搜尋結果的標題、URL 與摘要，標為 PARTIALLY VERIFIED；價格、評論數、套餐內容一律 UNKNOWN（除非搜尋摘要明確給出並已註明）。
- 價格是「供應商公開標價」，不是成交價；行銷頁面不等於需求；testimonial 不具代表性（brief 規則）。
- 隱私：組織政策限制處理受個資法規範的資料。因此 provider 欄對個人使用平台 handle / 品牌名，不記錄個人履歷、學歷、住所；Toptal 個人履歷頁被工具拒絕處理，已略過（未收錄）。
- 台灣 / 亞洲獨立者：中文搜尋（MongoDB 顧問 / 資料庫顧問 個人 / 接案 / Kafka 顧問）沒有找到任何台灣個人 MongoDB 顧問的公開服務頁（只有技術文章、課程、公司頁）。這是「在本次搜尋範圍內未找到」，不代表不存在（UNKNOWN）。
- 未找到：獨立的 MongoDB 專屬「固定價 Health Check」個人站（只有 Contra 一筆 MongoDB+Redis audit）。未能確認任何 MongoDB Champion 在做獨立顧問（Champions 目錄頁不含名單，未驗證）。
- 「company_or_independent」：independent = 頁面或平台顯示為個人賣家；boutique = 小團隊/較小事務所（含 2 筆 benchmark：Mydbops、Delbridge，可能與 firm 資料集重複）。市集賣家是否真的 solo 為 UNVERIFIED（僅從個人 handle 推論）。

## 計數
- 總列數 39（independent 32、boutique 7）；去除 ZephyrCode 重複與 MentorCruise 聚合列後，獨立賣家 distinct = 30。
- 證據：VERIFIED（頁面已讀）17 列；PARTIALLY VERIFIED（僅搜尋摘要）22 列。
- 頁面已讀的獨立列 10 列（9 個 distinct 賣家，其中 1 筆是無價格的作品集貼文）；其餘獨立列是市集 gig 的搜尋摘要。因此「真正 solo 且頁面已核實」只有約 9 個；達到 20+ 靠市集賣家的 handle 推論（UNVERIFIED）。
- evidence_type：全部為 provider_marketing（供給面行銷）；無 purchase 證據。
- 來源平台：Contra 5 頁、Freelancer.com 2 profile、個人/小型網站 3（ZephyrCode、Pine Street Analytics、GenAI Data Solutions）、boutique 公司頁 6、Upwork 9、Fiverr 12、MentorCruise 1。

## 矩陣（完整欄位見 04_COMPETITOR_DATASET_independent.csv）

| id | provider | 類型 | 服務 | 定價模式 | 公開價格(頁面原文) | 付費診斷先行? | 證據 |
|---|---|---|---|---|---|---|---|
| I001 | Contra seller 'prasham_trivedi_bp0zi5qs' | independent | MongoDB and Redis Performance Audit | fixed-price (starting at) | Starting at $1,800 (USD) | - | VERIFIED |
| I002 | ZephyrCode (solo practitioner) | independent | Kafka & event-streaming audit (ZC-KAFKA) | fixed-price | $7,500 | Y | VERIFIED |
| I003 | ZephyrCode (solo practitioner) | independent | 48-hour triage (paid, credited to audit) | fixed-price | $1,200 fixed; credited in full to an audit booked within 30 days | Y | VERIFIED |
| I004 | Pine Street Analytics (solo) | independent | Reliability Audit (data pipelines/platform) | fixed-price audit; retainer (Fractional  | Not published | - | VERIFIED |
| I005 | Contra seller (SQL and Database Optimization; Ri | independent | SQL and Database Optimization (MongoDB tagged) | hourly or project-based | Starting at $50/hr (USD) | - | VERIFIED |
| I006 | Contra seller (Analytics Engineering Audit; Pari | independent | Analytics Engineering Audit (BigQuery/dbt; adjacent to pipel | fixed-price (starting at) | Starting at $1,200 (USD) | - | VERIFIED |
| I007 | Contra seller 'freelancer_mjdptbp6' (Kafka) | independent | Design and Deploy Apache Kafka Seamlessly | hourly | $25/hr (USD) | - | VERIFIED |
| I008 | Contra seller (Fractional data engineer post) | independent | Fractional data engineer (MongoDB -> BigQuery work example) | UNKNOWN (portfolio post, no price) | Not published | - | VERIFIED |
| I009 | Database SPA (senior-team practice) | boutique | Health Check / Slow Query Review (MySQL, MariaDB, MongoDB, P | UNKNOWN | Not published | - | VERIFIED |
| I010 | GenAI Data Solutions (two-person EU team) | boutique | Paid Discovery / AI Opportunity Audit / LLM Cost & Quality A | fixed-fee (no hourly) + monthly retainer | Not published | Y | VERIFIED |
| I011 | Dattell | boutique | Apache Kafka Audit | fixed-price | $5,000 USD (10 hours expert consultation over one month) | - | VERIFIED |
| I012 | JusDB | boutique | MongoDB Consulting - free single-instance audit then fixed-s | free audit -> fixed-scope sprint or advi | No prices listed | free audit | VERIFIED |
| I013 | Champlin Enterprises LLC (small agency) | boutique | Sprint (architectural audit + production rollout blueprint); | fixed-fee sprint | Sprints start at $10,000 | - | VERIFIED |
| I014 | Mydbops LLP (established DBA firm; included as b | boutique | MongoDB Performance & Security Audit | fixed-scope, quoted after discovery call | Not published | - | VERIFIED |
| I015 | Delbridge Solutions (MongoDB partner; included a | boutique | MongoDB Implementation Consulting (architecture reviews and  | fixed price / T&M / subscription | Not published | - | VERIFIED |
| I016 | Freelancer.com profile '/u/MaTGaPa' (individual) | independent | MongoDB freelancer (generalist developer) | hourly | $25/hr (listing page) | - | VERIFIED |
| I017 | Freelancer.com profile '/u/ajaynpaladiya' (indiv | independent | MongoDB freelancer (generalist developer) | hourly | $15/hr (listing page) | - | VERIFIED |
| I018 | MentorCruise MongoDB mentors (marketplace aggreg | independent | Subscription mentorship / consulting sessions | monthly subscription per mentor | Search snippet: plans $70/mo (1 call) to $290/mo (4 calls); one mentor | - | PARTIAL |
| I019 | Upwork seller (Atlas cost & cluster sizing) | independent | MongoDB Atlas Cost Optimization & Cluster Sizing Consultatio | fixed-scope project catalog | UNKNOWN (not shown in snippet) | - | PARTIAL |
| I020 | Upwork seller (DB performance audit Node.js) | independent | Database performance audit for a Node.js web app (MySQL/Post | fixed-scope project catalog | $90 (search snippet; entry package) | - | PARTIAL |
| I021 | Upwork seller (Advanced MongoDB solutions) | independent | Advanced MongoDB Solutions for Efficient Data Handling | fixed-scope project catalog | UNKNOWN | - | PARTIAL |
| I022 | Upwork seller (MongoDB query optimisation mongoo | independent | Optimised MongoDB queries or aggregations (mongoose.js/prism | fixed-scope project catalog | UNKNOWN (search summary mentioned tiers between ~$150 and $1,500 acros | - | PARTIAL |
| I023 | Upwork seller (optimization report for MongoDB) | independent | An optimization report for MongoDB | fixed-scope project catalog | UNKNOWN | - | PARTIAL |
| I024 | Upwork seller (AWS data pipeline health check) | independent | AWS Data Pipeline Health Check with ETL Performance Review | fixed-scope project catalog | UNKNOWN | - | PARTIAL |
| I025 | Upwork seller (Data Pipeline Audit) | independent | Data Pipeline Audit to Identify Cost, Performance, and Data  | fixed-scope project catalog | Search summary cites a $399, 7-day-delivery audit listing; attribution | - | PARTIAL |
| I026 | Upwork seller (Postgres->Kafka->MongoDB CDC) | independent | Real-time CDC pipeline PostgreSQL -> Kafka -> MongoDB (Quark | fixed-scope project catalog | UNKNOWN | - | PARTIAL |
| I027 | Upwork seller (MongoDB developer: design, querie | independent | MongoDB Developer for Database Design, Queries & Performance | fixed-scope project catalog | UNKNOWN | - | PARTIAL |
| I028 | Fiverr seller 'bonakelelesiban' | independent | Query optimization (mongoose/prisma) | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I029 | Fiverr seller 'tjsuryacn' | independent | MySQL/MongoDB design, optimize, fix | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I030 | Fiverr seller 'abdou_mongodb' | independent | MongoDB query optimization (French market) | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I031 | Fiverr seller 'ahmed_khamis_22' | independent | Strict 2-hour diagnostic review of Node.js/MongoDB backend ( | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I032 | Fiverr seller 'victoriarence' | independent | Aggregation pipeline optimization and schema design | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I033 | Fiverr seller 'azeem_haider_' | independent | Slow-query fixing across engines | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I034 | Fiverr seller 'ashiqur90' | independent | Query/aggregation writing and fixing | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I035 | Fiverr seller 'bhdfreelance' | independent | Data infrastructure audit (analytics/dashboards) | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I036 | Fiverr seller 'ekele_james' | independent | Kafka cluster setup/optimization | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I037 | Fiverr seller 'amankhare94' | independent | Production-grade Kafka setup | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I038 | Fiverr seller 'aoksoft' | independent | Kafka event-driven build/fix/optimize | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |
| I039 | Fiverr seller 'teehemdigital' | independent | Kafka/Confluent setup, manage, troubleshoot | fixed-price gig tiers (typical of platfo | UNKNOWN (not retrievable; search summary noted only scattered prices e | - | PARTIAL |

## 重點觀察（皆來自上列列數；樣本小，不可外推）
- 公開標價的「審計型」固定價（頁面已讀）：Contra MongoDB+Redis audit 起價 $1,800（1 週）；Contra analytics audit 起價 $1,200（1 週）；ZephyrCode Kafka audit $7,500（2 週）與 $1,200 triage；Dattell Kafka audit $5,000（10 小時/1 個月）；Champlin Sprint 起價 $10,000（2-4 週，非 MongoDB 專屬）。價格跨度約 6 倍，且範圍/交付物差異大，不可視為單一市場價。
- 市集上的 MongoDB 單人 gig 多為「query/aggregation 優化」，不是 replica set / backup / upgrade readiness / oplog 風險審查（INFERENCE，來自標題與搜尋摘要）。
- 沒有任何獨立賣家（頁面已讀）公開 Backup/Restore readiness、Replication/Oplog 風險、Upgrade readiness 的 productized 方案（UNKNOWN 於其他未讀頁面）。
