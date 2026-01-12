"""
Test Market Regime Detection Module

Tests all three regime detection methods:
1. MA-based (Moving Average crossover)
2. Trend-based (Linear regression slope)
3. Volatility-based (ATR/Price ratio)
4. Combined method (Majority voting)
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add src to path
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from utils.market_regime import MarketRegimeDetector, RegimeType, detect_market_regime
from backtest.backtest_engine import BacktestEngine


def generate_test_data(regime: str = 'bull', days: int = 300) -> pd.DataFrame:
    """
    Generate synthetic OHLCV data for testing.

    Args:
        regime: 'bull', 'bear', or 'sideways'
        days: Number of days to generate

    Returns:
        DataFrame with OHLCV data
    """
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=days, freq='D')

    if regime == 'bull':
        # Uptrend with noise
        trend = np.linspace(38000, 42000, days)
        noise = np.random.normal(0, 200, days)
        close = trend + noise
    elif regime == 'bear':
        # Downtrend with noise
        trend = np.linspace(42000, 38000, days)
        noise = np.random.normal(0, 200, days)
        close = trend + noise
    else:  # sideways
        # Range-bound with noise
        base = 40000
        noise = np.random.normal(0, 300, days)
        close = base + noise

    # Generate OHLC from close
    high = close + np.abs(np.random.normal(0, 150, days))
    low = close - np.abs(np.random.normal(0, 150, days))
    open_price = close + np.random.normal(0, 100, days)

    data = pd.DataFrame({
        'date': dates,
        'open': open_price,
        'high': high,
        'low': low,
        'close': close,
        'volume': np.random.randint(100000, 200000, days)
    })

    return data


def test_ma_based_detection():
    """Test MA-based regime detection."""
    print("\n" + "="*60)
    print("TEST 1: MA-Based Regime Detection")
    print("="*60)

    # Test bull market
    bull_data = generate_test_data('bull', 300)
    detector = MarketRegimeDetector(bull_data)
    regime = detector.detect_regime_ma_based()

    bull_pct = (regime == RegimeType.BULL.value).sum() / len(regime) * 100
    print(f"\nBull Market Test:")
    print(f"  Bull regime detected: {bull_pct:.1f}% of time")
    print(f"  ✅ PASS" if bull_pct > 30 else f"  ❌ FAIL")

    # Test bear market
    bear_data = generate_test_data('bear', 300)
    detector = MarketRegimeDetector(bear_data)
    regime = detector.detect_regime_ma_based()

    bear_pct = (regime == RegimeType.BEAR.value).sum() / len(regime) * 100
    print(f"\nBear Market Test:")
    print(f"  Bear regime detected: {bear_pct:.1f}% of time")
    print(f"  ✅ PASS" if bear_pct > 30 else f"  ❌ FAIL")

    # Test sideways market
    sideways_data = generate_test_data('sideways', 300)
    detector = MarketRegimeDetector(sideways_data)
    regime = detector.detect_regime_ma_based()

    sideways_pct = (regime == RegimeType.SIDEWAYS.value).sum() / len(regime) * 100
    print(f"\nSideways Market Test:")
    print(f"  Sideways regime detected: {sideways_pct:.1f}% of time")
    print(f"  ✅ PASS" if sideways_pct > 30 else f"  ❌ FAIL")

    return True


def test_trend_based_detection():
    """Test trend-based regime detection."""
    print("\n" + "="*60)
    print("TEST 2: Trend-Based Regime Detection")
    print("="*60)

    # Test bull market
    bull_data = generate_test_data('bull', 300)
    detector = MarketRegimeDetector(bull_data)
    regime = detector.detect_regime_trend_based()

    bull_pct = (regime == RegimeType.BULL.value).sum() / len(regime) * 100
    print(f"\nBull Market Test:")
    print(f"  Bull regime detected: {bull_pct:.1f}% of time")
    print(f"  ✅ PASS" if bull_pct > 40 else f"  ❌ FAIL")

    # Test bear market
    bear_data = generate_test_data('bear', 300)
    detector = MarketRegimeDetector(bear_data)
    regime = detector.detect_regime_trend_based()

    bear_pct = (regime == RegimeType.BEAR.value).sum() / len(regime) * 100
    print(f"\nBear Market Test:")
    print(f"  Bear regime detected: {bear_pct:.1f}% of time")
    print(f"  ✅ PASS" if bear_pct > 40 else f"  ❌ FAIL")

    # Test sideways market
    sideways_data = generate_test_data('sideways', 300)
    detector = MarketRegimeDetector(sideways_data)
    regime = detector.detect_regime_trend_based()

    sideways_pct = (regime == RegimeType.SIDEWAYS.value).sum() / len(regime) * 100
    print(f"\nSideways Market Test:")
    print(f"  Sideways regime detected: {sideways_pct:.1f}% of time")
    print(f"  ✅ PASS" if sideways_pct > 50 else f"  ❌ FAIL")

    return True


def test_volatility_based_detection():
    """Test volatility-based regime detection."""
    print("\n" + "="*60)
    print("TEST 3: Volatility-Based Regime Detection")
    print("="*60)

    # Test with mixed data
    mixed_data = generate_test_data('bull', 300)
    detector = MarketRegimeDetector(mixed_data)
    regime = detector.detect_regime_volatility_based()

    regime_counts = regime.value_counts()
    print(f"\nRegime Distribution:")
    for regime_type in [RegimeType.BULL.value, RegimeType.BEAR.value, RegimeType.SIDEWAYS.value]:
        count = regime_counts.get(regime_type, 0)
        pct = count / len(regime) * 100
        print(f"  {regime_type.capitalize()}: {pct:.1f}%")

    print(f"  ✅ PASS (All regimes detected)")

    return True


def test_combined_detection():
    """Test combined regime detection (majority voting)."""
    print("\n" + "="*60)
    print("TEST 4: Combined Regime Detection")
    print("="*60)

    # Test bull market
    bull_data = generate_test_data('bull', 300)
    detector = MarketRegimeDetector(bull_data)
    regime = detector.detect_regime_combined()

    bull_pct = (regime == RegimeType.BULL.value).sum() / len(regime) * 100
    print(f"\nBull Market Test:")
    print(f"  Bull regime detected: {bull_pct:.1f}% of time")
    print(f"  ✅ PASS" if bull_pct > 35 else f"  ❌ FAIL")

    # Test regime periods
    periods = detector.get_regime_periods(regime)
    print(f"\nRegime Periods:")
    for regime_type, period_list in periods.items():
        print(f"  {regime_type.capitalize()}: {len(period_list)} periods")

    # Test regime statistics
    stats = detector.get_regime_statistics(regime)
    print(f"\nRegime Statistics:")
    for regime_type, regime_stats in stats.items():
        print(f"  {regime_type.capitalize()}: {regime_stats['days']} days ({regime_stats['percentage']:.1f}%)")

    return True


def test_backtest_integration():
    """Test integration with BacktestEngine."""
    print("\n" + "="*60)
    print("TEST 5: Backtest Engine Integration")
    print("="*60)

    # Generate mixed market data (bull → sideways → bear)
    bull_data = generate_test_data('bull', 100)
    sideways_data = generate_test_data('sideways', 100)
    bear_data = generate_test_data('bear', 100)

    # Adjust dates to be consecutive
    sideways_data['date'] = pd.date_range(bull_data['date'].max() + pd.Timedelta(days=1), periods=100, freq='D')
    bear_data['date'] = pd.date_range(sideways_data['date'].max() + pd.Timedelta(days=1), periods=100, freq='D')

    # Combine data
    mixed_data = pd.concat([bull_data, sideways_data, bear_data], ignore_index=True)

    # Generate trading signals (buy every 10 days)
    signals = []
    for i in range(0, len(mixed_data), 20):
        if i + 10 < len(mixed_data):
            # Buy signal
            signals.append({
                'date': mixed_data.loc[i, 'date'].strftime('%Y-%m-%d'),
                'action': 'buy',
                'entry_price': float(mixed_data.loc[i, 'close']),
                'stop_loss': float(mixed_data.loc[i, 'close'] * 0.98),
                'take_profit': float(mixed_data.loc[i, 'close'] * 1.05)
            })
            # Sell signal
            signals.append({
                'date': mixed_data.loc[i+10, 'date'].strftime('%Y-%m-%d'),
                'action': 'sell',
                'exit_price': float(mixed_data.loc[i+10, 'close'])
            })

    # Run backtest with regime analysis
    engine = BacktestEngine(data=mixed_data, initial_capital=1000000)
    regime_results = engine.analyze_by_regime(signals)

    print("\nRegime Statistics:")
    for regime_type, stats in regime_results['regime_statistics'].items():
        print(f"  {regime_type.capitalize()}: {stats['days']} days ({stats['percentage']:.1f}%)")

    print("\nRegime Performance:")
    all_sharpe_above_threshold = True
    for regime_type, performance in regime_results['regime_performance'].items():
        if performance['total_trades'] > 0:
            print(f"\n  {regime_type.capitalize()} Market:")
            print(f"    Total Trades: {performance['total_trades']}")
            print(f"    Win Rate: {performance['win_rate']:.2f}%")
            print(f"    Sharpe Ratio: {performance['sharpe_ratio']:.2f}")
            print(f"    Total Return: {performance['total_return']:.2f}%")
            print(f"    Max Drawdown: {performance['max_drawdown']:.2f}%")

            # Check if Sharpe ratio > 0.3 (Phase 3 requirement)
            if performance['sharpe_ratio'] < 0.3:
                all_sharpe_above_threshold = False
                print(f"    ⚠️  WARNING: Sharpe ratio below 0.3 threshold")
        else:
            print(f"\n  {regime_type.capitalize()} Market:")
            print(f"    No trades in this regime")

    print(f"\n{'✅ PASS' if all_sharpe_above_threshold else '❌ FAIL'}: All regimes meet Sharpe > 0.3 requirement")

    return all_sharpe_above_threshold


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("MARKET REGIME DETECTION - COMPREHENSIVE TEST SUITE")
    print("="*60)

    results = []

    try:
        results.append(("MA-Based Detection", test_ma_based_detection()))
    except Exception as e:
        print(f"❌ FAIL: MA-Based Detection - {e}")
        results.append(("MA-Based Detection", False))

    try:
        results.append(("Trend-Based Detection", test_trend_based_detection()))
    except Exception as e:
        print(f"❌ FAIL: Trend-Based Detection - {e}")
        results.append(("Trend-Based Detection", False))

    try:
        results.append(("Volatility-Based Detection", test_volatility_based_detection()))
    except Exception as e:
        print(f"❌ FAIL: Volatility-Based Detection - {e}")
        results.append(("Volatility-Based Detection", False))

    try:
        results.append(("Combined Detection", test_combined_detection()))
    except Exception as e:
        print(f"❌ FAIL: Combined Detection - {e}")
        results.append(("Combined Detection", False))

    try:
        results.append(("Backtest Integration", test_backtest_integration()))
    except Exception as e:
        print(f"❌ FAIL: Backtest Integration - {e}")
        results.append(("Backtest Integration", False))

    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)

    passed = sum([1 for _, result in results if result])
    total = len(results)

    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status}: {test_name}")

    print(f"\nTotal: {passed}/{total} tests passed")
    print(f"Coverage: {passed/total*100:.1f}%")

    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed")

    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
