# Topics - トピック別インデックス

このディレクトリには、AI/GenAI技術のトピック別に分類されたトランスクリプトへのシンボリックリンクを格納します。

## カテゴリ一覧

### agents/ - AIエージェント（420ファイル、89.6%）
- AIエージェント設計・開発
- マルチエージェントシステム
- エージェント間協調・連携
- 自律型AIシステム

### llm/ - 大規模言語モデル（356ファイル、75.9%）
- LLM基礎理解
- GPT-4、Claude、Geminiの比較・活用
- LLMの限界と対策（ハルシネーション等）
- 日本語LLMの特性

### rag/ - Retrieval-Augmented Generation（264ファイル、56.3%）
- RAGアーキテクチャ設計
- ベクトルデータベース（Pinecone、Chroma等）
- Embedding生成・最適化
- ハイブリッド検索戦略

### prompt_engineering/ - プロンプトエンジニアリング（306ファイル、65.2%）
- プロンプト設計技法
- Few-shot/Zero-shot Learning
- Chain-of-Thought（CoT）推論
- プロンプト最適化・テンプレート

### fine_tuning/ - モデルファインチューニング（56ファイル、11.9%）
- ファインチューニング手法
- PEFT（Parameter-Efficient Fine-Tuning）
- LoRA（Low-Rank Adaptation）
- ドメイン特化モデル作成

## 使用方法

各サブディレクトリには、該当トピックを含むトランスクリプトへのシンボリックリンクが配置されます。

例：
```bash
cd topics/agents/
ls -lah  # AIエージェント関連の全トランスクリプトを表示
```

## 更新方法

T005-5タスクで自動分類スクリプト（`scripts/t005_5_classify_transcripts.py`）により、メタデータのtopic_tagsに基づいてシンボリックリンクが自動生成されます。

---

**管理者**: Founder Agent System
**最終更新**: 2025-12-30
