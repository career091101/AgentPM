# X & Threads 同時投稿スキル

X（Twitter）とThreadsに同時投稿するClaude Codeスキルです。

## 機能

- ✅ X版コンテンツ生成（スレッド形式、バズ構文84パターン）
- ✅ Threads版コンテンツ生成（500字以内、絵文字・口語体最適化）
- ✅ Late API予約投稿（14日先まで空き日自動検索）
- ✅ リトライ機能付き（Rate Limit、Network Timeout対応）
- ✅ 部分成功許容（X失敗でもThreads成功でOK）

## クイックスタート

### 1. 設定ファイルの準備

**Late API設定** (`Stock/programs/副業/projects/SNS/config/late_api_config.json`):

```json
{
  "api_key": "sk_your_api_key_here",
  "base_url": "https://getlate.dev/api/v1",
  "accounts": {
    "twitter": {"accountId": "your_twitter_account_id", "platform": "twitter"},
    "threads": {"accountId": "your_threads_account_id", "platform": "threads"}
  }
}
```

または環境変数（`.env`）:

```bash
LATE_API_KEY=sk_your_api_key_here
LATE_TWITTER_ACCOUNT_ID=your_twitter_account_id
LATE_THREADS_ACCOUNT_ID=your_threads_account_id
```

### 2. スキル実行

Claude Codeで以下のように指示してください:

```
「X&Threads投稿」で以下のトピックについて投稿してください：
OpenAIのGPT-5.2プロンプトガイドが公開され、プロンプトエンジニアリングの常識が変わりつつある
```

または：

```
「同時投稿」でこの記事について投稿：https://example.com/ai-news
```

### 3. 実行結果

以下のファイルが生成されます：

```
Flow/202601/2026-01-06/
├── post_result_20260106_153000.json  # 結果サマリー（JSON）
└── post_result_20260106_153000.md    # 結果レポート（Markdown）
```

## 使用例

### 例1: トピック型（シンプル）

```json
{
  "input_type": "topic",
  "input_value": "AIの最新動向について解説"
}
```

### 例2: URL型（記事から生成）

```json
{
  "input_type": "article_url",
  "input_value": "https://example.com/ai-news"
}
```

### 例3: キーワード型（検索ベース）

```json
{
  "input_type": "keyword",
  "input_value": "生成AI 最新トレンド"
}
```

### 例4: 日付指定

```json
{
  "input_type": "topic",
  "input_value": "AIの未来について",
  "scheduled_date": "2026-01-10"
}
```

### 例5: 画像添付

```json
{
  "input_type": "topic",
  "input_value": "データ可視化の重要性",
  "image_path": "/path/to/chart.png"
}
```

## 出力仕様

### X版

- **形式**: スレッド（5-10ツイート、最適7）
- **文字数**: 280半角文字/ツイート（日本語140文字）
- **バズ構文**: 84パターンから最適選択
- **エンゲージメント予測**: X公式アルゴリズム実装

### Threads版

- **形式**: 単一投稿
- **文字数**: 300-500字
- **段落**: 2-4段落（空白2行禁止）
- **絵文字**: 3-5個
- **口語体**: 3-5回（「マジで」「ヤバい」等）
- **ハッシュタグ**: 1個のみ

## トラブルシューティング

### エラー: "LATE_API_KEY not found"

**原因**: Late API キーが設定されていません。

**対応**:
1. `.env`ファイルに`LATE_API_KEY=sk_...`を追加
2. または`late_api_config.json`に`api_key`を設定

### エラー: "14日先まで空き日がありません"

**原因**: 予約投稿が14日先まで埋まっています。

**対応**:
1. Late APIダッシュボードで不要な予約を削除
2. または`days_ahead`パラメータを30に拡張

### エラー: "文字数エラー: 280字（目標: 300-500字）"

**原因**: Threads版の文字数が不足しています。

**対応**:
- LLM生成プロンプトを調整し、300字以上になるよう指示

### エラー: "Rate Limit超過"

**原因**: Late APIのレート制限（300リクエスト/分）に到達。

**対応**:
- 自動的に1時間待機後リトライします
- または手動で時間をおいて再実行

## ファイル構成

```
.claude/skills/generate-x-threads-posts/
├── SKILL.md                      # メインスキル定義
├── README.md                     # 本ファイル
├── threads_patterns_config.json  # Threads最適化設定
└── examples/
    ├── sample_input.json         # サンプル入力
    └── sample_output.md          # サンプル出力

Stock/programs/副業/projects/SNS/scripts/
├── threads_adapter.py            # Threads Adapter
└── late_api_scheduler.py         # Late API Scheduler
```

## 関連ドキュメント

- [詳細設計書](../../../Flow/202601/2026-01-06/x_threads_simultaneous_posting_design.md)
- [Threads最適化分析](../../../Flow/202601/2026-01-06/threads_optimization_analysis.md)
- [Late API予約投稿ガイド](.claude/skills/sns-automation/LATE_API_SCHEDULED_POSTING_GUIDE.md)
- [X投稿スキル](../generate-x-posts/SKILL.md)

## ライセンス

このスキルは aipm_v0 プロジェクトの一部です。

---

**バージョン**: v1.0
**作成日**: 2026-01-06
**作成者**: Claude Sonnet 4.5
