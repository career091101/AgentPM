---
name: for-solo-create-persona
description: ForSolo特化版ペルソナ作成スキルを実行
---

# ForSolo Create Persona Command

このコマンドはForSolo特化版のペルソナ作成スキルを実行します。

## 実行内容

`/create-persona` スキル（ForSolo Edition）を起動し、以下を自動実行:

1. ペルソナプロファイル作成（1-3名）
2. ジョブ・課題・ゴール定義
3. ツール利用状況分析
4. 支払い意思レンジ推定
5. 1人実行可能性との整合性確認

## ForSolo特化要素

- **ペルソナ数**: 1-3名（ニッチ市場対応）
- **支払い意思**: 月額$10-$50の範囲
- **ツール利用**: 既存ツールスタックの把握
- **1人実行可能性**: ペルソナのニーズが1人で対応可能か評価
- Solopreneur Research統合: 85件

## 使用タイミング

- 課題調査完了後
- インタビューシミュレーション前
- ペルソナ再定義が必要な時

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/2_discovery/persona.md`

## 次のコマンド

作成完了後:
- `/for-solo-simulate-interview` - インタビューシミュレーションへ
- `/for-solo-validate-cpf` - CPF検証へ

## 参照

- スキル詳細: @.claude/skills/for_solo/create-persona/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
