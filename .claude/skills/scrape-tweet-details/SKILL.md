# scrape-tweet-details

---
name: scrape-tweet-details
description: |
  Top 10ツイートの詳細ページ（x.com/i/status/{tweet_id}）に遷移し、
  リンク（記事/YouTube/PDF）とリプライ上位5件を抽出。
  所要時間: 10-15分、出力: tweet_details.json
version: 1.0.0
trigger_keywords:
  - "ツイート詳細抽出"
  - "リンク・リプライ収集"
  - "ツイート詳細ページスクレイピング"
stage: Phase 1b - Detail Extraction
dependencies:
  - extract-top-tweets
output_file: "Stock/programs/副業/projects/SNS/data/tweet_details_{YYYYMMDD}.json"
execution_time: "10-15分"
priority: P0
model: claude-haiku-4-5-20251001  # Haiku 4.5 (2026年1月時点の最新モデル)
thinking: false
---

## Overview

`extract-top-tweets` スキルが抽出したTop 10ツイートの詳細ページに遷移し、以下の情報を収集します:

1. **リンク抽出**: ツイート本文内のURL（記事/YouTube/PDF）を分類
2. **リプライ抽出**: エンゲージメント上位5件のリプライを取得
3. **メタデータ取得**: 投稿時間、エンゲージメント詳細、メディア情報

**技術スタック**:
- Playwright (ブラウザ自動化)
- Cookie認証（30日有効期限）
- DOM解析

---

## Instructions

### STEP 1: 入力データ読み込み（1分）

**入力ファイル**:
- `Stock/programs/副業/projects/SNS/data/top_10_tweets_{YYYYMMDD}.json`
- Fallback: 最新日付のファイルを自動検索

**データ抽出**:
```python
# Top 10のツイートID・URLリストを作成
tweet_list = [
    {
        'tweet_id': tweet['tweet_id'],
        'url': f"https://x.com/i/status/{tweet['tweet_id']}",
        'username': tweet['username']
    }
    for tweet in input_data['top_tweets']
]
```

**検証**:
- [ ] tweet_id が存在するか
- [ ] URL形式が正しいか

---

### STEP 2: Cookie認証準備（1分）

**Cookie読み込み**:
- Cookie保存先: `Stock/programs/副業/projects/SNS/data/x_cookies.json`
- 形式: `{ "auth_token": "...", "ct0": "..." }`

**Cookie有効期限チェック**:
```python
if cookie_age > 30 days:
    print("⚠️ Cookie has expired. Please re-authenticate.")
    # @.claude/skills/_shared/error_handling_patterns.md#5-認証エラー
```

**Playwright初期化**:
```python
from playwright.sync_api import sync_playwright

browser = playwright.chromium.launch(headless=True)
context = browser.new_context()
context.add_cookies(cookies)
page = context.new_page()
```

---

### STEP 3: ツイート詳細ページ巡回（8-10分）

**並列処理の検討**:
- 10件を順次処理（安定性優先）
- 各ツイート処理時間: 約1分
- レート制限回避: 各リクエスト間に3秒待機

**ページ遷移ロジック**:
```python
for tweet in tweet_list:
    try:
        # 1. ページ遷移
        page.goto(tweet['url'], wait_until='networkidle')

        # 2. ページ完全読み込み待機（動的コンテンツ）
        page.wait_for_selector('article[data-testid="tweet"]', timeout=10000)

        # 3. スクロールしてリプライ読み込み
        page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        page.wait_for_timeout(2000)  # 2秒待機

        # 4. データ抽出（STEP 4-6）
        extract_links(page, tweet)
        extract_replies(page, tweet)

        # 5. レート制限回避
        page.wait_for_timeout(3000)  # 3秒待機

    except Exception as e:
        # エラーログ記録 + 次のツイートへ
        log_error(tweet['tweet_id'], str(e))
        continue
```

---

### STEP 4: リンク抽出と分類（1分/ツイート）

**リンク抽出セレクタ**:
```python
# ツイート本文内のリンク
links = page.query_selector_all('article[data-testid="tweet"] a[href^="http"]')
```

**リンク分類ロジック**:
```python
def classify_link(url):
    """URLを記事/YouTube/PDFに分類"""
    if 'youtube.com' in url or 'youtu.be' in url:
        return 'youtube'
    elif url.endswith('.pdf'):
        return 'pdf'
    elif any(domain in url for domain in ['medium.com', 'note.com', 'zenn.dev', 'qiita.com']):
        return 'article'
    else:
        # HEAD リクエストでContent-Typeチェック
        response = requests.head(url, allow_redirects=True, timeout=5)
        content_type = response.headers.get('Content-Type', '')

        if 'application/pdf' in content_type:
            return 'pdf'
        elif 'text/html' in content_type:
            return 'article'
        else:
            return 'other'
```

**短縮URL展開**:
```python
# t.co, bit.ly などの短縮URLを実URLに展開
if 't.co' in url or 'bit.ly' in url:
    response = requests.head(url, allow_redirects=True, timeout=5)
    url = response.url  # リダイレクト先URL
```

**出力データ構造**:
```json
"links": [
    {
        "url": "https://example.com/article",
        "type": "article",
        "title": "記事タイトル（可能な場合）",
        "domain": "example.com"
    },
    {
        "url": "https://youtube.com/watch?v=xxx",
        "type": "youtube",
        "title": "動画タイトル",
        "domain": "youtube.com"
    }
]
```

---

### STEP 5: リプライ抽出（1分/ツイート）

**リプライ取得セレクタ**:
```python
# リプライツイートのDOM要素
reply_elements = page.query_selector_all('article[data-testid="tweet"][role="article"]')
# 最初の1件は元ツイート自身なので除外
reply_elements = reply_elements[1:]
```

**リプライ情報抽出**:
```python
for reply_elem in reply_elements[:5]:  # 上位5件
    reply_data = {
        'username': reply_elem.query_selector('[data-testid="User-Name"] a').inner_text(),
        'text': reply_elem.query_selector('[data-testid="tweetText"]').inner_text(),
        'likes': int(reply_elem.query_selector('[data-testid="like"]').inner_text() or 0),
        'created_at': reply_elem.query_selector('time').get_attribute('datetime')
    }
```

**エンゲージメント順ソート**:
- X.comのデフォルト表示順（Top Repliesアルゴリズム）に依存
- 表示順の最初5件を取得

**リプライが5件未満の場合**:
- 警告表示: "⚠️ リプライ数が5件未満です（{N}件）"
- 取得可能な全件を出力

---

### STEP 6: メタデータ取得（30秒/ツイート）

**追加情報抽出**:
```python
metadata = {
    'has_media': bool(page.query_selector('[data-testid="tweetPhoto"]')),
    'media_count': len(page.query_selector_all('[data-testid="tweetPhoto"]')),
    'has_video': bool(page.query_selector('video')),
    'view_count': page.query_selector('[data-testid="views"]').inner_text() if page.query_selector('[data-testid="views"]') else None,
    'is_thread': '/' in page.query_selector('[data-testid="reply"]').inner_text() if page.query_selector('[data-testid="reply"]') else False
}
```

---

### STEP 7: データ統合・出力（2分）

**出力JSON構造**:
```json
{
  "metadata": {
    "processed_at": "2026-01-02T11:00:00+09:00",
    "source_file": "top_10_tweets_20260102.json",
    "total_tweets_processed": 10,
    "success_count": 10,
    "error_count": 0
  },
  "tweet_details": [
    {
      "tweet_id": "1234567890123456789",
      "username": "ai_researcher_jp",
      "url": "https://x.com/ai_researcher_jp/status/1234567890123456789",
      "engagement_score": 385,
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
        },
        ...
      ],
      "metadata": {
        "has_media": true,
        "media_count": 1,
        "has_video": false,
        "view_count": "12.5K",
        "is_thread": false
      }
    },
    ...
  ],
  "errors": []
}
```

**Write tool でファイル保存**:
- パス: `Stock/programs/副業/projects/SNS/data/tweet_details_{YYYYMMDD}.json`
- フォーマット: JSON（インデント2スペース）

---

### STEP 8: 品質検証（1分）

**検証項目**:

1. **データ完全性**:
   - [ ] 10件全てのツイート詳細が取得済み
   - [ ] リンク抽出成功率 > 80%
   - [ ] リプライ抽出成功率 > 80%

2. **リンク分類精度**:
   - [ ] YouTube URLが全て `youtube` に分類
   - [ ] PDF URLが全て `pdf` に分類
   - [ ] 記事URLが `article` に分類

3. **リプライ品質**:
   - [ ] リプライテキストが空文字列でない
   - [ ] ユーザー名が正しく抽出されている

**検証失敗時**:
- 警告ログ出力
- エラー詳細を `errors` 配列に記録

---

## Output Format

**成功時の表示例**:
```
✅ Tweet details extracted successfully

📊 Summary:
- Total tweets processed: 10/10
- Success rate: 100%
- Total links extracted: 18
  - Articles: 12 (66.7%)
  - YouTube: 5 (27.8%)
  - PDF: 1 (5.5%)
- Total replies extracted: 50 (avg 5.0/tweet)
- Output file: Stock/programs/副業/projects/SNS/data/tweet_details_20260102.json

🔗 Link Breakdown by Tweet:
- Tweet 1 (@ai_researcher_jp): 2 links (1 article, 1 YouTube)
- Tweet 2 (@startup_founder): 1 link (1 article)
- Tweet 3 (@tech_writer_jp): 3 links (2 articles, 1 PDF)
...

💬 Reply Insights:
- Average likes per reply: 23.4
- Most engaged reply: @tech_enthusiast (45 likes)
```

---

## Error Handling

### エラーパターン1: Cookie期限切れ
- **参照**: @.claude/skills/_shared/error_handling_patterns.md#5-認証エラー
- **対応**:
  1. エラーメッセージ表示
  2. Cookie再取得手順を案内
  3. 処理中断

### エラーパターン2: ページ読み込みタイムアウト
- **対応**:
  1. 3回リトライ（指数バックオフ: 5秒、10秒、20秒）
  2. 3回失敗後はスキップ + エラーログ記録
  3. 次のツイートに進む

### エラーパターン3: レート制限（429 Too Many Requests）
- **対応**:
  1. 60秒待機
  2. 再試行
  3. 3回連続失敗で処理中断 + 進捗保存

### エラーパターン4: DOM要素が見つからない
- **対応**:
  1. セレクタの代替パターンを試行
  2. 全て失敗した場合は `null` を記録
  3. 次のツイートに進む

### エラーパターン5: リンクURL展開失敗
- **対応**:
  1. 短縮URLのまま記録
  2. `type: "unknown"` でマーク
  3. 警告ログ出力

---

## Best Practices

### Playwright安定化テクニック

1. **動的コンテンツ待機**:
```python
# ❌ 悪い例
page.goto(url)
page.wait_for_timeout(5000)  # 固定待機は不安定

# ✅ 良い例
page.goto(url, wait_until='networkidle')
page.wait_for_selector('article[data-testid="tweet"]')
```

2. **レート制限回避**:
```python
# ランダム待機時間（3-5秒）でボット検出回避
import random
wait_time = random.uniform(3, 5)
page.wait_for_timeout(int(wait_time * 1000))
```

3. **User-Agent設定**:
```python
context = browser.new_context(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
)
```

4. **エラーログ詳細化**:
```python
try:
    page.goto(url)
except Exception as e:
    error_log = {
        'tweet_id': tweet_id,
        'error_type': type(e).__name__,
        'error_message': str(e),
        'url': url,
        'timestamp': datetime.now().isoformat()
    }
    errors.append(error_log)
```

---

## Quality Checklist

実行完了時に以下を確認:

- [ ] 10件全てのツイート詳細抽出完了
- [ ] リンク分類精度90%以上（手動で3件サンプル検証）
- [ ] リプライ抽出成功率90%以上
- [ ] Cookie認証成功（エラーなし）
- [ ] レート制限に引っかかっていない
- [ ] 出力JSONが正しい形式
- [ ] エラーログが適切に記録されている

---

## Dependencies

**前提スキル**:
- `extract-top-tweets`: Top 10ツイートID・URLリスト

**次フェーズスキル**:
- `extract-content`: 記事/YouTube/PDF からコンテンツ抽出
- `analyze-replies`: リプライから反響ポイント分析

**技術依存**:
- Playwright (インストール: `pip install playwright && playwright install chromium`)
- requests (インストール: `pip install requests`)

---

## Version History

- **v1.0.0** (2026-01-02): 初版作成
  - ツイート詳細ページ遷移機能
  - リンク抽出・分類（記事/YouTube/PDF）
  - リプライ上位5件取得
  - Cookie認証・レート制限対応
