#!/usr/bin/env python3
"""
LinkedIn投稿3案生成スクリプト（高野メソッド準拠）

Usage:
    from generate_linkedin_3_cases import generate_3_cases
    cases = generate_3_cases()
"""

import os
import json
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv
from anthropic import Anthropic

# .env読み込み
project_root = Path(__file__).parent.parent
load_dotenv(project_root / ".env")


def load_latest_research_findings() -> dict:
    """最新のリサーチデータを読み込み"""
    data_dir = project_root / "data"

    # research_findings_*.jsonから最新ファイルを取得
    research_files = list(data_dir.glob("research_findings_*_v2_*.json"))

    if not research_files:
        # v2がない場合は通常版
        research_files = list(data_dir.glob("research_findings_*.json"))

    if not research_files:
        raise FileNotFoundError("research_findings_*.json not found in data/")

    # 最新ファイル
    latest_file = max(research_files, key=lambda f: f.stat().st_mtime)

    print(f"📄 Using research file: {latest_file.name}")

    with open(latest_file, "r", encoding="utf-8") as f:
        return json.load(f)


def load_prompt_template() -> str:
    """高野メソッドプロンプトテンプレート読み込み"""
    prompt_file = project_root / "投稿文作成用プロンプト_v6_takano_refined"

    if not prompt_file.exists():
        raise FileNotFoundError(
            f"Prompt file not found: {prompt_file}"
        )

    return prompt_file.read_text(encoding="utf-8")


def generate_3_cases_with_claude(research_findings: dict) -> list:
    """
    Claude API経由で3案を生成

    Args:
        research_findings: リサーチデータ

    Returns:
        list: 3案のリスト
            [
                {"type": "数字インパクト型", "content": "...", "hashtags": "..."},
                {"type": "衝撃発言型", "content": "...", "hashtags": "..."},
                {"type": "問題提起型", "content": "...", "hashtags": "..."}
            ]
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY not found in .env file")

    client = Anthropic(api_key=api_key)

    # プロンプトテンプレート読み込み
    system_prompt = load_prompt_template()

    # リサーチデータから重要トピックを抽出
    key_takeaways = research_findings.get("key_takeaways", {})
    if not key_takeaways:
        raise ValueError("No key_takeaways found in research_findings")

    # key_takeawaysから主要トピックを構成
    topic_text = f"""**投資動向**: {key_takeaways.get('investment_landscape', '')}

**ツール比較**: {key_takeaways.get('tool_comparison', '')}

**市場成長**: {key_takeaways.get('market_growth', '')}

**市場リーダー**: {key_takeaways.get('market_leaders', '')}

**生産性の実態**: {key_takeaways.get('productivity_reality', '')}

**2026年予測**: {key_takeaways.get('2026_predictions', '')}
"""
    topic_url = "AI関連最新リサーチ（2026-01-04）"

    # ユーザープロンプト
    user_prompt = f"""以下のAI関連トピックから、LinkedIn投稿を3案作成してください。

**トピック情報**:
{topic_text}

**出典**: {topic_url}

**要件**:
1. **案1（数字インパクト型）**: 具体的数値・倍率・金額を最優先にしたフック
2. **案2（衝撃発言型）**: 著名人の発言や「マジで」「ヤバい」などの強い表現を使ったフック
3. **案3（問題提起型）**: 読者の課題や業界の変化を問いかける形のフック

**出力形式**（JSON）:
```json
[
  {{
    "type": "数字インパクト型",
    "content": "投稿本文（700-900字）",
    "hashtags": "#AI #スタートアップ"
  }},
  {{
    "type": "衝撃発言型",
    "content": "投稿本文（700-900字）",
    "hashtags": "#AI #テクノロジー"
  }},
  {{
    "type": "問題提起型",
    "content": "投稿本文（700-900字）",
    "hashtags": "#AI #経営"
  }}
]
```

**重要**:
- 各案は必ず700字以上
- 必ず問いかけで終わる
- ハッシュタグは2個まで
- 呼びかけ表現（「経営者のあなたへ:」等）は禁止
"""

    print("🤖 Claude APIでコンテンツ生成中...")

    # Claude API呼び出し
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )

    # レスポンス解析
    response_text = response.content[0].text

    # JSONブロック抽出
    if "```json" in response_text:
        json_start = response_text.find("```json") + 7
        json_end = response_text.find("```", json_start)
        json_text = response_text[json_start:json_end].strip()
    else:
        json_text = response_text.strip()

    try:
        cases = json.loads(json_text)
        print(f"✅ 3案生成完了!")
        return cases
    except json.JSONDecodeError as e:
        print(f"❌ JSON解析エラー: {e}")
        print(f"   Response: {response_text}")
        raise


def generate_3_cases() -> list:
    """
    3案を生成（メイン関数）

    Returns:
        list: 3案のリスト
    """
    print("=" * 60)
    print("LinkedIn投稿 3案生成")
    print("=" * 60)
    print()

    # 1. 最新リサーチデータ読み込み
    research_findings = load_latest_research_findings()

    # 2. Claude API経由で3案生成
    cases = generate_3_cases_with_claude(research_findings)

    # 3. 結果表示
    print("\n" + "=" * 60)
    print("生成された3案:")
    print("=" * 60)
    for i, case in enumerate(cases, 1):
        print(f"\n【案{i}】 {case['type']}")
        print(f"文字数: {len(case['content'])}字")
        print(f"ハッシュタグ: {case['hashtags']}")
        print(f"\n{case['content'][:200]}...")
        print()

    return cases


if __name__ == "__main__":
    try:
        cases = generate_3_cases()

        # data/posts_generated_3cases_YYYYMMDD.json に保存
        output_file = (
            project_root
            / "data"
            / f"posts_generated_3cases_{datetime.now().strftime('%Y%m%d')}.json"
        )
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(cases, f, ensure_ascii=False, indent=2)

        print(f"💾 保存完了: {output_file}")

    except Exception as e:
        print(f"❌ エラー: {e}")
        sys.exit(1)
