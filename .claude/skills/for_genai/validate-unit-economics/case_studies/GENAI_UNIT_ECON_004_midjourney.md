---
id: GENAI_UNIT_ECON_004
title: "Midjourney - LTV/CAC 75:1、Discord中心戦略"
product: Midjourney
company: Midjourney Inc.
period: "2023-01 to 2024-12"
tags: ["Unit Economics", "Midjourney", "LTV/CAC", "Discord"]
tier: 2
---

# Midjourney - LTV/CAC 75:1、Discord中心戦略

## Unit Economics指標サマリー

| 指標 | 実績 | ForGenAI基準 | 判定 |
|------|------|-------------|:----:|
| LTV/CAC | 75:1 | 5.0以上 | ✅ ✅ ✅ |
| CAC回収期間 | 4ヶ月 | 12ヶ月以内 | ✅ ✅ |
| Gross Margin | 85% | 70%以上 | ✅ ✅ |
| 月次成長率 | 22% | 20%以上 | ✅ |

## 詳細分析

### LTV計算
```
ARPU: $30/月（Standard Plan）
平均継続月数: 10ヶ月
Gross Margin: 85%（自社GPU、Stable Diffusionカスタマイズ）

LTV = $30 × 10 × 0.85 = $255
Churn率計算: $30 × 0.85 / 0.10 = $255
```

### CAC内訳

| チャネル | 獲得数 | 構成比 | CAC |
|---------|--------|-------|-----|
| Discord招待 | 150K | 50% | $1.5 |
| 口コミ・SNS | 100K | 33% | $0 |
| メディア露出 | 40K | 13% | $8 |
| X/Twitter広告 | 10K | 3% | $15 |

**平均CAC**: $2-4（Discord招待主体）

### AI固有コスト

| コスト項目 | 月次コスト/ユーザー | 割合 |
|----------|------------------|------|
| GPU推論（自社GPU） | $4.0 | 13.3% |
| Stable Diffusionカスタマイズ | $0.3 | 1.0% |
| ファインチューニング | $0.2 | 0.7% |
| **合計** | **$4.5** | **15%** |

**Gross Margin計算**:
```
Gross Margin = ($30 - $4.5) / $30 = 85%
```

**注**: Midjourneyは自社GPUを使用しており、外部API課金なし。Stable Diffusionをカスタマイズ、Gross Margin高い。

### 成長予測

**現状**（2024年末）:
- Standard Plan有料ユーザー数: 15.6K人
- MRR: $468K
- ARR: $5.6M

**2025年末予測**（月次成長率22%継続）:
- Standard Plan有料ユーザー数: 126K人
- MRR: $3.8M
- ARR: $45.6M

**ARRゴール到達時期**:
- $20M ARR: 2025年6月（予測）
- 根拠: 月次成長率22%継続で6ヶ月後に3倍成長

## 教訓

### 成功要因
1. **Discord中心戦略**: CAC $2-4、コミュニティドリブン成長
2. **プロンプト共有文化65%**: 全GenAI製品中最高、学習コスト低減
3. **自社GPU**: Gross Margin 85%、外部API依存脱却
4. **バイラル成長**: Discord招待、プロンプト共有、SNSシェア

### ForGenAI製品への教訓
1. **Discord中心戦略**: WebUI提供せず、コミュニティドリブン成長
2. **プロンプト共有文化構築**: 学習コスト低減、バイラル成長
3. **自社GPU投資**: Gross Margin 80%+、長期的な優位性
4. **DAU/MAU 0.48**: Discord中心でエンゲージメント高い

### 再現性の検討
- **Discord中心戦略**: 再現可能（コミュニティドリブン成長）
- **プロンプト共有文化**: 再現可能（共有機能、コミュニティ設計）
- **自社GPU投資**: 再現困難（初期投資大、技術ハードル高い）
- **バイラル成長**: 再現可能（Discord招待、プロンプト共有）

**現実的な目標**: LTV/CAC 50:1、CAC $3-5、Gross Margin 75%、月次成長率20%
