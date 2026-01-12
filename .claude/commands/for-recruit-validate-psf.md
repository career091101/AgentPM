---
name: for-recruit-validate-psf
description: ForRecruit特化版PSF検証スキルを実行
---

# ForRecruit Validate PSF Command

このコマンドはForRecruit特化版のPSF（Problem Solution Fit）検証スキルを実行します。

## 実行内容

`/validate-psf-for-recruit` スキルを起動し、以下を自動実行：

1. 成果物統合（cpf_diagnosis.md, 10x_validation.md, lean_canvas.md, lp/README.md）
2. PSF判定（ForRecruit調整版）
3. リクルート資産活用評価
4. 総合PSF判定
5. 次ステップ提案

## ForRecruit特化要素

- 10倍優位性基準: 1軸以上（社内リソース活用で差別化）
- MVP完成度基準: 社内PoC可能レベル（Ring 2段階での検証）
- LTV/CAC基準: 3.0以上（社内営業網活用でCAC削減）
- 初期顧客獲得基準: 50人（社内ベータテスト含む）
- Recruit Product Research統合: 30-40事例、10倍優位性パターン・失敗教訓

## 使用タイミング

- CPF達成後
- 10倍優位性検証・MVP選定完了後
- PSF達成を判断したい（Ring制度Ring 2～Ring 3ステージゲート）

## 出力

- `{IDEA_FOLDER}/documents/3_planning/psf_diagnosis.md`

## 次のコマンド

PSF達成時:
- `/create-sns-content` - SNSコンテンツ作成（ローンチ準備）
- `/startup-scorecard` - 最終評価（40点満点）

Ring 2継続時:
- `/enhance-10x-axis` - 10倍優位性軸の強化
- `/leverage-recruit-assets` - リクルート資産活用強化

要改善時:
- `/validate-10x` - 10倍優位性の再検証
- `/build-lp` - MVP類型の再検討

## 参照

- スキル詳細: @.claude/skills/for_recruit/validate-psf/SKILL.md
- Research: @Recruit_Product_Research/analysis/integrated_analysis_report.md
