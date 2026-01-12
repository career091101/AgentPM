#!/usr/bin/env python3
"""
Facebook データを analysis_result.json に統合
"""

import json
from datetime import datetime

def load_files():
    """ファイル読み込み"""
    # 既存の分析結果
    with open('/Users/yuichi/agentpm/Flow/202601/2026-01-12/analysis_result.json', 'r') as f:
        analysis = json.load(f)

    # Facebook データ
    with open('/Users/yuichi/agentpm/Stock/programs/副業/projects/SNS/data/fb_performance_2026-01-12.json', 'r') as f:
        fb_data = json.load(f)

    return analysis, fb_data

def integrate_facebook():
    """Facebook データを統合"""
    analysis, fb_data = load_files()

    # Facebook セクション作成
    fb_summary = fb_data['summary']
    fb_kpi = fb_data['kpi_evaluation']

    facebook_section = {
        'views': fb_kpi['views_period_total'],
        'viewers': fb_summary.get('viewers', 0),
        'interactions': fb_kpi['interactions_period_total'],
        'reactions': fb_summary.get('reactions', 0),
        'comments': fb_summary.get('comments', 0),
        'shares': fb_summary.get('shares', 0),
        'followers': fb_summary['total_followers'],
        'net_followers': fb_summary['net_followers'],
        'engagement_rate': (fb_kpi['interactions_period_total'] / fb_kpi['views_period_total'] * 100) if fb_kpi['views_period_total'] > 0 else 0,
        'views_change': fb_summary['views_change_percent'],
        'interactions_change': fb_summary['interactions_change_percent'],
        'followers_change': (fb_summary['net_followers'] / fb_summary['total_followers'] * 100) if fb_summary['total_followers'] > 0 else 0,
        'avg_views_per_post': fb_kpi['views_daily_average'],
        'posts': fb_data['content_library']['total_posts_collected']
    }

    # platforms に Facebook を追加
    analysis['platforms']['facebook'] = facebook_section

    # サマリーを更新（Facebook を含める）
    analysis['summary']['total_posts'] += facebook_section['posts']
    # Facebook は views を使用（impressions とは別）
    analysis['summary']['total_engagement'] += facebook_section['interactions']

    # 生成時刻を更新
    analysis['period']['generated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # KPI評価にFacebookを追加
    # 目標: 週間閲覧数 100,000、インタラクション 1,500、フォロワー増 150
    fb_views_achievement = (fb_kpi['views_period_total'] / 100000) * 100
    fb_interactions_achievement = (fb_kpi['interactions_period_total'] / 1500) * 100
    fb_followers_achievement = (fb_summary['net_followers'] / 150) * 100

    def evaluate_kpi(achievement):
        if achievement >= 100:
            return "✅"
        elif achievement >= 80:
            return "⚠️"
        else:
            return "❌"

    analysis['kpi_evaluation']['facebook_views'] = {
        'achievement': round(fb_views_achievement, 1),
        'status': evaluate_kpi(fb_views_achievement)
    }

    analysis['kpi_evaluation']['facebook_interactions'] = {
        'achievement': round(fb_interactions_achievement, 1),
        'status': evaluate_kpi(fb_interactions_achievement)
    }

    analysis['kpi_evaluation']['facebook_followers'] = {
        'achievement': round(fb_followers_achievement, 1),
        'status': evaluate_kpi(fb_followers_achievement)
    }

    # 保存
    output_file = '/Users/yuichi/agentpm/Flow/202601/2026-01-12/analysis_result.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, ensure_ascii=False, indent=2)

    print("✅ Facebook データ統合完了")
    print(f"- Facebook閲覧数: {facebook_section['views']:,}回")
    print(f"- Facebookインタラクション: {facebook_section['interactions']:,}件")
    print(f"- Facebookフォロワー: {facebook_section['followers']:,}人 (+{facebook_section['net_followers']})")
    print(f"- Facebookエンゲージメント率: {facebook_section['engagement_rate']:.2f}%")
    print(f"\n📊 KPI達成状況:")
    print(f"- 閲覧数: {fb_views_achievement:.1f}% {analysis['kpi_evaluation']['facebook_views']['status']}")
    print(f"- インタラクション: {fb_interactions_achievement:.1f}% {analysis['kpi_evaluation']['facebook_interactions']['status']}")
    print(f"- フォロワー増: {fb_followers_achievement:.1f}% {analysis['kpi_evaluation']['facebook_followers']['status']}")

if __name__ == '__main__':
    integrate_facebook()
