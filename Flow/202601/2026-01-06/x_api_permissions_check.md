# X API Permissions チェック

**作成日時**: 2026-01-06 06:30
**ステータス**: 🔴 **401 Unauthorized継続中 - 権限設定要確認**

---

## 現在の状況

### ✅ 成功している部分
```
✅ OAuth 1.0a認証成功
✅ ユーザー情報取得成功（User ID, Username, Followers）
```

### ❌ 失敗している部分
```
❌ ツイート取得: 401 Unauthorized
❌ 詳細Analytics: スキップ（ツイートID取得不可）
```

---

## 根本原因の推定

**認証は成功しているが、ツイート取得で401エラー**

これは、X APIアプリの**Permissions（権限）設定が不適切**であることを示しています。

### X API Permissions構造

| Permission Level | 取得可能なデータ |
|-----------------|----------------|
| **Read** | ユーザー情報、公開ツイート |
| **Read and Write** | Read + 投稿・削除 |
| **Read and Write and Direct Messages** | Read and Write + DM |

### 現在の問題

- `GET /2/users/me` → ✅ 成功（Read権限で可能）
- `GET /2/users/{id}/tweets` → ❌ 401（**Read権限が正しく設定されていない可能性**）

---

## 即座に確認すべき項目

### STEP 1: X Developer Portalで権限確認

1. **X Developer Portalにアクセス**:
   ```
   https://developer.twitter.com/en/portal/dashboard
   ```

2. **Projects & Apps → [Your App] → Settings**

3. **User authentication settings → Edit**

4. **App permissions**を確認:
   ```
   ✅ Read (必須)
   ✅ Write（投稿が必要な場合）
   ❌ Direct Messages（不要ならOFF）
   ```

5. **Type of App**を確認:
   ```
   推奨: Web App, Automated App or Bot, または Native App
   ```

---

### STEP 2: 権限変更後のトークン再生成

**重要**: 権限を変更した場合、**Access TokenとAccess Token Secretを再生成**しないと反映されません。

1. **Keys and Tokens → Access Token and Secret → Regenerate**

2. **新しいトークンを`.env`に反映**:
   ```bash
   X_ACCESS_TOKEN=新しいAccess Token
   X_ACCESS_TOKEN_SECRET=新しいAccess Token Secret
   ```

3. **再度スクリプト実行**:
   ```bash
   python3 scripts/fetch_x_analytics_direct.py
   ```

---

### STEP 3: OAuth 1.0a vs OAuth 2.0確認

X API v2では、OAuth 2.0も利用可能ですが、今回はOAuth 1.0aを使用しています。

**OAuth 1.0aの制約**:
- Access TokenとAccess Token Secretが必要
- アプリ権限がユーザー権限を上書きする
- 権限変更後はトークン再生成必須

**確認項目**:
- アプリが**OAuth 1.0aをサポート**しているか
- User authentication settingsで**OAuth 1.0a**が有効か

---

## 代替案: Bearer Tokenでの検証

Bearer Tokenは**アプリレベルの認証**で、ユーザー情報の取得には使えませんが、公開ツイートの取得には使用可能です。

### Bearer Tokenテスト

```bash
curl -X GET "https://api.twitter.com/2/tweets/2007770258292043823?tweet.fields=public_metrics" \
  -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAKpPxwEAAAAAooKTZz%2BbM9UK%2FDDmybs1SCXC%2BLo%3Dp8qU9gdAy3QOF7MOd6TK2lFr0vbIdhdTZ9oFy31uegAsm4S2tv"
```

**期待結果**:
- ✅ 200 OK + ツイートデータ → Bearer Tokenは有効
- ❌ 401 Unauthorized → Bearer Tokenも無効

---

## 次のアクション（優先順位順）

### 🔥 Priority 1: X Developer Portal権限確認（今すぐ実行）

1. https://developer.twitter.com/en/portal/dashboard にアクセス
2. Projects & Apps → [Your App] → Settings
3. User authentication settings → Edit
4. **App permissions**: Read and Write に設定
5. **Type of App**: Web App, Automated App or Bot に設定
6. 保存後、Keys and Tokens → **Access Token再生成**

---

### 🔥 Priority 2: Bearer Tokenテスト（検証用）

```bash
cd Stock/programs/副業/projects/SNS

curl -X GET "https://api.twitter.com/2/tweets/2007770258292043823?tweet.fields=public_metrics" \
  -H "Authorization: Bearer $(grep X_BEARER_TOKEN .env | cut -d= -f2)"
```

**成功**: Bearer Tokenは有効 → OAuth 1.0aのAccess Token問題に絞られる
**失敗**: すべての認証が無効 → アプリ全体の再作成が必要

---

### ⏳ Priority 3: Late API再認証（並行実行）

X API直接アクセス修正と並行して、Late API再認証も実行してください。

1. https://app.getlate.dev
2. Settings → Connected Accounts → X/Twitter
3. Disconnect → Reconnect
4. **Read, Write, Analytics権限をすべて許可**

---

## トラブルシューティング

### Q1: 権限を変更したのに401が解消しない

**A**: Access TokenとAccess Token Secretを**再生成**しましたか？

権限変更後、**既存のトークンでは新しい権限が反映されません**。必ずRegenerateしてください。

---

### Q2: Bearer Tokenも401エラーになる

**A**: アプリ自体が無効化されている可能性があります。

X Developer Portalで以下を確認：
- App Status: Active
- API Key and Secret: Valid
- Project Status: Active

すべて無効な場合、**新しいアプリを作成**する必要があります。

---

### Q3: Late API再認証後もデータ取得できない

**A**: X API Tier（Free vs Basic）の問題の可能性があります。

Late APIは`non_public_metrics`または`organic_metrics`を使用している可能性があり、Free Tierではアクセスできません。

**解決策**:
- X API Basic Tier購入（$100/month）
- または手動データ収集（X Analytics Dashboard）

---

## 参照

- X API v2 Authentication: https://developer.twitter.com/en/docs/authentication/oauth-1-0a
- X API Permissions: https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens
- Late API Support: support@getlate.dev

---

**次のアクション**: 今すぐX Developer Portalで権限設定を確認し、Access Tokenを再生成してください。
