# Phase 4 - レジーム別戦略最適化レポート

生成日時: 2026-01-01 20:35:52

## エグゼクティブサマリー

- データ期間: 2020-01-01 ~ 2025-12-31
- データポイント: 1566 日
- 戦略比較: 固定パラメータ vs レジーム適応

## レジーム別最適パラメータ

### BULL Market

| パラメータ | 値 |
|-----------|----|
| ma_short | 10 |
| ma_long | 30 |
| rsi_oversold | 25 |
| rsi_overbought | 65 |
| position_size_pct | 0.9 |
| stop_loss_pct | 0.015 |

### BEAR Market

| パラメータ | 値 |
|-----------|----|
| ma_short | 20 |
| ma_long | 50 |
| rsi_oversold | 20 |
| rsi_overbought | 70 |
| position_size_pct | 0.7 |
| stop_loss_pct | 0.01 |

### SIDEWAYS Market

| パラメータ | 値 |
|-----------|----|
| bb_period | 15 |
| bb_std | 1.5 |
| rsi_oversold | 25 |
| rsi_overbought | 65 |
| position_size_pct | 0.8 |
| stop_loss_pct | 0.015 |

## 固定戦略パフォーマンス

| メトリクス | 値 |
|-----------|----|
| total_trades | 15.000 |
| winning_trades | 6.000 |
| losing_trades | 9.000 |
| win_rate | 40.000 |
| total_return | -1.976 |
| sharpe_ratio | 0.137 |
| max_drawdown | 6.402 |
| avg_rr_ratio | 1.694 |
| final_capital | 980236.385 |

## 適応戦略パフォーマンス

| メトリクス | 値 |
|-----------|----|
| total_trades | 52.000 |
| winning_trades | 18.000 |
| losing_trades | 34.000 |
| win_rate | 34.615 |
| total_return | -21.789 |
| sharpe_ratio | -0.330 |
| max_drawdown | 24.101 |
| avg_rr_ratio | 1.066 |
| final_capital | 782114.565 |

## 戦略比較

| メトリクス | 固定 | 適応 | 改善率 |
|-----------|------|------|--------|
| sharpe_ratio | 0.137 | -0.330 | -339.96% |
| total_return | -1.976 | -21.789 | -1002.46% |
| win_rate | 40.000 | 34.615 | -13.46% |
| max_drawdown | 6.402 | 24.101 | +276.47% |

## レジーム統計

- 総日数: 1366 日
- レジーム切り替え回数: 35 回
- レジーム分布: {'bull': 793, 'sideways': 484, 'bear': 89}

## 結論

⚠️  **要改善**: 適応戦略のSharpe Ratio改善は-339.96%で、目標の+20%に未達です。

## 次のアクション

1. Phase 4 Agent 1（実データバックテスト）との統合
2. Phase 4 Agent 3（KPI再評価）との統合
3. Phase 4最終検証の実施
