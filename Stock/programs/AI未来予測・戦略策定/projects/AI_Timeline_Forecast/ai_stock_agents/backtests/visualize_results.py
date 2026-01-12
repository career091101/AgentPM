"""
Backtest Results Visualization

Create equity curve, drawdown chart, and monthly returns heatmap
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from pathlib import Path
from datetime import datetime
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")


def load_backtest_result(result_path: Path) -> dict:
    """Load backtest result JSON"""
    with open(result_path) as f:
        return json.load(f)


def create_equity_curve(weekly_returns: pd.DataFrame, output_path: Path):
    """Create equity curve chart"""
    # Convert date column to datetime
    weekly_returns['date'] = pd.to_datetime(weekly_returns['date'])

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

    # Equity curve
    ax1.plot(weekly_returns['date'], weekly_returns['portfolio_value'],
             linewidth=2, label='AI Portfolio', color='#2E86AB')
    ax1.set_ylabel('Portfolio Value ($)', fontsize=12, fontweight='bold')
    ax1.set_title('AI Stock Portfolio - Equity Curve (2020-2024)',
                  fontsize=14, fontweight='bold', pad=20)
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc='upper left', fontsize=10)

    # Format y-axis as currency
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))

    # Add annotations for key milestones
    milestones = [
        (weekly_returns.iloc[0]['date'], weekly_returns.iloc[0]['portfolio_value'], 'Start\n$1.0M'),
        (weekly_returns.iloc[52]['date'], weekly_returns.iloc[52]['portfolio_value'], '2020 End\n$2.1M'),
        (weekly_returns.iloc[104]['date'], weekly_returns.iloc[104]['portfolio_value'], '2021 End\n$2.9M'),
        (weekly_returns.iloc[-1]['date'], weekly_returns.iloc[-1]['portfolio_value'], 'Final\n$5.0M'),
    ]

    for date, value, label in milestones:
        ax1.annotate(label, xy=(pd.to_datetime(date), value),
                    xytext=(10, 10), textcoords='offset points',
                    fontsize=8, bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.7),
                    arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

    # Weekly returns
    colors = ['green' if r >= 0 else 'red' for r in weekly_returns['return']]
    ax2.bar(weekly_returns['date'], weekly_returns['return'] * 100,
            color=colors, alpha=0.6, width=5)
    ax2.set_ylabel('Weekly Return (%)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    # Format x-axis
    ax2.xaxis.set_major_locator(mdates.YearLocator())
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax2.xaxis.set_minor_locator(mdates.MonthLocator((1, 4, 7, 10)))

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Equity curve saved: {output_path}")
    plt.close()


def create_drawdown_chart(weekly_returns: pd.DataFrame, output_path: Path):
    """Create drawdown chart"""
    # Convert date column to datetime
    weekly_returns['date'] = pd.to_datetime(weekly_returns['date'])

    # Calculate cumulative returns and drawdown
    cumulative = (1 + weekly_returns['return']).cumprod()
    running_max = cumulative.cummax()
    drawdown = (cumulative - running_max) / running_max

    fig, ax = plt.subplots(figsize=(14, 6))

    ax.fill_between(weekly_returns['date'], drawdown * 100, 0,
                     color='red', alpha=0.3, label='Drawdown')
    ax.plot(weekly_returns['date'], drawdown * 100,
            color='darkred', linewidth=1.5)

    ax.set_ylabel('Drawdown (%)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax.set_title('Portfolio Drawdown (2020-2024)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower left', fontsize=10)

    # Annotate max drawdown
    max_dd_idx = drawdown.idxmin()
    max_dd_date = weekly_returns.iloc[max_dd_idx]['date']
    max_dd_value = drawdown.iloc[max_dd_idx] * 100

    ax.annotate(f'Max DD: {max_dd_value:.1f}%\n{pd.to_datetime(max_dd_date).strftime("%Y-%m-%d")}',
                xy=(pd.to_datetime(max_dd_date), max_dd_value),
                xytext=(20, -40), textcoords='offset points',
                fontsize=10, bbox=dict(boxstyle='round,pad=0.5', fc='orange', alpha=0.8),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2',
                              color='red', lw=2))

    # Format x-axis
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator((1, 4, 7, 10)))

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Drawdown chart saved: {output_path}")
    plt.close()


def create_monthly_returns_heatmap(weekly_returns: pd.DataFrame, output_path: Path):
    """Create monthly returns heatmap"""
    # Convert to datetime
    weekly_returns['date'] = pd.to_datetime(weekly_returns['date'])
    weekly_returns.set_index('date', inplace=True)

    # Resample to monthly returns
    monthly = weekly_returns['return'].resample('M').apply(lambda x: np.prod(1 + x) - 1)

    # Create pivot table (Year x Month)
    monthly_df = pd.DataFrame({
        'Year': monthly.index.year,
        'Month': monthly.index.month,
        'Return': monthly.values * 100
    })

    pivot = monthly_df.pivot(index='Year', columns='Month', values='Return')
    pivot.columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                     'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Create heatmap
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.heatmap(pivot, annot=True, fmt='.1f', cmap='RdYlGn', center=0,
                cbar_kws={'label': 'Monthly Return (%)'},
                linewidths=0.5, linecolor='gray', ax=ax)

    ax.set_title('Monthly Returns Heatmap (2020-2024)',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Month', fontsize=12, fontweight='bold')
    ax.set_ylabel('Year', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Monthly heatmap saved: {output_path}")
    plt.close()


def create_performance_summary(result_data: dict, output_path: Path):
    """Create performance summary visualization"""
    metrics = result_data['metrics']

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Returns comparison
    returns_data = {
        'Total Return': float(metrics['returns']['total_return'].rstrip('%')),
        'Annualized': float(metrics['returns']['annualized_return'].rstrip('%')),
    }

    ax1.bar(returns_data.keys(), returns_data.values(), color=['#2E86AB', '#A23B72'])
    ax1.set_ylabel('Return (%)', fontweight='bold')
    ax1.set_title('Return Metrics', fontweight='bold', fontsize=12)
    ax1.grid(True, alpha=0.3, axis='y')

    for i, (k, v) in enumerate(returns_data.items()):
        ax1.text(i, v + 5, f'{v:.1f}%', ha='center', fontweight='bold')

    # 2. Risk-adjusted ratios
    ratios_data = {
        'Sharpe': float(metrics['risk_adjusted']['sharpe_ratio']),
        'Sortino': float(metrics['risk_adjusted']['sortino_ratio']),
        'Calmar': float(metrics['risk_adjusted']['calmar_ratio']),
    }

    ax2.bar(ratios_data.keys(), ratios_data.values(), color=['#F18F01', '#C73E1D', '#6A994E'])
    ax2.set_ylabel('Ratio', fontweight='bold')
    ax2.set_title('Risk-Adjusted Performance', fontweight='bold', fontsize=12)
    ax2.grid(True, alpha=0.3, axis='y')
    ax2.axhline(y=1.0, color='red', linestyle='--', linewidth=1, label='Target: 1.0')
    ax2.legend()

    for i, (k, v) in enumerate(ratios_data.items()):
        ax2.text(i, v + 0.05, f'{v:.2f}', ha='center', fontweight='bold')

    # 3. Risk metrics
    risk_data = {
        'Max DD': abs(float(metrics['risk']['max_drawdown'].rstrip('%'))),
        'Volatility': float(metrics['risk']['annualized_volatility'].rstrip('%')),
    }

    ax3.bar(risk_data.keys(), risk_data.values(), color=['red', 'orange'])
    ax3.set_ylabel('Percentage (%)', fontweight='bold')
    ax3.set_title('Risk Metrics', fontweight='bold', fontsize=12)
    ax3.grid(True, alpha=0.3, axis='y')

    for i, (k, v) in enumerate(risk_data.items()):
        ax3.text(i, v + 1, f'{v:.1f}%', ha='center', fontweight='bold')

    # 4. Trading stats
    win_rate = float(metrics['trading']['win_rate'].rstrip('%'))

    ax4.pie([win_rate, 100-win_rate], labels=['Wins', 'Losses'],
            autopct='%1.1f%%', startangle=90, colors=['green', 'red'])
    ax4.set_title(f'Win Rate: {win_rate:.1f}%', fontweight='bold', fontsize=12)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"✅ Performance summary saved: {output_path}")
    plt.close()


def main():
    # Find latest result files
    results_dir = Path(__file__).parent / "results"
    result_files = sorted(results_dir.glob("backtest_result_*.json"), reverse=True)
    csv_files = sorted(results_dir.glob("weekly_returns_*.csv"), reverse=True)

    if not result_files or not csv_files:
        print("❌ No backtest results found")
        return

    latest_result = result_files[0]
    latest_csv = csv_files[0]
    print(f"📊 Loading results from:")
    print(f"   JSON: {latest_result.name}")
    print(f"   CSV:  {latest_csv.name}")

    # Load data
    result_data = load_backtest_result(latest_result)
    weekly_returns = pd.read_csv(latest_csv)

    # Create output directory
    viz_dir = Path(__file__).parent / "visualizations"
    viz_dir.mkdir(exist_ok=True)

    print("\n🎨 Creating visualizations...")

    # Create all charts
    create_equity_curve(weekly_returns, viz_dir / "equity_curve.png")
    create_drawdown_chart(weekly_returns, viz_dir / "drawdown_chart.png")
    create_monthly_returns_heatmap(weekly_returns.copy(), viz_dir / "monthly_returns_heatmap.png")
    create_performance_summary(result_data, viz_dir / "performance_summary.png")

    print(f"\n✅ All visualizations created successfully!")
    print(f"   Output directory: {viz_dir}")
    print(f"\n📁 Generated files:")
    print(f"   - equity_curve.png")
    print(f"   - drawdown_chart.png")
    print(f"   - monthly_returns_heatmap.png")
    print(f"   - performance_summary.png")


if __name__ == "__main__":
    main()
