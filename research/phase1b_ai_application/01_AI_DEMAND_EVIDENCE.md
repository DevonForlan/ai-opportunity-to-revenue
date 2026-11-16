# 01 AI Demand Evidence（索引與合併摘要）
合併資料集 `02_AI_DEMAND_DATASET.csv`（295 列 = hiring/purchase 140 + pain 155）。細節：`01_AI_DEMAND_EVIDENCE_hiring.md`、`01_AI_DEMAND_EVIDENCE_pain.md`；AI＋DB 另見 14。

| evidence_type | 列數 | 說明 |
|---|---:|---|
| purchase | 126 | 台灣 PCC 105（A，官方鏡像 API）＋USAspending 21（A）；**皆為公部門** |
| pain | 143 | n8n 社群 76、Make 31、HN 21、OpenAI 10、LangChain 5（C 級；多為標題＋API 摘要） |
| hiring | 25 | n8n 徵才 12、HN 11、RemoteOK 3 等 |
| provider_marketing | 1 | — |

重點：購買證據全為公部門；論壇 pain 36 列為明確付費求助（標題規則，未人工審）；預算只有 5 列有數字且偏低。限制見 15。
