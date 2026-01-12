#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全プラットフォーム統合分析スクリプト

目的: Facebook、LinkedIn、X、Instagram、Threadsの5プラットフォームを統合分析
1. 全プラットフォーム合計インプレッション
2. プラットフォーム別寄与率
3. 目標達成率（346,766 → 1,000,000）
4. プラットフォーム別エンゲージメント率比較
"""

import pandas as pd
import json
from pathlib import Path
from typing import Dict, List

def load_facebook_data(base_path: Path) -> Dict:
    """Facebookデータを読み込み"""
    facebook_dir = base_path / 'Facebook'
    csv_files = list(facebook_dir.glob('facebook_*.csv'))

    if not csv_files:
        return {'posts': 0, 'impressions': 0, 'engagement_rate': 0}

    df = pd.read_csv(csv_files[0], encoding='utf-8-sig')

    # カラム名を動的に検出
    imp_col = [col for col in df.columns if 'インプレッション' in col]
    react_col = [col for col in df.columns if 'リアクション' in col]

    if not imp_col:
        return {'posts': 0, 'impressions': 0, 'engagement_rate': 0}

    total_impressions = int(df[imp_col[0]].sum())
    total_reactions = int(df[react_col[0]].sum()) if react_col else 0
    engagement_rate = (total_reactions / total_impressions * 100) if total_impressions > 0 else 0

    return {
        'posts': len(df),
        'impressions': total_impressions,
        'engagement_rate': float(engagement_rate)
    }

def load_linkedin_data(base_path: Path) -> Dict:
    """LinkedInデータを読み込み"""
    linkedin_dir = base_path / 'LinkedIn'
    csv_files = list(linkedin_dir.glob('linkedin_*.csv'))

    if not csv_files:
        return {'posts': 0, 'impressions': 0, 'engagement_rate': 0}

    # 複数CSVがある場合は最新のものを使用
    latest_csv = sorted(csv_files, reverse=True)[0]
    df = pd.read_csv(latest_csv, encoding='utf-8-sig')

    # LinkedInは「インプレッション数」「エンゲージメント数」のカラムがある
    imp_col = [col for col in df.columns if 'インプレッション' in col]
    engage_col = [col for col in df.columns if 'エンゲージメント' in col]

    if not imp_col:
        return {'posts': 0, 'impressions': 0, 'engagement_rate': 0}

    total_impressions = int(df[imp_col[0]].sum())
    total_engagement = int(df[engage_col[0]].sum()) if engage_col else 0
    engagement_rate = (total_engagement / total_impressions * 100) if total_impressions > 0 else 0

    return {
        'posts': len(df),
        'impressions': total_impressions,
        'engagement_rate': float(engagement_rate)
    }

def load_x_data(base_path: Path) -> Dict:
    """Xデータを読み込み"""
    x_dir = base_path / 'X'
    csv_files = list(x_dir.glob('*.csv'))

    if not csv_files:
        return {'posts': 0, 'impressions': 0, 'engagement_rate': 0}

    # 最新のCSVを使用
    latest_csv = sorted(csv_files, reverse=True)[0]
    df = pd.read_csv(latest_csv, encoding='utf-8-sig')

    # Xは「インプレッション数」「エンゲージメント数」のカラムがある
    imp_col = [col for col in df.columns if 'インプレッション' in col or 'impression' in col.lower()]
    engage_col = [col for col in df.columns if 'エンゲージメント' in col or 'engagement' in col.lower()]

    if not imp_col:
        return {'posts': 0, 'impressions': 0, 'engagement_rate': 0}

    total_impressions = int(df[imp_col[0]].sum())
    total_engagement = int(df[engage_col[0]].sum()) if engage_col else 0
    engagement_rate = (total_engagement / total_impressions * 100) if total_impressions > 0 else 0

    return {
        'posts': len(df),
        'impressions': total_impressions,
        'engagement_rate': float(engagement_rate)
    }

def load_instagram_data(base_path: Path) -> Dict:
    """Instagramデータを読み込み"""
    instagram_dir = base_path / 'Instagram'
    csv_files = list(instagram_dir.glob('instagram_*.csv'))

    if not csv_files:
        return {'posts': 0, 'impressions': 0, 'engagement_rate': 0}

    # 最新のCSVを使用
    latest_csv = sorted(csv_files, reverse=True)[0]
    df = pd.read_csv(latest_csv, encoding='utf-8-sig')

    total_impressions = int(df['インプレッション数'].sum())
    avg_engagement_rate = float(df['エンゲージメント率'].mean())

    return {
        'posts': len(df),
        'impressions': total_impressions,
        'engagement_rate': avg_engagement_rate
    }

def load_threads_data(base_path: Path) -> Dict:
    """Threadsデータを読み込み"""
    threads_dir = base_path / 'Threads'
    csv_files = list(threads_dir.glob('threads_*.csv'))

    if not csv_files:
        return {'posts': 0, 'views': 0, 'engagement_rate': 0}

    # 最新のCSVを使用
    latest_csv = sorted(csv_files, reverse=True)[0]
    df = pd.read_csv(latest_csv, encoding='utf-8-sig')

    total_views = int(df['閲覧数'].sum())
    avg_engagement_rate = float(df['エンゲージメント率'].mean())

    return {
        'posts': len(df),
        'views': total_views,  # Threadsは閲覧数
        'engagement_rate': avg_engagement_rate
    }

def analyze_all_platforms():
    """全プラットフォーム統合分析"""

    base_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS')

    print("=" * 80)
    print("全プラットフォーム統合分析レポート")
    print("=" * 80)
    print()

    # 各プラットフォームのデータ読み込み
    print("📥 各プラットフォームのデータを読み込み中...")
    facebook = load_facebook_data(base_path)
    linkedin = load_linkedin_data(base_path)
    x = load_x_data(base_path)
    instagram = load_instagram_data(base_path)
    threads = load_threads_data(base_path)

    # 合計インプレッション数計算（Threadsは閲覧数をインプレッション相当として扱う）
    total_impressions = (
        facebook['impressions'] +
        linkedin['impressions'] +
        x['impressions'] +
        instagram['impressions'] +
        threads.get('views', 0)
    )

    # 総投稿数
    total_posts = (
        facebook['posts'] +
        linkedin['posts'] +
        x['posts'] +
        instagram['posts'] +
        threads['posts']
    )

    print("✅ データ読み込み完了")
    print()

    # プラットフォーム別寄与率
    platforms = {
        'Facebook': {
            'posts': facebook['posts'],
            'impressions': facebook['impressions'],
            'contribution_rate': (facebook['impressions'] / total_impressions * 100) if total_impressions > 0 else 0,
            'engagement_rate': facebook['engagement_rate']
        },
        'LinkedIn': {
            'posts': linkedin['posts'],
            'impressions': linkedin['impressions'],
            'contribution_rate': (linkedin['impressions'] / total_impressions * 100) if total_impressions > 0 else 0,
            'engagement_rate': linkedin['engagement_rate']
        },
        'X': {
            'posts': x['posts'],
            'impressions': x['impressions'],
            'contribution_rate': (x['impressions'] / total_impressions * 100) if total_impressions > 0 else 0,
            'engagement_rate': x['engagement_rate']
        },
        'Instagram': {
            'posts': instagram['posts'],
            'impressions': instagram['impressions'],
            'contribution_rate': (instagram['impressions'] / total_impressions * 100) if total_impressions > 0 else 0,
            'engagement_rate': instagram['engagement_rate']
        },
        'Threads': {
            'posts': threads['posts'],
            'impressions': threads.get('views', 0),  # 閲覧数をインプレッション相当として扱う
            'contribution_rate': (threads.get('views', 0) / total_impressions * 100) if total_impressions > 0 else 0,
            'engagement_rate': threads['engagement_rate']
        }
    }

    # 目標達成率
    current_monthly_imp = total_impressions  # 過去90日分なので月平均に換算する場合は /3
    target_monthly_imp = 1_000_000
    baseline_monthly_imp = 346_766

    achievement_rate = (total_impressions / target_monthly_imp * 100)
    growth_from_baseline = (total_impressions / baseline_monthly_imp * 100) - 100

    # サマリー表示
    print("【基本統計】")
    print("-" * 80)
    print(f"総投稿数: {total_posts}件")
    print(f"総インプレッション数: {total_impressions:,}")
    print(f"平均インプレッション/投稿: {total_impressions / total_posts:.0f}" if total_posts > 0 else "N/A")
    print()

    print("【目標達成状況】")
    print("-" * 80)
    print(f"現在の総インプレッション: {total_impressions:,}")
    print(f"目標月間インプレッション: {target_monthly_imp:,}")
    print(f"達成率: {achievement_rate:.1f}%")
    print(f"ベースライン（{baseline_monthly_imp:,}）からの成長: {growth_from_baseline:+.1f}%")
    print()

    print("【プラットフォーム別分析】")
    print("-" * 80)
    for platform_name, stats in platforms.items():
        print(f"{platform_name}:")
        print(f"  投稿数: {stats['posts']}件")
        print(f"  インプレッション: {stats['impressions']:,}")
        print(f"  寄与率: {stats['contribution_rate']:.1f}%")
        print(f"  エンゲージメント率: {stats['engagement_rate']:.2f}%")
        print()

    # エンゲージメント率比較
    print("【エンゲージメント率ランキング】")
    print("-" * 80)
    sorted_platforms = sorted(platforms.items(), key=lambda x: x[1]['engagement_rate'], reverse=True)
    for i, (platform_name, stats) in enumerate(sorted_platforms, 1):
        print(f"{i}. {platform_name}: {stats['engagement_rate']:.2f}%")
    print()

    # JSON出力
    result = {
        'summary': {
            'total_posts': total_posts,
            'total_impressions': total_impressions,
            'avg_impressions_per_post': float(total_impressions / total_posts) if total_posts > 0 else 0
        },
        'goal_achievement': {
            'current_impressions': total_impressions,
            'target_monthly_impressions': target_monthly_imp,
            'achievement_rate': float(achievement_rate),
            'growth_from_baseline': float(growth_from_baseline)
        },
        'platforms': platforms
    }

    output_dir = base_path / 'documents' / '2_discovery' / 'General'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / 'multi_platform_analysis.json'

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"💾 詳細結果をJSONで保存: {output_path}")
    print()
    print("✅ 処理完了")

if __name__ == '__main__':
    analyze_all_platforms()
