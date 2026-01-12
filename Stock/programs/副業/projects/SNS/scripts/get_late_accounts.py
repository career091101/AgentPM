#!/usr/bin/env python3
"""
Late API経由で接続済みアカウント一覧とAccount IDを取得するスクリプト

Usage:
    python3 get_late_accounts.py
"""

import os
import sys
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# Late API設定
LATE_API_BASE_URL = "https://getlate.dev/api/v1"
LATE_API_KEY = os.getenv("LATE_API_KEY")


def get_late_accounts():
    """
    Late API経由で接続済みアカウント一覧を取得

    Returns:
        dict: アカウント情報
    """
    if not LATE_API_KEY:
        print("❌ Error: LATE_API_KEY environment variable not set")
        print("   Please set LATE_API_KEY in .env file")
        sys.exit(1)

    url = f"{LATE_API_BASE_URL}/accounts"
    headers = {
        "Authorization": f"Bearer {LATE_API_KEY}",
        "Content-Type": "application/json"
    }

    print(f"📡 Fetching accounts from Late API...")
    print(f"   URL: {url}")
    print(f"   API Key: {LATE_API_KEY[:20]}...")

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        accounts_data = response.json()
        print(f"✅ Successfully fetched accounts!\n")

        return accounts_data

    except requests.exceptions.HTTPError as e:
        print(f"❌ Late API Error: {e}")
        print(f"   Status Code: {e.response.status_code}")
        print(f"   Response: {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


def display_accounts(accounts_data):
    """
    アカウント情報を見やすく表示

    Args:
        accounts_data: Late APIからのレスポンス
    """
    accounts = accounts_data.get("accounts", [])

    if not accounts:
        print("⚠️  No accounts found. Please connect your social media accounts at https://getlate.dev/dashboard")
        return

    print("=" * 80)
    print("Connected Accounts")
    print("=" * 80)

    # プラットフォーム別にグループ化
    platform_map = {}
    for account in accounts:
        platform = account.get("platform", "unknown")
        if platform not in platform_map:
            platform_map[platform] = []
        platform_map[platform].append(account)

    # 表示
    for platform, accs in sorted(platform_map.items()):
        print(f"\n🔹 {platform.upper()}")
        print("-" * 80)
        for acc in accs:
            account_id = acc.get("_id", "N/A")
            username = acc.get("username", "N/A")
            display_name = acc.get("displayName", "N/A")
            print(f"   Account ID: {account_id}")
            print(f"   Username:   {username}")
            print(f"   Name:       {display_name}")
            print()

    print("=" * 80)


def generate_env_config(accounts_data):
    """
    .env ファイル用の設定を生成

    Args:
        accounts_data: Late APIからのレスポンス
    """
    accounts = accounts_data.get("accounts", [])

    print("\n📝 .env Configuration:")
    print("=" * 80)

    # プラットフォーム名マッピング（環境変数名用）
    platform_env_map = {
        "twitter": "LATE_TWITTER_ACCOUNT_ID",
        "linkedin": "LATE_LINKEDIN_ACCOUNT_ID",
        "facebook": "LATE_FACEBOOK_ACCOUNT_ID",
        "threads": "LATE_THREADS_ACCOUNT_ID"
    }

    for platform, env_var in platform_env_map.items():
        # 該当プラットフォームのアカウントを検索
        matching_accounts = [acc for acc in accounts if acc.get("platform") == platform]

        if matching_accounts:
            # 最初のアカウントを使用
            account_id = matching_accounts[0].get("_id", "")
            username = matching_accounts[0].get("username", "")
            print(f'{env_var}="{account_id}"  # {username}')
        else:
            print(f'{env_var}="your_{platform}_account_id_here"  # Not connected yet')

    print("=" * 80)
    print("\n💡 Copy the above lines to your .env file")


def save_accounts_json(accounts_data):
    """
    アカウント情報をJSONファイルに保存

    Args:
        accounts_data: Late APIからのレスポンス
    """
    data_dir = Path(__file__).parent.parent / "data"
    output_file = data_dir / "late_accounts.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(accounts_data, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Account data saved to: {output_file}")


def main():
    # アカウント一覧取得
    accounts_data = get_late_accounts()

    # 表示
    display_accounts(accounts_data)

    # .env設定生成
    generate_env_config(accounts_data)

    # JSON保存
    save_accounts_json(accounts_data)


if __name__ == "__main__":
    main()
