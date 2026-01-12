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
| 総Views | {threads_views:,}回 |
| 投稿あたり平均Views | {threads_avg_views:,}回 |
| 総エンゲージメント | {threads_engagement:,}件 |
| エンゲージメント率 | {threads_engagement_rate}% |

**注意**: Threadsは `views` フィールドを使用。views=0の場合は「計測不可」としてエンゲージメント絶対数のみで評価してください。

### Facebook（Professional Dashboard）

| 指標 | 値 |
|------|-----|
| 総閲覧数（28日累計） | {facebook_views:,}回 |
| 閲覧者数 | {facebook_viewers:,}人 |
| 総インタラクション | {facebook_interactions:,}件 |
| └ リアクション | {facebook_reactions:,}件 |
| └ コメント | {facebook_comments:,}件 |
| └ シェア | {facebook_shares:,}件 |
| エンゲージメント率 | {facebook_engagement_rate}% |
| フォロワー数 | {facebook_followers:,}人 |
| 純フォロー数（28日） | {facebook_net_followers}人 |
| 閲覧数変化率 | {facebook_views_change} |
| インタラクション変化率 | {facebook_interactions_change} |

**データソース**: Professional Dashboard (Chrome MCP経由)
**データ品質**: {facebook_data_quality}%
**注意**: 28日間累計データ。週次比較は変化率で評価してください。

---

## 🎯 KPI達成状況

| KPI指標 | 目標値 | 実績値 | 達成率 | 評価 |
|---------|--------|--------|--------|------|
| 総インプレッション（週間） | 150,000 | {total_impressions:,} | {impressions_achievement}% | {impressions_status} |
| 平均エンゲージメント率（週間） | 1.5% | {engagement_rate}% | {engagement_achievement}% | {engagement_status} |
| LinkedIn投稿あたり平均インプレッション | 8,000 | {linkedin_avg_impressions:,} | {linkedin_achievement}% | {linkedin_status} |
| X投稿あたり平均インプレッション | 2,000 | {x_avg_impressions:,} | {x_achievement}% | {x_status} |
| Threads投稿あたり平均Views | 100 | {threads_avg_views:,} | {threads_views_achievement}% | {threads_views_status} |
| **Facebook週間閲覧数** | **100,000** | **{facebook_views:,}** | **{facebook_views_achievement}%** | **{facebook_views_status}** |
| **Facebookインタラクション** | **1,500** | **{facebook_interactions:,}** | **{facebook_interactions_achievement}%** | **{facebook_interactions_status}** |
| **Facebookフォロワー増** | **150** | **{facebook_net_followers}** | **{facebook_followers_achievement}%** | **{facebook_followers_status}** |

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
| 総Views | {prev_threads_views:,}回 | {threads_views:,}回 | {threads_views_delta:,} |
| 投稿あたり平均Views | {prev_threads_avg_views:,}回 | {threads_avg_views:,}回 | {threads_avg_views_delta:,} |
| 総エンゲージメント | {prev_threads_engagement:,}件 | {threads_engagement:,}件 | {threads_engagement_delta:,} |

#### Facebook（28日累計データ）
| 指標 | 変化率 | 評価 |
|------|--------|------|
| 閲覧数 | {facebook_views_change} | {facebook_views_trend} |
| インタラクション | {facebook_interactions_change} | {facebook_interactions_trend} |
| フォロワー | {facebook_followers_change} | {facebook_followers_trend} |

**注意**: Facebookは28日間ローリングウィンドウのため、週次絶対値比較ではなく変化率で評価

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

1. **Threads Views指標**: Threadsは `views` フィールドを使用してリーチを測定。views=0の場合は「計測不可」としてエンゲージメント絶対数のみで評価してください。
2. **エンゲージメント率計算**: 全体のエンゲージメント率は、Threads viewsを除外した数値（LinkedIn + X のインプレッションのみ）で計算されています。
3. **データ更新**: Late API のアナリティクスデータは、プラットフォームからの同期に最大24時間かかる場合があります。最新データが反映されていない可能性があります。
4. **Facebook 28日累計データ**: FacebookはProfessional Dashboard経由で収集。28日間ローリングウィンドウのため、週次比較は変化率で評価してください。
5. **Facebook収集失敗時**: Chrome MCP接続エラー等でFacebookデータが取得できない場合、Late APIプラットフォーム（LinkedIn, X, Threads）のみで分析を継続します。

---

**レポート生成**: Claude Code - analyze-sns-performance-weekly SKILL
**データソース**: Late API Analytics Addon + Facebook Professional Dashboard (Chrome MCP)
