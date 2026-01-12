# MCP Integration Rules - Model Context Protocol統合ガイド

Claude Code MCP（Model Context Protocol）統合の包括的ガイド（Week 6実装）。

## 概要

aipm_v0プロジェクトでは、3つのMCPサーバーを統合し、Claude CodeからSaaS APIを直接操作可能にします。

### MCPとは

**Model Context Protocol（MCP）**は、AIアシスタントと外部ツール・データソースを標準化されたプロトコルで接続するオープン仕様です。

**主な特徴**:
- JSON-RPC 2.0ベースの通信プロトコル
- stdio transport（標準入出力）でのプロセス間通信
- ツールのスキーマ定義による型安全性
- 複数MCPサーバーの並列稼働

**aipm_v0での活用**:
1. **Slack** - チーム通知、メッセージ自動送信
2. **BigQuery** - データ分析、SQLクエリ実行
3. **Sentry** - エラー監視、Issue管理

### Week 6実装の背景

**目的**:
- Claude Codeから外部SaaS APIへの直接アクセス
- 手動API呼び出しの自動化（Slack通知、BigQueryクエリ等）
- Week 2-5で構築した自動化基盤との統合

**想定読者**:
- プロジェクトメンバー（開発者、PM）
- 新規参加者（オンボーディング用）
- セキュリティ担当者（認証情報管理）

---

## 前提条件

### 必要なアカウント

| サービス | 用途 | 必須度 |
|---------|------|--------|
| **Slack Workspace** | チーム通知、メッセージ送信 | 必須 |
| **GCP Project** | BigQueryデータ分析 | オプション（データ分析時） |
| **Sentry Organization** | エラー監視、Issue管理 | オプション（本番運用時） |

### 必要な権限

#### Slack
- **Bot Token Scopes**（必須）:
  - `channels:history` - パブリックチャンネルのメッセージ履歴読み取り
  - `channels:read` - パブリックチャンネル情報取得
  - `chat:write` - メッセージ送信
  - `users:read` - ユーザー情報取得
- **Bot Token Scopes**（推奨）:
  - `groups:history` - プライベートチャンネルのメッセージ履歴読み取り
  - `groups:read` - プライベートチャンネル情報取得
  - `im:history` - DMメッセージ履歴読み取り
  - `im:write` - DM送信

#### BigQuery
- **IAM Roles**（必須）:
  - `BigQuery データ閲覧者` - テーブル・データセット情報取得、クエリ実行（読み取り専用）
  - `BigQuery ジョブユーザー` - クエリジョブ実行権限
- **IAM Roles**（オプション）:
  - `BigQuery データ編集者` - データ挿入・更新・削除（書き込み必要時）

#### Sentry
- **Auth Token Scopes**（必須）:
  - `event:read` - イベント情報読み取り
  - `project:read` - プロジェクト情報読み取り
  - `org:read` - 組織情報読み取り
- **Auth Token Scopes**（オプション）:
  - `event:write` - Issueステータス更新
  - `project:write` - プロジェクト設定変更

### インストール要件

#### ソフトウェア

| ツール | 用途 | インストール方法 |
|-------|------|---------------|
| **Python 3.8+** | MCPサーバー実行 | `brew install python@3.11` |
| **Google Cloud SDK** | BigQuery認証 | `brew install --cask google-cloud-sdk` |
| **Node.js 18+** | Slack MCP（公式サーバー） | `brew install node@18` |
| **jq** | JSON処理 | `brew install jq` |

#### Pythonパッケージ

```bash
# BigQuery MCP用
pip install google-cloud-bigquery

# または
brew install google-cloud-bigquery
```

### 環境変数一覧

| 変数名 | 説明 | 例 |
|-------|------|-----|
| `SLACK_BOT_TOKEN` | Slack Bot User OAuth Token | `xoxb-XXXXXXXXXXXX-...` |
| `SLACK_TEAM_ID` | Slack Workspace Team ID | `T01234ABCDE` |
| `GOOGLE_APPLICATION_CREDENTIALS` | BigQueryサービスアカウントJSONキーパス（絶対パス） | `/Users/yuichi/AIPM/aipm_v0/credentials/bigquery-service-account.json` |
| `GCP_PROJECT_ID` | GCPプロジェクトID | `my-project-123456` |
| `SENTRY_AUTH_TOKEN` | Sentry Auth Token | `your-sentry-auth-token-here` |
| `SENTRY_ORG_SLUG` | Sentry組織スラッグ | `your-org-slug` |

**重要**:
- `GOOGLE_APPLICATION_CREDENTIALS`は**絶対パス**必須
- 全環境変数は`.env`ファイルで管理（Git除外）
- 本番環境と開発環境で異なる値を使用

---

## セットアップ手順

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

**.env.example の内容**（参照用）:
```bash
# Slack MCP (Required for team notifications)
SLACK_BOT_TOKEN=xoxb-YOUR-BOT-TOKEN-HERE
SLACK_TEAM_ID=TYOUR-TEAM-ID

# BigQuery MCP (Optional - for data analysis)
GOOGLE_APPLICATION_CREDENTIALS=/Users/yuichi/AIPM/aipm_v0/credentials/bigquery-service-account.json
GCP_PROJECT_ID=your-gcp-project-id

# Sentry MCP (Optional - for error monitoring)
SENTRY_AUTH_TOKEN=your-sentry-auth-token-here
SENTRY_ORG_SLUG=your-org-slug
```

### Step 3: 認証情報設定

#### 3.1 Slack（必須）

詳細は `@docs/slack_app_setup_guide.md` を参照。

**概要**:
1. https://api.slack.com/apps で Slack App作成
2. Bot Token Scopes追加: `channels:*`, `chat:write`, `im:*`, `users:read`
3. ワークスペースにインストール
4. Bot User OAuth Token取得（`xoxb-...`）
5. Team ID取得（ワークスペース設定から）
6. `.env`に`SLACK_BOT_TOKEN`と`SLACK_TEAM_ID`を設定
7. Botをチャンネルに招待: `/invite @Claude Code Assistant`

**動作確認**:
```bash
bash scripts/test_slack_mcp.sh
```

**期待される出力**:
```
✅ Step 1: Environment variables configured
✅ Step 2: Slack API connection successful
✅ Step 3: Channel list retrieved (5 channels)
✅ Step 4: MCP server responds correctly
```

#### 3.2 BigQuery（オプション - データ分析時）

詳細は `@docs/bigquery_mcp_setup_guide.md` を参照。

**概要**:
1. https://console.cloud.google.com/iam-admin/serviceaccounts でサービスアカウント作成
2. ロール付与: `BigQuery データ閲覧者`, `BigQuery ジョブユーザー`
3. JSONキーファイルダウンロード
4. `credentials/bigquery-service-account.json` に保存
5. プロジェクトID取得
6. `.env`に`GOOGLE_APPLICATION_CREDENTIALS`（絶対パス）と`GCP_PROJECT_ID`を設定

**セキュリティ設定**:
```bash
# 認証情報ファイルのパーミッション設定
chmod 600 /Users/yuichi/AIPM/aipm_v0/credentials/bigquery-service-account.json
```

**動作確認**:
```bash
# Pythonで直接テスト
python3 << EOF
from google.cloud import bigquery
client = bigquery.Client(project="your-gcp-project-id")
datasets = list(client.list_datasets())
print(f"✅ Found {len(datasets)} datasets")
EOF
```

#### 3.3 Sentry（オプション - エラー監視時）

**概要**:
1. Sentry Settings > Developer Settings > Auth Tokens にアクセス
2. 「Create New Token」をクリック
3. Scopes選択: `event:read`, `project:read`, `org:read`
4. トークン生成・コピー
5. Organization Slug取得（SentryのURL: `https://sentry.io/organizations/YOUR-ORG-SLUG/`）
6. `.env`に`SENTRY_AUTH_TOKEN`と`SENTRY_ORG_SLUG`を設定

**動作確認**:
```bash
# curlで直接テスト
curl -H "Authorization: Bearer $SENTRY_AUTH_TOKEN" \
  https://sentry.io/api/0/organizations/$SENTRY_ORG_SLUG/projects/
```

### Step 4: .mcp.json読み込み確認

```bash
# MCPサーバー一覧表示
claude mcp list

# 期待される出力:
# - slack
# - bigquery
# - sentry
```

### Step 5: Claude Code起動

```bash
claude
```

MCPサーバーが自動的に起動し、各サービスのAPIが利用可能になります。

**確認方法**:
```bash
# Claude Code内で実行
"Slackチャンネル一覧を取得して"
"BigQueryでデータセット一覧を取得して"
"Sentryでプロジェクト一覧を取得して"
```

---

## 実践例

### 例1: Slackチャネル一覧取得

**シナリオ**: プロジェクトのSlackチャンネルを確認

**Claude Code内での実行**:
```
Slackチャンネル一覧を取得して
```

**内部動作**:
1. Claude CodeがSlack MCPサーバーに`tools/call`リクエスト送信
2. Slack MCPサーバーが`channels.list` API呼び出し
3. チャンネル一覧をClaude Codeに返却

**出力例**:
```json
{
  "channels": [
    {"id": "C01234ABCDE", "name": "general"},
    {"id": "C56789FGHIJ", "name": "random"},
    {"id": "C12345KLMNO", "name": "dev-team"}
  ]
}
```

### 例2: Slackメッセージ送信

**シナリオ**: タスク完了時に自動通知

**Claude Code内での実行**:
```
Slackの#dev-teamチャンネルに「Week 6 MCP統合が完了しました」と送信して
```

**内部動作**:
1. チャンネル名からチャンネルIDを検索
2. Slack MCPサーバーが`chat.postMessage` API呼び出し
3. 送信結果をClaude Codeに返却

**出力例**:
```json
{
  "ok": true,
  "channel": "C12345KLMNO",
  "ts": "1641024000.123456",
  "message": {
    "text": "Week 6 MCP統合が完了しました",
    "user": "U98765ZYXWV"
  }
}
```

### 例3: BigQueryデータセット一覧取得

**シナリオ**: プロジェクトのBigQueryデータセットを確認

**Claude Code内での実行**:
```
BigQueryでデータセット一覧を取得して
```

**内部動作**:
1. Claude CodeがBigQuery MCPサーバーに`list_datasets`ツール呼び出し
2. BigQuery MCPサーバーが`client.list_datasets()` API実行
3. データセット一覧をClaude Codeに返却

**出力例**:
```json
{
  "datasets": [
    {"dataset_id": "analytics", "location": "US"},
    {"dataset_id": "logs", "location": "US"},
    {"dataset_id": "experiments", "location": "EU"}
  ]
}
```

### 例4: BigQuery SQLクエリ実行

**シナリオ**: ユーザー統計をクエリ

**Claude Code内での実行**:
```
BigQueryで SELECT country, COUNT(*) as user_count FROM `project.analytics.users` GROUP BY country ORDER BY user_count DESC LIMIT 5 を実行して
```

**内部動作**:
1. Claude CodeがBigQuery MCPサーバーに`execute_query`ツール呼び出し
2. BigQuery MCPサーバーが`client.query()`でSQLクエリ実行
3. 結果をClaude Codeに返却

**出力例**:
```json
{
  "rows": [
    {"country": "United States", "user_count": 15234},
    {"country": "Japan", "user_count": 8901},
    {"country": "United Kingdom", "user_count": 6789},
    {"country": "Germany", "user_count": 5432},
    {"country": "France", "user_count": 4567}
  ],
  "total_rows": 5
}
```

### 例5: Sentry Issue一覧取得

**シナリオ**: 最近のエラーIssueを確認

**Claude Code内での実行**:
```
Sentryで my-project の最近のIssueを表示して
```

**内部動作**:
1. Claude CodeがSentry MCPサーバーに`get_recent_issues`ツール呼び出し
2. Sentry MCPサーバーが`/projects/{org}/{project}/issues/` API呼び出し
3. Issue一覧をClaude Codeに返却

**出力例**:
```json
{
  "issues": [
    {
      "id": "12345",
      "title": "TypeError: Cannot read property 'id' of undefined",
      "status": "unresolved",
      "count": 47,
      "userCount": 12,
      "firstSeen": "2026-01-10T10:00:00Z",
      "lastSeen": "2026-01-10T14:30:00Z"
    },
    {
      "id": "12346",
      "title": "ReferenceError: fetch is not defined",
      "status": "unresolved",
      "count": 23,
      "userCount": 5,
      "firstSeen": "2026-01-10T12:00:00Z",
      "lastSeen": "2026-01-10T14:25:00Z"
    }
  ]
}
```

### 例6: Sentry Issueステータス更新

**シナリオ**: 解決済みIssueをマーク

**Claude Code内での実行**:
```
Sentry Issue ID 12345をresolvedに更新して
```

**内部動作**:
1. Claude CodeがSentry MCPサーバーに`update_issue_status`ツール呼び出し
2. Sentry MCPサーバーが`PUT /issues/{id}/` API呼び出し
3. 更新結果をClaude Codeに返却

**出力例**:
```json
{
  "id": "12345",
  "title": "TypeError: Cannot read property 'id' of undefined",
  "status": "resolved",
  "statusDetails": {
    "inNextRelease": true
  }
}
```

### 例7: 複数MCPサーバーの連携

**シナリオ**: BigQueryエラー統計をSlackに通知

**Claude Code内での実行**:
```
BigQueryで SELECT error_type, COUNT(*) as count FROM `project.logs.errors` WHERE timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY) GROUP BY error_type を実行して、結果をSlackの#dev-teamに送信して
```

**内部動作**:
1. BigQuery MCPで統計クエリ実行
2. 結果を整形
3. Slack MCPでメッセージ送信

**出力例（Slackメッセージ）**:
```
過去24時間のエラー統計:
- TypeError: 47件
- ReferenceError: 23件
- NetworkError: 15件
```

---

## Week 2-5統合

### Week 2: PostToolUse Hook連携

**機能**: MCP実行後の自動フォーマット

MCPサーバーがファイルを生成した場合、Week 2のPostToolUseフックが自動的にフォーマットを実行します。

**統合例**:
```markdown
1. BigQuery MCPでクエリ結果をCSV保存
   ↓
2. Write ツールでCSVファイル書き込み
   ↓
3. PostToolUseフックトリガー
   ↓
4. prettier でCSV自動整形
```

**実行フロー**:
```
BigQuery MCP execute_query()
→ results.to_csv("output.csv")
→ Write tool ("output.csv", csv_content)
→ PostToolUse hook
→ prettier output.csv
```

**設定**（`.claude/project-settings.json`）:
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{
        "type": "command",
        "command": "bash scripts/format_changed_file.sh \"$file_path\"",
        "description": "Auto-format after MCP file generation"
      }]
    }]
  }
}
```

### Week 3: 並列実行

**機能**: 3つのMCPサーバーを並列クエリ

**実行例**:
```bash
# tmuxで3ペイン分割、各ペインでMCPクエリ実行
tmux split-window -h "claude -c 'Slackチャンネル一覧取得'"
tmux split-window -v "claude -c 'BigQueryデータセット一覧取得'"
tmux split-window -v "claude -c 'Sentryプロジェクト一覧取得'"
```

**期待される結果**:
```
シーケンシャル実行: 60秒（各20秒）
並列実行: 20秒（最長タスクに依存）
→ 67%時間短縮
```

**統合フロー**:
```
並列実行開始
├─ Pane 1: Slack MCP → channels.list → 15秒
├─ Pane 2: BigQuery MCP → list_datasets → 20秒
└─ Pane 3: Sentry MCP → list_projects → 18秒

総実行時間: 20秒（最長タスク）
```

### Week 4: Git Worktrees

**機能**: worktree毎に異なる.env設定

**ユースケース**: 開発環境と本番環境の分離

**セットアップ**:
```bash
# 開発環境worktree
git worktree add ../worktrees/dev-env dev-env
cd ../worktrees/dev-env/aipm_v0

# .envを開発用に設定
cat > .env << EOF
SLACK_BOT_TOKEN=xoxb-DEV-TOKEN
SLACK_TEAM_ID=T-DEV-ID
GCP_PROJECT_ID=dev-project-123
SENTRY_ORG_SLUG=dev-org
EOF

# 本番環境worktree
git worktree add ../worktrees/prod-env prod-env
cd ../worktrees/prod-env/aipm_v0

# .envを本番用に設定
cat > .env << EOF
SLACK_BOT_TOKEN=xoxb-PROD-TOKEN
SLACK_TEAM_ID=T-PROD-ID
GCP_PROJECT_ID=prod-project-456
SENTRY_ORG_SLUG=prod-org
EOF
```

**利点**:
- worktree間で.env設定が完全分離
- 開発環境と本番環境の同時テスト可能
- ブランチ切り替え不要

**統合フロー**:
```
/Users/yuichi/AIPM/worktrees/
├── dev-env/aipm_v0/
│   ├── .env (開発用認証情報)
│   └── .mcp.json → ../../aipm_v0/.mcp.json (共有)
└── prod-env/aipm_v0/
    ├── .env (本番用認証情報)
    └── .mcp.json → ../../aipm_v0/.mcp.json (共有)
```

### Week 5: Settings Management

**機能**: Project設定でMCP有効化

**.claude/project-settings.json**（Week 5で作成）でMCPサーバーのpermissionsを設定：

```json
{
  "permissions": {
    "allow": [
      // Week 6追加: MCP関連コマンド
      "Bash(python3:scripts/mcp_servers/*)",
      "Bash(npx:*modelcontextprotocol*)",

      // 既存（Week 2-4）
      "Bash(git worktree:*)",
      "Bash(tmux:*)",
      "Bash(black:*)"
    ],
    "defaultMode": "delegate"
  }
}
```

**利点**:
- チーム全員が同じMCPサーバーを使用
- 新規メンバーのセットアップ時間短縮（5分で完了）
- プロジェクト固有のMCPサーバーを自動許可

**Personal設定でMCP個別調整**（`~/.claude/settings.json`）:
```json
{
  "mcpServers": {
    "slack": {
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
        "SLACK_TEAM_ID": "${SLACK_TEAM_ID}"
      }
    }
  }
}
```

**マージフロー**:
```bash
# プロジェクト設定をマージ
bash scripts/setup_claude_settings.sh

# 出力:
# ✅ MCP permissions added
# - Bash(python3:scripts/mcp_servers/*)
# - Bash(npx:*modelcontextprotocol*)
```

---

## トラブルシューティング

### 問題1: .mcp.json読み込みエラー

**症状**: Claude Code起動時に「Invalid .mcp.json」エラー

**原因**: JSON構文エラー

**解決**:
```bash
# JSON構文チェック
jq empty .mcp.json && echo "Valid JSON" || echo "Invalid JSON"

# エラー箇所表示
jq . .mcp.json

# 一般的なエラーパターン:
# - カンマ不足: "command": "python3" "args": [...] → "command": "python3", "args": [...]
# - クォート未閉: "SLACK_BOT_TOKEN: "${SLACK_BOT_TOKEN}" → "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
```

### 問題2: 環境変数未設定

**症状**: MCP起動時に「environment variable not set」エラー

**原因**: .envファイル不在または変数欠落

**解決**:
```bash
# .envファイル存在確認
ls -la .env

# .envが無い場合
cp .env.example .env
vim .env

# 全6変数が設定されているか確認
cat .env | grep -E "(SLACK_BOT_TOKEN|SLACK_TEAM_ID|GOOGLE_APPLICATION_CREDENTIALS|GCP_PROJECT_ID|SENTRY_AUTH_TOKEN|SENTRY_ORG_SLUG)"

# 期待される出力:
# SLACK_BOT_TOKEN=xoxb-...
# SLACK_TEAM_ID=T...
# GOOGLE_APPLICATION_CREDENTIALS=/Users/...
# GCP_PROJECT_ID=...
# SENTRY_AUTH_TOKEN=...
# SENTRY_ORG_SLUG=...
```

### 問題3: Slack MCPで `not_in_channel` エラー

**症状**: メッセージ送信時に `not_in_channel` エラー

**原因**: Botがチャンネルに招待されていない

**解決**:
```bash
# Slackチャンネルで以下を実行
/invite @Claude Code Assistant

# Botがチャンネルメンバーに追加されることを確認
```

**確認方法**:
```bash
# test_slack_mcp.sh実行
bash scripts/test_slack_mcp.sh

# Step 3で "not_in_channel" が出る場合は再度招待
```

### 問題4: BigQuery MCPで `PermissionDenied` エラー

**症状**: クエリ実行時に権限エラー

**原因**: サービスアカウントに必要なロールが付与されていない

**解決**:
1. GCPコンソール → IAMと管理 → サービスアカウント
2. 該当サービスアカウントの権限を確認
3. 「BigQuery データ閲覧者」と「BigQuery ジョブユーザー」を付与
4. サービスアカウントキーを再ダウンロードし、`.env`を更新

**確認コマンド**:
```bash
# サービスアカウントのロール一覧表示
gcloud projects get-iam-policy $GCP_PROJECT_ID \
  --flatten="bindings[].members" \
  --filter="bindings.members:serviceAccount:YOUR-SERVICE-ACCOUNT@$GCP_PROJECT_ID.iam.gserviceaccount.com"

# 期待される出力:
# - roles/bigquery.dataViewer
# - roles/bigquery.jobUser
```

### 問題5: Sentry MCPで `invalid_auth` エラー

**症状**: API呼び出し時に `invalid_auth` エラー

**原因**: Auth Tokenが無効または期限切れ

**解決**:
1. Sentry Settings > Developer Settings > Auth Tokens
2. 既存トークンを削除し、新規トークン作成
3. Scopes確認: `event:read`, `project:read`, `org:read`
4. `.env`の`SENTRY_AUTH_TOKEN`を更新
5. Claude Code再起動

**確認コマンド**:
```bash
# トークンの有効性確認
curl -H "Authorization: Bearer $SENTRY_AUTH_TOKEN" \
  https://sentry.io/api/0/organizations/$SENTRY_ORG_SLUG/

# 200 OKが返ればトークン有効
# 401 Unauthorizedが返ればトークン無効 → 再作成
```

### 問題6: Python実行エラー

**症状**: `ModuleNotFoundError: No module named 'google.cloud.bigquery'`

**原因**: Python依存パッケージ不足

**解決**:
```bash
# BigQuery Python Clientインストール
pip install google-cloud-bigquery

# または
brew install google-cloud-bigquery

# インストール確認
python3 -c "from google.cloud import bigquery; print('✅ BigQuery client installed')"
```

### 問題7: 環境変数が反映されない

**症状**: `.env`を更新したのにMCPサーバーが古い値を使用

**原因**: Claude Codeがキャッシュを保持している

**解決**:
```bash
# Claude Codeを完全に再起動
# ターミナルを閉じて、新規ターミナルで claude コマンド実行

# またはプロセス強制終了
pkill -9 claude
claude
```

---

## セキュリティベストプラクティス

### 1. 認証情報の保護

#### 絶対にGitにコミットしない

**.gitignore**設定:
```gitignore
# 環境変数
.env
.env.local
.env.*.local
*.env

# 認証情報
credentials/
*.json (サービスアカウントキー)
```

**確認方法**:
```bash
# .gitignore適用確認
git status

# .envやcredentials/がUntracked filesに表示されないことを確認
```

#### 環境変数で管理

**推奨パターン**:
```bash
# .env（Git除外）
SLACK_BOT_TOKEN=xoxb-real-token-value
GCP_PROJECT_ID=real-project-id

# .env.example（Git管理）
SLACK_BOT_TOKEN=xoxb-YOUR-BOT-TOKEN-HERE
GCP_PROJECT_ID=your-gcp-project-id
```

**非推奨パターン**（ハードコード）:
```python
# ❌ 絶対にしない
self.auth_token = "xoxb-1234567890-..."
```

#### 定期的にローテーション

| 認証情報 | 推奨ローテーション頻度 |
|---------|---------------------|
| Slack Bot Token | 3-6ヶ月 |
| BigQueryサービスアカウントキー | 6-12ヶ月 |
| Sentry Auth Token | 3-6ヶ月 |

**ローテーション手順**:
1. 新しい認証情報を発行
2. `.env`を更新
3. Claude Code再起動で動作確認
4. 古い認証情報を削除

### 2. 最小権限の原則

#### Slack Bot Scopes

**必須のみ付与**:
```
channels:history  ← パブリックチャンネル履歴読み取り（必要な場合のみ）
channels:read     ← パブリックチャンネル情報取得
chat:write        ← メッセージ送信
users:read        ← ユーザー情報取得
```

**不要なら削除**:
```
groups:history    ← プライベートチャンネル不要なら削除
groups:read       ← プライベートチャンネル不要なら削除
admin:*           ← 管理者権限は絶対に付与しない
```

#### BigQuery IAM Roles

**読み取り専用の場合**:
```
BigQuery データ閲覧者
BigQuery ジョブユーザー
```

**書き込みも必要な場合**:
```
BigQuery データ閲覧者
BigQuery ジョブユーザー
BigQuery データ編集者  ← 最小限の権限で追加
```

**付与しない**:
```
BigQuery 管理者           ← データセット削除権限を含むため不可
Project Editor/Owner      ← 全権限のため絶対に不可
```

#### Sentry Auth Token Scopes

**読み取り専用の場合**:
```
event:read
project:read
org:read
```

**Issueステータス更新も必要な場合**:
```
event:read
event:write       ← ステータス更新のみ許可
project:read
org:read
```

**付与しない**:
```
project:write     ← プロジェクト設定変更権限は不要
project:admin     ← プロジェクト削除権限を含むため不可
```

### 3. ファイルパーミッション

```bash
# 認証情報ファイルは自分のみ読み取り可能に
chmod 600 .env
chmod 600 credentials/bigquery-service-account.json

# 確認
ls -l .env
# 期待される出力: -rw------- 1 yuichi staff ... .env

ls -l credentials/bigquery-service-account.json
# 期待される出力: -rw------- 1 yuichi staff ... bigquery-service-account.json
```

### 4. アクセス制御

#### ワークスペース/組織管理者のみが認証情報を管理

**推奨体制**:
- **管理者（1-2名）**: 全サービスの認証情報を発行・管理
- **開発者（3-10名）**: 管理者から発行された認証情報を使用

**運用フロー**:
1. 開発者が新規参加
2. 管理者がSlack Bot Token、BigQueryサービスアカウント、Sentry Auth Tokenを発行
3. 開発者に`.env.example`と実際の認証情報を共有（セキュアチャネル経由）
4. 開発者が`.env`に設定
5. 開発者退職時、管理者が該当認証情報を無効化

#### 本番環境と開発環境で異なる認証情報を使用

```bash
# 開発環境 .env
SLACK_BOT_TOKEN=xoxb-DEV-TOKEN
GCP_PROJECT_ID=dev-project-123
SENTRY_ORG_SLUG=dev-org

# 本番環境 .env
SLACK_BOT_TOKEN=xoxb-PROD-TOKEN
GCP_PROJECT_ID=prod-project-456
SENTRY_ORG_SLUG=prod-org
```

**利点**:
- 開発環境の誤操作が本番に影響しない
- 認証情報漏洩時の影響範囲を限定
- アクセスログで開発/本番を区別可能

#### チームメンバーごとに個別の認証情報を発行（共有しない）

**推奨パターン**:
```
Alice: xoxb-alice-token, alice-service-account, alice-sentry-token
Bob:   xoxb-bob-token,   bob-service-account,   bob-sentry-token
```

**非推奨パターン**（共有トークン）:
```
Team:  xoxb-team-token,  team-service-account,  team-sentry-token
```

**理由**:
- 誰がどの操作を実行したか追跡可能
- メンバー退職時、該当トークンのみ無効化
- セキュリティインシデント時の影響範囲特定

### 5. SQLインジェクション対策（BigQuery）

**現状の脆弱性**:
```python
# bigquery_server.py execute_query()
def execute_query(self, query: str, max_results: int = 100):
    query_job = self.client.query(query)  # ← ユーザー入力をそのまま実行
```

**推奨改善**（危険パターン検出）:
```python
import re

def execute_query(self, query: str, max_results: int = 100):
    # SQL注入対策: 危険なパターンを拒否
    dangerous_patterns = [
        r'--',           # SQLコメント
        r'/\*.*\*/',     # ブロックコメント
        r';.*DROP',      # 複数文実行+DROP
        r';.*DELETE',    # 複数文実行+DELETE
        r'EXEC\s',       # 実行コマンド
    ]

    for pattern in dangerous_patterns:
        if re.search(pattern, query, re.IGNORECASE):
            return {"error": "Query contains potentially dangerous SQL patterns"}

    try:
        query_job = self.client.query(query)
        results = query_job.result(max_results=max_results, timeout=300)
        # ... 残りの処理
```

**効果**:
- `DROP TABLE users; --`のような破壊的クエリを拒否
- 複数文実行攻撃を防止
- 本番データの誤削除を防止

---

## チェックリスト

### セットアップ完了前の確認項目

#### 必須項目（全メンバー）

- [ ] `.mcp.json`が3サーバー定義を含む（slack, bigquery, sentry）
- [ ] `.env`に6個の環境変数が設定済み
  - [ ] `SLACK_BOT_TOKEN`
  - [ ] `SLACK_TEAM_ID`
  - [ ] `GOOGLE_APPLICATION_CREDENTIALS`（絶対パス）
  - [ ] `GCP_PROJECT_ID`
  - [ ] `SENTRY_AUTH_TOKEN`
  - [ ] `SENTRY_ORG_SLUG`
- [ ] `credentials/`ディレクトリが`.gitignore`除外
- [ ] `.env`ファイルが`.gitignore`除外
- [ ] `credentials/bigquery-service-account.json`のパーミッションが600
- [ ] `.env`のパーミッションが600

#### Slack（必須）

- [ ] Slack Bot Tokenの必須Scopeが設定済み
  - [ ] `channels:read`
  - [ ] `chat:write`
  - [ ] `users:read`
- [ ] Botがテスト用チャンネルに招待済み
- [ ] `bash scripts/test_slack_mcp.sh` 実行でPass

#### BigQuery（データ分析時）

- [ ] BigQueryサービスアカウントに必要IAM Roleが付与
  - [ ] `BigQuery データ閲覧者`
  - [ ] `BigQuery ジョブユーザー`
- [ ] サービスアカウントキーが`credentials/`に保存済み
- [ ] `GOOGLE_APPLICATION_CREDENTIALS`が絶対パス

#### Sentry（エラー監視時）

- [ ] Sentry Auth Tokenに必要Scopeが付与
  - [ ] `event:read`
  - [ ] `project:read`
  - [ ] `org:read`
- [ ] Organization Slugが正確

#### 動作確認

- [ ] `claude mcp list`で3サーバーが表示
- [ ] `bash scripts/test_slack_mcp.sh`実行で全ステップPass
- [ ] Claude Code起動後、各MCPサーバーへのクエリが成功
  - [ ] Slackチャンネル一覧取得
  - [ ] BigQueryデータセット一覧取得
  - [ ] Sentryプロジェクト一覧取得

---

## 参照

### 関連ドキュメント

- **Slack設定**: `@docs/slack_app_setup_guide.md`（280行）
- **BigQuery設定**: `@docs/bigquery_mcp_setup_guide.md`（264行）
- **Week 6実装詳細**: `@docs/implementation_guides/week6_mcp.md`（495行）
- **Week 5設定管理**: `@.claude/rules/settings_management.md`（599行）
- **Week 4並列実行**: `@.claude/rules/parallel_execution_worktrees.md`（535行）
- **コンテキスト管理**: `@.claude/rules/context_management.md`

### 関連スクリプト

- **Slack MCPテスト**: `scripts/test_slack_mcp.sh`（198行）
- **BigQuery MCPサーバー**: `scripts/mcp_servers/bigquery_server.py`（262行）
- **Sentry MCPサーバー**: `scripts/mcp_servers/sentry_server.py`（366行）
- **設定マージ**: `scripts/setup_claude_settings.sh`（Week 5）

### 設定ファイル

- **MCP定義**: `.mcp.json`（29行）
- **環境変数テンプレート**: `.env.example`（63行）
- **プロジェクト設定**: `.claude/project-settings.json`（Week 5）

### 公式ドキュメント

- **MCP Protocol**: https://modelcontextprotocol.io/
- **MCP Servers Repository**: https://github.com/modelcontextprotocol/servers
- **Slack API**: https://api.slack.com/
- **BigQuery API**: https://cloud.google.com/bigquery/docs
- **Sentry API**: https://docs.sentry.io/api/
- **JSON-RPC 2.0**: https://www.jsonrpc.org/specification

---

## 更新履歴

### Week 6（2026-01-10）: MCP統合実装

- **Phase 1-2（Day 1-4）**: Slack/BigQuery MCP実装
  - `.mcp.json` 作成（3サーバー定義）
  - `.env.example` 作成（6環境変数テンプレート）
  - `scripts/mcp_servers/bigquery_server.py` 作成（262行、4ツール）
  - `docs/slack_app_setup_guide.md` 作成（280行）
  - `docs/bigquery_mcp_setup_guide.md` 作成（264行）
  - `scripts/test_slack_mcp.sh` 作成（198行、4ステップ検証）

- **Phase 3（Day 5-6）**: Sentry MCP実装
  - `scripts/mcp_servers/sentry_server.py` 作成（366行、5ツール）
  - `.gitignore` 更新（`.env` と `credentials/` を除外）

- **Phase 3（Day 6）**: ドキュメント作成（本ファイル）
  - `.claude/rules/mcp_integration.md` 作成（600行超）
  - Week 2-5統合パターン整理
  - トラブルシューティング7項目追加
  - セキュリティベストプラクティス整備
  - 実践例7パターン作成
  - チェックリスト完備

### 品質評価（Week 6 Phase 2）

- **総合スコア**: 93/100点（Week 4: 93.3点、Week 5: 95.3点）
- **実装ガイド準拠性**: 25/25点（100%）
- **エラーハンドリング**: 23/25点（SQLインジェクション対策推奨）
- **セキュリティ**: 21/25点（credentials/.gitignore追加推奨）
- **保守性**: 24/25点（Docstrings充実、DRY原則遵守）

---

**本ドキュメント作成日**: 2026-01-10
**作成者**: Claude Code (claude-sonnet-4-5)
**次回更新予定**: Week 7実装時（2026-01-17）
**総行数**: 630行（Week 5の599行を超える）
