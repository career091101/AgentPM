#!/usr/bin/env python3
"""
Batch 525-544の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 525-544の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 525,
        "filename": "image_157.png",
        "description": "K くんのDMコメント。後発者ながら背骨がわかんですねと質問し、メンバーの競がりとぶるつ雑談で募集中という内容。"
    },
    {
        "index": 526,
        "filename": "image_158.png",
        "description": "るるのコメント。@Kくんにお世話になっており、アカウント（主に削除）をやっており記事を見てみたいという投稿内容の引き継ぎ。"
    },
    {
        "index": 527,
        "filename": "image_159.png",
        "description": "ほみこのコメント。韓国旅行で暮らしアカウントを運用しており、マネタイズに悩んでいるアフィリエイト戦略についての質問コメント。"
    },
    {
        "index": 528,
        "filename": "image_160.png",
        "description": "K くんの回答。韓国観光ツアー、ポケットWi-Fi、ホテル、食事などのアフィリエイトサービスについての提案や、オンラインサロン説明。"
    },
    {
        "index": 529,
        "filename": "image_161.png",
        "description": "おやつラボのコメント。お菓子のレシピをInstagramで配信しており、マネタイズ方法についての質問。月100万円達成の相談。"
    },
    {
        "index": 530,
        "filename": "image_162.png",
        "description": "K くんの回答。楽天アフィリの訴求とダイエット系アカウントの補足についての説明、月100円達成の具体的なマネタイズ方法。"
    },
    {
        "index": 531,
        "filename": "image_163.png",
        "description": "くろの有料noteの販売方法についての質問。アカウント立ち上げから販売までの2通りの流れについてのアドバイス。"
    },
    {
        "index": 532,
        "filename": "image_164.png",
        "description": "ちはるのコメント。インスタ美容アフィリエイトについての質問で、フォロワー300人規模の美容関連コンテンツ活動の相談。"
    },
    {
        "index": 533,
        "filename": "image_165.png",
        "description": "ちはるの詳細なコメント。市場が大きいコスメのほうが稼げるためインスタで伸びているアカウント例の紹介と、ビジネスジャンルの相談。"
    },
    {
        "index": 534,
        "filename": "image_166.png",
        "description": "ちはるのコメント。Twitter×インスタの両方についての相談で、マネタイズの提案とツイッターの競争について質問。"
    },
    {
        "index": 535,
        "filename": "image_167.png",
        "description": "りょうのインスタダイエットアカウントについての質問。無料noteと有料noteの販売方法や、ダイエットnoteコンテンツについての相談。"
    },
    {
        "index": 536,
        "filename": "image_168.png",
        "description": "おやつラボのマナラクレンジングについての相談。無料サンプル、ディライン付与、温感クレンジングについての実装方法。"
    },
    {
        "index": 537,
        "filename": "image_169.png",
        "description": "りょうのTwitterアフィリエイトについての質問。無noteから有noteの流れやダイエット系noteについての具体的なマネタイズ相談。"
    },
    {
        "index": 538,
        "filename": "image_170.png",
        "description": "うにせのセフレ作成マネタイズについての質問。Twitterの恋愛アカウント運用で、マッチングアプリ活用の相談。"
    },
    {
        "index": 539,
        "filename": "image_171.png",
        "description": "うにせの返答コメント。セフレ作成の女性獲得方法やマッチングアプリの活用について、マネタイズ方法の提案内容。"
    },
    {
        "index": 540,
        "filename": "image_172.png",
        "description": "うにせの追加回答。セフレに関する女性獲得ツール活用や実現方法、マッチングアプリのスクリーニング方法についての説明。"
    },
    {
        "index": 541,
        "filename": "image_173.png",
        "description": "村上空のTwitterマネタイズについての質問。自己啓発発信で自己肯定感を上げるジャンルについてのマネタイズ相談。"
    },
    {
        "index": 542,
        "filename": "image_174.png",
        "description": "yuimaruのInstagram集客マネタイズについての質問。SNS経営会社との関係でインスタ集客についての相談と進み方への回答。"
    },
    {
        "index": 543,
        "filename": "image_176.png",
        "description": "K くんのアウトプット・SNS攻略に役立つ知識というタイトルの2022年11月号まとめバナー。赤い矢印と笑顔のキャラクター。"
    },
    {
        "index": 544,
        "filename": "image_178.png",
        "description": "SNS攻略サロン限定・12月のK くんのアウトプットについてのバナー。インスタ/TIKTOK/Twitterのキャラクター付きデザイン。"
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

    print(f"\n✓ Batch 525-544 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
