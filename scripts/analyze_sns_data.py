#!/usr/bin/env python3
"""
SNS Data Analysis Script
分析要件に基づいたFacebook投稿データの分析
"""

import csv
import json
from collections import defaultdict
from datetime import datetime
import os

# データファイルパス
DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/documents/2_discovery/data"
FB_CSV = os.path.join(DATA_DIR, "facebook_Sep-22-2025_Dec-21-2025_コンテンツ_公開日時_概要_1438120577831327.csv")

def load_facebook_data():
    """Facebookデータを読み込み"""
    posts = []
    with open(FB_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 自分の投稿のみ（他者のシェアや言及を除外）
            if row.get('ページ名') == '佐藤 優一' and row.get('インプレッション数'):
                try:
                    impressions = int(row.get('インプレッション数', '0').replace(',', ''))
                    interactions = int(row.get('インタラクション', '0').replace(',', ''))
                    reactions = int(row.get('リアクション', '0').replace(',', ''))
                    saves = int(row.get('保存数', '0').replace(',', ''))
                    shares = int(row.get('シェア', '0').replace(',', ''))
                    
                    posts.append({
                        'id': row.get('投稿ID'),
                        'title': row.get('タイトル', '')[:200],  # 最初の200文字
                        'date': row.get('公開時間'),
                        'type': row.get('投稿タイプ'),
                        'impressions': impressions,
                        'interactions': interactions,
                        'reactions': reactions,
                        'saves': saves,
                        'shares': shares,
                        'engagement_rate': (interactions / impressions * 100) if impressions > 0 else 0,
                        'link': row.get('リンク')
                    })
                except (ValueError, TypeError):
                    continue
    return posts

def basic_statistics(posts):
    """基礎統計量の算出"""
    impressions = [p['impressions'] for p in posts]
    engagement_rates = [p['engagement_rate'] for p in posts]
    
    stats = {
        'total_posts': len(posts),
        'impressions': {
            'total': sum(impressions),
            'mean': sum(impressions) / len(impressions) if impressions else 0,
            'median': sorted(impressions)[len(impressions)//2] if impressions else 0,
            'max': max(impressions) if impressions else 0,
            'min': min(impressions) if impressions else 0,
        },
        'engagement_rate': {
            'mean': sum(engagement_rates) / len(engagement_rates) if engagement_rates else 0,
            'median': sorted(engagement_rates)[len(engagement_rates)//2] if engagement_rates else 0,
        }
    }
    return stats

def get_top_bottom_posts(posts, n=10):
    """トップ10%とボトム10%の投稿を抽出"""
    sorted_by_imp = sorted(posts, key=lambda x: x['impressions'], reverse=True)
    
    top_n = max(1, len(posts) // 10)  # 10%
    bottom_n = max(1, len(posts) // 10)
    
    return {
        'top_posts': sorted_by_imp[:top_n],
        'bottom_posts': sorted_by_imp[-bottom_n:],
        'top_n': top_n,
        'bottom_n': bottom_n
    }

def analyze_post_types(posts):
    """投稿タイプ別の分析"""
    type_stats = defaultdict(lambda: {'count': 0, 'total_imp': 0, 'total_eng': 0})
    
    for p in posts:
        ptype = p['type'] or 'その他'
        type_stats[ptype]['count'] += 1
        type_stats[ptype]['total_imp'] += p['impressions']
        type_stats[ptype]['total_eng'] += p['interactions']
    
    # 平均を計算
    for ptype in type_stats:
        count = type_stats[ptype]['count']
        type_stats[ptype]['avg_imp'] = type_stats[ptype]['total_imp'] / count if count > 0 else 0
        type_stats[ptype]['avg_eng'] = type_stats[ptype]['total_eng'] / count if count > 0 else 0
    
    return dict(type_stats)

def extract_topics(posts):
    """トピック/キーワード抽出（簡易版）"""
    keywords = {
        'OpenAI': ['OpenAI', 'ChatGPT', 'GPT', 'サム・アルトマン', 'アルトマン'],
        'Google/Gemini': ['Google', 'Gemini', 'グーグル'],
        'AI全般': ['AI', '人工知能', 'エージェント', 'AGI'],
        'ロボット': ['ロボット', 'テスラ', 'ヒューマノイド'],
        '半導体': ['NVIDIA', 'エヌビディア', 'GPU', '半導体'],
        '投資/経済': ['投資', 'バブル', '株', 'GDP', '経済'],
    }
    
    topic_stats = defaultdict(lambda: {'count': 0, 'total_imp': 0, 'posts': []})
    
    for p in posts:
        title = p['title']
        for topic, kws in keywords.items():
            if any(kw in title for kw in kws):
                topic_stats[topic]['count'] += 1
                topic_stats[topic]['total_imp'] += p['impressions']
                topic_stats[topic]['posts'].append(p)
    
    # 平均を計算
    for topic in topic_stats:
        count = topic_stats[topic]['count']
        topic_stats[topic]['avg_imp'] = topic_stats[topic]['total_imp'] / count if count > 0 else 0
    
    return dict(topic_stats)

def main():
    print("=" * 60)
    print("SNS Data Analysis - Facebook")
    print("=" * 60)
    
    # データ読み込み
    print("\n📂 データ読み込み中...")
    posts = load_facebook_data()
    print(f"   読み込み完了: {len(posts)}件の投稿")
    
    # 基礎統計
    print("\n📊 基礎統計量")
    print("-" * 40)
    stats = basic_statistics(posts)
    print(f"   総投稿数: {stats['total_posts']}件")
    print(f"   総インプレッション: {stats['impressions']['total']:,}")
    print(f"   平均インプレッション: {stats['impressions']['mean']:,.0f}")
    print(f"   中央値インプレッション: {stats['impressions']['median']:,}")
    print(f"   最大インプレッション: {stats['impressions']['max']:,}")
    print(f"   平均エンゲージメント率: {stats['engagement_rate']['mean']:.2f}%")
    
    # トップ/ボトム投稿
    print("\n🏆 トップ10%投稿")
    print("-" * 40)
    top_bottom = get_top_bottom_posts(posts)
    for i, p in enumerate(top_bottom['top_posts'][:5], 1):
        print(f"   {i}. [{p['impressions']:,} imp] {p['title'][:60]}...")
    
    print("\n⚠️ ボトム10%投稿")
    print("-" * 40)
    for i, p in enumerate(top_bottom['bottom_posts'][:5], 1):
        print(f"   {i}. [{p['impressions']:,} imp] {p['title'][:60]}...")
    
    # 投稿タイプ別
    print("\n📁 投稿タイプ別パフォーマンス")
    print("-" * 40)
    type_stats = analyze_post_types(posts)
    for ptype, data in sorted(type_stats.items(), key=lambda x: x[1]['avg_imp'], reverse=True):
        print(f"   {ptype}: {data['count']}件, 平均{data['avg_imp']:,.0f} imp")
    
    # トピック別
    print("\n🏷️ トピック別パフォーマンス")
    print("-" * 40)
    topic_stats = extract_topics(posts)
    for topic, data in sorted(topic_stats.items(), key=lambda x: x[1]['avg_imp'], reverse=True):
        print(f"   {topic}: {data['count']}件, 平均{data['avg_imp']:,.0f} imp")
    
    # 結果をJSONで出力
    output = {
        'basic_stats': stats,
        'top_posts': top_bottom['top_posts'][:10],
        'bottom_posts': top_bottom['bottom_posts'][:10],
        'type_stats': type_stats,
        'topic_stats': {k: {kk: vv for kk, vv in v.items() if kk != 'posts'} for k, v in topic_stats.items()}
    }
    
    output_path = os.path.join(DATA_DIR, "facebook_analysis_results.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\n💾 分析結果を保存: {output_path}")
    
    print("\n" + "=" * 60)
    print("分析完了")
    print("=" * 60)

if __name__ == "__main__":
    main()
