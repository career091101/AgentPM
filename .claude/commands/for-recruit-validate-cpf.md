---
name: for-recruit-validate-cpf
description: ForRecruit特化版CPF検証スキルを実行
---

# ForRecruit Validate CPF Command

このコマンドはForRecruit特化版のCPF（Customer Problem Fit）検証スキルを実行します。

## 実行内容

`/validate-cpf-for-recruit` スキルを起動し、以下を自動実行：

1. 成果物統合（persona.md, interview_simulation.md, problem_research.md）
2. 4指標評価（ForRecruit調整版）
3. 総合CPF判定
4. 社内先行導入オプション検討
5. 次ステップ提案

## ForRecruit特化要素

- インタビュー数基準: 15人以上（社内ネットワーク・既存顧客基盤活用）
- 課題共通率基準: 60%以上（社内PoC前提での段階的検証）
- 緊急性スコア基準: 6/10以上（社内リソース活用で解決可能）
- Recruit Product Research統合: 30-40事例、成功パターン・失敗教訓

## 使用タイミング

- ペルソナ・仮想インタビュー・課題裏付け調査完了後
- CPF達成を判断したい（Ring制度Ring 1～Ring 2段階）
- PSF検証へ進むべきか確認したい

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/documents/2_discovery/cpf_judgment.md`

## 次のコマンド

CPF達成時:
- `/for-recruit-research-competitors` - 競合調査へ（PSF検証開始）
- `/for-recruit-validate-psf` - PSF検証へ

要改善時:
- `/for-recruit-research-problem` - 追加インタビュー実施
- `/for-recruit-discover-demand` - 別の課題を探索

## 参照

- スキル詳細: @.claude/skills/for_recruit/validate-cpf/SKILL.md
- Research: @Recruit_Product_Research/analysis/integrated_analysis_report.md
