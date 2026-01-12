#!/usr/bin/env python3
"""
ClaudeCode自動修正ヘルパー
修正リクエストを読み込み、ClaudeCodeのLLM機能で自動修正
"""
import os
import sys
import json
from datetime import datetime
import pytz

SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"


def process_refine_request_auto(thread_ts):
    """
    修正リクエストを読み込み、自動修正プロンプトを生成
    """
    request_file = os.path.join(SNS_DATA_DIR, f"refine_request_{thread_ts}.json")

    if not os.path.exists(request_file):
        print(f"❌ 修正リクエストが見つかりません: {request_file}")
        return None

    with open(request_file, "r", encoding="utf-8") as f:
        request_data = json.load(f)

    print("=" * 60)
    print("📝 ClaudeCode自動修正リクエスト")
    print("=" * 60)

    # ClaudeCodeが直接LLM推論を実行するためのプロンプトを表示
    prompt = f"""あなたはSNS投稿の編集者です。以下の投稿を、指示に従って部分修正してください。

【元の投稿】
{request_data['original_content']}

【投稿スタイル情報】
- バリエーション: {request_data['variant_info'].get('variant', '不明')}
- 評価: {request_data['variant_info'].get('rating', '不明')}

【修正指示】
{request_data['instruction']}

【修正ルール】
1. 修正指示に従った変更のみを行う（余計な変更はしない）
2. 投稿の基本構造（改行、見出し等）は維持する
3. 文字数は200字以内に収める
4. LinkedIn投稿として自然な文体を保つ
5. 元の投稿の主旨・メッセージは維持する

修正後の投稿内容のみを出力してください（説明文は不要）。"""

    print("\n" + prompt)
    print("\n" + "=" * 60)
    print("👆 上記のプロンプトをClaudeCodeに入力して、修正結果を取得してください")
    print("=" * 60)
    print("\nまたは、以下のコマンドで修正結果を保存できます:")
    print(f"  python3 scripts/save_refine_response.py {thread_ts} \"修正後の内容\"")
    print()

    return request_data


def save_refine_response(thread_ts, refined_content):
    """
    修正結果を保存（外部スクリプトから呼び出し可能）
    """
    jst = pytz.timezone("Asia/Tokyo")
    response_file = os.path.join(SNS_DATA_DIR, f"refine_response_{thread_ts}.json")
    request_file = os.path.join(SNS_DATA_DIR, f"refine_request_{thread_ts}.json")

    response_data = {
        "status": "completed",
        "refined_content": refined_content,
        "completed_at": datetime.now(jst).isoformat()
    }

    with open(response_file, "w", encoding="utf-8") as f:
        json.dump(response_data, f, ensure_ascii=False, indent=2)

    # リクエストファイル削除
    if os.path.exists(request_file):
        os.remove(request_file)

    print(f"✅ 修正結果を保存しました: {response_file}")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: process_refine_request_auto.py <thread_ts> [refined_content]")
        sys.exit(1)

    thread_ts = sys.argv[1]

    if len(sys.argv) == 3:
        # 修正結果が引数で渡された場合
        refined_content = sys.argv[2]
        success = save_refine_response(thread_ts, refined_content)
        sys.exit(0 if success else 1)
    else:
        # プロンプト表示のみ
        request_data = process_refine_request_auto(thread_ts)
        sys.exit(0 if request_data else 1)
