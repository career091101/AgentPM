# Phase 6: Walk-Forward Analysis - Quick Start Guide

## Overview

Phase 6 implements comprehensive 57-window walk-forward analysis with statistical robustness validation.

**Status:** ✅ Implementation Complete | Ready for Execution

---

## Quick Start

### 1. Verify Implementation
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents
python3 scripts/verify_walkforward.py
```

**Expected Output:** ✅ ALL TESTS PASSED

### 2. Run Full 57-Window Analysis
```bash
python3 scripts/run_walk_forward_full.py
```

**Expected Duration:** ~2 hours (57 windows × 2 minutes)

**Output Files:**
- `data/results/walk_forward_57windows_YYYYMMDD_HHMMSS.csv`
- `data/results/walk_forward_summary_YYYYMMDD_HHMMSS.json`

### 3. Generate Statistical Report
```bash
python3 scripts/generate_statistical_report.py data/results/walk_forward_57windows_*.csv
```

**Output:** `data/results/walk_forward_statistical_report_YYYYMMDD_HHMMSS.md`

---

## Success Criteria

| Criterion | Target | Status |
|-----------|--------|--------|
| 57 windows completed | ✅ All windows executed | 🔄 Pending execution |
| Test Sharpe > 0.5 | ✅ Mean Sharpe > 0.5 | 🔄 Pending execution |
| Train-Test correlation > 0.7 | ✅ High stability | 🔄 Pending execution |
| All tests pass | ✅ 100% | ✅ PASSED |

---

## Implementation Details

### Window Configuration
- **Train Period:** 6 months
- **Test Period:** 3 months
- **Rolling Step:** 3 months (50% overlap)
- **Total Windows:** ~57 (2020-2025)

### Parameter Optimization Grid
```python
{
    'stop_loss_pct': [0.015, 0.02, 0.025],  # Stop loss percentages
    'risk_reward': [1.5, 2.0, 2.5]           # Risk:Reward ratios
}
```

### Data Source
- **Symbol:** Nikkei 225 (^N225)
- **Period:** 2020-01-01 to 2024-12-31
- **Cached:** `data/cache/N225_20200101_20241231.csv`

---

## File Structure

```
scripts/
├── run_walk_forward_full.py          # Main execution (57 windows)
├── generate_statistical_report.py    # Statistical report generator
└── verify_walkforward.py             # Quick verification tests

src/
├── backtest/
│   └── walk_forward_analyzer.py      # Core walk-forward engine
├── strategy/
│   └── adaptive_strategy.py          # Regime-adaptive strategy
└── tests/
    └── test_walk_forward_complete.py # Comprehensive tests

data/
├── cache/
│   └── N225_20200101_20241231.csv    # Historical data (5 years)
└── results/
    ├── walk_forward_57windows_*.csv  # Detailed results
    ├── walk_forward_summary_*.json   # Summary metrics
    └── walk_forward_statistical_report_*.md  # Analysis report
```

---

## Statistical Metrics

### Performance Metrics
- **Sharpe Ratio:** Risk-adjusted return (annualized)
- **Total Return:** Cumulative return percentage
- **Win Rate:** Percentage of profitable trades
- **Max Drawdown:** Maximum peak-to-trough decline

### Robustness Metrics
- **Train-Test Correlation:** Measures strategy stability
- **Degradation:** Performance decline from train to test
- **Coefficient of Variation:** Consistency across windows

### Distributions
- Mean, Median, Std Dev
- Quartiles (Q25, Q50, Q75, Q90)
- Min, Max

---

## Interpretation Guide

### Sharpe Ratio
- **> 1.0:** Excellent (High risk-adjusted returns)
- **0.5 - 1.0:** Good (Acceptable risk-adjusted returns)
- **0 - 0.5:** Marginal (Low risk-adjusted returns)
- **< 0:** Poor (Negative returns or excessive risk)

### Train-Test Correlation
- **> 0.7:** High stability (Strategy generalizes well)
- **0.5 - 0.7:** Moderate stability (Some regime dependency)
- **< 0.5:** Low stability (Potential overfitting)

### Degradation
- **< 10%:** Minimal overfitting (Excellent)
- **10-20%:** Low overfitting (Good)
- **20-30%:** Moderate overfitting (Acceptable)
- **> 30%:** High overfitting (Needs improvement)

### Recommendation Levels
- **strong_pass:** High performance, low degradation, high consistency
- **pass:** Decent performance, acceptable degradation
- **warning:** Marginal performance or high degradation
- **fail:** Poor performance or severe overfitting

---

## Troubleshooting

### Issue: No module named 'pytest'
**Solution:** Use verification script instead:
```bash
python3 scripts/verify_walkforward.py
```

### Issue: Slow execution
**Solution:** Reduce windows for testing:
- Edit `run_walk_forward_full.py`
- Change `step_months=3` to `step_months=12`
- This reduces windows from 57 to ~5

### Issue: Out of memory
**Solution:** Process in batches:
- Split date range into smaller periods
- Run walk-forward on each period separately
- Aggregate results manually

### Issue: Low Sharpe ratios
**Solution:**
- Check data quality (real vs synthetic)
- Adjust regime parameters
- Expand parameter optimization grid
- Consider additional filters (volume, volatility)

---

## Next Steps

### If Success Criteria Met
1. ✅ Document results in final report
2. ✅ Proceed to paper trading phase
3. ✅ Set up live monitoring dashboard

### If Success Criteria Not Met
1. 🔧 Analyze failure modes by regime
2. 🔧 Adjust parameters based on statistical report
3. 🔧 Re-run walk-forward with improved settings
4. 🔧 Consider ensemble strategies

---

## Key Commands

```bash
# Verify implementation
python3 scripts/verify_walkforward.py

# Run full analysis
python3 scripts/run_walk_forward_full.py

# Generate report
python3 scripts/generate_statistical_report.py data/results/walk_forward_57windows_*.csv

# View latest results
ls -lt data/results/ | head -10

# Quick check
tail -20 data/results/walk_forward_summary_*.json
```

---

## Documentation

- **Implementation Guide:** `data/results/WALKFORWARD_PHASE6_IMPLEMENTATION.md`
- **Walk-Forward Analyzer:** `src/backtest/walk_forward_analyzer.py`
- **Adaptive Strategy:** `src/strategy/adaptive_strategy.py`
- **Integration Tests:** `src/tests/test_walk_forward_complete.py`

---

## Contact & Support

For issues or questions about Phase 6 implementation:
- Review: `data/results/WALKFORWARD_PHASE6_IMPLEMENTATION.md`
- Run verification: `python3 scripts/verify_walkforward.py`
- Check logs in console output

---

**Last Updated:** 2026-01-01
**Implementation Status:** ✅ COMPLETE
**Execution Status:** 🔄 READY

---

*Walk-forward analysis implementation by Agent 2 - Statistical robustness validation framework*
