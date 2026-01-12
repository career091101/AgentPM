#!/usr/bin/env python3
"""
Batch 1465-1484の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1465-1484の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1465,
        "filename": "image_18.png",
        "description": "インスタグラムのDMスレッド。ユーザー「DD」がインスタのジャンル選定についての質問をしており、Notionアカウント設定やビジネススキル系の発信に関する提案が記載されている。"
    },
    {
        "index": 1466,
        "filename": "image_19.png",
        "description": "Voicy音声プラットフォームの紹介。「KくんのSNS攻略『くんのSNS攻略ラジオ』」というコンテンツの詳細説明画像。300万人のフォロワーを持つSNS攻略サロン等の情報が掲載されている。"
    },
    {
        "index": 1467,
        "filename": "image_20.png",
        "description": "ユーザー「ささみ」からのDMでダイエットジャンルの100日チャレンジについての質問と、KくんからのTwitterまたはInstagramでのスタート方法の回答。"
    },
    {
        "index": 1468,
        "filename": "image_21.png",
        "description": "ユーザー「しゅう」からの「いいね数・保存率改善施策」についての質問。Instagramのフィード投稿の分析データ（リーチ11,111、フォロー数の増減内訳）が含まれている。"
    },
    {
        "index": 1469,
        "filename": "image_22.png",
        "description": "ユーザー「しゅう」への返答。投稿の質と関連性、テーマ選択の重要性、Instagramストーリーズの活用についてKくんからのアドバイスが記載されている。"
    },
    {
        "index": 1470,
        "filename": "image_23.png",
        "description": "ユーザー「クラシブ」からの複数件のDM。7月のzoomコンサルで恋愛系Instagramアカウント運用について相談、ブログ記事の作成についての質問が含まれている。"
    },
    {
        "index": 1471,
        "filename": "image_24.png",
        "description": "Kくんの返答メッセージ。女性ターゲットなら恋愛ジャンル選定が重要、Tiktokとブログの役割分担、記事作成時の留意点についてのアドバイスが記載されている。"
    },
    {
        "index": 1472,
        "filename": "image_25.png",
        "description": "Kくんから「クラシブ」への詳細なコンサル返答。勉強法の実装方法（Youtube活用、TikTok戦略、恋愛ジャンルのコンテンツ構成）についての具体的なガイダンス。"
    },
    {
        "index": 1473,
        "filename": "image_26.png",
        "description": "ユーザー「おさく」からの複数質問。レシピ系アカウントのマネタイズ方法、フォロワー増加施策についての相談。Instagramプロフィールのアクセス数等のデータも含まれている。"
    },
    {
        "index": 1474,
        "filename": "image_27.png",
        "description": "Kくんの返答とその後の補足。Instagramプロフィールへのアクセス数が少ない場合のジャンル選定重要性、マネタイズの具体的手段（アフィリエイト等）についての説明。"
    },
    {
        "index": 1475,
        "filename": "image_28.png",
        "description": "ユーザー「りーしぇ」へのKくんの返答。NFT×AI発信についての具体的施策。リリース再生数が伸びない要因分析と改善方法（ChatGPT利用、タイトル選定等）についての提案。"
    },
    {
        "index": 1476,
        "filename": "image_29.png",
        "description": "ユーザー「ai」からのLINE×エルステップ導入についての相談。LINE公式アカウント×エルステップの構築受注をゴールにしたInstagram導入提案が記載されている。"
    },
    {
        "index": 1477,
        "filename": "image_30.png",
        "description": "ユーザー「ai」へのKくんのYoutube活用アドバイス。マインドマップやスライド作成支援、フォロワー1,000人程度での商品販売可能性についての具体的なガイダンス。"
    },
    {
        "index": 1478,
        "filename": "image_31.png",
        "description": "ユーザー「Coco」からの複数質問。SNS初心者向けインスタアカウント設計、Canvaのデザイン選定、アフィリエイト教材の詳細についての相談が記載されている。"
    },
    {
        "index": 1479,
        "filename": "image_32.png",
        "description": "Kくんの返答。Canvaの無料テンプレート活用、デザインスクール活用、アフィリエイトビジネス構築のためのCANVA活用ツール紹介が含まれている。"
    },
    {
        "index": 1480,
        "filename": "image_33.png",
        "description": "ユーザー「Coco」へのフォローアップ。Canvas設計完了の報告とKくんからの発信軸としてユーザーがくるのか理想的か確認するための返答メッセージ。"
    },
    {
        "index": 1481,
        "filename": "image_34.png",
        "description": "ユーザー「めぬ」からの複数質問。Instagramからのコンテンツ販売、Note×Brain×Tipsの選択肢、販売ロードマップについてのアドバイス要請が記載されている。"
    },
    {
        "index": 1482,
        "filename": "image_35.png",
        "description": "Kくんの返答。Note→Brain→Tipsの段階的売却戦略、tipsの利用規約、Brain見つかることの難しさについての詳細なガイダンスが記載されている。"
    },
    {
        "index": 1483,
        "filename": "image_36.png",
        "description": "ユーザー「青山ボカレ」からの複数相談。Noteを使った恋愛系の無料部分と購買意欲形成についての質問が記載されている。"
    },
    {
        "index": 1484,
        "filename": "image_37.png",
        "description": "Kくんの返答。Istepという自動配布ツール、ビフォーアフター系ノートの無料部分活用法、サーバーアフィリの実装についての具体的なガイダンス。"
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

    print(f"\n✓ Batch 1465-1484 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
