# Trading Agent 不足コンポーネントリスト

**作成日**: 2025-12-30
**分析者**: Claude Sonnet 4.5
**情報ソース**: Exploreエージェント(ab7951a) + プロジェクト構造調査

---

## 概要

Trading Agentプロジェクトは**フォルダ構造のみ存在**し、**Pythonコード実装が0個**という状態です。

- **不足Pythonファイル数**: 29個以上
- **不足設定ファイル数**: 3個
- **不足テストファイル数**: 3個以上
- **合計不足**: **35個以上のファイル**

---

## 1. Pythonコード（src/）

### 1.1 agents/ (0/18ファイル存在)

| # | ファイル名 | 用途 | 優先度 | 依存関係 | 期待される行数 |
|---|-----------|------|-------|---------|--------------|
| **1** | **data_collector.py** | データ収集エージェント | **Critical** | requests, pandas | 150-200行 |
| **2** | **technical_agent.py** | テクニカル分析エージェント | **Critical** | technical_indicators.py | 200-250行 |
| **3** | **strategy_synthesizer.py** | 戦略統合エージェント | **Critical** | なし | 150-200行 |
| **4** | **backtest_validator.py** | バックテスト検証エージェント | **Critical** | backtest_engine.py | 250-300行 |
| 5 | elliott_wave_agent.py | エリオット波動分析 | High | technical_indicators.py | 200-250行 |
| 6 | sentiment_agent.py | センチメント分析 | High | requests | 150-200行 |
| 7 | fundamentals_agent.py | ファンダメンタルズ分析 | Medium | requests, BeautifulSoup | 150-200行 |
| 8 | market_agent.py | マーケット分析 | Medium | technical_indicators.py | 150-200行 |
| 9 | news_agent.py | ニュース分析 | Medium | requests, BeautifulSoup | 100-150行 |
| 10 | bull_researcher.py | 強気シナリオ | Medium | なし | 100-150行 |
| 11 | bear_researcher.py | 弱気シナリオ | Medium | なし | 100-150行 |
| 12 | research_manager.py | リサーチ統合 | Medium | なし | 100-150行 |
| 13 | risky_portfolio.py | 積極的ポートフォリオ | Low | なし | 100-150行 |
| 14 | safe_portfolio.py | 保守的ポートフォリオ | Low | なし | 100-150行 |
| 15 | neutral_portfolio.py | バランス型ポートフォリオ | Low | なし | 100-150行 |
| 16 | risk_manager.py | リスク管理 | Medium | numpy | 150-200行 |
| 17 | fund_manager.py | 資金管理 | Low | なし | 100-150行 |
| 18 | trader.py | トレード実行 | Medium | なし | 150-200行 |

**期待総行数**: 約 2,650-3,650行

#### 詳細機能仕様

**1. data_collector.py**
```python
# 期待される機能
- fetch_current_price() -> dict  # IG証券から現在価格取得
- fetch_historical_data(symbol, years=5) -> pd.DataFrame  # Yahoo Financeから履歴データ
- check_data_completeness(df) -> float  # データ完全性チェック（95%以上）
- fallback_to_alternative_source()  # Investing.comへのフォールバック
- save_to_json(data, filepath)  # market_data.json保存
```

**2. technical_agent.py**
```python
# 期待される機能
- calculate_all_indicators(df) -> dict  # 8指標計算（MA, MACD, RSI等）
- weighted_scoring(indicators) -> float  # 重み付けスコアリング
- generate_entry_exit_prices(df, indicators) -> dict  # エントリー/エグジット/ストップロス価格
- generate_report() -> str  # technical_analysis.md生成
```

**3. strategy_synthesizer.py**
```python
# 期待される機能
- load_agent_results(technical, elliott, sentiment) -> dict  # 3エージェント結果読み込み
- weighted_voting(results, weights=[2.0, 1.8, 1.2]) -> dict  # 重み付け投票
- calculate_entry_price(votes) -> float  # エントリー価格（加重平均）
- calculate_exit_price(votes) -> float  # 目標価格（最も保守的な値）
- calculate_stop_loss(votes) -> float  # ストップロス（最も近い値）
- calculate_risk_reward_ratio() -> float  # R:R比率
- generate_report() -> str  # synthesized_strategy.md生成
```

**4. backtest_validator.py**
```python
# 期待される機能
- load_strategy(filepath) -> dict  # 戦略ファイル読み込み
- split_data(df, ratios=[0.6, 0.2, 0.2]) -> tuple  # Train/Validate/Test分割
- run_backtest(strategy, data) -> dict  # バックテスト実行
- calculate_sharpe_ratio(returns) -> float  # シャープレシオ計算
- walk_forward_analysis() -> dict  # ウォークフォワード分析
- check_bias_prevention() -> bool  # ルックアヘッド/サバイバーシップバイアス検証
- generate_report() -> str  # backtest_validation_report.md生成
```

---

### 1.2 strategies/ (0/3ファイル存在)

| # | ファイル名 | 用途 | 優先度 | 依存関係 | 期待される行数 |
|---|-----------|------|-------|---------|--------------|
| **1** | **ma_cross_strategy.py** | 移動平均クロス戦略 | High | technical_indicators.py | 100-150行 |
| 2 | rsi_strategy.py | RSI戦略 | Medium | technical_indicators.py | 100-150行 |
| 3 | bollinger_strategy.py | ボリンジャーバンド戦略 | Medium | technical_indicators.py | 100-150行 |

**期待総行数**: 約 300-450行

#### 詳細機能仕様

**1. ma_cross_strategy.py**
```python
# 期待される機能
class MACrossStrategy:
    def __init__(self, short_window=50, long_window=200):
        pass
    def generate_signals(self, df) -> pd.DataFrame:  # 売買シグナル生成
        pass
    def calculate_entry_exit(self, df) -> dict:  # エントリー/エグジット価格
        pass
```

---

### 1.3 backtest/ (0/3ファイル存在)

| # | ファイル名 | 用途 | 優先度 | 依存関係 | 期待される行数 |
|---|-----------|------|-------|---------|--------------|
| **1** | **backtest_engine.py** | バックテストエンジン | **Critical** | pandas, numpy | 300-400行 |
| 2 | walk_forward.py | ウォークフォワード分析 | High | backtest_engine.py | 150-200行 |
| 3 | performance_metrics.py | パフォーマンス指標計算 | High | numpy | 100-150行 |

**期待総行数**: 約 550-750行

#### 詳細機能仕様

**1. backtest_engine.py**
```python
# 期待される機能
class BacktestEngine:
    def __init__(self, initial_capital=1000000):
        pass
    def run(self, strategy, data) -> dict:  # バックテスト実行
        pass
    def calculate_returns(self, trades) -> pd.Series:  # リターン計算
        pass
    def calculate_sharpe_ratio(self, returns, risk_free_rate=0.02) -> float:
        pass
    def calculate_max_drawdown(self, equity_curve) -> float:
        pass
    def prevent_look_ahead_bias(self) -> bool:  # ルックアヘッドバイアス防止
        pass
    def prevent_survivorship_bias(self) -> bool:  # サバイバーシップバイアス防止
        pass
    def prevent_overfitting(self, train_sharpe, test_sharpe) -> bool:  # オーバーフィッティング防止
        pass
```

---

### 1.4 data_fetcher/ (0/3ファイル存在)

| # | ファイル名 | 用途 | 優先度 | 依存関係 | 期待される行数 |
|---|-----------|------|-------|---------|--------------|
| **1** | **yahoo_finance_fetcher.py** | Yahoo Financeデータ取得 | **Critical** | yfinance, requests | 100-150行 |
| 2 | ig_securities_fetcher.py | IG証券データ取得 | High | selenium, BeautifulSoup | 150-200行 |
| 3 | cnn_fear_greed_fetcher.py | Fear & Greed Index取得 | Medium | requests, BeautifulSoup | 80-100行 |

**期待総行数**: 約 330-450行

#### 詳細機能仕様

**1. yahoo_finance_fetcher.py**
```python
# 期待される機能
class YahooFinanceFetcher:
    def fetch_historical(self, symbol, years=5) -> pd.DataFrame:
        """
        Returns: DataFrame with columns [Date, Open, High, Low, Close, Volume]
        """
        pass
    def check_data_quality(self, df) -> float:  # データ完全性（%）
        pass
```

**2. ig_securities_fetcher.py**
```python
# 期待される機能
class IGSecuritiesFetcher:
    def fetch_current_price(self, symbol="日経225") -> dict:
        """
        Returns: {"price": 33100.0, "timestamp": "2025-12-30 17:00:00"}
        """
        pass
```

---

### 1.5 utils/ (0/2ファイル存在)

| # | ファイル名 | 用途 | 優先度 | 依存関係 | 期待される行数 |
|---|-----------|------|-------|---------|--------------|
| **1** | **technical_indicators.py** | テクニカル指標計算ライブラリ | **Critical** | pandas, numpy | 200-300行 |
| 2 | logging_utils.py | ロギングユーティリティ | Low | logging | 50-80行 |

**期待総行数**: 約 250-380行

#### 詳細機能仕様

**1. technical_indicators.py**
```python
# 期待される機能
def calculate_sma(df, window=50) -> pd.Series:  # 単純移動平均
    pass
def calculate_ema(df, window=10) -> pd.Series:  # 指数移動平均
    pass
def calculate_macd(df) -> tuple:  # MACD, Signal, Histogram
    pass
def calculate_rsi(df, window=14) -> pd.Series:  # RSI
    pass
def calculate_bollinger_bands(df, window=20) -> tuple:  # Upper, Middle, Lower
    pass
def calculate_atr(df, window=14) -> pd.Series:  # ATR
    pass
def calculate_vwma(df, window=20) -> pd.Series:  # 出来高加重移動平均
    pass
def calculate_stochastic(df, k_window=14) -> tuple:  # %K, %D
    pass
```

---

### Pythonコード合計

| カテゴリ | ファイル数 | 期待総行数 |
|---------|----------|-----------|
| agents/ | 18 | 2,650-3,650行 |
| strategies/ | 3 | 300-450行 |
| backtest/ | 3 | 550-750行 |
| data_fetcher/ | 3 | 330-450行 |
| utils/ | 2 | 250-380行 |
| **合計** | **29** | **4,080-5,680行** |

---

## 2. 設定ファイル（config/）

| # | ファイル名 | 用途 | 優先度 | 期待される内容 |
|---|-----------|------|-------|--------------|
| **1** | **trading_config.yaml** | トレード設定 | High | エントリー/エグジット/ストップロスルール |
| 2 | backtest_config.yaml | バックテスト設定 | Medium | データ期間、WF分割比率、バイアス防止設定 |
| 3 | .env | API認証情報 | High | IG証券、Yahoo Finance APIキー（存在しない可能性） |

**実装状況**: **0/3 (0%)**

### 詳細仕様

**1. trading_config.yaml**
```yaml
# 期待される内容
trading:
  symbol: "日経225"
  style: "swing"  # 1週間スイング
  position_size: 0.02  # 資金の2%

entry:
  confirmation_signals: 2  # 2つ以上のシグナル一致必須

exit:
  target_rr_ratio: 2.0  # リスク・リワード比率 1:2
  trailing_stop: true

stop_loss:
  max_loss_per_trade: 0.02  # 1トレード最大2%損失

risk_management:
  max_drawdown_limit: 0.10  # 最大ドローダウン10%
  max_concurrent_positions: 1  # 同時ポジション数
```

**2. backtest_config.yaml**
```yaml
# 期待される内容
backtest:
  initial_capital: 1000000  # 初期資金100万円
  data_period: 5  # 5年データ
  commission: 0.0003  # 手数料0.03%
  slippage: 0.0001  # スリッページ0.01%

walk_forward:
  train_ratio: 0.6
  validate_ratio: 0.2
  test_ratio: 0.2
  wf_efficiency_threshold: 0.5  # WF効率50%以上

bias_prevention:
  look_ahead_check: true
  survivorship_check: true
  overfitting_threshold: 0.3  # Train vs Test Sharpe差30%以内
```

---

## 3. テストコード（tests/）

| # | ファイル名 | 用途 | 優先度 | テスト対象 |
|---|-----------|------|-------|----------|
| 1 | test_data_collector.py | データ収集テスト | High | data_collector.py |
| 2 | test_technical_agent.py | テクニカル分析テスト | Medium | technical_agent.py |
| 3 | test_backtest_engine.py | バックテストエンジンテスト | High | backtest_engine.py |

**実装状況**: **0/3 (0%)**

### 詳細仕様

**1. test_data_collector.py**
```python
# 期待されるテストケース
def test_fetch_current_price():  # 現在価格取得テスト
    pass
def test_fetch_historical_data():  # 履歴データ取得テスト
    pass
def test_data_completeness_check():  # データ完全性95%テスト
    pass
def test_fallback_source():  # フォールバック機能テスト
    pass
```

---

## 4. その他不足コンポーネント

### 4.1 ドキュメント（完備されている）

| ファイル | 状態 | サイズ |
|---------|------|-------|
| README.md | ✅ 存在 | 18KB |
| knowledge/technical_indicators.md | ✅ 存在 | - |
| knowledge/backtest_methodology.md | ✅ 存在 | - |
| knowledge/risk_management.md | ✅ 存在 | - |

### 4.2 データディレクトリ（構造のみ）

| ディレクトリ | 状態 | 期待されるファイル |
|------------|------|------------------|
| data/market_data/ | ✅ 存在（空） | market_data_{YYYY-MM-DD}.json |
| data/sources/{YYYY-MM-DD}/ | ✅ 存在（空） | - |
| data/results/{YYYY-MM-DD}/ | ✅ 存在（空） | 7ファイル（*_analysis.md等） |

---

## 5. 実装優先順位

### 優先度Critical（即実装、1週間以内）

| # | ファイル | 工数（人日） | 難易度 | 期限 |
|---|---------|------------|-------|------|
| 1 | src/data_fetcher/yahoo_finance_fetcher.py | 1.0 | Medium | 2026-01-03 |
| 2 | src/agents/data_collector.py | 1.5 | Medium | 2026-01-04 |
| 3 | src/utils/technical_indicators.py | 2.0 | Medium | 2026-01-06 |
| 4 | src/agents/technical_agent.py | 2.0 | Medium | 2026-01-08 |
| 5 | src/backtest/backtest_engine.py | 3.0 | High | 2026-01-10 |
| 6 | src/agents/strategy_synthesizer.py | 1.5 | Medium | 2026-01-11 |
| 7 | src/agents/backtest_validator.py | 2.0 | High | 2026-01-13 |
| 8 | config/trading_config.yaml | 0.5 | Low | 2026-01-02 |

**優先度Critical合計**: **13.5人日**

---

### 優先度High（重要、2週間以内）

| # | ファイル | 工数（人日） | 難易度 | 期限 |
|---|---------|------------|-------|------|
| 9 | src/agents/elliott_wave_agent.py | 2.0 | High | 2026-01-15 |
| 10 | src/agents/sentiment_agent.py | 1.5 | Medium | 2026-01-16 |
| 11 | src/strategies/ma_cross_strategy.py | 1.0 | Low | 2026-01-17 |
| 12 | src/data_fetcher/ig_securities_fetcher.py | 2.0 | High | 2026-01-17 |
| 13 | src/backtest/performance_metrics.py | 1.0 | Medium | 2026-01-17 |
| 14 | config/backtest_config.yaml | 0.5 | Low | 2026-01-10 |
| 15 | tests/test_data_collector.py | 1.0 | Medium | 2026-01-17 |
| 16 | tests/test_backtest_engine.py | 1.5 | Medium | 2026-01-17 |

**優先度High合計**: **10.5人日**

---

### 優先度Medium（2週間〜1ヶ月）

| # | ファイル | 工数（人日） | 難易度 |
|---|---------|------------|-------|
| 17-18 | agent-fundamentals-analyst, agent-market-analyst | 各1.5 | Medium |
| 19 | agent-news-analyst | 1.0 | Medium |
| 20-22 | Phase2エージェント（bull/bear/research-manager） | 各1.0 | Medium |
| 23 | src/backtest/walk_forward.py | 2.0 | High |
| 24-25 | strategies/rsi_strategy.py, bollinger_strategy.py | 各1.0 | Low |
| 26 | src/data_fetcher/cnn_fear_greed_fetcher.py | 1.0 | Low |
| 27 | tests/test_technical_agent.py | 1.0 | Medium |

**優先度Medium合計**: 約 **12人日**

---

### 優先度Low（1ヶ月以降）

| # | ファイル | 工数（人日） |
|---|---------|------------|
| 28-31 | Phase3エージェント（risky/safe/neutral-portfolio, risk-manager） | 各1.0 |
| 32-33 | Phase4エージェント（trader, fund-manager） | 各1.5 |
| 34 | src/utils/logging_utils.py | 0.5 |

**優先度Low合計**: 約 **7.5人日**

---

## 6. 実装見積もり総括

| 優先度 | ファイル数 | 工数（人日） | 期限 | 効果 |
|--------|----------|------------|------|------|
| **Critical** | 8 | 13.5 | 2026-01-13 | MVP動作（STEP 1〜7基本実行） |
| **High** | 8 | 10.5 | 2026-01-17 | 全7ステップ完全動作 |
| **Medium** | 11 | 12.0 | 2026-02-14 | Phase2-3機能追加 |
| **Low** | 7 | 7.5 | 2026-02-28 | 全24スキル完全実装 |
| **合計** | **34** | **43.5** | - | - |

---

## 7. 技術スタック（推奨）

| 用途 | 推奨ライブラリ | インストールコマンド |
|------|-------------|-------------------|
| データ取得 | yfinance, requests | `pip install yfinance requests` |
| テクニカル指標 | pandas-ta, ta-lib | `pip install pandas-ta` |
| バックテスト | backtrader | `pip install backtrader` |
| データ分析 | pandas, numpy | `pip install pandas numpy` |
| Webスクレイピング | BeautifulSoup4, selenium | `pip install beautifulsoup4 selenium` |
| 設定管理 | PyYAML, python-dotenv | `pip install PyYAML python-dotenv` |

---

## 8. 次のアクション

### 即座に実施（今日中）

- [ ] requirements.txtの作成（上記技術スタックを記載）
- [ ] config/trading_config.yaml の作成（優先度Critical #8）
- [ ] src/フォルダ構造の確認

### 1週間以内

- [ ] データ取得系の実装（#1-2）: yahoo_finance_fetcher.py, data_collector.py
- [ ] テクニカル指標ライブラリ（#3）: technical_indicators.py
- [ ] テクニカル分析エージェント（#4）: technical_agent.py

### 2週間以内

- [ ] バックテスト系の実装（#5, #7）: backtest_engine.py, backtest_validator.py
- [ ] 戦略統合エージェント（#6）: strategy_synthesizer.py
- [ ] 最小限のテストコード作成（#15-16）

---

## 参照資料

- **Exploreエージェントレポート**: Agent ID ab7951a
- **プロジェクト構造**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents/`
- **README**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents/README.md`

---

**レポート作成日**: 2025-12-30
**作成者**: Claude Sonnet 4.5
**ステータス**: 完了
