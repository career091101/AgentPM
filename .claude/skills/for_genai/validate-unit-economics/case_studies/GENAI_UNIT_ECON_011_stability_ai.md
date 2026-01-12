---
id: GENAI_UNIT_ECON_011
title: "Stability AI - LTV/CAC 65:1、Stable Diffusion + Enterprise"
product: Stability AI
company: Stability AI
period: "2023-01 to 2024-12"
tags: ["Unit Economics", "Stability AI", "LTV/CAC", "Stable Diffusion", "Enterprise"]
tier: 2
---

# Stability AI - LTV/CAC 65:1、Stable Diffusion + Enterprise

## Unit Economics指標サマリー

| 指標 | 実績 | ForGenAI基準 | 判定 |
|------|------|-------------|:----:|
| LTV/CAC | 65:1 | 5.0以上 | ✅ ✅ ✅ |
| CAC回収期間 | 9ヶ月 | 12ヶ月以内 | ✅ ✅ |
| Gross Margin | 75% | 70%以上（API課金80%+） | ✅ |
| 月次成長率 | 20% | 20%以上 | ✅ |

## 詳細分析

### LTV計算
```
ARPU: $50/月（API + Enterprise混在）
平均継続月数: 10ヶ月
Gross Margin: 75%（API課金 + Enterprise）

LTV = $50 × 10 × 0.75 = $375
Churn率計算: $50 × 0.75 / 0.10 = $375
```

### CAC内訳

| チャネル | 獲得数 | 構成比 | CAC |
|---------|--------|-------|-----|
| オープンソース（Stable Diffusion） | 15K | 50% | $0 |
| GitHub統合 | 7.5K | 25% | $2 |
| カンファレンス・イベント | 4.5K | 15% | $15 |
| Enterprise営業 | 3K | 10% | $20 |

**平均CAC**: $5.75（オープンソース主体）

### AI固有コスト

| コスト項目 | 月次コスト/ユーザー | 割合 |
|----------|------------------|------|
| GPU時間課金（Stable Diffusion） | $10.5 | 21% |
| モデルホスティング | $1.5 | 3% |
| ファインチューニング | $0.5 | 1% |
| **合計** | **$12.5** | **25%** |

**Gross Margin計算**:
```
Gross Margin = ($50 - $12.5) / $50 = 75%
```

**注**: Stability AIはAPI課金 + Enterpriseの混合モデル。Gross Margin 75%（API課金モデル目標80%にやや届かず）。

### 成長予測

**現状**（2024年末）:
- 有料ユーザー数: 30K人
- MRR: $1.5M
- ARR: $18M

**2025年末予測**（月次成長率20%継続）:
- 有料ユーザー数: 180K人
- MRR: $9M
- ARR: $108M

**ARRゴール到達時期**:
- $50M ARR: 2025年7月（予測）
- 根拠: 月次成長率20%継続で7ヶ月後に2.8倍成長

## 教訓

### 成功要因
1. **オープンソース戦略**: Stable Diffusion無料版、CAC $0
2. **API + Enterprise混合**: ARPU $50/月、多様な収益源
3. **画像生成特化**: 垂直特化、ポジショニング明確
4. **LTV/CAC 65:1**: VC調達基準5.0以上を大幅超過

### ForGenAI製品への教訓
1. **オープンソース戦略**: 無料版で体験→API/Enterprise転換
2. **混合収益モデル**: API課金 + Enterprise、ARPU最大化
3. **垂直特化**: 画像生成特化、ポジショニング明確
4. **Gross Margin最適化**: 独自GPU効率化、75-80%目指す

### 再現性の検討
- **オープンソース戦略**: 再現可能（無料版→API/Enterprise転換）
- **混合収益モデル**: 再現可能（API課金 + Enterprise）
- **垂直特化**: 再現可能（特定領域に特化）
- **Gross Margin最適化**: 再現可能（GPU効率化、独自最適化）

**現実的な目標**: LTV/CAC 50:1、CAC $5-10、Gross Margin 75%、月次成長率20%
