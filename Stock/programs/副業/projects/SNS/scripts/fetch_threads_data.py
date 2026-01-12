#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Threads API データ取得スクリプト

目的: Threads APIを使用して過去90日分のデータを取得
機能:
1. 投稿一覧取得
2. 各投稿のInsights取得
3. CSV形式でエクスポート
4. レート制限対応（指数バックオフ）
"""

import os
import time
import requests
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv

# .envファイルを読み込み
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# 環境変数から認証情報を取得
THREADS_USER_ID = os.getenv('THREADS_USER_ID')
THREADS_ACCESS_TOKEN = os.getenv('THREADS_ACCESS_TOKEN')
DATA_DIR = os.getenv('DATA_DIR', str(Path(__file__).parent.parent))

# API設定
API_VERSION = 'v1.0'
BASE_URL = f'https://graph.threads.net/{API_VERSION}'

def exponential_backoff(attempt, max_wait=60):
    """指数バックオフ計算"""
    wait_time = min(2 ** attempt, max_wait)
    return wait_time

def api_request(url, params, max_retries=5):
    """
    API呼び出しとレート制限対応

    Args:
        url: APIエンドポイントURL
        params: リクエストパラメータ
        max_retries: 最大リトライ回数

    Returns:
        JSONレスポンス
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=30)

            # レート制限エラー（HTTP 429）
            if response.status_code == 429:
                wait_time = exponential_backoff(attempt)
                print(f"⚠️  レート制限エラー。{wait_time}秒待機中...")
                time.sleep(wait_time)
                continue

            # その他のエラー
            if response.status_code != 200:
                print(f"❌ エラー: {response.status_code} - {response.text}")
                return None

            return response.json()

        except requests.exceptions.Timeout:
            print(f"⚠️  タイムアウト。リトライ {attempt + 1}/{max_retries}")
            time.sleep(exponential_backoff(attempt))

        except requests.exceptions.RequestException as e:
            print(f"❌ ネットワークエラー: {e}")
            return None

    print(f"❌ 最大リトライ回数に達しました。")
    return None

def get_threads_list(threads_user_id, access_token, since_timestamp, until_timestamp):
    """
    過去90日分のThreads投稿一覧を取得

    Args:
        threads_user_id: Threads User ID
        access_token: アクセストークン
        since_timestamp: 開始日時（Unixタイムスタンプ）
        until_timestamp: 終了日時（Unixタイムスタンプ）

    Returns:
        投稿リスト
    """
    url = f"{BASE_URL}/{threads_user_id}/threads"
    params = {
        'fields': 'id,text,timestamp,permalink,media_type,media_url,username',
        'access_token': access_token,
        'since': since_timestamp,
        'until': until_timestamp,
        'limit': 100  # 最大100件/リクエスト
    }

    all_threads = []

    print("📥 Threads投稿一覧を取得中...")

    while True:
        data = api_request(url, params)

        if not data:
            break

        if 'data' in data:
            all_threads.extend(data['data'])
            print(f"   取得済み: {len(all_threads)}件")

        # ページネーション処理
        if 'paging' in data and 'next' in data['paging']:
            url = data['paging']['next']
            params = {}  # nextにはパラメータ含まれているので空にする
        else:
            break

    print(f"✅ Threads投稿一覧取得完了: {len(all_threads)}件")
    return all_threads

def get_threads_insights(thread_id, access_token):
    """
    Threads投稿のInsightsを取得

    Args:
        thread_id: Threads投稿ID
        access_token: アクセストークン

    Returns:
        Insights辞書
    """
    url = f"{BASE_URL}/{thread_id}/insights"
    params = {
        'metric': 'views,likes,replies,reposts,quotes,shares',
        'access_token': access_token
    }

    data = api_request(url, params)

    if not data or 'data' not in data:
        return {}

    # Insightsを辞書形式に変換
    insights = {}
    for item in data['data']:
        metric_name = item['name']
        metric_value = item['values'][0]['value'] if item['values'] else 0
        insights[metric_name] = metric_value

    return insights

def fetch_all_threads_data(days=90):
    """
    過去90日分のThreadsデータを取得してCSVに保存

    Args:
        days: 取得日数（デフォルト90日）
    """
    if not THREADS_USER_ID or not THREADS_ACCESS_TOKEN:
        print("❌ 環境変数が設定されていません。.envファイルを確認してください。")
        return

    # 日時範囲の計算
    until_date = datetime.now()
    since_date = until_date - timedelta(days=days)

    since_timestamp = int(since_date.timestamp())
    until_timestamp = int(until_date.timestamp())

    print(f"📅 取得期間: {since_date.strftime('%Y-%m-%d')} 〜 {until_date.strftime('%Y-%m-%d')}")
    print()

    # 投稿一覧を取得
    threads_list = get_threads_list(
        THREADS_USER_ID,
        THREADS_ACCESS_TOKEN,
        since_timestamp,
        until_timestamp
    )

    if not threads_list:
        print("⚠️  データが取得できませんでした。")
        return

    print()
    print("📊 各投稿のInsightsを取得中...")

    # 各投稿のInsightsを取得
    results = []
    for i, thread in enumerate(threads_list, 1):
        print(f"   取得中: {i}/{len(threads_list)}件 - ID: {thread['id']}")

        # Insights取得
        insights = get_threads_insights(
            thread['id'],
            THREADS_ACCESS_TOKEN
        )

        # エンゲージメント数計算
        likes = insights.get('likes', 0)
        replies = insights.get('replies', 0)
        reposts = insights.get('reposts', 0)
        quotes = insights.get('quotes', 0)
        shares = insights.get('shares', 0)
        total_engagement = likes + replies + reposts + quotes + shares

        # エンゲージメント率計算（閲覧数ベース）
        views = insights.get('views', 0)
        engagement_rate = (total_engagement / views * 100) if views > 0 else 0

        # データ整形
        result = {
            '投稿ID': thread['id'],
            'ユーザー名': thread.get('username', ''),
            '投稿日時': thread.get('timestamp', ''),
            'テキスト': thread.get('text', '')[:200] if thread.get('text') else '',  # 200文字まで
            'メディアタイプ': thread.get('media_type', 'TEXT'),
            'パーマリンク': thread.get('permalink', ''),
            '閲覧数': views,
            'いいね数': likes,
            '返信数': replies,
            'リポスト数': reposts,
            '引用数': quotes,
            'シェア数': shares,
            'エンゲージメント数': total_engagement,
            'エンゲージメント率': round(engagement_rate, 2)
        }

        results.append(result)

        # レート制限対策
        time.sleep(0.1)

    print(f"✅ Insights取得完了: {len(results)}件")
    print()

    # DataFrameに変換
    df = pd.DataFrame(results)

    # 投稿日時でソート（降順）
    df['投稿日時'] = pd.to_datetime(df['投稿日時'])
    df = df.sort_values('投稿日時', ascending=False)
    df['投稿日時'] = df['投稿日時'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # CSV出力
    output_dir = Path(DATA_DIR) / 'Threads'
    output_dir.mkdir(parents=True, exist_ok=True)

    today_str = datetime.now().strftime('%Y-%m-%d')
    output_path = output_dir / f'threads_{today_str}.csv'

    df.to_csv(output_path, index=False, encoding='utf-8-sig')

    print(f"💾 CSVファイル保存完了: {output_path}")
    print()

    # サマリー表示
    print("=" * 80)
    print("Threads データ取得サマリー")
    print("=" * 80)
    print(f"総投稿数: {len(df)}件")
    print(f"総閲覧数: {df['閲覧数'].sum():,}")
    print(f"平均閲覧数: {df['閲覧数'].mean():.0f}")
    print(f"平均エンゲージメント率: {df['エンゲージメント率'].mean():.2f}%")
    print()

    # メディアタイプ別集計
    print("【メディアタイプ別集計】")
    for media_type in df['メディアタイプ'].unique():
        type_df = df[df['メディアタイプ'] == media_type]
        print(f"  {media_type}: {len(type_df)}件 (平均閲覧数: {type_df['閲覧数'].mean():.0f})")
    print()

    print("✅ 処理完了")

if __name__ == '__main__':
    fetch_all_threads_data()
