# 10 獨立顧問模式分析：信任訊號、定位、無品牌背書時的最低需求

## Method & limitations（方法與限制）
- 資料：`04_COMPETITOR_DATASET_independent.csv`（39 列：independent 32、boutique 7）。所有統計都是對這些列的計數，不是市場統計。
- **樣本不足聲明**：頁面實際讀到的獨立賣家只有 10 列（約 9 個 distinct 賣家）；其中真正有完整服務頁（價格、交付物、信任訊號）的獨立 solo 賣家只有 4 個（Contra MongoDB+Redis audit、ZephyrCode、Pine Street Analytics、Contra analytics audit）。另 22 列僅有搜尋摘要（Fiverr / Upwork / MentorCruise，頁面 403）。因此下面的「出現頻率」只能描述本樣本，**不能推論任何轉換率、勝率或成交機率（UNKNOWN）**。
- 全部證據為 provider_marketing；沒有任何 purchase 證據（沒有成交數、沒有付款資料）。價格是標價，不是成交價。
- 台灣/亞洲獨立顧問：搜尋沒找到公開服務頁（UNKNOWN，非不存在）。
- 隱私：依組織政策，provider 欄用平台 handle/品牌名，不記錄個人履歷。
- 標籤：BASELINE（Phase 0）本檔未重新驗證，不引用；以下為 NEW EVIDENCE 或 INFERENCE。

## 計數（來源 / evidence_type）
| 類別 | 列數 |
|---|---|
| 頁面已讀 獨立（Contra 5、Freelancer.com 2、個人網站 3 含 ZephyrCode 兩列） | 10 |
| 頁面已讀 boutique | 7 |
| 搜尋摘要 only：Upwork 9、Fiverr 12、MentorCruise 1 | 22 |
| evidence_type = provider_marketing | 39 / 39 |
| evidence_type = purchase / hiring / pain | 0 |

## 1. 定位模式（NEW EVIDENCE，來自頁面已讀列）
1. **固定價、短期、唯讀的「審計/拆解」**（5 列：I001 $1,800 起；I002 $7,500；I003 $1,200 triage；I004 價格未公開；I006 $1,200 起）。週期 1-2 週，存取需求多為 read-only，交付物為書面報告 + 優先順序清單 + （有的）walkthrough call。
2. **時薪/專案混合的「技能掛牌」**（I005 起價 $50/hr、I007 $25/hr、Freelancer.com 兩人 $15-$25/hr）：沒有產品化範圍、沒有審計方案，賣的是工時。價格明顯低於審計型。
3. **審計 -> 建置 -> 留任的階梯**（I002 稱審計後附 scoped build proposal，implementation 起價 $15k；I004 稱「Start with an audit」再接 Data Foundations 與 Fractional retainer）。審計是入口，收入來源是後續。
4. **付費診斷先行 / 可抵扣**：I003（$1,200 triage，30 天內訂審計可全額抵扣）；GenAI Data Solutions（paid discovery，30 天內續約抵扣，boutique）。這是唯一在樣本中明確出現「paid diagnostic first」的結構。
5. **市集 gig（搜尋摘要，PARTIAL）**：MongoDB 相關 gig 的標題集中在 query / aggregation 優化、schema；沒有看到 replica set、backup/restore 演練、upgrade readiness、oplog 風險的產品化 gig（INFERENCE：僅依標題/摘要，可能漏看）。

## 2. 信任訊號出現頻率（頁面已讀 solo/小型獨立賣家，n=8；排除 Freelancer.com 2 個純時薪 profile）
| 訊號 | 出現次數 | 說明 |
|---|---|---|
| 公開價格 | 6 / 8 | 僅 I004（Pine Street）與 I008（作品集貼文）未標價 |
| 第三方證照（產品證照如 MongoDB DBA） | 0 / 8 | 獨立賣家頁面都未列；3 家 boutique 有列（Database SPA、Mydbops、Delbridge）+ JusDB 稱「pursuing」 |
| 客戶 testimonial（頁面內） | 0 / 8 | 平台評論（Freelancer.com 894 / 1258 則）只出現在純時薪 profile |
| 具名客戶案例 | 0 / 8 | I001 有未具名的自述案例；I002 有「代表性」範例；boutique 僅 Mydbops 有 3 個具名案例 |
| 範例報告 / 範例 finding | 1 / 8 | 只有 ZephyrCode（含代表性 finding 與前後數字） |
| 公開技術內容 / GitHub / LinkedIn | 1 / 8 solo（ZephyrCode）；另 GenAI Data Solutions（boutique）有 MIT 開源工具 | |
| 唯讀存取承諾 | 3 / 8 明示（I001、I002、I003） | boutique 另有 Mydbops、JusDB（NDA + named read-only accounts） |
| 免費初談 | 1 / 8（I005 30 分鐘）；boutique 7 家中 5 家 | |
| 保證/限制條款 | 1 / 8（ZephyrCode「honest-verdict」：找不到問題就給清白報告，非退款） | |
| 自述資歷（年數/前雇主） | 5 / 8 | 全部為自述，未經第三方驗證 |

**解讀（INFERENCE）**：在本樣本中，獨立賣家最常見的信任替代物不是證照或 testimonial，而是「範圍/價格/存取方式寫清楚 + 自述資歷」；唯一的高價（$7,500）solo 賣家同時具備：範例 finding、公開 teardown、唯讀存取、誠實裁決條款、可抵扣的 triage。這只是單一個案的組合，不能說明這些元素「導致」成交。

## 3. 價格對照（僅頁面原文，標價≠成交價）
- 審計型固定價（頁面已讀）：$1,200 起（1 週 analytics）、$1,800 起（1 週 MongoDB+Redis）、$5,000（Dattell，10 小時/1 月）、$7,500（Kafka，2 週）、Sprint $10,000 起（Champlin，非 MongoDB 專屬）。
- 時薪（頁面已讀）：$15、$25、$25、$50/hr。
- 市集搜尋摘要（PARTIAL，未歸屬到單一頁面不使用）：$90（Upwork DB audit entry）、$399（疑為 Upwork pipeline audit，歸屬未確認）、MentorCruise 訂閱 $70-$290/月。
- 價格分散約 80 倍（$90 至 $7,500，$90 僅為搜尋摘要），顯示「audit」一詞在不同賣家的範圍差距極大；不可將中位數當作市場價。

## 4. 沒有 Percona / MongoDB Inc. 品牌時的「最低需求」（INFERENCE，非因果結論）
依本樣本中獨立賣家實際使用的元素（而非已證實有效的元素）：
1. 明確、有限的範圍 + 固定交付物清單（書面報告、優先序、walkthrough call）。
2. 明確存取邊界（read-only、不碰 production、NDA）— 樣本中 3 個 solo 明示。
3. 價格公開或至少價格區間 + 週期（6/8 公開）。
4. 一個「樣本 finding / 脫敏範例報告」取代案例（樣本中 solo 只有 1 個做到；Mydbops 提供脫敏樣本供索取）。
5. 公開技術證據（部落格、GitHub、teardown）取代品牌；證照在獨立賣家中 0/8 出現，因此**不是**本樣本的必要條件，但是否影響買家決策 UNKNOWN。
6. 低風險入口（paid triage 可抵扣，或免費 20-30 分鐘初談）。
7. 明確的後續路徑（審計 -> 實作 -> retainer）。

**未知（需另行取得 purchase 證據）**：這些元素是否提高成交率、買家是否為此付費、MongoDB 專屬審計的實際成交價、台灣市場的接受度。本檔沒有任何勝率或轉換率數據。

## 5. 與任務的關聯與缺口
- 唯一接近目標產品（MongoDB 遠端審計）的獨立賣家是 I001（$1,800 起），且頁面無評論；MongoDB 專屬的 Backup/Restore、Replication/Oplog、Upgrade readiness 獨立產品化方案在樣本中未出現（可能是空白，也可能是搜尋覆蓋不足）。
- 建議下一步（不在本任務範圍）：取得 purchase 類證據（例如公開 Upwork 合約紀錄、買家討論），再判斷價格帶。
