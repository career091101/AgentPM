# X (Twitter) API認証情報 取得ガイド

## 手順1: X Developer Portalにアクセス

1. https://developer.twitter.com/en/portal/dashboard にアクセス
2. Xアカウントでログイン
3. 「Sign up for Free Account」（初回のみ）

## 手順2: Projectを作成

1. 「Projects & Apps」→「Overview」をクリック
2. 「+ Create Project」をクリック
3. プロジェクト情報を入力：

### Project Name
```
SNS Automation
```

### Use Case
```
Making a bot
```

### Project Description
```
Automated posting bot for LinkedIn, Facebook, and X (Twitter)
```

4. 「Next」をクリック

## 手順3: Appを作成

1. **App name**を入力：
```
SNS Automation Bot
```

2. 「Complete」をクリック

3. **重要**: この画面で表示される**API Key**と**API Secret**をコピーして保存
   - API Key: `abcdefghijklmnopqrstuvwx`
   - API Secret: `1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN`
   - **この画面は1回しか表示されません！**

4. 「App settings」をクリック

## 手順4: User Authentication Settingsを設定

1. 「Settings」タブをクリック
2. 「User authentication settings」セクションで「Set up」をクリック
3. 設定を入力：

### App permissions
```
☑ Read and write
```

### Type of App
```
☑ Web App, Automated App or Bot
```

### App info

**Callback URI / Redirect URL**:
```
http://localhost:8080/callback
```

**Website URL**:
```
https://example.com
```
（任意、なければダミーURLでOK）

4. 「Save」をクリック

## 手順5: Keys and Tokensを取得

1. 「Keys and tokens」タブをクリック
2. **API Key and Secret**セクション：
   - すでに手順3で取得済み
   - 紛失した場合は「Regenerate」で再発行

3. **Bearer Token**セクション：
   - 「Generate」をクリック
   - Bearer Tokenをコピーして保存：
     ```
     AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
     ```

4. **Access Token and Secret**セクション：
   - 「Generate」をクリック
   - Access TokenとAccess Token Secretをコピーして保存：
     - Access Token: `123456789-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk`
     - Access Token Secret: `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO`

## 手順6: 環境変数設定

```bash
export X_BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
export X_API_KEY="abcdefghijklmnopqrstuvwx"
export X_API_SECRET="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN"
export X_ACCESS_TOKEN="123456789-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk"
export X_ACCESS_TOKEN_SECRET="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO"
```

## 手順7: 動作確認（Python）

```python
import tweepy

# 認証
client = tweepy.Client(
    bearer_token=os.environ.get("X_BEARER_TOKEN"),
    consumer_key=os.environ.get("X_API_KEY"),
    consumer_secret=os.environ.get("X_API_SECRET"),
    access_token=os.environ.get("X_ACCESS_TOKEN"),
    access_token_secret=os.environ.get("X_ACCESS_TOKEN_SECRET")
)

# テスト投稿
response = client.create_tweet(text="テスト投稿 - SNS自動化")
print(f"投稿成功: https://x.com/i/web/status/{response.data['id']}")
```

## トラブルシューティング

### エラー: 403 Forbidden

**原因**: App permissionsが「Read only」になっている

**対処法**:
1. User authentication settingsで「Read and write」を選択
2. Access TokenとSecretを再生成

### エラー: 401 Unauthorized

**原因**: 認証情報が間違っている

**対処法**:
1. 環境変数が正しく設定されているか確認
2. Access TokenとSecretを再生成

### Bearer Tokenが表示されない

**対処法**:
1. ProjectとAppが正しく作成されているか確認
2. X Developer Portalのダッシュボードをリロード

---

## 重要な注意事項

1. **API Keyと API Secretは再発行すると古いものは無効になります**
2. **Access TokenとSecretも再発行すると古いものは無効になります**
3. **Bearer Tokenは再発行可能ですが、古いものは無効になります**
4. **全ての認証情報を安全に保管してください（.envファイル推奨）**

---

## .env ファイル例

```bash
# Slack
SLACK_WEBHOOK_URL="https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXX"

# LinkedIn
LINKEDIN_ACCESS_TOKEN="AQVABCDEFabcdefg1234567890..."
LINKEDIN_PERSON_URN="abc123xyz"

# X (Twitter)
X_BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
X_API_KEY="abcdefghijklmnopqrstuvwx"
X_API_SECRET="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN"
X_ACCESS_TOKEN="123456789-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijk"
X_ACCESS_TOKEN_SECRET="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO"
```

読み込み方法：
```bash
source .env
```
