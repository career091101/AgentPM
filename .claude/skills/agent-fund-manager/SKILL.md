---
name: agent-fund-manager
description: |
  全フェーズ（Phase1-4）の結果を統合し、最終戦略レポートを作成する自律型エージェント。
  Phase1-4の全分析結果をレビューし、最終承認・ポートフォリオ最適化を実施。
  final_strategy_report.md（システム全体の最終成果物）を生成（10-15分）。

  使用タイミング：
  - Phase4完了後、最終レポート作成時
  - システム全体の統合判断が必要な時

  所要時間：10-15分（自動実行）
  出力：final_strategy_report.md

trigger_keywords:
  - "最終レポート"
  - "Fund Manager"
  - "最終承認"

dependencies:
  - trading-phase1-analysts
  - trading-phase2-research
  - trading-phase3-risk
  - agent-trader

input_files:
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase1/{YYYY-MM-DD}/analysts_summary.md
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/research_consensus.md
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/risk_management_report.md
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase4/{YYYY-MM-DD}/trading_plan.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase4/{YYYY-MM-DD}/final_strategy_report.md

execution_time: 10-15分（自動実行）

stage: Phase4 - Trading Team (Fund Manager)

priority: P0
---

# Fund Manager Skill

全フェーズの結果を統合し、最終戦略レポートを作成する自律型エージェント。

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 10-15分

### ステップ1: 全フェーズ結果読み込み

```markdown
Read: phase1/analysts_summary.md
Read: phase2/research_consensus.md
Read: phase3/risk_management_report.md
Read: phase4/trading_plan.md
```

### ステップ2: 統合レビュー

Phase1-4の整合性確認、最終チェック。

### ステップ3: 最終承認

トレード戦略の最終承認、リスク管理最終確認。

### ステップ4: final_strategy_report.md生成

**システム全体の最終成果物**を生成。
- エグゼクティブサマリー
- Phase1-4の統合結果
- 最終推奨トレード戦略
- リスク管理指針
- 実行チェックリスト

---

## 成果物

```
TradingAgents/data/results/phase4/2025-12-29/
├── trading_plan.md
└── final_strategy_report.md ← システム全体の最終成果物
```
