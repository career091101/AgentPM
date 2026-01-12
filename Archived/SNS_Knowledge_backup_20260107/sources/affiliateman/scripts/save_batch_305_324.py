#!/usr/bin/env python3
"""
Batch 305-324の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
インデックス305-324の20枚を処理
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 305-324の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 305,
        "filename": "image_32.jpg",
        "description": "スーツを着た女性の横顔シルエット。黒髪で赤いネクタイを結んでいる、ビジネスシーンのアイコン。"
    },
    {
        "index": 306,
        "filename": "image_33.jpg",
        "description": "金髪で青いシャツを着た女性の顔のみのキャラクターイラスト。7月〜9月のインスタ質問回答まとめのナビゲーターキャラクター。"
    },
    {
        "index": 307,
        "filename": "image_34.png",
        "description": "「食べログ」の焼肉店検索ページ。全国の焼肉お店が832,629件、クチコミ46,697,014件との統計情報が表示されている。"
    },
    {
        "index": 308,
        "filename": "image_35.png",
        "description": "焼肉レストラン「俺のやきとり銀座9丁目」の詳細ページ。3.49星評価で468件のクチコミ、32734件の店舗ページ閲覧がある人気店の情報表示。"
    },
    {
        "index": 309,
        "filename": "image_36.jpg",
        "description": "金髪で青いシャツを着た女性キャラクターの顔イラスト。会話形式の説明用ナビゲーターキャラ。"
    },
    {
        "index": 310,
        "filename": "image_37.jpg",
        "description": "スーツを着た女性の横顔シルエット。黒髪で赤いネクタイを結んでいるビジネスウーマンアイコン。"
    },
    {
        "index": 311,
        "filename": "image_38.jpg",
        "description": "金髪で青いシャツを着た女性キャラクターの顔。説明用のナレーター役イラスト。"
    },
    {
        "index": 312,
        "filename": "image_39.png",
        "description": "顔をしかめている黄色い絵文字アイコン。不満足や戸惑いを表現するシンボル。"
    },
    {
        "index": 313,
        "filename": "image_40.jpg",
        "description": "スーツを着た女性の横顔シルエット。黒髪で赤いネクタイを結んでいる、ビジネスシーンのアイコン。"
    },
    {
        "index": 314,
        "filename": "image_41.jpg",
        "description": "金髪で青いシャツを着た女性キャラクターの顔イラスト。記事内の質問回答コンテンツの進行役。"
    },
    {
        "index": 315,
        "filename": "image_42.jpg",
        "description": "金髪で青いシャツを着た女性キャラクターのポートレートイラスト。インタビューや説明の進行役。"
    },
    {
        "index": 316,
        "filename": "image_43.jpg",
        "description": "スーツを着た女性の横顔シルエット。黒髪で赤いネクタイを結んでいるビジネスウーマンアイコン。"
    },
    {
        "index": 317,
        "filename": "image_44.jpg",
        "description": "金髪で青いシャツを着た女性キャラクターの顔。質問コーナーのナビゲーター役として使用。"
    },
    {
        "index": 318,
        "filename": "image_45.jpg",
        "description": "スーツを着た女性の横顔シルエット。黒髪で赤いネクタイを結んでいるキャラクターアイコン。"
    },
    {
        "index": 319,
        "filename": "image_46.jpg",
        "description": "金髪で青いシャツを着た女性キャラクターの顔イラスト。インスタグラムの質問回答コンテンツの語り部。"
    },
    {
        "index": 320,
        "filename": "image_47.jpg",
        "description": "スーツを着た女性の横顔シルエット。黒髪で赤いネクタイを結んでいるビジネスパーソンのアイコン。"
    },
    {
        "index": 321,
        "filename": "image_48.png",
        "description": "両手を上げている黄色い笑顔絵文字。満足や喜びを表現するシンボル。"
    },
    {
        "index": 322,
        "filename": "image_49.jpg",
        "description": "金髪で青いシャツを着た女性キャラクターの顔。ブログ記事内の説明・質問回答のナビゲーター。"
    },
    {
        "index": 323,
        "filename": "image_50.jpg",
        "description": "金髪で青いシャツを着た女性キャラクターの顔イラスト。記事内の会話形式コンテンツで使用。"
    },
    {
        "index": 324,
        "filename": "image_51.jpg",
        "description": "金髪で青いシャツを着た女性キャラクターの顔。インスタグラム運用に関する質問回答コーナーの案内人。"
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

    print(f"\n✓ Batch 305-324 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
