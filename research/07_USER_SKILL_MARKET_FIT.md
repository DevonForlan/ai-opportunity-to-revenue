# 07 User Skill × Market Fit

> 評分為**定性判斷（1–5，5 最佳；Competition 5=競爭低）**，非量測數據。依據：05（Freelancer 抽樣 30 筆，多為低價）、04、02、Productized 服務公開價格。Upwork/Contra/Toptal 等需求量 **UNKNOWN**（403 / 未嘗試）。

| Skill | Market Demand | Typical Budget | Competition | AI Leverage | User Fit | Priority |
|---|---:|---|---:|---:|---:|---|
| MongoDB（health check / upgrade / 調校） | UNKNOWN（有公開付費服務：Percona 審計起價 $11,400、AVP $490，VERIFIED） | 高（顧問型） | 3 | 3（診斷腳本化，判斷仍需人） | 5 | **P1** |
| Database Migration | UNKNOWN | UNKNOWN | 3 | 4 | 5 | P1–P2（與 MongoDB 綁成同一服務線） |
| Data Engineering / ETL / Pipeline | 部分驗證（Freelancer 有案，價格偏低 $4–50/hr） | 低–中 | 2 | 4 | 5 | P2 |
| Kafka | 部分驗證（Confluent 論壇 1 筆 $90/hr，2026-04，已過 60 天） | 中–高但案少 | 4 | 3 | 5 | P2（利基） |
| Python Automation | 高量但低價（Freelancer） | 低 | 1 | 5 | 5 | P3（紅海，易被壓價） |
| API Integration | 有量 | 低–中 | 2 | 5 | 5 | P3 |
| AI Agent / Claude | 少量高價離群（1 筆 $5–10k） | 不穩定 | 2 | 5 | 5 | P2（機會型，非主力） |
| RAG | 有量；Fiverr 價 UNVERIFIED | 低–中 | 1 | 5 | 4 | P3 |
| MCP | UNKNOWN | UNKNOWN | UNKNOWN | 5 | 4 | UNKNOWN |

**結論**：AI 並非 ROI 最高處。AI Leverage 高的領域（Python 自動化、RAG、API）同時競爭最高、價格最低；用戶稀缺的深度技能（MongoDB/Kafka/DB migration）競爭較低、單價較高、公開有人買。**直接偏向 DB/Data 顧問型服務，AI 當作降低交付工時的工具**。限制：此判斷基於小樣本與定性評分，需以 30 天實驗驗證。
