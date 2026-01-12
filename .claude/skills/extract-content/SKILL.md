---
name: extract-content
description: |
  ツイート詳細データから記事・YouTube・PDFリンクのコンテンツを抽出するスキル。
  ClaudeCode LLMが直接WebFetch/Readツールを使用してコンテンツを取得・解析します。

  使用タイミング：
  - SNS投稿作成の事前調査時
  - 参照記事の要約が必要な時
  - リンク先の詳細情報を取得したい時

  所要時間：5-10分（リンク数に依存）
  出力：extracted_contents_ai_{YYYYMMDD}.json
trigger_keywords:
  - "コンテンツ抽出"
  - "記事抽出"
  - "リンク先抽出"
  - "extract content"
stage: Phase 2 - Content Extraction
dependencies: ["scrape-tweet-details"]
output_file: Stock/programs/副業/projects/SNS/data/extracted_contents_ai_{YYYYMMDD}.json
execution_time: 5-10分
framework_reference: Stock/programs/副業/projects/SNS/
priority: P1
model: claude-haiku-4-5-20251001  # Haiku 4.5 (2026年1月時点の最新モデル)
---

# Extract Content Skill

ツイート詳細から記事・YouTube・PDFのコンテンツを抽出するスキル。

---

## このSkillでできること

1. **記事コンテンツ抽出**: WebFetchツールでHTML解析、タイトル・本文・メタ情報を取得
2. **YouTube動画情報取得**: タイトル・説明文を取得（字幕抽出は今後実装）
3. **PDF情報取得**: メタ情報を取得（全文抽出は今後実装）
4. **複数リンク一括処理**: ツイート詳細内の全リンクを自動処理
5. **AI関連度スコア付与**: 抽出コンテンツにAI関連度（0-3点）を自動判定・付与
6. **エラーハンドリング**: タイムアウト・403エラー等を適切に記録

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | tweet_details_ai_{YYYYMMDD}.json（ツイート詳細+リンク情報） |
| **出力** | extracted_contents_ai_{YYYYMMDD}.json（抽出コンテンツ + AI関連度スコア） |
| **次のアクション** | filter-extracted-content（フィルタリング）、analyze-replies（リプライ分析）、research-topic（Web調査） |

---

## Instructions

**実行モード**: ClaudeCode LLM自律実行
**推定所要時間**: 5-10分（リンク数に依存）

### STEP 1: 入力ファイル読み込み（30秒）

**Readツール使用**:
```
/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/tweet_details_ai_{最新日付}.json
```

**確認項目**:
- ファイル存在確認
- `tweet_details` 配列の読み込み
- 各ツイートの `links` 配列を抽出

**フォールバック**:
- 最新日付ファイルが見つからない場合、`tweet_details_*.json` の最新ファイルを検索

---

### STEP 2: リンク分類（1分）

**全ツイートからリンクを収集**:
```python
# 疑似コード（LLM内で実行）
all_links = []
for tweet in tweet_details:
    for link in tweet['links']:
        all_links.append({
            'tweet_id': tweet['tweet_id'],
            'username': tweet['username'],
            'url': link['url'],
            'type': link['type'],  # article, youtube, pdf, other
            'domain': link['domain']
        })

# タイプ別カウント
link_types = {
    'article': [link for link in all_links if link['type'] == 'article'],
    'youtube': [link for link in all_links if link['type'] == 'youtube'],
    'pdf': [link for link in all_links if link['type'] == 'pdf'],
    'other': [link for link in all_links if link['type'] == 'other']
}
```

**ユーザーに報告**:
```
📊 リンク分類結果
- 記事: X件
- YouTube: Y件
- PDF: Z件
- その他: W件

合計: N件のコンテンツを抽出します。
```

---

### STEP 3: コンテンツ抽出（3-8分）

#### 3A. 記事コンテンツ抽出（WebFetchツール使用）

**各記事URLに対して**:
```
WebFetch(
  url=link['url'],
  prompt="この記事からタイトル、本文（最初の500ワード）、メタディスクリプションを抽出してください。JSONフォーマットで返してください: {title: string, content: string, meta_description: string}"
)
```

**抽出結果の構造化**:
```json
{
  "url": "https://example.com/article",
  "type": "article",
  "title": "記事タイトル",
  "content": "本文の最初の500ワード...",
  "meta_description": "記事の説明",
  "word_count": 450,
  "extracted_at": "2026-01-02T12:00:00",
  "status": "success",
  "tweet_id": "2006...",
  "username": "cb_doge",
  "domain": "example.com"
}
```

**エラーハンドリング**:
- **Timeout**: `status: "timeout"`, `error: "Request timeout"`
- **403 Forbidden**: `status: "forbidden"`, `error: "Access denied"`
- **404 Not Found**: `status: "not_found"`, `error: "Page not found"`
- **その他**: `status: "error"`, `error: error_message`

#### 3B. YouTube動画情報取得

**現在の実装**: 基本情報のみ
```json
{
  "url": "https://youtube.com/watch?v=xxx",
  "type": "youtube",
  "status": "partial",
  "title": "動画タイトル（URLから推測）",
  "note": "字幕抽出は今後実装予定",
  "tweet_id": "2006...",
  "username": "hasan28d"
}
```

**今後の実装**: youtube-transcript-api 使用

#### 3C. PDF情報取得

**現在の実装**: メタ情報のみ
```json
{
  "url": "https://example.com/paper.pdf",
  "type": "pdf",
  "status": "partial",
  "note": "PDF全文抽出は今後実装予定",
  "tweet_id": "2006...",
  "username": "researcher"
}
```

**今後の実装**: pdfplumber + pytesseract 使用

---

### STEP 3.5: AI関連度スコア付与（1-2分）

**判定基準の参照**: `@.claude/skills/_shared/ai_relevance_criteria.md`

#### 3.5A. 各コンテンツのAI関連度判定

**全抽出コンテンツに対して**:

```python
# 疑似コード（LLM内で実行）
for content in extracted_contents:
    if content['status'] != 'success':
        # エラー・パーシャルは0点
        content['ai_relevance_score'] = 0
        content['ai_relevance_reason'] = "抽出失敗"
        continue

    title = content.get('title', '')
    text = content.get('content', '')

    # タイトル優先判定
    score = check_title_keywords(title)

    if score > 0:
        content['ai_relevance_score'] = score
        content['ai_relevance_reason'] = f"タイトルに{score}点キーワード含有"
        continue

    # 本文キーワード密度判定
    score = calculate_keyword_density(text)

    content['ai_relevance_score'] = score

    if score == 3:
        content['ai_relevance_reason'] = "本文にAI技術キーワード含有（密度2%以上）"
    elif score == 2:
        content['ai_relevance_reason'] = "本文にAI企業名含有（密度1%以上）"
    elif score == 1:
        content['ai_relevance_reason'] = "本文にML/データサイエンス含有（密度0.5%以上）"
    else:
        content['ai_relevance_reason'] = "AI関連キーワード不在"
```

#### 3.5B. キーワードマッチング実装

**簡易版実装**（キーワード存在判定）:

```python
# 3点キーワード
keywords_3pt = [
    "LLM", "ChatGPT", "Claude", "GPT", "Gemini", "生成AI",
    "generative AI", "transformer", "neural network",
    "プロンプトエンジニアリング", "RAG", "fine-tuning"
]

# 2点キーワード
keywords_2pt = [
    "OpenAI", "Anthropic", "DeepMind", "Google AI",
    "Microsoft AI", "Meta AI", "機械学習モデル"
]

# 1点キーワード
keywords_1pt = [
    "機械学習", "machine learning", "データサイエンス",
    "data science", "予測モデル"
]

def check_title_keywords(title: str) -> int:
    """タイトルからAI関連度を判定"""
    title_lower = title.lower()

    if any(kw.lower() in title_lower for kw in keywords_3pt):
        return 3
    if any(kw.lower() in title_lower for kw in keywords_2pt):
        return 2
    if any(kw.lower() in title_lower for kw in keywords_1pt):
        return 1

    return 0
```

**詳細な判定基準**: `@.claude/skills/_shared/ai_relevance_criteria.md` を参照

---

### STEP 4: 結果集計（1分）

**統計情報計算**:
```python
# 疑似コード
success_count = len([c for c in extracted if c['status'] == 'success'])
partial_count = len([c for c in extracted if c['status'] == 'partial'])
error_count = len([c for c in extracted if c['status'] in ['timeout', 'forbidden', 'error']])

total_words = sum([c.get('word_count', 0) for c in extracted if c['status'] == 'success'])
avg_words = total_words / success_count if success_count > 0 else 0

success_rate = (success_count / len(all_links)) * 100

# AI関連度スコア集計
score_distribution = {
    '3点': len([c for c in extracted if c.get('ai_relevance_score', 0) == 3]),
    '2点': len([c for c in extracted if c.get('ai_relevance_score', 0) == 2]),
    '1点': len([c for c in extracted if c.get('ai_relevance_score', 0) == 1]),
    '0点': len([c for c in extracted if c.get('ai_relevance_score', 0) == 0])
}

ai_relevant_rate = (sum([score_distribution['3点'], score_distribution['2点'], score_distribution['1点']]) / len(extracted)) * 100 if len(extracted) > 0 else 0
```

---

### STEP 5: 出力ファイル生成（30秒）

**出力JSONフォーマット**:
```json
{
  "metadata": {
    "processed_at": "2026-01-02T12:38:00",
    "source_file": "tweet_details_ai_20260102.json",
    "total_links": 12,
    "success_count": 11,
    "partial_count": 0,
    "error_count": 1,
    "success_rate": 91.7,
    "link_types": {
      "article": 11,
      "youtube": 0,
      "pdf": 1
    },
    "ai_relevance_distribution": {
      "3点": 5,
      "2点": 3,
      "1点": 1,
      "0点": 3
    },
    "ai_relevant_rate": 75.0
  },
  "extracted_contents": [
    {
      "url": "https://...",
      "type": "article",
      "title": "...",
      "content": "...",
      "word_count": 530,
      "status": "success",
      "tweet_id": "...",
      "username": "...",
      "domain": "...",
      "ai_relevance_score": 3,
      "ai_relevance_reason": "タイトルに3点キーワード含有"
    }
  ]
}
```

**保存先**: `Stock/programs/副業/projects/SNS/data/extracted_contents_ai_{YYYYMMDD}.json`

---

### STEP 6: サマリーレポート生成（30秒）

**ユーザーへの報告**:
```
✅ コンテンツ抽出完了

📊 Summary:
  - Total links processed: 12
  - Success: 11 (91.7%)
  - Errors: 1 (8.3%)

📝 Content statistics:
  - Total words extracted: 1,322
  - Average words per article: 120

🎯 AI関連度分布:
  - 3点（高関連度）: 5件 (41.7%)
  - 2点（中関連度）: 3件 (25.0%)
  - 1点（低関連度）: 1件 (8.3%)
  - 0点（非AI関連）: 3件 (25.0%)
  - AI関連率: 75.0%

🏆 Top 3 AI関連コンテンツ:
  1. [3点] ChatGPT-4のRAG実装パターン (530 words)
  2. [3点] Claude 3.5プロンプトエンジニアリング (412 words)
  3. [2点] OpenAI新モデル発表 (298 words)

💾 Output: extracted_contents_ai_20260102.json (35KB)

📌 Next: filter-extracted-content（フィルタリング）、analyze-replies（リプライ分析）、research-topic（Web調査）
```

---

## エラーハンドリング

### WebFetchタイムアウト
- **原因**: サーバー応答遅延、ネットワーク不安定
- **対応**: `status: "timeout"` で記録、次のリンクへ進む
- **リトライ**: なし（時間効率優先）

### 403 Forbidden
- **原因**: User-Agent制限、アクセス制限
- **対応**: `status: "forbidden"` で記録、次のリンクへ進む
- **例**: help.x.com（X公式ヘルプはアクセス制限あり）

### コンテンツ抽出失敗
- **原因**: HTML構造が予測外
- **対応**: `content: ""`, `word_count: 0` で記録
- **ログ**: `status: "success"` だが `word_count: 0` の場合は警告

---

## データ品質保証

| 品質指標 | 目標 | 実績（2026-01-02） |
|---------|------|------------------|
| **成功率** | ≥80% | 91.7% (11/12) |
| **総抽出ワード数** | ≥500 | 1,322 |
| **平均ワード数/記事** | ≥50 | 120 |
| **AI関連率** | ≥60% | 75.0% (9/12) |
| **高関連度（3点）比率** | ≥30% | 41.7% (5/12) |

---

## 使用例

### 基本的な使用

```
User: コンテンツ抽出
```

システムが自動的に：
1. 最新の `tweet_details_ai_*.json` を読み込み
2. 全リンクを分類
3. WebFetchツールで各リンクのコンテンツを抽出
4. AI関連度スコアを付与（0-3点）
5. 統計情報を計算（AI関連度分布含む）
6. JSON出力生成
7. サマリーレポート表示

---

## 依存ツール

**必須**:
- `Read`: 入力ファイル読み込み
- `WebFetch`: 記事コンテンツ取得
- `Write`: 出力ファイル保存

**参照**:
- `@.claude/skills/_shared/ai_relevance_criteria.md`: AI関連度判定基準

**オプション（今後実装）**:
- `Bash`: youtube-transcript-api、pdfplumber実行

---

## 次のアクション提案

抽出完了後、以下のアクションを提案します：

1. **filter-extracted-content**: AI関連度でコンテンツをフィルタリング（推奨）
2. **analyze-replies**: リプライから反響ポイントを抽出
3. **research-topic**: WebSearchで最新ニュース・ファクトチェック
4. **generate-sns-posts**: AI関連コンテンツを元に投稿文生成

---

## 更新履歴

- 2026-01-02: 初版作成（ClaudeCode LLM直接実行型）
  - 実績: 11/12リンク成功（91.7%）、1,322ワード抽出
- 2026-01-12: AI関連度スコア付与機能を追加（STEP 3.5）
  - AI関連度判定基準: `ai_relevance_criteria.md` v1.0準拠
  - 出力にai_relevance_score, ai_relevance_reasonを追加
  - メタデータにai_relevance_distribution, ai_relevant_rateを追加
