#!/usr/bin/env python3
"""
Batch 1305-1324の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1305-1324の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1305,
        "filename": "image_125.png",
        "description": "K君からの返信メッセージ。月100安定して稼ぐためのコンサル・note・アフィリエイト・オンラインサロン運営についての詳細な戦略説明。サロン収益性とコンサル単価の設定方法についても言及。"
    },
    {
        "index": 1306,
        "filename": "image_126.png",
        "description": "すや（ユーザー名）からのメッセージ。やはり単価上げ方法についての質問に対し、フロント購入者リストへのバックエンド販売戦略と別商品との組み合わせマネタイズ方法の提案。"
    },
    {
        "index": 1307,
        "filename": "image_127.png",
        "description": "ざい（ユーザー名）からの新規質問。エンジニアのマネタイズ方法について複数の選択肢（コンサル・転職/副業アフィ・自身で副業・販売・セミナー/講習）を提示し、マネタイズ方法の相談。"
    },
    {
        "index": 1308,
        "filename": "image_128.png",
        "description": "K君からざいへの返信。プログラミング教材（Skill Hacks）紹介、完全初心者からプログラミング習得可能性、10-15万円の費用と収入見込みについての詳細説明。"
    },
    {
        "index": 1309,
        "filename": "image_129.png",
        "description": "しろくち（ユーザー名）からの相談。エンジニアアカウント・複数アカウント運用・ジャンル選択について相談。最新AIやSier勤務の利点と副業スキルについての質問。"
    },
    {
        "index": 1310,
        "filename": "image_130.png",
        "description": "K君からしろくちへの返信。プログラミング教材Skill Hacksの説明、完全初心者向けカリキュラム、Webアプリ開発方法、1MB以下のサイズについての詳細説明。"
    },
    {
        "index": 1311,
        "filename": "image_131.png",
        "description": "マーティ（ユーザー名）からの質問。Instagramのマネタイズについて、アカウントの現状（投稿ストーリーなし）、LPデザイン・Kindleキー・noteなどフロント商品についての相談。"
    },
    {
        "index": 1312,
        "filename": "image_132.png",
        "description": "K君からマーティへの返信。ファン化戦略、LP/副作の必要性、モニターやセミナー開催によるコミュ実績構築、実績不足の初心者向けアドバイス。"
    },
    {
        "index": 1313,
        "filename": "image_133.png",
        "description": "恋愛TikTokerからの相談。Instagram（ハイライト）での美容アフィについて困惑、以前ハイアグラについて質問（DMで回答済み）、アフターピルの訴求方法について。"
    },
    {
        "index": 1314,
        "filename": "image_134.png",
        "description": "K君からのアフターピル訴求返信。コンドーム破裂時の72時間以内対応、99%避妊率、リスク管理と病院対応についての詳細な医学的説明と避妊方法の戦略提案。"
    },
    {
        "index": 1315,
        "filename": "image_135.png",
        "description": "さいい（ユーザー名）からの新規相談。恋愛系ジャンル、ナンパマッチングアプリについて、K君がフォローしていた男性ユーザーについて質問し、戦略確認を求めている。"
    },
    {
        "index": 1316,
        "filename": "image_136.png",
        "description": "K君からさいいへの返信。ナンパ界隈のコンサル・tips販売、アプリのアフィについて、ナンパアプリもマネタイズできることを説明。"
    },
    {
        "index": 1317,
        "filename": "image_137.png",
        "description": "りく（ユーザー名）からの相談。ブログ・Webライター・複数ジャンル運用についてのマネタイズ方法質問。Webライターの将来性（継続性と単価の上限）についての懸念。"
    },
    {
        "index": 1318,
        "filename": "image_138.png",
        "description": "K君からりくへの返信。SNS×プロジャンル（マネタイズ・ドメインサーバー・アフィ・note・コンサル）とWebライタージャンル（マネタイズ・note・コンサル）の2つの戦略比較説明。"
    },
    {
        "index": 1319,
        "filename": "image_139.png",
        "description": "りく（さらに詳細質問）からの追加相談。SNS×ブログ・副業との両立、フォロワー7000人でのマッチングアプリ活用、サロン・LINE認証・LINE事前についての質問。"
    },
    {
        "index": 1320,
        "filename": "image_140.png",
        "description": "K君からりくへの詳細返信。資産運用系（LINE証券・WLAZZ ASPI）の説明、LINE認証コード4000円程度、WLAZZ ASPの詳細説明、Blogサイト登録戦略についての回答。"
    },
    {
        "index": 1321,
        "filename": "image_142.png",
        "description": "りっか（ユーザー名）からの相談。ボイ法・Amazon・Amazonアフェについての複数マネタイズ質問、K君のアカウント活用方法の確認、LINE認証・ASP位置について。"
    },
    {
        "index": 1322,
        "filename": "image_143.png",
        "description": "K君からりっかへの返信。資産運用系案件の推奨（LINE証券・WLAZZ ASPI）、LINE認証コード4000円程度のおすすめ説明、同様な初心者向けコンサルティング回答。"
    },
    {
        "index": 1323,
        "filename": "image_01.png",
        "description": "K君のアウトプット情報バナー。青と白の配色で「K君のアウトプット」「SNS攻略に役立つ知識」「2022年11月号まとめ」と記載。キャラクターイラスト付き。"
    },
    {
        "index": 1324,
        "filename": "image_02.png",
        "description": "SNS運用情報バナー。紫色背景で「SNS運用 超役立つ情報」「SNS運用知識まとめ」「【2022年10月分】」と記載。地球と人物キャラクターのイラスト付き。"
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

    print(f"\n✓ Batch 1305-1324 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
