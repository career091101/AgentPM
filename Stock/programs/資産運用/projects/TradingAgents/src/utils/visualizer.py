"""
可視化モジュール

Phase 3で実装した分析結果を可視化するシンプルなユーティリティ。
以下の3つのグラフを生成：
  1. エクイティカーブ（資産推移）
  2. レジーム別パフォーマンス
  3. ドローダウンチャート
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Dict, Optional, List
import numpy as np


def plot_equity_curve(
    equity_curve: pd.Series,
    save_path: Optional[str] = None,
    title: str = "Equity Curve"
) -> None:
    """
    エクイティカーブを描画

    Args:
        equity_curve: 資本の推移（DatetimeIndex付きのSeries）
        save_path: 保存先パス。Noneの場合は表示のみ
        title: グラフタイトル
    """
    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(equity_curve.index, equity_curve.values, linewidth=2, color='blue')
    ax.fill_between(equity_curve.index, equity_curve.values, alpha=0.3, color='blue')

    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Equity ($)', fontsize=12)
    ax.grid(True, alpha=0.3)

    # 最終値を表示
    final_value = equity_curve.iloc[-1]
    initial_value = equity_curve.iloc[0]
    total_return = (final_value - initial_value) / initial_value * 100
    ax.text(
        0.02, 0.98,
        f'Total Return: {total_return:.2f}%',
        transform=ax.transAxes,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    )

    plt.tight_layout()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Equity curve saved to {save_path}")
    else:
        plt.show()

    plt.close()


def plot_regime_performance(
    regime_results: Dict,
    save_path: Optional[str] = None
) -> None:
    """
    レジーム別パフォーマンスを棒グラフで表示

    Args:
        regime_results: レジーム別バックテスト結果
            {
                'uptrend': {'sharpe_ratio': ..., 'total_return': ..., ...},
                'downtrend': {...},
                'range': {...},
                'high_volatility': {...}
            }
        save_path: 保存先パス。Noneの場合は表示のみ
    """
    regimes = ['uptrend', 'downtrend', 'range', 'high_volatility']
    sharpe_ratios = []
    total_returns = []
    win_rates = []

    for regime in regimes:
        if regime in regime_results and regime_results[regime]:
            result = regime_results[regime]
            sharpe_ratios.append(result.get('sharpe_ratio', 0))
            total_returns.append(result.get('total_return', 0))
            win_rates.append(result.get('win_rate', 0))
        else:
            sharpe_ratios.append(0)
            total_returns.append(0)
            win_rates.append(0)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # シャープレシオ
    colors_sharpe = ['green' if s > 0.3 else 'red' for s in sharpe_ratios]
    axes[0].bar(regimes, sharpe_ratios, color=colors_sharpe, alpha=0.7)
    axes[0].axhline(y=0.3, color='black', linestyle='--', linewidth=2, label='Min Threshold (0.3)')
    axes[0].axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    axes[0].set_title('Sharpe Ratio by Regime', fontsize=12, fontweight='bold')
    axes[0].set_ylabel('Sharpe Ratio', fontsize=11)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3, axis='y')

    # 総リターン
    colors_return = ['green' if r > 0 else 'red' for r in total_returns]
    axes[1].bar(regimes, total_returns, color=colors_return, alpha=0.7)
    axes[1].axhline(y=0, color='black', linestyle='-', linewidth=1)
    axes[1].set_title('Total Return by Regime', fontsize=12, fontweight='bold')
    axes[1].set_ylabel('Total Return (%)', fontsize=11)
    axes[1].grid(True, alpha=0.3, axis='y')

    # 勝率
    colors_winrate = ['green' if w > 50 else 'red' for w in win_rates]
    axes[2].bar(regimes, win_rates, color=colors_winrate, alpha=0.7)
    axes[2].axhline(y=50, color='black', linestyle='--', linewidth=2, label='50% (Break-even)')
    axes[2].set_title('Win Rate by Regime', fontsize=12, fontweight='bold')
    axes[2].set_ylabel('Win Rate (%)', fontsize=11)
    axes[2].set_ylim(0, 100)
    axes[2].legend()
    axes[2].grid(True, alpha=0.3, axis='y')

    plt.tight_layout()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Regime performance chart saved to {save_path}")
    else:
        plt.show()

    plt.close()


def plot_drawdown(
    equity_curve: pd.Series,
    save_path: Optional[str] = None
) -> None:
    """
    ドローダウンチャートを描画

    ドローダウン = 相対的ピーク以降の資本の低下率

    Args:
        equity_curve: 資本の推移（DatetimeIndex付きのSeries）
        save_path: 保存先パス。Noneの場合は表示のみ
    """
    # 累積最大値を計算
    cumulative_max = equity_curve.expanding().max()

    # ドローダウンを計算
    drawdown = (equity_curve - cumulative_max) / cumulative_max * 100

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

    # エクイティカーブ
    ax1.plot(equity_curve.index, equity_curve.values, linewidth=2, color='blue', label='Equity')
    ax1.plot(cumulative_max.index, cumulative_max.values, linewidth=1, color='green',
             linestyle='--', label='Cumulative Maximum')
    ax1.fill_between(equity_curve.index, equity_curve.values, cumulative_max.values,
                     alpha=0.3, color='red')
    ax1.set_title('Equity Curve with Drawdown', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Equity ($)', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # ドローダウン
    ax2.fill_between(drawdown.index, drawdown.values, alpha=0.5, color='red', label='Drawdown')
    ax2.plot(drawdown.index, drawdown.values, linewidth=1, color='darkred')
    ax2.set_title('Drawdown (%)', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Date', fontsize=12)
    ax2.set_ylabel('Drawdown (%)', fontsize=12)
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    # 最大ドローダウンを表示
    max_drawdown = drawdown.min()
    max_drawdown_date = drawdown.idxmin()
    ax2.text(
        0.02, 0.95,
        f'Max Drawdown: {max_drawdown:.2f}%\nDate: {max_drawdown_date.strftime("%Y-%m-%d")}',
        transform=ax2.transAxes,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7)
    )

    plt.tight_layout()

    if save_path:
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Drawdown chart saved to {save_path}")
    else:
        plt.show()

    plt.close()


def save_all_visualizations(
    equity_curve: pd.Series,
    regime_results: Optional[Dict] = None,
    output_dir: str = "data/visualizations"
) -> Dict[str, str]:
    """
    全ての可視化を一度に生成して保存

    Args:
        equity_curve: 資本の推移
        regime_results: レジーム別バックテスト結果
        output_dir: 出力ディレクトリ

    Returns:
        生成されたファイルパスの辞書
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    file_paths = {}

    # エクイティカーブ
    equity_path = f"{output_dir}/equity_curve.png"
    plot_equity_curve(equity_curve, save_path=equity_path)
    file_paths['equity_curve'] = equity_path

    # ドローダウン
    drawdown_path = f"{output_dir}/drawdown.png"
    plot_drawdown(equity_curve, save_path=drawdown_path)
    file_paths['drawdown'] = drawdown_path

    # レジーム別パフォーマンス
    if regime_results:
        regime_path = f"{output_dir}/regime_performance.png"
        plot_regime_performance(regime_results, save_path=regime_path)
        file_paths['regime_performance'] = regime_path

    print(f"\n✅ All visualizations saved to {output_dir}")
    return file_paths
