---
name: for-solo-validate-unit-economics
description: ForSolo特化版ユニットエコノミクス検証スキルを実行
---

# ForSolo Validate Unit Economics Command

このコマンドはForSolo特化版のユニットエコノミクス検証スキルを実行します。

## 実行内容

`/validate-unit-economics` スキル（ForSolo Edition）を起動し、以下を自動実行:

1. CAC（顧客獲得コスト）算出
2. LTV（顧客生涯価値）算出
3. LTV/CAC比率評価
4. 利益率分析
5. 収益化戦略最適化

## ForSolo特化要素

- **CAC目標**: $0-10（広告費ゼロ前提、SEO・Build in Public重視）
- **LTV目標**: $100以上（月額$10 × 12ヶ月継続想定）
- **LTV/CAC比率**: 10.0以上（ForStartup 3.0より厳格、利益率重視）
- **利益率**: 80%以上（コスト最小化戦略）
- **Payback Period**: 1ヶ月以内（即座に回収）
- Solopreneur Research統合: 85件

## 使用タイミング

- PMF検証完了後
- 収益化本格化時
- 四半期レビュー

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/solopreneur/unit_economics.md`

## 次のコマンド

検証完了後:
- `/for-solo-design-micro-saas-model` - Micro-SaaS収益化モデル最適化へ
- `/for-solo-measure-aarrr` - AARRR測定へ

## 参照

- スキル詳細: @.claude/skills/for_solo/validate-unit-economics/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
