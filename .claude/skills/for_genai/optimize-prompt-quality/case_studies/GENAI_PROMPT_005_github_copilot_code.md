---
id: GENAI_PROMPT_005
title: "GitHub Copilot - Code Completion Few-shot Optimization"
product: GitHub Copilot
pattern: "Few-shot + Code Comments"
improvement: "精度 75% → 88%"
tags: ["Prompt Optimization", "Few-shot", "GitHub Copilot", "Code"]
tier: 2
---

# GitHub Copilot - Code Completion Few-shot Optimization

## プロンプト最適化サマリー

| 指標 | 改善前 | 改善後 | 改善率 |
|------|--------|--------|--------|
| コード補完精度 | 75% | 88% | +13% |
| 応答速度 | 2.2秒 | 1.8秒 | -0.4秒 |
| 開発速度 | 1.5倍 | 2.5倍 | +67% |
| バグ率 | 15% | 8% | -7% |

## 最適化戦略

### Few-shot + コメント活用

**改善後プロンプト（コード内）**:
```python
# 例1: リスト内包表記でフィルタリング
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]

# 例2: 辞書内包表記
squares = {n: n**2 for n in range(1, 6)}

# 例3: map関数での変換
doubled = list(map(lambda x: x * 2, numbers))

# では、以下の関数を実装してください:
# ユーザーのリストから、年齢が18歳以上のユーザーのみを抽出する
users = [{"name": "Alice", "age": 25}, {"name": "Bob", "age": 15}]
# → GitHub CopilotがFew-shotから学習し、リスト内包表記を提案
```

## 成功要因

1. **コード補完精度+13%**: Few-shot examplesによる学習効果
2. **開発速度2.5倍**: コード生成速度向上
3. **バグ率-7%**: 高品質コード生成

## 参照

- **出典**: GitHub Copilot Research (2023)
