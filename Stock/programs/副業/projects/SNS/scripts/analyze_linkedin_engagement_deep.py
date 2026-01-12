#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn総合エンゲージメント分析（Option B: 追加の課題深掘り）

データソース統合:
1. linkedin-2026-01-01.csv - 投稿本文（文字数、パターン、問いかけ終結）
2. linkedin_人気の投稿.csv - Top 50投稿のエンゲージメント＆インプレッション
3. linkedin_エンゲージメント.csv - 日次総合エンゲージメント
4. linkedin_フォロワー.csv - フォロワー成長
5. linkedin_統計データ.csv - オーディエンス属性

⚠️ データ制約:
- LinkedInエクスポートには、コメント・シェア・保存の個別内訳が含まれない
- 利用可能なのは総エンゲージメント数（いいね+コメント+シェア+その他）のみ
"""

import pandas as pd
import json
import re
from pathlib import Path
from datetime import datetime

def load_post_text_analysis(csv_path: str) -> dict:
    """投稿本文分析結果の読み込み"""
    df = pd.read_csv(csv_path, encoding='utf-8-sig')

    posts = {}
    content_col = 'media-description'
    url_col = 'content-link href'

    for idx, row in df.iterrows():
        url = str(row[url_col]) if url_col in df.columns else None
        if url and pd.notna(url):
            # URLから投稿IDを抽出
            match = re.search(r'activity:(\d+)', url)
            post_id = match.group(1) if match else None

            if post_id:
                text = str(row[content_col])
                if pd.notna(text) and text != 'nan':
                    char_count = len(text)
                    has_question = check_question_ending(text)
                    pattern = classify_pattern(text)
                    company_count = count_company_mentions(text)

                    posts[post_id] = {
                        'url': url,
                        'char_count': char_count,
                        'has_question': has_question,
                        'pattern': pattern,
                        'company_mentions': company_count,
                        'text_preview': text[:100]
                    }

    return posts

def classify_pattern(text: str) -> str:
    """パターン分類（既存ロジックを再利用）"""
    if re.search(r'(氏は|氏が|氏によれば|によると|報道によると|発表|述べた|明らかにした|断言した|提唱する|指摘する)', text[:150]):
        return 'Pattern 3: ニュース引用型'
    if '【告知】' in text or 'イベント' in text[:50]:
        return 'Pattern 5: イベント型'
    if re.search(r'(である|だ|でした)。', text[:200]):
        return 'Pattern 1: 断定型'
    num_count = len(re.findall(r'\d+,?\d*', text))
    if num_count >= 5:
        return 'Pattern 4: リスト型・衝撃ファクト'
    return 'その他'

def check_question_ending(text: str) -> bool:
    """問いかけ終結チェック"""
    ending = text[-100:]
    question_patterns = [
        r'か？', r'でしょうか', r'ますか', r'ませんか',
        r'のでは', r'だろうか', r'はいかが', r'どう思いますか',
        r'いかがでしょうか', r'ではないか', r'のではないか'
    ]
    return any(re.search(pattern, ending) for pattern in question_patterns)

def count_company_mentions(text: str) -> int:
    """企業名引用数カウント"""
    company_patterns = [
        r'OpenAI', r'Google|グーグル', r'Microsoft|マイクロソフト',
        r'Tesla|テスラ', r'Anthropic|アンソロッピック', r'Meta',
        r'Apple', r'Amazon', r'NVIDIA|エヌビディア',
        r'Alibaba|アリババ', r'DeepSeek|ディープシーク',
        r'Gemini', r'ChatGPT', r'Claude', r'セコイア',
        r'ゴールドマン', r'a16z|A16z', r'ソフトバンク',
        r'Walmart|ウォルマート', r'エポックAI|Epoch AI',
        r'スペースX|SpaceX', r'LayerX|レイヤーエックス',
        r'トランスコスモス', r'DeepMind|ディープマインド', r'バクラク'
    ]

    count = 0
    for pattern in company_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        count += len(matches)

    return count

def load_popular_posts(csv_path: str) -> pd.DataFrame:
    """人気の投稿データ読み込み"""
    df = pd.read_csv(csv_path, encoding='utf-8-sig')

    # ヘッダー行を特定（row 3）
    df_engagement = df.iloc[3:, [0, 1, 2]].copy()
    df_engagement.columns = ['url', 'date', 'engagement']

    df_impressions = df.iloc[3:, [4, 5, 6]].copy()
    df_impressions.columns = ['url', 'date', 'impressions']

    # NaNを除外
    df_engagement = df_engagement.dropna(subset=['url'])
    df_impressions = df_impressions.dropna(subset=['url'])

    # マージ
    df_combined = pd.merge(df_engagement, df_impressions, on='url', how='outer', suffixes=('_eng', '_imp'))

    # 投稿IDを抽出
    df_combined['post_id'] = df_combined['url'].str.extract(r'activity:(\d+)')

    # 数値変換
    df_combined['engagement'] = pd.to_numeric(df_combined['engagement'], errors='coerce')
    df_combined['impressions'] = pd.to_numeric(df_combined['impressions'], errors='coerce')

    # ER計算
    df_combined['er_pct'] = (df_combined['engagement'] / df_combined['impressions'] * 100).round(2)

    return df_combined

def analyze_linkedin_deep(
    post_text_csv: str,
    popular_posts_csv: str,
    engagement_csv: str,
    follower_csv: str,
    stats_csv: str
) -> dict:
    """LinkedIn総合エンゲージメント深掘り分析"""

    # 1. 投稿本文分析読み込み
    posts_text = load_post_text_analysis(post_text_csv)

    # 2. 人気投稿データ読み込み
    popular_df = load_popular_posts(popular_posts_csv)

    # 3. 投稿本文とエンゲージメントデータを統合
    enriched_posts = []
    for idx, row in popular_df.iterrows():
        post_id = row['post_id']
        if pd.notna(post_id) and post_id in posts_text:
            post_data = {
                'post_id': post_id,
                'url': row['url'],
                'impressions': row['impressions'],
                'engagement': row['engagement'],
                'er_pct': row['er_pct'],
                **posts_text[post_id]
            }
            enriched_posts.append(post_data)

    enriched_df = pd.DataFrame(enriched_posts)

    # 4. フォロワーデータ読み込み
    follower_df = pd.read_csv(follower_csv, encoding='utf-8-sig', skiprows=2)
    total_followers = 32056  # CSVの1行目に記載

    # 5. オーディエンス属性
    stats_df = pd.read_csv(stats_csv, encoding='utf-8-sig')

    # 6. 分析実行

    # 6.1 問いかけ終結率とERの相関
    if len(enriched_df) > 0:
        question_yes = enriched_df[enriched_df['has_question'] == True]
        question_no = enriched_df[enriched_df['has_question'] == False]

        question_analysis = {
            'with_question': {
                'count': len(question_yes),
                'avg_er': question_yes['er_pct'].mean() if len(question_yes) > 0 else 0,
                'avg_impressions': question_yes['impressions'].mean() if len(question_yes) > 0 else 0
            },
            'without_question': {
                'count': len(question_no),
                'avg_er': question_no['er_pct'].mean() if len(question_no) > 0 else 0,
                'avg_impressions': question_no['impressions'].mean() if len(question_no) > 0 else 0
            }
        }
    else:
        question_analysis = {}

    # 6.2 文字数とERの相関
    if len(enriched_df) > 0:
        char_count_bins = {
            'under_500': enriched_df[enriched_df['char_count'] < 500],
            '500_700': enriched_df[(enriched_df['char_count'] >= 500) & (enriched_df['char_count'] < 700)],
            '700_900': enriched_df[(enriched_df['char_count'] >= 700) & (enriched_df['char_count'] < 900)],
            'over_900': enriched_df[enriched_df['char_count'] >= 900]
        }

        char_count_analysis = {}
        for range_name, subset in char_count_bins.items():
            if len(subset) > 0:
                char_count_analysis[range_name] = {
                    'count': len(subset),
                    'avg_er': subset['er_pct'].mean(),
                    'avg_impressions': subset['impressions'].mean()
                }
    else:
        char_count_analysis = {}

    # 6.3 パターン別ER
    if len(enriched_df) > 0:
        pattern_analysis = {}
        for pattern in enriched_df['pattern'].unique():
            subset = enriched_df[enriched_df['pattern'] == pattern]
            pattern_analysis[pattern] = {
                'count': len(subset),
                'avg_er': subset['er_pct'].mean(),
                'avg_impressions': subset['impressions'].mean()
            }
    else:
        pattern_analysis = {}

    # 6.4 Top 10 vs Bottom 10 比較
    if len(enriched_df) >= 20:
        top_10 = enriched_df.nlargest(10, 'er_pct')
        bottom_10 = enriched_df.nsmallest(10, 'er_pct')

        top_bottom_comparison = {
            'top_10': {
                'avg_er': top_10['er_pct'].mean(),
                'avg_char_count': top_10['char_count'].mean(),
                'question_rate': (top_10['has_question'].sum() / len(top_10) * 100),
                'avg_company_mentions': top_10['company_mentions'].mean()
            },
            'bottom_10': {
                'avg_er': bottom_10['er_pct'].mean(),
                'avg_char_count': bottom_10['char_count'].mean(),
                'question_rate': (bottom_10['has_question'].sum() / len(bottom_10) * 100),
                'avg_company_mentions': bottom_10['company_mentions'].mean()
            }
        }
    else:
        top_bottom_comparison = {}

    # 6.5 フォロワー成長トレンド
    follower_growth = {
        'total_followers': total_followers,
        'daily_growth_avg': follower_df['新規フォロワー'].mean() if '新規フォロワー' in follower_df.columns else 0,
        'daily_growth_median': follower_df['新規フォロワー'].median() if '新規フォロワー' in follower_df.columns else 0
    }

    # 6.6 オーディエンス属性（CEO比率）
    ceo_row = stats_df[stats_df['値'] == 'CEO']
    ceo_pct = float(ceo_row['パーセンテージ'].values[0]) * 100 if len(ceo_row) > 0 else 0

    audience_stats = {
        'ceo_percentage': round(ceo_pct, 2),
        'top_job_titles': stats_df.head(10).to_dict('records') if len(stats_df) > 0 else []
    }

    # 7. 総合結果
    return {
        'data_constraint_note': 'LinkedInエクスポートにはコメント・シェア・保存の個別内訳が含まれない。総エンゲージメント数のみ利用可能。',
        'total_posts_analyzed': len(enriched_df),
        'overall_metrics': {
            'avg_er': enriched_df['er_pct'].mean() if len(enriched_df) > 0 else 0,
            'median_er': enriched_df['er_pct'].median() if len(enriched_df) > 0 else 0,
            'avg_impressions': enriched_df['impressions'].mean() if len(enriched_df) > 0 else 0,
            'avg_engagement': enriched_df['engagement'].mean() if len(enriched_df) > 0 else 0
        },
        'question_ending_correlation': question_analysis,
        'char_count_correlation': char_count_analysis,
        'pattern_performance': pattern_analysis,
        'top_bottom_comparison': top_bottom_comparison,
        'follower_growth': follower_growth,
        'audience_stats': audience_stats,
        'top_10_posts': enriched_df.nlargest(10, 'er_pct')[['url', 'er_pct', 'impressions', 'engagement', 'char_count', 'has_question', 'pattern']].to_dict('records') if len(enriched_df) >= 10 else [],
        'benchmark_takano': {
            'er_range': '4-6%',
            'char_count_avg': 760.1,
            'question_ending_rate': '80%+',
            'company_mentions_avg': 1.58
        }
    }

if __name__ == '__main__':
    base_dir = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS')

    post_text_csv = base_dir / 'X' / 'linkedin-2026-01-01.csv'
    popular_posts_csv = base_dir / 'LinkedIn' / 'linkedin_人気の投稿.csv'
    engagement_csv = base_dir / 'LinkedIn' / 'linkedin_エンゲージメント.csv'
    follower_csv = base_dir / 'LinkedIn' / 'linkedin_フォロワー.csv'
    stats_csv = base_dir / 'LinkedIn' / 'linkedin_統計データ.csv'

    result = analyze_linkedin_deep(
        str(post_text_csv),
        str(popular_posts_csv),
        str(engagement_csv),
        str(follower_csv),
        str(stats_csv)
    )

    # 結果表示
    print("=" * 80)
    print("LinkedIn総合エンゲージメント深掘り分析レポート（Option B）")
    print("=" * 80)
    print()

    print(f"⚠️  {result['data_constraint_note']}")
    print()

    print(f"分析対象投稿数: {result['total_posts_analyzed']}投稿")
    print()

    print("【1. 全体メトリクス】")
    print("-" * 80)
    om = result['overall_metrics']
    print(f"平均ER: {om['avg_er']:.2f}%")
    print(f"中央値ER: {om['median_er']:.2f}%")
    print(f"平均インプレッション: {om['avg_impressions']:,.0f}")
    print(f"平均エンゲージメント: {om['avg_engagement']:.0f}")
    print()
    print(f"高野氏ベンチマーク ER: {result['benchmark_takano']['er_range']}")
    print()

    if result['question_ending_correlation']:
        print("【2. 問いかけ終結率とERの相関】")
        print("-" * 80)
        qac = result['question_ending_correlation']
        print(f"問いかけあり: {qac['with_question']['count']}投稿、平均ER {qac['with_question']['avg_er']:.2f}%")
        print(f"問いかけなし: {qac['without_question']['count']}投稿、平均ER {qac['without_question']['avg_er']:.2f}%")

        if qac['with_question']['count'] > 0 and qac['without_question']['count'] > 0:
            er_diff = qac['with_question']['avg_er'] - qac['without_question']['avg_er']
            print(f"差分: {er_diff:+.2f}ポイント")
        print()

    if result['char_count_correlation']:
        print("【3. 文字数とERの相関】")
        print("-" * 80)
        for range_name, data in result['char_count_correlation'].items():
            print(f"{range_name}: {data['count']}投稿、平均ER {data['avg_er']:.2f}%")
        print()

    if result['pattern_performance']:
        print("【4. パターン別パフォーマンス】")
        print("-" * 80)
        for pattern, data in sorted(result['pattern_performance'].items(), key=lambda x: x[1]['avg_er'], reverse=True):
            print(f"{pattern}: {data['count']}投稿、平均ER {data['avg_er']:.2f}%")
        print()

    if result['top_bottom_comparison']:
        print("【5. Top 10 vs Bottom 10 比較】")
        print("-" * 80)
        tbc = result['top_bottom_comparison']
        print(f"Top 10平均ER: {tbc['top_10']['avg_er']:.2f}%")
        print(f"  - 平均文字数: {tbc['top_10']['avg_char_count']:.0f}字")
        print(f"  - 問いかけ率: {tbc['top_10']['question_rate']:.0f}%")
        print(f"  - 平均企業名: {tbc['top_10']['avg_company_mentions']:.1f}社")
        print()
        print(f"Bottom 10平均ER: {tbc['bottom_10']['avg_er']:.2f}%")
        print(f"  - 平均文字数: {tbc['bottom_10']['avg_char_count']:.0f}字")
        print(f"  - 問いかけ率: {tbc['bottom_10']['question_rate']:.0f}%")
        print(f"  - 平均企業名: {tbc['bottom_10']['avg_company_mentions']:.1f}社")
        print()

    print("【6. フォロワー成長】")
    print("-" * 80)
    fg = result['follower_growth']
    print(f"総フォロワー数: {fg['total_followers']:,}人")
    print(f"日次成長平均: {fg['daily_growth_avg']:.1f}人/日")
    print(f"日次成長中央値: {fg['daily_growth_median']:.0f}人/日")
    print()

    print("【7. オーディエンス属性】")
    print("-" * 80)
    aus = result['audience_stats']
    print(f"CEO比率: {aus['ceo_percentage']:.2f}%")
    print()

    # JSON出力
    output_path = base_dir / 'LinkedIn' / 'linkedin_engagement_deep_analysis.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"詳細結果をJSONで保存: {output_path}")
