# Slack Interactive Buttons セットアップガイド

このガイドでは、SNS承認フローをSlack Interactive Buttons（ワンタップ承認）に切り替える手順を説明します。

---

## 概要

**旧方式**: スレッドに「1」「2」「3」を返信（3タップ）
**新方式**: ボタンをワンタップ（1タップ）

**所要時間**: 約15分

---

## 前提条件

- Slack Appが既に作成されていること
- SLACK_BOT_TOKENとSLACK_CHANNELが環境変数に設定されていること
- Python 3.8以上
- ngrok（開発環境用）またはHTTPSサーバー（本番環境用）

---

## 手順1: 依存ライブラリのインストール

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# 必要なPythonライブラリをインストール
pip install flask pytz

# ngrok インストール（Homebrewの場合）
brew install ngrok

# または、公式サイトからダウンロード
# https://ngrok.com/download
```

---

## 手順2: Slack Appの権限確認

1. [Slack API](https://api.slack.com/apps)にアクセス
2. 対象のSlack Appを選択
3. 左メニュー「OAuth & Permissions」をクリック
4. **Bot Token Scopes**に以下が含まれているか確認：
   - `chat:write`
   - `chat:write.public`

   含まれていない場合は「Add an OAuth Scope」で追加し、「Reinstall to Workspace」を実行

---

## 手順3: Interactivity & Shortcutsの有効化

1. 左メニュー「Interactivity & Shortcuts」をクリック
2. 「Interactivity」を**ON**にする
3. **Request URL**は後で設定するため、一旦空欄のまま「Save Changes」

---

## 手順4: ngrokでローカルサーバーを公開（開発環境）

### 4-1. Flaskサーバー起動

**ターミナル1**:
```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# 環境変数読み込み（.envファイルがある場合）
source ../.env

# Flaskサーバー起動
python3 scripts/slack_approval_server.py
```

起動成功すると以下のように表示されます：
```
============================================================
Slack Interactive Buttons受信サーバー起動
============================================================

📡 リスニング中: http://0.0.0.0:5000
   エンドポイント: /slack/interactive
   ヘルスチェック: /health
```

### 4-2. ngrokでトンネル作成

**ターミナル2**:
```bash
ngrok http 5000
```

以下のように表示されます：
```
Forwarding                    https://xxxx-xx-xx-xx-xx.ngrok-free.app -> http://localhost:5000
```

**重要**: `https://xxxx-xx-xx-xx-xx.ngrok-free.app` の部分をコピーしてください（毎回異なります）

### 4-3. ヘルスチェック確認

ブラウザまたはcurlで以下のURLにアクセスし、サーバーが正常動作しているか確認：

```bash
curl https://xxxx-xx-xx-xx-xx.ngrok-free.app/health
```

期待される応答:
```json
{"service":"slack-approval-server","status":"ok"}
```

---

## 手順5: Slack AppにRequest URLを設定

1. [Slack API](https://api.slack.com/apps) > 対象のSlack App > 「Interactivity & Shortcuts」に戻る
2. **Request URL**に以下を入力：
   ```
   https://xxxx-xx-xx-xx-xx.ngrok-free.app/slack/interactive
   ```
   ※ `xxxx-xx-xx-xx-xx.ngrok-free.app` は手順4-2でコピーしたngrok URLに置き換え

3. 「Save Changes」をクリック
4. Slackが自動的にRequest URLを検証します（緑のチェックマークが表示されればOK）

**注意**: ngrok無料版はURLが24時間で失効します。ngrokを再起動した場合は、新しいURLでRequest URLを更新してください。

---

## 手順6: Signing Secretの設定（オプション、推奨）

セキュリティ強化のため、Slack署名検証を有効化します。

1. [Slack API](https://api.slack.com/apps) > 対象のSlack App > 「Basic Information」
2. **App Credentials** > **Signing Secret**の「Show」をクリックしてコピー
3. 環境変数に追加：

```bash
export SLACK_SIGNING_SECRET="your_signing_secret_here"

# または.envファイルに追加
echo 'SLACK_SIGNING_SECRET="your_signing_secret_here"' >> ../.env
```

4. Flaskサーバーを再起動

---

## 手順7: テスト実行

### 7-1. テスト用モックデータ作成

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# テスト用投稿データ作成
cat > data/posts_generated_test_20260103.json << 'TEST_DATA_EOF'
{
  "metadata": {
    "topic_selected": "AI活用テスト",
    "generated_at": "2026-01-03T14:00:00+09:00",
    "takano_method_compliance": 100
  },
  "posts": [
    {
      "variant": "数字型",
      "rating": "S級",
      "content": "【テスト投稿1】\n\nAI導入で業務効率が300%向上した企業の事例を調査しました。\n\n結論: データ整備が成功の鍵です。",
      "character_count": 80,
      "predicted_er": "8.5%",
      "recommended": true
    },
    {
      "variant": "衝撃型",
      "rating": "A級",
      "content": "【テスト投稿2】\n\n「AIは人間の仕事を奪う」は本当か？\n\n最新調査では、むしろ新しい職種が生まれています。",
      "character_count": 75,
      "predicted_er": "7.2%",
      "recommended": false
    },
    {
      "variant": "問題提起型",
      "rating": "A級",
      "content": "【テスト投稿3】\n\nAI時代に求められるスキルとは？\n\n技術スキルだけでなく、倫理観も重要です。",
      "character_count": 70,
      "predicted_er": "6.8%",
      "recommended": false
    }
  ]
}
TEST_DATA_EOF
```

### 7-2. スクリプト実行

```bash
python3 scripts/approve_and_schedule.py
```

### 7-3. Slackで承認

1. Slackの`#sns-automation`チャンネルを開く
2. 「🚀 LinkedIn投稿3案生成完了」というメッセージが表示される
3. 3つのボタン（「✅ 案1を承認」「✅ 案2を承認」「✅ 案3を承認」）が表示される
4. いずれかのボタンをクリック

### 7-4. 結果確認

ボタンクリック後、以下のファイルが生成されます：

```bash
# 承認結果
ls -la data/approval_result_*.json

# スケジューリングキュー
ls -la data/posts_queue_*.json
cat data/posts_queue_*.json
```

期待される出力:
```json
{
  "approved_at": "2026-01-03T14:30:00+09:00",
  "approved_variant": "案1",
  "posts": [
    {
      "platform": "LinkedIn",
      "content": "【テスト投稿1】...",
      "scheduled_time": "2026-01-04T08:00:00+09:00",
      "status": "scheduled"
    },
    ...
  ]
}
```

---

## トラブルシューティング

### エラー1: Request URL検証失敗

**症状**: Slack AppでRequest URLを保存しようとすると「We had trouble connecting to your server」エラー

**原因**:
- Flaskサーバーが起動していない
- ngrok URLが間違っている
- ngrokが停止している

**対処**:
1. Flaskサーバーが起動しているか確認（`ps aux | grep flask`）
2. ngrokが起動しているか確認（`ps aux | grep ngrok`）
3. ngrok Forwarding URLが正しいか確認
4. ヘルスチェックが成功するか確認（`curl https://xxxx.ngrok-free.app/health`）

### エラー2: ボタンクリックしても反応しない

**症状**: Slackでボタンをクリックしてもメッセージが更新されない

**原因**:
- Flaskサーバーのログにエラーが出ている
- Slack署名検証に失敗している

**対処**:
1. Flaskサーバーのログを確認
2. SLACK_SIGNING_SECRETが正しいか確認
3. 署名検証を一時的に無効化してテスト（本番では非推奨）

### エラー3: 承認結果ファイルが生成されない

**症状**: `approval_result_*.json`が作成されない

**原因**:
- data/ディレクトリへの書き込み権限がない
- パスが間違っている

**対処**:
```bash
# 書き込み権限確認
ls -ld /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data

# 権限がない場合は付与
chmod 755 /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data
```

---

## 本番環境へのデプロイ（オプション）

ngrokは開発環境用のため、本番環境では以下のいずれかを推奨します：

### オプション1: Heroku（無料枠あり）

```bash
# Heroku CLI インストール
brew install heroku

# アプリ作成
heroku create sns-approval-server

# デプロイ
git push heroku main

# Request URLにHeroku URLを設定
https://sns-approval-server.herokuapp.com/slack/interactive
```

### オプション2: AWS Lambda + API Gateway

サーバーレスで実行、コスト効率が良い。設定はやや複雑。

### オプション3: VPS（さくらVPS、ConoHa等）

常時稼働サーバーが必要な場合。

---

## まとめ

✅ Slack Interactive Buttonsで**タップ数3→1に削減**
✅ ユーザー体験が大幅向上
✅ 誤操作が減少（ボタンが明確）

次のステップ:
- Phase 3の残りのスキル実装（generate-sns-posts）
- 自動投稿実装（LinkedIn/Facebook/X API）
- cronで定期実行設定

