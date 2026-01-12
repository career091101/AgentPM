#!/usr/bin/env python3
"""
SNS Multi-Platform Analysis Script
Facebook, LinkedIn, X の統合分析
"""

import csv
import json
from collections import defaultdict
from datetime import datetime
import os

# pandasとopenpyxlがあれば使用
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

# データファイルパス
DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/documents/2_discovery/data"
FB_CSV = os.path.join(DATA_DIR, "facebook_Sep-22-2025_Dec-21-2025_コンテンツ_公開日時_概要_1438120577831327.csv")
X_CSV = os.path.join(DATA_DIR, "account_overview_analytics.csv")
LINKEDIN_XLSX = os.path.join(DATA_DIR, "Linkedin_Content_2025-09-23_2025-12-21_優一佐藤.xlsx")

def load_facebook_data():
    """Facebookデータを読み込み"""
    posts = []
    with open(FB_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('ページ名') == '佐藤 優一' and row.get('インプレッション数'):
                try:
                    impressions = int(row.get('インプレッション数', '0').replace(',', ''))
                    interactions = int(row.get('インタラクション', '0').replace(',', ''))
                    reactions = int(row.get('リアクション', '0').replace(',', ''))
                    saves = int(row.get('保存数', '0').replace(',', ''))
                    shares = int(row.get('シェア', '0').replace(',', ''))
                    
                    posts.append({
                        'id': row.get('投稿ID'),
                        'title': row.get('タイトル', '')[:300],
                        'date': row.get('公開時間'),
                        'type': row.get('投稿タイプ'),
                        'impressions': impressions,
                        'interactions': interactions,
                        'reactions': reactions,
                        'saves': saves,
                        'shares': shares,
                        'engagement_rate': (interactions / impressions * 100) if impressions > 0 else 0,
                        'link': row.get('リンク'),
                        'platform': 'Facebook'
                    })
                except (ValueError, TypeError):
                    continue
    return posts

def load_x_data():
    """X(Twitter)データを読み込み - 日次データ"""
    daily_stats = []
    with open(X_CSV, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                impressions = int(row.get('インプレッション数', '0').replace(',', ''))
                likes = int(row.get('いいね', '0').replace(',', ''))
                engagement = int(row.get('エンゲージメント', '0').replace(',', ''))
                bookmarks = int(row.get('ブックマーク', '0').replace(',', ''))
                shares = int(row.get('共有された回数\\', '0').replace(',', ''))
                new_follows = int(row.get('新しいフォロー', '0').replace(',', ''))
                posts_created = int(row.get('ポストを作成', '0').replace(',', ''))
                
                daily_stats.append({
                    'date': row.get('Date'),
                    'impressions': impressions,
                    'likes': likes,
                    'engagement': engagement,
                    'bookmarks': bookmarks,
                    'shares': shares,
                    'new_follows': new_follows,
                    'posts_created': posts_created,
                    'platform': 'X'
                })
            except (ValueError, TypeError):
                continue
    return daily_stats

def load_linkedin_data():
    """LinkedInデータを読み込み（XLSXファイル）"""
    if not HAS_PANDAS:
        print("   ⚠️ pandasがインストールされていないため、LinkedInデータはスキップ")
        return []
    
    try:
        df = pd.read_excel(LINKEDIN_XLSX)
        posts = []
        for _, row in df.iterrows():
            try:
                impressions = int(row.get('Impressions', 0)) if pd.notna(row.get('Impressions')) else 0
                reactions = int(row.get('Reactions', 0)) if pd.notna(row.get('Reactions')) else 0
                comments = int(row.get('Comments', 0)) if pd.notna(row.get('Comments')) else 0
                reposts = int(row.get('Reposts', 0)) if pd.notna(row.get('Reposts')) else 0
                
                posts.append({
                    'date': str(row.get('Date', '')),
                    'title': str(row.get('Post copy', ''))[:300] if pd.notna(row.get('Post copy')) else '',
                    'impressions': impressions,
                    'reactions': reactions,
                    'comments': comments,
                    'reposts': reposts,
                    'interactions': reactions + comments + reposts,
                    'engagement_rate': ((reactions + comments + reposts) / impressions * 100) if impressions > 0 else 0,
                    'platform': 'LinkedIn'
                })
            except (ValueError, TypeError) as e:
                continue
        return posts
    except Exception as e:
        print(f"   ⚠️ LinkedInデータ読み込みエラー: {e}")
        return []

def extract_topics(title):
    """トピック/キーワード抽出"""
    keywords = {
        'OpenAI': ['OpenAI', 'ChatGPT', 'GPT', 'サム・アルトマン', 'アルトマン', 'Sam Altman'],
        'Google/Gemini': ['Google', 'Gemini', 'グーグル', 'Antigravity'],
        'Anthropic': ['Anthropic', 'Claude', 'アンソロピック', 'アントロピック'],
        'AI全般': ['AI', '人工知能', 'エージェント', 'AGI', 'LLM'],
        'ロボット': ['ロボット', 'テスラ', 'ヒューマノイド', 'humanoid', 'robot'],
        '半導体': ['NVIDIA', 'エヌビディア', 'GPU', '半導体', 'チップ'],
        '投資/経済': ['投資', 'バブル', '株', 'GDP', '経済', '赤字', '収益'],
    }
    
    matched_topics = []
    for topic, kws in keywords.items():
        if any(kw.lower() in title.lower() for kw in kws):
            matched_topics.append(topic)
    
    return matched_topics if matched_topics else ['その他']

def analyze_facebook(posts):
    """Facebook詳細分析"""
    print("\n" + "=" * 60)
    print("📘 FACEBOOK 分析")
    print("=" * 60)
    
    # 基礎統計
    impressions = [p['impressions'] for p in posts]
    total_imp = sum(impressions)
    avg_imp = total_imp / len(posts) if posts else 0
    
    print(f"\n📊 基礎統計")
    print(f"   投稿数: {len(posts)}件")
    print(f"   総インプレッション: {total_imp:,}")
    print(f"   平均インプレッション: {avg_imp:,.0f}")
    print(f"   最大: {max(impressions):,} / 最小: {min(impressions):,}")
    
    # トップ投稿
    sorted_posts = sorted(posts, key=lambda x: x['impressions'], reverse=True)
    print(f"\n🏆 トップ5投稿")
    for i, p in enumerate(sorted_posts[:5], 1):
        topics = extract_topics(p['title'])
        print(f"   {i}. [{p['impressions']:,} imp] [{', '.join(topics)}]")
        print(f"      {p['title'][:80]}...")
    
    # トピック別分析
    topic_stats = defaultdict(lambda: {'count': 0, 'total_imp': 0})
    for p in posts:
        for topic in extract_topics(p['title']):
            topic_stats[topic]['count'] += 1
            topic_stats[topic]['total_imp'] += p['impressions']
    
    print(f"\n🏷️ トピック別パフォーマンス")
    for topic, data in sorted(topic_stats.items(), key=lambda x: x[1]['total_imp']/max(x[1]['count'],1), reverse=True):
        avg = data['total_imp'] / data['count'] if data['count'] > 0 else 0
        print(f"   {topic}: {data['count']}件, 平均{avg:,.0f} imp")
    
    return {
        'total_posts': len(posts),
        'total_impressions': total_imp,
        'avg_impressions': avg_imp,
        'top_posts': sorted_posts[:10],
        'topic_stats': dict(topic_stats)
    }

def analyze_x(daily_stats):
    """X(Twitter)分析"""
    print("\n" + "=" * 60)
    print("🐦 X (Twitter) 分析")
    print("=" * 60)
    
    total_imp = sum(d['impressions'] for d in daily_stats)
    total_engagement = sum(d['engagement'] for d in daily_stats)
    total_posts = sum(d['posts_created'] for d in daily_stats)
    total_follows = sum(d['new_follows'] for d in daily_stats)
    
    print(f"\n📊 期間サマリー（{len(daily_stats)}日間）")
    print(f"   総インプレッション: {total_imp:,}")
    print(f"   総エンゲージメント: {total_engagement:,}")
    print(f"   エンゲージメント率: {(total_engagement/total_imp*100):.2f}%" if total_imp > 0 else "N/A")
    print(f"   投稿数: {total_posts}件")
    print(f"   新規フォロワー: {total_follows}人")
    print(f"   日平均インプレッション: {total_imp/len(daily_stats):,.0f}")
    
    # 高パフォーマンスの日
    sorted_days = sorted(daily_stats, key=lambda x: x['impressions'], reverse=True)
    print(f"\n🏆 トップ5日")
    for i, d in enumerate(sorted_days[:5], 1):
        print(f"   {i}. {d['date']}: {d['impressions']:,} imp, {d['engagement']} eng")
    
    return {
        'total_days': len(daily_stats),
        'total_impressions': total_imp,
        'total_engagement': total_engagement,
        'total_posts': total_posts,
        'avg_daily_impressions': total_imp / len(daily_stats) if daily_stats else 0,
        'top_days': sorted_days[:10]
    }

def analyze_linkedin(posts):
    """LinkedIn分析"""
    print("\n" + "=" * 60)
    print("💼 LINKEDIN 分析")
    print("=" * 60)
    
    if not posts:
        print("   データなし")
        return {}
    
    impressions = [p['impressions'] for p in posts]
    total_imp = sum(impressions)
    avg_imp = total_imp / len(posts) if posts else 0
    
    print(f"\n📊 基礎統計")
    print(f"   投稿数: {len(posts)}件")
    print(f"   総インプレッション: {total_imp:,}")
    print(f"   平均インプレッション: {avg_imp:,.0f}")
    
    # トップ投稿
    sorted_posts = sorted(posts, key=lambda x: x['impressions'], reverse=True)
    print(f"\n🏆 トップ5投稿")
    for i, p in enumerate(sorted_posts[:5], 1):
        topics = extract_topics(p['title'])
        print(f"   {i}. [{p['impressions']:,} imp] [{', '.join(topics)}]")
        print(f"      {p['title'][:80]}...")
    
    # トピック別分析
    topic_stats = defaultdict(lambda: {'count': 0, 'total_imp': 0})
    for p in posts:
        for topic in extract_topics(p['title']):
            topic_stats[topic]['count'] += 1
            topic_stats[topic]['total_imp'] += p['impressions']
    
    print(f"\n🏷️ トピック別パフォーマンス")
    for topic, data in sorted(topic_stats.items(), key=lambda x: x[1]['total_imp']/max(x[1]['count'],1), reverse=True):
        avg = data['total_imp'] / data['count'] if data['count'] > 0 else 0
        print(f"   {topic}: {data['count']}件, 平均{avg:,.0f} imp")
    
    return {
        'total_posts': len(posts),
        'total_impressions': total_imp,
        'avg_impressions': avg_imp,
        'top_posts': sorted_posts[:10],
        'topic_stats': dict(topic_stats)
    }

def cross_platform_comparison(fb_stats, x_stats, li_stats):
    """クロスプラットフォーム比較"""
    print("\n" + "=" * 60)
    print("📊 クロスプラットフォーム比較")
    print("=" * 60)
    
    print(f"\n{'プラットフォーム':<15} {'投稿/日数':<12} {'総インプレッション':<20} {'平均':<15}")
    print("-" * 70)
    
    if fb_stats:
        print(f"{'Facebook':<15} {fb_stats['total_posts']:<12} {fb_stats['total_impressions']:>15,} {fb_stats['avg_impressions']:>12,.0f}")
    
    if x_stats:
        print(f"{'X (Twitter)':<15} {x_stats['total_days']:<12} {x_stats['total_impressions']:>15,} {x_stats['avg_daily_impressions']:>12,.0f}/日")
    
    if li_stats and li_stats.get('total_posts'):
        print(f"{'LinkedIn':<15} {li_stats['total_posts']:<12} {li_stats['total_impressions']:>15,} {li_stats['avg_impressions']:>12,.0f}")
    
    # 合計
    total_imp = (fb_stats.get('total_impressions', 0) + 
                 x_stats.get('total_impressions', 0) + 
                 li_stats.get('total_impressions', 0))
    print("-" * 70)
    print(f"{'合計':<15} {'':<12} {total_imp:>15,}")
    print(f"\n📈 月間換算: {total_imp / 3:,.0f} imp/月")
    print(f"📎 目標(100万)との差: {((total_imp / 3) / 1000000 * 100):.1f}%達成")

def main():
    print("=" * 60)
    print("SNS Multi-Platform Analysis")
    print("=" * 60)
    
    # データ読み込み
    print("\n📂 データ読み込み中...")
    fb_posts = load_facebook_data()
    print(f"   Facebook: {len(fb_posts)}件")
    
    x_daily = load_x_data()
    print(f"   X: {len(x_daily)}日分")
    
    li_posts = load_linkedin_data()
    print(f"   LinkedIn: {len(li_posts)}件")
    
    # 各プラットフォーム分析
    fb_stats = analyze_facebook(fb_posts)
    x_stats = analyze_x(x_daily)
    li_stats = analyze_linkedin(li_posts)
    
    # クロスプラットフォーム比較
    cross_platform_comparison(fb_stats, x_stats, li_stats)
    
    # 結果をJSONで保存
    output = {
        'facebook': {
            'total_posts': fb_stats['total_posts'],
            'total_impressions': fb_stats['total_impressions'],
            'avg_impressions': fb_stats['avg_impressions'],
        },
        'x': {
            'total_days': x_stats['total_days'],
            'total_impressions': x_stats['total_impressions'],
            'avg_daily_impressions': x_stats['avg_daily_impressions'],
        },
        'linkedin': {
            'total_posts': li_stats.get('total_posts', 0),
            'total_impressions': li_stats.get('total_impressions', 0),
            'avg_impressions': li_stats.get('avg_impressions', 0),
        }
    }
    
    output_path = os.path.join(DATA_DIR, "multi_platform_analysis.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\n💾 分析結果を保存: {output_path}")
    
    print("\n" + "=" * 60)
    print("分析完了")
    print("=" * 60)

if __name__ == "__main__":
    main()
