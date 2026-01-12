#!/usr/bin/env python3
"""
ClaudeCodeヘルパー: 修正リクエスト処理スクリプト
ClaudeCodeが修正を実行し、結果を保存
"""
import os
import sys
import json
from datetime import datetime
import pytz

SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"


def process_refine_request(thread_ts):
    """
    修正リクエストを読み込み、ClaudeCodeに修正内容を提示
    """
    request_file = os.path.join(SNS_DATA_DIR, f"refine_request_{thread_ts}.json")

    if not os.path.exists(request_file):
        print(f"❌ 修正リクエストが見つかりません: {request_file}")
        return False

    with open(request_file, "r", encoding="utf-8") as f:
        request_data = json.load(f)

    print("=" * 60)
    print("📝 ClaudeCode修正リクエスト")
    print("=" * 60)
    print(f"\n【元の投稿内容】")
    print(request_data["original_content"])
    print(f"\n【修正指示】")
    print(request_data["instruction"])
    print(f"\n【バリエーション情報】")
    print(f"  - variant: {request_data['variant_info'].get('variant')}")
    print(f"  - rating: {request_data['variant_info'].get('rating')}")
    print(f"  - character_count: {request_data['variant_info'].get('character_count')}")
    print("\n" + "=" * 60)
    print("ClaudeCodeで修正内容を入力してください:")
    print("（複数行の場合は、空行を2回入力で終了）")
    print("=" * 60)
    print()

    # ユーザー入力を受け取る
    lines = []
    empty_count = 0

    while True:
        try:
            line = input()
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
            else:
                empty_count = 0
            lines.append(line)
        except EOFError:
            break

    refined_content = '\n'.join(lines).strip()

    if not refined_content:
        print("❌ 修正内容が空です")
        return False

    # 修正結果を保存
    jst = pytz.timezone("Asia/Tokyo")
    response_file = os.path.join(SNS_DATA_DIR, f"refine_response_{thread_ts}.json")

    response_data = {
        "status": "completed",
        "refined_content": refined_content,
        "completed_at": datetime.now(jst).isoformat()
    }

    with open(response_file, "w", encoding="utf-8") as f:
        json.dump(response_data, f, ensure_ascii=False, indent=2)

    # リクエストファイル削除
    os.remove(request_file)

    print("\n" + "=" * 60)
    print(f"✅ 修正結果を保存しました: {response_file}")
    print("=" * 60)
    print(f"\n【修正後の内容】")
    print(refined_content)
    print()

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: process_refine_request.py <thread_ts>")
        sys.exit(1)

    thread_ts = sys.argv[1]
    success = process_refine_request(thread_ts)

    sys.exit(0 if success else 1)
