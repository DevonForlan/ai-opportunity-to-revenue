# 01 Audit Part 2：Freelance 樣本與供給端（獨立稽核）

稽核日：2026-11-17。對象：Phase 1B `06_AI_FREELANCE_SAMPLES.csv`（137 列）、`04_AI_COMPETITOR_DATASET.csv`（96 列）、`12_AI_PRICING_EVIDENCE.md`、`11_SOLO_CONSULTANT_MODEL.md`。標籤：BASELINE / NEW EVIDENCE / INFERENCE。**不假設原標籤正確；全部為唯讀 GET，未登入、未繞過 403/CAPTCHA、未聯絡任何人。**

## 0. 方法與限制（先讀）

- **Freelance 抽樣（Task 1）**：Python `random.seed(7)`。第 1 步：14 個 platform 各 `random.sample` 1 列（14）；第 2 步：補足尚未出現的 product_mapping（結果 14 類已全涵蓋，補 0）；第 3 步：從 Freelancer / Upwork / PeoplePerHour / n8n 四大平台剩餘列隨機補到 35。n=35。這是**分層便利抽樣，不是比例抽樣**，錯誤率只對本批 35 列有效；信賴區間用 Wilson 95%。腳本在 scratchpad（`aud2/sample.py`）。
- **重開 URL 的手段**：Freelancer 用公開 API（`/api/projects/0.1/projects/?seo_urls[]=`，與 Phase 1B 同一來源，讀 status/budget/description）；PeoplePerHour、PRO360、Arc、LinkedIn、Dice、Wellfound、Working Nomads、Remotive 直接 curl 讀 HTML；n8n/Make 讀 Discourse `.json`。**Upwork（6 列）403、Indeed 401、Braintrust 鏡像 403：不繞過，標 unknown**（WebFetch 對 Upwork 同樣 403）。
- **時間差**：Freelancer 列擷取於 2026-11-16，我重查在 11-17，只隔 1 天；所以 Freelancer 的 frozen 狀態不是「時間久了過期」，而是擷取當下就可能已凍結（CSV 沒有 status 欄）。PPH 列的 CSV 備註已寫「past listing」的，**狀態 Awarded/Expired 並非新出現**，錯在 CSV 把它們仍當需求列計數。
- **供給端（Task 2）**：Python seed 7，強制納入 ≥12 solo（實際 15 solo / 10 company 或 boutique）、涵蓋有價 audit、無價 audit、非 audit solo、公司有價/無價、折抵列、台灣列。n=25。重算部分用**全 96 列**，Python 規則見 §3。
- **限制**：供給頁是 provider marketing（標價 ≠ 成交價）；頁面可讀不等於賣家真的有成交；`solo` 判斷只能依頁面第一人稱/自述，無法證明沒有分包。

## 1. Task 1：Freelance 35 列稽核結果

完整逐列在 `01_audit_freelance_sample.csv`。

| 指標 | 結果 | 說明 |
|---|---|---|
| 仍 live（y） | **16/35** | Freelancer API active、PPH Open for Proposals、n8n/Make 頁面在、Arc/PRO360/LinkedIn 頁面在 |
| 已死或已結案（n） | **11/35** | Freelancer frozen 2（AF025, AF019）、PPH Awarded 4（AF068, AF058, AF055, AF059）、Dice 410 頁面寫 no longer available 2（AG059, AG057）、Wellfound closed 1（AG060）、Lemon.io 404/expired 2（AG055, AG054） |
| 無法確認（unknown） | 8/35 | Upwork 6、Indeed 1、Braintrust 鏡像 1（全部 403/401，未繞過） |
| 可判定者中的死亡率 | **11/27 = 41%（Wilson 95% CI 25–59%）** | 注意樣本是分層，非母體比例 |
| product_mapping 不成立 | **11/35 = 31%（CI 19–48%）** | 保守版（剔除我自己標為邊緣的 AF048、AF025、AG052）為 8/35 = 23% |
| stated_budget 抄錯或不可歸屬 | **2/27 可核對 = 7%（CI 2–23%）**；另 8 列不可核對 | AG063（CSV 自承金額未對應此 URL）、AG057（頁面 meta 明寫 Bill Rate $72/hour，CSV 填 UNKNOWN） |
| verification_status 標籤誠實度 | **0/35 標籤與「是否真讀過頁面」衝突** | Upwork/Dice/Wellfound/Indeed 標 UNVERIFIED、PPH 標 PARTIAL 都合理；Arc 標 PARTIAL 偏保守（我開得到） |
| 但「VERIFIED」≠「有效且仍 live 的需求」 | 抽到的 14 列 VERIFIED 中 **4 列（29%）不是有效 live 需求**：AF025（frozen）、AF019（frozen + 賣家自我宣傳）、AF007（賣家自我宣傳）、AG054（expired + 招募廣告） | VERIFIED 只代表「讀到 payload」，被後續分析當成需求證據強度，這是標籤語意問題 |

### 1.1 錯誤型態（NEW EVIDENCE）

1. **賣家自我宣傳被算成需求**：AF007、AF019 的描述開頭是「I build … / I'm an engineer who helps businesses …」。CSV 備註已承認「reads like freelancer self-promo」，仍放在 `workflow-automation`（該類 25 列中至少 2 列 = 8%）。
2. **招募/聚合頁被算成需求**：AG055、AG054（Lemon.io 在招工程師，賣方）、AG066（LinkedIn n8n 聚合頁，頁面標題 17,000+ 與 CSV 摘要 ~88 筆相矛盾）。
3. **已 Awarded/Expired 的 PPH 列仍計入**：我把 PPH 全部 26 列重讀：**Open for Proposals 10（38%）、Expired 9（35%）、Awarded 6（23%）、無法判讀 1**。換句話說 PPH 26 列中只有約四成是仍可投標的需求。Awarded 6 列金額 US$100–660（顯示值）。
4. **mapping 偏向「AI 關鍵字」而非交付物**：AF030（行銷歸因 n8n 管線）被放 `ai-ready-data`；AF059（chatbot 故障排除）被放 `eval-guardrail`；AF025（整套 SaaS 產品）被放 `ops-copilot`；AG051（Shopify 追蹤 + Klaviyo）被放 `sales-backoffice`。
5. **幣別**：PPH 金額是 PPH 顯示的 USD 換算值（原幣 GBP），CSV 欄位寫「USD (as displayed by PPH)」，所以**不算錯**，但原幣沒存（AF068 頁面文字 GBP 500/月 vs 顯示 $660，CSV 已標示不確定）。

### 1.2 Freelancer 全母體（45 列）附帶檢查（NEW EVIDENCE）

用 API 重讀全部 Freelancer 列：**41 active、3 frozen（AF019、AF025、AF040）、1 查無（AF041）**；**44 個可查列的預算區間與 CSV 全數一致**（0 抄錯）。Freelancer 預算是平台**預設級距**（15 列 USD 固定價中 9 列是同一個 US$250–750 級距），所以「Freelancer 固定價中位 US$250–750」是級距選項的產物，不是市場價格分佈（BASELINE 12 號檔寫的 14/16 ≤US$800，我重算為 13/15，一致）。

## 2. Task 1 推論：assessment 與 implementation（見 §4(b)）

## 3. Task 2：供給端稽核與全母體重算

### 3.1 25 列頁面稽核（`01_audit_supplier_sample.csv`）

- 頁面可開：**25/25**。
- 價格與頁面一致：**24/25**（唯一差異：AS024 頁面 EUR 39.43，CSV 39.39，金額無實質影響）。
- scope 與頁面一致：25/25；但 **AS016 的「audit」入口其實是 30 分鐘通話（US$75）**，完整 feasibility report 另計，把它算成 audit 入口是高估。
- solo 宣稱（15 列 solo）：12 列頁面支持（第一人稱/單一署名）、2 列「unknown」（AS013、AS001：頁面混用 I/we 或未明說）、**0 列被推翻**。
- 折抵（credit-toward-build）頁面確認：AS018、AS020、AS001、AC006（US$12,500 全額折抵 US$25k+，90 天內）、AC032（INR 25K–50K 全額折抵）。AS017 FAQ 有問題但**沒有可見答案**（CSV 同樣寫未答）。
- 來源品質問題：AC036 的 URL 是 TechNews 報導不是叡揚官網；AS050 是 benchmark 部落格不是報價頁；AC032（SOT Labs）被標為 company，但審計價約 US$300–600，與 solo 同價帶。

### 3.2 資料集結構問題（NEW EVIDENCE）

- **重複供應商**：AS047 = AC001（Main and Machine，同網域）、AS014 = AC010（Outright Mental）。另 AC015/AC016/AC033（IT Partner 三個產品）、AC024–AC026（Caylent 三個產品）是同一公司多列。
- **「公司 43」其實是 AC 系列 43 列，內含 2 列 independent（AC008、AC010）**，真正 company = 41。
- **「47% 價格可見」只對 AC 系列成立**：AC 43 列中 20 列有價 = 46.5%；若只算 company 41 列為 19/41 = 46%。全 96 列為 50/96 = 52%；solo（independent 系，去重後 44 列）24/44 = 55%；boutique 6/10。
- 可見價格規則：`public_price` 不以 UNKNOWN 開頭且含數字即算可見（含搜尋摘要來源的 AS051、AS053，因此是寬鬆上限；AS040/AS049 這類「UNKNOWN（平台範圍/摘要）」不算）。

### 3.3 重算：solo 以 audit/diagnostic 為入口的比例

分母（去重 independent 系）= **44**（BASELINE 用 39 = AS001–AS039，含 AS033 已停止接案）。

| 定義 | 列數 | 占 44 | 占 BASELINE 39 |
|---|---|---|---|
| BASELINE 名單（AS001, 002, 005, 006, 008, 009, 012, 013, 014, 016–020, 025, 034, 035, 036） | 18 | 41% | 46% |
| 嚴格：有獨立命名、有書面成果的 audit/review/diagnostic（排除 AS016 的 30 分鐘通話與 AS006 的諮詢） | 16 | 36% | 41% |
| 寬鬆：BASELINE 名單 + AS052（Upwork catalog readiness audit） | 19 | 43% | — |
| 最寬：再加以 audit 當 bundle 內步驟或免費 lead magnet（AS010, AS011, AS015, AS027, AS030） | 24 | 55% | — |

結論：**「約 18/39」可重現為 36–43%（去重 44 分母），上限 55%**，BASELINE 的 46% 屬區間內但偏高（分母較小）。重要偏誤：樣本是以 audit/assessment/fixed price/fractional 為搜尋關鍵字挑出的（11 號檔自述），所以這是**關鍵字選擇的結果，不是市場普遍度**。另其中標價可見者只有 11 列，其餘 5–8 列的 audit 價格是 UNKNOWN。

### 3.4 重算：audit/diagnostic 入口價（幣別分開）

解析規則：取 `public_price`（必要時對照 `service`）中**明示為 audit/diagnostic/feasibility/review 之獨立入口**的金額；區間取下限；USD 以外幣別不併入。

**Solo（全部 USD，去重，n=10，不含離群值）**：45（AS025）、75（AS016）、150（AS005）、350（AS017）、499（AS020）、750（AS035）、997（AS008）、1,500（AS019）、2,500（AS018）、4,500（AS014）。
- 中位數 **624.5**；Q1 200；Q3 1,374。→ BASELINE 的「US$500–750」**可重現**（中位落在第 5、6 個值 499 與 750 之間）。
- 其中 5/10 ≤ US$500（50%）。
- **敏感度**：納入離群 AS002（80,000）n=11 → 中位 750；AS016 改用 feasibility 900 → 中位 825；加入 AS006 的 95 元諮詢 → 中位 499。故**合理區間是 US$499–825，不是穩定的「500–750」**，且每個值都是 asking price，n 很小。
- 另有 solo 價格未算入：AS002 audit USD 80,000（企業定位離群）。

**公司/boutique（USD，去重，n=11）**：50、197、500、2,000、3,500、3,950、4,950、5,000、7,500、8,000、12,500 → 中位 **3,950**；Q1 1,250；Q3 6,250。僅公司（n=8）中位 4,975（Q1 3,838；Q3 7,625）。
- 排除（幣別/定義不同）：AC032 INR 25K–50K；AC037 AUD 12,000；AC007 BD 250（幣別不明）；AC018「$1,700 ex GST」（澳洲，幣別 CSV 標 USD 但未證實）；AS047 與 AC001 重複；AS014 與 AC010 重複。
- **含義**：公司/boutique 與 solo 的入口價中位相差約 6–8 倍（624 vs 3,950），但 boutique 內也有 US$50–500 的 audit（AS044、AS045、AS046），價帶並不乾淨分層。

### 3.5 其他供給端陳述核對

- **「折抵後續」**：BASELINE 說 3 家公司折抵 + solo 4。我重數：公司/boutique 5（AC001、AC006、AC032、AS041、AS048）+ solo 4（AS001、AS018、AS020、AS035）；AS017 未答。**BASELINE 低估公司端折抵（3→5）。**
- **「沒有 solo 賣 MongoDB」**：96 列所有欄位 grep `mongo` = **0 列**（連公司列也無）。陳述為真，但**資訊量低**：這個資料集的搜尋不是以 MongoDB 為關鍵字，沒有出現不代表市場缺口（11 號檔自己也這麼說）。MongoDB 結論不能由此資料集支持或推翻。

## 4. 三個 Phase 1B 推論的檢驗

### (a) 低價市集證據在排名中被過度加權？ — **不成立（原假說），但有更準確的風險**

證據（我用 02/06 資料重算 Buyer breadth，門檻 H≥45、M 15–44、L<15）：

| product_mapping | pain+hiring | freelance 全部 | Buyer（BASELINE） | 排除 UNVERIFIED 與 2 列賣家宣傳後的 freelance | Buyer（調整後） |
|---|---|---|---|---|---|
| workflow-automation | 21 | 25 | 46 H | 16 | 37 M |
| sales-backoffice | 21 | 18 | 39 M | 14 | 35 M |
| support-automation | 20 | 15 | 35 M | 13 | 33 M |
| assessment | 1 | 4 | 5 L | 3 | 4 L |

- 只有 workflow 的 Buyer 等級由 H 掉到 M；**Top 5 的排序不是由 freelance 計數決定**（#1 assessment 在自己的表上 Purchase=L、Buyer=L、競爭=H，仍排第一，是「結構」推論）。低價市集主要出現在「競爭/商品化」與「預算可見度」兩欄，方向是**扣分**而不是加分。
- 因此「低價市集被過度加權導致排名失真」站不住。
- **更準確的風險（INFERENCE）**：(1) Buyer breadth 的大宗是論壇 pain 列（C 級：n8n 76、Make 31、HN 21），不是市集；(2) Freelancer 預算是平台預設級距，12 號檔以其「中位」當價格證據是人為產物；(3) 真正推動 #1 的是**供給端 asking price 與賣家敘事**（provider_marketing），而它同時是 41% 賣家擠進的入口、價格 US$45–4,500。
- 信心：中（對「排序不受影響」高；對「市集價格作為價格證據的可靠度」高：不可靠）。

### (b) Assessment 需求弱於 implementation？ — **成立（方向），但市集結構性偏向 implementation**

計數（BASELINE 分類，NEW EVIDENCE 重算；未做我的修正，因為修正只會讓 assessment 更少）：

| 資料 | assessment 形狀 | implementation 形狀 | 其他 |
|---|---|---|---|
| Freelance 137 列 | **4（2.9%）**：AF048、AG016（US$15 的 30 分鐘諮詢）、AG033、AG034（PRO360）；加 AG035、AF018 的顧問性質最多 6（4.4%） | **101（74%）**：workflow 25、sales-backoffice 18、agent 15、support 15、rag 11、ai-api 6、internal-assistant 4、ops-copilot 4、doc 3 | other/none/eval/data 32 |
| 台灣 PCC 105 筆（公部門） | 11 評估/研究 + 6 PoC/pilot + 2 PoC/可行性 = 19（18%） | 63 實作 + 21 維運 = 84（80%） | PM/QA 2 |
| 14_AI_DB_EVIDENCE 81 列 | 3 | 22 | 50 為 title-only UNKNOWN |

- 我的抽樣中 4 列 assessment 有 1 列（AF048）經檢視屬「策略 + 訓練」，非 workflow 評估；所以 freelance 端 assessment 形狀約 3–4 列。
- **對抗證據**：PRO360（台灣私人小額需求）6 列中 3 列為「AI 顧問/導入」顧問形狀（AG033、AG034、AG035），但**無預算、無成交**，n=6。
- **解讀限制**：市集是「貼任務找人做」的結構，評估通常透過顧問直銷/關係成交，市集天然低估；且抓取關鍵字是否含 assessment 字樣，方法檔未記錄（UNKNOWN）。所以只能說「在可觀察的公開需求中，implementation 形狀約 25 倍於 assessment」，**不能說私人市場不買 assessment**。這也代表 BASELINE 把 assessment 排 #1 的理由純靠供給端結構，與需求端證據反向（BASELINE 已自述，我同意）。
- 信心：方向高、幅度低。

### (c) 台灣公部門證據被外推到私人 SMB？ — **部分成立：文字已設限，但兩處論述仍外推**

- 事實：126 列購買證據全為公部門（台灣 105 + 美國 21），私人買家購買證據 0。BASELINE 在多處明講「不可推論私人市場」。
- 仍外推的兩處：
  1. **「個人可及規模」**：16 號檔與 08 號檔以「105 筆中 31 筆 ≤TWD 1.5M」支持 assessment/PoC 可由個人承接。我重查這 31 筆：**投標家數已知者 22 筆中 15 筆僅 1 家**（約 68%）；採購方式為「公開取得報價單或企劃書」15、公開取得電子報價單 1、限制性招標 7、UNKNOWN 8。≤1.5M 的 assessment/PoC/pilot 類 8 筆（AH075、077、079、081、083、086、089、104）買方為國營銀行、大學、研究機構、中央/地方機關，**沒有任何私人買方，個人資格 UNKNOWN**。
  2. **#2 Support Automation「購買證據較強」**：Support H(28)、Internal assistant H(33) 兩欄 100% 來自公部門；用它排序等於把「公部門買」當作「SMB 會買」。
- 信心：高（對「資料本身不含私人買家」）。

## 5. 修正後的關鍵數字（建議取代 BASELINE 引用）

1. Freelance 需求列有效性：抽樣中可判定者 **41% 已死/已結案**（PPH 全 26 列僅 38% 仍開放）；mapping 錯 **31%**（CI 19–48）；預算抄錯 7%（可核對者）。**需求列計數應排除賣家宣傳、招募聚合、已 Awarded/Expired 列後再用**。
2. Solo audit 入口：**36–43%（分母 44）**，不是 18/39 的 46% 一個點估計；入口價中位 **US$499–825（n=10）**，一半 ≤US$500。
3. 價格可見度：「47%」只屬 AC 系列（含 2 列 independent）；全資料集 52%，solo 55%。
4. 折抵：公司/boutique 5 家、solo 4 家（BASELINE 公司端 3 家低估）。
5. 資料集含 2 組重複供應商（M&M、Outright Mental）與 4 組同公司多列。

## 6. 對 Phase 2 的含義（INFERENCE）

- 不要用市集預算或 solo asking price 當 assessment 定價依據；assessment 價格證據仍只有 provider 標價。
- Assessment 的「需求面」最弱，下一步最有價值的是**私人買方的成交證據**（BASELINE 缺口），而不是更多市集列。
- PPH 有 6 列 Awarded（含 2 列 PRE-FUNDED）：屬 marketplace_completed 類弱證據（award ≠ 付款，金額 US$100–660），可作為 Phase 2 私人買方表的候選，但**金額太小，不代表 assessment 或 PoC 的價格**。

## 7. 檔案

- `research/phase2_validation/01_audit_freelance_sample.csv`（35 列）
- `research/phase2_validation/01_audit_supplier_sample.csv`（25 列）
- `research/phase2_validation/_sources/audit2.csv`
