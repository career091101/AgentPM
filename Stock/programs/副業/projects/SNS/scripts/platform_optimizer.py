#!/usr/bin/env python3
"""
Platform Optimizer
プラットフォーム別投稿最適化モジュール

LinkedIn投稿をX/Threadsに最適化して変換
"""

import os
import json
from typing import Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv()

# OpenAI API設定
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# プラットフォーム別最適化プロンプト
PLATFORM_PROMPTS = {
    "X": """
以下のLinkedIn投稿をX (Twitter)向けに最適化してください。

【元の投稿（LinkedIn）】
{linkedin_content}

【X最適化の要件】
1. **文字数**: 最大280文字（スレッド化の場合は複数ツイートに分割可能）
2. **トーン**: カジュアル、簡潔、インパクト重視
3. **ハッシュタグ**: 2-3個に厳選（#AI #キャリア #ChatGPT など）
4. **絵文字**: 適度に使用（🔥⚡💡など）
5. **構成**:
   - 1ツイート目: 最も重要なメッセージを冒頭に
   - 2ツイート目以降: データ・詳細を展開
6. **改行**: 読みやすさ重視で適度に改行
7. **スレッド番号**: (1/N)形式で明示

【フォーマット変換】
- 「〜だと考えています」→「〜です」（断定型）
- 箇条書きを短文に変換
- 長文の段落を140文字以内に分割

【出力形式】
以下のJSON形式で出力してください：

```json
{
  "optimized_content": "最適化された投稿内容（スレッド化しない場合）",
  "thread_posts": [
    "(1/5) 最初のツイート内容...",
    "(2/5) 2つ目のツイート内容...",
    ...
  ],
  "recommended_format": "single" または "thread",
  "character_count": 投稿文字数,
  "optimization_notes": "最適化のポイント"
}
```

【重要】
- 元のメッセージの核心は必ず保持
- 数値データは削除せず、むしろ強調
- 支持派・懐疑派の両論併記は不要（明確な主張のみ）
""",

    "Threads": """
以下のLinkedIn投稿をThreads向けに最適化してください。

【元の投稿（LinkedIn）】
{linkedin_content}

【Threads最適化の要件】
1. **文字数**: 最大500文字/投稿（3-5投稿のスレッド推奨）
2. **トーン**: 会話的、親しみやすい、カジュアル
3. **ハッシュタグ**: 1-2個に抑える
4. **絵文字**: 積極的に使用（💬✨🎯など）
5. **構成**:
   - 1投稿目: 問いかけまたは共感から始める
   - 2投稿目以降: 段階的に深掘り
   - 最終投稿: 「あなたはどう思う？」など対話誘導
6. **改行**: 短い段落で読みやすく
7. **箇条書き**: 絵文字箇条書きに変換（✅、⚡、💡など）

【フォーマット変換】
- 「〜だと考えています」→「〜なんですよね」（口語体）
- 「データによると」→「実はね、」（親しみやすく）
- 箇条書きを会話的な段落に変換

【出力形式】
以下のJSON形式で出力してください：

```json
{
  "optimized_content": "最適化された投稿内容（スレッド化しない場合）",
  "thread_posts": [
    "1投稿目の内容（500文字以内）...",
    "2投稿目の内容（500文字以内）...",
    ...
  ],
  "recommended_format": "single" または "thread",
  "character_count": 投稿文字数,
  "optimization_notes": "最適化のポイント"
}
```

【重要】
- 元のメッセージの核心は必ず保持
- 数値データは削除せず、会話的に表現
- 読者との対話を意識した表現
"""
}


def optimize_for_platform(
    linkedin_content: str,
    platform: str,
    model: str = "gpt-4o"
) -> Dict:
    """
    LinkedIn投稿をプラットフォーム別に最適化

    Args:
        linkedin_content: LinkedIn投稿の内容
        platform: "X" または "Threads"
        model: OpenAIモデル名（デフォルト: gpt-4o）

    Returns:
        Dict: {
            "optimized_content": str,
            "thread_posts": List[str],
            "recommended_format": "single" | "thread",
            "character_count": int,
            "optimization_notes": str
        }
    """
    if platform not in PLATFORM_PROMPTS:
        raise ValueError(f"Unsupported platform: {platform}. Use 'X' or 'Threads'")

    # プロンプト生成
    prompt = PLATFORM_PROMPTS[platform].format(linkedin_content=linkedin_content)

    print(f"🔄 Optimizing for {platform}...")

    # OpenAI API呼び出し
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": f"あなたは{platform}専門のSNSコンテンツ最適化エキスパートです。LinkedIn投稿を{platform}向けに最適化します。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={"type": "json_object"},
        temperature=0.7
    )

    # レスポンス解析
    result_json = response.choices[0].message.content
    result = json.loads(result_json)

    print(f"✅ Optimization complete for {platform}")
    print(f"   Format: {result.get('recommended_format', 'N/A')}")
    print(f"   Character count: {result.get('character_count', 'N/A')}")

    return result


def optimize_all_platforms(
    linkedin_content: str,
    platforms: list[str] = ["X", "Threads"]
) -> Dict[str, Dict]:
    """
    複数プラットフォーム向けに一括最適化

    Args:
        linkedin_content: LinkedIn投稿の内容
        platforms: 最適化対象プラットフォームリスト

    Returns:
        Dict[str, Dict]: {
            "LinkedIn": {"optimized_content": linkedin_content},
            "X": {...},
            "Threads": {...}
        }
    """
    results = {
        "LinkedIn": {
            "optimized_content": linkedin_content,
            "recommended_format": "single",
            "character_count": len(linkedin_content),
            "optimization_notes": "元の投稿（最適化なし）"
        }
    }

    for platform in platforms:
        if platform == "LinkedIn":
            continue  # LinkedIn は最適化不要
        if platform == "Facebook":
            continue  # Facebook は自動投稿対象外

        try:
            results[platform] = optimize_for_platform(linkedin_content, platform)
        except Exception as e:
            print(f"⚠️  Warning: Failed to optimize for {platform}: {e}")
            # フォールバック: LinkedIn投稿をそのまま使用
            results[platform] = {
                "optimized_content": linkedin_content,
                "recommended_format": "single",
                "character_count": len(linkedin_content),
                "optimization_notes": f"最適化失敗、LinkedIn投稿を使用: {e}"
            }

    return results


def save_optimization_result(
    queue_id: str,
    optimization_results: Dict[str, Dict],
    output_dir: str
):
    """
    最適化結果をJSONファイルに保存

    Args:
        queue_id: キューID
        optimization_results: optimize_all_platforms() の出力
        output_dir: 出力ディレクトリ
    """
    from datetime import datetime

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_file = os.path.join(
        output_dir,
        f"platform_optimized_{timestamp}_{queue_id}.json"
    )

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(optimization_results, f, ensure_ascii=False, indent=2)

    print(f"📁 Optimization results saved to: {output_file}")
    return output_file


# 使用例
if __name__ == "__main__":
    # サンプルLinkedIn投稿
    sample_linkedin_post = """
AIエージェントが2027年までにホワイトカラー業務の40%を代替する、という予測が話題です。

しかし、本当に恐れるべきはAIではなく、AIを使いこなせない自分自身です。

実際、OpenAIの最新レポートによると、AIツールを積極活用する社員は、非活用社員と比べて：
• 生産性が35%向上
• 創造的タスクに費やす時間が2倍
• 年収が平均18%高い

私が先月から実践している「AIファースト・ワークフロー」では、以下を徹底しています：
1. 情報収集はPerplexity AIで10分
2. 資料作成はClaude + Canvaで30分
3. メール対応はChatGPTで5分

結果、残業時間が月40時間削減され、戦略的思考に集中できるようになりました。

AIに仕事を奪われるのではなく、AIを武器に市場価値を高める。
これが2027年のキャリア戦略です。

あなたは、どのAIツールを使っていますか？

#AI #キャリア戦略 #ChatGPT #Claude #生産性向上
"""

    print("🚀 Platform Optimizer Test\n")

    # 全プラットフォーム最適化
    results = optimize_all_platforms(sample_linkedin_post)

    # 結果表示
    for platform, result in results.items():
        print(f"\n{'='*60}")
        print(f"📱 {platform}")
        print(f"{'='*60}")
        print(f"Format: {result.get('recommended_format', 'N/A')}")
        print(f"Character count: {result.get('character_count', 'N/A')}")
        print(f"\n{result.get('optimized_content', 'N/A')}\n")

        if result.get("thread_posts"):
            print("Thread posts:")
            for i, post in enumerate(result["thread_posts"], 1):
                print(f"\n[Post {i}]\n{post}")

    # 結果をファイル保存
    data_dir = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data"
    save_optimization_result("test_001", results, data_dir)
