#!/usr/bin/env python3
"""
Batch 1445-1464の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1445-1464の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1445,
        "filename": "image_123.png",
        "description": "Instagramのコメント欄DM会話。ユーザー「なび」が美容・整形ジャンルのNote販売戦略について質問。Kくんが整形クリニックの選択基準やマネタイズ方法についてアドバイスしている。"
    },
    {
        "index": 1446,
        "filename": "image_127.png",
        "description": "SNS攻略サロンの酔醐味とSlackの過去情報まとめのバナー画像。緑色のデザインで「Slack」のロゴが大きく表示されており、情報提供の価値を視覚的に表現している。"
    },
    {
        "index": 1447,
        "filename": "image_129.png",
        "description": "3万個のNOTE販売リンクプレゼントの告知バナー。120ジャンルのnoteからいいねが多い人気noteを厳選し、サロン参加に無料プレゼントという企画内容が記載されている。"
    },
    {
        "index": 1448,
        "filename": "image_01.png",
        "description": "Instagram上でのDM会話スクリーンショット。ユーザー「こば」がNote販売で恋愛系ジャンルの戦略についてKくんに相談している。ストーリー閲覧数やフォロワー数の計算方法について質問している。"
    },
    {
        "index": 1449,
        "filename": "image_02.png",
        "description": "Kくんからの返答メッセージ。Note販売における無料コンテンツ配布とコメント機能活用、istepというDMボットツールの紹介が含まれている。"
    },
    {
        "index": 1450,
        "filename": "image_03.png",
        "description": "ユーザー「こば」からの追加質問。無料Noteのハイライト機能設置や、フィードへのコメント機能の使用方法についての疑問が記載されている。"
    },
    {
        "index": 1451,
        "filename": "image_04.png",
        "description": "Kくんからの詳細なアドバイス。ハイライトへのNote配置方法、istepを使ったコメント誘導、自動DM機能についての技術的な説明。"
    },
    {
        "index": 1452,
        "filename": "image_05.png",
        "description": "Kくんのアドバイス続き。無料Noteの活用方法と重要性、マッチングサイト攻略などの副業戦略、月150万円の売上を達成した例についての説明。"
    },
    {
        "index": 1453,
        "filename": "image_06.png",
        "description": "ユーザー「ゆーだい」からのInstagramアカウント相談。ギター講師として、ビジネススキル系の発信に関する質問と、複数アカウント戦略についての相談が含まれている。"
    },
    {
        "index": 1454,
        "filename": "image_07.png",
        "description": "Kくんからの返答。ギター講師向けコンサル提案、女性ターゲット向けのレッスン戦略、Youtubeとの連携によるコンテンツ販売についてのガイダンス。"
    },
    {
        "index": 1455,
        "filename": "image_08.png",
        "description": "はななさんの質問と関連する詳細。子育てジャンルでのInstagram参入戦略、STEAM教育関連のアカウント設計についての懸念と、複数ジャンル戦略についての相談が記載されている。"
    },
    {
        "index": 1456,
        "filename": "image_09.png",
        "description": "Kくんからのアドバイス。プログラミング教育とSTEAM教育の組み合わせ、子育て市場での競争戦略、コンテンツ販売とコンサル併用についての提案。"
    },
    {
        "index": 1457,
        "filename": "image_10.png",
        "description": "Kくんの続きのメッセージ。SEOブログ戦略とInstagram戦略の組み合わせ、マスクキー特化との組み合わせについての技術的な説明。"
    },
    {
        "index": 1458,
        "filename": "image_11.png",
        "description": "ユーザー「くまさん」からの初歩的な質問。アカウント作成3週間でフォロワー200、グルメアカウントの戦略についての基本的な相談内容。"
    },
    {
        "index": 1459,
        "filename": "image_12.png",
        "description": "Kくんからの詳細なコンサル返答。リポストの利用規約、写真引用時のコミュニティガイドライン遵守、広告配信時の費用と期間についての説明。"
    },
    {
        "index": 1460,
        "filename": "image_13.png",
        "description": "ユーザー「石井俊人」からの相談。営業会社採用とInstagram個人アカウント運用、リール動画内容の秘密性についての相談メッセージ。"
    },
    {
        "index": 1461,
        "filename": "image_14.png",
        "description": "Kくんからの返答とTikTok採用活動の紹介。企業の動画構成を真似る手法、TikTokでの就職活動についての提案が含まれている。"
    },
    {
        "index": 1462,
        "filename": "image_15.png",
        "description": "20代転職相談についてのDM会話。ショート動画での集客、オフ会やInstagram誘導、質問回答やブログ記事の活用についての質問スレッド。"
    },
    {
        "index": 1463,
        "filename": "image_16.png",
        "description": "コンサル依頼と業界選択についての相談。Kくんがコンサル対応中であることと、マネタイズポイントをブログにするか商品化するかについての相談が記載されている。"
    },
    {
        "index": 1464,
        "filename": "image_17.png",
        "description": "飲食店メニュー掲載戦略についてのDM。ユーザー「さもちん」がフィード投稿とメニュー紹介、女性向け低カロリーメニュー提案など、飲食業特化のInstagram戦略について相談している。"
    }
]

def update_inventory_with_descriptions(batch_descriptions):
    """image_inventory_progress.jsonを読み込み、説明を追加"""

    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'
    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {inventory[idx]['filename']}: 説明更新")

    total = len(inventory)

    # 自動生成でない詳細説明のカウント
    def is_auto_generated(desc):
        if not desc:
            return True
        auto_patterns = [
            "運用に関する説明画像または投稿サムネイル。記事",
            "運用に関する説明画像または図解。",
            "記事のバナー画像またはメインビジュアル。",
            "関連コンテンツ。"
        ]
        for pattern in auto_patterns:
            if pattern in desc:
                return True
        return False

    completed = sum(1 for item in inventory if not is_auto_generated(item.get('description', '')))

    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Batch 1445-1464 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
