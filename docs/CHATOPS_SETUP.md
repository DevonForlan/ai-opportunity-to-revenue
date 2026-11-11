# Cloud / ChatOps 架構

- Engine：gh-aw v1.2.2（`.github/workflows/control.md` → 編譯成 `control.lock.yml`），`engine: claude`。
- 觸發：在 **Control Issue** 留言 `/status` `/continue` `/research <題目>` `/analyze <題目>` `/finalize`（僅 repo admin；手機 GitHub App 可用）。
- 路由：`strategy: centralized` → `agentic_commands.yml`。
- 輸出（safe-outputs，agent 本身唯讀）：只有 **add-comment（1 則）** 與 **draft PR（1 個，前綴 `[agent]`，label `agent-output`）**。沒有 merge / 付款 / 對外發訊息的工具。
- 規則：`AGENTS.md`。每次非 `/status` 執行都要更新 `research/CURRENT_STATUS.md`，並在 Control Issue 留摘要。
- 修改 `control.md` 後必須執行 `gh aw compile` 並 commit `.lock.yml`。

## 你需要在 GitHub UI 做的設定（CLI 無法/不該代做）
1. **Secret**：https://github.com/DevonForlan/ai-opportunity-to-revenue/settings/secrets/actions → New repository secret → Name：`ANTHROPIC_API_KEY`，Value：你的 Anthropic API key（console.anthropic.com 建立；建議設月額度上限）。驗證：`gh secret list -R DevonForlan/ai-opportunity-to-revenue` 出現該名稱。
2. **允許 Actions 開 PR**：…/settings/actions → Workflow permissions → 勾選「Allow GitHub Actions to create and approve pull requests」→ Save。驗證：之後 agent 能建立 draft PR。（注意：同時允許 Actions 核准 PR；請勿把 main 的自動合併打開。）
3. （建議）…/settings/branches：若方案支援，對 `main` 設 branch protection 要求 PR；agent 無 merge 工具，但這是第二道防線。
4. 驗證整體：到 Control Issue 留言 `/status`，約 1–3 分鐘內應出現 👀 reaction 與摘要留言；失敗看 Actions 分頁的 "Control Agent (ChatOps)" 執行紀錄。

## 已知限制
- 未實測：尚未提供 API key，所以**端到端執行未驗證**；只驗證了 `gh aw compile` 成功。
- Claude 以 API key 計費（用量成本 UNKNOWN，需看 Anthropic console）。
- `/research` 需對外網路；gh-aw 預設 network allowlist（`defaults`）可能擋住部分網域，需要時於 `network.allowed` 加入。
