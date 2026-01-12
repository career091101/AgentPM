---
id: GENAI_PROMPT_006
title: "Cursor - System Message Optimization"
product: Cursor
pattern: "System Message Design"
improvement: "コード生成精度 80% → 88%"
tags: ["Prompt Optimization", "System Message", "Cursor", "IDE"]
tier: 2
---

# Cursor - System Message Optimization

## プロンプト最適化サマリー

| 指標 | 改善前 | 改善後 | 改善率 |
|------|--------|--------|--------|
| コード生成精度 | 80% | 88% | +8% |
| 応答速度 | 2.0秒 | 1.8秒 | -0.2秒 |
| バグ率 | 18% | 6% | -12% |
| ユーザー満足度 | 78% | 92% | +14% |

## 最適化戦略

### System Message最適化

**改善前**:
```
System: あなたは優秀なAIアシスタントです。
```

**改善後**:
```
System: あなたは上級エンジニア（10年以上の経験）です。

役割：
- 高品質で保守性の高いコードを生成する
- ベストプラクティスに従う
- セキュリティとパフォーマンスを重視する

制約：
- TypeScript優先（型安全性）
- コメントは簡潔に
- テストコードも生成する

出力フォーマット：
- コードブロックで囲む
- 説明は3行以内
```

## 成功要因

1. **役割定義明確化**: 「上級エンジニア」と明記
2. **ベストプラクティス強制**: バグ率-12%
3. **出力フォーマット統一**: 一貫性向上

## 参照

- **出典**: Cursor Documentation (2024)
