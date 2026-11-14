# Cloud / ChatOps 架構（claude-code-action + OAuth token）

取代先前的 gh-aw 版本（gh-aw 不支援 `CLAUDE_CODE_OAUTH_TOKEN`）。

## 運作
在 **Control Issue #2** 留言（僅 repo owner；手機 GitHub App 可用）：
`/status` · `/continue` · `/research <題目>` · `/analyze <題目>` · `/finalize`

`.github/workflows/control.yml`，三個 job：
| Job | 權限 | 內容 |
|---|---|---|
| `gate` | `{}` | 驗證 issue #2、留言者 = owner、指令白名單；解析參數 |
| `status` | contents: read, issues: write | 唯讀：工具僅 Read/Glob/Grep；回覆留言 |
| `work` | contents: write, pull-requests: write, issues: write | 模型只能改檔 + 本地 commit；push / draft PR / 留言由**固定步驟**執行 |

## 取代 gh-aw safe-outputs 的控制
- 模型沒有 push 權：checkout `persist-credentials: false`，`git push`、`gh`、`curl`、`env` 等被 `--disallowedTools` 禁止；推送由 guard 步驟用 branch `agent/<cmd>-<run_id>` 執行，不可能推到 main。
- Guard 步驟在 push 前檢查：無變更→不開 PR；變更含 `.github/` 或 `AGENTS.md`→阻擋；diff/commit/摘要含 OAuth token 或 `sk-ant-` 等→阻擋。
- 只開 **draft PR**；沒有 merge 步驟，人工 merge。
- 工作流程層：`permissions: {}` 預設、concurrency 單一執行、timeout、`show_full_output: false`、action 以 commit SHA 固定。
- 與 gh-aw 相比**較弱之處**：沒有網路防火牆（runner 可連外網）、沒有 threat-detection 步驟；WebFetch/WebSearch 開啟下仍有 prompt injection 風險，故以「無 push 權 + 內容掃描 + 人工 review PR」補強。Repo 是 public，agent 分支與 PR 內容皆公開——**merge 前請審閱**。

## 你需要在 GitHub UI 做的設定
1. **Secret**：https://github.com/DevonForlan/ai-opportunity-to-revenue/settings/secrets/actions → New repository secret → Name：`CLAUDE_CODE_OAUTH_TOKEN`，Secret：貼上你自己保存的 `claude setup-token` token → Add secret。驗證：`gh secret list -R DevonForlan/ai-opportunity-to-revenue` 出現該名稱。
2. **允許 Actions 開 PR**：…/settings/actions → Workflow permissions → 勾選「Allow GitHub Actions to create and approve pull requests」→ Save。（沒有它，`work` 只能 push 分支，PR 建立失敗，會在 Issue 留言提示。）
3. **移除舊 secret（若曾設）**：`ANTHROPIC_API_KEY` 不再需要。
4. **建議**：…/settings/branches 或 Rulesets 對 `main` 要求 PR、禁止 force push（public repo 可免費使用）。

## 第一次 `/status` E2E 測試
1. 合併本 PR 後，在 Issue #2 留言 `/status`。
2. 預期：1–3 分鐘內 Actions 出現 "Control Agent (ChatOps)"，`gate`→`status` 成功，Issue 出現含摘要的回覆。
3. 失敗排查：看該 run 的 `status` job log（不會輸出 token）；常見原因＝secret 未設或 token 無效。
4. 再測 `/continue` 前，先完成上面第 2 項。

## 已知限制
- 未做端到端實測（token 在你那端）；僅驗證 YAML 結構、指令解析與洩漏偵測函式。
- OAuth token 綁 WebComm Team 帳號：用量走該訂閱額度，是否產生額外費用、公司是否允許於個人公開 repo 使用 → UNVERIFIED，請自行確認公司政策。
- 公司 Team 帳號 token 若外洩可被他人以你的訂閱使用；一旦懷疑洩漏請立即撤銷並重新 `setup-token`。
