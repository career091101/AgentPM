---
name: generate-kpi-dashboard
description: |
  全KPI（Financial/Customer/Product/Growth）を統合管理するダッシュボードを自動生成。MRR、CAC、LTV、Churn、成長率、NPS等を一元表示し、投資家レポート・取締役会資料に即座に活用できます。

  使用タイミング：
  - 月次/週次レビュー時
  - 投資家レポート作成時
  - 取締役会準備時
  - Phase2-4（PMF検証〜スケール）

  所要時間：20-30分（初回設定含む）
  出力：kpi_dashboard.md（Markdown/PDF/PNG対応）
trigger_keywords:
  - "KPIダッシュボード"
  - "経営指標"
  - "投資家レポート"
  - "メトリクス統合"
  - "ダッシュボード生成"
stage: Phase2-4（PMF検証-スケール）
dependencies:
  - validate-pmf
  - measure-aarrr
  - monitor-burn-rate
  - validate-unit-economics
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/kpi_dashboard.md
execution_time: 20-30分
framework_reference: Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/
priority: P0
framework_compliance: 100%
---

# KPI Dashboard Generator Skill

全KPI（Financial/Customer/Product/Growth）を統合管理するダッシュボード生成Skill。

---

## このSkillでできること

1. **KPI統合**: Financial/Customer/Product/Growthの15-20指標を統合
2. **Top 5 KPI自動選定**: ビジネスステージに応じた重要指標を自動選定
3. **トレンドグラフ生成**: 6ヶ月間の推移を可視化
4. **アラート自動発行**: 閾値超過時に警告を表示
5. **業界ベンチマーク比較**: SaaS/E-commerce等の業界標準と比較
6. **投資家レポート形式エクスポート**: PDF/PNG形式で即座に共有可能
7. **自動更新設定**: 週次/月次の定期更新

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 各KPI測定結果（PMF検証、AARRR、ユニットエコノミクス等） |
| **出力** | `Flow/{YYYYMM}/{YYYY-MM-DD}/kpi_dashboard.md` |
| **次のSkill** | 投資家レポート作成、取締役会資料作成 |

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 20-30分

### 自動実行ステップ

1. **KPI統合**: 全成果物から15-20指標を自動収集
2. **Top 5 KPI選定**: ステージ別重要指標を自動選定
3. **トレンドグラフ生成**: 6ヶ月分の時系列データを可視化
4. **アラート設定**: 閾値超過時の警告を自動生成
5. **業界ベンチマーク比較**: 標準値との差分を算出
6. **エグゼクティブサマリー生成**: 経営判断のための要約作成
7. **投資家レポート形式エクスポート**: PDF/PNG形式でエクスポート
8. **自動更新設定**: 週次/月次の更新スケジュール設定
9. **成果物出力**: `kpi_dashboard.md`を生成

---

## KPI統合カテゴリ

### 1. Financial KPI（財務）

| KPI | 説明 | 目標値 | データソース |
|-----|------|--------|------------|
| **MRR** | 月次経常収益 | 10%/月成長 | validate-pmf |
| **Burn Rate** | 月次資金消費額 | -$50K以下 | monitor-burn-rate |
| **Runway** | 資金残存期間 | 18ヶ月以上 | monitor-burn-rate |
| **LTV/CAC Ratio** | 顧客生涯価値 / 獲得コスト | 3:1以上 | validate-unit-economics |
| **Gross Margin** | 粗利率 | 70%以上（SaaS） | validate-unit-economics |

### 2. Customer KPI（顧客）

| KPI | 説明 | 目標値 | データソース |
|-----|------|--------|------------|
| **CAC** | 顧客獲得コスト | $100以下（B2C） | validate-unit-economics |
| **LTV** | 顧客生涯価値 | $300以上（B2C） | validate-unit-economics |
| **Churn Rate** | 解約率 | 5%/月以下 | validate-pmf |
| **NPS** | 顧客推奨度 | 30-40（SaaS平均） | validate-pmf |
| **Retention Rate** | 継続率 | 95%/月以上 | measure-aarrr |

### 3. Product KPI（プロダクト）

| KPI | 説明 | 目標値 | データソース |
|-----|------|--------|------------|
| **MAU** | 月間アクティブユーザー | 10%/月成長 | validate-pmf |
| **DAU/MAU** | デイリー/マンスリー比率 | 20%以上 | measure-aarrr |
| **Feature Adoption** | 主要機能採用率 | 60%以上 | measure-aarrr |
| **Time to Value** | 初回価値体験までの時間 | 5分以内 | measure-aarrr |
| **WAU** | 週間アクティブユーザー | - | measure-aarrr |

### 4. Growth KPI（成長）

| KPI | 説明 | 目標値 | データソース |
|-----|------|--------|------------|
| **Monthly Growth Rate** | 月次成長率 | 10%/月以上 | validate-pmf |
| **Sean Ellis Test** | PMF指標（非常に残念%） | 40%以上 | validate-pmf |
| **Viral Coefficient** | バイラル係数 | 1.0以上 | measure-aarrr |
| **Activation Rate** | アクティベーション率 | 25%以上 | measure-aarrr |
| **Referral Rate** | 紹介率 | 15%以上 | measure-aarrr |

---

## ステージ別Top 5 KPI自動選定ロジック

### Phase 2（PMF検証）

1. **Sean Ellis Test**: PMF達成の必須指標（40%以上）
2. **Monthly Growth Rate**: 成長トレンド（10%/月以上）
3. **Churn Rate**: 継続率（5%/月以下）
4. **NPS**: 顧客満足度（30以上）
5. **Burn Rate**: 資金管理（18ヶ月以上のランウェイ）

### Phase 3（初期スケール）

1. **MRR**: 月次収益成長（10%/月以上）
2. **LTV/CAC Ratio**: ユニットエコノミクス（3:1以上）
3. **Monthly Growth Rate**: 成長持続性（10%/月以上）
4. **Activation Rate**: ファネル効率（AARRR）
5. **Runway**: 資金余力（18ヶ月以上）

### Phase 4（スケール）

1. **MRR**: 月次収益（$100K以上）
2. **LTV/CAC Ratio**: 収益性（3:1以上）
3. **Gross Margin**: 粗利率（70%以上）
4. **Viral Coefficient**: 自然成長（1.0以上）
5. **Retention Rate**: 継続率（95%/月以上）

---

## トレンドグラフ仕様

### グラフタイプ

1. **折れ線グラフ**: 時系列推移（MRR、MAU、Churn Rate等）
2. **棒グラフ**: 月次比較（CAC、LTV等）
3. **ドーナツグラフ**: 割合表示（Churn Rate、NPS分布）
4. **ゲージチャート**: 目標達成度（Sean Ellis Test等）

### データ期間

- **デフォルト**: 直近6ヶ月
- **オプション**: 3ヶ月/12ヶ月
- **比較**: 前期比・前年比

### Markdown埋め込み

```markdown
## MRR推移（直近6ヶ月）

| 月 | MRR | 前月比 | 成長率 |
|----|-----|--------|--------|
| 2025-07 | $10,000 | - | - |
| 2025-08 | $11,200 | +$1,200 | +12% |
| 2025-09 | $12,500 | +$1,300 | +11.6% |
| 2025-10 | $14,000 | +$1,500 | +12% |
| 2025-11 | $15,500 | +$1,500 | +10.7% |
| 2025-12 | $17,200 | +$1,700 | +11% |

**トレンド**: 📈 健全な成長（平均11.5%/月）
**目標達成度**: ✅ 目標（10%/月）を達成
```

---

## アラート設定

### 🔴 Critical（緊急対応必要）

| KPI | 閾値 | アラート内容 |
|-----|------|------------|
| **Runway** | < 12ヶ月 | 資金調達を即座に開始 |
| **Churn Rate** | > 10%/月 | プロダクト改善が急務 |
| **LTV/CAC Ratio** | < 1:1 | ビジネスモデル見直し |
| **Monthly Growth Rate** | < 0% | Pivot検討 |

### 🟡 Warning（要監視）

| KPI | 閾値 | アラート内容 |
|-----|------|------------|
| **Runway** | < 18ヶ月 | 資金調達計画を開始 |
| **Churn Rate** | 5-10%/月 | 継続率改善施策を実施 |
| **LTV/CAC Ratio** | 1-3:1 | 獲得コスト最適化 |
| **Monthly Growth Rate** | 0-5%/月 | 成長施策の強化 |

### 🟢 Healthy（健全）

| KPI | 閾値 | 状態 |
|-----|------|------|
| **Runway** | ≥ 18ヶ月 | 安全圏 |
| **Churn Rate** | ≤ 5%/月 | PMF達成レベル |
| **LTV/CAC Ratio** | ≥ 3:1 | ユニットエコノミクス健全 |
| **Monthly Growth Rate** | ≥ 10%/月 | スケール可能 |

---

## 業界ベンチマーク比較

### SaaS業界標準（B2B）

| KPI | 業界平均 | Top 25% | Top 10% |
|-----|---------|---------|---------|
| **LTV/CAC Ratio** | 3:1 | 5:1 | 7:1 |
| **Churn Rate** | 5%/月 | 3%/月 | 2%/月 |
| **NPS** | 30 | 50 | 70 |
| **Gross Margin** | 70% | 80% | 85% |
| **CAC Payback** | 12ヶ月 | 6ヶ月 | 3ヶ月 |

### E-commerce業界標準（B2C）

| KPI | 業界平均 | Top 25% | Top 10% |
|-----|---------|---------|---------|
| **LTV/CAC Ratio** | 3:1 | 4:1 | 5:1 |
| **Retention Rate** | 30% | 50% | 70% |
| **AOV** | $50 | $75 | $100 |
| **Conversion Rate** | 2% | 3.5% | 5% |
| **Repeat Purchase Rate** | 20% | 35% | 50% |

### 比較表示例

```markdown
## LTV/CAC Ratio - 業界比較

| 指標 | 自社 | 業界平均 | Top 25% | 評価 |
|-----|------|---------|---------|------|
| **LTV/CAC** | 4.2:1 | 3:1 | 5:1 | 🟢 業界平均以上、Top 25%未達 |

**インサイト**: LTV/CACは健全だが、Top 25%（5:1）達成にはCAC削減またはLTV向上が必要。チャネル最適化を推奨。
```

---

## エグゼクティブサマリー生成

### テンプレート構造

```markdown
# KPIダッシュボード - エグゼクティブサマリー

**作成日**: {YYYY-MM-DD}
**対象期間**: {YYYY-MM} - {YYYY-MM}（6ヶ月）
**ビジネスステージ**: Phase {X}（{ステージ名}）

---

## 🎯 総合評価: {健全/要改善/要見直し}

**総合スコア**: {X}/100点

- ✅ 健全: 80-100点 → スケール継続
- ⚠️ 要改善: 50-79点 → 改善施策実施
- ❌ 要見直し: 0-49点 → Pivot検討

---

## 📊 Top 5 KPI

1. **{KPI名}**: {値} ({目標} 比 {+X%/-X%})
   - 📈 トレンド: {上昇/横ばい/下降}
   - 🎯 評価: {✅達成/⚠️要改善/❌未達}

2. ...

---

## 🚨 Critical Alerts（緊急対応必要）

1. **{KPI名}**: {現状値} → 閾値{閾値}を超過
   - **リスク**: {リスク内容}
   - **推奨アクション**: {アクション}

---

## 💡 Key Insights

1. **成長トレンド**: {インサイト}
2. **顧客行動**: {インサイト}
3. **財務健全性**: {インサイト}

---

## 📋 推奨アクション（優先順位順）

1. **{アクション名}**: {理由}（実施期限: {YYYY-MM-DD}）
2. ...

---

## 📈 次回レビュー予定

- **定期レビュー**: 週次/月次
- **次回アップデート**: {YYYY-MM-DD}
```

---

## 投資家レポート形式

### PDF/PNG エクスポート仕様

**フォーマット**:
- **A4サイズ**: 210mm × 297mm
- **レイアウト**: 1ページ目（サマリー）、2ページ目（詳細グラフ）
- **カラースキーム**: プロフェッショナル（青/緑/赤）

**エクスポートコマンド**:
```bash
# Markdownをベースに生成
pandoc kpi_dashboard.md -o kpi_dashboard.pdf --pdf-engine=xelatex

# または画像エクスポート
# （グラフ部分のみPNG形式）
```

### 投資家レポート専用テンプレート

```markdown
# {Company Name} - Investor KPI Report

**Report Date**: {YYYY-MM-DD}
**Reporting Period**: {Q1/Q2/Q3/Q4} {YYYY}
**Prepared by**: {Name}

---

## Executive Summary

{会社の現状を3-5行で要約}

---

## Key Metrics

| Category | Metric | Current | Target | Status |
|----------|--------|---------|--------|--------|
| **Growth** | MRR | ${X}K | ${Y}K | {🟢/🟡/🔴} |
| **Efficiency** | LTV/CAC | {X}:{Y} | 3:1 | {🟢/🟡/🔴} |
| **Health** | Churn Rate | {X}% | <5% | {🟢/🟡/🔴} |

---

## Financial Highlights

- **MRR Growth**: {X}% MoM
- **Runway**: {X} months
- **Burn Rate**: ${X}K/month

---

## Customer Highlights

- **New Customers**: {X} ({+Y%} MoM)
- **Total Customers**: {X}
- **NPS**: {X}

---

## Product Highlights

- **MAU**: {X}K ({+Y%} MoM)
- **DAU/MAU**: {X}%
- **Feature Adoption**: {X}%

---

## Outlook & Next Steps

1. {次の四半期の重点施策}
2. ...

---

**Contact**: {email}
**Next Report**: {YYYY-MM-DD}
```

---

## 自動更新設定

### 週次更新

```yaml
schedule:
  frequency: weekly
  day: Monday
  time: 09:00
  actions:
    - collect_kpi_data
    - generate_dashboard
    - send_email_notification
```

### 月次更新

```yaml
schedule:
  frequency: monthly
  day: 1
  time: 09:00
  actions:
    - collect_kpi_data
    - generate_dashboard
    - generate_investor_report
    - archive_previous_report
```

---

## Knowledge Base参照

- AARRRフレームワーク: `@startup_science/02_frameworks/aarrr/aarrr_overview.md`
- ユニットエコノミクス: `@startup_science/02_frameworks/unit_economics/unit_economics_overview.md`
- PMF検証: `@startup_science/01_stages/pmf/pmf_overview.md`
- 業界ベンチマーク: `@startup_science/03_benchmarks/saas_benchmarks.md`

---

## 成功基準

- ✅ 全KPI統合（15-20指標）
- ✅ Top 5 KPI自動選定
- ✅ トレンドグラフ生成（6ヶ月）
- ✅ アラート自動発行（Critical/Warning）
- ✅ 業界ベンチマーク比較完了
- ✅ エグゼクティブサマリー生成
- ✅ 投資家レポート形式エクスポート（PDF/PNG）
- ✅ 自動更新設定（週次/月次）

---

## 注意事項

1. **データ精度**: 各KPI測定Skillの実行が前提（validate-pmf、measure-aarrr等）
2. **ベンチマーク更新**: 業界標準値は年次で見直し
3. **プライバシー**: 投資家レポートは機密情報として管理
4. **カスタマイズ**: 業界・ビジネスモデルに応じてKPI項目を調整可能

---

## 参考リンク

- [SaaS Metrics 2.0](https://www.forentrepreneurs.com/saas-metrics-2/) - David Skok
- [Startup Metrics for Pirates](https://www.slideshare.net/dmc500hats/startup-metrics-for-pirates-long-version) - Dave McClure
- [The Only Metric That Matters](https://www.startup-marketing.com/the-startup-pyramid/) - Sean Ellis

---

**作成日**: 2025-12-31
**バージョン**: v1.0
**メンテナ**: Claude Sonnet 4.5
