---
id: GENAI_PROMPT_008
title: "Midjourney - Prompt Guide Optimization"
product: Midjourney
pattern: "Structured Prompt Format"
improvement: "画像生成成功率 70% → 92%"
tags: ["Prompt Optimization", "Midjourney", "Image Generation", "Prompt Format"]
tier: 2
---

# Midjourney - Prompt Guide Optimization

## プロンプト最適化サマリー

| 指標 | 改善前 | 改善後 | 改善率 |
|------|--------|--------|--------|
| 画像生成成功率 | 70% | 92% | +22% |
| ユーザー満足度 | 68% | 88% | +20% |
| 1回目で満足 | 35% | 72% | +37% |
| 再生成回数 | 3.2回 | 1.5回 | -1.7回 |

## 最適化戦略

### 構造化プロンプトフォーマット

**改善前**:
```
/imagine beautiful sunset
```

**改善後（構造化フォーマット）**:
```
/imagine [主題], [スタイル], [構図], [照明], [品質指定]

例:
/imagine a serene sunset over ocean, oil painting style, wide angle composition, warm golden hour lighting, high quality, detailed, 4K, --ar 16:9 --v 6
```

**構造化要素**:
1. **主題（Subject）**: 何を描くか
2. **スタイル（Style）**: oil painting, watercolor, photorealistic等
3. **構図（Composition）**: wide angle, close-up, bird's eye view等
4. **照明（Lighting）**: golden hour, dramatic lighting, soft light等
5. **品質指定（Quality）**: high quality, detailed, 4K等
6. **パラメータ（Parameters）**: --ar 16:9（アスペクト比）、--v 6（バージョン）

## 成功要因

1. **構造化プロンプト**: 成功率+22%（最大改善幅）
2. **1回目満足率+37%**: 再生成回数激減
3. **プロンプト共有文化**: Discord内で高品質プロンプト共有

## 教訓

- **構造化フォーマット強力**: 画像生成で特に効果大
- **パラメータ活用**: --ar、--v等のパラメータで品質向上
- **コミュニティ学習**: Discord内でベストプラクティス共有

## 参照

- **出典**: Midjourney Prompt Guide (2024)
