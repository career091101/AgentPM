#!/usr/bin/env python3
"""
ClaudeCode統合版: LLM投稿修正エンジン
Anthropic APIを使ってClaudeが直接修正を実行
"""
import os
import sys
import json
import re
import glob
from datetime import datetime
import pytz
from pathlib import Path
from dotenv import load_dotenv

# .envファイル読み込み
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# 環境変数
SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"
MAX_REFINE_COUNT = 10
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")


def parse_refine_instruction(message_text):
    """
    修正指示を解析

    Returns:
        tuple: (variant_num, instruction) or (None, None)
    """
    # パターン1: 案N をに .+
    pattern1 = r'案(\d+)\s*[をに]\s*(.+)'
    match = re.search(pattern1, message_text)
    if match:
        return int(match.group(1)), match.group(2).strip()

    # パターン2: 案N: .+ or 案N .+
    pattern2 = r'案(\d+)[:：\s]\s*(.+)'
    match = re.search(pattern2, message_text)
    if match:
        return int(match.group(1)), match.group(2).strip()

    return None, None


def load_original_post(variant_num):
    """元の投稿を読み込み"""
    files = glob.glob(f"{SNS_DATA_DIR}/posts_generated_*.json")
    if not files:
        raise FileNotFoundError("posts_generated_*.json が見つかりません")

    latest_file = max(files, key=os.path.getctime)

    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if variant_num < 1 or variant_num > len(data["posts"]):
        raise ValueError(f"案{variant_num}は存在しません（1-{len(data['posts'])}のみ）")

    return data["posts"][variant_num - 1]


def refine_with_claudecode(original_content, instruction, variant_info, session_id):
    """
    ClaudeCodeに修正を依頼（LLM推論で直接実行）
    """
    import time

    # 修正依頼ファイルを作成
    request_file = os.path.join(SNS_DATA_DIR, f"refine_request_{session_id}.json")
    response_file = os.path.join(SNS_DATA_DIR, f"refine_response_{session_id}.json")

    # 既存の応答ファイルを削除
    if os.path.exists(response_file):
        os.remove(response_file)

    jst = pytz.timezone("Asia/Tokyo")
    request_data = {
        "status": "pending",
        "created_at": datetime.now(jst).isoformat(),
        "session_id": session_id,
        "original_content": original_content,
        "instruction": instruction,
        "variant_info": variant_info,
        "prompt": f"""以下のSNS投稿を、指示に従って修正してください。

【元の投稿】
{original_content}

【修正指示】
{instruction}

【投稿情報】
- バリエーション: {variant_info.get('variant', '不明')}
- 文字数: {variant_info.get('character_count', '不明')}字
- 評価: {variant_info.get('rating', '不明')}

【修正ルール】
1. 修正指示に従って内容を変更してください
2. 元の投稿の意図やトーンは維持してください
3. 文字数は80-150字程度に収めてください
4. 修正後の投稿のみを出力してください（説明不要）"""
    }

    with open(request_file, "w", encoding="utf-8") as f:
        json.dump(request_data, f, ensure_ascii=False, indent=2)

    print(f"📝 ClaudeCode修正依頼作成: {request_file}", file=sys.stderr)
    print(f"", file=sys.stderr)
    print(f"⏳ ClaudeCodeによるLLM推論を待機中（最大60秒）...", file=sys.stderr)
    print(f"", file=sys.stderr)

    # ClaudeCodeからの応答を待機（60秒）
    start_time = time.time()
    while time.time() - start_time < 60:
        if os.path.exists(response_file):
            with open(response_file, "r", encoding="utf-8") as f:
                response_data = json.load(f)

            if response_data.get("status") == "completed":
                refined_content = response_data["refined_content"]
                print(f"✅ ClaudeCodeで修正完了（{len(refined_content)}字）", file=sys.stderr)

                # 応答ファイルを削除
                os.remove(response_file)
                return refined_content

        time.sleep(1)

    # タイムアウト: フォールバック修正（Anthropic API）
    print(f"⚠️  ClaudeCode応答タイムアウト（60秒）", file=sys.stderr)
    print(f"   フォールバックLLM修正を実行します", file=sys.stderr)
    return apply_simple_refinement(original_content, instruction)


def apply_simple_refinement(original_content, instruction):
    """
    フォールバック: Anthropic APIでLLM修正
    """
    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY == "your_anthropic_api_key_here":
        print("⚠️  ANTHROPIC_API_KEY not set, returning original content", file=sys.stderr)
        return original_content

    try:
        from anthropic import Anthropic

        client = Anthropic(api_key=ANTHROPIC_API_KEY)

        message = client.messages.create(
            model="claude-haiku-3-5-20241022",
            max_tokens=500,
            messages=[{
                "role": "user",
                "content": f"""以下のSNS投稿を、指示に従って修正してください。

【元の投稿】
{original_content}

【修正指示】
{instruction}

【修正ルール】
1. 修正指示に従って内容を変更してください
2. 元の投稿の意図やトーンは維持してください
3. 文字数は80-150字程度に収めてください
4. 修正後の投稿のみを出力してください（説明不要）"""
            }]
        )

        refined_content = message.content[0].text.strip()
        print(f"✅ Anthropic APIで修正完了（{len(refined_content)}字）", file=sys.stderr)
        return refined_content

    except Exception as e:
        print(f"⚠️  Anthropic API呼び出し失敗: {str(e)}", file=sys.stderr)
        print(f"   元の内容をそのまま返却します", file=sys.stderr)
        return original_content


def load_refine_context(session_id):
    """修正コンテキストを読み込み"""
    context_file = os.path.join(SNS_DATA_DIR, f"refine_context_{session_id}.json")

    if os.path.exists(context_file):
        with open(context_file, "r", encoding="utf-8") as f:
            return json.load(f)

    return {
        "session_id": session_id,
        "refine_count": 0,
        "history": []
    }


def save_refine_context(context):
    """修正コンテキストを保存"""
    # thread_ts（旧）とsession_id（新）の両方に対応
    context_id = context.get("session_id") or context.get("thread_ts")
    context_file = os.path.join(SNS_DATA_DIR, f"refine_context_{context_id}.json")

    with open(context_file, "w", encoding="utf-8") as f:
        json.dump(context, f, ensure_ascii=False, indent=2)


def refine_post(variant_num, instruction, session_id):
    """
    修正処理のメイン関数（export可能）

    Parameters:
    - variant_num: 案番号（1, 2, 3）
    - instruction: 修正指示（例: "もっとカジュアルに"）
    - session_id: セッションID（thread_tsの代わり）

    Returns:
    - dict: 修正結果
    """
    jst = pytz.timezone("Asia/Tokyo")

    # 修正コンテキスト読み込み（session_idを使用）
    context = load_refine_context(session_id)

    # 修正回数チェック
    if context["refine_count"] >= MAX_REFINE_COUNT:
        return {
            "success": False,
            "error": f"修正回数が上限（{MAX_REFINE_COUNT}回）に達しました",
            "refine_count": context["refine_count"]
        }

    # 元の投稿を読み込み
    try:
        original_post = load_original_post(variant_num)
    except (FileNotFoundError, ValueError) as e:
        return {
            "success": False,
            "error": str(e)
        }

    # ClaudeCodeで直接修正を実行
    print(f"🤖 ClaudeCodeで修正実行中...", file=sys.stderr)
    print(f"   元の内容: {original_post['content'][:50]}...", file=sys.stderr)
    print(f"   修正指示: {instruction}", file=sys.stderr)

    refined_content = refine_with_claudecode(
        original_post["content"],
        instruction,
        original_post,
        session_id
    )

    # 修正履歴を更新
    context["refine_count"] += 1
    context["history"].append({
        "variant_num": variant_num,
        "instruction": instruction,
        "original_content": original_post["content"],
        "refined_content": refined_content,
        "refined_at": datetime.now(jst).isoformat()
    })

    # コンテキスト保存
    save_refine_context(context)

    # 修正後の投稿情報を作成
    refined_post = {
        "content": refined_content,
        "character_count": len(refined_content),
        "predicted_er": original_post.get("predicted_er", "未計算"),
        "refined_from": variant_num,
        "variant": f"{original_post.get('variant', '不明')}（修正版）",
        "rating": original_post.get("rating", "不明")
    }

    # 結果を返す
    return {
        "success": True,
        "refine_count": context["refine_count"],
        "refined_post": refined_post,
        "instruction": instruction
    }


def main(variant_num, instruction, thread_ts):
    """
    メインフロー（ClaudeCode統合版）
    ※後方互換性のため、refine_post()を呼び出す

    Parameters:
    - variant_num: 案番号（1, 2, 3）
    - instruction: 修正指示
    - thread_ts: thread_ts（session_idと同義）

    Returns:
    - dict: 修正結果
    """
    # refine_post()を呼び出し（thread_ts = session_id）
    return refine_post(variant_num, instruction, thread_ts)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(json.dumps({
            "success": False,
            "error": "Usage: refine_post_variant_claudecode.py <variant_num> <instruction> <thread_ts>"
        }))
        sys.exit(1)

    try:
        variant_num = int(sys.argv[1])
        instruction = sys.argv[2]
        thread_ts = sys.argv[3]

        result = main(variant_num, instruction, thread_ts)
        print(json.dumps(result, ensure_ascii=False, indent=2))

        if result["success"]:
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        print(json.dumps({
            "success": False,
            "error": f"予期しないエラー: {str(e)}"
        }))
        sys.exit(1)
