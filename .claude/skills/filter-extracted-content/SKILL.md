---
name: filter-extracted-content
deprecated: true
deprecation_reason: "extract-contentスキルにLLM判定ワンパス化統合により廃止（v2.2、2026-01-12）"
replacement: "extract-content（LLM判定ワンパス化版）"
description: |
  ⚠️ **DEPRECATED**: このスキルは廃止されました。extract-contentスキルがLLM判定ワンパス化により、フィルタリング機能を統合しました。

  以下は参考情報です（使用しないでください）:
  抽出済みコンテンツをAI関連度でフィルタリングするスキル。
  記事タイトル・本文からAI関連度スコア（0-3点）を付与し、非AI関連コンテンツを除外します。

  使用タイミング：
  - extract-contentスキル実行後
  - Phase 2.1（コンテンツ抽出）完了後
  - Phase 3（投稿生成）前の品質管理

  所要時間：5-10分（記事数に依存）
  出力：extracted_contents_filtered_{YYYYMMDD}.json
trigger_keywords:
  - "コンテンツフィルタリング"
  - "AI関連度判定"
  - "非AI関連除外"
  - "filter content"
stage: Phase 2.5 - Content Filtering
dependencies: ["extract-content"]
output_file: Stock/programs/副業/projects/SNS/data/extracted_contents_filtered_{YYYYMMDD}.json
execution_time: 5-10分
framework_reference: Stock/programs/副業/projects/SNS/
priority: P0
model: claude-sonnet-4-5-20250929  # Sonnet 4.5 (判定精度重視)
---

# Filter Extracted Content Skill

抽出済みコンテンツをAI関連度でフィルタリングし、非AI関連コンテンツを除外するスキル。

**Version**: 1.0

---

## このSkillでできること

1. **AI関連度スコア付与**: タイトル・本文からAI関連度（0-3点）を自動判定
2. **非AI関連コンテンツ除外**: スコア0のコンテンツを自動除外
3. **統計レポート生成**: フィルタリング前後の統計情報を出力
4. **除外コンテンツ保存**: 除外されたコンテンツを別ファイルに保存（検証用）
5. **品質保証**: Phase 3投稿生成に渡すコンテンツの品質を担保

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | extracted_contents_{YYYYMMDD}.json（全抽出コンテンツ） |
| **出力1** | extracted_contents_filtered_{YYYYMMDD}.json（AI関連のみ） |
| **出力2** | non_ai_contents_{YYYYMMDD}.json（除外コンテンツ） |
| **次のアクション** | research-topic（Web調査）、generate-sns-posts（投稿生成） |

---

## Instructions

**実行モード**: ClaudeCode LLM自律実行（Sonnet 4.5）
**推定所要時間**: 5-10分（記事数に依存）

---

### STEP 1: 入力ファイル読み込み（30秒）

**Readツール使用**:
```
/Users/yuichi/agentpm/Stock/programs/副業/projects/SNS/data/extracted_contents_{最新日付}.json
```

**確認項目**:
- ファイル存在確認
- `extracted_contents` 配列の読み込み
- メタデータ（total_links, success_count等）の取得

**フォールバック**:
- 最新日付ファイルが見つからない場合、`extracted_contents_*.json` の最新ファイルを検索

---

### STEP 2: AI関連度スコア計算（3-8分）

#### 2A. 判定基準の読み込み

**必読**: `@.claude/skills/_shared/ai_relevance_criteria.md`

この基準ファイルには以下が記載されています：
- スコアリング基準（0-3点）
- AI技術キーワード（50+個）
- 除外対象の定義
- 判定ロジック

**実装方式の注意**:
- このスキルは**キーワードマッチング方式**を採用（高速・低コスト）
- extract-top-tweetsスキルは**LLM判定方式**を採用（高精度・中コスト）
- 判定基準は両スキルで共通（`ai_relevance_criteria.md`）
- 使い分け: TOP10抽出（少量）→LLM判定、コンテンツフィルタ（大量）→キーワードマッチング

#### 2B. 各記事のAI関連度スコア計算

**全記事に対して**:

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

    # STEP 2B-1: タイトル優先判定
    score = check_title_keywords(title)

    if score > 0:
        content['ai_relevance_score'] = score
        content['ai_relevance_reason'] = f"タイトルに{score}点キーワード含有"
        continue

    # STEP 2B-2: 本文キーワード密度判定
    score = calculate_keyword_density(text)

    content['ai_relevance_score'] = score
    content['ai_relevance_reason'] = get_reason_text(score)
```

#### 2C. キーワードマッチング実装

**3点キーワード判定**:
```python
keywords_3pt = [
    "LLM", "ChatGPT", "Claude", "GPT", "Gemini", "生成AI",
    "generative AI", "transformer", "neural network",
    "プロンプトエンジニアリング", "RAG", "fine-tuning",
    "diffusion model", "DALL-E", "Stable Diffusion"
]

def check_3pt_keywords(text: str) -> bool:
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords_3pt)
```

**2点キーワード判定**:
```python
keywords_2pt = [
    "OpenAI", "Anthropic", "DeepMind", "Google AI",
    "Microsoft AI", "Meta AI", "機械学習モデル",
    "ニューラルネットワーク", "アンソロピック"
]

def check_2pt_keywords(text: str) -> bool:
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords_2pt)
```

**1点キーワード判定**:
```python
keywords_1pt = [
    "機械学習", "machine learning", "データサイエンス",
    "data science", "予測モデル", "自動化システム"
]

def check_1pt_keywords(text: str) -> bool:
    text_lower = text.lower()
    return any(kw.lower() in text_lower for kw in keywords_1pt)
```

#### 2D. キーワード密度計算

```python
def calculate_keyword_density(text: str) -> int:
    """
    本文キーワード密度からスコアを計算

    Args:
        text: 記事本文

    Returns:
        0-3のスコア
    """
    total_words = len(text.split())
    if total_words == 0:
        return 0

    # 各レベルのキーワード出現回数
    count_3pt = count_keywords(text, keywords_3pt)
    count_2pt = count_keywords(text, keywords_2pt)
    count_1pt = count_keywords(text, keywords_1pt)

    # 密度計算
    density_3pt = count_3pt / total_words
    density_2pt = count_2pt / total_words
    density_1pt = count_1pt / total_words

    # スコア判定
    if density_3pt >= 0.02:  # 2%以上
        return 3
    elif density_2pt >= 0.01:  # 1%以上
        return 2
    elif density_1pt >= 0.005:  # 0.5%以上
        return 1
    else:
        return 0
```

---

### LLM判定 vs キーワードマッチング

このスキルは**キーワードマッチング方式**を採用していますが、extract-top-tweetsスキルは**LLM判定方式**を採用しています。以下の比較表で違いを理解してください。

| 方式 | 使用スキル | 精度 | 速度 | コスト | 適用対象 |
|------|-----------|------|------|--------|---------|
| **LLM判定** | extract-top-tweets | 高（100%） | 中速 | 中コスト | TOP10抽出（少量・精度重視） |
| **キーワードマッチング** | filter-extracted-content | 中（90%） | 高速 | 低コスト | コンテンツフィルタ（大量・速度重視） |

**使い分けの理由**:
- **TOP10抽出（少量）**: 10-50件程度の少量データなのでLLM判定の高精度を優先
- **コンテンツフィルタ（大量）**: 数百件以上の大量データなのでキーワードマッチングの高速処理を優先

**共通点**:
- 両方式とも同じ判定基準（`@.claude/skills/_shared/ai_relevance_criteria.md`）を使用
- 0-3点のスコアリングシステムを採用
- 最低スコア1点以上で合格

---

### STEP 3: フィルタリング実行（1分）

#### 3A. AI関連コンテンツ抽出

```python
# AI関連コンテンツ（スコア >= 1）
ai_contents = [
    content for content in extracted_contents
    if content.get('ai_relevance_score', 0) >= 1
]

# 非AI関連コンテンツ（スコア = 0）
non_ai_contents = [
    content for content in extracted_contents
    if content.get('ai_relevance_score', 0) == 0
]
```

#### 3B. スコア別集計

```python
# スコア別カウント
score_distribution = {
    '3点': len([c for c in ai_contents if c['ai_relevance_score'] == 3]),
    '2点': len([c for c in ai_contents if c['ai_relevance_score'] == 2]),
    '1点': len([c for c in ai_contents if c['ai_relevance_score'] == 1]),
    '0点': len(non_ai_contents)
}

# 保持率計算
retention_rate = (len(ai_contents) / len(extracted_contents)) * 100
```

---

### STEP 4: 出力ファイル生成（1分）

#### 4A. フィルタリング済みコンテンツ（メイン出力）

**出力JSONフォーマット**:
```json
{
  "metadata": {
    "filtered_at": "2026-01-12T12:00:00",
    "source_file": "extracted_contents_20260112.json",
    "original_count": 12,
    "filtered_count": 9,
    "excluded_count": 3,
    "retention_rate": 75.0,
    "score_distribution": {
      "3点": 5,
      "2点": 3,
      "1点": 1,
      "0点": 3
    },
    "filter_criteria": "AI関連度スコア >= 1"
  },
  "ai_contents": [
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
      "ai_relevance_reason": "タイトルに3点キーワード含有（LLM, RAG）"
    }
  ]
}
```

**保存先**: `Stock/programs/副業/projects/SNS/data/extracted_contents_filtered_{YYYYMMDD}.json`

#### 4B. 除外コンテンツ（検証用出力）

**出力JSONフォーマット**:
```json
{
  "metadata": {
    "excluded_at": "2026-01-12T12:00:00",
    "source_file": "extracted_contents_20260112.json",
    "excluded_count": 3,
    "exclusion_reason": "AI関連度スコア = 0"
  },
  "non_ai_contents": [
    {
      "url": "https://rakuten.com/fashion/...",
      "type": "article",
      "title": "楽天ファッション全額ポイントバック",
      "content": "...",
      "status": "success",
      "ai_relevance_score": 0,
      "ai_relevance_reason": "AI関連キーワード不在"
    }
  ]
}
```

**保存先**: `Stock/programs/副業/projects/SNS/data/non_ai_contents_{YYYYMMDD}.json`

---

### STEP 5: サマリーレポート生成（30秒）

**ユーザーへの報告**:
```
✅ コンテンツフィルタリング完了

📊 フィルタリング結果:
  - 元コンテンツ数: 12
  - AI関連（保持）: 9 (75.0%)
  - 非AI関連（除外）: 3 (25.0%)

📈 スコア分布:
  - 3点（高関連度）: 5件
  - 2点（中関連度）: 3件
  - 1点（低関連度）: 1件
  - 0点（除外）: 3件

🏆 高スコアコンテンツ（Top 3）:
  1. [3点] ChatGPT-4のRAG実装パターン (530 words)
  2. [3点] Claude 3.5プロンプトエンジニアリング (412 words)
  3. [2点] OpenAI新モデル発表 (298 words)

❌ 除外されたコンテンツ:
  1. [0点] 楽天ファッション全額ポイントバック
  2. [0点] DR.VAPE製品紹介
  3. [0点] U-NEXT動画配信サービス

💾 出力:
  - AI関連: extracted_contents_filtered_20260112.json (28KB)
  - 除外: non_ai_contents_20260112.json (8KB)

📌 Next: research-topic（Web調査）、generate-sns-posts（投稿生成）
```

---

## エラーハンドリング

### 入力ファイル不在
- **原因**: extract-contentスキル未実行、ファイルパス誤り
- **対応**: エラーメッセージ表示、処理中断
- **メッセージ**: "extracted_contents_{date}.json が見つかりません。extract-contentスキルを先に実行してください。"

### 全コンテンツが除外される
- **原因**: AI非関連ツイートのみが抽出されていた
- **対応**: 警告メッセージ表示、Phase 1の見直しを提案
- **メッセージ**: "全コンテンツが非AI関連と判定されました。Phase 1のTop 10抽出基準を見直してください。"

### スコア計算エラー
- **原因**: 記事本文が空、不正なデータ形式
- **対応**: 該当コンテンツをスコア0として処理、次へ進む
- **ログ**: `ai_relevance_reason: "スコア計算失敗（本文なし）"`

---

## データ品質保証

| 品質指標 | 目標 | 期待値 |
|---------|------|-------|
| **保持率** | 60-90% | 75% |
| **3点コンテンツ比率** | ≥40% | 50% |
| **除外精度** | 100% | 100%（非AI関連を誤って保持しない） |
| **実行時間** | ≤10分 | 5-8分 |

---

## 使用例

### 基本的な使用

```
User: コンテンツフィルタリング
```

システムが自動的に：
1. 最新の `extracted_contents_*.json` を読み込み
2. 各記事のAI関連度スコアを計算
3. スコア0のコンテンツを除外
4. フィルタリング済みJSONを出力
5. 除外コンテンツを別ファイルに保存
6. サマリーレポート表示

---

## 依存ツール

**必須**:
- `Read`: 入力ファイル読み込み
- `Write`: 出力ファイル保存（2ファイル）

**参照**:
- `@.claude/skills/_shared/ai_relevance_criteria.md`: AI関連度判定基準

---

## 統合ポイント

### Phase 2での位置づけ

```
Phase 2.1: コンテンツ抽出
    ↓
Phase 2.15: コンテンツフィルタリング ← このスキル
    ↓
Phase 2.2: リプライ分析
    ↓
Phase 2.3: Web調査
```

### Phase 3への影響

**改善前**:
- Phase 3が非AI関連コンテンツを参照する可能性あり
- LinkedIn投稿の主題が曖昧化

**改善後**:
- Phase 3にAI関連コンテンツのみが渡される
- 投稿品質の向上、主題の明確化

---

## 次のアクション提案

フィルタリング完了後、以下のアクションを提案します：

1. **analyze-replies**: リプライから反響ポイントを抽出（Phase 2.2）
2. **research-topic**: WebSearchで最新ニュース・ファクトチェック（Phase 2.3）
3. **generate-sns-posts**: AI関連コンテンツを元に投稿文生成（Phase 3）

---

## 更新履歴

- 2026-01-12: 初版作成（Phase 2フィルタリング機能追加）
- AI関連度判定基準: `ai_relevance_criteria.md` v1.0準拠
