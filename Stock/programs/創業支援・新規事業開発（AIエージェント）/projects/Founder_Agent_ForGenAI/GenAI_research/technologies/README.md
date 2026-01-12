# Technologies - 技術スタック別インデックス

このディレクトリには、具体的な技術・プロダクト・フレームワーク別に分類されたトランスクリプトへのシンボリックリンクを格納します。

## カテゴリ一覧

### langchain/ - LangChain
- LangChainフレームワークの使用方法
- Chainの構築パターン
- Agentの実装事例

### llamaindex/ - LlamaIndex
- LlamaIndexによるRAG実装
- インデックス構築戦略
- クエリエンジンの最適化

### openai/ - OpenAI
- OpenAI APIの活用
- GPT-4/GPT-3.5の比較
- Assistants API
- Fine-tuning

### anthropic/ - Anthropic Claude
- Claude APIの統合
- Claude vs GPT比較
- プロンプトキャッシング
- Function Calling

### chatgpt/ - ChatGPT
- ChatGPTの活用事例
- プラグイン開発
- カスタムGPTs
- エンタープライズ利用

## 使用方法

各サブディレクトリには、該当技術を使用・言及しているトランスクリプトへのシンボリックリンクが配置されます。

例：
```bash
cd technologies/langchain/
ls -lah  # LangChain関連の全トランスクリプトを表示
```

## 更新方法

T005-5タスクで自動分類スクリプト（`scripts/t005_5_classify_transcripts.py`）により、メタデータのtechnologies_mentionedに基づいてシンボリックリンクが自動生成されます。

---

**管理者**: Founder Agent System
**最終更新**: 2025-12-30
