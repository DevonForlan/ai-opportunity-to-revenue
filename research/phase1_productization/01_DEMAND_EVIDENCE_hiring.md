# 01 需求證據：徵才 / 外包 / 採購（hiring + purchase）

捕獲日期：2026-11-16。資料集：`02_DEMAND_DATASET_hiring.csv`（H001-H090，共 90 列）。來源清單：`_sources/demand_hiring.csv`。

## 方法與限制（先讀）

- 方法：用公開 API 與公開頁面取得。PCC 政府電子採購網資料用 `pcc-api.openfun.app`（g0v 鏡像，等同官方決標公告資料）以中文關鍵字（資料庫健檢／效能／升級／維運／移轉／Oracle／SQL Server／MongoDB 等）查詢，只保留 2021 年起、含決標金額、且標題明確為 DBMS 服務的案件；Dice、LinkedIn（guest 公開列表）、Freelancer.com 以 WebFetch 抓取；Upwork、UK Contracts Finder、stotles 為 403 或僅有搜尋摘要，一律標 PARTIALLY VERIFIED；HN 用 Algolia API。
- 證據類型定義：`purchase` 僅限有公開決標／契約金額者（PCC、英國 Contracts Finder）；`hiring` 為職缺／接案平台案件，**職缺不等於付費合約**。
- 限制 1：**PCC 47 列沒有一筆標題明確為 MongoDB**。PCC 搜尋 "MongoDB" 只出現一筆 2022 年東華大學的 MongoDB Developer 訓練課採購（決標 NT$2,405,700，向 Udemy 採購，屬教育訓練，未列入資料集）。PCC 列多數 DBMS 為 UNKNOWN 或 Oracle / SQL Server，只能證明「台灣公部門會付費購買資料庫健檢／調校／升級／維運服務」，不能證明 MongoDB 專屬需求。（NEW EVIDENCE，對 Phase 0 為補強而非修正）
- 限制 2：PCC 決標金額為公開契約金額，部分標題是與系統功能擴充捆綁（已在 notes 標註），不可當成純資料庫服務單價；招標文件（RFP 範圍、是否可遠端、廠商資格）未逐案讀取，remote_onsite 一律 UNKNOWN。公部門案件通常有資格／本國廠商限制，Taiwan 個人接案者能否投標 UNKNOWN。
- 限制 3：LinkedIn 列表僅 10 列／查詢、發布日為相對時間；部分列只有列表資訊（標 PARTIALLY VERIFIED）。Dice 多為美國人力仲介 C2C／W2 合約，常要求美國工作許可或現場。
- 限制 4：Freelancer.com / Upwork 預算極低（見下），是 C 級證據；行情不代表資深診斷服務的價值。
- 未取得：104、1111、Yes123、CakeResume（WebFetch 以 104 單一職缺 403；搜尋僅得 104 列表摘要，未取得可逐列驗證的 MongoDB 接案案件，故未納入）；Tasker 3 個案件頁雖可取得，但皆為爬蟲／關聯式 DB 需求，與 MongoDB 無關，未納入；Wellfound、Indeed、Toptal、Lemon.io、Arc 未取得可驗證列（RemoteOK API 回傳 98 筆、Remotive 搜尋回傳 17 筆，標題／標籤無 MongoDB 或 DB 服務類職缺，未納入）；SAM.gov、TED、澳洲 tender 搜尋無 MongoDB 健檢類標案。

## 數量統計

| 來源 | evidence_type | 列數 | 證據等級 |
|---|---|---|---|
| PCC 政府電子採購網 | purchase | 47 | A |
| UK Contracts Finder（摘要） | purchase | 4 | A（皆 PARTIALLY VERIFIED） |
| stotles 聚合（摘要） | purchase | 1 | B（PARTIALLY VERIFIED） |
| Dice | hiring | 8 | B |
| LinkedIn guest listings | hiring | 16 | B |
| Freelancer.com | hiring | 9 | C |
| Upwork（摘要） | hiring | 2 | C（PARTIALLY VERIFIED） |
| Hacker News Who is hiring | hiring | 3 | B |
| 合計 | purchase 52 / hiring 38 | 90 | VERIFIED 67 / PARTIALLY VERIFIED 23 |

其中直接提到 MongoDB 的列約 33 列（Dice 8、LinkedIn 約 9 含 Taiwan 1、Freelancer/Upwork 約 11、HN 3、UK 2）；其餘為 DBMS 服務採購（Oracle/SQL Server/未明）與 Kafka 相關職缺。「採購」中 MongoDB 實際服務購買證據：0 列（UK 的 DVLA／DWP 兩列是 Atlas 軟體訂閱，不是服務）。

## 重點發現

1. **（NEW EVIDENCE）台灣公部門確有重複性、定價可見的「資料庫健檢／調校」採購**。中華郵政「郵政核心商務系統資料庫健檢及優化服務專案」連續兩年決標：113 年 NT$1,480,000（預算 1,488,000）、114 年 NT$1,400,000（預算 1,488,000），為最貼近 Health Check 產品的公開購買證據（H 列 PCC，DBMS UNKNOWN）。行政院人事行政總處「114 年度資料庫效能調校服務案」決標 NT$3,170,000（預算 3,450,000）。台鐵「網頁版人事薪工系統資料庫效能提升案」NT$8,030,000。VERIFIED（金額），但廠商與範圍未讀。
2. **升級／移轉類採購很多且價格帶寬**：小案約 NT$265,900-NT$590,000（苗栗縣、澎湖縣、臺灣銀行單一系統升級、台鐵），大案 NT$數百萬至數千萬（臺灣銀行 NT$27,096,000、衛福部 NT$44,100,000 等，皆為捆綁系統工作）。銀行／政府／國營事業是主要買方。INFERENCE：低價帶（約 NT$30 萬以下的維運／升級）與遠端單人接案的規模相近，但是否允許遠端、是否限本國立案廠商 UNKNOWN。
3. **MongoDB 本身的「外部服務」需求證據偏弱**：Dice／LinkedIn 的 MongoDB 職缺多為美國現場或 W2/C2C 人力仲介（Synkriom 6 個月、Techno Talent 12 個月、Netpace 12 個月以上；多數薪資 UNKNOWN 或 "Depends on experience"），內容（replica set／sharding、backup/restore 自動化、版本升級、效能調校、HA/DR）與目標服務範圍高度重疊，但屬長期駐點／人力派遣，不是可遠端產品化的固定範圍服務。Taiwan 唯一 MongoDB 職缺（OpenNet DBRE，台北混合辦公）為全職。
4. **接案平台的 MongoDB 效能／備份／遷移案件預算極低**：Freelancer.com 為 INR 600-1,500、USD 2-8/小時、AUD 10-30、CAD 250-750、USD 30-250；Upwork 的 Atlas 慢查詢優化為 fixed USD 100（摘要，PARTIALLY VERIFIED）。競標數 7-210 件，平均出價 USD 8/小時至 CAD 447。這些屬 C 級，證明「需求存在但在此通路被價格壓低」，不構成高單價診斷服務的需求。（對 Phase 0 的「接案平台價格」假設為補強）
5. **英國 Contracts Finder 有最接近的海外對照**：Datalynx「Database Review and Migration Options」決標 GBP 14,425（health review + 建議，非遷移本身；技術未知），OFCOM 資料遷移 GBP 23,400，Bedfordshire 大學 Oracle/SQL Server 支援 GBP 34,686。僅 PARTIALLY VERIFIED（頁面 403，摘要取得）。可作為「外部審查案約 GBP 1-3.5 萬」的價位參考，但勿外推為 MongoDB 價格。
6. **HelpMyCash（HN）** 是公開的「~4 小時/週 retainer + on-call 溢價」範例（AWS 與 MongoDB Atlas 為其技術棧之一），顯示 retainer 型可靠度服務有買家，但限 EU/CET 時區、費率未公開。

## 對產品化的含意（INFERENCE，非結論）

- 有公開購買證據的是「資料庫健檢／調校／升級」這個服務類別（台灣公部門，NT$約 140-320 萬），但 **沒有任何公開購買證據指向 MongoDB 專屬健檢**；MongoDB 側的證據僅有職缺與低預算接案單。
- 若要鎖定台灣公部門／金融市場，需另行確認：投標資格（本國立案、資本額、實績）、是否接受遠端、DBMS 組成（Oracle/SQL Server 為主，MongoDB 占比 UNKNOWN）。
- 轉換率、成交率、實際成交價：UNKNOWN（本資料集無此類資料）。

## 資料集欄位說明

CSV 為 DEMAND schema：`id,source,url,capture_date,title_problem,technology,customer_type,stated_budget_rate,pricing_model,remote_onsite,geography,pain_point,requested_outcome,status,evidence_type,evidence_level,verification_status,notes`。PCC 的 URL 為 `https://pcc.g0v.ronny.tw` + API 回傳的 case 路徑（由 API 取得，頁面本身未另行開啟）。
