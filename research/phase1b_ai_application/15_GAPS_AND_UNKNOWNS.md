# 15 Gaps and Unknowns

## A. 決策相關缺口
1. **私人買家購買證據 = 0**：全部 126 筆 purchase 皆為公部門（台灣 PCC 105、美國 USAspending 21）。
2. **公部門案是否可由個人/遠端承接 UNKNOWN**：標案文件未讀；多為限制性招標（96 筆有投標家數者 47 筆僅 1 家），廠商資格（通常需公司）未驗證。
3. **個人實際成交價 UNKNOWN**；所有價格為 list/asking/得標額；solo 入口審計價（US$45–5,000）顯示商品化壓力。
4. **Pain 資料（155 列）皆 C 級、偏 n8n/Make 低程式碼使用者**；僅 5 列有數字預算；Reddit、StackExchange、GitHub issues、Indie Hackers、Zapier、Dify 未涵蓋。
5. **Freelance 樣本**：Upwork 27 列全為搜尋摘要（403）；Freelancer 預算為預設級距、客戶資訊隱藏、僅一週快照；PeoplePerHour 幣別基準不明；Contra/Codeable/Malt/Toptal 只有供應方檔案；104、CakeResume、Tasker 不可得；多筆摘要連結已失效（高估現存需求）。
6. **product_mapping 與類別標註為關鍵字啟發式，未經人工覆核**（尤其 internal-assistant 33 筆與 RAG/客服重疊）。
7. **公開付費交付物範本不存在**（僅廠商/標準框架）；交付物形狀為 INFERENCE。
8. **自動化比例全部 UNKNOWN**（僅 1 個 n8n workflow JSON 的 n=1 腳本實驗）；其餘 21 步未測。
9. **AI+DB/MongoDB/Kafka 買家證據 = 0**；未系統性搜尋台灣個人賣家，其存在與否 UNKNOWN。
10. **平台規則**：Upwork/Fiverr/OpenAI 條款頁 403 → UNVERIFIED；Anthropic 夥伴計畫的個人資格、OpenAI 夥伴計畫資格 UNKNOWN；AWS Marketplace 付費賣家國家清單不含台灣（A）；n8n Experts 為封閉試行且地區不含台灣（A）。
11. **法務/稅務**：AI 服務在台稅務、IP 歸屬（Anthropic 條款將 Outputs 歸 API 帳號持有人；台灣法律留待契約）、個資法 §4 受託認定 — 全部非定論，需專業意見；條文編號來自摘要需人工核對。
12. 雇主兼職/NDA 合約：UNKNOWN。
13. 公司政策：WebComm 禁止客戶資料/個資進 Claude → 客戶資料處理需去識別化或預先許可。
14. 公司層供給樣本偏向「會公開價格的英語供應商」，47% 價格透明度不代表市場。
15. 資料品質：多數頁面為 WebFetch 小模型摘要，非逐字；引用需人工對照。

## B. 能縮小不確定性的下一步
1. 讀 3–5 件 PCC 標案文件（資格、限制性招標、可否轉包/聯合承攬）。
2. 以暖關係人工驗證：是否有人願意為固定範圍 assessment/PoC 簽書面付費意願（人工外聯，由使用者決定）。
3. 用公開/合成資料做一次完整 pilot 交付並記錄人工時數 → 才能算自動化槓桿與有效時薪。
4. 雇主政策、稅務、收款路線確認。
