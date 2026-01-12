#!/usr/bin/env python3
"""
Late API セットアップスクリプト
- APIキー接続テスト
- 接続済みアカウント一覧取得
- テスト投稿（オプション）
"""

import requests
import json
from datetime import datetime, timedelta
import os

# Late API設定
API_KEY = "sk_25a52d19aa714c4811832be20a11717c27c3b77c59c1d0df62f270609429cff4"
BASE_URL = "https://getlate.dev/api/v1"

def get_headers():
    """APIリクエストヘッダー"""
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

def test_connection():
    """APIキー接続テスト"""
    print("=" * 60)
    print("Late API 接続テスト")
    print("=" * 60)

    try:
        # プロフィール一覧取得で接続テスト
        response = requests.get(
            f"{BASE_URL}/profiles",
            headers=get_headers()
        )

        print(f"ステータスコード: {response.status_code}")

        if response.status_code == 200:
            print("✅ API接続成功")
            return True
        else:
            print(f"❌ API接続失敗: {response.text}")
            return False

    except Exception as e:
        print(f"❌ エラー: {e}")
        return False

def get_profiles():
    """プロフィール一覧取得"""
    print("\n" + "=" * 60)
    print("プロフィール一覧取得")
    print("=" * 60)

    try:
        response = requests.get(
            f"{BASE_URL}/profiles",
            headers=get_headers()
        )

        if response.status_code == 200:
            profiles = response.json()
            print(f"\n取得したプロフィール数: {len(profiles)}")

            for profile in profiles:
                print(f"\n📁 プロフィール: {profile.get('name', 'N/A')}")
                print(f"   ID: {profile.get('_id', 'N/A')}")

            return profiles
        else:
            print(f"❌ プロフィール取得失敗: {response.text}")
            return []

    except Exception as e:
        print(f"❌ エラー: {e}")
        return []

def get_accounts(profile_id=None):
    """接続済みアカウント一覧取得"""
    print("\n" + "=" * 60)
    print("接続済みアカウント一覧取得")
    print("=" * 60)

    try:
        url = f"{BASE_URL}/accounts"
        if profile_id:
            url += f"?profileId={profile_id}"

        response = requests.get(url, headers=get_headers())

        if response.status_code == 200:
            accounts = response.json()
            print(f"\n取得したアカウント数: {len(accounts)}")

            # プラットフォーム別に整理
            platform_accounts = {}
            for account in accounts:
                platform = account.get('platform', 'unknown')
                if platform not in platform_accounts:
                    platform_accounts[platform] = []
                platform_accounts[platform].append(account)

            # 表示
            for platform, accts in platform_accounts.items():
                print(f"\n🌐 {platform.upper()}")
                for acct in accts:
                    print(f"   - {acct.get('displayName', 'N/A')} (@{acct.get('username', 'N/A')})")
                    print(f"     Account ID: {acct.get('_id', 'N/A')}")

            return accounts
        else:
            print(f"❌ アカウント取得失敗: {response.text}")
            return []

    except Exception as e:
        print(f"❌ エラー: {e}")
        return []

def save_config(profiles, accounts):
    """設定をJSONファイルに保存"""
    config_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/config/late_api_config.json"

    os.makedirs(os.path.dirname(config_path), exist_ok=True)

    config = {
        "api_key": API_KEY,
        "base_url": BASE_URL,
        "profiles": profiles,
        "accounts": accounts,
        "updated_at": datetime.now().isoformat()
    }

    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print(f"\n✅ 設定を保存しました: {config_path}")

def create_test_post_draft():
    """テスト投稿のドラフト作成（実際には投稿しない）"""
    print("\n" + "=" * 60)
    print("テスト投稿ドラフト作成")
    print("=" * 60)

    # 投稿データ例（JSONファイルから読み込んだ案2を使用）
    post_content = """「Elon Muskは、マジで異次元のエンジニアだ」

$3兆企業NVIDIAのCEO Jensen Huangが、ここまで言い切った。

「extraordinary engineer」——この言葉の意味がわかるだろうか。

半導体業界の頂点に立つ男が、Tesla創業者を「一緒に仕事ができて嬉しい」と公言。
そしてOptimus（テスラのヒューマノイドロボット）を「次の数兆ドル産業」と断言した。

これはヤバい。

【Jensen Huangの予測】
・2026年末：Optimus年間100万台生産体制
・目標価格：$20,000〜$30,000
・5年以内：工場でのヒューマノイドロボット標準化
・「ロボティクスの10年」が始まる

（中略）

#HumanoidRobot #Tesla"""

    # 予約投稿時刻（明日の朝8時）
    tomorrow_8am = datetime.now() + timedelta(days=1)
    tomorrow_8am = tomorrow_8am.replace(hour=8, minute=0, second=0, microsecond=0)

    draft_post = {
        "content": post_content[:280],  # 最初の280文字のみ（例）
        "scheduledFor": tomorrow_8am.isoformat(),
        "timezone": "Asia/Tokyo",
        "platforms": [
            # {"platform": "twitter", "accountId": "TWITTER_ACCOUNT_ID"},
            # {"platform": "linkedin", "accountId": "LINKEDIN_ACCOUNT_ID"},
            # {"platform": "facebook", "accountId": "FACEBOOK_ACCOUNT_ID"}
        ]
    }

    print("\n📝 投稿ドラフト:")
    print(json.dumps(draft_post, indent=2, ensure_ascii=False))
    print("\n⚠️  実際の投稿には、上記のplatformsにAccount IDを設定してください")

    return draft_post

def main():
    """メイン処理"""
    print("\n🚀 Late API セットアップ開始\n")

    # 1. 接続テスト
    if not test_connection():
        print("\n❌ セットアップ失敗: API接続に問題があります")
        return

    # 2. プロフィール取得
    profiles = get_profiles()

    # 3. アカウント取得
    profile_id = profiles[0]['_id'] if profiles else None
    accounts = get_accounts(profile_id)

    # 4. 設定保存
    save_config(profiles, accounts)

    # 5. テスト投稿ドラフト作成
    create_test_post_draft()

    print("\n" + "=" * 60)
    print("✅ セットアップ完了")
    print("=" * 60)
    print("\n次のステップ:")
    print("1. config/late_api_config.json を確認")
    print("2. アカウントIDを使って投稿スクリプト作成")
    print("3. 予約投稿テスト実行")
    print()

if __name__ == "__main__":
    main()
