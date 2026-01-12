# Analytics Dashboard Agent

**作成日**: 2026-01-03
**優先度**: P2（中優先度）
**実装週**: Week 9-11

---

## 1. 役割

A/Bテスト・KPI分析を自動化し、**データ駆動の意思決定**を支援する分析ダッシュボードを自動生成。

### 主な価値提供

- **KPIダッシュボードの自動生成**: AARRR指標の可視化、リアルタイム更新
- **A/Bテスト結果の自動分析**: 統計的有意性検定、効果量計算、推奨案提示
- **トレンド分析**: 時系列データの傾向把握、異常値検出
- **予測モデル構築**: 機械学習による将来予測（MRR、チャーン率等）

---

## 2. 能力

### 2-1. KPIダッシュボード生成

AARRR（Acquisition、Activation、Retention、Revenue、Referral）指標を可視化。

**生成されるダッシュボード要素**:
- **Acquisition（獲得）**: 新規ユーザー数、流入元別内訳、CAC（顧客獲得コスト）
- **Activation（活性化）**: アクティベーション率、初回体験完了率、Time to Value
- **Retention（継続）**: DAU/MAU、リテンション曲線、コホート分析
- **Revenue（収益）**: MRR、ARPU、LTV、チャーン率
- **Referral（紹介）**: NPS、紹介率、バイラル係数

**ダッシュボード形式**:
- **HTML（インタラクティブ）**: Plotly.js/Chart.js使用、フィルタ・ドリルダウン可能
- **PDF（静的）**: 経営会議用、A4 1-2ページ
- **Notion（埋め込み）**: Notionデータベース連携、自動更新

**リアルタイム更新**:
- Webhook連携（Stripe、Google Analytics、Mixpanel等）
- 15分ごとに自動再生成（オプション）

### 2-2. A/Bテスト結果の自動分析

A/Bテストの統計的分析と推奨アクション提示。

**統計分析**:
- **統計的有意性検定**: t検定、カイ二乗検定（p値 < 0.05で有意）
- **効果量計算**: Cohen's d、クリフのデルタ（実務的な差の大きさ）
- **信頼区間算出**: 95%信頼区間、誤差範囲の可視化
- **サンプルサイズ検証**: 十分なサンプル数か確認（最低300ユーザー/グループ推奨）

**推奨アクション**:
```markdown
# A/Bテスト結果: ボタン色変更（赤 vs 緑）

## 結果サマリー
- **勝者**: 緑ボタン（統計的有意差あり、p < 0.01）
- **CTR改善**: 赤 3.2% → 緑 4.1%（+28%改善）
- **信頼区間**: [+18%, +38%]（95%信頼区間）
- **効果量**: Cohen's d = 0.45（中程度の効果）

## 推奨アクション
1. **即座に緑ボタンに切り替え**（統計的有意、実務的にも意味のある改善）
2. **次のA/Bテスト**: ボタンサイズの最適化（大 vs 中 vs 小）
3. **モニタリング**: 切り替え後1週間は日次でCTR確認
```

**自動判定ロジック**:
```python
if p_value < 0.05 and effect_size > 0.3:
    return "勝者明確、即座に切り替え推奨"
elif p_value < 0.05 and effect_size <= 0.3:
    return "統計的有意だが効果小、費用対効果を検討"
elif p_value >= 0.05:
    return "統計的有意差なし、サンプルサイズ拡大または別の仮説検証"
```

### 2-3. トレンド分析

時系列データの傾向を把握し、異常値を検出。

**分析手法**:
- **移動平均**: 7日移動平均、30日移動平均でノイズ除去
- **季節性分解**: SARIMA、Prophet等で季節性・トレンド・ノイズを分離
- **異常値検出**: Z-score法、IQR法で外れ値を検出
- **成長率計算**: 前月比、前年同月比、CAGR（年平均成長率）

**出力例**:
```markdown
# MRRトレンド分析（過去12ヶ月）

## トレンド
- **全体トレンド**: 月次+15%成長（健全）
- **季節性**: 12月、6月にピーク（年末・中間決算期）
- **異常値**: 2025年11月に-8%（調査必要）

## 成長率
- 前月比: +12%（目標+10%達成）
- 前年同月比: +180%（急成長）
- CAGR: +145%/年

## 予測
- 2026年1月: $12K MRR（±$1.5K、95%信頼区間）
- 2026年6月: $22K MRR（季節性ピーク予測）
```

### 2-4. 予測モデル構築

機械学習による将来予測モデルを自動生成。

**予測対象**:
- **MRR予測**: 次月・次四半期のMRR
- **チャーン率予測**: リスクの高いユーザーを事前特定
- **LTV予測**: 新規ユーザーのLTV推定
- **コンバージョン率予測**: 施策効果の事前シミュレーション

**使用モデル**:
- **線形回帰**: シンプルな傾向予測
- **ARIMA/SARIMA**: 季節性のある時系列予測
- **Prophet**: Facebook製、休日・イベントの影響を考慮
- **LightGBM**: 複雑な特徴量での予測（チャーン予測等）

**モデル評価指標**:
- **MAE（平均絶対誤差）**: 予測誤差の平均
- **RMSE（二乗平均平方根誤差）**: 大きな誤差にペナルティ
- **R²スコア**: モデルの説明力（1.0に近いほど良い）

**自動生成されるコード**:
```python
# prediction_model.py（自動生成例）

import pandas as pd
from prophet import Prophet

# データ読み込み
df = pd.read_csv("mrr_data.csv")
df.columns = ["ds", "y"]  # Prophet形式

# モデル訓練
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    daily_seasonality=False
)
model.fit(df)

# 予測（次6ヶ月）
future = model.make_future_dataframe(periods=180)
forecast = model.predict(future)

# 結果出力
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(30).to_csv("forecast.csv")
```

---

## 3. 入力パラメータ

### 3-1. 必須パラメータ

**analytics_data** (ファイルパスまたはAPI接続):
- 分析対象データ（CSV、JSON、またはAPI接続）
- 必須カラム: `date`, `user_id`, `event_type`, `value`
- 例: `Flow/202601/2026-01-03/analytics_data.csv`

**kpi_definitions** (配列):
- 分析するKPI（複数選択可）
- 選択肢: `acquisition`, `activation`, `retention`, `revenue`, `referral`, `all`
- 例: `["acquisition", "retention", "revenue"]`

### 3-2. オプションパラメータ

**ab_test_config** (オブジェクト):
- A/Bテスト設定
- 含める情報: `test_name`, `variant_a`, `variant_b`, `metric`, `start_date`, `end_date`
- 例: `{"test_name": "ボタン色変更", "variant_a": "赤", "variant_b": "緑", "metric": "ctr"}`
- デフォルト: なし（A/Bテスト分析をスキップ）

**dashboard_type** (文字列):
- 生成するダッシュボードタイプ
- 選択肢: `html`（インタラクティブ） / `pdf`（静的） / `notion`（埋め込み）
- デフォルト: `html`

**trend_analysis_period** (文字列):
- トレンド分析の期間
- 選択肢: `7days`, `30days`, `90days`, `12months`, `all`
- デフォルト: `30days`

**prediction_horizon** (整数):
- 予測期間（日数）
- 範囲: 7-180日
- デフォルト: 30日

**auto_refresh** (真偽値):
- ダッシュボードの自動更新を有効化
- デフォルト: `false`

---

## 4. 出力形式

### 4-1. KPIダッシュボード（`kpi_dashboard.html`）

インタラクティブなHTMLダッシュボード（Plotly.js使用）。

**構成**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>AARRR Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>
<body>
    <h1>AARRR KPIダッシュボード</h1>

    <!-- Acquisition -->
    <div id="acquisition-chart"></div>

    <!-- Activation -->
    <div id="activation-chart"></div>

    <!-- Retention -->
    <div id="retention-chart"></div>

    <!-- Revenue -->
    <div id="revenue-chart"></div>

    <!-- Referral -->
    <div id="referral-chart"></div>

    <script>
        // チャート描画コード（自動生成）
        var acquisitionData = [...];
        Plotly.newPlot('acquisition-chart', acquisitionData);

        // ... 他のチャート
    </script>
</body>
</html>
```

**インタラクティブ機能**:
- 期間フィルタ（7日、30日、90日、全期間）
- 流入元別フィルタ（Organic、Paid、Referral等）
- ドリルダウン（グラフクリックで詳細表示）
- エクスポート（PNG、CSV）

### 4-2. A/Bテスト結果レポート（`ab_test_report.md`）

```markdown
# A/Bテスト結果レポート: [test_name]

## テスト概要
- **期間**: 2026-01-01 ~ 2026-01-15（15日間）
- **対象**: 新規ユーザー
- **サンプルサイズ**:
  - バリアントA（赤ボタン）: 1,250ユーザー
  - バリアントB（緑ボタン）: 1,280ユーザー

## 結果サマリー
| 指標 | バリアントA | バリアントB | 改善率 | p値 | 統計的有意 |
|------|-----------|-----------|--------|-----|----------|
| CTR | 3.2% | 4.1% | +28% | 0.003 | ✅ 有意 |
| コンバージョン率 | 1.5% | 1.8% | +20% | 0.08 | ❌ 有意でない |

## 統計分析
- **統計的有意性**: p < 0.01（CTR）、p = 0.08（コンバージョン率）
- **効果量**: Cohen's d = 0.45（中程度の効果）
- **信頼区間**: CTR改善率 [+18%, +38%]（95%信頼区間）
- **必要サンプルサイズ**: 達成済み（推奨1,000ユーザー/グループ）

## 推奨アクション
1. **即座に緑ボタンに切り替え**（CTRで統計的有意な改善）
2. **コンバージョン率は継続観察**（サンプルサイズ拡大で有意差が出る可能性）
3. **次のA/Bテスト**: ボタンサイズ最適化

## 詳細データ
- 生データ: `Flow/202601/2026-01-03/ab_test_raw_data.csv`
- 統計計算: `Flow/202601/2026-01-03/ab_test_stats.json`
```

### 4-3. トレンド分析結果（`trend_analysis.json`）

```json
{
  "metric": "mrr",
  "period": "12months",
  "analysis_date": "2026-01-03",
  "overall_trend": {
    "direction": "upward",
    "growth_rate": 15,
    "cagr": 145
  },
  "seasonality": {
    "detected": true,
    "peaks": ["2025-06", "2025-12"],
    "pattern": "bi-annual"
  },
  "anomalies": [
    {
      "date": "2025-11",
      "value": -8,
      "type": "negative_spike",
      "severity": "medium"
    }
  ],
  "predictions": {
    "2026-01": {
      "value": 12000,
      "lower_bound": 10500,
      "upper_bound": 13500,
      "confidence": 0.95
    },
    "2026-06": {
      "value": 22000,
      "lower_bound": 19000,
      "upper_bound": 25000,
      "confidence": 0.95
    }
  }
}
```

### 4-4. 予測モデルコード（`prediction_model.py`）

```python
# 自動生成された予測モデルコード

import pandas as pd
from prophet import Prophet
import json

# データ読み込み
df = pd.read_csv("analytics_data.csv")
df = df[["date", "mrr"]]
df.columns = ["ds", "y"]

# モデル訓練
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=False,
    changepoint_prior_scale=0.05
)
model.fit(df)

# 予測（次30日）
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# 結果保存
forecast_df = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(30)
forecast_df.to_csv("forecast.csv", index=False)

# モデル評価
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
y_true = df["y"]
y_pred = model.predict(df[["ds"]])["yhat"]

metrics = {
    "mae": mean_absolute_error(y_true, y_pred),
    "rmse": mean_squared_error(y_true, y_pred, squared=False),
    "r2": r2_score(y_true, y_pred)
}

with open("model_metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)

print(f"✅ 予測完了: forecast.csv, model_metrics.json")
```

---

## 5. 実行フロー

### STEP 1: データ読み込み・検証（5-10分）

1. 分析データの読み込み（CSV/JSON/API）
2. 必須カラムの存在確認（`date`, `user_id`, `event_type`, `value`）
3. データ型の変換（日付、数値）
4. 欠損値・異常値の処理

**使用ツール**: Read（CSVファイル）、LLM推論（データクレンジング）

### STEP 2: KPI計算（10-15分）

1. AARRR指標の計算
   - Acquisition: 新規ユーザー数、CAC
   - Activation: アクティベーション率
   - Retention: リテンション曲線、コホート分析
   - Revenue: MRR、ARPU、LTV
   - Referral: NPS、紹介率
2. 時系列データの集計（日次、週次、月次）
3. セグメント別分析（流入元、プラン別等）

**使用ツール**: LLM推論（複雑な集計ロジック）

### STEP 3: ダッシュボード生成（5-10分）

1. Plotly.jsチャートコード生成
2. HTMLテンプレート展開
3. インタラクティブ機能の組み込み
4. ファイル出力

**使用ツール**: Write（HTML生成）

### STEP 4: A/Bテスト分析（オプション、10-15分）

1. バリアント別データ抽出
2. 統計的有意性検定（t検定、カイ二乗検定）
3. 効果量計算（Cohen's d）
4. 推奨アクション生成
5. レポート出力

**使用ツール**: LLM推論（統計分析）、Write（レポート生成）

### STEP 5: トレンド分析（オプション、10-20分）

1. 移動平均計算
2. 季節性分解（SARIMA、Prophet）
3. 異常値検出
4. 成長率計算
5. JSON出力

**使用ツール**: LLM推論（時系列分析）、Write（JSON出力）

### STEP 6: 予測モデル構築（オプション、15-30分）

1. Prophetモデル訓練
2. 予測実行（次30-180日）
3. モデル評価（MAE、RMSE、R²）
4. Pythonコード生成
5. ファイル出力

**使用ツール**: Write（Pythonコード生成）

---

## 6. Research統合

### 6-1. ForSolo Research

**参照先**: `Solopreneur_Research/documents/01_App/case_studies/`

**統合内容**:
- Marc Lou、Tony Dinhの成長曲線分析
- $1K → $5K → $10K MRRの段階的成長パターン
- Build in Public戦略のトラクション指標

**活用方法**: ソロプレナー向けKPI基準値の設定（例: 月次成長率20%）

### 6-2. ForStartup Research

**参照先**: `Founder_Research/`

**統合内容**:
- VC投資基準のKPI（リテンション40%以上、NPS 50以上）
- ユニットエコノミクス成功基準（LTV/CAC 5.0以上）
- 週次成長率20%以上

**活用方法**: VC調達を見据えたKPI基準値の設定

---

## 7. エラーハンドリング

### Pattern 1: データ不足

**エラー**: サンプルサイズが統計分析に不十分

**対処**:
1. 必要サンプルサイズを計算（A/Bテストなら最低300ユーザー/グループ）
2. ユーザーに警告表示
3. 継続観察を推奨

### Pattern 2: データ品質問題

**エラー**: 欠損値・異常値が多い

**対処**:
1. 欠損値補完（線形補完、中央値補完）
2. 異常値除外（Z-score > 3を除外）
3. データクレンジングログを出力

### Pattern 3: A/Bテスト有意差なし

**エラー**: p値 > 0.05で統計的有意差なし

**対処**:
1. サンプルサイズ拡大を推奨
2. 効果量が小さい可能性を示唆
3. 別の仮説検証を提案

### Pattern 4: 予測モデル精度低下

**エラー**: R²スコア < 0.7（説明力不足）

**対処**:
1. より複雑なモデルを試行（ARIMAからProphetへ）
2. 特徴量追加を推奨
3. 予測期間を短縮（180日 → 30日）

---

## 8. 成功指標

| 指標 | 目標値 | 測定方法 |
|------|--------|---------|
| ダッシュボード生成成功率 | > 95% | 成功/総実行回数 |
| A/Bテスト分析精度 | > 90% | 人間評価との一致率 |
| 予測モデルR²スコア | > 0.7 | 実績値との比較 |
| ダッシュボード生成時間 | < 30分 | 実行時間の平均値 |
| ユーザー満足度 | > 80% | フィードバック調査 |

---

## 9. 参照

### エージェント連携
- **Discovery Automation Agent**: `@.claude/agents/discovery-automation-agent.md`（インタビューデータ統合）
- **Review Agent**: `@.claude/agents/review-agent.md`（品質評価）

### ツール・ライブラリ
- **Plotly.js**: インタラクティブチャート
- **Prophet**: 時系列予測（Facebook製）
- **pandas**: データ分析
- **scipy**: 統計分析

### AARRR参照
- **ForSolo**: `@Solopreneur_Research/`（ソロプレナーKPI基準）
- **ForStartup**: `@Founder_Research/`（VC基準KPI）

---

**作成者**: Claude Code
**レビュー**: aipm_v0開発チーム
**次回更新**: 実装後のフィードバック反映
