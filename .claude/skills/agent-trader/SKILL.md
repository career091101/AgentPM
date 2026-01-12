---
name: agent-trader
description: |
  Phase3リスク管理結果を基に具体的なトレード実行計画を作成する自律型エージェント。
  エントリー/イグジット条件、注文パラメータ（指値/成行/ストップロス）、
  実行スケジュールを明確化し、trading_plan.mdを生成（10-15分）。

  使用タイミング：
  - Phase3完了後、トレード実行計画が必要な時
  - 注文パラメータの詳細設計時

  所要時間：10-15分（自動実行）
  出力：trading_plan.md

trigger_keywords:
  - "トレード計画"
  - "Trader"
  - "実行計画"

dependencies:
  - trading-phase3-risk

input_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/risk_management_report.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase4/{YYYY-MM-DD}/trading_plan.md

execution_time: 10-15分（自動実行）

stage: Phase4 - Trading Team (Trader)

priority: P0
---

# Trader Skill

Phase3リスク管理結果を基に具体的なトレード実行計画を作成する自律型エージェント。

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 10-15分

### ステップ1: Phase3結果読み込み

```markdown
Read: risk_management_report.md

抽出項目:
- 推奨ポートフォリオ: [Risky/Safe/Neutral]
- エントリー価格: XX,XXX円
- 利益確定目標: XX,XXX円
- ストップロス: XX,XXX円
- ポジションサイズ: XX%
- レバレッジ: X倍
```

### ステップ2: 注文パラメータ設計

エントリー・イグジット・ストップロスの具体的な注文パラメータを設計：
- 指値 vs 成行
- トレーリングストップ
- OCO注文設計

### ステップ3: 実行スケジュール作成

1週間のトレード実行スケジュールを作成。

### ステップ4: trading_plan.md生成

Phase4最終成果物を生成。

---

## 成果物

```
TradingAgents/data/results/phase4/2025-12-29/
└── trading_plan.md
```
