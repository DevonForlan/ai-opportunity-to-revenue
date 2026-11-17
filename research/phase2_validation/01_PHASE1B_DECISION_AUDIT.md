# 01 Phase 1B Decision Audit（合併 + 修正後排名）

細節：`01_AUDIT_part1_purchase_and_demand.md`、`01_AUDIT_part2_freelance_and_supply.md`；抽查資料：`01_purchase_remap.csv`（126）、`01_audit_demand_sample.csv`（50）、`01_audit_freelance_sample.csv`（35）、`01_audit_supplier_sample.csv`（25）。審計由獨立 agent 在不預設舊標籤正確的前提下執行；我另外重算了關鍵數字。**審計樣本：purchase 126（全數）＋demand 50＋freelance 35＋supplier 25 ＝ 236 筆**（Issue 要求 50/30/20，皆達標）。

## 1. 判決：Phase 1B 的結論**需要修正，已直接修正**
**我（Phase 1B 的作者）犯的錯，審計抓到：**
| # | Phase 1B 說法 | 審計結果 | 影響 |
|---|---|---|---|
| 1 | Workflow Automation purchase = 20 | **20 筆全是 RPA/流程自動化標案，不是 AI**；AI 的 workflow purchase = **0** | Workflow 的購買支撐被抽空 |
| 2 | Internal AI Assistant purchase = 33 | 實為 **4**；26 筆移到「用途不明的 AI」，2→doc、1→RAG | 重複計算被消除 |
| 3 | Assessment purchase = 7 | 修為 **4** | Assessment 的購買支撐更弱 |
| 4 | 「≤TWD 1.5M 共 31/105，購買證據落在個人可及規模」 | 其中 8 筆是 RPA；**AI 列 23/89（26%）**；有投標家數的 19 筆中 **11 筆僅 1 家投標**；僅 1 筆是 assessment（TWD 1.48M，單一投標）；「政大 RAG PoC 1.45M」是**學術研究**，不是商業 PoC | 「個人可及規模」論證被削弱 |
| 5 | 126 筆 purchase 的 mapping／type | **50% 被修改**（mapping 44%、type 15%）；16% 不是 AI | 見下表 |
| 6 | Pain 資料 155 列為「買家需求」 | 抽 50 筆：僅 **24% 明確是買家**；59% 的 pain 列是從業者討論、bug、功能需求或其實是徵才；嚴格誤分類 12%、mapping 需改 26% | Pain 只能當訊號 |
| 7 | Freelance 137 列 | 抽 35：**41% 已失效（Wilson 95% CI 25–59）**、mapping 錯 31%（CI 19–48）、預算錯 7%；14 筆抽查 VERIFIED 中有 4 筆不是有效需求 | 高估現存需求 |
| 8 | 供給端「47% 價格透明」 | 僅 AC 系列成立；全資料 50/96＝**52%**；solo 24/44＝55%；有重複列（AS047=AC001、AS014=AC010） | 小幅修正 |
| 9 | 「solo 以審計為入口約 18/39」 | 去重後 **36–43%**（上限 55%，因樣本以 audit 關鍵字蒐集）；中位 **US$624.5（n=10，四分位 200/1,374）**，敏感度 US$499–825；一半 ≤US$500；公司/boutique 中位 US$3,950（n=11） | 數字可重現但脆弱 |

## 2. 修正後的 purchase 分佈（126 列；`01_purchase_remap.csv`）
| 修正後類別 | 列數 | 備註 |
|---|---:|---|
| 用途不明的 AI（other-AI） | 31 | **不得用於次級排名** |
| Support／客服 | 28 | 仍是最強的單一類別 |
| Document／知識文件 | 14 |  |
| RAG／知識庫 | 13 |  |
| Agent | 7 |  |
| Assessment | 4 | 原 7 |
| Eval | 4 | 皆為產品／研發／QA |
| Internal assistant | 4 | 原 33 |
| AI-ready data | 1 |  |
| **不是 AI（RPA）** | 20 | 原計入 Workflow |
類型：implementation 72、maintenance 18、other 15、assessment/research 13、PoC 8。

## 3. 對 Issue §1 七個問題的回答
1. **product_mapping 是否真被證據支持？** purchase 一半被改；pain 26% 需改；freelance 31% 錯 → **不可信至「排名細節」層級**，只能支持粗類別。
2. **purchase/hiring/pain/marketing 是否混淆？** 是：pain 中 59% 非買家；freelance 中混入賣家廣告與招募聚合頁。
3. **Internal Assistant／RAG／Support／Workflow 是否重複？** 是：Internal 33→4；Workflow 20 筆為 RPA。
4. **Assessment #1 是否被 scoring 偏好「容易 solo 交付」而高估？** **是。** 其購買證據降為 4、需求形狀為 implementation 遠多於 assessment（見 5），Phase 1B 的 #1 靠的是「結構」論證，而審計＋solo 案例研究（04）沒有證實該結構。
5. **implementation 需求是否比 assessment 強？** **是（方向成立）**：Freelance 約 4 vs 101（/137）；PCC 19 vs 84（/105）；solo 已交付案例 32/39 為直接實作、audit-first 8/39，且**「審計轉成建置」已驗證案例＝0**（04）。反向訊號：PRO360 的 AI 顧問需求 3/6 為諮詢形狀（無預算）；marketplace 本身偏任務型。
6. **低價 marketplace 是否過度影響排名？** 審計判定**不成立**：移除未驗證與賣家廣告列，只讓 workflow 的 Buyer breadth 由 H→M。更實際的風險是**論壇 pain 與供應商標價**在撐 #1（assessment）。
7. **公部門證據是否被錯誤外推到私人 SMB？** **部分成立**：Phase 1B 有寫限制，但「個人可及規模」與 #2 Support 的論證仍倚賴公部門資料；PCC 文件級分析（06）顯示 9/10 單一投標、客服標案需過往完工證明、赢家為 SI/大學/基金會，**沒有可見的個人得標者**。私人 purchase 嚴格計算見 02（真正私人且有金額＝2 筆，皆百萬美元級）。

## 4. 修正後排名（`INFERENCE`；信心：中低）
| 新排名 | 候選 | 為何 | 與 Phase 1B 比 |
|---|---|---|---|
| 1 | **Support / Service Automation（以固定範圍 PoC 實作）** | AI 購買證據最集中（28）；freelance 需求最大宗之一；solo 已交付案例以實作為主；結果清楚（減少重複客服處理） | ↑（原 #2） |
| 2 | **Workflow ＋ Document Automation**（併計；注意 AI 的 workflow purchase＝0，文件類 14） | freelance 需求最大；但**常常不需要 AI**（規則/腳本即可），價格最低、競爭最高 | ≈（原 #3，購買支撐下修） |
| 3 | **RAG / Knowledge Assistant** | 購買 13；市集預算較高但 n 小；資料敏感度與存取負擔最高 | ≈（原 #4） |
| 4 | **Assessment/Diagnostic（僅作 PoC 的前置、可折抵，不當獨立主力產品）** | 購買證據 4、轉換為建置的驗證案例 0；供給端大量且價格兩極（solo 中位 US$624.5 vs boutique US$3,950） | **↓（原 #1）** |
| 5 | **Eval / Guardrail** | 結構清楚但購買 4（皆產品/研發）；單獨付費 UNKNOWN；適合作為 #1–#3 的附加品質交付 | ≈ |

**信心**：高→「20 筆非 AI」「Internal 33→4」「implementation 需求形狀多於 assessment」；中→類別間排序；低→任何以公部門或標價推論個人成交。

## 5. 對 Phase 1B 文件的處理
已在 `phase1b_ai_application/08_AI_PRODUCT_SCORING.md` 與 `16_PHASE1B_RECOMMENDATION.md` 頂部加入「Phase 2 審計修正」橫幅；原內容保留供追溯，**不再作為決策依據**。
