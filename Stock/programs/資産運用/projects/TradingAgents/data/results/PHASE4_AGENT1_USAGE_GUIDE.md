# Phase 4 Agent 1 - Usage Guide

Quick start guide for using the real data backtest implementation.

---

## Quick Start (Demo Mode)

Run the demo backtest using sample data (no dependencies required):

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents
python3 scripts/run_real_data_backtest_demo.py
```

**Output**:
- Console output with backtest results
- Report saved to: `data/results/phase4_real_data_backtest_report_[timestamp].md`

---

## Quick Start (Production Mode)

### Prerequisites

1. **Python 3.10+** (required for yfinance)
2. **Install yfinance**:

```bash
pip install yfinance
```

### Run Production Backtest

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents
python3 scripts/run_real_data_backtest.py
```

**What it does**:
1. Fetches Nikkei 225 data from Yahoo Finance (2020-2025)
2. Caches data locally for faster subsequent runs
3. Splits data into train (2020-2022) and test (2023-2025)
4. Generates trading signals using SMA crossover
5. Runs backtest with Phase 3 engine
6. Calculates overfitting metrics
7. Generates comprehensive report

---

## Run Unit Tests

### With pytest (recommended)

```bash
pip install pytest
pytest src/tests/test_real_data_loader.py -v
```

### Without pytest (simple runner)

```bash
python3 scripts/test_real_data_loader_simple.py
```

**Expected output**: 7/7 tests passed

---

## Using RealDataLoader Programmatically

### Example 1: Fetch and Cache Data

```python
from src.data.real_data_loader import RealDataLoader

# Initialize loader
loader = RealDataLoader(
    ticker="^N225",
    start_date="2020-01-01",
    end_date="2025-12-31"
)

# Fetch data (uses cache if available)
data = loader.fetch_data(use_cache=True)

print(f"Loaded {len(data)} data points")
print(data.head())
```

### Example 2: Split Train/Test

```python
# After fetching data
train_data, test_data = loader.split_train_test(
    train_start="2020-01-01",
    train_end="2022-12-31",
    test_start="2023-01-01",
    test_end="2025-12-31"
)

print(f"Train: {len(train_data)} points")
print(f"Test: {len(test_data)} points")
```

### Example 3: Check Data Quality

```python
# After fetching data
quality = loader.get_data_quality()

print(f"Completeness: {quality['completeness']}%")
print(f"Actual points: {quality['actual_points']}")
print(f"Missing points: {quality['missing_points']}")
print(f"Date gaps: {len(quality['date_gaps'])}")
```

### Example 4: Convenience Function

```python
from src.data.real_data_loader import load_nikkei225_data

# Quick data loading
data = load_nikkei225_data(
    start_date="2020-01-01",
    end_date="2025-12-31",
    use_cache=True
)
```

---

## Running Custom Backtests

### Example: Custom Strategy

```python
from src.data.real_data_loader import RealDataLoader
from src.backtest.backtest_engine import BacktestEngine

# Load data
loader = RealDataLoader()
data = loader.fetch_data()

# Generate custom signals
signals = [
    {
        'date': '2020-02-01',
        'action': 'buy',
        'entry_price': 23000,
        'stop_loss': 22500,
        'take_profit': 24000
    },
    {
        'date': '2020-03-01',
        'action': 'sell',
        'exit_price': 23800
    }
]

# Run backtest
engine = BacktestEngine(
    data=data,
    initial_capital=10_000_000,
    commission_pct=0.0005,
    slippage_pct=0.001
)

results = engine.run_backtest(signals)

print(f"Win Rate: {results['win_rate']:.2f}%")
print(f"Total Return: {results['total_return']:.2f}%")
print(f"Sharpe Ratio: {results['sharpe_ratio']:.2f}")
```

---

## Directory Structure

```
TradingAgents/
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   └── real_data_loader.py        # Data fetching module
│   ├── backtest/
│   │   └── backtest_engine.py         # Backtest engine (Phase 3)
│   └── tests/
│       └── test_real_data_loader.py   # Unit tests
├── scripts/
│   ├── run_real_data_backtest.py      # Production backtest
│   ├── run_real_data_backtest_demo.py # Demo backtest
│   └── test_real_data_loader_simple.py # Simple test runner
└── data/
    ├── cache/
    │   └── N225_20200101_20251231.csv # Cached data
    └── results/
        ├── phase4_real_data_backtest_report_*.md  # Reports
        ├── PHASE4_AGENT1_IMPLEMENTATION_SUMMARY.md
        └── PHASE4_AGENT1_USAGE_GUIDE.md (this file)
```

---

## Configuration Options

### RealDataLoader

| Parameter | Default | Description |
|-----------|---------|-------------|
| ticker | "^N225" | Yahoo Finance ticker symbol |
| start_date | "2020-01-01" | Start date (YYYY-MM-DD) |
| end_date | "2025-12-31" | End date (YYYY-MM-DD) |

### BacktestEngine

| Parameter | Default | Description |
|-----------|---------|-------------|
| initial_capital | 10,000,000 | Starting capital (JPY) |
| position_size_pct | 0.95 | Position size as % of capital |
| commission_pct | 0.0005 | Commission rate (0.05%) |
| slippage_pct | 0.001 | Slippage rate (0.1%) |

---

## Troubleshooting

### Issue: yfinance import error

**Error**: `TypeError: unsupported operand type(s) for |`

**Solution**: Upgrade to Python 3.10+

```bash
# Check Python version
python3 --version

# If < 3.10, use demo mode or upgrade Python
python3 scripts/run_real_data_backtest_demo.py
```

### Issue: No module named 'pytest'

**Solution**: Install pytest or use simple test runner

```bash
# Option 1: Install pytest
pip install pytest

# Option 2: Use simple runner
python3 scripts/test_real_data_loader_simple.py
```

### Issue: Cache not found

**Solution**: The first run will download data and create cache automatically

```bash
# Force fresh download (ignore cache)
# Edit run_real_data_backtest.py:
# Change: data = loader.fetch_data(use_cache=True)
# To: data = loader.fetch_data(use_cache=False)
```

---

## Performance Tips

1. **Use cache**: Set `use_cache=True` to avoid repeated downloads
2. **Reduce date range**: For faster testing, use shorter date ranges
3. **Sample data**: Use demo mode for quick iterations

---

## Next Steps

After running Phase 4 Agent 1:

1. **Review Report**: Check `data/results/phase4_real_data_backtest_report_*.md`
2. **Analyze Overfitting**: If degradation > 30%, consider:
   - Regime-based optimization (Phase 4 Agent 2)
   - Parameter tuning
   - Strategy adjustment
3. **Phase 4 Agent 2**: Regime-based optimization
4. **Phase 4 Agent 3**: KPI re-evaluation

---

## Support

For issues or questions:
1. Check `PHASE4_AGENT1_IMPLEMENTATION_SUMMARY.md` for technical details
2. Review test cases in `src/tests/test_real_data_loader.py`
3. Examine demo script for usage examples

---

**Last Updated**: 2026-01-01
**Version**: Phase 4 Agent 1
**Status**: Production Ready
