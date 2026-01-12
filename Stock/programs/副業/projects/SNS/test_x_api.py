#!/usr/bin/env python3
"""
X API認証情報のテストスクリプト

使い方:
1. 環境変数を読み込む: source load_env.sh
2. このスクリプトを実行: python test_x_api.py
"""

import os
import sys

def test_x_api_credentials():
    """X API認証情報の確認"""
    print("=" * 50)
    print("X API認証情報テスト")
    print("=" * 50)
    print()

    # 環境変数の確認
    required_vars = [
        "X_BEARER_TOKEN",
        "X_API_KEY",
        "X_API_SECRET",
        "X_ACCESS_TOKEN",
        "X_ACCESS_TOKEN_SECRET"
    ]

    missing_vars = []
    for var in required_vars:
        value = os.environ.get(var)
        if not value or value.startswith("your_"):
            missing_vars.append(var)
            print(f"❌ {var}: 未設定")
        else:
            # トークンの最初の10文字のみ表示
            masked_value = value[:15] + "..." if len(value) > 15 else value
            print(f"✅ {var}: {masked_value}")

    print()

    if missing_vars:
        print(f"⚠️  以下の環境変数が設定されていません: {', '.join(missing_vars)}")
        print("   .envファイルを確認してください。")
        return False

    # tweepyのインポート確認
    try:
        import tweepy
        print("✅ tweepy ライブラリ: インストール済み")
    except ImportError:
        print("❌ tweepy ライブラリ: 未インストール")
        print("   インストールコマンド: pip install tweepy")
        return False

    print()
    print("=" * 50)
    print("認証情報テスト")
    print("=" * 50)
    print()

    try:
        # Tweepy Clientの作成
        client = tweepy.Client(
            bearer_token=os.environ.get("X_BEARER_TOKEN"),
            consumer_key=os.environ.get("X_API_KEY"),
            consumer_secret=os.environ.get("X_API_SECRET"),
            access_token=os.environ.get("X_ACCESS_TOKEN"),
            access_token_secret=os.environ.get("X_ACCESS_TOKEN_SECRET")
        )

        # 自分のユーザー情報を取得（認証テスト）
        print("📡 X APIに接続中...")
        me = client.get_me()

        if me.data:
            print(f"✅ 認証成功！")
            print(f"   ユーザー名: @{me.data.username}")
            print(f"   ユーザーID: {me.data.id}")
            print(f"   名前: {me.data.name}")
            print()
            print("🎉 X API認証情報は正しく設定されています！")
            print("   approve-and-scheduleスキルでX投稿が可能です。")
            return True
        else:
            print("❌ 認証失敗: ユーザー情報を取得できませんでした")
            return False

    except tweepy.errors.Unauthorized as e:
        print(f"❌ 認証エラー: {e}")
        print("   認証情報が正しくない可能性があります。")
        print("   .envファイルの内容を確認してください。")
        return False
    except tweepy.errors.Forbidden as e:
        print(f"❌ 権限エラー: {e}")
        print("   App Permissionsが「Read and write」になっているか確認してください。")
        return False
    except Exception as e:
        print(f"❌ エラー: {e}")
        return False

if __name__ == "__main__":
    success = test_x_api_credentials()
    sys.exit(0 if success else 1)
