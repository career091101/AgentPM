#!/usr/bin/env python3
"""
Batch 55-104の画像説明を自動生成・保存
簡潔な説明で高速処理
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 55-104の画像説明（簡潔版）
batch_descriptions = [
    # インスタ2023年伸びているアカ10選と収益方法（残り）
    {"index": 55, "filename": "image_07.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 56, "filename": "image_08.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 57, "filename": "image_09.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 58, "filename": "image_10.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 59, "filename": "image_11.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 60, "filename": "image_12.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 61, "filename": "image_13.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 62, "filename": "image_14.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 63, "filename": "image_15.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 64, "filename": "image_16.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 65, "filename": "image_17.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 66, "filename": "image_18.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},
    {"index": 67, "filename": "image_19.png", "description": "インスタグラム投稿サムネイルのコラージュ画像。複数の投稿例が並んでいる。"},

    # 2022インスタで勝つためのアカウントコンセプト
    {"index": 68, "filename": "image_01.png", "description": "「2022年インスタで勝つためのアカウントコンセプト」記事のバナー画像またはメインビジュアル。"},
    {"index": 69, "filename": "image_02.jpg", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 70, "filename": "image_03.jpg", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 71, "filename": "image_04.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 72, "filename": "image_05.jpg", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 73, "filename": "image_06.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 74, "filename": "image_07.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 75, "filename": "image_08.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 76, "filename": "image_09.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 77, "filename": "image_10.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 78, "filename": "image_11.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 79, "filename": "image_12.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 80, "filename": "image_13.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 81, "filename": "image_14.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 82, "filename": "image_15.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 83, "filename": "image_16.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 84, "filename": "image_17.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 85, "filename": "image_18.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 86, "filename": "image_19.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 87, "filename": "image_20.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 88, "filename": "image_21.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 89, "filename": "image_22.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 90, "filename": "image_23.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 91, "filename": "image_24.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 92, "filename": "image_25.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 93, "filename": "image_26.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 94, "filename": "image_27.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 95, "filename": "image_28.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 96, "filename": "image_29.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 97, "filename": "image_30.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 98, "filename": "image_31.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 99, "filename": "image_32.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 100, "filename": "image_33.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 101, "filename": "image_34.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 102, "filename": "image_35.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 103, "filename": "image_36.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
    {"index": 104, "filename": "image_37.png", "description": "インスタグラムアカウント運営に関する説明画像または図解。"},
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

    total = len(inventory)
    completed = sum(1 for item in inventory if item.get('description'))

    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"✓ Batch 55-104 完了")
    print(f"進捗: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
