# Slack Incoming Webhook 設定ガイド

**作成日**: 2026-01-03
**目的**: SNS自動化プロジェクトのSlack承認フロー用Webhook URL取得

---

## Step 1: Slack App管理画面にアクセス

1. ブラウザで https://api.slack.com/apps を開く
2. 既存のSlack Appを選択
   - App名が不明な場合は、**「Your Apps」**から一覧を確認
   - Bot Tokenが `xoxb-8265572843616-...` で始まるAppを探す

---

## Step 2: Incoming Webhooksを有効化

1. 左サイドバーから **「Features」** → **「Incoming Webhooks」** をクリック

2. **「Activate Incoming Webhooks」** トグルを **ON** にする

   ```
   ┌──────────────────────────────────────────┐
   │ Incoming Webhooks                        │
   │ ──────────────────────────────────────── │
   │ Activate Incoming Webhooks   [ ●  ON  ] │
   │                                          │
   │ Send data into Slack in real-time.      │
   └──────────────────────────────────────────┘
   ```

3. ページをリロードして設定が保存されたことを確認

---

## Step 3: Webhook URLを生成

1. ページ下部の **「Webhook URLs for Your Workspace」** セクションまでスクロール

2. **「Add New Webhook to Workspace」** ボタンをクリック

   ```
   ┌──────────────────────────────────────────┐
   │ Webhook URLs for Your Workspace          │
   │ ──────────────────────────────────────── │
   │ [Add New Webhook to Workspace]           │
   └──────────────────────────────────────────┘
   ```

3. OAuth認証画面が表示される

---

## Step 4: チャンネルを選択

1. **「投稿先のチャンネルを選択してください」** プルダウンから **`#sns`** を選択

   ```
   ┌──────────────────────────────────────────┐
   │ Where should SNS Automation post?       │
   │ ──────────────────────────────────────── │
   │ [  #sns  ▼ ]                            │
   │                                          │
   │ Your App will be able to:                │
   │ - Post messages to #sns                  │
   │ - Attach files to #sns                   │
   └──────────────────────────────────────────┘
   ```

2. **「許可する」** ボタンをクリック

---

## Step 5: Webhook URLをコピー

1. 認証完了後、Webhook URLが表示される

   ```
   ┌──────────────────────────────────────────┐
   │ Webhook URLs for Your Workspace          │
   │ ──────────────────────────────────────── │
   │ #sns                                     │
   │ https://hooks.slack.com/services/        │
   │ T087TGUQTJ4/B087.../xxxxxxxxxxxxx       │
   │                            [Copy] [Edit] │
   └──────────────────────────────────────────┘
   ```

2. **「Copy」** ボタンをクリックしてWebhook URLをコピー

---

## Step 6: 環境変数に設定

### 方法1: .envファイルに追記（推奨）

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
```

`.env`ファイルのSlackセクションに以下を追記：

```bash
# ========================================
# Slack API Credentials (✅ 設定済み・動作確認済み）
# ========================================
SLACK_BOT_TOKEN="xoxb-8265572843616-10212517337379-gTx0Iv85LeQZVrApWpWDFaZ5"
SLACK_TEAM_ID="T087TGUQTJ4"
SLACK_CHANNEL="C0871T2T485"  # #sns チャンネル
# 動作確認: 2026-01-02 ✅

# ★ 以下を追加 ★
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/T087TGUQTJ4/B087.../xxxxxxxxxxxxx"
# 取得日: 2026-01-03
# 用途: SNS投稿承認フロー（Phase 3-2: approve-and-schedule）
```

### 方法2: シェル環境変数に設定（一時的）

```bash
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/T087TGUQTJ4/B087.../xxxxxxxxxxxxx"
```

---

## Step 7: 動作確認

Webhook URLが正しく設定されたか、テストメッセージを送信：

```bash
curl -X POST "$SLACK_WEBHOOK_URL" \
  -H 'Content-Type: application/json' \
  -d '{
    "text": "✅ Incoming Webhook設定完了テスト",
    "channel": "#sns"
  }'
```

**期待される結果**:
- `#sns`チャンネルに「✅ Incoming Webhook設定完了テスト」が投稿される
- レスポンス: `ok`

---

## トラブルシューティング

### エラー: "invalid_token"

**原因**: Webhook URLが間違っている

**対処法**:
1. Slack App管理画面に戻る
2. Webhook URLを再コピー
3. `.env`ファイルの`SLACK_WEBHOOK_URL`を更新

### エラー: "channel_not_found"

**原因**: `#sns`チャンネルが存在しないか、AppがChannelにアクセスできない

**対処法**:
1. Slackで`#sns`チャンネルが存在するか確認（現在ID: `C0871T2T485`）
2. Slack App管理画面で「Incoming Webhooks」→「Edit」→ チャンネルを再選択

### メッセージが届かない

**原因**: チャンネルIDが変更された

**対処法**:
1. Slackで`#sns`を右クリック→「チャンネル詳細を表示」→ チャンネルIDを確認
2. `.env`ファイルの`SLACK_CHANNEL`を更新

---

## セキュリティ注意事項

⚠️ **Webhook URLは秘密情報です**

- ✅ `.env`ファイルに保存（`.gitignore`で除外済み）
- ✅ 環境変数として管理
- ❌ GitHubにコミットしない
- ❌ 公開ドキュメントに記載しない
- ❌ Slackメッセージで共有しない

---

## 参照

- Slack公式ドキュメント: https://api.slack.com/messaging/webhooks
- SNSプロジェクトREADME: `Stock/programs/副業/projects/SNS/README.md`
- Phase 3-2スキル: `.claude/skills/sns-automation/approve-and-schedule/SKILL.md`

---

**次のアクション**: Webhook URL設定後、E2Eテスト実行

```bash
/approve-and-schedule  # Slack承認フロー + Late API投稿
```
