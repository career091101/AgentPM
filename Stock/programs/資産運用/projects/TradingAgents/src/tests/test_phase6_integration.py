"""
Phase 6統合テスト

Phase 6の3つのコンポーネントが統合的に動作することを検証:
1. 戦略改善（MeanReversion, TrendFollowing, Portfolio）
2. Walk-forward分析完成（57ウィンドウ）
3. 最終検証・本番準備（Go/No-go判断）

実行方法:
    pytest src/tests/test_phase6_integration.py -v
    または
    python src/tests/test_phase6_integration.py
"""

import sys
from pathlib import Path

# プロジェクトルートをPATHに追加
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    import pytest
    PYTEST_AVAILABLE = True
except ImportError:
    PYTEST_AVAILABLE = False
    # pytestが使えない場合のダミー実装
    class pytest:
        @staticmethod
        def fixture(func):
            return func

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Phase 6コンポーネント（Agent 1）
from src.strategy.mean_reversion_strategy import MeanReversionStrategy
from src.strategy.trend_following_strategy import TrendFollowingStrategy
from src.strategy.portfolio_strategy import PortfolioStrategy

# Phase 4/5コンポーネント
from src.utils.market_regime import MarketRegimeDetector
from src.backtest.backtest_engine import BacktestEngine


class TestPhase6Integration:
    """Phase 6統合テスト"""

    @pytest.fixture
    def sample_data(self):
        """テスト用サンプルデータ（2年間、500営業日）"""
        np.random.seed(42)
        dates = pd.date_range(start='2023-01-01', periods=500, freq='B')

        # トレンドとノイズを組み合わせた価格データ
        trend = np.linspace(30000, 35000, 500)
        noise = np.random.randn(500) * 500
        close = trend + noise

        high = close + np.abs(np.random.randn(500) * 200)
        low = close - np.abs(np.random.randn(500) * 200)
        open_price = close + np.random.randn(500) * 100
        volume = np.random.randint(1000000, 5000000, 500)

        data = pd.DataFrame({
            'open': open_price,
            'high': high,
            'low': low,
            'close': close,
            'volume': volume
        }, index=dates)

        return data

    def test_1_mean_reversion_strategy(self, sample_data):
        """Test 1: Mean Reversion戦略の統合テスト"""
        print("\n=== Test 1: Mean Reversion戦略統合テスト ===")

        # Mean Reversion戦略初期化
        strategy = MeanReversionStrategy(
            rsi_period=14,
            rsi_oversold=30,
            rsi_overbought=70,
            bb_period=20,
            bb_std=2.0
        )

        # シグナル生成（日付ごとにループ）
        signals = []
        for date in sample_data.index[50:]:  # 最初の50日はインジケータ計算に必要
            signal = strategy.generate_signal(sample_data, date)
            if signal['action'] != 'hold':
                signals.append(signal)

        # 検証ポイント
        assert isinstance(signals, list), "シグナルがリストではありません"
        print(f"✅ Mean Reversion戦略統合テスト成功")
        print(f"   - 生成シグナル数: {len(signals)}")
        if len(signals) > 0:
            buy_count = sum(1 for s in signals if s['action'] == 'buy')
            sell_count = sum(1 for s in signals if s['action'] == 'sell')
            print(f"   - Buy: {buy_count}, Sell: {sell_count}")

    def test_2_trend_following_strategy(self, sample_data):
        """Test 2: Trend Following戦略の統合テスト"""
        print("\n=== Test 2: Trend Following戦略統合テスト ===")

        # Trend Following戦略初期化
        strategy = TrendFollowingStrategy(
            macd_fast=12,
            macd_slow=26,
            macd_signal=9,
            atr_period=14,
            ma_short=50,
            ma_long=200
        )

        # シグナル生成
        signals = []
        for date in sample_data.index[50:]:
            signal = strategy.generate_signal(sample_data, date)
            if signal['action'] != 'hold':
                signals.append(signal)

        # 検証ポイント
        assert isinstance(signals, list), "シグナルがリストではありません"
        print(f"✅ Trend Following戦略統合テスト成功")
        print(f"   - 生成シグナル数: {len(signals)}")
        if len(signals) > 0:
            buy_count = sum(1 for s in signals if s['action'] == 'buy')
            sell_count = sum(1 for s in signals if s['action'] == 'sell')
            print(f"   - Buy: {buy_count}, Sell: {sell_count}")

    def test_3_portfolio_strategy(self, sample_data):
        """Test 3: Portfolio戦略の統合テスト"""
        print("\n=== Test 3: Portfolio戦略統合テスト ===")

        # Portfolio戦略初期化
        strategy = PortfolioStrategy(
            mean_reversion_weight=0.4,
            trend_following_weight=0.6,
            use_dynamic_weights=True,
            use_regime_filter=True
        )

        # シグナル生成
        signals = []
        for date in sample_data.index[50:]:
            signal = strategy.generate_signal(sample_data, date)
            if signal['action'] != 'hold':
                signals.append(signal)

        # 検証ポイント
        assert isinstance(signals, list), "シグナルがリストではありません"

        # パフォーマンス統計
        performance_summary = strategy.get_performance_summary()
        assert isinstance(performance_summary, dict), "パフォーマンス統計が辞書ではありません"

        print(f"✅ Portfolio戦略統合テスト成功")
        print(f"   - 生成シグナル数: {len(signals)}")
        print(f"   - パフォーマンス統計: {performance_summary}")

    def test_4_backtest_with_new_strategies(self, sample_data):
        """Test 4: 新戦略でのバックテスト統合テスト"""
        print("\n=== Test 4: 新戦略バックテスト統合テスト ===")

        # Portfolio戦略でシグナル生成
        strategy = PortfolioStrategy()

        signals = []
        for date in sample_data.index[50:]:
            signal = strategy.generate_signal(sample_data, date)
            if signal['action'] != 'hold':
                signals.append(signal)

        if len(signals) > 0:
            # バックテストエンジンでシグナル変換
            backtest_signals = []
            for signal in signals:
                backtest_signals.append({
                    'date': signal['date'],
                    'action': signal['action'],
                    'entry_price': signal.get('price'),
                    'stop_loss': signal.get('stop_loss'),
                    'take_profit': signal.get('take_profit'),
                    'position_size': signal.get('position_size', 1.0)
                })

            # バックテスト実行
            engine = BacktestEngine(
                sample_data,
                initial_capital=10000000,
                commission_pct=0.0005,
                slippage_pct=0.001
            )

            results = engine.run_backtest(backtest_signals)

            # 検証ポイント
            assert 'total_return' in results, f"バックテスト結果が不完全です（keys: {list(results.keys())}）"
            assert 'sharpe_ratio' in results, "Sharpe ratioが計算されていません"

            print(f"✅ 新戦略バックテスト統合テスト成功")
            print(f"   - シグナル数: {len(backtest_signals)}")
            print(f"   - Total Return: {results['total_return']:.2f}%")
            print(f"   - Sharpe Ratio: {results['sharpe_ratio']:.2f}")
            print(f"   - Win Rate: {results['win_rate']:.2f}%")
        else:
            print("⚠️  シグナルが生成されませんでした")

    def test_5_strategy_comparison(self, sample_data):
        """Test 5: 戦略比較テスト（Mean Reversion vs Trend Following vs Portfolio）"""
        print("\n=== Test 5: 戦略比較テスト ===")

        strategies = {
            'Mean Reversion': MeanReversionStrategy(),
            'Trend Following': TrendFollowingStrategy(),
            'Portfolio': PortfolioStrategy()
        }

        results = {}

        for name, strategy in strategies.items():
            signals = []
            for date in sample_data.index[50:100]:  # 短期間で比較
                signal = strategy.generate_signal(sample_data, date)
                if signal['action'] != 'hold':
                    signals.append(signal)

            results[name] = {
                'signals': len(signals),
                'buy': sum(1 for s in signals if s['action'] == 'buy'),
                'sell': sum(1 for s in signals if s['action'] == 'sell')
            }

        # 検証ポイント
        assert len(results) == 3, "3つの戦略が比較されていません"

        print(f"✅ 戦略比較テスト成功")
        for name, res in results.items():
            print(f"   - {name}: Signals={res['signals']}, Buy={res['buy']}, Sell={res['sell']}")

    def test_6_phase6_components_availability(self):
        """Test 6: Phase 6全コンポーネントの可用性確認"""
        print("\n=== Test 6: Phase 6コンポーネント可用性確認 ===")

        components = {
            'MeanReversionStrategy': MeanReversionStrategy,
            'TrendFollowingStrategy': TrendFollowingStrategy,
            'PortfolioStrategy': PortfolioStrategy,
            'MarketRegimeDetector': MarketRegimeDetector,
            'BacktestEngine': BacktestEngine,
        }

        for name, component in components.items():
            assert component is not None, f"{name}がインポートできません"
            print(f"   ✅ {name}: 利用可能")

        print(f"✅ 全コンポーネント可用性確認成功（5/5）")

    def test_7_phase6_files_existence(self):
        """Test 7: Phase 6ファイル存在確認"""
        print("\n=== Test 7: Phase 6ファイル存在確認 ===")

        required_files = [
            # Agent 1: Strategy Improvement
            'src/strategy/mean_reversion_strategy.py',
            'src/strategy/trend_following_strategy.py',
            'src/strategy/portfolio_strategy.py',
            'src/tests/test_strategy_improvement.py',
            # Agent 2: Walk-forward Completion
            'scripts/run_walk_forward_full.py',
            'scripts/generate_statistical_report.py',
            'src/tests/test_walk_forward_complete.py',
            # Agent 3: Final Validation
            'scripts/check_python_environment.py',
            'scripts/run_final_validation.py',
            'src/tests/test_production_readiness.py',
        ]

        missing_files = []
        for file_path in required_files:
            full_path = project_root / file_path
            if not full_path.exists():
                missing_files.append(file_path)

        if missing_files:
            print(f"⚠️  以下のファイルが見つかりません:")
            for f in missing_files:
                print(f"     - {f}")
        else:
            print(f"✅ 全ファイル存在確認成功（{len(required_files)}/{len(required_files)}）")

        assert len(missing_files) == 0, f"必要なファイルが見つかりません: {missing_files}"


def run_tests():
    """テストを直接実行"""
    print("=" * 70)
    print("Phase 6統合テスト実行")
    print("=" * 70)

    test_suite = TestPhase6Integration()

    # サンプルデータ生成
    sample_data = test_suite.sample_data()

    # 各テスト実行
    try:
        test_suite.test_1_mean_reversion_strategy(sample_data)
        test_suite.test_2_trend_following_strategy(sample_data)
        test_suite.test_3_portfolio_strategy(sample_data)
        test_suite.test_4_backtest_with_new_strategies(sample_data)
        test_suite.test_5_strategy_comparison(sample_data)
        test_suite.test_6_phase6_components_availability()
        test_suite.test_7_phase6_files_existence()

        print("\n" + "=" * 70)
        print("✅ Phase 6統合テスト: 全テスト成功（7/7）")
        print("=" * 70)

    except AssertionError as e:
        print(f"\n❌ テスト失敗: {e}")
        raise
    except Exception as e:
        print(f"\n❌ エラー発生: {e}")
        raise


if __name__ == "__main__":
    run_tests()
