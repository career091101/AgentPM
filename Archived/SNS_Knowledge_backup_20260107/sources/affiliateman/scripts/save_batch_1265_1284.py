#!/usr/bin/env python3
"""
Batch 1265-1284の画像説明を保存
【2023年5月】質疑応答のまとめ（20枚）
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1265-1284の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1265,
        "filename": "image_85.png",
        "description": "インスタグラムのDM質問機能で受けた複数の質問。「初心者向けのビジネス系Twitter運用」についての質問が多く、ブロフィ統一や有益ツイートの工数、フォロワーへのリプ活動など具体的なアドバイス求める内容。"
    },
    {
        "index": 1266,
        "filename": "image_86.png",
        "description": "新規アカウント立ち上げのマネタイズについての質問。「行動経済学（心理学・経済学）×ビジネス」という発信コンセプトで、Twitterマーケティングと行動経済学を組み合わせた戦略について相談。"
    },
    {
        "index": 1267,
        "filename": "image_87.png",
        "description": "K くんからの回答で、「行動経済学」の基本概念とSNS運用への活用方法を説明。ビジネス系での初心者向けアプローチと、SNSの本質の違いを解説した長文返信。"
    },
    {
        "index": 1268,
        "filename": "image_88.png",
        "description": "「行動経済学」と「SNS攻略」についてK くんが詳しく解説。「仕事×SNSで使える心理学」としてレベルからスタートすることの重要性を指摘。"
    },
    {
        "index": 1269,
        "filename": "image_89.png",
        "description": "初心者が月100万円稼ぐマネタイズについての質問。フォロワーの目安（1000人以上）と稼ぎ方について、K くんが複数の実例やマネタイズ手法を紹介。"
    },
    {
        "index": 1270,
        "filename": "image_90.png",
        "description": "フォロワー数とマネタイズの関係についての回答。「Twitterとインスタで違う向性」「SNS▼ブログで100万円達成」という具体的な数字を示した説明。"
    },
    {
        "index": 1271,
        "filename": "image_91.png",
        "description": "SNS運用でのジャンル選択とマネタイズ戦略の相談。恋愛ジャンルと食べ物ジャンルのマネタイズしやすさを比較する質問に対する回答。"
    },
    {
        "index": 1272,
        "filename": "image_92.png",
        "description": "ブログ・SNS・マネタイズについてのメンション活用法に関する相談。「画像」「マーケティング」「コンテンツ販売」の軸の広げ方を提案する長文回答。"
    },
    {
        "index": 1273,
        "filename": "image_93.png",
        "description": "女性向けの恋愛コンセプトアカウント作成についての質問。note販売やメインでのマネタイズ方法、ファン化戦略についての複数の相談。"
    },
    {
        "index": 1274,
        "filename": "image_94.png",
        "description": "Webデザイナーとしてのターゲット設定やTwitter活用相談。「デザインスクール」「サロン」などのマネタイズ施策についてK くんがアドバイス。"
    },
    {
        "index": 1275,
        "filename": "image_95.png",
        "description": "新規アカウント立ち上げでのアドバイス求め。デザイナー界隈のブランディング戦略や初心者が避けるべき施策について相談。"
    },
    {
        "index": 1276,
        "filename": "image_96.png",
        "description": "TikTok での別媒体展開についての相談。1000人フォロワーを超えたタイミングで、TikTok→別媒体への導線作り（教育・信頼→有料販売）を検討する質問。"
    },
    {
        "index": 1277,
        "filename": "image_97.png",
        "description": "TikTok での20代後半〜30代男性ターゲット設定と、恋愛系ジャンルのマネタイズについての相談。オープンチャット「SNSマガジン」の紹介も含む。"
    },
    {
        "index": 1278,
        "filename": "image_98.png",
        "description": "オープンチャット活用についての詳しい説明。サプリーム機能やZOOMでの相談、グループセミナーなどのマネタイズ方法を紹介する回答。"
    },
    {
        "index": 1279,
        "filename": "image_99.png",
        "description": "ヨガのアカウント運用についてのアドバイス。ヨガ講座やオンライン教室のマネタイズ、TikTok でのリーチ戦略についての相談への回答。"
    },
    {
        "index": 1280,
        "filename": "image_100.png",
        "description": "ヨガ講座アフィリエイトについての複合的な質問。100日後のコンセプト設定や、オンライン講座、YouTube での動画化戦略について提案。"
    },
    {
        "index": 1281,
        "filename": "image_101.png",
        "description": "不動産とTikTok 、Instagram 運用についての相談。TikTok での新規アカウント開設時の適切なフィード設定についての具体的なアドバイス。"
    },
    {
        "index": 1282,
        "filename": "image_102.png",
        "description": "TikTok でのジャンル選択とマネタイズについての相談。恋愛系と食べ物系のマネタイズしやすさの比較、アドバイス求める質問。"
    },
    {
        "index": 1283,
        "filename": "image_103.png",
        "description": "店舗SNS運用のマネタイズについての質問。リラクゼーション・エステ店舗での Instagram 、Twitter 、TikTok の活用戦略について相談。"
    },
    {
        "index": 1284,
        "filename": "image_104.png",
        "description": "店舗SNS運用でのマネタイズ施策についての詳細な回答。商品販売、クーポン配布、リピーター育成など複数のアプローチを説明。"
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

    print(f"\n✓ Batch 1265-1284 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
