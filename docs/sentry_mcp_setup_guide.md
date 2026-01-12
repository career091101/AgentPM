# Sentry MCP Setup Guide

Week 6 Day 5-6: Sentry MCP統合のためのSentry Auth Token作成ガイド

## 概要

Claude CodeからSentry APIを操作するために、Sentry Auth Tokenを作成し、必要な認証情報を取得します。

---

## 前提条件

- Sentryアカウント（個人またはOrganization）
- Sentry Organization管理者権限（Auth Token作成権限）

---

## Step 1: Sentry Organization Slugの確認

### 1-1. Sentry Organizationにアクセス

https://sentry.io/ にアクセスし、対象のOrganizationを選択。

### 1-2. Organization SlugをURLから取得

ブラウザのアドレスバーに表示されるURL:

```
https://sentry.io/organizations/YOUR-ORG-SLUG/
                                ^^^^^^^^^^^^^^
                           この部分がOrganization Slug
```

例: `my-company` → Organization Slug

この値を**メモ**しておく（後で環境変数として使用）。

---

## Step 2: Auth Tokenの作成

### 2-1. Developer Settingsに移動

Sentry画面で以下の手順で移動：

1. 右上のプロフィールアイコンをクリック
2. **「Settings」** を選択
3. 左サイドバーから **「Developer Settings」** を選択
4. **「Auth Tokens」** タブを選択

### 2-2. 新規トークンの作成

「Create New Token」ボタンをクリック。

### 2-3. トークン設定

| フィールド | 値 | 説明 |
|----------|-----|------|
| **Name** | `Claude Code MCP` | トークン識別名（任意） |
| **Scopes** | 以下を選択（必須） | |
| - `event:read` | ✅ | イベント・エラー情報の読み取り |
| - `project:read` | ✅ | プロジェクト情報の読み取り |
| - `org:read` | ✅ | Organization情報の読み取り |
| - `issue:write` | ✅ | Issueステータス更新（resolved/ignored） |

**重要**: 上記の4つのScopeは**すべて必須**です。

### 2-4. トークンの生成とコピー

「Create Token」をクリック → トークンが表示されます：

```
sntrys_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

この**トークン全体を安全な場所にコピー**（一度しか表示されません）。

---

## Step 3: 環境変数の設定

### 3-1. .envファイルの作成

プロジェクトルートに`.env`ファイルを作成（Gitには含めない）：

```bash
# .env (aipm_v0/.env)

# Sentry MCP Integration (Week 6)
SENTRY_AUTH_TOKEN=sntrys_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
SENTRY_ORG_SLUG=my-company
```

### 3-2. .gitignoreに追加

```bash
# .gitignore に以下を追加（すでに追加済みの場合はスキップ）
.env
```

### 3-3. .env.exampleの作成

チームメンバー向けのテンプレート（すでに存在する場合はスキップ）：

```bash
# .env.example (aipm_v0/.env.example)

# Sentry MCP Integration (Week 6)
# 1. Go to Sentry Settings > Developer Settings > Auth Tokens
# 2. Create new token with scopes: event:read, project:read, org:read, issue:write
# 3. Copy token and set below
# 4. Set your Sentry organization slug
SENTRY_AUTH_TOKEN=your-sentry-auth-token
SENTRY_ORG_SLUG=your-org-slug
```

---

## Step 4: 動作確認（手動テスト）

### 4-1. Sentry REST APIでテスト

#### プロジェクト一覧取得テスト

```bash
# 環境変数を読み込み
source .env

# プロジェクト一覧取得
curl -X GET "https://sentry.io/api/0/organizations/${SENTRY_ORG_SLUG}/projects/" \
  -H "Authorization: Bearer ${SENTRY_AUTH_TOKEN}" \
  -H "Content-Type: application/json"
```

**成功レスポンス例**:
```json
[
  {
    "id": "12345",
    "slug": "my-project",
    "name": "My Project",
    "platform": "python",
    "status": "active"
  }
]
```

#### Issue一覧取得テスト

```bash
# プロジェクトのIssue一覧取得（project_slugは上記で取得した値を使用）
PROJECT_SLUG="my-project"

curl -X GET "https://sentry.io/api/0/projects/${SENTRY_ORG_SLUG}/${PROJECT_SLUG}/issues/?statsPeriod=24h&limit=10" \
  -H "Authorization: Bearer ${SENTRY_AUTH_TOKEN}" \
  -H "Content-Type: application/json"
```

**成功レスポンス例**:
```json
[
  {
    "id": "67890",
    "title": "ZeroDivisionError: division by zero",
    "status": "unresolved",
    "level": "error",
    "count": "5",
    "userCount": "3",
    "firstSeen": "2026-01-10T00:00:00Z",
    "lastSeen": "2026-01-10T12:00:00Z",
    "permalink": "https://sentry.io/organizations/my-company/issues/67890/"
  }
]
```

### 4-2. MCP Serverテストスクリプト（オプション）

カスタムテストスクリプトを作成（`scripts/test_sentry_mcp.sh`）:

```bash
#!/bin/bash
# test_sentry_mcp.sh - Sentry MCP Connection Test

set -e

# Load environment variables
if [ -f .env ]; then
    source .env
fi

# Check environment variables
if [ -z "$SENTRY_AUTH_TOKEN" ]; then
    echo "❌ SENTRY_AUTH_TOKEN is not set"
    exit 1
fi

if [ -z "$SENTRY_ORG_SLUG" ]; then
    echo "❌ SENTRY_ORG_SLUG is not set"
    exit 1
fi

echo "✅ Environment variables are set"

# Test API connection
echo "Testing Sentry API connection..."
response=$(curl -s -w "\n%{http_code}" -X GET \
  "https://sentry.io/api/0/organizations/${SENTRY_ORG_SLUG}/projects/" \
  -H "Authorization: Bearer ${SENTRY_AUTH_TOKEN}" \
  -H "Content-Type: application/json")

http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')

if [ "$http_code" == "200" ]; then
    echo "✅ Sentry API connection successful"
    echo "Projects:"
    echo "$body" | jq -r '.[] | "  - \(.slug) (\(.name))"' 2>/dev/null || echo "$body"
else
    echo "❌ Sentry API connection failed (HTTP $http_code)"
    echo "$body" | jq '.' 2>/dev/null || echo "$body"
    exit 1
fi
```

実行:
```bash
chmod +x scripts/test_sentry_mcp.sh
bash scripts/test_sentry_mcp.sh
```

---

## セキュリティベストプラクティス

### 1. トークンの保護

- **絶対にGitにコミットしない**（`.env`を`.gitignore`に追加）
- **環境変数で管理**（`.env`ファイル使用）
- **定期的にローテーション**（3-6ヶ月ごとに再生成推奨）

### 2. 最小権限の原則

- 必要なScopeのみ付与（不要なScopeは削除）
- 読み取り専用でよい場合は `issue:write` を削除
- 書き込み権限が必要な場合のみ `issue:write` を追加

**推奨Scope構成**:

| ユースケース | 必要Scope |
|------------|----------|
| **読み取り専用**（Issueの監視のみ） | `event:read`, `project:read`, `org:read` |
| **Issue管理**（ステータス更新も可能） | `event:read`, `project:read`, `org:read`, `issue:write` |

### 3. アクセス制御

- Organization管理者のみがAuth Tokenを管理
- 本番環境と開発環境で異なるトークンを使用
- チームメンバーごとに個別のトークンを発行（共有しない）

### 4. ファイルパーミッション

```bash
# 認証情報ファイルは自分のみ読み取り可能に
chmod 600 .env
```

---

## トラブルシューティング

### 問題1: `Invalid token` エラー

**症状**: API呼び出し時に `401 Unauthorized` または `Invalid token` エラー

**原因**: Auth Tokenが無効または期限切れ

**解決策**:
1. Sentry Settings > Developer Settings > Auth Tokens
2. 既存トークンを削除し、新規トークン作成
3. `.env`の`SENTRY_AUTH_TOKEN`を更新
4. Claude Code再起動

---

### 問題2: `Insufficient scope` エラー

**症状**: 特定のAPI呼び出しで `403 Forbidden` または `Insufficient scope` エラー

**原因**: 必要なScopeが不足

**解決策**:
1. Sentry Settings > Developer Settings > Auth Tokens
2. 該当トークンを削除し、新規トークン作成
3. 必要なScope（`event:read`, `project:read`, `org:read`, `issue:write`）をすべて選択
4. `.env`の`SENTRY_AUTH_TOKEN`を更新

---

### 問題3: `Organization not found` エラー

**症状**: `404 Not Found` または `Organization not found` エラー

**原因**: `SENTRY_ORG_SLUG`が間違っている

**解決策**:
1. ブラウザでSentryにアクセス
2. URLから正しいOrganization Slugを確認（`https://sentry.io/organizations/YOUR-ORG-SLUG/`）
3. `.env`の`SENTRY_ORG_SLUG`を修正
4. Claude Code再起動

---

### 問題4: 環境変数が反映されない

**症状**: `.env`を更新したのにMCPサーバーが古い値を使用

**原因**: Claude Codeがキャッシュを保持している

**解決策**:
```bash
# Claude Codeを完全に再起動
# ターミナルを閉じて、新規ターミナルで claude コマンド実行
```

---

## 次のステップ

Sentry Auth Token作成完了後、以下のファイルで設定を統合：

1. **MCP設定**: `.mcp.json` に `mcpServers.sentry` 設定（すでに完了）
2. **環境変数読み込み**: `.env` の `SENTRY_AUTH_TOKEN`, `SENTRY_ORG_SLUG` をMCPサーバーが参照
3. **動作確認**: Claude Code内でSentry APIを操作

---

## Sentry MCP利用可能機能

Claude Code内で以下のような操作が可能になります：

```python
# プロジェクト一覧取得
"Sentryでプロジェクト一覧を取得して"

# 最近のIssue取得
"Sentryで my-project の最近のIssueを表示して"

# Issue詳細確認
"Sentry Issue ID 12345の詳細を確認して"

# Issueステータス更新
"Sentry Issue ID 12345をresolvedに更新して"

# エラー統計取得
"Sentryで my-project の24時間のエラー統計を取得して"
```

---

## 参照

### 関連ドキュメント

- **Week 6実装ガイド**: @docs/implementation_guides/week6_mcp.md
- **Slack設定**: @docs/slack_app_setup_guide.md
- **BigQuery設定**: @docs/bigquery_mcp_setup_guide.md

### 関連スクリプト

- **Sentry MCPサーバー**: `scripts/mcp_servers/sentry_server.py`
- **Sentry MCPテスト**: `scripts/test_sentry_mcp.sh`（作成推奨）

### 公式ドキュメント

- **Sentry API Documentation**: https://docs.sentry.io/api/
- **Sentry Auth Tokens**: https://docs.sentry.io/api/auth/
- **MCP Protocol**: https://modelcontextprotocol.io/
