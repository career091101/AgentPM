# Late API Analytics取得方法の解決策

**作成日時**: 2026-01-05 19:30:00
**調査結果**: Late APIには専用の`/v1/analytics`エンドポイントが存在

---

## 🔍 問題の原因

### 誤ったエンドポイント使用

**現在の実装**:
```python
# ❌ 誤り: /v1/posts エンドポイントを使用
response = requests.get(f"{base_url}/posts", headers=headers, timeout=30)
```

**問題点**:
- `/v1/posts`エンドポイントは投稿のメタデータのみを返す
- `analytics`オブジェクトは含まれるが、すべてのフィールドが`0`
- エンゲージメントデータを取得するには**専用の`/v1/analytics`エンドポイント**が必要

---

## ✅ 正しい実装方法

### STEP 1: Analytics APIエンドポイントの使用

```python
# ✅ 正しい: /v1/analytics エンドポイントを使用
response = requests.get(
    f"{base_url}/analytics",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    params={
        "platform": "linkedin",      # LinkedInのみフィルタ
        "fromDate": "2026-01-04",    # 開始日
        "toDate": "2026-01-05",      # 終了日
        "sortBy": "date",            # 日付順
        "order": "desc",             # 降順
        "limit": 100                 # 最大100件
    },
    timeout=30
)

analytics_data = response.json()
```

### STEP 2: 単一投稿の詳細Analytics取得

```python
# 特定投稿IDのAnalyticsを取得
post_id = "695a540ef497177b163fd7be"

response = requests.get(
    f"{base_url}/analytics",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    params={"postId": post_id},
    timeout=30
)

post_analytics = response.json()
```

---

## 📊 レスポンスデータ構造

### 完全なAnalyticsオブジェクト

```json
{
  "postId": "695a540ef497177b163fd7be",
  "status": "published",
  "content": "Google社員がClaude Code使用...",
  "scheduledFor": "2026-01-04T23:00:00Z",
  "publishedAt": "2026-01-04T23:00:05Z",
  "analytics": {
    "impressions": 15420,          // ✅ 実際の値
    "reach": 12350,                // ✅ 実際の値
    "likes": 342,                  // ✅ 実際の値
    "comments": 28,                // ✅ 実際の値
    "shares": 45,                  // ✅ 実際の値
    "clicks": 189,                 // ✅ 実際の値
    "views": 0,                    // 動画のみ
    "engagementRate": 2.78,        // ✅ 自動計算
    "lastUpdated": "2026-01-05T08:30:00Z"
  },
  "platformAnalytics": [{
    "platform": "linkedin",
    "status": "published",
    "accountId": "64e1f0a9e2b5af0012ab34cd",
    "accountUsername": "yuichi_takano",
    "analytics": {
      "impressions": 15420,
      "reach": 12350,
      "likes": 342,
      "comments": 28,
      "shares": 45,
      "clicks": 189,
      "views": 0,
      "engagementRate": 2.78,
      "lastUpdated": "2026-01-05T08:30:00Z"
    }
  }],
  "platform": "linkedin",
  "platformPostUrl": "https://www.linkedin.com/feed/update/urn:li:share:123456789",
  "isExternal": false
}
```

---

## 🚨 重要な前提条件

### 1. Analytics Addonの有効化が必須

**料金**: $10/月（すべてのプランに追加可能）

**有効化方法**:
1. Late Dashboard (https://app.getlate.dev) にログイン
2. Settings → Billing へ移動
3. "Analytics Addon" を追加購入（$10/月）
4. アドオン有効化後、APIで`/v1/analytics`エンドポイントにアクセス可能

**確認方法**:
```bash
# Analytics API へのアクセス可否を確認
curl -H "Authorization: Bearer YOUR_API_KEY" \
     https://getlate.dev/api/v1/analytics?limit=1
```

### 2. LinkedIn個人アカウントの制限

**Late API公式ドキュメントより**:

> **LinkedIn Personal Accounts:**
> - Analytics are only available for posts published through Late
> - External post syncing is not available (LinkedIn limitation)
> - Available metrics: impressions, reach, likes, comments, shares

**LinkedIn Organization Accounts:**
> - Full analytics support including external post syncing
> - All metrics available

**現在のアカウント**: 個人アカウント（推定）
**影響**: Late経由で投稿した投稿のみAnalytics取得可能

---

## 📋 実装スクリプト

### `/scripts/fetch_late_analytics.py`（新規作成）

```python
#!/usr/bin/env python3
"""
Late API Analytics取得スクリプト

Usage:
    python3 scripts/fetch_late_analytics.py --from-date 2026-01-04 --to-date 2026-01-05
    python3 scripts/fetch_late_analytics.py --post-id 695a540ef497177b163fd7be
"""

import requests
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path
import argparse

# プロジェクトルート
project_root = Path(__file__).parent.parent

# Late API設定読み込み
env_file = project_root / ".env"
env_vars = {}

if env_file.exists():
    with open(env_file, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()

LATE_API_KEY = env_vars.get("LATE_API_KEY")
LATE_BASE_URL = env_vars.get("LATE_BASE_URL", "https://getlate.dev/api/v1")

def fetch_analytics(from_date=None, to_date=None, post_id=None, platform="linkedin"):
    """
    Late API /v1/analytics からエンゲージメントデータを取得

    Args:
        from_date (str): 開始日 (YYYY-MM-DD)
        to_date (str): 終了日 (YYYY-MM-DD)
        post_id (str): 特定投稿ID
        platform (str): プラットフォーム（デフォルト: linkedin）

    Returns:
        dict: Analyticsデータ
    """
    headers = {
        "Authorization": f"Bearer {LATE_API_KEY}",
        "Content-Type": "application/json"
    }

    params = {}

    if post_id:
        # 単一投稿のAnalytics取得
        params["postId"] = post_id
    else:
        # 日付範囲でフィルタ
        if from_date:
            params["fromDate"] = from_date
        if to_date:
            params["toDate"] = to_date

        params["platform"] = platform
        params["sortBy"] = "date"
        params["order"] = "desc"
        params["limit"] = 100

    try:
        response = requests.get(
            f"{LATE_BASE_URL}/analytics",
            headers=headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()

        analytics_data = response.json()

        # レスポンスヘッダからレート制限情報を取得
        rate_limit_info = {
            "limit": response.headers.get("X-RateLimit-Limit"),
            "remaining": response.headers.get("X-RateLimit-Remaining"),
            "reset": response.headers.get("X-RateLimit-Reset")
        }

        return {
            "success": True,
            "data": analytics_data,
            "rate_limit": rate_limit_info
        }

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 402:
            return {
                "success": False,
                "error": "Analytics Addon not enabled. Please add $10/month Analytics Addon in Late Dashboard.",
                "error_code": 402
            }
        elif e.response.status_code == 429:
            return {
                "success": False,
                "error": "Rate limit exceeded (150 requests/hour). Please wait.",
                "error_code": 429,
                "reset": e.response.headers.get("X-RateLimit-Reset")
            }
        else:
            return {
                "success": False,
                "error": f"HTTP Error: {e.response.status_code} - {e.response.text}",
                "error_code": e.response.status_code
            }

    except Exception as e:
        return {
            "success": False,
            "error": f"Request failed: {str(e)}"
        }

def calculate_engagement_rate(analytics):
    """
    エンゲージメント率を計算（Late APIが提供しない場合）

    ER = (Likes + Comments×2 + Shares×3) / Impressions × 100
    """
    impressions = analytics.get("impressions", 0)
    if impressions == 0:
        return 0.0

    likes = analytics.get("likes", 0)
    comments = analytics.get("comments", 0)
    shares = analytics.get("shares", 0)

    engagement = likes + (comments * 2) + (shares * 3)
    er = (engagement / impressions) * 100

    return round(er, 2)

def main():
    parser = argparse.ArgumentParser(description="Late API Analytics取得")
    parser.add_argument("--from-date", help="開始日 (YYYY-MM-DD)")
    parser.add_argument("--to-date", help="終了日 (YYYY-MM-DD)")
    parser.add_argument("--post-id", help="特定投稿ID")
    parser.add_argument("--platform", default="linkedin", help="プラットフォーム（デフォルト: linkedin）")
    parser.add_argument("--output", help="出力ファイルパス（デフォルト: data/late_analytics_{date}.json）")

    args = parser.parse_args()

    # デフォルト値設定
    if not args.from_date and not args.post_id:
        # デフォルト: 過去7日間
        jst = timezone(timedelta(hours=9))
        today = datetime.now(jst).date()
        args.from_date = str(today - timedelta(days=7))
        args.to_date = str(today)

    print("=" * 60)
    print("Late API Analytics取得")
    print("=" * 60)

    if args.post_id:
        print(f"Post ID: {args.post_id}")
    else:
        print(f"期間: {args.from_date} ~ {args.to_date}")
        print(f"プラットフォーム: {args.platform}")
    print()

    # Analytics取得
    result = fetch_analytics(
        from_date=args.from_date,
        to_date=args.to_date,
        post_id=args.post_id,
        platform=args.platform
    )

    if not result["success"]:
        print(f"❌ エラー: {result['error']}")
        if result.get("error_code") == 402:
            print("\n💡 解決方法:")
            print("   1. Late Dashboard (https://app.getlate.dev) にログイン")
            print("   2. Settings → Billing へ移動")
            print("   3. Analytics Addon ($10/月) を追加購入")
        return

    # 結果表示
    data = result["data"]

    if args.post_id:
        # 単一投稿
        print(f"✅ 投稿Analytics取得成功")
        print(f"\n📊 エンゲージメントデータ:")
        analytics = data.get("analytics", {})
        print(f"   Impressions: {analytics.get('impressions', 0):,}")
        print(f"   Reach: {analytics.get('reach', 0):,}")
        print(f"   Likes: {analytics.get('likes', 0):,}")
        print(f"   Comments: {analytics.get('comments', 0):,}")
        print(f"   Shares: {analytics.get('shares', 0):,}")
        print(f"   Clicks: {analytics.get('clicks', 0):,}")
        print(f"   Views: {analytics.get('views', 0):,}")

        # エンゲージメント率計算
        if "engagementRate" in analytics:
            print(f"   ER: {analytics['engagementRate']}%")
        else:
            er = calculate_engagement_rate(analytics)
            print(f"   ER (計算): {er}%")

        print(f"\n⏱️  最終更新: {analytics.get('lastUpdated', 'N/A')}")
    else:
        # 複数投稿
        posts = data.get("posts", [])
        print(f"✅ Analytics取得成功: {len(posts)}件")

        if posts:
            print(f"\n📊 投稿一覧:")
            for i, post in enumerate(posts, 1):
                analytics = post.get("analytics", {})
                print(f"\n{i}. {post.get('content', '')[:50]}...")
                print(f"   Published: {post.get('publishedAt', 'N/A')}")
                print(f"   Impressions: {analytics.get('impressions', 0):,}")
                print(f"   Likes: {analytics.get('likes', 0):,}")
                print(f"   Comments: {analytics.get('comments', 0):,}")
                print(f"   Shares: {analytics.get('shares', 0):,}")

                # エンゲージメント率
                if "engagementRate" in analytics:
                    print(f"   ER: {analytics['engagementRate']}%")
                else:
                    er = calculate_engagement_rate(analytics)
                    print(f"   ER (計算): {er}%")

    # レート制限情報
    rate_limit = result["rate_limit"]
    print(f"\n🔄 レート制限:")
    print(f"   上限: {rate_limit['limit']}/時間")
    print(f"   残り: {rate_limit['remaining']}/時間")
    print(f"   リセット: {rate_limit['reset']}")

    # ファイル保存
    if args.output:
        output_path = Path(args.output)
    else:
        jst = timezone(timedelta(hours=9))
        today = datetime.now(jst).strftime("%Y%m%d")
        output_path = project_root / "data" / f"late_analytics_{today}.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"\n💾 出力: {output_path}")
    print(f"   サイズ: {output_path.stat().st_size:,} bytes")

if __name__ == "__main__":
    main()
```

---

## 🔧 使用方法

### 1. 過去7日間のAnalytics取得（デフォルト）

```bash
cd Stock/programs/副業/projects/SNS
python3 scripts/fetch_late_analytics.py
```

### 2. 特定期間のAnalytics取得

```bash
python3 scripts/fetch_late_analytics.py \
  --from-date 2026-01-04 \
  --to-date 2026-01-05 \
  --platform linkedin
```

### 3. 特定投稿のAnalytics取得

```bash
python3 scripts/fetch_late_analytics.py \
  --post-id 695a540ef497177b163fd7be
```

### 4. 出力ファイル指定

```bash
python3 scripts/fetch_late_analytics.py \
  --from-date 2026-01-04 \
  --to-date 2026-01-05 \
  --output data/custom_analytics.json
```

---

## 📅 実行タイムライン

### Priority 1: Analytics Addon有効化（即座）

1. **Late Dashboardにログイン**
   - URL: https://app.getlate.dev
   - Settings → Billing へ移動

2. **Analytics Addon購入**
   - $10/月を追加
   - 有効化確認

3. **API動作確認**
   ```bash
   python3 scripts/fetch_late_analytics.py --post-id 695a540ef497177b163fd7be
   ```

### Priority 2: 予約投稿のAnalytics測定（1/7 12:00以降）

```bash
# 2026-01-07 12:00: 案2公開24時間後
python3 scripts/fetch_late_analytics.py --from-date 2026-01-07 --to-date 2026-01-07

# 2026-01-08 12:00: 案1公開24時間後
python3 scripts/fetch_late_analytics.py --from-date 2026-01-08 --to-date 2026-01-08

# 2026-01-09 12:00: 案3公開24時間後
python3 scripts/fetch_late_analytics.py --from-date 2026-01-09 --to-date 2026-01-09
```

### Priority 3: 週次レポート作成（1/10以降）

```bash
# 3案の総合比較レポート
python3 scripts/fetch_late_analytics.py \
  --from-date 2026-01-07 \
  --to-date 2026-01-09 \
  --output data/weekly_performance_20260107.json
```

---

## 📊 期待される出力例

### 成功時

```json
{
  "success": true,
  "data": {
    "postId": "695a540ef497177b163fd7be",
    "status": "published",
    "content": "Google社員がClaude Code使用...",
    "publishedAt": "2026-01-04T23:00:05Z",
    "analytics": {
      "impressions": 3250,
      "reach": 2890,
      "likes": 127,
      "comments": 18,
      "shares": 23,
      "clicks": 95,
      "views": 0,
      "engagementRate": 4.15,
      "lastUpdated": "2026-01-05T19:30:00Z"
    },
    "platformAnalytics": [{
      "platform": "linkedin",
      "analytics": {
        "impressions": 3250,
        "reach": 2890,
        "likes": 127,
        "comments": 18,
        "shares": 23,
        "clicks": 95,
        "engagementRate": 4.15
      }
    }]
  },
  "rate_limit": {
    "limit": "150",
    "remaining": "149",
    "reset": "1735995600"
  }
}
```

### Analytics Addon未有効化時

```json
{
  "success": false,
  "error": "Analytics Addon not enabled. Please add $10/month Analytics Addon in Late Dashboard.",
  "error_code": 402
}
```

---

## 🎯 まとめ

### 問題の根本原因

1. **誤ったエンドポイント使用**: `/v1/posts`ではなく`/v1/analytics`が正しい
2. **Analytics Addon未有効化**: $10/月のアドオンが必須（おそらく未購入）

### 解決策

1. ✅ **Analytics Addon購入**: Late Dashboardで$10/月を追加
2. ✅ **正しいエンドポイント使用**: `/v1/analytics`に変更
3. ✅ **専用スクリプト作成**: `fetch_late_analytics.py`で自動取得

### 次のアクション

1. **即座**: Analytics Addon有効化
2. **1/7 12:00**: 案2のAnalytics測定（予測ER 3.5-4.2% vs 実測）
3. **1/8 12:00**: 案1のAnalytics測定（予測ER 3.8-4.5% vs 実測）
4. **1/9 12:00**: 案3のAnalytics測定（予測ER 4.0-4.8% vs 実測）
5. **1/10**: 週次パフォーマンスレポート作成

---

**参照**:
- Late API Analytics公式ドキュメント: https://docs.getlate.dev/core/analytics
- Late API価格: https://getlate.dev/pricing
- Late Dashboard: https://app.getlate.dev

**作成日時**: 2026-01-05 19:30:00
**次回更新**: Analytics Addon有効化後
