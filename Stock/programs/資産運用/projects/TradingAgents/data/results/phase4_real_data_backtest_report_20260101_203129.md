# Phase 4 - Real Data Backtest Report (Demo)

**Generated**: 2026-01-01 20:31:29
**Note**: This is a demonstration using sample data. For production, use actual Yahoo Finance data.

## Executive Summary

Comprehensive backtesting on simulated Nikkei 225 data from 2020 to 2025, using the high-reliability backtest engine developed in Phase 3.

### Configuration

- **Strategy**: Simple Moving Average Crossover (20/50 periods)
- **Test Period**: 2020-01-01 to 2025-12-31 (5 years)
- **Initial Capital**: ¥10,000,000
- **Commission**: 0.05%
- **Slippage**: 0.1%
- **Risk per Trade**: 2%

---

## 1. Full Period Performance (2020-2025)

| Metric | Value |
|--------|-------|
| Total Trades | 15 |
| Winning Trades | 6 |
| Losing Trades | 9 |
| Win Rate | 40.00% |
| Total Return | -0.57% |
| Sharpe Ratio | 0.14 |
| Max Drawdown | 6.13% |
| Final Capital | ¥9,943,234 |

---

## 2. Train vs Test Comparison

### Train Period (2020-2022)

| Metric | Value |
|--------|-------|
| Total Trades | 9 |
| Win Rate | 44.44% |
| Total Return | 0.79% |
| Sharpe Ratio | 0.41 |
| Max Drawdown | 6.13% |
| Final Capital | ¥10,078,876 |

### Test Period (2023-2025)

| Metric | Value |
|--------|-------|
| Total Trades | 6 |
| Win Rate | 33.33% |
| Total Return | -1.35% |
| Sharpe Ratio | -0.21 |
| Max Drawdown | 4.13% |
| Final Capital | ¥9,865,420 |

### Overfitting Assessment

| Metric | Train | Test | Degradation |
|--------|-------|------|-------------|
| Total Return | 0.79% | -1.35% | -270.62% |
| Sharpe Ratio | 0.41 | -0.21 | -150.64% |
| Win Rate | 44.44% | 33.33% | -25.00% |

**Assessment**: FAIL (Overfitting detected)

---

## 3. Success Criteria

- ✅ Data acquisition (sample data generated)
- ✅ Train/Test backtest completed
- ✅ Overfitting detection implemented
- ✅ Report generation completed
- ⚠️ Test success rate: Pending unit tests

---

## 4. Conclusions and Next Steps

### Key Insights

1. **Strategy Performance**: SMA crossover tested on 5-year sample data
2. **Overfitting Analysis**: Train/Test comparison reveals model generalization
3. **Risk Management**: 2% risk per trade with stop-loss enforcement

### Next Actions

1. **Install yfinance with Python 3.10+**: For real Yahoo Finance data
2. **Run unit tests**: `pytest src/tests/test_real_data_loader.py -v`
3. **Phase 4 Agent 2**: Regime-based optimization
4. **Phase 4 Agent 3**: KPI re-evaluation

---

**Report End**
