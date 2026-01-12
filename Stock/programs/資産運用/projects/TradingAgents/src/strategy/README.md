# Trading Strategies

このディレクトリには、Nikkei 225先物取引用の戦略が含まれています。

## 利用可能な戦略

### 1. Mean Reversion Strategy（平均回帰戦略）

レンジ相場に特化した逆張り戦略。

**使用方法**:

```python
from strategy.mean_reversion_strategy import MeanReversionStrategy

# 初期化
strategy = MeanReversionStrategy(
    rsi_period=14,
    rsi_oversold=30,
    rsi_overbought=70,
    bb_period=20,
    bb_std=2.0,
    position_size=1.0,
    use_volatility_sizing=True
)

# シグナル生成
signal = strategy.generate_signal(data, current_date)

# 結果
print(f"Action: {signal['action']}")  # 'buy', 'sell', or 'hold'
print(f"Confidence: {signal['confidence']}")
print(f"Position Size: {signal['position_size']}")
print(f"Price: {signal['price']}")
print(f"Stop Loss: {signal['stop_loss']}")
```

**適用環境**: Sideways market（レンジ相場）

**シグナルロジック**:
- Buy: RSI < 30 AND Price <= Bollinger Band 下限
- Sell: RSI > 70 AND Price >= Bollinger Band 上限
- Hold: その他

### 2. Trend Following Strategy（トレンドフォロー戦略）

トレンド相場に特化した順張り戦略。

**使用方法**:

```python
from strategy.trend_following_strategy import TrendFollowingStrategy

# 初期化
strategy = TrendFollowingStrategy(
    macd_fast=12,
    macd_slow=26,
    macd_signal=9,
    ma_short=50,
    ma_long=200,
    position_size=1.0,
    use_ma_filter=True
)

# シグナル生成
signal = strategy.generate_signal(data, current_date)
```

**適用環境**: Bull/Bear market（トレンド相場）

**シグナルロジック**:
- Buy: MACD crosses above Signal line (オプション: SMA50 > SMA200)
- Sell: MACD crosses below Signal line
- Hold: その他

### 3. Portfolio Strategy（ポートフォリオ戦略）

複数戦略を組み合わせたリスク分散戦略。

**使用方法**:

```python
from strategy.portfolio_strategy import PortfolioStrategy

# 初期化
portfolio = PortfolioStrategy(
    mean_reversion_weight=0.4,
    trend_following_weight=0.6,
    use_dynamic_weights=True,
    use_regime_filter=True,
    performance_lookback=20
)

# シグナル生成
signal = portfolio.generate_signal(data, current_date)

# 詳細情報
print(f"Current Regime: {signal['regime']}")
print(f"Weights: {signal['weights']}")
print(f"Sub-signals: {signal['sub_signals']}")

# ウェイト履歴を確認
weight_history = portfolio.get_weight_history()
print(weight_history.tail())
```

**適用環境**: すべての市場環境（レジーム認識で自動切り替え）

**特徴**:
- 動的ウェイト調整: パフォーマンスに基づいて自動調整
- レジーム認識: Bull/Bear/Sidewaysを自動判定
- リスク分散: 複数戦略の組み合わせでオーバーフィッティング抑制

### 4. Adaptive Strategy（既存）

動的パラメータ切り替え戦略（Phase 5で実装）。

**使用方法**:

```python
from strategy.adaptive_strategy import AdaptiveStrategy
from utils.market_regime import MarketRegimeDetector

# レジーム検出器を初期化
detector = MarketRegimeDetector(data)

# レジーム別パラメータを定義
regime_params = {
    'bull': {'ma_short': 15, 'ma_long': 40, 'rsi_period': 14},
    'bear': {'ma_short': 30, 'ma_long': 60, 'rsi_period': 14},
    'sideways': {'bb_period': 20, 'bb_std': 2.0, 'rsi_period': 14}
}

# 戦略を初期化
strategy = AdaptiveStrategy(
    regime_detector=detector,
    regime_params=regime_params,
    stability_days=5
)

# シグナル生成
signal = strategy.generate_signal(data, current_date)
```

## データ形式

すべての戦略は同じデータ形式を期待します:

```python
import pandas as pd

# 必須カラム: open, high, low, close, volume
# インデックス: pd.DatetimeIndex
data = pd.DataFrame({
    'open': [...],
    'high': [...],
    'low': [...],
    'close': [...],
    'volume': [...]
}, index=pd.date_range('2020-01-01', '2025-12-31', freq='D'))
```

## シグナル出力形式

すべての戦略は統一されたシグナル形式を返します:

```python
{
    'date': pd.Timestamp,           # シグナル日時
    'action': str,                  # 'buy', 'sell', or 'hold'
    'confidence': float,            # 0-1の信頼度
    'position_size': float,         # ポジションサイズ
    'price': float,                 # 現在価格
    'stop_loss': float or None,     # ストップロス価格
    'indicators': dict,             # 使用したインジケーター値
    'reason': str                   # シグナル理由
}
```

## バックテスト

戦略のバックテストには専用のテストスクリプトを使用:

```bash
# クイックバリデーション
python src/tests/quick_validation.py

# 包括的なバリデーション
python src/tests/run_strategy_validation.py

# pytestでテスト実行
pytest src/tests/test_strategy_improvement.py -v
```

## パフォーマンスメトリクス

バックテストで計算されるメトリクス:

- **Total Return**: 総リターン
- **Sharpe Ratio**: シャープレシオ（年率換算）
- **Win Rate**: 勝率
- **Max Drawdown**: 最大ドローダウン
- **Total Trades**: 総トレード数
- **Average Trade Return**: 平均トレードリターン

## 戦略選択ガイド

### 市場環境別の推奨戦略

| 市場環境 | 推奨戦略 | 理由 |
|---------|---------|------|
| レンジ相場 | Mean Reversion | 平均回帰が効果的 |
| 上昇トレンド | Trend Following | トレンドに順張り |
| 下降トレンド | Trend Following | トレンドに順張り |
| 不明 | Portfolio | リスク分散 |

### オーバーフィッティング対策

1. **Portfolio Strategyを使用**
   - 複数戦略の組み合わせでリスク分散
   - 動的ウェイト調整で過学習を抑制

2. **レジーム認識を有効化**
   - `use_regime_filter=True`
   - 市場環境に応じた自動切り替え

3. **ボラティリティ調整を有効化**
   - `use_volatility_sizing=True`
   - ATRベースのポジションサイジング

4. **Train/Test分割を実施**
   - 80%訓練、20%テスト
   - Train-Test Gap < 30%を目標

## カスタマイズ

### パラメータチューニング

```python
# Mean Reversion Strategy
strategy = MeanReversionStrategy(
    rsi_period=14,          # RSI期間（デフォルト: 14）
    rsi_oversold=25,        # 売られすぎ閾値（デフォルト: 30）
    rsi_overbought=75,      # 買われすぎ閾値（デフォルト: 70）
    bb_period=20,           # BB期間（デフォルト: 20）
    bb_std=2.5,             # BB標準偏差（デフォルト: 2.0）
    position_size=1.0,      # ベースポジションサイズ
    use_volatility_sizing=True
)

# Trend Following Strategy
strategy = TrendFollowingStrategy(
    macd_fast=10,           # MACD短期（デフォルト: 12）
    macd_slow=28,           # MACD長期（デフォルト: 26）
    macd_signal=8,          # シグナルライン（デフォルト: 9）
    ma_short=40,            # 短期MA（デフォルト: 50）
    ma_long=180,            # 長期MA（デフォルト: 200）
    use_ma_filter=True      # MAフィルター使用
)

# Portfolio Strategy
portfolio = PortfolioStrategy(
    mean_reversion_weight=0.3,      # MR重み（デフォルト: 0.4）
    trend_following_weight=0.7,     # TF重み（デフォルト: 0.6）
    use_dynamic_weights=True,       # 動的調整
    performance_lookback=30,        # 評価期間（デフォルト: 20）
    use_regime_filter=True          # レジームフィルター
)
```

### カスタムパラメータ設定

```python
# Mean Reversion用カスタムパラメータ
mr_params = {
    'rsi_period': 14,
    'rsi_oversold': 25,
    'rsi_overbought': 75,
    'bb_period': 20,
    'bb_std': 2.5
}

# Trend Following用カスタムパラメータ
tf_params = {
    'macd_fast': 10,
    'macd_slow': 28,
    'macd_signal': 8,
    'ma_short': 40,
    'ma_long': 180
}

# Portfolioにカスタムパラメータを適用
portfolio = PortfolioStrategy(
    mean_reversion_params=mr_params,
    trend_following_params=tf_params
)
```

## トラブルシューティング

### 問題: シグナルが生成されない

```python
# 原因1: データ不足
# 解決策: 十分なデータ期間を確保（最低200日以上）

# 原因2: 閾値が厳しすぎる
# 解決策: パラメータを調整
strategy = MeanReversionStrategy(
    rsi_oversold=35,  # 30から35に緩和
    rsi_overbought=65  # 70から65に緩和
)
```

### 問題: パフォーマンスが悪い

```python
# 解決策1: Portfolio Strategyを使用
portfolio = PortfolioStrategy(
    use_dynamic_weights=True,
    use_regime_filter=True
)

# 解決策2: ボラティリティ調整を有効化
strategy = MeanReversionStrategy(
    use_volatility_sizing=True
)

# 解決策3: パラメータ最適化
# src/utils/parameter_optimizer.py を使用
```

## 参考資料

- **技術指標**: `src/utils/technical_indicators.py`
- **レジーム検出**: `src/utils/market_regime.py`
- **パラメータ最適化**: `src/utils/parameter_optimizer.py`
- **バックテスト**: `src/tests/test_strategy_improvement.py`
- **実装詳細**: `PHASE6_STRATEGY_IMPROVEMENT.md`

## ライセンス

プロジェクトライセンスに準拠

---

**最終更新**: 2026-01-01
**バージョン**: 1.0.0
**ステータス**: 実装完了、動作確認済み
