# X API Elevated Access確認ガイド

**作成日時**: 2026-01-06 06:57
**ステータス**: 🔴 **401継続中 - Elevated Access要確認**

---

## 現在の状況

### ✅ 成功している部分
```
✅ OAuth 1.0a認証成功
✅ ユーザー情報取得成功（GET /2/users/me）
```

### ❌ 失敗している部分
```
❌ ツイート取得失敗（GET /2/users/{id}/tweets）
   エラー: 401 Unauthorized
```

---

## 原因の可能性

### 可能性1: Elevated Access未申請（確率80%）

X API v2では、一部のエンドポイントに**Elevated Access**が必要です。

| Access Level | 利用可能エンドポイント |
|--------------|---------------------|
| **Essential** | `/2/users/me`（基本ユーザー情報） |
| **Elevated** | `/2/users/:id/tweets`（ユーザーのツイート取得） |

**現在の状況**:
- `/2/users/me` → ✅ 成功（Essential Accessで可能）
- `/2/users/:id/tweets` → ❌ 401（**Elevated Access必要**）

---

### 可能性2: App-only AuthenticationとUser Context Authenticationの混在

X API v2には2種類の認証があります：

| 認証タイプ | 用途 | 取得可能データ |
|-----------|------|--------------|
| **App-only** (Bearer Token) | 公開データアクセス | 公開ツイート、ユーザー情報 |
| **User Context** (OAuth 1.0a/2.0) | ユーザー固有データアクセス | 自分のツイート、Analytics |

**現在の問題**:
- OAuth 1.0aを使用しているが、アプリが**User Context Authentication**を正しくサポートしていない可能性

---

## 確認すべき項目

### 🔥 確認1: X Developer PortalでAccess Level確認

#### STEP 1: Portalにアクセス

```
https://developer.twitter.com/en/portal/dashboard
```

#### STEP 2: プロジェクトのAccess Levelを確認

```
Projects & Apps → [Your Project] → Settings
```

**Access Level**を確認：
- **Essential** (デフォルト、制限あり)
- **Elevated** (申請必要、より多くのエンドポイントにアクセス可能)

#### STEP 3: ElevatedでないならApply for Elevated

```
Projects & Apps → [Your Project] → Apply for Elevated
```

**申請内容**:
- アプリの用途説明（自社SNS分析ツール等）
- 取得したいデータの説明
- プライバシー保護の説明

**審査時間**: 通常1-2営業日

---

### 🔥 確認2: User authentication settingsの詳細確認

#### STEP 1: User authentication settingsを開く

```
Projects & Apps → [Your App] → Settings → User authentication settings → Edit
```

#### STEP 2: 以下を確認

**App permissions**:
```
✅ Read and Write
```

**Type of App**:
```
推奨: Web App, Automated App or Bot
```

**OAuth 1.0a**:
```
✅ Enabled
```

**Callback URLs**:
```
http://127.0.0.1（ローカル開発用）
または
https://your-domain.com/callback
```

**Website URL**:
```
必須: https://your-website.com
```

---

### 🔥 確認3: OAuth 2.0への切り替え検討

OAuth 1.0aは複雑で、設定ミスが起きやすいです。

X API v2では**OAuth 2.0 with PKCE**がより簡単で推奨されています。

#### OAuth 2.0のメリット
- シンプルな実装
- より明確なエラーメッセージ
- Refresh Token自動更新

#### OAuth 1.0aの問題
- 4つの認証情報が必要（API Key, API Secret, Access Token, Access Token Secret）
- 署名生成が複雑
- 権限設定のミスに気づきにくい

---

## 代替アプローチ: Bearer Tokenで十分なケース

もし目的が**公開ツイートのAnalytics取得のみ**なら、Bearer Tokenで十分です。

### Bearer Tokenで取得可能なデータ

```python
# Bearer Tokenで公開ツイートのAnalyticsを取得
response = requests.get(
    f"https://api.twitter.com/2/tweets/{tweet_id}",
    headers={"Authorization": f"Bearer {BEARER_TOKEN}"},
    params={"tweet.fields": "public_metrics"}
)

# 取得可能なデータ
{
  "impression_count": 37109,
  "like_count": 169,
  "retweet_count": 18,
  "reply_count": 2,
  "quote_count": 0,
  "bookmark_count": 57
}
```

**制約**:
- 自分のツイートリストは取得できない（ツイートIDを手動指定）
- Non-public metricsは取得不可

---

## 推奨される次のステップ

### 🔥 Option 1: Elevated Access申請（推奨、1-2日）

**メリット**:
- `/2/users/:id/tweets`エンドポイントにアクセス可能
- 自分のツイートリストを自動取得
- Free Tierでも多くの機能が使用可能

**デメリット**:
- 審査に1-2営業日かかる

**手順**:
1. https://developer.twitter.com/en/portal/dashboard
2. Projects & Apps → [Your Project] → Apply for Elevated
3. フォームに記入（英語）
   - Use case: Social media analytics for business
   - Data usage: Retrieve my own tweet metrics for performance analysis
   - Privacy: No personal data of other users will be collected
4. Submit

---

### 🔥 Option 2: Bearer Token暫定ソリューション（即座、無料）

Elevated Access申請中の間、Bearer Tokenを使用してAnalyticsを取得します。

**実装済みスクリプト**:
```bash
python3 scripts/fetch_x_analytics_bearer.py
```

**機能**:
- Bearer TokenでPublic Metrics取得
- ツイートIDは手動指定（Late APIから取得可能）

---

### 🔥 Option 3: Late API経由でAnalytics取得（検証用）

Late APIは独自のトークンを持っており、それは正常動作しています。

**Late APIを信頼してAnalytics取得**:
```bash
python3 scripts/fetch_late_analytics.py --from-date 2026-01-05 --platform twitter
```

**もし0を返す場合**:
- Late APIがX API Free Tierを使用している
- Free Tierではnon_public_metricsにアクセスできない
- Late APIのバグまたは仕様

---

## トラブルシューティング

### Q1: Elevated Access申請が却下された

**A**: 以下を明確に説明してください：
- アプリが自分のツイートAnalyticsのみを取得する
- 他のユーザーのデータは収集しない
- ビジネス目的（SNSパフォーマンス分析）

### Q2: Elevated Accessがあっても401が出る

**A**: User authentication settingsを再確認：
- Callback URLsが正しく設定されているか
- Website URLが設定されているか
- OAuth 1.0aが有効か

### Q3: どのくらい待てば結果が出るか

**A**: X APIのAccess Level申請は通常24-48時間以内に結果が出ます。

---

## まとめ

**現在の問題**: X APIアプリが**Essential Access**のため、`/2/users/:id/tweets`エンドポイントにアクセスできない。

**即座の解決策**:
1. ✅ **Elevated Access申請**（1-2日、推奨）
2. ✅ **Bearer Token暫定ソリューション**（即座、実装済み）
3. ✅ **Late API経由でAnalytics取得**（検証用）

**次のアクション**: X Developer Portalで現在のAccess Levelを確認し、Essentialなら**Elevated Access申請**を実施してください。
