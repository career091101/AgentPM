# Slack App Setup Guide for MCP Integration

Week 6 Day 1-2: Slack MCP統合のためのSlack App作成ガイド

## 概要

Claude CodeからSlack APIを操作するために、Slack App（Bot）を作成し、必要な認証情報を取得します。

---

## 前提条件

- Slackワークスペースの管理者権限（App追加権限）
- Slackアカウント

---

## Step 1: Slack Appの作成

### 1-1. Slack API ページにアクセス

https://api.slack.com/apps にアクセスし、「Create New App」をクリック。

### 1-2. アプリ作成方法の選択

- **「From scratch」** を選択（マニフェストではなく手動設定）

### 1-3. アプリ基本情報の入力

| フィールド | 値 |
|----------|-----|
| **App Name** | `Claude Code Assistant` |
| **Workspace** | 対象のワークスペースを選択 |

「Create App」をクリック。

---

## Step 2: Bot User の作成

### 2-1. 「OAuth & Permissions」に移動

左サイドバーから「OAuth & Permissions」を選択。

### 2-2. Scopesの設定

**Bot Token Scopes** セクションで以下のスコープを追加：

| Scope | 説明 | 必須度 |
|-------|------|--------|
| `channels:history` | パブリックチャンネルのメッセージ履歴読み取り | 必須 |
| `channels:read` | パブリックチャンネル情報の取得 | 必須 |
| `chat:write` | メッセージ送信 | 必須 |
| `groups:history` | プライベートチャンネルのメッセージ履歴読み取り | 推奨 |
| `groups:read` | プライベートチャンネル情報の取得 | 推奨 |
| `im:history` | DMの履歴読み取り | 推奨 |
| `im:read` | DM情報の取得 | 推奨 |
| `im:write` | DMの送信 | 推奨 |
| `mpim:history` | グループDMの履歴読み取り | オプション |
| `mpim:read` | グループDM情報の取得 | オプション |
| `mpim:write` | グループDMの送信 | オプション |
| `users:read` | ユーザー情報の取得 | 推奨 |
| `files:read` | ファイル情報の取得 | オプション |
| `reactions:read` | リアクション情報の取得 | オプション |

---

## Step 3: アプリをワークスペースにインストール

### 3-1. 「Install App」に移動

左サイドバーから「Install App」を選択。

### 3-2. インストール実行

「Install to Workspace」ボタンをクリック → 権限確認画面で「許可する」をクリック。

### 3-3. Bot User OAuth Tokenの取得

インストール完了後、以下のトークンが表示されます：

- **Bot User OAuth Token**: `xoxb-XXXXXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXX`

このトークンを**安全な場所にコピー**（後で環境変数として使用）。

---

## Step 4: Team IDの取得

### 4-1. ワークスペース設定を開く

Slackデスクトップアプリまたはウェブで、ワークスペース名をクリック → 「設定と管理」→ 「ワークスペースの設定」

### 4-2. Team IDを確認

URLに含まれる Team ID をコピー：

```
https://[workspace-name].slack.com/admin/settings#general
                                          ↑
                        この部分のURLパラメータに Team ID が含まれる
```

または、以下のAPIエンドポイントで確認：

```bash
curl -H "Authorization: Bearer xoxb-YOUR-BOT-TOKEN" \
  https://slack.com/api/team.info
```

レスポンスの `team.id` フィールドが Team ID（例: `T01234ABCDE`）。

---

## Step 5: 環境変数の設定

### 5-1. .envファイルの作成

プロジェクトルートに`.env`ファイルを作成（Gitには含めない）：

```bash
# .env (aipm_v0/.env)

# Slack MCP Integration (Week 6)
SLACK_BOT_TOKEN=xoxb-XXXXXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXX
SLACK_TEAM_ID=T01234ABCDE
```

### 5-2. .gitignoreに追加

```bash
# .gitignore に以下を追加
.env
```

### 5-3. .env.exampleの作成

チームメンバー向けのテンプレート：

```bash
# .env.example (aipm_v0/.env.example)

# Slack MCP Integration (Week 6)
# 1. Create Slack App at https://api.slack.com/apps
# 2. Add Bot Token Scopes: channels:history, channels:read, chat:write, groups:*, im:*, users:read
# 3. Install App to Workspace
# 4. Copy Bot User OAuth Token and Team ID
SLACK_BOT_TOKEN=xoxb-YOUR-BOT-TOKEN-HERE
SLACK_TEAM_ID=TYOUR-TEAM-ID
```

---

## Step 6: Botをチャンネルに招待

Slack MCPでメッセージを送信するには、Botをチャンネルに招待する必要があります。

### 6-1. チャンネルを開く

対象のチャンネル（例: `#general`, `#claude-notifications`）を開く。

### 6-2. Botを招待

チャンネル内で以下のコマンドを実行：

```
/invite @Claude Code Assistant
```

または、チャンネル詳細 → 「インテグレーション」→ 「アプリを追加する」→ `Claude Code Assistant` を選択。

---

## Step 7: 動作確認（手動テスト）

### 7-1. Web APIでテスト

```bash
# メッセージ送信テスト
curl -X POST https://slack.com/api/chat.postMessage \
  -H "Authorization: Bearer ${SLACK_BOT_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "channel": "C01234ABCDE",
    "text": "Hello from Claude Code!"
  }'
```

成功レスポンス：
```json
{
  "ok": true,
  "channel": "C01234ABCDE",
  "ts": "1234567890.123456",
  "message": {
    "text": "Hello from Claude Code!",
    ...
  }
}
```

---

## セキュリティベストプラクティス

### 1. トークンの保護

- **絶対にGitにコミットしない**（`.env`を`.gitignore`に追加）
- **環境変数で管理**（`.env`ファイル使用）
- **定期的にローテーション**（3ヶ月ごとに再生成推奨）

### 2. 最小権限の原則

- 必要なScopeのみ付与（不要なScopeは削除）
- プライベートチャンネルアクセスが不要なら `groups:*` を削除

### 3. アクセス制御

- ワークスペース管理者のみがApp管理可能に設定
- Botの招待を制限（特定チャンネルのみ）

---

## トラブルシューティング

### 問題1: `not_in_channel` エラー

**症状**: メッセージ送信時に `not_in_channel` エラー

**原因**: Botがチャンネルに招待されていない

**解決策**:
```
/invite @Claude Code Assistant
```

---

### 問題2: `invalid_auth` エラー

**症状**: API呼び出し時に `invalid_auth` エラー

**原因**: Bot Tokenが無効または期限切れ

**解決策**:
1. Slack API「OAuth & Permissions」で「Reinstall App」を実行
2. 新しいBot Tokenを`.env`に設定

---

### 問題3: `missing_scope` エラー

**症状**: 特定のAPI呼び出しで `missing_scope` エラー

**原因**: 必要なScopeが不足

**解決策**:
1. 「OAuth & Permissions」で必要なScopeを追加
2. 「Reinstall App」を実行
3. 新しいBot Tokenを`.env`に設定

---

## 次のステップ

Slack App作成完了後、以下のファイルで設定を統合：

1. **MCP設定**: `~/.claude/settings.json` に `mcpServers.slack` 追加
2. **環境変数読み込み**: `.env` の `SLACK_BOT_TOKEN`, `SLACK_TEAM_ID` をMCPサーバーが参照
3. **動作確認**: Claude Code内でSlack APIを操作

---

## 参照

- **Slack API Documentation**: https://api.slack.com/
- **Bot Token Scopes**: https://api.slack.com/scopes
- **MCP Slack Server**: https://github.com/modelcontextprotocol/servers/tree/main/src/slack
- **Week 6実装ガイド**: @.claude/rules/mcp_integration.md（作成予定）
