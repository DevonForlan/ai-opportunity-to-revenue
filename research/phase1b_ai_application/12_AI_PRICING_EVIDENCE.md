# 12 AI Pricing Evidence

規則：只列觀察到的價格。**list price ≠ 成交價；job budget ≠ 成交價；RFP/得標金額 ≠ 個人可得價格**。來源：`04_AI_COMPETITOR_DATASET.csv`（96 列）、`02_AI_DEMAND_DATASET.csv`（公部門得標）、`06_AI_FREELANCE_SAMPLES.csv`（137 列）。幣別不換算。

## 1. 觀察到的價格（依客群）

| 客群 | 產品類型 | 觀察 | Evidence |
|---|---|---|---|
| 公司/boutique | Assessment / readiness | US$3.5k–8.5k（Main & Machine）、US$12.5k（WorkWise，**折抵 US$25k+ 後續**）、US$4.5k（Outright Mental）、US$3,950–4,950（IT Partner Copilot）、US$1,700 ex GST（Steadfast）、US$5k–15k（VibeFactory FAQ）、AUD 12k（SSW）、US$7.5k 起（ISO 42001 readiness）、US$8k–20k（Alian discovery） | VERIFIED（廠商自述頁） |
| 公司/boutique | PoC / Sprint | EUR 2,900（Pragma-Code n8n sprint）、US$9.5k（Outright Mental）、US$25–60k（Just Think AI）、GBP 8k–30k（Pixelfield PoC）、US$12k–45k（M&M sprint） | VERIFIED |
| 公司/agency | n8n/Make 建置 | US$3k–10k（GrowwStacks）、US$5k 起/4 workflows（Goodspeed） | VERIFIED |
| 公司 | Retainer | 約 US$1.5k–45k/月 | VERIFIED（廣泛區間） |
| Solo | 審計／診斷（入口） | US$45–5,000；約 18/39 賣家以此為入口；agent 手算中位約 US$500–750；例：US$197（getaiaudit）、US$499 折抵（Contra）、US$997（Zoll）、US$1,500+（Mann）、US$2,500–5,000（Willis） | VERIFIED（asking price，n≈18，agent 手算） |
| Solo | 固定價建置 | US$500–3,000（Contra）、US$3,000–7,500（Jester）、US$10,000 起（AI Architects） | VERIFIED |
| Solo | 月 retainer | US$1,800/3,400/6,400（8/16/32h，Vantage Point）、US$3,400（Contra）、US$5,000–9,000（Contra embedded）；2 賣家明確拒絕 retainer | VERIFIED |
| Solo | 時薪 | US$50/h 起（Contra）、極端值 US$1,000/h（fractional CAIO，80h 最低） | VERIFIED（離群值不代表市場） |
| 市集 | 固定價 | Freelancer 固定價級距中位 US$250–750（16 列 USD 固定價中 14 列上限 ≤US$800）；PeoplePerHour 固定價中位顯示 US$198（n=23）；Upwork 摘要 US$5–150（多為佔位）；Upwork catalog n8n 建置 US$130–1,450 | PARTIAL（級距/摘要） |
| 市集 | 時薪 | US$15–25/h（n=4）、US$50+/h（n=1） | PARTIAL |
| 市集 | RAG 客服助理（最高預算類，n=6） | US$50+/h、GBP 5–10k、US$1.5–3k | PARTIAL |
| Agency 轉包 | n8n | US$300–900 / workflow（n8n 徵才貼文） | C |
| 台灣公部門（**購買證據**，標題級；個人可否承接 UNKNOWN） | AI 應用得標（105 筆；TWD） | 最小 271,140；**中位 3,677,000**；最大 485,508,000；≤500k 11 筆、≤1M 21 筆、≤1.5M 31 筆、≤3M 45 筆、≤10M 97 筆 | A（官方資料，PCC 鏡像 API） |
| | 其中 assessment/研究類（11） | 中位 TWD 2.65M（950k–9.37M）；PoC/可行性類（2）TWD 0.85–1.45M | A（類別為依標題推論） |
| | 維運/擴充類（21） | 中位 TWD 2.93M | A |
| 美國聯邦（購買證據） | USAspending AI 相關（21） | 例：US$0.48M–2.9M | A |
| 台灣民間 | 供給側 | 4 家台灣賣家皆無公開價格；PRO360 AI 顧問需求無預算 | UNKNOWN |

## 2. Price clusters（INFERENCE）
- **Solo 入口審計：USD 45–5,000（中位約 500–750 asking）**：擁擠、低價、範圍差異大。
- **Boutique 評估：US$3.5k–12.5k**（多數可折抵後續）。
- **n8n/Make 建置：agency US$3k–10k；solo US$500–3,000；市集 US$130–1,450。**
- **Retainer：solo US$1.8k–9k/月；公司更高。**
- **台灣公部門 AI 案：TWD 0.27M 至數億，中位 3.68M**（不可與個人報價直接比較）。

## 3. Pricing hypotheses（待 pilot 驗證）
- H1：個人 assessment 若定位為「固定範圍、以流程結果命名、費用折抵 PoC」，比較帶為 US$1.5k–5k（對標 solo 上緣與 boutique 下緣）— **假說，不是可成交價**。
- H2：入口審計太便宜（US$45–500）會把定位拉向商品化；不宜降價競爭。
- H3：不要以 US$40–60k 或公部門得標額推估個人價格。

## 4. UNKNOWN
個人實際成交價；成交率；折扣；私人買家預算分佈；台灣民間顧問行情；任一價格是否有人實付。
