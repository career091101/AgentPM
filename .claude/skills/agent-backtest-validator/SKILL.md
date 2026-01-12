---
name: agent-backtest-validator
description: |
  統合戦略を3-5年分の過去データでバックテストし、実用可能性を検証するエージェント。ルックアヘッドバイアス、サバイバーシップバイアス、オーバーフィッティングを防止し、ウォークフォワード分析（WF効率≥50%）とマーケットレジーム別評価（全レジームでシャープレシオ>0.3）で厳格に検証。合格基準はシャープレシオ≥1.0。

  使用タイミング：
  - 統合戦略生成後のバックテスト検証
  - 戦略の実用可能性判定
  - パフォーマンス指標の算出

  所要時間：50-70分
  出力：backtest_validation_report.md（パフォーマンス指標 + WF分析 + レジーム別評価 + 合否判定）
trigger_keywords:
  - "バックテスト"
  - "戦略検証"
  - "パフォーマンス評価"
stage: Backtest Validation
dependencies:
  - agent-data-collector
  - agent-strategy-synthesizer
output_file: Stock/programs/資産運用/projects/TradingAgents/data/results/{YYYY-MM-DD}/backtest_validation_report.md
execution_time: 50-70分
framework_reference: Stock/programs/資産運用/projects/TradingAgents/knowledge/backtest_methodology.md
priority: P0
framework_compliance: 100%
---

# Agent Backtest Validator Skill

統合戦略をバックテストで検証し、実用可能性を判定するエージェント。

詳細な実装内容は計画書を参照してください。

---

## 更新履歴

- 2025-12-29: 初版作成（MVP Phase 1）
