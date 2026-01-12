#!/usr/bin/env python3
"""
Instagram歯科医院データ収集タスク
ハッシュタグ: #歯周病治療
目標: 100投稿をチェックして歯科医院データを収集
"""

from browser_collector import collect_from_hashtag, save_to_csv
import sys

def main():
    print("=" * 60)
    print("Instagram歯科医院データ収集タスク")
    print("=" * 60)
    print()

    hashtag = "歯周病治療"
    max_posts = 100

    print(f"ハッシュタグ: #{hashtag}")
    print(f"目標投稿数: {max_posts}")
    print()

    # データ収集実行
    profiles = collect_from_hashtag(
        hashtag=hashtag,
        max_posts=max_posts,
        headless=True
    )

    print()
    print("=" * 60)
    print("収集結果")
    print("=" * 60)

    if profiles:
        # CSV保存
        csv_file = save_to_csv(profiles, hashtag)

        # 統計情報
        print(f"✅ 収集完了: {len(profiles)}件")
        print(f"💾 保存先: {csv_file}")

        # 住所データ件数カウント
        address_count = sum(1 for p in profiles if p.get('address'))
        print(f"📍 住所データあり: {address_count}件")

        print()
        print("詳細:")
        for i, profile in enumerate(profiles[:5], 1):
            print(f"  {i}. {profile.get('name', 'N/A')}")
            if profile.get('address'):
                print(f"     📍 {profile['address']}")
            if profile.get('phone'):
                print(f"     📞 {profile['phone']}")

        if len(profiles) > 5:
            print(f"  ... ほか{len(profiles)-5}件")

        return 0
    else:
        print("⚠️ データなし")
        print("可能な理由:")
        print("  - Instagramクッキーが無効")
        print("  - ハッシュタグページで投稿が見つからない")
        print("  - ネットワーク接続の問題")
        return 1

if __name__ == "__main__":
    sys.exit(main())
