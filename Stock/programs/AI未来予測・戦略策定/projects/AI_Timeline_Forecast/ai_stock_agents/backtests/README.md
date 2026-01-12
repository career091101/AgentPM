# AI Stock Agent Backtest System

信頼性の高いバックテストシステム - ルックアヘッドバイアス、サバイバーシップバイアスを厳格に排除

## 概要

このバックテストシステムは、AI株式投資エージェントの戦略を過去データで検証するために設計されています。

### 主な特徴

1. **ルックアヘッドバイアス防止**
   - 二重タイムスタンプ管理（effective_date / as_of_date）
   - T時点の判断にT-1までのデータのみ使用
   - 財務データは発表日ベースで管理

2. **サバイバーシップバイアス対策**
   - IPO情報管理（各企業の上場日）
   - 上場廃止情報管理
   - 各時点で実際に投資可能だった銘柄のみを対象

3. **マーケットレジーム分析**
   - 相場環境を自動判定（上昇トレンド/レンジ/暴落）
   - レジーム別のパフォーマンス測定

4. **ウォークフォワード分析**
   - In-Sample / Out-of-Sample分割
   - ローリングウィンドウによる堅牢性検証
   - 過剰最適化の検出

5. **リアリスティックなコスト計算**
   - 手数料、スプレッド、スリッページを考慮
   - 銘柄流動性に応じたコストモデル

## ディレクトリ構成

```
backtests/
├── README.md                           # 本ドキュメント
├── BACKTEST_DESIGN.md                  # 設計書
├── run_backtest.py                     # CLI実行スクリプト
│
├── core/                               # コアコンポーネント
│   ├── timestamped_data.py             # 時系列データ管理
│   ├── universe_manager.py             # ユニバース履歴管理
│   └── market_regime.py                # レジーム検出器
│
├── engine/                             # エンジン
│   ├── backtest_engine.py              # メインエンジン
│   ├── walk_forward.py                 # ウォークフォワード分析
│   └── cost_model.py                   # コスト・スリッページ
│
├── metrics/                            # メトリクス
│   └── performance_metrics.py          # パフォーマンス指標計算
│
└── data/                               # データ（実行時生成）
    ├── universe_history.json
    ├── earnings_calendar.json
    └── delisting_info.json
```

## クイックスタート

### 1. 環境準備

```bash
# 依存パッケージインストール（プロジェクトルートで）
pip install -r requirements.txt
```

### 2. バックテスト実行

```bash
# シンプルな等ウェイト戦略でテスト（2020-2024年）
python backtests/run_backtest.py \
    --start 2020-01-01 \
    --end 2024-12-31 \
    --capital 1000000 \
    --output results/

# コストなしでテスト（理想的な環境）
python backtests/run_backtest.py \
    --start 2020-01-01 \
    --end 2024-12-31 \
    --no-costs
```

### 3. 結果確認

```bash
# 結果ファイル（JSON）
cat results/backtest_2020-01-01_2024-12-31.json
```

## 使用方法

### カスタム戦略の実装

```python
from datetime import datetime
from typing import Dict, List

def my_ai_strategy(decision_date: datetime, available_tickers: List[str]) -> Dict[str, float]:
    """
    カスタムAI投資戦略

    Args:
        decision_date: 判断日（この日までのデータのみ使用可能）
        available_tickers: 投資可能な銘柄リスト（サバイバーシップバイアス排除済み）

    Returns:
        {ticker: weight} の辞書（合計は1.0）
    """
    # ここに戦略ロジックを実装
    # 例: AI Milestone Proximity Index（AMPI）でウェイト決定

    weights = {}
    # ... 戦略ロジック ...

    return weights
```

### バックテストエンジンの使用

```python
from backtests.engine.backtest_engine import BacktestEngine, BacktestConfig
from backtests.core.timestamped_data import TimeSeriesDataManager
from backtests.core.universe_manager import create_ai_stock_universe
from backtests.engine.cost_model import create_ai_stock_cost_model

# 設定
config = BacktestConfig(
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2024, 12, 31),
    initial_capital=1000000,
)

# 初期化
data_manager = TimeSeriesDataManager()
universe_manager = create_ai_stock_universe()
cost_model = create_ai_stock_cost_model()

engine = BacktestEngine(
    config=config,
    data_manager=data_manager,
    universe_manager=universe_manager,
    cost_model=cost_model,
)

# 実行
result = engine.run(my_ai_strategy)

# 結果表示
print(f"Sharpe Ratio: {result.metrics.sharpe_ratio:.2f}")
print(f"Max Drawdown: {result.metrics.max_drawdown:.2%}")
```

### ウォークフォワード分析

```python
from backtests.engine.walk_forward import WalkForwardAnalyzer, WalkForwardConfig

# 設定
wf_config = WalkForwardConfig(
    start_date=datetime(2020, 1, 1),
    end_date=datetime(2024, 12, 31),
    train_period_months=24,  # 2年訓練
    test_period_months=6,    # 6ヶ月テスト
    anchored=True,           # Anchored Walk-Forward
)

# 分析実行
analyzer = WalkForwardAnalyzer(wf_config)
wf_result = analyzer.run_analysis(my_ai_strategy, returns_data)

# 結果評価
print(f"Avg Test Sharpe: {wf_result.avg_test_sharpe:.2f}")
print(f"Degradation: {wf_result.avg_degradation:.2%}")
```

## バイアス防止の詳細

### ルックアヘッドバイアス防止

```python
from backtests.core.timestamped_data import TimestampedData, DataType
from datetime import datetime

# 例: 2024-Q4決算（2024-12-31期末）が2025-02-05に発表
earnings = TimestampedData(
    effective_date=datetime(2024, 12, 31),  # 決算期末日
    as_of_date=datetime(2025, 2, 5),        # 発表日
    value={"revenue": 1000000, "eps": 2.5},
    data_type=DataType.FUNDAMENTAL
)

# 2025-02-04時点では利用不可
assert not earnings.is_available_at(datetime(2025, 2, 4))

# 2025-02-05以降は利用可能
assert earnings.is_available_at(datetime(2025, 2, 5))
```

### サバイバーシップバイアス対策

```python
from backtests.core.universe_manager import UniverseManager

universe = create_ai_stock_universe()

# 2020-01-01時点で投資可能な銘柄（IPO日チェック済み）
available_2020 = universe.get_available_tickers(datetime(2020, 1, 1))

# 2024-12-31時点で投資可能な銘柄
available_2024 = universe.get_available_tickers(datetime(2024, 12, 31))

# リスト長は異なる（新規IPO、上場廃止を考慮）
assert len(available_2020) != len(available_2024)
```

## パフォーマンスメトリクス

計算される主な指標：

| カテゴリ | メトリクス |
|---------|-----------|
| **リターン** | 累積リターン、年率リターン、月次リターン |
| **リスク** | 年率ボラティリティ、最大ドローダウン、ドローダウン期間 |
| **リスク調整済み** | シャープレシオ、ソルティノレシオ、カルマーレシオ |
| **トレーディング** | 勝率、プロフィットファクター |
| **ベンチマーク比較** | アルファ、ベータ、情報レシオ |
| **コスト** | 総取引コスト、コストドラッグ |

### 目標基準

| レベル | シャープレシオ | カルマーレシオ | 最大ドローダウン | 勝率 |
|--------|---------------|---------------|----------------|------|
| **Minimum** | > 1.0 | > 0.8 | < -40% | > 50% |
| **Good** | > 1.5 | > 1.2 | < -30% | > 55% |
| **Excellent** | > 2.0 | > 1.8 | < -20% | > 60% |

## トラブルシューティング

### データ不足エラー

```
ValueError: Insufficient data for 2020-01-01. Need at least 252 trading days.
```

**解決策**: start_dateを1年以上遅らせる（レジーム検出には200日MA必要）

### ティッカーが見つからない

```
⚠️  Week 52: No available tickers on 2020-12-28
```

**解決策**: UniverseManagerにティッカーのIPO情報を追加

## 次のステップ

1. **データ統合**: yfinance、SimFin等からの実データ取得実装
2. **AI戦略統合**: AgentSkillsシステムとの連携
3. **可視化**: エクイティカーブ、ドローダウンチャート作成
4. **最適化**: パラメータチューニング機構実装

## 参考資料

- [BACKTEST_DESIGN.md](BACKTEST_DESIGN.md) - 詳細設計書
- [親プロジェクトREADME](../README.md) - AI Timeline Forecast全体概要

---

**作成日**: 2026-01-01
**バージョン**: v1.0
**ステータス**: Phase 3-Week 7 実装完了
