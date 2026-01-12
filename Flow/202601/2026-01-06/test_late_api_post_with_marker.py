#!/usr/bin/env python3
"""
Late API投稿テスト（タイトル重複修正版）

【テスト】マーカーを付けて1案のみを投稿
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime, timedelta, timezone

# プロジェクトルート設定
project_root = Path(__file__).parent.parent.parent.parent / "Stock/programs/副業/projects/SNS"
sys.path.append(str(project_root / "scripts"))

# 修正版の関数をインポート
import requests


def extract_variant_content(markdown: str, variant_number: int) -> dict:
    """
    案Nのタイトルと本文を抽出（Markdown装飾除去版 + タイトル重複除去）
    """
    pattern = rf'## 案{variant_number}:.*?\n\n### タイトル\n\*\*(.*?)\*\*\n\n### 本文.*?\n\n(.*?)(?=\n---\n|\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        return None

    title = match.group(1).strip()
    body = match.group(2).strip()

    def remove_markdown(text):
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        text = re.sub(r'^\- ', '', text, flags=re.MULTILINE)
        text = re.sub(r'^\d+\. ', '', text, flags=re.MULTILINE)
        return text

    title_clean = remove_markdown(title)
    body_clean = remove_markdown(body)

    # 【修正】本文1行目がタイトルと同じ場合は除去（タイトル重複防止）
    body_lines = body_clean.split('\n')
    if body_lines and body_lines[0].strip().rstrip('。！？') == title_clean.strip():
        body_clean = '\n'.join(body_lines[1:]).strip()

    # 【テスト】マーカーを追加
    full_content = f"【テスト】{title_clean}\n\n{body_clean}"

    return {
        "title": title_clean,
        "body": body_clean,
        "full_content": full_content
    }


def post_to_late_api(content: str, scheduled_datetime: datetime) -> dict:
    """Late APIに1件の投稿を送信"""
    env_file = project_root / ".env"
    env_vars = {}

    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    if "#" in value:
                        in_quote = False
                        quote_char = None
                        clean_value = []
                        for i, ch in enumerate(value):
                            if ch in ['"', "'"]:
                                if not in_quote:
                                    in_quote = True
                                    quote_char = ch
                                elif ch == quote_char:
                                    in_quote = False
                                    quote_char = None
                            elif ch == "#" and not in_quote:
                                break
                            clean_value.append(ch)
                        value = "".join(clean_value)
                    value = value.strip().strip('"').strip("'")
                    env_vars[key.strip()] = value

    api_key = env_vars.get("LATE_API_KEY")
    linkedin_account_id = env_vars.get("LATE_LINKEDIN_ACCOUNT_ID")

    if not api_key:
        raise ValueError(f"LATE_API_KEY not found in .env file")
    if not linkedin_account_id:
        raise ValueError(f"LATE_LINKEDIN_ACCOUNT_ID not found in .env file")

    base_url = "https://getlate.dev/api/v1"
    JST = timezone(timedelta(hours=9))

    if scheduled_datetime.tzinfo is None:
        scheduled_datetime = scheduled_datetime.replace(tzinfo=JST)

    scheduled_datetime_str = scheduled_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")
    if len(scheduled_datetime_str) >= 5:
        scheduled_datetime_str = scheduled_datetime_str[:-2] + ':' + scheduled_datetime_str[-2:]

    payload = {
        "content": content,
        "platforms": [
            {
                "platform": "linkedin",
                "accountId": linkedin_account_id
            }
        ],
        "scheduledFor": scheduled_datetime_str,
        "timezone": "Asia/Tokyo"
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        f"{base_url}/posts",
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code not in [200, 201]:
        error_msg = f"Late API Error: {response.status_code} - {response.text}"
        raise Exception(error_msg)

    return response.json()


def main():
    """メイン処理"""
    print("=" * 60)
    print("Late API投稿テスト（タイトル重複修正版）")
    print("=" * 60)
    print()

    try:
        # 1. 最新のMarkdownファイルを読み込み
        data_dir = project_root / "data"
        markdown_files = list(data_dir.glob("posts_generated_takano_*.md"))

        if not markdown_files:
            print("❌ posts_generated_takano_*.md ファイルが見つかりません")
            sys.exit(1)

        latest_file = max(markdown_files, key=lambda f: f.stat().st_mtime)
        print(f"📄 入力ファイル: {latest_file.name}")

        markdown_content = latest_file.read_text(encoding="utf-8")

        # 2. 案2のみ抽出（テスト用）
        variant_data = extract_variant_content(markdown_content, 2)

        if not variant_data:
            print("❌ 案2の抽出に失敗しました")
            sys.exit(1)

        print(f"✅ 案2抽出成功")
        print(f"   タイトル: {variant_data['title'][:50]}...")
        print(f"   本文長: {len(variant_data['body'])} 文字")
        print()

        # 3. 投稿計画（30分後に予約）
        JST = timezone(timedelta(hours=9))
        scheduled_time = datetime.now(JST) + timedelta(minutes=30)

        print("=" * 60)
        print("投稿計画（テスト）")
        print("=" * 60)
        print(f"📅 予約時刻: {scheduled_time.strftime('%Y-%m-%d %H:%M')} JST")
        print(f"   案2: 【テスト】{variant_data['title'][:50]}...")
        print()

        # 投稿内容のプレビュー
        print("=" * 60)
        print("投稿内容プレビュー（冒頭200文字）")
        print("=" * 60)
        print(variant_data['full_content'][:200] + "...")
        print()

        # タイトル重複チェック結果
        title_count = variant_data['full_content'].count(variant_data['title'])
        print("=" * 60)
        print("タイトル重複チェック結果")
        print("=" * 60)
        print(f"タイトルの出現回数: {title_count}")
        print(f"検証結果: {'✅ 正常（1回のみ）' if title_count == 1 else '❌ 異常（重複あり）'}")
        print()

        if title_count != 1:
            print("⚠️  タイトルが重複しています！投稿を中止します。")
            sys.exit(1)

        # 4. 自動実行（ユーザー確認なし）
        print("=" * 60)
        print("⚠️  注意: この投稿はLate APIに予約投稿されます")
        print("=" * 60)
        print("✅ 自動実行モード: テスト投稿を開始します")

        print()
        print("=" * 60)
        print("Late API投稿実行中...")
        print("=" * 60)
        print()

        # 5. Late API POST
        print(f"📤 案2を投稿中...")
        print(f"   タイトル: 【テスト】{variant_data['title'][:50]}...")
        print(f"   予約日時: {scheduled_time.strftime('%Y-%m-%d %H:%M')} JST")

        result = post_to_late_api(variant_data["full_content"], scheduled_time)

        post_id = result.get("post", {}).get("_id") or result.get("id")

        print(f"   ✅ 成功! Post ID: {post_id}")
        print()

        # 6. 結果保存
        result_file = data_dir / f"late_api_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(result_file, "w", encoding="utf-8") as f:
            json.dump({
                "test_type": "title_duplicate_fix_verification",
                "executed_at": datetime.now(JST).isoformat(),
                "scheduled_for": scheduled_time.isoformat(),
                "platform": "linkedin",
                "variant": "案2",
                "title_duplicate_check": {
                    "title_count": title_count,
                    "status": "pass" if title_count == 1 else "fail"
                },
                "post_id": post_id,
                "api_response": result
            }, f, indent=2, ensure_ascii=False)

        print("=" * 60)
        print("実行完了")
        print("=" * 60)
        print(f"💾 結果保存: {result_file.name}")
        print()
        print("🎉 テスト投稿が成功しました！")
        print()
        print("📊 Late APIダッシュボードで確認:")
        print("   https://getlate.dev/dashboard")
        print()
        print(f"⏰ 投稿予定時刻: {scheduled_time.strftime('%Y-%m-%d %H:%M')} JST")
        print(f"   （約{(scheduled_time - datetime.now(JST)).seconds // 60}分後）")
        print()
        print("✅ タイトル重複: なし（1回のみ表示）")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ エラー: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
