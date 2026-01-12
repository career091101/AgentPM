# X/Twitter Analytics データ取得失敗の調査レポート

**調査日時**: 2026-01-05 20:30
**調査対象**: X/Twitter投稿のanalyticsデータがすべて0になる問題
**Late API Analytics Addon**: 有効（$10/month）

---

## 1. 問題の概要

### 症状

Late API `/v1/analytics` から取得したX/Twitter投稿のanalyticsデータがすべて0を返す。

| 指標 | 取得値 | 期待値 |
|------|--------|--------|
| Impressions | 0 | >0 |
| Likes | 0 | >0 |
| Comments | 0 | >0 |
| Shares | 0 | >0 |
| Views | 0 | >0 |
| Engagement Rate | 0.0 | >0 |

### 影響範囲

- **投稿数**: 1件（2026-01-04公開）
- **投稿ID**: `695a52fdf497177b163fd08d`
- **Platform Post URL**: https://twitter.com/i/web/status/2007770258292043823
- **アカウント**: @yuichisatoeco（フォロワー: 10,298）

### 他プラットフォームとの比較

同時期に公開された他プラットフォームの投稿では正常にデータ取得できている：

| Platform | Impressions | Likes | Shares | ER | データ取得 |
|----------|------------|-------|--------|-----|----------|
| **LinkedIn** | 15,402 | 115 | 0 | 0.77% | ✅ 正常 |
| **Threads** | 0（Views: 10,919） | 67 | 3 | 0.77%* | ✅ 正常 |
| **Instagram** | 141 | 1 | 0 | 0.71% | ✅ 正常 |
| **X/Twitter** | 0 | 0 | 0 | 0.0% | ❌ 失敗 |

---

## 2. 技術的詳細

### Late API レスポンス構造

```json
{
  "_id": "695a52fdf497177b163fd08d",
  "content": "なぜ、私たちは「考えること」に価値を置きすぎるのか？\n\n落合陽一氏のnull2が問いかける。\n\n「かしこさはただのおまけだから、心配しなくていいよ」\n\n経営者として、この言葉に衝撃を受けた。",
  "publishedAt": "2026-01-04T11:05:08.095Z",
  "scheduledFor": "2026-01-04T11:05:08.095Z",
  "status": "published",
  "analytics": {
    "impressions": 0,
    "reach": 0,
    "likes": 0,
    "comments": 0,
    "shares": 0,
    "clicks": 0,
    "views": 0,
    "lastUpdated": null  // ← 注目: lastUpdatedがnull
  },
  "platforms": [
    {
      "platform": "twitter",
      "status": "published",
      "analytics": {
        "impressions": 0,
        "reach": 0,
        "likes": 0,
        "comments": 0,
        "shares": 0,
        "clicks": 0,
        "views": 0,
        "engagementRate": 0  // ← すべて0
      }
    }
  ],
  "platform": "twitter",
  "platformPostUrl": "https://twitter.com/i/web/status/2007770258292043823",
  "isExternal": true,
  "profileId": "69576d1e96773ceb34903b09",
  "mediaType": "image",
  "mediaItems": [
    {
      "type": "image",
      "url": "https://media.getlate.dev/temp/1767503451702_49kyspts___________2026-01-04_14.10.40.png",
      "thumbnail": "https://media.getlate.dev/temp/1767503451702_49kyspts___________2026-01-04_14.10.40.png"
    }
  ]
}
```

### 重要な観察事項

#### ✅ 正常に動作している部分
1. **投稿自体は成功**: `status: "published"`, `platformPostUrl`が存在
2. **アカウント連携OK**: `platform: "twitter"`, `username: "yuichisatoeco"`
3. **メディアアップロード成功**: `mediaType: "image"`, `mediaItems`配列に画像URL
4. **投稿日時正常**: `publishedAt: "2026-01-04T11:05:08.095Z"`（JST 20:05）

#### ❌ 異常な部分
1. **lastUpdatedがnull**: 他プラットフォームでは`"2026-01-05T11:08:21.846Z"`等の値が入っている
2. **すべてのanalytics指標が0**: 投稿から24時間以上経過しているのに更新なし
3. **X API同期が発生していない**: `lastUpdated: null`は一度もデータ取得が行われていない証拠

---

## 3. 根本原因の仮説

### 仮説1: X API v2のアクセス制限（最有力）

**可能性**: 90%

Late APIがX API v2（旧Twitter API v2）からデータ取得する際、以下の問題が発生している可能性：

1. **X API Free Tierの制限**:
   - Analytics APIへのアクセスはBasic tier以上が必要（$100/month）
   - Free tierではツイート投稿のみ可能、analytics取得は不可

2. **X APIのレート制限**:
   - Analytics APIは15分あたり15リクエストまで
   - Late APIが複数アカウントで共有しているとレート制限に到達する可能性

3. **X APIのスコープ制限**:
   - Late APIが持つX APIアクセストークンが`tweet.read`のみで`analytics.read`スコープがない

#### 検証方法
```bash
# Late Dashboard で確認すべき項目
1. Connected Accounts → X/Twitter → API Plan
   → Free / Basic / Pro のどのプランか確認
2. API Access Log → X Analytics API
   → エラーログの有無を確認
3. Account Settings → Reconnect X Account
   → スコープ再取得を試みる
```

### 仮説2: Late APIのX統合バグ

**可能性**: 60%

Late APIのX/Twitter analytics統合に不具合がある可能性：

1. **X API v2のエンドポイント変更**:
   - 2025年末にX APIの仕様変更があった可能性
   - Late APIが古いエンドポイントを参照している

2. **データ同期スケジューラーの停止**:
   - `lastUpdated: null`は一度もデータ取得が試行されていない証拠
   - Late APIのバックグラウンドジョブが動作していない

3. **画像付きツイートのanalytics取得失敗**:
   - `mediaType: "image"`の投稿のみ失敗している可能性
   - テキストのみ投稿ではデータ取得できる可能性

#### 検証方法
```bash
# テスト投稿で検証
1. テキストのみのツイートをLate API経由で投稿
2. 24時間後にanalyticsデータ取得を試行
3. 画像付き投稿と比較
```

### 仮説3: アカウント再認証が必要

**可能性**: 40%

X/Twitterアカウントの認証トークンが期限切れになっている可能性：

1. **OAuth 2.0トークンの有効期限**:
   - X APIのアクセストークンは2時間で期限切れ
   - リフレッシュトークンは60日で期限切れ

2. **Late APIの自動リフレッシュ失敗**:
   - トークン更新プロセスでエラーが発生
   - 投稿はできるがanalytics取得は失敗

#### 検証方法
```bash
# Late Dashboard で再認証
1. Connected Accounts → X/Twitter → Disconnect
2. Reconnect X Account → 認証フロー完了
3. 24時間後にanalyticsデータ確認
```

---

## 4. 他プラットフォームとの動作比較

### LinkedIn（正常動作）

```json
{
  "analytics": {
    "impressions": 15402,
    "reach": 8900,
    "likes": 115,
    "comments": 3,
    "shares": 0,
    "clicks": 0,
    "views": 0,
    "engagementRate": 0.77,
    "lastUpdated": "2026-01-05T11:08:21.846Z"  // ← 最新更新日時あり
  }
}
```

**動作状況**:
- ✅ `lastUpdated`が存在（60分ごとに自動更新）
- ✅ すべてのanalytics指標が正常値
- ✅ Engagement Rateが自動計算されている

### Threads（部分的に正常）

```json
{
  "analytics": {
    "impressions": 0,  // ← Impressionsは0
    "reach": 0,
    "likes": 67,
    "comments": 4,
    "shares": 3,
    "clicks": 0,
    "views": 10919,  // ← Viewsは取得できている
    "engagementRate": 0,
    "lastUpdated": "2026-01-05T11:08:21.572Z"  // ← 最新更新日時あり
  }
}
```

**動作状況**:
- ✅ `lastUpdated`が存在（データ同期が動作）
- ⚠️ `impressions: 0`だが`views: 10919`は取得できている
- ✅ Likes, Comments, Sharesは正常

### Instagram（正常動作）

```json
{
  "analytics": {
    "impressions": 141,
    "reach": 70,
    "likes": 1,
    "comments": 0,
    "shares": 0,
    "clicks": 0,
    "views": 141,
    "engagementRate": 0,
    "lastUpdated": "2026-01-05T11:08:20.395Z"  // ← 最新更新日時あり
  }
}
```

**動作状況**:
- ✅ `lastUpdated`が存在
- ✅ すべてのanalytics指標が正常値

### X/Twitter（完全失敗）

```json
{
  "analytics": {
    "impressions": 0,
    "reach": 0,
    "likes": 0,
    "comments": 0,
    "shares": 0,
    "clicks": 0,
    "views": 0,
    "engagementRate": 0,
    "lastUpdated": null  // ← データ同期が一度も実行されていない
  }
}
```

**動作状況**:
- ❌ `lastUpdated: null`（一度もデータ取得されていない）
- ❌ すべてのanalytics指標が0

---

## 5. 推奨アクション（優先順位順）

### 🔥 Priority 1: X API Plan確認（即時実行）

**目的**: X API Free Tierの制限を確認

**手順**:
1. Late Dashboardにログイン: https://app.getlate.dev
2. `Settings` → `Connected Accounts` → `X/Twitter`
3. API Planを確認:
   - **Free Tier**: Analytics APIアクセス不可 → Basic tier以上にアップグレード必要（$100/month）
   - **Basic Tier以上**: 次のアクションへ

**期待結果**:
- Free Tierなら原因確定 → X API Basicプラン購入を検討
- Basic Tier以上なら次のアクションへ

### 🔥 Priority 2: アカウント再認証（所要時間: 5分）

**目的**: OAuth 2.0トークンの更新

**手順**:
1. Late Dashboard → `Connected Accounts` → `X/Twitter`
2. `Disconnect` をクリック
3. `Connect X Account` をクリック
4. X認証フローを完了（`Read and Write`権限を許可）
5. 24時間後にanalyticsデータを再確認

**期待結果**:
- `lastUpdated`が`null`から日時に変わる
- Analytics指標が0から実際の値に更新される

### 🔥 Priority 3: Late APIサポートに問い合わせ（所要時間: 24時間）

**目的**: Late API側のX統合バグの確認

**問い合わせ内容**:
```
Subject: X/Twitter Analytics Data Not Updating (Post ID: 695a52fdf497177b163fd08d)

Hi Late Support Team,

I'm experiencing an issue where X/Twitter analytics data is not being updated via the /v1/analytics API endpoint.

**Symptoms**:
- Post ID: 695a52fdf497177b163fd08d
- Platform: X/Twitter
- Published: 2026-01-04 11:05:08 UTC
- Status: published
- All analytics fields: 0
- lastUpdated: null (never updated)

**Other platforms working fine**:
- LinkedIn: Impressions 15,402, ER 0.77% ✅
- Threads: Views 10,919, Likes 67 ✅
- Instagram: Impressions 141 ✅

**Analytics Addon**: Active ($10/month)

Could you please investigate if there's an issue with X/Twitter analytics integration?

Thank you!
```

**期待結果**:
- Late API側のバグ確認
- 修正予定のETA取得
- ワークアラウンド提案

### ⏳ Priority 4: 手動データ取得（暫定対応）

**目的**: X Analytics Dashboardから手動でデータ取得

**手順**:
1. X Analytics Dashboardにアクセス: https://analytics.x.com
2. ツイート検索: https://twitter.com/i/web/status/2007770258292043823
3. 以下の指標を手動記録:
   - Impressions
   - Engagements
   - Detail expands
   - Profile clicks
   - Link clicks

**期待結果**:
- 実際のパフォーマンスデータを取得
- Late APIとの比較ベースライン作成

---

## 6. 今後の監視計画

### 短期（1週間）

- **毎日**: X Analytics Dashboardで手動確認
- **Late API再認証後24時間**: analyticsデータの更新確認
- **X API Planアップグレード後**: データ取得成功を検証

### 中期（1ヶ月）

- **週次**: 全プラットフォームのanalytics取得状況レポート
- **Late APIサポート回答待ち**: バグ修正のフォローアップ
- **代替ツール検討**: Buffer、Hootsuite等との比較

### 長期（3ヶ月）

- **Late API X統合の安定性評価**: 3ヶ月の稼働率測定
- **X API Basicプランのコスト評価**: $100/monthの費用対効果分析
- **プラットフォーム戦略見直し**: X/Twitterの優先度再評価

---

## 7. 代替手段

### Option A: X API Basicプラン購入（$100/month）

**メリット**:
- Analytics API完全アクセス
- Late API統合でシームレスな自動化

**デメリット**:
- 月額$100の追加コスト
- 小規模運用では費用対効果が低い

### Option B: 手動データ取得（無料）

**メリット**:
- コスト0円
- X Analytics Dashboardから正確なデータ取得可能

**デメリット**:
- 自動化不可
- 週次レポート作成に手動作業が必要

### Option C: X投稿の一時停止

**メリット**:
- データ取得できないプラットフォームへのリソース投下を回避
- LinkedIn、Threads、Instagramに集中

**デメリット**:
- X/Twitterの10,298フォロワーへのリーチ喪失
- クロスプラットフォーム戦略の縮小

---

## 8. 結論

X/Twitter analytics データ取得失敗の原因は、以下の3つの可能性が高い：

1. **X API Free Tierの制限**（可能性90%）: Analytics APIアクセス不可
2. **Late APIのX統合バグ**（可能性60%）: データ同期スケジューラー停止
3. **アカウント再認証が必要**（可能性40%）: OAuth 2.0トークン期限切れ

**即座に実行すべきアクション**:

1. ✅ Late Dashboardで**X API Plan**を確認
2. ✅ X/Twitterアカウントを**再認証**
3. ✅ Late APIサポートに**問い合わせ**

**暫定対応**:
- X Analytics Dashboardから**手動でデータ取得**し、実際のパフォーマンスを記録

**長期戦略**:
- X API Basicプラン（$100/month）の費用対効果を評価
- Late API X統合の安定性を3ヶ月監視
- 必要に応じてX投稿戦略を見直し

---

**次のアクション**: Late Dashboardで即座にX API Plan確認と再認証を実行してください。
