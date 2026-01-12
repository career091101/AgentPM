# LinkedIn API認証情報 取得ガイド

## 手順1: LinkedIn Developerアプリ作成

1. https://www.linkedin.com/developers/apps にアクセス
2. 「Create app」ボタンをクリック
3. アプリ情報を入力：
   - **App name**: SNS Automation
   - **LinkedIn Page**: 自分の個人ページまたは会社ページを選択
   - **Privacy policy URL**: （任意、なければ空欄）
   - **App logo**: （任意）
4. 「Create app」をクリック

## 手順2: Productsを追加

1. 作成したアプリの「Products」タブをクリック
2. 「Share on LinkedIn」を探して「Request access」をクリック
3. 承認されるまで待機（通常は即座に承認）

## 手順3: OAuth 2.0設定

1. 「Auth」タブをクリック
2. **Client ID**と**Client Secret**をコピーして保存
3. 「OAuth 2.0 settings」セクションで：
   - **Authorized redirect URLs for your app**に以下を追加：
     ```
     http://localhost:8080/callback
     ```
   - 「Update」をクリック

## 手順4: Authorization Codeを取得

1. 以下のURLをブラウザで開く（{CLIENT_ID}を実際のClient IDに置き換え）：

```
https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri=http://localhost:8080/callback&scope=w_member_social
```

例：
```
https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=86abcdefgh123456&redirect_uri=http://localhost:8080/callback&scope=w_member_social
```

2. LinkedInにログインし、「Allow」をクリック
3. リダイレクト先のURLから`code`パラメータをコピー：

```
http://localhost:8080/callback?code=AQTABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789&state=
```

上記の場合、`code`は`AQTABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789`

## 手順5: Access Tokenを取得

ターミナルで以下のcurlコマンドを実行（{CODE}、{CLIENT_ID}、{CLIENT_SECRET}を実際の値に置き換え）：

```bash
curl -X POST https://www.linkedin.com/oauth/v2/accessToken \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "code={CODE}" \
  -d "client_id={CLIENT_ID}" \
  -d "client_secret={CLIENT_SECRET}" \
  -d "redirect_uri=http://localhost:8080/callback"
```

レスポンス例：
```json
{
  "access_token": "AQVABCDEFabcdefg1234567890...",
  "expires_in": 5184000,
  "scope": "w_member_social"
}
```

**Access Token**をコピーして保存。

## 手順6: Person URNを取得

ターミナルで以下のcurlコマンドを実行（{ACCESS_TOKEN}を実際の値に置き換え）：

```bash
curl -X GET https://api.linkedin.com/v2/userinfo \
  -H "Authorization: Bearer {ACCESS_TOKEN}"
```

レスポンス例：
```json
{
  "sub": "abc123xyz",
  "name": "Yuichi Tanaka",
  "email": "yuichi@example.com",
  "email_verified": true
}
```

**Person URN**は`sub`の値（例: `abc123xyz`）

## 手順7: 環境変数設定

```bash
export LINKEDIN_ACCESS_TOKEN="AQVABCDEFabcdefg1234567890..."
export LINKEDIN_PERSON_URN="abc123xyz"
```

## 確認

以下のコマンドで投稿テスト：

```bash
curl -X POST https://api.linkedin.com/v2/ugcPosts \
  -H "Authorization: Bearer $LINKEDIN_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -H "X-Restli-Protocol-Version: 2.0.0" \
  -d '{
    "author": "urn:li:person:'$LINKEDIN_PERSON_URN'",
    "lifecycleState": "PUBLISHED",
    "specificContent": {
      "com.linkedin.ugc.ShareContent": {
        "shareCommentary": {
          "text": "テスト投稿 - SNS自動化"
        },
        "shareMediaCategory": "NONE"
      }
    },
    "visibility": {
      "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
  }'
```

成功すれば、LinkedInに投稿が表示されます。

---

**有効期限**: Access Tokenは60日間有効です。期限切れ後は手順4-5を再実行してください。
