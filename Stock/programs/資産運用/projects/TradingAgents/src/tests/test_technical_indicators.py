#!/usr/bin/env python3
"""
Integration Test for Technical Indicators Module

Comprehensive test suite for all 8 technical indicators in TradingAgents.
Validates:
- Individual indicator calculations (SMA, MACD, RSI, Bollinger, ATR, Volume, VWMA, Stochastic)
- Weighted voting system
- Edge cases (minimal data, extreme volatility)
- Performance (execution time)

Run with: python3 src/tests/test_technical_indicators.py
"""

import sys
import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import json
import time

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from utils.technical_indicators import TechnicalIndicators, analyze_market_data


class TestTechnicalIndicators:
    """Comprehensive test suite for technical indicators."""

    def __init__(self):
        """Initialize test suite."""
        self.test_results = {}
        self.start_time = time.time()

    def generate_test_data(self, days=100, seed=42):
        """
        Generate realistic OHLCV test data.

        Args:
            days: Number of days of data to generate
            seed: Random seed for reproducibility

        Returns:
            DataFrame with OHLCV data
        """
        np.random.seed(seed)
        dates = pd.date_range(start='2024-08-01', periods=days, freq='D')

        # Generate price data with trend
        base_price = 30000
        prices = [base_price]
        for i in range(days - 1):
            change = np.random.normal(50, 200)
            prices.append(max(prices[-1] + change, base_price * 0.8))

        close_prices = np.array(prices)
        open_prices = close_prices + np.random.normal(0, 50, days)
        high_prices = np.maximum(close_prices, open_prices) + np.abs(np.random.normal(0, 100, days))
        low_prices = np.minimum(close_prices, open_prices) - np.abs(np.random.normal(0, 100, days))
        volumes = np.random.randint(500000, 2000000, days)

        data = pd.DataFrame({
            'date': dates,
            'open': open_prices,
            'high': high_prices,
            'low': low_prices,
            'close': close_prices,
            'volume': volumes
        })

        return data

    def print_header(self, title):
        """Print section header."""
        print("\n" + "=" * 80)
        print(title)
        print("=" * 80)

    def print_subheader(self, title):
        """Print subheader."""
        print("\n" + "-" * 80)
        print(title)
        print("-" * 80)

    def test_data_validation(self, data):
        """Test data validation."""
        self.print_subheader("STEP 1: Testing Data Validation")

        try:
            indicators = TechnicalIndicators(data)
            self.test_results['data_validation'] = {'status': 'PASS'}
            print("✅ Data validation passed")
            return True
        except Exception as e:
            self.test_results['data_validation'] = {'status': 'FAIL', 'error': str(e)}
            print(f"❌ Data validation failed: {e}")
            return False

    def test_sma(self, indicators):
        """Test SMA calculation."""
        print("\n1. Testing SMA (Moving Average)...")
        try:
            result = indicators.calculate_sma()
            self.test_results['sma'] = {'status': 'PASS', 'data': result}
            print(f"   ✅ SMA50: {result['sma50']:.2f}")
            print(f"   ✅ SMA200: {result['sma200']}")
            print(f"   ✅ Signal: {result['signal']} (Strength: {result['strength']:.2f}%)")
            return True
        except Exception as e:
            self.test_results['sma'] = {'status': 'FAIL', 'error': str(e)}
            print(f"   ❌ Error: {e}")
            return False

    def test_macd(self, indicators):
        """Test MACD calculation."""
        print("\n2. Testing MACD (Moving Average Convergence Divergence)...")
        try:
            result = indicators.calculate_macd()
            self.test_results['macd'] = {'status': 'PASS', 'data': result}
            print(f"   ✅ MACD: {result['macd']:.4f}")
            print(f"   ✅ Signal Line: {result['signal_line']:.4f}")
            print(f"   ✅ Histogram: {result['histogram']:.4f}")
            print(f"   ✅ Signal: {result['signal']} (Strength: {result['strength']:.2f}%)")
            return True
        except Exception as e:
            self.test_results['macd'] = {'status': 'FAIL', 'error': str(e)}
            print(f"   ❌ Error: {e}")
            return False

    def test_rsi(self, indicators):
        """Test RSI calculation."""
        print("\n3. Testing RSI (Relative Strength Index)...")
        try:
            result = indicators.calculate_rsi()
            # Validate RSI is in 0-100 range
            assert 0 <= result['rsi'] <= 100, "RSI must be between 0 and 100"
            self.test_results['rsi'] = {'status': 'PASS', 'data': result}
            print(f"   ✅ RSI: {result['rsi']:.2f}")
            print(f"   ✅ Signal: {result['signal']} (Strength: {result['strength']:.2f})")
            return True
        except Exception as e:
            self.test_results['rsi'] = {'status': 'FAIL', 'error': str(e)}
            print(f"   ❌ Error: {e}")
            return False

    def test_bollinger_bands(self, indicators):
        """Test Bollinger Bands calculation."""
        print("\n4. Testing Bollinger Bands...")
        try:
            result = indicators.calculate_bollinger_bands()
            # Validate band ordering
            assert result['lower'] <= result['middle'] <= result['upper'], "Band ordering incorrect"
            self.test_results['bollinger'] = {'status': 'PASS', 'data': result}
            print(f"   ✅ Upper: {result['upper']:.2f}")
            print(f"   ✅ Middle: {result['middle']:.2f}")
            print(f"   ✅ Lower: {result['lower']:.2f}")
            print(f"   ✅ Signal: {result['signal']} (Strength: {result['strength']:.2f}%)")
            return True
        except Exception as e:
            self.test_results['bollinger'] = {'status': 'FAIL', 'error': str(e)}
            print(f"   ❌ Error: {e}")
            return False

    def test_atr(self, indicators):
        """Test ATR calculation."""
        print("\n5. Testing ATR (Average True Range)...")
        try:
            result = indicators.calculate_atr()
            self.test_results['atr'] = {'status': 'PASS', 'data': result}
            print(f"   ✅ ATR: {result['atr']:.2f}")
            print(f"   ✅ ATR%: {result['atr_percent']:.2f}%")
            print(f"   ✅ Volatility: {result['volatility']}")
            return True
        except Exception as e:
            self.test_results['atr'] = {'status': 'FAIL', 'error': str(e)}
            print(f"   ❌ Error: {e}")
            return False

    def test_volume_ratio(self, indicators):
        """Test Volume Ratio calculation."""
        print("\n6. Testing Volume Ratio...")
        try:
            result = indicators.calculate_volume_ratio()
            self.test_results['volume'] = {'status': 'PASS', 'data': result}
            print(f"   ✅ Volume Ratio: {result['volume_ratio']:.2f}")
            print(f"   ✅ Current Volume: {result['current_volume']:,}")
            print(f"   ✅ Signal: {result['signal']} (Strength: {result['strength']:.2f}%)")
            return True
        except Exception as e:
            self.test_results['volume'] = {'status': 'FAIL', 'error': str(e)}
            print(f"   ❌ Error: {e}")
            return False

    def test_vwma(self, indicators):
        """Test VWMA calculation."""
        print("\n7. Testing VWMA (Volume Weighted Moving Average)...")
        try:
            result = indicators.calculate_vwma()
            self.test_results['vwma'] = {'status': 'PASS', 'data': result}
            print(f"   ✅ VWMA: {result['vwma']:.2f}")
            print(f"   ✅ Current Price: {result['current_price']:.2f}")
            print(f"   ✅ Diff%: {result['diff_percent']:.2f}%")
            print(f"   ✅ Signal: {result['signal']} (Strength: {result['strength']:.2f}%)")
            return True
        except Exception as e:
            self.test_results['vwma'] = {'status': 'FAIL', 'error': str(e)}
            print(f"   ❌ Error: {e}")
            return False

    def test_stochastic(self, indicators):
        """Test Stochastic Oscillator calculation."""
        print("\n8. Testing Stochastic Oscillator...")
        try:
            result = indicators.calculate_stochastic()
            # Validate Stochastic is in 0-100 range
            assert 0 <= result['k'] <= 100, "%K must be between 0 and 100"
            self.test_results['stochastic'] = {'status': 'PASS', 'data': result}
            print(f"   ✅ %K: {result['k']:.2f}")
            print(f"   ✅ %D: {result['d']:.2f}")
            print(f"   ✅ Signal: {result['signal']} (Strength: {result['strength']:.2f})")
            return True
        except Exception as e:
            self.test_results['stochastic'] = {'status': 'FAIL', 'error': str(e)}
            print(f"   ❌ Error: {e}")
            return False

    def test_weighted_voting(self, indicators):
        """Test weighted voting system."""
        self.print_subheader("STEP 2: Testing Weighted Voting System")

        try:
            result = indicators.calculate_all()
            self.test_results['weighted_voting'] = {'status': 'PASS', 'data': result['weighted_voting']}

            voting = result['weighted_voting']
            print(f"✅ Weighted Voting Results:")
            print(f"   Buy Score: {voting['buy_score']:.2f}")
            print(f"   Sell Score: {voting['sell_score']:.2f}")
            print(f"   Total Weight: {voting['total_weight']:.2f}")
            print(f"   Final Signal: {voting['final_signal'].upper()}")
            print(f"   Confidence: {voting['confidence']:.2f}%")
            return True
        except Exception as e:
            self.test_results['weighted_voting'] = {'status': 'FAIL', 'error': str(e)}
            print(f"❌ Error: {e}")
            return False

    def test_edge_cases(self, data):
        """Test edge cases."""
        self.print_subheader("STEP 3: Testing Edge Cases")

        # Test with minimal data
        print("Testing with minimal data (30 days)...")
        try:
            minimal_data = data.iloc[-30:].reset_index(drop=True)
            indicators_minimal = TechnicalIndicators(minimal_data)
            result = indicators_minimal.calculate_all()
            self.test_results['edge_case_minimal'] = {'status': 'PASS'}
            print("✅ Minimal data test passed")
        except Exception as e:
            self.test_results['edge_case_minimal'] = {'status': 'FAIL', 'error': str(e)}
            print(f"❌ Minimal data test failed: {e}")

        # Test with extreme volatility
        print("Testing with extreme volatility data...")
        try:
            volatile_data = data.copy()
            volatile_data['close'] = volatile_data['close'] * (1 + np.random.normal(0, 0.05, len(volatile_data)))
            volatile_data['high'] = volatile_data['close'] * 1.1
            volatile_data['low'] = volatile_data['close'] * 0.9

            indicators_volatile = TechnicalIndicators(volatile_data)
            result = indicators_volatile.calculate_all()
            self.test_results['edge_case_volatile'] = {'status': 'PASS'}
            print("✅ Extreme volatility test passed")
        except Exception as e:
            self.test_results['edge_case_volatile'] = {'status': 'FAIL', 'error': str(e)}
            print(f"❌ Extreme volatility test failed: {e}")

    def print_summary(self):
        """Print test summary."""
        self.print_header("TEST SUMMARY")

        pass_count = sum(1 for v in self.test_results.values() if v['status'] == 'PASS')
        fail_count = sum(1 for v in self.test_results.values() if v['status'] == 'FAIL')
        total_tests = pass_count + fail_count

        elapsed_time = time.time() - self.start_time

        print(f"Total Tests: {total_tests}")
        print(f"Passed: {pass_count} ✅")
        print(f"Failed: {fail_count} ❌")
        print(f"Execution Time: {elapsed_time:.2f} seconds")
        print()

        print("Detailed Results:")
        for test_name, result in self.test_results.items():
            status_icon = "✅" if result['status'] == 'PASS' else "❌"
            print(f"  {status_icon} {test_name}: {result['status']}")
            if result['status'] == 'FAIL':
                print(f"     Error: {result.get('error', 'Unknown error')}")

        print()
        if fail_count == 0:
            print("=" * 80)
            print("🎉 ALL TESTS PASSED 🎉")
            print("=" * 80)
        else:
            print("=" * 80)
            print(f"⚠️  {fail_count} TEST(S) FAILED")
            print("=" * 80)

    def run(self):
        """Run all tests."""
        self.print_header("TECHNICAL INDICATORS INTEGRATION TEST")
        print(f"Test Start: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        # Step 1: Generate test data
        print("STEP 1: Generating Sample OHLCV Data")
        print("-" * 80)
        data = self.generate_test_data()
        print(f"✅ Generated {len(data)} days of OHLCV data")
        print(f"   Date range: {data['date'].min().date()} to {data['date'].max().date()}")
        print(f"   Price range: {data['close'].min():.2f} to {data['close'].max():.2f}")
        print(f"   Avg Volume: {data['volume'].mean():,.0f}")
        print()

        # Step 2: Validate data
        if not self.test_data_validation(data):
            sys.exit(1)

        # Step 3: Test individual indicators
        self.print_subheader("STEP 2: Testing Individual Indicators")
        indicators = TechnicalIndicators(data)
        self.test_sma(indicators)
        self.test_macd(indicators)
        self.test_rsi(indicators)
        self.test_bollinger_bands(indicators)
        self.test_atr(indicators)
        self.test_volume_ratio(indicators)
        self.test_vwma(indicators)
        self.test_stochastic(indicators)

        # Step 4: Test weighted voting
        self.test_weighted_voting(indicators)

        # Step 5: Test edge cases
        self.test_edge_cases(data)

        # Step 6: Print summary
        self.print_summary()

        # Return exit code
        fail_count = sum(1 for v in self.test_results.values() if v['status'] == 'FAIL')
        return 0 if fail_count == 0 else 1


def main():
    """Main entry point."""
    tester = TestTechnicalIndicators()
    exit_code = tester.run()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
