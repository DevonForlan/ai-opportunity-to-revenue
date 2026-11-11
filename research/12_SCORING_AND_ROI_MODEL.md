# 12 Scoring & ROI Model（v0，未校準）

## 閘門（先 gate，再評分）
任一為真 → score = 0（不進入排序）：已指派/已結算、repo 停滯、付款證據=無、國家資格=已證實不可、需簽 NDA 而不可使用 AI 且無授權。

## 加權（0–100）
| 因子 | 權重 |
|---|---:|
| Payment Confidence | 20 |
| Technical Fit | 15 |
| Effective Hourly Rate（用中位工時估算） | 15 |
| AI Leverage | 10 |
| Acceptance Clarity | 8 |
| Client/Maintainer Activity | 8 |
| Competition | 6 |
| Country Eligibility + Payment Availability | 8 |
| Platform Risk | 5 |
| Reuse / Productization Potential | 5 |

規則：Reward 不單獨計分，只經 Effective Hourly Rate 進入；**Payment Confidence=Low 時總分上限 40**；UNKNOWN 因子以 0 分計並標記「資料不足」，不填假值。初始權重為設計假設，需用 30 天結果校準。

## ROI
```
Expected Net / Human Hour = (P_accept × P_pay × Reward − AI_cost − platform_fee − payment_fee − infra) / Human_hours
```
P_accept、P_pay 目前**無資料 → UNKNOWN**；先以實驗記錄實際轉換率，再填入。未取得前只報告「若 P=1 的上限時薪」並標明為上限。

## 範例（說明用，非資料）
Reward $5,000、Payment Confidence=Low、200 小時 → 被 cap 在 ≤40，且 Effective Rate 低 → 排序墊底。
