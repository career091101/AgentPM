---
name: for-solo-validate-psf
description: ForSolo特化版PSF検証スキルを実行
---

# ForSolo Validate PSF Command

このコマンドはForSolo特化版のPSF（Problem Solution Fit）検証スキルを実行します。

## 実行内容

`/validate-psf` スキル（ForSolo Edition）を起動し、以下を自動実行:

1. MVP/プロトタイプ評価
2. 初期ユーザーフィードバック分析
3. ソリューション受容性評価
4. 価格感度テスト
5. PSF総合判定

## ForSolo特化要素

- **初期ユーザー数**: 30人以上（ForStartup 50人より緩和、Micro-SaaS基準）
- **ソリューション満足度**: 70%以上
- **価格受容性**: 月額$10-$50で60%が「適切」
- **継続利用意向**: 60%以上
- **MVP実装コスト**: $1,000以下
- Solopreneur Research統合: 85件

## 使用タイミング

- CPF検証完了後
- MVP/プロトタイプ作成後
- PSF達成を判断したい

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/2_discovery/psf_judgment.md`

## 次のコマンド

PSF達成時:
- `/for-solo-validate-pmf` - PMF検証へ
- `/for-solo-design-micro-saas-model` - Micro-SaaS収益化モデル設計へ

要改善時:
- `/for-solo-validate-cpf` - CPF再検証
- `/for-solo-simulate-interview` - 追加インタビュー

## 参照

- スキル詳細: @.claude/skills/for_solo/validate-psf/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
