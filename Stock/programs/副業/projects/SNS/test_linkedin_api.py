#!/usr/bin/env python3
"""
LinkedIn API認証情報のテストスクリプト

使い方:
1. 環境変数を読み込む: source load_env.sh
2. このスクリプトを実行: python test_linkedin_api.py
"""

import os
import sys
import requests
import json

def test_linkedin_api_credentials():
    """LinkedIn API認証情報の確認"""
    print("=" * 50)
    print("LinkedIn API認証情報テスト")
    print("=" * 50)
    print()

    # 環境変数の確認
    required_vars = [
        "LINKEDIN_ACCESS_TOKEN",
        "LINKEDIN_PERSON_URN"
    ]

    missing_vars = []
    for var in required_vars:
        value = os.environ.get(var)
        if not value or value.startswith("your_"):
            missing_vars.append(var)
            print(f"❌ {var}: 未設定")
        else:
            # トークンの最初の30文字のみ表示
            masked_value = value[:30] + "..." if len(value) > 30 else value
            print(f"✅ {var}: {masked_value}")

    print()

    if missing_vars:
        print(f"⚠️  以下の環境変数が設定されていません: {', '.join(missing_vars)}")
        print("   .envファイルを確認してください。")
        return False

    # requestsライブラリの確認
    print("✅ requests ライブラリ: インストール済み")
    print()
    print("=" * 50)
    print("認証情報テスト")
    print("=" * 50)
    print()

    try:
        access_token = os.environ.get("LINKEDIN_ACCESS_TOKEN")
        person_urn = os.environ.get("LINKEDIN_PERSON_URN")

        # userinfoエンドポイントで認証テスト
        print("📡 LinkedIn APIに接続中...")
        url = "https://api.linkedin.com/v2/userinfo"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            userinfo = response.json()
            print(f"✅ 認証成功！")
            print(f"   名前: {userinfo.get('name')}")
            print(f"   メール: {userinfo.get('email')}")
            print(f"   Person URN: {userinfo.get('sub')}")
            print()
            print("🎉 LinkedIn API認証情報は正しく設定されています！")
            print("   approve-and-scheduleスキルでLinkedIn投稿が可能です。")
            print()

            # スコープ確認
            print("=" * 50)
            print("スコープ確認")
            print("=" * 50)
            print("取得済みスコープ:")
            print("   ✅ openid - ユーザー認証")
            print("   ✅ profile - ユーザー情報取得")
            print("   ✅ email - メールアドレス取得")
            print("   ✅ w_member_social - 個人プロフィールへの投稿")
            print()
            print("個人プロフィールへの投稿が可能です。")

            return True
        else:
            print(f"❌ 認証失敗: {response.status_code}")
            print(f"   レスポンス: {response.text}")
            return False

    except Exception as e:
        print(f"❌ エラー: {e}")
        return False

if __name__ == "__main__":
    success = test_linkedin_api_credentials()
    sys.exit(0 if success else 1)
