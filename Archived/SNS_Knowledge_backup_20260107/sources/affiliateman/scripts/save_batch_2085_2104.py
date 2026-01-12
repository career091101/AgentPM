#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2085, "filename": "image_10.png", "description": "Twitterの投稿例で、インスタ不動産ジャンルでの稼ぎ方無料公開を告知するキャプチャと、ブログURL掲載による有料商品販売フロー図解。"},
    {"index": 2086, "filename": "image_11.png", "description": "フォロリツ企画から無料記事プレゼント、有料コンサルへの導線を示すフロー図。"},
    {"index": 2087, "filename": "image_12.jpg", "description": "スーツを着たビジネス女性の上半身イラスト。"},
    {"index": 2088, "filename": "image_13.jpg", "description": "スーツを着たビジネス女性の上半身イラスト。"},
    {"index": 2089, "filename": "image_14.png", "description": "SNSのマネタイズ事例として、DMで商品を売る施策例を説明するバナー画像。"},
    {"index": 2090, "filename": "image_15.png", "description": "1日で4000人フォロワー増加を実現した実例を紹介するTwitterバズ戦略完全版の告知タイトル画像。"},
    {"index": 2091, "filename": "image_16.png", "description": "2023年Twitter攻略・フォロワー伸ばし方を説明するサムネイルで、1万人フォロワー目指そうというテキスト付き。"},
    {"index": 2092, "filename": "image_17.png", "description": "Twitter0→1攻略・フォロワーUP成功事例とアカ初期の最強施策を説明するサムネイル画像。"},
    {"index": 2093, "filename": "image_18.png", "description": "Twitterの恋愛ジャンルで変わった稼げるアフィ案件について説明するサムネイル。"},
    {"index": 2094, "filename": "image_19.png", "description": "Twitterの恋愛ジャンルで変わった稼げるアフィ案件についてのおすすめASP・まとめを紹介するサムネイル。"},
    {"index": 2095, "filename": "image_01.png", "description": "1日でフォロワー4000人増加したTwitterバズ戦略の完全版告知タイトル画像。"},
    {"index": 2096, "filename": "image_02.jpg", "description": "スーツを着たビジネス女性の上半身イラスト。"},
    {"index": 2097, "filename": "image_03.png", "description": "ChatGPTを使うインスタアカウント実例で、月15-20万の収益化を目指す仕組みと別アカ存在を説明するスクリーンショット。"},
    {"index": 2098, "filename": "image_04.jpg", "description": "スーツを着たビジネス女性の上半身イラスト。"},
    {"index": 2099, "filename": "image_05.png", "description": "複数SNS（インスタ、Twitter、LINE）とツールを組み合わせたアカウント導線で、LINE友達3000人獲得を目指す仕組みを図解。"},
    {"index": 2100, "filename": "image_06.png", "description": "SNSの恐ろしい事実として、Instagram・Twitterで投稿しても20%未満のフォロワーしかリーチできない一方、LINEは100%のメッセージ開封が見込める比較図解。"},
    {"index": 2101, "filename": "image_07.png", "description": "告知メッセージ配信をフォロ・リツ企画、note告知、バズ投稿を通じてLINE友達に配信し、imp数増加につなげるフロー図。"},
    {"index": 2102, "filename": "image_08.png", "description": "アカバンされた時のリカバリー対策として、新規アカフォロー促進とLINE友達戻す方法により、バンされてもフォロワー戻りやすくする仕組みを説明する図解。"},
    {"index": 2103, "filename": "image_09.png", "description": "商品を売りまくるマネタイズ戦略「Twitter稼ぐ戦略」で少ないフォロワーで月100万稼げるケースと、サロン限定動画でコンサル受講者を紹介するプロモーション画像。"},
    {"index": 2104, "filename": "image_10.png", "description": "フォロワー増加の10施策として、外部誘導によるフォロワー爆伸びをインスタ・Twitterの成功事例を交えて紹介するサムネイル。"},
]

def is_auto_generated(desc):
    patterns = [
        "インスタグラム運用に関する",
        "説明画像または投稿サムネイル",
        "運用に関する説明画像",
        "投稿用のサムネイル",
    ]
    return any(p in desc for p in patterns)

def update_inventory_with_descriptions(batch_descriptions):
    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'

    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {desc['filename']}: 説明更新")

    completed = sum(1 for item in inventory if not is_auto_generated(item.get('description', '')))
    total = len(inventory)
    remaining = total - completed
    percentage = (completed / total) * 100

    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Batch 2085-2104 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
