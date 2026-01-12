# AI Stock Investment Timing System

TradingAgents-mainアーキテクチャをベースにした、AI技術マイルストーンを考慮した株式投資タイミングシステム。

## 概要

46社のAI関連企業を対象に、AI Milestone Proximity Index (AMPI)などのAI特化指標を用いて、週次でポートフォリオ最適化を行うマルチエージェントシステム。

### 主要機能

- **AI Timeline予測**: GPT-5、AGI等のマイルストーンへの近接度を数値化
- **6層マルチエージェント**: Analyst → Researcher → Portfolio Strategist → Risk Team
- **7カテゴリ分析**: Big Tech、半導体GPU、半導体Foundry、データセンター等
- **ChromaDB学習**: 過去の成功/失敗から継続学習
- **既存プロジェクト統合**: Nexus（月次レポート）、SNS（週次投稿）、TradingAgents（コンテキスト提供）

## セットアップ

### 1. 環境構築

```bash
# Python 3.10以上推奨
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存パッケージインストール
pip install -r requirements.txt
```

### 2. APIキー設定

```bash
# .env.exampleをコピー
cp .env.example .env

# .envファイルを編集してAPIキーを設定
nano .env
```

**必須APIキー**:
- `OPENAI_API_KEY`: OpenAI API（LLM + Embeddings）
- `FINNHUB_API_KEY`: FinnHub API（ニュース・センチメント）※既に設定済み
- `SIMFIN_API_KEY`: SimFin API（ファンダメンタル）※既に設定済み

**オプショナルAPIキー**:
- `NEWSAPI_KEY`: NewsAPI（ニュース集約）※既に設定済み
- `REDDIT_CLIENT_ID/SECRET`: Reddit API（SNSセンチメント）※既に設定済み
- `ALPHA_VANTAGE_API_KEY`: Alpha Vantage（テクニカル指標）

### 3. データ準備

```bash
# AI Timelineデータは既に作成済み
cat data/ai_milestones.json

# 企業別関連度スコアの確認・調整
# 必要に応じてdata/ai_milestones.jsonを編集
```

### 4. データ取得テスト（オプショナル）

週次データフェッチャーが正しく動作するか確認：

```python
from dataflows.yfinance_weekly import get_weekly_stock_data
from datetime import datetime, timedelta

# テスト: MSFTの過去4週間データ取得
end_date = datetime.now().strftime("%Y-%m-%d")
start_date = (datetime.now() - timedelta(weeks=4)).strftime("%Y-%m-%d")

data = get_weekly_stock_data("MSFT", start_date, end_date)
print(data)
```

## アーキテクチャ

### 6層構造

```
Layer 0: Portfolio Coordinator
  ├─ 週次スケジューリング（毎週月曜）
  └─ 46社のバッチ処理

Layer I: AI拡張アナリストチーム
  ├─ Market Analyst (週次テクニカル)
  ├─ AI Milestone Analyst (AMPI)
  ├─ Category Momentum Analyst (CMS)
  ├─ News Sentiment Analyst (NSV)
  ├─ Insider Trading Analyst (ITS)
  └─ Fundamentals Analyst

Layer II: Researcher Team
  ├─ Bull ⟷ Bear (2ラウンドDebate)
  └─ Research Manager

Layer III: Portfolio Strategist
  └─ Kelly Criterion + リバランス

Layer IV: Risk Management Team
  ├─ Risky ⟷ Safe ⟷ Neutral
  └─ Risk Manager

Layer V: Integration Manager
  ├─ Nexus月次レポート
  ├─ SNS週次投稿
  └─ TradingAgentsコンテキスト

Layer VI: Final Decision
```

### AI特化指標

1. **AMPI (AI Milestone Proximity Index)**
   - マイルストーンへの近接度（指数減衰、半減期180日）
   - 企業別関連度スコアで重み付け
   - 閾値: ≥80 強気、50-80 中立、<50 低影響

2. **CMS (Category Momentum Score)**
   - 7カテゴリのセクターローテーション検出
   - 価格モメンタム40% + 相対強度30% + 出来高20% + センチメント10%

3. **NSV (News Sentiment Velocity)**
   - センチメント変化速度（加速度）
   - 閾値: >+5 急速改善、<-5 急速悪化

4. **ITS (Insider Trading Signal)**
   - SEC Form 4分析、役職重み付け
   - クラスター検出（3人以上買いで1.3倍ボーナス）

## 使用方法

### 週次分析実行

```bash
# Phase 2実装後に利用可能
python main.py --date 2026-01-06  # Monday
```

### バックテスト

```bash
# Phase 3実装後に利用可能
python backtests/run_backtest.py --start 2023-01-01 --end 2024-12-31
```

### CLIダッシュボード

```bash
# Phase 4実装後に利用可能
python cli/main.py
```

## データソース

| データ種別 | ソース | API | コスト |
|-----------|--------|-----|--------|
| 株価OHLCV | yfinance | - | 無料 |
| ニュース | FinnHub | REST | 無料60calls/min |
| ファンダメンタル | SimFin | REST | 無料2000calls/day |
| インサイダー取引 | SEC EDGAR | HTTPS | 無料（10req/sec） |
| SNSセンチメント | Reddit | PRAW | 無料 |
| マイルストーン | 手動更新 | - | - |

## ディレクトリ構造

```
ai_stock_agents/
├── main.py                     # エントリーポイント
├── default_ai_stock_config.py  # 設定ファイル
├── requirements.txt            # Python依存
├── .env                        # APIキー（Git管理外）
├── .env.example                # APIキーテンプレート
│
├── agents/
│   ├── analysts/               # 6種類のアナリスト
│   ├── researchers/            # Bull/Bear
│   ├── managers/               # Research/Risk Manager
│   ├── portfolio/              # Portfolio Strategist [NEW]
│   ├── integration/            # Nexus/SNS/TradingAgents [NEW]
│   └── utils/
│       ├── agent_states.py     # State定義
│       ├── ai_timeline_tools.py  # AMPI計算
│       ├── category_tools.py     # CMS計算
│       ├── insider_tools.py      # ITS計算
│       └── memory.py             # ChromaDB
│
├── graph/
│   ├── ai_stock_graph.py       # LangGraphオーケストレーター
│   ├── conditional_logic.py    # 条件分岐
│   └── reflection.py           # 学習メカニズム
│
├── dataflows/
│   ├── __init__.py              # モジュール初期化
│   ├── config.py                # 設定管理（get_config, set_config）
│   ├── interface.py             # ベンダールーティング（route_to_vendor）
│   ├── yfinance_weekly.py       # [完了] 週次データ（yfinance）
│   └── sec_edgar.py             # [完了] Form 4取得（SEC EDGAR、無料）
│
├── cli/
│   └── main.py                 # Rich UIダッシュボード
│
└── data/
    └── ai_milestones.json      # AIマイルストーン
```

## 開発ステータス

### ✅ Phase 1-Week 1 完了
- [x] プロジェクト構造作成
- [x] 設定ファイル作成（default_ai_stock_config.py）
- [x] State定義作成（agents/utils/agent_states.py）
- [x] AI Timeline JSONデータ作成（data/ai_milestones.json）
- [x] APIキー管理設定（.env, .env.example）
- [x] 週次データフェッチャー実装（dataflows/yfinance_weekly.py）
- [x] データフロー基盤構築（dataflows/interface.py, config.py）
- [x] SEC EDGAR API統合（dataflows/sec_edgar.py, agents/utils/insider_tools.py）
- [x] ITS (Insider Trading Signal) 計算ツール実装

### ✅ Phase 1-Week 2 完了
- [x] graph/conditional_logic.py作成（6層グラフの条件分岐ロジック）
- [x] ChromaDB初期化（agents/utils/memory.py、6コレクション対応）
- [ ] graph/setup.py作成（グラフセットアップヘルパー）※Phase 2完了後に実装
- [ ] エンドツーエンドコンパイル検証※Phase 2完了後に実装

### ✅ Phase 2-Week 3 完了（コアアナリスト）
- [x] Market Analyst実装（agents/analysts/market_analyst.py）
  - 週次テクニカル指標分析（SMA10/40, RSI週次, MACD週次等）
  - AIマイルストーンコンテキスト統合
- [x] AI Milestone Analyst実装（agents/analysts/ai_milestone_analyst.py）[NEW]
  - AMPI（AI Milestone Proximity Index）計算
  - AIマイルストーンへの近接度分析
  - agents/utils/ai_timeline_tools.py（計算ツール）
- [x] Fundamentals Analyst実装（agents/analysts/fundamentals_analyst.py）
  - AI企業特化のファンダメンタル分析
  - R&D支出、AI売上、GPU投資等の分析
  - dataflows/yfinance_weekly.py::get_fundamentals追加

### ✅ Phase 2-Week 4 完了（新規アナリスト）
- [x] Category Momentum Analyst実装（agents/analysts/category_momentum_analyst.py）
  - 7カテゴリのセクターローテーション分析
  - CMS（Category Momentum Score）計算
  - agents/utils/category_tools.py（計算ツール）
- [x] News Sentiment Analyst実装（agents/analysts/news_sentiment_analyst.py）
  - NSV（News Sentiment Velocity）計算
  - センチメント変化速度の分析
  - agents/utils/news_tools.py（計算ツール）
- [x] Insider Trading Analyst実装（agents/analysts/insider_trading_analyst.py）
  - SEC Form 4分析
  - ITS（Insider Trading Signal）計算
  - 既存ツール利用（agents/utils/insider_tools.py）

### ✅ Phase 2-Week 5 完了（Debate & Portfolio）
- [x] Bull Researcher実装（agents/researchers/bull_researcher.py）
  - 2ラウンドディベート対応
  - ChromaDB RAG統合
  - AI Timeline コンテキスト統合
- [x] Bear Researcher実装（agents/researchers/bear_researcher.py）
  - 2ラウンドディベート対応
  - ChromaDB RAG統合
  - AI競争リスク分析
- [x] Research Manager実装（agents/managers/research_manager.py）
  - deep_thinking_llm (o1-mini) 使用
  - Bull vs Bear 統合評価
  - 銘柄推奨（BUY/HOLD/SELL）
- [x] Portfolio Strategist実装（agents/portfolio/portfolio_strategist.py）[NEW LAYER]
  - 46株全体のポートフォリオ管理
  - Kelly Criterionポジションサイジング
  - カテゴリ配分制約（最大30%/カテゴリ）
  - リバランス判定（週次マイナー、月次フル）
- [x] Risk Team実装（agents/risk_mgmt/）
  - Risky Debator（risky_debator.py）: 積極的AI投資主張
  - Safe Debator（safe_debator.py）: 保守的リスク管理主張
  - Neutral Debator（neutral_debator.py）: バランス型主張
  - Risk Manager（managers/risk_manager.py）: 最終ポートフォリオ決定（deep_thinking_llm）

### 🎉 Phase 2完了！
**全エージェント実装完了（6アナリスト + 2リサーチャー + 2マネージャー + 1ストラテジスト + 3リスクデベーター = 14エージェント）**

### ✅ Phase 3-Week 6 完了（LangGraph統合）
- [x] GraphSetup実装（graph/setup.py）
  - 14エージェント全てをLangGraphに統合
  - Tool-calling ループロジック
  - 条件分岐ロジック（debate、risk analysis）
  - 6層アーキテクチャ実装
- [x] 条件分岐ロジック完成（graph/conditional_logic.py）
  - 6アナリスト用 tool-calling判定
  - Bull vs Bear ディベートロジック（2ラウンド）
  - Risky vs Safe vs Neutral リスクディベートロジック（2ラウンド）
- [x] モジュール構造整備
  - agents/__init__.py（全14エージェントエクスポート）
  - researchers/__init__.py
  - managers/__init__.py
  - portfolio/__init__.py
  - risk_mgmt/__init__.py
  - agents/utils/agent_utils.py（メッセージクリア関数）

### 📋 今後の予定
- Phase 3-Week 7: バックテスト & 学習（Reflection、パフォーマンス検証、AMPI予測力評価）
- Phase 4 (Week 8): 統合 & CLI（Nexus/SNS/TradingAgents統合、ダッシュボード）

## 参考

- TradingAgents-main: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/AI未来予測・戦略策定/projects/AI_Timeline_Forecast/documents/3_planning/TradingAgents-main`
- 実装計画: `/Users/yuichi/.claude/plans/steady-spinning-badger.md`

## ライセンス

TBD
