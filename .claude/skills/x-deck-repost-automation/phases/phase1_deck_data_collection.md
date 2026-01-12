# Phase 1: デッキデータ収集

## 概要

X Pro Decksの16個のキュレーションデッキから高エンゲージメントの海外AI動向投稿を自動収集するフェーズ。

**所要時間**: 20-30分
**並列化**: 可能（デッキ毎に並列実行）
**推奨モデル**: haiku（I/O待機が多く、データ収集に最適）

---

## 目的

1. 16個のX Pro Decksから投稿を自動収集
2. インプレッション数10万以上の投稿のみフィルタ
3. AI関連投稿のみをLLM判定で抽出
4. 上位10-20件の高品質投稿を選定

---

## 入力ファイル

### `deck_search_queries.json`

16個のデッキ検索クエリ定義。

**ファイルパス**: `.claude/skills/x-deck-repost-automation/deck_search_queries.json`

**データ構造**:
```json
{
  "extractedAt": "2026-01-12",
  "deckUrl": "https://pro.x.com/i/decks/1710553908769378676",
  "totalDecks": 16,
  "decks": [
    {
      "deckName": "JP AI Leader",
      "searchQuery": "(from:keitowebai OR from:ctgptlb OR ...) min_retweets:10 -is:reply -is:retweetet",
      "description": "日本のAIリーダー6名のツイート（リツイート10以上、返信とリツイート除外）"
    },
    ...
  ]
}
```

### `repost_config.json`

フィルタ条件設定。

**ファイルパス**: `.claude/skills/x-deck-repost-automation/repost_config.json`

**関連設定**:
```json
{
  "filters": {
    "min_impressions": 100000,
    "ai_related_only": true,
    "engagement_threshold": {
      "min_likes": 1000,
      "min_retweets": 100
    }
  },
  "data_collection": {
    "decks_to_scan": 16,
    "tweets_per_deck": 30,
    "max_tweets_to_analyze": 20,
    "final_selection": 6
  }
}
```

---

## 処理フロー

### STEP 1: 検索クエリ読み込み

```python
import json

# deck_search_queries.jsonを読み込み
with open('.claude/skills/x-deck-repost-automation/deck_search_queries.json', 'r') as f:
    deck_config = json.load(f)

decks = deck_config['decks']
print(f"検索対象デッキ数: {len(decks)}個")
```

### STEP 2: Claude in Chrome MCPでデッキ検索

各デッキの検索クエリを実行し、投稿を収集。

**実装パターン**:
```python
# Chrome MCP初期化
tabs_context_mcp(createIfEmpty=True)
tab_id = tabs_create_mcp()

all_tweets = []

for deck in decks:
    deck_name = deck['deckName']
    search_query = deck['searchQuery']

    # X検索実行
    search_url = f"https://x.com/search?q={urllib.parse.quote(search_query)}&f=live"
    navigate(url=search_url, tabId=tab_id)

    wait(duration=2)  # ページロード待機

    # 投稿リスト取得（スクロールで20-30件取得）
    for i in range(3):  # 3回スクロール
        scroll(scroll_direction="down", scroll_amount=5, tabId=tab_id)
        wait(duration=1)

    # スクリーンショット保存（証拠記録）
    screenshot(tabId=tab_id)

    # ページコンテンツ取得
    page_content = get_page_text(tabId=tab_id)

    # 投稿データ抽出（JavaScript実行）
    tweets_data = javascript_tool(
        action="javascript_exec",
        text="""
        const tweets = [];
        document.querySelectorAll('article[data-testid="tweet"]').forEach(tweet => {
            const textEl = tweet.querySelector('[data-testid="tweetText"]');
            const linkEl = tweet.querySelector('a[href*="/status/"]');
            const statsEls = tweet.querySelectorAll('[role="group"] span');

            if (linkEl) {
                tweets.push({
                    text: textEl ? textEl.innerText : '',
                    url: 'https://x.com' + linkEl.getAttribute('href'),
                    // エンゲージメント統計は画面から取得困難のため、後続フェーズで詳細取得
                });
            }
        });
        tweets;
        """,
        tabId=tab_id
    )

    # デッキ名を追加
    for tweet in tweets_data:
        tweet['source_deck'] = deck_name

    all_tweets.extend(tweets_data[:30])  # 各デッキから最大30件

print(f"収集投稿数: {len(all_tweets)}件")
```

### STEP 3: 投稿詳細取得（エンゲージメント数）

各投稿のURLに遷移し、インプレッション数・いいね数・リツイート数を取得。

**重要**: X APIでインプレッション数は取得できないため、画面から直接抽出。

**実装パターン**:
```python
detailed_tweets = []

for tweet in all_tweets[:100]:  # 最初の100件のみ詳細取得（時間短縮）
    navigate(url=tweet['url'], tabId=tab_id)
    wait(duration=1)

    # エンゲージメント統計取得（JavaScript実行）
    engagement = javascript_tool(
        action="javascript_exec",
        text="""
        const stats = {};

        // インプレッション数（"Views" 表示）
        const viewsEl = document.querySelector('[href$="/analytics"] span');
        if (viewsEl) {
            const viewsText = viewsEl.innerText;
            // "1.2M Views" → 1200000 に変換
            stats.impressions = parseViewCount(viewsText);
        }

        // いいね数・リツイート数・リプライ数
        const groupEl = document.querySelector('[role="group"]');
        if (groupEl) {
            const statsText = groupEl.innerText;
            // テキストから数値抽出
            stats.likes = extractNumber(statsText, 'likes');
            stats.retweets = extractNumber(statsText, 'retweets');
            stats.replies = extractNumber(statsText, 'replies');
        }

        stats;

        function parseViewCount(text) {
            const match = text.match(/([\\d.]+)([MKB]?)/);
            if (!match) return 0;
            const num = parseFloat(match[1]);
            const suffix = match[2];
            if (suffix === 'M') return num * 1000000;
            if (suffix === 'K') return num * 1000;
            if (suffix === 'B') return num * 1000000000;
            return num;
        }

        function extractNumber(text, type) {
            // 実装省略（テキストから数値抽出）
            return 0;
        }
        """,
        tabId=tab_id
    )

    tweet.update(engagement)
    detailed_tweets.append(tweet)

    # レート制限回避
    wait(duration=0.5)

print(f"詳細取得完了: {len(detailed_tweets)}件")
```

### STEP 4: インプレッション数フィルタ（10万以上）

```python
# repost_config.jsonから閾値読み込み
with open('.claude/skills/x-deck-repost-automation/repost_config.json', 'r') as f:
    config = json.load(f)

min_impressions = config['filters']['min_impressions']
min_likes = config['filters']['engagement_threshold']['min_likes']
min_retweets = config['filters']['engagement_threshold']['min_retweets']

# フィルタ実行
high_engagement_tweets = [
    tweet for tweet in detailed_tweets
    if tweet.get('impressions', 0) >= min_impressions
    and tweet.get('likes', 0) >= min_likes
    and tweet.get('retweets', 0) >= min_retweets
]

print(f"高エンゲージメント投稿: {len(high_engagement_tweets)}件")
```

### STEP 5: AI関連判定（LLM判定ワンパス化）

**既存スキル流用**: `.claude/skills/sns-automation/extract-content.md` のLLM判定ロジック

```python
# LLM判定プロンプト
ai_related_prompt = """
以下のツイートがAI関連の投稿かどうかを判定してください。

**判定基準**:
- AI技術（機械学習、深層学習、LLM、生成AI等）
- AI企業・プロダクト（OpenAI、Google AI、Microsoft AI等）
- AIビジネス・戦略（投資、M&A、競争環境等）
- AIロボティクス（自律走行、ヒューマノイド等）

**ツイート全文**:
{tweet_text}

**回答形式**:
スコア: 0-3（0=無関連、1=やや関連、2=関連、3=強く関連）
理由: [30字以内で判定理由]

0スコアの場合は即座にワンパスで除外してください。
"""

ai_related_tweets = []

for tweet in high_engagement_tweets:
    # LLM判定実行（Claude Sonnet 4.5で高速判定）
    judgment = llm_judge(
        prompt=ai_related_prompt.format(tweet_text=tweet['text']),
        model="sonnet"
    )

    if judgment['score'] >= 1:  # スコア1以上（やや関連以上）
        tweet['ai_score'] = judgment['score']
        tweet['ai_reason'] = judgment['reason']
        ai_related_tweets.append(tweet)

print(f"AI関連投稿: {len(ai_related_tweets)}件")
```

### STEP 6: インプレッション数でソート、上位10-20件抽出

```python
# インプレッション数でソート（降順）
ai_related_tweets.sort(key=lambda x: x.get('impressions', 0), reverse=True)

# 上位20件を抽出
top_tweets = ai_related_tweets[:20]

print(f"最終選定投稿: {len(top_tweets)}件")

# 上位投稿のサマリー表示
for i, tweet in enumerate(top_tweets[:10], 1):
    print(f"{i}. {tweet['impressions']:,}インプ | {tweet['likes']:,}いいね | {tweet['source_deck']}")
    print(f"   {tweet['text'][:100]}...")
```

---

## 出力ファイル

### `deck_timeline_{date}.json`

全デッキから収集した投稿データ（320-480件）。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/deck_timeline_{date}.json`

**データ構造**:
```json
{
  "collected_at": "2026-01-12T10:30:00+09:00",
  "total_tweets": 450,
  "decks_scanned": 16,
  "tweets": [
    {
      "url": "https://x.com/username/status/123456789",
      "text": "Tweet full text...",
      "source_deck": "AI People #1",
      "impressions": 250000,
      "likes": 3500,
      "retweets": 450,
      "replies": 120,
      "author": "@username",
      "author_name": "Author Name",
      "posted_at": "2026-01-11T15:30:00Z"
    },
    ...
  ]
}
```

### `deck_top_tweets_{date}.json`

フィルタ後の上位投稿（10-20件、AI関連のみ）。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/deck_top_tweets_{date}.json`

**データ構造**:
```json
{
  "filtered_at": "2026-01-12T11:00:00+09:00",
  "total_selected": 20,
  "filter_criteria": {
    "min_impressions": 100000,
    "min_likes": 1000,
    "min_retweets": 100,
    "ai_related_only": true
  },
  "tweets": [
    {
      "rank": 1,
      "url": "https://x.com/username/status/123456789",
      "text": "Tweet full text...",
      "source_deck": "AI Leaders #1",
      "impressions": 1500000,
      "likes": 25000,
      "retweets": 3500,
      "replies": 850,
      "ai_score": 3,
      "ai_reason": "OpenAI投資ラウンドに関する詳細分析"
    },
    ...
  ]
}
```

---

## エラーハンドリング

### エラー1: デッキ検索失敗

**エラー**: "Deck not accessible" または検索結果が0件

```python
# 対策
try:
    navigate(url=search_url, tabId=tab_id)
    wait(duration=2)
    page_content = get_page_text(tabId=tab_id)

    if "No results" in page_content or len(page_content) < 100:
        # X Pro未対応の場合、標準検索に切り替え
        standard_search_url = f"https://x.com/search?q={urllib.parse.quote(search_query)}&src=typed_query&f=top"
        navigate(url=standard_search_url, tabId=tab_id)
        wait(duration=2)
except Exception as e:
    print(f"デッキ {deck_name} の検索失敗: {e}")
    continue  # 次のデッキに進む
```

### エラー2: インプレッション数取得失敗

**エラー**: JavaScript実行でインプレッション数が取得できない

```python
# 対策: いいね数・リツイート数でエンゲージメントを推定
if tweet.get('impressions', 0) == 0:
    # 推定式: インプレッション ≒ (いいね数 + リツイート数) × 50
    estimated_impressions = (tweet.get('likes', 0) + tweet.get('retweets', 0)) * 50
    tweet['impressions'] = estimated_impressions
    tweet['impressions_estimated'] = True
```

### エラー3: Chrome MCP接続エラー

**エラー**: "Tab context not found" または "Tab ID invalid"

```python
# 対策: 接続再初期化
try:
    tabs_context_mcp(createIfEmpty=True)
    tab_id = tabs_create_mcp()
except Exception as e:
    print(f"Chrome MCP接続エラー: {e}")
    print("解決策:")
    print("1. Chromeを再起動")
    print("2. Claude in Chrome拡張機能を再インストール")
    print("3. エージェントを再起動")
    raise
```

---

## 並列化戦略

### デッキ毎の並列実行

16個のデッキを5つずつバッチ処理で並列実行（最大5並列）。

**実装例**:
```python
from concurrent.futures import ThreadPoolExecutor

def collect_from_deck(deck, tab_id):
    """1つのデッキから投稿を収集"""
    # STEP 2の処理を実行
    return tweets_from_deck

# 5デッキずつ並列実行
batch_size = 5
all_tweets = []

for i in range(0, len(decks), batch_size):
    batch = decks[i:i+batch_size]

    # 各デッキ用のタブを作成
    tab_ids = [tabs_create_mcp() for _ in batch]

    # 並列実行
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(collect_from_deck, deck, tab_id)
            for deck, tab_id in zip(batch, tab_ids)
        ]

        # 結果収集
        for future in futures:
            tweets = future.result()
            all_tweets.extend(tweets)

    print(f"バッチ {i//batch_size + 1} 完了: {len(all_tweets)}件")

# 並列実行により、20-30分 → 8-12分に短縮可能
```

---

## パフォーマンス最適化

### 最適化1: デッキ選択の優先度付け

高品質投稿が多いデッキを優先的に収集。

```python
# 優先度順にソート
deck_priority = {
    "AI Leaders #1": 1,
    "AI People #1": 2,
    "AI Companies #1": 3,
    # ...その他のデッキ
}

decks_sorted = sorted(decks, key=lambda d: deck_priority.get(d['deckName'], 99))

# 上位10デッキのみ収集（時間短縮）
decks_to_scan = decks_sorted[:10]
```

### 最適化2: 早期終了条件

目標件数（20件）達成時点で収集を停止。

```python
# 20件のAI関連高エンゲージメント投稿が集まったら終了
if len(ai_related_tweets) >= 20:
    print(f"目標達成: {len(ai_related_tweets)}件収集完了")
    break
```

### 最適化3: キャッシング

前日収集した投稿は再収集せず、キャッシュから読み込み。

```python
import datetime

yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
cache_file = f"Flow/{yesterday[:7]}/{yesterday}/deck_timeline_{yesterday}.json"

if os.path.exists(cache_file):
    with open(cache_file, 'r') as f:
        cached_tweets = json.load(f)['tweets']

    # 24時間以内の投稿はキャッシュから除外（新規のみ収集）
    all_tweets = [t for t in all_tweets if t['url'] not in [c['url'] for c in cached_tweets]]
```

---

## 検証項目

Phase 1完了時に以下を確認:

- [ ] 16個のデッキから投稿を収集できたか
- [ ] 合計320-480件の投稿を取得できたか
- [ ] インプレッション数10万以上の投稿をフィルタできたか
- [ ] AI関連判定で適切にフィルタできたか（LLM判定）
- [ ] 上位10-20件の投稿を選定できたか
- [ ] 出力ファイル（`deck_timeline_{date}.json`, `deck_top_tweets_{date}.json`）が生成されたか
- [ ] エラー発生時に適切にリトライ・フォールバックできたか

---

## 次のステップ

Phase 1完了後、Phase 2（コンテンツ分析）に進む:
- 上位10-20件の投稿詳細を取得（全文・画像・動画）
- リプライ分析でエンゲージメント理解
- Web調査で解説文の素材収集

**次のPhase**: `phases/phase2_content_analysis.md`

---

## 参照

- **メインSkill定義**: `../SKILL.md`
- **設定ファイル**: `../repost_config.json`
- **検索クエリ**: `../deck_search_queries.json`
- **既存スキル（流用）**: `.claude/skills/sns-automation/collect-x-timeline/`
- **Chrome MCP公式**: https://anthropic.com/claude-in-chrome
