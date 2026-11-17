# 02 Private Buyer Evidence（嚴格分級）

資料：`03_PRIVATE_BUYER_DATASET.csv`（93 列 = Part A 56 + Part B 37；新增欄位 `strict_tier`）。細節：`02_PRIVATE_BUYER_EVIDENCE_partA.md`、`..._partB.md`。台灣另見 05。

## 1. 先說結論（`NEW EVIDENCE`，且與 Issue 的目標有落差）
**目標 ≥40 筆「私人企業實際購買」：嚴格計算做不到。** 93 列看似超過門檻，但依嚴格定義（私人預算、有金額或可驗證的付款/完成、AI 自動化範圍），實際分佈如下，**天花板很低**：

| 嚴格分級 | 列數 | 驗證 | 說明 |
|---|---:|---|---|
| **T1** 真正私人買家、公開合約金額 | **2** | VERIFIED（SEC 8-K，A） | INNO Holdings US$3.0M（里程碑付款）、Qintess 最低 US$6.5M／3 年。皆為**承諾而非已付款**，且為百萬美元級，**遠超單人規模** |
| **T2** 得標金額可驗證，但買家雖為私法人**經費來自政府補助** | 9 | VERIFIED（A） | 醫院/大學/財團法人（例：羅東博愛醫院 NT$8.95M）。**不是私人預算需求，不得外推到 SMB** |
| **T3** Freelancer.com 公開評價顯示已付款金額的完成案 | 26 | PARTIALLY（C） | 雇主類型多半未知。USD 14 筆：**中位 US$100、最大 US$1,200、合計 US$3,175**；另有 INR/EUR/AUD/SGD/CAD/GBP。唯一具名企業：Adelaide Pool Patrol AUD 1,500 |
| **T3b** Clutch 客戶評價（只有成本區間） | 26 | PARTIALLY（C） | 區間不是金額：10 個 <US$10k、5 個 US$10–49.9k、1 個 US$50–199k |
| **T4** 具名客戶＋範圍＋供應商，**無價格** | 15（13 計入） | PARTIALLY | 13 筆由 BotsCrew（7）、Master of Code（2）等中型代理商提供；**無單人供應商**；成果多為供應商自述 |
| **T5** 供應商自述／夥伴故事 | 15 | UNVERIFIED／PARTIALLY | 不算購買 |

**「私人 SMB 付費給單人顧問、有明示價格的 AI 自動化」= 0 筆（VERIFIED）。** 最接近的是 T3：價格非常低（中位約 US$100）。

## 2. 各通路的證據天花板
- Founder 自述付款（HN、Indie Hackers、Reddit）：0 列（搜尋僅得供應商價目指南）。
- TWSE／MOPS 重大訊息：0 列（MOPS 為 POST/JS；公開 API 只有當日）。
- Fiverr、PeoplePerHour、Upwork：0 列（403／列表頁／已過期）。
- Freelancer.com bids 端點 401（未繞過）→ 得標者與出價歷史 UNKNOWN。
- EDGAR：小型私人公司不申報，幾乎無法涵蓋 SMB。
- 以上屬**公開資料的結構性上限**：真正的 SMB 合約多半不公開。這代表「再多搜尋」邊際效益很低；要降低此不確定性需要**直接與買家接觸**（需使用者授權）。

## 3. 負面資料點（保留，不淡化）
一個 Growwstacks 雜貨客戶回報準確率不到 50%（目標 98%），專案遠超兩週提案期（Part A）。→ 小型自動化案件的範圍與驗收風險真實存在。

## 4. 對決策的含義
1. 私人買家 purchase evidence 在公開資料裡**不會**達到「有說服力」程度 → 必須以 **獲客測試**取得（見 15）。
2. 單人尺度的可觀察成交價偏低（T3 中位約 US$100；台灣 Tasker 預算 NT$5k–100k，見 05）；高價（US$3.5k–12.5k）只出現在**供應商標價**，沒有任何成交證據。
3. 因此**定價假說必須誠實標示「錨點來自標價，成交未證」**（見 14）。
