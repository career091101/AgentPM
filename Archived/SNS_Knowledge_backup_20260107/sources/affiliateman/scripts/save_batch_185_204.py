#!/usr/bin/env python3
"""
Batch 185-204の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 185-204の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 185,
        "filename": "image_07.png",
        "description": "転職ジャンルのインスタグラムアカウント紹介。machicooooo（投稿216件、フォロワー3.1万人）と「年収200万アップ」をテーマにした転職支援アカウント、および komu.taro（投稿229件、フォロワー3.6万人）による初心者向けの資産運用・転職スキル情報アカウント。"
    },
    {
        "index": 186,
        "filename": "image_08.png",
        "description": "歯と口臭ジャンルのインスタグラムアカウント「dentaltimes」（投稿1058件、フォロワー5.1万人）。歯と美容の総合メディアとして、デンタルケアや美容情報を発信している。"
    },
    {
        "index": 187,
        "filename": "image_09.png",
        "description": "ふるさと納税ジャンルのインスタグラムアカウント紹介。furusatoshufu（投稿121件、フォロワー1万人）による納税大好き主婦の返礼品レビュー、および yummy_recipe.jp（投稿630件、フォロワー9万人）による日本最大級のふるさと納税SNS「Yummy」。"
    },
    {
        "index": 188,
        "filename": "image_10.png",
        "description": "バストアップジャンルのインスタグラムアカウント紹介。rire_bust（投稿324件、フォロワー1.4万人）はバストアップ・育乳専門サロンの新宿/銀座/広尾店紹介、nice_boobs_nao（投稿880件、フォロワー1.5万人）はバストアップ・マンネリ解消@NAOのアカウント。"
    },
    {
        "index": 189,
        "filename": "image_11.png",
        "description": "ペットジャンルのインスタグラムアカウント紹介。wanchanngram.of...（投稿270件、フォロワー1万人）による犬のための情報メディア、petcy_official（投稿554件、フォロワー4.5万人）によるペット専門メディア「Petcy」、doglifelab（投稿212件、フォロワー3.2万人）による愛犬との暮らし研究所。"
    },
    {
        "index": 190,
        "filename": "image_12.png",
        "description": "ペットを含む宿泊施設の検索結果ページ。ペット同伴可能な宿泊プラン検索で、東京ディズニーリゾート関連の宿泊オプションや、わんちゃんと一緒に泊まれるリゾートティ施設が表示されている。"
    },
    {
        "index": 191,
        "filename": "image_13.png",
        "description": "ブルーオーシャンジャンルの見解を示すバナー画像。紫地に「各ジャンルの僕の見解」というタイトルと、左右の装飾的なボックスアイコンが配置されている。"
    },
    {
        "index": 192,
        "filename": "image_14.png",
        "description": "2023年以降のインスタグラム稼ぎ方に関する情報バナー。赤地に「インスタで稼ぐための固定ピン活用事例まとめ」というタイトルと、ロケットアイコン、目盛りアイコン、ビジネスマンの図解が表示されている。"
    },
    {
        "index": 193,
        "filename": "image_15.png",
        "description": "2023年インスタ攻略のストーリー閲覧率爆伸びに関する情報バナー。紫と赤地に「1週間で7%から38%」という数値改善結果を示すグラフと、ビジネスマンの図解が配置されている。"
    },
    {
        "index": 194,
        "filename": "image_16.png",
        "description": "フォロワー増加の施策に関する情報バナー。青地に「外部誘導でフォロワー爆伸び - インスタ＆Twitter【フォロワー伸びた成功事例紹介】」というタイトルと、SNSアイコンが表示されている。"
    },
    {
        "index": 195,
        "filename": "image_17.png",
        "description": "メンズ美容ジャンルのインスタグラムアカウント紹介。mens.kirei（投稿140件、フォロワー2346人）による「モペくん」のメンズ美容お兄さんアカウント、menk_inc（投稿666件、フォロワー2.6万人）によるメンズメイク・スキンケア情報アカウント「Menk」。"
    },
    {
        "index": 196,
        "filename": "image_18.png",
        "description": "各ジャンルの見解を示すセクションの見出しバナー。左右の装飾的なボックスアイコンと中央に「各ジャンルの僕の見解」というテキストが配置されている。"
    },
    {
        "index": 197,
        "filename": "image_19.png",
        "description": "2023年以降のインスタで稼ぐために必要な知識に関する情報バナー。紫地に「稼ぐアカウント特徴」というタイトルと、土星アイコン、ビジネスマンの図解が表示されている。"
    },
    {
        "index": 198,
        "filename": "image_20.png",
        "description": "インスタで稼ぐジャンルで月100万円を狙える内容に関する情報バナー。黄地に「月100万円狙えるジャンル - マネタイズ戦略を共有」というタイトルと、手のジェスチャー、コイン装飾アイコンが配置されている。"
    },
    {
        "index": 199,
        "filename": "image_21.png",
        "description": "2023年インスタ攻略のコンセプト設計基礎に関する情報バナー。紫地に「圧倒的な差別化をしよう」というサブタイトルと、ターゲットアイコン、ビジネスマンの図解が表示されている。"
    },
    {
        "index": 200,
        "filename": "image_22.png",
        "description": "2023年以降のインスタで稼ぐために必要な知識に関する総括バナー。紫地に「稼ぐアカウント特徴」というタイトル、土星アイコン、ビジネスマンの図解が配置された総合セクションのヘッダー。"
    },
    {
        "index": 201,
        "filename": "image_23.png",
        "description": "インスタグラムのアカウント設計における発信者と属人性の関係図。女性図解の発信者から「発言内容/情報」への3本の矢印が出て、「興味」ハートを経由して、「属人性あり」（赤円）と「属人性なし」（オレンジ円）に分岐する概念図。"
    },
    {
        "index": 202,
        "filename": "image_24.png",
        "description": "ビューティー・スキンケアジャンルのインスタグラムアカウント紹介。riena.excel（投稿134件、フォロワー20.9万人）による「Excel Cafe」のエクセル初心者向けアカウント、she_officails（投稿2641件、フォロワー14.1万人）によるシーライクスのブランドアカウント。"
    },
    {
        "index": 203,
        "filename": "image_01.png",
        "description": "美容整形ジャンルのインスタグラムアカウント紹介。mimitan090909（投稿381件、フォロワー6.9万人）による美容愛好家アカウント（ベビーオイル洗顔推奨）、sbc_sakuratomita（投稿227件、フォロワー1万人）による美容整形医のアカウント（SBC新橋銀座口院）。"
    },
    {
        "index": 204,
        "filename": "image_02.jpg",
        "description": "インスタグラムのアカウント設計における発信者と属人性の基本構図。左側に「発信者」、右側に「発言内容/情報」の枠、その下に「興味」ハートマークと「属人性あり」「属人性なし」の2つの属性が示された概念図。"
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

    print(f"\n✓ Batch 185-204 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
