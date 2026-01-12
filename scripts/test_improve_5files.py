#!/usr/bin/env python3
"""
Test improvement script on 5 high-priority files
"""

import json
from pathlib import Path
import shutil

# Import main improvement function
import sys
sys.path.append(str(Path(__file__).parent))
from improve_forsolo_tier2_files import improve_file, load_audit_data, BASE_PATH

def main():
    """Test improvement on 5 files"""
    print("テスト実行: 優先度「高」5ファイル改善")

    # Load audit data
    audit_data = load_audit_data()

    # Filter high-priority files
    high_priority = [item for item in audit_data if item["priority"] == "高"]
    test_files = high_priority[:5]  # First 5 high-priority files

    print(f"\nテスト対象: {len(test_files)}ファイル")

    for i, item in enumerate(test_files, 1):
        file_path = BASE_PATH / item["file"]

        # Create backup
        backup_path = file_path.with_suffix('.md.backup')
        shutil.copy2(file_path, backup_path)
        print(f"\n{i}. {item['file']}")
        print(f"   バックアップ作成: {backup_path.name}")

        # Improve file
        if improve_file(file_path, item):
            print(f"   ✅ 改善完了")

            # Show file size change
            original_size = backup_path.stat().st_size
            new_size = file_path.stat().st_size
            size_diff = new_size - original_size
            print(f"   ファイルサイズ: {original_size} → {new_size} (+{size_diff} bytes)")
        else:
            print(f"   ❌ 改善失敗")
            # Restore from backup
            shutil.copy2(backup_path, file_path)
            print(f"   バックアップから復元")

    print(f"\n{'='*60}")
    print("テスト完了")
    print(f"{'='*60}")
    print("\n次のステップ:")
    print("1. 改善ファイルを手動確認")
    print("2. 問題なければ全ファイル改善スクリプト実行")
    print("3. 問題あればバックアップから復元（.md.backup）")

if __name__ == "__main__":
    main()
