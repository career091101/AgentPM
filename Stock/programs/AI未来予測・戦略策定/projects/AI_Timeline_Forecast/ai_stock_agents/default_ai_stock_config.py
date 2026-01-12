# AI Stock Investment Timing System Configuration
# Based on TradingAgents-main architecture

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AI_STOCK_CONFIG = {
    # API Keys (loaded from environment variables)
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "finnhub_api_key": os.getenv("FINNHUB_API_KEY"),
    "reddit_client_id": os.getenv("REDDIT_CLIENT_ID"),
    "reddit_client_secret": os.getenv("REDDIT_CLIENT_SECRET"),
    "reddit_user_agent": os.getenv("REDDIT_USER_AGENT"),
    "simfin_api_key": os.getenv("SIMFIN_API_KEY"),
    "newsapi_key": os.getenv("NEWSAPI_KEY"),
    "alpha_vantage_api_key": os.getenv("ALPHA_VANTAGE_API_KEY"),
    "sec_user_agent": os.getenv("SEC_USER_AGENT", "AI Stock Agents/1.0"),

    # LLM設定
    "llm_provider": "openai",
    "deep_think_llm": "o1-mini",          # Managers用（深い推論）
    "quick_think_llm": "gpt-4o-mini",     # Analysts用（高速推論）
    "backend_url": "https://api.openai.com/v1",

    # ワークフロー設定
    "analysis_frequency": "weekly",
    "analysis_day": "Monday",             # 毎週月曜日に実行
    "portfolio_size": 46,
    "batch_size": 10,                     # 並列処理する銘柄数

    # Debate設定（Nikkei先物版より増加）
    "max_debate_rounds": 2,               # vs 1 (Nikkei)
    "max_risk_discuss_rounds": 2,         # vs 1 (Nikkei)

    # ポートフォリオ制約
    "max_position_size": 0.10,            # 10%/銘柄
    "max_category_size": 0.30,            # 30%/カテゴリ
    "rebalance_threshold": 0.05,          # 5%ドリフトでリバランス

    # AI Timeline設定
    "ai_timeline_file": "./data/ai_milestones.json",
    "ampi_half_life_days": 180,           # 6ヶ月半減期

    # カテゴリ定義（7カテゴリ）
    "categories": {
        "Big_Tech": ["MSFT", "GOOGL", "META", "AMZN", "AAPL"],
        "Semiconductors_GPU": ["NVDA", "AMD", "INTC"],
        "Semiconductors_Foundry": ["TSM", "MU", "SSNLF"],
        "Data_Centers": ["EQIX", "DLR", "SMCI"],
        "AI_Applications": ["PLTR"],
        "Cloud": [],                      # 間接保有（Big Tech経由）
        "AI_Research": []                 # 間接保有（MSFT/GOOGL経由）
    },

    # データベンダー設定
    "data_vendors": {
        "core_stock_apis": "yfinance",     # 価格データ: yfinance (無料)
        "technical_indicators": "yfinance", # テクニカル指標: yfinance
        "fundamental_data": "simfin",      # ファンダメンタル: SimFin API
        "news_data": "finnhub",            # ニュース: FinnHub API
        "sentiment_data": "reddit",        # センチメント: Reddit API
        "insider_data": "sec_edgar",       # インサイダー取引: SEC EDGAR (無料)
        "ai_timeline_data": "local"        # AIマイルストーン: 手動更新
    },

    # データベンダー別設定
    "vendor_configs": {
        "finnhub": {
            "base_url": "https://finnhub.io/api/v1",
            "rate_limit": 60,  # calls/minute (free tier)
        },
        "simfin": {
            "base_url": "https://simfin.com/api/v2",
            "rate_limit": 2000,  # calls/day (free tier)
        },
        "newsapi": {
            "base_url": "https://newsapi.org/v2",
            "rate_limit": 100,  # requests/day (free tier)
        },
        "sec_edgar": {
            "base_url": "https://www.sec.gov/cgi-bin/browse-edgar",
            "rate_limit": 10,  # requests/second (SEC guideline)
        }
    },

    # 統合パス設定
    "nexus_output_dir": "../../../副業/projects/Nexus/content/ai_stocks",
    "sns_output_dir": "../../../副業/projects/SNS/content/ai_stocks",
    "tradingagents_context_file": "../../../資産運用/context/ai_stock_context.json",

    # メモリ設定（ChromaDB）
    "memory_collections": [
        "bull_memory",
        "bear_memory",
        "trader_memory",
        "invest_judge_memory",
        "risk_manager_memory",
        "portfolio_strategist_memory"
    ]
}
