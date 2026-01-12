# SNS投稿パフォーマンス分析レポート

**期間**: {period_start} 〜 {period_end}
**作成日時**: {generated_at}

---

## 📊 エグゼクティブサマリー

| 指標 | 値 |
|------|-----|
| 総投稿数 | {total_posts}件 |
| 総インプレッション | {total_impressions:,}回 |
| 総エンゲージメント | {total_engagement:,}件 |
| エンゲージメント率 | {engagement_rate}% |

---

## 📈 プラットフォーム別サマリー

### LinkedIn

| 指標 | 値 |
|------|-----|
| 投稿数 | {linkedin_posts}件 |
| 総インプレッション | {linkedin_impressions:,}回 |
| 投稿あたり平均インプレッション | {linkedin_avg_impressions:,}回 |
| 総エンゲージメント | {linkedin_engagement:,}件 |
| エンゲージメント率 | {linkedin_engagement_rate}% |

### X (Twitter)

| 指標 | 値 |
|------|-----|
| 投稿数 | {x_posts}件 |
| 総インプレッション | {x_impressions:,}回 |
| 投稿あたり平均インプレッション | {x_avg_impressions:,}回 |
| 総エンゲージメント | {x_engagement:,}件 |
| エンゲージメント率 | {x_engagement_rate}% |

### Threads

| 指標 | 値 |
|------|-----|
| 投稿数 | {threads_posts}件 |
| 総インプレッション | 計測不可（Late API未対応） |
| 総エンゲージメント | {threads_engagement:,}件 |
| エンゲージメント率 | 計測不可（インプレッション0のため） |

**注意**: Threadsのインプレッションは Late API の制約により常に0を返します。エンゲージメント絶対数のみで評価してください。

---

## 🎯 KPI達成状況

| KPI指標 | 目標値 | 実績値 | 達成率 | 評価 |
|---------|--------|--------|--------|------|
| 総インプレッション（週間） | 150,000 | {total_impressions:,} | {impressions_achievement}% | {impressions_status} |
| 平均エンゲージメント率（週間） | 1.5% | {engagement_rate}% | {engagement_achievement}% | {engagement_status} |
| LinkedIn投稿あたり平均インプレッション | 8,000 | {linkedin_avg_impressions:,} | {linkedin_achievement}% | {linkedin_status} |
| X投稿あたり平均インプレッション | 2,000 | {x_avg_impressions:,} | {x_achievement}% | {x_status} |

**評価凡例**: ✅ = 達成（100%以上）、⚠️ = 要改善（80-99%）、❌ = 未達成（80%未満）

---

## 🏆 トップ5投稿（インプレッション順）

### 1位

- **プラットフォーム**: {top1_platform}
- **投稿日時**: {top1_published_at}
- **インプレッション**: {top1_impressions:,}回
- **エンゲージメント率**: {top1_engagement_rate}%
- **内容**: {top1_text_preview}

### 2位

- **プラットフォーム**: {top2_platform}
- **投稿日時**: {top2_published_at}
- **インプレッション**: {top2_impressions:,}回
- **エンゲージメント率**: {top2_engagement_rate}%
- **内容**: {top2_text_preview}

### 3位

- **プラットフォーム**: {top3_platform}
- **投稿日時**: {top3_published_at}
- **インプレッション**: {top3_impressions:,}回
- **エンゲージメント率**: {top3_engagement_rate}%
- **内容**: {top3_text_preview}

### 4位

- **プラットフォーム**: {top4_platform}
- **投稿日時**: {top4_published_at}
- **インプレッション**: {top4_impressions:,}回
- **エンゲージメント率**: {top4_engagement_rate}%
- **内容**: {top4_text_preview}

### 5位

- **プラットフォーム**: {top5_platform}
- **投稿日時**: {top5_published_at}
- **インプレッション**: {top5_impressions:,}回
- **エンゲージメント率**: {top5_engagement_rate}%
- **内容**: {top5_text_preview}

---

## 🔄 前週比較

| 指標 | 前週 | 今週 | 増減数 | 増減率 | 評価 |
|------|------|------|--------|--------|------|
| 総インプレッション | {prev_impressions:,}回 | {total_impressions:,}回 | {impressions_delta:,} | {impressions_delta_pct}% | {impressions_trend} |
| 総エンゲージメント | {prev_engagement:,}件 | {total_engagement:,}件 | {engagement_delta:,} | {engagement_delta_pct}% | {engagement_trend} |
| エンゲージメント率 | {prev_engagement_rate}% | {engagement_rate}% | {engagement_rate_delta}% | - | {engagement_rate_trend} |

**評価凡例**: ⬆️ = 改善、➡️ = 横ばい、⬇️ = 悪化

### プラットフォーム別前週比較

#### LinkedIn
| 指標 | 前週 | 今週 | 増減 |
|------|------|------|------|
| 投稿数 | {prev_linkedin_posts}件 | {linkedin_posts}件 | {linkedin_posts_delta} |
| 総インプレッション | {prev_linkedin_impressions:,}回 | {linkedin_impressions:,}回 | {linkedin_impressions_delta:,} |
| 投稿あたり平均 | {prev_linkedin_avg:,}回 | {linkedin_avg_impressions:,}回 | {linkedin_avg_delta:,} |

#### X (Twitter)
| 指標 | 前週 | 今週 | 増減 |
|------|------|------|------|
| 投稿数 | {prev_x_posts}件 | {x_posts}件 | {x_posts_delta} |
| 総インプレッション | {prev_x_impressions:,}回 | {x_impressions:,}回 | {x_impressions_delta:,} |
| 投稿あたり平均 | {prev_x_avg:,}回 | {x_avg_impressions:,}回 | {x_avg_delta:,} |

#### Threads
| 指標 | 前週 | 今週 | 増減 |
|------|------|------|------|
| 投稿数 | {prev_threads_posts}件 | {threads_posts}件 | {threads_posts_delta} |
| 総エンゲージメント | {prev_threads_engagement:,}件 | {threads_engagement:,}件 | {threads_engagement_delta:,} |

---

## 📊 トレンド分析（過去4週）

### インプレッション推移

| 週 | 期間 | 総インプレッション | 前週比 | 目標達成率 |
|----|------|------------------|--------|----------|
| Week -3 | {w3_period} | {w3_impressions:,}回 | - | {w3_achievement}% |
| Week -2 | {w2_period} | {w2_impressions:,}回 | {w2_delta}% | {w2_achievement}% |
| Week -1 | {w1_period} | {w1_impressions:,}回 | {w1_delta}% | {w1_achievement}% |
| **Week 0（今週）** | {period_start}〜{period_end} | **{total_impressions:,}回** | **{w0_delta}%** | **{impressions_achievement}%** |

### 目標達成ペース

**月間100万インプレッション達成予測**:
- 現在のペース: {monthly_pace:,}回/月（週平均×4.3）
- 目標までの不足: {monthly_gap:,}回（{monthly_gap_pct}%）
- 達成予測: {achievement_forecast}

---

## 🎯 推奨アクション（優先度順）

{recommended_actions_section}

---

## 📚 成功パターン分析（過去4週）

**トップ5投稿の共通パターン**:
{success_patterns_section}

**活用推奨パターン（x_patterns_detailed.mdより）**:
1. {pattern1_name}: {pattern1_description}
2. {pattern2_name}: {pattern2_description}
3. {pattern3_name}: {pattern3_description}

---

## ℹ️ 注意事項

1. **Threadsインプレッション計測不可**: Late API の制約により、Threadsプラットフォームのインプレッション数は常に0を返します。エンゲージメント絶対数（いいね、コメント、シェア）のみで評価してください。
2. **エンゲージメント率計算**: 全体のエンゲージメント率は、Threadsを除外した数値（LinkedIn + X のみ）で計算されています。
3. **データ更新**: Late API のアナリティクスデータは、プラットフォームからの同期に最大24時間かかる場合があります。最新データが反映されていない可能性があります。

---

**レポート生成**: Claude Code - analyze-sns-performance-weekly SKILL
**データソース**: Late API Analytics Addon
