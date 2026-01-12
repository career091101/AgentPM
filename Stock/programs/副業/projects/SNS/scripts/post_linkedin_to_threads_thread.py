#!/usr/bin/env python3
"""
LinkedIn投稿 → Threadsスレッド形式変換・投稿スクリプト

目的:
- LinkedIn投稿（1,150-1,300字）をThreadsスレッド形式（500字×3投稿）に分割
- Late API経由でThreads予約投稿

使用方法:
    python3 post_linkedin_to_threads_thread.py
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
    split_for_threads,
    LateAPIError
)


# LinkedIn投稿案2（1,195文字）
LINKEDIN_POST = """OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」、ITバブルの再来か。

日本経済新聞が報じた衝撃のレポート。
OpenAIが約200兆円規模のインフラ投資を発表し、その資金調達手法が「売り手と買い手で資金が循環する手法はIT（情報技術）バブル期に類似する」と警告されている。
なぜ世界トップのAI企業が、こんな危うい手法を取るのか。

答えは単純だ。膨大なGPU需要に対し、通常の資金調達では間に合わないから。

**投資規模の異常性**:
- 総額約200兆円のインフラ投資（日本の国家予算2年分に相当）
- OpenAIのスターゲート・プロジェクト: UAEで2026年末までに第1フェーズの200MW容量達成
- ガスタービン4基で発電する巨大データセンター

**循環投資の仕組み**:
vendor financingメカニズム。NVIDIAがGPUを販売 → OpenAIが購入 → その資金をNVIDIAが融資 → OpenAIがさらにGPU購入。
売り手と買い手が同じエコシステム内で資金を循環させる構造。

**OpenAIの財務状況の実態**:
社員平均年収2.2億円。売り上げの半分が人件費に消える。
2024年の売上50億ドルに対し、営業費用が圧倒的に高い。黒字化の見通しは不透明。

でも、ここからが本当の話だ。

これは単なるバブルじゃなく、「AGI（汎用人工知能）獲得競争の最終局面」という側面もある。
孫正義がSoftBankで3.5兆円追加投資し、出資比率11%を確保した理由も同じ。
「OpenAIは地球上で最も価値ある会社になる」（孫正義、2025年6月株主総会）

負債カバー率は10%台で、まだ余裕ありまくり。
Armの株を担保にしたローンで115億ドル、つなぎ融資で150億ドル。

一方、学術界は冷静だ。
MITの研究者は「現在のLLMアーキテクチャは効率性の限界に近づいている」と警告。
データセンター電力需要が2030年までに倍増する試算もある。

日経の指摘が鋭い。
「循環が止まった瞬間に連鎖破綻のリスク」と。
AI業界の未来は、この循環投資が本物の成長につながるか、バブル崩壊で終わるか、その二択だ。

あなたの会社は、この変化にどう対処する？"""


def convert_linkedin_to_threads_thread(linkedin_content: str, max_length: int = 500) -> list:
    """
    LinkedIn投稿をThreadsスレッド形式に変換

    Args:
        linkedin_content: LinkedIn投稿本文
        max_length: Threads1投稿の最大文字数（デフォルト: 500）

    Returns:
        list: Threadsスレッド投稿リスト（3投稿）
    """
    # Markdown装飾を除去
    import re

    # **太字**を除去
    content = re.sub(r'\*\*(.+?)\*\*', r'\1', linkedin_content)

    # 箇条書き記号を除去
    content = re.sub(r'^\- ', '', content, flags=re.MULTILINE)

    # セクション区切りを挿入（━━━で分割するため）
    # 「投資規模の異常性:」→「━━━投資規模の異常性:」
    content = re.sub(r'\n(投資規模の異常性|循環投資の仕組み|OpenAIの財務状況の実態):', r'\n━━━\n\1:', content)

    # split_for_threads関数を使用（late_api_post.pyから）
    threads = split_for_threads(content, max_length=max_length)

    return threads


def main():
    """メイン実行"""
    print("=" * 70)
    print("LinkedIn → Threadsスレッド形式投稿")
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

    # LinkedIn投稿をThreadsスレッドに変換
    print("\n🔄 LinkedIn投稿をThreadsスレッド形式に変換中...")
    threads_posts = convert_linkedin_to_threads_thread(LINKEDIN_POST)

    print(f"✅ 変換完了: {len(threads_posts)}投稿のスレッド")
    print()

    # 各投稿の文字数表示
    for i, post in enumerate(threads_posts, 1):
        print(f"投稿{i}: {len(post)}文字")
        print(f"--- プレビュー ---")
        print(post[:100] + "..." if len(post) > 100 else post)
        print()

    # 利用可能日付を取得
    print("\n📅 利用可能日付を検索中...")
    try:
        date_info = find_available_dates(count=1)
        available_dates = date_info['available_dates']
        print(f"✅ 利用可能日付: {str(available_dates[0])}")

        if date_info['existing_scheduled_count'] > 0:
            print(f"📊 既存予約投稿: {date_info['existing_scheduled_count']}件")
    except Exception as e:
        print(f"❌ 日付検索エラー: {e}")
        return

    # スケジュール設定（翌日20:00 JST）
    jst = ZoneInfo('Asia/Tokyo')
    scheduled_datetime = datetime.combine(
        available_dates[0],
        datetime.min.time()
    ).replace(hour=20, minute=0, second=0, tzinfo=jst)

    # 投稿計画表示
    print("\n" + "=" * 70)
    print("📋 投稿計画")
    print("=" * 70)
    print()
    print(f"形式: Threadsスレッド（{len(threads_posts)}投稿）")
    print(f"予約日時: {scheduled_datetime.strftime('%Y-%m-%d %H:%M JST')}")
    print(f"元LinkedIn投稿: 1,195文字")
    print(f"Threads総文字数: {sum(len(p) for p in threads_posts)}文字")
    print()

    # ユーザー確認
    print("=" * 70)
    confirm = input("この内容でThreadsスレッドとして予約投稿しますか？ (y/n): ").strip().lower()

    if confirm != 'y':
        print("\n❌ 投稿をキャンセルしました")
        return

    print("\n🚀 Late API経由でThreadsスレッド予約投稿を実行中...")
    print()

    # Threadsスレッド投稿
    try:
        # threadItems形式に変換
        thread_items_data = [{"content": post} for post in threads_posts]

        # 最初の投稿をcontentに設定（Late API仕様）
        result = post_to_late_api(
            content=threads_posts[0],
            platform="threads",
            account_id=threads_account_id,
            scheduled_for=scheduled_datetime.isoformat(),
            timezone="Asia/Tokyo",
            platform_specific_data={"threadItems": thread_items_data}
        )

        post_id = result.get("id", "unknown")
        print(f"✅ Threadsスレッド予約完了")
        print(f"   Post ID: {post_id}")
        print(f"   URL: https://app.getlate.dev/posts/{post_id}")
        print(f"   スレッド投稿数: {len(threads_posts)}投稿")
        print()

    except LateAPIError as e:
        print(f"❌ Threads投稿失敗: {e}")
        result = {"status": "error", "error": str(e)}
        return

    # 結果サマリー保存
    output_data = {
        "executed_at": datetime.now(jst).isoformat(),
        "post_type": "linkedin_to_threads_thread",
        "linkedin_source": {
            "variant": "案2（OpenAI × NVIDIA）",
            "character_count": len(LINKEDIN_POST),
            "content": LINKEDIN_POST
        },
        "threads_thread": {
            "post_count": len(threads_posts),
            "total_character_count": sum(len(p) for p in threads_posts),
            "posts": threads_posts,
            "scheduled_for": scheduled_datetime.isoformat(),
            "result": result
        }
    }

    output_path = f"/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/data/linkedin_to_threads_thread_{datetime.now(jst).strftime('%Y%m%d_%H%M%S')}.json"

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print("✅ Threadsスレッド投稿完了")
    print("=" * 70)
    print()
    print(f"📊 結果ファイル: {output_path}")
    print()
    print("Late APIダッシュボード: https://app.getlate.dev/dashboard")
    print()


if __name__ == "__main__":
    main()
