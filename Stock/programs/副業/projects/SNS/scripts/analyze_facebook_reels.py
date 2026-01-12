#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Facebook Reels個別パフォーマンス分析スクリプト
"""

import pandas as pd
import json
from pathlib import Path

def analyze_facebook_reels(csv_path: str) -> dict:
    """Facebook CSVからReels投稿を分析"""

    df = pd.read_csv(csv_path, encoding='utf-8-sig')

    # 投稿タイプ列を確認
    type_col = [col for col in df.columns if 'タイプ' in col or 'type' in col.lower()][0]

    # Reels投稿を抽出
    reels_df = df[df[type_col].str.contains('リール', na=False)]
    photo_df = df[df[type_col].str.contains('写真', na=False)]

    # 列名を確認
    imp_col = [col for col in df.columns if 'インプレッション' in col][0]
    react_col = [col for col in df.columns if 'リアクション' in col][0]
    comment_col = [col for col in df.columns if 'コメント数' in col][0]
    share_col = [col for col in df.columns if 'シェア' in col][0]
    save_col = [col for col in df.columns if '保存数' in col][0]
    title_col = [col for col in df.columns if 'タイトル' in col][0]
    date_col = [col for col in df.columns if '公開時間' in col or '日時' in col][0]
    link_col = [col for col in df.columns if 'リンク' in col][0]

    # Reels個別データ
    reels_list = []
    for idx, row in reels_df.iterrows():
        imp = row[imp_col]
        reactions = row[react_col]
        comments = row[comment_col]
        shares = row[share_col]
        saves = row[save_col]

        engagement = reactions + comments + shares + saves if pd.notna(reactions) else 0
        er = (engagement / imp * 100) if imp > 0 else 0

        reels_list.append({
            'date': str(row[date_col]),
            'title_preview': str(row[title_col])[:100] + '...' if len(str(row[title_col])) > 100 else str(row[title_col]),
            'impressions': int(imp) if pd.notna(imp) else 0,
            'reactions': int(reactions) if pd.notna(reactions) else 0,
            'comments': int(comments) if pd.notna(comments) else 0,
            'shares': int(shares) if pd.notna(shares) else 0,
            'saves': int(saves) if pd.notna(saves) else 0,
            'total_engagement': int(engagement),
            'engagement_rate': round(er, 2),
            'link': str(row[link_col])
        })

    # Reels統計
    reels_stats = {
        'count': len(reels_df),
        'total_impressions': int(reels_df[imp_col].sum()) if len(reels_df) > 0 else 0,
        'avg_impressions': float(reels_df[imp_col].mean()) if len(reels_df) > 0 else 0,
        'median_impressions': float(reels_df[imp_col].median()) if len(reels_df) > 0 else 0,
        'max_impressions': int(reels_df[imp_col].max()) if len(reels_df) > 0 else 0,
        'min_impressions': int(reels_df[imp_col].min()) if len(reels_df) > 0 else 0
    }

    # 写真投稿との比較
    photo_stats = {
        'count': len(photo_df),
        'avg_impressions': float(photo_df[imp_col].mean()) if len(photo_df) > 0 else 0
    }

    return {
        'reels_stats': reels_stats,
        'photo_stats': photo_stats,
        'comparison': {
            'reels_vs_photo_ratio': round(reels_stats['avg_impressions'] / photo_stats['avg_impressions'], 2) if photo_stats['avg_impressions'] > 0 else 0,
            'reels_percentage': round(len(reels_df) / len(df) * 100, 1),
            'benchmark_min': 15.0,  # ベンチマーク最小15%
            'benchmark_max': 25.0,  # ベンチマーク最大25%
            'gap_from_benchmark_min': round(len(reels_df) / len(df) * 100 - 15.0, 1)
        },
        'individual_reels': sorted(reels_list, key=lambda x: x['impressions'], reverse=True)
    }

def main():
    base_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS')
    csv_path = list((base_path / 'Facebook').glob('facebook_*.csv'))[0]

    result = analyze_facebook_reels(str(csv_path))

    print("=" * 80)
    print("Facebook Reels個別パフォーマンス分析レポート")
    print("=" * 80)
    print()

    print("【Reels統計】")
    print("-" * 80)
    rs = result['reels_stats']
    print(f"総Reels数: {rs['count']}投稿")
    print(f"総インプレッション: {rs['total_impressions']:,}")
    print(f"平均インプレッション: {rs['avg_impressions']:.0f}")
    print(f"中央値: {rs['median_impressions']:.0f}")
    print(f"最大: {rs['max_impressions']:,}")
    print(f"最小: {rs['min_impressions']:,}")
    print()

    print("【写真投稿との比較】")
    print("-" * 80)
    ps = result['photo_stats']
    comp = result['comparison']
    print(f"写真投稿数: {ps['count']}投稿")
    print(f"写真平均インプレッション: {ps['avg_impressions']:.0f}")
    print(f"Reels vs 写真比率: {comp['reels_vs_photo_ratio']:.2f}倍")
    print()
    print(f"Reels投稿比率: {comp['reels_percentage']:.1f}%")
    print(f"ベンチマーク範囲: {comp['benchmark_min']:.0f}% - {comp['benchmark_max']:.0f}%")
    print(f"ベンチマーク最小値とのギャップ: {comp['gap_from_benchmark_min']:+.1f}ポイント")
    print()

    print("【個別Reels投稿（インプレッション降順）】")
    print("-" * 80)
    for i, reel in enumerate(result['individual_reels'], 1):
        print(f"{i}. {reel['date']} - {reel['impressions']:,} imp | ER {reel['engagement_rate']:.2f}%")
        print(f"   {reel['title_preview']}")
        print(f"   リアクション: {reel['reactions']} | コメント: {reel['comments']} | シェア: {reel['shares']} | 保存: {reel['saves']}")
        print(f"   リンク: {reel['link']}")
        print()

    # JSON出力
    output_path = base_path / 'Facebook' / 'facebook_reels_analysis.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"詳細結果をJSONで保存: {output_path}")

if __name__ == '__main__':
    main()
