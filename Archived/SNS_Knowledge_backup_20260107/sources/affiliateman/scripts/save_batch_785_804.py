#!/usr/bin/env python3
"""
Batch 785-804の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 785-804の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 785,
        "filename": "image_185.png",
        "description": "ジョーカーさんが2ヶ月前に投稿した質問。学んだ知識とコンテンツ化について、コンサル受講でも生徒さんに成果を出してあげられるか、などの質問が記載されている。"
    },
    {
        "index": 786,
        "filename": "image_186.png",
        "description": "K君が2ヶ月前に投稿したジョーカーさんの質問への回答。自分の実績と選定理由、高額単発コンサルの話など、具体的な事例を混じえた詳細な返信内容。"
    },
    {
        "index": 787,
        "filename": "image_187.png",
        "description": "ジョーカーさんとK君の対話。ジョーカーさんが長期コンサルのイメージについて質問し、K君が長期コンサルと短期コンサルの順序について返信している会話。"
    },
    {
        "index": 788,
        "filename": "image_188.png",
        "description": "はしぎさんが2ヶ月前に投稿した質問。個人的にアフィリエイト導入を考えており、ダイエット系の投稿をしている中でアフィリエイト選定について相談している。"
    },
    {
        "index": 789,
        "filename": "image_189.png",
        "description": "はしぎさんが提示した3つのアフィリエイト案件について、K君が骨盤ケア系アカウント向けの詳細なアドバイスを返信している画像。"
    },
    {
        "index": 790,
        "filename": "image_190.png",
        "description": "トヨさんが2ヶ月前に投稿した質問。Twitterフォロワー1900人でnote販売を検討中で、具体的な売上数値の例を挙げながら相談している。"
    },
    {
        "index": 791,
        "filename": "image_191.png",
        "description": "K君がトヨさんのnote売却戦略について返信。フォロワー数が実績に与える影響について、具体的な例を用いながら詳しく説明している。"
    },
    {
        "index": 792,
        "filename": "image_192.png",
        "description": "トヨさんが引き続き投稿。noteの売却可能性について、K君のアドバイスと自身の課題についての会話が続いている。"
    },
    {
        "index": 793,
        "filename": "image_193.png",
        "description": "3104hasegawaさんが2ヶ月前に投稿した質問。noteでアフィリエイトしたいが、記事内のアフィリエイトリンク設定方法とASP連携について質問している。"
    },
    {
        "index": 794,
        "filename": "image_194.png",
        "description": "K君が3104hasegawaさんへ返信。noteでのアフィリエイトはASP側の規約制限が全て適用されること、WordPressとcodocでの組み合わせについて説明している。"
    },
    {
        "index": 795,
        "filename": "image_195.png",
        "description": "ましゅー / Twitterも同じ名前ですさんが2ヶ月前に投稿した質問。note or コンサルで選択に迷っており、骨格診断やパーソナルカラー診断との組み合わせについて相談している。"
    },
    {
        "index": 796,
        "filename": "image_196.png",
        "description": "K君がましゅーさんへ返信。note売却の位置づけとコンサルの違い、女性向けの「ゴールデット」による需要の話など、ジャンル分析を交えた詳細なアドバイス。"
    },
    {
        "index": 797,
        "filename": "image_197.png",
        "description": "ましゅーさんが2ヶ月前に投稿した続きの質問。20代前半の女性ペルソナについての具体的な課題や、コンテンツ選択肢についての相談内容。"
    },
    {
        "index": 798,
        "filename": "image_198.png",
        "description": "ワタルさんが2ヶ月前に投稿した質問。Twitterからオンラインサロンへのマネタイズを考えており、サロン誘導の具体的な方法について相談している。"
    },
    {
        "index": 799,
        "filename": "image_199.png",
        "description": "K君がワタルさんへ返信。Twitter上での無料相談やzoomでの個別相談、ライン読導によるセールス方法など、3つの具体的な施策を提案している。"
    },
    {
        "index": 800,
        "filename": "image_200.png",
        "description": "シュンさんが2ヶ月前に投稿した質問。恋愛系のnoteが2980円で売上が出ており、K君のコンバージョン率を聞きながら価格設定についての相談。"
    },
    {
        "index": 801,
        "filename": "image_201.png",
        "description": "K君がシュンさんへ返信。Twitterのフォロワー数と収益の相関関係について、具体的な金額例を挙げながら詳しく説明している。"
    },
    {
        "index": 802,
        "filename": "image_202.png",
        "description": "Romuさんが2ヶ月前に投稿した質問。Instagramでの恋愛占いアフィリについて、記事内容の最適化とストーリーズ活用による売上向上について相談している。"
    },
    {
        "index": 803,
        "filename": "image_203.png",
        "description": "K君がRomuさんへ返信。恋愛相談回答から恋愛占いアフィリへのシフト、マッチングアプリを用いたコンテンツ作成など、実践的なアドバイスを詳述している。"
    },
    {
        "index": 804,
        "filename": "image_204.png",
        "description": "ひなたさんが2ヶ月前に投稿した質問。SNSで宣伝依頼を受けるサービス「Price2Alert」について紹介し、ユーザー拡大方法についての相談内容。"
    }
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

    print(f"\n✓ Batch 785-804 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
