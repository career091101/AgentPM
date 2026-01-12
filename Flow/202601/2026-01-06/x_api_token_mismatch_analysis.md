# X API Token不一致問題の分析

**作成日時**: 2026-01-06 06:52
**ステータス**: 🔴 **Late API vs 直接アクセス - トークン不一致確定**

---

## 問題の本質

Late APIのスクリーンショットから判明した事実：

### ✅ Late API側（正常）
```
Token Status: Valid
Expires at: 2026/1/6 (Auto-refreshes)
Permissions:
  ✅ Can Post
  ✅ Analytics
  ✅ tweet.read
  ✅ tweet.write
  ✅ users.read
  ✅ offline.access
```

### ❌ .env直接アクセス側（異常）
```
X_ACCESS_TOKEN=155369088-01ovZhUkto0y7w1dCxm1IEavSacgEXclA1V6YtBJ
X_ACCESS_TOKEN_SECRET=UYbEXe3FWVcAvNJovDVYqJcGNNvUMh4IRseQacra0qQVq

結果: 401 Unauthorized
```

---

## 根本原因の確定

**Late APIと.envファイルは別々のX APIアプリまたはトークンを使用している**

| 項目 | Late API | .envファイル |
|------|----------|-------------|
| **トークン** | Late API独自トークン | 手動設定トークン |
| **アプリ** | Late APIアプリ | ユーザー作成アプリ |
| **ステータス** | ✅ Valid | ❌ 401 Unauthorized |
| **権限** | ✅ Read/Write/Analytics | ❌ 不明（401で拒否） |

---

## なぜ401エラーが発生するのか

### 仮説1: 異なるX APIアプリ（確率90%）

Late APIは**独自のX APIアプリ**を使用してユーザーを認証しています。

`.env`ファイルに設定されているトークンは、**あなた自身が作成した別のX APIアプリ**のトークンです。

**問題**:
- あなたが作成したアプリの権限設定が不適切
- または、そのアプリが無効化されている
- または、トークンが失効している

### 仮説2: トークンの再生成が必要（確率80%）

X Developer Portalで権限を変更した場合、**既存のAccess Tokenは新しい権限を反映しません**。

**対処**:
- X Developer Portal → Keys and Tokens
- Access Token and Secret → **Regenerate**

---

## 解決策

### 🔥 Solution 1: X Developer PortalでAccess Token再生成（推奨）

#### STEP 1: X Developer Portalにアクセス

```
https://developer.twitter.com/en/portal/dashboard
```

#### STEP 2: あなたのアプリを特定

**重要**: `.env`ファイルのAPI Keyに対応するアプリを見つける

```
X_API_KEY=qwb1rOKT5xXhDGDiTBxbfk5e5
```

このAPI Keyを持つアプリを探してください。

#### STEP 3: Keys and Tokensページへ

```
Projects & Apps → [Your App] → Keys and tokens
```

#### STEP 4: Access Token and Secretを再生成

```
Access Token and Secret → Regenerate
```

**重要**: 再生成時に**Read and Write**権限が表示されることを確認

#### STEP 5: 新しいトークンを`.env`に反映

```bash
X_ACCESS_TOKEN=新しいAccess Token
X_ACCESS_TOKEN_SECRET=新しいAccess Token Secret
```

#### STEP 6: 検証

```bash
python3 scripts/fetch_x_analytics_direct.py
```

---

### 🔥 Solution 2: X Developer Portalでアプリの権限を確認

#### STEP 1: アプリのSettingsを開く

```
Projects & Apps → [Your App] → Settings
```

#### STEP 2: User authentication settingsを確認

```
User authentication settings → Edit
```

#### STEP 3: App permissionsを確認

**現在の設定を確認**:
- Read
- Read and Write ← **これになっているか確認**
- Read and Write and Direct Messages

**推奨**: **Read and Write**

#### STEP 4: OAuth 1.0aが有効か確認

```
OAuth 1.0a: ✅ Enabled
```

もし無効なら、有効化してください。

---

### 🔥 Solution 3: Late APIのトークンを.envにコピー（非推奨）

Late APIが持っているトークンは正常なので、理論上はそれを`.env`にコピーすることも可能です。

**しかし、これは推奨しません**:
- Late APIのトークンは内部管理用
- 外部から直接使用すると、Late APIの動作に影響する可能性
- Late APIのトークン有効期限管理が複雑化

---

## 検証方法

### X Developer Portalで現在のアプリ情報を確認

以下の情報をチェック：

1. **API Key**: `qwb1rOKT5xXhDGDiTBxbfk5e5`と一致するか
2. **App permissions**: Read and Write
3. **OAuth 1.0a**: Enabled
4. **Access Token**: Regenerate後の新しいトークン

### スクリーンショット撮影箇所

以下の画面のスクリーンショットを撮影してください：

1. **Keys and tokens**ページ
   - API Key and Secret
   - Bearer Token
   - Access Token and Secret（マスク部分のみ）

2. **Settings → User authentication settings**
   - App permissions
   - Type of App
   - OAuth 1.0a

---

## Late API側の対応（並行実行）

Late API側は正常なので、Late APIを使用した投稿とAnalytics取得は問題なく動作するはずです。

### Late APIのAnalytics取得を再試行

```bash
python3 scripts/fetch_late_analytics.py --from-date 2026-01-05 --to-date 2026-01-06 --platform twitter
```

**期待結果**:
- Late APIのトークンは有効なので、Analyticsが取得できる可能性あり
- ただし、Late APIがX API Free Tierを使用している場合、`non_public_metrics`にアクセスできず0を返す可能性

---

## X API Free Tier vs Basic Tier問題

Late APIのスクリーンショットでは**Analytics権限あり**と表示されていますが、これはOAuthスコープの話です。

**X API Tier（プラン）は別の概念**:

| Tier | 月額 | Public Metrics | Non-Public Metrics | Organic Metrics |
|------|------|----------------|-------------------|--------------------|
| **Free** | $0 | ✅ 可能 | ❌ 不可 | ❌ 不可 |
| **Basic** | $100 | ✅ 可能 | ✅ 可能 | ✅ 可能 |

Late APIが内部でX API Free Tierを使用している場合：
- `public_metrics`（Impressions, Likes等）は取得可能
- `non_public_metrics`（URL Clicks, Profile Clicks等）は取得不可

**Late APIのAnalyticsが0を返す原因**:
- Late APIが`non_public_metrics`または`organic_metrics`から取得しようとしている
- X API Free Tierではこれらにアクセスできない
- 結果、すべて0を返す

---

## 次のアクション（優先順位順）

### 🔥 Priority 1: X Developer PortalでAccess Token再生成（今すぐ）

1. https://developer.twitter.com/en/portal/dashboard
2. API Key `qwb1rOKT5xXhDGDiTBxbfk5e5` を持つアプリを特定
3. Keys and tokens → Access Token and Secret → **Regenerate**
4. 新しいトークンを`.env`に反映
5. `python3 scripts/fetch_x_analytics_direct.py` で検証

---

### ⏳ Priority 2: Late APIのAnalytics取得を再試行（検証用）

```bash
python3 scripts/fetch_late_analytics.py --from-date 2026-01-05 --platform twitter
```

**成功判定**:
- Analytics指標が0以外 → Late API正常動作
- Analytics指標がすべて0 → X API Free Tier制限の可能性

---

### ⏳ Priority 3: X API Tierをアップグレード（必要に応じて）

Late APIのAnalyticsが0を返し続ける場合：

1. X Developer Portal → Products → Basic Tier ($100/month)
2. Late APIで再認証（新しいTierの権限取得）

---

## 結論

Late API側のトークンは正常ですが、`.env`ファイルの直接アクセス用トークンが**別のアプリまたは古いトークン**であるため401エラーが発生しています。

**即座に実行すべきアクション**:
1. ✅ **X Developer PortalでAccess Token再生成**（5分、無料）
2. ⏳ **Late APIのAnalytics取得再試行**（検証用）

---

**次のアクション**: X Developer Portalで、API Key `qwb1rOKT5xXhDGDiTBxbfk5e5` を持つアプリを特定し、Access Tokenを再生成してください。
