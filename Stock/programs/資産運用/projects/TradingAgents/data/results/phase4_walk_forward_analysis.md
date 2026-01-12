# Walk-forward分析 詳細レポート

**日付**: 2026-01-01
**プロジェクト**: TradingAgents - AI駆動型トレーディング戦略
**分析手法**: Walk-forward Analysis (Rolling Window Cross-Validation)

---

## 1. Walk-forward分析とは

### 1.1 概要

Walk-forward分析は、**時系列データに特化したクロスバリデーション手法**であり、以下の目的で使用される:

1. **オーバーフィッティング検出**: Train期間で最適化したパラメータがTest期間でも機能するか検証
2. **頑健性評価**: 異なる市場環境（時期）でのパフォーマンス安定性を評価
3. **現実的なKPI設定**: 実データ分布に基づく達成可能なKPI目標を設定

### 1.2 通常のバックテストとの違い

| 特徴 | 通常のバックテスト | Walk-forward分析 |
|------|------------------|-----------------|
| データ分割 | Train/Test 1回のみ | 複数のTrain/Testウィンドウ |
| パラメータ最適化 | Trainデータで1回 | 各ウィンドウで最適化 |
| オーバーフィッティング検出 | 困難 | Train-Test乖離で定量評価 |
| 市場環境変化への対応 | 評価困難 | 複数時期で評価可能 |
| KPI統計 | 1つの結果のみ | 分布統計（中央値、四分位） |

---

## 2. 実装仕様

### 2.1 ウィンドウパラメータ

```python
WalkForwardAnalyzer(
    data=historical_data,
    train_months=6,      # 訓練期間: 6ヶ月
    test_months=3,       # テスト期間: 3ヶ月
    step_months=3,       # ローリングステップ: 3ヶ月
    initial_capital=1000000
)
```

### 2.2 ウィンドウ分割の詳細

**データ期間**: 2020-01-01 〜 2025-12-31（6年間）

**期待されるウィンドウ数**: 約20ウィンドウ

```
Window 1:
  Train: 2020-01-01 ~ 2020-06-30 (6ヶ月、180日)
  Test:  2020-07-01 ~ 2020-09-30 (3ヶ月、90日)

Window 2:
  Train: 2020-04-01 ~ 2020-09-30 (6ヶ月)
  Test:  2020-10-01 ~ 2020-12-31 (3ヶ月)

Window 3:
  Train: 2020-07-01 ~ 2020-12-31 (6ヶ月)
  Test:  2021-01-01 ~ 2021-03-31 (3ヶ月)

...

Window 20:
  Train: 2025-01-01 ~ 2025-06-30 (6ヶ月)
  Test:  2025-07-01 ~ 2025-09-30 (3ヶ月)
```

### 2.3 オーバーラップ戦略

**50%オーバーラップ**（ステップ3ヶ月、Train期間6ヶ月）

メリット:
- より多くのウィンドウ数→統計的有意性向上
- 市場環境の連続性を保持
- データの有効活用

デメリット:
- ウィンドウ間の相関が発生
- 独立性は完全ではない（許容範囲内）

---

## 3. 分析プロセス

### 3.1 各ウィンドウでの処理フロー

```
1. データ分割
   ↓
2. Trainデータでパラメータ最適化（Grid Search）
   ↓
3. 最適パラメータを取得
   ↓
4. Testデータで前方検証（最適パラメータ使用）
   ↓
5. Train/Test両方のメトリクスを記録
   ↓
6. Train-Test乖離を計算
```

### 3.2 パラメータ最適化（Grid Search）

**対象パラメータ例**:
```python
param_grid = {
    'position_size_pct': [0.8, 0.9, 0.95],
    'stop_loss_pct': [0.01, 0.02, 0.03],
    'ma_short': [10, 15, 20],
    'ma_long': [20, 30, 40]
}
```

**最適化メトリック**: Sharpe Ratio（リスク調整後リターン）

### 3.3 前方検証（Forward Testing）

- Trainデータで最適化したパラメータをTestデータに適用
- **データリークなし**: TestデータはTrain期間に一切使用されない
- 実際のトレーディングに最も近い検証方法

---

## 4. 評価指標

### 4.1 各ウィンドウで記録されるメトリクス

#### Train期間メトリクス
- Sharpe Ratio
- Total Return (%)
- Win Rate (%)
- Max Drawdown (%)
- Total Trades

#### Test期間メトリクス
- 同上（Trainと同じ指標）

#### オーバーフィッティング指標
- **Degradation (%)** = (Train Sharpe - Test Sharpe) / Train Sharpe × 100
  - 0%: 完璧な一致（現実的には稀）
  - 10-20%: 健全な範囲
  - 30%以上: オーバーフィッティングの疑い
  - 50%以上: 重大な過学習

### 4.2 全体統計

全ウィンドウのTest結果を集計:

| 統計量 | 意味 |
|--------|------|
| Median (中央値) | 50%のウィンドウで達成可能な水準 |
| Q25 (25%ile) | 75%のウィンドウで達成可能（保守的目標） |
| Q75 (75%ile) | 25%のウィンドウで達成可能（挑戦目標） |
| Mean (平均) | 全ウィンドウの平均パフォーマンス |
| Std (標準偏差) | パフォーマンスのばらつき |
| CV (変動係数) | Std / Mean、安定性指標 |

---

## 5. オーバーフィッティング検出

### 5.1 Train-Test乖離の評価

```python
degradation_pct = ((train_sharpe - test_sharpe) / abs(train_sharpe)) * 100
```

#### 評価基準

| Degradation | 評価 | 対応 |
|-------------|------|------|
| 0-10% | 優秀 | 頑健な戦略 |
| 10-20% | 良好 | 許容範囲 |
| 20-30% | 警告 | パラメータ調整推奨 |
| 30%以上 | 失敗 | 戦略の見直し必須 |

### 5.2 複数ウィンドウでの一貫性

**安定した戦略の条件**:
- 80%以上のウィンドウで正のリターン
- 平均Degradation < 30%
- Sharpe RatioのCV < 0.5（変動係数）

---

## 6. KPI統計分析

### 6.1 分布統計の計算

```python
statistics = {
    'sharpe_ratio': {
        'median': 0.65,
        'mean': 0.70,
        'std': 0.35,
        'q25': 0.40,
        'q50': 0.65,
        'q75': 0.90,
        'q90': 1.20,
        'min': -0.20,
        'max': 1.35,
        'coefficient_of_variation': 0.50
    },
    ...
}
```

### 6.2 達成確率の計算

```python
def calculate_achievement_probability(kpi_name, target_value):
    """
    例: Sharpe Ratio 1.0以上を達成したウィンドウの割合
    """
    achieved_windows = sum(test_sharpe >= 1.0 for test_sharpe in all_test_results)
    probability = (achieved_windows / total_windows) * 100
    return probability
```

**例**:
- 目標: Sharpe Ratio 1.0以上
- 達成ウィンドウ数: 6/20
- 達成確率: 30%

### 6.3 3段階KPI目標の提案

```python
targets = {
    'conservative': {
        'sharpe_ratio': Q25,  # 達成確率75%
        'total_return': Q25,
        'win_rate': Q25,
        'max_drawdown': Q75   # worst 25%
    },
    'standard': {
        'sharpe_ratio': Median,  # 達成確率50%
        ...
    },
    'aggressive': {
        'sharpe_ratio': Q75,  # 達成確率25%
        ...
    }
}
```

---

## 7. 可視化

### 7.1 Equity Curve（全ウィンドウ）

```
Equity (JPY)
  1,500,000 |                    ___
            |               ___/
  1,250,000 |          ___/
            |     ___/
  1,000,000 |___/___________________
            |
    750,000 |
            +--------------------------> Time
             W1  W5   W10  W15  W20
```

### 7.2 KPIヒストグラム

```
Sharpe Ratio Distribution
  Frequency
      8 |        ___
        |       |   |
      6 |       |   |___
        |   ___|       |
      4 | _|           |___
        ||_________________|___
      0 +-----------------------> Sharpe Ratio
         -0.5  0.0  0.5  1.0  1.5
               Q25  Q50  Q75
              (0.4)(0.65)(0.9)
```

### 7.3 Box Plot（KPI比較）

```
KPI Distributions (Normalized)
  Z-Score
     2 |           o
       |      ┌────┐
     1 |──────┤    ├──────
       |      │    │
     0 |──────┼────┼──────  Median
       |      │    │
    -1 |──────┤    ├──────
       |      └────┘
    -2 |           o
       +------------------------
         Sharpe  Return  Win  Drawdown
```

---

## 8. 実装の使い方

### 8.1 基本的な使用例

```python
from src.backtest.walk_forward_analyzer import WalkForwardAnalyzer
import pandas as pd

# データロード
data = pd.read_csv('data/market_data/btc_usd_daily.csv')

# アナライザー初期化
analyzer = WalkForwardAnalyzer(
    data=data,
    train_months=6,
    test_months=3,
    step_months=3
)

# 戦略関数定義
def moving_average_strategy(data, ma_short=10, ma_long=20):
    # 移動平均クロスオーバー戦略
    signals = []
    data_copy = data.copy()

    if 'date' not in data_copy.columns:
        data_copy = data_copy.reset_index()

    data_copy['ma_short'] = data_copy['close'].rolling(ma_short).mean()
    data_copy['ma_long'] = data_copy['close'].rolling(ma_long).mean()

    position = None

    for i in range(ma_long, len(data_copy)):
        row = data_copy.iloc[i]
        prev_row = data_copy.iloc[i-1]

        # Buy: short MA crosses above long MA
        if (row['ma_short'] > row['ma_long'] and
            prev_row['ma_short'] <= prev_row['ma_long'] and
            position is None):

            signals.append({
                'date': row['date'].strftime('%Y-%m-%d'),
                'action': 'buy',
                'entry_price': row['close'],
                'stop_loss': row['close'] * 0.98,
                'take_profit': row['close'] * 1.04
            })
            position = 'long'

        # Sell: short MA crosses below long MA
        elif (row['ma_short'] < row['ma_long'] and
              prev_row['ma_short'] >= prev_row['ma_long'] and
              position == 'long'):

            signals.append({
                'date': row['date'].strftime('%Y-%m-%d'),
                'action': 'sell',
                'exit_price': row['close']
            })
            position = None

    return signals

# パラメータグリッド定義
param_grid = {
    'ma_short': [5, 10, 15],
    'ma_long': [20, 30, 40]
}

# 分析実行
results = analyzer.run_analysis(moving_average_strategy, param_grid)

# 結果表示
print(f"Total Windows: {results['num_windows']}")
print(f"Positive Return Rate: {results['positive_return_rate']:.1f}%")
print(f"Avg Degradation: {results['avg_degradation']:.1f}%")
print(f"Median Sharpe: {results['statistics']['sharpe_ratio']['median']:.2f}")
print(f"Recommendation: {results['recommendation']}")

# 結果エクスポート
analyzer.export_results(results, 'data/results/walk_forward_results.csv')
```

### 8.2 KPI統計分析

```python
from scripts.analyze_kpi_statistics import KPIStatisticsAnalyzer

# アナライザー初期化
kpi_analyzer = KPIStatisticsAnalyzer(results_csv='data/results/walk_forward_results.csv')

# 統計計算
stats = kpi_analyzer.calculate_statistics()

# 目標提案
targets = kpi_analyzer.propose_targets()

# 現行目標との比較
current_targets = {
    'sharpe_ratio': 1.0,
    'total_return': 3.0,
    'win_rate': 60.0,
    'max_drawdown': -10.0
}
comparison = kpi_analyzer.compare_with_current_targets(current_targets)

# 可視化
kpi_analyzer.visualize_distributions(output_dir='data/results/kpi_analysis')

# レポート生成
kpi_analyzer.generate_report(
    output_path='data/results/kpi_statistics_report.md',
    current_targets=current_targets
)
```

---

## 9. 注意事項とベストプラクティス

### 9.1 データ要件

- **最低データ量**: Train + Test期間の2倍以上推奨
  - Train 6ヶ月 + Test 3ヶ月 = 9ヶ月 → 最低18ヶ月必要
  - 統計的有意性のため、2年以上推奨

- **データ品質**: 欠損値、外れ値の事前処理必須

### 9.2 パラメータ設定

- **Train期間**: 長すぎると市場環境変化に対応できない（6ヶ月推奨）
- **Test期間**: 短すぎると評価が不安定（3ヶ月推奨）
- **ステップ**: 50%オーバーラップが一般的

### 9.3 オーバーフィッティング対策

1. **パラメータ数を増やしすぎない**: 最適化変数は3-5個以内
2. **Grid Searchの粒度**: 細かすぎるグリッドは過学習リスク
3. **Degradationモニタリング**: 平均30%以上なら戦略見直し

### 9.4 市場レジームとの統合

- Walk-forward分析とレジーム分析を統合
- 各レジーム別にWalk-forward分析を実行
- レジーム転換期のパフォーマンスを特に注視

---

## 10. 今後の改善案

### 10.1 アンカー型Walk-forward

現行は**ローリング型**（固定ウィンドウが移動）だが、**アンカー型**（Train期間が累積的に増加）も検討可能:

```
Anchored Walk-forward:
  Window 1: Train 2020/01-2020/06, Test 2020/07-2020/09
  Window 2: Train 2020/01-2020/09, Test 2020/10-2020/12
  Window 3: Train 2020/01-2020/12, Test 2021/01-2021/03
```

メリット: より多くのデータで訓練
デメリット: 古いデータの影響が残る

### 10.2 Combinatorial Purged Cross-Validation

より高度な時系列CV手法:
- パージ期間を設けてウィンドウ間の情報リークを完全防止
- エンバーゴ期間（取引実行不可期間）を考慮

### 10.3 Monte Carlo Walk-forward

- 各ウィンドウでMonte Carloシミュレーションを実行
- 信頼区間付きKPI分布を算出

---

## 11. 参考文献

1. Prado, M. L. (2018). *Advances in Financial Machine Learning*. Wiley.
   - Chapter 7: Cross-Validation in Finance
   - Chapter 12: Backtesting through Cross-Validation

2. Aronson, D. (2006). *Evidence-Based Technical Analysis*. Wiley.
   - Chapter 9: Walk-Forward Analysis

3. Pardo, R. (2011). *The Evaluation and Optimization of Trading Strategies* (2nd ed.). Wiley.
   - Chapter 7: Walk-Forward Analysis

---

**作成者**: Agent 3 (KPI Reevaluation & Walk-forward Specialist)
**最終更新**: 2026-01-01
**次回更新予定**: 実データ分析完了後
