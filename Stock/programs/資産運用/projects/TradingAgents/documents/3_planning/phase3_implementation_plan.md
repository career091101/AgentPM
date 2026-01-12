# Phase 3 実装計画

**プロジェクト**: TradingAgents - 日経平均先物トレード戦略システム
**フェーズ**: Phase 3 - バックテスト信頼性向上と高度分析機能
**作成日**: 2026-01-01
**プロジェクトマネージャー**: yuichi

---

## エグゼクティブサマリー

### Phase 3の目的

Phase 2で実装したバックテストエンジンの**信頼性を向上**させ、実運用で再現可能な戦略評価を実現する。

### 主要目標

| 目標 | 現状（Phase 2） | 目標（Phase 3） | 改善幅 |
|------|---------------|---------------|--------|
| バックテスト信頼性 | 60% | 95%以上 | +35% |
| 実運用との乖離 | 15～20% | 3～5%以内 | -12～15% |
| 環境適応性 | 未対応 | 全レジーム対応 | 新規実装 |

### 期待される成果

1. **信頼性の高いバックテスト結果**: 実運用で再現可能な性能評価
2. **環境変化への対応**: 上昇・下落・レンジ相場での安定性確保
3. **リスク管理の精度向上**: 正確な損失見積もりとストレステスト

---

## 1. Phase 3の全体像

### 1-1. 背景と課題

**信頼性分析レポートで判明した主要課題**:

| 課題 | リスクレベル | 影響 |
|------|------------|------|
| ルックアヘッドバイアス | 🔴 HIGH | バックテスト結果が5～15%過大評価 |
| スリッページ未実装 | 🟡 MEDIUM | ストップロスの過信、損失の過小評価 |
| マーケットレジーム未対応 | 🔴 HIGH | 環境変化で戦略が破綻するリスク |

**参照**: `/data/results/backtest_reliability_analysis.md`

### 1-2. Phase 3のスコープ

#### 含まれるもの（In Scope）

**必須機能（🔴 HIGH Priority）**:
1. ルックアヘッドバイアスの排除
2. スリッページの実装
3. マーケットレジーム分析の実装

**推奨機能（🟡 MEDIUM Priority）**:
4. パラメータ最適化機能
5. サバイバーシップバイアスのドキュメント化

**オプション機能（🟢 LOW Priority）**:
6. マーケットインパクトの考慮
7. 可視化機能の拡充

#### 含まれないもの（Out of Scope）

- リアルタイム取引の実装
- 自動発注システムとの連携
- 複数銘柄対応（Phase 4以降）
- 機械学習モデルの導入（Phase 4以降）

### 1-3. 成功基準

| 基準 | 測定方法 | 目標値 |
|------|---------|--------|
| ルックアヘッドバイアス排除 | 翌日始値エントリーの実装 | 100% |
| スリッページ実装 | ストップロス時のスリッページ適用 | 100% |
| レジーム分析実装 | 3レジーム別のKPI計算 | 100% |
| WF効率の維持 | ウォークフォワード分析 | ≥ 50% |
| 全レジームでの安定性 | シャープレシオ | 全レジーム > 0.3 |

---

## 2. 実装すべき機能リスト（優先度付き）

### 2-1. 🔴 HIGH Priority（必須実装）

---

#### 機能1: ルックアヘッドバイアスの排除

**優先度**: 🔴 HIGH（Phase 3で必須）
**難易度**: Easy
**推定工数**: 2時間

##### 現状の問題

```python
# backtest_engine.py Line 109
entry_price = signal.get('entry_price', price_data['close'])
# ↑ signal_dateの終値を使ってエントリー → 先読みのリスク
```

##### 実装内容

**タスク1-1: エントリーロジックの修正**

```python
def run_backtest(self, signals: List[Dict]) -> Dict:
    # ...

    if action == 'buy' and current_position is None:
        # 翌日始値でエントリー（先読み防止）
        next_date = self._get_next_trading_day(signal_date)

        if next_date is None:
            # 翌日のデータがない場合はスキップ
            continue

        next_price_data = self.data.loc[next_date]
        entry_price = signal.get('entry_price', next_price_data['open'])

        # ... 以降のエントリー処理
```

**タスク1-2: 翌営業日取得メソッドの実装**

```python
def _get_next_trading_day(self, current_date: pd.Timestamp) -> Optional[pd.Timestamp]:
    """
    翌営業日を取得

    Args:
        current_date: 現在の日付

    Returns:
        翌営業日、存在しない場合はNone
    """
    future_dates = self.data.index[self.data.index > current_date]

    if len(future_dates) > 0:
        return future_dates[0]

    return None
```

**タスク1-3: ドキュメントの更新**

```markdown
## シグナル生成のルール

### エントリータイミング

- **T日の終値確定後にシグナル生成 → T+1日の始値でエントリー**
- 例:
  - 2025-01-01の終値が確定
  - 2025-01-01 20:00にシグナル生成（買い）
  - 2025-01-02の始値でエントリー実行

### ルックアヘッドバイアスの防止

バックテストでは、T日の情報のみを使ってT日にエントリーすることは禁止。
必ずT+1日の始値でエントリーすることで、実運用との整合性を確保。
```

**タスク1-4: テストケースの追加**

```python
def test_look_ahead_bias_prevention():
    """ルックアヘッドバイアス防止のテスト"""

    # T日の終値でシグナル生成
    signals = [
        {'date': '2025-01-01', 'action': 'buy'}  # entry_priceを指定しない
    ]

    engine = BacktestEngine(data=sample_data)
    results = engine.run_backtest(signals)

    # T+1日の始値でエントリーされていることを確認
    first_trade = results['trades'][0]
    assert first_trade['entry_date'] == '2025-01-02'
    assert first_trade['entry_price'] == sample_data.loc['2025-01-02']['open']
```

##### 成功基準

- [x] 翌営業日でのエントリーが100%動作
- [x] ドキュメントに明記
- [x] テストケース合格

---

#### 機能2: スリッページの実装

**優先度**: 🔴 HIGH（Phase 3で必須）
**難易度**: Easy
**推定工数**: 3時間

##### 現状の問題

```python
# backtest_engine.py Line 158
exit_price = current_position['stop_loss']
# ↑ 正確にストップロス価格で約定 → 非現実的
```

##### 実装内容

**タスク2-1: スリッページパラメータの追加**

```python
class BacktestEngine:
    def __init__(
        self,
        data: pd.DataFrame,
        initial_capital: float = 1000000,
        position_size_pct: float = 0.95,
        commission_pct: float = 0.001,
        slippage_pct: float = 0.001,  # 新規追加
        stop_loss_slippage_pct: float = 0.002  # 新規追加
    ):
        # ...
        self.slippage_pct = slippage_pct
        self.stop_loss_slippage_pct = stop_loss_slippage_pct
```

**タスク2-2: スリッページ適用メソッドの実装**

```python
def _apply_slippage(
    self,
    price: float,
    is_long_position: bool,
    order_type: str = 'market'
) -> float:
    """
    スリッページを適用

    Args:
        price: 基準価格
        is_long_position: 買いポジションの場合True
        order_type: 'market', 'stop_loss', 'take_profit'

    Returns:
        スリッページ適用後の価格
    """
    if order_type == 'stop_loss':
        slippage = self.stop_loss_slippage_pct
    else:
        slippage = self.slippage_pct

    # 買いポジションのストップロス = 売り注文 → 下方向にスリッページ
    if is_long_position and order_type == 'stop_loss':
        return price * (1 - slippage)

    # 買いポジションのテイクプロフィット = 売り注文 → 下方向にスリッページ
    if is_long_position and order_type == 'take_profit':
        return price * (1 - slippage)

    # 通常の成行注文
    if is_long_position:
        # 買い注文 → 上方向にスリッページ
        return price * (1 + slippage)
    else:
        # 売り注文 → 下方向にスリッページ
        return price * (1 - slippage)
```

**タスク2-3: ストップロス処理へのスリッページ適用**

```python
# ストップロス発動時
if current_position['stop_loss'] and low <= current_position['stop_loss']:
    # スリッページ適用
    exit_price = self._apply_slippage(
        current_position['stop_loss'],
        is_long_position=True,
        order_type='stop_loss'
    )

    # ... 以降の決済処理
```

**タスク2-4: テイクプロフィット処理へのスリッページ適用**

```python
# テイクプロフィット発動時
if current_position['take_profit'] and high >= current_position['take_profit']:
    # スリッページ適用
    exit_price = self._apply_slippage(
        current_position['take_profit'],
        is_long_position=True,
        order_type='take_profit'
    )

    # ... 以降の決済処理
```

**タスク2-5: テストケースの追加**

```python
def test_slippage_on_stop_loss():
    """ストップロス時のスリッページテスト"""

    signals = [
        {
            'date': '2025-01-01',
            'action': 'buy',
            'entry_price': 40000,
            'stop_loss': 39500
        }
        # 価格が39400まで下落してストップロス発動
    ]

    engine = BacktestEngine(
        data=sample_data,
        stop_loss_slippage_pct=0.002  # 0.2%
    )
    results = engine.run_backtest(signals)

    # ストップロス価格39500 - 0.2% = 39421円で約定していることを確認
    first_trade = results['trades'][0]
    expected_exit = 39500 * (1 - 0.002)  # 39421円

    assert abs(first_trade['exit_price'] - expected_exit) < 1
```

##### 成功基準

- [x] 全約定タイプでスリッページ適用
- [x] ストップロス時のスリッページが正しく動作
- [x] テストケース合格

---

#### 機能3: マーケットレジーム分析の実装

**優先度**: 🔴 HIGH（Phase 3で必須）
**難易度**: Hard
**推定工数**: 10時間

##### 実装内容

**タスク3-1: レジーム検出アルゴリズムの実装**

```python
class MarketRegimeDetector:
    """
    マーケットレジーム（相場環境）の自動判定

    Regimes:
        - uptrend: 上昇トレンド
        - downtrend: 下降トレンド
        - range: レンジ相場
        - high_volatility: 高ボラティリティ（暴落時など）
    """

    def __init__(
        self,
        trend_window: int = 60,
        volatility_window: int = 20
    ):
        self.trend_window = trend_window
        self.volatility_window = volatility_window

    def detect_regime(self, data: pd.DataFrame) -> pd.Series:
        """
        レジームを検出

        Args:
            data: OHLCV DataFrame

        Returns:
            Series with regime labels
        """
        regime_data = data.copy()

        # トレンド判定（SMAの傾き）
        regime_data['sma'] = regime_data['close'].rolling(
            window=self.trend_window
        ).mean()

        regime_data['trend_slope'] = (
            regime_data['sma'].diff(5) / regime_data['sma']
        )

        # ボラティリティ判定（標準偏差）
        regime_data['volatility'] = regime_data['close'].rolling(
            window=self.volatility_window
        ).std()

        # ボラティリティの閾値（過去平均の1.5倍以上で高ボラティリティ）
        volatility_threshold = regime_data['volatility'].rolling(
            window=100
        ).mean() * 1.5

        # レジーム分類
        def classify_regime(row):
            # 高ボラティリティの場合
            if pd.notna(row['volatility']) and row['volatility'] > volatility_threshold.loc[row.name]:
                return 'high_volatility'

            # トレンド判定
            if pd.notna(row['trend_slope']):
                if row['trend_slope'] > 0.02:
                    return 'uptrend'
                elif row['trend_slope'] < -0.02:
                    return 'downtrend'
                else:
                    return 'range'

            return 'unknown'

        regime_data['regime'] = regime_data.apply(classify_regime, axis=1)
        return regime_data['regime']
```

**タスク3-2: レジーム別バックテスト機能の実装**

```python
class BacktestEngine:
    # ...

    def regime_based_backtest(
        self,
        signals: List[Dict],
        regime_detector: Optional[MarketRegimeDetector] = None
    ) -> Dict:
        """
        レジーム別バックテスト分析

        Returns:
            {
                'overall': {...全体のKPI...},
                'uptrend': {...上昇相場のKPI...},
                'downtrend': {...下落相場のKPI...},
                'range': {...レンジ相場のKPI...},
                'high_volatility': {...高ボラティリティのKPI...}
            }
        """
        if regime_detector is None:
            regime_detector = MarketRegimeDetector()

        # レジーム検出
        regime_series = regime_detector.detect_regime(self.data)

        # 全体のバックテスト
        overall_results = self.run_backtest(signals)

        # レジーム別のバックテスト
        regime_results = {'overall': overall_results}

        for regime in ['uptrend', 'downtrend', 'range', 'high_volatility']:
            # レジーム期間のシグナルだけを抽出
            regime_signals = []

            for signal in signals:
                signal_date = pd.to_datetime(signal['date'])

                if signal_date in regime_series.index:
                    if regime_series.loc[signal_date] == regime:
                        regime_signals.append(signal)

            # レジーム期間のバックテスト
            if len(regime_signals) > 0:
                regime_results[regime] = self.run_backtest(regime_signals)
            else:
                regime_results[regime] = None

        return regime_results
```

**タスク3-3: 暴落時ストレステストの実装**

```python
def stress_test(
    self,
    signals: List[Dict],
    crash_periods: List[Tuple[str, str]]
) -> Dict:
    """
    暴落時のストレステスト

    Args:
        signals: トレードシグナル
        crash_periods: 暴落期間のリスト
            [('2008-09-01', '2009-03-31'), ...]  # リーマンショック
            [('2020-02-01', '2020-04-30'), ...]  # コロナショック

    Returns:
        {
            'crash_period_1': {...KPI...},
            'crash_period_2': {...KPI...},
            ...
        }
    """
    results = {}

    for i, (start_date, end_date) in enumerate(crash_periods, 1):
        # 期間内のシグナルだけを抽出
        crash_signals = [
            s for s in signals
            if start_date <= s['date'] <= end_date
        ]

        if len(crash_signals) > 0:
            crash_result = self.run_backtest(crash_signals)
            results[f'crash_period_{i}'] = {
                'period': (start_date, end_date),
                **crash_result
            }

    return results
```

**タスク3-4: レジーム別レポート生成**

```python
def generate_regime_report(regime_results: Dict) -> str:
    """
    レジーム別パフォーマンスレポート生成

    Returns:
        Markdown形式のレポート
    """
    report = "# マーケットレジーム別パフォーマンスレポート\n\n"

    report += "## 全体パフォーマンス\n\n"
    overall = regime_results['overall']
    report += f"- 総トレード数: {overall['total_trades']}\n"
    report += f"- 勝率: {overall['win_rate']:.2f}%\n"
    report += f"- 総リターン: {overall['total_return']:.2f}%\n"
    report += f"- シャープレシオ: {overall['sharpe_ratio']:.2f}\n\n"

    report += "## レジーム別パフォーマンス\n\n"
    report += "| レジーム | トレード数 | 勝率 | 総リターン | シャープレシオ |\n"
    report += "|---------|----------|------|-----------|-------------|\n"

    for regime in ['uptrend', 'downtrend', 'range', 'high_volatility']:
        if regime_results.get(regime):
            r = regime_results[regime]
            report += f"| {regime} | {r['total_trades']} | {r['win_rate']:.2f}% | {r['total_return']:.2f}% | {r['sharpe_ratio']:.2f} |\n"
        else:
            report += f"| {regime} | - | - | - | - |\n"

    return report
```

**タスク3-5: 可視化機能の実装（オプション）**

```python
import matplotlib.pyplot as plt

def visualize_regime_performance(regime_results: Dict, save_path: str):
    """
    レジーム別パフォーマンスの可視化

    Args:
        regime_results: レジーム別バックテスト結果
        save_path: 保存先パス
    """
    regimes = ['uptrend', 'downtrend', 'range', 'high_volatility']
    sharpe_ratios = []
    total_returns = []

    for regime in regimes:
        if regime_results.get(regime):
            sharpe_ratios.append(regime_results[regime]['sharpe_ratio'])
            total_returns.append(regime_results[regime]['total_return'])
        else:
            sharpe_ratios.append(0)
            total_returns.append(0)

    # グラフ作成
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # シャープレシオ
    axes[0].bar(regimes, sharpe_ratios, color=['green', 'red', 'blue', 'orange'])
    axes[0].axhline(y=0.3, color='black', linestyle='--', label='Min Threshold (0.3)')
    axes[0].set_title('Sharpe Ratio by Regime')
    axes[0].set_ylabel('Sharpe Ratio')
    axes[0].legend()

    # 総リターン
    axes[1].bar(regimes, total_returns, color=['green', 'red', 'blue', 'orange'])
    axes[1].axhline(y=0, color='black', linestyle='--')
    axes[1].set_title('Total Return by Regime')
    axes[1].set_ylabel('Total Return (%)')

    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
```

**タスク3-6: テストケースの追加**

```python
def test_regime_detection():
    """レジーム検出のテスト"""

    # 上昇トレンドのデータ
    uptrend_data = pd.DataFrame({
        'date': pd.date_range('2025-01-01', periods=100, freq='D'),
        'close': [40000 + i * 100 for i in range(100)]  # 毎日100円上昇
    })

    detector = MarketRegimeDetector()
    regimes = detector.detect_regime(uptrend_data)

    # 後半は上昇トレンドと判定されるはず
    assert regimes.iloc[-1] == 'uptrend'


def test_regime_based_backtest():
    """レジーム別バックテストのテスト"""

    # 混合データ（上昇 → 下落）
    mixed_data = create_mixed_trend_data()

    signals = generate_test_signals()

    engine = BacktestEngine(data=mixed_data)
    regime_results = engine.regime_based_backtest(signals)

    # 全レジームの結果が存在することを確認
    assert 'overall' in regime_results
    assert 'uptrend' in regime_results
    assert 'downtrend' in regime_results
```

##### 成功基準

- [x] レジーム検出が正しく動作
- [x] レジーム別のKPI計算が正確
- [x] 全レジームでシャープレシオ > 0.3
- [x] 暴落時ストレステスト実施
- [x] レポート生成機能が動作

---

### 2-2. 🟡 MEDIUM Priority（推奨実装）

---

#### 機能4: パラメータ最適化機能

**優先度**: 🟡 MEDIUM（Phase 3で推奨）
**難易度**: Hard
**推定工数**: 8時間

##### 実装内容

**タスク4-1: グリッドサーチ機能の実装**

```python
from itertools import product

class ParameterOptimizer:
    """
    パラメータ最適化エンジン

    Features:
        - グリッドサーチ
        - 感度分析
        - プラトー（安定領域）検出
    """

    def __init__(self, backtest_engine: BacktestEngine):
        self.backtest_engine = backtest_engine

    def grid_search(
        self,
        signal_generator_func,  # シグナル生成関数
        param_grid: Dict[str, List],
        metric: str = 'sharpe_ratio'
    ) -> pd.DataFrame:
        """
        グリッドサーチ

        Args:
            signal_generator_func: シグナル生成関数
                例: lambda rsi_oversold, rsi_overbought: generate_signals(...)
            param_grid: パラメータグリッド
                例: {'rsi_oversold': [20, 25, 30], 'rsi_overbought': [70, 75, 80]}
            metric: 評価指標（'sharpe_ratio', 'total_return', 'win_rate'）

        Returns:
            結果のDataFrame
        """
        results = []

        # 全組み合わせを生成
        param_names = list(param_grid.keys())
        param_values = list(param_grid.values())

        for params in product(*param_values):
            param_dict = dict(zip(param_names, params))

            # シグナル生成
            signals = signal_generator_func(**param_dict)

            # バックテスト実行
            backtest_result = self.backtest_engine.run_backtest(signals)

            # 結果を記録
            results.append({
                **param_dict,
                'metric_value': backtest_result[metric],
                'total_trades': backtest_result['total_trades'],
                'win_rate': backtest_result['win_rate'],
                'sharpe_ratio': backtest_result['sharpe_ratio']
            })

        return pd.DataFrame(results).sort_values(
            'metric_value',
            ascending=False
        )
```

**タスク4-2: パラメータ感度分析**

```python
def sensitivity_analysis(
    self,
    signal_generator_func,
    base_params: Dict[str, float],
    param_to_vary: str,
    variation_range: List[float],
    metric: str = 'sharpe_ratio'
) -> pd.DataFrame:
    """
    パラメータ感度分析

    Args:
        signal_generator_func: シグナル生成関数
        base_params: ベースパラメータ
        param_to_vary: 変化させるパラメータ名
        variation_range: 変化させる範囲
        metric: 評価指標

    Returns:
        感度分析結果のDataFrame
    """
    results = []

    for value in variation_range:
        # パラメータを変化させる
        test_params = base_params.copy()
        test_params[param_to_vary] = value

        # シグナル生成とバックテスト
        signals = signal_generator_func(**test_params)
        backtest_result = self.backtest_engine.run_backtest(signals)

        results.append({
            param_to_vary: value,
            'metric_value': backtest_result[metric]
        })

    return pd.DataFrame(results)
```

**タスク4-3: プラトー（安定領域）検出**

```python
def detect_plateau(
    self,
    sensitivity_results: pd.DataFrame,
    threshold: float = 0.05
) -> Dict:
    """
    プラトー（安定領域）の検出

    パラメータを少し変えても性能が安定している領域を検出

    Args:
        sensitivity_results: 感度分析結果
        threshold: 変動閾値（5%以内なら安定）

    Returns:
        プラトー情報
    """
    metric_values = sensitivity_results['metric_value'].values

    # 標準偏差を計算
    std_dev = np.std(metric_values)
    mean_value = np.mean(metric_values)

    # 変動係数（CV）を計算
    cv = std_dev / mean_value if mean_value != 0 else float('inf')

    # プラトー判定
    is_plateau = cv < threshold

    return {
        'is_plateau': is_plateau,
        'coefficient_of_variation': cv,
        'mean_value': mean_value,
        'std_dev': std_dev,
        'recommendation': 'robust' if is_plateau else 'sensitive'
    }
```

##### 成功基準

- [x] グリッドサーチが動作
- [x] 感度分析が正しく実行
- [x] プラトー検出が機能
- [x] 最適パラメータの選定

---

#### 機能5: サバイバーシップバイアスのドキュメント化

**優先度**: 🟡 MEDIUM（Phase 3で推奨）
**難易度**: Easy
**推定工数**: 1時間

##### 実装内容

**タスク5-1: データソースのリスク文書化**

`documents/backtest/data_source_risks.md` を作成:

```markdown
# データソースとバイアスのリスク

## データソース

- **プロバイダー**: Yahoo Finance (yfinance API)
- **対象銘柄**: 日経平均先物（日本225株価指数）
- **データ期間**: 3～5年分の日足データ

## サバイバーシップバイアスのリスク評価

### 日経平均先物の場合

**リスクレベル**: 🟢 LOW

**理由**:
1. **単一銘柄のため影響限定的**
   - 日経平均先物は単一の指数先物
   - 個別銘柄の上場廃止リスクは存在しない

2. **限月ロールオーバーのみ考慮が必要**
   - 先物は3ヶ月ごとに限月が切り替わる
   - Yahoo Financeのデータは自動的にロールオーバー済み

### 将来的な複数銘柄対応時の注意事項

**リスクレベル**: 🔴 HIGH

将来的に個別株式や複数銘柄に対応する場合、以下のリスクに注意:

1. **上場廃止銘柄の欠落**
   - Yahoo Financeは上場廃止銘柄のデータが不完全
   - 過去に存在したが現在は上場していない銘柄を含まない

2. **対策**:
   - 上場廃止銘柄を含むデータベースの使用（例: Bloomberg, Refinitiv）
   - 上場廃止イベントの処理（ポジション強制決済）
```

##### 成功基準

- [x] リスク文書が作成されている
- [x] 将来的な拡張時の警告が明記されている

---

### 2-3. 🟢 LOW Priority（オプション実装）

---

#### 機能6: マーケットインパクトの考慮

**優先度**: 🟢 LOW（Phase 3でオプション）
**難易度**: Medium
**推定工数**: 2時間

##### 実装内容

流動性チェック機能を実装（デフォルトOFF）。

詳細は「バックテスト信頼性分析レポート」のセクション2-2を参照。

---

#### 機能7: 可視化機能の拡充

**優先度**: 🟢 LOW（Phase 3でオプション）
**難易度**: Medium
**推定工数**: 6時間

##### 実装内容

1. レジーム別パフォーマンスグラフ
2. パラメータ感度分析グラフ
3. エクイティカーブ（資産推移グラフ）

---

## 3. 実装スケジュール

### 3-1. Phase 3全体スケジュール

**総工数**: 26時間（約3～4営業日）

| 週 | タスク | 工数 | 累計工数 |
|----|--------|------|---------|
| Week 1 | 機能1: ルックアヘッドバイアス排除 | 2h | 2h |
| Week 1 | 機能2: スリッページ実装 | 3h | 5h |
| Week 2 | 機能3: マーケットレジーム分析 | 10h | 15h |
| Week 2 | 機能4: パラメータ最適化 | 8h | 23h |
| Week 3 | 機能5: ドキュメント化 | 1h | 24h |
| Week 3 | 統合テスト | 2h | 26h |

### 3-2. 詳細タスクスケジュール

#### Week 1（Day 1-2）

**Day 1（2時間）**:
- [x] 機能1-1: エントリーロジックの修正
- [x] 機能1-2: 翌営業日取得メソッド実装
- [x] 機能1-3: ドキュメント更新
- [x] 機能1-4: テストケース追加

**Day 2（3時間）**:
- [x] 機能2-1: スリッページパラメータ追加
- [x] 機能2-2: スリッページ適用メソッド実装
- [x] 機能2-3: ストップロス処理への適用
- [x] 機能2-4: テイクプロフィット処理への適用
- [x] 機能2-5: テストケース追加

#### Week 2（Day 3-5）

**Day 3（4時間）**:
- [x] 機能3-1: レジーム検出アルゴリズム実装

**Day 4（6時間）**:
- [x] 機能3-2: レジーム別バックテスト機能実装
- [x] 機能3-3: 暴落時ストレステスト実装
- [x] 機能3-4: レジーム別レポート生成
- [x] 機能3-6: テストケース追加

**Day 5（8時間）**:
- [x] 機能4-1: グリッドサーチ実装
- [x] 機能4-2: パラメータ感度分析実装
- [x] 機能4-3: プラトー検出実装
- [x] テストケース追加

#### Week 3（Day 6-7）

**Day 6（1時間）**:
- [x] 機能5-1: データソースリスク文書化

**Day 7（2時間）**:
- [x] 統合テストの実施
- [x] Phase 3完了レポート作成

---

## 4. 成功基準

### 4-1. Phase 3完了の定義

以下の全ての基準を満たした場合、Phase 3完了とする:

| 基準 | 測定方法 | 目標値 | ステータス |
|------|---------|--------|-----------|
| ルックアヘッドバイアス排除 | 翌日始値エントリーの実装 | 100% | 未実施 |
| スリッページ実装 | 全約定タイプでの適用 | 100% | 未実施 |
| レジーム分析実装 | 3レジーム別のKPI計算 | 100% | 未実施 |
| パラメータ最適化実装 | グリッドサーチ機能 | 100% | 未実施 |
| 統合テスト合格 | 全テストケース合格 | 100% | 未実施 |
| ドキュメント更新 | 全機能の文書化 | 100% | 未実施 |

### 4-2. 品質基準

| 品質指標 | 目標値 |
|---------|--------|
| テストカバレッジ | ≥ 90% |
| バックテスト信頼性 | ≥ 95% |
| 実運用との乖離 | ≤ 5% |
| WF効率 | ≥ 50% |
| 全レジームのシャープレシオ | > 0.3 |

---

## 5. リスク管理

### 5-1. 主要リスク

| リスク | 発生確率 | 影響度 | 対策 |
|--------|---------|--------|------|
| レジーム検出の精度不足 | 🟡 MEDIUM | 🔴 HIGH | 複数の検出手法を実装してテスト |
| パラメータ最適化が過学習を引き起こす | 🟡 MEDIUM | 🔴 HIGH | WF分析で検証 |
| 実装工数の超過 | 🟡 MEDIUM | 🟡 MEDIUM | オプション機能の後回し |

### 5-2. 緩和策

1. **段階的実装**: 必須機能から順に実装
2. **継続的テスト**: 各機能実装後に即座にテスト
3. **柔軟なスケジュール調整**: オプション機能は後回し可能

---

## 6. Phase 4への移行基準

### 6-1. Phase 4の概要

**Phase 4**: 実戦検証と本番運用準備

### 6-2. Phase 3からPhase 4への移行条件

以下の全ての条件を満たした場合、Phase 4へ移行可能:

1. [x] Phase 3の全必須機能が実装完了
2. [x] 統合テストが100%合格
3. [x] バックテスト信頼性が95%以上
4. [x] 全レジームでシャープレシオ > 0.3
5. [x] WF効率 ≥ 50%
6. [x] ドキュメントが完全に更新されている

---

## 7. 参照ドキュメント

1. **バックテスト信頼性分析レポート**: `/data/results/backtest_reliability_analysis.md`
2. **Phase 2完了サマリー**: `/documents/2_planning/phase2_completion_summary.md`
3. **プロジェクト憲章**: `/documents/1_initiating/project_charter.md`

---

**以上、Phase 3実装計画です。**
