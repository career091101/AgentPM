#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn人気投稿分析（データ制約下での最大限の分析）

データ制約:
- 投稿本文CSVにはURLが含まれていない（マッチング不可）
- コメント・シェア・保存の個別内訳なし（総エンゲージメントのみ）

分析可能項目:
1. エンゲージメント率（ER）の分布と統計
2. インプレッション vs エンゲージメントの相関
3. Top/Bottom投稿の特性比較
4. 日付別トレンド
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime

def analyze_linkedin_popular_posts(csv_path: str) -> dict:
    """人気投稿データから最大限の分析を実施"""

    df = pd.read_csv(csv_path, encoding='utf-8-sig')

    # ヘッダー行を特定（row 3）
    df_engagement = df.iloc[3:, [0, 1, 2]].copy()
    df_engagement.columns = ['url', 'date_eng', 'engagement']

    df_impressions = df.iloc[3:, [4, 5, 6]].copy()
    df_impressions.columns = ['url_imp', 'date_imp', 'impressions']

    # NaNを除外
    df_engagement = df_engagement.dropna(subset=['url'])
    df_impressions = df_impressions.dropna(subset=['url_imp'])

    # マージ
    df_combined = pd.merge(
        df_engagement,
        df_impressions,
        left_on='url',
        right_on='url_imp',
        how='outer'
    )

    # 数値変換
    df_combined['engagement'] = pd.to_numeric(df_combined['engagement'], errors='coerce')
    df_combined['impressions'] = pd.to_numeric(df_combined['impressions'], errors='coerce')

    # NaN除外
    df_combined = df_combined.dropna(subset=['engagement', 'impressions'])

    # ER計算
    df_combined['er_pct'] = (df_combined['engagement'] / df_combined['impressions'] * 100).round(2)

    # 投稿IDを抽出
    df_combined['post_id'] = df_combined['url'].str.extract(r'activity:(\d+)')

    # 日付処理
    df_combined['date'] = pd.to_datetime(df_combined['date_eng'], format='%Y/%m/%d', errors='coerce')

    # 1. 全体統計
    overall_stats = {
        'total_posts': len(df_combined),
        'avg_impressions': df_combined['impressions'].mean(),
        'median_impressions': df_combined['impressions'].median(),
        'avg_engagement': df_combined['engagement'].mean(),
        'median_engagement': df_combined['engagement'].median(),
        'avg_er': df_combined['er_pct'].mean(),
        'median_er': df_combined['er_pct'].median(),
        'min_er': df_combined['er_pct'].min(),
        'max_er': df_combined['er_pct'].max()
    }

    # 2. ER分布
    er_distribution = {
        'under_1pct': len(df_combined[df_combined['er_pct'] < 1.0]),
        '1_2pct': len(df_combined[(df_combined['er_pct'] >= 1.0) & (df_combined['er_pct'] < 2.0)]),
        '2_3pct': len(df_combined[(df_combined['er_pct'] >= 2.0) & (df_combined['er_pct'] < 3.0)]),
        '3_4pct': len(df_combined[(df_combined['er_pct'] >= 3.0) & (df_combined['er_pct'] < 4.0)]),
        '4_5pct': len(df_combined[(df_combined['er_pct'] >= 4.0) & (df_combined['er_pct'] < 5.0)]),
        '5_6pct': len(df_combined[(df_combined['er_pct'] >= 5.0) & (df_combined['er_pct'] < 6.0)]),
        'over_6pct': len(df_combined[df_combined['er_pct'] >= 6.0])
    }

    # 3. Top 10 vs Bottom 10
    top_10_er = df_combined.nlargest(10, 'er_pct')
    bottom_10_er = df_combined.nsmallest(10, 'er_pct')

    top_10_imp = df_combined.nlargest(10, 'impressions')
    bottom_10_imp = df_combined.nsmallest(10, 'impressions')

    top_bottom_comparison = {
        'by_er': {
            'top_10': {
                'avg_er': top_10_er['er_pct'].mean(),
                'avg_impressions': top_10_er['impressions'].mean(),
                'avg_engagement': top_10_er['engagement'].mean(),
                'urls': top_10_er['url'].tolist()
            },
            'bottom_10': {
                'avg_er': bottom_10_er['er_pct'].mean(),
                'avg_impressions': bottom_10_er['impressions'].mean(),
                'avg_engagement': bottom_10_er['engagement'].mean(),
                'urls': bottom_10_er['url'].tolist()
            }
        },
        'by_impressions': {
            'top_10': {
                'avg_er': top_10_imp['er_pct'].mean(),
                'avg_impressions': top_10_imp['impressions'].mean(),
                'avg_engagement': top_10_imp['engagement'].mean()
            },
            'bottom_10': {
                'avg_er': bottom_10_imp['er_pct'].mean(),
                'avg_impressions': bottom_10_imp['impressions'].mean(),
                'avg_engagement': bottom_10_imp['engagement'].mean()
            }
        }
    }

    # 4. 月別トレンド
    df_combined['month'] = df_combined['date'].dt.to_period('M').astype(str)
    monthly_stats = df_combined.groupby('month').agg({
        'impressions': 'mean',
        'engagement': 'mean',
        'er_pct': 'mean',
        'post_id': 'count'
    }).to_dict('index')

    # 5. インプレッション vs ER の逆相関チェック
    # 高インプレッションは低ERになりがちか？
    high_imp = df_combined[df_combined['impressions'] > df_combined['impressions'].median()]
    low_imp = df_combined[df_combined['impressions'] <= df_combined['impressions'].median()]

    impression_er_correlation = {
        'high_impressions': {
            'avg_impressions': high_imp['impressions'].mean(),
            'avg_er': high_imp['er_pct'].mean()
        },
        'low_impressions': {
            'avg_impressions': low_imp['impressions'].mean(),
            'avg_er': low_imp['er_pct'].mean()
        },
        'note': '高インプレッション投稿はERが低い傾向があるか？'
    }

    # 6. 勝ちパターン特定（高ER × 高Imp）
    median_er = df_combined['er_pct'].median()
    median_imp = df_combined['impressions'].median()

    winners = df_combined[
        (df_combined['er_pct'] >= median_er) &
        (df_combined['impressions'] >= median_imp)
    ]

    losers = df_combined[
        (df_combined['er_pct'] < median_er) &
        (df_combined['impressions'] < median_imp)
    ]

    win_loss_analysis = {
        'winners_count': len(winners),
        'winners_avg_er': winners['er_pct'].mean() if len(winners) > 0 else 0,
        'winners_avg_imp': winners['impressions'].mean() if len(winners) > 0 else 0,
        'losers_count': len(losers),
        'losers_avg_er': losers['er_pct'].mean() if len(losers) > 0 else 0,
        'losers_avg_imp': losers['impressions'].mean() if len(losers) > 0 else 0,
        'winner_urls': winners['url'].tolist() if len(winners) > 0 else []
    }

    return {
        'data_source': 'linkedin_人気の投稿.csv（Top 50投稿のみ）',
        'data_constraint': 'コメント・シェア・保存の個別内訳なし。総エンゲージメントのみ。',
        'overall_stats': overall_stats,
        'er_distribution': er_distribution,
        'top_bottom_comparison': top_bottom_comparison,
        'monthly_trends': monthly_stats,
        'impression_er_correlation': impression_er_correlation,
        'win_loss_analysis': win_loss_analysis,
        'benchmark_takano': {
            'er_range': '4-6%',
            'user_avg_er': overall_stats['avg_er'],
            'gap': overall_stats['avg_er'] - 5.0  # 中央値5%との差
        },
        'top_10_posts_by_er': df_combined.nlargest(10, 'er_pct')[['url', 'date_eng', 'er_pct', 'impressions', 'engagement']].to_dict('records')
    }

if __name__ == '__main__':
    csv_path = '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/LinkedIn/linkedin_人気の投稿.csv'

    result = analyze_linkedin_popular_posts(csv_path)

    print("=" * 80)
    print("LinkedIn人気投稿分析レポート（データ制約下の最大限分析）")
    print("=" * 80)
    print()

    print(f"データソース: {result['data_source']}")
    print(f"データ制約: {result['data_constraint']}")
    print()

    print("【1. 全体統計】")
    print("-" * 80)
    os = result['overall_stats']
    print(f"分析対象投稿数: {os['total_posts']}投稿")
    print(f"平均ER: {os['avg_er']:.2f}% （中央値: {os['median_er']:.2f}%）")
    print(f"ER範囲: {os['min_er']:.2f}% ~ {os['max_er']:.2f}%")
    print(f"平均インプレッション: {os['avg_impressions']:,.0f}")
    print(f"平均エンゲージメント: {os['avg_engagement']:.0f}")
    print()
    print(f"高野氏ベンチマーク ER: {result['benchmark_takano']['er_range']}")
    print(f"ギャップ: {result['benchmark_takano']['gap']:.2f}ポイント")
    print()

    print("【2. ER分布】")
    print("-" * 80)
    erd = result['er_distribution']
    total = sum(erd.values())
    for range_name, count in erd.items():
        pct = count / total * 100 if total > 0 else 0
        print(f"{range_name}: {count}投稿 ({pct:.1f}%)")
    print()
    benchmark_4_6 = erd.get('4_5pct', 0) + erd.get('5_6pct', 0) + erd.get('over_6pct', 0)
    print(f"高野氏ベンチマーク範囲（4-6%以上）: {benchmark_4_6}投稿 ({benchmark_4_6/total*100:.1f}%)")
    print()

    print("【3. Top 10 vs Bottom 10（ER基準）】")
    print("-" * 80)
    tbc_er = result['top_bottom_comparison']['by_er']
    print(f"Top 10平均ER: {tbc_er['top_10']['avg_er']:.2f}%")
    print(f"  - 平均インプレッション: {tbc_er['top_10']['avg_impressions']:,.0f}")
    print(f"  - 平均エンゲージメント: {tbc_er['top_10']['avg_engagement']:.0f}")
    print()
    print(f"Bottom 10平均ER: {tbc_er['bottom_10']['avg_er']:.2f}%")
    print(f"  - 平均インプレッション: {tbc_er['bottom_10']['avg_impressions']:,.0f}")
    print(f"  - 平均エンゲージメント: {tbc_er['bottom_10']['avg_engagement']:.0f}")
    print()

    print("【4. インプレッション vs ER の関係】")
    print("-" * 80)
    iec = result['impression_er_correlation']
    print(f"高インプレッション群: 平均ER {iec['high_impressions']['avg_er']:.2f}%")
    print(f"低インプレッション群: 平均ER {iec['low_impressions']['avg_er']:.2f}%")
    print(f"結論: {iec['note']}")
    print()

    print("【5. 勝ちパターン分析（高ER × 高Imp）】")
    print("-" * 80)
    wla = result['win_loss_analysis']
    print(f"勝ち投稿（ER・Imp両方が中央値以上）: {wla['winners_count']}投稿")
    print(f"  - 平均ER: {wla['winners_avg_er']:.2f}%")
    print(f"  - 平均Imp: {wla['winners_avg_imp']:,.0f}")
    print()
    print(f"負け投稿（ER・Imp両方が中央値未満）: {wla['losers_count']}投稿")
    print(f"  - 平均ER: {wla['losers_avg_er']:.2f}%")
    print(f"  - 平均Imp: {wla['losers_avg_imp']:,.0f}")
    print()

    if result['monthly_trends']:
        print("【6. 月別トレンド】")
        print("-" * 80)
        for month, stats in result['monthly_trends'].items():
            print(f"{month}: {stats['post_id']:.0f}投稿、平均ER {stats['er_pct']:.2f}%、平均Imp {stats['impressions']:,.0f}")
        print()

    print("【7. Top 10投稿（ER基準）】")
    print("-" * 80)
    for idx, post in enumerate(result['top_10_posts_by_er'], 1):
        print(f"{idx}. ER {post['er_pct']:.2f}% | Imp {post['impressions']:,.0f} | Eng {post['engagement']:.0f}")
        print(f"   {post['url']}")
        print()

    # JSON出力
    output_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/LinkedIn/linkedin_popular_posts_analysis.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"詳細結果をJSONで保存: {output_path}")
