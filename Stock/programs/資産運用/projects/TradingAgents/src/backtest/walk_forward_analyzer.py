"""
Walk-forward Analyzer
Time-series cross-validation for trading strategies using rolling windows.

Features:
- Rolling window data splitting (Train/Test)
- Parameter optimization on Train data
- Forward testing on Test data
- Statistical aggregation across all windows
- Overfitting detection (Train vs Test degradation)
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Callable, Optional
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Add src to path for imports
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from backtest.backtest_engine import BacktestEngine
from utils.parameter_optimizer import GridSearchOptimizer


class WalkForwardAnalyzer:
    """
    Walk-forward analysis engine for time-series cross-validation.

    Example usage:
        analyzer = WalkForwardAnalyzer(
            data=historical_data,
            train_months=6,
            test_months=3,
            step_months=3
        )

        param_grid = {
            'position_size_pct': [0.8, 0.9, 0.95],
            'stop_loss_pct': [0.01, 0.02, 0.03]
        }

        results = analyzer.run_analysis(strategy_function, param_grid)
        print(f"Median Sharpe: {results['statistics']['sharpe_ratio']['median']}")
    """

    def __init__(
        self,
        data: pd.DataFrame,
        train_months: int = 6,
        test_months: int = 3,
        step_months: int = 3,
        initial_capital: float = 1000000
    ):
        """
        Initialize walk-forward analyzer.

        Args:
            data: DataFrame with OHLCV data (columns: date, open, high, low, close, volume)
            train_months: Training window size in months (default: 6)
            test_months: Testing window size in months (default: 3)
            step_months: Rolling step size in months (default: 3, 50% overlap)
            initial_capital: Initial capital for backtest (default: 1,000,000)
        """
        self.data = data.copy()
        self.train_months = train_months
        self.test_months = test_months
        self.step_months = step_months
        self.initial_capital = initial_capital

        # Ensure date column is datetime and set as index
        if 'date' in self.data.columns:
            self.data['date'] = pd.to_datetime(self.data['date'])
            self.data = self.data.set_index('date')

        # Sort by date
        self.data = self.data.sort_index()

    def split_data(self) -> List[Tuple[pd.DataFrame, pd.DataFrame, datetime, datetime]]:
        """
        Split data into Train/Test windows using rolling time-series split.

        Returns:
            List of (train_data, test_data, train_start, test_end) tuples
        """
        windows = []

        start_date = self.data.index.min()
        end_date = self.data.index.max()

        current_start = start_date

        while True:
            # Calculate window boundaries
            train_end = current_start + pd.DateOffset(months=self.train_months)
            test_start = train_end
            test_end = test_start + pd.DateOffset(months=self.test_months)

            # Check if we have enough data
            if test_end > end_date:
                break

            # Extract train and test data
            train_data = self.data[(self.data.index >= current_start) & (self.data.index < train_end)]
            test_data = self.data[(self.data.index >= test_start) & (self.data.index < test_end)]

            # Only add if both windows have data
            if len(train_data) > 0 and len(test_data) > 0:
                windows.append((train_data, test_data, current_start, test_end))

            # Move to next window
            current_start += pd.DateOffset(months=self.step_months)

        return windows

    def optimize_and_test(
        self,
        train_data: pd.DataFrame,
        test_data: pd.DataFrame,
        strategy_function: Callable,
        param_grid: Dict[str, List]
    ) -> Dict:
        """
        Optimize parameters on Train data and test on Test data.

        Args:
            train_data: Training period data
            test_data: Testing period data
            strategy_function: Function that generates signals given (data, **params)
                              Should return List[Dict] of trading signals
            param_grid: Parameter grid for optimization

        Returns:
            Dict with results:
                {
                    'train_metrics': Dict,
                    'test_metrics': Dict,
                    'best_params': Dict,
                    'degradation_pct': float
                }
        """
        # Create backtest wrapper function
        def backtest_wrapper(data: pd.DataFrame, **params) -> Dict:
            """Wrapper to run strategy + backtest"""
            signals = strategy_function(data, **params)
            engine = BacktestEngine(data=data, initial_capital=self.initial_capital)
            results = engine.run_backtest(signals)
            return results

        # Optimize on train data
        optimizer = GridSearchOptimizer(backtest_function=backtest_wrapper)
        optimization_results = optimizer.optimize(
            data=train_data,
            param_grid=param_grid,
            metric='sharpe_ratio',
            maximize=True
        )

        best_params = optimization_results['best_params']
        train_metrics = optimization_results['best_metrics']

        # Test on test data with optimized parameters
        test_results = backtest_wrapper(test_data, **best_params)
        test_metrics = {
            'sharpe_ratio': test_results.get('sharpe_ratio', 0),
            'total_return': test_results.get('total_return', 0),
            'win_rate': test_results.get('win_rate', 0),
            'max_drawdown': test_results.get('max_drawdown', 0),
            'total_trades': test_results.get('total_trades', 0)
        }

        # Calculate degradation (overfitting indicator)
        train_sharpe = train_metrics.get('sharpe_ratio', 0)
        test_sharpe = test_metrics.get('sharpe_ratio', 0)

        degradation_pct = 0
        if train_sharpe != 0:
            degradation_pct = ((train_sharpe - test_sharpe) / abs(train_sharpe)) * 100

        return {
            'train_metrics': train_metrics,
            'test_metrics': test_metrics,
            'best_params': best_params,
            'degradation_pct': float(degradation_pct)
        }

    def run_analysis(
        self,
        strategy_function: Callable,
        param_grid: Dict[str, List]
    ) -> Dict:
        """
        Run complete walk-forward analysis.

        Args:
            strategy_function: Function that generates signals given (data, **params)
            param_grid: Parameter grid for optimization

        Returns:
            Dict with walk-forward analysis results:
                {
                    'windows': List[Dict],  # Results for each window
                    'statistics': Dict,     # Statistical summary across all windows
                    'num_windows': int,
                    'positive_return_rate': float,  # % of windows with positive return
                    'avg_degradation': float,       # Average Train-Test degradation
                    'recommendation': str
                }
        """
        # Split data into windows
        windows = self.split_data()

        if len(windows) == 0:
            raise ValueError("Not enough data for walk-forward analysis")

        print(f"Walk-forward Analysis: {len(windows)} windows")
        print(f"Train window: {self.train_months} months, Test window: {self.test_months} months")
        print(f"Rolling step: {self.step_months} months")
        print("=" * 60)

        # Analyze each window
        window_results = []

        for i, (train_data, test_data, train_start, test_end) in enumerate(windows, 1):
            print(f"\nWindow {i}/{len(windows)}: {train_start.strftime('%Y-%m-%d')} → {test_end.strftime('%Y-%m-%d')}")

            # Optimize and test
            result = self.optimize_and_test(
                train_data=train_data,
                test_data=test_data,
                strategy_function=strategy_function,
                param_grid=param_grid
            )

            # Add window metadata
            window_result = {
                'window_id': i,
                'train_start': train_start.strftime('%Y-%m-%d'),
                'train_end': (train_start + pd.DateOffset(months=self.train_months)).strftime('%Y-%m-%d'),
                'test_start': (train_start + pd.DateOffset(months=self.train_months)).strftime('%Y-%m-%d'),
                'test_end': test_end.strftime('%Y-%m-%d'),
                **result
            }

            window_results.append(window_result)

            # Print window summary
            print(f"  Train: Sharpe={result['train_metrics']['sharpe_ratio']:.2f}, "
                  f"Return={result['train_metrics']['total_return']:.1f}%")
            print(f"  Test:  Sharpe={result['test_metrics']['sharpe_ratio']:.2f}, "
                  f"Return={result['test_metrics']['total_return']:.1f}%")
            print(f"  Degradation: {result['degradation_pct']:.1f}%")

        # Calculate statistics
        statistics = self._calculate_statistics(window_results)

        # Calculate positive return rate
        positive_returns = sum(1 for w in window_results if w['test_metrics']['total_return'] > 0)
        positive_return_rate = (positive_returns / len(window_results)) * 100

        # Average degradation
        avg_degradation = np.mean([w['degradation_pct'] for w in window_results])

        # Generate recommendation
        recommendation = self._generate_recommendation(statistics, positive_return_rate, avg_degradation)

        print("\n" + "=" * 60)
        print("Walk-forward Analysis Summary:")
        print(f"  Total windows: {len(window_results)}")
        print(f"  Positive return rate: {positive_return_rate:.1f}%")
        print(f"  Avg degradation: {avg_degradation:.1f}%")
        print(f"  Median Sharpe: {statistics['sharpe_ratio']['median']:.2f}")
        print(f"  Recommendation: {recommendation}")

        return {
            'windows': window_results,
            'statistics': statistics,
            'num_windows': len(window_results),
            'positive_return_rate': float(positive_return_rate),
            'avg_degradation': float(avg_degradation),
            'recommendation': recommendation
        }

    def _calculate_statistics(self, window_results: List[Dict]) -> Dict:
        """
        Calculate statistical summary across all windows.

        Args:
            window_results: List of window results

        Returns:
            Dict with statistics for each KPI:
                {
                    'sharpe_ratio': {'median': float, 'q25': float, 'q75': float, ...},
                    'total_return': {...},
                    ...
                }
        """
        kpis = ['sharpe_ratio', 'total_return', 'win_rate', 'max_drawdown']
        statistics = {}

        for kpi in kpis:
            # Extract test metrics for this KPI
            values = [w['test_metrics'][kpi] for w in window_results]

            statistics[kpi] = {
                'median': float(np.median(values)),
                'mean': float(np.mean(values)),
                'std': float(np.std(values)),
                'q25': float(np.percentile(values, 25)),
                'q50': float(np.percentile(values, 50)),
                'q75': float(np.percentile(values, 75)),
                'q90': float(np.percentile(values, 90)),
                'min': float(np.min(values)),
                'max': float(np.max(values)),
                'coefficient_of_variation': float(np.std(values) / np.mean(values)) if np.mean(values) != 0 else 0
            }

        return statistics

    def _generate_recommendation(
        self,
        statistics: Dict,
        positive_return_rate: float,
        avg_degradation: float
    ) -> str:
        """
        Generate overall recommendation based on walk-forward results.

        Args:
            statistics: Statistical summary
            positive_return_rate: % of windows with positive return
            avg_degradation: Average Train-Test degradation

        Returns:
            Recommendation string: 'strong_pass', 'pass', 'warning', 'fail'
        """
        # Criteria
        median_sharpe = statistics['sharpe_ratio']['median']
        median_return = statistics['total_return']['median']

        # Strong pass: High performance, low degradation, high consistency
        if (median_sharpe >= 1.0 and
            positive_return_rate >= 80 and
            avg_degradation <= 20):
            return 'strong_pass'

        # Pass: Decent performance, acceptable degradation
        elif (median_sharpe >= 0.5 and
              positive_return_rate >= 60 and
              avg_degradation <= 30):
            return 'pass'

        # Warning: Marginal performance or high degradation
        elif (median_sharpe >= 0 and
              positive_return_rate >= 50 and
              avg_degradation <= 40):
            return 'warning'

        # Fail: Poor performance or severe overfitting
        else:
            return 'fail'

    def export_results(self, results: Dict, output_path: str) -> None:
        """
        Export walk-forward results to CSV.

        Args:
            results: Walk-forward analysis results
            output_path: Path to output CSV file
        """
        # Create DataFrame from window results
        windows_data = []

        for window in results['windows']:
            row = {
                'window_id': window['window_id'],
                'train_start': window['train_start'],
                'train_end': window['train_end'],
                'test_start': window['test_start'],
                'test_end': window['test_end'],
                'train_sharpe': window['train_metrics']['sharpe_ratio'],
                'train_return': window['train_metrics']['total_return'],
                'train_win_rate': window['train_metrics']['win_rate'],
                'test_sharpe': window['test_metrics']['sharpe_ratio'],
                'test_return': window['test_metrics']['total_return'],
                'test_win_rate': window['test_metrics']['win_rate'],
                'test_max_drawdown': window['test_metrics']['max_drawdown'],
                'test_trades': window['test_metrics']['total_trades'],
                'degradation_pct': window['degradation_pct']
            }
            windows_data.append(row)

        df = pd.DataFrame(windows_data)
        df.to_csv(output_path, index=False)

        print(f"\n✅ Walk-forward results exported to: {output_path}")


# Convenience function
def quick_walk_forward(
    data: pd.DataFrame,
    strategy_function: Callable,
    param_grid: Dict[str, List],
    train_months: int = 6,
    test_months: int = 3
) -> Dict:
    """
    Quick walk-forward analysis wrapper.

    Args:
        data: Historical OHLCV data
        strategy_function: Strategy signal generator
        param_grid: Parameter grid
        train_months: Training window size
        test_months: Testing window size

    Returns:
        Walk-forward analysis results
    """
    analyzer = WalkForwardAnalyzer(
        data=data,
        train_months=train_months,
        test_months=test_months
    )

    return analyzer.run_analysis(strategy_function, param_grid)


# Example usage
if __name__ == "__main__":
    print("Walk-forward Analyzer - Test Run")
    print("=" * 60)

    # Sample data (2 years for multiple windows)
    dates = pd.date_range('2023-01-01', '2025-01-01', freq='D')
    sample_data = pd.DataFrame({
        'date': dates,
        'open': np.random.randint(39000, 41000, len(dates)),
        'high': np.random.randint(39500, 41500, len(dates)),
        'low': np.random.randint(38500, 40500, len(dates)),
        'close': np.random.randint(39000, 41000, len(dates)),
        'volume': np.random.randint(100000, 200000, len(dates))
    })

    # Sample strategy function
    def sample_strategy(data: pd.DataFrame, position_size_pct: float = 0.95,
                       stop_loss_pct: float = 0.02) -> List[Dict]:
        """Dummy strategy for testing"""
        signals = []

        # Simple trend-following: buy when close > 20-day MA
        data_copy = data.copy()
        if 'date' not in data_copy.columns:
            data_copy = data_copy.reset_index()

        data_copy['ma20'] = data_copy['close'].rolling(20).mean()

        position = None

        for i in range(20, len(data_copy)):
            row = data_copy.iloc[i]
            prev_row = data_copy.iloc[i-1]

            # Buy signal: close crosses above MA
            if row['close'] > row['ma20'] and prev_row['close'] <= prev_row['ma20'] and position is None:
                signals.append({
                    'date': row['date'].strftime('%Y-%m-%d'),
                    'action': 'buy',
                    'entry_price': row['close'],
                    'stop_loss': row['close'] * (1 - stop_loss_pct),
                    'take_profit': row['close'] * (1 + stop_loss_pct * 2)
                })
                position = 'long'

            # Sell signal: close crosses below MA
            elif row['close'] < row['ma20'] and prev_row['close'] >= prev_row['ma20'] and position == 'long':
                signals.append({
                    'date': row['date'].strftime('%Y-%m-%d'),
                    'action': 'sell',
                    'exit_price': row['close']
                })
                position = None

        return signals

    # Run walk-forward analysis
    param_grid = {
        'position_size_pct': [0.8, 0.9, 0.95],
        'stop_loss_pct': [0.01, 0.02, 0.03]
    }

    results = quick_walk_forward(
        data=sample_data,
        strategy_function=sample_strategy,
        param_grid=param_grid,
        train_months=6,
        test_months=3
    )

    print("\n" + "=" * 60)
    print("✅ Walk-forward analysis completed")
