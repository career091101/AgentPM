#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3媒体（LinkedIn/Facebook/X）投稿時間帯分析スクリプト
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime
from collections import Counter

def analyze_linkedin_times(csv_path: str) -> dict:
    """LinkedInエンゲージメントCSVから投稿時間帯を分析"""
    try:
        df = pd.read_csv(csv_path, encoding='utf-8-sig')

        # 日付列を確認
        date_col = df.columns[0]  # 最初の列が日付のはず
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

        # 時間帯別の集計（日付のみのデータの場合は時間帯不明）
        hours = df[date_col].dt.hour.dropna()

        if len(hours) == 0:
            return {
                'platform': 'LinkedIn',
                'total_posts': len(df),
                'time_data_available': False,
                'note': '時刻データが含まれていないため、日付のみで分析'
            }

        hour_distribution = Counter(hours)

        return {
            'platform': 'LinkedIn',
            'total_posts': len(df),
            'time_data_available': True,
            'hour_distribution': dict(hour_distribution),
            'peak_hours': sorted(hour_distribution.items(), key=lambda x: x[1], reverse=True)[:3],
            'morning_6_12': sum(1 for h in hours if 6 <= h < 12),
            'afternoon_12_18': sum(1 for h in hours if 12 <= h < 18),
            'evening_18_22': sum(1 for h in hours if 18 <= h < 22),
            'night_22_6': sum(1 for h in hours if h >= 22 or h < 6)
        }

    except Exception as e:
        return {'platform': 'LinkedIn', 'error': str(e)}

def analyze_facebook_times(csv_path: str) -> dict:
    """Facebook CSVから投稿時間帯を分析"""
    try:
        df = pd.read_csv(csv_path, encoding='utf-8-sig')

        # '公開時間'または'公開日時'列を探す
        date_cols = [col for col in df.columns if '公開時間' in col or '公開日時' in col or '日時' in col or 'date' in col.lower()]

        if not date_cols:
            return {
                'platform': 'Facebook',
                'error': '日時列が見つかりませんでした',
                'available_columns': list(df.columns)
            }

        date_col = date_cols[0]
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

        # 時間帯別の集計
        hours = df[date_col].dt.hour.dropna()

        if len(hours) == 0:
            return {
                'platform': 'Facebook',
                'total_posts': len(df),
                'time_data_available': False
            }

        hour_distribution = Counter(hours)

        return {
            'platform': 'Facebook',
            'total_posts': len(df),
            'time_data_available': True,
            'hour_distribution': dict(hour_distribution),
            'peak_hours': sorted(hour_distribution.items(), key=lambda x: x[1], reverse=True)[:3],
            'morning_6_12': sum(1 for h in hours if 6 <= h < 12),
            'afternoon_12_18': sum(1 for h in hours if 12 <= h < 18),
            'evening_18_22': sum(1 for h in hours if 18 <= h < 22),
            'night_22_6': sum(1 for h in hours if h >= 22 or h < 6)
        }

    except Exception as e:
        return {'platform': 'Facebook', 'error': str(e)}

def analyze_x_times(csv_path: str) -> dict:
    """X（Twitter）CSVから投稿時間帯を分析"""
    try:
        df = pd.read_csv(csv_path, encoding='utf-8-sig')

        # '時刻'または'time'列を探す
        date_cols = [col for col in df.columns if '時刻' in col or 'time' in col.lower() or 'date' in col.lower()]

        if not date_cols:
            return {
                'platform': 'X',
                'error': '日時列が見つかりませんでした',
                'available_columns': list(df.columns[:10])
            }

        date_col = date_cols[0]
        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')

        # 時間帯別の集計
        hours = df[date_col].dt.hour.dropna()

        if len(hours) == 0:
            return {
                'platform': 'X',
                'total_posts': len(df),
                'time_data_available': False
            }

        hour_distribution = Counter(hours)

        return {
            'platform': 'X',
            'total_posts': len(df),
            'time_data_available': True,
            'hour_distribution': dict(hour_distribution),
            'peak_hours': sorted(hour_distribution.items(), key=lambda x: x[1], reverse=True)[:3],
            'morning_6_12': sum(1 for h in hours if 6 <= h < 12),
            'afternoon_12_18': sum(1 for h in hours if 12 <= h < 18),
            'evening_18_22': sum(1 for h in hours if 18 <= h < 22),
            'night_22_6': sum(1 for h in hours if h >= 22 or h < 6)
        }

    except Exception as e:
        return {'platform': 'X', 'error': str(e)}

def main():
    base_path = Path('/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS')

    # LinkedIn分析
    linkedin_csv = base_path / 'LinkedIn' / 'linkedin_エンゲージメント.csv'
    linkedin_result = analyze_linkedin_times(str(linkedin_csv))

    # Facebook分析
    facebook_csv = list((base_path / 'Facebook').glob('*.csv'))[0]  # 最初のCSVファイル
    facebook_result = analyze_facebook_times(str(facebook_csv))

    # X分析
    x_csv = base_path / 'X' / 'account_analytics_content_2025-10-03_2025-12-31.csv'
    x_result = analyze_x_times(str(x_csv))

    # 結果を統合
    results = {
        'linkedin': linkedin_result,
        'facebook': facebook_result,
        'x': x_result
    }

    # コンソール出力
    print("=" * 80)
    print("3媒体 投稿時間帯分析レポート")
    print("=" * 80)
    print()

    for platform_name, result in results.items():
        print(f"【{result.get('platform', platform_name.upper())}】")
        print("-" * 80)

        if 'error' in result:
            print(f"エラー: {result['error']}")
            if 'available_columns' in result:
                print(f"利用可能な列: {result['available_columns'][:5]}...")
        elif not result.get('time_data_available', True):
            print(f"総投稿数: {result.get('total_posts', 'N/A')}")
            print(f"時刻データ: 利用不可")
            print(f"備考: {result.get('note', 'データに時刻情報が含まれていません')}")
        else:
            print(f"総投稿数: {result['total_posts']}")
            print()
            print("時間帯別分布:")
            print(f"  朝(6-12時): {result['morning_6_12']}投稿 ({result['morning_6_12']/result['total_posts']*100:.1f}%)")
            print(f"  昼(12-18時): {result['afternoon_12_18']}投稿 ({result['afternoon_12_18']/result['total_posts']*100:.1f}%)")
            print(f"  夜(18-22時): {result['evening_18_22']}投稿 ({result['evening_18_22']/result['total_posts']*100:.1f}%)")
            print(f"  深夜(22-6時): {result['night_22_6']}投稿 ({result['night_22_6']/result['total_posts']*100:.1f}%)")
            print()
            print("ピーク時間帯 Top 3:")
            for rank, (hour, count) in enumerate(result['peak_hours'], 1):
                print(f"  {rank}. {hour:02d}時台: {count}投稿")

        print()

    # JSON出力
    output_path = base_path / 'General' / 'posting_time_analysis.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"詳細結果をJSONで保存: {output_path}")

if __name__ == '__main__':
    main()
