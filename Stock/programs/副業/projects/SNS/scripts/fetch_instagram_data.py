#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Graph API データ取得スクリプト

目的: Instagram Graph API v21.0を使用して過去90日分のデータを取得
機能:
1. メディア一覧取得
2. 各メディアのInsights取得
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
INSTAGRAM_BUSINESS_ACCOUNT_ID = os.getenv('INSTAGRAM_BUSINESS_ACCOUNT_ID')
INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')
DATA_DIR = os.getenv('DATA_DIR', str(Path(__file__).parent.parent))

# API設定
API_VERSION = 'v21.0'
BASE_URL = f'https://graph.facebook.com/{API_VERSION}'

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

def get_media_list(ig_user_id, access_token, since_timestamp, until_timestamp):
    """
    過去90日分のメディア一覧を取得

    Args:
        ig_user_id: Instagram Business Account ID
        access_token: アクセストークン
        since_timestamp: 開始日時（Unixタイムスタンプ）
        until_timestamp: 終了日時（Unixタイムスタンプ）

    Returns:
        メディアリスト
    """
    url = f"{BASE_URL}/{ig_user_id}/media"
    params = {
        'fields': 'id,caption,media_type,media_url,permalink,timestamp,username,like_count,comments_count',
        'access_token': access_token,
        'since': since_timestamp,
        'until': until_timestamp,
        'limit': 100  # 最大100件/リクエスト
    }

    all_media = []

    print("📥 メディア一覧を取得中...")

    while True:
        data = api_request(url, params)

        if not data:
            break

        if 'data' in data:
            all_media.extend(data['data'])
            print(f"   取得済み: {len(all_media)}件")

        # ページネーション処理
        if 'paging' in data and 'next' in data['paging']:
            url = data['paging']['next']
            params = {}  # nextにはパラメータ含まれているので空にする
        else:
            break

    print(f"✅ メディア一覧取得完了: {len(all_media)}件")
    return all_media

def get_media_insights(media_id, access_token, media_type):
    """
    メディアのInsightsを取得

    Args:
        media_id: メディアID
        access_token: アクセストークン
        media_type: メディアタイプ（IMAGE, VIDEO, CAROUSEL_ALBUM, REELS）

    Returns:
        Insights辞書
    """
    # メディアタイプによってメトリクスが異なる
    if media_type == 'VIDEO':
        metrics = 'impressions,reach,saved,video_views,shares'
    elif media_type == 'REELS':
        metrics = 'impressions,reach,saved,video_views,shares,plays,total_interactions'
    else:  # IMAGE, CAROUSEL_ALBUM
        metrics = 'impressions,reach,saved,shares'

    url = f"{BASE_URL}/{media_id}/insights"
    params = {
        'metric': metrics,
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

def fetch_all_instagram_data(days=90):
    """
    過去90日分のInstagramデータを取得してCSVに保存

    Args:
        days: 取得日数（デフォルト90日）
    """
    if not INSTAGRAM_BUSINESS_ACCOUNT_ID or not INSTAGRAM_ACCESS_TOKEN:
        print("❌ 環境変数が設定されていません。.envファイルを確認してください。")
        return

    # 日時範囲の計算
    until_date = datetime.now()
    since_date = until_date - timedelta(days=days)

    since_timestamp = int(since_date.timestamp())
    until_timestamp = int(until_date.timestamp())

    print(f"📅 取得期間: {since_date.strftime('%Y-%m-%d')} 〜 {until_date.strftime('%Y-%m-%d')}")
    print()

    # メディア一覧を取得
    media_list = get_media_list(
        INSTAGRAM_BUSINESS_ACCOUNT_ID,
        INSTAGRAM_ACCESS_TOKEN,
        since_timestamp,
        until_timestamp
    )

    if not media_list:
        print("⚠️  データが取得できませんでした。")
        return

    print()
    print("📊 各メディアのInsightsを取得中...")

    # 各メディアのInsightsを取得
    results = []
    for i, media in enumerate(media_list, 1):
        print(f"   取得中: {i}/{len(media_list)}件 - ID: {media['id']}")

        # Insights取得
        insights = get_media_insights(
            media['id'],
            INSTAGRAM_ACCESS_TOKEN,
            media.get('media_type', 'IMAGE')
        )

        # エンゲージメント数計算
        likes = media.get('like_count', 0)
        comments = media.get('comments_count', 0)
        saved = insights.get('saved', 0)
        shares = insights.get('shares', 0)
        total_engagement = likes + comments + saved + shares

        # エンゲージメント率計算
        impressions = insights.get('impressions', 0)
        engagement_rate = (total_engagement / impressions * 100) if impressions > 0 else 0

        # データ整形
        result = {
            '投稿ID': media['id'],
            'ユーザー名': media.get('username', ''),
            '投稿日時': media.get('timestamp', ''),
            'キャプション': media.get('caption', '')[:200] if media.get('caption') else '',  # 200文字まで
            'メディアタイプ': media.get('media_type', ''),
            'パーマリンク': media.get('permalink', ''),
            'インプレッション数': impressions,
            'リーチ数': insights.get('reach', 0),
            'エンゲージメント数': total_engagement,
            'いいね数': likes,
            'コメント数': comments,
            '保存数': saved,
            'シェア数': shares,
            'エンゲージメント率': round(engagement_rate, 2)
        }

        results.append(result)

        # レート制限対策（200リクエスト/時間）
        # 各メディアで1リクエスト消費するため、少し待機
        time.sleep(0.5)

    print(f"✅ Insights取得完了: {len(results)}件")
    print()

    # DataFrameに変換
    df = pd.DataFrame(results)

    # 投稿日時でソート（降順）
    df['投稿日時'] = pd.to_datetime(df['投稿日時'])
    df = df.sort_values('投稿日時', ascending=False)
    df['投稿日時'] = df['投稿日時'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # CSV出力
    output_dir = Path(DATA_DIR) / 'Instagram'
    output_dir.mkdir(parents=True, exist_ok=True)

    today_str = datetime.now().strftime('%Y-%m-%d')
    output_path = output_dir / f'instagram_{today_str}.csv'

    df.to_csv(output_path, index=False, encoding='utf-8-sig')

    print(f"💾 CSVファイル保存完了: {output_path}")
    print()

    # サマリー表示
    print("=" * 80)
    print("Instagram データ取得サマリー")
    print("=" * 80)
    print(f"総投稿数: {len(df)}件")
    print(f"総インプレッション数: {df['インプレッション数'].sum():,}")
    print(f"平均インプレッション数: {df['インプレッション数'].mean():.0f}")
    print(f"平均エンゲージメント率: {df['エンゲージメント率'].mean():.2f}%")
    print()

    # メディアタイプ別集計
    print("【メディアタイプ別集計】")
    for media_type in df['メディアタイプ'].unique():
        type_df = df[df['メディアタイプ'] == media_type]
        print(f"  {media_type}: {len(type_df)}件 (平均imp: {type_df['インプレッション数'].mean():.0f})")
    print()

    print("✅ 処理完了")

if __name__ == '__main__':
    fetch_all_instagram_data()
