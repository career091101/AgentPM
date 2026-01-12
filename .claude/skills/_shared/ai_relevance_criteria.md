# AI関連度判定基準

SNS自動化スキルで使用する統一的なAI関連度判定基準。

---

## スコアリング基準（0-3点）

| スコア | レベル | 判定基準 | 具体例 |
|--------|--------|---------|--------|
| **3点** | 高 | 明示的なAI技術キーワードが含まれる | LLM, 生成AI, Claude, GPT, Gemini, transformer, neural network, diffusion model |
| **2点** | 中 | AI企業名が明記されている、または技術的な詳細がある | OpenAI, Anthropic, DeepMind, Google AI, Microsoft AI + ニュース/発表 |
| **1点** | 低 | ML/データサイエンス/自動化が主題 | machine learning, データサイエンス、予測モデル、自動化システム |
| **0点** | 対象外 | 上記いずれにも該当しない | 一般ビジネス、マーケティング、製品紹介（AI非関連） |

---

## AI技術キーワード（50+個）

### コア技術（3点対象）
- **基本**: AI, artificial intelligence, 人工知能
- **機械学習**: machine learning, ML, 機械学習, deep learning, 深層学習
- **モデルアーキテクチャ**: transformer, neural network, CNN, RNN, LSTM, GAN, diffusion model
- **生成AI**: generative AI, 生成AI, LLM, large language model, ラージランゲージモデル
- **製品名**: ChatGPT, Claude, Gemini, GPT-4, GPT-3.5, Llama, Mistral, Phi

### AI企業（2-3点対象）
- **主要企業**: OpenAI, Anthropic, DeepMind, Google AI, Microsoft AI, Meta AI
- **日本企業**: Preferred Networks, Sakana AI, ELYZA, rinna
- **中国企業**: Baidu AI, ByteDance AI, Alibaba AI

### AI応用技術（2-3点対象）
- **プロンプト**: prompt engineering, プロンプトエンジニアリング, few-shot learning, chain-of-thought
- **RAG**: retrieval augmented generation, RAG, 検索拡張生成
- **ファインチューニング**: fine-tuning, RLHF, PEFT, LoRA
- **画像生成**: image generation, Stable Diffusion, DALL-E, Midjourney
- **エージェント**: AI agent, autonomous agent, multi-agent, エージェント
- **その他**: embedding, vector database, token, context window, inference

### ML/データサイエンス（1-2点対象）
- **基礎**: データサイエンス, data science, 予測モデル, prediction model
- **手法**: 分類, classification, 回帰, regression, クラスタリング, clustering
- **ツール**: scikit-learn, TensorFlow, PyTorch, Keras, Hugging Face

---

## 日本語キーワード

### 高関連度（3点）
- 生成AI, LLM, ラージランゲージモデル, 大規模言語モデル
- ChatGPT, クロード, ジェミニ
- プロンプトエンジニアリング, プロンプト設計
- RAG, 検索拡張生成
- ファインチューニング, 微調整
- 画像生成AI, 拡散モデル
- AIエージェント, 自律エージェント

### 中関連度（2点）
- OpenAI, アンソロピック, ディープマインド
- 機械学習モデル, ニューラルネットワーク
- トランスフォーマー, アテンション機構

### 低関連度（1点）
- 機械学習, ML
- データサイエンス, 予測分析
- 自動化システム, 自動化技術

---

## 除外対象（0点）

### 明確な非AI関連
- **一般ビジネス**: マーケティング戦略（AI非関連）、営業手法、経営論
- **製品紹介**: 電子機器、ファッション、食品、化粧品（AI機能なし）
- **エンタメ**: 映画、音楽、ドラマ、ゲーム（AI非関連）
- **スポーツ**: スポーツニュース、試合結果（AI非関連）
- **政治・経済**: 政治ニュース、株価、為替（AI非関連）

### 曖昧な表現（要確認）
- **「AI」のみ言及**: 技術的詳細なし、企業名なし → 本文確認必要
- **「機械学習」のみ言及**: 具体的手法なし → 本文確認必要
- **比喩的使用**: 「AIのような人間」「AIレベルの判断力」 → 0点

---

## 判定ロジック

### 1. タイトル優先判定

```
IF タイトルに3点キーワード含有 THEN
  スコア = 3
ELSE IF タイトルに2点キーワード含有 THEN
  スコア = 2
ELSE
  本文判定へ
END IF
```

### 2. 本文キーワード密度判定

```
# キーワード出現回数をカウント
keyword_count_3pt = 3点キーワードの出現回数
keyword_count_2pt = 2点キーワードの出現回数
keyword_count_1pt = 1点キーワードの出現回数

total_words = 本文総単語数

# 密度計算
density_3pt = keyword_count_3pt / total_words
density_2pt = keyword_count_2pt / total_words
density_1pt = keyword_count_1pt / total_words

IF density_3pt >= 0.02 THEN  # 2%以上
  スコア = 3
ELSE IF density_2pt >= 0.01 THEN  # 1%以上
  スコア = 2
ELSE IF density_1pt >= 0.005 THEN  # 0.5%以上
  スコア = 1
ELSE
  スコア = 0
END IF
```

### 3. LLM補完判定（境界ケース）

```
IF スコア = 1 AND タイトルに曖昧表現 THEN
  # Claude Sonnetで本文を分析
  LLM判定(本文) -> AI関連 OR 非AI関連

  IF LLM判定 = "AI関連" THEN
    スコア = 2に引き上げ
  ELSE
    スコア = 0に引き下げ
  END IF
END IF
```

---

## 合格基準

### Phase 2.1（コンテンツ抽出後フィルタリング）

| 用途 | 最低スコア | 理由 |
|------|----------|------|
| **LinkedIn投稿生成** | **2点以上** | 高品質なAI関連コンテンツのみ使用 |
| **X/Threads投稿生成** | **1点以上** | 幅広いAI関連トピックを許容 |
| **Web調査補完** | **1点以上** | ML/データサイエンス含む |

### Phase 1.2（ツイート抽出）

| 用途 | 最低スコア | 理由 |
|------|----------|------|
| **Top 10抽出** | **1点以上** | 初期フィルタリング段階 |

---

## 実装例

### Python実装（キーワードマッチング）

```python
# AI関連度スコア判定
def calculate_ai_relevance_score(title: str, content: str) -> int:
    """
    AI関連度スコア（0-3点）を計算

    Args:
        title: 記事タイトル
        content: 記事本文

    Returns:
        0-3のスコア
    """
    # 3点キーワード
    keywords_3pt = [
        "LLM", "ChatGPT", "Claude", "GPT", "Gemini", "生成AI",
        "generative AI", "transformer", "neural network",
        "プロンプトエンジニアリング", "RAG", "fine-tuning"
    ]

    # 2点キーワード
    keywords_2pt = [
        "OpenAI", "Anthropic", "DeepMind", "Google AI",
        "Microsoft AI", "機械学習モデル", "ニューラルネットワーク"
    ]

    # 1点キーワード
    keywords_1pt = [
        "機械学習", "machine learning", "データサイエンス",
        "data science", "予測モデル", "自動化"
    ]

    # タイトル優先判定
    title_lower = title.lower()
    if any(kw.lower() in title_lower for kw in keywords_3pt):
        return 3
    if any(kw.lower() in title_lower for kw in keywords_2pt):
        return 2

    # 本文キーワード密度判定
    content_lower = content.lower()
    total_words = len(content.split())

    count_3pt = sum(content_lower.count(kw.lower()) for kw in keywords_3pt)
    count_2pt = sum(content_lower.count(kw.lower()) for kw in keywords_2pt)
    count_1pt = sum(content_lower.count(kw.lower()) for kw in keywords_1pt)

    if total_words > 0:
        density_3pt = count_3pt / total_words
        density_2pt = count_2pt / total_words
        density_1pt = count_1pt / total_words

        if density_3pt >= 0.02:
            return 3
        elif density_2pt >= 0.01:
            return 2
        elif density_1pt >= 0.005:
            return 1

    return 0
```

### LLM判定（Claude Sonnet）

```python
# 境界ケースのLLM判定
def llm_ai_relevance_check(title: str, content: str) -> bool:
    """
    LLMを使用してAI関連度を判定（境界ケースのみ）

    Args:
        title: 記事タイトル
        content: 記事本文

    Returns:
        True: AI関連, False: 非AI関連
    """
    prompt = f"""
    以下の記事がAI・機械学習・データサイエンス関連のコンテンツかどうか判定してください。

    タイトル: {title}
    本文抜粋: {content[:500]}...

    判定基準:
    - AI技術、機械学習、深層学習、生成AIが主題 → AI関連
    - AI企業のニュース・発表が主題 → AI関連
    - データサイエンス、予測モデルが主題 → AI関連
    - 上記以外（ビジネス一般、製品紹介、エンタメ等） → 非AI関連

    回答: "AI関連" または "非AI関連" のみで答えてください。
    """

    # Claude Sonnet APIコール（疑似コード）
    response = claude_sonnet_api_call(prompt)

    return "AI関連" in response
```

---

## テストケース

### 3点ケース（高関連度）
- ✅ 「ChatGPT-4のRAG実装パターン」
- ✅ 「Claude 3.5 Sonnetのプロンプトエンジニアリング」
- ✅ 「生成AIのファインチューニング手法」

### 2点ケース（中関連度）
- ✅ 「OpenAIが新モデル発表」
- ✅ 「Anthropicの最新研究論文」
- ✅ 「機械学習モデルの精度向上手法」

### 1点ケース（低関連度）
- ✅ 「データサイエンティストのキャリアパス」
- ✅ 「予測モデル構築の基礎」
- ✅ 「業務自動化の成功事例」

### 0点ケース（非AI関連）
- ❌ 「楽天ファッション全額ポイントバック」
- ❌ 「DR.VAPE製品紹介」
- ❌ 「U-NEXT動画配信サービス」
- ❌ 「マーケティング戦略の最新トレンド」（AI言及なし）

---

## 更新履歴

- 2026-01-12: 初版作成（Phase 2フィルタリング機能追加に伴う統一基準策定）
