#!/usr/bin/env python3
"""
Batch 745-764の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 745-764の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 745,
        "filename": "image_145.png",
        "description": "インスタグラムのDM画面。ユーザーくん（@ちゃむ）がアカウント設定やフォロワーの増やし方について質問・相談する複数のメッセージが表示されている。"
    },
    {
        "index": 746,
        "filename": "image_146.png",
        "description": "トヨさん（@KK さん）がリツイート企画の失敗について相談。企画内容不足やプレゼント条件の問題、速度不足が原因として分析されている。"
    },
    {
        "index": 747,
        "filename": "image_147.png",
        "description": "トヨさんとKK さんのDM会話。フォロワー増加とセンス無しアカウントについての議論、DM戦略についてのアドバイスが含まれている。"
    },
    {
        "index": 748,
        "filename": "image_148.png",
        "description": "トヨさんとKK さんの継続的なDM会話。ネタ集案や過去ツイートの活用、フォロワー層の特性を活かしたコンテンツ戦略について議論。"
    },
    {
        "index": 749,
        "filename": "image_149.png",
        "description": "ときさん（@KK さん）からのDM。 RTやビジネスアカウント関連の質問が記載され、フォロワー数1万人超の目標設定と達成方法が示されている。"
    },
    {
        "index": 750,
        "filename": "image_150.png",
        "description": "あべさん（@KK さん）からのDM。メンタル系アカウントについての質問や、コミュ障との関係性、フォロワー伸ばし方、マネタイズ戦略について相談。"
    },
    {
        "index": 751,
        "filename": "image_151.png",
        "description": "もりりさん（@KK さん）からのTikTok/YouTube活用に関するDM。大人ファッションアカウント運営での複数プラットフォーム戦略についての相談。"
    },
    {
        "index": 752,
        "filename": "image_152.png",
        "description": "もりりさんのBMXアカウント関連DM。TikTokのニッチジャンル活用、アカウント名の決め方、4タイトルの改善提案が記載されている。"
    },
    {
        "index": 753,
        "filename": "image_153.png",
        "description": "KK さんのDM返信。転職ジャンルでのアフィリエイト販売方法やスキル系の短編動画についての具体的なアドバイスが含まれている。"
    },
    {
        "index": 754,
        "filename": "image_154.png",
        "description": "10番（@KK さん）からのDM。TikTokの企画要件や再生数の稼ぎやすいジャンル、企画の成功パターンについての質問が記載。"
    },
    {
        "index": 755,
        "filename": "image_155.png",
        "description": "コーヒー（kohi）さんのDM。TikToで企業案件の条件（フォロワー数など）やPR案件の見つけ方についての相談。"
    },
    {
        "index": 756,
        "filename": "image_156.png",
        "description": "ぶろぶろさん（@KK さん）のDM。TikTokアカウント参加条件（バイト、転職、バイト&転職など）について3つのオプションが提示されている。"
    },
    {
        "index": 757,
        "filename": "image_157.png",
        "description": "やまくちさん（@KK さん）のDM。転職ジャンルでのアフィリエイト販売方法やブログ作成と公式ラインでの教育法について相談。"
    },
    {
        "index": 758,
        "filename": "image_158.png",
        "description": "やまくちさんのDM。TikTokの投稿頻度・ライブ活用・インスタ誘導・ブログリンク・アフィリエイト販売など総合的な戦略に関する質問。"
    },
    {
        "index": 759,
        "filename": "image_159.png",
        "description": "たけるさん（@KK さん）のDM。iPhone便利技・ガジェット系Instagramアカウント（1.6万フォロワー）の運営状況とマネタイズ課題について相談。"
    },
    {
        "index": 760,
        "filename": "image_160.png",
        "description": "たけるさんのDM。iPhone系アフィリエイト販売の売上げ方法や使い分けについての詳細な質問と、KK さんの具体的なアドバイス。"
    },
    {
        "index": 761,
        "filename": "image_161.png",
        "description": "たけるさんのDM続き。「Screenshot-2023-02-03T020634.513.png」というファイル名でZenlyなどのアプリ紹介画像が添付されている。"
    },
    {
        "index": 762,
        "filename": "image_162.png",
        "description": "たけるさんのDM。アフィについてのアドバイスやPR要件、コンテンツジャンルについての質問が続いている。"
    },
    {
        "index": 763,
        "filename": "image_163.png",
        "description": "たけるさんのDM。女性向けマッチングアプリやTwitterのコンテンツ発信タイミング、アカウント添付方法についての追加質問。"
    },
    {
        "index": 764,
        "filename": "image_164.png",
        "description": "たけるさんのDM最後のメッセージ。オンラインサロンやマネタイズ方法、テーマ選定について複数の疑問が記載されている。"
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

    print(f"\n✓ Batch 745-764 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
