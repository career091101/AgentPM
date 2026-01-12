---
name: agent-risk-manager
description: |
  3つのポートフォリオ（Risky/Safe/Neutral）を統合評価し、最終推奨を決定する自律型エージェント。
  VaR比較、シャープレシオ評価、Phase2期待リターンとの整合性を確認し、
  最適なリスクリターンプロファイルを選定（10-15分）。

  使用タイミング：
  - 3ポートフォリオ完成後、最終推奨が必要な時
  - Phase3の統合判断を行う時

  所要時間：10-15分（自動実行）
  出力：risk_management_report.md

trigger_keywords:
  - "リスク管理"
  - "Risk Manager"
  - "ポートフォリオ選定"

dependencies:
  - agent-risky-portfolio
  - agent-safe-portfolio
  - agent-neutral-portfolio

input_files:
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/research_consensus.md
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/risky_portfolio.md
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/safe_portfolio.md
  - Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/neutral_portfolio.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/risk_management_report.md

execution_time: 10-15分（自動実行）

stage: Phase3 - Risk Management Team (Risk Manager)

priority: P1
---

# Risk Manager Skill

3つのポートフォリオを統合評価し、最終推奨を決定する自律型エージェント。

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 10-15分

### ステップ1: 全ポートフォリオ読み込み

```markdown
Read: research_consensus.md
Read: risky_portfolio.md
Read: safe_portfolio.md
Read: neutral_portfolio.md
```

### ステップ2: ポートフォリオ比較

3つのポートフォリオを以下の基準で比較：
1. VaR（95%）
2. シャープレシオ
3. 期待リターン
4. 最大ドローダウン
5. Phase2期待リターンとの整合性

### ステップ3: 最終推奨選定

Phase2の期待リターン、確信度、投資家プロファイルから最適なポートフォリオを選定。

### ステップ4: リスク管理レポート生成

`risk_management_report.md`を生成し、Phase4への引き継ぎ事項を明確化。

---

## 成果物

```
TradingAgents/data/results/phase3/2025-12-29/
├── risky_portfolio.md
├── safe_portfolio.md
├── neutral_portfolio.md
└── risk_management_report.md ← このスキルが生成
```
