#!/usr/bin/env python3
"""
プラットフォーム別スケジュール投稿テスト

LinkedIn（朝8時）とその他SNS（夜20時）を異なる時刻に予約投稿
"""

import sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).parent))
from late_api_post import (
    get_account_id,
    calculate_schedule,
    post_to_late_api,
    LateAPIError
)


def test_different_schedule_posting():
    """プラットフォーム別スケジュール投稿テスト"""

    print("=" * 70)
    print("プラットフォーム別スケジュール投稿テスト")
    print("=" * 70)

    # アカウント情報取得
    try:
        linkedin_account_id = get_account_id("linkedin")
        twitter_account_id = get_account_id("twitter")
        threads_account_id = get_account_id("threads")
    except ValueError as e:
        print(f"\n❌ エラー: {e}")
        return False

    # スケジュール計算（トピック1 = 今日）
    schedule = calculate_schedule(topic_index=0)

    print(f"\n📅 投稿スケジュール:")
    print(f"  LinkedIn: {schedule['linkedin']}")
    print(f"  その他:   {schedule['others']}")

    # テスト投稿内容
    test_content = """プラットフォーム別スケジュール投稿テスト 🕐

この投稿は、プラットフォームごとに異なる時刻に予約投稿されています。

- LinkedIn: 朝8:00
- X (Twitter): 夜20:00
- Threads: 夜20:00

Late APIの柔軟なスケジューリング機能を活用した例です。

#LateAPI #scheduling #automation"""

    results = []

    # LinkedIn投稿（朝8時）
    print(f"\n1️⃣ LinkedIn予約投稿")
    print(f"   投稿時刻: {schedule['linkedin']}")
    try:
        result = post_to_late_api(
            content=test_content,
            platform="linkedin",
            account_id=linkedin_account_id,
            scheduled_for=schedule['linkedin']
        )
        post_id = result['post']['_id']
        print(f"   ✅ 予約成功 - Post ID: {post_id}")
        results.append(("LinkedIn", True, post_id, schedule['linkedin']))
    except LateAPIError as e:
        print(f"   ❌ エラー: {e}")
        results.append(("LinkedIn", False, str(e), schedule['linkedin']))

    # X (Twitter) 投稿（夜20時）
    print(f"\n2️⃣ X (Twitter) 予約投稿")
    print(f"   投稿時刻: {schedule['others']}")
    try:
        result = post_to_late_api(
            content=test_content,
            platform="twitter",
            account_id=twitter_account_id,
            scheduled_for=schedule['others']
        )
        post_id = result['post']['_id']
        print(f"   ✅ 予約成功 - Post ID: {post_id}")
        results.append(("X (Twitter)", True, post_id, schedule['others']))
    except LateAPIError as e:
        print(f"   ❌ エラー: {e}")
        results.append(("X (Twitter)", False, str(e), schedule['others']))

    # Threads投稿（夜20時）
    print(f"\n3️⃣ Threads予約投稿")
    print(f"   投稿時刻: {schedule['others']}")
    try:
        result = post_to_late_api(
            content=test_content,
            platform="threads",
            account_id=threads_account_id,
            scheduled_for=schedule['others']
        )
        post_id = result['post']['_id']
        print(f"   ✅ 予約成功 - Post ID: {post_id}")
        results.append(("Threads", True, post_id, schedule['others']))
    except LateAPIError as e:
        print(f"   ❌ エラー: {e}")
        results.append(("Threads", False, str(e), schedule['others']))

    # 結果サマリー
    print("\n" + "=" * 70)
    print("予約投稿結果サマリー")
    print("=" * 70)

    for platform, success, info, scheduled_time in results:
        status = "✅ 成功" if success else "❌ 失敗"
        print(f"\n{platform}: {status}")
        print(f"  予約時刻: {scheduled_time}")
        if success:
            print(f"  Post ID: {info}")
        else:
            print(f"  エラー: {info}")

    # タイムラインの可視化
    print("\n" + "=" * 70)
    print("投稿タイムライン 📊")
    print("=" * 70)

    # 予約投稿の時刻を解析
    linkedin_time = datetime.fromisoformat(schedule['linkedin'])
    others_time = datetime.fromisoformat(schedule['others'])

    print(f"""
{linkedin_time.strftime('%Y-%m-%d')}
├─ {linkedin_time.strftime('%H:%M')} - LinkedIn投稿
│
└─ {others_time.strftime('%H:%M')} - X (Twitter), Threads投稿

時間差: {(others_time - linkedin_time).seconds // 3600}時間
    """)

    print("\n💡 Late APIダッシュボードで確認:")
    print("   https://getlate.dev/dashboard")

    return all(success for _, success, _, _ in results)


if __name__ == "__main__":
    print("LinkedIn vs その他SNS - 異なる時刻での予約投稿テスト\n")

    print("このテストは実際にLate APIに予約投稿を作成します。")
    print("実行しますか？ [yes/no]: ", end='')

    user_input = input().strip().lower()

    if user_input == 'yes':
        success = test_different_schedule_posting()

        if success:
            print("\n🎉 全てのプラットフォームで予約投稿が成功しました！")
        else:
            print("\n⚠️  一部のプラットフォームで失敗しました")

        sys.exit(0 if success else 1)
    else:
        print("\n⏸️  テストをキャンセルしました")
        sys.exit(0)
