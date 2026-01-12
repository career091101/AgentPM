---
name: agent-safe-portfolio
description: |
  保守的なリスクリターンプロファイルのポートフォリオ戦略を設計する自律型エージェント。
  レバレッジ1倍、ストップロス-2%、目標+3%の低リスク低リターン戦略（5-10分）。

  使用タイミング：
  - Phase2完了後、リスク管理フェーズで保守的戦略が必要な時
  - 低リスク許容度のトレーダー向け

  所要時間：5-10分（自動実行）
  出力：safe_portfolio.md

trigger_keywords:
  - "保守的ポートフォリオ"
  - "Safe Portfolio"
  - "低リスク戦略"

dependencies:
  - trading-phase2-research

input_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/research_consensus.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/safe_portfolio.md

execution_time: 5-10分（自動実行）

stage: Phase3 - Risk Management Team (Safe Portfolio)

priority: P1
---

# Safe Portfolio Skill

保守的なリスクリターンプロファイルのポートフォリオ戦略を設計する自律型エージェント。

---

## ポートフォリオ設計パラメータ

```yaml
Risk Profile: Safe（保守的）
Leverage: 1倍
Target Return: +3%
Stop Loss: -2%
Position Size: ハーフ（50%）
Risk Tolerance: 低
```

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 5-10分

Phase2のresearch_consensus.mdを読み込み、保守的な戦略を設計：
- レバレッジなし（1倍）
- 狭いストップロス（-2%）
- 控えめな目標（+3%）
- ハーフポジション（50%）
- VaR（95%）計算
- ストレステスト

最終成果物として`safe_portfolio.md`を生成。

---

## 成果物

```
TradingAgents/data/results/phase3/2025-12-29/
└── safe_portfolio.md
```
