# 13 AI 服務獲客管道與 AI 專屬付款/稅務/法律補充（Phase 1B）

- access date：2026-11-16（brief 要求 2026-11-18 以後；本環境日期為 2026-11-16，如需對齊請人工複核）
- 標籤：VERIFIED / PARTIALLY VERIFIED / UNVERIFIED / UNKNOWN；證據等級 A=官方、B=高可信第二手、C=社群/弱；結論標 BASELINE / NEW EVIDENCE / INFERENCE。
- **不是法律、稅務或財務建議（not legal advice）**；依 WebComm 政策須人工複核，不得視為正式文件。

## 0. Method & limitations

- 工具：WebFetch（回傳為小模型摘要，非原文逐字；「」或引號內短句為摘要引述，上線前須對照原文）、WebSearch。未登入、未建帳號、未聯絡任何人、未接受條款、未繞過任何阻擋。
- BASELINE：`research/phase1_productization/12_ACQUISITION_CHANNELS.md`（管道結構、LinkedIn/HN/GitHub/Contra/Freelancer ToS 自動化條款）與 `13_TAIWAN_PAYMENT_TAX.md`（收款、營業稅 §7(2)、起徵點、二代健保）**不重做**；本檔只擴充 AI 專屬面向與官方夥伴計畫。
- 403/不可讀：Upwork（support / legal）、Fiverr 兩篇 AI 官方 help（`37333301560593`、`37333179414289`、`34998793899665`）、OpenAI（Business Terms、business-data、Services Agreement、Partner Network 官方頁）、Make `/terms-of-use` 404、Zapier `/partnerships/experts` 404、TIPO PDF（二進位，工具無法解析）。替代：搜尋摘要與鏡像頁，**一律 UNVERIFIED**。特別提醒：Upwork「Ethics of AI」內容僅取得非官方網域（z3n-cab-workshop-2.zendesk.com，疑為測試/鏡像站）的文字，證據等級降為 C。
- 未取得任何成交率、得標率、收入數字；平台費用僅引官方文字，否則 UNKNOWN 或標 C。
- 計數：管道/計畫列 24 列（見 §1）；來源 CSV `_sources/ai_channels.csv` 共 34 列，其中實際讀到官方原頁（A，經摘要）約 17 列，其餘為 403+搜尋摘要或 C 級。
  - 依證據等級：A 約 17／A-B 混合 7／C 約 10。
  - 依 verification：管道欄位之官方條款 VERIFIED（摘要層級）= Contra、AWS Marketplace、n8n、Make、Zapier、Anthropic CPN；UNVERIFIED = Upwork、Fiverr、OpenAI、Google Cloud、Reddit。
  - evidence_type 以 provider_marketing / policy 為主，**無 purchase**。

## 1. 管道比較總表

欄位：買家證據＝該管道上是否可觀測 AI 工作需求（hiring/provider_marketing，非 purchase）；價格＝價格可見度；TW＝Taiwan 資格；solo＝solo 契合度（[INF]=推論）。

| # | 管道 | 買家證據（AI） | 價格可見度 | 競爭 | TW 資格 | 收款 | 官方費用 | ToS：自動化/AI 提案/爬取（短引） | 信任門檻 | solo 契合 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Upwork | NEW EVIDENCE：官方有 AI Agent Developers 行銷頁與 2023 AI Services hub（provider_marketing；搜尋出現多筆 AI agent/RAG/n8n 職缺 = hiring，C/A 混合，未逐筆驗證） | 公開 job 預算（hiring），成交價 UNKNOWN | 高 [INF] | UNKNOWN（官方 403） | UNVERIFIED（BASELINE） | 第二手 0–15% 依合約，自 2025-05-01（C，與 BASELINE 一致，UNVERIFIED） | 官方 403。鏡像文字（C）：「Always disclose to clients whether you use AI-generated content or tools」；第二手稱 ToS 預設允許 AI 工具除非客戶明示限制（C）。**無證實的全面禁止** | 新帳號高 | 中 [INF]：fixed-price 可做，但低價競爭 |
| 2 | Contra | UNKNOWN（有 hire 頁，buyer 證據 UNKNOWN） | 依 profile | 中 [INF] | PARTIALLY VERIFIED（BASELINE：180+ 國，未點名 Taiwan） | BASELINE | 0% commission（BASELINE，A） | **NEW EVIDENCE（A，摘要）**：ToS 有「Indy AI」章節：「Users are responsible for ensuring their use of AI generated content does not infringe on any third party rights」；仍禁「spiders, robots, crawlers, data mining tools」與用「automated tools」規避外聯上限；Indy AI 禁 "using bots or scripts"。未見禁止 AI 撰寫提案 | 中高 | 中 [INF]；ToS §2 禁免費試做（BASELINE） |
| 3 | Fiverr | UNKNOWN（官方 AI 頁 403） | gig 價公開（provider_marketing） | 高 [INF] | UNKNOWN | UNVERIFIED | 第二手 20%（C，UNVERIFIED） | 官方 AI 頁 403。搜尋摘要（C）：允許 AI 跨類別使用，須「ethical, legal, transparent」，需持有交付物權利，不得大量重複產出，違規可能永久停權。揭露義務：來源互相矛盾 → UNKNOWN | 高 | 中低 [INF] |
| 4 | Freelancer.com | UNKNOWN | job 預算公開 | 高 | UNKNOWN | BASELINE | UNKNOWN（BASELINE） | BASELINE：§33 禁機器人/scraper；AI 條款未讀 | 高 | 低 [INF] |
| 5 | PeoplePerHour | **未研究到足夠資料** → UNKNOWN（本次未取得官方頁） | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |
| 6 | Arc / Toptal / Lemon.io | provider_marketing；Arc 有 Taiwan 專頁（`arc.dev/en-tw/hire-developers`，搜尋顯示 Taiwan 時區開發者，A/B）；Toptal 通過率「約 3%」僅第二手（C）；Lemon.io 對 Taiwan 無官方陳述 | 費率由平台/成員設定，UNKNOWN | 篩選門檻本身即競爭 | Arc：Taiwan 開發者出現於其頁面（PARTIALLY VERIFIED）；Toptal/Lemon：UNKNOWN（BASELINE 同） | BASELINE | UNKNOWN | UNKNOWN | 高（多階段審核，BASELINE） | 低 [INF]：時薪派遣，非 productized |
| 7 | LinkedIn（人工） | UNKNOWN | 無 | 中 | 開放 | — | 免費 | BASELINE（A）：§8.2 禁 scripts/robots 爬取 | 中 | 中高 [INF] |
| 8 | Reddit | pain 研究用 | 無 | — | 開放 | — | — | UNVERIFIED（BASELINE 403） | 低-中 | 低 [INF] |
| 9 | Hacker News | pain/hiring 觀測（Algolia，屬 DEMAND dataset） | 無 | — | 開放 | — | — | BASELINE（A）：「Please don't use HN primarily for promotion」「Please don't put generated text in HN posts」 | 低 | 低 [INF]，僅內容 |
| 10 | GitHub | 信任證據 | 無 | — | 開放 | — | 免費 | BASELINE（A）§H 禁以 API 蒐集資料做 spam | 低-中 | 中 [INF]（作信任證據） |
| 11 | **n8n Experts** | provider_marketing | 不公開 | — | **NEW EVIDENCE（A，摘要）：closed pilot；要求「Already implement services with n8n」「Have at least 3 active n8n customers」「Are active n8n community members」；地區限定 UK、Ireland、Northern Europe、North America → Taiwan 不在所列地區（INFERENCE：目前不符資格）；對象為「agencies and system integrators」，solo 資格頁面未述** | — | 頁面未提費用（UNKNOWN） | 無讀到自動化條款；申請採 Typeform waitlist | 中（需 3 個客戶） | 低 [INF] |
| 12 | **Make Solution Partner** | provider_marketing | — | — | 頁面未述地理限制（UNKNOWN） | — | 官方：「completely free for qualifying applicants」；3 tier（Silver/Gold/Platinum）有 Make 派 leads；需「Experience in providing automation services」、至少 1 名 automation expert、必修訓練與認證、onboarding 最長約 2 個月 | — | 中 | 中 [INF]：對象「agencies and consultants」，solo 是否可：UNKNOWN |
| 13 | **Zapier Solution Partner**（原 Experts） | provider_marketing | — | — | 條件：不得居住於或隸屬於被美國制裁國家；Taiwan 未被點名（PARTIALLY VERIFIED） | — | 頁面未列費用；有 referral commission 說明 | 申請需「active business website」且「We do not accept applications that rely solely on third-party profiles」；須 custom-domain email；開放狀態 UNKNOWN（社群貼文稱曾暫停，未註明日期，C） | 中 | 中 [INF]：需自有網站與網域 email，solo 可行但需自建公司品牌 |
| 14 | **Microsoft AI Cloud Partner Program** | provider_marketing | — | — | UNKNOWN；Taiwan 發票需聯絡 support 並提供統編（A，搜尋摘要） | — | A：Services 方案 Partner Launch $350、Core $925、Expanded $4,125、Solutions Partner designation $4,875（USD，頁面更新 2026-06-25） | — | 高（需企業驗證：company name/address） | 低 [INF]：成本相對無案源保證；solo/sole proprietor 資格 UNKNOWN |
| 15 | **Anthropic Claude Partner Network** | provider_marketing | — | — | A：「Any organization that is bringing Claude to market is eligible」；會員「free of charge」；頁面未列地區限制；**單位為 organization，個人是否可加入未述**；CPNA 前言稱個人若「lawfully able to enter into contracts」可接受協議，並須經 Anthropic 書面核准（A.1，核准屬 Anthropic 裁量）；Program fee 另見 Partner Program Guide（未讀） | — | 免費加入 | CPNA C.4：Program 不授權 resale/sublicense Anthropic Services | 高 | 見 §2 |
| 16 | **OpenAI Partner Network**（2026-06 發布，C/B） | provider_marketing | — | — | **UNKNOWN**：官方頁 403；二手稱 Select/Advanced/Elite 三層、US$150M 投資、目標 300,000 certified consultants（目標非現況）；未見個人資格與費用（C） | — | UNKNOWN（二手稱無公開報名費，C） | — | UNKNOWN | UNKNOWN |
| 17 | **AWS Partner Network / Marketplace** | provider_marketing | — | — | **NEW EVIDENCE（A）：AWS Marketplace 付費產品賣家須為「permanent resident or citizen in an eligible jurisdiction, or a business entity organized or incorporated in one」；官方名單（澳洲、巴林、哥倫比亞、EU、香港、印度、以色列、日本、紐西蘭、挪威、卡達、南韓、瑞士、UAE、英國、美國）不含 Taiwan → Taiwan 個人無法直接作為 Marketplace 付費賣家（VERIFIED：名單未列；須銀行帳戶於 eligible jurisdiction 收 USD）** | 須 USD 銀行帳戶（eligible jurisdiction） | Partner Central 註冊需「Legal authority to register on behalf of your company」+ paid AWS account（A）；APN 年費 USD 2,500（Select/Advanced/Premier，搜尋摘要，UNVERIFIED） | — | 高 | 低 [INF]；免費產品與 Partner Central 註冊另論 |
| 18 | **Google Cloud Partner Advantage** | provider_marketing | — | — | UNKNOWN（Taiwan 與 Marketplace 賣家規則未找到） | — | UNKNOWN | — | 高（組織名義、需有權簽協議） | 低 [INF] |
| 19 | 個人網站 / SEO | 自有 | 自訂 | — | 不受限 | 自選 | 網站成本 UNKNOWN | 無平台 ToS | 高（冷啟動）| 高 [INF]（BASELINE 一致） |
| 20 | 技術內容 | 自有 | — | — | 不受限 | — | — | 發布平台各自條款；HN 禁生成文字（A） | 中 | 中高 [INF] |
| 21 | 轉介 | 取決於關係 | 自訂 | — | 不受限 | 自選 | — | — | 低 | 高 [INF]；現有轉介來源 UNKNOWN |
| 22 | Taiwan B2B 本地 | UNKNOWN | UNKNOWN | — | 是 | TWD [INF] | 本地接案平台：Tasker 第二手 12%/6%（接案者/案主）或 9%，兩說互相矛盾（C，UNVERIFIED）；104 外包網確切費率 UNKNOWN | — | 中 | 中 [INF]；AI 需求證據在 DEMAND dataset |
| 23 | 專業人脈 | 取決於 | — | — | 是 | — | — | — | 低-中 | 中 [INF] |
| 24 | 分包給 agency/SI | UNKNOWN | 議價 | — | 不受限 | 合約 | — | 須自行確認 NDA/IP | 中 | 中 [INF]：可借信任，需有人願意分包，準則公開資訊不足，須主動聯絡才能知道（依規則不聯絡） |

PeoplePerHour、Google Cloud 與 OpenAI 官方頁因讀取失敗，欄位多為 UNKNOWN；此為研究限制，不代表該管道不可行。

## 2. 個人（solo）能否取得官方 AI 夥伴身分

| 計畫 | 最低門檻（官方） | solo 可達？ | 標籤 |
|---|---|---|---|
| Anthropic CPN（加入） | 任何「organization bringing Claude to market」；免費；需 Hub 申請與書面核准 | 個人是否算 organization：UNKNOWN；CPNA 條文未要求法人 | PARTIALLY VERIFIED |
| Anthropic Services Track（tier） | Select：10 位 active certified individuals、2 個 12 個月內 production 聯合客戶、1 則公開客戶案例；證書屬個人 | **solo 不可能達到 Select（需 10 人）**；僅能加入網絡、考個人認證（INFERENCE；證書是否對個人開放：頁面述「belong to individual people」，但報考資格 UNKNOWN） | NEW EVIDENCE（A，摘要）/ INFERENCE |
| OpenAI Partner Network | 官方頁 403；二手稱 Select/Advanced/Elite | UNKNOWN | UNVERIFIED |
| Microsoft | 付費方案 USD 350 起；企業驗證 | UNKNOWN（成本高於案源證據） | PARTIALLY VERIFIED |
| AWS | Partner Central 以公司為單位；Marketplace 付費賣家須 eligible jurisdiction（無 Taiwan） | Taiwan 個人：Marketplace 不可（VERIFIED：名單） | NEW EVIDENCE |
| n8n / Make / Zapier | n8n：3 客戶＋區域限定；Make：服務經驗＋認證；Zapier：自有網站＋網域 email | n8n 區域不含 Taiwan（INFERENCE）；Make/Zapier：solo 可能但頁面未明說 | NEW EVIDENCE |

**INFERENCE**：官方夥伴生態系大多假設「公司＋既有客戶案例」。對尚無客戶案例的 solo，這些屬於**第二階段**（先有 2–3 個公開案例後再申請）而非冷啟動管道；本結論無成效數據支持。

## 3. AI 專屬規則（NEW EVIDENCE，對 BASELINE 的補充）

1. **Contra**：ToS 明列 Indy AI 與 AI 內容責任條款（A，摘要）；仍禁 bots/scripts 與自動化外聯。
2. **Upwork / Fiverr**：官方 AI 頁皆 403。可得（均 UNVERIFIED）：Upwork 於 2023 提供 AI Services hub、鼓勵揭露 AI 使用；2026-01 條款更新含以平台內容訓練 AI 與 opt-out（第二手，C）；Fiverr 允許 AI 但要求原創、權利歸屬與合規。**對 solo 的務實結論（INFERENCE）：不論平台，對客戶主動揭露「使用 AI 輔助、不輸入客戶機密到未經核准的服務」是成本最低且最不易違規的做法。**
3. **平台 AI 類別/列表**：Upwork 有 AI Agent Developers 行銷頁（A，provider_marketing）；Fiverr AI agency 類別：本次**未找到證據**（UNKNOWN）。
4. **自動化提案**：沿用 BASELINE——AI 可協助起草，但不做自動抓取/批量外聯；Contra、LinkedIn、Freelancer、HN 條款文字皆如此。

## 4. 依證據排序（INFERENCE，非預期收益）

排序標準：官方條款可讀且不排除 Taiwan / solo 可達 / 契合固定範圍 AI 服務 / 信任門檻。

1. **個人網站＋技術內容＋轉介/人脈**（19/20/21/23）— 結構契合、無資格限制；弱點：冷啟動，轉介來源 UNKNOWN。（與 BASELINE 一致）
2. **Contra**（A 級條款；Taiwan 未排除）— 弱點：客戶來源與 AI 需求證據 UNKNOWN；禁免費試做。
3. **Upwork**（可觀測 AI hiring 面最廣，但官方條款/費率/資格 403）— 僅人工操作。
4. **LinkedIn（人工）**。
5. **Make / Zapier solution partner**（官方免費或無列費；需自有網站、服務經驗；solo 資格未述）— 取得案例後再申請（第二階段）。
6. **Anthropic CPN 加入**（免費、僅 organization 語言）與個人認證；tier 不可達。
7. **Taiwan 本地平台/B2B**（付款最簡單 [INF]；證據缺）。
8. **Fiverr / Freelancer / Arc / Toptal / Lemon.io**。
9. **HN / Reddit / GitHub**（內容與信任，不推銷）。
10. **AWS / Google / Microsoft 市集與夥伴**：AWS Marketplace 對 Taiwan 個人封閉（A）；Microsoft 有費用門檻；Google UNKNOWN。n8n Experts 目前地區不含 Taiwan（A）。

## 5. UNKNOWN 清單

Upwork/Fiverr/OpenAI 官方原文；PeoplePerHour；各平台 Taiwan 明確資格；Anthropic 個人認證報考資格與 Program fee；OpenAI 個人資格；Microsoft/Google solo 資格；Make/Zapier 對 solo 的實際接受度；Taiwan 平台確切費率；所有轉換率、價格成交資訊。

---

# AI-service-specific payment/tax/legal additions

**聲明：以下不是法律、稅務或財務建議（not legal advice）。所有法律結論標 UNKNOWN，須由律師/會計師/國稅局確認。** 通用收款與稅務（PayPal/Wise/Payoneer、外匯申報、營業稅 §7(2) 零稅率、起徵點、二代健保）沿用 BASELINE `13_TAIWAN_PAYMENT_TAX.md`，不重述。

## A. 方法與限制

法規取自 law.moj.gov.tw（A，WebFetch 摘要；個資法頁面標示最近修正 114-11-11，部分修正條文尚未施行，生效日未定）；Anthropic 條款（A，摘要）；OpenAI 條款頁 403，僅有搜尋摘要（UNVERIFIED）。TIPO AI 著作權指引 PDF 無法解析，AI 輸出著作權立場僅有新聞/二手（C）。**條文摘要由小模型產生，條號請人工核對原文。**

## B. AI 交付物 IP 與所有權

| 議題 | 證據 | 標籤 |
|---|---|---|
| Anthropic API/商業條款：Outputs 歸屬 | 官方（摘要，Section B）：「hereby assigns to Customer its right, title and interest (if any) in and to Outputs」；Customer 保有 Inputs 權利。注意「(if any)」——是否存在可轉讓權利取決於法律 | VERIFIED（摘要）/ 法律效果 UNKNOWN |
| OpenAI：Output 歸屬 | 搜尋摘要稱 Business Terms：as between you and OpenAI，customer 擁有 Output（官方頁 403） | UNVERIFIED |
| 誰是 Customer | 條款的 Customer 是**簽 API 帳號者**。若顧問用自己的帳號，Outputs 先歸顧問，須再在服務合約轉讓/授權給客戶；若用客戶的 API key/帳號，條款關係在客戶與供應商之間 | INFERENCE |
| Taiwan 著作權法 | §3 作品定義未明文要求人類創作；§12 受聘/出資作品預設歸受聘人（契約可約定歸出資人）；§36/§37 轉讓與授權範圍以約定為準，不明部分推定未轉讓 → **合約須明寫轉讓/授權範圍** | VERIFIED（條文摘要） |
| AI 純生成物能否受著作權保護 | 無查到智慧局正式函釋；新聞稱智慧局官員表示純 AI 生成原則上不受保護，人類實質投入可主張（2023，C）；另有「生成式 AI 著作權指引 1.0」報導（C，未取得原文） | UNVERIFIED |
| 實務含義 | 對客戶交付的程式碼/workflow/文件，條款宜寫「依法律允許範圍轉讓/授權，不保證可受著作權保護」；不得保證 AI 輸出未侵權（Anthropic K 章 IP 補償僅對 Customer 且有排除項，顧問非必然為受益人）| INFERENCE |
| 營業秘密法 | §2 三要件（非公知、經濟價值、合理保密措施）；§4 出資聘請：契約未訂時歸受聘人但出資人可使用；§3 受僱人職務上研發歸雇主（對兼職顧問與雇主 IP 衝突重要，BASELINE §4）；§13-1/§13-2 刑責含意圖在境外使用 | VERIFIED（條文摘要）；個案 UNKNOWN |

## C. 客戶資料、NDA、DPA

| 議題 | 證據 | 標籤 |
|---|---|---|
| 供應商是否以客戶資料訓練 | Anthropic：「Anthropic may not train models on Customer Content from Services」且 Customer Content 為 Customer 的 Confidential Information（Section B/E.1，A，摘要）。OpenAI：搜尋摘要稱 API/Business 資料預設不用於訓練（官方頁 403；保留 30 天/ZDR 說法來自第三方 conductatlas，C） | Anthropic：VERIFIED（摘要）；OpenAI：UNVERIFIED |
| DPA | 兩家 DPA 本次均未取得 → UNKNOWN（OpenAI 社群帖有爭議，C） | UNKNOWN |
| 顧問立場 | 若處理客戶資料，顧問可能是客戶的「受託人」：個資法 §4「受…委託蒐集、處理或利用個人資料者，於本法適用範圍內，視同委託機關」→ 受託期間可能被視同委託機關而負責 | VERIFIED（條文）；適用性 UNKNOWN |
| 個資法其他條文 | §19/§20 特定目的與使用範圍；§20-1 保有個資檔案者的安全維護（摘要稱 §27 已刪除、移至 §20-1，須人工核對）；§29 非公務機關違法損害賠償（證明無故意過失可免責）；§41/§42 刑責最高 5 年有期徒刑、罰金最高 NT$100 萬；§21 國際傳輸限制（主管機關得限制） | VERIFIED（摘要） |
| 跨境 | 客戶資料送至美國 LLM API = 國際傳輸/境外處理，是否構成須處理事項：UNKNOWN | UNKNOWN |
| 與 WebComm 政策 | 組織政策禁止將客戶個資、合約、機密輸入 AI 工具；本研究/服務設計須避免取得客戶敏感資料（BASELINE §4 同） | BASELINE |
| 設計建議（INFERENCE） | (1) 服務範圍以 metadata、去識別化樣本、客戶自行環境內執行為主；(2) 客戶使用自己的 API 帳號與 key，顧問不持有資料；(3) NDA 先行，並明寫禁止輸入未核准 AI 服務；(4) 不處理 GDPR/個資受規範資料，除非另有法務意見 | INFERENCE |

## D. 責任、保證與風險分配

- Anthropic 要求 Customer 向 Users 告知 Outputs 事實陳述不可未經驗證信賴（D.3，A 摘要）；Contra 亦稱 AI 內容「should not rely … as a sole source of truth」。→ 合約應寫人工審查義務與不保證輸出正確性（INFERENCE）。
- Anthropic K.2：Customer 就其 Inputs 與誤用對 Anthropic 補償；顧問若為 Customer，須注意輸入客戶資料的權利（INFERENCE）。
- 責任上限、損害賠償、保險（專業責任險）：Taiwan 適用與市價：UNKNOWN，未查。
- 準據法/管轄、跨境執行：UNKNOWN。

## E. AI 服務專屬的 Taiwan 稅務/付款項目（全為待查，非結論）

| 項目 | 現況 | 標籤 |
|---|---|---|
| 轉售 LLM/SaaS 用量 | Anthropic 條款 D.4(a)：不得 resell Services，除非 Anthropic 明確核准；CPNA C.4 亦稱 Program 不授權轉售/再授權。→ 以「加價轉售 API 用量」為商業模式有條款風險；以客戶自己的帳號計費較安全（INFERENCE） | 條款：VERIFIED（摘要）；OpenAI：UNVERIFIED |
| 第三方 API 成本報銷/代墊 | 屬「代收代付」或「營業收入」，稅務認定（營業稅、所得稅費用認列）UNKNOWN；Taiwan 會計師/國稅局待問 | UNKNOWN |
| 軟體/AI 服務歸類 | 對境外客戶之顧問、客製軟體開發、SaaS 訂閱收入，營業稅零稅率適用（§7(2)，BASELINE）與所得類別是否不同：UNKNOWN | UNKNOWN |
| 開發的軟體資產之 IP 授權金（license fee） | 若交付「授權」而非「勞務」，所得性質（權利金？）可能不同：UNKNOWN，須會計師判定 | UNKNOWN |
| 對境外客戶開立發票 | 營業稅/統一發票是否需要取決於營業人身分（BASELINE §5 UNKNOWN）；境外客戶常要求 invoice 與 W-8BEN（BASELINE：US 預扣/W-8BEN 未重驗）| UNKNOWN |
| 夥伴計畫費用 | Microsoft USD 350–4,875（A）；AWS APN 年費 USD 2,500（搜尋摘要，UNVERIFIED）；Anthropic CPN 免費；Make 免費（A）。費用是否可列報為費用：UNKNOWN | 費用金額：A/UNVERIFIED |
| AWS Marketplace 收款 | Taiwan 不在 eligible jurisdictions → 無法直接收款 | VERIFIED（名單） |
| 雇主契約 | 兼職、IP 歸屬、使用雇主資源：UNKNOWN（BASELINE §4） | UNKNOWN |

## F. 建議下一步（人工）

1. 閱讀自己的雇傭契約（兼職/IP/競業）。
2. 由律師審一份通用的跨境 AI 服務合約範本：IP 轉讓/授權、保密、資料處理與禁輸入條款、無保證與責任上限、準據法。
3. 向 Anthropic/OpenAI 取得並閱讀原文條款與 DPA（本研究不可聯絡第三方，故由人工執行）。
4. 向國稅局/會計師書面詢問：個人顧問與軟體授權所得類別、API 代墊款處理、零稅率適用。
5. 在客戶端設計上採用「客戶自有 API 帳號＋去識別化資料」以降低個資與資料訓練風險。

## G. 本檔 vs BASELINE 修正摘要

- NEW EVIDENCE：AWS Marketplace 賣家 eligible jurisdictions 不含 Taiwan；n8n Experts 地區限定與 3 客戶門檻；Anthropic CPN／Services Track 門檻（solo 不可達 Select）；Make/Zapier 官方條件；Microsoft 費用表；Contra 的 Indy AI 條款；Anthropic Outputs 歸屬與禁轉售條款；Taiwan 個資法/營業秘密法/著作權法條文與 AI 專屬含意。
- BASELINE 未變：Upwork/Fiverr 官方頁仍 403；PayPal/Wise/Payoneer 等收款資訊。
- 未解：OpenAI 條款原文、PeoplePerHour、Google Cloud Taiwan、TIPO 指引原文。
