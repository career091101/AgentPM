# 週次トレード戦略レポート: {week_start} 〜 {week_end}

**レポート生成日**: {report_date}
**対象期間**: {week_start} 〜 {week_end}
**現在のレジーム**: {current_regime}

---

## エグゼクティブサマリー

### 今週のパフォーマンス

| 指標 | 今週 | 先週 | 変化 |
|------|------|------|------|
| 週間リターン | {weekly_return}% | {last_week_return}% | {return_change} |
| 勝率 | {win_rate}% | {last_week_win_rate}% | {win_rate_change} |
| Sharpe ratio | {sharpe_ratio} | {last_week_sharpe} | {sharpe_change} |
| 最大ドローダウン | {max_dd}% | {last_week_max_dd}% | {dd_change} |

### 重要事項
- {key_point_1}
- {key_point_2}
- {key_point_3}

---

## 今週のトレード詳細

### トレード一覧

| 日付 | エントリー/イグジット | 価格 | サイズ | 損益 | 累積損益 |
|------|---------------------|------|--------|------|---------|
{trade_details}

### トレード統計

- 総トレード数: {total_trades}
- 勝ちトレード: {win_trades}
- 負けトレード: {lose_trades}
- 平均利益: {avg_profit}円
- 平均損失: {avg_loss}円
- Profit Factor: {profit_factor}

---

## レジーム分析

### 現在のマーケット状況

- **検出レジーム**: {current_regime}（{regime_confidence}%信頼度）
- **レジーム継続期間**: {regime_duration}日
- **最終レジーム切り替え**: {last_regime_switch}

### レジーム推移

{regime_history}

---

## 次週の戦略推奨

### エントリーポイント

{entry_recommendations}

### リスク管理

- **推奨ポジションサイズ**: {position_size}%
- **Stop Loss**: {stop_loss}
- **Take Profit**: {take_profit}
- **最大リスク**: {max_risk}%

### 注意事項

{risk_warnings}

---

## パフォーマンス可視化

### Equity Curve（今週）

![Equity Curve](./charts/equity_curve_{week_id}.png)

### Drawdown（今週）

![Drawdown](./charts/drawdown_{week_id}.png)

### レジーム推移（過去4週間）

![Regime History](./charts/regime_history_{week_id}.png)

---

## 付録

### テクニカル指標

- **SMA 20**: {sma_20}
- **SMA 50**: {sma_50}
- **RSI**: {rsi}
- **MACD**: {macd}
- **Bollinger Bands**: {bb_upper} / {bb_middle} / {bb_lower}

### システム状態

- **バックテスト信頼性**: 97.5%
- **データ完全性**: {data_completeness}%
- **レジーム検出精度**: {regime_accuracy}%
- **最終更新**: {last_update}

---

**免責事項**: このレポートは情報提供のみを目的としており、投資助言ではありません。最終的な投資判断はご自身で行ってください。
