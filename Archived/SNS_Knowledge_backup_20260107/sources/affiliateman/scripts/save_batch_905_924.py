#!/usr/bin/env python3
"""
Batch 905-924の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
【2023年2月】質疑応答のまとめ + 【2023年3月】質疑応答のまとめ
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 905-924の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 905,
        "filename": "image_81.png",
        "description": "インスタグラム運用コンサルのKくんによる、副業・日常の仕事術と稼ぐジャンル選びについてのコメント返信。ニッチなジャンルもみんないになってしまった悩みへのアドバイスを紹介。"
    },
    {
        "index": 906,
        "filename": "image_82.png",
        "description": "みいさんからのリール・動画ストック戦略についての詳しい質問と、Kくんによるレストラン・ホテル・デートスポット発信についてのアドバイスコメント。"
    },
    {
        "index": 907,
        "filename": "image_83.png",
        "description": "Tanaさんからのアカウント方向性とマネタイズについての相談。お金関する技術を多めにしたほうがいいか、海外住まいで海外移住関連情報についての質問内容を記載。"
    },
    {
        "index": 908,
        "filename": "image_84.png",
        "description": "Kくんによる@Tanaへのマネタイズ戦略アドバイス。お金系のアフィが多いほか、海外移住系アフィ、個別コンサルなどの収益化方法を詳しく解説。"
    },
    {
        "index": 909,
        "filename": "image_85.png",
        "description": "まさとさんからのアカウント活用事例。現在おかけ系のアカウント運用で、認知・お出かけ旅系のマネタイズ方法についての詳しい質問。"
    },
    {
        "index": 910,
        "filename": "image_86.png",
        "description": "YouTubeとSNS攻略限定による神奈川グルメアカウントの事例動画。PRだけで月100万稼ぐ方法についてのKくんのコメント含むYouTubeサムネイル画像。"
    },
    {
        "index": 911,
        "filename": "image_87.png",
        "description": "おゆきさんからの複雑な悩み相談。恋愛選択や風水、プロ感とキャラが出づらくなったアカウント運用についての複数の質問を記載。"
    },
    {
        "index": 912,
        "filename": "image_88.png",
        "description": "Kくんによるおゆきさんへの細かいアドバイス返信。プロ感は圧倒的な知識量が大事、ビジュアル分析、キャラ構築など複数のジャンル別運用方法を解説。"
    },
    {
        "index": 913,
        "filename": "image_89.png",
        "description": "しずかさんからのNailS（ネイルズ）アカウント運用事例。ネイルデザイン発信のターゲット、フォロワー数とリーチ改善についての詳しい質問内容。"
    },
    {
        "index": 914,
        "filename": "image_90.png",
        "description": "Kくんによるしずかさんへのアカウント改善アドバイス。フォロワー2000人以上達成のためのリーチ改善、初動フェーズでの結局法を詳しく記載。"
    },
    {
        "index": 915,
        "filename": "image_91.png",
        "description": "しずかさんとKくんのキュレーションやリール編成についての質疑応答。画像素材がない場合の動画作成方法についてのアドバイス交換。"
    },
    {
        "index": 916,
        "filename": "image_92.png",
        "description": "Kくんによるキュレーション動画とTikTok運用の詳しいアドバイス。ネイルショート動画の細かい工夫と高級感の出し方についての具体例を記載。"
    },
    {
        "index": 917,
        "filename": "image_93.png",
        "description": "しずかさんからのキュレーションリール運用についての詳しい相談。TikTokのキュレーション法やInstagramリール編成との違いについての質問。"
    },
    {
        "index": 918,
        "filename": "image_94.png",
        "description": "Kくんによる詳しいTikTok運用と2020年代のインスタイメージについてのアドバイス。2023年以降の100万投稿の事例紹介と戦略指南。"
    },
    {
        "index": 919,
        "filename": "image_95.png",
        "description": "しずかさんとKくんによるTikTokのキュレーションアカウント運用とインスタ同様のルールについての質疑応答。ベンチマークについての追加質問。"
    },
    {
        "index": 920,
        "filename": "image_96.png",
        "description": "茶トラ兄弟さんからのペット系アカウント運用相談。女性タレント系アカウントの戦略と男性ファンを狙う場合の写真構成についての質問。"
    },
    {
        "index": 921,
        "filename": "image_97.png",
        "description": "Kくんによる茶トラ兄弟さんへの女性タレント系アカウント戦略アドバイス。ビジュアル系とアイドル系の違い、難しい場合の高度な文字入れスタイル提案。"
    },
    {
        "index": 922,
        "filename": "image_98.png",
        "description": "こはく転職と仕事術さんからのハイライト無料プレゼント配布戦略についての質問。フォロー→DM→テンプレート100選配布→感想特典といった具体的なファネル戦略。"
    },
    {
        "index": 923,
        "filename": "image_205.png",
        "description": "ひなたさんからの無料サービスのマネタイズについての質問と複数のKくんからのアドバイス返信。必要素材の提供、フォロー200人程度での公式ライン誘導戦略。"
    },
    {
        "index": 924,
        "filename": "image_99.png",
        "description": "こはく転職と仕事術さんへのKくんからのアドバイス返信。転職希望者向けのハイライト施策、SNS内での閲覧と投稿パターンについての詳細解説。"
    },
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

    print(f"\n✓ Batch 905-924 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
