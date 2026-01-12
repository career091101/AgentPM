#!/usr/bin/env python3
"""
複数歯科関連ハッシュタグで並列収集
"""
import sys
from browser_collector import collect_from_hashtag, save_to_csv
from datetime import datetime
from pathlib import Path

def main():
    print("\n" + "="*60)
    print("複数ハッシュタグによる歯科医院データ収集")
    print("="*60)
    print(f"時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60 + "\n")
    
    # 複数ハッシュタグの試行
    hashtags = [
        ("小児歯科", 50),
        ("矯正歯科", 50),
        ("審美歯科", 50),
        ("インプラント", 50),
        ("歯科医院", 30),
    ]
    
    all_profiles = []
    seen_handles = set()
    
    for hashtag, max_posts in hashtags:
        print(f"\n🔍 ハッシュタグ: #{hashtag} (最大{max_posts}投稿)")
        print("-" * 60)
        
        try:
            profiles = collect_from_hashtag(
                hashtag=hashtag,
                max_posts=max_posts,
                headless=True
            )
            
            # 重複排除
            new_count = 0
            for p in profiles:
                handle = p.get('instagram_handle')
                if handle and handle not in seen_handles:
                    seen_handles.add(handle)
                    all_profiles.append(p)
                    new_count += 1
            
            print(f"✅ {hashtag}: {len(profiles)}件検出 → {new_count}件新規")
            
        except Exception as e:
            print(f"❌ {hashtag}: エラー発生 - {str(e)}")
    
    # 結果報告
    print("\n" + "="*60)
    print("最終結果")
    print("="*60)
    
    if all_profiles:
        # CSV保存
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_file = f"dental_instagram_{timestamp}_multi.csv"
        
        # CSVヘッダー
        csv_path = Path(csv_file)
        headers = [
            "instagram_handle", "full_name", "bio", "followers",
            "external_url", "is_business", "postal_code", "address",
            "phone", "keywords_matched"
        ]
        
        with open(csv_path, 'w', encoding='utf-8-sig') as f:
            f.write(','.join(headers) + '\n')
            for p in all_profiles:
                row = [
                    p.get('instagram_handle', ''),
                    p.get('full_name', ''),
                    p.get('bio', ''),
                    str(p.get('followers', '')),
                    p.get('external_url', ''),
                    'Yes' if p.get('is_business') else 'No',
                    p.get('postal_code', ''),
                    p.get('address', ''),
                    p.get('phone', ''),
                    ','.join(p.get('keywords_matched', []))
                ]
                f.write(','.join([f'"{x}"' if ',' in str(x) else str(x) for x in row]) + '\n')
        
        print(f"✅ 収集完了: {len(all_profiles)}件")
        print(f"💾 保存先: {csv_file}")
        
        # 統計
        with_address = sum(1 for p in all_profiles if p.get('address'))
        with_postal = sum(1 for p in all_profiles if p.get('postal_code'))
        with_phone = sum(1 for p in all_profiles if p.get('phone'))
        
        print(f"\n📊 データ統計:")
        print(f"   - ユニークアカウント: {len(all_profiles)}件")
        print(f"   - 住所情報あり: {with_address}件 ({100*with_address//len(all_profiles)}%)")
        print(f"   - 郵便番号あり: {with_postal}件 ({100*with_postal//len(all_profiles)}%)")
        print(f"   - 電話番号あり: {with_phone}件 ({100*with_phone//len(all_profiles)}%)")
        
        print("\n🎉 実行完了!")
        return 0
    else:
        print("⚠️ ハッシュタグから歯科医院データを取得できませんでした")
        print("\n💡 推奨:")
        print("   - GoogleマップAPIで歯科医院リストを取得")
        print("   - 医院名でInstagram検索")
        return 1

if __name__ == "__main__":
    sys.exit(main())
