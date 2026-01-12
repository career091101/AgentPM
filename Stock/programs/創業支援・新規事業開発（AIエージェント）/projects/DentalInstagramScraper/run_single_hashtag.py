#!/usr/bin/env python3
"""
単一ハッシュタグでテスト実行
"""
import sys
from browser_collector import collect_from_hashtag
from datetime import datetime
from pathlib import Path

def main():
    print("\n" + "="*60)
    print("歯科医院データ収集 - 単一ハッシュタグテスト")
    print("="*60)
    print(f"時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60 + "\n")
    
    # 矯正歯科で50投稿をテスト
    hashtag = "矯正歯科"
    print(f"🔍 ハッシュタグ: #{hashtag} (最大50投稿)\n")
    
    try:
        profiles = collect_from_hashtag(
            hashtag=hashtag,
            max_posts=50,
            headless=True
        )
        
        print(f"\n✅ 完了: {len(profiles)}件の歯科医院を収集")
        
        if profiles:
            # 統計
            with_address = sum(1 for p in profiles if p.get('address'))
            with_postal = sum(1 for p in profiles if p.get('postal_code'))
            
            print(f"\n📊 統計:")
            print(f"   - アカウント数: {len(profiles)}")
            print(f"   - 住所あり: {with_address} ({100*with_address//len(profiles)}%)")
            print(f"   - 郵便番号あり: {with_postal} ({100*with_postal//len(profiles)}%)")
            
            # サンプル表示
            print(f"\n📋 サンプル（最初の3件）:")
            for i, p in enumerate(profiles[:3], 1):
                print(f"\n[{i}] {p.get('instagram_handle', 'N/A')}")
                print(f"    名前: {p.get('full_name', 'N/A')}")
                print(f"    住所: {p.get('address', 'N/A')}")
                print(f"    郵便番号: {p.get('postal_code', 'N/A')}")
        
        return 0
    except Exception as e:
        print(f"❌ エラー: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
