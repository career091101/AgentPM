---
id: GENAI_PROMPT_009
title: "Runway ML - Gen-2 Video Prompt Optimization"
product: Runway ML (Gen-2)
pattern: "Detailed Descriptive Prompts"
improvement: "動画生成成功率 75% → 85%"
tags: ["Prompt Optimization", "Runway ML", "Video Generation", "Gen-2"]
tier: 2
---

# Runway ML - Gen-2 Video Prompt Optimization

## プロンプト最適化サマリー

| 指標 | 改善前 | 改善後 | 改善率 |
|------|--------|--------|--------|
| 動画生成成功率 | 75% | 85% | +10% |
| ユーザー満足度 | 70% | 82% | +12% |
| 1回目で満足 | 40% | 65% | +25% |
| プロンプト長 | 50 tokens | 120 tokens | +140% |

## 最適化戦略

### 詳細記述プロンプト

**改善前**:
```
A person walking in a city
```

**改善後（詳細記述）**:
```
A young woman in her 20s, wearing a red coat and black jeans, walking confidently down a bustling Tokyo street at night. Neon signs illuminate the rain-soaked pavement. Camera slowly pans following her movement. Cinematic lighting with bokeh effect. 4 seconds duration.

具体的要素:
- 人物: young woman, 20s, red coat, black jeans
- 動作: walking confidently
- 場所: Tokyo street, night, bustling
- 天候: rain-soaked pavement
- 照明: neon signs, cinematic lighting, bokeh
- カメラ: slowly pans, following movement
- 時間: 4 seconds
```

## 成功要因

1. **詳細記述**: 成功率+10%
2. **1回目満足率+25%**: 再生成コスト削減
3. **プロンプト長+140%**: 詳細ほど品質向上

## 教訓

- **動画生成は詳細記述必須**: 画像生成以上に詳細が重要
- **カメラワーク指定**: 動画特有の要素
- **時間指定**: 4秒等の具体的時間指定

## 参照

- **出典**: Runway ML Gen-2 Documentation (2024)
