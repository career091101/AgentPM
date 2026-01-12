#!/usr/bin/env python3
"""
Batch 325-344の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 325-344の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 325,
        "filename": "image_52.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 326,
        "filename": "image_53.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 327,
        "filename": "image_54.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 328,
        "filename": "image_55.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 329,
        "filename": "image_56.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 330,
        "filename": "image_57.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 331,
        "filename": "image_58.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 332,
        "filename": "image_59.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 333,
        "filename": "image_60.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 334,
        "filename": "image_61.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 335,
        "filename": "image_62.png",
        "description": "黒髪のビジネスウーマンキャラクターのプロフィール画像。紺色のスーツと赤いネクタイを着用した横顔のイラストで、専門性・信頼性を表現するデザイン。"
    },
    {
        "index": 336,
        "filename": "image_63.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 337,
        "filename": "image_64.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 338,
        "filename": "image_65.jpg",
        "description": "金髪のロングウェーブヘアに濃い青色のトップスを着た女性キャラクターのイラスト。スマートで知的な表情の漫画風のキャラで、affiliateman記事の挿絵として使用。"
    },
    {
        "index": 339,
        "filename": "image_66.jpg",
        "description": "白背景に複数の「？」「？」「？」のカラフルなアイコンが配置されたイメージ。Twitter/TikTokに関する質問回答まとめの見出し画像。"
    },
    {
        "index": 340,
        "filename": "image_67.jpg",
        "description": "白背景に複数の「？」「？」「？」のカラフルなアイコンが配置されたイメージ。Instagram/Twitter/TikTokに関する質問回答まとめの見出し画像。"
    },
    {
        "index": 341,
        "filename": "image_68.png",
        "description": "紫のラッパーに白地のタイトル「SNSの有益情報公開 SNS運用 役立つ情報【2022年7～9月分】」とチェックマーク付きのキャラクター。SNS運用情報の記事バナー画像。"
    },
    {
        "index": 342,
        "filename": "image_69.png",
        "description": "青いラッパーに白地のタイトル「SNS攻略サロン限定 11月の質疑回答まとめ インスタ/TIKTOK/Twitter」とロケットアイコン、キャラクターを配置した記事見出し。"
    },
    {
        "index": 343,
        "filename": "image_70.png",
        "description": "白背景の「？」「？」「？」のカラフルなアイコン。複数のSNS プラットフォームに関する質問・回答コンテンツの見出し画像。"
    },
    {
        "index": 344,
        "filename": "image_71.png",
        "description": "カラフルな「？」マーク（黄、赤、青、緑など）が複数配置された見出しデザイン。SNS関連の質疑応答・コンテンツの前置き画像として使用。"
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

    print(f"\n✓ Batch 325-344 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
