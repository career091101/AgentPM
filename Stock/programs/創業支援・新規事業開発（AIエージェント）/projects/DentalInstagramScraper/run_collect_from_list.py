#!/usr/bin/env python3
"""
実際の歯科医院インスタンスハンドルのシードリストを使用した収集
"""
import sys
from collect_from_list import collect_dental_data, save_to_csv
from datetime import datetime

def main():
    print("\n" + "="*60)
    print("歯科医院Instagramデータ収集（シードリスト方式）")
    print("="*60)
    print(f"時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # 実際の歯科医院関連ハンドルのシードリスト
    # 注: これらは確認済みの実在するハンドルではなく、テスト用です
    # 実際には「歯科医院 Instagram site:instagram.com」で検索して取得
    seed_handles = [
        "dentaltown",           # テスト用（STATUS_REPORT で確認済み）
        # 実際の歯科医院ハンドルを追加してください
        # 例:
        # "tokyo_dental_clinic",
        # "orthopedic_dental_jp",
        # "pediatric_dental_tokyo",
    ]
    
    print(f"🔍 シードリスト: {len(seed_handles)}件")
    for h in seed_handles:
        print(f"   - @{h}")
    print()
    
    # 収集実行
    data = collect_dental_data(seed_handles)
    
    # 結果報告
    print("\n" + "="*60)
    print("結果")
    print("="*60)
    
    if data:
        csv_file = save_to_csv(data)
        
        print(f"\n📊 統計:")
        print(f"   - チェック対象: {len(seed_handles)}件")
        print(f"   - 歯科医院: {len(data)}件")
        print(f"   - 住所あり: {sum(1 for d in data if d['address'])}件")
        print(f"   - 郵便番号あり: {sum(1 for d in data if d['postal_code'])}件")
        print(f"   - 手動レビュー必要: {sum(1 for d in data if d['needs_manual_review'])}件")
        
        print(f"\n✅ 完了!")
        print(f"出力ファイル: {csv_file}")
        return 0
    else:
        print("\n⚠️ 歯科医院データが取得できませんでした")
        print("\n💡 推奨:")
        print("   1. シードリストに実際の歯科医院ハンドルを追加してください")
        print("   2. Google検索: 「歯科医院 Instagram site:instagram.com」")
        print("   3. または find_dental_handles.py を実行して自動発見")
        return 1

if __name__ == "__main__":
    sys.exit(main())
