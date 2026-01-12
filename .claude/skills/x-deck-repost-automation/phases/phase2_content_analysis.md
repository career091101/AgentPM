# Phase 2: コンテンツ分析

## 概要

Phase 1で選定した上位10-20件の投稿に対して詳細分析を実施し、takano式解説文作成のための素材を収集するフェーズ。

**所要時間**: 20-30分
**並列化**: 可能（投稿毎に並列実行）
**推奨モデル**: sonnet（分析・調査にバランス重視）

---

## 目的

1. 投稿の全文取得（「さらに表示」クリックで省略部分展開）
2. 画像・動画のマルチモーダルキャプチャ
3. リプライ分析によるエンゲージメント理解
4. Web調査による最新情報・ファクトチェック・専門家意見収集

---

## 入力ファイル

### `deck_top_tweets_{date}.json`

Phase 1で選定した上位投稿（10-20件）。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/deck_top_tweets_{date}.json`

**使用データ**:
```json
{
  "tweets": [
    {
      "rank": 1,
      "url": "https://x.com/username/status/123456789",
      "text": "Tweet text (省略されている可能性あり)...",
      "impressions": 1500000,
      "likes": 25000,
      "retweets": 3500,
      "ai_score": 3
    },
    ...
  ]
}
```

---

## 処理フロー

### STEP 1: 投稿詳細取得（全文・画像・動画）

#### 1.1 全文取得（「さらに表示」クリック）

X投稿は280字を超えると「さらに表示」ボタンで省略される。Claude in Chrome MCPで自動展開。

```python
# Chrome MCP初期化
tabs_context_mcp(createIfEmpty=True)
tab_id = tabs_create_mcp()

full_tweets = []

for tweet in top_tweets:
    navigate(url=tweet['url'], tabId=tab_id)
    wait(duration=2)  # ページロード待機

    # 「さらに表示」ボタンを検索
    show_more_btn = find(query="さらに表示", tabId=tab_id)

    if show_more_btn:
        # ボタンをクリックして全文展開
        left_click(ref=show_more_btn[0]['ref'], tabId=tab_id)
        wait(duration=0.5)

    # 全文取得
    full_text = javascript_tool(
        action="javascript_exec",
        text="""
        const tweetTextEl = document.querySelector('[data-testid="tweetText"]');
        tweetTextEl ? tweetTextEl.innerText : '';
        """,
        tabId=tab_id
    )

    tweet['full_text'] = full_text

    # スクリーンショット保存（全文表示状態）
    screenshot_path = f"Flow/{date_path}/screenshots/tweet_{tweet['rank']}_full.png"
    screenshot_result = screenshot(tabId=tab_id)
    # screenshot_resultのimageIdを保存
    tweet['screenshot_id'] = screenshot_result['imageId']

    full_tweets.append(tweet)

print(f"全文取得完了: {len(full_tweets)}件")
```

#### 1.2 画像・動画取得

```python
for tweet in full_tweets:
    navigate(url=tweet['url'], tabId=tab_id)
    wait(duration=1)

    # 画像・動画要素を検索
    media_elements = find(query="image or video in tweet", tabId=tab_id)

    tweet['media_items'] = []

    for media_el in media_elements[:4]:  # 最大4個まで
        # メディアタイプ判定
        media_type = javascript_tool(
            action="javascript_exec",
            text=f"""
            const el = document.querySelector('[data-ref-id="{media_el['ref']}"]');
            if (el.tagName === 'IMG') return 'image';
            if (el.tagName === 'VIDEO') return 'video';
            return 'unknown';
            """,
            tabId=tab_id
        )

        if media_type == 'image':
            # 画像URL取得
            img_url = javascript_tool(
                action="javascript_exec",
                text=f"""
                const el = document.querySelector('[data-ref-id="{media_el['ref']}"]');
                el.src;
                """,
                tabId=tab_id
            )
            tweet['media_items'].append({
                'type': 'image',
                'url': img_url
            })

        elif media_type == 'video':
            # 動画のサムネイル取得
            video_thumbnail = screenshot(tabId=tab_id)
            tweet['media_items'].append({
                'type': 'video',
                'thumbnail_id': video_thumbnail['imageId'],
                'note': 'Video content - screenshot captured'
            })

print(f"メディア取得完了")
```

### STEP 2: リプライ分析（エンゲージメント理解）

**既存スキル流用**: `.claude/skills/sns-automation/analyze-replies.md`

上位3-5件の高エンゲージメントリプライを分析し、投稿への反応（共感・批判・質問・追加情報）を理解。

```python
reply_insights = []

for tweet in full_tweets[:10]:  # 上位10件のみ（時間短縮）
    navigate(url=tweet['url'], tabId=tab_id)
    wait(duration=2)

    # リプライセクションまでスクロール
    scroll(scroll_direction="down", scroll_amount=3, tabId=tab_id)
    wait(duration=1)

    # 上位5件のリプライ取得
    replies = javascript_tool(
        action="javascript_exec",
        text="""
        const replyEls = document.querySelectorAll('article[data-testid="tweet"]');
        const replies = [];

        replyEls.forEach((el, index) => {
            if (index === 0) return;  // 最初は元ツイート
            if (index > 5) return;  // 上位5件まで

            const textEl = el.querySelector('[data-testid="tweetText"]');
            const authorEl = el.querySelector('[data-testid="User-Name"]');
            const likesEl = el.querySelector('[data-testid="like"]');

            replies.push({
                text: textEl ? textEl.innerText : '',
                author: authorEl ? authorEl.innerText : '',
                likes: likesEl ? parseInt(likesEl.getAttribute('aria-label').match(/\\d+/)[0]) : 0
            });
        });

        replies;
        """,
        tabId=tab_id
    )

    # LLM分析: リプライの反応ポイント抽出
    reply_analysis = llm_analyze(
        prompt=f"""
以下のリプライから、元ツイートへの反応ポイントを4つのカテゴリで分類してください。

**元ツイート**: {tweet['full_text'][:200]}...

**リプライ一覧**:
{json.dumps(replies, indent=2, ensure_ascii=False)}

**分類カテゴリ**:
1. 共感（Empathy）: 「同感」「その通り」等の同意
2. 批判（Criticism）: 反論・懸念・疑問
3. 質問（Questions）: 追加情報・詳細を求める質問
4. 追加情報（Additional Info）: 補足データ・関連事例

**出力形式**（JSON）:
{{
  "empathy": ["共感ポイント1", "共感ポイント2"],
  "criticism": ["批判ポイント1"],
  "questions": ["質問1", "質問2"],
  "additional_info": ["追加情報1"]
}}
        """,
        model="sonnet"
    )

    tweet['reply_insights'] = reply_analysis
    reply_insights.append({
        'tweet_url': tweet['url'],
        'insights': reply_analysis
    })

print(f"リプライ分析完了: {len(reply_insights)}件")
```

### STEP 3: Web調査（最新情報・ファクトチェック・専門家意見）

**既存スキル流用**: `.claude/skills/sns-automation/research-topic.md`

各投稿のトピックについて、最新ニュース・ファクトチェック・専門家意見を2倍の調査量で収集。

```python
research_findings = []

for tweet in full_tweets[:10]:  # 上位10件のみ
    # トピック抽出（LLM）
    topic = llm_extract_topic(
        prompt=f"""
以下のツイートからメイントピックを抽出してください（10単語以内）。

**ツイート**: {tweet['full_text']}

**出力**: [トピック名]
        """,
        model="sonnet"
    )

    # Web調査実行（WebSearchツール使用）
    # 1. 最新ニュース検索
    latest_news = WebSearch(
        query=f"{topic['topic']} AI 2026 latest news",
        limit=5
    )

    # 2. ファクトチェック検索
    fact_check = WebSearch(
        query=f"{topic['topic']} fact check verification",
        limit=3
    )

    # 3. 専門家意見検索
    expert_opinions = WebSearch(
        query=f"{topic['topic']} expert analysis opinion",
        limit=3
    )

    # 各検索結果の詳細取得（WebFetch）
    detailed_findings = []

    for news in latest_news[:3]:  # 上位3件のみ詳細取得
        content = WebFetch(
            url=news['url'],
            prompt=f"""
以下の記事から、{topic['topic']}に関する重要な情報を抽出してください。

**抽出項目**:
- 主要な数値データ（金額、成長率、ユーザー数等）
- 関連企業名
- 専門家のコメント
- 今後の見通し

**出力形式**（箇条書き）:
- [情報1]
- [情報2]
...
            """
        )
        detailed_findings.append({
            'source': news['title'],
            'url': news['url'],
            'findings': content
        })

    tweet['research_findings'] = {
        'topic': topic['topic'],
        'latest_news': detailed_findings,
        'fact_check_results': fact_check,
        'expert_opinions': expert_opinions
    }

    research_findings.append({
        'tweet_url': tweet['url'],
        'topic': topic['topic'],
        'findings': tweet['research_findings']
    })

    # レート制限回避
    wait(duration=1)

print(f"Web調査完了: {len(research_findings)}件")
```

---

## 出力ファイル

### `tweet_details_full_{date}.json`

投稿詳細データ（全文・画像・動画含む）。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/tweet_details_full_{date}.json`

**データ構造**:
```json
{
  "analyzed_at": "2026-01-12T12:00:00+09:00",
  "total_tweets": 10,
  "tweets": [
    {
      "rank": 1,
      "url": "https://x.com/username/status/123456789",
      "full_text": "Complete tweet text with no truncation...",
      "screenshot_id": "img_12345",
      "media_items": [
        {
          "type": "image",
          "url": "https://pbs.twimg.com/media/..."
        },
        {
          "type": "video",
          "thumbnail_id": "img_67890",
          "note": "Video content - screenshot captured"
        }
      ],
      "impressions": 1500000,
      "likes": 25000,
      "retweets": 3500,
      "author": "@username",
      "author_name": "Author Name",
      "posted_at": "2026-01-11T15:30:00Z"
    },
    ...
  ]
}
```

### `reply_insights_{date}.json`

リプライ分析結果。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/reply_insights_{date}.json`

**データ構造**:
```json
{
  "analyzed_at": "2026-01-12T12:30:00+09:00",
  "total_analyzed": 10,
  "insights": [
    {
      "tweet_url": "https://x.com/username/status/123456789",
      "insights": {
        "empathy": [
          "『早期投資の重要性』に多くの経営者が共感",
          "AIへの投資タイミングに関する不安が共通"
        ],
        "criticism": [
          "後発組でも勝算はあるとの反論"
        ],
        "questions": [
          "具体的な投資先の選定基準は？",
          "中小企業でも実践可能なAI活用方法は？"
        ],
        "additional_info": [
          "GoogleのDeepMind買収後の成果に関する補足",
          "Microsoftの最新AI投資動向"
        ]
      }
    },
    ...
  ]
}
```

### `research_findings_{date}.json`

Web調査結果。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/research_findings_{date}.json`

**データ構造**:
```json
{
  "researched_at": "2026-01-12T13:00:00+09:00",
  "total_topics": 10,
  "findings": [
    {
      "tweet_url": "https://x.com/username/status/123456789",
      "topic": "OpenAI 投資ラウンド評価額",
      "findings": {
        "latest_news": [
          {
            "source": "TechCrunch - OpenAI新ラウンド発表",
            "url": "https://techcrunch.com/...",
            "findings": "- 評価額1570億ドル\n- Sequoia Capital主導\n- 年間売上100億ドル見込み"
          },
          ...
        ],
        "fact_check_results": [
          {
            "title": "OpenAI評価額の真偽検証",
            "url": "https://factcheck.org/...",
            "summary": "評価額は公式発表に基づく正確な数値"
          }
        ],
        "expert_opinions": [
          {
            "title": "AI投資専門家の見解 - a16z",
            "url": "https://a16z.com/...",
            "summary": "AIスタートアップへの早期投資は今後も高リターンが期待される"
          }
        ]
      }
    },
    ...
  ]
}
```

---

## エラーハンドリング

### エラー1: 「さらに表示」ボタンが見つからない

**エラー**: findツールで「さらに表示」が検出できない

```python
# 対策: ボタン無し = 全文がすでに表示されている
show_more_btn = find(query="さらに表示", tabId=tab_id)

if not show_more_btn:
    # すでに全文表示されている
    full_text = javascript_tool(
        action="javascript_exec",
        text="""
        const tweetTextEl = document.querySelector('[data-testid="tweetText"]');
        tweetTextEl ? tweetTextEl.innerText : '';
        """,
        tabId=tab_id
    )
else:
    # ボタンをクリックして展開
    left_click(ref=show_more_btn[0]['ref'], tabId=tab_id)
    wait(duration=0.5)
    # 全文取得
```

### エラー2: リプライ取得失敗

**エラー**: リプライが非表示・制限されている

```python
# 対策: リプライ無しとして処理
try:
    replies = javascript_tool(...)
except Exception as e:
    print(f"リプライ取得失敗: {e}")
    tweet['reply_insights'] = {
        'note': 'Replies not accessible',
        'empathy': [],
        'criticism': [],
        'questions': [],
        'additional_info': []
    }
```

### エラー3: Web調査でのレート制限

**エラー**: WebSearchまたはWebFetchがレート制限に引っかかる

```python
# 対策: 指数バックオフリトライ
import time

def web_search_with_retry(query, retries=3):
    for i in range(retries):
        try:
            return WebSearch(query=query)
        except RateLimitError:
            wait_time = 2 ** i  # 1秒 → 2秒 → 4秒
            print(f"レート制限検出、{wait_time}秒待機...")
            time.sleep(wait_time)

    # 3回失敗したらスキップ
    return []
```

---

## 並列化戦略

### 投稿毎の並列実行

10-20件の投稿を5つずつバッチ処理で並列実行（最大5並列）。

**実装例**:
```python
from concurrent.futures import ThreadPoolExecutor

def analyze_tweet(tweet, tab_id):
    """1つの投稿を詳細分析"""
    # STEP 1: 全文・画像取得
    # STEP 2: リプライ分析
    # STEP 3: Web調査
    return analyzed_tweet

# 5投稿ずつ並列実行
batch_size = 5
analyzed_tweets = []

for i in range(0, len(full_tweets), batch_size):
    batch = full_tweets[i:i+batch_size]

    # 各投稿用のタブを作成
    tab_ids = [tabs_create_mcp() for _ in batch]

    # 並列実行
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(analyze_tweet, tweet, tab_id)
            for tweet, tab_id in zip(batch, tab_ids)
        ]

        # 結果収集
        for future in futures:
            result = future.result()
            analyzed_tweets.append(result)

    print(f"バッチ {i//batch_size + 1} 完了: {len(analyzed_tweets)}件")

# 並列実行により、20-30分 → 8-12分に短縮可能
```

---

## パフォーマンス最適化

### 最適化1: 上位投稿のみ詳細分析

全20件ではなく、上位10件のみ詳細分析（リプライ分析・Web調査）。

```python
# 上位10件のみ詳細分析
detailed_tweets = full_tweets[:10]

# 残り10件は全文・画像取得のみ
lightweight_tweets = full_tweets[10:]
```

### 最適化2: Web調査の範囲限定

各トピックで取得する記事数を制限。

```python
# 最新ニュース: 3件
# ファクトチェック: 1件
# 専門家意見: 2件

latest_news = WebSearch(query=..., limit=3)
fact_check = WebSearch(query=..., limit=1)
expert_opinions = WebSearch(query=..., limit=2)
```

### 最適化3: キャッシング

同一トピックのWeb調査結果をキャッシュ。

```python
research_cache = {}

topic_key = topic['topic']
if topic_key in research_cache:
    tweet['research_findings'] = research_cache[topic_key]
else:
    # Web調査実行
    findings = perform_web_research(topic)
    research_cache[topic_key] = findings
    tweet['research_findings'] = findings
```

---

## 検証項目

Phase 2完了時に以下を確認:

- [ ] 上位10-20件の投稿の全文を取得できたか
- [ ] 「さらに表示」クリックで省略部分を展開できたか
- [ ] 画像・動画のマルチモーダルキャプチャができたか
- [ ] リプライ分析で4カテゴリ（共感・批判・質問・追加情報）を抽出できたか
- [ ] Web調査で最新情報・ファクトチェック・専門家意見を収集できたか
- [ ] 出力ファイル（`tweet_details_full_{date}.json`, `reply_insights_{date}.json`, `research_findings_{date}.json`）が生成されたか
- [ ] エラー発生時に適切にリトライ・スキップできたか

---

## 次のステップ

Phase 2完了後、Phase 3（リポスト投稿生成）に進む:
- takano式解説文（700-1500字）を生成
- 高野メソッド7要素チェック（70点以上）
- リポスト投稿JSON生成

**次のPhase**: `phases/phase3_repost_generation.md`

---

## 参照

- **メインSkill定義**: `../SKILL.md`
- **takano式テンプレート**: `../takano_repost_template.md`
- **既存スキル（リプライ分析）**: `.claude/skills/sns-automation/analyze-replies/`
- **既存スキル（Web調査）**: `.claude/skills/sns-automation/research-topic/`
- **Chrome MCP公式**: https://anthropic.com/claude-in-chrome
