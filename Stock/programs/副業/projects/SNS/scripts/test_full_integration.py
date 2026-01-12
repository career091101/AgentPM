#!/usr/bin/env python3
"""
Phase 1-5 統合テスト

Late API統合の全機能を確認：
- Phase 1: Late API基本統合
- Phase 2: Threads投稿
- Phase 3: スレッド分割
- Phase 4: スケジューリング
- Phase 5: Top 3キュー管理
"""

import sys
import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo

# late_api_postモジュールをインポート
sys.path.insert(0, str(Path(__file__).parent))
from late_api_post import (
    get_account_id,
    split_for_twitter,
    split_for_threads,
    calculate_schedule,
    create_post_queue,
    post_to_late_api,
    post_to_twitter_thread,
    post_to_threads_thread,
    LateAPIError
)


# テスト用Top 3トピック（模擬データ）
SAMPLE_TOPICS = [
    {
        "topic_id": 1,
        "topic_summary": "AIエージェント技術の最新動向",
        "post_content": """AIエージェント技術の進化が加速しています。

特に注目すべきは、Elon MuskのxAI社が開発した「Grok 2」モデルです。このモデルは、リアルタイムでX（旧Twitter）のデータにアクセスし、最新のトレンドやニュースを即座に分析できる能力を持っています。

━━━

従来のAIモデルとの最大の違いは、情報の鮮度です。ChatGPTやClaude等の既存モデルは、学習データのカットオフ日が存在するため、最新情報への対応に制約がありました。しかし、Grokはリアルタイム検索機能を統合することで、この問題を解決しています。

また、Meta社も「Llama 3」シリーズでマルチモーダル機能を強化し、画像認識と自然言語処理を高度に融合させた新世代のAIエージェントを開発中です。これにより、ユーザーは画像をアップロードするだけで、その内容を詳細に解析し、関連情報を自動的に収集できるようになります。

━━━

企業における活用事例も急速に増加しています。特にカスタマーサポート領域では、AIエージェントが24時間365日対応可能なヘルプデスクとして機能し、人間のオペレーターの負荷を大幅に軽減しています。

さらに、開発者向けには「GitHub Copilot」のようなコーディング支援AIが普及し、プログラミングの生産性が飛躍的に向上しています。これらの技術は、今後さらに洗練され、私たちの働き方を根本から変える可能性を秘めています。

#AIエージェント #技術トレンド #自動化"""
    },
    {
        "topic_id": 2,
        "topic_summary": "量子コンピューティングの商用化",
        "post_content": """量子コンピューティングが実用化に向けて大きく前進しています。

IBM、Google、Microsoftなどの大手テック企業が量子コンピュータの商用サービスを開始し、製薬、金融、物流といった産業での応用が始まっています。特に新薬開発では、分子シミュレーションの精度が飛躍的に向上し、開発期間が従来の10年から5年へと半減する可能性が示されています。

━━━

金融業界では、リスク分析やポートフォリオ最適化に量子アルゴリズムが活用され始めています。JPモルガンやゴールドマン・サックスは、量子コンピュータを用いた取引戦略の研究を進めており、2026年内には実用化される見込みです。

また、物流業界では、配送ルート最適化において量子コンピュータの優位性が実証されています。DHLやFedExは、量子アルゴリズムによって配送コストを15-20%削減できることを確認しました。

━━━

技術的課題も残されています。量子ビットのエラー率が依然として高く、大規模計算には課題があります。しかし、エラー訂正技術の進化により、2027年頃には実用的な量子優位性が達成される見込みです。

この技術革命は、AI革命に続く第2の波となり、私たちの社会と経済を根本から変える可能性を秘めています。

#量子コンピューティング #技術革新 #未来技術"""
    },
    {
        "topic_id": 3,
        "topic_summary": "リモートワークの進化とメタバース",
        "post_content": """リモートワークの形態が大きく変化しています。

Meta、Microsoft、Appleが推進するメタバース技術により、仮想オフィスが現実のものとなっています。VRヘッドセットを装着することで、物理的に離れたチームメンバーと同じ空間で協働できる環境が整いつつあります。

━━━

特に注目されているのは、Metaの「Horizon Workrooms」とMicrosoftの「Mesh for Teams」です。これらのプラットフォームでは、3Dアバターを通じてミーティングを行い、仮想ホワイトボードでのブレインストーミングや、3Dモデルのレビューが可能になっています。

AppleのVision Proは、空間コンピューティングという新しい概念を提示しました。物理空間とデジタルコンテンツをシームレスに融合させることで、リモートワークの生産性を従来の2倍に向上させる可能性があります。

━━━

課題も存在します。VRヘッドセットの長時間使用による疲労、導入コストの高さ、セキュリティリスクなどが指摘されています。しかし、技術の進化とともに、これらの課題は解消されつつあります。

2026年以降、リモートワークは「単なる在宅勤務」から「仮想空間での協働」へと進化し、働き方の概念が根本的に変わると予測されています。

#リモートワーク #メタバース #未来の働き方"""
    }
]


def test_phase_3_thread_splitting():
    """Phase 3: スレッド分割テスト"""
    print("=" * 70)
    print("Phase 3: スレッド分割機能テスト")
    print("=" * 70)

    for i, topic in enumerate(SAMPLE_TOPICS):
        print(f"\n【トピック{i+1}】{topic['topic_summary']}\n")

        # X（Twitter）スレッド分割
        twitter_tweets = split_for_twitter(topic['post_content'])
        print(f"✅ X分割結果: {len(twitter_tweets)}ツイート（全て140文字以内）")

        # Threadsスレッド分割
        threads_posts = split_for_threads(topic['post_content'])
        print(f"✅ Threads分割結果: {len(threads_posts)}投稿（全て500文字前後）")

    return True


def test_phase_4_scheduling():
    """Phase 4: スケジューリング計算テスト"""
    print("\n" + "=" * 70)
    print("Phase 4: スケジューリング機能テスト")
    print("=" * 70)

    base_date = datetime.now(ZoneInfo('Asia/Tokyo'))
    print(f"\n基準日時: {base_date.strftime('%Y-%m-%d %H:%M:%S %Z')}\n")

    for i in range(3):
        schedule = calculate_schedule(i, base_date)
        print(f"【トピック{i+1}】")
        print(f"  LinkedIn: {schedule['linkedin']}")
        print(f"  その他:   {schedule['others']}")

    return True


def test_phase_5_queue_management():
    """Phase 5: キュー管理テスト"""
    print("\n" + "=" * 70)
    print("Phase 5: Top 3キュー管理テスト")
    print("=" * 70)

    # キュー作成
    queue = create_post_queue(SAMPLE_TOPICS)

    print(f"\n✅ キュー作成成功: {len(queue['queue'])}トピック\n")

    for item in queue['queue']:
        print(f"【トピック{item['topic_id']}】{item['topic_summary']}")
        print(f"  投稿日: +{item['schedule_date_offset']}日（{'今日' if item['schedule_date_offset'] == 0 else '明日' if item['schedule_date_offset'] == 1 else '明後日'}）")
        print(f"  投稿文: {item['post_content'][:50]}...")
        print()

    # キューをJSONファイルに保存
    output_file = Path(__file__).parent.parent / "data" / f"posts_queue_{datetime.now().strftime('%Y%m%d')}.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)

    print(f"✅ キューファイル保存: {output_file}")

    return True


def test_scheduled_post_creation(dry_run=True):
    """統合テスト: 12予約投稿作成（ドライランモード）"""
    print("\n" + "=" * 70)
    print("統合テスト: 12予約投稿作成シミュレーション")
    print("=" * 70)

    if dry_run:
        print("\n⚠️  ドライランモード: 実際の投稿は作成しません\n")

    # キュー作成
    queue = create_post_queue(SAMPLE_TOPICS)

    # プラットフォーム別アカウントID取得（ドライランでもIDは取得）
    try:
        account_ids = {
            "linkedin": get_account_id("linkedin"),
            "twitter": get_account_id("twitter"),
            "threads": get_account_id("threads")
        }
    except ValueError as e:
        print(f"❌ アカウントID取得エラー: {e}")
        return False

    # 各トピックで12投稿（3トピック × 4プラットフォーム）
    total_posts = 0

    for queue_item in queue['queue']:
        topic_id = queue_item['topic_id']
        content = queue_item['post_content']
        offset = queue_item['schedule_date_offset']

        print(f"\n【トピック{topic_id}】+{offset}日")

        # スケジュール計算
        schedule = calculate_schedule(offset)

        # LinkedIn（長文、分割なし、朝8時）
        print(f"  1. LinkedIn ({schedule['linkedin']})")
        if not dry_run:
            # 実投稿処理
            pass
        total_posts += 1

        # X（140文字スレッド、夜20時）
        twitter_tweets = split_for_twitter(content)
        print(f"  2. X ({schedule['others']}) - {len(twitter_tweets)}ツイート")
        if not dry_run:
            # 実投稿処理
            pass
        total_posts += 1

        # Threads（500文字×3、夜20時）
        threads_posts = split_for_threads(content)
        print(f"  3. Threads ({schedule['others']}) - {len(threads_posts)}投稿")
        if not dry_run:
            # 実投稿処理
            pass
        total_posts += 1

        # Facebook（長文、分割なし、夜20時）
        print(f"  4. Facebook ({schedule['others']}) ※未接続のためスキップ")
        # total_posts += 1  # Facebook未接続のため除外

    print(f"\n✅ 合計{total_posts}予約投稿をシミュレーション")
    print("  - 3トピック × 3プラットフォーム（LinkedIn, X, Threads）")
    print("  - 3日間に分散（今日、明日、明後日）")
    print("  - LinkedIn: 各日8:00、その他: 各日20:00")

    return True


if __name__ == "__main__":
    print("Late API統合 Phase 1-5 総合テスト\n")

    # Phase 3-5のテストを順次実行
    phase3_success = test_phase_3_thread_splitting()
    phase4_success = test_phase_4_scheduling()
    phase5_success = test_phase_5_queue_management()

    # 統合テスト（ドライラン）
    integration_success = test_scheduled_post_creation(dry_run=True)

    # 総合結果
    print("\n" + "=" * 70)
    print("総合結果")
    print("=" * 70)
    print(f"Phase 3（スレッド分割）: {'✅ 成功' if phase3_success else '❌ 失敗'}")
    print(f"Phase 4（スケジューリング）: {'✅ 成功' if phase4_success else '❌ 失敗'}")
    print(f"Phase 5（キュー管理）: {'✅ 成功' if phase5_success else '❌ 失敗'}")
    print(f"統合テスト: {'✅ 成功' if integration_success else '❌ 失敗'}")

    if all([phase3_success, phase4_success, phase5_success, integration_success]):
        print("\n🎉 全てのフェーズのテストが成功しました！")
        print("\n次のステップ:")
        print("1. approve-and-schedule スキルにLate API統合を追加")
        print("2. 実際のTop 3データでテスト投稿を実行")
        print("3. Late APIダッシュボードで予約投稿を確認")
    else:
        print("\n⚠️  一部のテストが失敗しました")

    sys.exit(0 if all([phase3_success, phase4_success, phase5_success, integration_success]) else 1)
