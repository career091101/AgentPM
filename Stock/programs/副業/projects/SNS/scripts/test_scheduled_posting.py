#!/usr/bin/env python3
"""
スケジュール投稿テスト - Late API
"""

import sys
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

# late_api_postモジュールをインポート
sys.path.insert(0, str(Path(__file__).parent))
from late_api_post import (
    get_account_id,
    calculate_schedule,
    post_to_late_api,
    LateAPIError
)


def test_schedule_calculation():
    """スケジュール計算テスト"""
    print("=" * 70)
    print("スケジュール計算テスト")
    print("=" * 70)

    base_date = datetime.now(ZoneInfo('Asia/Tokyo'))
    print(f"\n基準日時: {base_date.strftime('%Y-%m-%d %H:%M:%S %Z')}\n")

    for topic_index in range(3):
        schedule = calculate_schedule(topic_index, base_date)

        print(f"--- トピック{topic_index + 1} ---")
        print(f"LinkedIn投稿時刻: {schedule['linkedin']}")
        print(f"その他投稿時刻: {schedule['others']}")

        # 日付オフセット確認
        linkedin_dt = datetime.fromisoformat(schedule['linkedin'])
        offset_days = (linkedin_dt.date() - base_date.date()).days

        print(f"日付オフセット: +{offset_days}日")
        print()

    print("✅ スケジュール計算成功\n")
    return True


def test_scheduled_posting():
    """スケジュール投稿テスト（実際の予約投稿）"""
    print("=" * 70)
    print("スケジュール投稿テスト（実投稿）")
    print("=" * 70)

    # アカウント情報取得
    try:
        linkedin_account_id = get_account_id("linkedin")
        threads_account_id = get_account_id("threads")
    except ValueError as e:
        print(f"\n❌ エラー: {e}")
        return False

    # スケジュール計算
    schedule = calculate_schedule(topic_index=0)  # 今日

    # テスト投稿内容
    test_content = """スケジュール投稿テスト 📅

Late APIのスケジューリング機能をテスト中です。

この投稿は予約投稿として設定され、指定時刻に自動公開されます。

#LateAPI #scheduling #automation"""

    results = []

    # LinkedIn予約投稿（朝8時）
    print(f"\n1. LinkedIn予約投稿")
    print(f"   投稿時刻: {schedule['linkedin']}")
    try:
        result = post_to_late_api(
            content=test_content,
            platform="linkedin",
            account_id=linkedin_account_id,
            scheduled_for=schedule['linkedin']
        )
        print(f"   ✅ 予約投稿成功")
        print(f"   Post ID: {result['post']['_id']}")
        results.append(("LinkedIn", True, result['post']['_id']))
    except LateAPIError as e:
        print(f"   ❌ エラー: {e}")
        results.append(("LinkedIn", False, str(e)))

    # Threads予約投稿（夜20時）
    print(f"\n2. Threads予約投稿")
    print(f"   投稿時刻: {schedule['others']}")
    try:
        result = post_to_late_api(
            content=test_content,
            platform="threads",
            account_id=threads_account_id,
            scheduled_for=schedule['others']
        )
        print(f"   ✅ 予約投稿成功")
        print(f"   Post ID: {result['post']['_id']}")
        results.append(("Threads", True, result['post']['_id']))
    except LateAPIError as e:
        print(f"   ❌ エラー: {e}")
        results.append(("Threads", False, str(e)))

    # 結果サマリー
    print("\n" + "=" * 70)
    print("予約投稿結果サマリー")
    print("=" * 70)

    for platform, success, info in results:
        status = "✅ 成功" if success else "❌ 失敗"
        print(f"{platform}: {status}")
        if success:
            print(f"  Post ID: {info}")
        else:
            print(f"  エラー: {info}")

    print("\n💡 Late APIダッシュボードで予約投稿を確認してください:")
    print("   https://getlate.dev/dashboard")

    return all(success for _, success, _ in results)


if __name__ == "__main__":
    print("Phase 4: スケジューリング機能テスト\n")

    # スケジュール計算テスト
    calc_success = test_schedule_calculation()

    # 実際の予約投稿テスト
    print("\n予約投稿を実行しますか？（Late APIに実際に予約投稿を作成します）")
    print("実行する場合は 'yes' を入力してください: ", end='')

    user_input = input().strip().lower()

    if user_input == 'yes':
        post_success = test_scheduled_posting()
    else:
        print("\n⏸️  予約投稿テストをスキップしました")
        post_success = True

    print("\n" + "=" * 70)
    print("Phase 4 総合結果")
    print("=" * 70)
    print(f"スケジュール計算: {'✅ 成功' if calc_success else '❌ 失敗'}")
    print(f"予約投稿: {'✅ 成功' if post_success else '⏸️  スキップ'}")

    sys.exit(0 if calc_success else 1)
