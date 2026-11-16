# 11 Pricing Evidence

規則：只列觀察到的 list / award 價格；**list price ≠ 成交價**；不推估「我們能賣多少」。資料來源：`04_COMPETITOR_DATASET.csv`（73 列）、`02_DEMAND_DATASET_hiring.csv`（PCC 得標 47 列）、`06_FREELANCE_SAMPLES.csv`。幣別不換算。

## 1. 觀察到的價格（依客群分開）

| 群組 | 觀察 | 範圍／值 | Evidence |
|---|---|---|---|
| Enterprise consulting（MongoDB 專屬） | Percona Database Health Audit | **US$11,400 起**（頁面內 1–5 與 1–6 天描述不一致） | VERIFIED（A，provider 頁） |
| Enterprise（非 MongoDB 服務） | Canonical managed MongoDB | US$3,099/年/VM 等（為託管訂閱，非評估） | VERIFIED，不可比 |
| Enterprise managed／MSP | Datavail、Pythian、Instaclustr 等 | quote-only | UNKNOWN 價格 |
| Boutique／小型公司 productized（Data/Kafka，非 MongoDB） | TBDC Data Pipeline Audit | US$1,990 固定 | VERIFIED |
| | DataBeansAI 2 週 sprint | US$2,000 固定（不含稅） | VERIFIED |
| | Hikmah Data Platform Audit | US$3,000（可折抵後續建置） | VERIFIED |
| | Gigabit data assessment | US$4,000（後續建置 US$44,000；retainer US$2,000/月） | VERIFIED |
| | Dattell Kafka Audit | US$5,000（10 小時專家諮詢/月） | VERIFIED |
| | Champlin sprint | US$10,000 起 | VERIFIED |
| | Data at Depth 串流評估 | US$3,500–5,000 | UNVERIFIED（snippet） |
| Independent／solo（MongoDB） | Contra：MongoDB+Redis Performance Audit | **US$1,800 起**，1 週 | VERIFIED（自述行銷） |
| Independent（Kafka） | ZephyrCode Kafka audit | US$7,500；另有 US$1,200 48 小時 triage，全額折抵 30 天內預訂的 audit | VERIFIED |
| Independent（相鄰） | Contra Analytics Engineering Audit | US$1,200 起 | VERIFIED |
| Independent（時薪） | Contra SQL/DB 優化 | US$50/hr 起 | VERIFIED |
| | Contra Kafka | US$25/hr | VERIFIED |
| | Freelancer.com 個人檔案（MongoDB） | US$15、US$25/hr | VERIFIED（頁面自述） |
| Marketplace 低價 gig | Upwork DB 效能 audit entry | US$90 | PARTIALLY（snippet） |
| | Upwork data pipeline audit | US$399／7 天 | PARTIALLY（snippet，歸屬不確定） |
| | MentorCruise MongoDB mentors | US$70/月（1 次通話）–US$290/月（4 次） | PARTIALLY（snippet） |
| Freelance 貼文預算（MongoDB） | Freelancer/Upwork 貼文 | 時薪 US$2–8、固定 US$70–100 | C（多為 UNVERIFIED／過期） |
| 台灣公部門採購（**購買證據**；DBMS 多為 Oracle/SQL Server，無 MongoDB） | PCC 得標 47 筆 | NT$239,000–NT$44,100,000；**中位數 NT$1,400,000**；≤NT$1M 22 筆、NT$1–5M 16 筆、>NT$5M 9 筆 | A（官方 API；範圍含多年維運與平台案，**非同一產品**） |
| | 「資料庫健檢及優化」專案（中華郵政） | NT$1,480,000（2024）、NT$1,400,000（2025） | A |
| | 「資料庫效能調校」（主計總處） | NT$3,170,000 | A |
| | 小型資料庫升級案 | 約 NT$270,000–590,000 | A |
| 英國公部門 | Database Review award | GBP 14,425（技術未知） | PARTIALLY（snippet） |

## 2. Price clusters（INFERENCE，描述性）
- **固定價 read-only audit，獨立/小型業者：US$1,200–$5,000** 為主要群聚（TBDC、DataBeansAI、Hikmah、Contra audit、Dattell、Data at Depth），單一 solo Kafka 賣家 US$7,500。
- **品牌大廠：US$11,400 起**（單一 MongoDB 專屬資料點）。
- **Marketplace 入門價：US$90–$399**（snippet，擁擠、範圍不明）。
- **台灣公部門案：NT$0.24M 至數千萬**，但為大型/多年/多系統，與個人 read-only 評估不可直接比較。

## 3. Price anchors / hypotheses（皆為假說，待 pilot 驗證）
- H-P1：個人 MongoDB read-only risk assessment 的合理對標帶為 US$1,200–$5,000（來自同類獨立/小型業者的 list price；**不等於我們能成交**）。
- H-P2：「paid triage 全額折抵 audit」（ZephyrCode 模式）是唯一在獨立賣家中出現的低風險入口結構。
- H-P3：不要以 Percona US$11,400 比例推估個人價格（Issue #4 明文禁止）。

## 4. UNKNOWN
個人實際成交價；轉換率；折扣；客戶預算分佈；台灣民間（非政府）顧問行情；MongoDB 專屬案件的實際付款資料。

## 5. 限制
多個價格來自 provider 自述頁；snippet 價格未驗證；PCC 金額為官方資料但案名不一定含 MongoDB，供應商與詳細 scope 未讀（tender 文件未讀）。
