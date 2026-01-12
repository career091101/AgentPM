# Phase 3: リポスト投稿生成

## 概要

Phase 2で収集した投稿詳細と調査結果を基に、takano式（高野メソッド）解説文付きリポスト投稿を生成するフェーズ。

**所要時間**: 30-40分
**並列化**: 可能（投稿毎に並列実行）
**推奨モデル**: sonnet（高品質な文章生成にバランス重視）

---

## 目的

1. takano式解説文（700-1500字）を自動生成
2. 高野メソッド7要素をすべて満たす（70点以上必須）
3. URL埋め込み方式でリポスト投稿JSONを生成
4. 4-6件の最終投稿案を選定

---

## 入力ファイル

### `tweet_details_full_{date}.json`

投稿詳細データ（Phase 2出力）。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/tweet_details_full_{date}.json`

### `reply_insights_{date}.json`

リプライ分析結果（Phase 2出力）。

### `research_findings_{date}.json`

Web調査結果（Phase 2出力）。

---

## 処理フロー

### STEP 1: 投稿選定（4-6件）

エンゲージメント順に上位4-6件を選定。

```python
import json

# Phase 2出力読み込み
with open('Flow/{date_path}/tweet_details_full_{date}.json', 'r') as f:
    tweet_details = json.load(f)

with open('Flow/{date_path}/reply_insights_{date}.json', 'r') as f:
    reply_insights = json.load(f)

with open('Flow/{date_path}/research_findings_{date}.json', 'r') as f:
    research_findings = json.load(f)

# repost_config.jsonから最終選定数読み込み
with open('.claude/skills/x-deck-repost-automation/repost_config.json', 'r') as f:
    config = json.load(f)

final_selection = config['data_collection']['final_selection']  # 6

# 上位6件を選定
selected_tweets = tweet_details['tweets'][:final_selection]

print(f"最終選定: {len(selected_tweets)}件")
```

### STEP 2: takano式解説文生成

**テンプレート参照**: `../takano_repost_template.md`

#### 2.1 プロンプト構築

各投稿に対して、takano式テンプレートに基づくプロンプトを構築。

```python
# takano_repost_template.mdを読み込み
with open('.claude/skills/x-deck-repost-automation/takano_repost_template.md', 'r') as f:
    template = f.read()

repost_drafts = []

for tweet in selected_tweets:
    # リプライ分析・Web調査結果を統合
    reply_insight = next((r for r in reply_insights['insights'] if r['tweet_url'] == tweet['url']), {})
    research_finding = next((r for r in research_findings['findings'] if r['tweet_url'] == tweet['url']), {})

    # プロンプト生成
    prompt = f"""
{template}

## 元ツイート情報

**投稿者**: @{tweet['author']} ({tweet['author_name']})
**URL**: {tweet['url']}
**エンゲージメント**: {tweet['impressions']:,}インプレッション、{tweet['likes']:,}いいね、{tweet['retweets']:,}RT

**全文**:
---
{tweet['full_text']}
---

**添付メディア**: {json.dumps(tweet.get('media_items', []), ensure_ascii=False)}

**リプライ分析結果**:
{json.dumps(reply_insight.get('insights', {}), indent=2, ensure_ascii=False)}

**Web調査結果**:
{json.dumps(research_finding.get('findings', {}), indent=2, ensure_ascii=False)}

## 作成指示

上記の情報を基に、takano式解説文（700-1500字）を生成してください。

**重要**:
- 高野メソッド7要素（Hook/Data/Empathy/Insight/Advice/Question/Proper nouns）を必ず満たす
- 総合点70点以上を目指す
- カジュアル・親しみやすいトーン（「マジで」「ヤバい」断定型）
- CEO・経営者向けのビジネス戦略観点
- 固有名詞10個以上、数値5個以上必須

**出力フォーマット**:
以下の形式で1案のみ出力してください。

---

## X長文リポスト投稿案（パターンX: [選択したパターン名]）

**トピック**: [元ツイートの要約タイトル]

---

[takano式解説文（700-1500字）]

🔗 元の投稿: {tweet['url']}

---

## 品質チェック（自己評価）

| 要素 | 配点 | 自己評価 | 確認項目 |
|------|------|---------|---------|
| Hook | 15点 | X/15点 | 冒頭で注意を引けているか |
| Data/Evidence | 20点 | X/20点 | 数値5個以上、企業名3社以上 |
| Empathy | 10点 | X/10点 | CEO向け共感要素 |
| Insight | 15点 | X/15点 | 「つまり」「ポイントは」で洞察 |
| Advice | 10点 | X/10点 | 具体的行動提案 |
| Question ending | 15点 | X/15点 | CEO向け問いかけ |
| Proper nouns | 15点 | X/15点 | 固有名詞10個以上 |
| **総合点** | **100点** | **X/100点** | **70点以上で合格** |

**文字数**: {{実際の文字数}}字（目標: 700-1500字）

**固有名詞リスト**: [使用した固有名詞10個以上]

---
    """

    # LLM実行（takano式解説文生成）
    generated_content = llm_generate(
        prompt=prompt,
        model="sonnet",
        temperature=0.7,
        max_tokens=4000
    )

    repost_drafts.append({
        'tweet_url': tweet['url'],
        'tweet_rank': tweet['rank'],
        'generated_content': generated_content
    })

print(f"解説文生成完了: {len(repost_drafts)}件")
```

#### 2.2 品質チェック（70点以上必須）

生成された解説文の品質を自動評価。

```python
approved_drafts = []

for draft in repost_drafts:
    content = draft['generated_content']

    # 品質チェック表をパース
    quality_check = parse_quality_check(content)

    if quality_check['total_score'] >= 70:
        draft['quality_score'] = quality_check['total_score']
        draft['quality_details'] = quality_check
        approved_drafts.append(draft)
        print(f"✓ Rank {draft['tweet_rank']}: {quality_check['total_score']}点 - 合格")
    else:
        print(f"✗ Rank {draft['tweet_rank']}: {quality_check['total_score']}点 - 不合格（再生成）")
        # 再生成ロジック（後述）

print(f"合格投稿: {len(approved_drafts)}件")
```

#### 2.3 不合格時の再生成

70点未満の場合、プロンプト改善して再生成（最大2回）。

```python
def regenerate_with_feedback(draft, max_retries=2):
    """品質不足時の再生成"""
    quality_score = parse_quality_check(draft['generated_content'])['total_score']

    for retry in range(1, max_retries + 1):
        if quality_score >= 70:
            return draft

        # 不足要素を特定
        weak_elements = [
            elem for elem, score in quality_score['details'].items()
            if score < elem['threshold']
        ]

        # フィードバックプロンプト
        feedback_prompt = f"""
前回の生成結果が品質基準（70点）を満たしていませんでした。

**前回の総合点**: {quality_score}点

**不足要素**:
{json.dumps(weak_elements, indent=2, ensure_ascii=False)}

**改善指示**:
- {weak_elements[0]}: [具体的な改善方法]
- {weak_elements[1]}: [具体的な改善方法]

上記を踏まえ、takano式解説文を再生成してください。
        """

        # 再生成
        regenerated = llm_generate(
            prompt=original_prompt + "\n\n" + feedback_prompt,
            model="sonnet",
            temperature=0.7,
            max_tokens=4000
        )

        draft['generated_content'] = regenerated
        quality_score = parse_quality_check(regenerated)['total_score']

        print(f"  再生成 {retry}回目: {quality_score}点")

    return draft
```

### STEP 3: リポスト投稿JSON生成

**Late API仕様**: URL埋め込み方式（引用リポスト未対応のため）

```python
import datetime

# 投稿時間帯設定読み込み
time_slots = config['posting']['time_slots']

# スケジュール生成（翌日の投稿時間）
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
tomorrow_str = tomorrow.strftime('%Y-%m-%d')

schedule = []
for slot_config in time_slots:
    for time_str in slot_config['slots']:
        schedule.append(f"{tomorrow_str}T{time_str}:00+09:00")

# 投稿JSON生成
repost_posts = []

for i, draft in enumerate(approved_drafts[:6]):  # 最大6件
    # takano式解説文を抽出（品質チェック表の前まで）
    content_text = extract_content_text(draft['generated_content'])

    # URL埋め込み
    url_embed = f"\n\n🔗 元の投稿: {draft['tweet_url']}"
    full_content = content_text + url_embed

    # Late API仕様準拠のJSON
    post_json = {
        "content": full_content,
        "platforms": [
            {
                "platform": "twitter",
                "accountId": "LATE_TWITTER_ACCOUNT_ID"  # 環境変数から取得
            }
        ],
        "scheduledFor": schedule[i] if i < len(schedule) else schedule[-1],
        "timezone": "Asia/Tokyo"
    }

    repost_posts.append({
        'tweet_url': draft['tweet_url'],
        'tweet_rank': draft['tweet_rank'],
        'quality_score': draft['quality_score'],
        'scheduled_time': schedule[i] if i < len(schedule) else schedule[-1],
        'post_json': post_json
    })

print(f"投稿JSON生成完了: {len(repost_posts)}件")
```

---

## 出力ファイル

### `repost_drafts_{date}.json`

リポスト投稿案（4-6件）。

**ファイルパス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/repost_drafts_{date}.json`

**データ構造**:
```json
{
  "generated_at": "2026-01-12T14:00:00+09:00",
  "total_drafts": 6,
  "drafts": [
    {
      "tweet_url": "https://x.com/username/status/123456789",
      "tweet_rank": 1,
      "quality_score": 85,
      "quality_details": {
        "hook": 14,
        "data_evidence": 19,
        "empathy": 9,
        "insight": 14,
        "advice": 9,
        "question_ending": 14,
        "proper_nouns": 14,
        "total": 85
      },
      "scheduled_time": "2026-01-13T07:30:00+09:00",
      "post_json": {
        "content": "[takano式解説文]\n\n🔗 元の投稿: https://x.com/username/status/123456789",
        "platforms": [
          {
            "platform": "twitter",
            "accountId": "LATE_TWITTER_ACCOUNT_ID"
          }
        ],
        "scheduledFor": "2026-01-13T07:30:00+09:00",
        "timezone": "Asia/Tokyo"
      },
      "generated_content_full": "[完全な生成結果テキスト]"
    },
    ...
  ],
  "rejected_drafts": [
    {
      "tweet_rank": 7,
      "quality_score": 65,
      "reason": "総合点70点未満、2回再生成後も基準未達"
    }
  ]
}
```

---

## エラーハンドリング

### エラー1: 品質基準未達（70点未満）

**対策**: 最大2回再生成、それでも不合格なら次の投稿に進む

```python
for draft in repost_drafts:
    # 初回生成
    quality_score = check_quality(draft)

    if quality_score < 70:
        # 再生成（最大2回）
        draft = regenerate_with_feedback(draft, max_retries=2)

        if check_quality(draft) >= 70:
            approved_drafts.append(draft)
        else:
            # 不合格記録
            rejected_drafts.append({
                'tweet_rank': draft['tweet_rank'],
                'quality_score': check_quality(draft),
                'reason': '2回再生成後も品質基準未達'
            })
```

### エラー2: 文字数超過・不足

**エラー**: 700字未満または1500字超過

```python
# 対策: 文字数調整プロンプト
if len(content_text) < 700:
    adjustment_prompt = f"""
現在{len(content_text)}字です。700字以上に拡充してください。

**追加指示**:
- Data/Evidence セクションに具体例を追加
- Insight セクションで洞察を深掘り
    """
elif len(content_text) > 1500:
    adjustment_prompt = f"""
現在{len(content_text)}字です。1500字以内に要約してください。

**削減指示**:
- 重複表現を削除
- 冗長な説明を簡潔化
    """
```

### エラー3: 固有名詞・数値不足

**エラー**: 固有名詞10個未満、数値5個未満

```python
# 対策: 不足要素の補完プロンプト
if proper_nouns_count < 10:
    supplement_prompt = f"""
現在の固有名詞: {proper_nouns_count}個（目標: 10個以上）

**追加指示**:
- 関連企業名を追加（Google, Microsoft, OpenAI等）
- 人名を追加（サム・アルトマン、サティア・ナデラ等）
- 製品名を追加（ChatGPT, Azure, DeepMind等）
    """

if numbers_count < 5:
    supplement_prompt += f"""
現在の数値データ: {numbers_count}個（目標: 5個以上）

**追加指示**:
- 金額データを追加
- 成長率を追加
- ユーザー数・市場規模を追加
    """
```

---

## 並列化戦略

### 投稿毎の並列生成

6件の投稿を並列生成（最大5並列）。

**実装例**:
```python
from concurrent.futures import ThreadPoolExecutor

def generate_repost_for_tweet(tweet, reply_insight, research_finding):
    """1つの投稿のリポスト解説文を生成"""
    # プロンプト構築
    # LLM実行
    # 品質チェック
    # 再生成（必要時）
    return draft

# 並列実行
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [
        executor.submit(
            generate_repost_for_tweet,
            tweet,
            get_reply_insight(tweet['url']),
            get_research_finding(tweet['url'])
        )
        for tweet in selected_tweets
    ]

    # 結果収集
    repost_drafts = [future.result() for future in futures]

# 並列実行により、30-40分 → 12-16分に短縮可能
```

---

## パフォーマンス最適化

### 最適化1: プロンプトキャッシング

同一テンプレートを再利用（Anthropic Prompt Caching）。

```python
# takano_repost_template.mdをキャッシュ
cached_template = cache_prompt(template)

# 各投稿で再利用
for tweet in selected_tweets:
    prompt = build_prompt(cached_template, tweet, ...)
```

### 最適化2: 品質チェックの自動パース

生成結果からJSON形式で品質スコアを抽出。

```python
def parse_quality_check(generated_content):
    """品質チェック表をパースしてJSONに変換"""
    # テーブル部分を抽出
    table_match = re.search(r'\| 要素 \| 配点 \| 自己評価 \|.*?\| \*\*総合点\*\* \| \*\*100点\*\* \| \*\*(\d+)/100点\*\*', generated_content, re.DOTALL)

    if not table_match:
        return {'total_score': 0, 'details': {}}

    total_score = int(table_match.group(1))

    # 各要素のスコアを抽出
    # ...

    return {
        'total_score': total_score,
        'details': {...}
    }
```

---

## 検証項目

Phase 3完了時に以下を確認:

- [ ] takano式解説文（700-1500字）を生成できたか
- [ ] 高野メソッド7要素をすべて満たしたか
- [ ] 総合点70点以上の投稿を4-6件生成できたか
- [ ] URL埋め込み方式のLate API JSON形式で出力できたか
- [ ] 固有名詞10個以上、数値5個以上を含むか
- [ ] 不合格投稿の再生成ロジックが動作したか
- [ ] 出力ファイル（`repost_drafts_{date}.json`）が生成されたか

---

## takano式7要素の実装チェックリスト

### 1. Hook（15点）

- [ ] 衝撃的数字を冒頭に配置
- [ ] 企業名を明記
- [ ] 断定型の文体（「〜だ。」「〜である。」）
- [ ] 100-150字の範囲内

### 2. Data/Evidence（20点）

- [ ] 具体的数値5個以上
- [ ] 企業名3社以上
- [ ] 出典明記（元ツイート、記事、レポート）
- [ ] 300-500字の範囲内

### 3. Empathy（10点）

- [ ] CEO・経営者の痛み・不安・欲求に言及
- [ ] 「CEOなら〜」「経営者なら〜」の共感喚起

### 4. Insight（15点）

- [ ] 「つまり」「ポイントは」で自己解釈
- [ ] 3つのポイントで構造化
- [ ] 200-400字の範囲内

### 5. Advice（10点）

- [ ] 具体的な行動提案3つ
- [ ] 「今すぐできること」「次の一手」を明示

### 6. Question ending（15点）

- [ ] CEO向け問いかけで締めくくる
- [ ] 「あなたはどう思う？」「生き残れる？」
- [ ] 100-200字の範囲内

### 7. Proper nouns（15点）

- [ ] 固有名詞10個以上使用
- [ ] 企業名、サービス名、人名、製品名等

---

## 次のステップ

Phase 3完了後、Phase 4（Late API予約投稿）に進む:
- Late API経由で4-6投稿を予約投稿
- エラーハンドリング（指数バックオフリトライ）
- 投稿結果レポート生成

**次のPhase**: `phases/phase4_late_api_scheduling.md`

---

## 参照

- **メインSkill定義**: `../SKILL.md`
- **takano式テンプレート**: `../takano_repost_template.md`
- **設定ファイル**: `../repost_config.json`
- **既存プロンプト**: `Stock/programs/副業/projects/SNS/投稿文作成用プロンプト_v6_takano_refined`
- **Anthropic Prompt Caching**: https://docs.anthropic.com/en/docs/prompt-caching
