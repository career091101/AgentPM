# Slack修正フィードバック機能 統合テストレポート

実行日時: 2026-01-03 16:00 JST

---

## テスト結果サマリー

| カテゴリ | ステータス | 詳細 |
|---------|----------|------|
| **構文チェック** | ✅ 成功 | 全3ファイル |
| **単体テスト** | ✅ 成功 | 修正指示解析、ファイル操作 |
| **依存ライブラリ** | ✅ 完了 | anthropic, flask, pytz, requests |
| **Flaskサーバー起動** | ✅ 成功 | ポート5001で起動中 |
| **ヘルスチェック** | ✅ 成功 | /health エンドポイント正常 |
| **LLM修正処理** | ⚠️ スキップ | ANTHROPIC_API_KEY未設定 |
| **Slack通知** | ⏸️ 保留 | ngrok + Slack App設定が必要 |

---

## ✅ 成功した検証

### 1. 構文チェック（全て成功）

```bash
✅ refine_post_variant.py: 構文OK
✅ slack_approval_server.py: 構文OK
✅ approve_and_schedule.py: 構文OK
```

### 2. 単体テスト（全て成功）

#### parse_refine_instruction()
```
✅ テスト1: 案1をもっとカジュアルに → (1, "もっとカジュアルに")
✅ テスト2: 案2: 数字を増やして → (2, "数字を増やして")
✅ テスト3: 案3 もっと短く → (3, "もっと短く")
✅ テスト4: エラーケース（案番号なし） → (None, None)
```

#### ファイル操作
```
✅ refine_context作成・読み込み・検証成功
```

### 3. Flaskサーバー起動

```bash
✅ Flaskサーバー起動成功 (PID: 2798, ポート: 5001)
```

**起動ログ**:
```
============================================================
Slack Interactive Buttons受信サーバー起動
============================================================

📡 リスニング中: http://0.0.0.0:5001
   エンドポイント: /slack/interactive
   ヘルスチェック: /health
```

### 4. ヘルスチェック

```bash
$ curl http://localhost:5001/health

{
    "service": "slack-approval-server",
    "status": "ok"
}

✅ ヘルスチェック成功
```

---

## ⚠️ 未完了の検証

### 1. ANTHROPIC_API_KEY設定

**現状**: `.env`ファイルにプレースホルダーが設定されています。

```bash
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

**必要な対応**:
1. Anthropic Consoleで API Keyを取得
2. `.env`ファイルを更新:
   ```bash
   ANTHROPIC_API_KEY=sk-ant-api03-...
   ```

**検証コマンド**:
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts
source ../.env
python3 refine_post_variant.py 1 "もっとカジュアルに" "test_thread_123"
```

**期待される出力**:
```json
{
  "success": true,
  "refine_count": 1,
  "refined_post": {
    "content": "[修正後の投稿内容]",
    ...
  }
}
```

---

### 2. ngrok起動とSlack App設定

**必要な手順**:

#### Step 1: ngrok起動

```bash
# ターミナル2
ngrok http 5001
```

**期待される出力**:
```
Forwarding  https://xxxx-xx-xx-xx-xx.ngrok-free.app -> http://localhost:5001
```

#### Step 2: Slack App設定

1. [Slack API](https://api.slack.com/apps)にアクセス
2. 対象のSlack Appを選択

**Interactivity & Shortcuts**:
- Request URL: `https://xxxx.ngrok-free.app/slack/interactive`
- Save Changes（緑のチェックマークが表示されればOK）

**Event Subscriptions**:
- Interactivityを**ON**にする
- Request URL: `https://xxxx.ngrok-free.app/slack/events`
- Subscribe to bot events: `message.channels` を追加
- Save Changes（緑のチェックマークが表示されればOK）

---

### 3. エンドツーエンドテスト

**実行手順**（上記1, 2が完了後）:

#### Step 1: 承認フロー起動

```bash
# ターミナル3
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS
source .env
python3 scripts/approve_and_schedule.py
```

**期待される出力**:
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
```

#### Step 2: Slackで修正フィードバック送信

1. Slackの`#sns-automation`チャンネルを開く
2. スレッド返信で以下を送信:

```
案1をもっとカジュアルに
```

**期待される動作**:
1. 「🔄 案1を修正中...（5-10秒お待ちください）」メッセージが表示
2. 5-10秒後、修正案が投稿される
3. 「✅ 修正案を承認」ボタンが表示される

#### Step 3: 修正案承認

1. 「✅ 修正案を承認」ボタンをクリック

**期待される動作**:
1. メッセージが更新: 「✅ 修正案1回目が承認されました！」
2. `data/approval_result_*.json`が作成される
3. `data/posts_queue_*.json`が作成される

---

## 📊 現在の統合テスト環境

### サーバー状態

```bash
$ ps -p 2798
PID   TTY      STAT   TIME COMMAND
2798  ??       S      0:01.23 python3 scripts/slack_approval_server.py
```

**エンドポイント**:
- ✅ http://localhost:5001/health
- ✅ http://localhost:5001/slack/interactive
- ✅ http://localhost:5001/slack/events

### テストデータ

```bash
$ ls -lh data/posts_generated_test_20260103.json
-rw-------  1 yuichi  staff   1.1K Jan  3 15:49 data/posts_generated_test_20260103.json
```

---

## 🔧 トラブルシューティング

### 問題1: ポート5000が使用中

**原因**: macOSのControlCenter（AirPlay Receiver）が使用

**対処**: ポート5001を使用（既に対応済み）

**確認コマンド**:
```bash
lsof -ti:5001
```

### 問題2: ANTHROPIC_API_KEY未設定

**症状**:
```json
{
  "success": false,
  "error": "LLM修正処理エラー: \"Could not resolve authentication method...\""
}
```

**対処**: `.env`ファイルに実際のAPIキーを設定

---

## ✅ 次のステップ

### 即座に実行可能

1. **ANTHROPIC_API_KEY設定**
   ```bash
   # .envファイル編集
   vi /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/.env

   # 以下に変更
   ANTHROPIC_API_KEY=sk-ant-api03-YOUR_ACTUAL_KEY_HERE
   ```

2. **LLM修正処理テスト**
   ```bash
   cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts
   source ../.env
   python3 refine_post_variant.py 1 "もっとカジュアルに" "test_thread_123"
   ```

### 手動操作が必要

3. **ngrok起動**
   ```bash
   ngrok http 5001
   ```

4. **Slack App設定**
   - Interactivity & Shortcuts: Request URL設定
   - Event Subscriptions: Request URL設定、`message.channels`追加

5. **エンドツーエンドテスト**
   - `approve_and_schedule.py`実行
   - Slackでスレッド返信
   - 修正案承認ボタンクリック

---

## 📋 成功基準

- [x] Flaskサーバーが起動する
- [x] ヘルスチェックが成功する
- [x] 構文チェックが成功する
- [x] 単体テストが成功する
- [ ] LLM修正処理が成功する（APIキー設定後）
- [ ] Slack通知が送信される（ngrok設定後）
- [ ] スレッド返信で修正指示が認識される
- [ ] 修正案が5-10秒で生成・投稿される
- [ ] 修正案承認ボタンが機能する
- [ ] スケジューリングキューに修正版が保存される

---

## 🎯 完了した実装

1. ✅ refine_post_variant.py（LLM修正エンジン）
2. ✅ slack_approval_server.py（Events API、修正案投稿・承認）
3. ✅ approve_and_schedule.py（thread_ts管理、修正案対応）
4. ✅ INTEGRATION_TEST_GUIDE.md（詳細手順書）
5. ✅ posts_generated_test_20260103.json（テストデータ）

---

## 📞 サポート

詳細な手順は以下を参照:
- `INTEGRATION_TEST_GUIDE.md` - 詳細な統合テスト手順
- `SLACK_INTERACTIVE_BUTTONS_SETUP.md` - Slack App設定ガイド

---

## サーバー停止方法

テスト完了後、Flaskサーバーを停止:

```bash
kill 2798
# または
kill $(cat /tmp/slack_server.pid)
```
