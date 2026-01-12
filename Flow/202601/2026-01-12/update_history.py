#!/usr/bin/env python3
"""
history.json 更新スクリプト
"""

import json
from datetime import datetime

def load_files():
    """ファイル読み込み"""
    # 分析結果
    with open('/Users/yuichi/agentpm/Flow/202601/2026-01-12/analysis_result.json', 'r') as f:
        analysis = json.load(f)

    # 履歴データ
    with open('/Users/yuichi/agentpm/Stock/programs/副業/projects/SNS/history.json', 'r') as f:
        history = json.load(f)

    # Late APIデータ（トップ5投稿のテキスト取得用）
    with open('/Users/yuichi/agentpm/Flow/202601/2026-01-12/late_api_analytics_20260101-20260111.json', 'r') as f:
        late_data = json.load(f)

    return analysis, history, late_data

def find_top_posts_details(analysis, late_data):
    """トップ5投稿の詳細を取得"""
    top_posts_detailed = []
    posts = late_data.get('data', [])

    for top in analysis['top_posts']:
        # Late APIデータから対応する投稿を検索
        post = next((p for p in posts if p.get('impressions') == top['impressions']), None)

        if post:
            engagement = post.get('likes', 0) + post.get('comments', 0) + post.get('shares', 0)
            text = post.get('text', '')

            top_posts_detailed.append({
                'rank': top['rank'],
                'platform': top['platform'],
                'published_at': top['published_at'],
                'impressions': top['impressions'],
                'engagement_rate': top['engagement_rate'],
                'theme': '未分類',  # テーマは手動または別のロジックで設定
                'text_preview': text[:150] if text else 'N/A'
            })

    return top_posts_detailed

def update_history():
    """history.json更新"""
    analysis, history, late_data = load_files()

    # トップ5投稿詳細を取得
    top_posts = find_top_posts_details(analysis, late_data)

    # 新規週データ作成
    new_week = {
        'week_id': '2026-W02',
        'period_start': '2026-01-01',
        'period_end': '2026-01-11',
        'kpi': {
            'total_posts': analysis['summary']['total_posts'],
            'total_impressions': analysis['summary']['total_impressions'],
            'total_engagement': analysis['summary']['total_engagement'],
            'engagement_rate': analysis['summary']['avg_engagement_rate'],
            'platforms': {
                'linkedin': {
                    'posts': analysis['platforms']['linkedin']['posts'],
                    'impressions': analysis['platforms']['linkedin']['impressions'],
                    'engagement': analysis['platforms']['linkedin']['engagement'],
                    'engagement_rate': analysis['platforms']['linkedin']['engagement_rate'],
                    'avg_impressions_per_post': analysis['platforms']['linkedin']['avg_impressions_per_post']
                },
                'x': {
                    'posts': analysis['platforms']['x']['posts'],
                    'impressions': analysis['platforms']['x']['impressions'],
                    'engagement': analysis['platforms']['x']['engagement'],
                    'engagement_rate': analysis['platforms']['x']['engagement_rate'],
                    'avg_impressions_per_post': analysis['platforms']['x']['avg_impressions_per_post']
                },
                'threads': {
                    'posts': analysis['platforms']['threads']['posts'],
                    'views': analysis['platforms']['threads']['views'],
                    'impressions': 0,
                    'engagement': analysis['platforms']['threads']['engagement'],
                    'engagement_rate': analysis['platforms']['threads']['engagement_rate'],
                    'avg_views_per_post': analysis['platforms']['threads']['avg_views_per_post'],
                    'note': 'viewsフィールド使用。views>0の場合のみエンゲージメント率計算'
                }
            }
        },
        'top_posts': top_posts,
        'success_patterns': {
            'top_themes': [],
            'pattern_library_reference': 'x_patterns_detailed.md',
            'high_performing_patterns': []
        }
    }

    # weeks配列に追加
    history['weeks'].append(new_week)

    # 4週間を超える古いデータを削除
    if len(history['weeks']) > 4:
        history['weeks'] = history['weeks'][-4:]

    # last_updated更新
    history['last_updated'] = '2026-01-12'

    # 保存
    with open('/Users/yuichi/agentpm/Stock/programs/副業/projects/SNS/history.json', 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

    print("✅ history.json更新完了")
    print(f"- 総週数: {len(history['weeks'])}週")
    print(f"- 最新週: {new_week['week_id']} ({new_week['period_start']} 〜 {new_week['period_end']})")
    print(f"- 総投稿数: {new_week['kpi']['total_posts']}件")

if __name__ == '__main__':
    update_history()
