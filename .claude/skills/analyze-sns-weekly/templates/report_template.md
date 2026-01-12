# SNS週次パフォーマンスレポート

**分析期間**: {{FROM_DATE}} 〜 {{TO_DATE}}
**レポート生成日時**: {{GENERATED_AT}}
**対象プラットフォーム**: LinkedIn, X (Twitter), Threads

---

## 📊 エグゼクティブサマリー

### 総合評価

{{EXECUTIVE_SUMMARY}}

### 主要KPI達成状況

| プラットフォーム | インプレッション | エンゲージメント | エンゲージメント率 | KPI達成度 |
|----------------|----------------|----------------|------------------|----------|
| LinkedIn       | {{LINKEDIN_IMPRESSIONS}} | {{LINKEDIN_ENGAGEMENT}} | {{LINKEDIN_ENGAGEMENT_RATE}} | {{LINKEDIN_KPI_STATUS}} |
| X (Twitter)    | {{X_IMPRESSIONS}} | {{X_ENGAGEMENT}} | {{X_ENGAGEMENT_RATE}} | {{X_KPI_STATUS}} |
| Threads        | N/A※ | {{THREADS_ENGAGEMENT}} | N/A※ | {{THREADS_KPI_STATUS}} |

※ Threadsはインプレッション数の取得に対応していないため、エンゲージメント絶対数で評価

---

## 📈 プラットフォーム別詳細

### LinkedIn

#### パフォーマンスサマリー
- **総投稿数**: {{LINKEDIN_POST_COUNT}}件
- **インプレッション**: {{LINKEDIN_IMPRESSIONS}} / 目標 1,000
- **エンゲージメント**: {{LINKEDIN_ENGAGEMENT}} / 目標 50
- **エンゲージメント率**: {{LINKEDIN_ENGAGEMENT_RATE}} / 目標 5%

#### 分析
{{LINKEDIN_ANALYSIS}}

#### 推奨アクション
{{LINKEDIN_RECOMMENDATIONS}}

---

### X (Twitter)

#### パフォーマンスサマリー
- **総投稿数**: {{X_POST_COUNT}}件
- **インプレッション**: {{X_IMPRESSIONS}} / 目標 2,000
- **エンゲージメント**: {{X_ENGAGEMENT}} / 目標 100
- **エンゲージメント率**: {{X_ENGAGEMENT_RATE}} / 目標 5%

#### 分析
{{X_ANALYSIS}}

#### 推奨アクション
{{X_RECOMMENDATIONS}}

---

### Threads

#### パフォーマンスサマリー
- **総投稿数**: {{THREADS_POST_COUNT}}件
- **エンゲージメント**: {{THREADS_ENGAGEMENT}} / 目標 30
- **備考**: インプレッション数は技術的制約により取得不可

#### 分析
{{THREADS_ANALYSIS}}

#### 推奨アクション
{{THREADS_RECOMMENDATIONS}}

---

## 🏆 Top 5投稿分析

### 全プラットフォーム総合

{{TOP_POSTS_TABLE}}

### 成功パターン

{{SUCCESS_PATTERNS}}

---

## 📊 前週比較

### KPI変動

| プラットフォーム | インプレッション変化 | エンゲージメント変化 | エンゲージメント率変化 |
|----------------|-------------------|------------------|-------------------|
| LinkedIn       | {{LINKEDIN_IMPRESSIONS_CHANGE}} | {{LINKEDIN_ENGAGEMENT_CHANGE}} | {{LINKEDIN_ENGAGEMENT_RATE_CHANGE}} |
| X (Twitter)    | {{X_IMPRESSIONS_CHANGE}} | {{X_ENGAGEMENT_CHANGE}} | {{X_ENGAGEMENT_RATE_CHANGE}} |
| Threads        | N/A | {{THREADS_ENGAGEMENT_CHANGE}} | N/A |

### 分析

{{WEEK_OVER_WEEK_ANALYSIS}}

### 重要な変化

{{KEY_CHANGES}}

---

## 📉 4週トレンド分析

### インプレッション推移

| プラットフォーム | 4週前 | 3週前 | 2週前 | 前週 | 今週 | トレンド |
|----------------|------|------|------|-----|-----|---------|
| LinkedIn       | {{LINKEDIN_TREND_W4}} | {{LINKEDIN_TREND_W3}} | {{LINKEDIN_TREND_W2}} | {{LINKEDIN_TREND_W1}} | {{LINKEDIN_IMPRESSIONS}} | {{LINKEDIN_TREND}} |
| X (Twitter)    | {{X_TREND_W4}} | {{X_TREND_W3}} | {{X_TREND_W2}} | {{X_TREND_W1}} | {{X_IMPRESSIONS}} | {{X_TREND}} |

### エンゲージメント推移

| プラットフォーム | 4週前 | 3週前 | 2週前 | 前週 | 今週 | トレンド |
|----------------|------|------|------|-----|-----|---------|
| LinkedIn       | {{LINKEDIN_ENG_TREND_W4}} | {{LINKEDIN_ENG_TREND_W3}} | {{LINKEDIN_ENG_TREND_W2}} | {{LINKEDIN_ENG_TREND_W1}} | {{LINKEDIN_ENGAGEMENT}} | {{LINKEDIN_ENG_TREND}} |
| X (Twitter)    | {{X_ENG_TREND_W4}} | {{X_ENG_TREND_W3}} | {{X_ENG_TREND_W2}} | {{X_ENG_TREND_W1}} | {{X_ENGAGEMENT}} | {{X_ENG_TREND}} |
| Threads        | {{THREADS_ENG_TREND_W4}} | {{THREADS_ENG_TREND_W3}} | {{THREADS_ENG_TREND_W2}} | {{THREADS_ENG_TREND_W1}} | {{THREADS_ENGAGEMENT}} | {{THREADS_ENG_TREND}} |

### トレンド分析

{{TREND_ANALYSIS}}

---

## 💡 推奨アクション

### 優先度：高

{{HIGH_PRIORITY_ACTIONS}}

### 優先度：中

{{MEDIUM_PRIORITY_ACTIONS}}

### 優先度：低

{{LOW_PRIORITY_ACTIONS}}

---

## 📝 次週の戦略

{{NEXT_WEEK_STRATEGY}}

---

## 📎 補足情報

### データ品質

- **データ収集成功率**: {{DATA_COLLECTION_SUCCESS_RATE}}
- **欠損データ**: {{MISSING_DATA}}
- **備考**: {{DATA_NOTES}}

### 制約事項

- Threadsのインプレッション数は常に0を返すため、エンゲージメント絶対数で評価しています
- Late API Analytics Addonの仕様により、一部の詳細メトリクスは取得できない場合があります

---

**レポート生成**: Claude Code - analyze-sns-weekly skill
**データソース**: Late API (https://getlate.dev)
**分析期間**: {{FROM_DATE}} 〜 {{TO_DATE}}
