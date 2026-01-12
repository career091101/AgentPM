---
name: agent-neutral-portfolio
description: |
  バランス型リスクリターンプロファイルのポートフォリオ戦略を設計する自律型エージェント。
  レバレッジ1.5倍、ストップロス-3%、目標+5%の中リスク中リターン戦略（5-10分）。

  使用タイミング：
  - Phase2完了後、リスク管理フェーズでバランス戦略が必要な時
  - 中リスク許容度のトレーダー向け

  所要時間：5-10分（自動実行）
  出力：neutral_portfolio.md

trigger_keywords:
  - "バランスポートフォリオ"
  - "Neutral Portfolio"
  - "中リスク戦略"

dependencies:
  - trading-phase2-research

input_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase2/{YYYY-MM-DD}/research_consensus.md

output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/phase3/{YYYY-MM-DD}/neutral_portfolio.md

execution_time: 5-10分（自動実行）

stage: Phase3 - Risk Management Team (Neutral Portfolio)

priority: P1
---

# Neutral Portfolio Skill

バランス型リスクリターンプロファイルのポートフォリオ戦略を設計する自律型エージェント。

---

## ポートフォリオ設計パラメータ

```yaml
Risk Profile: Neutral（バランス型）
Leverage: 1.5倍
Target Return: +5%
Stop Loss: -3%
Position Size: 標準（75%）
Risk Tolerance: 中
```

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 5-10分

Phase2のresearch_consensus.mdを読み込み、バランス型戦略を設計：
- 適度なレバレッジ（1.5倍）
- 適度なストップロス（-3%）
- 適度な目標（+5%）
- 標準ポジション（75%）
- VaR（95%）計算
- ストレステスト

最終成果物として`neutral_portfolio.md`を生成。

---

## 成果物

```
TradingAgents/data/results/phase3/2025-12-29/
└── neutral_portfolio.md
```
