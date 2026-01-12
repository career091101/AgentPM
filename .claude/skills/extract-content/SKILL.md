---
name: extract-content
description: |
  ツイート詳細データから記事・YouTube・PDFリンクのコンテンツを抽出し、LLM判定でAI関連度をスコアリング。
  スコア0のコンテンツは即座に除外（ワンパス化）。ClaudeCode LLMが直接WebFetch/Readツールを使用。

  使用タイミング：
  - SNS投稿作成の事前調査時
  - 参照記事の要約が必要な時
  - リンク先の詳細情報を取得したい時

  所要時間：7-14分（リンク数に依存、ワンパス化により従来比▲3-6分短縮）
  出力1：extracted_contents_filtered_{YYYYMMDD}.json（AI関連のみ）
  出力2：non_ai_contents_{YYYYMMDD}.json（除外コンテンツ）
trigger_keywords:
  - "コンテンツ抽出"
  - "記事抽出"
  - "リンク先抽出"
  - "extract content"
stage: Phase 2 - Content Extraction
dependencies: ["scrape-tweet-details"]
output_file: Stock/programs/副業/projects/SNS/data/extracted_contents_filtered_{YYYYMMDD}.json
execution_time: 7-14分
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
| **出力1** | extracted_contents_filtered_{YYYYMMDD}.json（AI関連コンテンツのみ） |
| **出力2** | non_ai_contents_{YYYYMMDD}.json（除外された非AI関連コンテンツ） |
| **次のアクション** | analyze-replies（リプライ分析）、research-topic（Web調査）※filter-extracted-contentは廃止 |

---

## Instructions

**実行モード**: ClaudeCode LLM自律実行
**推定所要時間**: 7-14分（LLM判定ワンパス化、従来比▲3-6分短縮）

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

### STEP 3.5: AI関連度LLM判定 + フィルタリング（ワンパス化、2-4分）

**判定基準の参照**: `@.claude/skills/_shared/ai_relevance_criteria.md`

**⚡ ワンパス化**: キーワード密度判定を廃止し、LLM（Claude Sonnet）で直接AI関連度を判定。スコア0のコンテンツは即座に除外。

#### 3.5A. LLMによるAI関連度判定

**全抽出コンテンツに対して**:

```python
# 疑似コード（LLM内で実行）
ai_contents = []  # AI関連コンテンツ（スコア1-3）
non_ai_contents = []  # 非AI関連コンテンツ（スコア0）

for content in extracted_contents:
    if content['status'] != 'success':
        # エラー・パーシャルは0点
        content['ai_relevance_score'] = 0
        content['ai_relevance_reason'] = "抽出失敗"
        non_ai_contents.append(content)
        continue

    title = content.get('title', '')
    text = content.get('content', '')

    # LLMでAI関連度を判定（Claude Sonnet推奨）
    prompt = f"""
    以下のコンテンツがAI技術に関連するか判定してください。

    タイトル: {title}
    本文: {text[:1000]}  # 最初の1000文字

    判定基準（@.claude/skills/_shared/ai_relevance_criteria.md）:
    - 3点: LLM、生成AI、ChatGPT、Claude、GPT、プロンプトエンジニアリング等の明示的なAI技術キーワード含有
    - 2点: OpenAI、Anthropic、DeepMind等のAI企業名が明記、または技術的な詳細あり
    - 1点: 機械学習、データサイエンス、予測モデル等が主題
    - 0点: 上記いずれにも該当しない（一般ビジネス、製品紹介、エンタメ等）

    JSONフォーマットで返答:
    {{
      "score": 0-3,
      "reason": "判定理由（50文字以内）",
      "is_ai_related": true/false
    }}
    """

    # LLM判定実行
    llm_result = claude_sonnet_judge(prompt)

    content['ai_relevance_score'] = llm_result['score']
    content['ai_relevance_reason'] = llm_result['reason']

    # フィルタリング: スコア0は即座に除外
    if llm_result['score'] == 0:
        non_ai_contents.append(content)
    else:
        ai_contents.append(content)
```

#### 3.5B. LLM判定の利点

**従来のキーワード密度判定との比較**:

| 項目 | キーワード密度判定 | LLM判定（ワンパス化） |
|------|------------------|---------------------|
| **精度** | 90.9%（2点判定が弱い） | **95%+**（文脈理解） |
| **処理時間** | 1-2分 | 2-4分（+1-2分） |
| **2点境界ケース** | 誤判定リスク高 | 文脈理解で正確 |
| **フィルタリング** | 別スキル必要 | **統合済み** |
| **総所要時間** | 5-10分（コンテンツ抽出）+ 5-10分（フィルタリング）= **10-20分** | **7-14分**（ワンパス） |

**短縮効果**: ▲3-6分（30%短縮）

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
all_extracted = ai_contents + non_ai_contents

success_count = len([c for c in all_extracted if c['status'] == 'success'])
partial_count = len([c for c in all_extracted if c['status'] == 'partial'])
error_count = len([c for c in all_extracted if c['status'] in ['timeout', 'forbidden', 'error']])

total_words = sum([c.get('word_count', 0) for c in all_extracted if c['status'] == 'success'])
avg_words = total_words / success_count if success_count > 0 else 0

success_rate = (success_count / len(all_links)) * 100

# AI関連度スコア集計
score_distribution = {
    '3点': len([c for c in ai_contents if c.get('ai_relevance_score', 0) == 3]),
    '2点': len([c for c in ai_contents if c.get('ai_relevance_score', 0) == 2]),
    '1点': len([c for c in ai_contents if c.get('ai_relevance_score', 0) == 1]),
    '0点': len(non_ai_contents)
}

# フィルタリング統計
filtered_count = len(ai_contents)
excluded_count = len(non_ai_contents)
retention_rate = (filtered_count / len(all_extracted)) * 100 if len(all_extracted) > 0 else 0
```

---

### STEP 5: 出力ファイル生成（2ファイル、30秒）

**⚡ ワンパス化対応**: AI関連コンテンツと非AI関連コンテンツを別ファイルに出力

#### 5A. AI関連コンテンツ（extracted_contents_filtered_{date}.json）

**出力JSONフォーマット**:
```json
{
  "metadata": {
    "processed_at": "2026-01-12T12:38:00",
    "source_file": "tweet_details_ai_20260112.json",
    "filtered_at": "2026-01-12T12:40:00",
    "total_links": 12,
    "success_count": 11,
    "filtered_count": 9,
    "excluded_count": 3,
    "retention_rate": 75.0,
    "link_types": {
      "article": 11,
      "youtube": 0,
      "pdf": 1
    },
    "ai_relevance_distribution": {
      "3点": 5,
      "2点": 3,
      "1点": 1
      "0点": 3
    },
    "ai_relevant_rate": 75.0
  },
  "ai_contents": [
    {
      "url": "https://...",
      "type": "article",
      "title": "ChatGPT-4のRAG実装パターン",
      "content": "...",
      "word_count": 530,
      "status": "success",
      "tweet_id": "...",
      "username": "...",
      "domain": "...",
      "ai_relevance_score": 3,
      "ai_relevance_reason": "LLM判定: 生成AI技術の詳細解説"
    }
  ]
}
```

**保存先**: `Stock/programs/副業/projects/SNS/data/extracted_contents_filtered_{YYYYMMDD}.json`

---

#### 5B. 非AI関連コンテンツ（non_ai_contents_{date}.json）

**出力JSONフォーマット**:
```json
{
  "metadata": {
    "excluded_at": "2026-01-12T12:40:00",
    "excluded_count": 3,
    "reason": "AI関連度スコア0点（AI技術非関連）"
  },
  "non_ai_contents": [
    {
      "url": "https://rakuten.com/fashion/...",
      "type": "article",
      "title": "楽天ファッション全額ポイントバック",
      "content": "...",
      "word_count": 200,
      "status": "success",
      "ai_relevance_score": 0,
      "ai_relevance_reason": "LLM判定: 一般製品紹介（AI非関連）"
    }
  ]
}
```

**保存先**: `Stock/programs/副業/projects/SNS/data/non_ai_contents_{YYYYMMDD}.json`

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
