#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 324, "filename": "image_51.jpg", "description": "金髪でかわいらしい表情の女性キャラクターのイラスト。インスタグラム運用に関する質問回答コンテンツの案内人として登場。"},
    {"index": 1566, "filename": "image_16.png", "description": "インスタグラムのDM会話スクリーンショット。女性向け恋愛系アカウント運用における初期フォロー戦略と投稿頻度についての相談と回答が記載されている。"},
    {"index": 1625, "filename": "image_75.png", "description": "インスタグラムのDM会話スクリーンショット。新規アカウント開設時のフォロワー獲得方法やいいね活動戦略についての質問と詳細な回答が記載されている。"},
    {"index": 2025, "filename": "image_12.png", "description": "「SNS運用 超役立つ情報」というテーマの2022年10月分まとめコンテンツのヘッダーバナー。紫色のデザインとキャラクターイラストが配置されている。"},
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

    print(f"\n✓ 単発画像 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

    if remaining == 0:
        print("\n🎉🎉🎉 全2,172枚の画像説明が完了しました！ 🎉🎉🎉")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
