---
name: trading-phase4-execution
description: |
  Phase4トレーディングチーム全体を自律実行するオーケストレータースキル。
  Trader→Fund Managerの2ステップを順次実行（20-30分）。
  トレード実行計画作成→最終承認→final_strategy_report.md生成。
  システム全体の最終成果物を出力。

  使用タイミング：
  - Phase3完了後、トレード実行フェーズを開始する時
  - Phase4を一気通貫で実行したい

  所要時間：20-30分（自動実行）
  出力：final_strategy_report.md

trigger_keywords:
  - "Phase4実行"
  - "トレード実行"
  - "最終レポート作成"

stage: Phase4 - Trading Team

dependencies:
  - agent-trader
  - agent-fund-manager

input_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/risk_management_report.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase4/{YYYY-MM-DD}/final_strategy_report.md

execution_time: 20-30分（自動実行）

priority: P0
---

# Trading Phase4 Execution Orchestrator Skill

Phase4トレーディングチーム全体を自律実行するオーケストレーターSkill。

---

## Instructions

**実行モード**: 自律実行（ステージゲートで停止）
**推定所要時間**: 20-30分

### Phase4実行ステップ（全2エージェント）

#### エージェント1: Trader（トレード実行計画）

**実行**: `/agent-trader`
**推定時間**: 10-15分
**期待成果物**: `trading_plan.md`

#### エージェント2: Fund Manager（最終承認・レポート生成）

**実行**: `/agent-fund-manager`
**推定時間**: 10-15分
**期待成果物**: `final_strategy_report.md`（システム全体の最終成果物）

### ステージゲート判定

**ステージゲート4: Phase4完了確認**

- **合格条件**:
  1. 2エージェント全実行完了
  2. trading_plan.md生成完了
  3. final_strategy_report.md生成完了
  4. Phase1-4全フェーズ整合性確認

---

## 成果物

```
TradingAgents/data/results/phase4/2025-12-29/
├── trading_plan.md
└── final_strategy_report.md ← システム全体の最終成果物
```
