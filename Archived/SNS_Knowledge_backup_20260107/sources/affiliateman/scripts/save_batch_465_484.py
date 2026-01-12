#!/usr/bin/env python3
"""
Batch 465-484の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 465-484の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 465,
        "filename": "image_97.png",
        "description": "Instagramのコメント欄。ユーザーRyoko（27日前）から「早速ですが、下記について質問させてください」と3つの補填アカウント運営に関する質問が投稿されている。"
    },
    {
        "index": 466,
        "filename": "image_98.png",
        "description": "Instagramのコメント返信。ユーザーひろ（25日前）が「@Kくん お世話になっております。質問失礼します」と述べ、マネタイズ方法や低予算で親子で遊べるコンテンツ企画に関する質問をしている。"
    },
    {
        "index": 467,
        "filename": "image_99.png",
        "description": "Instagramのコメント返信。Kくん（25日前）が「あります。これもちゃい感じですね」と返信し、マネタイズ方法やストーリー、プロフィール構成、ブログ活用についてのアドバイスを詳細に記述している。"
    },
    {
        "index": 468,
        "filename": "image_100.png",
        "description": "Instagramのコメント続き。ストーリーやリール運用について「ストーリー3：2で回収した回答をまとめる」などの具体的な戦略が記載されている。"
    },
    {
        "index": 469,
        "filename": "image_101.png",
        "description": "Instagramのコメント。「属人性の有無」について「あ、こちらに関しては悩み系が多いので、情報に価値を持たせた方が大切なので、絶対に要るということはないです」という回答が記載されている。"
    },
    {
        "index": 470,
        "filename": "image_102.png",
        "description": "Instagramのコメント。美種ユーザーが初心者むけアカウント研究について質問しており、Kくんが「Twitter新版のをフォローせて貴きました」と返信している。"
    },
    {
        "index": 471,
        "filename": "image_103.png",
        "description": "Instagramのコメント返信。美種ユーザーがパーソナルカラーや美容系アカウント運営に関する質問をしており、Kくんが詳細なアドバイスを提供している。"
    },
    {
        "index": 472,
        "filename": "image_104.png",
        "description": "Instagramのコメント。美種ユーザー（24日前）が初心者向けアカウントのリサーチと上手くいくコツについて質問している。また別の質問として「新規フォロワーの見分け方」についても質問されている。"
    },
    {
        "index": 473,
        "filename": "image_105.png",
        "description": "Instagramのコメント返信。美種ユーザーが「なぜ完全に文字入れしないで始めるのは厳しいですか」と追加質問をしており、Kくんが詳細な説明を提供している。"
    },
    {
        "index": 474,
        "filename": "image_106.png",
        "description": "Instagramのコメント。美種ユーザー（18日前）から「ありがとうございます！」で始まる長文コメントがあり、TikTokとInstagramの運用方針の違いについて質問されている。"
    },
    {
        "index": 475,
        "filename": "image_107.png",
        "description": "Instagramのコメント返信。Kくん（17日前）が「なるほど、インスタに関してはリールを使い回してフィードはそこまで重要視しなくて良いということですね」と返信している。"
    },
    {
        "index": 476,
        "filename": "image_108.png",
        "description": "Instagramのコメント返信。もり（25日前）が「一点質問させてください」と、投稿が異様にリーチ数が下がっている理由についての質問を投稿している。"
    },
    {
        "index": 477,
        "filename": "image_109.png",
        "description": "Instagramのコメント返信。もり（24日前）が「あります」と返信しており、アルゴリズム変化とリーチ数の関係についての詳細な説明が記載されている。"
    },
    {
        "index": 478,
        "filename": "image_110.png",
        "description": "Instagramのコメント。ルッチ（27日前）から「現在不動産紹介アカウントを構築しようと動いている段階です」と自社の現状について述べられており、相場感や契約方法についての質問がある。"
    },
    {
        "index": 479,
        "filename": "image_111.png",
        "description": "Instagramのコメント返信。Kくん（26日前）が「上記のような感じでやってくかかるのかの教えてください」と返信し、不動産アカウント構築に関するアドバイスを提供している。"
    },
    {
        "index": 480,
        "filename": "image_112.png",
        "description": "Instagramのコメント。村上空（26日前）が「質問失礼します」と述べ、自己啓発会社員と自己啓発教員での発信について質問をしている。"
    },
    {
        "index": 481,
        "filename": "image_113.png",
        "description": "Instagramのコメント返信。Kくん（8日前）が回答をしており、参考になるアカウント例として複数のInstagramアカウントのURLリストが記載されている。"
    },
    {
        "index": 482,
        "filename": "image_114.png",
        "description": "Instagramのコメント。Shun（25日前）が「プレゼント企画についてご質問させていただきます」と述べ、InstagramとTwitterでのプレゼント企画の実施方法についての質問がある。"
    },
    {
        "index": 483,
        "filename": "image_115.png",
        "description": "Instagramのコメント返信。Kくん（25日前）が「プレゼント企画はグレーですね」と返信し、Instagramでのプレゼント企画の実施方法やリスクについての詳細な説明が記載されている。"
    },
    {
        "index": 484,
        "filename": "image_116.png",
        "description": "Instagramのコメント返信。Kくん（25日前）から「ありがとうございます！」で始まる返信があり、プレゼント企画戦略に関する詳細なアドバイスが記載されている。"
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

    print(f"\n✓ Batch 465-484 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
