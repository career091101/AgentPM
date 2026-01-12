# Extract Top Tweets Skill

## 概要

Xタイムライン収集データから高エンゲージメント投稿Top 10を抽出するスキル。

## 使用方法

### コマンド実行

```bash
/extract-top-tweets
```

### 自然言語トリガー

- "Top 10抽出"
- "高エンゲージメント投稿"
- "X投稿ランキング"

## 前提条件

1. **依存スキル**: `/collect-x-timeline` が実行済み
2. **入力ファイル**: `Stock/programs/副業/projects/SNS/data/x_timeline_{YYYYMMDD}.json`
3. **データ件数**: 最低10件以上のツイートデータ

## 実行フロー

```
入力: x_timeline_{YYYYMMDD}.json (200件)
  ↓
STEP 1: タイムラインデータ読み込み
  ↓
STEP 2: エンゲージメントスコア計算
  engagement_score = likes + (retweets × 3) + (replies × 5)
  ↓
STEP 3: フィルタリング（世界的著名人除外）
  ↓
STEP 4: ソート・Top 10抽出（降順）
  ↓
STEP 5: メタデータ付与
  ↓
STEP 6: ファイル出力
  ↓
STEP 7: 品質検証
  ↓
出力: top_10_tweets_{YYYYMMDD}.json (10件)
```

## 出力形式

```json
{
  "metadata": {
    "processed_at": "2026-01-02T10:30:00+09:00",
    "source_file": "x_timeline_20260102.json",
    "total_tweets": 200,
    "filtered_tweets": 195,
    "top_tweets_count": 10
  },
  "top_tweets": [
    {
      "rank": 1,
      "tweet_id": "1234567890123456789",
      "username": "ai_researcher_jp",
      "text": "...",
      "likes": 150,
      "retweets": 45,
      "replies": 20,
      "engagement_score": 385,
      "created_at": "2026-01-02T08:15:00+09:00",
      "url": "https://x.com/ai_researcher_jp/status/1234567890123456789"
    }
  ]
}
```

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| ファイル未検出 | ユーザー通知 + 処理中断 |
| JSONパースエラー | エラー行特定 + 修正提案 |
| データ不足（<10件） | 警告 + 全件出力 |
| 全件が著名人 | フィルタ条件緩和提案 |

## 実行時間

- **標準**: 3-5分
- **モデル**: haiku
- **Thinking**: Off

## 次のステップ

このスキル実行後、以下のスキルを実行してください:

```bash
/scrape-tweet-details
```

ツイート詳細ページからリンク・リプライを抽出します。

## バージョン履歴

- **v1.0.0** (2026-01-02): 初版作成
  - 基本的なTop 10抽出機能
  - エンゲージメントスコア計算
  - 著名人フィルタリング
