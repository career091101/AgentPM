#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram/Threads アクセストークン更新スクリプト

目的: 長期アクセストークン（60日間有効）を自動更新
機能:
1. .envファイルから現在のトークンを読み込み
2. トークンリフレッシュAPIを呼び出し
3. 新しいトークンを.envファイルに自動書き込み
4. 実行結果を表示

実行タイミング:
- トークン発行から24時間以上経過後、かつ60日以内
- 推奨: 月1回の手動実行
"""

import os
import requests
from pathlib import Path
from dotenv import load_dotenv, set_key

# .envファイルを読み込み
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# 環境変数から認証情報を取得
INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')
THREADS_ACCESS_TOKEN = os.getenv('THREADS_ACCESS_TOKEN')

# API設定
REFRESH_URL = 'https://graph.instagram.com/refresh_access_token'

def refresh_access_token(current_token: str) -> dict:
    """
    アクセストークンをリフレッシュ

    Args:
        current_token: 現在の長期アクセストークン

    Returns:
        レスポンス辞書
    """
    params = {
        'grant_type': 'ig_refresh_token',
        'access_token': current_token
    }

    try:
        response = requests.get(REFRESH_URL, params=params, timeout=30)

        if response.status_code != 200:
            print(f"❌ エラー: {response.status_code}")
            print(f"   レスポンス: {response.text}")
            return None

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"❌ ネットワークエラー: {e}")
        return None

def update_env_token(env_key: str, new_token: str):
    """
    .envファイルのトークンを更新

    Args:
        env_key: 環境変数のキー名
        new_token: 新しいアクセストークン
    """
    set_key(env_path, env_key, new_token)
    print(f"✅ .envファイルを更新しました: {env_key}")

def main():
    print("=" * 80)
    print("Instagram/Threads アクセストークン更新")
    print("=" * 80)
    print()

    if not INSTAGRAM_ACCESS_TOKEN:
        print("❌ INSTAGRAM_ACCESS_TOKENが設定されていません。")
        return

    # Instagram/Threadsは同じトークンを使用する
    print("🔄 Instagramアクセストークンをリフレッシュ中...")
    result = refresh_access_token(INSTAGRAM_ACCESS_TOKEN)

    if not result:
        print("❌ トークンのリフレッシュに失敗しました。")
        print()
        print("原因候補:")
        print("1. トークンが既に期限切れ（60日経過）")
        print("2. トークン発行から24時間未満（リフレッシュ不可期間）")
        print("3. ネットワークエラー")
        print()
        print("対処法:")
        print("1. Meta for Developersで新しいトークンを取得")
        print("2. .envファイルのINSTAGRAM_ACCESS_TOKENを手動更新")
        return

    # 新しいトークンを取得
    new_token = result.get('access_token')
    expires_in = result.get('expires_in')
    token_type = result.get('token_type')

    if not new_token:
        print("❌ 新しいトークンが取得できませんでした。")
        return

    print(f"✅ 新しいトークンを取得しました")
    print(f"   トークンタイプ: {token_type}")
    print(f"   有効期限: {expires_in}秒 ({expires_in / 86400:.0f}日)")
    print()

    # .envファイルを更新
    print("💾 .envファイルを更新中...")
    update_env_token('INSTAGRAM_ACCESS_TOKEN', new_token)
    update_env_token('THREADS_ACCESS_TOKEN', new_token)  # Instagram/Threadsは同じトークン

    print()
    print("✅ トークン更新完了")
    print()
    print("次回の更新推奨日: 約30日後")

if __name__ == '__main__':
    main()
