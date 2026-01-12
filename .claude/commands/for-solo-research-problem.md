---
name: for-solo-research-problem
description: ForSolo特化版課題調査スキルを実行
---

# ForSolo Research Problem Command

このコマンドはForSolo特化版の課題調査スキルを実行します。

## 実行内容

`/research-problem` スキル（ForSolo Edition）を起動し、以下を自動実行:

1. ソーシャルリスニング（X/Twitter、Reddit、Indie Hackers）
2. 競合プロダクトレビュー分析
3. フォーラム・コミュニティ調査
4. 課題の定量化（頻度、深刻度）
5. 1人実行可能性スクリーニング

## ForSolo特化要素

- **調査ソース**: X/Twitter、Reddit、Indie Hackers、Product Hunt等
- **課題数**: 10-15件（ニッチ領域重視）
- **1人実行可能性**: 各課題に対して6点満点で評価
- **コスト制約**: 解決策が月$50以下で実装可能か
- Solopreneur Research統合: 85件

## 使用タイミング

- 需要発見後
- ペルソナ作成前
- 課題深掘りが必要な時

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/2_discovery/problem_research.md`

## 次のコマンド

調査完了後:
- `/for-solo-create-persona` - ペルソナ作成へ
- `/for-solo-validate-cpf` - CPF検証へ

## 参照

- スキル詳細: @.claude/skills/for_solo/research-problem/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
