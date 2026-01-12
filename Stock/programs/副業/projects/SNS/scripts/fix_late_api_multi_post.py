#!/usr/bin/env python3
"""
Late API 3案別々投稿スクリプト（修正版）

問題: 1投稿に3案が全て入る
原因: コンテンツ抽出と投稿ループの実装が不正確
解決: 各案を個別に抽出し、確実に3回POSTリクエストを送信

Usage:
    python3 scripts/fix_late_api_multi_post.py
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime, timedelta
import requests

# pytz代替: datetimeのtimezoneを使用
from datetime import timezone

# プロジェクトルート設定
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root / "scripts"))


def extract_variant_content(markdown: str, variant_number: int) -> dict:
    """
    案Nのタイトルと本文を抽出（Markdown装飾除去版）

    Args:
        markdown: Phase 3生成されたMarkdownファイルの内容
        variant_number: バリアント番号（1, 2, 3）

    Returns:
        dict: {"title": str, "body": str, "full_content": str}
              full_content = title + "\n\n" + body
        None: 抽出失敗時
    """
    # 案N: パターンX → ### タイトル → ### 本文 → --- の構造を抽出
    pattern = rf'## 案{variant_number}:.*?\n\n### タイトル\n\*\*(.*?)\*\*\n\n### 本文.*?\n\n(.*?)(?=\n---\n|\Z)'
    match = re.search(pattern, markdown, re.DOTALL)

    if not match:
        return None

    # タイトルと本文を抽出
    title = match.group(1).strip()
    body = match.group(2).strip()

    # Markdown装飾を除去
    def remove_markdown(text):
        """Markdown装飾を除去"""
        # **太字** → 通常テキスト
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        # - 箇条書き → 通常テキスト
        text = re.sub(r'^\- ', '', text, flags=re.MULTILINE)
        # 1. 番号付きリスト → 通常テキスト
        text = re.sub(r'^\d+\. ', '', text, flags=re.MULTILINE)
        return text

    title_clean = remove_markdown(title)
    body_clean = remove_markdown(body)

    # 【修正】本文1行目がタイトルと同じ場合は除去（タイトル重複防止）
    body_lines = body_clean.split('\n')
    if body_lines and body_lines[0].strip().rstrip('。！？') == title_clean.strip():
        # 1行目（タイトル重複）を除去
        body_clean = '\n'.join(body_lines[1:]).strip()

    # 完全なコンテンツ = タイトル + 本文（タイトル重複除去済み）
    full_content = f"{title_clean}\n\n{body_clean}"

    return {
        "title": title_clean,
        "body": body_clean,
        "full_content": full_content
    }


def post_to_late_api(content: str, scheduled_datetime: datetime) -> dict:
    """
    Late APIに1件の投稿を送信

    Args:
        content: 投稿本文
        scheduled_datetime: 予約日時（JST）

    Returns:
        dict: Late APIレスポンス

    Raises:
        Exception: API呼び出し失敗時
    """
    # 環境変数を直接.envファイルから読み込み
    env_file = project_root / ".env"
    env_vars = {}

    if env_file.exists():
        with open(env_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    # インラインコメント除去（クォート外の # 以降を削除）
                    if "#" in value:
                        # クォート内かどうかチェック
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
                                # クォート外の # 以降は切り捨て
                                break
                            clean_value.append(ch)
                        value = "".join(clean_value)

                    # クォート除去
                    value = value.strip().strip('"').strip("'")
                    env_vars[key.strip()] = value

    api_key = env_vars.get("LATE_API_KEY")
    linkedin_account_id = env_vars.get("LATE_LINKEDIN_ACCOUNT_ID")

    if not api_key:
        raise ValueError(f"LATE_API_KEY not found in .env file. Available keys: {list(env_vars.keys())}")

    if not linkedin_account_id:
        raise ValueError(f"LATE_LINKEDIN_ACCOUNT_ID not found in .env file. Available keys: {list(env_vars.keys())}")

    # 正しいエンドポイント（設定ファイルから確認済み）
    base_url = "https://getlate.dev/api/v1"

    # UTCに変換 (JST = UTC+9)
    JST = timezone(timedelta(hours=9))
    UTC = timezone.utc

    if scheduled_datetime.tzinfo is None:
        scheduled_datetime = scheduled_datetime.replace(tzinfo=JST)

    # ISO8601形式に変換（JSTタイムゾーン付き）
    scheduled_datetime_str = scheduled_datetime.strftime("%Y-%m-%dT%H:%M:%S%z")
    # %z は +0900 形式なので、コロン挿入して +09:00 にする
    if len(scheduled_datetime_str) >= 5:
        scheduled_datetime_str = scheduled_datetime_str[:-2] + ':' + scheduled_datetime_str[-2:]

    # リクエストボディ（late_api_post.pyと同じスキーマ）
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

    # API呼び出し
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

    # エラーハンドリング
    if response.status_code not in [200, 201]:
        error_msg = f"Late API Error: {response.status_code} - {response.text}"
        raise Exception(error_msg)

    return response.json()


def main():
    """メイン処理"""
    print("=" * 60)
    print("Late API 3案別々投稿スクリプト（修正版）")
    print("=" * 60)
    print()

    try:
        # 1. Phase 3生成されたMarkdownファイルを読み込み
        data_dir = project_root / "data"

        # 最新のposts_generated_takano_*.mdファイルを検索
        markdown_files = list(data_dir.glob("posts_generated_takano_*.md"))

        if not markdown_files:
            print("❌ posts_generated_takano_*.md ファイルが見つかりません")
            sys.exit(1)

        # 最新ファイルを取得
        latest_file = max(markdown_files, key=lambda f: f.stat().st_mtime)
        print(f"📄 入力ファイル: {latest_file.name}")

        markdown_content = latest_file.read_text(encoding="utf-8")

        # 2. 3案すべてを個別に抽出
        variants = []
        for variant_num in [1, 2, 3]:
            variant_data = extract_variant_content(markdown_content, variant_num)

            if not variant_data:
                print(f"⚠️  案{variant_num}の抽出に失敗しました")
                continue

            variants.append({
                "variant_num": variant_num,
                "title": variant_data["title"],
                "body": variant_data["body"],
                "full_content": variant_data["full_content"]
            })

            print(f"✅ 案{variant_num}抽出成功")
            print(f"   タイトル: {variant_data['title'][:50]}...")
            print(f"   本文長: {len(variant_data['body'])} 文字")
            print()

        if len(variants) != 3:
            print(f"❌ 3案すべての抽出に失敗しました（抽出成功: {len(variants)}件）")
            sys.exit(1)

        # 3. 投稿計画を作成（案2 → 案1 → 案3 の順で Jan 7, 8, 9）
        JST = timezone(timedelta(hours=9))
        base_date = datetime.now(JST).replace(hour=8, minute=0, second=0, microsecond=0)

        # 翌々日から3日間（Jan 7, 8, 9）
        posting_plan = [
            {"variant_num": 2, "date": base_date + timedelta(days=2)},  # Jan 7
            {"variant_num": 1, "date": base_date + timedelta(days=3)},  # Jan 8
            {"variant_num": 3, "date": base_date + timedelta(days=4)},  # Jan 9
        ]

        print("=" * 60)
        print("投稿計画")
        print("=" * 60)
        for plan in posting_plan:
            variant = next(v for v in variants if v["variant_num"] == plan["variant_num"])
            print(f"📅 {plan['date'].strftime('%Y-%m-%d %H:%M')} JST")
            print(f"   案{plan['variant_num']}: {variant['title'][:60]}...")
            print()

        # 4. ユーザー確認
        print("=" * 60)
        confirm = input("上記の計画で投稿を実行しますか？ (y/n): ")

        if confirm.lower() != 'y':
            print("❌ 実行をキャンセルしました")
            sys.exit(0)

        print()
        print("=" * 60)
        print("Late API投稿実行中...")
        print("=" * 60)
        print()

        # 5. 3案すべてを個別にPOST
        results = []

        for plan in posting_plan:
            variant = next(v for v in variants if v["variant_num"] == plan["variant_num"])
            variant_num = plan["variant_num"]
            scheduled_datetime = plan["date"]

            print(f"📤 案{variant_num}を投稿中...")
            print(f"   タイトル: {variant['title'][:60]}...")
            print(f"   予約日時: {scheduled_datetime.strftime('%Y-%m-%d %H:%M')} JST")

            try:
                # Late API POST
                result = post_to_late_api(variant["full_content"], scheduled_datetime)

                post_id = result.get("post", {}).get("_id") or result.get("id")

                print(f"   ✅ 成功! Post ID: {post_id}")
                print()

                results.append({
                    "variant": f"案{variant_num}",
                    "status": "success",
                    "post_id": post_id,
                    "scheduled_for": scheduled_datetime.isoformat(),
                    "platform": "linkedin",
                    "title": variant["title"]
                })

            except Exception as e:
                print(f"   ❌ 失敗: {e}")
                print()

                results.append({
                    "variant": f"案{variant_num}",
                    "status": "error",
                    "error_message": str(e),
                    "scheduled_for": scheduled_datetime.isoformat(),
                    "platform": "linkedin"
                })

        # 6. 結果保存
        result_file = data_dir / f"late_api_fixed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(result_file, "w", encoding="utf-8") as f:
            json.dump({
                "executed_at": datetime.now(JST).isoformat(),
                "target_dates": [plan["date"].strftime("%Y-%m-%d") for plan in posting_plan],
                "platform": "linkedin",
                "results": results
            }, f, indent=2, ensure_ascii=False)

        print("=" * 60)
        print("実行完了")
        print("=" * 60)
        print(f"💾 結果保存: {result_file.name}")

        # 7. サマリー表示
        success_count = sum(1 for r in results if r["status"] == "success")
        failed_count = len(results) - success_count

        print()
        print(f"✅ 成功: {success_count}/3 案")
        print(f"❌ 失敗: {failed_count}/3 案")

        if success_count == 3:
            print()
            print("🎉 全3案の投稿が成功しました！")
            print("Late APIダッシュボードで確認してください:")
            print("https://getlate.dev/dashboard")
        elif success_count > 0:
            print()
            print("⚠️  一部の案が失敗しました")
            for r in results:
                if r["status"] == "error":
                    print(f"   - {r['variant']}: {r.get('error_message', 'Unknown error')}")
        else:
            print()
            print("❌ 全ての案が失敗しました")
            print("エラーログを確認してください")

        print("=" * 60)

    except Exception as e:
        print(f"\n❌ エラー: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
