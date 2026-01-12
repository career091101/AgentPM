#!/usr/bin/env python3
"""
高野式LinkedIn投稿 → Threads A/Bテスト投稿スクリプト

目的:
- Pattern A（データドリブン型、400-500字）
- Pattern B（簡潔型、300-350字）
を異なる時刻にThreads予約投稿し、72時間後のエンゲージメントを比較

使用方法:
    python3 post_takano_threads_ab_test.py
"""

import sys
import os
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import json

# late_api_post.pyをインポート
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from late_api_post import (
    post_to_late_api,
    get_account_id,
    find_available_dates,
    LateAPIError
)


# Pattern A: データドリブン型（430文字）
PATTERN_A = """🚨 OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か。

日本経済新聞が警告。OpenAIが200兆円規模のインフラ投資を発表。その資金調達手法はITバブル期に類似する「循環投資」だ。

主要データ:
- 総額約200兆円（日本の国家予算2年分）
- 孫正義が3.5兆円追加投資、出資比率11%確保
- OpenAI社員平均年収2.2億円、売上の半分が人件費

でも、ここからが本当の話だ。負債カバー率は10%台でまだ余裕あり。Armの株を担保に115億ドル調達済み。

日経は「循環が止まった瞬間に連鎖破綻のリスク」と指摘。AI業界の未来は、この循環投資が本物の成長につながるか、バブル崩壊で終わるか。

あなたの会社は、この変化にどう対処する？"""

# Pattern B: 簡潔型（295文字）
PATTERN_B = """🚨 OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、マジでITバブルの再来だ。

日本経済新聞が警告。OpenAIが200兆円規模のインフラ投資を発表。孫正義が3.5兆円追加投資で出資比率11%確保。社員平均年収は2.2億円。

でも、マジでここからが本当の話。日経は「循環が止まった瞬間に連鎖破綻のリスク」と指摘。AI業界の未来は、バブル崩壊か本物の成長か。

あなたの会社はどう対処する？"""


def main():
    """メイン実行"""
    print("=" * 70)
    print("高野式LinkedIn → Threads A/Bテスト投稿")
    print("=" * 70)
    print()

    # Threadsアカウント取得
    try:
        threads_account_id = get_account_id("threads")
        print(f"✅ Threadsアカウント取得成功: {threads_account_id}")
    except Exception as e:
        print(f"❌ エラー: Threadsアカウントが見つかりません")
        print(f"詳細: {e}")
        return

    # 利用可能日付を2日分取得
    print("\n📅 利用可能日付を検索中...")
    try:
        date_info = find_available_dates(count=2)
        available_dates = date_info['available_dates']
        print(f"✅ 利用可能日付: {[str(d) for d in available_dates]}")

        if date_info['existing_scheduled_count'] > 0:
            print(f"📊 既存予約投稿: {date_info['existing_scheduled_count']}件")
            print(f"🚫 8:00 AM予約済み日付: {[str(d) for d in date_info['reserved_8am_dates']]}")
    except Exception as e:
        print(f"❌ 日付検索エラー: {e}")
        return

    # スケジュール設定
    jst = ZoneInfo('Asia/Tokyo')

    # Pattern A: 翌日 12:00 JST（昼休み時間帯）
    pattern_a_datetime = datetime.combine(
        available_dates[0],
        datetime.min.time()
    ).replace(hour=12, minute=0, second=0, tzinfo=jst)

    # Pattern B: 翌日 20:00 JST（夜リラックス時間帯）
    pattern_b_datetime = datetime.combine(
        available_dates[0],
        datetime.min.time()
    ).replace(hour=20, minute=0, second=0, tzinfo=jst)

    # 投稿計画表示
    print("\n" + "=" * 70)
    print("📋 投稿計画")
    print("=" * 70)
    print()
    print(f"Pattern A（データドリブン型、430文字）")
    print(f"  予約日時: {pattern_a_datetime.strftime('%Y-%m-%d %H:%M JST')}")
    print(f"  期待ER: 3-4%")
    print(f"  文字数: {len(PATTERN_A)}字")
    print()
    print(f"Pattern B（簡潔型、295文字）")
    print(f"  予約日時: {pattern_b_datetime.strftime('%Y-%m-%d %H:%M JST')}")
    print(f"  期待ER: 6-7%")
    print(f"  文字数: {len(PATTERN_B)}字")
    print()

    # ユーザー確認
    print("=" * 70)
    confirm = input("この内容でThreadsに予約投稿しますか？ (y/n): ").strip().lower()

    if confirm != 'y':
        print("\n❌ 投稿をキャンセルしました")
        return

    print("\n🚀 Late API経由でThreads予約投稿を実行中...")
    print()

    # Pattern A投稿
    print("📤 Pattern A投稿中...")
    try:
        result_a = post_to_late_api(
            content=PATTERN_A,
            platform="threads",
            account_id=threads_account_id,
            scheduled_for=pattern_a_datetime.isoformat(),
            timezone="Asia/Tokyo"
        )

        post_id_a = result_a.get("id", "unknown")
        print(f"✅ Pattern A予約完了")
        print(f"   Post ID: {post_id_a}")
        print(f"   URL: https://app.getlate.dev/posts/{post_id_a}")
        print()

    except LateAPIError as e:
        print(f"❌ Pattern A投稿失敗: {e}")
        result_a = {"status": "error", "error": str(e)}

    # Pattern B投稿
    print("📤 Pattern B投稿中...")
    try:
        result_b = post_to_late_api(
            content=PATTERN_B,
            platform="threads",
            account_id=threads_account_id,
            scheduled_for=pattern_b_datetime.isoformat(),
            timezone="Asia/Tokyo"
        )

        post_id_b = result_b.get("id", "unknown")
        print(f"✅ Pattern B予約完了")
        print(f"   Post ID: {post_id_b}")
        print(f"   URL: https://app.getlate.dev/posts/{post_id_b}")
        print()

    except LateAPIError as e:
        print(f"❌ Pattern B投稿失敗: {e}")
        result_b = {"status": "error", "error": str(e)}

    # 結果サマリー保存
    output_data = {
        "executed_at": datetime.now(jst).isoformat(),
        "test_type": "takano_linkedin_to_threads_ab_test",
        "pattern_a": {
            "variant": "データドリブン型",
            "content": PATTERN_A,
            "character_count": len(PATTERN_A),
            "scheduled_for": pattern_a_datetime.isoformat(),
            "expected_er": "3-4%",
            "result": result_a
        },
        "pattern_b": {
            "variant": "簡潔型",
            "content": PATTERN_B,
            "character_count": len(PATTERN_B),
            "scheduled_for": pattern_b_datetime.isoformat(),
            "expected_er": "6-7%",
            "result": result_b
        },
        "measurement_window": {
            "start": pattern_a_datetime.isoformat(),
            "end": (pattern_b_datetime + timedelta(hours=72)).isoformat(),
            "note": "72時間後にエンゲージメント測定"
        }
    }

    output_path = f"/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/threads_ab_test_{datetime.now(jst).strftime('%Y%m%d_%H%M%S')}.json"

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print("✅ A/Bテスト投稿完了")
    print("=" * 70)
    print()
    print(f"📊 結果ファイル: {output_path}")
    print()
    print("📅 次のアクション:")
    print(f"  1. {(pattern_a_datetime + timedelta(hours=72)).strftime('%Y-%m-%d %H:%M')} - Pattern Aエンゲージメント測定")
    print(f"  2. {(pattern_b_datetime + timedelta(hours=72)).strftime('%Y-%m-%d %H:%M')} - Pattern Bエンゲージメント測定")
    print(f"  3. エンゲージメント比較分析")
    print()
    print("Late APIダッシュボード: https://app.getlate.dev/dashboard")
    print()


if __name__ == "__main__":
    main()
