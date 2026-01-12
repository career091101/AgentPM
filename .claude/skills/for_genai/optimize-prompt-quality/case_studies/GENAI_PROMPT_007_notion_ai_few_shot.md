---
id: GENAI_PROMPT_007
title: "Notion AI - Document Summarization Few-shot Optimization"
product: Notion AI
pattern: "Few-shot Learning"
improvement: "要約精度 82% → 88%"
tags: ["Prompt Optimization", "Few-shot", "Notion AI", "Summarization"]
tier: 2
---

# Notion AI - Document Summarization Few-shot Optimization

## プロンプト最適化サマリー

| 指標 | 改善前 | 改善後 | 改善率 |
|------|--------|--------|--------|
| 要約精度 | 82% | 88% | +6% |
| 応答速度 | 3.5秒 | 3.2秒 | -0.3秒 |
| トークン数 | 450 | 290 | -36% |
| プロンプトコスト | $0.028/1K | $0.018/1K | -36% |

## 最適化戦略

### Few-shot Examples（要約タスク）

**改善後プロンプト**:
```
以下のドキュメントを要約してください（3文以内）。

例1:
入力: 「AIは急速に発展しており、2025年にはGPT-5がリリースされる見込みです。GPT-5は...（500語）」
出力: 「GPT-5が2025年にリリース予定。性能大幅向上、マルチモーダル対応。」

例2:
入力: 「プロンプトエンジニアリングは、AI精度を向上させる重要な技術です...（500語）」
出力: 「プロンプトエンジニアリングがAI精度向上に重要。Chain-of-Thought、Few-shot等のパターン活用。」

では、以下を要約してください:
```

## 成功要因

1. **要約精度+6%**: Few-shot examplesによる学習
2. **トークン数-36%**: 簡潔な要約フォーマット学習
3. **コスト削減-36%**: トークン削減効果大

## 参照

- **出典**: Notion AI Blog (2023)
