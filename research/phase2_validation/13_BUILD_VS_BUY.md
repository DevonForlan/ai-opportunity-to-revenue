# 13 Build vs Buy / Tooling

原則（Issue §9）：技術服務於 outcome；deterministic workflow 能解就不用 LLM；workflow 能解就不用 autonomous agent。

| 工具 | 適用 | 優點 | 風險／限制 | 判斷 |
|---|---|---|---|---|
| **Python（標準庫為主）** | 分流/擷取/評估/稽核/報告（本 PoC 已證明可行） | 可測試、可重跑、無鎖定、成本 $0、資料不外流 | 需自行維護；非技術客戶無法自行改 | **核心** |
| n8n（自架或雲端） | 客戶已用或需「看得到的流程」；連接 SaaS | 視覺化、連接器多、客戶好交接 | 版本升級與憑證管理；供給端市集價格低；雲端版資料外流評估 | **客戶要求時使用**（作為交付形式，不作內部核心） |
| Make / Zapier | 客戶既有環境 | 客戶熟悉 | 供應商鎖定、按操作計費、可觀測性弱；Zapier 夥伴計畫需自有網站與網域信箱（baseline） | 僅在客戶已訂閱時 |
| LangGraph / agent framework | 真的需要多步決策與工具呼叫的任務 | 彈性 | 本 PoC 場景**不需要**；增加不可預測性與評估成本 | **暫不採用**（無需求證據） |
| OpenAI / Anthropic API | 規則吃不到的語意分類、草稿潤飾 | 品質上限高 | **本輪未測**；客戶資料外送、成本、供應商條款（Anthropic 條款將 Outputs 歸 API 帳號持有人、禁轉售服務 — baseline）；公司政策禁止客戶資料入 Claude | **僅作為可替換 provider**，須先做評估與資料決策 |
| 本地/開源模型 | 資料不能外送的客戶 | 資料留在本地 | 品質、部署與維運成本 UNKNOWN | 保留為選項，未評估 |
| 向量 DB | RAG | — | 本 PoC 用詞彙檢索已夠；DB 是否必要無證據（AI+DB 買家證據=0） | **不採用**（先用檔案/SQLite 檢索） |
| 客戶既有 SaaS API（Gmail、Shopify、CRM） | 整合 | 客戶已有 | 需客戶授權、最小權限；PoC 用 mock | 上線階段 |

## 推薦 stack（第一版）
- **決定性 Python 核心**（分流、遮蔽、擷取、KB 檢索、稽核、評估）＋ **SQLite**。
- **可替換 `ModelProvider`**：預設規則；LLM provider 作為可選項，須在真實資料上先過評估閘門才啟用。
- **交付形式**：交付程式碼＋runbook＋評估集；若客戶要求視覺化工作流，才以 n8n 包裝連接器。
- 不採用：agent framework、向量 DB、多租戶 SaaS（無證據支持）。

## 風險
- vendor lock-in：低（Python＋SQLite）；若使用 n8n/Make/Zapier 則轉嫁至客戶環境。
- 成本：核心 $0；LLM/API 成本 UNKNOWN（未測）。
- 可觀測性：自建稽核鏈＋指標；長期維運工具 UNKNOWN。
