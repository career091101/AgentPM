#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2039, "filename": "image_02.png", "description": "ノートパソコンの画面にロケットが発射するイラスト。緑色の背景に赤と白のロケット、青空と白い雲が描かれており、スタートアップやコンテンツ配信の成功を象徴している。"},
    {"index": 2040, "filename": "image_03.jpg", "description": "濃紺色のスーツを着た黒髪の女性の横顔シルエット。シンプルなミニマルデザインで、プロフェッショナルで凛々しい表情を表現している。"},
    {"index": 2041, "filename": "image_04.png", "description": "TikTokのバイラルコンテンツ事例3つを並べた画像。卵を割る動画、バズる髪ケア製品、カラフルなASMR動画など、実際の高エンゲージメント投稿のスクリーンショット。"},
    {"index": 2042, "filename": "image_05.png", "description": "コスメ商品の紹介画像2点を掲載。左に熱中症対策のリップクリーム、右にハチミツのような黄色いジャムの商品写真で、バズるコンテンツの商品選定例を示している。"},
    {"index": 2043, "filename": "image_06.png", "description": "「2023年TikTok攻略 / フォロワー伸ばし方」というバナーテキスト。TikTokロゴと1万人フォロワー達成を目指すタイトル、キャラクターイラスト付きの記事バナー画像。"},
    {"index": 2044, "filename": "image_07.png", "description": "「2023年TikTok攻略 / 稼げるおすすめジャンル」というバナーテキスト。TikTokロゴとジャンル選定の重要性を示すタイトル、金のコイン、キャラクターイラスト付きの記事バナー画像。"},
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

    print(f"\n✓ Batch 2039-2044 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
