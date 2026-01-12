#!/usr/bin/env python3
"""
Batch 1085-1104の画像説明を保存
実際に画像を読み込んで詳細な説明を生成（20枚）
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1085-1104の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1085,
        "filename": "image_51.png",
        "description": "Instagram DM質問機能の画面。ユーザー「くくん」への質問で、アカウントコンセプト、フォロワー数、マネタイズ方法について相談者から複数の質問が寄せられている。"
    },
    {
        "index": 1086,
        "filename": "image_52.png",
        "description": "ペット関連のインスタグラムアカウント紹介。「mugyu_official」というアカウントがペット情報を主に発信しており、アカウント方向性やマネタイズについてのアドバイス対象。"
    },
    {
        "index": 1087,
        "filename": "image_53.png",
        "description": "くくんの回答メッセージ。ペット関連アカウント運用に関するリール戦略、フォロワー増加方法、ペット商品紹介のアフィリエイト活用について詳しく説明している。"
    },
    {
        "index": 1088,
        "filename": "image_54.png",
        "description": "みかさからの質問回答。リール製作のコツ、フォロワー数別の施策、noteの販売戦略などについてくくんがアドバイスしている。"
    },
    {
        "index": 1089,
        "filename": "image_55.png",
        "description": "はやからの質問。インスタ広告の効果測定やアカウント攻略、マネタイズ方法についての3つの質問が掲載されている。"
    },
    {
        "index": 1090,
        "filename": "image_56.png",
        "description": "くくんの詳細な回答。インスタ広告の有効活用、フォロワー増加のための具体的なマネタイズ方法について、コンサルやnote、企業案件など複数の手段を提案。"
    },
    {
        "index": 1091,
        "filename": "image_57.png",
        "description": "はやとからの質問。インテリア・ホテルジャンルのインスタ運用についての相談で、現在の運用状況とマネタイズ戦略について説明している。"
    },
    {
        "index": 1092,
        "filename": "image_58.png",
        "description": "ホテルアカウントの説明画像。Instagram「hh.room」はホテルジャンルのインスタアカウントで、今後のマネタイズ方向性についてのアドバイスを求めている。"
    },
    {
        "index": 1093,
        "filename": "image_59.png",
        "description": "ユーザー「shoma」のInstagram インサイト画面。過去30日間に3,391件のアカウントにリーチした内訳を示す折れ線グラフが表示されている。"
    },
    {
        "index": 1094,
        "filename": "image_60.png",
        "description": "shomaへのくくんの回答。リールのエンゲージメント施策やアダルトジャンルでのストーリー・フィード活用に関するアドバイスを提供。"
    },
    {
        "index": 1095,
        "filename": "image_61.png",
        "description": "shomaのInstagram インサイト画面。過去30日間に3,660件のアカウントにリーチした詳細な統計グラフが表示されている。"
    },
    {
        "index": 1096,
        "filename": "image_62.png",
        "description": "ユーザー「shoto」からの質問。エロ系ワードの使用についてやマイメアリー、ハイプについてのコンテンツ戦略について相談している。"
    },
    {
        "index": 1097,
        "filename": "image_63.png",
        "description": "issei から「ガチで売上UP」についての質問。脱毛ガリガリコーチとしての事業でパーソナルトレーニング投稿について複数の悩みを相談。"
    },
    {
        "index": 1098,
        "filename": "image_64.png",
        "description": "くくんがissei に対する回答。見込み客の獲得方法や見込み顧客リストの増やし方、パーソナルトレーニングのマネタイズについて複数のアドバイスを提供。"
    },
    {
        "index": 1099,
        "filename": "image_65.png",
        "description": "くくんからissei への継続的なアドバイス。フォロワー数に応じたメンション営業戦略やオープンチャット活用について詳しく説明。"
    },
    {
        "index": 1100,
        "filename": "image_66.png",
        "description": "Slack共有のURL。くくんのSNS攻略ラジオ「Voicy」の共有で、『誰でも簡単にバズる投稿を作る3ステップ』というテーマの音声コンテンツ。"
    },
    {
        "index": 1101,
        "filename": "image_67.png",
        "description": "のあからの質問。アカウント設計やリール、フォロワー増加の具体的施策について4つの質問が掲載されている。"
    },
    {
        "index": 1102,
        "filename": "image_68.png",
        "description": "くくんの回答メッセージ。リールの重要性やフォロワー3000人までの施策、外部流入獲得方法についてのアドバイス。"
    },
    {
        "index": 1103,
        "filename": "image_69.png",
        "description": "tanakatenichiro からの質問。男性向けダイエットジャンルの新規アカウント開設・運用についての相談で、ジャンル選定の確認を求めている。"
    },
    {
        "index": 1104,
        "filename": "image_70.png",
        "description": "tanakatenichiro の詳細なプロフィール説明。男性向けダイエットジャンルの強み（フィジーク、栄養、マーケティング、メンタルヘルス）と補足情報を記載。"
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

    print(f"\n✓ Batch 1085-1104 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
