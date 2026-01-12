# MCP Integration Rules

Claude Code MCP（Model Context Protocol）統合の包括的ガイド（Week 6実装）。

## 概要

aipm_v0プロジェクトでは、3つのMCPサーバーを統合し、Claude CodeからSaaS APIを直接操作可能にします：

1. **Slack** - メッセージ送信、チャンネル情報取得（公式MCPサーバー使用）
2. **BigQuery** - SQLクエリ実行、データセット管理（カスタムMCPサーバー）
3. **Sentry** - エラー監視、Issue管理（カスタムMCPサーバー）

---

## MCPサーバー構成

### 設定ファイル構造

| ファイル | 用途 | 管理方法 |
|---------|------|---------|
| `.mcp.json` | MCPサーバー定義（Git管理） | プロジェクト標準 |
| `.env` | 認証情報（秘密情報） | 個人管理（Git除外） |
| `.env.example` | 環境変数テンプレート | プロジェクト標準（Git管理） |

### .mcp.json 構造

```json
{
  "$schema": "https://github.com/modelcontextprotocol/servers/blob/main/mcp.schema.json",
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "SLACK_TEAM_ID": "${SLACK_TEAM_ID}"
      }
    },
    "bigquery": {
      "command": "python3",
      "args": ["/Users/yuichi/AIPM/aipm_v0/scripts/mcp_servers/bigquery_server.py"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "${GOOGLE_APPLICATION_CREDENTIALS}",
        "GCP_PROJECT_ID": "${GCP_PROJECT_ID}"
      }
    },
    "sentry": {
      "command": "python3",
      "args": ["/Users/yuichi/AIPM/aipm_v0/scripts/mcp_servers/sentry_server.py"],
      "env": {
        "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
        "SENTRY_ORG_SLUG": "${SENTRY_ORG_SLUG}"
      }
    }
  }
}
```

---

## 1. Slack MCP（公式サーバー）

### セットアップ手順

#### Step 1: Slack App作成

詳細は `@docs/slack_app_setup_guide.md` を参照。

**概要**:
1. https://api.slack.com/apps で Slack App作成
2. Bot Token Scopes追加: `channels:*`, `chat:write`, `im:*`, `users:read`
3. ワークスペースにインストール
4. Bot User OAuth Token取得（`xoxb-...`）
5. Team ID取得

#### Step 2: 環境変数設定

`.env`ファイルに以下を追加：

```bash
SLACK_BOT_TOKEN=xoxb-XXXXXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXX
SLACK_TEAM_ID=T01234ABCDE
```

#### Step 3: Botをチャンネルに招待

```
/invite @Claude Code Assistant
```

#### Step 4: 動作確認

```bash
bash scripts/test_slack_mcp.sh
```

### 利用可能な機能

- チャンネル一覧取得
- メッセージ送信（パブリック/プライベートチャンネル、DM）
- メッセージ履歴読み取り
- ユーザー情報取得

---

## 2. BigQuery MCP（カスタムサーバー）

### セットアップ手順

#### Step 1: GCPサービスアカウント作成

詳細は `@docs/bigquery_mcp_setup_guide.md` を参照。

**概要**:
1. https://console.cloud.google.com/iam-admin/serviceaccounts でサービスアカウント作成
2. ロール付与: `BigQuery データ閲覧者`, `BigQuery ジョブユーザー`
3. JSONキーファイルダウンロード
4. `credentials/bigquery-service-account.json` に保存
5. プロジェクトID取得

#### Step 2: Pythonパッケージインストール

```bash
pip install google-cloud-bigquery
```

または

```bash
brew install google-cloud-bigquery
```

#### Step 3: 環境変数設定

`.env`ファイルに以下を追加（**絶対パス**必須）：

```bash
GOOGLE_APPLICATION_CREDENTIALS=/Users/yuichi/AIPM/aipm_v0/credentials/bigquery-service-account.json
GCP_PROJECT_ID=my-project-123456
```

### 利用可能な機能

- データセット一覧取得（`list_datasets`）
- テーブル一覧取得（`list_tables`）
- SQLクエリ実行（`execute_query`）
- テーブルスキーマ取得（`get_table_schema`）

### 使用例

```python
# Claude Code内で実行可能
"BigQueryでデータセット一覧を取得して"
"BigQueryで SELECT * FROM `project.dataset.table` LIMIT 10 を実行して"
"BigQueryでtable_nameのスキーマを確認して"
```

---

## 3. Sentry MCP（カスタムサーバー）

### セットアップ手順

#### Step 1: Sentry Auth Token作成

1. Sentry Settings > Developer Settings > Auth Tokens にアクセス
2. 「Create New Token」をクリック
3. Scopes選択: `event:read`, `project:read`, `org:read`
4. トークン生成・コピー

#### Step 2: Organization Slug取得

SentryのURL: `https://sentry.io/organizations/YOUR-ORG-SLUG/`

#### Step 3: 環境変数設定

`.env`ファイルに以下を追加：

```bash
SENTRY_AUTH_TOKEN=your-sentry-auth-token-here
SENTRY_ORG_SLUG=your-org-slug
```

### 利用可能な機能

- プロジェクト一覧取得（`list_projects`）
- 最近のIssue取得（`get_recent_issues`）
- Issue詳細取得（`get_issue_details`）
- Issueステータス更新（`update_issue_status`）
- エラー統計取得（`get_stats`）

### 使用例

```python
# Claude Code内で実行可能
"Sentryでプロジェクト一覧を取得して"
"Sentryで my-project の最近のIssueを表示して"
"Sentry Issue ID 12345の詳細を確認して"
"Sentry Issue ID 12345をresolvedに更新して"
"Sentryで my-project の24時間のエラー統計を取得して"
```

---

## セットアップガイド（新規メンバー向け）

### Step 1: リポジトリクローン

```bash
git clone https://github.com/your-org/aipm_v0.git
cd aipm_v0
```

### Step 2: .envファイル作成

`.env.example`をコピーして`.env`を作成：

```bash
cp .env.example .env
```

### Step 3: 各サービスのセットアップ

#### Slack（必須）

1. @docs/slack_app_setup_guide.md に従いSlack App作成
2. `.env`に`SLACK_BOT_TOKEN`と`SLACK_TEAM_ID`を設定
3. 動作確認: `bash scripts/test_slack_mcp.sh`

#### BigQuery（オプション - データ分析が必要な場合）

1. @docs/bigquery_mcp_setup_guide.md に従いGCPサービスアカウント作成
2. `.env`に`GOOGLE_APPLICATION_CREDENTIALS`と`GCP_PROJECT_ID`を設定
3. `pip install google-cloud-bigquery`

#### Sentry（オプション - エラー監視が必要な場合）

1. Sentry Auth Token作成（上記手順）
2. `.env`に`SENTRY_AUTH_TOKEN`と`SENTRY_ORG_SLUG`を設定

### Step 4: Claude Code起動

```bash
claude
```

MCPサーバーが自動的に起動し、各サービスのAPIが利用可能になります。

---

## トラブルシューティング

### 問題1: MCPサーバーが起動しない

**症状**: Claude Code起動時にMCPサーバーエラー

**診断手順**:

1. **環境変数確認**
   ```bash
   cat .env | grep -E "(SLACK_BOT_TOKEN|GCP_PROJECT_ID|SENTRY_AUTH_TOKEN)"
   ```

2. **.mcp.json構文確認**
   ```bash
   jq empty .mcp.json && echo "Valid JSON" || echo "Invalid JSON"
   ```

3. **Pythonスクリプト実行権限確認**
   ```bash
   ls -l scripts/mcp_servers/*.py
   ```

   期待される出力: `-rwxr-xr-x`（実行権限付き）

4. **手動起動テスト**
   ```bash
   # BigQuery MCPサーバーを手動起動
   python3 scripts/mcp_servers/bigquery_server.py
   # Ctrl+C で終了
   ```

**解決策**:
- 環境変数未設定: `.env`ファイルを再確認
- JSON構文エラー: `.mcp.json`を再編集
- 実行権限なし: `chmod +x scripts/mcp_servers/*.py`

---

### 問題2: Slack MCPで `not_in_channel` エラー

**症状**: メッセージ送信時に `not_in_channel` エラー

**原因**: Botがチャンネルに招待されていない

**解決策**:
```
/invite @Claude Code Assistant
```

---

### 問題3: BigQuery MCPで `PermissionDenied` エラー

**症状**: クエリ実行時に権限エラー

**原因**: サービスアカウントに必要なロールが付与されていない

**解決策**:
1. GCPコンソール → IAMと管理 → サービスアカウント
2. 該当サービスアカウントの権限を確認
3. 「BigQuery データ閲覧者」と「BigQuery ジョブユーザー」を付与
4. サービスアカウントキーを再ダウンロードし、`.env`を更新

---

### 問題4: Sentry MCPで `invalid_auth` エラー

**症状**: API呼び出し時に `invalid_auth` エラー

**原因**: Auth Tokenが無効または期限切れ

**解決策**:
1. Sentry Settings > Developer Settings > Auth Tokens
2. 既存トークンを削除し、新規トークン作成
3. `.env`の`SENTRY_AUTH_TOKEN`を更新
4. Claude Code再起動

---

### 問題5: 環境変数が反映されない

**症状**: `.env`を更新したのにMCPサーバーが古い値を使用

**原因**: Claude Codeがキャッシュを保持している

**解決策**:
```bash
# Claude Codeを完全に再起動
# ターミナルを閉じて、新規ターミナルで claude コマンド実行
```

---

## セキュリティベストプラクティス

### 1. 認証情報の保護

- **絶対にGitにコミットしない**（`.env`, `credentials/`を`.gitignore`に追加）
- **環境変数で管理**（`.env`ファイル使用）
- **定期的にローテーション**（3-6ヶ月ごとに再生成推奨）

### 2. 最小権限の原則

#### Slack
- 必要なScopeのみ付与
- プライベートチャンネルアクセスが不要なら`groups:*`を削除

#### BigQuery
- 読み取り専用でよい場合は「BigQuery データ閲覧者」のみ
- 書き込みが必要な場合のみ「BigQuery データ編集者」を追加

#### Sentry
- 必要なScopeのみ付与（`event:read`, `project:read`, `org:read`）
- 書き込み権限（`event:write`, `project:write`）は最小限に

### 3. ファイルパーミッション

```bash
# 認証情報ファイルは自分のみ読み取り可能に
chmod 600 .env
chmod 600 credentials/bigquery-service-account.json
```

### 4. アクセス制御

- ワークスペース/組織管理者のみが認証情報を管理
- 本番環境と開発環境で異なる認証情報を使用
- チームメンバーごとに個別の認証情報を発行（共有しない）

---

## 実装詳細

### カスタムMCPサーバーの構造

#### BigQuery MCP Server (`scripts/mcp_servers/bigquery_server.py`)

**主要機能**:
- stdio transportでの通信（標準入出力）
- JSON-RPC形式のリクエスト/レスポンス処理
- BigQuery Python Client Libraryを使用

**ツール一覧**:
1. `list_datasets` - データセット一覧
2. `list_tables` - テーブル一覧
3. `execute_query` - SQLクエリ実行
4. `get_table_schema` - スキーマ取得

#### Sentry MCP Server (`scripts/mcp_servers/sentry_server.py`)

**主要機能**:
- Sentry REST APIとの通信（urllib使用）
- stdio transportでの通信
- JSON-RPC形式のリクエスト/レスポンス処理

**ツール一覧**:
1. `list_projects` - プロジェクト一覧
2. `get_recent_issues` - 最近のIssue
3. `get_issue_details` - Issue詳細
4. `update_issue_status` - Issueステータス更新
5. `get_stats` - エラー統計

---

## チーム協働ガイドライン

### MCPサーバー追加のワークフロー

#### 1. 新しいMCPサーバーの追加（プロジェクト全体に影響）

```bash
# 1. カスタムMCPサーバーPythonスクリプト作成
vim scripts/mcp_servers/new_service_server.py

# 2. .mcp.json に設定追加
vim .mcp.json

# 3. .env.example にテンプレート追加
vim .env.example

# 4. セットアップガイド作成
vim docs/new_service_mcp_setup_guide.md

# 5. 変更をコミット
git add .mcp.json .env.example scripts/mcp_servers/new_service_server.py docs/new_service_mcp_setup_guide.md
git commit -m "feat(mcp): Add new_service MCP integration"
git push origin main

# 6. チームメンバーに通知
# Slackなどで「新しいMCPサーバーを追加したので、セットアップガイドを参照してください」と伝える
```

#### 2. 個人の認証情報設定（自分のみに影響）

```bash
# .envファイルを直接編集
vim .env

# 各サービスのセットアップガイドに従い認証情報を取得
# .envに追加

# Git管理対象外のため、コミット不要
```

---

## 設定変更履歴

### Week 6（2026-01-04）: MCP統合

- 追加: `.mcp.json` - MCPサーバー定義（Git管理）
- 追加: `.env.example` - 環境変数テンプレート
- 追加: `scripts/mcp_servers/bigquery_server.py` - BigQuery MCPサーバー
- 追加: `scripts/mcp_servers/sentry_server.py` - Sentry MCPサーバー
- 追加: `docs/slack_app_setup_guide.md` - Slackセットアップガイド
- 追加: `docs/bigquery_mcp_setup_guide.md` - BigQueryセットアップガイド
- 追加: `scripts/test_slack_mcp.sh` - Slack MCP動作確認スクリプト
- 更新: `.gitignore` - `.env` と `credentials/` を除外

---

## 参照

### 関連ドキュメント

- **Slack設定**: @docs/slack_app_setup_guide.md
- **BigQuery設定**: @docs/bigquery_mcp_setup_guide.md
- **Week 5設定管理**: @.claude/rules/settings_management.md
- **コンテキスト管理**: @.claude/rules/context_management.md

### 関連スクリプト

- **Slack MCPテスト**: `scripts/test_slack_mcp.sh`
- **BigQuery MCPサーバー**: `scripts/mcp_servers/bigquery_server.py`
- **Sentry MCPサーバー**: `scripts/mcp_servers/sentry_server.py`

### 公式ドキュメント

- **MCP Protocol**: https://modelcontextprotocol.io/
- **MCP Servers Repository**: https://github.com/modelcontextprotocol/servers
- **Slack API**: https://api.slack.com/
- **BigQuery API**: https://cloud.google.com/bigquery/docs
- **Sentry API**: https://docs.sentry.io/api/
