# Slack修正フィードバック機能 統合テストガイド

## テスト目的

Slack Interactive Buttonsで投稿承認後、スレッド返信で修正フィードバックを送り、修正案が自動生成されることを検証します。

---

## 前提条件

- [ ] ANTHROPIC_API_KEYが設定されている
- [ ] SLACK_BOT_TOKENが設定されている
- [ ] SLACK_CHANNELが設定されている（例: `#sns-automation`）
- [ ] Pythonライブラリがインストール済み（flask, pytz, anthropic, requests）
- [ ] ngrokがインストール済み

---

## テスト手順

### Step 1: 環境変数確認

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# .envファイル確認
cat .env | grep -E "ANTHROPIC_API_KEY|SLACK_BOT_TOKEN|SLACK_CHANNEL"

# 環境変数読み込み
source .env

# 確認
echo "ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:0:10}..."
echo "SLACK_BOT_TOKEN: ${SLACK_BOT_TOKEN:0:10}..."
echo "SLACK_CHANNEL: $SLACK_CHANNEL"
```

**期待結果**: すべての環境変数が表示される

---

### Step 2: Flaskサーバー起動

**ターミナル1**:

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# 環境変数読み込み
source .env

# Flaskサーバー起動
python3 scripts/slack_approval_server.py
```

**期待結果**:
```
============================================================
Slack Interactive Buttons受信サーバー起動
============================================================

📡 リスニング中: http://0.0.0.0:5000
   エンドポイント: /slack/interactive
   ヘルスチェック: /health

⚠️  ngrokでRequest URLを設定してください:
   1. 別ターミナルで: ngrok http 5000
   2. Forwarding URLをコピー（例: https://xxxx.ngrok-free.app）
   3. Slack App Management > Interactivity & Shortcuts > Request URL
   4. Request URLに設定: https://xxxx.ngrok-free.app/slack/interactive
```

---

### Step 3: ngrok起動

**ターミナル2**:

```bash
ngrok http 5000
```

**期待結果**:
```
Forwarding  https://xxxx-xx-xx-xx-xx.ngrok-free.app -> http://localhost:5000
```

**重要**: `https://xxxx-xx-xx-xx-xx.ngrok-free.app` をコピーしてください。

---

### Step 4: Slack App設定

1. [Slack API](https://api.slack.com/apps)にアクセス
2. 対象のSlack Appを選択
3. **Interactivity & Shortcuts**:
   - Request URL: `https://xxxx.ngrok-free.app/slack/interactive`
   - Save Changes（緑のチェックマークが表示されればOK）

4. **Event Subscriptions**:
   - Interactivityを**ON**にする
   - Request URL: `https://xxxx.ngrok-free.app/slack/events`
   - Subscribe to bot events: `message.channels` を追加
   - Save Changes（緑のチェックマークが表示されればOK）

**期待結果**: 両方のRequest URLが検証成功

---

### Step 5: 承認フロー起動

**ターミナル3**:

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# 環境変数読み込み
source .env

# 承認フロー実行
python3 scripts/approve_and_schedule.py
```

**期待結果**:
```
============================================================
Slack Interactive Buttons承認システム
============================================================

📋 設定確認
   チャンネル: #sns-automation

📂 Phase 3データ読み込み中...
✅ 読み込み完了: AI活用テスト

📝 Slack Block Kitメッセージ作成中...
✅ ボタン付きメッセージ作成完了（21ブロック）

📤 Slack通知送信中...
✅ Slack通知送信成功
   チャンネル: C1234567890
   タイムスタンプ: 1735884000.123456

⏳ Slack承認待機中...
   Slackの #sns-automation チャンネルでボタンをクリックしてください
   タイムアウト: 300秒
```

---

### Step 6: Slackで修正フィードバック送信

1. Slackの`#sns-automation`チャンネルを開く
2. 「🚀 LinkedIn投稿3案生成完了」というメッセージが表示されていることを確認
3. スレッド返信で以下を送信:

```
案1をもっとカジュアルに
```

**期待結果（ターミナル1のFlaskサーバーログ）**:
```
📨 スレッド返信受信
   ユーザー: your_username (U1234567890)
   メッセージ: 案1をもっとカジュアルに
   thread_ts: 1735884000.123456
   → 修正対象: 案1, 指示: もっとカジュアルに
✅ 修正成功（修正回数: 1）
```

**期待結果（Slackスレッド）**:
- 「🔄 案1を修正中...（5-10秒お待ちください）」というメッセージが表示される
- 5-10秒後、修正案が投稿される:
  ```
  🔄 修正案1回目（元: 案1）

  バリエーション: 数字型（修正版）
  評価: S級

  文字数: XX字 | 予測ER: 8.5%

  [修正後の投稿内容]

  ✅ 修正案を承認

  残り修正回数: 2回
  ```

---

### Step 7: 修正案承認

1. Slackスレッドの「✅ 修正案を承認」ボタンをクリック

**期待結果（ターミナル1のFlaskサーバーログ）**:
```
📥 ボタンクリック受信
   アクション: approve_refined_variant_1
   値: refined_variant_1_1
   ユーザー: your_username (U1234567890)
✅ 修正案承認結果保存: /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/approval_result_20260103_HHMMSS.json
```

**期待結果（Slackメッセージ更新）**:
```
✅ 修正案1回目が承認されました！
投稿をスケジューリングします。
承認者: @your_username
```

**期待結果（ターミナル3のapprove_and_schedule.py）**:
```
✅ 修正案を使用: 案1（修正版）（修正1回目）

✅ 投稿スケジューリング完了: /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/posts_queue_20260103.json
   LinkedIn: 2026-01-04 08:00 JST
   Facebook/X: 2026-01-04 20:00 JST

✅ 承認フロー完了
   承認案: 案1（修正版）
   キューファイル: /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/posts_queue_20260103.json

============================================================
処理完了
============================================================
```

---

### Step 8: 結果ファイル確認

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data

# 承認結果ファイル確認
ls -lt approval_result_*.json | head -1
cat approval_result_*.json | jq .

# スケジューリングキュー確認
cat posts_queue_20260103.json | jq .

# 修正履歴確認
ls -lt refine_context_*.json | head -1
cat refine_context_*.json | jq .
```

**期待結果（approval_result_*.json）**:
```json
{
  "approved": true,
  "variant": "案1（修正版）",
  "refined": true,
  "refined_content": "[修正後の投稿内容]",
  "refine_count": 1,
  "instruction": "もっとカジュアルに",
  "timestamp": "2026-01-03T14:30:00+09:00",
  "user_id": "U1234567890",
  "user_name": "your_username"
}
```

**期待結果（posts_queue_20260103.json）**:
```json
{
  "approved_at": "2026-01-03T14:30:00+09:00",
  "approved_variant": "案1（修正版）",
  "posts": [
    {
      "platform": "LinkedIn",
      "content": "[修正後の投稿内容]",
      "scheduled_time": "2026-01-04T08:00:00+09:00",
      "status": "scheduled"
    },
    ...
  ]
}
```

**期待結果（refine_context_*.json）**:
```json
{
  "thread_ts": "1735884000.123456",
  "refine_count": 1,
  "history": [
    {
      "variant_num": 1,
      "instruction": "もっとカジュアルに",
      "original_content": "[元の投稿内容]",
      "refined_content": "[修正後の投稿内容]",
      "refined_at": "2026-01-03T14:25:00+09:00"
    }
  ]
}
```

---

## 追加テストシナリオ

### テスト2: 修正回数制限

同じスレッドで以下を順番に送信:

1. `案1をもっと短く`（2回目）
2. `案1に数字を追加して`（3回目）
3. `案1を書き直して`（4回目 - 上限エラーのはず）

**期待結果（4回目）**:
```
⚠️ 修正回数が上限（3回）に達しました。新しい承認フローを開始してください。
```

---

### テスト3: エラーハンドリング

#### 3-1. 案番号なし
スレッド返信:
```
もっとカジュアルに
```

**期待結果**: 反応なし（修正指示として認識されない）

#### 3-2. 存在しない案
スレッド返信:
```
案5をもっとカジュアルに
```

**期待結果**:
```
❌ 案5は存在しません（1-3のみ）
```

---

## トラブルシューティング

### エラー1: Request URL検証失敗

**症状**: Slack AppでRequest URLを保存しようとすると「We had trouble connecting to your server」エラー

**対処**:
1. Flaskサーバーが起動しているか確認: `ps aux | grep slack_approval_server`
2. ngrokが起動しているか確認: `ps aux | grep ngrok`
3. ngrok Forwarding URLが正しいか確認
4. ヘルスチェック: `curl https://xxxx.ngrok-free.app/health`

---

### エラー2: スレッド返信に反応しない

**症状**: Slackでスレッド返信しても修正処理が実行されない

**対処**:
1. Flaskサーバーのログを確認（📨 スレッド返信受信が表示されるか）
2. Events APIの`message.channels`が追加されているか確認
3. Bot自身のメッセージではないか確認

---

### エラー3: LLM修正処理タイムアウト

**症状**: 「❌ 修正処理がタイムアウトしました（30秒超過）」

**対処**:
1. ANTHROPIC_API_KEYが正しいか確認
2. ネットワーク接続を確認
3. refine_post_variant.pyを単体テスト:
   ```bash
   cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts
   source ../.env
   python3 refine_post_variant.py 1 "もっとカジュアルに" "test_thread_ts"
   ```

---

## 成功基準

- [x] Slack通知が正常に送信される
- [x] スレッド返信で修正指示が認識される
- [x] 修正案が5-10秒で生成・投稿される
- [x] 修正案承認ボタンが機能する
- [x] スケジューリングキューに修正版が保存される
- [x] 修正回数制限（3回）が正常動作する
- [x] エラーメッセージが適切に表示される

---

## テスト完了後のクリーンアップ

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data

# テストファイル削除
rm -f approval_result_test_*.json
rm -f refine_context_*.json
rm -f posts_queue_test_*.json
```

---

## 次のステップ

統合テスト成功後:
1. SLACK_INTERACTIVE_BUTTONS_SETUP.mdの更新
2. approve-and-scheduleスキルのSKILL.md更新
3. 本番環境デプロイの準備（Heroku/AWS Lambda等）
