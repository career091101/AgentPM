# AI Stock Agents - Agents Module Exports

# Analysts (6 types)
from .analysts import (
    create_market_analyst,
    create_ai_milestone_analyst,
    create_fundamentals_analyst,
    create_category_momentum_analyst,
    create_news_sentiment_analyst,
    create_insider_trading_analyst,
)

# Researchers (2 types)
from .researchers.bull_researcher import create_bull_researcher
from .researchers.bear_researcher import create_bear_researcher

# Managers (2 types)
from .managers.research_manager import create_research_manager
from .managers.risk_manager import create_risk_manager

# Portfolio (1 type)
from .portfolio.portfolio_strategist import create_portfolio_strategist

# Risk Management Debators (3 types)
from .risk_mgmt.risky_debator import create_risky_debator
from .risk_mgmt.safe_debator import create_safe_debator
from .risk_mgmt.neutral_debator import create_neutral_debator

__all__ = [
    # Analysts
    "create_market_analyst",
    "create_ai_milestone_analyst",
    "create_fundamentals_analyst",
    "create_category_momentum_analyst",
    "create_news_sentiment_analyst",
    "create_insider_trading_analyst",
    # Researchers
    "create_bull_researcher",
    "create_bear_researcher",
    # Managers
    "create_research_manager",
    "create_risk_manager",
    # Portfolio
    "create_portfolio_strategist",
    # Risk Debators
    "create_risky_debator",
    "create_safe_debator",
    "create_neutral_debator",
]
