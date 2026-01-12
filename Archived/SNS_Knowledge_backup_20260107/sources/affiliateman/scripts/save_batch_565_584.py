#!/usr/bin/env python3
"""
Batch 565-584の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 565-584の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 565,
        "filename": "image_21.png",
        "description": "Twitterユーザー「えり」の質問。地域アカウント（2.5万フォロワー）運営中で、現在アフィのみの収益で企業PR逆営業を検討している状況。無料で継続vs商談で決める判断について相談している。"
    },
    {
        "index": 566,
        "filename": "image_22.png",
        "description": "KKさんからの回答。PR案件月100万円の実績者の対談動画を最初公開したが、グルメ店での営業施策事例や固定ツイートのテーマ展開、有料noteのマネタイズ方法について詳細に説明。"
    },
    {
        "index": 567,
        "filename": "image_23.png",
        "description": "食べログの渋谷駅グルメ・レストラン検索画面。850m圏内の店舗と『焼肉 黒田』の詳細情報が表示されている。4270件のクチコミがある店舗情報例。"
    },
    {
        "index": 568,
        "filename": "image_24.png",
        "description": "Twitterユーザー「よし」の質問。インスタで女性向け複線アカウント運営中で、コンサル商品販売を検討している複線コンサルについての相談。"
    },
    {
        "index": 569,
        "filename": "image_25.png",
        "description": "KKさんからの回答。複線アフィのマッチングアプリ(Pairs/タップル/omiai)、電話占い、コンプレックス商材に関する詳細なマネタイズ方法と必要な教育について説明。"
    },
    {
        "index": 570,
        "filename": "image_26.png",
        "description": "アカウント「かける」の質問。インスタ金運・スピジャンルで選ぶ3ヶ月でフォロワー4000人にまで来たが、アフィやnoteリンクのストーリー頻度増加について質問。"
    },
    {
        "index": 571,
        "filename": "image_27.png",
        "description": "KKさんからの回答。インスタマネタイズ戦略についての詳細説明。note有料化やコンサル希望者紹介、フォロワー数と収益の関係性について説明。"
    },
    {
        "index": 572,
        "filename": "image_28.png",
        "description": "Twitterユーザー「やす」の質問。公式LINEのリスト数が400人でダイエット3ヶ月で49800円のコーチング検討中。ダイエットジャンルの女性向け複線ジャンル参入について相談。"
    },
    {
        "index": 573,
        "filename": "image_29.png",
        "description": "KKさんからの回答。複線アフィのマッチングアプリ・電話占い・コンプレックス商材のマネタイズ方法を詳細に説明。有料noteの価格設定やコンサル商品価格の50%戦略について言及。"
    },
    {
        "index": 574,
        "filename": "image_30.png",
        "description": "yanoユーザーの質問。インスタ画像とTikTok視線で2点の悩み。ダイエット等で情報発信するSNSの選択肢やTikTokマネタイズについて質問している。"
    },
    {
        "index": 575,
        "filename": "image_31.png",
        "description": "Twitterユーザー「Kan」の質問。友人が美容院店舗アカウントで売上100万円に達成し、運用代行業を展開中。DM専用アカウント作成とモデルアカウント化についての相談。"
    },
    {
        "index": 576,
        "filename": "image_32.png",
        "description": "KKさんからの回答。店舗DM営業と運用代行モデル化についての説明。Kanさんが参考にできるInstagramアカウント実例と固定ピンの使い方について紹介。"
    },
    {
        "index": 577,
        "filename": "image_33.png",
        "description": "アカウント「かける」の質問。ダイエット等で初めて投稿し2点質問。ダイエット缶Twitter(4000人フォロワー)で朝6時のツイートインプの平均状況と公式LINE集客施策について。"
    },
    {
        "index": 578,
        "filename": "image_34.png",
        "description": "KKさんからの回答。マネタイズ方法について詳細説明。(1)複線のアフィについてのPairsやタップルのマッチングアプリ解説と(2)複線コンサル施策の料金モデル比較。"
    },
    {
        "index": 579,
        "filename": "image_35.png",
        "description": "アカウント「かける」の追加質問。6点について質問。プレインでnoが無いノートなのか等、月100万の内訳、月1回限定の頻度でnoteの告知ツイート、購入特典など詳細について質問。"
    },
    {
        "index": 580,
        "filename": "image_36.png",
        "description": "KKさんからの回答。noteについてのビジネス構築に関する詳細説明。Brainとnoteの違い、コンテンツ販売とコンサルの収益構造、月1回100万超えダイエット方法について説明。"
    },
    {
        "index": 581,
        "filename": "image_37.png",
        "description": "KKさんの続きの回答。noteの月間売上が130万円の実績紹介。無料noteのリリース後の施策とフォロワー紹介、コンテンツの内容についての戦略説明。"
    },
    {
        "index": 582,
        "filename": "image_38.png",
        "description": "Twitterユーザー「Toyo(トヨ)」の質問。Twitterアカウント＆商材について。Twitterフォロー、note英語学習教材、12月4件、1月0件の販売実績についての質問。"
    },
    {
        "index": 583,
        "filename": "image_39.png",
        "description": "KKさんからの回答。ToyoさんへのサムネTwitter構成と英語学習教材の販売戦略についての回答。TOEICの単語、日常英会話等のツイートリップ戦略と指導的アドバイス。"
    },
    {
        "index": 584,
        "filename": "image_40.png",
        "description": "アカウント「るる」の質問。女性向けの複線ジャンル参入について。SNSの選択肢、フロー設定、1SNS複線専門アカウント作成などについて7件の相談をしている。"
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

    print(f"\n✓ Batch 565-584 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
