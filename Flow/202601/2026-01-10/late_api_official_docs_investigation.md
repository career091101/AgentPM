# Late API アナリティクス取得方法調査レポート

**調査日**: 2026-01-10
**調査者**: Claude Code Agent
**調査目的**: Late APIの正しいアナリティクスデータ取得方法の特定

## 1. 公式ドキュメント確認結果

### ドキュメントURL
- **メインドキュメント**: https://docs.getlate.dev/
- **API Reference**: https://docs.getlate.dev/core/
- **料金プラン**: https://docs.getlate.dev/pricing

### 最終更新日
公式ドキュメントには明示的な最終更新日の記載なし。2026年時点で有効なドキュメント。

### ドキュメント構成
```
Late API Documentation
├── Getting Started
│   ├── Overview
│   ├── Authentication
│   └── Quickstart
├── API Reference
│   ├── Core
│   │   ├── Profiles
│   │   ├── Accounts
│   │   ├── Posts ← 投稿管理
│   │   ├── Analytics ← アナリティクス専用エンドポイント
│   │   ├── Webhooks
│   │   └── Logs
│   ├── Management
│   ├── Utilities
│   └── Tools
└── Pricing
```

---

## 2. 投稿データ取得エンドポイント (`/v1/posts`)

### 仕様詳細

**エンドポイント**:
```
GET https://getlate.dev/api/v1/posts
```

**認証**:
```http
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

### クエリパラメータ

| パラメータ | 型 | 説明 | 例 |
|-----------|-----|------|-----|
| `page` | integer | ページ番号（1-based） | `1` |
| `limit` | integer | ページサイズ（1-100、デフォルト10） | `50` |
| `status` | string | フィルター: draft, scheduled, published, failed | `published` |
| `platform` | string | プラットフォーム別フィルター | `twitter`, `linkedin` |
| `profileId` | string | プロフィール別フィルター | `profile_abc123` |
| `createdBy` | string | 作成者別フィルター | `user_xyz789` |
| `dateFrom` | date | 期間フィルター（開始日） | `2026-01-01` |
| `dateTo` | date | 期間フィルター（終了日） | `2026-01-10` |
| `includeHidden` | boolean | 非表示投稿含有 | `false` |

### レスポンス例

```json
{
  "posts": [
    {
      "_id": "65f1c0a9e2b5af0012ab34cd",
      "title": "Launch post",
      "content": "We just launched!",
      "status": "published",
      "scheduledFor": "2026-01-10T12:00:00Z",
      "platforms": [
        {
          "platform": "twitter",
          "platformPostUrl": "https://twitter.com/acme/status/123...",
          "status": "published"
        },
        {
          "platform": "linkedin",
          "platformPostUrl": "https://linkedin.com/posts/...",
          "status": "published"
        }
      ],
      "createdAt": "2026-01-09T10:00:00Z",
      "updatedAt": "2026-01-10T12:01:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 1,
    "pages": 1
  }
}
```

### 投稿ステータスの定義

| ステータス | 説明 |
|----------|------|
| `draft` | 下書き状態（未公開） |
| `scheduled` | スケジュール待機中（予約済み） |
| `published` | 公開済み（全プラットフォームで成功） |
| `failed` | 公開失敗（全プラットフォームで失敗） |
| `partial` | 一部プラットフォームで失敗 |

### 重要な制限

**`/v1/posts` エンドポイントではアナリティクスデータ（impressions, likes, shares等）は取得できません。**

アナリティクスデータは別途 `/v1/analytics` エンドポイントで取得する必要があります。

---

## 3. Analytics専用エンドポイント (`/v1/analytics`)

### 存在確認結果

**Yes** - Analytics専用エンドポイントが存在します。

**エンドポイント**:
```
GET https://getlate.dev/api/v1/analytics
```

### 必要なAddon

**Analytics Addon（有料）** - **必須**

| 項目 | 詳細 |
|------|------|
| **料金** | $1/social set/月 |
| **対象プラン** | Build, Accelerate, Unlimitedプランでのみ追加可能 |
| **Freeプラン** | Analytics Addonは利用不可 |

### リクエストパラメータ

| パラメータ | 型 | 説明 | 例 |
|-----------|-----|------|-----|
| `postId` | string | 単一投稿ID（LateまたはExternal） | `65f1c0a9e2b5af0012ab34cd` |
| `platform` | string | プラットフォーム指定（デフォルト"all"） | `twitter`, `linkedin` |
| `profileId` | string | プロフィールID指定（デフォルト"all"） | `profile_abc123` |
| `fromDate` | date | 範囲検索下限 | `2026-01-01` |
| `toDate` | date | 範囲検索上限 | `2026-01-10` |
| `limit` | integer | ページサイズ（1-100、デフォルト50） | `50` |
| `page` | integer | ページ番号（デフォルト1） | `1` |
| `sortBy` | string | ソート基準（"date"または"engagement"） | `engagement` |
| `order` | string | ソート順（"asc"または"desc"） | `desc` |

### レスポンスフィールド

#### 基本メトリクス（全プラットフォーム共通）

| フィールド | 説明 |
|----------|------|
| `impressions` | 投稿の表示回数（インプレッション） |
| `reach` | ユニークユーザーリーチ数 |
| `likes` | いいね数 |
| `comments` | コメント数 |
| `shares` | シェア数 |
| `clicks` | クリック数（プラットフォーム依存） |
| `views` | 動画再生回数（動画投稿のみ） |
| `engagementRate` | エンゲージメント率（%） |
| `lastUpdated` | 最終更新日時 |

#### レスポンス例

```json
{
  "postId": "65f1c0a9e2b5af0012ab34cd",
  "status": "published",
  "analytics": {
    "impressions": 15420,
    "reach": 12350,
    "likes": 342,
    "comments": 28,
    "shares": 14,
    "clicks": 235,
    "engagementRate": 2.78,
    "lastUpdated": "2026-01-10T14:00:00Z"
  },
  "platformBreakdown": [
    {
      "platform": "twitter",
      "impressions": 8420,
      "reach": 7100,
      "likes": 210,
      "engagementRate": 2.49
    },
    {
      "platform": "linkedin",
      "impressions": 7000,
      "reach": 5250,
      "likes": 132,
      "engagementRate": 1.88
    }
  ]
}
```

### プラットフォーム別制限

#### LinkedIn

| アカウントタイプ | 外部投稿対応 | 制限事項 |
|---------------|-----------|---------|
| **個人アカウント** | ✗ 非対応 | Late経由で公開した投稿のみ分析可能（LinkedIn API制限） |
| **企業アカウント** | ✓ 対応 | 外部投稿のアナリティクスも同期可能 |

#### Telegram

- **対応状況**: ✗ 非対応
- **理由**: Telegram Bot APIがメッセージビューカウントを提供していないため、プラットフォーム側の制限により取得不可

#### その他プラットフォーム

- **Twitter/X**: 完全対応
- **Instagram**: 完全対応
- **Facebook**: 完全対応
- **TikTok**: 完全対応
- **YouTube**: 完全対応（動画再生回数含む）
- **Pinterest**: 完全対応
- **Reddit**: 完全対応
- **Bluesky**: 完全対応
- **Threads**: 完全対応
- **Google Business**: 完全対応

### レート制限

- **APIリクエスト**: 制限なし（"There is no rate limit on API requests"）
- **キャッシュ更新**: 最大1時間に1回（"refreshed at most once per hour"）

**重要**: アナリティクスデータは1時間ごとにキャッシュされるため、リアルタイムデータは取得できません。最新データは最大60分遅延する可能性があります。

---

## 4. 正しいアナリティクス取得方法

### ステップバイステップ手順

#### 前提条件

1. **有料プランへのアップグレード** (Build以上)
2. **Analytics Addonの購入** ($1/social set/月)
3. **API Keyの取得** (https://getlate.dev/signup)

#### 手順1: 投稿データの取得

公開済み投稿を取得し、`postId` を特定します。

```python
import requests

# API Key設定
API_KEY = "your_api_key_here"
BASE_URL = "https://getlate.dev/api/v1"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 公開済み投稿を取得
response = requests.get(
    f"{BASE_URL}/posts",
    headers=headers,
    params={
        "status": "published",
        "dateFrom": "2026-01-01",
        "dateTo": "2026-01-10",
        "limit": 50
    }
)

posts = response.json()["posts"]
print(f"取得した投稿数: {len(posts)}")

# postIdリストを作成
post_ids = [post["_id"] for post in posts]
```

#### 手順2: 各投稿のアナリティクス取得

```python
analytics_data = []

for post_id in post_ids:
    # 単一投稿のアナリティクスを取得
    analytics_response = requests.get(
        f"{BASE_URL}/analytics",
        headers=headers,
        params={
            "postId": post_id
        }
    )

    if analytics_response.status_code == 200:
        analytics = analytics_response.json()
        analytics_data.append(analytics)
        print(f"Post {post_id}: {analytics['analytics']['impressions']} impressions")
    else:
        print(f"エラー: {analytics_response.status_code} - {analytics_response.text}")

print(f"\n合計アナリティクス取得数: {len(analytics_data)}")
```

#### 手順3: 期間指定での一括取得

```python
# 期間指定で一括取得（ページネーション対応）
all_analytics = []
page = 1

while True:
    response = requests.get(
        f"{BASE_URL}/analytics",
        headers=headers,
        params={
            "fromDate": "2026-01-01",
            "toDate": "2026-01-10",
            "platform": "all",  # または特定プラットフォーム
            "sortBy": "engagement",
            "order": "desc",
            "limit": 50,
            "page": page
        }
    )

    data = response.json()
    all_analytics.extend(data.get("analytics", []))

    # 次のページがあるか確認
    pagination = data.get("pagination", {})
    if page >= pagination.get("pages", 1):
        break

    page += 1

print(f"取得したアナリティクス総数: {len(all_analytics)}")
```

### 必要な認証情報

| 項目 | 取得方法 |
|------|---------|
| **API Key** | Late Dashboardで生成 (https://getlate.dev/signup) |
| **Authorization Header** | `Bearer YOUR_API_KEY` 形式 |

### サンプルコード（完全版）

```python
import requests
import json
from datetime import datetime, timedelta

class LateAnalytics:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://getlate.dev/api/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def get_published_posts(self, from_date, to_date, limit=50):
        """公開済み投稿を取得"""
        response = requests.get(
            f"{self.base_url}/posts",
            headers=self.headers,
            params={
                "status": "published",
                "dateFrom": from_date,
                "dateTo": to_date,
                "limit": limit
            }
        )
        response.raise_for_status()
        return response.json()["posts"]

    def get_post_analytics(self, post_id):
        """単一投稿のアナリティクスを取得"""
        response = requests.get(
            f"{self.base_url}/analytics",
            headers=self.headers,
            params={"postId": post_id}
        )
        response.raise_for_status()
        return response.json()

    def get_analytics_by_date_range(self, from_date, to_date, platform="all"):
        """期間指定でアナリティクスを一括取得"""
        all_analytics = []
        page = 1

        while True:
            response = requests.get(
                f"{self.base_url}/analytics",
                headers=self.headers,
                params={
                    "fromDate": from_date,
                    "toDate": to_date,
                    "platform": platform,
                    "sortBy": "engagement",
                    "order": "desc",
                    "limit": 50,
                    "page": page
                }
            )
            response.raise_for_status()

            data = response.json()
            all_analytics.extend(data.get("analytics", []))

            pagination = data.get("pagination", {})
            if page >= pagination.get("pages", 1):
                break

            page += 1

        return all_analytics

    def calculate_total_engagement(self, analytics_list):
        """合計エンゲージメントを計算"""
        total_impressions = sum(a["analytics"]["impressions"] for a in analytics_list)
        total_likes = sum(a["analytics"]["likes"] for a in analytics_list)
        total_comments = sum(a["analytics"]["comments"] for a in analytics_list)
        total_shares = sum(a["analytics"]["shares"] for a in analytics_list)

        return {
            "total_impressions": total_impressions,
            "total_likes": total_likes,
            "total_comments": total_comments,
            "total_shares": total_shares,
            "avg_engagement_rate": sum(a["analytics"]["engagementRate"] for a in analytics_list) / len(analytics_list)
        }

# 使用例
if __name__ == "__main__":
    # API Key設定
    API_KEY = "your_api_key_here"

    # LateAnalyticsインスタンス作成
    late = LateAnalytics(API_KEY)

    # 過去7日間のアナリティクスを取得
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    # 1. 投稿データ取得
    posts = late.get_published_posts(start_date, end_date)
    print(f"公開済み投稿数: {len(posts)}")

    # 2. 各投稿のアナリティクス取得
    analytics_list = []
    for post in posts:
        try:
            analytics = late.get_post_analytics(post["_id"])
            analytics_list.append(analytics)
            print(f"Post {post['_id']}: {analytics['analytics']['impressions']} impressions")
        except Exception as e:
            print(f"エラー: {e}")

    # 3. 合計エンゲージメント計算
    if analytics_list:
        totals = late.calculate_total_engagement(analytics_list)
        print("\n=== 合計エンゲージメント ===")
        print(json.dumps(totals, indent=2))

    # 4. 期間指定での一括取得
    all_analytics = late.get_analytics_by_date_range(start_date, end_date, platform="twitter")
    print(f"\nTwitterアナリティクス取得数: {len(all_analytics)}")
```

---

## 5. 推奨アプローチ

### Late API単独使用（推奨）

**メリット**:
- ✓ 統一されたインターフェース（12プラットフォーム対応）
- ✓ レート制限なし（アナリティクスAPIのみ）
- ✓ プラットフォームAPIの変更に対応不要
- ✓ 認証管理が単一API Keyで完結
- ✓ キャッシュによる高速レスポンス

**デメリット**:
- ✗ Analytics Addonが有料（$1/social set/月）
- ✗ データ更新が最大1時間遅延（キャッシュ制限）
- ✗ LinkedIn個人アカウントの外部投稿非対応
- ✗ Telegram非対応

**推奨シナリオ**:
1. 複数プラットフォームを統合管理したい
2. リアルタイム性より統一性を重視
3. プラットフォームAPIの複雑さを避けたい
4. 月額コストが許容範囲内（$1〜数十ドル）

### プラットフォームAPI併用（部分的併用）

**メリット**:
- ✓ リアルタイムデータ取得可能
- ✓ プラットフォーム固有の詳細メトリクス取得
- ✓ Telegram等のLate非対応プラットフォーム対応

**デメリット**:
- ✗ 各プラットフォームの認証管理が必要
- ✗ APIレート制限が厳しい（例: Twitter API v2 - 75 req/15min）
- ✗ API仕様変更への対応コストが高い
- ✗ データ形式が統一されていない

**推奨シナリオ**:
1. 特定プラットフォームでリアルタイムデータが必須
2. Late非対応プラットフォーム（Telegram等）を使用
3. プラットフォーム固有の高度なメトリクスが必要（例: Twitter APIのretweet_count詳細）

### ハイブリッドアプローチ（Late + プラットフォームAPI併用）

**実装パターン**:
```python
# Late APIでメインデータ取得（統一インターフェース）
late_analytics = late.get_analytics_by_date_range("2026-01-01", "2026-01-10")

# 特定プラットフォームでリアルタイムデータ補完
twitter_api = TwitterAPI(bearer_token)
for analytics in late_analytics:
    if analytics["platform"] == "twitter":
        # Late APIのデータ（1時間キャッシュ）
        late_impressions = analytics["analytics"]["impressions"]

        # Twitter APIでリアルタイムデータ取得（オプション）
        tweet_id = extract_tweet_id(analytics["platformPostUrl"])
        realtime_data = twitter_api.get_tweet_metrics(tweet_id)

        # データをマージ
        analytics["analytics"]["realtime_impressions"] = realtime_data["impressions"]
        analytics["analytics"]["delta"] = realtime_data["impressions"] - late_impressions
```

**推奨シナリオ**:
1. Late APIで統一管理しつつ、特定プラットフォームでリアルタイム補完
2. Telegram等のLate非対応プラットフォームを一部使用
3. コスト効率とデータ精度のバランスを取りたい

---

## 6. 結論

### 課題の根本原因

**現在のコード（Late API使用）の問題点**:

1. **`/v1/posts` エンドポイントではアナリティクスデータが取得できない**
   - `impressions`, `likes`, `shares` 等のフィールドは `/v1/posts` レスポンスに含まれていない
   - 投稿メタデータ（status, publishedAt, platformPostUrl）のみが取得可能

2. **Analytics Addonが必要**
   - Freeプランではアナリティクスデータが一切取得できない
   - Build以上のプラン + Analytics Addon ($1/social set/月) が必須

3. **`/v1/analytics` エンドポイントの使用が必須**
   - アナリティクスデータは `/v1/analytics` 専用エンドポイントでのみ取得可能
   - `postId` を指定した単一投稿取得、または期間指定での一括取得が必要

### 修正方法

#### 方法1: Late API Analytics エンドポイントの正しい使用（推奨）

**ステップ**:
1. **有料プランへアップグレード** (Build: $19/月 以上)
2. **Analytics Addon購入** ($1/social set/月)
3. **コード修正**:
   - `/v1/posts` → 公開済み投稿の `postId` 取得専用
   - `/v1/analytics` → アナリティクスデータ取得専用

**修正後のコード構造**:
```python
# STEP 1: 公開済み投稿を取得（postId特定）
posts = late_api.get("/v1/posts", params={"status": "published"})

# STEP 2: 各投稿のアナリティクスを取得
for post in posts:
    analytics = late_api.get("/v1/analytics", params={"postId": post["_id"]})
    # impressions, likes, shares等を取得
```

**コスト**:
- Build プラン: $19/月
- Analytics Addon: $1/social set/月
- **合計**: $20〜30/月（プラットフォーム数による）

#### 方法2: プラットフォームAPI直接使用（Late非使用）

**対象プラットフォームとAPI**:
- **Twitter/X**: Twitter API v2 (https://developer.twitter.com/en/docs/twitter-api)
- **LinkedIn**: LinkedIn API (https://learn.microsoft.com/en-us/linkedin/marketing/)
- **Instagram**: Instagram Graph API (https://developers.facebook.com/docs/instagram-api/)
- **Threads**: Threads API (2026年1月時点で公式API提供中)

**メリット**:
- リアルタイムデータ取得
- Late APIの料金が不要（プラットフォームAPI自体は無料〜安価）

**デメリット**:
- 各プラットフォームの認証管理が複雑
- APIレート制限が厳しい（例: Twitter v2 - 75 req/15min）
- API仕様変更への対応コストが高い

#### 方法3: ハイブリッド（Late + プラットフォームAPI併用）

**実装**:
- Late API: 統一インターフェースでメインデータ取得（統計・レポート用）
- プラットフォームAPI: 特定プラットフォームでリアルタイムデータ補完

**推奨度**:
- ⭐⭐⭐⭐⭐ **方法1（Late API Analytics）**: コスト効率と実装容易性のバランスが最良
- ⭐⭐⭐ **方法3（ハイブリッド）**: リアルタイム性が必須の場合
- ⭐⭐ **方法2（プラットフォームAPI直接）**: Late APIコストを避けたい場合のみ

### 最終推奨

**Late API Analytics エンドポイント (`/v1/analytics`) を使用する方法1を推奨します。**

**理由**:
1. 統一されたインターフェースで12プラットフォーム対応
2. プラットフォームAPI変更への対応不要
3. レート制限なし（アナリティクスAPIのみ）
4. 実装が単純明快
5. 月額$20〜30は許容範囲内（複数プラットフォーム管理の対価として）

**次のステップ**:
1. Late Dashboard (https://getlate.dev/signup) でアカウント作成
2. Buildプラン以上にアップグレード
3. Analytics Addonを購入
4. API Keyを生成
5. 本レポートの「4. 正しいアナリティクス取得方法」のサンプルコードを実装

---

## 参照資料

### 公式ドキュメント
- [Late API Documentation](https://docs.getlate.dev/)
- [Posts API Reference](https://docs.getlate.dev/core/posts)
- [Analytics API Reference](https://docs.getlate.dev/core/analytics)
- [Pricing](https://docs.getlate.dev/pricing)
- [Quickstart Guide](https://docs.getlate.dev/quickstart)

### 関連リソース
- [Late API Main Site](https://getlate.dev)
- [Late API Dashboard](https://getlate.dev/signup)

---

**レポート終了**
