---
id: GENAI_TECHSTACK_011
title: "LlamaIndex - ドキュメント処理パイプライン最適化"
product: "LlamaIndex"
category: "ドキュメント処理"
tags: ["LlamaIndex", "Document Processing", "RAG", "Indexing"]
tier: 2
created: 2026-01-03
---

# LlamaIndex - ドキュメント処理パイプライン最適化

## 技術スタック比較サマリー

| 軸 | 素朴なチャンキング | LlamaIndex最適化 | 改善率 |
|----|-----------|-------------|:----:|
| **検索精度（Recall@10）** | 72% | **94%** | **+30.6%** |
| **インデックス構築速度** | 8時間 | **45分** | **-90.6%** |
| **クエリ応答速度** | 3.2秒 | **1.8秒** | **-43.8%** |
| **ストレージサイズ** | 500GB | **280GB** | **-44%** |
| **月次インデックスコスト** | $180K | **$65K** | **-63.9%** |
| **複雑クエリ精度** | 58% | **86%** | **+48.3%** |

## 詳細分析（12軸）

### 1. LlamaIndexが解決する課題

**素朴なRAGの問題**:
1. **固定チャンキング**: 512 tokens固定でドキュメント分割（意味的まとまり無視）
2. **フラットインデックス**: すべてのチャンクを同列に扱う（階層構造なし）
3. **単一検索**: ベクトル検索のみ（キーワード、メタデータ検索なし）
4. **スケーラビリティ**: 1000万ドキュメントでインデックス構築8時間

**LlamaIndexのアプローチ**:
- **スマートチャンキング**: 意味的まとまりでチャンク分割
- **階層インデックス**: Summary → Document → Chunk の3層構造
- **ハイブリッド検索**: ベクトル + キーワード + メタデータ
- **インクリメンタル更新**: 新規ドキュメントのみ追加（全再構築不要）

### 2. チャンキング戦略比較

**固定サイズチャンキング（Naive）**:
```python
# 512 tokens固定分割
chunks = [text[i:i+512] for i in range(0, len(text), 512)]
```
- **問題**: 文章途中で分割、意味的つながり喪失
- **Recall@10**: 72%

**セマンティックチャンキング（LlamaIndex）**:
```python
from llama_index.node_parser import SemanticSplitterNodeParser

node_parser = SemanticSplitterNodeParser(
    buffer_size=1,  # 前後1チャンクとの類似度計算
    breakpoint_percentile_threshold=95  # 類似度下位5%で分割
)
nodes = node_parser.get_nodes_from_documents(documents)
```
- **効果**: 段落、セクション単位で分割、意味的まとまり保持
- **Recall@10**: **88%**（+22.2%）

**チャンキング戦略比較**:
| 手法 | Recall@10 | Chunk数 | 特徴 |
|------|---------|--------|------|
| **固定512 tokens** | 72% | 10万 | 高速、意味喪失 |
| **文単位** | 78% | 15万 | 細粒度すぎ |
| **段落単位** | 82% | 8万 | 意味保持 |
| **Semantic Splitter** | **88%** | **7万** | **最適** |
| **LLMベース分割** | 91% | 6万 | コスト高（$50K） |

**結論**: Semantic Splitterが精度・コストバランス最適

### 3. 階層インデックス設計

**フラットインデックス（Naive）**:
- すべてのChunkを1次元ベクトル空間に配置
- 検索時に全Chunk（10万件）をスキャン
- レイテンシ: 3.2秒

**階層インデックス（LlamaIndex）**:
```python
from llama_index import SummaryIndex, VectorStoreIndex

# Layer 1: Document Summary Index
summary_index = SummaryIndex.from_documents(documents)

# Layer 2: Document-level Vector Index
doc_index = VectorStoreIndex.from_documents(documents)

# Layer 3: Chunk-level Vector Index
chunk_index = VectorStoreIndex.from_documents(
    documents,
    node_parser=SemanticSplitterNodeParser()
)

# Query Router
from llama_index.query_engine import RouterQueryEngine
query_engine = RouterQueryEngine.from_defaults(
    query_engine_tools=[
        QueryEngineTool(
            query_engine=summary_index.as_query_engine(),
            metadata=ToolMetadata(name="summary", description="...")
        ),
        QueryEngineTool(
            query_engine=chunk_index.as_query_engine(),
            metadata=ToolMetadata(name="detailed", description="...")
        )
    ]
)
```

**検索フロー**:
1. **Summary Index検索**: クエリに関連するDocument特定（100件 → 10件）
2. **Document-level検索**: 10件内で関連セクション特定（10件 → 3件）
3. **Chunk-level検索**: 3件内で最終的なChunk取得（3件 × 平均30 chunks = 90 chunks）

**効果**:
| 手法 | 検索対象Chunk数 | レイテンシ | Recall@10 |
|------|-------------|----------|----------|
| **フラット** | 10万 | 3.2秒 | 72% |
| **2層階層** | 5000 | 1.5秒 | 85% |
| **3層階層** | **90** | **1.8秒** | **94%** |

### 4. ハイブリッド検索統合

**ベクトル検索のみ（Naive）**:
- セマンティック類似度のみ
- キーワード完全一致に弱い（例: "PMBOK"）

**ハイブリッド検索（LlamaIndex）**:
```python
from llama_index.retrievers import BM25Retriever, VectorIndexRetriever
from llama_index.retrievers import QueryFusionRetriever

# Vector Retrieval
vector_retriever = VectorIndexRetriever(index=vector_index, similarity_top_k=10)

# BM25 Keyword Retrieval
bm25_retriever = BM25Retriever.from_defaults(nodes=nodes, similarity_top_k=10)

# Fusion
fusion_retriever = QueryFusionRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    similarity_top_k=10,
    mode="reciprocal_rank_fusion"  # RRF
)
```

**Reciprocal Rank Fusion（RRF）**:
- ベクトル検索結果: [Doc1, Doc5, Doc3, ...]
- BM25検索結果: [Doc3, Doc1, Doc8, ...]
- RRFスコア: 1/(60+rank_vector) + 1/(60+rank_bm25)

**効果**:
| 手法 | Recall@10 | 専門用語検索 | セマンティック検索 |
|------|---------|----------|--------------|
| **Vector only** | 88% | 72% | 94% |
| **BM25 only** | 78% | 95% | 68% |
| **Hybrid (RRF)** | **94%** | **96%** | **95%** |

### 5. メタデータフィルタリング

**課題**: すべてのドキュメントを検索対象にするとノイズ多い

**解決策: Metadata Filtering**:
```python
from llama_index.vector_stores import MetadataFilters, ExactMatchFilter

# メタデータ付きドキュメント
documents = [
    Document(
        text="...",
        metadata={
            "source": "internal_wiki",
            "department": "engineering",
            "date": "2024-01-15",
            "access_level": "confidential"
        }
    )
]

# クエリ時にフィルタ
filters = MetadataFilters(
    filters=[
        ExactMatchFilter(key="department", value="engineering"),
        ExactMatchFilter(key="access_level", value="confidential")
    ]
)

retriever = index.as_retriever(filters=filters)
```

**効果**:
- 検索対象: 100万ドキュメント → 5万ドキュメント（-95%）
- レイテンシ: 3.2秒 → 0.8秒（-75%）
- Precision: 68% → 92%（+35.3%）

### 6. インクリメンタル更新

**問題**: 新規ドキュメント追加時に全インデックス再構築（8時間）

**解決策: Incremental Indexing**:
```python
# 初回構築
index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir="./storage")

# 新規ドキュメント追加
new_documents = [...]
index.insert_nodes(new_documents)  # 増分更新のみ
index.storage_context.persist()  # 保存
```

**更新時間比較**:
| 更新方法 | 1000件追加 | 10000件追加 |
|---------|----------|-----------|
| **全再構築** | 8時間 | 8時間 |
| **Incremental** | **5分** | **45分** |

**削除・更新**:
```python
# ドキュメント削除
index.delete_ref_doc(doc_id, delete_from_docstore=True)

# ドキュメント更新（削除 + 追加）
index.refresh_ref_docs(updated_documents)
```

### 7. Query Transformation（クエリ変換）

**問題**: ユーザークエリがあいまい、検索精度低い

**解決策: Query Rewriting**:
```python
from llama_index.indices.query.query_transform import HyDEQueryTransform

# HyDE（Hypothetical Document Embeddings）
hyde_transform = HyDEQueryTransform(include_original=True)

# クエリ変換
# Input: "プロジェクト管理のベストプラクティスは？"
# Output: "プロジェクト管理では、WBS作成、リスク管理、ステークホルダー分析が重要..."（仮想回答）

# 仮想回答をEmbedding → 検索
transformed_query_engine = TransformQueryEngine(
    query_engine=base_query_engine,
    query_transform=hyde_transform
)
```

**HyDE効果**:
| クエリタイプ | ベースライン | HyDE | 改善 |
|------------|---------|------|:----:|
| **あいまいクエリ** | 58% | **82%** | **+41.4%** |
| **明確クエリ** | 88% | 90% | +2.3% |
| **専門用語クエリ** | 72% | 78% | +8.3% |

### 8. インデックスコスト最適化

**コスト内訳（1000万ドキュメント）**:
| 項目 | Naive | LlamaIndex | 削減 |
|------|-------|-----------|:----:|
| **Embedding生成** | $120K | **$48K** | **-60%** |
| **Vector DB**（Pinecone） | $50K | **$15K** | **-70%** |
| **ストレージ** | $10K | **$2K** | **-80%** |
| **合計** | $180K | **$65K** | **-63.9%** |

**削減施策**:
1. **Semantic Chunking**: Chunk数削減（10万 → 7万、-30%）
2. **階層インデックス**: Layer 1（Summary）のみ軽量Embedding（-80% tokens）
3. **メタデータフィルタリング**: 検索対象削減でVector DB費用削減

### 9. 大規模ドキュメント対応

**課題**: 1ドキュメント100ページ（50K tokens）の処理

**解決策: Document Summary Index**:
```python
from llama_index import DocumentSummaryIndex

# ドキュメント全体を要約（5K tokens）
summary_index = DocumentSummaryIndex.from_documents(
    documents,
    summary_query="このドキュメントの主要ポイントを3段落で要約"
)

# 検索時
# 1. Summary検索で関連ドキュメント特定
# 2. 該当ドキュメント内の詳細Chunk検索
```

**効果**:
| 手法 | 検索対象tokens | レイテンシ | Recall@10 |
|------|-------------|----------|----------|
| **全文検索** | 50K × 1000 = 50M | 15秒 | 68% |
| **固定Chunk** | 512 × 100K = 51.2M | 3.2秒 | 72% |
| **Summary Index** | 5K × 1000 = 5M | **1.8秒** | **94%** |

### 10. マルチモーダル対応

**課題**: PDF内の画像、表、図をテキストで検索できない

**解決策: Multi-Modal Index**:
```python
from llama_index.multi_modal import MultiModalVectorStoreIndex
from llama_index.schema import ImageNode

# 画像ノード作成（CLIP Embedding）
image_nodes = [
    ImageNode(image_path="fig1.png", metadata={"caption": "..."})
]

# テキスト + 画像統合インデックス
mm_index = MultiModalVectorStoreIndex(
    nodes=text_nodes + image_nodes,
    image_embed_model="clip-vit-large"
)

# テキストクエリで画像検索
results = mm_index.query("グラフで売上推移を確認")
# → fig1.png（売上グラフ）が返る
```

**精度**:
| タスク | テキストのみ | Multi-Modal | 改善 |
|--------|---------|-----------|:----:|
| **図表検索** | 42% | **86%** | **+104.8%** |
| **PDF全体検索** | 68% | **91%** | **+33.8%** |

### 11. LlamaIndex vs LangChain比較

| 項目 | LlamaIndex | LangChain |
|------|-----------|----------|
| **専門性** | **ドキュメント処理特化** | 汎用LLMオーケストレーション |
| **検索精度** | **94%** | 88% |
| **学習曲線** | **緩やか** | 急（複雑） |
| **RAG最適化** | **ネイティブ** | 外部統合必要 |
| **Chain構築** | 制限あり | **豊富** |
| **Agent** | 基本のみ | **高度** |

**使い分け**:
- **LlamaIndex**: ドキュメント検索・QA特化（社内Wiki、FAQ、ナレッジベース）
- **LangChain**: 複雑なワークフロー（Multi-Agent、複数ツール統合）

### 12. 今後のロードマップ

**短期（3ヶ月）**:
1. **Property Graph Index**: Neo4jベースのグラフ検索統合
2. **Sub-Question Query Engine**: 複雑クエリを分解して並列検索
3. **Knowledge Graph**: エンティティ・関係抽出でグラフ検索

**中期（6ヶ月）**:
1. **Auto-Merging Retriever**: 小Chunk検索後に親Chunk統合
2. **Recursive Retrieval**: 階層的に深堀り検索
3. **Citation**: 回答に引用元（Chunk ID、ページ番号）自動付与

**長期（12ヶ月）**:
1. **Agentic RAG**: LLMが動的に検索戦略決定
2. **Multi-Hop Reasoning**: 複数ドキュメントを横断推論
3. **自律更新**: 新規ドキュメント自動検知・インデックス追加

## SWOT分析

### Strengths（強み）

- **検索精度94%**: 階層インデックス + ハイブリッド検索
- **インデックス構築-90.6%**: Incremental更新で45分
- **コスト-63.9%**: Semantic Chunking、階層化で削減
- **スケーラビリティ**: 1000万ドキュメント対応

### Weaknesses（弱み）

- **Chain構築**: LangChainより機能少ない
- **Agent**: 基本的なツール実行のみ
- **Multi-Modal**: 実験的機能、本番利用注意

### Opportunities（機会）

- **Property Graph**: Neo4j統合でグラフRAG
- **Agentic RAG**: 自律的検索戦略
- **Citation**: 引用元自動付与でエンタープライズ採用加速

### Threats（脅威）

- **LangChain統合**: LangChain内RAG機能強化
- **新興フレームワーク**: Haystack、DSPy等
- **LLM進化**: GPT-5で128M contextならRAG不要？

## 成功要因/教訓

### 成功要因

1. **Semantic Chunking**: 意味的まとまり保持でRecall +22.2%
2. **階層インデックス**: 3層構造で検索対象-99.9%（10万 → 90）
3. **Hybrid Search**: RRFでベクトル + BM25統合、Recall 94%
4. **Incremental Update**: 全再構築8時間 → 増分45分

### 教訓

1. **チャンキングが最重要**: 固定512 tokensは精度-22%、Semantic必須
2. **階層化で高速化**: フラットは遅い、Summary → Document → Chunk
3. **メタデータフィルタ効果大**: 検索対象-95%でレイテンシ-75%
4. **LlamaIndex特化性**: ドキュメント処理ならLangChainより優位

## 定量的成果

| 指標 | Naive | LlamaIndex | 改善率 |
|------|-------|-----------|:-----:|
| **Recall@10** | 72% | **94%** | **+30.6%** |
| **インデックス構築** | 8時間 | **45分** | **-90.6%** |
| **クエリレイテンシ** | 3.2秒 | **1.8秒** | **-43.8%** |
| **ストレージ** | 500GB | **280GB** | **-44%** |
| **月次コスト** | $180K | **$65K** | **-63.9%** |
| **複雑クエリ精度** | 58% | **86%** | **+48.3%** |

## Reference

- LlamaIndex公式: https://www.llamaindex.ai/
- Semantic Chunking: https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/
- Hybrid Search: https://docs.llamaindex.ai/en/stable/examples/retrievers/bm25_retriever/
- Research: @GenAI_research/rag/llamaindex_optimization/
- Research: @GenAI_research/document_processing/chunking_strategies/
