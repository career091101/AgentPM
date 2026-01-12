#!/usr/bin/env python3
"""
LLM投稿修正エンジン
Slack返信から修正指示を受け取り、Claude Haikuで投稿内容を部分修正
"""
import os
import sys
import json
import re
import glob
from datetime import datetime
from anthropic import Anthropic
import pytz

# 環境変数
SNS_DATA_DIR = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"
MAX_REFINE_COUNT = 3


def parse_refine_instruction(message_text):
    """
    修正指示を解析

    入力例:
    - "案1をもっとカジュアルに"
    - "案2: 数字を増やして"
    - "案3 もっと短く"

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
    """
    generate-sns-posts出力から元の投稿を読み込み

    Args:
        variant_num: 案番号（1, 2, 3）

    Returns:
        dict: 元の投稿データ
    """
    # 最新のposts_generated_*.jsonを検索
    files = glob.glob(f"{SNS_DATA_DIR}/posts_generated_*.json")
    if not files:
        raise FileNotFoundError("posts_generated_*.json が見つかりません")

    latest_file = max(files, key=os.path.getctime)

    with open(latest_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    if variant_num < 1 or variant_num > len(data["posts"]):
        raise ValueError(f"案{variant_num}は存在しません（1-{len(data['posts'])}のみ）")

    return data["posts"][variant_num - 1]


def refine_with_llm(original_content, instruction, variant_info):
    """
    Claude Haikuで投稿内容を部分修正

    Args:
        original_content: 元の投稿内容
        instruction: 修正指示（自然言語）
        variant_info: 元の投稿のメタ情報（variant, rating等）

    Returns:
        str: 修正後の投稿内容
    """
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    prompt = f"""あなたはSNS投稿の編集者です。以下の投稿を、指示に従って部分修正してください。

【元の投稿】
{original_content}

【投稿スタイル情報】
- バリエーション: {variant_info.get('variant', '不明')}
- 評価: {variant_info.get('rating', '不明')}

【修正指示】
{instruction}

【修正ルール】
1. 修正指示に従った変更のみを行う（余計な変更はしない）
2. 投稿の基本構造（改行、見出し等）は維持する
3. 文字数は200字以内に収める
4. LinkedIn投稿として自然な文体を保つ
5. 元の投稿の主旨・メッセージは維持する

修正後の投稿内容のみを出力してください（説明文は不要）。"""

    try:
        message = client.messages.create(
            model="claude-haiku-20250110",
            max_tokens=1024,
            temperature=0.7,
            timeout=15.0,  # 15秒タイムアウト
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        refined_content = message.content[0].text.strip()
        return refined_content

    except Exception as e:
        raise RuntimeError(f"LLM修正処理エラー: {str(e)}")


def load_refine_context(thread_ts):
    """
    修正コンテキストを読み込み

    Returns:
        dict: 修正コンテキスト（存在しない場合は初期値）
    """
    context_file = os.path.join(SNS_DATA_DIR, f"refine_context_{thread_ts}.json")

    if os.path.exists(context_file):
        with open(context_file, "r", encoding="utf-8") as f:
            return json.load(f)

    # 初期値
    return {
        "thread_ts": thread_ts,
        "refine_count": 0,
        "history": []
    }


def save_refine_context(context):
    """修正コンテキストを保存"""
    context_file = os.path.join(SNS_DATA_DIR, f"refine_context_{context['thread_ts']}.json")

    with open(context_file, "w", encoding="utf-8") as f:
        json.dump(context, f, ensure_ascii=False, indent=2)


def main(variant_num, instruction, thread_ts):
    """
    メインフロー

    Args:
        variant_num: 修正対象の案番号（1, 2, 3）
        instruction: 修正指示（自然言語）
        thread_ts: Slackスレッドタイムスタンプ

    Returns:
        dict: 修正結果（JSON形式）
    """
    jst = pytz.timezone("Asia/Tokyo")

    # 修正コンテキスト読み込み
    context = load_refine_context(thread_ts)

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

    # LLMで修正実行
    try:
        refined_content = refine_with_llm(
            original_post["content"],
            instruction,
            original_post
        )
    except RuntimeError as e:
        return {
            "success": False,
            "error": str(e)
        }

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


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(json.dumps({
            "success": False,
            "error": "Usage: refine_post_variant.py <variant_num> <instruction> <thread_ts>"
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
