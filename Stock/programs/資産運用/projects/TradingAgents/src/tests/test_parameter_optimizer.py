"""
Test script for parameter optimization and market impact features.

Tests:
1. Grid search optimization
2. Sensitivity analysis
3. Overfitting detection
4. Market impact (liquidity constraint)
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add src to path
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from utils.parameter_optimizer import GridSearchOptimizer, SensitivityAnalyzer
from backtest.backtest_engine import BacktestEngine


def generate_sample_data(days=252, volatility=0.02):
    """Generate sample OHLCV data for testing"""
    np.random.seed(42)

    dates = pd.date_range('2024-01-01', periods=days, freq='D')

    # Generate price series with trend
    close_prices = 40000 + np.cumsum(np.random.randn(days) * volatility * 40000)

    data = pd.DataFrame({
        'date': dates,
        'open': close_prices * (1 + np.random.randn(days) * 0.001),
        'high': close_prices * (1 + np.abs(np.random.randn(days)) * 0.005),
        'low': close_prices * (1 - np.abs(np.random.randn(days)) * 0.005),
        'close': close_prices,
        'volume': np.random.randint(100000, 500000, days)
    })

    return data


def generate_sample_signals(data, num_signals=10):
    """Generate sample trading signals"""
    np.random.seed(42)

    signals = []
    dates = data['date'].values

    for i in range(0, len(dates) - 20, len(dates) // num_signals):
        entry_date = dates[i]
        exit_date = dates[min(i + 10, len(dates) - 1)]

        signals.append({
            'date': str(entry_date)[:10],
            'action': 'buy',
            'stop_loss': 39000,
            'take_profit': 42000
        })

        signals.append({
            'date': str(exit_date)[:10],
            'action': 'sell'
        })

    return signals


def backtest_wrapper(data, position_size_pct=0.95, commission_pct=0.001, max_volume_pct=0.01):
    """Wrapper function for parameter optimization"""
    signals = generate_sample_signals(data)

    engine = BacktestEngine(
        data=data,
        initial_capital=1000000,
        position_size_pct=position_size_pct,
        commission_pct=commission_pct,
        max_volume_pct=max_volume_pct
    )

    results = engine.run_backtest(signals)
    return results


def test_grid_search():
    """Test 1: Grid Search Optimization"""
    print("\n" + "=" * 60)
    print("TEST 1: Grid Search Optimization")
    print("=" * 60)

    data = generate_sample_data(days=252)

    param_grid = {
        'position_size_pct': [0.8, 0.9, 0.95],
        'commission_pct': [0.0005, 0.001, 0.002],
        'max_volume_pct': [0.005, 0.01, 0.02]
    }

    print(f"\nParameter grid:")
    for param, values in param_grid.items():
        print(f"  {param}: {values}")
    print(f"Total combinations: {len(param_grid['position_size_pct']) * len(param_grid['commission_pct']) * len(param_grid['max_volume_pct'])}")

    optimizer = GridSearchOptimizer(backtest_function=backtest_wrapper)
    results = optimizer.optimize(data, param_grid, metric='sharpe_ratio')

    print(f"\n✅ Optimization completed")
    print(f"\nBest parameters:")
    for param, value in results['best_params'].items():
        print(f"  {param}: {value}")

    print(f"\nBest performance:")
    print(f"  Sharpe ratio: {results['best_score']:.3f}")
    print(f"  Total return: {results['best_metrics'].get('total_return', 0):.2f}%")
    print(f"  Win rate: {results['best_metrics'].get('win_rate', 0):.2f}%")
    print(f"  Max drawdown: {results['best_metrics'].get('max_drawdown', 0):.2f}%")

    print(f"\nOptimization summary:")
    print(f"  Valid results: {results['optimization_summary']['valid_results']}")
    print(f"  Score mean: {results['optimization_summary']['score_mean']:.3f}")
    print(f"  Score std: {results['optimization_summary']['score_std']:.3f}")
    print(f"  Score range: [{results['optimization_summary']['score_range'][0]:.3f}, {results['optimization_summary']['score_range'][1]:.3f}]")

    return results


def test_sensitivity_analysis():
    """Test 2: Sensitivity Analysis"""
    print("\n" + "=" * 60)
    print("TEST 2: Sensitivity Analysis")
    print("=" * 60)

    data = generate_sample_data(days=252)

    base_params = {
        'position_size_pct': 0.95,
        'commission_pct': 0.001,
        'max_volume_pct': 0.01
    }

    print(f"\nBase parameters:")
    for param, value in base_params.items():
        print(f"  {param}: {value}")

    analyzer = SensitivityAnalyzer(backtest_function=backtest_wrapper)
    results = analyzer.analyze(data, base_params, variation_pct=0.1)

    print(f"\n✅ Sensitivity analysis completed")
    print(f"\nBase score (Sharpe): {results['base_score']:.3f}")
    print(f"Stability score: {results['stability_score']:.1f}/100")
    print(f"Plateau detected: {results['plateau_detected']}")
    print(f"Recommendation: {results['recommendation']}")

    print(f"\nSensitivity by parameter:")
    for param, analysis in results['sensitivity_by_param'].items():
        print(f"\n  {param}:")
        print(f"    Scores (-10%, base, +10%): {[f'{s:.3f}' for s in analysis['scores']]}")
        print(f"    Sensitivity: {analysis['sensitivity']:.3f}")
        print(f"    Score range: {analysis['score_range']:.3f}")

    return results


def test_overfitting_detection():
    """Test 3: Overfitting Detection"""
    print("\n" + "=" * 60)
    print("TEST 3: Overfitting Detection")
    print("=" * 60)

    # Generate train and test data
    full_data = generate_sample_data(days=504)
    train_data = full_data.iloc[:252].copy()
    test_data = full_data.iloc[252:].copy()

    print(f"\nTrain period: {len(train_data)} days")
    print(f"Test period: {len(test_data)} days")

    # Optimize on train data
    param_grid = {
        'position_size_pct': [0.8, 0.9, 0.95],
        'commission_pct': [0.001, 0.002]
    }

    optimizer = GridSearchOptimizer(backtest_function=backtest_wrapper)
    train_results = optimizer.optimize(train_data, param_grid)

    print(f"\nOptimized parameters (from train): {train_results['best_params']}")

    # Test for overfitting
    overfitting_results = optimizer.detect_overfitting(
        train_data=train_data,
        test_data=test_data,
        best_params=train_results['best_params']
    )

    print(f"\n✅ Overfitting detection completed")
    print(f"\nTrain Sharpe: {overfitting_results['train_score']:.3f}")
    print(f"Test Sharpe: {overfitting_results['test_score']:.3f}")
    print(f"Degradation: {overfitting_results['degradation_pct']:.2f}%")
    print(f"Overfitting detected: {overfitting_results['overfitting_detected']}")
    print(f"Recommendation: {overfitting_results['recommendation']}")

    return overfitting_results


def test_market_impact():
    """Test 4: Market Impact (Liquidity Constraint)"""
    print("\n" + "=" * 60)
    print("TEST 4: Market Impact - Liquidity Constraint")
    print("=" * 60)

    data = generate_sample_data(days=100)
    signals = generate_sample_signals(data, num_signals=5)

    # Test with different volume constraints
    volume_constraints = [0.005, 0.01, 0.02, 0.05]

    results = []

    for max_vol_pct in volume_constraints:
        engine = BacktestEngine(
            data=data,
            initial_capital=1000000,
            position_size_pct=0.95,
            max_volume_pct=max_vol_pct
        )

        result = engine.run_backtest(signals)
        results.append({
            'max_volume_pct': max_vol_pct,
            'total_trades': result['total_trades'],
            'total_return': result['total_return'],
            'final_capital': result['final_capital']
        })

    print(f"\n✅ Market impact test completed")
    print(f"\nResults with different liquidity constraints:")
    print(f"{'Max Vol %':<12} {'Trades':<8} {'Return %':<12} {'Final Capital':<15}")
    print("-" * 50)

    for r in results:
        print(f"{r['max_volume_pct']:<12.3f} {r['total_trades']:<8} {r['total_return']:<12.2f} ¥{r['final_capital']:>13,.0f}")

    print(f"\nObservation: Stricter liquidity constraints (lower %) may reduce position sizes")

    return results


def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("PARAMETER OPTIMIZER & MARKET IMPACT - TEST SUITE")
    print("=" * 60)

    try:
        # Test 1: Grid Search
        grid_results = test_grid_search()

        # Test 2: Sensitivity Analysis
        sensitivity_results = test_sensitivity_analysis()

        # Test 3: Overfitting Detection
        overfitting_results = test_overfitting_detection()

        # Test 4: Market Impact
        market_impact_results = test_market_impact()

        # Summary
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print("✅ Test 1: Grid Search Optimization - PASSED")
        print("✅ Test 2: Sensitivity Analysis - PASSED")
        print("✅ Test 3: Overfitting Detection - PASSED")
        print("✅ Test 4: Market Impact (Liquidity) - PASSED")
        print("\n" + "=" * 60)
        print("ALL TESTS COMPLETED SUCCESSFULLY")
        print("=" * 60)

        return {
            'grid_search': grid_results,
            'sensitivity': sensitivity_results,
            'overfitting': overfitting_results,
            'market_impact': market_impact_results
        }

    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    results = main()
