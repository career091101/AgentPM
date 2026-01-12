# SNS投稿パフォーマンス分析レポート

**期間**: {period_start} 〜 {period_end}
**作成日時**: {generated_at}

---

## 📊 エグゼクティブサマリー

| 指標 | 値 |
|------|-----|
| 総投稿数 | {total_posts}件 |
| **総リーチ** | **{total_reach:,}回** |
| ├ LinkedIn impressions | {linkedin_impressions:,}回 |
| ├ X impressions | {x_impressions:,}回 |
| ├ Threads views | {threads_views:,}回 |
| └ Facebook views | {facebook_views:,}回 |
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
| **総リーチ** | **500,000** | **{total_reach:,}** | **{total_reach_achievement}%** | **{total_reach_status}** |
| └ Late API impressions | 150,000 | {total_impressions:,} | {impressions_achievement}% | {impressions_status} |
| └ Threads views | 5,000 | {threads_views:,} | {threads_views_achievement}% | {threads_views_status} |
| └ Facebook views | 100,000 | {facebook_views:,} | {facebook_views_achievement}% | {facebook_views_status} |
| 平均エンゲージメント率（週間） | 1.5% | {engagement_rate}% | {engagement_achievement}% | {engagement_status} |
| LinkedIn投稿あたり平均インプレッション | 8,000 | {linkedin_avg_impressions:,} | {linkedin_achievement}% | {linkedin_status} |
| X投稿あたり平均インプレッション | 2,000 | {x_avg_impressions:,} | {x_achievement}% | {x_status} |
| Threads投稿あたり平均Views | 100 | {threads_avg_views:,} | {threads_views_achievement}% | {threads_views_status} |
| **Facebookインタラクション** | **1,500** | **{facebook_interactions:,}** | **{facebook_interactions_achievement}%** | **{facebook_interactions_status}** |
| **Facebookフォロワー増** | **150** | **{facebook_net_followers}** | **{facebook_followers_achievement}%** | **{facebook_followers_status}** |

**評価凡例**: ✅ = 達成（100%以上）、⚠️ = 要改善（80-99%）、❌ = 未達成（80%未満）

---

## 🏆 トップ20投稿（全プラットフォーム統合）

| 順位 | Platform | タイトル（最初100文字） | Reach | 💙 Likes | 💬 Comments | 🔄 Shares | Engagement Rate |
|------|----------|---------------------|-------|----------|-------------|----------|----------------|
| 1 | {top1_platform_icon} | {top1_title_100chars} | {top1_reach:,} | {top1_likes} | {top1_comments} | {top1_shares} | {top1_rate}% |
| 2 | {top2_platform_icon} | {top2_title_100chars} | {top2_reach:,} | {top2_likes} | {top2_comments} | {top2_shares} | {top2_rate}% |
| 3 | {top3_platform_icon} | {top3_title_100chars} | {top3_reach:,} | {top3_likes} | {top3_comments} | {top3_shares} | {top3_rate}% |
| 4 | {top4_platform_icon} | {top4_title_100chars} | {top4_reach:,} | {top4_likes} | {top4_comments} | {top4_shares} | {top4_rate}% |
| 5 | {top5_platform_icon} | {top5_title_100chars} | {top5_reach:,} | {top5_likes} | {top5_comments} | {top5_shares} | {top5_rate}% |
| 6 | {top6_platform_icon} | {top6_title_100chars} | {top6_reach:,} | {top6_likes} | {top6_comments} | {top6_shares} | {top6_rate}% |
| 7 | {top7_platform_icon} | {top7_title_100chars} | {top7_reach:,} | {top7_likes} | {top7_comments} | {top7_shares} | {top7_rate}% |
| 8 | {top8_platform_icon} | {top8_title_100chars} | {top8_reach:,} | {top8_likes} | {top8_comments} | {top8_shares} | {top8_rate}% |
| 9 | {top9_platform_icon} | {top9_title_100chars} | {top9_reach:,} | {top9_likes} | {top9_comments} | {top9_shares} | {top9_rate}% |
| 10 | {top10_platform_icon} | {top10_title_100chars} | {top10_reach:,} | {top10_likes} | {top10_comments} | {top10_shares} | {top10_rate}% |
| 11 | {top11_platform_icon} | {top11_title_100chars} | {top11_reach:,} | {top11_likes} | {top11_comments} | {top11_shares} | {top11_rate}% |
| 12 | {top12_platform_icon} | {top12_title_100chars} | {top12_reach:,} | {top12_likes} | {top12_comments} | {top12_shares} | {top12_rate}% |
| 13 | {top13_platform_icon} | {top13_title_100chars} | {top13_reach:,} | {top13_likes} | {top13_comments} | {top13_shares} | {top13_rate}% |
| 14 | {top14_platform_icon} | {top14_title_100chars} | {top14_reach:,} | {top14_likes} | {top14_comments} | {top14_shares} | {top14_rate}% |
| 15 | {top15_platform_icon} | {top15_title_100chars} | {top15_reach:,} | {top15_likes} | {top15_comments} | {top15_shares} | {top15_rate}% |
| 16 | {top16_platform_icon} | {top16_title_100chars} | {top16_reach:,} | {top16_likes} | {top16_comments} | {top16_shares} | {top16_rate}% |
| 17 | {top17_platform_icon} | {top17_title_100chars} | {top17_reach:,} | {top17_likes} | {top17_comments} | {top17_shares} | {top17_rate}% |
| 18 | {top18_platform_icon} | {top18_title_100chars} | {top18_reach:,} | {top18_likes} | {top18_comments} | {top18_shares} | {top18_rate}% |
| 19 | {top19_platform_icon} | {top19_title_100chars} | {top19_reach:,} | {top19_likes} | {top19_comments} | {top19_shares} | {top19_rate}% |
| 20 | {top20_platform_icon} | {top20_title_100chars} | {top20_reach:,} | {top20_likes} | {top20_comments} | {top20_shares} | {top20_rate}% |

**プラットフォームアイコン**:
- 💼 = LinkedIn
- 🐦 = X (Twitter)
- 🧵 = Threads
- 📘 = Facebook

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

### 📍 アクション1: {action1_title}

**期待効果**: {action1_expected_effect}
**優先度**: {action1_priority}/100
**エビデンス強度**: {action1_evidence_score}/100

#### 📊 根拠とエビデンス

**内部データ分析**:
{action1_internal_data}

**業界ベストプラクティス**:
- 参照: {action1_best_practice_ref}
- {action1_best_practice_quote}

**最新トレンド**（2026年1月）:
{action1_trend_insight}

**競合成功事例**:
{action1_competitor_example}

#### 5ステップ実装手順

**STEP 1: 現状分析**
{action1_step1_analysis}

**STEP 2: 目標設定**
{action1_step2_goal}

**STEP 3: 実施**
{action1_step3_implementation}

**プラットフォーム固有の注意事項**:
{action1_platform_notes}

**STEP 4: 測定**
{action1_step4_measurement}

**STEP 5: 調整**
{action1_step5_adjustment}

---

### 📍 アクション2: {action2_title}

**期待効果**: {action2_expected_effect}
**優先度**: {action2_priority}/100
**エビデンス強度**: {action2_evidence_score}/100

#### 📊 根拠とエビデンス

**内部データ分析**:
{action2_internal_data}

**業界ベストプラクティス**:
- 参照: {action2_best_practice_ref}
- {action2_best_practice_quote}

**最新トレンド**（2026年1月）:
{action2_trend_insight}

**競合成功事例**:
{action2_competitor_example}

#### 5ステップ実装手順

**STEP 1: 現状分析**
{action2_step1_analysis}

**STEP 2: 目標設定**
{action2_step2_goal}

**STEP 3: 実施**
{action2_step3_implementation}

**プラットフォーム固有の注意事項**:
{action2_platform_notes}

**STEP 4: 測定**
{action2_step4_measurement}

**STEP 5: 調整**
{action2_step5_adjustment}

---

### 📍 アクション3: {action3_title}

**期待効果**: {action3_expected_effect}
**優先度**: {action3_priority}/100
**エビデンス強度**: {action3_evidence_score}/100

#### 📊 根拠とエビデンス

**内部データ分析**:
{action3_internal_data}

**業界ベストプラクティス**:
- 参照: {action3_best_practice_ref}
- {action3_best_practice_quote}

**最新トレンド**（2026年1月）:
{action3_trend_insight}

**競合成功事例**:
{action3_competitor_example}

#### 5ステップ実装手順

**STEP 1: 現状分析**
{action3_step1_analysis}

**STEP 2: 目標設定**
{action3_step2_goal}

**STEP 3: 実施**
{action3_step3_implementation}

**プラットフォーム固有の注意事項**:
{action3_platform_notes}

**STEP 4: 測定**
{action3_step4_measurement}

**STEP 5: 調整**
{action3_step5_adjustment}

---

### 📍 アクション4: {action4_title}

**期待効果**: {action4_expected_effect}
**優先度**: {action4_priority}/100
**エビデンス強度**: {action4_evidence_score}/100

#### 📊 根拠とエビデンス

**内部データ分析**:
{action4_internal_data}

**業界ベストプラクティス**:
- 参照: {action4_best_practice_ref}
- {action4_best_practice_quote}

**最新トレンド**（2026年1月）:
{action4_trend_insight}

**競合成功事例**:
{action4_competitor_example}

#### 5ステップ実装手順

**STEP 1: 現状分析**
{action4_step1_analysis}

**STEP 2: 目標設定**
{action4_step2_goal}

**STEP 3: 実施**
{action4_step3_implementation}

**プラットフォーム固有の注意事項**:
{action4_platform_notes}

**STEP 4: 測定**
{action4_step4_measurement}

**STEP 5: 調整**
{action4_step5_adjustment}

---

### 📍 アクション5: {action5_title}

**期待効果**: {action5_expected_effect}
**優先度**: {action5_priority}/100
**エビデンス強度**: {action5_evidence_score}/100

#### 📊 根拠とエビデンス

**内部データ分析**:
{action5_internal_data}

**業界ベストプラクティス**:
- 参照: {action5_best_practice_ref}
- {action5_best_practice_quote}

**最新トレンド**（2026年1月）:
{action5_trend_insight}

**競合成功事例**:
{action5_competitor_example}

#### 5ステップ実装手順

**STEP 1: 現状分析**
{action5_step1_analysis}

**STEP 2: 目標設定**
{action5_step2_goal}

**STEP 3: 実施**
{action5_step3_implementation}

**プラットフォーム固有の注意事項**:
{action5_platform_notes}

**STEP 4: 測定**
{action5_step4_measurement}

**STEP 5: 調整**
{action5_step5_adjustment}

---

### 📍 アクション6: {action6_title}

**期待効果**: {action6_expected_effect}
**優先度**: {action6_priority}/100
**エビデンス強度**: {action6_evidence_score}/100

#### 📊 根拠とエビデンス

**内部データ分析**:
{action6_internal_data}

**業界ベストプラクティス**:
- 参照: {action6_best_practice_ref}
- {action6_best_practice_quote}

**最新トレンド**（2026年1月）:
{action6_trend_insight}

**競合成功事例**:
{action6_competitor_example}

#### 5ステップ実装手順

**STEP 1: 現状分析**
{action6_step1_analysis}

**STEP 2: 目標設定**
{action6_step2_goal}

**STEP 3: 実施**
{action6_step3_implementation}

**プラットフォーム固有の注意事項**:
{action6_platform_notes}

**STEP 4: 測定**
{action6_step4_measurement}

**STEP 5: 調整**
{action6_step5_adjustment}

---

### 📍 アクション7: {action7_title}

**期待効果**: {action7_expected_effect}
**優先度**: {action7_priority}/100
**エビデンス強度**: {action7_evidence_score}/100

#### 📊 根拠とエビデンス

**内部データ分析**:
{action7_internal_data}

**業界ベストプラクティス**:
- 参照: {action7_best_practice_ref}
- {action7_best_practice_quote}

**最新トレンド**（2026年1月）:
{action7_trend_insight}

**競合成功事例**:
{action7_competitor_example}

#### 5ステップ実装手順

**STEP 1: 現状分析**
{action7_step1_analysis}

**STEP 2: 目標設定**
{action7_step2_goal}

**STEP 3: 実施**
{action7_step3_implementation}

**プラットフォーム固有の注意事項**:
{action7_platform_notes}

**STEP 4: 測定**
{action7_step4_measurement}

**STEP 5: 調整**
{action7_step5_adjustment}

---

### 📍 アクション8: {action8_title}

**期待効果**: {action8_expected_effect}
**優先度**: {action8_priority}/100
**エビデンス強度**: {action8_evidence_score}/100

#### 📊 根拠とエビデンス

**内部データ分析**:
{action8_internal_data}

**業界ベストプラクティス**:
- 参照: {action8_best_practice_ref}
- {action8_best_practice_quote}

**最新トレンド**（2026年1月）:
{action8_trend_insight}

**競合成功事例**:
{action8_competitor_example}

#### 5ステップ実装手順

**STEP 1: 現状分析**
{action8_step1_analysis}

**STEP 2: 目標設定**
{action8_step2_goal}

**STEP 3: 実施**
{action8_step3_implementation}

**プラットフォーム固有の注意事項**:
{action8_platform_notes}

**STEP 4: 測定**
{action8_step4_measurement}

**STEP 5: 調整**
{action8_step5_adjustment}

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
