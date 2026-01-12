---
description: 新規アイデア検討時に関連する失敗パターンを警告表示する
---

# /check_failure_patterns ワークフロー

**バージョン**: 1.0  
**作成日**: 2025-12-26

---

## 概要

新規アイデア検討時に、`failure_patterns.md`から関連する失敗パターンを検索し、リスク警告を表示する。

## ファイルパス

```
BASE_PATH: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Solopreneur_Research/documents

DB: {BASE_PATH}/01_App/data/failure_patterns.md
出力（任意）: {IDEA_FOLDER}/documents/references/failure_check.md
```

---

## 実行コマンド

```text
/check_failure_patterns category="マッチングアプリ"
/check_failure_patterns keywords="AI,画像生成,SaaS"
/check_failure_patterns category="SaaS" keywords="スケジューラー"
```

---

## 入力パラメータ

| パラメータ | 必須 | 説明 | 例 |
|-----------|------|------|-----|
| `category` | △ | アイデアのカテゴリ | マッチングアプリ、SaaS、EC |
| `keywords` | △ | 関連キーワード（カンマ区切り） | AI,画像生成,自動化 |
| `output` | - | レポート出力先（任意） | {IDEA_FOLDER}/... |

※ `category` または `keywords` のいずれかは必須

---

## ワークフローステップ

### STEP 1: DBロード
// turbo
```text
処理:
  1. failure_patterns.md を読み込み
  2. 各セクションをパース:
     - カテゴリ別統計
     - 失敗理由パターン
     - 失敗事例詳細

ツール: view_file
```

---

### STEP 2: カテゴリマッチング
// turbo
```text
処理:
  1. 入力categoryがカテゴリ別統計に存在するかチェック
  2. 該当する場合:
     - リスク評価を取得（🔴/🟡/🟢）
     - 代表事例を取得
     - 失敗件数を取得

出力:
  カテゴリ一致: あり/なし
  リスク評価: 🔴高リスク / 🟡中リスク / 🟢低リスク
  失敗件数: X件
  代表事例: [事例名]
```

---

### STEP 3: キーワードマッチング
// turbo
```text
処理:
  1. 入力keywordsで失敗事例詳細テーブルを検索
  2. プロダクト名、カテゴリ、失敗理由にヒットする行を抽出
  3. 関連パターン（P1〜P10）を特定

出力:
  ヒット件数: X件
  関連パターン: [P1, P2, ...]
  該当事例: [事例リスト]
```

---

### STEP 4: リスク評価出力
// turbo
```text
出力フォーマット:

## ⚠️ 失敗パターン警告

### カテゴリリスク
| カテゴリ | リスク | 失敗件数 | 理由 |
|---------|-------|---------|------|
| {category} | 🔴/🟡/🟢 | X件 | ... |

### 関連失敗パターン
- **P1: 市場検証なしで作りすぎ**
  - 対策: MVPで1週間以内にローンチ
  
- **P2: バズっても収益化できない**
  - 対策: 必ず購入ボタンを付ける

### 類似失敗事例
| 人物 | プロダクト | 失敗理由 | 学び |
|------|----------|---------|------|
| ... | ... | ... | ... |

### 推奨アクション
1. ...
2. ...
```

---

### STEP 5: レポート生成（任意）
// turbo
```text
条件: output パラメータが指定された場合

処理:
  1. STEP 4 の出力をファイルに保存
  2. {IDEA_FOLDER}/documents/references/failure_check.md に出力

ツール: write_to_file
```

---

## 出力例

### 入力
```text
/check_failure_patterns category="マッチングアプリ"
```

### 出力
```markdown
## ⚠️ 失敗パターン警告

### カテゴリリスク
| カテゴリ | リスク | 失敗件数 | 理由 |
|---------|-------|---------|------|
| マッチングアプリ | 🔴高リスク | 1件 | 既存競合（Tinder等）が強すぎる |

### 関連失敗パターン
- **P1: 市場検証なしで作りすぎ**
  - 事例: Marc Lou「スポーツTinder」1年開発→ユーザー0
  - 対策: MVPで1週間以内にローンチ、事前売りで検証

### 類似失敗事例
| 人物 | プロダクト | 失敗理由 | 学び |
|------|----------|---------|------|
| Marc Lou | スポーツTinder | ユーザー0 | 市場検証なしで作りすぎ |

### 推奨アクション
1. 超ニッチに絞る（例: 特定スポーツ×特定地域）
2. MVPをできるだけ早くリリースして検証
3. VC調達せずブートストラップで進める
4. 既存競合の弱点を徹底分析する
```

---

## orchestrate_phase1_solo との統合

### 統合ポイント

```text
STEP 1: /discover_idea の後に自動実行
  1. アイデアのカテゴリを抽出
  2. /check_failure_patterns category="{抽出カテゴリ}"
  3. 警告を表示
  4. リスクが🔴の場合は確認プロンプト
```

### 統合例

```text
/discover_idea 完了後:

⚠️ このアイデアカテゴリの失敗リスクをチェック中...

[/check_failure_patterns 実行結果]

⚠️ 高リスクカテゴリが検出されました。
このまま進めますか？(y/n)
```

---

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| DBが存在しない | `/compile_failure_patterns` 実行を促す |
| カテゴリ・キーワードどちらもなし | パラメータ入力を促す |
| ヒットなし | 「該当する失敗パターンはありません」と表示 |

---

## 使用例

### カテゴリ指定
```text
/check_failure_patterns category="SaaS"
→ SaaSカテゴリの失敗パターンを警告
```

### キーワード検索
```text
/check_failure_patterns keywords="AI,チャットボット"
→ AI、チャットボット関連の失敗事例を検索
```

### 複合検索 + ファイル出力
```text
/check_failure_patterns category="EC" keywords="物販,配送" output=true
→ EC×物販の失敗パターンを検索し、レポートファイルを生成
```
