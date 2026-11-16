# 14 Source Log

集中來源紀錄：`14_SOURCE_LOG.csv`（207 列，依 URL 去重；欄位：source,url,source_type,access_date,published_or_updated,evidence_level,used_for,confidence,notes,origin_file）。各資料集列（demand/competitor/freelance）另有自己的 url 欄；原始分線來源在 `_sources/`。

Evidence level 分佈：A 132、B 33、C 37、其他 5。存取日 2026-11-16 前後。多數 provider/官方頁由 WebFetch 摘要讀取，引用需人工對照原頁。
