# Collect X Timeline Skill

X (Twitter) のホームタイムラインから高エンゲージメント投稿を効率的に収集するClaude Code Skill。

---

## 概要

**カーソルベースAPI傍受方式**により、GraphQL APIのHomeTimelineエンドポイントをネットワークレスポンスで傍受し、**重複率0%**でツイートデータを収集します。

---

## クイックスタート

### 1. Cookie認証ファイルの準備

```bash
# X.com にブラウザでログイン
# 開発者ツール → Application → Cookies → x.com
# クッキーをJSON形式でエクスポート

# 保存先
Stock/programs/副業/projects/SNS/data/x_cookies.json
```

### 2. スキル実行

```bash
# Claude Codeで実行
Xタイムライン収集
```

または

```bash
# スラッシュコマンドで実行（将来的に実装予定）
/collect-x-timeline
```

### 3. 出力確認

```bash
# 出力ファイル
Stock/programs/副業/projects/SNS/data/x_timeline_YYYYMMDD.json

# 内容確認
cat Stock/programs/副業/projects/SNS/data/x_timeline_20260101.json | jq '.total_tweets'
```

---

## 実行パラメータ

| パラメータ | デフォルト | 説明 |
|-----------|-----------|------|
| **目標収集件数** | 200件 | 収集するツイート数 |
| **出力パス** | `data/x_timeline_{YYYY-MM-DD}.json` | 出力ファイルパス |
| **Cookie** | `data/x_cookies.json` | 認証用Cookieファイル |
| **デバッグモード** | OFF | APIレスポンス保存 |

---

## 出力フォーマット

```json
{
  "collected_at": "2026-01-01T22:30:00",
  "total_tweets": 211,
  "unique_tweets": 211,
  "duplicate_rate": 0.0,
  "cursors_collected": 7,
  "quality_score": {
    "achievement_rate": 105.5,
    "duplicate_rate": 0.0,
    "engagement_completeness": 95.2
  },
  "tweets": [
    {
      "tweet_id": "1234567890",
      "username": "@elonmusk",
      "text": "Tweet content...",
      "likes": 103049,
      "retweets": 25000,
      "replies": 8500,
      "timestamp_text": "Mon Jan 01 22:20:00 +0000 2026",
      "collected_at": "2026-01-01T22:30:00"
    }
  ]
}
```

---

## パフォーマンス

| 指標 | 実績（2026-01-01） |
|------|------------------|
| **収集件数** | 211件（目標200件の105.5%） |
| **重複率** | 0% |
| **実行時間** | 約5分 |
| **Username抽出率** | 100% |
| **エンゲージメント完全性** | 95.2% |

---

## トラブルシューティング

### Cookie認証失敗

**症状**: `auth_failure` エラー

**対処法**:
1. X.com に再ログイン
2. Cookieを再取得
3. `data/x_cookies.json` を更新

### Username抽出が"unknown"になる

**症状**: `username: "unknown"` が多数

**対処法**: 自動的にフォールバックパスで再抽出されます（通常対応不要）

### エンゲージメント指標が0になる

**症状**: `likes: 0, retweets: 0` が多数

**対処法**: GraphQL APIから直接抽出するため、通常発生しません（発生時はDOM変更の可能性）

---

## 次のアクション

収集完了後、以下のアクションを実行できます：

1. **トレンド分析**: 高エンゲージメント投稿Top 50抽出
2. **インフルエンサー分析**: 影響力の高いユーザーTop 10特定
3. **コンテンツ戦略**: 人気トピック・キーワード抽出
4. **時系列分析**: 日次・週次トレンド推移可視化

---

## 技術詳細

詳細は [SKILL.md](SKILL.md) を参照してください。

---

## 参照ドキュメント

- **実装ガイド**: `Stock/programs/副業/projects/SNS/X_COLLECTION_INSTRUCTIONS.md`
- **修正版ガイド**: `Stock/programs/副業/projects/SNS/docs/x_timeline_collection_fixed_guide.md`
- **成功レポート**: `Stock/programs/副業/projects/SNS/data/x_timeline_20260101_final/FINAL_SUCCESS_REPORT.md`
- **比較レポート**: `Stock/programs/副業/projects/SNS/data/cursor_vs_scroll_comparison_report.md`

---

## 更新履歴

- 2026-01-02: 初版作成（Claude Code Skill対応）
