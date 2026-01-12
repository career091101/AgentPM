# Late API Analytics データ収集調査レポート

**作成日時**: 2026-01-10
**対象期間**: 2026-01-01 ～ 2026-01-10
**調査目的**: インプレッション数が0になる問題の解明と解決策の提示

## 問題の経緯

### 前回のデータ収集結果

**ファイル**: `Stock/programs/副業/projects/SNS/data/late_api_data_20260101-20260110.json`

- 総投稿数: 81件（X: 27, Threads: 27, LinkedIn: 27）
- **問題**: 全投稿のインプレッション数が0
- 使用エンドポイント: `/v1/posts`

### 今回の調査結果

**使用エンドポイント**:
1. `/v1/posts` - 投稿一覧取得
2. `/v1/analytics` - Analyticsデータ取得

**結果**:
- X: 0件の投稿（全0件中）
- Threads: 0件の投稿（全9件中）→ 9件は存在するが期間外
- LinkedIn: 0件の投稿（全8件中）→ 8件は存在するが期間外

## 根本原因の特定

### 1. Late APIの仕様

Late APIは**予約投稿管理サービス**であり、以下の機能を提供:

- ✅ 予約投稿のスケジューリング
- ✅ 予約投稿の管理（作成・編集・削除）
- ❌ **公開後のアナリティクス取得（有料Addon）**

### 2. 投稿ステータスの確認

前回収集したデータの実際の投稿ステータス:

```json
{
  "post_id": "695e4b0073abd0b06df75f4b",
  "platform": "x",
  "published_at": "2026-01-07T12:01:04.715Z",
  "impressions": 0,
  "status": "scheduled"
}
```

**重要な発見**:
- `status: "scheduled"` → まだ公開されていない予約投稿
- `publishedAt: "2026-01-07T12:01:04.715Z"` → 公開予定日時（実際の公開日時ではない）
- `impressions: 0` → 公開されていないためインプレッション数は0

### 3. Late API `/posts` エンドポイントの実際のレスポンス

```json
{
  "_id": "695e4b0073abd0b06df75f4b",
  "status": "scheduled",
  "publishedAt": null,
  "scheduledAt": null
}
```

**結論**:
- Late APIは予約投稿を返すが、`publishedAt` は `null`
- 実際の公開は各プラットフォーム（X, Threads, LinkedIn）が行う
- Late APIは公開後のステータス更新を行わない（または遅延がある）

## 解決策

### オプション1: Late API Analytics Addon（有料）

**料金**: $10/月
**提供内容**: 公開後のインプレッション数、エンゲージメント率、リーチなど

**メリット**:
- Late API内で完結
- 統一されたAPI
- 複数プラットフォーム対応

**デメリット**:
- 月額費用が発生
- Addonが有効化されているか未確認

**実装方法**:
1. Late Dashboard (https://app.getlate.dev/settings/billing) でAnalytics Addonを有効化
2. `/v1/analytics` エンドポイントを使用
3. 実際のインプレッション数を取得

### オプション2: 各プラットフォームのAPI直接利用（推奨）

**料金**: 無料（各プラットフォームのAPI制限内）
**提供内容**: 公式APIから最も正確なデータを取得

#### X (Twitter) API v2

**エンドポイント**: `/2/tweets/:id`
**取得データ**: impressions, likes, retweets, replies

**実装スクリプト**: `scripts/integrate_x_analytics.py` （既存）

#### Threads API

**エンドポイント**: `/threads/{id}/insights`
**取得データ**: views, likes, replies, quotes

**実装スクリプト**: 作成が必要

#### LinkedIn API

**エンドポイント**: `/ugcPosts/{id}/statistics`
**取得データ**: impressions, clicks, likes, comments, shares

**実装スクリプト**: 作成が必要

### オプション3: ハイブリッドアプローチ（最適解）

1. **Late API**: 予約投稿の管理のみ使用
2. **各プラットフォームAPI**: アナリティクス取得
3. **統合スクリプト**: Late APIの投稿IDと各プラットフォームのAPIデータを結合

**メリット**:
- コスト効率が高い（Late APIの基本料金のみ）
- 各プラットフォームの最新APIを使用できる
- データの正確性が最も高い

**デメリット**:
- 実装が複雑
- 各APIの認証情報が必要

## 推奨アクション

### 短期（即座に実施可能）

1. **既存スクリプトの活用**:
   - `scripts/integrate_x_analytics.py` を使用してX APIからデータ取得
   - 既にX API統合が実装済み

2. **Late API Addonの検証**:
   ```bash
   python3 scripts/fetch_late_analytics.py --from-date 2026-01-01 --to-date 2026-01-10 --platform x
   ```
   → 402エラーが出る場合はAddon未契約

### 中期（1週間以内）

1. **Threads API統合**:
   - Threads Graph APIを使用したアナリティクス取得スクリプト作成
   - `scripts/integrate_threads_analytics.py` を新規作成

2. **LinkedIn API統合**:
   - LinkedIn Marketing API使用
   - `scripts/integrate_linkedin_analytics.py` を新規作成

### 長期（1ヶ月以内）

1. **統合ダッシュボード**:
   - 全プラットフォームのアナリティクスを一元管理
   - Late APIの投稿IDとプラットフォームAPIデータを自動結合

2. **自動化**:
   - 毎日定時実行でデータ収集
   - GitHub ActionsまたはAWS Lambdaで自動化

## 現時点での結論

**Late APIではインプレッション数を取得できない理由**:

1. Late APIは予約投稿管理サービス
2. 公開後のアナリティクスは有料Addon（$10/月）が必要
3. 前回のデータは全て「予約投稿」であり、まだ公開されていない

**次のステップ**:

1. ✅ Late API Analytics Addonの契約状況を確認
2. ✅ X API統合スクリプト (`integrate_x_analytics.py`) を実行して実データ取得を試行
3. ⏳ Threads APIとLinkedIn APIの統合スクリプト作成（必要に応じて）

## 添付データ

### 前回収集データのサンプル

**ファイル**: `late_api_data_20260101-20260110.json`

```json
{
  "metadata": {
    "total_posts": 81,
    "platform_stats": {
      "x": {
        "total_posts": 27,
        "impressions": 0,
        "total_engagement": 0
      }
    }
  },
  "data": [
    {
      "post_id": "695e4b0073abd0b06df75f4b",
      "platform": "x",
      "published_at": "2026-01-07T12:01:04.715Z",
      "impressions": 0,
      "raw_data": {
        "status": "scheduled"
      }
    }
  ]
}
```

### 今回の調査結果

**ファイル**: `late_api_analytics_20260101-0110.json`

```json
{
  "metadata": {
    "fetched_at": "2026-01-10T...",
    "period_start": "2026-01-01",
    "period_end": "2026-01-10",
    "total_posts": 0,
    "platform_stats": {
      "x": {
        "total_posts": 0,
        "impressions": 0,
        "total_engagement": 0
      },
      "threads": {
        "total_posts": 0,
        "impressions": 0,
        "total_engagement": 0
      },
      "linkedin": {
        "total_posts": 0,
        "impressions": 0,
        "total_engagement": 0
      }
    }
  },
  "data": []
}
```

## 参考リンク

- [Late API Documentation](https://docs.getlate.dev)
- [Late API Analytics Addon](https://app.getlate.dev/settings/billing)
- [X (Twitter) API v2 Analytics](https://developer.twitter.com/en/docs/twitter-api/metrics)
- [Threads API Insights](https://developers.facebook.com/docs/threads/insights)
- [LinkedIn Marketing API Statistics](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/community-management/shares/ugc-post-api)
