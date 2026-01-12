#!/usr/bin/env python3
"""
東京歯科ハッシュタグで100投稿をチェック
"""
import sys
from browser_collector import collect_from_hashtag, save_to_csv
from datetime import datetime

def main():
    print("\n" + "="*60)
    print("Instagram歯科医院データ収集")
    print("="*60)
    print(f"時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"ハッシュタグ: #東京歯科")
    print(f"目標投稿数: 100")
    print("="*60 + "\n")
    
    # 実行
    profiles = collect_from_hashtag(
        hashtag="東京歯科",
        max_posts=100,
        headless=True
    )
    
    # 結果報告
    print("\n" + "="*60)
    print("実行結果")
    print("="*60)
    
    if profiles:
        csv_file = save_to_csv(profiles, "東京歯科")
        
        # 統計情報
        print(f"✅ 収集完了: {len(profiles)}件")
        print(f"💾 保存先: {csv_file}")
        
        # 住所情報の集計
        with_address = sum(1 for p in profiles if p.get('address'))
        with_postal = sum(1 for p in profiles if p.get('postal_code'))
        
        print(f"\n📊 データ統計:")
        print(f"   - ユニークアカウント: {len(profiles)}件")
        print(f"   - 住所情報あり: {with_address}件 ({100*with_address//len(profiles) if profiles else 0}%)")
        print(f"   - 郵便番号あり: {with_postal}件 ({100*with_postal//len(profiles) if profiles else 0}%)")
        
        print("\n🎉 実行完了!")
        return 0
    else:
        print("⚠️ データなし")
        return 1

if __name__ == "__main__":
    sys.exit(main())
