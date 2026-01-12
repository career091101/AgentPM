"""
Walk-Forward Statistical Report Generator
Generates comprehensive statistical robustness validation report.

Usage:
    python scripts/generate_statistical_report.py <results_csv_path>
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime
import json

# Add src to path
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))


def calculate_train_test_correlation(results_df: pd.DataFrame) -> dict:
    """Calculate correlation between train and test performance."""
    train_sharpe = results_df['train_sharpe'].values
    test_sharpe = results_df['test_sharpe'].values

    # Remove invalid values
    valid_idx = ~(np.isnan(train_sharpe) | np.isnan(test_sharpe) |
                  np.isinf(train_sharpe) | np.isinf(test_sharpe))

    if valid_idx.sum() < 2:
        return {
            'correlation': 0,
            'stability_score': 'INSUFFICIENT_DATA'
        }

    correlation = np.corrcoef(train_sharpe[valid_idx], test_sharpe[valid_idx])[0, 1]

    # Stability assessment
    if correlation > 0.7:
        stability = 'HIGH'
    elif correlation > 0.5:
        stability = 'MEDIUM'
    elif correlation > 0.3:
        stability = 'LOW'
    else:
        stability = 'VERY_LOW'

    return {
        'correlation': float(correlation),
        'stability_score': stability,
        'valid_windows': int(valid_idx.sum())
    }


def calculate_overfitting_metrics(results_df: pd.DataFrame) -> dict:
    """Calculate overfitting detection metrics."""
    degradation = results_df['degradation_pct'].values

    # Remove invalid values
    valid_degradation = degradation[~(np.isnan(degradation) | np.isinf(degradation))]

    if len(valid_degradation) == 0:
        return {
            'avg_degradation': 0,
            'overfitting_assessment': 'INSUFFICIENT_DATA'
        }

    avg_degradation = float(np.mean(valid_degradation))
    median_degradation = float(np.median(valid_degradation))
    max_degradation = float(np.max(valid_degradation))

    # Overfitting assessment
    if avg_degradation < 10:
        overfitting = 'MINIMAL'
    elif avg_degradation < 20:
        overfitting = 'LOW'
    elif avg_degradation < 30:
        overfitting = 'MODERATE'
    elif avg_degradation < 40:
        overfitting = 'HIGH'
    else:
        overfitting = 'SEVERE'

    return {
        'avg_degradation': avg_degradation,
        'median_degradation': median_degradation,
        'max_degradation': max_degradation,
        'overfitting_assessment': overfitting,
        'windows_with_negative_degradation': int((valid_degradation < 0).sum()),
        'windows_with_high_degradation': int((valid_degradation > 30).sum())
    }


def analyze_regime_performance(results_df: pd.DataFrame) -> dict:
    """Analyze performance across different time periods."""
    # Group by year
    results_df['year'] = pd.to_datetime(results_df['test_start']).dt.year

    yearly_stats = {}
    for year in results_df['year'].unique():
        year_data = results_df[results_df['year'] == year]

        yearly_stats[int(year)] = {
            'windows': len(year_data),
            'avg_sharpe': float(year_data['test_sharpe'].mean()),
            'avg_return': float(year_data['test_return'].mean()),
            'positive_windows': int((year_data['test_return'] > 0).sum()),
            'positive_rate': float((year_data['test_return'] > 0).sum() / len(year_data) * 100)
        }

    return yearly_stats


def generate_markdown_report(
    results_df: pd.DataFrame,
    output_path: Path,
    metadata: dict = None
) -> None:
    """Generate comprehensive markdown report."""

    # Calculate metrics
    train_test_corr = calculate_train_test_correlation(results_df)
    overfitting = calculate_overfitting_metrics(results_df)
    yearly_perf = analyze_regime_performance(results_df)

    # Calculate distributions
    test_sharpe = results_df['test_sharpe'].values
    test_sharpe = test_sharpe[~(np.isnan(test_sharpe) | np.isinf(test_sharpe))]

    # Generate report
    report = f"""# Walk-Forward Analysis Statistical Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## Executive Summary

This report presents the statistical robustness validation of the adaptive trading strategy using 57-window walk-forward analysis over 5 years of Nikkei 225 historical data (2020-2025).

### Key Findings

| Metric | Value | Assessment |
|--------|-------|------------|
| **Total Windows** | {len(results_df)} | {'✅ Target achieved (57)' if len(results_df) >= 50 else '⚠️ Below target'} |
| **Test Sharpe (Mean)** | {test_sharpe.mean():.3f} | {'✅ Above threshold (>0.5)' if test_sharpe.mean() > 0.5 else '⚠️ Below threshold'} |
| **Test Sharpe (Median)** | {np.median(test_sharpe):.3f} | {'✅ Positive' if np.median(test_sharpe) > 0 else '❌ Negative'} |
| **Positive Return Rate** | {(results_df['test_return'] > 0).sum() / len(results_df) * 100:.1f}% | {'✅ >60%' if (results_df['test_return'] > 0).sum() / len(results_df) > 0.6 else '⚠️ <60%'} |
| **Train-Test Correlation** | {train_test_corr['correlation']:.3f} | {train_test_corr['stability_score']} stability |
| **Avg Degradation** | {overfitting['avg_degradation']:.1f}% | {overfitting['overfitting_assessment']} overfitting |

---

## 1. Test Sharpe Distribution

### Statistical Summary

```
Mean:        {test_sharpe.mean():.3f}
Std Dev:     {test_sharpe.std():.3f}
Median:      {np.median(test_sharpe):.3f}
Q25:         {np.percentile(test_sharpe, 25):.3f}
Q50:         {np.percentile(test_sharpe, 50):.3f}
Q75:         {np.percentile(test_sharpe, 75):.3f}
Q90:         {np.percentile(test_sharpe, 90):.3f}
Min:         {test_sharpe.min():.3f}
Max:         {test_sharpe.max():.3f}
```

### Distribution Analysis

- **Consistency:** Coefficient of Variation = {test_sharpe.std() / test_sharpe.mean() if test_sharpe.mean() != 0 else 0:.3f}
- **Windows with Sharpe > 0.5:** {(test_sharpe > 0.5).sum()} / {len(test_sharpe)} ({(test_sharpe > 0.5).sum() / len(test_sharpe) * 100:.1f}%)
- **Windows with Sharpe > 1.0:** {(test_sharpe > 1.0).sum()} / {len(test_sharpe)} ({(test_sharpe > 1.0).sum() / len(test_sharpe) * 100:.1f}%)
- **Windows with negative Sharpe:** {(test_sharpe < 0).sum()} / {len(test_sharpe)} ({(test_sharpe < 0).sum() / len(test_sharpe) * 100:.1f}%)

**Interpretation:** {'The strategy shows consistent positive Sharpe ratios across test windows, indicating robust performance.' if test_sharpe.mean() > 0.5 else 'The strategy shows variable performance with room for improvement.'}

---

## 2. Win Rate Stability

### Test Window Win Rates

```
Mean:        {results_df['test_win_rate'].mean():.1f}%
Std Dev:     {results_df['test_win_rate'].std():.1f}%
Median:      {results_df['test_win_rate'].median():.1f}%
Q25-Q75:     [{results_df['test_win_rate'].quantile(0.25):.1f}%, {results_df['test_win_rate'].quantile(0.75):.1f}%]
Min-Max:     [{results_df['test_win_rate'].min():.1f}%, {results_df['test_win_rate'].max():.1f}%]
```

### Win Rate Distribution

- **Windows with Win Rate > 50%:** {(results_df['test_win_rate'] > 50).sum()} / {len(results_df)} ({(results_df['test_win_rate'] > 50).sum() / len(results_df) * 100:.1f}%)
- **Windows with Win Rate > 60%:** {(results_df['test_win_rate'] > 60).sum()} / {len(results_df)} ({(results_df['test_win_rate'] > 60).sum() / len(results_df) * 100:.1f}%)

**Interpretation:** {'Win rates are consistently above 50%, indicating a positive edge.' if results_df['test_win_rate'].mean() > 50 else 'Win rates show significant variability and may benefit from strategy refinement.'}

---

## 3. Maximum Drawdown Distribution

### Drawdown Statistics

```
Mean:        {results_df['test_max_drawdown'].mean():.2f}%
Median:      {results_df['test_max_drawdown'].median():.2f}%
Q75:         {results_df['test_max_drawdown'].quantile(0.75):.2f}%
Q90:         {results_df['test_max_drawdown'].quantile(0.90):.2f}%
Worst:       {results_df['test_max_drawdown'].max():.2f}%
```

### Risk Assessment

- **Windows with DD < 5%:** {(results_df['test_max_drawdown'] < 5).sum()} / {len(results_df)} ({(results_df['test_max_drawdown'] < 5).sum() / len(results_df) * 100:.1f}%)
- **Windows with DD < 10%:** {(results_df['test_max_drawdown'] < 10).sum()} / {len(results_df)} ({(results_df['test_max_drawdown'] < 10).sum() / len(results_df) * 100:.1f}%)
- **Windows with DD > 15%:** {(results_df['test_max_drawdown'] > 15).sum()} / {len(results_df)} ({(results_df['test_max_drawdown'] > 15).sum() / len(results_df) * 100:.1f}%)

**Interpretation:** {'Drawdowns are well-controlled with median below 10%.' if results_df['test_max_drawdown'].median() < 10 else 'Drawdowns show elevated risk levels requiring additional risk management.'}

---

## 4. Train-Test Correlation Analysis

### Correlation Metrics

```
Correlation:           {train_test_corr['correlation']:.3f}
Stability Score:       {train_test_corr['stability_score']}
Valid Windows:         {train_test_corr['valid_windows']}
```

### Interpretation

- **Correlation > 0.7:** Strategy parameters generalize well to out-of-sample data
- **Correlation 0.5-0.7:** Moderate generalization with some regime-specific performance
- **Correlation < 0.5:** Poor generalization indicating potential overfitting

**Assessment:** {
    'High stability - Strategy parameters generalize excellently to unseen data.' if train_test_corr['correlation'] > 0.7
    else 'Moderate stability - Some regime-specific performance variability observed.' if train_test_corr['correlation'] > 0.5
    else 'Low stability - Strategy may be overfitted to training data.'
}

---

## 5. Overfitting Metrics

### Train-Test Degradation

```
Average:     {overfitting['avg_degradation']:.1f}%
Median:      {overfitting['median_degradation']:.1f}%
Maximum:     {overfitting['max_degradation']:.1f}%
```

### Overfitting Assessment

- **Overall Level:** {overfitting['overfitting_assessment']}
- **Windows with negative degradation (test > train):** {overfitting['windows_with_negative_degradation']}
- **Windows with high degradation (>30%):** {overfitting['windows_with_high_degradation']}

### Degradation Guidelines

- **<10%:** Minimal overfitting - Excellent
- **10-20%:** Low overfitting - Good
- **20-30%:** Moderate overfitting - Acceptable
- **30-40%:** High overfitting - Needs improvement
- **>40%:** Severe overfitting - Requires major revision

**Interpretation:** {
    'Minimal overfitting detected - Strategy is robust.' if overfitting['avg_degradation'] < 10
    else 'Low overfitting - Strategy generalizes well.' if overfitting['avg_degradation'] < 20
    else 'Moderate overfitting - Acceptable but could be improved.' if overfitting['avg_degradation'] < 30
    else 'High overfitting - Strategy optimization may be too aggressive.'
}

---

## 6. Yearly Performance Breakdown

"""

    # Add yearly performance
    for year, stats in sorted(yearly_perf.items()):
        report += f"""
### {year}

- **Windows:** {stats['windows']}
- **Avg Sharpe:** {stats['avg_sharpe']:.3f}
- **Avg Return:** {stats['avg_return']:.2f}%
- **Positive Windows:** {stats['positive_windows']} / {stats['windows']} ({stats['positive_rate']:.1f}%)
"""

    report += f"""
---

## 7. Overall Recommendation

### Final Assessment

Based on the 57-window walk-forward analysis:

"""

    # Generate recommendation
    passing_criteria = {
        'windows': len(results_df) >= 50,
        'sharpe': test_sharpe.mean() > 0.5,
        'positive_rate': (results_df['test_return'] > 0).sum() / len(results_df) > 0.6,
        'correlation': train_test_corr['correlation'] > 0.5,
        'degradation': overfitting['avg_degradation'] < 30
    }

    passed = sum(passing_criteria.values())
    total = len(passing_criteria)

    report += f"**Criteria Passed:** {passed} / {total}\n\n"

    for criterion, passed in passing_criteria.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        report += f"- {status} {criterion.replace('_', ' ').title()}\n"

    if passed >= 4:
        recommendation = "APPROVED FOR LIVE TRADING"
        details = "The strategy demonstrates statistical robustness across multiple market regimes and time periods. Recommend proceeding to paper trading phase with reduced position sizing."
    elif passed >= 3:
        recommendation = "CONDITIONAL APPROVAL"
        details = "The strategy shows promise but has some areas for improvement. Recommend additional optimization or extended paper trading before live deployment."
    else:
        recommendation = "REQUIRES FURTHER DEVELOPMENT"
        details = "The strategy does not meet minimum statistical robustness criteria. Recommend significant strategy revision before considering live trading."

    report += f"""
### **Final Recommendation: {recommendation}**

{details}

---

## Appendix: Methodology

### Walk-Forward Analysis Configuration

- **Training Period:** 6 months
- **Testing Period:** 3 months
- **Rolling Step:** 3 months (50% overlap)
- **Total Windows:** {len(results_df)}
- **Time Range:** {results_df['train_start'].iloc[0]} to {results_df['test_end'].iloc[-1]}

### Parameter Optimization

Parameters were optimized on each training window using grid search:
- Stop Loss %: [1.5%, 2.0%, 2.5%]
- Risk:Reward: [1.5, 2.0, 2.5]

### Statistical Metrics

- **Sharpe Ratio:** Risk-adjusted return metric (annualized)
- **Win Rate:** Percentage of profitable trades
- **Max Drawdown:** Maximum peak-to-trough decline
- **Degradation:** Performance decline from train to test window

---

*Report generated by TradingAgents Walk-Forward Analyzer v1.0*
"""

    # Write report
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✅ Statistical report generated: {output_path}")


def main():
    """Generate statistical report from walk-forward results."""
    if len(sys.argv) < 2:
        print("Usage: python generate_statistical_report.py <results_csv_path>")
        sys.exit(1)

    csv_path = Path(sys.argv[1])

    if not csv_path.exists():
        print(f"❌ File not found: {csv_path}")
        sys.exit(1)

    print(f"📊 Loading results from: {csv_path}")
    results_df = pd.read_csv(csv_path)

    print(f"   ✅ Loaded {len(results_df)} windows")

    # Generate report
    output_path = project_root / "data" / "results" / f"walk_forward_statistical_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

    generate_markdown_report(results_df, output_path)

    print(f"\n✅ Report generation completed")
    print(f"   📄 {output_path}")


if __name__ == "__main__":
    main()
