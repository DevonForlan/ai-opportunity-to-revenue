# 10 Pilot B — Implementation（可執行的 fixed-scope PoC）

> **全部資料為 SYNTHETIC。** 程式在 `pilot/phase2/supportdesk/`（標準庫 Python，約 1,100 行含測試與評估；無網路、無付費服務、無憑證）。
> **LLM 路徑未實作也未測試**：唯一的「模型」是決定性規則 `rules-v1`；介面 `ModelProvider` 已預留。

## 1. 題目選擇
`BASELINE` 預設題目（Issue #8）：合成客服信件 → 分類/擷取 → 知識庫查詢 → 草稿 → 人工核准 → mock CRM → 稽核。
Decision Audit（01）顯示客服類是購買證據最集中的類別之一（28 筆公部門，另有 chatbot 依據），也不需要真實 credentials 即可驗證，因此**沿用預設題目**。
**誠實註記**：Pilot B 先於 Pilot A 完成，故題目非由 Pilot A 獨立導出；Pilot A 的敏感度檢驗（08）只驗證了排名對輸入穩健。

## 2. 架構
```
JSONL / form ─► schema 驗證 ──(失敗)──► dead_letters
                 │
                 ▼
          PII 遮蔽 + 注入偵測 ─► 規則分類/欄位擷取 ─► KB 檢索 ─► 有依據的草稿
                 │                                          │
                 └──────── escalation 規則（任一觸發即升級、無草稿）┘
                 ▼
   requests / results / crm_tickets(mock) / audit_log(hash chain)
                 ▼
   待核准 ──► 人工 approve ──► outbox（唯一「寄出」的地方）
```
元件：`schemas.py`（輸入/輸出 schema）、`guardrails.py`（遮蔽、注入、承諾過濾）、`classifier.py`（規則＋擷取）、`retrieval.py`（雙語詞彙檢索）、`drafter.py`（KB 文字＋固定模板）、`store.py`（SQLite、重試、冪等、稽核鏈）、`pipeline.py`、`cli.py`。

## 3. 需求對照（Issue #8 §6）
| 需求 | 實作 |
|---|---|
| input / output schema | `SupportRequest.from_raw`、`TriageResult` |
| human approval checkpoint | 只有 `approve` 能寄出；escalated 不可核准（測試） |
| error handling | 畸形輸入 → dead-letter，不崩潰 |
| retry / idempotency | `with_retry` 3 次；冪等鍵 = hash(channel, message_id)，**以「完成結果」判定**（見 §5 bug） |
| logs / audit trail | hash-chain，竄改可偵測；稽核無原始 PII |
| evaluation dataset / functional tests / edge cases | 72 個合成案例（DEV 42 + HELDOUT 30）；21 個單元測試 |
| prompt/model config versioning | `config.json` 版本＋hash 寫入每筆稽核 |
| basic guardrails | 遮蔽、注入模式、承諾過濾、KB 依據 |
| README / runbook / reproducible startup | `README.md`、`RUNBOOK.md`；`python -m supportdesk.cli run data/sample_requests.jsonl` |

## 4. 端到端實跑（合成 37 行輸入）
`run` 輸出：`{"pending_approval": 24, "dead_letter": 6, "escalated": 6, "duplicate": 1}`；核准成功；重複核准被拒；`verify` → audit chain OK；整檔重跑 → 31 duplicate（冪等）。

## 5. 過程中實際發現並修正的缺陷（誠實紀錄）
1. **子字串關鍵字 bug**（HELDOUT 發現）：`"sue"` 命中 `reissue`/`issue` → 一般帳務信被當成客訴。修：ASCII 關鍵字改為詞界匹配。
2. **冪等 bug（我自己質疑測試時發現）**：請求列已寫入、結果寫入失敗，重送被誤判為 duplicate 且沒有工單 → **客訴遺失**。原本那個「partial failure」測試其實只讓第一次寫入失敗，沒測到。修：冪等以 `results` 為準，請求寫入改 `INSERT OR IGNORE`，並加入真正的回歸測試。
3. 檢索門檻過嚴與複數詞（`invoice` vs `Invoices`）→ DEV 調整。
4. 多重意圖草稿只回答其中一個需求 → 新增 `multi_intent` 升級規則（**由 HELDOUT H16 啟發**，故 HELDOUT 對此規則不再乾淨）。

## 6. 限制
- 規則詞彙有缺口（「send back」「two charges」）→ 失敗方向為**升級**（安全但過度升級）。
- **改寫過的 prompt injection 無法被模式偵測**（H24）。緩解是結構性的：草稿只含 KB 文字＋固定模板、承諾過濾、人工核准；**不是**偵測。
- 未做：LLM provider、真實 Gmail/CRM 連接器、多租戶、web UI、真實流量、人工核准時間量測。
