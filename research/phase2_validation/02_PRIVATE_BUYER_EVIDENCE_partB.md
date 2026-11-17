# Phase 2 — 私人買家商業證據 Part B（marketplace / SEC / 台灣私立機構標案）

日期：2026-11-17　資料集：`03_PRIVATE_BUYER_DATASET_partB.csv`（PB001–PB037）　來源：`_sources/private_buyer_b.csv`

## 0. 方法與限制（先讀）

**方法**：以公開、免登入的結構化來源取代搜尋引擎摘要——(1) Freelancer.com 公開 API（closed 專案搜尋 + 專案 review 的 `paid_amount` 欄位）；(2) SEC EDGAR 全文搜尋 + 直接閱讀 8-K Item 1.01；(3) 台灣政府電子採購網決標公告（g0v/openfun 公開 API 鏡像），篩出法律型態為私立學校/醫療財團法人/財團法人的買方。未登入、未繞過 401/403/CAPTCHA、未聯絡任何人、未執行第三方程式碼。

**筆數**：共 37 列，**全部為真實 URL 且已實際讀取**；`VERIFIED` 11 列、`PARTIALLY VERIFIED` 26 列；`contract_value_public` 11 列、`marketplace_completed` 26 列；`named_client_case_study` / `partner_story` / `provider_claim_only` / `testimonial_only` 為 0（刻意不收）。未達 Part A+B 合計 40 的要求之處由 Part A 補足；我方達成 ≥25 目標（37）。

**最重要的限制（INFERENCE，請勿誤讀）**：
1. 11 列 `contract_value_public` **沒有任何一列**是「私人預算自掏腰包向小型供應商購買 AI 自動化服務」。2 列 SEC 是美元百萬級、對手為開發公司/上市公司；9 列台灣標案的買方雖為私立法律型態，**資金幾乎全部是政府補助**（衛福部「健康台灣深耕計畫」、教育部、農業部）。
2. 26 列 marketplace 是真實付款（平台記錄 `paid_amount`）但為**低單價**（中位數約 USD 108，最高 USD 1,200），雇主身分（企業/個人）多半無法確認，review 可被灌水。
3. 頻道 (4)(5)（創辦人「我付 $X 給某承包商」貼文：HN/IH/Reddit）與 TWSE 重大訊息：**零列**，原因見 §5。

## 1. 各頻道證據天花板

| 頻道 | 列數 | commercial_evidence_type | 天花板 | 最高可支持的主張 |
|---|---|---|---|---|
| SEC 8-K | 2 | contract_value_public (A) | 簽約承諾而非已付款；金額 USD 3M / 6.5M；買方為微型上市公司或轉售商；Qintess 案含給買方的股權誘因 | 「有私人公司簽下 AI agent / agentic AI 服務合約」——與 solo 顧問定價無關 |
| 台灣標案（私立形式買方） | 9 | contract_value_public (A) | 買方私立但**經費為公帑**；多為設備/授權；供應商為 SME 公司 | 「私立醫院/大學的 AI 專案在公開決標公告留有金額」；**不可**當作私人預算願付證據 |
| Freelancer.com | 26 | marketplace_completed (C) | 付款金額為平台記錄；雇主類型多為 unknown；小額；review 可被操縱；Freelancer 非 solo 顧問的目標市場 | 「AI 自動化/聊天機器人/RAG 小案在該平台有已完成且付款的交易，典型 USD 20–500」 |
| HN / IH / Reddit | 0 | — | 搜尋只回傳廠商定價文章；HN Algolia 4 次查詢無第一人稱付款貼文；Reddit 未嘗試（不得繞過限制） | UNKNOWN |
| TWSE/MOPS 重大訊息 | 0 | — | mops.twse.com.tw 為 POST/JS；openapi 只回傳當日公告；未找到 AI 合約 | UNKNOWN |
| Fiverr / PeoplePerHour / Freelancehunt / Upwork 公開頁 | 0 | — | Freelancehunt 403；PPH 範例為過期未決標；Fiverr/Upwork 為 gig/job 列表（非完成交易） | 不使用 |

## 2. SEC 8-K（2 列，VERIFIED / A）

- **PB001 INNO Holdings**（Nasdaq: INHD，美國德州，二手手機業務）與香港 AI 服務商簽 Development Services Agreement，**USD 3.0M**，五期里程碑付款、驗收制、2026-06-08 至 2027-05-31，買方擁有全部 IP、可 10 天通知終止。公司自述專案「早期開發、尚未部署」。URL: https://www.sec.gov/Archives/edgar/data/1961847/000149315226028058/form8-k.htm
- **PB002 Qintess（巴西 IT 服務公司）× Fusemachines**：MSA 最低採購承諾 **USD 6.5M / 3 年**，涵蓋 agentic AI 產品、授權、實作與專業服務；Fusemachines 配發最多 1.25M 股給買方。URL: https://www.sec.gov/Archives/edgar/data/2033383/000149315226037251/form8-k.htm
- **NEW EVIDENCE**：這是 Phase 1 缺的「私人買方有簽約金額」的第一批 A 級列；**INFERENCE**：兩案規模、對手與條款結構（里程碑驗收、買方持有 IP；股權交換）可作為 PoC 合約條款參考，但不能外推價格。
- EDGAR 全文搜尋約 15 組查詢噪音大；小型私人公司不申報，故此頻道對 SMB 價格幾乎沒有覆蓋（結構性天花板）。

## 3. 台灣私立法律型態買方標案（9 列，VERIFIED / A，需附註補助來源）

| ID | 買方（法律型態） | 標案 | 得標金額 (TWD) | 補助 |
|---|---|---|---|---|
| PB006 | 醫療財團法人羅許基金會羅東博愛醫院 | 導入生成式AI優化醫護病歷撰寫（勞務類842） | 8,950,000 | 衛福部 9,000,000（100%） |
| PB003 | 中國醫藥大學附設醫院 | 生成式AI語音智慧醫療紀錄系統應用服務 | 3,600,000 | 衛福部（100%） |
| PB004 | 中國醫藥大學附設醫院 | 生成式AI衛教及照護機器人 | 2,238,750 | 衛福部（100%） |
| PB005 | 中國醫藥大學附設醫院 | 生成式AI照護機器人（設備租賃） | 28,750,000 | 衛福部 20,142,000（約59%） |
| PB007 | 財團法人農業科技研究院 | 農業跨域生成式AI支援應用系統規劃及設計 | 950,000 | 農業部（100%） |
| PB008 | 財團法人農業科技研究院 | 農業領域生成式AI數位化系統知識庫建立與擴充 | 1,296,750 | 公告未顯示 |
| PB009 | 臺北醫學大學 | 數位學習平台AI出題模組及知識庫系統 | 1,900,000 | 教育部 2,000,000 |
| PB010 | 中華大學 | 生成式AI平台使用儲值金與軟體資源建置 | 1,820,000 | 教育部（100%） |
| PB011 | 中華醫事科技大學 | 生成式AI虛擬人教案平台 | 414,000 | 教育部（100%） |

- **關鍵發現（NEW EVIDENCE）**：PB006 是與「AI workflow 專案」最接近的服務型決標（軟體執行服務、限制性招標經公開評選）；PB007→PB008 為同買方、同供應商（凌誠科技）的**規劃設計 → 知識庫擴充**接續案（INFERENCE：存在「小規劃案帶出實作案」的真實路徑，但為補助案）。
- **誠實分類**：買方 `buyer_is_private=yes` 僅指法律型態。農科院為政府捐助財團法人（準公部門），已在 buyer 欄註明。這 9 列與 Phase 0/1 的 126 列公部門證據性質高度相近，不應被計為「私人預算」證據。
- 另掃出但**未收**：僅有招標/報價公告而無決標的（嘉南藥理 TQC 題庫、文藻 AI AMAZE 三年授權 NT$900,000 預算）、純硬體（明新 GPU 設備 2.54M、亞東 GPU 工作站）、公立醫院/大學（臺大醫院新竹分院、臺北榮總、臺中教育大學 RAG 助理 NT$4.2–6.0M 等，屬公部門）、非 AI 的圖書館知識庫。

## 4. Freelancer.com 已完成且付款（26 列，PARTIALLY VERIFIED / C）

- 流程：10 組查詢 → 1,392 件 closed → 150 件 `closed_awarded` 且完成 → 其中 94 件 review 含 `paid_amount>0` → 手選 26 件 AI 自動化/聊天機器人/RAG/workflow 相關（排除成人內容、純網站/設計、一般 SaaS）。
- 付款分布（轉 USD 近似）：最小 ≈7、最大 1,200；26 件總計約 USD 6.3k；中位數約 USD 108；≥USD 500 者 4 件（PB013 AUD 1,500 ≈ USD 1,012；Healthcare chatbot USD 1,200；Zoho CRM/Recruit automation CAD 800 ≈ USD 559；AI agent workflow integration USD 500），另有 EUR 400 ≈ USD 440 一件。
- **PB013 Adelaide Pool Patrol**（澳洲泳池服務企業，專案文字具名）：ServiceM8 + n8n 自動化，AUD 1,500 已付、5 星 review——本批唯一「具名私人企業 + 付款金額 + 完成」的 workflow 自動化列，但為平台公開資料，非契約。
- **INFERENCE**：低單價市場（USD 20–500）由大量低價競標者定價（單案 100+ 投標），若以 solo 顧問高單價服務切入，不宜以此定價；但它證明「買方願意為 n8n/LLM/RAG 小案付款並完成」。
- 限制：bids 端點需登入（401，未繞過），故無法取得得標者身分/報價歷史；`paid_amount` 為平台欄位，非獨立稽核；雇主是企業或個人多半未知（僅 1 列 yes，其餘 unknown）。

## 5. 未能取得證據的頻道（誠實說明）

- **創辦人付款貼文（HN/Indie Hackers/Reddit）**：搜尋引擎回傳的皆是廠商定價指南（標為 marketing estimate，不採用）；HN Algolia 4 組查詢無符合貼文；Reddit 無公開免登入查詢途徑，依規則未嘗試繞過。結論：UNKNOWN，非「不存在」。
- **TWSE/MOPS 重大訊息**：MOPS 查詢為 POST/JS；TWSE openapi `t187ap04_L` 只暴露當日公告，無法搜尋歷史；網頁搜尋也未找到上市櫃公司 AI 專案採購合約公告（僅找到苗栗縣政府 × 群聯 AI 客服 MOU，無金額、公部門）。UNKNOWN。
- **Upwork / Fiverr / Contra / PeoplePerHour / n8n-Make-Zapier expert directories**：公開頁多為 gig 列表或過期職缺，不構成完成交易；Fiverr 搜尋摘要僅出現一則不理想的 USD 200–400 n8n 訂單負評（未擷取為列）。不使用。

## 6. 結論（供 Phase 2 決策）

1. **BASELINE 缺口只被部分填補**：已有 11 列帶金額的 A 級私人法律型態買方、26 列小額已付款 marketplace，但**尚無任何「台灣中小企業私人預算向 solo 顧問買 AI 自動化」的帶金額證據**。（NEW EVIDENCE + INFERENCE）
2. 台灣最有價值的新發現是**私立醫療/學校的 AI 決標是補助驅動**（衛福部健康台灣深耕計畫、教育部），供應商為 SME 級系統商——這是「補助型採購」通道，不是 SMB 自費通道。
3. Marketplace 證明小案存在但價格壓低；若走 Assessment 入門款，需在報價上靠「在地、中文、可開統編發票、驗收制」差異化，此為 INFERENCE，未經驗證。
4. 建議後續（需人類授權，本任務未做）：以訪談/試銷驗證私人買方，而非繼續網路檢索。

## 7. 資料品質檢核

- 去重：以 URL 去重，37 個 URL 皆不同。
- 無虛構列；Freelancer 供應商以「handle withheld」表示、雇主匿名（符合組織個資規範），僅具名企業（Adelaide Pool Patrol）出自專案公開文字。
- 金額欄 `contract_value_or_price` 為來源原始幣別；USD 近似值僅放在 notes/measurable_outcome，由平台 `price_usd` 欄位提供。
