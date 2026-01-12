# Trading Agent スキル役割マッピング表

**作成日**: 2025-12-30
**分析者**: Claude Sonnet 4.5
**情報ソース**: Exploreエージェント(afa817e) + SKILL.mdファイル調査

---

## 概要

Trading Agent システムは **24個のスキル**で構成されています：
- **オーケストレーター**: 6個（メイン2個 + フェーズ別4個）
- **エージェント**: 18個（データ収集、分析、戦略、リスク、実行、検証）

---

## 1. オーケストレーター階層

### 1.1 メインオーケストレーター（2個）

| スキル名 | 役割 | 実行時間 | 依存スキル | トリガーワード |
|---------|------|---------|-----------|-------------|
| **trading-agents** | 全フェーズ統合実行 | 2.5-4時間 | phase1-4の4オーケストレーター | "トレード戦略立案", "Trading Agents", "全フェーズ実行" |
| **orchestrate-trading-strategy** | 7ステップ版（スタンドアロン） | 90-120分 | 6エージェント（直接呼び出し） | "トレード戦略", "日経平均先物", "スイング戦略立案" |

#### trading-agents の詳細
- **目的**: Phase1〜4を順次実行する最上位オーケストレーター
- **実行フロー**: Phase1（75分）→ Phase2（38分）→ Phase3（30分）→ Phase4（25分）
- **成果物**: `final_strategy_report.md`（全Phase統合版）
- **ステージゲート**: 各Phaseの終了時に品質チェック

#### orchestrate-trading-strategy の詳細
- **目的**: 単独で完結する7ステップ実行（Phase1〜4を内包しない軽量版）
- **実行フロー**: データ収集（15分）→ 並列分析（30分）→ 統合（20分）→ バックテスト（60分）→ 出力（5分）
- **成果物**: `final_trading_strategy.md`（9項目必須）
- **ステージゲート**: 3箇所（データ完全性95%、分析成功率66%、シャープレシオ1.0）

---

### 1.2 フェーズオーケストレーター（4個）

| スキル名 | 役割 | 実行時間 | 依存スキル（個数） | 成果物 |
|---------|------|---------|------------------|--------|
| **trading-phase1-analysts** | アナリストチーム統括 | 60-90分 | 4エージェント | `analysts_summary.md` |
| **trading-phase2-research** | リサーチチーム統括 | 30-45分 | 3エージェント | `research_consensus.md` |
| **trading-phase3-risk** | リスク管理チーム統括 | 25-35分 | 4エージェント | `risk_management_report.md` |
| **trading-phase4-execution** | トレーディングチーム統括 | 20-30分 | 2エージェント | `final_strategy_report.md` |

#### 各フェーズの詳細

**Phase1: Analysts Team**
- **目的**: 市場全体を4視点で分析
- **依存エージェント**: market-analyst, fundamentals-analyst, news-analyst, sentiment-analyst
- **ステージゲート**: 4エージェント全て完了、コンセンサス明確、3+データソース/エージェント

**Phase2: Research Team**
- **目的**: Bull/Bearシナリオ作成と統合
- **依存エージェント**: bull-researcher, bear-researcher, research-manager
- **ステージゲート**: 3エージェント全て完了、期待リターン計算済み、R:R比率≥1.0

**Phase3: Risk Management Team**
- **目的**: 3種類のポートフォリオ設計
- **依存エージェント**: risky-portfolio, safe-portfolio, neutral-portfolio, risk-manager
- **ステージゲート**: 4エージェント全て完了、VaR計算済み、シャープレシオ評価済み

**Phase4: Trading Team**
- **目的**: 最終戦略レポート作成
- **依存エージェント**: trader, fund-manager
- **ステージゲート**: 2エージェント全て完了、トレード計画生成、Phase整合性確認

---

## 2. エージェント階層（18個）

### 2.1 データ収集（1個）

| スキル名 | 役割 | 実行時間 | データソース | 出力 |
|---------|------|---------|------------|------|
| **agent-data-collector** | 市場データ収集 | 10-15分 | IG証券（現在価格）<br>Yahoo Finance（5年履歴）<br>Investing.com（補完） | `market_data.json`<br>（現在価格+5年OHLCV） |

**詳細機能**:
- データ完全性チェック（95%以上必須）
- 複数ソースからのフォールバック
- 欠損データの補完

---

### 2.2 Phase1分析エージェント（4個）

| スキル名 | 役割 | 実行時間 | 分析対象 | 出力 |
|---------|------|---------|---------|------|
| **agent-market-analyst** | テクニカル分析（基本） | 20-30分 | 8指標（SMA50/200, EMA10, MACD, RSI, Bollinger, VWMA） | `market_analysis.md` |
| **agent-fundamentals-analyst** | マクロ経済分析 | 20-30分 | BOJ/FRB政策、USD/JPY、経済指標 | `fundamentals_analysis.md` |
| **agent-news-analyst** | ニュース収集・分析 | 10-15分 | Google News（日英7日間） | `news_analysis.md` |
| **agent-sentiment-analyst** | 市場心理分析 | 10-15分 | VIX、Fear & Greed Index、Put/Call ratio、SNS | `sentiment_analysis.md` |

**実行方法**: ReAct loop（5-6イテレーション）、WebSearch/WebFetchを活用

---

### 2.3 高度分析エージェント（2個）

| スキル名 | 役割 | 実行時間 | 分析手法 | 出力 |
|---------|------|---------|---------|------|
| **agent-technical-analyst** | 詳細テクニカル分析 | 8-12分 | 8指標の重み付けスコアリング<br>（MA=2.0, MACD=1.8, RSI=1.6等） | `technical_analysis.md` |
| **agent-elliott-wave-analyst** | エリオット波動分析 | 15-20分 | 波動カウント（Primary/Intermediate/Minor）<br>フィボナッチ目標価格 | `elliott_wave_analysis.md` |

**agent-technical-analyst の詳細**:
- 指標: MA, MACD, RSI, Bollinger Bands, ATR, Volume, VWMA, Stochastic
- 重み付け統合でトレンド判定
- エントリー/エグジット/ストップロス価格提案

**agent-elliott-wave-analyst の詳細**:
- メイン/サブシナリオの提示
- フィボナッチリトレースメント（23.6%, 38.2%, 50%, 61.8%）

---

### 2.4 Phase2戦略エージェント（3個）

| スキル名 | 役割 | 実行時間 | 出力 | 特徴 |
|---------|------|---------|------|------|
| **agent-bull-researcher** | 強気シナリオ構築 | 10-15分 | `bull_scenario.md` | 上昇トレンド要因の分析 |
| **agent-bear-researcher** | 弱気シナリオ構築 | 10-15分 | `bear_scenario.md` | 下降トレンド要因の分析 |
| **agent-research-manager** | シナリオ統合・判断 | 10-15分 | `research_consensus.md` | Bull/Bearの確率評価、期待リターン計算 |

---

### 2.5 Phase3リスク管理エージェント（4個）

| スキル名 | 役割 | 実行時間 | 出力 | リスク許容度 |
|---------|------|---------|------|-----------|
| **agent-risky-portfolio** | 積極的戦略 | 6-9分 | `risky_portfolio.md` | 高（レバレッジ活用） |
| **agent-safe-portfolio** | 保守的戦略 | 6-9分 | `safe_portfolio.md` | 低（ストップロス厳格） |
| **agent-neutral-portfolio** | バランス型戦略 | 6-9分 | `neutral_portfolio.md` | 中（標準リスク） |
| **agent-risk-manager** | リスク管理統合 | 7-8分 | `risk_management_report.md` | VaR、シャープレシオ評価 |

---

### 2.6 Phase4実行エージェント（2個）

| スキル名 | 役割 | 実行時間 | 出力 | 責務 |
|---------|------|---------|------|------|
| **agent-fund-manager** | 資金管理 | 5-10分 | （システム統合） | ポジションサイズ決定、資金配分 |
| **agent-trader** | トレード実行計画 | 15-20分 | `trading_plan.md` | 具体的な執行タイミング、価格レンジ |

---

### 2.7 検証エージェント（2個）

| スキル名 | 役割 | 実行時間 | 検証内容 | 出力 |
|---------|------|---------|---------|------|
| **agent-strategy-synthesizer** | 戦略統合 | 20分 | 3エージェント（technical/elliott/sentiment）の重み付け投票<br>重み: Technical 2.0, Elliott 1.8, Sentiment 1.2 | `synthesized_strategy.md` |
| **agent-backtest-validator** | バックテスト検証 | 60分 | 3-5年データでバックテスト<br>バイアス防止（look-ahead/survivorship/overfitting）<br>ウォークフォワード分析 | `backtest_validation_report.md` |

**agent-backtest-validator の詳細**:
- **合格基準**: シャープレシオ≥1.0 AND WF効率≥50%
- **データ分割**: Train 60% / Validate 20% / Test 20%
- **マーケットレジーム別評価**: 全レジームでシャープレシオ>0.3

---

## 3. 依存関係マップ

### 3.1 trading-agents の依存ツリー

```
trading-agents (Main Orchestrator)
  ├─ trading-phase1-analysts (60-90分)
  │   ├─ agent-market-analyst (20-30分)
  │   ├─ agent-fundamentals-analyst (20-30分)
  │   ├─ agent-news-analyst (10-15分)
  │   └─ agent-sentiment-analyst (10-15分)
  │
  ├─ trading-phase2-research (30-45分)
  │   ├─ agent-bull-researcher (10-15分)
  │   ├─ agent-bear-researcher (10-15分)
  │   └─ agent-research-manager (10-15分)
  │
  ├─ trading-phase3-risk (25-35分)
  │   ├─ agent-risky-portfolio (6-9分)
  │   ├─ agent-safe-portfolio (6-9分)
  │   ├─ agent-neutral-portfolio (6-9分)
  │   └─ agent-risk-manager (7-8分)
  │
  └─ trading-phase4-execution (20-30分)
      ├─ agent-fund-manager (5-10分)
      └─ agent-trader (15-20分)
```

**総実行時間**: 135-200分（2.25-3.33時間）

---

### 3.2 orchestrate-trading-strategy の依存ツリー

```
orchestrate-trading-strategy (Standalone Orchestrator)
  ├─ STEP 1: agent-data-collector (15分)
  │
  ├─ STEP 2-4: 並列実行（30分）
  │   ├─ agent-technical-analyst (8-12分)
  │   ├─ agent-elliott-wave-analyst (15-20分)
  │   └─ agent-sentiment-analyst (10-15分)
  │
  ├─ STEP 5: agent-strategy-synthesizer (20分)
  │
  └─ STEP 6: agent-backtest-validator (60分)
```

**総実行時間**: 90-120分（1.5-2時間）

---

## 4. 実装状況

### 4.1 オーケストレーター（6個）

| スキル名 | SKILL.md | フォルダ存在 | Pythonコード | 動作確認 | 備考 |
|---------|---------|-----------|------------|---------|------|
| **trading-agents** | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 | SKILL.mdは完備 |
| **orchestrate-trading-strategy** | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 失敗 | T002-1でUnknown skillエラー |
| **trading-phase1-analysts** | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 | - |
| **trading-phase2-research** | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 | - |
| **trading-phase3-risk** | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 | - |
| **trading-phase4-execution** | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 | - |

**実装率**: SKILL.md 6/6 (100%), Pythonコード 0/6 (0%), 動作確認 0/6 (0%)

---

### 4.2 エージェント（18個）

#### データ収集 (1/1)

| スキル名 | SKILL.md | フォルダ存在 | Pythonコード | 動作確認 |
|---------|---------|-----------|------------|---------|
| agent-data-collector | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |

#### Phase1分析 (4/4)

| スキル名 | SKILL.md | フォルダ存在 | Pythonコード | 動作確認 |
|---------|---------|-----------|------------|---------|
| agent-market-analyst | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |
| agent-fundamentals-analyst | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |
| agent-news-analyst | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |
| agent-sentiment-analyst | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |

#### 高度分析 (2/2)

| スキル名 | SKILL.md | フォルダ存在 | Pythonコード | 動作確認 |
|---------|---------|-----------|------------|---------|
| agent-technical-analyst | ⚠️ 推定存在 | ✅ 存在（推定） | ❌ 未実装 | ❌ 未確認 |
| agent-elliott-wave-analyst | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |

#### Phase2戦略 (3/3)

| スキル名 | SKILL.md | フォルダ存在 | Pythonコード | 動作確認 |
|---------|---------|-----------|------------|---------|
| agent-bull-researcher | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |
| agent-bear-researcher | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |
| agent-research-manager | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |

#### Phase3リスク (4/4)

| スキル名 | SKILL.md | フォルダ存在 | Pythonコード | 動作確認 |
|---------|---------|-----------|------------|---------|
| agent-risky-portfolio | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |
| agent-safe-portfolio | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |
| agent-neutral-portfolio | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |
| agent-risk-manager | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |

#### Phase4実行 (2/2)

| スキル名 | SKILL.md | フォルダ存在 | Pythonコード | 動作確認 |
|---------|---------|-----------|------------|---------|
| agent-fund-manager | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |
| agent-trader | ⚠️ 推定存在 | ✅ 存在（推定） | ❌ 未実装 | ❌ 未確認 |

#### 検証 (2/2)

| スキル名 | SKILL.md | フォルダ存在 | Pythonコード | 動作確認 |
|---------|---------|-----------|------------|---------|
| agent-strategy-synthesizer | ⚠️ 推定存在 | ✅ 存在（推定） | ❌ 未実装 | ❌ 未確認 |
| agent-backtest-validator | ✅ 存在 | ✅ 存在 | ❌ 未実装 | ❌ 未確認 |

**実装率**: SKILL.md 15/18 (83%), フォルダ 18/18 (100%), Pythonコード 0/18 (0%), 動作確認 0/18 (0%)

---

### 4.3 総合実装状況

| カテゴリ | SKILL.md | フォルダ | Pythonコード | 動作確認 |
|---------|---------|---------|------------|---------|
| **オーケストレーター** | 6/6 (100%) | 6/6 (100%) | 0/6 (0%) | 0/6 (0%) |
| **エージェント** | 15/18 (83%) | 18/18 (100%) | 0/18 (0%) | 0/18 (0%) |
| **合計** | **21/24 (88%)** | **24/24 (100%)** | **0/24 (0%)** | **0/24 (0%)** |

**主要な発見**:
- **SKILL.md**: 88%が存在（3個のみ推定）
- **フォルダ構造**: 100%完備
- **Pythonコード**: **0%実装（全くなし）**
- **動作確認**: 0%（スキル登録問題により全て未確認）

---

## 5. スキルトリガーワードマップ

| スキル名 | トリガーワード（一部） |
|---------|-------------------|
| trading-agents | "トレード戦略立案", "Trading Agents", "全フェーズ実行", "日経先物戦略" |
| orchestrate-trading-strategy | "トレード戦略", "日経平均先物", "スイング戦略立案", "日経225戦略" |
| trading-phase1-analysts | "アナリスト", "Phase1" |
| trading-phase2-research | "リサーチ", "Phase2" |
| trading-phase3-risk | "リスク管理", "Phase3" |
| trading-phase4-execution | "トレーディング", "Phase4" |
| agent-data-collector | "データ収集" |
| agent-market-analyst | "マーケット分析" |
| ... | ... |

**注**: 全てのスキルは現在Skillツールに登録されていないため、トリガーワードが機能していない

---

## 6. 実装優先順位（スキル別）

### 最優先（Phase1動作に必須）

1. **orchestrate-trading-strategy** - スタンドアロンで完結するため最優先
2. **agent-data-collector** - 全ての基盤
3. **agent-technical-analyst** - 基本分析
4. **agent-strategy-synthesizer** - 統合機能
5. **agent-backtest-validator** - 検証機能

### 高優先（Phase1完全動作）

6. agent-elliott-wave-analyst
7. agent-sentiment-analyst

### 中優先（全Phaseオーケストレーター）

8. trading-agents
9. trading-phase1-analysts
10. trading-phase2-research
11. trading-phase3-risk
12. trading-phase4-execution

### 低優先（Phase2-4エージェント）

13-24. 残りの12エージェント

---

## 参照資料

- **Exploreエージェントレポート**: Agent ID afa817e
- **SKILL.mdファイル**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/*/SKILL.md`
- **プロジェクト構造**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/資産運用/projects/TradingAgents/`

---

**レポート作成日**: 2025-12-30
**作成者**: Claude Sonnet 4.5
**ステータス**: 完了
