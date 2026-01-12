#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LinkedIn日次エンゲージメント率分析

データソース: linkedin_エンゲージメント.csv
分析内容:
1. 日次ER計算
2. 月別ER平均・トレンド
3. 週別パターン分析
4. 高ER日と低ER日の特徴比較
5. ERの変動要因分析
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime

def analyze_linkedin_daily_engagement(csv_path: str) -> dict:
    """LinkedIn日次エンゲージメント率の詳細分析"""

    df = pd.read_csv(csv_path, encoding='utf-8-sig')

    # 列名を正規化
    df.columns = ['date', 'impressions', 'engagements']

    # 日付変換
    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d', errors='coerce')

    # NaN除外
    df = df.dropna(subset=['date', 'impressions', 'engagements'])

    # ER計算（%）
    df['er_pct'] = (df['engagements'] / df['impressions'] * 100).round(2)

    # 負のエンゲージメント（異常値）を除外
    df = df[df['engagements'] >= 0]

    # 月・週・曜日を追加
    df['month'] = df['date'].dt.to_period('M').astype(str)
    df['week'] = df['date'].dt.to_period('W').astype(str)
    df['weekday'] = df['date'].dt.day_name()
    df['day_of_week'] = df['date'].dt.dayofweek  # 0=Monday, 6=Sunday

    # 1. 全体統計
    overall_stats = {
        'total_days': len(df),
        'date_range': {
            'start': df['date'].min().strftime('%Y-%m-%d'),
            'end': df['date'].max().strftime('%Y-%m-%d')
        },
        'total_impressions': int(df['impressions'].sum()),
        'total_engagements': int(df['engagements'].sum()),
        'overall_er': round(df['engagements'].sum() / df['impressions'].sum() * 100, 2),
        'daily_avg': {
            'impressions': round(df['impressions'].mean(), 1),
            'engagements': round(df['engagements'].mean(), 1),
            'er': round(df['er_pct'].mean(), 2)
        },
        'daily_median': {
            'impressions': int(df['impressions'].median()),
            'engagements': int(df['engagements'].median()),
            'er': round(df['er_pct'].median(), 2)
        },
        'er_range': {
            'min': round(df['er_pct'].min(), 2),
            'max': round(df['er_pct'].max(), 2)
        }
    }

    # 2. 月別トレンド
    monthly_stats = df.groupby('month').agg({
        'impressions': ['sum', 'mean'],
        'engagements': ['sum', 'mean'],
        'er_pct': 'mean',
        'date': 'count'
    }).round(2)

    monthly_trends = {}
    for month in monthly_stats.index:
        monthly_trends[month] = {
            'days': int(monthly_stats.loc[month, ('date', 'count')]),
            'total_impressions': int(monthly_stats.loc[month, ('impressions', 'sum')]),
            'avg_impressions': round(monthly_stats.loc[month, ('impressions', 'mean')], 1),
            'total_engagements': int(monthly_stats.loc[month, ('engagements', 'sum')]),
            'avg_engagements': round(monthly_stats.loc[month, ('engagements', 'mean')], 1),
            'avg_er': round(monthly_stats.loc[month, ('er_pct', 'mean')], 2)
        }

    # 3. 曜日別パターン
    weekday_stats = df.groupby('weekday').agg({
        'impressions': 'mean',
        'engagements': 'mean',
        'er_pct': 'mean',
        'date': 'count'
    }).round(2)

    # 曜日順序を定義
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_patterns = {}
    for day in weekday_order:
        if day in weekday_stats.index:
            weekday_patterns[day] = {
                'days_count': int(weekday_stats.loc[day, 'date']),
                'avg_impressions': round(weekday_stats.loc[day, 'impressions'], 1),
                'avg_engagements': round(weekday_stats.loc[day, 'engagements'], 1),
                'avg_er': round(weekday_stats.loc[day, 'er_pct'], 2)
            }

    # 4. Top 10 vs Bottom 10 日（ER基準）
    top_10_days = df.nlargest(10, 'er_pct')
    bottom_10_days = df.nsmallest(10, 'er_pct')

    top_bottom_comparison = {
        'top_10': {
            'avg_er': round(top_10_days['er_pct'].mean(), 2),
            'avg_impressions': round(top_10_days['impressions'].mean(), 1),
            'avg_engagements': round(top_10_days['engagements'].mean(), 1),
            'dates': top_10_days[['date', 'er_pct', 'impressions', 'engagements']].to_dict('records')
        },
        'bottom_10': {
            'avg_er': round(bottom_10_days['er_pct'].mean(), 2),
            'avg_impressions': round(bottom_10_days['impressions'].mean(), 1),
            'avg_engagements': round(bottom_10_days['engagements'].mean(), 1),
            'dates': bottom_10_days[['date', 'er_pct', 'impressions', 'engagements']].to_dict('records')
        }
    }

    # 日付をフォーマット
    for item in top_bottom_comparison['top_10']['dates']:
        item['date'] = item['date'].strftime('%Y-%m-%d')
    for item in top_bottom_comparison['bottom_10']['dates']:
        item['date'] = item['date'].strftime('%Y-%m-%d')

    # 5. インプレッション vs ER の相関
    median_imp = df['impressions'].median()
    high_imp_days = df[df['impressions'] > median_imp]
    low_imp_days = df[df['impressions'] <= median_imp]

    imp_er_correlation = {
        'high_impressions_days': {
            'count': len(high_imp_days),
            'avg_impressions': round(high_imp_days['impressions'].mean(), 1),
            'avg_er': round(high_imp_days['er_pct'].mean(), 2)
        },
        'low_impressions_days': {
            'count': len(low_imp_days),
            'avg_impressions': round(low_imp_days['impressions'].mean(), 1),
            'avg_er': round(low_imp_days['er_pct'].mean(), 2)
        }
    }

    # 6. ER分布
    er_distribution = {
        'under_1pct': len(df[df['er_pct'] < 1.0]),
        '1_2pct': len(df[(df['er_pct'] >= 1.0) & (df['er_pct'] < 2.0)]),
        '2_3pct': len(df[(df['er_pct'] >= 2.0) & (df['er_pct'] < 3.0)]),
        '3_4pct': len(df[(df['er_pct'] >= 3.0) & (df['er_pct'] < 4.0)]),
        '4_5pct': len(df[(df['er_pct'] >= 4.0) & (df['er_pct'] < 5.0)]),
        '5_6pct': len(df[(df['er_pct'] >= 5.0) & (df['er_pct'] < 6.0)]),
        'over_6pct': len(df[df['er_pct'] >= 6.0])
    }

    # 7. 12月詳細分析（Imp減少の原因調査）
    dec_days = df[df['month'] == '2025-12']
    nov_days = df[df['month'] == '2025-11']
    oct_days = df[df['month'] == '2025-10']

    december_analysis = {
        'december': {
            'days': len(dec_days),
            'avg_er': round(dec_days['er_pct'].mean(), 2) if len(dec_days) > 0 else 0,
            'avg_impressions': round(dec_days['impressions'].mean(), 1) if len(dec_days) > 0 else 0,
            'total_impressions': int(dec_days['impressions'].sum()) if len(dec_days) > 0 else 0
        },
        'november': {
            'days': len(nov_days),
            'avg_er': round(nov_days['er_pct'].mean(), 2) if len(nov_days) > 0 else 0,
            'avg_impressions': round(nov_days['impressions'].mean(), 1) if len(nov_days) > 0 else 0,
            'total_impressions': int(nov_days['impressions'].sum()) if len(nov_days) > 0 else 0
        },
        'october': {
            'days': len(oct_days),
            'avg_er': round(oct_days['er_pct'].mean(), 2) if len(oct_days) > 0 else 0,
            'avg_impressions': round(oct_days['impressions'].mean(), 1) if len(oct_days) > 0 else 0,
            'total_impressions': int(oct_days['impressions'].sum()) if len(oct_days) > 0 else 0
        }
    }

    return {
        'data_source': 'linkedin_エンゲージメント.csv（日次データ）',
        'overall_stats': overall_stats,
        'monthly_trends': monthly_trends,
        'weekday_patterns': weekday_patterns,
        'top_bottom_comparison': top_bottom_comparison,
        'imp_er_correlation': imp_er_correlation,
        'er_distribution': er_distribution,
        'december_analysis': december_analysis,
        'benchmark_takano': {
            'er_range': '4-6%',
            'user_overall_er': overall_stats['overall_er'],
            'gap': overall_stats['overall_er'] - 5.0
        }
    }

if __name__ == '__main__':
    csv_path = '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/LinkedIn/linkedin_エンゲージメント.csv'

    result = analyze_linkedin_daily_engagement(csv_path)

    print("=" * 80)
    print("LinkedIn日次エンゲージメント率分析レポート")
    print("=" * 80)
    print()

    print(f"データソース: {result['data_source']}")
    print()

    print("【1. 全体統計】")
    print("-" * 80)
    os = result['overall_stats']
    print(f"分析期間: {os['date_range']['start']} ~ {os['date_range']['end']} ({os['total_days']}日間)")
    print(f"総インプレッション: {os['total_impressions']:,}")
    print(f"総エンゲージメント: {os['total_engagements']:,}")
    print(f"**全体ER: {os['overall_er']:.2f}%**")
    print()
    print(f"日次平均:")
    print(f"  - インプレッション: {os['daily_avg']['impressions']:,.1f}")
    print(f"  - エンゲージメント: {os['daily_avg']['engagements']:.1f}")
    print(f"  - ER: {os['daily_avg']['er']:.2f}%")
    print()
    print(f"日次中央値:")
    print(f"  - インプレッション: {os['daily_median']['impressions']:,}")
    print(f"  - エンゲージメント: {os['daily_median']['engagements']}")
    print(f"  - ER: {os['daily_median']['er']:.2f}%")
    print()
    print(f"ER範囲: {os['er_range']['min']:.2f}% ~ {os['er_range']['max']:.2f}%")
    print()
    print(f"高野氏ベンチマーク ER: {result['benchmark_takano']['er_range']}")
    print(f"ギャップ: {result['benchmark_takano']['gap']:.2f}ポイント")
    print()

    print("【2. 月別トレンド】")
    print("-" * 80)
    for month, stats in result['monthly_trends'].items():
        print(f"{month}: {stats['days']}日間")
        print(f"  - 平均ER: {stats['avg_er']:.2f}%")
        print(f"  - 平均Imp: {stats['avg_impressions']:,.1f}")
        print(f"  - 総Imp: {stats['total_impressions']:,}")
        print(f"  - 平均Eng: {stats['avg_engagements']:.1f}")
        print()

    print("【3. 12月詳細分析（Imp減少原因調査）】")
    print("-" * 80)
    dec_analysis = result['december_analysis']
    print(f"10月: {dec_analysis['october']['days']}日間、平均ER {dec_analysis['october']['avg_er']:.2f}%、平均Imp {dec_analysis['october']['avg_impressions']:,.1f}")
    print(f"11月: {dec_analysis['november']['days']}日間、平均ER {dec_analysis['november']['avg_er']:.2f}%、平均Imp {dec_analysis['november']['avg_impressions']:,.1f}")
    print(f"12月: {dec_analysis['december']['days']}日間、平均ER {dec_analysis['december']['avg_er']:.2f}%、平均Imp {dec_analysis['december']['avg_impressions']:,.1f}")
    print()

    if dec_analysis['december']['days'] > 0 and dec_analysis['november']['days'] > 0:
        er_change = dec_analysis['december']['avg_er'] - dec_analysis['november']['avg_er']
        imp_change_pct = (dec_analysis['december']['avg_impressions'] / dec_analysis['november']['avg_impressions'] - 1) * 100
        print(f"11月→12月変化:")
        print(f"  - ER: {er_change:+.2f}ポイント")
        print(f"  - Imp: {imp_change_pct:+.1f}%")
        print()

    print("【4. 曜日別パターン】")
    print("-" * 80)
    for day, stats in result['weekday_patterns'].items():
        print(f"{day}: {stats['days_count']}日、平均ER {stats['avg_er']:.2f}%、平均Imp {stats['avg_impressions']:,.1f}")
    print()

    print("【5. ER分布】")
    print("-" * 80)
    erd = result['er_distribution']
    total = sum(erd.values())
    for range_name, count in erd.items():
        pct = count / total * 100 if total > 0 else 0
        print(f"{range_name}: {count}日 ({pct:.1f}%)")
    print()
    benchmark_4_6 = erd.get('4_5pct', 0) + erd.get('5_6pct', 0) + erd.get('over_6pct', 0)
    print(f"高野氏ベンチマーク範囲（4-6%以上）: {benchmark_4_6}日 ({benchmark_4_6/total*100:.1f}%)")
    print()

    print("【6. Top 10 vs Bottom 10 日（ER基準）】")
    print("-" * 80)
    tbc = result['top_bottom_comparison']
    print(f"Top 10平均ER: {tbc['top_10']['avg_er']:.2f}%")
    print(f"  - 平均Imp: {tbc['top_10']['avg_impressions']:,.1f}")
    print(f"  - 平均Eng: {tbc['top_10']['avg_engagements']:.1f}")
    print()
    print(f"Bottom 10平均ER: {tbc['bottom_10']['avg_er']:.2f}%")
    print(f"  - 平均Imp: {tbc['bottom_10']['avg_impressions']:,.1f}")
    print(f"  - 平均Eng: {tbc['bottom_10']['avg_engagements']:.1f}")
    print()

    print("【7. インプレッション vs ER の関係】")
    print("-" * 80)
    iec = result['imp_er_correlation']
    print(f"高Imp日（中央値以上）: {iec['high_impressions_days']['count']}日、平均ER {iec['high_impressions_days']['avg_er']:.2f}%")
    print(f"低Imp日（中央値未満）: {iec['low_impressions_days']['count']}日、平均ER {iec['low_impressions_days']['avg_er']:.2f}%")
    print()

    # JSON出力
    output_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/LinkedIn/linkedin_daily_engagement_analysis.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=str)

    print(f"詳細結果をJSONで保存: {output_path}")
