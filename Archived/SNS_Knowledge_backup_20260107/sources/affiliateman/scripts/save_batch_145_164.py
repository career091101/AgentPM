#!/usr/bin/env python3
"""
Batch 145-164の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 145-164の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 145,
        "filename": "image_04.png",
        "description": "トレーニング・痩せ・グルメジャンルの4つのインスタアカウント事例。diet_minpasoはパーソナルトレーナー（フォロワー15.7万人）、rakuyasejoshiはラク痩せ販（フォロワー18.1万人）、shibasaki_insはオートミール特化（フォロワー9.2万人）、protein_meiはプロテイン女子（フォロワー3744人）を紹介。"
    },
    {
        "index": 146,
        "filename": "image_05.png",
        "description": "美容・コスメジャンルの4つのインスタアカウント事例。bluebe_chanはパーソナルカラー診断（フォロワー9万人）、make_hitoeはひとえメイク講座（フォロワー2.1万人）、lipsjpはLIPS公式コスメ・メイク動画（フォロワー81.5万人）、kosme_jpはコスミー韓国コスメ情報（フォロワー5.5万人）を展示。"
    },
    {
        "index": 147,
        "filename": "image_06.png",
        "description": "教育・言語ジャンルの3つのインスタアカウント事例。easy_eikawaは初心者向け英会話教育（フォロワー2.7万人）、eigo_no_senpaiは英会話講座（フォロワー6.2万人）、hiro.historyは日本史のヒロキ（フォロワー3.6万人）で学習コンテンツを提供。"
    },
    {
        "index": 148,
        "filename": "image_07.png",
        "description": "知育玩具・子育てジャンルの4つのインスタアカウント事例。gmamanoikujiは虹色の知育玩具（フォロワー10.1万人）、mamapost_officialはママボスト子育て情報（フォロワー14.2万人）、meeeroomは離乳食ズボラママ向け情報（フォロワー12.5万人）、yurupura_haruは子育てあるある発信（フォロワー1.6万人）。"
    },
    {
        "index": 149,
        "filename": "image_08.png",
        "description": "楽天・割引・ポイ活ジャンルの4つのインスタアカウント事例。rakuten_okanは楽天特化情報（フォロワー12.4万人）、chiaki_chokisはチーク貯金・割引情報（フォロワー9.3万人）、pointkodukai はポイ活解説（フォロワー4.3万人）、tamerun_は貯金術メディア（フォロワー8.8万人）。"
    },
    {
        "index": 150,
        "filename": "image_09.png",
        "description": "時短レシピ・節約レシピジャンルの4つのインスタアカウント事例。yummy_recipe.jpは時短レシピ（フォロワー9.8万人）、setsuyacookは節約レシピまとめ（フォロワー45.7万人）、kyou_nani_tabetaは低糖質レシピ（フォロワー11.6万人）、tamago_recipeはスイーツレシピ（フォロワー2.6万人）。"
    },
    {
        "index": 151,
        "filename": "image_10.png",
        "description": "ひとり暮らし・同棟暮らし・ニトリ特化ジャンルの4つのインスタアカウント事例。hiyo_101211はひとり暮らし美容情報（フォロワー17.8万人）、tiptiptip_は同棟カップルインテリア情報（フォロワー18.4万人）、hitommy_teddyroomはニトリ女子（フォロワー1.1万人）、ririri031は掃除特化情報（フォロワー7.7万人）。"
    },
    {
        "index": 152,
        "filename": "image_11.png",
        "description": "旅行・交通ジャンルの4つのインスタアカウント事例。travelife_coupleは夫婦旅行情報（フォロワー21.5万人）、tabinessは国内旅行Ness（フォロワー6.7万人）、tabimemo_globalは海外旅行メモ（フォロワー1728人）、trevary_hotelsはホテル選び情報（フォロワー4.7万人）。"
    },
    {
        "index": 153,
        "filename": "image_12.png",
        "description": "キャリア・転職・就活ジャンルの4つのインスタアカウント事例。machioooooは転職で年収200万アップ情報（フォロワー2.5万人）、white_tensyoku_officialはホワイト転職アドバイザー（フォロワー3.4万人）、menhera_shukatsuは元メンヘラ就活生向け情報（フォロワー5.8万人）、ao.no.kurashiは大学生バイト情報（フォロワー1.7万人）。"
    },
    {
        "index": 154,
        "filename": "image_13.png",
        "description": "ファッション系インスタアカウント4つの事例。低身長向けコーデ、ユニクロ活用、古着スタイル、大人コーディネートの各特化アカウントを紹介して、それぞれのニッチジャンル展開の成功例を示している。"
    },
    {
        "index": 155,
        "filename": "image_14.png",
        "description": "渋谷トレンド・流行テーマジャンルの3つのインスタアカウント事例。109_shibuya（SHIBUYA109公式、フォロワー10.1万人）、trendmirror_jpはトレンドミラーメディア（フォロワー3.6万人）、trepo.jpはトレポトレンド情報ライター（フォロワー1万人）でトレンド発信。"
    },
    {
        "index": 156,
        "filename": "image_15.png",
        "description": "雑学・教養系インスタアカウント3つの事例。zatsugakukunは雑学系ブロガー（フォロワー12.5万人）、zatsugaku2021は雑学の館エンタメサイト（フォロワー5.8万人）、zatsugaku_chanは毎日雑学更新（フォロワー8.9万人）で知識コンテンツを提供。"
    },
    {
        "index": 157,
        "filename": "image_16.png",
        "description": "エンタメ系インスタアカウント2つの事例。everyday_debudoriは毎日でぶどり漫画（フォロワー34.7万人）、buson2025はBUSON動画クリエイター（フォロワー72万人）で笑い・エンタメコンテンツを発信。"
    },
    {
        "index": 158,
        "filename": "image_17.png",
        "description": "恋愛・体験談系インスタアカウント3つの事例。sare_misakiはサレ妻みさき浮気女（フォロワー4.8万人）、sareo_oiはサレ夫浮気男（フォロワー6.6万人）、jun.waidanは純猿談恋愛話（フォロワー12.2万人）で体験談を発信。"
    },
    {
        "index": 159,
        "filename": "image_18.png",
        "description": "アダルト・成人向けジャンルの3つのインスタアカウント事例。lclovecosmetic_japanはラブコスメ公式アダルトグッズ情報（フォロワー6.5万人）、hiraizumiharunaはエロ漫画アート技術（フォロワー25.4万人）、sexy_joyuはAV女優情報（フォロワー6965人）。"
    },
    {
        "index": 160,
        "filename": "image_19.png",
        "description": "日用品・食品店舗紹介系インスタアカウント3つの事例。miji_mujiは無印良品ガチレビュー（フォロワー21.2万人）、mizuki_karudi_はカルディー商品レビュー（フォロワー約5万人）、otoriyose_foodsはお取り寄せコンシェルジュ（フォロワー12.2万人）。"
    },
    {
        "index": 161,
        "filename": "image_20.png",
        "description": "健康・美容整体系インスタアカウント2つの事例。sangokotsuban.leafは産後骨盤矯正専門家あずま先生（フォロワー10.9万人）、yori_mindbodyはYori骨格から美身体作成（フォロワー4.2万人）で美容健康情報を提供。"
    },
    {
        "index": 162,
        "filename": "image_21.png",
        "description": "グルメ・お取り寄せ系インスタアカウント2つの事例。otoriyose_foodsはお取り寄せ食品コンシェルジュ（フォロワー12.2万人）、otoriyose.jpは全国お取り寄せグルメ情報（フォロワー5.8万人）で食品紹介を発信。"
    },
    {
        "index": 163,
        "filename": "image_22.png",
        "description": "アウトドア・趣味系インスタアカウント3つの事例。camp_hackはCAMP_HACK日本最大級アウトドアWEBマガジン（フォロワー38.7万人）、cammeshiはキャンメシキャンプ飯（フォロワー12万人）、sauna_matomeiはサウナまとめ情報（フォロワー7685人）。"
    },
    {
        "index": 164,
        "filename": "image_23.png",
        "description": "美容・健康特化系インスタアカウント3つの事例。hotel_lovers.officialはカラコン通販HOTEL LOVERS特化（フォロワー8.2万人）、dentaltimesはデンタルタイムズ歯磨き・美容総合メディア（フォロワー3.6万人）、hair_channel.jpはヘアチャネルヘアアレンジ動画（フォロワー10.1万人）。"
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

    print(f"\n✓ Batch 145-164 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
