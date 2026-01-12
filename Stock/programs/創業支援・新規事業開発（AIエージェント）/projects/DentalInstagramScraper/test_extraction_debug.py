#!/usr/bin/env python3
"""
プロフィール抽出のデバッグテスト - 1投稿のみ
"""
import sys
from browser_collector import collect_from_hashtag
from datetime import datetime

def main():
    print("\n" + "="*60)
    print("デバッグテスト - プロフィール抽出")
    print("="*60)
    print(f"時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # 1投稿のみ収集
    hashtag = "矯正歯科"
    print(f"🔍 ハッシュタグ: #{hashtag} (最大1投稿)\n")
    
    try:
        profiles = collect_from_hashtag(
            hashtag=hashtag,
            max_posts=1,  # 1投稿のみ
            headless=True
        )
        
        print(f"\n✅ 完了: {len(profiles)}件")
        
        if profiles:
            for i, p in enumerate(profiles, 1):
                print(f"\n[{i}] プロフィール情報:")
                for key, val in p.items():
                    print(f"    {key}: {val}")
        
        return 0
    except Exception as e:
        print(f"❌ エラー: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
