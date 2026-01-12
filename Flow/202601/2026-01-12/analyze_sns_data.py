#!/usr/bin/env python3
"""
SNS Performance Analysis Script
2026-01-01 ～ 2026-01-11 のデータを分析
"""

import json
from datetime import datetime
from typing import Dict, List, Any

def load_data(file_path: str) -> Dict:
    """JSONデータを読み込み"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_platform(posts: List[Dict], platform: str) -> Dict:
    """プラットフォーム別分析"""
    platform_posts = [p for p in posts if p.get('platform') == platform]

    if not platform_posts:
        return {
            'posts': 0,
            'impressions': 0,
            'engagement': 0,
            'engagement_rate': 0,
            'avg_impressions_per_post': 0
        }

    total_impressions = sum(p.get('impressions', 0) for p in platform_posts)
    total_views = sum(p.get('views', 0) for p in platform_posts)
    total_engagement = sum(
        p.get('likes', 0) + p.get('comments', 0) + p.get('shares', 0)
        for p in platform_posts
    )

    # Threads は views を使用
    if platform == 'threads':
        engagement_rate = (total_engagement / total_views * 100) if total_views > 0 else None
        avg_per_post = total_views / len(platform_posts) if platform_posts else 0
        return {
            'posts': len(platform_posts),
            'views': total_views,
            'impressions': 0,  # Threads は impressions 計測不可
            'engagement': total_engagement,
            'engagement_rate': engagement_rate,
            'avg_views_per_post': avg_per_post
        }
    else:
        engagement_rate = (total_engagement / total_impressions * 100) if total_impressions > 0 else 0
        avg_per_post = total_impressions / len(platform_posts) if platform_posts else 0
        return {
            'posts': len(platform_posts),
            'impressions': total_impressions,
            'engagement': total_engagement,
            'engagement_rate': engagement_rate,
            'avg_impressions_per_post': avg_per_post
        }

def get_top_posts(posts: List[Dict], limit: int = 5) -> List[Dict]:
    """トップN投稿を抽出"""
    sorted_posts = sorted(posts, key=lambda x: x.get('impressions', 0), reverse=True)

    top_posts = []
    for i, post in enumerate(sorted_posts[:limit], 1):
        impressions = post.get('impressions', 0)
        engagement = post.get('likes', 0) + post.get('comments', 0) + post.get('shares', 0)
        engagement_rate = (engagement / impressions * 100) if impressions > 0 else 0

        top_posts.append({
            'rank': i,
            'platform': post.get('platform', 'unknown'),
            'published_at': post.get('published_at', ''),
            'impressions': impressions,
            'engagement': engagement,
            'engagement_rate': round(engagement_rate, 2),
            'text_preview': post.get('text', '')[:100] if post.get('text') else 'N/A'
        })

    return top_posts

def evaluate_kpi(achievement: float) -> str:
    """KPI評価記号"""
    if achievement >= 100:
        return "✅"
    elif achievement >= 80:
        return "⚠️"
    else:
        return "❌"

def main():
    # データ読み込み
    data_file = '/Users/yuichi/agentpm/Flow/202601/2026-01-12/late_api_analytics_20260101-20260111.json'
    data = load_data(data_file)

    posts = data.get('data', [])
    metadata = data.get('metadata', {})

    # プラットフォーム別分析
    linkedin_stats = analyze_platform(posts, 'linkedin')
    x_stats = analyze_platform(posts, 'twitter')
    threads_stats = analyze_platform(posts, 'threads')

    # 全体サマリー（LinkedIn + X のみ）
    total_posts = len(posts)
    total_impressions = linkedin_stats['impressions'] + x_stats['impressions']
    total_engagement = linkedin_stats['engagement'] + x_stats['engagement'] + threads_stats['engagement']
    avg_engagement_rate = (linkedin_stats['engagement'] + x_stats['engagement']) / total_impressions * 100 if total_impressions > 0 else 0

    # KPI評価
    kpi_targets = {
        'total_impressions': 150000,
        'engagement_rate': 1.5,
        'linkedin_avg': 8000,
        'x_avg': 2000
    }

    impressions_achievement = (total_impressions / kpi_targets['total_impressions']) * 100
    engagement_achievement = (avg_engagement_rate / kpi_targets['engagement_rate']) * 100
    linkedin_achievement = (linkedin_stats['avg_impressions_per_post'] / kpi_targets['linkedin_avg']) * 100
    x_achievement = (x_stats['avg_impressions_per_post'] / kpi_targets['x_avg']) * 100

    # トップ5投稿
    top_posts = get_top_posts(posts, 5)

    # 結果出力
    result = {
        'period': {
            'start': '2026-01-01',
            'end': '2026-01-11',
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        'summary': {
            'total_posts': total_posts,
            'total_impressions': total_impressions,
            'total_engagement': total_engagement,
            'avg_engagement_rate': round(avg_engagement_rate, 2)
        },
        'platforms': {
            'linkedin': linkedin_stats,
            'x': x_stats,
            'threads': threads_stats
        },
        'kpi_evaluation': {
            'impressions': {
                'achievement': round(impressions_achievement, 1),
                'status': evaluate_kpi(impressions_achievement)
            },
            'engagement_rate': {
                'achievement': round(engagement_achievement, 1),
                'status': evaluate_kpi(engagement_achievement)
            },
            'linkedin_avg': {
                'achievement': round(linkedin_achievement, 1),
                'status': evaluate_kpi(linkedin_achievement)
            },
            'x_avg': {
                'achievement': round(x_achievement, 1),
                'status': evaluate_kpi(x_achievement)
            }
        },
        'top_posts': top_posts
    }

    # JSON出力
    output_file = '/Users/yuichi/agentpm/Flow/202601/2026-01-12/analysis_result.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✅ 分析完了: {output_file}")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
