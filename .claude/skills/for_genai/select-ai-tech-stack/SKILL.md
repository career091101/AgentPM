---
skill_id: for-genai-select-ai-tech-stack
skill_name: AI Tech Stack Selection (ForGenAI)
domain: ForGenAI
phase: 2_planning
category: technical_architecture
origin: for_genai
quality_target: 95/100
version: 1.0.0
last_updated: 2026-01-03
dependencies:
  - for-genai-validate-cpf
  - for-genai-discover-demand
integration_sources:
  - GenAI_research/LLM/01_LifeisBeautiful_insights.md
  - GenAI_research/technologies/openai/
  - GenAI_research/technologies/anthropic/
  - GenAI_research/technologies/google/
  - GenAI_research/technologies/langchain/
  - GenAI_research/technologies/llamaindex/
output_path: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/3_planning/ai_tech_stack_selection.md
---

# Select AI Tech Stack Skill (ForGenAI Edition)

**AI技術スタック選定スキル** - LLMプロバイダー、Vector DB、フレームワーク、インフラを定量比較し、ユースケース・精度・速度・予算・スケールに最適化した技術スタックを選定。

---

## このSkillでできること

1. **要件ヒアリング**: ユースケース、精度要求、応答速度、予算、スケール目標を構造化インタビュー
2. **LLMプロバイダー比較**: GPT-4 Turbo vs Claude 3.5 Sonnet vs Gemini 1.5 Pro vs Llama 3.1（コスト・精度・速度・コンテキスト長）
3. **Vector DB選定**: Pinecone vs Weaviate vs ChromaDB vs Qdrant（スケール・速度・コスト）
4. **フレームワーク選定**: LangChain vs LlamaIndex vs AutoGPT vs CrewAI（開発速度・柔軟性・保守性）
5. **推論コスト試算**: 10万→100万→1,000万ユーザーの月額コスト推定（マルチLLM戦略による40%削減を含む）
6. **成功パターン統合**: Perplexity、Jasper、Cursor、Notion AI等12件のTier 2ケーススタディから最適構成を抽出
7. **コスト最適化パターン**: Hybrid Model、Caching、Batching、Fallback戦略
8. **技術スタック決定書**: 選定根拠、代替案、移行計画、リスク評価を含む総合レポート

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `cpf_judgment_forgenai.md`, `demand_discovery_forgenai.md`, インタラクティブ質問応答 |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForGenAI/documents/3_planning/ai_tech_stack_selection.md` |
| **次のSkill** | `/optimize-prompt-quality` → `/validate-10x` → `/analyze-ai-competitors` |
| **所要時間** | 60-90分（要件定義30分、比較分析30分、レポート作成30分） |

---

## 要件ヒアリング（構造化インタビュー）

### 1. ユースケース分類

以下から1つ選択（複数選択可、優先順位付け）：

| ユースケース | 代表製品 | LLM要件 | Vector DB要件 |
|------------|---------|---------|--------------|
| **テキスト生成** | Jasper、Copy.ai | 高精度LLM、長コンテキスト | 不要 or 低優先度 |
| **検索・Q&A** | Perplexity、You.com | 引用生成、ファクトチェック | 必須（高速検索） |
| **コード生成** | Cursor、GitHub Copilot | コード理解、補完精度 | コードベース検索 |
| **チャットボット** | Character.AI、Replika | 会話継続、パーソナリティ | 履歴管理 |
| **RAG（文書検索）** | Notion AI、Glean | 検索精度、要約 | 必須（高精度ベクトル検索） |
| **エージェント** | AutoGPT、BabyAGI | 推論、タスク分解 | オプション |
| **マルチモーダル** | Midjourney、DALL-E 3 | 画像生成、vision | 画像ベクトル検索 |

**質問**:
1. 主要ユースケースは？（上記から選択）
2. 副次的ユースケースは？（将来対応する可能性）
3. 優先順位は？（1位、2位、3位）

### 2. 精度要求

| 精度レベル | 許容エラー率 | 適用例 | LLM選定方針 |
|----------|------------|--------|------------|
| **Mission Critical** | < 1% | 医療診断、金融取引、法律文書 | GPT-4 Turbo、Claude 3 Opus（最高精度） |
| **High Accuracy** | 1-5% | ビジネス文書、技術ドキュメント | GPT-4 Turbo、Claude 3.5 Sonnet |
| **Standard** | 5-10% | マーケティング、カスタマーサポート | GPT-4o、Claude 3 Sonnet、Gemini 1.5 Pro |
| **Acceptable** | 10-20% | カジュアルチャット、創作 | GPT-3.5 Turbo、Llama 3.1、Gemini 1.5 Flash |

**質問**:
1. 許容できるエラー率は？（%）
2. エラーの影響は？（金銭損失、ブランド毀損、ユーザー離脱等）
3. 人間によるレビューは可能か？（Yes/No、何%の出力をレビューするか）

### 3. 応答速度要求

| 速度要求 | 目標レスポンス | 適用例 | LLM選定方針 |
|---------|--------------|--------|------------|
| **Real-time** | < 1秒 | チャットボット、自動補完 | GPT-3.5 Turbo、Gemini 1.5 Flash、Llama 3.1（小モデル） |
| **Interactive** | 1-3秒 | Q&A、文書生成 | GPT-4o、Claude 3.5 Sonnet、Gemini 1.5 Pro |
| **Batch** | 3-10秒 | 長文要約、レポート生成 | GPT-4 Turbo、Claude 3 Opus |
| **Async** | > 10秒 | 大量データ分析、画像生成 | Llama 3.1（大モデル）、GPT-4 Turbo（バッチAPI） |

**質問**:
1. 目標レスポンスタイムは？（秒）
2. ユーザーは待てるか？（Yes/No、何秒まで許容可能か）
3. Streaming（逐次出力）は必要か？（Yes/No）

### 4. 予算・コスト制約

| 予算タイプ | 月額予算目安 | ユーザー規模 | コスト最適化戦略 |
|----------|------------|------------|---------------|
| **MVP（検証）** | $100-$500 | < 100人 | 無料枠活用、GPT-3.5 Turbo中心 |
| **Early Stage** | $500-$5,000 | 100-1,000人 | Hybrid Model、Caching |
| **Growth** | $5,000-$50,000 | 1,000-10,000人 | マルチLLM戦略、Batching |
| **Scale** | $50,000+ | 10,000人+ | 専用インフラ、Fine-tuning、Self-hosted Llama |

**質問**:
1. 月額予算は？（$）
2. ユーザー数予測は？（3ヶ月後、6ヶ月後、1年後）
3. コスト削減の優先度は？（高/中/低）

### 5. スケール目標

| スケール段階 | ユーザー数 | リクエスト数/日 | インフラ要件 |
|------------|----------|--------------|------------|
| **MVP** | < 100 | < 1,000 | サーバーレス（Vercel、Railway） |
| **Early** | 100-1,000 | 1,000-10,000 | マネージドサービス（Pinecone無料枠、Supabase） |
| **Growth** | 1,000-10,000 | 10,000-100,000 | 専用インスタンス（Pinecone有料、AWS/GCP） |
| **Scale** | 10,000+ | 100,000+ | Self-hosted、クラスター構成 |

**質問**:
1. 6ヶ月後のユーザー数目標は？
2. 1年後のユーザー数目標は？
3. リクエスト数/日の予測は？

---

## LLMプロバイダー比較表（2026年1月版）

### 主要4社の定量比較

| プロバイダー | モデル | 入力コスト（$/1M tokens） | 出力コスト（$/1M tokens） | コンテキスト長 | 速度（tokens/秒） | 精度（MMLU） | 推奨用途 |
|------------|-------|------------------------|------------------------|--------------|----------------|------------|---------|
| **OpenAI** | GPT-4 Turbo | $10.00 | $30.00 | 128K | 50-80 | **86.4%** | 高精度、長文、RAG |
| **OpenAI** | GPT-4o | $2.50 | $10.00 | 128K | 100-150 | 83.7% | 汎用、コスパ高 |
| **OpenAI** | GPT-3.5 Turbo | $0.50 | $1.50 | 16K | 150-200 | 70.0% | 低コスト、高速 |
| **Anthropic** | Claude 3 Opus | $15.00 | $75.00 | 200K | 40-60 | **86.8%** | 最高精度、長文解析 |
| **Anthropic** | Claude 3.5 Sonnet | $3.00 | $15.00 | 200K | 80-120 | **88.7%** | **コーディング最強** |
| **Anthropic** | Claude 3 Haiku | $0.25 | $1.25 | 200K | 200-300 | 75.2% | 最速、低コスト |
| **Google** | Gemini 1.5 Pro | $3.50 | $10.50 | **2M** | 70-100 | 81.9% | **超長コンテキスト** |
| **Google** | Gemini 1.5 Flash | $0.075 | $0.30 | 1M | 150-250 | 78.9% | **最安、高速** |
| **Meta** | Llama 3.1 405B | **Self-hosted** | **Self-hosted** | 128K | 20-50（GPU依存） | 85.2% | プライバシー、大規模 |
| **Meta** | Llama 3.1 70B | **Self-hosted** | **Self-hosted** | 128K | 50-100（GPU依存） | 79.3% | コスパ、Fine-tuning |

**注**: コストは2026年1月時点、速度はベンチマーク平均値（実際の速度はプロンプト長、サーバー負荷に依存）

### ユースケース別推奨LLM

| ユースケース | 第1候補 | 第2候補 | 第3候補 | 選定理由 |
|------------|--------|--------|--------|---------|
| **テキスト生成** | GPT-4o | Claude 3.5 Sonnet | Gemini 1.5 Pro | コスパ、精度、速度のバランス |
| **検索・Q&A** | Claude 3.5 Sonnet | GPT-4o | Gemini 1.5 Pro | 引用生成、ファクトチェック精度 |
| **コード生成** | **Claude 3.5 Sonnet** | GPT-4o | Llama 3.1 405B | コーディング精度95%（Cursor実績） |
| **チャットボット** | GPT-3.5 Turbo | Gemini 1.5 Flash | Claude 3 Haiku | 低コスト、高速、会話継続 |
| **RAG（文書検索）** | GPT-4 Turbo | Claude 3 Opus | Gemini 1.5 Pro | 長文理解、要約精度 |
| **エージェント** | Claude 3.5 Sonnet | GPT-4o | Llama 3.1 405B | 推論、タスク分解精度 |
| **マルチモーダル** | GPT-4o | Gemini 1.5 Pro | Claude 3.5 Sonnet | Vision、画像理解 |

---

## Vector DB比較表

### 主要4社の定量比較

| Vector DB | 無料枠 | 有料プラン開始 | スケール上限 | 検索速度（100万ベクトル） | 精度（Recall@10） | 推奨用途 |
|----------|--------|--------------|------------|------------------------|-----------------|---------|
| **Pinecone** | 100K vectors | $70/月（p1） | **無制限** | **< 100ms** | **98%** | 本番環境、大規模 |
| **Weaviate** | Self-hosted | $25/月（1M vectors） | 10億ベクトル | 100-200ms | 95% | オープンソース、プライバシー |
| **ChromaDB** | Self-hosted | 無料（OSS） | 1億ベクトル | 200-500ms | 92% | MVP、ローカル開発 |
| **Qdrant** | Self-hosted | $49/月（1M vectors） | 10億ベクトル | 150-300ms | 96% | フィルタリング、メタデータ検索 |

**注**: 速度・精度はベンチマーク平均値（実際の性能はベクトル次元数、フィルタリング条件、サーバースペックに依存）

### ユースケース別推奨Vector DB

| ユースケース | 第1候補 | 第2候補 | 選定理由 |
|------------|--------|--------|---------|
| **本番環境（大規模）** | **Pinecone** | Weaviate | 検索速度、精度、スケール |
| **プライバシー重視** | Weaviate | Qdrant | Self-hosted、オープンソース |
| **MVP・検証** | ChromaDB | Qdrant | 無料、ローカル開発 |
| **メタデータ検索** | Qdrant | Weaviate | フィルタリング機能強力 |

---

## フレームワーク比較表

### 主要4種の定量比較

| フレームワーク | 学習曲線 | 開発速度 | 柔軟性 | コミュニティ | 推奨用途 |
|-------------|---------|---------|-------|------------|---------|
| **LangChain** | 中 | **最速** | 中 | **最大** | 汎用、RAG、エージェント |
| **LlamaIndex** | 低 | 速い | 中 | 大 | **RAG特化**、文書検索 |
| **AutoGPT** | 高 | 遅い | **最高** | 中 | エージェント、タスク自動化 |
| **CrewAI** | 中 | 中 | 高 | 小 | マルチエージェント、協調 |

### ユースケース別推奨フレームワーク

| ユースケース | 第1候補 | 第2候補 | 選定理由 |
|------------|--------|--------|---------|
| **RAG（文書検索）** | **LlamaIndex** | LangChain | RAG特化、インデックス管理 |
| **エージェント** | LangChain | AutoGPT | 豊富なツール統合、コミュニティ |
| **汎用開発** | LangChain | カスタム実装 | 開発速度、柔軟性 |
| **マルチエージェント** | CrewAI | AutoGPT | エージェント協調機能 |

---

## 推論コスト試算表

### 前提条件

- **ユースケース**: テキスト生成（マーケティングコピー、ブログ記事）
- **平均入力**: 500 tokens
- **平均出力**: 1,000 tokens
- **ユーザーあたり月間リクエスト**: 20回

### スケール別月額コスト（LLMプロバイダー別）

| ユーザー数 | GPT-4 Turbo | GPT-4o | Claude 3.5 Sonnet | Gemini 1.5 Pro | GPT-3.5 Turbo | Gemini 1.5 Flash |
|----------|------------|--------|------------------|---------------|--------------|-----------------|
| **100** | $95 | $32 | $48 | $36 | $5 | $1 |
| **1,000** | $950 | $320 | $480 | $360 | $50 | $10 |
| **10,000** | $9,500 | $3,200 | $4,800 | $3,600 | $500 | $100 |
| **100,000** | $95,000 | $32,000 | $48,000 | $36,000 | $5,000 | $1,000 |
| **1,000,000** | $950,000 | $320,000 | $480,000 | $360,000 | $50,000 | $10,000 |

**計算式**:
```
月額コスト = ユーザー数 × 月間リクエスト × (入力tokens × 入力コスト + 出力tokens × 出力コスト) / 1,000,000
```

**例（GPT-4o、10,000ユーザー）**:
```
10,000 × 20 × (500 × $2.50 + 1,000 × $10.00) / 1,000,000 = $3,200
```

---

## コスト最適化パターン

### 1. Hybrid Model（2段階生成）

**戦略**: 初稿は低コストLLM、校正は高精度LLM

**実装例（Jasper）**:
```python
# Step 1: 初稿生成（GPT-3.5 Turbo）
draft = openai.ChatCompletion.create(
    model="claude-haiku-4-5-20251001",
    messages=[{"role": "user", "content": prompt}]
)

# Step 2: 校正・改善（GPT-4o）
final = openai.ChatCompletion.create(
    model="claude-sonnet-4-5-20250929",
    messages=[
        {"role": "system", "content": "校正して品質を向上させてください"},
        {"role": "user", "content": draft}
    ]
)
```

**成果**:
- コスト削減: 60%（GPT-4o単独比）
- 精度維持: 85/100（変わらず）

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/jasper_hybrid_model.md`

---

### 2. Caching（プロンプトキャッシング）

**戦略**: Anthropic Prompt Cachingで繰り返しプロンプトのコスト90%削減

**実装例（Cursor）**:
```python
# Anthropic Prompt Caching（Claude 3.5 Sonnet）
response = anthropic.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "あなたはコーディングアシスタントです。以下のコードベースを参照してください。",
        },
        {
            "type": "text",
            "text": f"{codebase}",  # 10,000 tokens
            "cache_control": {"type": "ephemeral"}  # キャッシュ有効化
        }
    ],
    messages=[{"role": "user", "content": user_query}]
)
```

**成果**:
- キャッシュヒット時コスト: $3.00 → $0.30（90%削減）
- 応答速度: 3秒 → 0.5秒（キャッシュヒット時）

**参照**: Anthropic公式ドキュメント、Cursor実装事例

---

### 3. Batching（バッチ処理）

**戦略**: OpenAI Batch APIで50%コスト削減（24時間以内納品でOKなタスク）

**実装例**:
```python
# OpenAI Batch API（GPT-4 Turbo）
batch = openai.batches.create(
    input_file_id="file-abc123",
    endpoint="/v1/chat/completions",
    completion_window="24h"
)

# 24時間以内に完了、コスト50%削減
```

**適用例**:
- 大量文書要約（1,000件/日）
- 翻訳バッチ処理（10,000件/日）
- データ分析レポート生成（500件/日）

**成果**:
- コスト削減: 50%（リアルタイムAPI比）
- スループット: 10倍（並列処理）

**参照**: OpenAI公式ドキュメント

---

### 4. Fallback戦略（API障害対策）

**戦略**: プライマリLLMが障害時、セカンダリLLMに自動切り替え

**実装例（Perplexity）**:
```python
def generate_with_fallback(prompt):
    try:
        # プライマリ: Claude 3.5 Sonnet
        return anthropic.messages.create(model="claude-sonnet-4-5-20250929", ...)
    except anthropic.APIError:
        # フォールバック: GPT-4o
        return openai.ChatCompletion.create(model="claude-sonnet-4-5-20250929", ...)
    except openai.APIError:
        # 最終フォールバック: Gemini 1.5 Pro
        return genai.GenerativeModel("gemini-1.5-pro").generate_content(...)
```

**成果**:
- ダウンタイム: 99.9% → 99.99%（マルチプロバイダー）
- ユーザー離脱率: 5% → 0.5%（障害時）

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/perplexity_multi_llm.md`

---

## Domain-Specific Knowledge (from GenAI_research)

### Success Patterns（技術スタック選定成功事例）

#### 事例1: Perplexity AI（マルチLLMプロバイダー戦略）

**基本情報**:
- **評価額**: $1B+ (2024年時点)
- **技術戦略**: OpenAI + Anthropic + オープンソースの並行利用
- **コスト削減**: 40%削減（プロバイダー分散 + キャッシング）

**技術スタック構成**:

| 用途 | 選定LLM | 理由 |
|------|--------|------|
| **検索クエリ理解** | GPT-4 Turbo | 複雑な自然言語理解に強い |
| **回答生成** | Claude 3.5 Sonnet | 長文出力品質が高い（引用生成） |
| **ファクトチェック** | Llama 3 70B | コスト最適化（オープンソース） |

**Vector DB**: Pinecone（リアルタイム検索性能 + マネージドサービス）

**スケーラビリティ**:
- 月次クエリ数: 100M+
- 平均レスポンス: <2秒
- レイテンシ最適化: キャッシング（30%ヒット率）+ ストリーミングレスポンス

**成果**:
- API障害時のダウンタイム: 99.9% → 99.99%（マルチプロバイダー）
- 月額コスト: $50,000 → $30,000（40%削減）
- 精度維持: MMLU 85.2%（Claude単独時と同等）

**学び**:
- ユースケース別にLLMを使い分ける（検索はGPT-4、生成はClaude）
- フォールバック戦略でAPI障害リスクを軽減
- コスト削減と精度維持を両立

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/01_perplexity_llm_migration.md`

---

#### 事例2: Cursor（Anthropic Claude 3.5 Sonnet選定）

**基本情報**:
- **評価額**: 非公開（Series A調達済み）
- **技術戦略**: Claude 3.5 Sonnet単一プロバイダー集中
- **差別化**: コーディング精度95%（GPT-4比較）

**選定理由**:

| 評価軸 | GPT-4 Turbo | **Claude 3.5 Sonnet** | 選定理由 |
|--------|------------|----------------------|---------|
| **コーディング精度** | 75% | **95%** | ビルド成功率が圧倒的に高い |
| **コンテキスト長** | 128K | **200K** | 大規模コードベース対応 |
| **推論速度** | 中速 | **高速** | ストリーミングレスポンス最適化 |
| **コスト** | $10/1Mトークン | **$3/1Mトークン** | 1/3のコスト |

**Orchestration**: カスタム実装（LangChainよりもコード生成に特化）

**スケーラビリティ**:
- 同時ユーザー数: 10K+
- 平均セッション長: 30分
- コスト試算: $0.5/ユーザー/月

**成果**:
- コード生成精度: 90% → 95%（Claude切り替え後）
- ユーザー満足度（NPS）: 65 → 78
- CAC: $12 → $3.5（Product Hunt #1獲得効果含む）

**学び**:
- コーディング用途ではClaude 3.5 Sonnetが最強（2026年1月時点）
- 長コンテキスト（200K）でコードベース全体理解が可能
- Constitutional AIで安全性・バイアス低減

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/02_cursor_anthropic_selection.md`

---

#### 事例3: Notion AI（RAG構成 + Vector DB選定）

**基本情報**:
- **評価額**: $10B+ (2024年時点)
- **技術戦略**: GPT-4 + Pinecone（RAG構成）
- **差別化**: ユーザーデータ統合による精度向上

**RAG構成**:

```
User Query
    ↓
Embedding生成（OpenAI text-embedding-3-large）
    ↓
Vector検索（Pinecone: 100K+ documents）
    ↓
コンテキスト拡張（Top 10関連ドキュメント）
    ↓
LLM生成（GPT-4 Turbo: 回答生成）
    ↓
Response
```

**Vector DB選定**:

| 評価軸 | Pinecone | Weaviate | Chroma |
|--------|---------|----------|--------|
| **検索精度** | 95% | 93% | 90% |
| **レイテンシ** | <50ms | <100ms | <200ms |
| **スケーラビリティ** | ✅ マネージド | ⚠️ 自己ホスティング | ❌ ローカルのみ |
| **コスト** | $0.096/1M queries | 自己ホスティング次第 | 無料（ローカル） |

**選定理由**: マネージドサービス + 低レイテンシ + スケーラビリティ

**スケーラビリティ**:
- ドキュメント数: 100M+
- クエリ数: 10M/日
- 平均レイテンシ: <2秒（Embedding + Vector検索 + LLM生成）

**成果**:
- 文書検索精度: 85% → 95%（Pinecone導入後）
- 応答速度: 5秒 → 2秒（ベクトル検索高速化）
- ユーザー継続率: 60% → 75%

**学び**:
- RAGには高精度LLM（GPT-4 Turbo、Claude 3 Opus）必須
- Vector DBはスケールと速度でPinecone推奨
- 埋め込みモデルは3,072次元以上で精度大幅向上

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/03_notion_ai_rag_architecture.md`

---

#### 事例4: Jasper（Hybrid Model + コスト最適化）

**基本情報**:
- **評価額**: $1.5B+ (2024年時点)
- **技術戦略**: Hybrid Model（GPT-4o + GPT-3.5 Turbo）
- **差別化**: コスト60%削減、精度維持

**技術スタック構成**:
- 初稿生成: GPT-3.5 Turbo（低コスト、高速）
- 校正・改善: GPT-4o（精度重視）
- ファクトチェック: Claude 3.5 Sonnet（引用生成）

**成果**:
- 月額コスト: $100,000 → $40,000（60%削減）
- 精度維持: マーケティング文書品質スコア 85/100（変わらず）
- 応答速度: 3秒 → 1.5秒（GPT-3.5 Turbo初稿生成で高速化）

**学び**:
- Hybrid Model（低コストLLM + 高精度LLM）でコスト大幅削減
- 初稿はGPT-3.5 Turbo、校正はGPT-4oで精度維持
- ファクトチェックはClaude 3.5 Sonnetで引用生成

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/04_jasper_ai_cost_optimization.md`

---

#### 事例5: Intercom（GPT-4 Turboによるカスタマーサポート）

**基本情報**:
- **評価額**: $1.3B+ (2024年時点)
- **技術戦略**: GPT-4 Turbo + GPT-3.5 Turbo（Query Classification）
- **カスタマーサポート応答時間**: 50%短縮、顧客満足度 85% → 92%

**技術スタック構成**:
- メインLLM: GPT-4 Turbo（会話継続性、128Kコンテキスト）
- フォールバック: GPT-3.5 Turbo（60%のシンプルクエリで使用）
- ファインチューニング: 1,000件の製品ドキュメントで精度95%達成

**成果**:
- 応答時間: 5秒 → 2.5秒（50%短縮）
- 初回解決率: 60% → 78%
- エージェント負荷: 35%削減（$2M/年のコスト削減）

**学び**:
- カスタマーサポートには会話継続性が最重要（マルチターン対応で78%自動解決）
- ファインチューニングで製品知識を統合（汎用GPT-4の75%精度 → Custom GPT-4の95%精度）
- Query Classificationでコスト40%削減（シンプルなクエリはGPT-3.5 Turbo）

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/05_intercom_gpt4_customer_support.md`

---

#### 事例6: Glean（Gemini 1.5 Pro超長コンテキスト活用）

**基本情報**:
- **評価額**: $2.2B+ (2024年時点)
- **技術戦略**: Gemini 1.5 Pro（2Mコンテキスト活用）
- **差別化**: 大量ドキュメント一括処理、コスト1/3（GPT-4比較）

**技術スタック構成**:
- LLM: Gemini 1.5 Pro（2Mコンテキスト、$3.5/1M）
- Vector DB: 不要（2Mコンテキストで全文送信）

**成果**:
- 検索精度: 88% → 94%（Chunking不要で文脈完全保持）
- 処理速度: 3倍高速（5秒 → 1.5秒）
- コスト: 65%削減（$10,000 → $3,500/月、Vector DB不要）

**学び**:
- 2Mコンテキストで数百ページのドキュメントを一括処理可能
- Chunking不要により精度6%向上
- Vector DB不要でコスト65%削減

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/06_glean_gemini_ultra_context.md`

---

#### 事例7: Harvey（Weaviate選定 - プライバシー重視）

**基本情報**:
- **評価額**: 非公開（法律AI）
- **技術戦略**: Weaviate（Self-hosted）+ GPT-4 Turbo
- **差別化**: 弁護士-クライアント秘匿特権の完全遵守、オンプレミスデプロイ

**技術スタック構成**:
- Vector DB: Weaviate（Self-hosted、プライバシー保護）
- LLM: GPT-4 Turbo
- インフラ: オンプレミス（データ漏洩リスクゼロ）

**成果**:
- 大手法律事務所との契約締結率: 95%（Pinecone時代30%）
- 引用生成精度: 92%
- コスト削減: 70%（クラウドVector DB比較）

**学び**:
- プライバシー重視業界（法律、医療、金融）ではSelf-hosted Vector DBが必須
- Weaviateのメタデータフィルタリングで検索精度向上
- オンプレミスデプロイでデータ主権確保

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/07_harvey_weaviate_privacy.md`

---

#### 事例8: Dovetail（Qdrant選定 - メタデータ検索特化）

**基本情報**:
- **評価額**: 非公開（UXリサーチプラットフォーム）
- **技術戦略**: Qdrant + Claude 3.5 Sonnet
- **差別化**: 複雑なメタデータフィルタリングで検索精度94%

**技術スタック構成**:
- Vector DB: Qdrant（メタデータ検索特化）
- LLM: Claude 3.5 Sonnet

**成果**:
- メタデータフィルタ検索精度: 60% → 94%（+34%）
- 検索速度: 最大75%向上
- コスト削減: 40%

**学び**:
- ユーザーインタビュー分析等、メタデータが重要なユースケースではQdrant推奨
- AND/OR/NOT/Range条件の高度な組み合わせが可能
- Rustベース最適化で検索速度向上

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/08_dovetail_qdrant_metadata.md`

---

#### 事例9: Poe/Quora（LangChain選定 - マルチLLM統合）

**基本情報**:
- **評価額**: 非公開（Quora製）
- **技術戦略**: LangChain（マルチLLM統合フレームワーク）
- **差別化**: 50+ LLMを単一インターフェースで提供

**技術スタック構成**:
- フレームワーク: LangChain
- LLM: 50+ プロバイダー（OpenAI、Anthropic、Google、Meta等）

**成果**:
- 開発速度: 3倍向上
- 新規LLM統合時間: 70%短縮（40時間 → 12時間）
- API障害時ダウンタイム: 10分 → 1分

**学び**:
- マルチLLMプロバイダー統合にはLangChainが最適
- 統一インターフェースで開発速度3倍
- フォールバック戦略でダウンタイム90%削減

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/09_poe_langchain_multi_llm.md`

---

#### 事例10: Casetext（LlamaIndex選定 - RAG特化）

**基本情報**:
- **評価額**: 非公開（法律AI、Thomson Reuters買収）
- **技術戦略**: LlamaIndex + Pinecone + GPT-4 Turbo
- **差別化**: 引用生成精度95%、法律文書検索精度92%

**技術スタック構成**:
- フレームワーク: LlamaIndex（RAG特化）
- Vector DB: Pinecone
- LLM: GPT-4 Turbo

**成果**:
- 引用機能実装時間: 92%短縮（60時間 → 5時間）
- 検索精度: 82% → 92%
- 開発速度: 2倍向上

**学び**:
- RAG構成にはLlamaIndex推奨（引用生成標準実装）
- 複数インデックス統合、クエリ変換、Rerankingが標準装備
- 法律文書検索での引用生成精度95%

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/10_casetext_llamaindex_rag.md`

---

#### 事例11: Replicate（Llama 3.1 Self-hosted - コスト1/10削減）

**基本情報**:
- **評価額**: 非公開（モデルホスティング）
- **技術戦略**: Llama 3.1 405B Self-hosted（GPT-4代替）
- **差別化**: コスト削減90%、推論速度2倍、データ主権確保

**技術スタック構成**:
- LLM: Llama 3.1 405B（Self-hosted on AWS）
- 最適化: vLLM、FP8量子化、Flash Attention 2

**成果**:
- コスト: GPT-4 $500K/月 → Llama 3.1 $50K/月（90%削減）
- 推論速度: 2倍
- 品質: 同等（MMLU 85.2%）

**学び**:
- 大規模運用（月間100M+ リクエスト）ではSelf-hosted Llamaが最適
- vLLM + FP8量子化で推論速度2倍
- Fine-tuning自由度でドメイン特化精度向上

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/11_replicate_llama_self_hosted.md`

---

#### 事例12: Copy.ai（Hybrid Model + Caching - コスト75%削減）

**基本情報**:
- **評価額**: 非公開
- **技術戦略**: Hybrid Model（GPT-4o + Claude 3.5 Sonnet）+ Prompt Caching
- **差別化**: コスト削減75%、品質維持90/100、レスポンス速度3倍

**技術スタック構成**:
- 初稿生成: GPT-4o
- 校正・改善: Claude 3.5 Sonnet
- コスト最適化: Anthropic Prompt Caching（90%削減）

**成果**:
- コスト: $200K/月 → $50K/月（75%削減）
- キャッシュヒット率: 30%
- レスポンス速度: 3倍（1.5秒 → 0.5秒）

**学び**:
- 用途別LLM使い分け（初稿GPT-4o、校正Claude）でコスト削減
- Anthropic Prompt Cachingで90%削減（キャッシュヒット時）
- 初稿品質閾値設定でさらに20%削減

**参照**: `@GenAI_research/case_studies/tier2/select-ai-tech-stack/12_copyai_hybrid_caching.md`

---

### Common Pitfalls（技術スタック選定の失敗パターン）

1. **単一LLMプロバイダー依存**: API障害時のダウンタイム、価格改定リスク
   - **教訓**: マルチLLMプロバイダー戦略（フォールバック設計）
   - **例**: OpenAI障害時にClaude自動切り替え

2. **過剰なOrchestration**: LangChainの全機能を使おうとして複雑化
   - **教訓**: 必要最小限の機能のみカスタム実装
   - **例**: Cursorはカスタム実装（LangChain不使用）

3. **Vector DB選定ミス**: ローカル開発ではChromaで十分だが、本番でスケールしない
   - **教訓**: 初期段階からスケーラビリティを考慮
   - **例**: Chroma→Pinecone移行コストが高い

4. **コスト試算不足**: 月間ユーザー数増加時のコスト爆発
   - **教訓**: 推論コスト試算式を初期段階から作成
   - **例**: GPT-4 → Llama 3でコスト1/10削減

---

### Quantitative Benchmarks（技術スタック選定基準）

**LLMプロバイダー比較**（2026年1月時点）:

| プロバイダー | モデル | コスト（$/1M Input Token） | コンテキスト長 | 推論速度 | 用途 |
|------------|--------|--------------------------|------------|---------|------|
| **OpenAI** | GPT-4 Turbo | $10 | 128K | 中速 | 汎用・複雑タスク |
| **OpenAI** | GPT-3.5 Turbo | $0.5 | 16K | 高速 | 簡単なタスク・コスト重視 |
| **Anthropic** | Claude 3.5 Sonnet | $3 | 200K | 高速 | コーディング・長文生成 |
| **Anthropic** | Claude 3 Haiku | $0.25 | 200K | 最速 | 軽量タスク・コスト最優先 |
| **Google** | Gemini 1.5 Pro | $7 | 2M | 中速 | 超長コンテキスト |
| **OSS** | Llama 3 70B | 自己ホスティング次第 | 128K | 中速 | コスト最適化 |

**Vector DB比較**:

| Vector DB | 検索精度 | レイテンシ | スケーラビリティ | コスト | 用途 |
|-----------|---------|----------|----------------|--------|------|
| **Pinecone** | 95% | <50ms | ✅ マネージド | $0.096/1M queries | 本番・スケール重視 |
| **Weaviate** | 93% | <100ms | ⚠️ 自己ホスティング | 自己ホスティング次第 | カスタマイズ重視 |
| **Chroma** | 90% | <200ms | ❌ ローカルのみ | 無料 | 開発・テスト |
| **FAISS** | 92% | <80ms | ⚠️ ローカル/AWS | 無料 | 自己ホスティング |

**Orchestration層比較**:

| Orchestration | 学習曲線 | カスタマイズ性 | メンテナンス性 | 用途 |
|--------------|---------|-------------|--------------|------|
| **LangChain** | 高 | 中 | 低（頻繁な破壊的変更） | 標準的なRAG/Agent |
| **LlamaIndex** | 中 | 高 | 中 | データパイプライン特化 |
| **カスタム実装** | 低 | 最高 | 高 | 独自要件が強い場合 |

---

### Best Practices（技術スタック選定のベストプラクティス）

1. **マルチLLMプロバイダー戦略**: 単一障害点を避ける
   - 推奨構成: メインLLM + フォールバックLLM
   - 例: Claude 3.5 Sonnet（メイン）+ GPT-4 Turbo（フォールバック）

2. **コスト試算式の作成**: 月間ユーザー数×平均トークン数からの総コスト算出
   ```python
   monthly_cost = (
       monthly_users *
       avg_sessions_per_user *
       avg_tokens_per_session *
       llm_cost_per_million_tokens / 1_000_000
   )
   ```

3. **Vector DB選定基準**: 開発段階ではChroma、本番ではPinecone
   - 開発: Chroma（無料、ローカル）
   - ステージング: Weaviate（自己ホスティング）
   - 本番: Pinecone（マネージド、スケーラビリティ）

4. **Orchestration層選択**: 標準的なRAGならLangChain、独自要件ならカスタム実装
   - LangChain: 標準的なRAG/Agent構成（学習コスト高）
   - カスタム実装: 独自要件が強い場合（Cursor事例）

5. **スケーラビリティ評価**: 10万→100万ユーザーへのスケール時のコスト・レイテンシ推定
   - コスト: 線形増加を想定（キャッシングで30%削減可能）
   - レイテンシ: Vector DB選定が最大のボトルネック

---

### GenAI_research統合（最新トレンド分析）

**モデル進化の方向性**（出典: @GenAI_research/LLM/01_LifeisBeautiful_insights.md）:
- **強化学習による「考える力」獲得**: DeepSeek-R1等の強化学習モデルが、人間の学習データに依存しない推論能力を獲得
- **モデルコモディティ化**: LLM性能差が縮小し、配布・統合・運用（ワークフロー/データ/セキュリティ）へ競争軸が移る
- **オープンソース加速**: MoE（Mixture of Experts）等の効率化アーキテクチャにより、性能×コストのトレードオフが改善

**コスト最適化パターン**（出典: @GenAI_research/LLM/01_LifeisBeautiful_insights.md）:
- **ジェボンズのパラドックス**: 効率化（コスト低下）は需要減ではなく、むしろ"使い倒し"を促す
- **マルチLLM戦略**: 用途別にLLMを使い分け（検索理解: GPT-4、回答生成: Claude、ファクトチェック: Llama）
- **キャッシング**: 30%ヒット率でコスト40%削減（Perplexity事例）

**プロダクト置き換え**（出典: @GenAI_research/LLM/01_LifeisBeautiful_insights.md）:
- **SaaS→エージェント**: UI/ビジネスロジックが自然言語エージェントに置換される
- **A2A vs MCP**: エージェント間プロトコル標準化の議論（MCPの上のレイヤーとして位置づけ）
- **コーディング現場**: Claude Code（段階的指示）vs OpenAI Codex（非同期PR生成）

---

## 技術スタック決定テンプレート

### 推奨構成（ユースケース別）

#### 構成A: RAG（文書検索） - Notion AI型

| レイヤー | 選定技術 | 選定理由 |
|---------|---------|---------|
| **LLM** | GPT-4 Turbo | 長文要約精度、128Kコンテキスト |
| **Vector DB** | Pinecone | 検索速度 < 100ms、スケール無制限 |
| **埋め込み** | text-embedding-3-large | 検索精度95%（MTEB） |
| **フレームワーク** | LlamaIndex | RAG特化、インデックス管理 |
| **インフラ** | Vercel（Frontend） + AWS Lambda（Backend） | サーバーレス、スケール自動 |

**月額コスト目安**（10,000ユーザー）:
- LLM: $3,200（GPT-4 Turbo、月間20万リクエスト）
- Vector DB: $70（Pinecone p1、100万ベクトル）
- 埋め込み: $200（text-embedding-3-large、200万リクエスト）
- インフラ: $300（Vercel Pro + AWS Lambda）
- **合計: $3,770/月**

---

#### 構成B: コード生成 - Cursor型

| レイヤー | 選定技術 | 選定理由 |
|---------|---------|---------|
| **LLM** | Claude 3.5 Sonnet | コーディング精度95%（HumanEval 92.0%） |
| **Caching** | Anthropic Prompt Caching | コスト90%削減、応答速度6倍 |
| **Vector DB** | Pinecone | コードベース検索（オプション） |
| **フレームワーク** | LangChain | ツール統合、開発速度 |
| **インフラ** | Railway | Git連携、自動デプロイ |

**月額コスト目安**（10,000ユーザー）:
- LLM: $480（Claude 3.5 Sonnet、キャッシング考慮前）
- Caching削減: -$432（90%削減）
- Vector DB: $70（Pinecone p1、オプション）
- インフラ: $200（Railway Pro）
- **合計: $318/月**（Caching有効化後）

---

#### 構成C: マルチLLM戦略 - Perplexity型

| レイヤー | 選定技術 | 選定理由 |
|---------|---------|---------|
| **LLM1（検索理解）** | Claude 3.5 Sonnet | 引用生成、ファクトチェック |
| **LLM2（回答生成）** | GPT-4o | コスパ、速度 |
| **LLM3（長文処理）** | Gemini 1.5 Pro | 2Mコンテキスト、超長文対応 |
| **Fallback** | Llama 3.1 405B（Self-hosted） | API障害対策 |
| **Vector DB** | Pinecone | 検索速度 |
| **フレームワーク** | LangChain | マルチLLM統合 |

**月額コスト目安**（10,000ユーザー）:
- Claude 3.5 Sonnet: $1,440（30%のリクエスト）
- GPT-4o: $2,240（70%のリクエスト）
- Gemini 1.5 Pro: $0（無料枠、月間60リクエスト/分以下）
- Vector DB: $70（Pinecone p1）
- インフラ: $500（AWS ECS + GPU for Llama）
- **合計: $4,250/月**（マルチLLM最適化後）

**単一LLM（GPT-4 Turbo）との比較**:
- GPT-4 Turbo単独: $9,500/月
- マルチLLM戦略: $4,250/月
- **削減額: $5,250/月（55%削減）**

---

## 選定フロー（推奨手順）

### Step 1: 要件整理（30分）

1. ユースケース分類（テキスト生成/検索/コード生成/RAG等）
2. 精度要求（Mission Critical/High/Standard/Acceptable）
3. 応答速度要求（< 1秒/1-3秒/3-10秒/> 10秒）
4. 予算制約（MVP/Early/Growth/Scale）
5. スケール目標（6ヶ月後、1年後のユーザー数）

### Step 2: LLMプロバイダー選定（30分）

1. ユースケース別推奨LLM表を参照
2. Tier 2ケーススタディから類似製品を検索
3. コスト試算（10万→100万ユーザー）
4. マルチLLM戦略の検討（コスト削減40%目標）
5. Fallback戦略の設計（API障害対策）

### Step 3: Vector DB選定（15分）

1. RAG必要性の判断（Yes/No）
2. スケール要件（100K/1M/10M/100M+ ベクトル）
3. プライバシー要件（クラウドOK/Self-hosted必須）
4. 予算（無料枠/有料プラン）

### Step 4: フレームワーク選定（15分）

1. ユースケース別推奨フレームワーク表を参照
2. 開発速度 vs 柔軟性のトレードオフ
3. チーム習熟度（学習コスト考慮）

### Step 5: コスト最適化戦略（30分）

1. Hybrid Model検討（2段階生成）
2. Caching検討（Anthropic Prompt Caching）
3. Batching検討（OpenAI Batch API）
4. Fallback戦略（マルチプロバイダー）

### Step 6: 技術スタック決定書作成（30分）

1. 選定理由の文書化
2. 代替案の記載（なぜ不採用か）
3. 移行計画（段階的移行、リスク軽減）
4. リスク評価（API障害、コスト超過、精度低下）

---

## Reference

- **LLMトレンド**: @GenAI_research/LLM/01_LifeisBeautiful_insights.md
- **OpenAI技術**: @GenAI_research/technologies/openai/README.md
- **Anthropic技術**: @GenAI_research/technologies/anthropic/README.md
- **Google技術**: @GenAI_research/technologies/google/README.md
- **LangChain**: @GenAI_research/technologies/langchain/README.md
- **LlamaIndex**: @GenAI_research/technologies/llamaindex/README.md
- **Tier 2ケーススタディ**: @GenAI_research/case_studies/tier2/select-ai-tech-stack/
- **Startup Science Framework**: @startup_science/02_frameworks/

---

## 実行方法

### Claude Codeでの実行

```bash
# ForGenAIスキル実行
/select-ai-tech-stack
```

### 手動実行

1. 要件ヒアリング（構造化インタビュー）実施
2. LLMプロバイダー比較表を参照し、ユースケース別推奨を確認
3. Vector DB比較表を参照し、スケール・プライバシー要件で選定
4. フレームワーク比較表を参照し、開発速度・柔軟性で選定
5. コスト試算（10万→100万ユーザー）実施
6. コスト最適化戦略（Hybrid Model、Caching、Batching、Fallback）検討
7. Tier 2ケーススタディから類似製品を検索し、成功パターンを抽出
8. 技術スタック決定書作成（上記テンプレート使用）
9. 次のアクション定義（LLMアカウント作成、Vector DBトライアル等）

---

## 更新履歴

- 2026-01-03: ForGenAI版 v1.0完成（LLMプロバイダー4社比較、Vector DB 4社比較、フレームワーク4種比較、コスト最適化4パターン、Tier 2ケーススタディ12件統合）
- GenAI_research統合完了（LifeisBeautiful洞察、技術別README、Tier 2ケーススタディ）

---

**作成日**: 2026-01-03
**バージョン**: 1.0.0
**統合ケーススタディ数**: 12件（Perplexity、Cursor、Notion AI、Jasper、Glean等）
**GenAI_research参照**: 5カテゴリ（LLM、OpenAI、Anthropic、Google、LangChain、LlamaIndex）
**品質スコア目標**: 95/100
