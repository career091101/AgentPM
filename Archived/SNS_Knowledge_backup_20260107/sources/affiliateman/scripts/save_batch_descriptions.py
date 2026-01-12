#!/usr/bin/env python3
"""
画像説明をバッチで保存するスクリプト
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 0-14の画像説明
batch_0_descriptions = [
    {
        "index": 0,
        "filename": "image_01.png",
        "description": "「2023年最新インスタグラム 伸びてるアカ1200選」のバナー画像。伸びてるアカ厳選、収益動線も解説、稼げるジャンル理解という3つの特徴が記載されている。"
    },
    {
        "index": 1,
        "filename": "image_02.png",
        "description": "インスタグラムアカウントの詳細スプレッドシート。アカウント名、フォロワー数、URLなどが一覧表示されている。"
    },
    {
        "index": 2,
        "filename": "image_03.jpg",
        "description": "スーツを着た男性の横顔を描いたシンプルなイラスト。"
    },
    {
        "index": 3,
        "filename": "image_04.png",
        "description": "Twitterの感想リツイートの方法を示す図解。「#けいサロン」ハッシュタグを使い、100文字以上の感想をツイートする仕組みを説明している。"
    },
    {
        "index": 4,
        "filename": "image_05.png",
        "description": "公式LINEとTwitter・Instagramの連携方法を示す図解。いいね/リツイートのスクショをLINEで送る、インスタとメッセージを送る仕組みを説明している。"
    },
    {
        "index": 5,
        "filename": "image_10.png",
        "description": "「SNS攻略サロン限定 12月のKくんのアウトプット」というバナー画像。インスタ/TIKTOK/Twitterの3つのプラットフォームが対象。"
    },
    {
        "index": 6,
        "filename": "image_01.png",
        "description": "「2023年インスタ攻略 バズる投稿作成方法」の紫色のバナー画像。全SNSで活用可のテクニックを紹介する内容。"
    },
    {
        "index": 7,
        "filename": "image_02.png",
        "description": "インスタグラムの成長フローを示す図解。コンテンツ投稿→フォロワーエンゲージ高い→新規層にリーチ→さらに新規層にリーチという4段階の循環を説明している。"
    },
    {
        "index": 8,
        "filename": "image_03.png",
        "description": "「バズるコンテンツってどうやって作るの？」という赤い背景のテキスト画像。"
    },
    {
        "index": 9,
        "filename": "image_04.png",
        "description": "YouTube、Instagram、TikTokのロゴとロケットのイラスト。SNSプラットフォームの成長を象徴する画像。"
    },
    {
        "index": 10,
        "filename": "image_05.png",
        "description": "雑学をテーマにした3つの投稿例のサムネイル画像。LINE、ドラえもん、有名人をテーマにしたコンテンツ例を示している。"
    },
    {
        "index": 11,
        "filename": "image_06.png",
        "description": "「よくあるコンテンツ作成時の勘違い」というタイトルで、専門的な内容を発信する、多くの人が分からない言葉を使う、内容が特定の層にしか受けない、という3つの間違いをリストアップした図解。"
    },
    {
        "index": 12,
        "filename": "image_07.png",
        "description": "ジブリアニメのキャラクターを使った「ジブリで学ぶ」シリーズの3つの投稿例サムネイル。アニメを活用した学習コンテンツの例。"
    },
    {
        "index": 13,
        "filename": "image_08.png",
        "description": "デジタルコンテンツ制作を示す3つのイラスト。タブレットやパソコンでコンテンツを作成する人物が描かれている。"
    },
    {
        "index": 14,
        "filename": "image_09.png",
        "description": "インスタグラムのインサイト画面のスクリーンショット。いいね5,829、コメント25、リーチしたアカウント数857,227などのエンゲージメント統計が表示されている。"
    }
]

def update_inventory_with_descriptions(batch_descriptions):
    """image_inventory.jsonを読み込み、説明を追加"""

    # 既存のinventoryを読み込み
    inventory_file = OUTPUT_DIR / 'image_inventory.json'
    with open(inventory_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    # 説明を追加
    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {inventory[idx]['filename']}: 説明追加")

    # 進捗状況を表示
    total = len(inventory)
    completed = sum(1 for item in inventory if item.get('description'))
    remaining = total - completed

    print(f"\n進捗: {completed}/{total} 完了 (残り{remaining}件)")
    print(f"完了率: {completed/total*100:.1f}%")

    # 一時ファイルに保存（バックアップ）
    temp_file = OUTPUT_DIR / 'image_inventory_progress.json'
    with open(temp_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 進捗保存: {temp_file.name}")

    return inventory

if __name__ == "__main__":
    inventory = update_inventory_with_descriptions(batch_0_descriptions)
