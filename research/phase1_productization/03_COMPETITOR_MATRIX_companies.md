# 03 競品矩陣：公司型供給方（MongoDB / Database / Data Platform 顧問、MSP、Kafka review）

捕獲日期：2026-11-16。資料集：`04_COMPETITOR_DATASET_companies.csv`（C001–C034）。來源：`_sources/competitors_companies.csv`。

## 方法與限制（Method & limitations）

- 方法：WebSearch 找候選，再用 WebFetch 讀供應商自家頁面或 PDF。供應商自家頁面讀到的欄位標 VERIFIED（evidence level A，但只代表「供應商這樣宣稱」，不代表需求或成交）。新聞稿為 PARTIALLY VERIFIED（B）。只靠搜尋摘要為 UNVERIFIED（C）。
- evidence_type 全部為 **provider_marketing**。本檔不含 pain / hiring / purchase 證據。Marketing page != demand；list price != transaction price；testimonial/case study 不具代表性。
- 限制：
  - WebFetch 以小模型摘要頁面，個別欄位（如「頁面未寫」）可能是摘要遺漏；PDF 以 Read 直接讀（Datavail、Instaclustr、Somerford）可靠度較高。
  - CIGNEX、Data at Depth 因 DNS 失敗只有搜尋摘要（UNVERIFIED）。Nextbrick、Delbridge、Mimacom 部分欄位不確定，標 PARTIALLY VERIFIED。
  - 台灣：搜尋「叡揚、精誠、凌網」+ MongoDB 皆**無結果**（未找到證據，不代表不存在）。MongoDB Partner Finder 是 JS 目錄，未能讀取。僅找到新立資訊、CloudMile（新聞稿層級）。
  - Mydbops 頁面有內部數字衝突（客戶數 100+ vs 800+、首次回應 15 vs 30 分鐘、部分頁面數字為 placeholder）；已於 notes 註記。
  - AutoAuditDB 已確認停業，排除。Elastic observability review 等非 MongoDB/資料平台產品未納入。
- 未做：未聯絡任何供應商、未註冊、未取得 gated sample report。

## 筆數統計（來自 CSV 計算）

| 維度 | 筆數 |
|---|---|
| 總列數 | 34（31 company、3 independent） |
| evidence_status | VERIFIED 27、PARTIALLY VERIFIED 5、UNVERIFIED 2 |
| evidence_type | provider_marketing 34 |
| 分類（本檔自訂） | MongoDB audit/health/consulting 15；Kafka review 7；Data pipeline/platform audit 7；Managed/DBA 3；台灣 2 |
| 國家（依列） | India 9、US 9（含 US/global 等）、Taiwan 2、UK 2、Europe 2、Brazil 1、其餘未註明 |
| 來源 | 供應商官網頁 29、供應商 PDF 3（Datavail、Instaclustr、Somerford）、新聞 2（CIO Taiwan） |

## 1. 反覆出現的 scope 與 deliverable（MongoDB 類 15 列為主）

| 項目 | 出現情形（以有讀到頁面的 MongoDB 服務計） |
|---|---|
| Replica set / oplog / election / lag 檢視 | Percona、Ksolves、Datavail |
| Index 與 query review | 幾乎全部（Percona 明寫「僅建議」） |
| WiredTiger cache vs working set | Percona、Ksolves、Mydbops |
| Shard key / chunk balance | Percona、Ksolves |
| Security（RBAC/TLS/audit/encryption） | Ksolves、Mydbops x2、JusDB、Datavail；JusDB 與 Mydbops 另做 compliance mapping（SOC2/PCI/HIPAA/ISO） |
| Backup / restore / DR 設定 | Datavail、Mydbops、Ksolves（DR 服務） |
| 明確稱為 Upgrade readiness 的獨立品項 | **無獨立定價品項**。MongoDB Inc. Major Version Upgrade Consulting（assessment -> plan/dry run -> 選配執行）、Datavail（health check 為升級第 1 步）、Mydbops/JusDB 以 consulting 形式提供 |
| Kafka-MongoDB integration review | **未發現任何公開品項**（僅 Ksolves 個案提到 NiFi+Kafka 遷移） |

常見 deliverable 形態（INFERENCE，由列歸納）：PDF/書面報告 + severity 排序 findings + 30/60/90 天 roadmap + live walkthrough（Percona、Mydbops、Ksolves、Instaclustr、JusDB）。Scorecard/pass-warn-fail（Percona、Mydbops、JusDB 的 CIS matrix）是明顯的產品化包裝手法。

## 2. 價格可見度（34 列）

| 類別 | 數字公開價 | 說明 |
|---|---|---|
| 全部 | 7 / 34（20.6%）；其中 1 列（Data at Depth）僅來自搜尋摘要，頁面未讀到 | quote-only 約 11 列，其餘為「固定範圍但不公開金額」 |
| MongoDB audit/consulting（15 列） | **1 / 15（6.7%）**：Percona 起價 $11,400（MongoDB 變體，頁面稱 1–6 節點，At-a-glance 寫 1–5，自相矛盾） | Ksolves、JusDB 提供「免費 audit（單一 instance）」作 lead generation，付費價 UNKNOWN |
| Managed（3 列） | 1 / 3：Canonical $3,099/年/VM（公有雲）、$9,470/年/node（OpenStack） | 屬長期託管，非 audit |
| Data pipeline / platform audit（7 列） | 5 / 7：TBDC $1,990（3 週）、DataBeansAI $2,000（2 週）、Hikmah $3,000（約 1 週）、Gigabit $4,000（1 週）、Data at Depth $3,500–5,000（僅摘要，UNVERIFIED） | 全為小型/獨立工作室；Box5、Stonebridge 標「固定價」但金額未公開 |
| Kafka review（7 列） | 0 / 7 | Conduktor 為免費自助評分（lead gen）；Instaclustr、CIGNEX 等為 quote-only |
| MongoDB Inc. Flex Consulting | 時間盒（0.5/1/2/4 天）但價格未公布 | 「Buy in Atlas」 |

觀察（INFERENCE，非因果）：公開價錢集中在資料 pipeline 小型審查（約 $2,000–$4,000，1–3 週），MongoDB 專屬健檢僅 Percona 公開（$11,400 起，約 3 倍以上）。大型 MSP（Datavail、Pythian、Delbridge、Instaclustr）全部 quote-only。這是 provider list price，不等於成交價。

## 3. 交付時程、存取、後續

- 有明確 turnaround：21 / 34。典型：Percona 5–7 營業日；Mydbops Atlas/self-managed 2 週；Instaclustr Kafka 1–2 週（2020 PDF）；Pythian 2–4 週；JusDB/Ksolves 免費 audit 約 1 週（JusDB 明寫存取就緒後 1 週）。
- 明確寫 access requirements：15 / 34。最清楚的是 Mydbops（100% read-only，Atlas read-only 或暫時 scoped role）與 JusDB（NDA、metadata-only、read-only 診斷帳號、不查客戶 collection）。Percona 未寫存取方式。
- Remediation：明確「僅 review、實作另購」：Percona、Instaclustr PDF、Conduktor、Pythian、Hikmah、DataBeansAI（6 列）；Gigabit、Stonebridge 另有付費 Build（2 列）。Mydbops/JusDB 的 roadmap 含修復腳本或 runbook，執行為選配。Datavail 明列 Remediation 階段且可 fast-track 實作。
- 有 follow-up / walkthrough：26 / 34（多為 live readout 或 Q&A）。DataBeansAI、Hikmah、TBDC 有 30–90 分鐘 readout/call。

## 4. Trust signals 頻率（供應商自述，未獨立驗證）

| Signal | 列數 |
|---|---|
| 列出任何 certification/badge（ISO、SOC2、MongoDB Partner、AWS Partner 等） | 21 / 34 |
| 有 case study（含匿名） | 12 / 34 |
| 有 testimonial | 8 / 34 |
| 公開 sample report | 僅 Conduktor（可預覽）、DataBeansAI（頁面自述為虛構範例）；Mydbops x2 的「redacted sample」需填表（gated）；JusDB 僅單一 finding 節錄 |
| 保證 / 條件式退款 | 3（TBDC 無正式保證；Hikmah「day one 無可信機會則不收費」；DataBeansAI「teardown 後無值得修復則免費」） |

注意：JusDB 明說「與 ISO 27001/SOC 2 對齊，尚在取得中」（非已認證）。Ksolves 的 badge 無證書編號。XTIVIA 僅有 badge 圖檔名稱可見。這些為 marketing claim。

## 5. 台灣 / APAC（NEW EVIDENCE，皆為弱證據）

- **新立資訊**（C024）：CIO Taiwan 2023-05-11 報導，稱其「亦取得 MongoDB 認證」，提供一站式導入與技術支援，與 Dell PowerFlex 合作。**未見獨立健檢/audit 產品**。
- **CloudMile 萬里雲**（C025）：2024-06 獲 MongoDB 年度新興市場合作夥伴獎，2024-11-11 擴大 APAC 合作；服務為 Atlas+GCP/BigQuery/Vertex AI 整合，**無 assessment 品項**。
- 叡揚、精誠、凌網：搜尋無結果（UNKNOWN，非「不存在」）。
- INFERENCE：在本次可見範圍內，**台灣市場未發現公開、定價、可遠端的 MongoDB 健檢產品**；但這可能是搜尋能力限制（JS 目錄、中文網站索引不足），不可當成「市場空白」的結論。MongoDB.local Taipei 議程顯示原廠有台灣 SA/顧問，為原廠資源而非可委託的第三方顧問。

## 6. 對 Phase 1A 問題的初步含義（INFERENCE，需人工審閱）

1. 市場上「MongoDB health check / audit」已由多家供應商公開提供，且 Mydbops、JusDB、Ksolves 以免費/低門檻 audit 作為入口，價格壓力存在（來源：各官方頁）。
2. 已公開的 MongoDB 專屬固定價只有 Percona $11,400 起；其餘多為 quote-only。BASELINE 的價格假設若高於或低於此區間，缺乏獨立驗證。
3. 差異化空缺（僅就本次樣本）：Kafka-MongoDB integration review、獨立定價的 upgrade readiness、台灣在地（中文、時區）遠端產品，皆未見公開品項。這只代表「未在樣本中發現」，不代表有需求。
4. 小型獨立 pipeline audit 已有 $2,000–$4,000 的公開價位與「不滿意不收費」條件式保證，可作為定價與風險反轉設計的參照，但屬供應方宣稱，無成交證據。
5. 信任門檻：多數對手提供 NDA、read-only、metadata-only 存取，並以 ISO/SOC2 badge、Clutch、client logo 建立信任；獨立顧問缺乏這些訊號時，需靠 read-only 存取承諾、可預覽 sample report、條件式保證補足。

## 7. 資料列索引（id -> provider）

C001 Percona；C002–C003 Datavail；C004–C005 Instaclustr(NetApp)；C006–C007 Ksolves；C008 Delbridge；C009 XTIVIA/Virtual-DBA；C010–C012 Mydbops；C013 Conduktor；C014 Pythian；C015 Acosom；C016 Nextbrick；C017–C018 MongoDB Inc.；C019 Canonical；C020–C021 JusDB；C022 Rackspace；C023 Mimacom；C024 新立資訊；C025 CloudMile；C026 TBDC；C027 Box5；C028 Hikmah；C029 DataBeansAI；C030 Gigabit；C031 Stonebridge；C032 Somerford；C033 CIGNEX；C034 Data at Depth。

未涵蓋（建議後續）：Severalnines（搜尋僅見 ClusterControl 工具，無顧問品項）、Aiven、Confluent 官方 PS（舊頁面僅列 health checks，無範圍/價格）、Mydbops 其他頁、MongoDB 官方 Health Check datasheet PDF（webassets.mongodb.com，僅見連結，未讀內容）、MongoDB Partner Finder。

人工審閱提醒：所有內容為供應商行銷資訊的整理，需人工複核後再作決策依據。
