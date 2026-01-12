"""
Regime-Specific Parameter Optimizer
Optimizes strategy parameters for each market regime (Bull/Bear/Sideways).

Features:
- Regime-specific parameter grids
- Grid search optimization per regime
- Backtest validation for each regime
- Performance comparison across regimes
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Callable, Optional
import sys
from pathlib import Path

# Add parent to path for imports
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from utils.market_regime import MarketRegimeDetector, RegimeType
from utils.parameter_optimizer import GridSearchOptimizer


class RegimeSpecificOptimizer:
    """
    Optimize trading strategy parameters separately for each market regime.

    Example usage:
        detector = MarketRegimeDetector(data)
        optimizer = RegimeSpecificOptimizer(data, detector, backtest_function)

        # Optimize for bull market
        bull_params = optimizer.optimize_for_regime(
            regime_type=RegimeType.BULL,
            param_grid=bull_param_grid
        )

        # Get all regime-specific parameters
        all_params = optimizer.optimize_all_regimes(param_grids)
    """

    def __init__(
        self,
        data: pd.DataFrame,
        regime_detector: MarketRegimeDetector,
        backtest_function: Callable
    ):
        """
        Initialize regime-specific optimizer.

        Args:
            data: Historical OHLCV data
            regime_detector: MarketRegimeDetector instance
            backtest_function: Function that runs backtest
                              Should accept (data, **params) and return Dict with metrics
        """
        self.data = data.copy()
        self.regime_detector = regime_detector
        self.backtest_function = backtest_function

        # Detect regimes
        self.regime_series = regime_detector.detect_regime_combined()
        self.regime_periods = regime_detector.get_regime_periods(self.regime_series)

        # Validate data
        self._validate_regime_periods()

    def _validate_regime_periods(self):
        """Validate that each regime has sufficient data for optimization."""
        min_days = 60  # Minimum 60 days for meaningful optimization

        for regime_type, periods in self.regime_periods.items():
            total_days = sum((end - start).days for start, end in periods)
            if total_days < min_days:
                print(f"⚠️  Warning: {regime_type} has only {total_days} days (minimum {min_days} recommended)")

    def get_regime_data(self, regime_type: RegimeType) -> pd.DataFrame:
        """
        Extract data for specific regime periods.

        Args:
            regime_type: RegimeType (BULL, BEAR, or SIDEWAYS)

        Returns:
            DataFrame containing only data from specified regime periods
        """
        regime_value = regime_type.value if isinstance(regime_type, RegimeType) else regime_type
        periods = self.regime_periods.get(regime_value, [])

        if not periods:
            raise ValueError(f"No periods found for regime: {regime_value}")

        # Combine all periods for this regime
        regime_data_frames = []
        for start_date, end_date in periods:
            mask = (self.data.index >= start_date) & (self.data.index <= end_date)
            regime_data_frames.append(self.data[mask])

        if not regime_data_frames:
            raise ValueError(f"No data found for regime: {regime_value}")

        return pd.concat(regime_data_frames)

    def optimize_for_regime(
        self,
        regime_type: RegimeType,
        param_grid: Dict[str, List],
        metric: str = 'sharpe_ratio'
    ) -> Dict:
        """
        Optimize parameters for a specific market regime.

        Args:
            regime_type: RegimeType to optimize for
            param_grid: Dictionary of parameters to test
            metric: Metric to optimize (default: 'sharpe_ratio')

        Returns:
            Dict with optimization results:
                {
                    'regime': str,
                    'best_params': Dict,
                    'best_score': float,
                    'optimization_summary': Dict,
                    'regime_stats': Dict
                }
        """
        regime_value = regime_type.value if isinstance(regime_type, RegimeType) else regime_type

        print(f"\n🔍 Optimizing parameters for {regime_value.upper()} market...")

        # Get regime-specific data
        regime_data = self.get_regime_data(regime_type)
        print(f"   Data points: {len(regime_data)} days")

        # Run grid search
        optimizer = GridSearchOptimizer(self.backtest_function)
        opt_results = optimizer.optimize(
            data=regime_data,
            param_grid=param_grid,
            metric=metric,
            maximize=True
        )

        # Calculate regime statistics
        regime_stats = {
            'total_days': len(regime_data),
            'periods': len(self.regime_periods[regime_value]),
            'date_range': (regime_data.index.min(), regime_data.index.max())
        }

        print(f"✅ Best {metric}: {opt_results['best_score']:.3f}")
        print(f"   Parameters: {opt_results['best_params']}")

        return {
            'regime': regime_value,
            'best_params': opt_results['best_params'],
            'best_score': opt_results['best_score'],
            'best_metrics': opt_results.get('best_metrics', {}),
            'optimization_summary': opt_results['optimization_summary'],
            'regime_stats': regime_stats,
            'all_results': opt_results['all_results']
        }

    def optimize_all_regimes(
        self,
        param_grids: Dict[str, Dict[str, List]],
        metric: str = 'sharpe_ratio'
    ) -> Dict[str, Dict]:
        """
        Optimize parameters for all market regimes.

        Args:
            param_grids: Dictionary mapping regime names to parameter grids
                        Example: {
                            'bull': {'ma_short': [10, 15], 'ma_long': [30, 40]},
                            'bear': {'ma_short': [20, 30], 'ma_long': [50, 60]},
                            'sideways': {'bb_period': [15, 20], 'bb_std': [2.0, 2.5]}
                        }
            metric: Metric to optimize

        Returns:
            Dict mapping regime names to optimization results
        """
        results = {}

        for regime_name in ['bull', 'bear', 'sideways']:
            if regime_name not in param_grids:
                print(f"⚠️  Warning: No parameter grid for {regime_name}, skipping")
                continue

            try:
                regime_type = RegimeType(regime_name)
                param_grid = param_grids[regime_name]

                opt_result = self.optimize_for_regime(
                    regime_type=regime_type,
                    param_grid=param_grid,
                    metric=metric
                )

                results[regime_name] = opt_result

            except Exception as e:
                print(f"❌ Error optimizing {regime_name}: {e}")
                results[regime_name] = {'error': str(e)}

        return results

    def backtest_regime_specific(
        self,
        regime_params: Dict[str, Dict]
    ) -> Dict:
        """
        Backtest using regime-specific parameters.

        Args:
            regime_params: Dict mapping regime names to their optimized parameters
                          Example: {
                              'bull': {'ma_short': 15, 'ma_long': 40, ...},
                              'bear': {'ma_short': 30, 'ma_long': 60, ...},
                              'sideways': {'bb_period': 20, 'bb_std': 2.0, ...}
                          }

        Returns:
            Dict with regime-specific backtest results
        """
        results_by_regime = {}

        for regime_name, params in regime_params.items():
            regime_type = RegimeType(regime_name)
            regime_data = self.get_regime_data(regime_type)

            # Run backtest on this regime's data
            backtest_result = self.backtest_function(regime_data, **params)

            results_by_regime[regime_name] = {
                'params': params,
                'metrics': backtest_result,
                'data_points': len(regime_data)
            }

        # Calculate overall statistics
        overall_stats = self._calculate_overall_stats(results_by_regime)

        return {
            'by_regime': results_by_regime,
            'overall': overall_stats
        }

    def _calculate_overall_stats(self, results_by_regime: Dict) -> Dict:
        """Calculate weighted average statistics across all regimes."""
        total_days = sum(r['data_points'] for r in results_by_regime.values())

        weighted_sharpe = 0
        weighted_return = 0
        weighted_winrate = 0

        for regime, result in results_by_regime.items():
            weight = result['data_points'] / total_days
            metrics = result['metrics']

            weighted_sharpe += metrics.get('sharpe_ratio', 0) * weight
            weighted_return += metrics.get('total_return', 0) * weight
            weighted_winrate += metrics.get('win_rate', 0) * weight

        return {
            'weighted_sharpe_ratio': weighted_sharpe,
            'weighted_total_return': weighted_return,
            'weighted_win_rate': weighted_winrate,
            'total_days': total_days
        }

    def compare_with_baseline(
        self,
        regime_params: Dict[str, Dict],
        baseline_params: Dict,
        metric: str = 'sharpe_ratio'
    ) -> Dict:
        """
        Compare regime-specific strategy with baseline fixed parameters.

        Args:
            regime_params: Regime-specific parameters
            baseline_params: Fixed parameters for all regimes
            metric: Metric to compare

        Returns:
            Comparison results with improvement percentages
        """
        # Backtest with regime-specific params
        regime_results = self.backtest_regime_specific(regime_params)

        # Backtest with baseline params on each regime
        baseline_results = {}
        for regime_name in ['bull', 'bear', 'sideways']:
            regime_type = RegimeType(regime_name)
            regime_data = self.get_regime_data(regime_type)

            backtest_result = self.backtest_function(regime_data, **baseline_params)
            baseline_results[regime_name] = {
                'params': baseline_params,
                'metrics': backtest_result,
                'data_points': len(regime_data)
            }

        # Calculate improvements
        improvements = {}
        for regime_name in ['bull', 'bear', 'sideways']:
            regime_score = regime_results['by_regime'][regime_name]['metrics'].get(metric, 0)
            baseline_score = baseline_results[regime_name]['metrics'].get(metric, 0)

            if baseline_score != 0:
                improvement_pct = ((regime_score - baseline_score) / abs(baseline_score)) * 100
            else:
                improvement_pct = 0

            improvements[regime_name] = {
                'regime_score': regime_score,
                'baseline_score': baseline_score,
                'improvement_pct': improvement_pct,
                'improved': improvement_pct > 0
            }

        return {
            'regime_specific': regime_results,
            'baseline': baseline_results,
            'improvements': improvements,
            'overall_improvement': self._calculate_overall_improvement(improvements)
        }

    def _calculate_overall_improvement(self, improvements: Dict) -> float:
        """Calculate average improvement across all regimes."""
        improvement_values = [imp['improvement_pct'] for imp in improvements.values()]
        return np.mean(improvement_values)


# Default parameter grids for each regime
DEFAULT_PARAM_GRIDS = {
    'bull': {
        # Bull: Short-term trend following
        'ma_short': [10, 15, 20],
        'ma_long': [30, 40, 50],
        'rsi_oversold': [25, 30, 35],
        'rsi_overbought': [65, 70, 75],
        'position_size_pct': [0.90, 0.95, 1.00],
        'stop_loss_pct': [0.015, 0.020, 0.025]
    },
    'bear': {
        # Bear: Cautious with longer periods
        'ma_short': [20, 30, 40],
        'ma_long': [50, 60, 70],
        'rsi_oversold': [20, 25, 30],
        'rsi_overbought': [70, 75, 80],
        'position_size_pct': [0.70, 0.80, 0.90],
        'stop_loss_pct': [0.010, 0.015, 0.020]
    },
    'sideways': {
        # Sideways: Mean reversion with Bollinger Bands
        'bb_period': [15, 20, 25],
        'bb_std': [1.5, 2.0, 2.5],
        'rsi_oversold': [25, 30, 35],
        'rsi_overbought': [65, 70, 75],
        'position_size_pct': [0.80, 0.90, 0.95],
        'stop_loss_pct': [0.015, 0.020, 0.025]
    }
}


# Convenience function
def quick_regime_optimization(
    data: pd.DataFrame,
    backtest_function: Callable,
    param_grids: Optional[Dict] = None,
    metric: str = 'sharpe_ratio'
) -> Dict:
    """
    Quick regime-specific optimization wrapper.

    Args:
        data: Historical price data
        backtest_function: Backtest function
        param_grids: Custom parameter grids (default: use DEFAULT_PARAM_GRIDS)
        metric: Optimization metric

    Returns:
        Optimization results for all regimes
    """
    detector = MarketRegimeDetector(data)
    optimizer = RegimeSpecificOptimizer(data, detector, backtest_function)

    grids = param_grids if param_grids is not None else DEFAULT_PARAM_GRIDS

    return optimizer.optimize_all_regimes(grids, metric=metric)


if __name__ == "__main__":
    print("Regime-Specific Optimizer - Test Run")
    print("=" * 60)

    # Sample backtest function
    def sample_backtest(data, **params):
        """Dummy backtest for testing"""
        ma_short = params.get('ma_short', 20)
        ma_long = params.get('ma_long', 50)
        position_size = params.get('position_size_pct', 0.95)

        # Simulate performance
        sharpe = 1.5 * (position_size / 0.95) * (ma_short / ma_long)

        return {
            'sharpe_ratio': sharpe,
            'total_return': sharpe * 15,
            'win_rate': 55 + (position_size * 10),
            'max_drawdown': 12
        }

    # Sample data
    dates = pd.date_range('2020-01-01', '2025-12-31', freq='D')
    sample_data = pd.DataFrame({
        'date': dates,
        'open': np.random.randn(len(dates)).cumsum() + 40000,
        'high': np.random.randn(len(dates)).cumsum() + 40100,
        'low': np.random.randn(len(dates)).cumsum() + 39900,
        'close': np.random.randn(len(dates)).cumsum() + 40000,
        'volume': np.random.randint(1000, 10000, len(dates))
    })
    sample_data['date'] = pd.to_datetime(sample_data['date'])
    sample_data = sample_data.set_index('date')

    print("\n1. Running regime-specific optimization...")
    results = quick_regime_optimization(
        data=sample_data,
        backtest_function=sample_backtest,
        metric='sharpe_ratio'
    )

    print("\n2. Optimization Results:")
    for regime, result in results.items():
        if 'error' not in result:
            print(f"\n{regime.upper()}:")
            print(f"  Best Sharpe: {result['best_score']:.3f}")
            print(f"  Parameters: {result['best_params']}")

    print("\n" + "=" * 60)
    print("✅ Test completed")
