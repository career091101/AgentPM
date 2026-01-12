# Scrape Tweet Details Skill

## 概要

Top 10ツイートの詳細ページに遷移し、リンク（記事/YouTube/PDF）とリプライ上位5件を抽出するスキル。

**ステータス**: ✅ **本番Ready**（Playwright実装版、v1.0.0 Production）

## 使用方法

### コマンド実行

```bash
/scrape-tweet-details
```

### 自然言語トリガー

- "ツイート詳細抽出"
- "リンク・リプライ収集"
- "ツイート詳細ページスクレイピング"

## 前提条件

1. **依存スキル**: `/extract-top-tweets` が実行済み
2. **入力ファイル**: `Stock/programs/副業/projects/SNS/data/top_10_tweets_{YYYYMMDD}.json`
3. **Cookie認証**: `Stock/programs/副業/projects/SNS/data/x_cookies.json` が有効（30日以内）
4. **技術要件**: Playwright、requests ライブラリ

## 実行フロー

```
入力: top_10_tweets_{YYYYMMDD}.json (10件)
  ↓
STEP 1: 入力データ読み込み
  ↓
STEP 2: Cookie認証準備（有効期限チェック）
  ↓
STEP 3: ツイート詳細ページ巡回（10件）
  各ツイートごとに:
    - ページ遷移（https://x.com/i/status/{tweet_id}）
    - 動的コンテンツ読み込み待機
    - スクロールしてリプライ表示
    - STEP 4-6の処理
    - 3秒待機（レート制限回避）
  ↓
STEP 4: リンク抽出と分類（記事/YouTube/PDF）
  ↓
STEP 5: リプライ抽出（上位5件）
  ↓
STEP 6: メタデータ取得（メディア、ビュー数等）
  ↓
STEP 7: データ統合・出力
  ↓
STEP 8: 品質検証
  ↓
出力: tweet_details_{YYYYMMDD}.json
```

## 出力形式

```json
{
  "metadata": {
    "processed_at": "2026-01-02T11:00:00+09:00",
    "total_tweets_processed": 10,
    "success_count": 10
  },
  "tweet_details": [
    {
      "tweet_id": "1234567890123456789",
      "username": "ai_researcher_jp",
      "url": "https://x.com/ai_researcher_jp/status/1234567890123456789",
      "links": [
        {
          "url": "https://arxiv.org/abs/2401.12345",
          "type": "pdf",
          "title": "Research Paper on AI Agents",
          "domain": "arxiv.org"
        },
        {
          "url": "https://youtube.com/watch?v=abc123",
          "type": "youtube",
          "title": "AI Agent Tutorial",
          "domain": "youtube.com"
        }
      ],
      "replies": [
        {
          "username": "tech_enthusiast",
          "text": "これは素晴らしい研究ですね！特に...",
          "likes": 45,
          "created_at": "2026-01-02T08:30:00+09:00"
        }
      ],
      "metadata": {
        "has_media": true,
        "media_count": 1,
        "view_count": "12.5K"
      }
    }
  ]
}
```

## リンク分類ロジック

| URL パターン | 分類 |
|-------------|------|
| youtube.com, youtu.be | `youtube` |
| *.pdf | `pdf` |
| medium.com, note.com, zenn.dev, qiita.com | `article` |
| Content-Type: application/pdf | `pdf` |
| Content-Type: text/html | `article` |
| その他 | `other` |

**短縮URL展開**:
- t.co, bit.ly などは自動的に実URLに展開
- リダイレクト先を追跡

## エラーハンドリング

| エラー | 対応 |
|--------|------|
| Cookie期限切れ | ユーザー通知 + 再取得手順案内 + 処理中断 |
| ページ読み込みタイムアウト | 3回リトライ（5秒、10秒、20秒）→ スキップ |
| レート制限（429） | 60秒待機 → 再試行（最大3回）→ 進捗保存 |
| DOM要素未検出 | 代替セレクタ試行 → null記録 → 次へ |
| URL展開失敗 | 短縮URLのまま記録 + type: "unknown" |

## Best Practices

### Playwright安定化テクニック

```python
# ✅ 良い例: 動的コンテンツ待機
page.goto(url, wait_until='networkidle')
page.wait_for_selector('article[data-testid="tweet"]')

# ✅ ランダム待機でボット検出回避
import random
wait_time = random.uniform(3, 5)
page.wait_for_timeout(int(wait_time * 1000))

# ✅ User-Agent設定
context = browser.new_context(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
)
```

### レート制限回避

- 各リクエスト間に3秒待機
- 10件を順次処理（並列化しない）
- Cookie認証で成功率向上

## 実行時間

- **標準**: 10-15分（10件処理）
- **1件あたり**: 約1分
- **モデル**: haiku
- **Thinking**: Off

## 次のステップ

このスキル実行後、Phase 2スキルを実行してください:

```bash
# Phase 2: コンテンツ抽出（並列実行推奨）
/extract-content  # 記事/YouTube/PDF からコンテンツ抽出
/analyze-replies  # リプライから反響ポイント分析
/research-topic   # Web調査・ファクトチェック
```

## 技術依存

### インストール

```bash
# Playwright
pip install playwright
playwright install chromium

# その他
pip install requests
```

### Cookie取得方法

1. ブラウザでX.comにログイン
2. 開発者ツール → Application → Cookies
3. `auth_token` と `ct0` をコピー
4. `Stock/programs/副業/projects/SNS/data/x_cookies.json` に保存:

```json
{
  "auth_token": "your_auth_token_here",
  "ct0": "your_ct0_here"
}
```

**有効期限**: 30日

## バージョン履歴

- **v1.0.0** (2026-01-02): 初版作成
  - ツイート詳細ページ遷移機能
  - リンク抽出・分類（記事/YouTube/PDF）
  - リプライ上位5件取得
  - Cookie認証・レート制限対応
