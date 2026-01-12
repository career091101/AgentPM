# /for-recruit-design-exit-strategy

ForRecruit版撤退戦略設計コマンド。Yellow/Orange/Red Alert発動時の撤退判断、リソース再配分、ステークホルダーコミュニケーションを計画します。

## 使用方法

```
/for-recruit-design-exit-strategy
```

## 実行内容

1. Alert Level判定（Yellow/Orange/Red）
2. 撤退タイミング決定（3ヶ月 / 6ヶ月 / 即座）
3. リソース再配分計画（人材・技術・顧客データ80%活用）
4. ステークホルダーコミュニケーション計画
5. ブランド・顧客影響最小化策
6. レッスンズラーンド（失敗の教訓）
7. 次のチャレンジ機会提供

## 対象プロジェクト

- Ring 1-3で基準未達のプロジェクト
- カニバリゼーションスコア高（35%以上）
- CPF/PSF/PMFスコア低（基準未達）
- Moat Score低（Shallow Moat: 5.0未満）

## 統合データソース

- Recruit_Product_Research: 早期撤退成功事例（CODE.SCORE、エリクラ等）
- 撤退基準: 3年単月黒字、5年累損解消ルール
- 統計データ: 2年以内撤退で累損平均2億円、次の成功率60%

## スキル実行

このコマンドは以下のスキルを実行します:

```
@.claude/skills/for_recruit/design-exit-strategy/SKILL.md
```

## 前提条件

- `/validate-ring-criteria` 実行済み（Ring不合格判定）
- または `/analyze-cannibalization` 実行済み（カニバリゼーション高判定）

## 出力形式

YAML形式の撤退戦略レポート（決定、損切り、リソース再配分、コミュニケーション、教訓）
