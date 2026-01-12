---
name: trading-phase3-risk
description: |
  Phase3リスク管理チーム全体を自律実行するオーケストレータースキル。
  Risky/Safe/Neutral 3ポートフォリオ設計→Risk Manager統合判断の4ステップを順次実行（25-35分）。
  VaR計算、シャープレシオ評価で最終推奨ポートフォリオを決定。
  Phase4トレーディングチームへの引き継ぎ事項を明確化。

  使用タイミング：
  - Phase2完了後、リスク管理フェーズを開始する時
  - Phase3を一気通貫で実行したい

  所要時間：25-35分（自動実行）
  出力：risk_management_report.md

trigger_keywords:
  - "Phase3実行"
  - "リスク管理開始"
  - "ポートフォリオ設計"

stage: Phase3 - Risk Management Team

dependencies:
  - agent-risky-portfolio
  - agent-safe-portfolio
  - agent-neutral-portfolio
  - agent-risk-manager

input_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/research_consensus.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/risk_management_report.md

execution_time: 25-35分（自動実行）

priority: P1
---

# Trading Phase3 Risk Management Orchestrator Skill

Phase3リスク管理チーム全体を自律実行するオーケストレーターSkill。

---

## Instructions

**実行モード**: 自律実行（ステージゲートで停止）
**推定所要時間**: 25-35分

### Phase3実行ステップ（全4エージェント）

#### エージェント1: Risky Portfolio（積極的戦略）

**実行**: `/agent-risky-portfolio`
**推定時間**: 5-10分
**期待成果物**: `risky_portfolio.md`

#### エージェント2: Safe Portfolio（保守的戦略）

**実行**: `/agent-safe-portfolio`
**推定時間**: 5-10分
**期待成果物**: `safe_portfolio.md`

#### エージェント3: Neutral Portfolio（バランス型戦略）

**実行**: `/agent-neutral-portfolio`
**推定時間**: 5-10分
**期待成果物**: `neutral_portfolio.md`

#### エージェント4: Risk Manager（統合判断）

**実行**: `/agent-risk-manager`
**推定時間**: 10-15分
**期待成果物**: `risk_management_report.md`

### ステージゲート判定

**ステージゲート3: Phase3完了確認**

- **合格条件**:
  1. 4エージェント全実行完了
  2. 3ポートフォリオ全てVaR計算完了
  3. シャープレシオ評価完了
  4. 最終推奨ポートフォリオ明確

---

## 成果物

```
TradingAgents/data/results/phase3/2025-12-29/
├── risky_portfolio.md
├── safe_portfolio.md
├── neutral_portfolio.md
└── risk_management_report.md ← 最終成果物
```
