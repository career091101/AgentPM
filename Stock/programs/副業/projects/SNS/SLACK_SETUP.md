# Slack App 設定ガイド

SNS投稿管理システムとSlackを連携するための設定手順です。

## 現在のngrok URL

```
https://unconcluded-nontransitively-jannet.ngrok-free.dev
```

> **注意**: ngrokを再起動するとURLが変わります。その場合は以下の設定を再度更新してください。

---

## Step 1: Slack Appの作成（初回のみ）

1. https://api.slack.com/apps にアクセス
2. **Create New App** → **From scratch**
3. App Name: `SNS投稿管理Bot`
4. Workspace: 対象のワークスペースを選択

---

## Step 2: Bot Token Scopesの設定

**OAuth & Permissions** → **Scopes** → **Bot Token Scopes**:

| Scope | 用途 |
|-------|------|
| `chat:write` | メッセージ送信 |
| `channels:read` | チャンネル情報取得 |
| `users:read` | ユーザー情報取得 |

設定後、**Install to Workspace** をクリック。

---

## Step 3: Interactivity の設定（ボタン承認用）

**Interactivity & Shortcuts** → **Interactivity** を **On**

**Request URL**:
```
https://unconcluded-nontransitively-jannet.ngrok-free.dev/api/slack/interactive
```

---

## Step 4: Event Subscriptions の設定（スレッド返信受信用）

**Event Subscriptions** → **Enable Events** を **On**

**Request URL**:
```
https://unconcluded-nontransitively-jannet.ngrok-free.dev/api/slack/events
```

**Subscribe to bot events**:
- `message.channels` - チャンネルメッセージ受信

---

## Step 5: 環境変数の設定

`.env` ファイルに以下を追加:

```bash
# Basic Information → App Credentials → Signing Secret
SLACK_SIGNING_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# OAuth & Permissions → Bot User OAuth Token
SLACK_BOT_TOKEN=xoxb-xxxxxxxxxxxx-xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx

# 承認通知を送るチャンネルのID
SLACK_APPROVAL_CHANNEL=C0123456789
```

### チャンネルIDの取得方法

1. Slackでチャンネルを右クリック
2. **チャンネル詳細を表示**
3. 最下部の **チャンネルID** をコピー

---

## Step 6: Botをチャンネルに招待

承認通知を送りたいチャンネルで:
```
/invite @SNS投稿管理Bot
```

---

## Step 7: バックエンド再起動

環境変数を反映するためにバックエンドを再起動:

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# 既存プロセスを停止
pkill -f "sns_approval_api.py"

# 再起動
python3 scripts/sns_approval_api.py &
```

---

## 動作確認

### 1. エンドポイント疎通確認

```bash
# ngrok経由でヘルスチェック
curl https://unconcluded-nontransitively-jannet.ngrok-free.dev/api/posts
```

### 2. Slackからの承認テスト

1. WebUIで投稿を生成（http://localhost:3001）
2. Slackに承認ボタン付きメッセージが届く
3. ボタンをクリックして承認
4. WebUIにトースト通知が表示される

### 3. WebUIからの承認テスト

1. WebUIで投稿を承認
2. Slackにリアルタイム通知が届く

---

## トラブルシューティング

### ngrok URLが変わった場合

```bash
# 新しいURLを取得
curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url'

# Slack App設定を更新
# - Interactivity Request URL
# - Event Subscriptions Request URL
```

### Slack署名検証エラー

```
Invalid Slack signature
```

→ `.env`の`SLACK_SIGNING_SECRET`が正しいか確認

### チャンネル送信エラー

```
channel_not_found
```

→ Botがチャンネルに招待されているか確認（`/invite @BotName`）

---

## API エンドポイント一覧

| エンドポイント | メソッド | 用途 |
|--------------|---------|------|
| `/api/slack/interactive` | POST | Slackボタン受信 |
| `/api/slack/events` | POST | Slackイベント受信 |
| `/api/approval-events` | GET | 承認イベント取得（ポーリング用） |
| `/api/notify-slack` | POST | WebUI→Slack通知 |
| `/api/queue/approved` | GET | 承認済み投稿一覧 |
| `/api/queue/pending` | GET | 未承認投稿一覧 |

---

## 参照

- [Slack API Documentation](https://api.slack.com/docs)
- [Slack Interactive Messages](https://api.slack.com/messaging/interactivity)
- [Slack Events API](https://api.slack.com/events-api)
