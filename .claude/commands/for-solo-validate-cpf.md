---
name: for-solo-validate-cpf
description: ForSolo特化版CPF検証スキルを実行
---

# ForSolo Validate CPF Command

このコマンドはForSolo特化版のCPF（Customer Problem Fit）検証スキルを実行します。

## 実行内容

`/validate-cpf` スキル（ForSolo Edition）を起動し、以下を自動実行:

1. 成果物統合（persona.md, interview_simulation.md, problem_research.md）
2. 4指標評価（ForSolo調整版）
3. 3Uスコア評価（7点以上必須）
4. 1人実行可能性評価（6点満点）
5. 総合CPF判定
6. 次ステップ提案

## ForSolo特化要素

- インタビュー数基準: 20人以上（実インタビュー + 仮想インタビュー）
- **課題共通率基準**: 60%以上（ForStartup 70%より緩和、ニッチ市場対応）
- 支払い意思基準: 50%以上（月額$10-$50の低価格帯を重視）
- 緊急性スコア基準: 7/10以上
- **3Uスコア**: 7点以上必須（リソース限定のため高優先度課題に集中）
- **実行可能性スコア**: 6点満点（1人実行可能性が最重要）
- Solopreneur Research統合: 85件 + Tier 2ケーススタディ20件

## 使用タイミング

- ペルソナ・仮想インタビュー・課題裏付け調査完了後
- CPF達成を判断したい（ソロプレナー基準）
- PSF検証へ進むべきか確認したい

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/2_discovery/cpf_judgment.md`

## 次のコマンド

CPF達成時:
- `/for-solo-research-competitors` - 競合調査へ（PSF検証開始）
- `/for-solo-validate-10x` - 10倍優位性検証へ

要改善時:
- `/for-solo-simulate-interview` - 追加インタビュー実施
- `/for-solo-create-persona` - ペルソナ再定義
- `/for-solo-discover-demand` - 別の課題を探索

## 参照

- スキル詳細: @.claude/skills/for_solo/validate-cpf/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
- Tier 2 Cases: @knowledge_base/tier2_case_studies/validate-cpf/
