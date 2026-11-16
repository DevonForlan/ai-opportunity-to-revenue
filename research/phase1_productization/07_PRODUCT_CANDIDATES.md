# 07 Product Candidates（依證據排序）

標籤：`BASELINE` Phase 0 既有 · `NEW EVIDENCE` 本輪新資料 · `INFERENCE` 我的推論。資料集見 02/04/06。

## 1. 證據總表（計數皆來自本 repo 資料集）

| 候選產品 | Pain 列數（281 列，皆 level C） | 購買/雇用證據 | 供給端（公開價格／缺口） | Freelance 對應（86 列，皆為雇用貼文） |
|---|---:|---|---|---:|
| Backup/Restore Readiness | 45（最高） | 無 MongoDB 專屬 | 常見於大廠 audit 範圍；**未見獨立顧問單獨產品化**（INFERENCE，樣本內） | 2 |
| Replication / HA / Oplog Risk | 40 | 無 MongoDB 專屬 | 大廠 audit 必含；獨立顧問缺口同上 | 0 |
| Upgrade / EOL Readiness | 37 | 台灣 PCC：47 筆得標中 20 筆標題含「升級/升版」，但 DBMS 多為 Oracle/SQL Server | **未見獨立定價的 upgrade-readiness 產品** | 2 |
| Performance & Index Review | 35 | 無 MongoDB 專屬 | **供給最擁擠**：Fiverr/Upwork 大量低價查詢調校 gig | 8 |
| Kafka / CDC Integration Review | 39 | 無 | 獨立 $5,000–$7,500（Dattell、ZephyrCode，VERIFIED）；company 7 列 | 7 |
| MongoDB Health Check（泛稱） | （跨類別） | 台灣 PCC「資料庫健檢及優化」NT$1.40–1.48M（DBMS 未載明） | Percona $11,400 起（VERIFIED）；Contra 獨立 MongoDB+Redis audit $1,800 起 | 8 |
| Data Pipeline Reliability Review | 5 | 無 | 公司/獨立 $1,990–$4,000（list price） | 15（最大對應類別） |
| AI Automation Assessment | — | — | 非本輪核心 | 14（但與 MongoDB 無關） |
| Production Risk Assessment（以「風險結果」命名的組合） | = backup+HA+upgrade 合計 122/281 | 同上 | Mydbops/JusDB 等公開「read-only、NDA」交付 | — |

## 2. Ranking（INFERENCE，依上表四條證據線；不使用加權分數，因無依據）
1. **MongoDB Production Risk Assessment**（Backup/Restore + Replication/HA/Oplog + Upgrade/EOL + 必要 index/security 檢查，read-only）
   - 理由：三類最大 pain 合計 122/281（43%）；供給端獨立顧問缺口；大廠公開範圍重疊，代表此範圍是業界可標準化的交付；read-only 可行（見 09）。
   - **弱點（NEW EVIDENCE，負面）**：沒有任何 MongoDB 專屬的購買證據；281 則 pain 中 **0 則**表明預算或要找人付費（level C 論壇文）。
2. **Upgrade / EOL Readiness**（可作為 #1 的單點入口產品）：有 EOL 時間表驅動（6.0 EOL 2025-07-31、7.0 2027-08-31、8.0 2029-10-31，摘要，使用前需重驗）、台灣公部門有大量「資料庫升級」採購（但非 MongoDB）。
3. **Kafka/CDC Review**：有獨立價格錨點（$5,000–$7,500），但 pain 多為開發者 bug 回報，誰付費 UNKNOWN。
4. Performance & Index Review：需求量在，但低價 gig 擁擠 → 難以定價站位。
5. Data Pipeline Reliability：freelance 對應最多、有 $1,990–$4,000 list price，但 pain 僅 5 列且與 MongoDB 專長關聯弱。
6. 泛稱「Health Check」：名稱本身不是購買理由（見 §3）。
7. AI Automation Assessment：不與本研究目標直接相關，列後。

## 3. 客戶買的是什麼？（Issue #4 §2 的 13 問，以證據回答）
1. 最常見 pain：backup/restore、HA/oplog、Kafka/CDC、upgrade/EOL、performance（見表）。NEW EVIDENCE（level C，非付費證據）
2–4. 多為 **incident-driven 與 upgrade/migration 前**（備份還原失敗、failover、升級後變慢）；proactive 評估型貼文很少 → 「評估」常是事故後或升級前觸發。INFERENCE
5–6. 效能/索引、HA/oplog 是專項；7. security 19 列；8. Kafka/CDC 39 列。
9. 最易固定 scope：EOL/upgrade readiness、backup/restore readiness、replica set/oplog 風險（皆有明確檢查清單，見 08）。INFERENCE
10. 最適遠端：以上三項皆可用 read-only 證據完成。
11. 需 production write access：**不需要**（診斷階段）；restore 實測、調優落地需要客戶環境與寫入 → 應排除於 scope 外（remediation 另售）。
12. read-only 證據可完成：config/拓撲/oplog window/索引統計/備份設定/版本與相容性；**無法只靠 read-only 完成**：實際還原演練、負載下效能驗證。
13. **購買的是「降低明確風險」而非「Health Check」名稱**：台灣得標案名多為「資料庫健檢及優化」「效能調校」「升級」「維運」；獨立賣家用「audit / triage」；沒有證據顯示客戶搜尋「Health Check」。INFERENCE（案名證據為 A，結論為推論）

## 4. 產品定義草案（INFERENCE；尚未被市場驗證）

### P1 — MongoDB Production Risk Assessment（read-only）
- ICP：運行自管（self-managed）或 Atlas 的 MongoDB 的中小型團隊，沒有專職 DBA，觸發事件＝近期事故、即將升級／EOL、合規或稽核、交接。
- Problem：「我不知道備份是否真能還原、failover 是否安全、版本是否過期」。
- In-scope：topology/config 快照、replication+oplog window、backup/restore 設定審查（不含實際還原）、版本/FCV/EOL 與升級相容性清單、index 使用統計（$indexStats）、基本 security/access-control 審查。
- Out-of-scope：任何 production 寫入、實際還原演練、調優落地、遷移、24x7 支援、客戶資料內容檢視。
- 前置：客戶提供 read-only 帳號（`clusterMonitor`+`read` 類，最低權限需官方文件逐項確認，見 09）或自行執行我們提供的唯讀腳本並回傳輸出（**降低存取風險，也避開客戶資料進 AI 的政策問題**）。
- 交付物：見 08（Finding Register + 摘要 + roadmap + 證據包 + readout）。
- 驗收：每個 finding 有 evidence_ref；critical/high 經人工覆核。
- Remediation：另售。
- 標準化程度：高（rule-engine 可覆蓋大部分）。
- 風險：責任限制條款、NDA、客戶環境資料保密、WebComm 組織政策。

### P2 — MongoDB Upgrade / EOL Readiness（P1 的單點版本，用於低門檻入口）
同上，scope 限縮為版本差距、相容性、升級路徑、回滾前提。

不先硬套 Basic/Pro/Enterprise；等 pilot 取得 scope 變異資料再決定。

## 5. 相對 Phase 0 的修正
- `BASELINE`：「P1 = Productized MongoDB/Data 健檢（人主導）」→ `NEW EVIDENCE`：**方向保留，但證據強度下修**：MongoDB 專屬購買證據為 0；有價格錨點與公共採購的「泛資料庫健檢」證據。
- `BASELINE`：Contra 為可行通路 → `NEW EVIDENCE`：Contra 條款限制自動化外聯與「免費試用/導入服務」，免費 mini-audit 作 lead magnet 可能違規（見 12）。
