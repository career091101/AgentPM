#!/usr/bin/env python3
"""
Batch 205-224の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 205-224の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 205,
        "filename": "image_03.jpg",
        "description": "インスタグラムアカウント「zatsugaku_iincho」のプロフィール画面。投稿341件、フォロワー4.6万人。「つい自慢したくなる雑学」というバイオで、様々なジャンルの雑学投稿を発信している。下部には雑学記事のサムネイルと、アカウント設計の方針「発信者の個人情報や特徴」「価値」「投稿の発信内容」の3つのポイントを示す図が表示されている。"
    },
    {
        "index": 206,
        "filename": "image_04.jpg",
        "description": "左側は「a____home_」というアカウント(@_____home_)で、投稿527件、フォロワー27.9万人の女性が「仕事と暮らしを丁寧に」というテーマで発信している様子。右側には同じアカウントの投稿内容パターンとして、企業OLの平日服コーディネート6選やファッション・インテリアに関する投稿を紹介している。"
    },
    {
        "index": 207,
        "filename": "image_05.jpg",
        "description": "無印化粧品のおすすめをテーマにした図解。中央に女性の顔があり、オレンジ・赤・青の3色のアイコンで、異なるペルソナが「無印化粧品おすすめ」という同じ商品について、どのような特徴に着目しているかを示している。複数の視点から商品価値を提示するアカウント設計を表現している。"
    },
    {
        "index": 208,
        "filename": "image_06.jpg",
        "description": "ビジネススーツを着た女性の横顔イラスト。黒い髪、白い顔、紺色のビジネススーツに赤いネクタイが特徴。プロフェッショナルで知識豊富な人物というイメージを表現した、アカウント設計の「発信者の特徴」を示すイメージ画像。"
    },
    {
        "index": 209,
        "filename": "image_07.jpg",
        "description": "イラストキャラクターの女性の顔がアップで描かれている。金髪のウェーブヘア、大きな瞳、可愛らしい表情が特徴。アカウント設計のキャラクター作成例を示すファッションやメイク関連のアカウント向けイメージキャラクター。"
    },
    {
        "index": 210,
        "filename": "image_08.jpg",
        "description": "複数のアカウント事例を掲載。左は「a_____home_」で紺色シャツを着たコーディネート提案、右側は「ayami_room」のアカウントから好きなものに関する写真や、iPhoneの容量を増やす神アイテム、ぐっすり眠れる極上マットレス、おしゃれなリングの付け方など、ライフスタイル・インテリア関連の投稿内容が表示されている。"
    },
    {
        "index": 211,
        "filename": "image_09.jpg",
        "description": "イラストキャラクターの女性の顔。金髪のウェーブヘア、大きな瞳、可愛らしい笑顔。アカウント設計で使用するキャラクター表現の例。"
    },
    {
        "index": 212,
        "filename": "image_10.jpg",
        "description": "紹介文「一人暮らし男子」と同名アカウント「hiyo_101211」のコンテンツ紹介。複数の投稿スクリーンショットで、「当番のこと教えます」「美容部員の姉に学んだ美容の裏技」「意外と見られる手の清潔感をバクあげ法」「3500円以下コスパ最強のBBクリーム7選」などの投稿が表示されている。男性向けの美容・生活スタイル情報を提供するアカウント設計の例。"
    },
    {
        "index": 213,
        "filename": "image_11.jpg",
        "description": "イラストキャラクターの女性の顔。黒髪のまとめ髪、大きな瞳、可愛らしい表情で、ビジネス女性というテーマを表現したアカウント設計用キャラクター画像。"
    },
    {
        "index": 214,
        "filename": "image_12.jpg",
        "description": "アカウント「nken_second」のコンテンツを掲載。「一人暮らし不要なもの9〜10位」「フォロワーさんに聞いた一人暮らしで不要なもの18〜10位」のスクリーンショットと、子育て向けブログ・書籍も紹介されている。ミニマリスト向けの生活効率化情報を発信するアカウント設計。"
    },
    {
        "index": 215,
        "filename": "image_13.jpg",
        "description": "フォロワー18万人のアカウント「yoama_official」の投稿コンテンツ集。掲載されたタイトルは「担いしたくない無いいア」「8月は楽天市場注意」「2022年上半期買ってよかった8選」「娘が気になる激安商品7選」「今月最後のおむつ激安」などで、激安商品・掘り出し物の紹介をテーマとしたアカウント設計を表現している。"
    },
    {
        "index": 216,
        "filename": "image_14.jpg",
        "description": "フォロワー30万人のアカウント「purin_chan_」の投稿コンテンツ集。キャラクター描き方教室、アニメ・キャラクター関連（クレヨンしんちゃん、ポケモン、SPY×FAMILY）のイラスト教室、わんわんアニメ描き方、イラスト教科書などを紹介。子ども向けのイラスト描き方教育コンテンツを発信するアカウント設計。"
    },
    {
        "index": 217,
        "filename": "image_15.jpg",
        "description": "フォロワー17万人のアカウント「woolieart」の投稿コンテンツ集。羊毛フェルト・刺繍・DIY手芸関連の教室と、かわいい刺繍デザイン、T-シャツDIY、大きなリボンの刺繍方法などの手工芸クラフト情報を発信しているアカウント設計。"
    },
    {
        "index": 218,
        "filename": "image_16.jpg",
        "description": "イラストキャラクターの女性の顔。金髪のウェーブヘア、大きな瞳、優しい笑顔で、親しみやすい女性というイメージを表現したアカウント設計用キャラクター。"
    },
    {
        "index": 219,
        "filename": "image_17.png",
        "description": "イラストキャラクターの女性の顔。金髪のウェーブヘア、大きな瞳、可愛らしい笑顔。アカウント設計で使用するキャラクター表現の汎用例。"
    },
    {
        "index": 220,
        "filename": "image_18.png",
        "description": "イラストキャラクターの女性の顔。黒髪のまとめ髪、大きな瞳、優しい笑顔で、親切で信頼できる女性というイメージを表現したアカウント設計用キャラクター。"
    },
    {
        "index": 221,
        "filename": "image_19.png",
        "description": "イラストキャラクターの女性の顔。金髪のウェーブヘア、大きな瞳、可愛らしい表情で、フレンドリーで親しみやすい印象を与えるアカウント設計用キャラクター。"
    },
    {
        "index": 222,
        "filename": "image_20.jpg",
        "description": "イラストキャラクターの女性の顔。黒髪のボブヘア、大きな瞳、優しい笑顔で、親切で頼りになる女性というイメージを表現したアカウント設計用キャラクター。"
    },
    {
        "index": 223,
        "filename": "image_21.jpg",
        "description": "イラストキャラクターの女性の顔。茶色のウェーブヘア、大きな瞳、可愛らしい表情。アカウント設計のキャラクター表現例として、フレンドリーで親しみやすい女性のイメージを表現している。"
    },
    {
        "index": 224,
        "filename": "image_22.jpg",
        "description": "イラストキャラクターの女性の顔。黒髪のストレートヘア、大きな瞳、落ち着いた表情で、真面目で信頼できる女性というイメージを表現したアカウント設計用キャラクター。"
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

    print(f"\n✓ Batch 205-224 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
