# GitHub App Setup Guide for Claude Code

Week 7 Day 1-2: GitHub App統合のためのセットアップガイド

## 概要

Claude Code公式GitHub Appをインストールし、Pull Requestの自動レビュー機能を有効化します。

---

## 前提条件

- GitHubアカウント
- リポジトリの管理者権限（Settings > Integrationsへのアクセス）
- Claude Code CLI（最新版）

---

## Step 1: Claude Code GitHub Appのインストール

### 1-1. Claude Code CLIからインストール

Claude Code CLI内で以下のコマンドを実行：

```bash
claude
# Claude Code起動後
/install-github-app
```

**実行結果**:
- ブラウザが自動的に開き、GitHub App認証ページが表示されます
- GitHub App: `Claude Code`の認証画面が表示されます

### 1-2. GitHub App権限の確認

以下の権限が要求されます：

| 権限 | スコープ | 説明 |
|------|---------|------|
| **Pull requests** | Read & Write | PRの読み取り、コメント投稿 |
| **Contents** | Read | リポジトリファイルの読み取り |
| **Metadata** | Read | リポジトリメタデータの読み取り |
| **Issues** | Read & Write | Issue読み取り、コメント投稿（オプション） |
| **Workflows** | Read & Write | GitHub Actions実行（オプション） |

### 1-3. リポジトリの選択

**オプション1: 全リポジトリ（All repositories）**
- 現在および将来作成するすべてのリポジトリにClaude Codeアクセスを許可

**オプション2: 選択したリポジトリ（Only select repositories）**
- 特定のリポジトリのみ選択（推奨）
- 例: `aipm_v0`のみ選択

### 1-4. インストール完了

「Install」ボタンをクリック → Claude Code CLI に戻ると、インストール完了メッセージが表示されます。

---

## Step 2: リポジトリ設定の確認

### 2-1. GitHub Settings > Integrations

1. GitHubリポジトリページ → Settings → Integrations
2. 「Installed GitHub Apps」セクションに「Claude Code」が表示されていることを確認

### 2-2. アクセス許可の確認

「Configure」をクリック → 権限とリポジトリアクセスを確認

---

## Step 3: @claude タグの使用方法

### 3-1. Pull Requestでの使用

Pull Request内でClaude Codeを呼び出す方法：

#### 方法1: PRコメントで @claude メンション

```markdown
@claude このPRをレビューしてください
```

#### 方法2: PRタイトルまたは本文に @claude タグ

```markdown
## PR Title
feat: Add new feature @claude
```

#### 方法3: コミットメッセージに @claude タグ

```bash
git commit -m "feat: Add feature @claude review"
```

### 3-2. レビューリクエストの例

**基本的なレビュー**:
```markdown
@claude レビューしてください
```

**特定の観点でのレビュー**:
```markdown
@claude セキュリティの観点でレビューしてください
```

**コード品質チェック**:
```markdown
@claude このコードのパフォーマンスを改善できますか？
```

**テストカバレッジ確認**:
```markdown
@claude テストが十分か確認してください
```

---

## Step 4: CLAUDE.mdルール自動追記の設定

### 4-1. CLAUDE.mdの準備

プロジェクトルートに`CLAUDE.md`が存在することを確認：

```bash
ls -l CLAUDE.md
```

### 4-2. GitHub Actionワークフロー設定

`.github/workflows/claude_pr_review.yml`を作成（Week 7 Day 3-5で実装）。

このワークフローにより：
1. @claudeタグ検出時に自動レビュー実行
2. レビュー結果からルールを抽出
3. CLAUDE.mdに自動追記
4. 重複ルールの自動チェック

---

## 使用例

### 例1: 新機能のレビュー

**PRタイトル**: `feat: Add user authentication @claude`

**自動実行内容**:
1. Claude Codeが認証コードをレビュー
2. セキュリティリスク、ベストプラクティス違反をチェック
3. レビューコメントをPRに投稿
4. 発見したルール（例: 「パスワードは必ずハッシュ化すること」）をCLAUDE.mdに追記

### 例2: バグ修正のレビュー

**PRコメント**: `@claude この修正で本当にバグが解決しますか？`

**自動実行内容**:
1. 修正内容を分析
2. エッジケースのチェック
3. テストケースの提案
4. レビュー結果をコメント投稿

### 例3: リファクタリングのレビュー

**PRコメント**: `@claude パフォーマンスとコードの可読性を確認してください`

**自動実行内容**:
1. リファクタリング前後の比較
2. パフォーマンス改善の確認
3. 可読性の評価
4. 改善提案

---

## セキュリティとプライバシー

### 1. プライベートリポジトリの扱い

- Claude Code GitHub Appは**プライベートリポジトリにもアクセス可能**
- 必要最小限のリポジトリのみ選択することを推奨
- 機密情報を含むリポジトリは慎重に選択

### 2. コード送信の制御

- Claude Codeは**@claudeタグが付いたPRのみ処理**
- タグがないPRは自動レビューされない
- レビュー範囲はPRの差分のみ（リポジトリ全体は送信されない）

### 3. データ保持ポリシー

- Anthropicのデータ保持ポリシーに準拠
- レビューログは一定期間後に自動削除
- 詳細: https://www.anthropic.com/privacy

---

## トラブルシューティング

### 問題1: @claudeタグが反応しない

**症状**: PRで@claudeタグを付けても何も起こらない

**原因**:
1. GitHub Appがインストールされていない
2. リポジトリへのアクセス許可がない
3. GitHub Actionワークフローが未設定

**解決策**:
```bash
# 1. GitHub App再インストール
claude
/install-github-app

# 2. GitHub Settings > Integrations で権限確認
# 3. .github/workflows/claude_pr_review.yml が存在するか確認
ls -l .github/workflows/claude_pr_review.yml
```

---

### 問題2: 権限エラー

**症状**: `Error: Claude Code does not have permission to access this repository`

**原因**: GitHub Appがリポジトリにアクセスできない

**解決策**:
1. GitHub Settings > Integrations > Claude Code > Configure
2. 「Repository access」で対象リポジトリを追加
3. 「Save」をクリック

---

### 問題3: レビュー結果が投稿されない

**症状**: レビューは実行されるがPRコメントが投稿されない

**原因**: GitHub Appの「Pull requests」権限が不足

**解決策**:
1. GitHub App再インストール
2. 「Pull requests: Read & Write」権限を確認
3. 必要に応じて権限を追加

---

## GitHub App vs GitHub Action の違い

| 機能 | GitHub App | GitHub Action |
|------|-----------|--------------|
| **トリガー** | @claudeタグ検出 | PRイベント |
| **実行場所** | Anthropicサーバー | GitHub Actionsランナー |
| **認証** | GitHub App OAuth | GITHUB_TOKEN |
| **コスト** | Claudeサブスクリプション | GitHub Actionsランタイム |
| **制限** | Claude API制限 | GitHub Actions制限（月2000分無料） |
| **セットアップ** | `/install-github-app` | `.github/workflows/*.yml` |

**推奨**: 両方を併用
- **GitHub App**: リアルタイムの対話的レビュー（@claudeタグ）
- **GitHub Action**: 自動化された定期レビュー（全PR）

---

## ベストプラクティス

### 1. @claudeタグの使い分け

**レビュー依頼時**:
```markdown
@claude レビューしてください
```

**特定の観点**:
```markdown
@claude セキュリティとパフォーマンスを確認
```

**質問時**:
```markdown
@claude このアプローチは適切ですか？代替案はありますか？
```

### 2. CLAUDE.mdの管理

- 重複ルールを避けるため、定期的に整理
- セクション分けで可読性向上（例: Security, Performance, Code Style）
- レビューで抽出されたルールは必ず確認してからマージ

### 3. レビュー頻度の調整

- **すべてのPR**: セキュリティクリティカルなプロジェクト
- **重要なPRのみ**: 通常のプロジェクト
- **マージ前の最終確認**: 大規模リファクタリング

---

## 次のステップ

GitHub App設定完了後、以下を実装：

1. **GitHub Actionワークフロー**: `.github/workflows/claude_pr_review.yml`（Week 7 Day 3-5）
2. **CLAUDE.md自動更新**: レビュー結果のルール抽出と追記
3. **統合テスト**: 実際のPRでの動作確認

---

## 参照

- **Claude Code GitHub App**: https://github.com/apps/claude-code（仮想URL）
- **GitHub Apps Documentation**: https://docs.github.com/en/apps
- **Week 7実装ガイド**: @.claude/rules/github_action_integration.md（作成予定）
