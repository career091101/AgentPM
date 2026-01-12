"""
Walk-forward Analyzer Tests
Test suite for walk-forward analysis functionality.
"""

import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Add src to path
src_path = Path(__file__).parent.parent
sys.path.insert(0, str(src_path))

from backtest.walk_forward_analyzer import WalkForwardAnalyzer, quick_walk_forward
from backtest.backtest_engine import BacktestEngine


class TestWalkForwardAnalyzer:
    """Test suite for WalkForwardAnalyzer"""

    @pytest.fixture
    def sample_data(self):
        """Generate sample OHLCV data for 2 years"""
        dates = pd.date_range('2023-01-01', '2025-01-01', freq='D')
        np.random.seed(42)

        data = pd.DataFrame({
            'date': dates,
            'open': np.random.randint(39000, 41000, len(dates)),
            'high': np.random.randint(39500, 41500, len(dates)),
            'low': np.random.randint(38500, 40500, len(dates)),
            'close': np.random.randint(39000, 41000, len(dates)),
            'volume': np.random.randint(100000, 200000, len(dates))
        })

        return data

    @pytest.fixture
    def sample_strategy(self):
        """Simple moving average crossover strategy"""
        def strategy(data: pd.DataFrame, ma_short: int = 10, ma_long: int = 20) -> list:
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

        return strategy

    def test_initialization(self, sample_data):
        """Test analyzer initialization"""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=3
        )

        assert analyzer.train_months == 6
        assert analyzer.test_months == 3
        assert analyzer.step_months == 3
        assert len(analyzer.data) > 0
        assert isinstance(analyzer.data.index, pd.DatetimeIndex)

    def test_data_splitting(self, sample_data):
        """Test train/test window splitting"""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=3
        )

        windows = analyzer.split_data()

        # Should have multiple windows
        assert len(windows) > 0

        # Check each window
        for train_data, test_data, train_start, test_end in windows:
            # Both windows should have data
            assert len(train_data) > 0
            assert len(test_data) > 0

            # Train should come before test
            assert train_data.index.max() <= test_data.index.min()

            # Dates should be in order
            assert train_start < test_end

    def test_window_overlap(self, sample_data):
        """Test that windows have correct overlap"""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=3  # 50% overlap
        )

        windows = analyzer.split_data()

        if len(windows) >= 2:
            # Check overlap between consecutive windows
            window1_start = windows[0][2]
            window2_start = windows[1][2]

            # Second window should start 3 months after first (step_months)
            expected_diff = pd.DateOffset(months=3)
            actual_diff = window2_start - window1_start

            # Allow some tolerance (within a week)
            assert abs((actual_diff - expected_diff).days) <= 7

    def test_no_data_leakage(self, sample_data):
        """Test that test data is never used in training"""
        analyzer = WalkForwardAnalyzer(data=sample_data)
        windows = analyzer.split_data()

        for train_data, test_data, _, _ in windows:
            # Test dates should all be after train dates
            train_max_date = train_data.index.max()
            test_min_date = test_data.index.min()

            assert test_min_date >= train_max_date

            # No overlapping dates
            train_dates = set(train_data.index)
            test_dates = set(test_data.index)
            assert len(train_dates.intersection(test_dates)) == 0

    def test_optimize_and_test(self, sample_data, sample_strategy):
        """Test parameter optimization and forward testing"""
        analyzer = WalkForwardAnalyzer(data=sample_data)
        windows = analyzer.split_data()

        if len(windows) > 0:
            train_data, test_data, _, _ = windows[0]

            param_grid = {
                'ma_short': [5, 10],
                'ma_long': [20, 30]
            }

            result = analyzer.optimize_and_test(
                train_data=train_data,
                test_data=test_data,
                strategy_function=sample_strategy,
                param_grid=param_grid
            )

            # Check result structure
            assert 'train_metrics' in result
            assert 'test_metrics' in result
            assert 'best_params' in result
            assert 'degradation_pct' in result

            # Check metrics exist
            assert 'sharpe_ratio' in result['train_metrics']
            assert 'sharpe_ratio' in result['test_metrics']

    def test_run_analysis(self, sample_data, sample_strategy):
        """Test full walk-forward analysis"""
        analyzer = WalkForwardAnalyzer(
            data=sample_data,
            train_months=6,
            test_months=3,
            step_months=3
        )

        param_grid = {
            'ma_short': [10, 15],
            'ma_long': [20, 30]
        }

        results = analyzer.run_analysis(
            strategy_function=sample_strategy,
            param_grid=param_grid
        )

        # Check results structure
        assert 'windows' in results
        assert 'statistics' in results
        assert 'num_windows' in results
        assert 'positive_return_rate' in results
        assert 'avg_degradation' in results
        assert 'recommendation' in results

        # Should have multiple windows
        assert len(results['windows']) > 0

        # Statistics should have all KPIs
        assert 'sharpe_ratio' in results['statistics']
        assert 'total_return' in results['statistics']
        assert 'win_rate' in results['statistics']
        assert 'max_drawdown' in results['statistics']

    def test_statistics_calculation(self, sample_data, sample_strategy):
        """Test statistical calculations"""
        analyzer = WalkForwardAnalyzer(data=sample_data)

        param_grid = {'ma_short': [10], 'ma_long': [20]}

        results = analyzer.run_analysis(sample_strategy, param_grid)

        stats = results['statistics']

        # Each KPI should have required statistics
        for kpi_stats in stats.values():
            assert 'median' in kpi_stats
            assert 'mean' in kpi_stats
            assert 'std' in kpi_stats
            assert 'q25' in kpi_stats
            assert 'q50' in kpi_stats
            assert 'q75' in kpi_stats
            assert 'min' in kpi_stats
            assert 'max' in kpi_stats

            # Median should equal q50
            assert abs(kpi_stats['median'] - kpi_stats['q50']) < 0.01

    def test_recommendation_logic(self, sample_data, sample_strategy):
        """Test recommendation generation"""
        analyzer = WalkForwardAnalyzer(data=sample_data)

        param_grid = {'ma_short': [10], 'ma_long': [20]}

        results = analyzer.run_analysis(sample_strategy, param_grid)

        recommendation = results['recommendation']

        # Should be one of the valid recommendations
        assert recommendation in ['strong_pass', 'pass', 'warning', 'fail']

    def test_edge_case_insufficient_data(self):
        """Test with insufficient data"""
        # Only 3 months of data
        short_data = pd.DataFrame({
            'date': pd.date_range('2025-01-01', periods=90, freq='D'),
            'open': np.random.randint(39000, 41000, 90),
            'high': np.random.randint(39500, 41500, 90),
            'low': np.random.randint(38500, 40500, 90),
            'close': np.random.randint(39000, 41000, 90),
            'volume': np.random.randint(100000, 200000, 90)
        })

        analyzer = WalkForwardAnalyzer(
            data=short_data,
            train_months=6,
            test_months=3
        )

        windows = analyzer.split_data()

        # Should have 0 windows (not enough data)
        assert len(windows) == 0

    def test_export_results(self, sample_data, sample_strategy, tmp_path):
        """Test results export to CSV"""
        analyzer = WalkForwardAnalyzer(data=sample_data)

        param_grid = {'ma_short': [10], 'ma_long': [20]}

        results = analyzer.run_analysis(sample_strategy, param_grid)

        # Export to temporary file
        output_file = tmp_path / "test_results.csv"
        analyzer.export_results(results, str(output_file))

        # Check file was created
        assert output_file.exists()

        # Load and verify
        df = pd.read_csv(output_file)
        assert len(df) == len(results['windows'])
        assert 'window_id' in df.columns
        assert 'test_sharpe' in df.columns
        assert 'degradation_pct' in df.columns


class TestQuickWalkForward:
    """Test quick_walk_forward convenience function"""

    def test_quick_walk_forward(self):
        """Test quick_walk_forward wrapper"""
        dates = pd.date_range('2023-01-01', '2025-01-01', freq='D')
        data = pd.DataFrame({
            'date': dates,
            'open': np.random.randint(39000, 41000, len(dates)),
            'high': np.random.randint(39500, 41500, len(dates)),
            'low': np.random.randint(38500, 40500, len(dates)),
            'close': np.random.randint(39000, 41000, len(dates)),
            'volume': np.random.randint(100000, 200000, len(dates))
        })

        def simple_strategy(data: pd.DataFrame) -> list:
            # Just buy and sell randomly
            signals = []
            data_copy = data.copy()
            if 'date' not in data_copy.columns:
                data_copy = data_copy.reset_index()

            # Buy on day 30
            if len(data_copy) > 30:
                signals.append({
                    'date': data_copy.iloc[30]['date'].strftime('%Y-%m-%d'),
                    'action': 'buy',
                    'entry_price': data_copy.iloc[30]['close']
                })

            # Sell on day 60
            if len(data_copy) > 60:
                signals.append({
                    'date': data_copy.iloc[60]['date'].strftime('%Y-%m-%d'),
                    'action': 'sell',
                    'exit_price': data_copy.iloc[60]['close']
                })

            return signals

        param_grid = {}

        results = quick_walk_forward(
            data=data,
            strategy_function=simple_strategy,
            param_grid=param_grid,
            train_months=6,
            test_months=3
        )

        assert 'windows' in results
        assert 'recommendation' in results


# Integration test
def test_full_workflow():
    """Integration test: Full walk-forward workflow"""
    print("\n" + "=" * 60)
    print("Integration Test: Full Walk-forward Workflow")
    print("=" * 60)

    # 1. Generate data
    dates = pd.date_range('2023-01-01', '2025-01-01', freq='D')
    data = pd.DataFrame({
        'date': dates,
        'open': np.random.randint(39000, 41000, len(dates)),
        'high': np.random.randint(39500, 41500, len(dates)),
        'low': np.random.randint(38500, 40500, len(dates)),
        'close': np.random.randint(39000, 41000, len(dates)),
        'volume': np.random.randint(100000, 200000, len(dates))
    })

    # 2. Define strategy
    def ma_strategy(data: pd.DataFrame, ma_period: int = 20) -> list:
        signals = []
        data_copy = data.copy()

        if 'date' not in data_copy.columns:
            data_copy = data_copy.reset_index()

        data_copy['ma'] = data_copy['close'].rolling(ma_period).mean()

        position = None

        for i in range(ma_period, len(data_copy)):
            row = data_copy.iloc[i]

            if row['close'] > row['ma'] and position is None:
                signals.append({
                    'date': row['date'].strftime('%Y-%m-%d'),
                    'action': 'buy',
                    'entry_price': row['close']
                })
                position = 'long'

            elif row['close'] < row['ma'] and position == 'long':
                signals.append({
                    'date': row['date'].strftime('%Y-%m-%d'),
                    'action': 'sell',
                    'exit_price': row['close']
                })
                position = None

        return signals

    # 3. Run walk-forward analysis
    analyzer = WalkForwardAnalyzer(data=data)

    param_grid = {'ma_period': [10, 20, 30]}

    results = analyzer.run_analysis(ma_strategy, param_grid)

    # 4. Validate results
    assert len(results['windows']) > 0
    assert 'statistics' in results

    print(f"\n✅ Analyzed {results['num_windows']} windows")
    print(f"   Positive return rate: {results['positive_return_rate']:.1f}%")
    print(f"   Recommendation: {results['recommendation']}")

    print("\n" + "=" * 60)
    print("✅ Integration test passed")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
