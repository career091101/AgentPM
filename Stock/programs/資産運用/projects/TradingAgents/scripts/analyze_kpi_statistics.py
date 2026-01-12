"""
KPI Statistics Analyzer
Analyze KPI distributions from walk-forward analysis and propose achievable targets.

Features:
- Load walk-forward results
- Calculate KPI distribution statistics (median, quartiles, percentiles)
- Estimate target achievement probabilities
- Visualize KPI distributions (histograms, box plots)
- Propose 3-tier KPI targets (conservative, standard, aggressive)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys
from typing import Dict, List

# Add src to path for imports
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / 'src'))


class KPIStatisticsAnalyzer:
    """
    Analyze KPI statistics from walk-forward results.

    Example usage:
        analyzer = KPIStatisticsAnalyzer(results_csv='walk_forward_results.csv')
        stats = analyzer.calculate_statistics()
        targets = analyzer.propose_targets()
        analyzer.visualize_distributions(output_dir='./figures')
    """

    def __init__(self, results_csv: str = None, results_dict: Dict = None):
        """
        Initialize KPI statistics analyzer.

        Args:
            results_csv: Path to CSV file with walk-forward results
            results_dict: Or dict with walk-forward results
        """
        if results_csv:
            self.df = pd.read_csv(results_csv)
        elif results_dict:
            # Extract window results into DataFrame
            windows_data = []
            for window in results_dict['windows']:
                row = {
                    'window_id': window['window_id'],
                    'test_sharpe': window['test_metrics']['sharpe_ratio'],
                    'test_return': window['test_metrics']['total_return'],
                    'test_win_rate': window['test_metrics']['win_rate'],
                    'test_max_drawdown': window['test_metrics']['max_drawdown'],
                    'test_trades': window['test_metrics']['total_trades'],
                    'degradation_pct': window['degradation_pct']
                }
                windows_data.append(row)
            self.df = pd.DataFrame(windows_data)
        else:
            raise ValueError("Must provide either results_csv or results_dict")

        # KPI columns to analyze
        self.kpi_columns = {
            'sharpe_ratio': 'test_sharpe',
            'total_return': 'test_return',
            'win_rate': 'test_win_rate',
            'max_drawdown': 'test_max_drawdown'
        }

    def calculate_statistics(self) -> Dict:
        """
        Calculate comprehensive statistics for all KPIs.

        Returns:
            Dict with statistics for each KPI:
                {
                    'sharpe_ratio': {
                        'median': float,
                        'mean': float,
                        'std': float,
                        'q25': float,
                        'q50': float,
                        'q75': float,
                        'q90': float,
                        'min': float,
                        'max': float,
                        'coefficient_of_variation': float
                    },
                    ...
                }
        """
        statistics = {}

        for kpi_name, col_name in self.kpi_columns.items():
            values = self.df[col_name].values

            statistics[kpi_name] = {
                'median': float(np.median(values)),
                'mean': float(np.mean(values)),
                'std': float(np.std(values)),
                'q10': float(np.percentile(values, 10)),
                'q25': float(np.percentile(values, 25)),
                'q50': float(np.percentile(values, 50)),
                'q75': float(np.percentile(values, 75)),
                'q90': float(np.percentile(values, 90)),
                'min': float(np.min(values)),
                'max': float(np.max(values)),
                'coefficient_of_variation': float(np.std(values) / np.mean(values)) if np.mean(values) != 0 else 0
            }

        return statistics

    def calculate_achievement_probability(self, kpi_name: str, target_value: float) -> float:
        """
        Calculate probability of achieving a specific KPI target.

        Args:
            kpi_name: KPI name (e.g., 'sharpe_ratio')
            target_value: Target value to achieve

        Returns:
            Achievement probability (0-100%)
        """
        col_name = self.kpi_columns[kpi_name]
        values = self.df[col_name].values

        # For drawdown (negative is better), flip comparison
        if kpi_name == 'max_drawdown':
            achieved = np.sum(values <= target_value)
        else:
            achieved = np.sum(values >= target_value)

        probability = (achieved / len(values)) * 100

        return float(probability)

    def propose_targets(self) -> Dict:
        """
        Propose 3-tier KPI targets based on distribution statistics.

        Returns:
            Dict with target proposals:
                {
                    'conservative': {
                        'sharpe_ratio': float,
                        'total_return': float,
                        ...
                        'achievement_probability': 75%
                    },
                    'standard': {
                        ...
                        'achievement_probability': 50%
                    },
                    'aggressive': {
                        ...
                        'achievement_probability': 25%
                    }
                }
        """
        stats = self.calculate_statistics()

        targets = {
            'conservative': {
                'description': '保守的目標（達成確率75%）',
                'achievement_probability': 75,
                'targets': {}
            },
            'standard': {
                'description': '標準目標（達成確率50%、中央値）',
                'achievement_probability': 50,
                'targets': {}
            },
            'aggressive': {
                'description': '挑戦目標（達成確率25%）',
                'achievement_probability': 25,
                'targets': {}
            }
        }

        # Conservative: 25th percentile (75% achievement rate)
        for kpi_name in self.kpi_columns.keys():
            if kpi_name == 'max_drawdown':
                # For drawdown, use 75th percentile (worse drawdown, easier to achieve)
                targets['conservative']['targets'][kpi_name] = stats[kpi_name]['q75']
            else:
                targets['conservative']['targets'][kpi_name] = stats[kpi_name]['q25']

        # Standard: 50th percentile (median, 50% achievement rate)
        for kpi_name in self.kpi_columns.keys():
            targets['standard']['targets'][kpi_name] = stats[kpi_name]['q50']

        # Aggressive: 75th percentile (25% achievement rate)
        for kpi_name in self.kpi_columns.keys():
            if kpi_name == 'max_drawdown':
                # For drawdown, use 25th percentile (better drawdown, harder to achieve)
                targets['aggressive']['targets'][kpi_name] = stats[kpi_name]['q25']
            else:
                targets['aggressive']['targets'][kpi_name] = stats[kpi_name]['q75']

        return targets

    def compare_with_current_targets(self, current_targets: Dict) -> Dict:
        """
        Compare proposed targets with current KPI targets.

        Args:
            current_targets: Current KPI targets
                            {'sharpe_ratio': 1.0, 'win_rate': 60, ...}

        Returns:
            Dict with comparison results
        """
        stats = self.calculate_statistics()
        proposed = self.propose_targets()

        comparison = {}

        for kpi_name, current_value in current_targets.items():
            if kpi_name not in self.kpi_columns:
                continue

            # Calculate achievement probability of current target
            achievement_prob = self.calculate_achievement_probability(kpi_name, current_value)

            # Find which tier current target corresponds to
            tier = 'unrealistic'
            if achievement_prob >= 70:
                tier = 'conservative'
            elif achievement_prob >= 40:
                tier = 'standard'
            elif achievement_prob >= 20:
                tier = 'aggressive'

            comparison[kpi_name] = {
                'current_target': current_value,
                'median': stats[kpi_name]['median'],
                'achievement_probability': achievement_prob,
                'tier': tier,
                'proposed_conservative': proposed['conservative']['targets'][kpi_name],
                'proposed_standard': proposed['standard']['targets'][kpi_name],
                'proposed_aggressive': proposed['aggressive']['targets'][kpi_name]
            }

        return comparison

    def visualize_distributions(self, output_dir: str = None) -> None:
        """
        Visualize KPI distributions with histograms and box plots.

        Args:
            output_dir: Directory to save figures (optional)
        """
        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(parents=True, exist_ok=True)

        # Set style
        sns.set_style('whitegrid')

        # Create figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle('Walk-forward Analysis: KPI Distributions', fontsize=16, fontweight='bold')

        kpi_names = list(self.kpi_columns.keys())
        stats = self.calculate_statistics()

        for idx, (kpi_name, col_name) in enumerate(self.kpi_columns.items()):
            ax = axes[idx // 2, idx % 2]
            values = self.df[col_name].values

            # Histogram
            ax.hist(values, bins=15, alpha=0.7, color='steelblue', edgecolor='black')

            # Add vertical lines for quartiles
            q25 = stats[kpi_name]['q25']
            q50 = stats[kpi_name]['q50']
            q75 = stats[kpi_name]['q75']

            ax.axvline(q25, color='green', linestyle='--', linewidth=2, label=f'Q25: {q25:.2f}')
            ax.axvline(q50, color='orange', linestyle='-', linewidth=2, label=f'Median: {q50:.2f}')
            ax.axvline(q75, color='red', linestyle='--', linewidth=2, label=f'Q75: {q75:.2f}')

            # Labels
            ax.set_title(f'{kpi_name.replace("_", " ").title()}', fontweight='bold')
            ax.set_xlabel('Value')
            ax.set_ylabel('Frequency')
            ax.legend()
            ax.grid(True, alpha=0.3)

        plt.tight_layout()

        if output_dir:
            fig.savefig(output_path / 'kpi_distributions_histogram.png', dpi=300, bbox_inches='tight')
            print(f"✅ Histogram saved to {output_path / 'kpi_distributions_histogram.png'}")

        # Box plots
        fig2, ax2 = plt.subplots(figsize=(10, 6))

        box_data = [self.df[col_name].values for col_name in self.kpi_columns.values()]
        box_labels = [name.replace('_', ' ').title() for name in self.kpi_columns.keys()]

        # Normalize data for visualization (different scales)
        # Use z-score normalization
        normalized_data = []
        for data in box_data:
            z_scores = (data - np.mean(data)) / np.std(data)
            normalized_data.append(z_scores)

        bp = ax2.boxplot(normalized_data, labels=box_labels, patch_artist=True,
                        showmeans=True, meanline=True)

        # Color boxes
        for patch in bp['boxes']:
            patch.set_facecolor('lightblue')
            patch.set_alpha(0.7)

        ax2.set_title('Walk-forward Analysis: KPI Box Plots (Normalized)', fontsize=14, fontweight='bold')
        ax2.set_ylabel('Z-Score (Normalized)')
        ax2.grid(True, alpha=0.3, axis='y')

        plt.xticks(rotation=15, ha='right')
        plt.tight_layout()

        if output_dir:
            fig2.savefig(output_path / 'kpi_distributions_boxplot.png', dpi=300, bbox_inches='tight')
            print(f"✅ Box plot saved to {output_path / 'kpi_distributions_boxplot.png'}")

        if not output_dir:
            plt.show()

    def generate_report(self, output_path: str, current_targets: Dict = None) -> None:
        """
        Generate comprehensive KPI statistics report in Markdown.

        Args:
            output_path: Path to output Markdown file
            current_targets: Current KPI targets (optional)
        """
        stats = self.calculate_statistics()
        proposed = self.propose_targets()

        report_lines = [
            "# KPI Statistics Analysis Report",
            "",
            f"**Analysis Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Total Windows Analyzed**: {len(self.df)}",
            "",
            "## Walk-forward Analysis Summary",
            "",
            f"- Total windows: {len(self.df)}",
            f"- Positive return windows: {sum(self.df['test_return'] > 0)} ({sum(self.df['test_return'] > 0) / len(self.df) * 100:.1f}%)",
            f"- Average degradation: {self.df['degradation_pct'].mean():.1f}%",
            "",
            "## KPI Distribution Statistics",
            ""
        ]

        # Statistics table
        for kpi_name, kpi_stats in stats.items():
            report_lines.extend([
                f"### {kpi_name.replace('_', ' ').title()}",
                "",
                "| Statistic | Value |",
                "|-----------|-------|",
                f"| Median | {kpi_stats['median']:.3f} |",
                f"| Mean | {kpi_stats['mean']:.3f} |",
                f"| Std Dev | {kpi_stats['std']:.3f} |",
                f"| 10th Percentile | {kpi_stats['q10']:.3f} |",
                f"| 25th Percentile (Q1) | {kpi_stats['q25']:.3f} |",
                f"| 50th Percentile (Median) | {kpi_stats['q50']:.3f} |",
                f"| 75th Percentile (Q3) | {kpi_stats['q75']:.3f} |",
                f"| 90th Percentile | {kpi_stats['q90']:.3f} |",
                f"| Min | {kpi_stats['min']:.3f} |",
                f"| Max | {kpi_stats['max']:.3f} |",
                f"| Coefficient of Variation | {kpi_stats['coefficient_of_variation']:.3f} |",
                ""
            ])

        # Proposed targets
        report_lines.extend([
            "## Proposed KPI Targets (3-Tier)",
            "",
            "### Conservative Target (達成確率75%)",
            "",
            "| KPI | Target Value |",
            "|-----|--------------|"
        ])

        for kpi_name, value in proposed['conservative']['targets'].items():
            report_lines.append(f"| {kpi_name.replace('_', ' ').title()} | {value:.3f} |")

        report_lines.extend([
            "",
            "### Standard Target (達成確率50%、中央値)",
            "",
            "| KPI | Target Value |",
            "|-----|--------------|"
        ])

        for kpi_name, value in proposed['standard']['targets'].items():
            report_lines.append(f"| {kpi_name.replace('_', ' ').title()} | {value:.3f} |")

        report_lines.extend([
            "",
            "### Aggressive Target (達成確率25%)",
            "",
            "| KPI | Target Value |",
            "|-----|--------------|"
        ])

        for kpi_name, value in proposed['aggressive']['targets'].items():
            report_lines.append(f"| {kpi_name.replace('_', ' ').title()} | {value:.3f} |")

        # Current targets comparison (if provided)
        if current_targets:
            comparison = self.compare_with_current_targets(current_targets)

            report_lines.extend([
                "",
                "## Current vs Proposed Targets Comparison",
                "",
                "| KPI | Current | Achievement % | Tier | Proposed (Standard) |",
                "|-----|---------|---------------|------|---------------------|"
            ])

            for kpi_name, comp in comparison.items():
                report_lines.append(
                    f"| {kpi_name.replace('_', ' ').title()} | "
                    f"{comp['current_target']:.2f} | "
                    f"{comp['achievement_probability']:.1f}% | "
                    f"{comp['tier']} | "
                    f"{comp['proposed_standard']:.2f} |"
                )

        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report_lines))

        print(f"\n✅ KPI statistics report generated: {output_path}")


# Main execution
if __name__ == "__main__":
    print("KPI Statistics Analyzer")
    print("=" * 60)

    # Example: Load walk-forward results and analyze
    results_csv = project_root / 'data' / 'results' / 'walk_forward_results.csv'

    if results_csv.exists():
        analyzer = KPIStatisticsAnalyzer(results_csv=str(results_csv))

        # Calculate statistics
        print("\n1. Calculating KPI statistics...")
        stats = analyzer.calculate_statistics()

        print("\nKPI Statistics Summary:")
        for kpi_name, kpi_stats in stats.items():
            print(f"\n{kpi_name.upper()}:")
            print(f"  Median: {kpi_stats['median']:.3f}")
            print(f"  Q25-Q75: [{kpi_stats['q25']:.3f}, {kpi_stats['q75']:.3f}]")

        # Propose targets
        print("\n2. Proposing KPI targets...")
        targets = analyzer.propose_targets()

        print("\nProposed Targets:")
        for tier_name, tier_data in targets.items():
            print(f"\n{tier_name.upper()} ({tier_data['description']}):")
            for kpi_name, value in tier_data['targets'].items():
                print(f"  {kpi_name}: {value:.3f}")

        # Visualize
        print("\n3. Generating visualizations...")
        output_dir = project_root / 'data' / 'results' / 'kpi_analysis'
        analyzer.visualize_distributions(output_dir=str(output_dir))

        # Generate report
        print("\n4. Generating report...")
        report_path = output_dir / 'kpi_statistics_report.md'

        # Example current targets
        current_targets = {
            'sharpe_ratio': 1.0,
            'total_return': 3.0,
            'win_rate': 60.0,
            'max_drawdown': -10.0
        }

        analyzer.generate_report(str(report_path), current_targets=current_targets)

        print("\n" + "=" * 60)
        print("✅ KPI analysis completed")
    else:
        print(f"❌ Results file not found: {results_csv}")
        print("   Please run walk-forward analysis first")
