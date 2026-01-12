---
description: Solopreneur_Researchの事例データから関連事例を検索・抽出する
---
# 事例参照ワークフロー

ソロプレナー事例研究（Solo_App / Solo_SNS / Solo_Newsletter）から、現在のアイデアに関連する成功事例・失敗パターンを抽出する。

## 概要

SolopreneurAgentの7ステップで呼び出される共通ワークフロー。  
指定されたカテゴリ・キーワードに基づいて、事例データベースから参考情報を取得する。

## 入力

| パラメータ | 必須 | 説明 |
|-----------|------|------|
| `category` | ○ | 検索カテゴリ: `product` / `marketing` / `revenue` / `growth` |
| `keywords` | ○ | 検索キーワード（カンマ区切り） |
| `limit` | - | 取得件数（デフォルト: 5件） |
| `min_japan_score` | - | 日本市場適用性スコア下限（1-5、デフォルト: 3） |

## 出力

`{IDEA_FOLDER}/documents/references/solo_cases_{category}.md`

## 実行手順

### STEP 1: データソース特定
// turbo
```text
処理:
  カテゴリに応じてデータソースを選択
  - product: Solo_App/case_studies/ + research_progress.md
  - marketing: Solo_SNS/sns_targets_list.md + case_studies/
  - revenue: Solo_Newsletter/newsletter_articles_list.md
  - growth: Solo_Newsletter/strategies/
```

### STEP 2: キーワード検索
// turbo
```text
ツール: grep_search
処理:
  1. 指定キーワードでデータソースを検索
  2. 関連する事例ファイルを特定
  3. limit件数まで絞り込み
```

### STEP 3: 事例詳細取得
// turbo
```text
ツール: view_file
処理:
  1. 特定された事例ファイルを読み込み
  2. 以下の情報を抽出:
     - 人物名/プロダクト名
     - 成功要因
     - 失敗パターン（該当あれば）
     - 日本市場適用性スコア
     - 再現可能な戦略
```

### STEP 4: レポート生成
// turbo
```text
ツール: write_to_file
出力: {IDEA_FOLDER}/documents/references/solo_cases_{category}.md

内容:
  # 事例参照レポート: {category}
  
  **検索キーワード**: {keywords}
  **取得件数**: {count}件
  
  ## 関連事例
  
  ### 1. {事例名}
  - **概要**: ...
  - **成功要因**: ...
  - **適用可能な戦略**: ...
  - **日本市場適用性**: ★★★★☆ (4/5)
  
  ## 推奨アクション
  - ...
```

---

## 使用例

### アイデア発見時（プロダクトカテゴリ参照）
```
/reference_solo_cases category=product keywords="AI,SaaS,自動化"
```

### SNSマーケティング戦略参照
```
/reference_solo_cases category=marketing keywords="Twitter,TikTok,Build in Public"
```

### 収益モデル参照
```
/reference_solo_cases category=revenue keywords="サブスク,フリーミアム,価格設定"
```

---

## 参照データソース

| カテゴリ | データソース | 件数 |
|---------|-------------|------|
| product | Solo_App/case_studies/ | 4件（調査完了） |
| product | Solo_App/research_progress.md | 109件（リスト） |
| marketing | Solo_SNS/sns_targets_list.md | 200名 |
| revenue | Solo_Newsletter/newsletter_articles_list.md | 143件 |
| growth | Solo_Newsletter/strategies/ | 戦略記事群 |

---

## 注意事項

- 日本市場適用性スコアが低い（1-2）事例は自動的に除外
- 事例データは定期的に更新される（`research_progress.md` を確認）
- 未調査事例（🔲マーク）は概要情報のみ返却
