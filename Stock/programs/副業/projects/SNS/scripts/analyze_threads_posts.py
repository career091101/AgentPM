#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Threads投稿分析スクリプト

目的: Threads過去90日投稿の分析
1. 投稿数・総閲覧数
2. エンゲージメント率分析
3. リポスト/引用の傾向
4. Top 5 / Bottom 5投稿
5. テキスト長と閲覧数の相関
"""

import pandas as pd
import json
from pathlib import Path
from typing import Dict

def analyze_threads_posts(csv_path: str) -> Dict:
    """Threads投稿総合分析"""

    df = pd.read_csv(csv_path, encoding='utf-8-sig')

    if len(df) == 0:
        return {'error': 'データが空です'}

    # 投稿日時をdatetime型に変換
    df['投稿日時'] = pd.to_datetime(df['投稿日時'])
    df['曜日'] = df['投稿日時'].dt.day_name()
    df['時間帯'] = df['投稿日時'].dt.hour
    df['テキスト文字数'] = df['テキスト'].astype(str).str.len()

    # 基本統計
    total_posts = len(df)
    total_views = int(df['閲覧数'].sum())
    avg_views = float(df['閲覧数'].mean())
    median_views = float(df['閲覧数'].median())
    avg_engagement_rate = float(df['エンゲージメント率'].mean())

    # エンゲージメント詳細統計
    avg_likes = float(df['いいね数'].mean())
    avg_replies = float(df['返信数'].mean())
    avg_reposts = float(df['リポスト数'].mean())
    avg_quotes = float(df['引用数'].mean())
    avg_shares = float(df['シェア数'].mean())

    # リポスト/引用率
    repost_rate = (df['リポスト数'].sum() / df['閲覧数'].sum() * 100) if df['閲覧数'].sum() > 0 else 0
    quote_rate = (df['引用数'].sum() / df['閲覧数'].sum() * 100) if df['閲覧数'].sum() > 0 else 0

    # 曜日別分析
    weekday_analysis = {}
    for weekday in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        weekday_df = df[df['曜日'] == weekday]
        if len(weekday_df) > 0:
            weekday_analysis[weekday] = {
                'count': len(weekday_df),
                'avg_views': float(weekday_df['閲覧数'].mean())
            }

    # 時間帯別分析（6時間単位）
    time_slot_analysis = {
        '0-6時': df[(df['時間帯'] >= 0) & (df['時間帯'] < 6)]['閲覧数'].mean(),
        '6-12時': df[(df['時間帯'] >= 6) & (df['時間帯'] < 12)]['閲覧数'].mean(),
        '12-18時': df[(df['時間帯'] >= 12) & (df['時間帯'] < 18)]['閲覧数'].mean(),
        '18-24時': df[(df['時間帯'] >= 18) & (df['時間帯'] < 24)]['閲覧数'].mean()
    }
    # NaNを0に変換
    time_slot_analysis = {k: (float(v) if pd.notna(v) else 0) for k, v in time_slot_analysis.items()}

    # テキスト長との相関
    text_length_correlation = float(df[['テキスト文字数', '閲覧数']].corr().iloc[0, 1])

    # Top 5投稿
    top_5 = df.nlargest(5, '閲覧数')
    top_5_posts = [
        {
            '投稿日時': str(row['投稿日時']),
            '閲覧数': int(row['閲覧数']),
            'エンゲージメント率': float(row['エンゲージメント率']),
            'いいね数': int(row['いいね数']),
            'リポスト数': int(row['リポスト数']),
            '引用数': int(row['引用数']),
            'テキスト文字数': int(row['テキスト文字数']),
            'パーマリンク': row['パーマリンク']
        }
        for _, row in top_5.iterrows()
    ]

    # Bottom 5投稿
    bottom_5 = df.nsmallest(5, '閲覧数')
    bottom_5_posts = [
        {
            '投稿日時': str(row['投稿日時']),
            '閲覧数': int(row['閲覧数']),
            'エンゲージメント率': float(row['エンゲージメント率']),
            'いいね数': int(row['いいね数']),
            'リポスト数': int(row['リポスト数']),
            '引用数': int(row['引用数']),
            'テキスト文字数': int(row['テキスト文字数']),
            'パーマリンク': row['パーマリンク']
        }
        for _, row in bottom_5.iterrows()
    ]

    return {
        'basic_stats': {
            'total_posts': total_posts,
            'total_views': total_views,
            'avg_views': avg_views,
            'median_views': median_views,
            'avg_engagement_rate': avg_engagement_rate,
            'avg_likes': avg_likes,
            'avg_replies': avg_replies,
            'avg_reposts': avg_reposts,
            'avg_quotes': avg_quotes,
            'avg_shares': avg_shares
        },
        'engagement_trends': {
            'repost_rate': float(repost_rate),
            'quote_rate': float(quote_rate)
        },
        'weekday_analysis': weekday_analysis,
        'time_slot_analysis': time_slot_analysis,
        'text_length_correlation': text_length_correlation,
        'top_5_posts': top_5_posts,
        'bottom_5_posts': bottom_5_posts
    }

def main():
    base_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS')

    # 最新のCSVファイルを取得
    threads_dir = base_path / 'Threads'
    csv_files = list(threads_dir.glob('threads_*.csv'))

    if not csv_files:
        print("❌ Threadsデータが見つかりません。先にfetch_threads_data.pyを実行してください。")
        return

    # 最新ファイルを選択
    latest_csv = sorted(csv_files, reverse=True)[0]

    print("=" * 80)
    print("Threads投稿分析レポート")
    print("=" * 80)
    print(f"データソース: {latest_csv.name}")
    print()

    result = analyze_threads_posts(str(latest_csv))

    if 'error' in result:
        print(f"エラー: {result['error']}")
        return

    # 基本統計
    print("【基本統計】")
    print("-" * 80)
    bs = result['basic_stats']
    print(f"総投稿数: {bs['total_posts']}件")
    print(f"総閲覧数: {bs['total_views']:,}")
    print(f"平均閲覧数: {bs['avg_views']:.0f}")
    print(f"中央値: {bs['median_views']:.0f}")
    print(f"平均エンゲージメント率: {bs['avg_engagement_rate']:.2f}%")
    print()
    print(f"平均いいね数: {bs['avg_likes']:.1f}")
    print(f"平均返信数: {bs['avg_replies']:.1f}")
    print(f"平均リポスト数: {bs['avg_reposts']:.1f}")
    print(f"平均引用数: {bs['avg_quotes']:.1f}")
    print(f"平均シェア数: {bs['avg_shares']:.1f}")
    print()

    # エンゲージメント傾向
    print("【エンゲージメント傾向】")
    print("-" * 80)
    et = result['engagement_trends']
    print(f"リポスト率: {et['repost_rate']:.3f}%")
    print(f"引用率: {et['quote_rate']:.3f}%")
    print()

    # 曜日別分析
    print("【曜日別分析】")
    print("-" * 80)
    for weekday, stats in result['weekday_analysis'].items():
        print(f"{weekday}: {stats['count']}件 (平均閲覧数: {stats['avg_views']:.0f})")
    print()

    # 時間帯別分析
    print("【時間帯別分析】")
    print("-" * 80)
    for time_slot, avg_views in result['time_slot_analysis'].items():
        print(f"{time_slot}: 平均閲覧数 {avg_views:.0f}")
    print()

    # テキスト長との相関
    print("【テキスト長との相関】")
    print("-" * 80)
    print(f"相関係数: {result['text_length_correlation']:.3f}")
    print()

    # Top 5投稿
    print("【Top 5投稿】")
    print("-" * 80)
    for i, post in enumerate(result['top_5_posts'], 1):
        print(f"{i}. {post['投稿日時']} - {post['閲覧数']:,} views | ER {post['エンゲージメント率']:.2f}%")
        print(f"   いいね: {post['いいね数']} | リポスト: {post['リポスト数']} | 引用: {post['引用数']}")
        print(f"   テキスト: {post['テキスト文字数']}字")
        print(f"   {post['パーマリンク']}")
        print()

    # Bottom 5投稿
    print("【Bottom 5投稿】")
    print("-" * 80)
    for i, post in enumerate(result['bottom_5_posts'], 1):
        print(f"{i}. {post['投稿日時']} - {post['閲覧数']:,} views | ER {post['エンゲージメント率']:.2f}%")
        print(f"   いいね: {post['いいね数']} | リポスト: {post['リポスト数']} | 引用: {post['引用数']}")
        print(f"   テキスト: {post['テキスト文字数']}字")
        print()

    # JSON出力
    output_path = threads_dir / 'threads_analysis_results.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"💾 詳細結果をJSONで保存: {output_path}")

if __name__ == '__main__':
    main()
