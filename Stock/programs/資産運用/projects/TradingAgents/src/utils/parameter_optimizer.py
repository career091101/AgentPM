"""
Parameter Optimizer
Optimize trading strategy parameters using grid search and sensitivity analysis.

Features:
- Grid search for optimal parameters
- Sensitivity analysis for robustness evaluation
- Overfitting detection
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Callable, Any
from itertools import product


class GridSearchOptimizer:
    """
    Grid search optimizer for trading strategy parameters.

    Example usage:
        optimizer = GridSearchOptimizer(backtest_function=run_strategy)
        param_grid = {
            'position_size_pct': [0.8, 0.9, 0.95],
            'stop_loss_pct': [0.01, 0.02, 0.03]
        }
        results = optimizer.optimize(data, param_grid, metric='sharpe_ratio')
        print(f"Best params: {results['best_params']}")
    """

    def __init__(self, backtest_function: Callable):
        """
        Initialize grid search optimizer.

        Args:
            backtest_function: Function that runs backtest with params
                               Should accept (data, **params) and return Dict with metrics
        """
        self.backtest_function = backtest_function

    def optimize(
        self,
        data: pd.DataFrame,
        param_grid: Dict[str, List[Any]],
        metric: str = 'sharpe_ratio',
        maximize: bool = True
    ) -> Dict:
        """
        Run grid search optimization.

        Args:
            data: Historical price data
            param_grid: Dictionary of parameter names and values to test
                       Example: {'position_size_pct': [0.8, 0.9], 'stop_loss': [0.01, 0.02]}
            metric: Metric to optimize (default: 'sharpe_ratio')
            maximize: True to maximize metric, False to minimize (default: True)

        Returns:
            Dict with optimization results:
                {
                    'best_params': Dict,
                    'best_score': float,
                    'all_results': List[Dict],
                    'optimization_summary': Dict
                }
        """
        # Generate all parameter combinations
        param_names = list(param_grid.keys())
        param_values = list(param_grid.values())
        param_combinations = list(product(*param_values))

        results = []

        # Test each parameter combination
        for combo in param_combinations:
            params = dict(zip(param_names, combo))

            try:
                # Run backtest with these parameters
                backtest_result = self.backtest_function(data, **params)

                score = backtest_result.get(metric, 0)

                results.append({
                    'params': params.copy(),
                    'score': float(score),
                    'metrics': {
                        'sharpe_ratio': backtest_result.get('sharpe_ratio', 0),
                        'total_return': backtest_result.get('total_return', 0),
                        'win_rate': backtest_result.get('win_rate', 0),
                        'max_drawdown': backtest_result.get('max_drawdown', 0)
                    }
                })
            except Exception as e:
                # Skip invalid parameter combinations
                results.append({
                    'params': params.copy(),
                    'score': -np.inf if maximize else np.inf,
                    'error': str(e)
                })

        # Find best parameters
        if maximize:
            best_result = max(results, key=lambda x: x['score'])
        else:
            best_result = min(results, key=lambda x: x['score'])

        # Calculate optimization statistics
        scores = [r['score'] for r in results if not np.isinf(r['score'])]

        optimization_summary = {
            'total_combinations': len(param_combinations),
            'valid_results': len(scores),
            'score_mean': float(np.mean(scores)) if scores else 0,
            'score_std': float(np.std(scores)) if scores else 0,
            'score_range': [float(min(scores)), float(max(scores))] if scores else [0, 0]
        }

        return {
            'best_params': best_result['params'],
            'best_score': float(best_result['score']),
            'best_metrics': best_result.get('metrics', {}),
            'all_results': results,
            'optimization_summary': optimization_summary
        }

    def detect_overfitting(
        self,
        train_data: pd.DataFrame,
        test_data: pd.DataFrame,
        best_params: Dict,
        metric: str = 'sharpe_ratio'
    ) -> Dict:
        """
        Detect overfitting by comparing train vs test performance.

        Args:
            train_data: Training period data
            test_data: Test period data
            best_params: Optimized parameters from training
            metric: Metric to compare

        Returns:
            Dict with overfitting analysis:
                {
                    'train_score': float,
                    'test_score': float,
                    'degradation_pct': float,
                    'overfitting_detected': bool
                }
        """
        # Run backtest on train data
        train_result = self.backtest_function(train_data, **best_params)
        train_score = train_result.get(metric, 0)

        # Run backtest on test data
        test_result = self.backtest_function(test_data, **best_params)
        test_score = test_result.get(metric, 0)

        # Calculate degradation
        degradation_pct = 0
        if train_score != 0:
            degradation_pct = ((train_score - test_score) / abs(train_score)) * 100

        # Flag overfitting if test score drops by >30%
        overfitting_detected = degradation_pct > 30

        return {
            'train_score': float(train_score),
            'test_score': float(test_score),
            'degradation_pct': float(degradation_pct),
            'overfitting_detected': overfitting_detected,
            'recommendation': 'fail' if overfitting_detected else 'pass'
        }


class SensitivityAnalyzer:
    """
    Analyze parameter sensitivity and robustness.

    Example usage:
        analyzer = SensitivityAnalyzer(backtest_function=run_strategy)
        base_params = {'position_size_pct': 0.95, 'stop_loss_pct': 0.02}
        results = analyzer.analyze(data, base_params, variation_pct=0.1)
        print(f"Stability score: {results['stability_score']}")
    """

    def __init__(self, backtest_function: Callable):
        """
        Initialize sensitivity analyzer.

        Args:
            backtest_function: Function that runs backtest with params
        """
        self.backtest_function = backtest_function

    def analyze(
        self,
        data: pd.DataFrame,
        base_params: Dict[str, float],
        variation_pct: float = 0.1,
        metric: str = 'sharpe_ratio'
    ) -> Dict:
        """
        Analyze parameter sensitivity.

        Args:
            data: Historical price data
            base_params: Base parameter values
            variation_pct: Percentage to vary parameters (default: 10%)
            metric: Metric to evaluate (default: 'sharpe_ratio')

        Returns:
            Dict with sensitivity analysis:
                {
                    'base_score': float,
                    'sensitivity_by_param': Dict,
                    'stability_score': float (0-100),
                    'plateau_detected': bool
                }
        """
        # Get baseline score
        base_result = self.backtest_function(data, **base_params)
        base_score = base_result.get(metric, 0)

        sensitivity_results = {}
        score_variations = []

        # Test each parameter individually
        for param_name, base_value in base_params.items():
            if not isinstance(base_value, (int, float)):
                continue

            param_scores = []

            # Test -10%, base, +10%
            for multiplier in [1 - variation_pct, 1.0, 1 + variation_pct]:
                test_params = base_params.copy()
                test_params[param_name] = base_value * multiplier

                try:
                    result = self.backtest_function(data, **test_params)
                    score = result.get(metric, 0)
                    param_scores.append(float(score))
                except:
                    param_scores.append(np.nan)

            # Calculate sensitivity (% change in score per % change in parameter)
            valid_scores = [s for s in param_scores if not np.isnan(s)]
            if len(valid_scores) >= 2:
                score_range = max(valid_scores) - min(valid_scores)
                sensitivity = (score_range / abs(base_score)) if base_score != 0 else 0

                sensitivity_results[param_name] = {
                    'scores': param_scores,
                    'sensitivity': float(sensitivity),
                    'score_range': float(score_range)
                }

                score_variations.append(score_range)

        # Calculate overall stability score (lower variation = higher stability)
        avg_variation = np.mean(score_variations) if score_variations else 0
        stability_score = 100 * (1 - min(avg_variation / abs(base_score), 1.0)) if base_score != 0 else 0

        # Detect plateau (stable performance across parameter variations)
        plateau_detected = stability_score > 80

        return {
            'base_score': float(base_score),
            'sensitivity_by_param': sensitivity_results,
            'stability_score': float(stability_score),
            'plateau_detected': plateau_detected,
            'recommendation': 'robust' if plateau_detected else 'sensitive'
        }


# Convenience functions
def quick_grid_search(
    backtest_function: Callable,
    data: pd.DataFrame,
    param_grid: Dict[str, List[Any]],
    metric: str = 'sharpe_ratio'
) -> Dict:
    """
    Quick grid search wrapper.

    Args:
        backtest_function: Backtest function
        data: Price data
        param_grid: Parameters to test
        metric: Optimization metric

    Returns:
        Optimization results
    """
    optimizer = GridSearchOptimizer(backtest_function)
    return optimizer.optimize(data, param_grid, metric=metric)


def quick_sensitivity_analysis(
    backtest_function: Callable,
    data: pd.DataFrame,
    base_params: Dict[str, float],
    variation_pct: float = 0.1
) -> Dict:
    """
    Quick sensitivity analysis wrapper.

    Args:
        backtest_function: Backtest function
        data: Price data
        base_params: Base parameters
        variation_pct: Variation percentage

    Returns:
        Sensitivity analysis results
    """
    analyzer = SensitivityAnalyzer(backtest_function)
    return analyzer.analyze(data, base_params, variation_pct=variation_pct)


# Example usage
if __name__ == "__main__":
    print("Parameter Optimizer - Test Run")
    print("=" * 60)

    # Sample backtest function
    def sample_backtest(data, position_size_pct=0.95, stop_loss_pct=0.02):
        """Dummy backtest function for testing"""
        # Simulate performance based on parameters
        base_sharpe = 1.5
        sharpe = base_sharpe * (position_size_pct / 0.95) * (1 - stop_loss_pct * 10)

        return {
            'sharpe_ratio': sharpe,
            'total_return': sharpe * 10,
            'win_rate': 60,
            'max_drawdown': 15
        }

    # Sample data
    sample_data = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=100),
        'close': np.random.randn(100).cumsum() + 100
    })

    print("\n1. Grid Search Optimization...")
    param_grid = {
        'position_size_pct': [0.8, 0.9, 0.95],
        'stop_loss_pct': [0.01, 0.02, 0.03]
    }

    opt_results = quick_grid_search(sample_backtest, sample_data, param_grid)
    print(f"✅ Best parameters: {opt_results['best_params']}")
    print(f"   Best Sharpe ratio: {opt_results['best_score']:.2f}")

    print("\n2. Sensitivity Analysis...")
    base_params = {'position_size_pct': 0.95, 'stop_loss_pct': 0.02}
    sens_results = quick_sensitivity_analysis(sample_backtest, sample_data, base_params)
    print(f"✅ Stability score: {sens_results['stability_score']:.1f}/100")
    print(f"   Plateau detected: {sens_results['plateau_detected']}")

    print("\n" + "=" * 60)
    print("✅ Test completed")
