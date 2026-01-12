#!/usr/bin/env python3
"""
Batch 825-844の画像説明を保存
2023年3月質疑応答のまとめ記事（20枚）
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 825-844の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 825,
        "filename": "image_01.png",
        "description": "Instagramのコメント欄で、ユーザー「miho」がKくんへの質問に回答。ダイエットアカウント運用中で、毎日の投稿とリールを試行錯誤しながら投稿していることを説明している。"
    },
    {
        "index": 826,
        "filename": "image_02.png",
        "description": "Instagramコメント。Kくんがダイエットコンサルの月額料金やサロン運用についての質問に回答。ダイエットの稼ぎ方やブログ・SNS活用についての具体的なアドバイスを記載。"
    },
    {
        "index": 827,
        "filename": "image_03.png",
        "description": "Instagramコメント。ユーザー「サキ」が初心者として「30代子育てママ×田舎」というジャンルでマネタイズを目指していることを説明。インスタグラムのネタについてのアドバイスを受けている。"
    },
    {
        "index": 828,
        "filename": "image_04.png",
        "description": "Instagramコメント。Kくんがサキの質問に対して、ジャンルと発信内容のアフィ内容を変えられるかについて回答し、30代ママ向けのコンテンツ提案についてアドバイスしている。"
    },
    {
        "index": 829,
        "filename": "image_05.png",
        "description": "Instagramコメント。ユーザー「小麦粉」がインスタ運用初心者で、脱毛特化アカウントと30代OL向けアカウントの2つの方向性について質問。Kくんからアドバイスを受けている。"
    },
    {
        "index": 830,
        "filename": "image_06.png",
        "description": "Instagramコメント。Kくんが脱毛特化の難しさについて説明し、脱毛アカウント選定よりも、他の特性の方が取りやすいことを示唆している。"
    },
    {
        "index": 831,
        "filename": "image_07.png",
        "description": "Instagramコメント。小麦粉がメインアカウント運用についての質問を続け、Kくんがislandagramのリンクを含む説明やメインアカウント戦略についてのアドバイスを提供。"
    },
    {
        "index": 832,
        "filename": "image_08.png",
        "description": "Instagramコメント。吉田がKくんへ、月200万円稼ぐマネタイズ方法の詳細について質問。複数のマネタイズ方法や美容系クリニック紹介についての具体的な質問が記載。"
    },
    {
        "index": 833,
        "filename": "image_09.png",
        "description": "Instagramコメント。Kくんが吉田の質問に詳細に回答。Twitter普及での整形マネタイズやクリニック紹介での実績、ツイッター月限の美容アカウント運用についての説明。"
    },
    {
        "index": 834,
        "filename": "image_10.png",
        "description": "Instagramコメント。吉田の続きの質問。整形のクリニック紹介と直接提携による金銭リスクや報酬パターンについての詳細な質問が記載。"
    },
    {
        "index": 835,
        "filename": "image_11.png",
        "description": "Instagramコメント。ユーザー「しんたろう」がKくんへ、恋愛ジャンルでの発信について質問。目標やマネタイズについてのアドバイスを求めている。"
    },
    {
        "index": 836,
        "filename": "image_12.png",
        "description": "Instagramコメント。Kくんがしんたろうのアカウント提案についてアドバイス。恋愛系コンサルやマネタイズ方法、Twitter連携や異なるプラットフォーム戦略についての提案。"
    },
    {
        "index": 837,
        "filename": "image_13.png",
        "description": "Instagramコメント。ユーザー「s.nakaha」がKくんへ、韓国美容系アカウント運用での悩みを相談。フォロワー3万人での保存率の低さとフォロワー増加スピードについての質問。"
    },
    {
        "index": 838,
        "filename": "image_14.png",
        "description": "Instagramコメント。Kくんがs.nakahaの相談に対して、フォロワー増加のためのステップやDM戦略についてのアドバイスを提供。iステップの活用や関連マーケティング手法について説明。"
    },
    {
        "index": 839,
        "filename": "image_15.png",
        "description": "Instagramコメント。ユーザー「ten」がKくんへ、恋愛系アカウント運用についての質問。心理学的な観点からのプロデューサー的アプローチについての提案。"
    },
    {
        "index": 840,
        "filename": "image_16.png",
        "description": "Instagramコメント。Kくんが恋愛リールの構成や写真使用についての詳細なアドバイスを提供。フィード投稿の構成とリール活用の差別化について説明。"
    },
    {
        "index": 841,
        "filename": "image_17.png",
        "description": "Instagramコメント。ユーザー「かなこ」がKくんへ、SNS発信のジャンル決定についての質問。女性性や権威性の重要性について相談。"
    },
    {
        "index": 842,
        "filename": "image_18.png",
        "description": "Instagramコメント。Kくんがかなこの悩みについて詳細にアドバイス。ジャンル選定と実績作りのバランスについて、また子育てジャンルでの可能性について説明。"
    },
    {
        "index": 843,
        "filename": "image_19.png",
        "description": "Instagramコメント。ユーザー「貴」がKくんへ、言葉系アカウント運用についての質問。3000人フォロワーでのストーリー閲覧率と マネタイズの課題について相談。"
    },
    {
        "index": 844,
        "filename": "image_20.png",
        "description": "Instagramコメント。Kくんが貴の相談に回答。アフィリエイト選定の重要性や、ミイダス・VIEW・複数のアプリDLコンディションについての詳細な説明とアドバイスを記載。"
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

    print(f"\n✓ Batch 825-844 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
