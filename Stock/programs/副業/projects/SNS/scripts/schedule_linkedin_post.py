#!/usr/bin/env python3
"""
LinkedIn 3案自動予約投稿スクリプト（Late API統合）

機能:
1. SNS自動化スキルからコンテンツ取得（高野メソッド3案）
2. Late APIから最新予約投稿日を取得し、翌日8:00 JSTに予約
3. 3案すべてを同じ時刻に予約投稿
4. エラー時は手動投稿用Markdownファイル生成
5. ログ保存（data/post_result_scheduled_YYYYMMDD.json）

Usage:
    python3 scripts/schedule_linkedin_post.py
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv

# プロジェクトルート設定
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root / "scripts"))

# 自作モジュールインポート
from late_api_client import LateAPIClient
from generate_linkedin_3_cases import generate_3_cases

# .env読み込み
load_dotenv(project_root / ".env")


def get_next_schedule_date() -> datetime:
    """
    最新の予約投稿日の翌日を取得

    Returns:
        datetime: 翌日8:00 JST
    """
    data_dir = project_root / "data"

    # post_result_scheduled_*.json から最新日を取得
    scheduled_files = list(data_dir.glob("post_result_scheduled_*.json"))

    if not scheduled_files:
        # ファイルがない場合は明日8:00
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.replace(hour=8, minute=0, second=0, microsecond=0)

    # 最新ファイルから日付を抽出
    latest_file = max(scheduled_files, key=lambda f: f.stat().st_mtime)
    date_str = latest_file.stem.split("_")[-1]  # YYYYMMDD

    # 日付パース
    latest_date = datetime.strptime(date_str, "%Y%m%d")

    # 翌日8:00を返す
    next_date = latest_date + timedelta(days=1)
    return next_date.replace(hour=8, minute=0, second=0, microsecond=0)


def save_manual_post_markdown(cases: list, schedule_date: datetime, error_msg: str):
    """
    Late API失敗時の手動投稿用Markdownファイル生成

    Args:
        cases: 3案のリスト
        schedule_date: 予定投稿日時
        error_msg: エラーメッセージ
    """
    manual_dir = project_root / "data" / "manual_posts"
    manual_dir.mkdir(exist_ok=True)

    filename = f"linkedin_{schedule_date.strftime('%Y%m%d')}.md"
    filepath = manual_dir / filename

    markdown_content = f"""# LinkedIn 手動投稿（Late API 失敗時）

**日付**: {schedule_date.strftime('%Y-%m-%d')}
**予定時刻**: 08:00 JST

---

## 案1（{cases[0]['type']}）

{cases[0]['content']}

**ハッシュタグ**: {cases[0]['hashtags']}

---

## 案2（{cases[1]['type']}）

{cases[1]['content']}

**ハッシュタグ**: {cases[1]['hashtags']}

---

## 案3（{cases[2]['type']}）

{cases[2]['content']}

**ハッシュタグ**: {cases[2]['hashtags']}

---

**エラー理由**: {error_msg}

**手動投稿方法**:
1. Late APIダッシュボード (https://getlate.dev/dashboard) にアクセス
2. 上記3案から1案を選択
3. LinkedInに手動投稿
"""

    filepath.write_text(markdown_content, encoding="utf-8")
    print(f"📝 手動投稿用Markdownファイル生成: {filepath}")


def main():
    """メイン処理"""
    print("=" * 60)
    print("LinkedIn 3案自動予約投稿")
    print("=" * 60)
    print()

    try:
        # 1. 次の予約投稿日を取得
        next_date = get_next_schedule_date()
        print(f"📅 予約投稿日: {next_date.strftime('%Y-%m-%d %H:%M:%S')} JST\n")

        # 2. コンテンツ生成（3案）
        print("🔄 コンテンツ生成中...")
        cases = generate_3_cases()
        print(f"✅ 3案生成完了\n")

        # 3. Late APIクライアント初期化
        client = LateAPIClient()

        # 4. 3案すべてを予約投稿
        results = []
        for i, case in enumerate(cases, 1):
            print(f"📤 案{i}（{case['type']}）を予約投稿中...")

            try:
                # ハッシュタグを本文に追加
                full_content = f"{case['content']}\n\n{case['hashtags']}"

                # Late API呼び出し
                result = client.schedule_linkedin_post(full_content, next_date)

                post_id = result["post"]["_id"]
                print(f"   ✅ 成功! Post ID: {post_id}\n")

                results.append(
                    {
                        "case": i,
                        "type": case["type"],
                        "post_id": post_id,
                        "content": full_content,
                        "status": "success",
                    }
                )

            except Exception as e:
                print(f"   ❌ 失敗: {e}\n")

                # 失敗時はMarkdownファイル生成
                save_manual_post_markdown(cases, next_date, str(e))

                results.append(
                    {
                        "case": i,
                        "type": case["type"],
                        "status": "failed",
                        "error": str(e),
                    }
                )

        # 5. ログ保存
        log_file = (
            project_root
            / "data"
            / f"post_result_scheduled_{next_date.strftime('%Y%m%d')}.json"
        )
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "scheduled_date": next_date.isoformat(),
                    "scheduled_time_jst": next_date.strftime("%Y-%m-%d %H:%M:%S JST"),
                    "results": results,
                },
                f,
                indent=2,
                ensure_ascii=False,
            )

        print(f"💾 ログ保存完了: {log_file}")

        # 6. 結果サマリー
        success_count = sum(1 for r in results if r["status"] == "success")
        print("\n" + "=" * 60)
        print(f"✅ 完了: {success_count}/3 案が予約投稿成功")
        if success_count < 3:
            print(f"⚠️  {3 - success_count} 案は手動投稿が必要です")
            print(f"   Markdownファイル: data/manual_posts/linkedin_{next_date.strftime('%Y%m%d')}.md")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ エラー: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
