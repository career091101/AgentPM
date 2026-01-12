# AI Stock Agent State Definitions
# Based on TradingAgents-main/tradingagents/agents/utils/agent_states.py

from typing import TypedDict, List, Dict, Any
from langgraph.graph import MessagesState


class InvestDebateState(TypedDict):
    """投資議論状態（Bull vs Bear）"""
    bull_history: str              # 強気アナリストの会話履歴
    bear_history: str              # 弱気アナリストの会話履歴
    history: str                   # 全体会話履歴
    current_response: str          # 最新応答
    judge_decision: str            # 判定者の決定
    count: int                     # 会話ラウンド数


class RiskDebateState(TypedDict):
    """リスク議論状態（Risky vs Safe vs Neutral）"""
    risky_history: str             # 積極的アナリスト履歴
    safe_history: str              # 保守的アナリスト履歴
    neutral_history: str           # 中立アナリスト履歴
    history: str                   # 全体会話履歴
    latest_speaker: str            # 最後の発言者
    current_risky_response: str    # 積極的アナリスト最新応答
    current_safe_response: str     # 保守的アナリスト最新応答
    current_neutral_response: str  # 中立アナリスト最新応答
    judge_decision: str            # 判定者の決定
    count: int                     # 会話ラウンド数


class PortfolioState(TypedDict):
    """ポートフォリオ状態"""
    total_value: float
    cash_ratio: float
    positions: Dict[str, Dict]            # {ticker: {size, entry_price, current_price, unrealized_pnl, ...}}
    category_allocations: Dict[str, float]  # {category: allocation_ratio}
    last_rebalance_date: str


class AIStockAgentState(MessagesState):
    """AI株式投資エージェント状態（メイン）"""

    # ポートフォリオコンテキスト
    analysis_date: str                    # 週次: Monday YYYY-MM-DD
    portfolio_tickers: List[str]          # 全46社
    current_ticker: str                   # 処理中銘柄
    category: str                         # Big_Tech, Semiconductors_GPU等
    company_of_interest: str              # TradingAgents互換のため

    # AI Timeline [NEW]
    ai_timeline_data: Dict[str, Any]      # マイルストーンデータ全体
    next_milestone: str                   # "GPT-5 Mar 2026"
    days_to_milestone: int                # 次のマイルストーンまでの日数

    # Analyst reports（銘柄ごと）
    market_report: str                    # Market Analystレポート
    ai_milestone_report: str              # [NEW] AI Milestone Analyst（AMPI）
    category_report: str                  # [NEW] Category Momentum Analyst（CMS）
    news_sentiment_report: str            # News Sentiment Analyst（NSV）
    insider_trading_report: str           # [NEW] Insider Trading Analyst（ITS）
    fundamentals_report: str              # Fundamentals Analyst

    # Research debate（銘柄ごと）
    investment_debate_state: InvestDebateState
    stock_recommendation: str             # BUY/SELL/HOLD

    # Portfolio-level [NEW]
    portfolio_state: PortfolioState
    position_sizing: Dict[str, float]     # {ticker: size_ratio}
    rebalancing_actions: List[Dict]       # [{ticker, action, size, reason}, ...]

    # Risk management
    risk_debate_state: RiskDebateState
    final_portfolio_decision: Dict[str, Any]  # {ticker: {action, size, reason}, ...}

    # Integration outputs [NEW]
    nexus_content: str                    # Nexus月次レポート
    sns_posts: List[str]                  # SNS週次投稿（4種類）
    tradingagents_context: str            # TradingAgentsコンテキストJSON

    # Sender tracking (TradingAgents互換)
    sender: str                           # メッセージ送信者
