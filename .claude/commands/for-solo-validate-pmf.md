---
name: for-solo-validate-pmf
description: ForSolo特化版PMF検証スキルを実行
---

# ForSolo Validate PMF Command

このコマンドはForSolo特化版のPMF（Product Market Fit）検証スキルを実行します。

## 実行内容

`/validate-pmf` スキル（ForSolo Edition）を起動し、以下を自動実行:

1. PMF Score算出（Rahul Vohra式 + ソロプレナー調整）
2. 初期顧客評価（30人以上基準）
3. 利用頻度・定着率分析
4. WTP実績vs目標比較
5. Micro-SaaS収益化判定

## ForSolo特化要素

- **PMF Score基準**: 6.0以上（40%が「very disappointed」、ForStartup 7.0より緩和）
- **初期顧客数**: 30人以上（ForStartup 100人より緩和、Micro-SaaS基準）
- **LTV/CAC基準**: 10.0以上（広告費ゼロ前提、SEO・Build in Public重視）
- **利益率**: 80%以上（コスト最小化戦略）
- **月次成長率**: MRR 10%以上（$1K → $5K → $10Kロードマップ）
- Solopreneur Research統合: 85件 + Tier 2ケーススタディ20件

## 使用タイミング

- PSF検証完了後（初期顧客獲得後）
- MVP/β版リリース1-3ヶ月後
- PMF達成を判断したい

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/2_discovery/pmf_judgment.md`

## 次のコマンド

PMF達成時:
- `/for-solo-create-bip-strategy` - Build in Public戦略作成へ
- `/for-solo-design-micro-saas-model` - Micro-SaaS収益化モデル設計へ
- `/for-solo-build-flywheel` - 成長フライホイール構築へ

要改善時:
- `/for-solo-validate-psf` - PSF検証再実施
- `/for-solo-research-competitors` - 競合再分析

## 参照

- スキル詳細: @.claude/skills/for_solo/validate-pmf/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
- Tier 2 Cases: @knowledge_base/tier2_case_studies/validate-pmf/
