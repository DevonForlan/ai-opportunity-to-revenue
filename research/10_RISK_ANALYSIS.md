# 10 Risk Analysis（非法律/稅務意見）

| 風險 | 等級 | 證據狀態 |
|---|---|---|
| 自動投標/申請（Upwork/Freelancer/Fiverr ToS） | **HIGH** | ToS 未取得（403/未查）→ UNVERIFIED；預設禁止 |
| 平台 scraping（Upwork 403 即反爬） | HIGH | Upwork 403 VERIFIED（觀察）；ToS UNVERIFIED |
| 帳號自動化/CAPTCHA | HIGH | 不得繞過 |
| GitHub bounty 收款（Opire claim 不自動付款） | HIGH | Opire docs（A） |
| Algora/Gitcoin/Bountysource 平台萎縮 | HIGH | 04/03；Algora 關閉與否 UNKNOWN |
| Bounty label 與實付不符（glances#3485 $1k 標示、實付 $1） | HIGH | 外部留言（C），單案 |
| Taiwan 收款（自開 Stripe Taiwan） | MEDIUM | UNVERIFIED；Polar/Contra 官方列有台灣 |
| Taiwan 稅：服務在台執行可能為台灣來源所得，NT$100 萬海外所得門檻可能不適用 | MEDIUM–HIGH | 所得法§8(3)（A）；所得類別 UNKNOWN → 需會計師 |
| 雇主兼職/利益衝突/NDA（用戶僱傭合約內容） | **UNKNOWN→必查** | 未見合約 |
| 客戶機密與 AI 工具（組織政策禁止上傳機密/個資） | HIGH | WebComm 組織政策：不得輸入客戶資料；案件資料不可餵 AI 前需確認 |
| 開源授權/著作權 | LOW–MEDIUM | 逐案 |
| AI spam 聲譽（maintainer 反感） | MEDIUM | onyx#2281 現象 |
| 加密貨幣收款（USDC）會計 | MEDIUM | UNKNOWN |

**最優先要先釐清**：(1) 雇主兼職規定；(2) 稅務類別與是否需開立收據；(3) 組織 AI 使用政策與客戶資料。
