#!/usr/bin/env python3
"""
Batch 285-304の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 285-304の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 285,
        "filename": "image_12.jpg",
        "description": "黄色いセミロングの髪と青いトップスを着た女性キャラクターの顔アップイラスト。親しみやすい表情で、ブログ記事の解説用キャラクター。"
    },
    {
        "index": 286,
        "filename": "image_13.jpg",
        "description": "黄色いセミロングの髪と青いトップスを着た女性キャラクターの顔アップイラスト。親しみやすい表情で、ブログ記事の解説用キャラクター。"
    },
    {
        "index": 287,
        "filename": "image_14.png",
        "description": "子持ちママへの無料アンケートキャンペーン。ヘアドライヤーやシャープ空気清浄機など4製品と、アンケート回答で100円前後の報酬獲得機会を紹介。"
    },
    {
        "index": 288,
        "filename": "image_15.png",
        "description": "ダイエットボックスのマネタイズ事例。徒歩だけで海鮮が貰える仕組みを左右の図解で説明。ストーリー900件、定期訴求15件前後/回のスペック。"
    },
    {
        "index": 289,
        "filename": "image_16.jpg",
        "description": "スーツ姿でネクタイを締めた男性のビジネスパーソンを描いた横顔イラスト。サムネイル用の汎用性が高い人物イラスト。"
    },
    {
        "index": 290,
        "filename": "image_17.jpg",
        "description": "インスタグラムアカウント「well_official_」の分析。フォロワー19.5万人、投稿508件。夏までに痩せたい人向けの美容・ダイエット情報発信で、お金・サブスク・お部屋などマネタイズ施策を紹介。"
    },
    {
        "index": 291,
        "filename": "image_18.jpg",
        "description": "スーツ姿でネクタイを締めた男性のビジネスパーソンを描いた横顔イラスト。サムネイル用の汎用性が高い人物イラスト。"
    },
    {
        "index": 292,
        "filename": "image_19.jpg",
        "description": "スーツ姿でネクタイを締めた男性のビジネスパーソンを描いた横顔イラスト。サムネイル用の汎用性が高い人物イラスト。"
    },
    {
        "index": 293,
        "filename": "image_20.jpg",
        "description": "Instagram URL（https://Instagram.~）からTikTok、さらにInstagramへと誘導するフロー図。A、B、Cの3つのInstagramプロフィール候補から「インスタに行かないといけない理由を動画に」するメッセージフロー。"
    },
    {
        "index": 294,
        "filename": "image_21.jpg",
        "description": "黄色いセミロングの髪と青いトップスを着た女性キャラクターの顔アップイラスト。親しみやすい表情で、ブログ記事の解説用キャラクター。"
    },
    {
        "index": 295,
        "filename": "image_22.jpg",
        "description": "スーツ姿でネクタイを締めた男性のビジネスパーソンを描いた横顔イラスト。サムネイル用の汎用性が高い人物イラスト。"
    },
    {
        "index": 296,
        "filename": "image_23.jpg",
        "description": "黄色いセミロングの髪と青いトップスを着た女性キャラクターの顔アップイラスト。親しみやすい表情で、ブログ記事の解説用キャラクター。"
    },
    {
        "index": 297,
        "filename": "image_24.jpg",
        "description": "スーツ姿でネクタイを締めた男性のビジネスパーソンを描いた横顔イラスト。サムネイル用の汎用性が高い人物イラスト。"
    },
    {
        "index": 298,
        "filename": "image_25.jpg",
        "description": "黄色いセミロングの髪と青いトップスを着た女性キャラクターの顔アップイラスト。親しみやすい表情で、ブログ記事の解説用キャラクター。"
    },
    {
        "index": 299,
        "filename": "image_26.jpg",
        "description": "黄色いセミロングの髪と青いトップスを着た女性キャラクターの顔アップイラスト。親しみやすい表情で、ブログ記事の解説用キャラクター。"
    },
    {
        "index": 300,
        "filename": "image_27.jpg",
        "description": "黄色いセミロングの髪と青いトップスを着た女性キャラクターの顔アップイラスト。親しみやすい表情で、ブログ記事の解説用キャラクター。"
    },
    {
        "index": 301,
        "filename": "image_28.png",
        "description": "リンゴのキャラクター。赤い実のシンプルで可愛らしいイラスト。"
    },
    {
        "index": 302,
        "filename": "image_29.png",
        "description": "インスタグラムアカウント「keikun.simplelife」のプロフィール。フォロワー19.5万人、投稿508件。男女向けシンプルライフの個人ブログで、1LDK・ダイエット・お金アカウント・サブスクなどマネタイズ施策を複数展開。"
    },
    {
        "index": 303,
        "filename": "image_30.jpg",
        "description": "スーツ姿でネクタイを締めた男性のビジネスパーソンを描いた横顔イラスト。サムネイル用の汎用性が高い人物イラスト。"
    },
    {
        "index": 304,
        "filename": "image_31.jpg",
        "description": "黄色いセミロングの髪と青いトップスを着た女性キャラクターの顔アップイラスト。親しみやすい表情で、ブログ記事の解説用キャラクター。"
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

    print(f"\n✓ Batch 285-304 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
