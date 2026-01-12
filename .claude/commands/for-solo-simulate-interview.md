---
name: for-solo-simulate-interview
description: ForSolo特化版インタビューシミュレーションスキルを実行
---

# ForSolo Simulate Interview Command

このコマンドはForSolo特化版のインタビューシミュレーションスキルを実行します。

## 実行内容

`/simulate-interview` スキル（ForSolo Edition）を起動し、以下を自動実行:

1. ペルソナベースのインタビューシミュレーション
2. 3U検証（Unworkable/Unavoidable/Urgent）
3. 支払い意思確認（月額$10-$50範囲）
4. 1人実行可能性との整合性確認
5. インタビュー結果レポート作成

## ForSolo特化要素

- **インタビュー数**: 10-15人（仮想）
- **3Uスコア目標**: 7点以上
- **支払い意思**: 月額$10-$50で60%が「適切」
- **1人実行可能性**: ニーズが1人で対応可能か評価
- Solopreneur Research統合: 85件

## 使用タイミング

- ペルソナ作成完了後
- CPF検証前
- 追加インタビューが必要な時

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/2_discovery/interview_simulation.md`

## 次のコマンド

シミュレーション完了後:
- `/for-solo-validate-cpf` - CPF検証へ
- `/for-solo-research-problem` - 課題深掘りへ

## 参照

- スキル詳細: @.claude/skills/for_solo/simulate-interview/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
