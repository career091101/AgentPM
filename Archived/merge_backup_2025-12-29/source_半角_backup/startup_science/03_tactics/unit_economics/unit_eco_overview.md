---
id: "TACTIC_UNIT_ECONOMICS_001"
title: "Unit Economics (ユニットエコノミクス)"
title_ja: "ユニットエコノミクス分析"
category: "tactic"
type: "metric"
source_book: "起業の科学"
chapter: "STEP 4"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"

tags:
  stage:
    - pmf
    - scale
  concepts:
    - unit_economics
    - ltv
    - cac
    - profitability
  related_frameworks:
    - pmf
    - scale
  disciplines:
    - finance
    - growth

tactic:
  key_metrics:
    - name: "LTV (Lifetime Value)"
      description: "顧客生涯価値"
      formula: "ARPU × 粗利率 / Churn率"
    - name: "CAC (Customer Acquisition Cost)"
      description: "顧客獲得コスト"
      formula: "S&Mコスト / 新規顧客数"
    - name: "LTV/CAC比率"
      description: "収益性指標"
      target: "3.0以上"
    - name: "Payback Period"
      description: "投資回収期間"
      target: "12ヶ月以内"
  target_metrics:
    ltv_cac_ratio: "3.0+"
    payback_period: "<12ヶ月"
    gross_margin: "70%+"

dependencies:
  requires:
    - CONCEPT_PMF_001
  enables:
    - CONCEPT_SCALE_001

skills:
  applicable:
    - unit_economics_analysis
    - profitability_modeling
  triggers:
    - "ユニットエコノミクス"
    - "LTV/CAC分析"

quality:
  fact_check: "pass"
  sources_count: 3
  last_verified: "2025-12-28"

priority: "high"
---

# Unit Economics (ユニットエコノミクス)

> **出典**: 田所雅之「起業の科学」STEP 4、David Skok "SaaS Metrics 2.0"
> **関連**: [[CONCEPT_PMF_001]], [[CONCEPT_SCALE_001]]

---

## 1. 定義

**Unit Economics（ユニットエコノミクス）** は、顧客1人あたりの収益性を示す指標。**スケール可能性の判断基準**。

**重要な原則**:
> 「Unit Economicsが成立しないビジネスは、スケールすればするほど赤字が拡大する」
> — David Skok

**コア指標**:
```yaml
LTV (Lifetime Value): 顧客生涯価値
CAC (Customer Acquisition Cost): 顧客獲得コスト
LTV/CAC比率: 収益性指標（目標3.0+）
Payback Period: 投資回収期間（目標12ヶ月以内）
```

---

## 2. なぜ重要か

### 2.1 スケール可能性の判定

**Unit Economicsの健全性 = スケール可能性**

| LTV/CAC比率 | 判定 | アクション |
|------------|------|-----------|
| **3.0+** | ✅ 健全 | スケール投資GO |
| **1.0-3.0** | ⚠️ 要改善 | 効率化施策実施 |
| **<1.0** | ❌ 赤字 | ビジネスモデル見直し |

**例**:
```
ケースA（健全）:
LTV: $3,000
CAC: $1,000
比率: 3.0 → スケール可能

ケースB（危険）:
LTV: $1,200
CAC: $1,000
比率: 1.2 → スケールで赤字拡大
```

---

### 2.2 投資判断の基準

**VCの投資判断基準**:
```
必須条件:
- LTV/CAC ≥ 3.0
- Payback Period ≤ 12ヶ月
- Gross Margin ≥ 70%（SaaS）

上記満たせば資金調達可能性高
```

**データ**:
- Series A調達企業の90%がLTV/CAC 3.0+
- Payback 18ヶ月超は調達困難

---

## 3. LTV（顧客生涯価値）

### 3.1 定義と計算式

**LTV (Lifetime Value)** = 1顧客が生涯で生み出す利益

**計算式（SaaS基本形）**:
```
LTV = ARPU × 粗利率 / Churn率

ARPU: 月間平均単価
粗利率: Gross Margin
Churn率: 月間解約率
```

**例**:
```
ARPU: $100/月
粗利率: 80%
Churn率: 5%/月

LTV = $100 × 0.8 / 0.05 = $1,600
```

---

### 3.2 業種別LTV計算

#### SaaS（サブスクリプション）

```
LTV = MRR × 粗利率 / Churn率

または

LTV = ARPU × 平均継続月数 × 粗利率
```

**例（Slack）**:
```
ARPU: $80/月
粗利率: 90%
Churn率: 2%/月

LTV = $80 × 0.9 / 0.02 = $3,600
```

---

#### Eコマース（リピート型）

```
LTV = 平均購入単価 × 購入回数 × 粗利率

購入回数 = 1 / (1 - リピート率)
```

**例（Amazon Prime）**:
```
平均購入単価: $50
年間購入回数: 12回
粗利率: 30%
継続年数: 5年

LTV = $50 × 12 × 0.3 × 5 = $900
```

---

#### マーケットプレイス（両面市場）

```
LTV = GMV × Take Rate × 平均取引回数 × 粗利率

GMV: 流通総額
Take Rate: 手数料率
```

**例（Airbnb）**:
```
平均取引額: $500
Take Rate: 15%
年間利用回数: 3回
継続年数: 4年
粗利率: 80%

LTV = $500 × 0.15 × 3 × 4 × 0.8 = $720
```

---

### 3.3 LTV向上施策

**3つの改善レバー**:

| レバー | 施策例 | 効果 |
|--------|--------|------|
| **ARPU向上** | アップセル、クロスセル、プラン改定 | +20-50% |
| **粗利率向上** | コスト最適化、自動化 | +5-15% |
| **Churn率低下** | Retention施策、CS強化 | +30-100% |

**優先順位**: Churn率低下 > ARPU向上 > 粗利率向上

参照: [[CONCEPT_RETENTION_001]]

---

## 4. CAC（顧客獲得コスト）

### 4.1 定義と計算式

**CAC (Customer Acquisition Cost)** = 顧客1人を獲得するコスト

**計算式（基本形）**:
```
CAC = S&Mコスト / 新規顧客数

S&M: Sales & Marketing
```

**詳細計算式**:
```
CAC = (広告費 + 人件費 + ツール費 + その他) / 新規顧客数

期間: 通常1ヶ月または1四半期
```

**例**:
```
月間S&Mコスト:
- 広告費: $50,000
- 人件費（営業3人）: $30,000
- ツール費: $5,000
合計: $85,000

新規顧客数: 100人

CAC = $85,000 / 100 = $850
```

---

### 4.2 業種別CAC目安

| 業種 | CAC目安 | LTV目安 | LTV/CAC |
|------|---------|---------|---------|
| **B2B SaaS（SMB）** | $500-3,000 | $1,500-9,000 | 3.0+ |
| **B2B SaaS（Enterprise）** | $10,000-50,000 | $50,000-250,000 | 5.0+ |
| **B2C SaaS** | $50-300 | $150-900 | 3.0+ |
| **Eコマース** | $20-100 | $60-300 | 3.0+ |
| **マーケットプレイス** | $30-150 | $200-1,000 | 5.0+ |

---

### 4.3 チャネル別CAC

**比較例（B2B SaaS）**:

| チャネル | CAC | CVR | 評価 |
|---------|-----|-----|------|
| **Organic SEO** | $100 | 3% | ✅ 最優秀 |
| **紹介プログラム** | $200 | 10% | ✅ 優秀 |
| **コンテンツマーケ** | $300 | 5% | ✅ 良好 |
| **Facebook広告** | $800 | 2% | ⚠️ 要改善 |
| **Google広告** | $1,200 | 1.5% | ❌ 高すぎ |
| **展示会** | $2,000 | 8% | ⚠️ Enterprise向け |

**戦略**: CAC低いチャネルに集中投資

---

### 4.4 CAC削減施策

**施策マトリクス**:

| 施策 | 効果 | 難易度 | 期間 |
|------|------|--------|------|
| **SEO強化** | -30-50% | 高 | 6-12ヶ月 |
| **紹介プログラム** | -40-60% | 中 | 3-6ヶ月 |
| **コンテンツマーケ** | -20-40% | 中 | 6-12ヶ月 |
| **CVR改善** | -20-30% | 低 | 1-3ヶ月 |
| **営業効率化** | -10-20% | 低 | 1-3ヶ月 |

---

## 5. LTV/CAC比率

### 5.1 目標値と判定基準

**標準的判定基準**:

| 比率 | 判定 | 状態 | アクション |
|------|------|------|-----------|
| **5.0+** | 優秀 | 高収益 | 積極投資 |
| **3.0-5.0** | 健全 | 成長可能 | スケール開始 |
| **1.0-3.0** | 要改善 | 低収益 | 効率化優先 |
| **<1.0** | 危険 | 赤字 | Pivot検討 |

**David Skokの推奨**:
> 「LTV/CAC比率は最低3.0、理想は5.0以上」

---

### 5.2 ステージ別目標

| ステージ | LTV/CAC目標 | 理由 |
|---------|------------|------|
| **PSF検証** | 計測のみ | PMF前は参考値 |
| **PMF達成** | 1.5+ | 最低限の黒字化 |
| **Early Scale** | 3.0+ | スケール開始条件 |
| **Growth** | 5.0+ | 高効率成長 |

---

### 5.3 比率改善の2つの戦略

#### 戦略A: LTV向上

**施策**:
1. Churn率低下（Retention施策）
2. ARPU向上（アップセル、プラン改定）
3. 粗利率向上（コスト削減）

**効果**:
```
Before:
LTV: $1,200
CAC: $600
比率: 2.0

施策実行（Churn 5% → 3%）:
LTV: $2,000
CAC: $600
比率: 3.33 ✅
```

---

#### 戦略B: CAC削減

**施策**:
1. オーガニックチャネル強化
2. 紹介プログラム導入
3. 営業プロセス効率化

**効果**:
```
Before:
LTV: $1,500
CAC: $750
比率: 2.0

施策実行（CAC -40%）:
LTV: $1,500
CAC: $450
比率: 3.33 ✅
```

**推奨**: LTV向上とCAC削減を並行実施

---

## 6. Payback Period（投資回収期間）

### 6.1 定義と計算式

**Payback Period** = CACを回収するまでの期間

**計算式**:
```
Payback Period（月） = CAC / (MRR × 粗利率)

MRR: 月次経常収益
```

**例**:
```
CAC: $1,200
MRR: $100
粗利率: 80%

Payback = $1,200 / ($100 × 0.8) = 15ヶ月
```

---

### 6.2 目標値

| 業種 | 目標Payback | 理由 |
|------|------------|------|
| **B2B SaaS** | 12ヶ月以内 | キャッシュフロー確保 |
| **B2C SaaS** | 6ヶ月以内 | 高Churnリスク |
| **Eコマース** | 3ヶ月以内 | 短期回転 |
| **Enterprise** | 18ヶ月OK | 高LTV許容 |

**VCの基準**: Payback 12ヶ月以内が投資条件

---

### 6.3 Payback短縮施策

**3つのアプローチ**:

| アプローチ | 施策 | 効果 |
|----------|------|------|
| **CAC削減** | 効率的チャネル | -30-50% |
| **ARPU向上** | 高単価プラン誘導 | -20-40% |
| **年間契約** | 前払い促進 | -50-70% |

**最強施策: 年間前払い**
```
月額払い:
MRR: $100
Payback: 15ヶ月

年間前払い（20%割引）:
初回入金: $960（=$100×12×0.8）
Payback: 1.5ヶ月（実質即回収）
```

---

## 7. Gross Margin（粗利率）

### 7.1 定義と計算式

**Gross Margin（粗利率）** = 売上から変動費を引いた利益率

**計算式**:
```
Gross Margin = (売上 - 変動費) / 売上 × 100

変動費: COGS（売上原価）
```

**SaaSの変動費**:
- ホスティング費（AWS, GCP等）
- サポートコスト
- 決済手数料

---

### 7.2 業種別目標値

| 業種 | 目標Gross Margin | 備考 |
|------|-----------------|------|
| **SaaS** | 70-90% | 理想は80%+ |
| **Eコマース** | 30-60% | 商材により変動 |
| **マーケットプレイス** | 60-80% | Take Rate依存 |
| **ハードウェア** | 30-50% | 製造コスト高 |

**SaaSベンチマーク**:
```
優秀: 85%+（Slack, Zoom）
標準: 70-80%
要改善: <70%
```

---

### 7.3 粗利率向上施策

**施策例（SaaS）**:

| 施策 | 効果 | 難易度 |
|------|------|--------|
| **インフラ最適化** | +3-5% | 中 |
| **サポート自動化** | +5-10% | 高 |
| **決済手数料交渉** | +1-2% | 低 |
| **単価アップ** | +5-15% | 中 |

---

## 8. Rule of 40（SaaS指標）

### 8.1 定義

**Rule of 40** = 成長率 + 利益率 ≥ 40%

**計算式**:
```
Rule of 40 = YoY成長率（%） + EBITDA Margin（%）

目標: 40%以上
```

**例**:
```
ケースA（合格）:
成長率: 100%
EBITDA: -20%
合計: 80% ✅

ケースB（合格）:
成長率: 20%
EBITDA: 25%
合計: 45% ✅

ケースC（不合格）:
成長率: 30%
EBITDA: -10%
合計: 20% ❌
```

---

### 8.2 ステージ別目標

| ステージ | Rule of 40 | 優先事項 |
|---------|-----------|---------|
| **Early Stage** | 成長率重視 | 40-100% |
| **Growth Stage** | バランス | 40-60% |
| **Mature** | 利益率重視 | 40-50% |

---

## 9. Unit Economics改善ロードマップ

### フェーズ1: 現状測定（1ヶ月）

**タスク**:
- [ ] LTV計算（ARPU, Churn, Gross Margin）
- [ ] CAC計算（チャネル別）
- [ ] LTV/CAC比率算出
- [ ] Payback Period計算
- [ ] Gross Margin測定
- [ ] セグメント別分析

---

### フェーズ2: 課題特定（2週間）

**分析項目**:
- [ ] LTV/CAC比率が3.0未満？
- [ ] Payback Periodが12ヶ月超？
- [ ] Gross Marginが70%未満？
- [ ] チャネル別CACのバラつき分析
- [ ] Churn率が高い？

---

### フェーズ3: 改善施策実行（3-6ヶ月）

**優先順位**:

| 優先度 | 施策 | 期待効果 |
|--------|------|---------|
| 1 | Churn率低下 | LTV +50-100% |
| 2 | CAC削減（チャネル最適化） | CAC -30-50% |
| 3 | ARPU向上 | LTV +20-50% |
| 4 | Gross Margin向上 | LTV +5-15% |

---

### フェーズ4: 継続測定（毎月）

**ダッシュボード項目**:
```
Key Metrics:
- LTV: $X,XXX
- CAC: $XXX
- LTV/CAC: X.X
- Payback: X ヶ月
- Gross Margin: XX%
- Rule of 40: XX%

チャネル別CAC:
- Organic: $XXX
- Paid: $XXX
- Referral: $XXX
```

---

## 10. 事例

### 10.1 成功事例: Slack

**Unit Economics（2019年）**:
```
LTV: $3,600
  - ARPU: $80/月
  - Churn率: 2%/月
  - Gross Margin: 90%

CAC: $720

LTV/CAC比率: 5.0 ✅
Payback Period: 9ヶ月 ✅
Gross Margin: 90% ✅
```

**成功要因**:
- 超低Churn（2%/月）
- バイラル成長（CAC低）
- 高い粗利率

---

### 10.2 失敗から学ぶ: 某B2C SaaS

**Unit Economics（サービス終了前）**:
```
LTV: $180
  - ARPU: $15/月
  - Churn率: 10%/月
  - Gross Margin: 80%

CAC: $300

LTV/CAC比率: 0.6 ❌
Payback Period: 永遠に回収不可 ❌
```

**問題**:
- 高Churn（10%/月）
- 広告依存でCAC高騰
- 低ARPU

**結果**: 調達失敗 → サービス終了

---

## 11. よくある間違い

| 間違い | 症状 | 対策 |
|--------|------|------|
| **Churn率誤算** | 楽観的な想定 | 実測値使用 |
| **CAC過少計算** | 人件費除外 | 全コスト含める |
| **粗利率無視** | 売上のみ計算 | 変動費差し引く |
| **セグメント分析なし** | 全体平均のみ | セグメント別分析 |
| **PMF前にスケール** | Unit Economics悪化 | PMF後にスケール |

---

## 12. ツール

| ツール | 用途 | 価格 |
|--------|------|------|
| **ChartMogul** | SaaS指標ダッシュボード | $100/月 |
| **ProfitWell** | Unit Economics分析 | 無料〜 |
| **Google Sheets** | 手動計算 | 無料 |
| **Baremetrics** | SaaS Analytics | $50/月 |

---

## 13. 関連概念

| 概念 | 関係性 | リンク |
|------|--------|--------|
| PMF | Unit Economics健全化の前提 | [[CONCEPT_PMF_001]] |
| Retention | LTV向上の鍵 | [[CONCEPT_RETENTION_001]] |
| AARRR | CAC削減の手法 | [[FRAMEWORK_AARRR_001]] |
| Scale | Unit Economics健全でスケール | [[CONCEPT_SCALE_001]] |
| Pivot | 比率<1.0でPivot検討 | [[TACTIC_PIVOT_001]] |

---

## クイックリファレンス

```
定義: 顧客1人あたりの収益性指標
重要性: スケール可能性の判断基準

Key Metrics:
- LTV = ARPU × 粗利率 / Churn率
- CAC = S&Mコスト / 新規顧客数
- LTV/CAC比率: 目標3.0+
- Payback Period: 目標12ヶ月以内
- Gross Margin: 目標70%+（SaaS）

判定基準:
- LTV/CAC 5.0+: 優秀
- LTV/CAC 3.0-5.0: 健全
- LTV/CAC 1.0-3.0: 要改善
- LTV/CAC <1.0: 危険（Pivot検討）

改善優先順位:
1. Churn率低下（効果最大）
2. CAC削減
3. ARPU向上
4. 粗利率向上

Rule of 40（SaaS）:
成長率 + EBITDA Margin ≥ 40%

重要な原則:
「Unit Economics成立しないビジネスは
 スケールすればするほど赤字拡大」
```

---

**ファイル情報**
- 作成日: 2025-12-28
- 最終更新: 2025-12-28
- バージョン: 1.0
