#!/usr/bin/env python3
"""
Final Validation Script
Phase 6: Final Validation & Production Readiness

Validates:
- Real data fetch (or sample data fallback)
- Improved strategies from Agent 1
- Comparison with Phase 5 baseline
- Go/No-go decision criteria
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def fetch_real_data():
    """Attempt to fetch real Nikkei 225 data via yfinance"""
    print("=" * 60)
    print("Fetching Real Data (Nikkei 225)")
    print("=" * 60)

    try:
        import yfinance as yf

        ticker = "^N225"
        end_date = datetime.now()
        start_date = datetime(2020, 1, 1)

        print(f"\nFetching {ticker}...")
        print(f"Period: {start_date.date()} to {end_date.date()}")

        data = yf.download(ticker, start=start_date, end=end_date, progress=False)

        if data.empty:
            print("❌ No data received from yfinance")
            return None, "No data from API"

        print(f"✓ Data fetched: {len(data)} days")
        return data, None

    except Exception as e:
        print(f"❌ Failed to fetch data: {e}")
        return None, str(e)


def create_sample_data():
    """Create sample data for testing (fallback)"""
    print("\n" + "=" * 60)
    print("Creating Sample Data (Fallback)")
    print("=" * 60)

    np.random.seed(42)

    # Create 5 years of daily data
    dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='B')
    n = len(dates)

    # Simulate realistic Nikkei 225 data
    base_price = 20000
    returns = np.random.normal(0.0005, 0.015, n)
    prices = base_price * np.exp(np.cumsum(returns))

    data = pd.DataFrame({
        'Open': prices * (1 + np.random.uniform(-0.01, 0.01, n)),
        'High': prices * (1 + np.random.uniform(0, 0.02, n)),
        'Low': prices * (1 + np.random.uniform(-0.02, 0, n)),
        'Close': prices,
        'Volume': np.random.randint(100000, 500000, n)
    }, index=dates)

    print(f"✓ Sample data created: {len(data)} days")
    print(f"  Period: {data.index[0].date()} to {data.index[-1].date()}")

    return data


def calculate_indicators(data):
    """Calculate technical indicators"""
    df = data.copy()

    # Simple Moving Averages
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    # RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # MACD
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2
    df['MACD_signal'] = df['MACD'].ewm(span=9, adjust=False).mean()

    return df.dropna()


def run_improved_strategies(data):
    """Run improved strategies from Agent 1"""
    print("\n" + "=" * 60)
    print("Running Improved Strategies")
    print("=" * 60)

    df = calculate_indicators(data)

    # Split data: 80% train, 20% test
    split_idx = int(len(df) * 0.8)
    train_data = df.iloc[:split_idx]
    test_data = df.iloc[split_idx:]

    print(f"\nTrain period: {train_data.index[0].date()} to {train_data.index[-1].date()}")
    print(f"Test period: {test_data.index[0].date()} to {test_data.index[-1].date()}")

    results = {}

    # Strategy 1: Improved Momentum (reduced parameters)
    print("\n[1] Improved Momentum Strategy")
    train_perf_1 = backtest_momentum(train_data, rsi_oversold=35, rsi_overbought=65)
    test_perf_1 = backtest_momentum(test_data, rsi_oversold=35, rsi_overbought=65)
    results['Improved_Momentum'] = {'train': train_perf_1, 'test': test_perf_1}

    # Strategy 2: Improved Mean Reversion (conservative)
    print("\n[2] Improved Mean Reversion Strategy")
    train_perf_2 = backtest_mean_reversion(train_data, threshold=1.5)
    test_perf_2 = backtest_mean_reversion(test_data, threshold=1.5)
    results['Improved_Mean_Reversion'] = {'train': train_perf_2, 'test': test_perf_2}

    # Strategy 3: Improved Trend Following (simple)
    print("\n[3] Improved Trend Following Strategy")
    train_perf_3 = backtest_trend_following(train_data)
    test_perf_3 = backtest_trend_following(test_data)
    results['Improved_Trend_Following'] = {'train': train_perf_3, 'test': test_perf_3}

    return results


def backtest_momentum(data, rsi_oversold=35, rsi_overbought=65):
    """Improved Momentum strategy with reduced parameters"""
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0

    # Buy when RSI oversold, sell when overbought
    signals.loc[data['RSI'] < rsi_oversold, 'signal'] = 1
    signals.loc[data['RSI'] > rsi_overbought, 'signal'] = -1

    signals['position'] = signals['signal'].fillna(0).cumsum().clip(-1, 1)
    signals['returns'] = data['Close'].pct_change()
    signals['strategy_returns'] = signals['position'].shift(1) * signals['returns']

    return calculate_performance(signals['strategy_returns'].dropna())


def backtest_mean_reversion(data, threshold=1.5):
    """Improved Mean Reversion with conservative threshold"""
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0

    # Z-score based mean reversion
    z_score = (data['Close'] - data['SMA_20']) / data['Close'].rolling(20).std()

    signals.loc[z_score < -threshold, 'signal'] = 1
    signals.loc[z_score > threshold, 'signal'] = -1

    signals['position'] = signals['signal'].fillna(0).cumsum().clip(-1, 1)
    signals['returns'] = data['Close'].pct_change()
    signals['strategy_returns'] = signals['position'].shift(1) * signals['returns']

    return calculate_performance(signals['strategy_returns'].dropna())


def backtest_trend_following(data):
    """Improved Trend Following with simple SMA crossover"""
    signals = pd.DataFrame(index=data.index)
    signals['signal'] = 0

    # SMA crossover
    signals.loc[data['SMA_20'] > data['SMA_50'], 'signal'] = 1
    signals.loc[data['SMA_20'] < data['SMA_50'], 'signal'] = -1

    signals['position'] = signals['signal'].fillna(0)
    signals['returns'] = data['Close'].pct_change()
    signals['strategy_returns'] = signals['position'].shift(1) * signals['returns']

    return calculate_performance(signals['strategy_returns'].dropna())


def calculate_performance(returns):
    """Calculate strategy performance metrics"""
    if len(returns) == 0 or returns.std() == 0:
        return {
            'Total Return': 0.0,
            'Sharpe Ratio': 0.0,
            'Win Rate': 0.0,
            'Max Drawdown': 0.0,
            'Num Trades': 0
        }

    total_return = (1 + returns).cumprod().iloc[-1] - 1
    sharpe = returns.mean() / returns.std() * np.sqrt(252) if returns.std() > 0 else 0

    # Win rate
    winning_trades = (returns > 0).sum()
    total_trades = (returns != 0).sum()
    win_rate = winning_trades / total_trades if total_trades > 0 else 0

    # Max drawdown
    cumulative = (1 + returns).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max
    max_drawdown = drawdown.min()

    return {
        'Total Return': total_return,
        'Sharpe Ratio': sharpe,
        'Win Rate': win_rate,
        'Max Drawdown': max_drawdown,
        'Num Trades': int(total_trades)
    }


def compare_with_baseline(results):
    """Compare with Phase 5 baseline results"""
    print("\n" + "=" * 60)
    print("Comparison with Phase 5 Baseline")
    print("=" * 60)

    # Phase 5 baseline (from previous results)
    baseline = {
        'Momentum': {'train': {'Sharpe Ratio': 0.35}, 'test': {'Sharpe Ratio': -0.15}},
        'Mean_Reversion': {'train': {'Sharpe Ratio': 0.45}, 'test': {'Sharpe Ratio': 0.10}},
        'Trend_Following': {'train': {'Sharpe Ratio': 0.40}, 'test': {'Sharpe Ratio': 0.05}}
    }

    improvements = []

    print("\nStrategy Comparison:")
    for strategy_name, perf in results.items():
        baseline_name = strategy_name.replace('Improved_', '')

        if baseline_name in baseline:
            baseline_train_sharpe = baseline[baseline_name]['train']['Sharpe Ratio']
            baseline_test_sharpe = baseline[baseline_name]['test']['Sharpe Ratio']
            improved_train_sharpe = perf['train']['Sharpe Ratio']
            improved_test_sharpe = perf['test']['Sharpe Ratio']

            train_improve = improved_train_sharpe - baseline_train_sharpe
            test_improve = improved_test_sharpe - baseline_test_sharpe

            print(f"\n{strategy_name}:")
            print(f"  Train Sharpe: {improved_train_sharpe:.3f} (baseline: {baseline_train_sharpe:.3f}, Δ{train_improve:+.3f})")
            print(f"  Test Sharpe:  {improved_test_sharpe:.3f} (baseline: {baseline_test_sharpe:.3f}, Δ{test_improve:+.3f})")

            improvements.append({
                'strategy': strategy_name,
                'train_improve': train_improve,
                'test_improve': test_improve
            })

    return improvements


def make_go_nogo_decision(results):
    """Make Go/No-go decision based on criteria"""
    print("\n" + "=" * 60)
    print("Go/No-go Decision Analysis")
    print("=" * 60)

    decisions = []

    for strategy_name, perf in results.items():
        print(f"\n{strategy_name}:")

        test_perf = perf['test']
        train_perf = perf['train']

        # Criteria
        test_sharpe = test_perf['Sharpe Ratio']
        win_rate = test_perf['Win Rate']
        max_drawdown = test_perf['Max Drawdown']

        # Calculate train-test gap
        train_test_gap = abs(train_perf['Sharpe Ratio'] - test_sharpe) / (abs(train_perf['Sharpe Ratio']) + 1e-6)

        print(f"  Test Sharpe Ratio: {test_sharpe:.3f} (target: >0.5)")
        print(f"  Win Rate: {win_rate:.1%} (target: >50%)")
        print(f"  Max Drawdown: {max_drawdown:.1%} (target: >-20%)")
        print(f"  Train-Test Gap: {train_test_gap:.1%} (target: <30%)")

        # Check Go conditions
        go_conditions = {
            'Test Sharpe >0.5': test_sharpe > 0.5,
            'Win Rate >50%': win_rate > 0.5,
            'Max Drawdown >-20%': max_drawdown > -0.2,
            'Train-Test Gap <30%': train_test_gap < 0.3
        }

        all_met = all(go_conditions.values())

        print("\n  Decision Criteria:")
        for criterion, met in go_conditions.items():
            symbol = "✓" if met else "❌"
            print(f"    {symbol} {criterion}")

        decision = "GO" if all_met else "NO-GO"
        print(f"\n  Decision: {decision}")

        decisions.append({
            'strategy': strategy_name,
            'decision': decision,
            'criteria_met': sum(go_conditions.values()),
            'criteria_total': len(go_conditions),
            'test_sharpe': test_sharpe,
            'metrics': test_perf
        })

    # Overall decision
    print("\n" + "=" * 60)
    print("OVERALL DECISION")
    print("=" * 60)

    go_count = sum(1 for d in decisions if d['decision'] == 'GO')
    total_strategies = len(decisions)

    print(f"\nStrategies meeting GO criteria: {go_count}/{total_strategies}")

    if go_count >= 2:
        overall_decision = "GO FOR PRODUCTION"
        print(f"\n✓ {overall_decision}")
        print("  At least 2 strategies meet all criteria")
    elif go_count >= 1:
        overall_decision = "CONDITIONAL GO"
        print(f"\n⚠️  {overall_decision}")
        print("  Only 1 strategy meets criteria")
        print("  Proceed with caution")
    else:
        overall_decision = "NO-GO - PLAN PHASE 7"
        print(f"\n❌ {overall_decision}")
        print("  No strategies meet all criteria")
        print("  Further improvements needed")

    return decisions, overall_decision


def generate_validation_report(data_source, results, improvements, decisions, overall_decision):
    """Generate final validation report"""
    report_path = Path(__file__).parent.parent / "data" / "results" / "PHASE6_FINAL_VALIDATION_REPORT.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Phase 6: Final Validation Report\n\n")
        f.write(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## 1. Data Source\n\n")
        f.write(f"**Source**: {data_source}\n\n")

        f.write("## 2. Strategy Performance\n\n")
        f.write("| Strategy | Train Sharpe | Test Sharpe | Win Rate | Max DD | Trades |\n")
        f.write("|----------|--------------|-------------|----------|--------|--------|\n")

        for strategy_name, perf in results.items():
            train = perf['train']
            test = perf['test']
            f.write(f"| {strategy_name} | {train['Sharpe Ratio']:.3f} | {test['Sharpe Ratio']:.3f} | "
                   f"{test['Win Rate']:.1%} | {test['Max Drawdown']:.1%} | {test['Num Trades']} |\n")

        f.write("\n## 3. Improvement vs Phase 5 Baseline\n\n")
        f.write("| Strategy | Train Δ | Test Δ |\n")
        f.write("|----------|---------|--------|\n")

        for imp in improvements:
            f.write(f"| {imp['strategy']} | {imp['train_improve']:+.3f} | {imp['test_improve']:+.3f} |\n")

        f.write("\n## 4. Go/No-go Decision\n\n")
        f.write("### Decision Criteria:\n\n")
        f.write("- ✅ Test Sharpe >0.5\n")
        f.write("- ✅ Win Rate >50%\n")
        f.write("- ✅ Max Drawdown >-20%\n")
        f.write("- ✅ Train-Test Gap <30%\n\n")

        f.write("### Results:\n\n")
        for dec in decisions:
            symbol = "✓" if dec['decision'] == 'GO' else "❌"
            f.write(f"**{symbol} {dec['strategy']}**: {dec['decision']} "
                   f"({dec['criteria_met']}/{dec['criteria_total']} criteria met)\n\n")

        f.write("### Overall Decision:\n\n")
        if "GO FOR PRODUCTION" in overall_decision:
            f.write(f"## ✓ {overall_decision}\n\n")
        elif "CONDITIONAL" in overall_decision:
            f.write(f"## ⚠️  {overall_decision}\n\n")
        else:
            f.write(f"## ❌ {overall_decision}\n\n")

        f.write("## 5. Recommendations\n\n")
        if "GO FOR PRODUCTION" in overall_decision:
            f.write("- Deploy strategies that meet GO criteria\n")
            f.write("- Set up weekly monitoring and reporting\n")
            f.write("- Continue collecting real performance data\n")
        elif "CONDITIONAL" in overall_decision:
            f.write("- Deploy only the strategy that meets criteria\n")
            f.write("- Monitor closely for first month\n")
            f.write("- Continue improving other strategies\n")
        else:
            f.write("- Do NOT deploy to production\n")
            f.write("- Plan Phase 7: Further strategy improvements\n")
            f.write("- Consider ensemble methods or new indicators\n")

        f.write("\n---\n")
        f.write("*End of Report*\n")

    print(f"\n✓ Validation report saved to: {report_path}")
    return report_path


def main():
    """Main validation workflow"""
    print("=" * 60)
    print("PHASE 6: FINAL VALIDATION & PRODUCTION READINESS")
    print("=" * 60)

    # Step 1: Try to fetch real data
    data, error = fetch_real_data()

    if data is None:
        print(f"\nReason: {error}")
        print("\nUsing sample data fallback...")
        data = create_sample_data()
        data_source = "Sample Data (Fallback)"
    else:
        data_source = "Real Data (yfinance)"

    # Step 2: Run improved strategies
    results = run_improved_strategies(data)

    # Step 3: Compare with baseline
    improvements = compare_with_baseline(results)

    # Step 4: Make Go/No-go decision
    decisions, overall_decision = make_go_nogo_decision(results)

    # Step 5: Generate report
    report_path = generate_validation_report(data_source, results, improvements, decisions, overall_decision)

    print("\n" + "=" * 60)
    print("VALIDATION COMPLETE")
    print("=" * 60)
    print(f"\nReport: {report_path}")
    print(f"Decision: {overall_decision}")

    return overall_decision


if __name__ == "__main__":
    decision = main()
    sys.exit(0 if "GO" in decision else 1)
