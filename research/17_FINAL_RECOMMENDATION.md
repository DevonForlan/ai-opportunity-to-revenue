# 17 Final Recommendation

## 判定：**CONDITIONAL GO**（範圍受限的半自動系統；不是「全自動 AI 副業」）

## Why / Main Evidence
1. **GitHub bounty 路線 NO-GO**：28 個詳查、0 個同時未指派/未結算/有人回應/付款可證；最高 Fit 48/100；Algora 平台實質萎縮（bounties 頁 404、首頁轉 recruiting；是否正式關閉 UNKNOWN）；Opire claim 不保證付款；搜尋結果 ~72–87% 疑似 farm。（04, 03）
2. **接案平台低價紅海 + 可得資料有限**：Freelancer 樣本多為 $4–50/hr；Upwork 公開頁 403，需求/價格 UNKNOWN。（05）
3. **唯一有公開付費證據的方向 = 標準化 DB/Data 審計服務**：Percona 審計起價 $11,400、AVP $490（VERIFIED，個人顧問可成交價 UNKNOWN）。與用戶最強技能（MongoDB/Kafka/Data）重合。（05, 07）
4. **現成 OSS 只涵蓋「蒐集+去重」**，不涵蓋證據驗證/核准/收入追蹤；TIP 的價格是作者推測；Shipwright 太重。→ Hybrid。（02）

## Expected First Revenue Route
Productized「MongoDB / Data Pipeline Health Check」，人主導、AI 加速診斷腳本與報告產出；通路：直接外聯 + Contra 類（Contra 官方列台灣可收 USDC/PayPal/銀行）。

## Expected MVP
SQLite + CLI + 3 collectors + 每日 Markdown 報告 + 人工 approve（~2–3 天）。無 dashboard、無 multi-agent。

## Required Human Involvement
所有對外動作（帳號、提案、聯絡、合約、收款、報稅）全人工；驗證付款證據人工。

## Main Risks
雇主兼職/NDA（未知，必先查）、台灣稅務類別（服務在台執行可能屬台灣來源所得，需會計師）、組織政策禁止將客戶資料餵 AI、單一價格證據（兩個 anchor 相差 20 倍）、樣本小。

## Priority
- **P1** Productized DB/Data 服務　**P2** Data/DB freelancing（Contra 等）、AI agent 機會型案件　**P3** Python/API/RAG 接案
- **Avoid for now**：OSS bounty、Micro-SaaS、Dev tool、Newsletter

## 「要自動化多少才合理？」
自動化到「發現→驗證輔助→評分→任務包」即止（~2–3 天工程）；之後半自動。全自動無證據支持，ROI 不如人工主導。

## Kill Criteria
見 15。**升級為 GO 的條件**：30 天內拿到 ≥1 筆已入帳且可驗證的收入，且有效時薪高於用戶底線。

## 已知限制（誠實聲明）
未達 brief 目標：bounty 20 筆（實得 28 筆詳查但 0 可行，屬 finding）；接案樣本 30 筆但僅 9 筆逐頁驗證、Upwork 等未取得；成本模型多為 UNKNOWN；build-DNA repo 未確認；以上結論需人工複核。
