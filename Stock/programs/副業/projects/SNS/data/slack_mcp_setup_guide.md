# Slack MCP サーバー 設定ガイド

approve-and-scheduleスキルで使用するSlack MCP サーバーの設定手順。

---

## 手順1: Slack Appを作成

1. https://api.slack.com/apps にアクセス
2. 「Create New App」をクリック
3. 「From scratch」を選択
4. App情報を入力：
   - **App Name**: SNS Automation Bot
   - **Pick a workspace**: 自分のワークスペースを選択
5. 「Create App」をクリック

---

## 手順2: Bot Token Scopesを追加

1. 左メニューから「OAuth & Permissions」をクリック
2. 「Scopes」セクションまでスクロール
3. 「Bot Token Scopes」で以下のスコープを追加：

| Scope | 説明 |
|-------|------|
| `chat:write` | メッセージを送信 |
| `channels:history` | パブリックチャンネルの履歴を読み取り |
| `channels:read` | パブリックチャンネル情報を読み取り |
| `groups:history` | プライベートチャンネルの履歴を読み取り（オプション） |
| `groups:read` | プライベートチャンネル情報を読み取り（オプション） |

---

## 手順3: Bot User OAuth Tokenを取得

1. 「OAuth & Permissions」ページの上部にある「Install to Workspace」をクリック
2. 権限を確認し、「Allow」をクリック
3. **Bot User OAuth Token**が表示されます（`xoxb-`で始まる）
4. このトークンをコピーして保存

例: `xoxb-123456789012-1234567890123-AbCdEfGhIjKlMnOpQrStUvWx`

---

## 手順4: Workspace IDを取得

### 方法1: Slack App設定から取得

1. Slack Appの「Basic Information」ページを開く
2. 「App Credentials」セクションで「Workspace ID」を確認

### 方法2: Slack Workspaceから取得

1. Slackを開く
2. ワークスペース名をクリック → 「設定と管理」→「ワークスペースの設定」
3. URLに表示される `https://[workspace-name].slack.com/admin/settings#workspace_name` の[workspace-name]部分がWorkspace ID

---

## 手順5: Botを#sns-automationチャンネルに追加

1. Slackで#sns-automationチャンネルを開く（存在しない場合は作成）
2. チャンネル詳細を開く（チャンネル名をクリック）
3. 「インテグレーション」タブをクリック
4. 「アプリを追加する」をクリック
5. 「SNS Automation Bot」を検索して追加

---

## 手順6: ClaudeCode設定ファイルを編集

**設定ファイルパス**: `~/.config/claude/claude_desktop_config.json`

### 既存設定がある場合

既存の`mcpServers`に`slack`を追加：

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-slack"
      ],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-123456789012-1234567890123-AbCdEfGhIjKlMnOpQrStUvWx",
        "SLACK_TEAM_ID": "T01234567"
      }
    }
  }
}
```

### 新規設定の場合

ファイルを新規作成：

```bash
mkdir -p ~/.config/claude
nano ~/.config/claude/claude_desktop_config.json
```

以下の内容を貼り付け：

```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-slack"
      ],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-123456789012-1234567890123-AbCdEfGhIjKlMnOpQrStUvWx",
        "SLACK_TEAM_ID": "T01234567"
      }
    }
  }
}
```

**重要**:
- `SLACK_BOT_TOKEN`: 手順3で取得したトークンに置き換え
- `SLACK_TEAM_ID`: 手順4で取得したWorkspace IDに置き換え

---

## 手順7: ClaudeCodeを再起動

設定を反映させるため、ClaudeCodeを再起動してください。

---

## 手順8: 動作確認

ClaudeCodeで以下を実行して動作確認：

```
Slackの#sns-automationチャンネルにテストメッセージを送信してください。

メッセージ内容: "Slack MCP サーバー動作確認テスト"
```

ClaudeCodeがSlack MCPツールを使ってメッセージを送信し、Slackチャンネルにメッセージが表示されればOK。

---

## トラブルシューティング

### エラー: "Slack MCP server not found"

**原因**: ClaudeCodeが設定ファイルを読み込めていない

**対処法**:
1. 設定ファイルパスが正しいか確認：`~/.config/claude/claude_desktop_config.json`
2. JSON形式が正しいか確認（カンマ、括弧の位置）
3. ClaudeCodeを再起動

### エラー: "Invalid token"

**原因**: Bot User OAuth Tokenが間違っている

**対処法**:
1. Slack Appの「OAuth & Permissions」で正しいトークンをコピー
2. `xoxb-`で始まるトークンであることを確認
3. 設定ファイルに正しく貼り付け

### メッセージが送信されない

**原因**: Botがチャンネルに追加されていない

**対処法**:
1. Slackで#sns-automationチャンネルを開く
2. 「インテグレーション」→「アプリを追加する」でBotを追加
3. チャンネルに「SNS Automation Botが参加しました」と表示されることを確認

### エラー: "channel_not_found"

**原因**: チャンネル名が間違っている、またはBotがアクセスできない

**対処法**:
1. チャンネル名が`#sns-automation`であることを確認
2. Botがチャンネルに追加されているか確認
3. プライベートチャンネルの場合は`groups:history`スコープを追加

---

## 完了チェックリスト

- [ ] Slack App作成完了
- [ ] Bot Token Scopes追加完了（`chat:write`, `channels:history`, `channels:read`）
- [ ] Bot User OAuth Token取得完了
- [ ] Workspace ID取得完了
- [ ] Botを#sns-automationチャンネルに追加完了
- [ ] ClaudeCode設定ファイル編集完了
- [ ] ClaudeCode再起動完了
- [ ] 動作確認完了（テストメッセージ送信成功）

---

## 次のステップ

Slack MCP サーバー設定完了後、approve-and-scheduleスキルを実行できます：

```bash
/approve-and-schedule
```

または

```
投稿承認
```

---

## 参考資料

- Slack API Documentation: https://api.slack.com/
- Slack MCP Server: https://github.com/modelcontextprotocol/servers/tree/main/src/slack
- ClaudeCode MCP設定: https://modelcontextprotocol.io/quickstart/user
