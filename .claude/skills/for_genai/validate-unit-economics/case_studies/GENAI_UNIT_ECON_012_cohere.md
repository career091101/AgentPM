---
id: GENAI_UNIT_ECON_012
title: "Cohere - LTV/CAC 80:1、Enterprise API特化"
product: Cohere
company: Cohere
period: "2023-01 to 2024-12"
tags: ["Unit Economics", "Cohere", "LTV/CAC", "Enterprise API"]
tier: 2
---

# Cohere - LTV/CAC 80:1、Enterprise API特化

## Unit Economics指標サマリー

| 指標 | 実績 | ForGenAI基準 | 判定 |
|------|------|-------------|:----:|
| LTV/CAC | 80:1 | 5.0以上 | ✅ ✅ ✅ |
| CAC回収期間 | 6ヶ月 | 12ヶ月以内 | ✅ ✅ ✅ |
| Gross Margin | 82% | 70%以上（API課金80%+） | ✅ ✅ |
| 月次成長率 | 24% | 20%以上 | ✅ ✅ |

## 詳細分析

### LTV計算
```
ARPU: $200/月（Enterprise API平均）
平均継続月数: 18ヶ月（Enterprise長期契約）
Gross Margin: 82%（API課金モデル）

LTV = $200 × 18 × 0.82 = $2,952
Churn率計算: $200 × 0.82 / 0.056 = $2,929
```

### CAC内訳

| チャネル | 獲得数 | 構成比 | CAC |
|---------|--------|-------|-----|
| Enterprise営業 | 1.2K | 60% | $50 |
| パートナーチャネル | 500 | 25% | $25 |
| カンファレンス | 200 | 10% | $80 |
| コンテンツマーケ | 100 | 5% | $15 |

**平均CAC**: $36.5（Enterprise営業主体）

### AI固有コスト

| コスト項目 | 月次コスト/ユーザー | 割合 |
|----------|------------------|------|
| GPU時間課金（独自モデル） | $28 | 14% |
| モデルホスティング | $6 | 3% |
| ファインチューニング | $2 | 1% |
| **合計** | **$36** | **18%** |

**Gross Margin計算**:
```
Gross Margin = ($200 - $36) / $200 = 82%
```

**注**: CohereはEnterprise API課金モデルで、高ARPU $200/月。Gross Margin 82%（API課金モデル目標80%+クリア）。

### 成長予測

**現状**（2024年末）:
- Enterprise有料ユーザー数: 2K社
- MRR: $400K
- ARR: $4.8M

**2025年末予測**（月次成長率24%継続）:
- Enterprise有料ユーザー数: 16K社
- MRR: $3.2M
- ARR: $38.4M

**ARRゴール到達時期**:
- $20M ARR: 2025年7月（予測）
- 根拠: 月次成長率24%継続で7ヶ月後に4.2倍成長

## 教訓

### 成功要因
1. **Enterprise API特化**: 高ARPU $200/月、長期契約18ヶ月
2. **API課金モデル**: Gross Margin 82%、従量課金で顧客価値に連動
3. **独自モデル**: Cohere独自モデル、OpenAI API依存脱却
4. **LTV/CAC 80:1**: VC調達基準5.0以上を大幅超過

### ForGenAI製品への教訓
1. **Enterprise特化戦略**: 高ARPU、長期契約、LTV最大化
2. **API課金モデル**: Gross Margin 80%+、従量課金設計
3. **独自モデル投資**: Gross Margin向上、長期的な優位性
4. **パートナーチャネル**: CAC削減、Enterprise市場開拓

### 再現性の検討
- **Enterprise特化戦略**: 再現可能（高ARPU、長期契約）
- **API課金モデル**: 再現可能（従量課金設計）
- **独自モデル投資**: 再現困難（技術投資大、開発期間長い）
- **パートナーチャネル**: 再現可能（Enterprise市場開拓）

**現実的な目標**: LTV/CAC 60:1、CAC $30-40、ARPU $150-200/月、Gross Margin 80%
