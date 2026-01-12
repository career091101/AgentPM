#!/usr/bin/env python3
"""
Instagram & Threads データ一括収集スクリプト

InstagramとThreadsの両方からデータを収集します。

使用方法:
python3 collect_all_sns_data.py

依存関係:
pip install playwright pandas python-dotenv
playwright install chromium
"""

import subprocess
import sys
from pathlib import Path

# スクリプトディレクトリ
SCRIPT_DIR = Path(__file__).parent

# 各スクリプトのパス
INSTAGRAM_SCRIPT = SCRIPT_DIR / "scrape_instagram_insights.py"
THREADS_SCRIPT = SCRIPT_DIR / "scrape_threads_insights.py"


def run_script(script_path, script_name):
    """スクリプトを実行"""
    print("\n" + "=" * 60)
    print(f"{script_name}を実行中...")
    print("=" * 60)

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=SCRIPT_DIR,
            check=True,
            capture_output=False
        )
        print(f"\n✓ {script_name}が正常に完了しました")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n✗ {script_name}でエラーが発生しました: {e}")
        return False
    except Exception as e:
        print(f"\n✗ {script_name}で予期しないエラーが発生しました: {e}")
        return False


def main():
    """メイン処理"""
    print("=" * 60)
    print("Instagram & Threads データ一括収集")
    print("=" * 60)
    print("\n注意事項:")
    print("- 各スクリプトでブラウザが開きます")
    print("- 初回実行時は手動でログインが必要です")
    print("- ログイン状態は保存されます")
    print("\n実行順序:")
    print("1. Instagramデータ収集")
    print("2. Threadsデータ収集")

    input("\nEnterキーを押して開始してください...")

    results = {}

    # Instagramデータ収集
    results["Instagram"] = run_script(INSTAGRAM_SCRIPT, "Instagram データ収集")

    # Threadsデータ収集
    results["Threads"] = run_script(THREADS_SCRIPT, "Threads データ収集")

    # 結果サマリー
    print("\n" + "=" * 60)
    print("データ収集結果サマリー")
    print("=" * 60)

    for platform, success in results.items():
        status = "✓ 成功" if success else "✗ 失敗"
        print(f"{platform}: {status}")

    print("\n" + "=" * 60)

    # 出力ファイルの場所を表示
    project_root = SCRIPT_DIR.parent
    print("\n出力ファイルの場所:")
    print(f"- Instagram: {project_root}/Instagram/")
    print(f"- Threads: {project_root}/Threads/")
    print("\n次のステップ:")
    print("- データ分析スクリプトを実行してください")
    print("- python3 analyze_all_platforms.py")


if __name__ == "__main__":
    main()
