"""
パフォーマンスメトリクス計算

シャープレシオ、ソルティノレシオ、カルマーレシオ、
最大ドローダウン等の標準的な評価指標を計算。
"""

from dataclasses import dataclass
from typing import List, Dict, Any
import pandas as pd
import numpy as np


@dataclass
class BacktestMetrics:
    """バックテスト評価指標"""

    # リターン系
    total_return: float  # 累積リターン
    annualized_return: float  # 年率リターン
    monthly_returns: List[float]  # 月次リターン

    # リスク系
    annualized_volatility: float  # 年率ボラティリティ
    max_drawdown: float  # 最大ドローダウン
    max_drawdown_duration: int  # 最大ドローダウン期間（日数）

    # リスク調整済みリターン
    sharpe_ratio: float  # シャープレシオ
    sortino_ratio: float  # ソルティノレシオ
    calmar_ratio: float  # カルマーレシオ

    # 勝率・プロフィットファクター
    win_rate: float  # 勝率（週次リターン > 0の割合）
    profit_factor: float  # プロフィットファクター（総利益/総損失）

    # ベンチマーク比較
    benchmark_return: float  # ベンチマーク（S&P500）リターン
    alpha: float  # アルファ（超過リターン）
    beta: float  # ベータ（市場感応度）
    information_ratio: float  # 情報レシオ

    # コスト影響
    gross_return: float  # コスト前リターン
    net_return: float  # コスト後リターン
    total_trading_cost: float  # 総取引コスト

    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換"""
        return {
            "returns": {
                "total_return": f"{self.total_return:.2%}",
                "annualized_return": f"{self.annualized_return:.2%}",
                "gross_return": f"{self.gross_return:.2%}",
                "net_return": f"{self.net_return:.2%}",
            },
            "risk": {
                "annualized_volatility": f"{self.annualized_volatility:.2%}",
                "max_drawdown": f"{self.max_drawdown:.2%}",
                "max_drawdown_duration": f"{self.max_drawdown_duration} days",
            },
            "risk_adjusted": {
                "sharpe_ratio": f"{self.sharpe_ratio:.2f}",
                "sortino_ratio": f"{self.sortino_ratio:.2f}",
                "calmar_ratio": f"{self.calmar_ratio:.2f}",
            },
            "trading": {
                "win_rate": f"{self.win_rate:.2%}",
                "profit_factor": f"{self.profit_factor:.2f}",
            },
            "benchmark_comparison": {
                "benchmark_return": f"{self.benchmark_return:.2%}",
                "alpha": f"{self.alpha:.2%}",
                "beta": f"{self.beta:.2f}",
                "information_ratio": f"{self.information_ratio:.2f}",
            },
            "costs": {
                "total_trading_cost": f"${self.total_trading_cost:,.2f}",
                "cost_drag": f"{(self.gross_return - self.net_return):.2%}",
            },
        }


def calculate_performance_metrics(
    returns: pd.DataFrame,  # date, return
    benchmark_returns: pd.DataFrame,  # date, return
    trading_costs: List[float],
    initial_capital: float = 1000000,
    risk_free_rate: float = 0.04,
) -> BacktestMetrics:
    """
    総合的なパフォーマンスメトリクス計算

    Args:
        returns: ポートフォリオリターン（DataFrame: date, return）
        benchmark_returns: ベンチマークリターン（DataFrame: date, return）
        trading_costs: 各期間の取引コスト（ドル）
        initial_capital: 初期資本
        risk_free_rate: 無リスク金利（年率）

    Returns:
        BacktestMetrics
    """
    returns = returns.copy()
    returns.set_index("date", inplace=True)
    returns.sort_index(inplace=True)

    benchmark_returns = benchmark_returns.copy()
    benchmark_returns.set_index("date", inplace=True)
    benchmark_returns.sort_index(inplace=True)

    returns_arr = returns["return"].values
    benchmark_arr = benchmark_returns["return"].values

    # 総リターン
    total_return = np.prod(1 + returns_arr) - 1
    gross_return = total_return  # コスト前

    # コスト後リターン
    total_trading_cost = sum(trading_costs)
    cost_impact = total_trading_cost / initial_capital
    net_return = total_return - cost_impact

    # 年率リターン（週次データ想定）
    weeks = len(returns_arr)
    years = weeks / 52.0
    if years > 0:
        annualized_return = (1 + net_return) ** (1 / years) - 1
    else:
        annualized_return = 0.0

    # 年率ボラティリティ
    annualized_volatility = np.std(returns_arr) * np.sqrt(52)

    # シャープレシオ
    sharpe_ratio = calculate_sharpe_ratio(returns_arr, risk_free_rate)

    # ソルティノレシオ
    sortino_ratio = calculate_sortino_ratio(returns_arr, risk_free_rate)

    # 最大ドローダウン
    max_dd, max_dd_duration = calculate_max_drawdown(returns_arr)

    # カルマーレシオ
    calmar_ratio = calculate_calmar_ratio(annualized_return, max_dd)

    # 勝率
    win_rate = calculate_win_rate(returns_arr)

    # プロフィットファクター
    profit_factor = calculate_profit_factor(returns_arr)

    # ベンチマーク比較
    benchmark_total_return = np.prod(1 + benchmark_arr) - 1
    if years > 0:
        benchmark_annualized_return = (1 + benchmark_total_return) ** (1 / years) - 1
    else:
        benchmark_annualized_return = 0.0

    # アルファ・ベータ
    alpha, beta = calculate_alpha_beta(returns_arr, benchmark_arr, risk_free_rate)

    # 情報レシオ
    information_ratio = calculate_information_ratio(returns_arr, benchmark_arr)

    # 月次リターン
    returns_monthly = resample_to_monthly(returns)

    return BacktestMetrics(
        total_return=total_return,
        annualized_return=annualized_return,
        monthly_returns=returns_monthly,
        annualized_volatility=annualized_volatility,
        max_drawdown=max_dd,
        max_drawdown_duration=max_dd_duration,
        sharpe_ratio=sharpe_ratio,
        sortino_ratio=sortino_ratio,
        calmar_ratio=calmar_ratio,
        win_rate=win_rate,
        profit_factor=profit_factor,
        benchmark_return=benchmark_total_return,
        alpha=alpha,
        beta=beta,
        information_ratio=information_ratio,
        gross_return=gross_return,
        net_return=net_return,
        total_trading_cost=total_trading_cost,
    )


def calculate_sharpe_ratio(returns: np.ndarray, risk_free_rate: float = 0.04) -> float:
    """
    シャープレシオ計算

    Args:
        returns: リターン配列（週次想定）
        risk_free_rate: 無リスク金利（年率）

    Returns:
        シャープレシオ
    """
    mean_return = np.mean(returns)
    std_return = np.std(returns)

    # 年率化
    annualized_return = mean_return * 52
    annualized_vol = std_return * np.sqrt(52)

    if annualized_vol > 0:
        return (annualized_return - risk_free_rate) / annualized_vol
    else:
        return 0.0


def calculate_sortino_ratio(returns: np.ndarray, risk_free_rate: float = 0.04) -> float:
    """
    ソルティノレシオ計算（下方リスクのみ考慮）

    Args:
        returns: リターン配列
        risk_free_rate: 無リスク金利（年率）

    Returns:
        ソルティノレシオ
    """
    mean_return = np.mean(returns)
    annualized_return = mean_return * 52

    # 下方偏差（負のリターンのみ）
    downside_returns = returns[returns < 0]
    if len(downside_returns) > 0:
        downside_std = np.std(downside_returns)
        downside_vol = downside_std * np.sqrt(52)
    else:
        downside_vol = 0.0

    if downside_vol > 0:
        return (annualized_return - risk_free_rate) / downside_vol
    else:
        return 0.0


def calculate_calmar_ratio(annualized_return: float, max_drawdown: float) -> float:
    """
    カルマーレシオ計算

    Args:
        annualized_return: 年率リターン
        max_drawdown: 最大ドローダウン

    Returns:
        カルマーレシオ
    """
    if abs(max_drawdown) > 0:
        return annualized_return / abs(max_drawdown)
    else:
        return 0.0


def calculate_max_drawdown(returns: np.ndarray) -> tuple:
    """
    最大ドローダウンと期間計算

    Args:
        returns: リターン配列

    Returns:
        (最大ドローダウン, 最大ドローダウン期間)
    """
    cumulative = np.cumprod(1 + returns)
    cummax = np.maximum.accumulate(cumulative)
    drawdown = (cumulative / cummax) - 1

    max_dd = np.min(drawdown)

    # ドローダウン期間計算
    dd_duration = 0
    current_duration = 0
    for dd in drawdown:
        if dd < 0:
            current_duration += 1
            dd_duration = max(dd_duration, current_duration)
        else:
            current_duration = 0

    return max_dd, dd_duration


def calculate_win_rate(returns: np.ndarray) -> float:
    """
    勝率計算

    Args:
        returns: リターン配列

    Returns:
        勝率（0.0 ~ 1.0）
    """
    if len(returns) == 0:
        return 0.0

    wins = np.sum(returns > 0)
    return wins / len(returns)


def calculate_profit_factor(returns: np.ndarray) -> float:
    """
    プロフィットファクター計算

    Args:
        returns: リターン配列

    Returns:
        プロフィットファクター（総利益 / 総損失）
    """
    gains = returns[returns > 0]
    losses = returns[returns < 0]

    total_gain = np.sum(gains) if len(gains) > 0 else 0.0
    total_loss = abs(np.sum(losses)) if len(losses) > 0 else 0.0

    if total_loss > 0:
        return total_gain / total_loss
    else:
        return 0.0


def calculate_alpha_beta(
    returns: np.ndarray,
    benchmark_returns: np.ndarray,
    risk_free_rate: float = 0.04,
) -> tuple:
    """
    アルファ・ベータ計算（CAPM）

    Args:
        returns: ポートフォリオリターン
        benchmark_returns: ベンチマークリターン
        risk_free_rate: 無リスク金利（年率）

    Returns:
        (alpha, beta)
    """
    # 超過リターン
    excess_returns = returns - (risk_free_rate / 52)
    excess_benchmark = benchmark_returns - (risk_free_rate / 52)

    # ベータ計算（共分散 / 分散）
    covariance = np.cov(excess_returns, excess_benchmark)[0, 1]
    benchmark_variance = np.var(excess_benchmark)

    if benchmark_variance > 0:
        beta = covariance / benchmark_variance
    else:
        beta = 0.0

    # アルファ計算（年率化）
    mean_excess_return = np.mean(excess_returns) * 52
    mean_excess_benchmark = np.mean(excess_benchmark) * 52
    alpha = mean_excess_return - (beta * mean_excess_benchmark)

    return alpha, beta


def calculate_information_ratio(
    returns: np.ndarray,
    benchmark_returns: np.ndarray,
) -> float:
    """
    情報レシオ計算

    Args:
        returns: ポートフォリオリターン
        benchmark_returns: ベンチマークリターン

    Returns:
        情報レシオ
    """
    # アクティブリターン
    active_returns = returns - benchmark_returns

    # トラッキングエラー（年率化）
    tracking_error = np.std(active_returns) * np.sqrt(52)

    # 平均アクティブリターン（年率化）
    mean_active_return = np.mean(active_returns) * 52

    if tracking_error > 0:
        return mean_active_return / tracking_error
    else:
        return 0.0


def resample_to_monthly(returns: pd.DataFrame) -> List[float]:
    """
    週次リターンを月次リターンに変換

    Args:
        returns: DataFrame（date index, return column）

    Returns:
        月次リターンのリスト
    """
    # 月末でリサンプル
    monthly = returns.resample("M").apply(lambda x: np.prod(1 + x) - 1)
    return monthly["return"].tolist()
