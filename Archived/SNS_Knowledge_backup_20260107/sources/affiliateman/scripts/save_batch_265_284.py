#!/usr/bin/env python3
"""
Batch 265-284の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 265-284の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 265,
        "filename": "image_23.png",
        "description": "コンサル商品と別コンサルを組み合わせるマネタイズ戦略を示す図解。カラフルなショッピングバッグと黄色いハンドバッグのイラストで、異なる商品カテゴリを表現している。"
    },
    {
        "index": 266,
        "filename": "image_24.png",
        "description": "ハゲ改善を求める顧客の心理プロセスを図で説明。「ハゲ改善したい」という表面的な悩みから、その理由（モテたいから）を探り、ハゲ改善商品を経由してモテコンサルという解決策へと導く流れを表示。"
    },
    {
        "index": 267,
        "filename": "image_25.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクターのイラスト。黒髪で落ち着いた表情。シャツはグレー、ネクタイは赤色。"
    },
    {
        "index": 268,
        "filename": "image_26.png",
        "description": "インスタグラム運用コンテンツの3つのマネタイズ方法を紹介するバナー。「インスタ不動産ジャンル」のタイトルで、不動産関連コンテンツの伸び方と収益線を解説している。記事「不動産ジャンルの稼ぎ方」関連のサムネイル。"
    },
    {
        "index": 269,
        "filename": "image_27.png",
        "description": "「2023年インスタ攻略：バズる投稿作成方法」というタイトルのバナー。全SNSで活用可能なテクニックを紹介する記事のサムネイル。挿絵に男性キャラクター。"
    },
    {
        "index": 270,
        "filename": "image_28.png",
        "description": "「2023年インスタ攻略：ブルーオシャン16選」というタイトルのバナー。今後伸びそうなおすすめジャンルを16個紹介する記事のサムネイル。青い波のイラスト付き。"
    },
    {
        "index": 271,
        "filename": "image_29.png",
        "description": "「インスタ子育てジャンル：上手なコンセプトアカウント例」というタイトルのバナー。子育て関連コンテンツのコンセプト設計について説明する記事の紹介画像。黄色い顔のキャラクター付き。"
    },
    {
        "index": 272,
        "filename": "image_30.png",
        "description": "「Instagramに関する質問回答まとめ【2022年7～9月分】」というタイトルのメインビジュアル。紫背景に白いバナーと複数の色付きクエスチョンマーク（？）のアイコン、考える男性キャラクター。"
    },
    {
        "index": 273,
        "filename": "image_01.png",
        "description": "金髪で青いシャツを着たアニメ風のキャラクター。質問回答コンテンツの解説役として使用されるキャラクターイラスト。"
    },
    {
        "index": 274,
        "filename": "image_02.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクター。グレーのジャケット、赤いネクタイ。黒髪でプロフェッショナルな表情。"
    },
    {
        "index": 275,
        "filename": "image_03.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクター。グレーのジャケット、赤いネクタイ。黒髪でプロフェッショナルな表情。"
    },
    {
        "index": 276,
        "filename": "image_04.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクター。グレーのジャケット、赤いネクタイ。黒髪でプロフェッショナルな表情。"
    },
    {
        "index": 277,
        "filename": "image_05.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクター。グレーのジャケット、赤いネクタイ。黒髪でプロフェッショナルな表情。"
    },
    {
        "index": 278,
        "filename": "image_06.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクター。グレーのジャケット、赤いネクタイ。黒髪でプロフェッショナルな表情。"
    },
    {
        "index": 279,
        "filename": "image_07.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクター。グレーのジャケット、赤いネクタイ。黒髪でプロフェッショナルな表情。"
    },
    {
        "index": 280,
        "filename": "image_08.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクター。グレーのジャケット、赤いネクタイ。黒髪でプロフェッショナルな表情。"
    },
    {
        "index": 281,
        "filename": "image_09.jpg",
        "description": "金髪で青いシャツを着たアニメ風のキャラクター。質問回答コンテンツの解説役として使用されるキャラクターイラスト。"
    },
    {
        "index": 282,
        "filename": "image_10.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクター。グレーのジャケット、赤いネクタイ。黒髪でプロフェッショナルな表情。"
    },
    {
        "index": 283,
        "filename": "image_10.jpg",
        "description": "ビジネス向けのスーツを着た女性キャラクター。グレーのジャケット、赤いネクタイ。黒髪でプロフェッショナルな表情。"
    },
    {
        "index": 284,
        "filename": "image_11.jpg",
        "description": "金髪で青いシャツを着たアニメ風のキャラクター。質問回答コンテンツの解説役として使用されるキャラクターイラスト。"
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

    print(f"\n✓ Batch 265-284 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
