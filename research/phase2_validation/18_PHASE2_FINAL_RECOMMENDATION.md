# 18 Phase 2 Final Recommendation

## 判定：**HOLD**（研究階段可以結束；下一階段是「驗證」，不是「開發產品」）
詳見 17。重點：沒有任何一個未知數是「再做桌面研究」能解的——剩下的都需要使用者行動或接觸買家。

## 回答 Issue #8 要求回報的項目

**證據樣本數**
- Decision Audit：purchase 126（全數）＋demand 50＋freelance 35＋supplier 25 ＝ **236**
- 私人買家證據：93 列（嚴格分級見 02；真正私人且有金額＝2）
- Solo/boutique 已交付案例：39 列（≤15 人者 21；台灣 0）
- 台灣民間商業證據：34 列（具名買家＋具名供應商＋合約金額＝0）
- PCC 文件級分析：10 件（**招標文件本文無法取得**，僅讀公告欄位，全為 PARTIALLY VERIFIED）
- 去重來源：128

**Ranking audit 結果（01）**：Phase 1B 的結論需修正。20 筆「workflow purchase」是 RPA；Internal assistant 33→4；Assessment purchase 7→4；purchase 一半被誤分類；「個人可及規模」被削弱（AI 列 23/89；11/19 單一投標）；pain 僅 24% 是買家；freelance 41% 已失效。**修正後排名：1 Support PoC、2 Workflow/Document、3 RAG、4 Assessment（併入 PoC 診斷）、5 Eval。信心：中低。**

**Final offer（07）**：Revenue＝「客服信件處理時間縮減 PoC（人工核准版）」；Entry＝可選的「診斷週」（實驗臂，可折抵）；Follow-on＝上線輔導／月度調校（證據弱）。

**Pilot A/B 結果**
- Pilot A（**合成**）：完整評估報告已交付；客服流程在 59,049 種輸入組合中 94.4% 仍是 AI 類第一名（但輸入由我設定，且 Pilot B 先於 Pilot A 完成）；並明確告訴「客戶」P3、P4 不需要 AI。
- Pilot B（**合成**）：可執行 PoC（`pilot/phase2/supportdesk/`），21 測試通過，CLI 端到端可跑。**LLM 路徑未實作、未測。**

**Test / eval 結果（11）**
- DEV 42：outcome 1.00（但為調參資料）。
- **HELDOUT 30：初始 0.80；最終 0.833**；危險方向錯誤（該升級卻出草稿）**2/10**（H16 多重意圖、H24 改寫型注入）；過度升級 3/17；PII 洩漏 0；承諾違規 0；草稿皆有 KB 依據。
- 過程中發現並修正 2 個真缺陷（子字串關鍵字、**冪等遺失客訴**）；後者由我質疑自己的測試發現，不是測試套件發現。
- 初始 HELDOUT 的 H24 是「因錯誤原因被攔下」——最初的 1/10 低估了風險。

**Human time（12）**：**未量測（UNKNOWN）**。只量到 agent 牆鐘 ≈8 分鐘。**我不計算 automation ratio**——沒有人工時間與人工基準，任何百分比都會是虛構。

**Automation findings（12）**：確定性元件可重用且可秒級重跑；敘述類由 agent 撰寫但**未經人審**；兩個真缺陷都不是 agent 自己寫的程式裡自己抓到的 → 「agent 寫＋agent 測」需要獨立的對抗性審查，是不可省的成本。

**Pricing hypotheses（14）**：H1 診斷週 US$600–1,500＋PoC US$3,000–8,000（折抵）；H2 PoC 內含診斷 US$3,000–8,000；H3 小診斷 US$200–500→PoC。**皆為待驗證假說**；成交證據：Freelancer 中位約 US$100、單人 US$3k 以上成交＝0 筆；有效時薪取決於未量測的人工小時（14 §3 提供算術網格）。

**Build decision（17）**：**HOLD**。未滿足：#5 人工工時未量測、#10 雇主/稅務/法律限制未知；部分：#6 自動化槓桿、#9 資料政策。**未建立 `product/` 規格**（僅 GO 時需要）。

**Blockers**
1. 雇主兼職／NDA、稅務、行號、收款（使用者）。
2. 人工時間（需真人計時，U2）。
3. 客戶資料與 LLM 的處理方式（公司政策禁止客戶資料入 Claude）（使用者）。
4. 私人買家付費意願 — 公開資料已到天花板，需接觸買家（使用者授權與執行）。
5. PCC 招標文件本文無法取得（WAF／HTTP 500，未繞過）；所有 PCC 列為 PARTIALLY VERIFIED，需人用瀏覽器取得 RFP 才能升為 VERIFIED。
6. 台灣補助／輔導：獨立顧問被排除（輔導員須為正式全職員工）；SI 主承包需「能量登錄」等資格（獨資是否符合 UNKNOWN）。

**對 Issue #8 §18 完成條件的誠實對照**
| 條件 | 狀態 |
|---|---|
| Phase 1B ranking 已複核 | ✅ 並已修正 |
| private buyer targeted search | ✅ 完成，**但嚴格計算未達 ≥40**（天花板見 02） |
| solo/boutique 案例 | ✅ 39 列（已交付案例；audit→build 轉換驗證 = 0） |
| Taiwan commercial | ✅ 34 列（**具名買家＋供應商＋金額 = 0**；未達「≥20 可驗證案例」的嚴格解讀：named private cases 僅 4 且無價格） |
| 5–10 PCC 文件 | ⚠️ 10 件，**但僅讀公告欄位，招標文件本文取不到** |
| Offer 定義 | ✅ |
| Pilot A 完整 / Pilot B 可跑＋eval | ✅（合成） |
| 真實工時與自動化量測 | ❌ 人工時間未量；automation ratio 不計算 |
| Build-vs-buy、定價、獲客、商業素材 | ✅ |
| Readiness Gate／最終判定 | ✅ HOLD |
| PRD/MVP（若 GO） | 不適用（HOLD） |

## 建議的下一步（依序，最小成本）
1. **你**：確認雇主兼職政策、稅務與收款（U1）。
2. **你**：花約 1–2 小時照 17 的協定做一次**計時的人機協作 run**（U2），把人工分鐘貼回 `09_PILOT_A_TIMELOG.csv`。
3. **你**：決定客戶資料與 LLM 的處理方式（U4）。
4. 完成 1–3 後我重新評估 Gate；若通過，可啟動 15 的獲客測試（外聯由你決定與送出），並以「服務＋內部工具 v0.1」為上限的小範圍整理（17 末段）。
5. 若獲客測試 20 場合格對話後仍無書面付費意願 → 依 07/15 的 kill criteria 停止此 offer。

## 相對先前階段的總結
- Phase 0：副業系統 → 縮小到「顧問型、半自動」。
- Phase 1A：MongoDB 健檢（MongoDB 專屬購買證據 0）。
- Phase 1B：AI 應用；排名被 Phase 2 審計修正。
- **Phase 2：技術可交付性在合成資料上成立；商業需求在公開資料上到不了「有人付費給單人顧問」的證明。下一個資訊來自你，不來自我。**

## 驗證註記（我對 agent 回報的抽查）
04／05／06 與審計的數字大多來自獨立 agent。我自行重算或抽查了：purchase remap（126 列、63 列變更、20 列非 AI、各類別計數）、PCC 文件級 CSV（10 件、9 件單一投標、全為 PARTIALLY VERIFIED、僅讀公告欄位）、私人買家分級（93 列→T1–T5）、台灣方案規則列（TW002 為 A 級 VERIFIED）。**未逐一重新開啟各網頁**；agent 以小模型摘要讀取的條款與日期仍需人工對照原頁。
