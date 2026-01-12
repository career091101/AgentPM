#!/usr/bin/env python3
"""
Batch 144-173の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
インスタ2022年ジャンル別マネタイズ集31選の記事
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 144-173の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 144,
        "filename": "image_03.png",
        "description": "ファッション系インスタアカウント4つの事例。「低身長コーデ」（hyororii_69、フォロワー14.1万人）、「ユニクロ特化」（ayaka.k_n、フォロワー1.2万人）、「古着女子」（__atom_store__、フォロワー14.4万人）、「大人コーデ」（nature.otona.coord、フォロワー1.2万人）が並んでいる。"
    },
    {
        "index": 154,
        "filename": "image_13.png",
        "description": "ファッション系インスタアカウント4つの事例（image_03と同じ内容）。低身長、ユニクロ、古着、大人コーデの各特化アカウントを紹介。"
    },
    {
        "index": 155,
        "filename": "image_14.png",
        "description": "トレンド情報系インスタアカウント3つの事例。「渋谷トレンド」（109_shibuya、フォロワー10.1万人、SHIBUYA109公式）、「流行テーマ」（trendmirror_jp、フォロワー3.6万人、Trend Mirror）、「流行テーマ」（trepo.jp、フォロワー1万人、トレポ）が並んでいる。"
    },
    {
        "index": 156,
        "filename": "image_15.png",
        "description": "雑学・教養系インスタアカウント3つの事例。「雑学系」（zatsugakukun、フォロワー12.5万人）、「雑学系」（zatsugaku2021、フォロワー5.8万人、雑学の館）、「雑学系」（zatsugaku_chan、フォロワー8.9万人、雑学ちゃん）が並んでいる。"
    },
    {
        "index": 157,
        "filename": "image_16.png",
        "description": "エンタメ系インスタアカウント2つの事例。「漫画」（everyday_debudori、フォロワー34.7万人、毎日でぶどり）、「笑い」（buson2025、フォロワー72万人、BUSON動画クリエイター）が並んでいる。"
    },
    {
        "index": 158,
        "filename": "image_17.png",
        "description": "恋愛・体験談系インスタアカウント3つの事例。「浮気女」（sare_misaki、フォロワー4.8万人、サレ妻みさき）、「浮気男」（sareo_oi、フォロワー6.6万人、サレ夫ゆうすけ）、「恋愛話」（jun.waidan、フォロワー12.2万人、純猥談）が並んでいる。"
    },
    {
        "index": 159,
        "filename": "image_18.png",
        "description": "アダルト・性関連インスタアカウント3つの事例。「アダルトグッズ」（lclovecosmetic_japan、フォロワー6.5万人、ラブコスメ公式）、「エロ漫画」（hiraizumiharuna0204_2、フォロワー25.4万人、平泉春奈_シンプル画）、「AV女優」（sexy_joyu、フォロワー6965人、ヌケる！AV女優図鑑）が並んでいる。"
    },
    {
        "index": 160,
        "filename": "image_19.png",
        "description": "日用品・食品店紹介系インスタアカウント3つの事例。「無印」（miji_muji、フォロワー21.2万人、ミジ◉無印良品ガチレビュー）、「カルディー」（mizuki_site、フォロワー1.8万人、みぃKALDI）、「業務スーパー」（ayu_repo、フォロワー4.1万人、あゆ◉業務スーパーが好きなママ）が並んでいる。"
    },
    {
        "index": 161,
        "filename": "image_20.png",
        "description": "健康・美容整体系インスタアカウント2つの事例。「骨盤矯正」（sangokotsuban.leaf、フォロワー10.9万人、妊産婦専門家あずま先生、産後骨盤矯正専門院リーフ）、「整体系」（yori_mindbody、フォロワー4.2万人、Yori【骨格から美しい身体を作る先生】）が並んでいる。"
    },
    {
        "index": 162,
        "filename": "image_21.png",
        "description": "グルメ・お取り寄せ系インスタアカウント2つの事例。「お取り寄せ」（otoriyose_foods、フォロワー12.2万人、お取り寄せコンシェルジュ）、「お取り寄せ」（otoriyose.jp、フォロワー5.8万人、全国お取り寄せグルメ）が並んでいる。"
    },
    {
        "index": 163,
        "filename": "image_22.png",
        "description": "アウトドア・趣味系インスタアカウント3つの事例。「キャンプ」（camp_hack、フォロワー38.7万人、CAMP_HACK日本最大級のアウトドアWEBマガジン）、「キャンプ飯」（cammeshi、フォロワー12万人、キャンメシ）、「サウナ」（sauna_matome、フォロワー7685人、サウナまとめ人|厳選サウナ紹介）が並んでいる。"
    },
    {
        "index": 164,
        "filename": "image_23.png",
        "description": "美容・健康特化系インスタアカウント3つの事例。「カラコン特化」（hotel_lovers.official、フォロワー8.2万人、カラコン通販HOTEL LOVERS公式）、「歯磨き特化」（dentaltimes、フォロワー3.6万人、デンタルタイムズ|歯と美容の総合メディア）、「ヘアケア特化」（hair_channel.jp、フォロワー10.1万人、ヘアチャンネル|ヘアアレンジ動画）が並んでいる。"
    },
    {
        "index": 165,
        "filename": "image_24.png",
        "description": "恋愛相談系インスタアカウント2つの事例。「女性の恋愛」（renai_kyoshitsu、フォロワー2.2万人、恋愛教室、恋する乙女のための恋愛教室）、「男性の恋愛」（subaru_lovelife、フォロワー2.3万人、恋愛と人生のコンサルタント＠スバル）が並んでいる。"
    },
    {
        "index": 166,
        "filename": "image_25.png",
        "description": "エンタメ・アイドル情報系インスタアカウント2つの事例。「ジャニーズ」（johnnys_infogram、フォロワー3.4万人、ジャニーズ情報|ジャニオタ向けのオタ活情報）、「ジャニーズ」（j_otachan、フォロワー5.8万人、ジャニオタちゃん|ジャニーズ情報オタ活）が並んでいる。"
    },
    {
        "index": 167,
        "filename": "image_26.png",
        "description": "ディズニー情報系インスタアカウント2つの事例。「ディズニー」（disneypark__maru3、フォロワー2.1万人、まるさん＠ディズニーパーク情報）、「ディズニー」（disney_uramania、フォロワー9.8万人、ディズニー裏マニア）が並んでいる。"
    },
    {
        "index": 168,
        "filename": "image_27.png",
        "description": "音楽プレイリスト系インスタアカウント2つの事例。「音楽情報」（himekuri_playlist、フォロワー2.4万人、日めくりプレイリスト）、「音楽情報」（playlist_of、フォロワー18.8万人、PLAYLIST -プレイリスト-）が並んでいる。"
    },
    {
        "index": 169,
        "filename": "image_28.png",
        "description": "資産運用・金融リテラシー系インスタアカウント2つの事例。「資産運用」（nken.moneyliteracy、フォロワー2.7万人、エヌケン|一生使えるお金の知識）、「資産運用」（okanno_chie、フォロワー3.7万人、えみこのお金の話|資産運用で豊かな生活）が並んでいる。"
    },
    {
        "index": 170,
        "filename": "image_29.png",
        "description": "ビジネススキル系インスタアカウント2つの事例。「エクセル」（riena.excel、フォロワー14.5万人、りえなのExcel|初心者OK!実務で使えるエクセル時短）、「仕事術」（officeworker_plus、フォロワー3.6万人、オフィスワーカー|夫婦でライフワークを楽しむメディア）が並んでいる。"
    },
    {
        "index": 171,
        "filename": "image_30.png",
        "description": "大学生向け勉強術・ライフハック系インスタアカウント2つの事例。「大学生の勉強術」（annpi_s、フォロワー9.5万人、あんぴ◉大学生の勉強垢、iPadと手帳で暮らしを彩る）、「大学生の勉強術」（college_lab、フォロワー1.4万人、大学生活LAB|大学生のお金・勉強・暮らし）が並んでいる。"
    },
    {
        "index": 172,
        "filename": "image_31.png",
        "description": "ハンドメイド・クリエイティブ系インスタアカウント3つの事例。「刺繍系」（bukicho_hitsuji、フォロワー10.7万人、おひつじ|初心者向けの簡単ハンドメイド）、「デザイン系」（happy_mechan、フォロワー4177人、めちゃん|iPad加工術とインスタデザインのこと）、「アプリ紹介」（marie_okawa、フォロワー2.6万人、マリエ|お役立ちアプリとiPhone便利ワザ）が並んでいる。"
    },
    {
        "index": 173,
        "filename": "image_32.png",
        "description": "「2023年インスタ攻略 バズる投稿作成方法 全SNSで活用可のテクニック」という紫色のバナー画像。インスタグラムだけでなく全SNSで応用できるバイラルコンテンツ作成手法を解説する記事への導線。"
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

    print(f"\n✓ Batch 144-173 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
