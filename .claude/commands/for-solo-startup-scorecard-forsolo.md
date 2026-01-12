---
name: for-solo-startup-scorecard-forsolo
description: ForSolo特化版スタートアップスコアカードスキルを実行
---

# ForSolo Startup Scorecard Command

このコマンドはForSolo特化版のスタートアップスコアカードスキルを実行します。

## 実行内容

`/startup-scorecard-forsolo` スキル（ForSolo Edition）を起動し、以下を自動実行:

1. 6次元評価（市場機会、ビジネスモデル、実行可能性、チーム、競争優位性、トラクション）
2. ForSolo特化スコアリング
3. 総合スコア算出（40点満点）
4. 改善提案
5. 次のアクション提示

## ForSolo特化要素

- **市場機会**: 4点以上（ニッチ市場OK）
- **ビジネスモデル**: 6点以上（利益率80%、LTV/CAC 10.0以上）
- **実行可能性**: 6点以上（1人実行可能性が最重要）
- **チーム**: 5点（1人固定）
- **競争優位性**: 4点以上（10倍優位性2軸以上）
- **トラクション**: 変動（MRR $1K → $5K → $10K）
- **総合目標**: 30点以上
- Solopreneur Research統合: 85件

## 使用タイミング

- PMF検証完了後
- 四半期レビュー
- 総合評価が必要な時

## 出力

- `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForSolo/documents/solopreneur/startup_scorecard.md`

## 次のコマンド

評価完了後:
- スコア30点以上: 成長フェーズへ
- スコア25-29点: 改善フェーズ
- スコア24点以下: ピボット検討

## 参照

- スキル詳細: @.claude/skills/for_solo/startup-scorecard-forsolo/SKILL.md
- Research: @Solopreneur_Research/documents/01_App/case_studies/
