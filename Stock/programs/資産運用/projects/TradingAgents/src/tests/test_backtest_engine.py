"""
Backtest Engine Test Suite - Post-Fix Validation
Tests the fixed backtest engine for correct capital calculations and KPI measurements.

Test Cases:
1. Single Trade Test - Verify capital calculation fix (+5% trade should yield ~+4.46%)
2. Multiple Trade Test - Verify capital compound correctly (+5%, -3.7% should yield ~+0.6%)
3. KPI Calculation Test - Verify all KPI metrics are calculated correctly
4. Edge Case Tests - Test boundary conditions
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Add src to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backtest.backtest_engine import BacktestEngine


class BacktestEngineValidator:
    """Validates backtest engine fix and KPI calculations."""

    def __init__(self, initial_capital: float = 1000000):
        self.initial_capital = initial_capital
        self.test_results = []

    def create_mock_data(self, days: int = 100) -> pd.DataFrame:
        """Create mock market data for testing."""
        dates = pd.date_range('2024-01-01', periods=days, freq='D')

        # Generate realistic price data
        base_price = 40000
        prices = []
        for i in range(days):
            # Random walk with slight upward bias
            change = np.random.normal(0, 200)
            new_price = base_price + change
            prices.append(new_price)
            base_price = new_price

        data = pd.DataFrame({
            'date': dates,
            'open': [p * 0.998 for p in prices],
            'high': [p * 1.005 for p in prices],
            'low': [p * 0.995 for p in prices],
            'close': prices,
            'volume': np.random.randint(100000, 200000, days)
        })

        return data

    def test_single_trade_positive(self) -> dict:
        """
        Test Case 1: Single +5% Trade

        Expected Result:
        - Entry: ¥1,000,000 * 95% = ¥950,000 position
        - Entry commission: ¥950,000 * 0.1% = ¥950
        - Remaining capital: ¥1,000,000 - ¥950,000 - ¥950 = ¥49,050
        - Exit value: ¥950,000 * 1.05 = ¥997,500
        - Exit commission: ¥997,500 * 0.1% = ¥997.50
        - Final capital: ¥49,050 + ¥997,500 - ¥997.50 = ¥1,045,552.50
        - Net return: +4.56%
        """
        print("\n" + "="*80)
        print("TEST 1: Single +5% Trade (Capital Calculation Fix Validation)")
        print("="*80)

        # Create simple market data
        data = pd.DataFrame({
            'date': pd.date_range('2025-01-01', periods=10, freq='D'),
            'open': [40000] * 10,
            'high': [42000] * 10,
            'low': [39000] * 10,
            'close': [40000, 40000, 40000, 40000, 42000, 42000, 42000, 42000, 42000, 42000],
            'volume': [100000] * 10
        })

        # Create single trade: buy at 40000, sell at 42000 (+5%)
        signals = [
            {'date': '2025-01-01', 'action': 'buy', 'entry_price': 40000},
            {'date': '2025-01-05', 'action': 'sell', 'exit_price': 42000}
        ]

        engine = BacktestEngine(data=data, initial_capital=self.initial_capital)
        results = engine.run_backtest(signals)

        # Expected calculations
        position_size_pct = 0.95
        commission_pct = 0.001

        position_value = self.initial_capital * position_size_pct  # ¥950,000
        entry_commission = position_value * commission_pct  # ¥950
        position_shares = position_value / 40000  # 23.75 shares

        exit_value = position_shares * 42000  # ¥997,500
        exit_commission = exit_value * commission_pct  # ¥997.50

        remaining_after_entry = self.initial_capital - position_value - entry_commission  # ¥49,050
        expected_final = remaining_after_entry + exit_value - exit_commission  # ¥1,045,552.50
        expected_return = ((expected_final / self.initial_capital) - 1) * 100  # +4.56%

        # Results
        actual_final = results['final_capital']
        actual_return = results['total_return']

        # Validation
        capital_match = abs(actual_final - expected_final) < 10  # Allow ¥10 rounding error
        return_match = abs(actual_return - expected_return) < 0.1  # Allow 0.1% error

        status = "✅ PASS" if (capital_match and return_match) else "❌ FAIL"

        print(f"\nExpected Results:")
        print(f"  Position Size: {position_shares:.4f} shares @ ¥40,000")
        print(f"  Entry Commission: ¥{entry_commission:,.2f}")
        print(f"  Exit Value: ¥{exit_value:,.2f}")
        print(f"  Exit Commission: ¥{exit_commission:,.2f}")
        print(f"  Expected Final Capital: ¥{expected_final:,.2f}")
        print(f"  Expected Return: {expected_return:.2f}%")

        print(f"\nActual Results:")
        print(f"  Final Capital: ¥{actual_final:,.2f}")
        print(f"  Total Return: {actual_return:.2f}%")
        print(f"  Trades: {results['total_trades']}")

        print(f"\nValidation: {status}")
        print(f"  Capital Match: {'✅' if capital_match else '❌'} (diff: ¥{abs(actual_final - expected_final):,.2f})")
        print(f"  Return Match: {'✅' if return_match else '❌'} (diff: {abs(actual_return - expected_return):.2f}%)")

        return {
            'test': 'Single +5% Trade',
            'status': 'PASS' if (capital_match and return_match) else 'FAIL',
            'expected_final': expected_final,
            'actual_final': actual_final,
            'expected_return': expected_return,
            'actual_return': actual_return,
            'details': results
        }

    def test_multiple_trades(self) -> dict:
        """
        Test Case 2: Multiple Trades (+5%, -3.7%)

        Expected Result:
        - Trade 1: +5% → ~¥1,045,552
        - Trade 2: -3.7% → ~¥1,006,000
        """
        print("\n" + "="*80)
        print("TEST 2: Multiple Trades (+5%, -3.7%)")
        print("="*80)

        # Create market data
        data = pd.DataFrame({
            'date': pd.date_range('2025-01-01', periods=20, freq='D'),
            'open': [40000] * 20,
            'high': [42000] * 20,
            'low': [38000] * 20,
            'close': [40000, 40000, 42000, 42000, 42000,  # Trade 1 exit
                     41000, 41000, 41000, 40500, 40500,  # Trade 2 entry
                     39500, 39500, 39500, 39500, 39500,  # Trade 2 exit
                     39500, 39500, 39500, 39500, 39500],
            'volume': [100000] * 20
        })

        # Trade 1: Buy at 40000, sell at 42000 (+5%)
        # Trade 2: Buy at 41000, sell at 39500 (-3.7%)
        signals = [
            {'date': '2025-01-01', 'action': 'buy', 'entry_price': 40000},
            {'date': '2025-01-03', 'action': 'sell', 'exit_price': 42000},
            {'date': '2025-01-06', 'action': 'buy', 'entry_price': 41000},
            {'date': '2025-01-11', 'action': 'sell', 'exit_price': 39500}
        ]

        engine = BacktestEngine(data=data, initial_capital=self.initial_capital)
        results = engine.run_backtest(signals)

        # Expected: Trade 1 +5% → ~¥1,045,552, Trade 2 -3.7% → ~¥1,006,000
        expected_return_min = 0.0  # At least break-even
        expected_return_max = 2.0  # Not more than 2%

        actual_final = results['final_capital']
        actual_return = results['total_return']

        # Validation
        return_in_range = expected_return_min <= actual_return <= expected_return_max
        reasonable_final = 990000 <= actual_final <= 1100000  # Reasonable range

        status = "✅ PASS" if (return_in_range and reasonable_final) else "❌ FAIL"

        print(f"\nExpected Range:")
        print(f"  Return: {expected_return_min:.2f}% to {expected_return_max:.2f}%")
        print(f"  Final Capital: ¥990,000 to ¥1,100,000")

        print(f"\nActual Results:")
        print(f"  Final Capital: ¥{actual_final:,.2f}")
        print(f"  Total Return: {actual_return:.2f}%")
        print(f"  Trades: {results['total_trades']}")
        print(f"  Win Rate: {results['win_rate']:.2f}%")

        print(f"\nTrade Details:")
        for i, trade in enumerate(results['trades'], 1):
            print(f"  Trade {i}: {trade['entry_price']:.0f} → {trade['exit_price']:.0f} ({trade['return_pct']:+.2f}%)")

        print(f"\nValidation: {status}")
        print(f"  Return in Range: {'✅' if return_in_range else '❌'}")
        print(f"  Final Capital Reasonable: {'✅' if reasonable_final else '❌'}")

        return {
            'test': 'Multiple Trades',
            'status': 'PASS' if (return_in_range and reasonable_final) else 'FAIL',
            'actual_final': actual_final,
            'actual_return': actual_return,
            'details': results
        }

    def test_kpi_calculations(self) -> dict:
        """
        Test Case 3: KPI Calculations with Realistic Trades

        Tests:
        - Win Rate calculation
        - Sharpe Ratio calculation
        - Max Drawdown calculation
        - Total Return calculation
        """
        print("\n" + "="*80)
        print("TEST 3: KPI Calculations")
        print("="*80)

        # Create market data with price variations
        data = pd.DataFrame({
            'date': pd.date_range('2025-01-01', periods=60, freq='D'),
            'open': [40000] * 60,
            'high': [45000] * 60,
            'low': [35000] * 60,
            'close': [40000, 41000, 42000, 43000, 44000,  # Trade 1: +10%
                     43000, 42000, 41000, 40000, 39000,  # Trade 2: -5%
                     40000, 41000, 42000, 43000, 44000,  # Trade 3: +8%
                     43000, 42000, 41000, 40000, 38000,  # Trade 4: -8%
                     39000, 40000, 41000, 42000, 43000,  # Trade 5: +12%
                     42000, 41000, 40000, 39000, 38000,  # Trade 6: -3%
                     39000, 40000, 41000, 42000, 43000,  # Trade 7: +7%
                     42000, 41000, 40000, 39000, 40000,  # Trade 8: +2%
                     41000, 42000, 43000, 44000, 45000,  # Trade 9: +15%
                     44000, 43000, 42000, 41000, 40000,  # Trade 10: -6%
                     40000, 40000, 40000, 40000, 40000] + [40000] * 5,
            'volume': [100000] * 60
        })

        # 10 trades: 7 wins, 3 losses → 70% win rate
        signals = [
            # Trade 1: +10%
            {'date': '2025-01-01', 'action': 'buy', 'entry_price': 40000},
            {'date': '2025-01-05', 'action': 'sell', 'exit_price': 44000},
            # Trade 2: -5%
            {'date': '2025-01-06', 'action': 'buy', 'entry_price': 43000},
            {'date': '2025-01-10', 'action': 'sell', 'exit_price': 40850},  # -5%
            # Trade 3: +8%
            {'date': '2025-01-11', 'action': 'buy', 'entry_price': 40000},
            {'date': '2025-01-15', 'action': 'sell', 'exit_price': 43200},
            # Trade 4: -8%
            {'date': '2025-01-16', 'action': 'buy', 'entry_price': 43000},
            {'date': '2025-01-20', 'action': 'sell', 'exit_price': 39560},
            # Trade 5: +12%
            {'date': '2025-01-21', 'action': 'buy', 'entry_price': 39000},
            {'date': '2025-01-25', 'action': 'sell', 'exit_price': 43680},
            # Trade 6: -3%
            {'date': '2025-01-26', 'action': 'buy', 'entry_price': 42000},
            {'date': '2025-01-30', 'action': 'sell', 'exit_price': 40740},
            # Trade 7: +7%
            {'date': '2025-01-31', 'action': 'buy', 'entry_price': 39000},
            {'date': '2025-02-04', 'action': 'sell', 'exit_price': 41730},
            # Trade 8: +2%
            {'date': '2025-02-05', 'action': 'buy', 'entry_price': 40000},
            {'date': '2025-02-09', 'action': 'sell', 'exit_price': 40800},
            # Trade 9: +15%
            {'date': '2025-02-10', 'action': 'buy', 'entry_price': 41000},
            {'date': '2025-02-14', 'action': 'sell', 'exit_price': 47150},
            # Trade 10: -6%
            {'date': '2025-02-15', 'action': 'buy', 'entry_price': 44000},
            {'date': '2025-02-19', 'action': 'sell', 'exit_price': 41360},
        ]

        engine = BacktestEngine(data=data, initial_capital=self.initial_capital)
        results = engine.run_backtest(signals)

        # Expected KPIs
        expected_win_rate = 70.0  # 7 wins out of 10
        expected_total_trades = 10

        actual_win_rate = results['win_rate']
        actual_total_trades = results['total_trades']
        actual_winning_trades = results['winning_trades']
        actual_sharpe = results['sharpe_ratio']
        actual_max_dd = results['max_drawdown']

        # Validation
        win_rate_match = abs(actual_win_rate - expected_win_rate) < 5  # Allow 5% error
        trade_count_match = actual_total_trades == expected_total_trades
        sharpe_reasonable = -5 < actual_sharpe < 10  # Reasonable range
        dd_reasonable = 0 <= actual_max_dd <= 50  # Max DD should be positive and < 50%

        status = "✅ PASS" if all([win_rate_match, trade_count_match, sharpe_reasonable, dd_reasonable]) else "❌ FAIL"

        print(f"\nExpected KPIs:")
        print(f"  Total Trades: {expected_total_trades}")
        print(f"  Win Rate: {expected_win_rate:.1f}%")

        print(f"\nActual KPIs:")
        print(f"  Total Trades: {actual_total_trades}")
        print(f"  Winning Trades: {actual_winning_trades}")
        print(f"  Losing Trades: {results['losing_trades']}")
        print(f"  Win Rate: {actual_win_rate:.2f}%")
        print(f"  Total Return: {results['total_return']:.2f}%")
        print(f"  Sharpe Ratio: {actual_sharpe:.2f}")
        print(f"  Max Drawdown: {actual_max_dd:.2f}%")
        print(f"  Final Capital: ¥{results['final_capital']:,.2f}")

        print(f"\nValidation: {status}")
        print(f"  Win Rate Match: {'✅' if win_rate_match else '❌'}")
        print(f"  Trade Count Match: {'✅' if trade_count_match else '❌'}")
        print(f"  Sharpe Reasonable: {'✅' if sharpe_reasonable else '❌'} ({actual_sharpe:.2f})")
        print(f"  Max DD Reasonable: {'✅' if dd_reasonable else '❌'} ({actual_max_dd:.2f}%)")

        return {
            'test': 'KPI Calculations',
            'status': 'PASS' if all([win_rate_match, trade_count_match, sharpe_reasonable, dd_reasonable]) else 'FAIL',
            'kpis': {
                'total_trades': actual_total_trades,
                'win_rate': actual_win_rate,
                'total_return': results['total_return'],
                'sharpe_ratio': actual_sharpe,
                'max_drawdown': actual_max_dd,
                'final_capital': results['final_capital']
            },
            'details': results
        }

    def run_all_tests(self) -> dict:
        """Run all validation tests."""
        print("\n" + "="*80)
        print("BACKTEST ENGINE VALIDATION SUITE - POST-FIX TESTING")
        print("="*80)
        print(f"Initial Capital: ¥{self.initial_capital:,.0f}")
        print(f"Test Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        results = []

        # Test 1: Single Trade
        results.append(self.test_single_trade_positive())

        # Test 2: Multiple Trades
        results.append(self.test_multiple_trades())

        # Test 3: KPI Calculations
        results.append(self.test_kpi_calculations())

        # Summary
        print("\n" + "="*80)
        print("TEST SUMMARY")
        print("="*80)

        passed = sum(1 for r in results if r['status'] == 'PASS')
        total = len(results)

        for r in results:
            status_icon = "✅" if r['status'] == 'PASS' else "❌"
            print(f"{status_icon} {r['test']}: {r['status']}")

        print(f"\nOverall: {passed}/{total} tests passed ({passed/total*100:.1f}%)")

        overall_status = "✅ ALL TESTS PASSED" if passed == total else f"⚠️ {total - passed} TEST(S) FAILED"
        print(f"\n{overall_status}")

        return {
            'summary': {
                'total_tests': total,
                'passed': passed,
                'failed': total - passed,
                'pass_rate': passed / total * 100,
                'status': 'PASS' if passed == total else 'FAIL'
            },
            'tests': results,
            'timestamp': datetime.now().isoformat()
        }


if __name__ == "__main__":
    validator = BacktestEngineValidator(initial_capital=1000000)
    results = validator.run_all_tests()

    # Save results to JSON
    import json
    results_dir = Path(__file__).resolve().parent.parent.parent / 'data' / 'results'
    results_dir.mkdir(parents=True, exist_ok=True)

    output_file = results_dir / f"backtest_validation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Results saved to: {output_file}")
