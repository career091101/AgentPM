---
name: trading-agents
description: |
  TradingAgentsシステム全体を自律実行するメインオーケストレーター。
  Phase1→2→3→4を自動実行（2.5-4時間）。日経平均先物の1週間トレード戦略を
  完全自動で策定し、final_strategy_report.mdを生成。

  使用タイミング：
  - 週次トレード戦略立案
  - 日経平均先物の包括的分析が必要な時
  - システム全体を一発実行したい時

  所要時間：2.5-4時間（自動実行）
  出力：final_strategy_report.md

trigger_keywords:
  - "トレード戦略立案"
  - "Trading Agents"
  - "全フェーズ実行"
  - "日経先物戦略"

stage: Full System

dependencies:
  - trading-phase1-analysts
  - trading-phase2-research
  - trading-phase3-risk
  - trading-phase4-execution

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase4/{YYYY-MM-DD}/final_strategy_report.md

execution_time: 2.5-4時間（自動実行）

framework_reference: Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md

priority: P0

framework_compliance: 100%
---

# Trading Agents - Main Orchestrator

TradingAgentsシステム全体を自律実行するメインオーケストレーター。

---

## このSkillでできること

1. **完全自律実行**: Phase1-4を自動実行（Human介入不要）
2. **実データ収集**: WebSearch/WebFetchで市場データ収集
3. **4フェーズ統合**: アナリスト→リサーチ→リスク管理→トレーディング
4. **ステージゲート管理**: 各フェーズ完了確認
5. **最終戦略レポート**: final_strategy_report.md生成

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | なし（自動実行） |
| **出力** | final_strategy_report.md（システム全体の最終成果物） |
| **対象**: | 日経平均先物（日経225） |
| **期間** | 今後1週間（5営業日） |

---

## Instructions

**実行モード**: 自律実行（ステージゲートで停止）
**推定所要時間**: 2.5-4時間

### 全システム実行フロー

#### Phase 1: アナリストチーム（60-90分）

**実行**: `/trading-phase1-analysts`

**成果物**:
- market_analysis.md（テクニカル分析）
- fundamentals_analysis.md（ファンダメンタルズ分析）
- news_analysis.md（ニュース分析）
- sentiment_analysis.md（センチメント分析）
- analysts_summary.md（統合分析）

**ステージゲート1**:
- [ ] 4エージェント全完了
- [ ] コンセンサス判定明確
- [ ] データソースURL 3件以上/エージェント

**通過** → Phase 2へ進む
**未達成** → 停止、改善アクション提示

---

#### Phase 2: リサーチチーム（30-45分）

**実行**: `/trading-phase2-research`

**成果物**:
- bull_scenario.md（強気シナリオ）
- bear_scenario.md（弱気シナリオ）
- research_consensus.md（統合判断）

**ステージゲート2**:
- [ ] 3エージェント全完了
- [ ] 期待リターン計算完了
- [ ] Risk/Reward比率 ≥ 1.0
- [ ] 最終推奨明確

**通過** → Phase 3へ進む
**未達成** → 停止、改善アクション提示

---

#### Phase 3: リスク管理チーム（25-35分）

**実行**: `/trading-phase3-risk`

**成果物**:
- risky_portfolio.md（積極的戦略）
- safe_portfolio.md（保守的戦略）
- neutral_portfolio.md（バランス型戦略）
- risk_management_report.md（統合判断）

**ステージゲート3**:
- [ ] 4エージェント全完了
- [ ] 3ポートフォリオ全VaR計算完了
- [ ] シャープレシオ評価完了
- [ ] 最終推奨ポートフォリオ明確

**通過** → Phase 4へ進む
**未達成** → 停止、改善アクション提示

---

#### Phase 4: トレーディングチーム（20-30分）

**実行**: `/trading-phase4-execution`

**成果物**:
- trading_plan.md（トレード実行計画）
- final_strategy_report.md（システム全体の最終成果物）

**ステージゲート4**:
- [ ] 2エージェント全完了
- [ ] trading_plan.md生成完了
- [ ] final_strategy_report.md生成完了
- [ ] Phase1-4整合性確認

**通過** → システム完了
**未達成** → 停止、改善アクション提示

---

## 最終成果物

### ファイル構造

```
Stock/programs/資産運用/projects/TradingAgents/data/results/
├── phase1/2025-12-29/
│   ├── market_analysis.md
│   ├── fundamentals_analysis.md
│   ├── news_analysis.md
│   ├── sentiment_analysis.md
│   └── analysts_summary.md
├── phase2/2025-12-29/
│   ├── bull_scenario.md
│   ├── bear_scenario.md
│   └── research_consensus.md
├── phase3/2025-12-29/
│   ├── risky_portfolio.md
│   ├── safe_portfolio.md
│   ├── neutral_portfolio.md
│   └── risk_management_report.md
└── phase4/2025-12-29/
    ├── trading_plan.md
    └── final_strategy_report.md ← 最終成果物
```

---

## 総実行時間

| フェーズ | 最短 | 最長 | 平均 |
|---------|------|------|------|
| Phase 1 | 60分 | 90分 | 75分 |
| Phase 2 | 30分 | 45分 | 38分 |
| Phase 3 | 25分 | 35分 | 30分 |
| Phase 4 | 20分 | 30分 | 25分 |
| **合計** | **135分（2.25時間）** | **200分（3.33時間）** | **168分（2.8時間）** |

---

## Knowledge Base参照

- Phase1 Orchestrator: `.claude/skills/trading-phase1-analysts/SKILL.md`
- Phase2 Orchestrator: `.claude/skills/trading-phase2-research/SKILL.md`
- Phase3 Orchestrator: `.claude/skills/trading-phase3-risk/SKILL.md`
- Phase4 Orchestrator: `.claude/skills/trading-phase4-execution/SKILL.md`
- Project Requirements: `@Stock/programs/資産運用/projects/TradingAgents/documents/requirements/project_requirements.md`

---

## 使用例

```
User: /trading-agents

Skill:
# TradingAgents 全自動実行開始

対象: 日経平均先物（日経225）
分析期間: 今後1週間（2025-12-30 ~ 2026-01-10）
推定所要時間: 2.5-4時間

[自動実行中...]

## Phase 1: アナリストチーム ✅ 完了（78分）
- 4エージェント実行完了
- コンセンサス: 強気（+3/4）
- ステージゲート1: ✅ 通過

## Phase 2: リサーチチーム ✅ 完了（50分）
- Bull確率62%、目標+3.8%
- Bear確率38%、目標-2.8%
- 期待リターン: +1.29%
- ステージゲート2: ✅ 通過

## Phase 3: リスク管理チーム ✅ 完了（32分）
- 3ポートフォリオ設計完了
- 最終推奨: Neutral Portfolio
- VaR（95%）: -4.5%
- ステージゲート3: ✅ 通過

## Phase 4: トレーディングチーム ✅ 完了（25分）
- trading_plan.md生成完了
- final_strategy_report.md生成完了
- ステージゲート4: ✅ 通過

## 全システム完了

総実行時間: 185分（3時間5分）
最終推奨: ロング（慎重）
期待リターン: +1.29%
推奨ポートフォリオ: Neutral
VaR（95%）: -4.5%

次のアクション:
1. final_strategy_report.mdレビュー
2. トレード実行準備
3. リスク管理設定

成果物: final_strategy_report.md 生成完了
```
