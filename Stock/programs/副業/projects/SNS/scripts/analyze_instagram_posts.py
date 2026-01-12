#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram投稿分析スクリプト

目的: Instagram過去90日投稿の分析
1. 投稿数・総インプレッション
2. メディアタイプ別パフォーマンス
3. エンゲージメント率分析
4. Top 5 / Bottom 5投稿
5. 投稿時間帯分析
6. キャプション文字数との相関
"""

import pandas as pd
import json
from pathlib import Path
from typing import Dict

def analyze_instagram_posts(csv_path: str) -> Dict:
    """Instagram投稿総合分析"""

    df = pd.read_csv(csv_path, encoding='utf-8-sig')

    if len(df) == 0:
        return {'error': 'データが空です'}

    # 投稿日時をdatetime型に変換
    df['投稿日時'] = pd.to_datetime(df['投稿日時'])
    df['曜日'] = df['投稿日時'].dt.day_name()
    df['時間帯'] = df['投稿日時'].dt.hour
    df['キャプション文字数'] = df['キャプション'].astype(str).str.len()

    # 基本統計
    total_posts = len(df)
    total_impressions = int(df['インプレッション数'].sum())
    avg_impressions = float(df['インプレッション数'].mean())
    median_impressions = float(df['インプレッション数'].median())
    avg_engagement_rate = float(df['エンゲージメント率'].mean())

    # メディアタイプ別分析
    media_type_analysis = {}
    for media_type in df['メディアタイプ'].unique():
        type_df = df[df['メディアタイプ'] == media_type]
        media_type_analysis[media_type] = {
            'count': len(type_df),
            'avg_impressions': float(type_df['インプレッション数'].mean()),
            'avg_engagement_rate': float(type_df['エンゲージメント率'].mean()),
            'total_impressions': int(type_df['インプレッション数'].sum())
        }

    # 曜日別分析
    weekday_analysis = {}
    for weekday in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        weekday_df = df[df['曜日'] == weekday]
        if len(weekday_df) > 0:
            weekday_analysis[weekday] = {
                'count': len(weekday_df),
                'avg_impressions': float(weekday_df['インプレッション数'].mean())
            }

    # 時間帯別分析（6時間単位）
    time_slot_analysis = {
        '0-6時': df[(df['時間帯'] >= 0) & (df['時間帯'] < 6)]['インプレッション数'].mean(),
        '6-12時': df[(df['時間帯'] >= 6) & (df['時間帯'] < 12)]['インプレッション数'].mean(),
        '12-18時': df[(df['時間帯'] >= 12) & (df['時間帯'] < 18)]['インプレッション数'].mean(),
        '18-24時': df[(df['時間帯'] >= 18) & (df['時間帯'] < 24)]['インプレッション数'].mean()
    }
    # NaNを0に変換
    time_slot_analysis = {k: (float(v) if pd.notna(v) else 0) for k, v in time_slot_analysis.items()}

    # キャプション文字数との相関
    caption_length_correlation = float(df[['キャプション文字数', 'インプレッション数']].corr().iloc[0, 1])

    # Top 5投稿
    top_5 = df.nlargest(5, 'インプレッション数')
    top_5_posts = [
        {
            '投稿日時': str(row['投稿日時']),
            'インプレッション数': int(row['インプレッション数']),
            'エンゲージメント率': float(row['エンゲージメント率']),
            'メディアタイプ': row['メディアタイプ'],
            'キャプション文字数': int(row['キャプション文字数']),
            'パーマリンク': row['パーマリンク']
        }
        for _, row in top_5.iterrows()
    ]

    # Bottom 5投稿
    bottom_5 = df.nsmallest(5, 'インプレッション数')
    bottom_5_posts = [
        {
            '投稿日時': str(row['投稿日時']),
            'インプレッション数': int(row['インプレッション数']),
            'エンゲージメント率': float(row['エンゲージメント率']),
            'メディアタイプ': row['メディアタイプ'],
            'キャプション文字数': int(row['キャプション文字数']),
            'パーマリンク': row['パーマリンク']
        }
        for _, row in bottom_5.iterrows()
    ]

    return {
        'basic_stats': {
            'total_posts': total_posts,
            'total_impressions': total_impressions,
            'avg_impressions': avg_impressions,
            'median_impressions': median_impressions,
            'avg_engagement_rate': avg_engagement_rate
        },
        'media_type_analysis': media_type_analysis,
        'weekday_analysis': weekday_analysis,
        'time_slot_analysis': time_slot_analysis,
        'caption_length_correlation': caption_length_correlation,
        'top_5_posts': top_5_posts,
        'bottom_5_posts': bottom_5_posts
    }

def main():
    base_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS')

    # 最新のCSVファイルを取得
    instagram_dir = base_path / 'Instagram'
    csv_files = list(instagram_dir.glob('instagram_*.csv'))

    if not csv_files:
        print("❌ Instagramデータが見つかりません。先にfetch_instagram_data.pyを実行してください。")
        return

    # 最新ファイルを選択
    latest_csv = sorted(csv_files, reverse=True)[0]

    print("=" * 80)
    print("Instagram投稿分析レポート")
    print("=" * 80)
    print(f"データソース: {latest_csv.name}")
    print()

    result = analyze_instagram_posts(str(latest_csv))

    if 'error' in result:
        print(f"エラー: {result['error']}")
        return

    # 基本統計
    print("【基本統計】")
    print("-" * 80)
    bs = result['basic_stats']
    print(f"総投稿数: {bs['total_posts']}件")
    print(f"総インプレッション数: {bs['total_impressions']:,}")
    print(f"平均インプレッション数: {bs['avg_impressions']:.0f}")
    print(f"中央値: {bs['median_impressions']:.0f}")
    print(f"平均エンゲージメント率: {bs['avg_engagement_rate']:.2f}%")
    print()

    # メディアタイプ別分析
    print("【メディアタイプ別分析】")
    print("-" * 80)
    for media_type, stats in result['media_type_analysis'].items():
        print(f"{media_type}:")
        print(f"  投稿数: {stats['count']}件 ({stats['count']/bs['total_posts']*100:.1f}%)")
        print(f"  平均imp: {stats['avg_impressions']:.0f}")
        print(f"  平均ER: {stats['avg_engagement_rate']:.2f}%")
        print()

    # 曜日別分析
    print("【曜日別分析】")
    print("-" * 80)
    for weekday, stats in result['weekday_analysis'].items():
        print(f"{weekday}: {stats['count']}件 (平均imp: {stats['avg_impressions']:.0f})")
    print()

    # 時間帯別分析
    print("【時間帯別分析】")
    print("-" * 80)
    for time_slot, avg_imp in result['time_slot_analysis'].items():
        print(f"{time_slot}: 平均imp {avg_imp:.0f}")
    print()

    # キャプション文字数との相関
    print("【キャプション文字数との相関】")
    print("-" * 80)
    print(f"相関係数: {result['caption_length_correlation']:.3f}")
    print()

    # Top 5投稿
    print("【Top 5投稿】")
    print("-" * 80)
    for i, post in enumerate(result['top_5_posts'], 1):
        print(f"{i}. {post['投稿日時']} - {post['インプレッション数']:,} imp | ER {post['エンゲージメント率']:.2f}%")
        print(f"   {post['メディアタイプ']} | キャプション: {post['キャプション文字数']}字")
        print(f"   {post['パーマリンク']}")
        print()

    # Bottom 5投稿
    print("【Bottom 5投稿】")
    print("-" * 80)
    for i, post in enumerate(result['bottom_5_posts'], 1):
        print(f"{i}. {post['投稿日時']} - {post['インプレッション数']:,} imp | ER {post['エンゲージメント率']:.2f}%")
        print(f"   {post['メディアタイプ']} | キャプション: {post['キャプション文字数']}字")
        print()

    # JSON出力
    output_path = instagram_dir / 'instagram_analysis_results.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"💾 詳細結果をJSONで保存: {output_path}")

if __name__ == '__main__':
    main()
