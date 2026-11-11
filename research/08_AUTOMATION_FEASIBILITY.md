# 08 Automation Feasibility

Automation % 為**定性區間**（沒有實測資料；實驗中才量測）。🔒 = 必須人工授權（brief 第 34 條）。

| 階段 | Automation | Human Required | Risk |
|---|---|---|---|
| Opportunity discovery | 80–90%（公開 API/RSS 來源） | 設定來源 | 來源失效（Algora 已萎縮、Upwork 403） |
| Filtering | 70–80% | 校準規則 | 垃圾/農場帳號多（bounty 搜尋 ~72–87% 疑似 farm） |
| Verification | 40–60% | 付款證據需人工判讀 🔒 | 最關鍵、最難自動化 |
| Technical analysis | 70% | 審閱 | 低 |
| Effort estimation | 50% | 判斷 | 估不準 |
| ROI estimation | 60% | 輸入機率（無資料即 UNKNOWN） | 假精確 |
| Proposal generation | 80% | 審稿 | 平台反垃圾 |
| Coding / Testing / Docs | 60–80% | Review | 客戶環境差異 |
| PR generation | 70% | 🔒 對第三方發 PR | 反 AI spam 觀感（onyx#2281 10+ AI PR） |
| Submission / Application | 0%（建議） 🔒 | 全人工 | **帳號被停權（ToS 多數 UNVERIFIED）** |
| Client communication / Negotiation | ≤20% 🔒 | 人 | 信任 |
| Contract / Identity / Payment | 0% 🔒 | 人 | 法律/稅 |
| Revenue accounting | 70% | 確認入帳 | 低 |

**判斷**：自動化應止於「發現→驗證→評分→產出任務包」；之後 Human approval。全自動投遞不合理（ToS 風險 + 對外動作 + 低 conversion 證據）。
