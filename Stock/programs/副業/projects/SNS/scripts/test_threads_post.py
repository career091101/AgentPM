#!/usr/bin/env python3
"""
Threads投稿テスト - Late API経由でThreadsに投稿
"""

import sys
from pathlib import Path

# late_api_postモジュールをインポート
sys.path.insert(0, str(Path(__file__).parent))
from late_api_post import (
    get_account_id,
    post_to_late_api,
    LateAPIError
)

def test_simple_threads_post():
    """シンプルなThreads投稿テスト"""

    print("=" * 60)
    print("Threads投稿テスト - Late API")
    print("=" * 60)

    # Threadsアカウント情報取得
    try:
        threads_account_id = get_account_id("threads")
        print(f"\n✅ Threadsアカウント取得成功")
        print(f"   Account ID: {threads_account_id}")
    except ValueError as e:
        print(f"\n❌ エラー: {e}")
        return False

    # テスト投稿内容
    test_content = """Late API統合テスト🚀

Meta Threadsへの投稿機能を実装中です。
このメッセージはLate API経由で自動投稿されています。

#LateAPI #automation #test"""

    print(f"\n投稿内容:\n{test_content}\n")

    # Late API経由で投稿
    try:
        print("投稿中...")
        result = post_to_late_api(
            content=test_content,
            platform="threads",
            account_id=threads_account_id
        )

        print("\n✅ Threads投稿成功！")
        print(f"Response: {result}")

        return True

    except LateAPIError as e:
        print(f"\n❌ Late APIエラー: {e}")
        return False
    except Exception as e:
        print(f"\n❌ 予期しないエラー: {e}")
        return False

if __name__ == "__main__":
    success = test_simple_threads_post()
    sys.exit(0 if success else 1)
