> ⚠️ **PHASE 2 審計修正（2026-11-17）**：本檔的排名與若干計數已被 `research/phase2_validation/01_PHASE1B_DECISION_AUDIT.md` 修正（purchase 126 筆有 50% 被誤分類；Workflow 的 20 筆 purchase 為 RPA、非 AI；Internal assistant 33→4；Assessment 7→4；「個人可及規模」論證被削弱）。**下列內容保留供追溯，不再作為決策依據。**

# 00 Phase 1B Executive Summary（AI Application / AI Automation）

**判定：CONDITIONAL GO → 測試獲客 + 小型 pilot；不做 product build。** 詳見 `16_PHASE1B_RECOMMENDATION.md`。

## 規模（真實記錄列；皆為最低門檻以上）
| 資料集 | 列數 | 目標 |
|---|---:|---:|
| 需求（purchase 126／pain 143／hiring 25／provider 1） | 295 | ≥150 |
| 供給（公司 41＋獨立/boutique 55，含 39 個頁面實讀的 solo） | 96 | ≥60／≥25 |
| Freelance（API 平台 71＋其他平台 66） | 137 | ≥100 |
| AI＋DB 差異化專案資料集（獨立） | 81 | — |
| 去重來源 | 226 | — |

## 核心結論
1. **Top 5**：① AI Automation Assessment（assessment-first，折抵 PoC）② Support/Service Automation ③ Workflow Automation（含 Document automation）④ RAG/Knowledge Assistant ⑤ AI Eval/Guardrail Review。
2. **私人買家購買證據 = 0**；126 筆 purchase 全為公部門（台灣 PCC 105、美國 USAspending 21）。個人能否承接 UNKNOWN。
3. 台灣 PCC 105 筆 AI 得標：中位 TWD 3.68M；31 筆 ≤TWD 1.5M；assessment/PoC 類含 TWD 0.85–1.48M；47/96 僅 1 家投標。
4. 市集預算低、競爭高（Freelancer 固定價中位級距 US$250–750、投標中位 125）；solo 入口審計 US$45–5,000 擁擠；boutique 評估 US$3.5k–12.5k。
5. 客戶買的是**流程結果**，不是「AI」。需求端是 implementation 形狀，供給端以 assessment 作入口 → 「assessment 作銷售結構、PoC/建置作營收」。
6. **AI＋Data/MongoDB/Kafka 差異化：無買家證據**（AI+DB 買家證據 0）→ 不加分。MongoDB 降為次要能力。
7. 通路：人工直接接觸／網絡；市集不宜為主；AWS Marketplace 付費賣家不含台灣；n8n Experts 封閉且地區不含台灣。
8. 自動化比例 UNKNOWN（n=1 實驗）；客戶資料受公司政策限制，需去識別化。

## 文件導覽
01 需求 · 02 需求資料集 · 03/04 供給 · 05/06 Freelance · 07 候選與 Top5 設計 · 08 評分 · 09 交付物 · 10 交付自動化 · 11 Solo 模型 · 12 定價 · 13 通路/法務 · 14 AI+DB 差異化 · 15 缺口 · 16 建議 · `_sources/ALL_SOURCES.csv`。
