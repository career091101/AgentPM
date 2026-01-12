# KPI ダッシュボード生成スキル（Generate KPI Dashboard）

## スキル概要

全KPI（Financial/Customer/Product/Growth）を統合管理するダッシュボードを自動生成します。MRR、CAC、LTV、Churn、成長率、NPSなどの15-20指標を一元表示し、投資家レポート・取締役会資料に即座に活用できます。

### 対象ステージ

- **ステージ**: Phase 2-4（PMF検証～スケール）
- **前提条件**: validate-pmf、measure-aarrr等の各KPI測定スキル実行済み
- **所要時間**: 20-30分（初回設定含む）

### このスキルでできること

1. **KPI統合** - Financial/Customer/Product/Growthの15-20指標を統合管理
2. **Top 5 KPI自動選定** - ビジネスステージに応じた重要指標を自動選定
3. **トレンドグラフ生成** - 6ヶ月間の推移を可視化
4. **アラート自動発行** - 閾値超過時に警告を表示
5. **業界ベンチマーク比較** - SaaS/E-commerce等の業界標準と比較
6. **投資家レポート形式エクスポート** - PDF/PNG形式で即座に共有可能
7. **自動更新設定** - 週次/月次の定期更新を設定

---

## 使用タイミング

| タイミング | 条件 | 次のアクション |
|-----------|------|---------------|
| **月次/週次レビュー時** | KPI測定スキル実行済み | 経営判断の基準に使用 |
| **投資家レポート作成時** | 月末決算後 | レポート出力 |
| **取締役会準備時** | 四半期レビュー | 会議資料として提出 |
| **財務健全性監視時** | 毎月末 | Runway・Burn Rate確認 |

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

## ステージ別Top 5 KPI自動選定

### Phase 2（PMF検証）

優先順位が高い指標（スケール前のPMF達成が必須）：

1. **Sean Ellis Test** - PMF達成の必須指標（40%以上）
2. **Monthly Growth Rate** - 成長トレンド（10%/月以上）
3. **Churn Rate** - 継続率（5%/月以下）
4. **NPS** - 顧客満足度（30以上）
5. **Burn Rate** - 資金管理（18ヶ月以上のランウェイ）

### Phase 3（初期スケール）

スケール開始時の重要指標：

1. **MRR** - 月次収益成長（10%/月以上）
2. **LTV/CAC Ratio** - ユニットエコノミクス（3:1以上）
3. **Monthly Growth Rate** - 成長持続性（10%/月以上）
4. **Activation Rate** - ファネル効率（AARRR）
5. **Runway** - 資金余力（18ヶ月以上）

### Phase 4（スケール）

スケール段階での経営重点指標：

1. **MRR** - 月次収益（$100K以上）
2. **LTV/CAC Ratio** - 収益性（3:1以上）
3. **Gross Margin** - 粗利率（70%以上）
4. **Viral Coefficient** - 自然成長（1.0以上）
5. **Retention Rate** - 継続率（95%/月以上）

---

## アラート設定（自動警告）

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

| KPI | 閾値 |
|-----|------|
| **Runway** | ≥ 18ヶ月 |
| **Churn Rate** | ≤ 5%/月 |
| **LTV/CAC Ratio** | ≥ 3:1 |
| **Monthly Growth Rate** | ≥ 10%/月 |

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

---

## 使用例

### 例1: Phase2（PMF検証）での実行

**実行タイミング**: 初期顧客確保後、月次レビュー

**入力データ**:
```
- Sean Ellis Test: 42%
- Monthly Growth Rate: 11.5%/月
- Churn Rate: 4.2%/月
- NPS: 52
- Burn Rate: ¥1,200,000/月
```

**出力**:
- KPIダッシュボード（全5つのTop指標を可視化）
- エグゼクティブサマリー（スコア: 85/100 - 健全）
- 推奨アクション（スケール準備）

### 例2: Phase4（スケール）での投資家レポート作成

**実行タイミング**: 月末決算後、投資家報告時

**入力データ**:
- 過去6ヶ月のMRR、CAC、LTV等をまとめたデータシート

**出力**:
- KPI投資家レポート（PDF/PNG形式）
- 業界ベンチマーク比較表
- 財務健全性評価

---

## 出力フォーマット

| 項目 | 内容 |
|------|------|
| **出力先** | `Flow/{YYYYMM}/{YYYY-MM-DD}/kpi_dashboard.md` |
| **形式** | Markdown（PDF/PNG エクスポート対応） |
| **所要時間** | 20-30分 |

### 出力内容構成

1. **エグゼクティブサマリー** - 総合評価とTop 5 KPI
2. **トレンドグラフ** - 6ヶ月間の推移（表形式）
3. **業界ベンチマーク比較** - 自社 vs 業界平均
4. **Critical/Warning Alerts** - 警告が必要な指標
5. **推奨アクション** - 優先順位付きアクション項目
6. **投資家レポート形式** - PDF/PNG エクスポート用

---

## 関連スキル

| スキル | 説明 | 関連性 |
|--------|------|--------|
| **validate-pmf** | PMF達成判定 | 前提条件（Sean Ellis等のデータ入力） |
| **measure-aarrr** | 成長ファネル分析 | データソース（Retention、Referral等） |
| **monitor-burn-rate** | バーンレート監視 | データソース（Runway、Burn Rate） |
| **validate-unit-economics** | ユニットエコノミクス検証 | データソース（LTV/CAC、Gross Margin） |

---

## よくある質問（FAQ）

### Q1: どのKPIから入力すればいいですか？

**A**: 順番は自由です。ただしデータソースを確認してください：
- **validate-pmf** の結果から：Sean Ellis、Churn、NPS
- **measure-aarrr** の結果から：DAU/MAU、Retention等
- **monitor-burn-rate** から：Burn Rate、Runway
- **決算データ** から：MRR、Gross Margin、CAC、LTV

### Q2: 業界ベンチマークはどう設定するのか？

**A**: スキル実行時に業界タイプ（SaaS/E-commerce等）を選択すれば、自動的に最新ベンチマークが適用されます。カスタムベンチマークの設定も可能。

### Q3: 月次でダッシュボードを更新したい場合は？

**A**: 毎月末に同じスキルを再実行してください。新しい月次データが入力されると、自動的に更新されたダッシュボードが生成されます。自動更新スケジュール（週次/月次）も設定可能。

### Q4: 特定のKPIだけ追跡したい場合は？

**A**: テンプレート（`kpi_data_input.md`）でKPI項目をカスタマイズできます。不要なKPIは削除して使用してください。

---

## スキル実行フロー

```
STEP 1: 前提条件確認
  → validate-pmf、measure-aarrr等が実行済みか確認

STEP 2: KPIデータ入力
  → テンプレート（templates/kpi_data_input.md）を使用

STEP 3: ダッシュボード設定
  → ビジネスステージ（Phase 2-4）を指定
  → 業界タイプ（SaaS/E-commerce等）を選択

STEP 4: ダッシュボード自動生成
  → KPI統合 → Top 5選定 → トレンド生成
  → アラート設定 → ベンチマーク比較

STEP 5: エグゼクティブサマリー生成
  → 総合評価スコア計算 → アクション推奨

STEP 6: 投資家レポート形式エクスポート
  → PDF/PNG形式で出力

STEP 7: 自動更新スケジュール設定
  → 週次/月次の定期更新を設定（オプション）

STEP 8: 成果物出力
  → Flow/{YYYYMM}/{YYYY-MM-DD}/kpi_dashboard.md
```

---

## テンプレート・ファイル一覧

### 1. README.md（本ファイル）

スキルの概要、使用タイミング、KPI一覧、ステージ別選定ロジック、FAQ等を記載。

### 2. テンプレート: kpi_data_input.md

KPIデータ入力用テンプレート。以下を含む：
- Financial KPI（MRR、Burn Rate、Runway等）
- Customer KPI（CAC、LTV、Churn、NPS等）
- Product KPI（MAU、DAU/MAU、Feature Adoption等）
- Growth KPI（成長率、Sean Ellis、Viral Coefficient等）
- データ入力ガイダンス

### 3. テンプレート: dashboard_config.md

ダッシュボード設定用テンプレート。以下を含む：
- ビジネスステージ選択（Phase 2/3/4）
- 業界タイプ選択（SaaS/E-commerce等）
- ベンチマーク設定
- アラート閾値カスタマイズ
- グラフ期間設定（3/6/12ヶ月）

### 4. テンプレート: investor_report.md

投資家レポート専用テンプレート。以下を含む：
- Executive Summary
- Key Metrics（表形式）
- Financial Highlights
- Customer Highlights
- Product Highlights
- Outlook & Next Steps
- PDF/PNG エクスポート用フォーマット

---

## メタデータ

| 項目 | 値 |
|------|-----|
| **スキルID** | generate-kpi-dashboard |
| **ステージ** | Phase 2-4（PMF検証～スケール） |
| **所要時間** | 20-30分 |
| **出力ファイル** | Flow/{YYYYMM}/{YYYY-MM-DD}/kpi_dashboard.md |
| **前提スキル** | validate-pmf、measure-aarrr、monitor-burn-rate、validate-unit-economics |
| **フレームワーク準拠** | 起業の科学（100%） |
| **最終更新** | 2025-12-31 |
| **バージョン** | v1.0 |

---

## 次のステップ

1. **このREADMEを確認** → スキルの全体像を把握
2. **`templates/kpi_data_input.md`を参照** → 必要なKPIデータを準備
3. **スキル実行** → `/generate-kpi-dashboard` コマンド実行
4. **ダッシュボード確認** → Flow に生成されたファイルを確認
5. **投資家レポート作成** → 必要に応じてPDF/PNG エクスポート

---

**質問・改善提案**: SKILL.mdを参照し、フレームワークに関する質問や計算式の改善提案をお願いします。
