# /for-recruit-create-mvv

ForRecruit特化版: MVV（Mission/Vision/Values）を早期定義する自律実行型コマンド。リクルート企業価値観（新しい価値の創造、個の尊重、社会への貢献）との整合性チェックを必須化し、既存事業とのシナジー評価を追加します。

## Skill情報

- **Skill Name**: `create-mvv-for-recruit`
- **所要時間**: 20-40分（自動実行）
- **実行モード**: 自律実行型（対話なし）

## 入力要件

- `business_idea.md`: ビジネスアイデア（オプション）
- `lean_canvas.md`: リーンキャンバス（オプション）
- 未存在時はdemand_discovery.mdから推論

## ForRecruit固有の特徴

1. **企業価値観整合性チェック**: リクルート6つの価値観との整合性必須（4項目以上）
2. **既存事業シナジー評価**: 既存事業との相互補完性、カニバリゼーション回避
3. **社内先行導入前提**: Geppoモデル（社内実証→外販）の価値観反映
4. **Recruit Product Research統合**: 10-15事例統合

## 出力成果物

- `{IDEA_FOLDER}/documents/1_initiating/mvv.md`
  - Mission（存在意義）
  - Vision（目指す未来、定量目標含む）
  - Values（行動指針3-5個）
  - リクルート企業価値観整合性チェック（6項目）
  - 既存事業シナジー評価
  - MVV整合性検証
  - Lean Canvas整合性検証

## 次のステップ

- `/build-flywheel`: フライホイール設計
- `/orchestrate-phase1-recruit`: Phase1全体オーケストレーション

## 使用例

```bash
/for-recruit-create-mvv
```

## リクルート企業価値観6項目

1. **新しい価値の創造**: 既存の常識を覆す革新
2. **個の尊重**: 一人ひとりの可能性を最大化
3. **社会への貢献**: 社会課題の解決
4. **最高へのこだわり**: 妥協なき品質追求
5. **当事者意識**: 自ら考え、自ら実行
6. **チームワーク**: 協働による価値創造

## 参照

- Skill詳細: `.claude/skills/for_recruit/create-mvv/SKILL.md`
- Recruit Product Research: `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/`
- リクルート企業価値観: リクルートグループ公式サイト
