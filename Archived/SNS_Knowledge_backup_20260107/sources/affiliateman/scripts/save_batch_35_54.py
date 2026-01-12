#!/usr/bin/env python3
"""
Batch 35-54の画像説明を保存
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 35-54の画像説明
batch_descriptions = [
    {
        "index": 35,
        "filename": "image_06.png",
        "description": "緑のお菓子の箱の写真に「これ食べたことある？」という質問。クイックアクションでDMで教えてくださいと誘導するストーリー投稿の例。"
    },
    {
        "index": 36,
        "filename": "image_07.png",
        "description": "料理の写真に「みんなの今月の目標は？」という質問。4キロ痩せ、7キロ痩せ、10キロ痩せという選択肢があるダイエット関連のクイックアクション例。"
    },
    {
        "index": 37,
        "filename": "image_08.png",
        "description": "ぬいぐるみの写真に「やばい3キロ増えた」というテキスト。NO-米YES、おすすめのダイエット教えて欲しいというクイックアクションでエンゲージメントを促す例。"
    },
    {
        "index": 38,
        "filename": "image_09.png",
        "description": "ストーリー閲覧率の成長グラフ（施策(1)部分がグレーアウト、施策(2)が強調表示）。次のステップとしての施策(2)を示している。"
    },
    {
        "index": 39,
        "filename": "image_10.jpg",
        "description": "インスタグラムDMの受信画面のスクリーンショット。「リクエスト99+件」と大量のストーリーへの返信が表示されており、高エンゲージメントの証拠を示している。"
    },
    {
        "index": 40,
        "filename": "image_11.png",
        "description": "インスタストーリーのクイックアクション機能の使い方を示す2画面比較。①メッセージ送信→②絵文字リアクション（クイックリアクション）選択という操作の流れを解説。"
    },
    {
        "index": 41,
        "filename": "image_12.jpg",
        "description": "ダイエットドリンクの写真に「何キロ痩せたことある？」という質問。痩せたことなし、3キロ痩せた、5キロ以上痩せた、10キロ以上痩せた、15キロ以上痩せたという5段階の選択肢でクイックアクションを実装した例。"
    },
    {
        "index": 42,
        "filename": "image_13.png",
        "description": "料理の写真に「どんなコンテンツが見たい？」という質問。地域のうまいラーメン、デートスポット、おしゃれなレストラン、スイーツ店まとめという4つの選択肢でフォロワーのニーズを調査する例。"
    },
    {
        "index": 43,
        "filename": "image_14.png",
        "description": "「2023年インスタ攻略 伸びているジャンル31選 ニーズがあるジャンル理解」という紫のバナー画像。成長中のインスタグラムジャンルを解説する記事への誘導。"
    },
    {
        "index": 44,
        "filename": "image_15.png",
        "description": "「2023年インスタ攻略 ブルーオーシャン16選 今後伸びそうなお宝ジャンル」という紫のバナー画像。競合が少ない有望ジャンルを紹介する記事への誘導。"
    },
    {
        "index": 45,
        "filename": "image_16.png",
        "description": "「インスタマネタイズ ガチで売れるストーリー施策 稼げる最強の施策まとめ」という黄色のバナー画像。ストーリー機能を使った収益化手法を解説。"
    },
    {
        "index": 46,
        "filename": "image_17.png",
        "description": "「インスタ バズった事例紹介 トレンド攻略とリサーチ方法 バズるコンテンツ作成」という紫のバナー画像。バイラルコンテンツの作成ノウハウを紹介。"
    },
    {
        "index": 47,
        "filename": "image_18.png",
        "description": "「インスタで稼ぐための 固定ピン活用事例 まとめ フォロー率/売上UP」という赤/ピンクのバナー画像。プロフィールの固定投稿を活用した収益化戦略を解説。"
    },
    {
        "index": 48,
        "filename": "image_19.png",
        "description": "「2023年インスタ攻略 バズる投稿作成方法 全SNSで活用可のテクニック」という紫のバナー画像。インスタグラムだけでなく全SNSで使えるバズる投稿作成テクニックを紹介。"
    },
    {
        "index": 49,
        "filename": "image_01.png",
        "description": "「インスタ2023年伸びてるアカ 伸びているジャンルと収益方法 アカウント10選とマネタイズ施策」という赤と緑の大きなバナー画像（記事のメインビジュアル）。成功アカウントの分析と収益化手法を詳しく解説する記事。"
    },
    {
        "index": 50,
        "filename": "image_02.jpg",
        "description": "スーツを着た男性の横顔を描いたシンプルなイラスト。"
    },
    {
        "index": 51,
        "filename": "image_03.png",
        "description": "NFT関連の投稿サムネイル18個のコラージュ画像。オレンジ系と黒系の2パターンで、「NFTで人生変わった」「イラストで○○万円稼ぐ」「イーサリアム徹底解説」「OpenSea早押し必勝法」「NFT用語のスラング」などのテーマが並んでいる。"
    },
    {
        "index": 52,
        "filename": "image_04.png",
        "description": "マンガ風投稿サムネイル18個のコラージュ画像。「マッチングアプリ10個使ったのでランキング」「ネットワークビジネスにハマった私」「年収1000万と結婚した話」などの恋愛・お金系コンテンツが並んでいる。"
    },
    {
        "index": 53,
        "filename": "image_05.png",
        "description": "インスタグラム投稿サムネイル27個のコラージュ画像。青系と緑系の2パターンで、「良デザイン作ってみた」「コラボライブ成功の秘訣」「人を服従させる心理学」「投稿作成の時短レシピ」「ChatGPTでネタ切れ解消できる説」「リール動画再生数10倍になりました」などのインスタ運用ノウハウが並んでいる。"
    },
    {
        "index": 54,
        "filename": "image_06.png",
        "description": "インスタグラム投稿サムネイル24個のコラージュ画像。黒背景で、「65日バグを使う人が本当にヤバイ1軍サイト」「病院院長のプロフィール修正してみた」「灰色の使い方」「最強に便利サイト」「Insta Liveデザインの勉強会」「営業用資料簡単の型版」などのビジネス・デザイン系コンテンツが並んでいる。"
    }
]

def update_inventory_with_descriptions(batch_descriptions):
    """image_inventory_progress.jsonを読み込み、説明を追加"""

    # 進捗ファイルを読み込み
    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'
    with open(progress_file, 'r', encoding='utf-8') as f:
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

    # 進捗ファイルを更新
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 進捗保存: {progress_file.name}")

    return inventory

if __name__ == "__main__":
    inventory = update_inventory_with_descriptions(batch_descriptions)
