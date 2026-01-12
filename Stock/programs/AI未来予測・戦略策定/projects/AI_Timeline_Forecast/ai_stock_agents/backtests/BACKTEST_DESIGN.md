# バックテストシステム設計書

## 1. 概要

AI株式投資エージェントの信頼性の高いバックテストシステムを実装する。
過去データでの戦略検証を通じて、未来の実運用での成功確率を高める。

## 2. バイアス防止機構

### 2.1 ルックアヘッドバイアス（Look-Ahead Bias）防止

**定義**: トレード判断時点で「まだ知り得ない情報」を使用してしまう問題

**対策**:

#### A. タイムスタンプ二重管理
すべてのデータに2つの時刻を記録：

```python
@dataclass
class TimestampedData:
    """タイムスタンプ管理用データクラス"""

    # いつの期間のデータか（例: 2024-Q4決算 → 2024-12-31）
    effective_date: datetime

    # いつ時点で入手可能だったか（例: 決算発表日 → 2025-02-05）
    as_of_date: datetime

    # 実際のデータ
    value: Any

    def is_available_at(self, decision_date: datetime) -> bool:
        """指定日時点で利用可能か判定"""
        return decision_date >= self.as_of_date
```

#### B. 週次リバランスのタイミング制御

```
┌─────────────────────────────────────────────────────┐
│ 週次バックテストタイムライン（Monday Rebalance）      │
├─────────────────────────────────────────────────────┤
│                                                     │
│ 金曜終値（T-3）                                      │
│  ↓ データ利用可能（週末に分析）                      │
│ 月曜始値（T）                                        │
│  ├─ 判断実行: この時点で知り得る情報のみ使用         │
│  ├─ 発注: 月曜始値でエントリー                       │
│  └─ 約定: 月曜終値で約定と仮定（スリッページ考慮）    │
│                                                     │
│ NG例: 月曜終値を見て月曜始値で買ったことにする         │
│ OK例: 金曜終値までのデータで月曜始値に発注            │
└─────────────────────────────────────────────────────┘
```

#### C. 財務データの発表日管理

```python
# 決算発表スケジュール管理
EARNINGS_CALENDAR = {
    "GOOGL": {
        "2024-Q4": {
            "fiscal_period_end": "2024-12-31",
            "announcement_date": "2025-02-04",  # 実際の発表日
            "filing_date": "2025-02-05",         # SEC提出日
        }
    }
}

# バックテストでは filing_date 以降のみ利用可能
def get_fundamentals(ticker: str, as_of_date: datetime):
    """指定日時点で入手可能な財務データを取得"""
    available_data = []
    for period, info in EARNINGS_CALENDAR[ticker].items():
        if as_of_date >= info["filing_date"]:
            available_data.append(period)
    return available_data
```

### 2.2 サバイバーシップバイアス（Survivorship Bias）対策

**定義**: 現在上場している銘柄のみでテストし、上場廃止銘柄を除外する問題

**対策**:

#### A. ユニバース履歴管理

```python
@dataclass
class UniverseHistory:
    """投資対象ユニバースの履歴管理"""

    # 各時点での構成銘柄
    constituents: Dict[datetime, List[str]]

    # 上場廃止情報
    delistings: Dict[str, DelistingInfo]

    def get_available_tickers(self, as_of_date: datetime) -> List[str]:
        """指定日時点で投資可能な銘柄リスト"""
        # 上場済み かつ 未廃止 の銘柄のみ返す
        pass

@dataclass
class DelistingInfo:
    ticker: str
    delisting_date: datetime
    reason: str  # "bankruptcy", "merger", "acquisition"
    final_price: float  # 最終取引価格（損失計算用）
```

#### B. AI関連企業の特殊性

AI関連46社は比較的新興企業が多く、長期上場廃止データは限定的。
ただし以下を考慮：

- **IPO日管理**: 各企業のIPO日以降のみデータ利用可能
- **データ欠損処理**: 若い企業は財務履歴が短い
- **M&A処理**: 買収された企業（例: DeepMind → Google）の扱い

```python
AI_STOCK_UNIVERSE = {
    "NVDA": {"ipo_date": "1999-01-22", "category": "Compute"},
    "GOOGL": {"ipo_date": "2004-08-19", "category": "Frontier Labs"},
    # ... 46社
}
```

### 2.3 過剰最適化（Overfitting）防止

**定義**: 過去データに過度に適合し、未来で機能しない戦略になる問題

**対策**:

#### A. In-Sample / Out-of-Sample分割

```
┌──────────────────────────────────────────────────────┐
│ 2020-2024年データ（5年間）                             │
├──────────────────────────────────────────────────────┤
│                                                      │
│ In-Sample (3年): 2020-01 ~ 2022-12                   │
│  └─ パラメータ調整・戦略最適化                         │
│                                                      │
│ Out-of-Sample (2年): 2023-01 ~ 2024-12               │
│  └─ 最適化なし・検証のみ                              │
│                                                      │
│ 判定基準:                                             │
│  - Out-of-Sampleでもシャープレシオ > 1.0              │
│  - In vs Out のリターン差 < 30%                       │
└──────────────────────────────────────────────────────┘
```

#### B. ウォークフォワード分析（Anchored Walk-Forward）

```
┌──────────────────────────────────────────────────────┐
│ ローリングウィンドウによる堅牢性検証                    │
├──────────────────────────────────────────────────────┤
│                                                      │
│ Window 1:                                            │
│  Train: 2020-01 ~ 2021-12 (2年)                      │
│  Test:  2022-01 ~ 2022-06 (6ヶ月)                    │
│                                                      │
│ Window 2:                                            │
│  Train: 2020-01 ~ 2022-06 (2.5年)                    │
│  Test:  2022-07 ~ 2022-12 (6ヶ月)                    │
│                                                      │
│ Window 3:                                            │
│  Train: 2020-01 ~ 2022-12 (3年)                      │
│  Test:  2023-01 ~ 2023-06 (6ヶ月)                    │
│                                                      │
│ ... 最大8ウィンドウ（6ヶ月×8 = 4年テスト期間）         │
│                                                      │
│ 各ウィンドウで独立検証 → 平均パフォーマンス算出         │
└──────────────────────────────────────────────────────┘
```

## 3. マーケットレジーム（Market Regime）分析

### 3.1 レジーム定義

**3つのレジーム**:

1. **上昇トレンド相場（Bull Trend）**
   - S&P500の200日SMA上昇中
   - VIX < 20
   - 例: アベノミクス初期、コロナ後回復

2. **レンジ相場（Sideways Range）**
   - S&P500の200日SMA横ばい（±5%/年）
   - VIX 15-25
   - 例: 2015-2016年

3. **暴落・下降相場（Bear/Crash）**
   - S&P500の200日SMA下降中 or VIX > 30
   - 例: リーマンショック、コロナショック、2022年AI冬

### 3.2 レジーム検出アルゴリズム

```python
def detect_market_regime(date: datetime, spy_data: pd.DataFrame) -> str:
    """
    マーケットレジーム判定

    Returns:
        "bull_trend", "sideways", "bear_crash"
    """
    # S&P500（SPY）の200日移動平均
    sma200 = spy_data["close"].rolling(200).mean()
    sma200_slope = (sma200.iloc[-1] / sma200.iloc[-252] - 1)  # 年率変化率

    # VIX（恐怖指数）
    vix_current = get_vix(date)

    # 最大ドローダウン（過去3ヶ月）
    dd_3m = calculate_drawdown(spy_data, window=63)

    # 判定ロジック
    if vix_current > 30 or dd_3m < -0.15:
        return "bear_crash"
    elif sma200_slope > 0.05 and vix_current < 20:
        return "bull_trend"
    else:
        return "sideways"
```

### 3.3 レジーム別パフォーマンス測定

各レジームでの戦略パフォーマンスを個別測定：

```python
REGIME_PERFORMANCE = {
    "bull_trend": {
        "total_days": 520,
        "total_return": 0.45,
        "sharpe_ratio": 1.8,
        "max_drawdown": -0.12,
    },
    "sideways": {
        "total_days": 380,
        "total_return": 0.08,
        "sharpe_ratio": 0.6,
        "max_drawdown": -0.18,
    },
    "bear_crash": {
        "total_days": 120,
        "total_return": -0.22,
        "sharpe_ratio": -0.3,
        "max_drawdown": -0.35,
    },
}
```

**期待要件**:
- Bull Trend: シャープレシオ > 1.5（AI銘柄でアウトパフォーム）
- Sideways: シャープレシオ > 0.5（市場中立で耐える）
- Bear Crash: 最大ドローダウン < -40%（ディフェンシブに守る）

## 4. コスト・スリッページモデル

### 4.1 取引コスト

```python
TRADING_COSTS = {
    # 手数料（米国株）
    "commission_per_trade": 0.0,  # Interactive Brokers (IBKR) 無料

    # スプレッドコスト（ビッド・アスク）
    "spread_bps": {
        "large_cap": 2,    # 例: NVDA, GOOGL (0.02%)
        "mid_cap": 5,      # 例: PLTR (0.05%)
        "small_cap": 10,   # 例: AI.TO (0.10%)
    },

    # スリッページ（市場インパクト）
    "slippage_bps": {
        "small_order": 1,   # $10K未満 (0.01%)
        "medium_order": 3,  # $10K-$100K (0.03%)
        "large_order": 8,   # $100K以上 (0.08%)
    },
}
```

### 4.2 週次リバランスコスト計算

```python
def calculate_rebalance_cost(
    current_portfolio: Dict[str, float],
    target_portfolio: Dict[str, float],
    portfolio_value: float
) -> float:
    """
    リバランスコスト計算

    Returns:
        総コスト（ドル）
    """
    total_cost = 0.0

    for ticker in set(current_portfolio.keys()) | set(target_portfolio.keys()):
        current_weight = current_portfolio.get(ticker, 0.0)
        target_weight = target_portfolio.get(ticker, 0.0)

        # ウェイト変動量
        weight_change = abs(target_weight - current_weight)

        if weight_change > 0.001:  # 0.1%以上の変動のみ取引
            trade_value = weight_change * portfolio_value

            # スプレッドコスト
            spread_cost = trade_value * get_spread_bps(ticker) / 10000

            # スリッページ
            slippage_cost = trade_value * get_slippage_bps(trade_value) / 10000

            total_cost += spread_cost + slippage_cost

    return total_cost
```

## 5. パフォーマンスメトリクス

### 5.1 基本メトリクス

```python
@dataclass
class BacktestMetrics:
    """バックテスト評価指標"""

    # リターン系
    total_return: float              # 累積リターン
    annualized_return: float         # 年率リターン
    monthly_returns: List[float]     # 月次リターン

    # リスク系
    annualized_volatility: float     # 年率ボラティリティ
    max_drawdown: float              # 最大ドローダウン
    max_drawdown_duration: int       # 最大ドローダウン期間（日数）

    # リスク調整済みリターン
    sharpe_ratio: float              # シャープレシオ（無リスク金利 = 4%）
    sortino_ratio: float             # ソルティノレシオ（下方リスクのみ）
    calmar_ratio: float              # カルマーレシオ（リターン/最大DD）

    # 勝率・ドローダウン
    win_rate: float                  # 勝率（週次リターン > 0の割合）
    profit_factor: float             # プロフィットファクター（総利益/総損失）

    # ベンチマーク比較
    benchmark_return: float          # S&P500リターン
    alpha: float                     # アルファ（超過リターン）
    beta: float                      # ベータ（市場感応度）
    information_ratio: float         # 情報レシオ（アルファ/トラッキングエラー）

    # コスト影響
    gross_return: float              # コスト前リターン
    net_return: float                # コスト後リターン
    total_trading_cost: float        # 総取引コスト
```

### 5.2 目標基準（Target Benchmarks）

```python
TARGET_METRICS = {
    "minimum": {
        "sharpe_ratio": 1.0,
        "calmar_ratio": 0.8,
        "max_drawdown": -0.40,
        "win_rate": 0.50,
    },
    "good": {
        "sharpe_ratio": 1.5,
        "calmar_ratio": 1.2,
        "max_drawdown": -0.30,
        "win_rate": 0.55,
    },
    "excellent": {
        "sharpe_ratio": 2.0,
        "calmar_ratio": 1.8,
        "max_drawdown": -0.20,
        "win_rate": 0.60,
    },
}
```

## 6. バックテスト実行フロー

```
┌──────────────────────────────────────────────────────┐
│ バックテストエンジン実行フロー                          │
├──────────────────────────────────────────────────────┤
│                                                      │
│ 1. データ準備                                         │
│    ├─ 株価データ取得（2020-2024、46社）               │
│    ├─ 財務データ取得（発表日管理）                     │
│    ├─ AIマイルストーンデータ                          │
│    └─ ベンチマーク（SPY, QQQ）                        │
│                                                      │
│ 2. レジーム検出                                       │
│    └─ 各週のマーケットレジーム判定                     │
│                                                      │
│ 3. 週次ループ（Monday Rebalance）                     │
│    ├─ T-1時点のデータで判断                           │
│    ├─ AgentSkills実行                               │
│    ├─ ポートフォリオ決定                              │
│    ├─ 取引コスト計算                                  │
│    ├─ リバランス実行                                  │
│    └─ パフォーマンス記録                              │
│                                                      │
│ 4. メトリクス計算                                     │
│    ├─ リターン・リスク計算                            │
│    ├─ レジーム別パフォーマンス                         │
│    └─ ベンチマーク比較                                │
│                                                      │
│ 5. レポート生成                                       │
│    ├─ エクイティカーブプロット                         │
│    ├─ ドローダウンチャート                            │
│    ├─ レジーム別サマリー                              │
│    └─ JSON結果出力                                   │
└──────────────────────────────────────────────────────┘
```

## 7. 実装ファイル構成

```
backtests/
├── __init__.py
├── BACKTEST_DESIGN.md                  # 本ドキュメント
│
├── core/
│   ├── __init__.py
│   ├── timestamped_data.py             # タイムスタンプ管理
│   ├── universe_manager.py             # ユニバース履歴管理
│   └── market_regime.py                # レジーム検出器
│
├── engine/
│   ├── __init__.py
│   ├── backtest_engine.py              # メインエンジン
│   ├── walk_forward.py                 # ウォークフォワード分析
│   └── cost_model.py                   # コスト・スリッページ
│
├── metrics/
│   ├── __init__.py
│   ├── performance_metrics.py          # メトリクス計算
│   └── regime_analysis.py              # レジーム別分析
│
├── visualization/
│   ├── __init__.py
│   ├── equity_curve.py                 # エクイティカーブ
│   ├── drawdown_chart.py               # ドローダウン可視化
│   └── regime_report.py                # レジーム別レポート
│
├── data/
│   ├── universe_history.json           # ユニバース履歴
│   ├── earnings_calendar.json          # 決算カレンダー
│   └── delisting_info.json             # 上場廃止情報
│
└── run_backtest.py                     # CLI実行スクリプト
```

## 8. 次ステップ

1. ✅ 設計書作成（本ドキュメント）
2. ⏳ 時系列データ管理クラス実装
3. ⏳ サバイバーシップバイアス対策実装
4. ⏳ マーケットレジーム検出器実装
5. ⏳ ウォークフォワード分析エンジン実装
6. ⏳ バックテスト実行エンジン実装
7. ⏳ パフォーマンスメトリクス計算実装
8. ⏳ 結果可視化・レポート生成実装
9. ⏳ 統合テスト実行（2020-2024年データ）

---

**作成日**: 2026-01-01
**バージョン**: v1.0
**作成者**: AI Stock Agent Development Team
