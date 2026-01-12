#!/usr/bin/env python3
"""
Batch 225-244の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 225-244の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 225,
        "filename": "image_23.png",
        "description": "化粧品の購入訴求を示すインフォグラフィック。緑色の強調ボックスで「訴求1」「特徴」「機能」「成分」「効果」を配置し、ピンク色の化粧品イラストと「この商品使ってておはだ綺麗になって個人的には愛用してる」というテキストボックスで訴求メッセージを表示。"
    },
    {
        "index": 226,
        "filename": "image_24.png",
        "description": "屑人性ありのインスタグラムアカウント紹介。サークル写真付きで「ひよ」というユーザーが「工撃な暮らしと美容男子」というテーマで、社会人3年目(24)の一人暮らし、一般男子が工撃な美容と暮らしを発信している点と、3500円以下の美容コスメ情報の訴求を表示。"
    },
    {
        "index": 227,
        "filename": "image_25.png",
        "description": "屑人性なしの情報メディアの事例紹介。左側に工撃ケテやメンズコスメ記事、ヘアテクニック、シャンプー関連情報、右側にニキビ対策記事や美容サロン情報を示すコンテンツグリッドで複数ジャンルの美容情報を提供する情報メディアのモデルを例示。"
    },
    {
        "index": 228,
        "filename": "image_26.jpg",
        "description": "SNSマーケティングの異なるアカウントタイプの比較。左にmarke_hakaseアカウント（投稿88件、フォロワー603人）の緑と黄色のブランド「SNSマーケの教科書」シリーズ商品紹介9点、右にしじみこれくしょん⌒@アカウント（投稿64件、フォロワー6722人）の美容関連投稿フィードを表示。"
    },
    {
        "index": 229,
        "filename": "image_27.jpg",
        "description": "2つのインスタグラムプロフィール比較。左は「sns_freelance_aya」アカウント（投稿87件、フォロワー581人）でデジタルクリエイターが育成情報を発信、右は「mii_insta02」アカウント（投稿18件、フォロワー1609人）でフリーランスサロンやカフェ運営情報をDM販売で展開。"
    },
    {
        "index": 230,
        "filename": "image_28.jpg",
        "description": "体型変化のダイエット成功事例。左側に「何やっても変わらなかった太眼-18cm」というテキストで、ビフォーアフター写真を表示し、右側に「キャプション」というタイトルで詳細なダイエット方法や工夫をまとめた紫色のボックスを表示。"
    },
    {
        "index": 231,
        "filename": "image_29.jpg",
        "description": "ダイエット成功の詳細説明。5つのセクション（太っていた苦しい悪癖、提僧のターミングボイント、話せん伝えたいこと、痩せるかもしれない辛い工夫、進めてくるのに合わせて構成）で、ダイエット中の心情、重要な転換点、実施した工夫、継続のコツを詳細に説明。"
    },
    {
        "index": 232,
        "filename": "image_30.jpg",
        "description": "ダイエット中の悩みと解決策のQ&A集。左側に「悩み」「解決策」として「なんでもどうぞ」「生理で太くなりました。」などの悩みと対策、右側に朝食、食事タイミング、代謝、糖質制限に関する詳細なアドバイスを表示。"
    },
    {
        "index": 233,
        "filename": "image_31.jpg",
        "description": "ダイエット継続のための食事管理アドバイス。コメント風の吹き出しで「朝食だらぶれている訳わかないのに朝食を何年もしていまし…」「基本に毎日眼食を取ると太やすくなるかどーーー」などのQ&Aで食事タイミングと体重管理の関係を説明。"
    },
    {
        "index": 234,
        "filename": "image_32.jpg",
        "description": "ダイエット相談のコメント集。複数のコメントユーザーが「生理で太くなりました。」「ダイエット中に何食べていいかわかりません」などの質問に対し、詳細な栄養管理やタイミングのアドバイスが記載されたQ&Aスクリーンショット。"
    },
    {
        "index": 235,
        "filename": "image_33.jpg",
        "description": "ダイエット継続のための心理的サポート。「朝食だらぶれている訳わかない…」「痩せるかもしれない辛い…」などのユーザーの葛藤を受け取り、継続のコツとして「糖質制限で痩せ落ち薬せにくい…」「夜8時以降の脂肪になりやすい…」などの知識を提供。"
    },
    {
        "index": 236,
        "filename": "image_34.jpg",
        "description": "ダイエット情報の詳細なコメント返答。複数のユーザーコメントに対して「そこに糖分を加えれば～」「夜は8時以降は脂肪に…」などの具体的な栄養知識と「皮下脂肪も糖質制限で落ちます」「落ちすぎよ！ただ注意点として…」などの詳細なアドバイスを提供。"
    },
    {
        "index": 237,
        "filename": "image_35.png",
        "description": "インスタグラムのアカウント設計における「インスタバズった事例紹介」というセクションタイトル。紫色のバナーに「インスタ尖った事例介紹」、「差別化されたコンセプト設計」、「コンセプト設計講座」というテーマが表示。"
    },
    {
        "index": 238,
        "filename": "image_36.png",
        "description": "インスタグラムのマネタイズ事例を紹介するセクション。黄色いバナーに「SNSのマネタイズ事例」「DMで商品を売る施策例」「僕の成功事例紹介」というテーマで、複数のマネタイズ方法を紹介。"
    },
    {
        "index": 239,
        "filename": "image_37.png",
        "description": "インスタで稼げるジャンルを紹介するセクションタイトル。赤色のバナーに「インスタ2023年伸びてるアカウント」「伸びてるジャンルと収益方法」「アカウント10選とマネタイズ施策」というテーマが表示。"
    },
    {
        "index": 240,
        "filename": "image_38.png",
        "description": "フォロワー増加戦略を紹介するセクションタイトル。青色のバナーに「フォロワー増加の10施策」「外部導導でフォロワー爆伸び」「インスタとTwitter」「フォロワー伸びた成功事例紹介」というテーマで複数の成長戦略を紹介。"
    },
    {
        "index": 241,
        "filename": "image_39.png",
        "description": "インスタ子育てジャンルのコンセプト紹介セクション。紫色のバナーに「インスタ子育てジャンル」「上手なコンセプトアカ例」「コンセプト設計」というテーマで、子育て関連アカウントのコンセプト設計方法を紹介。"
    },
    {
        "index": 242,
        "filename": "image_40.png",
        "description": "月100万円稼げるジャンル紹介セクション。黄色いバナーに「インスタで稼げるジャンル」「月100万円狙えるジャンル」「マネタイズ戦略を共有」というテーマで、高収益ジャンルの紹介とマネタイズ方法を表示。"
    },
    {
        "index": 243,
        "filename": "image_01.png",
        "description": "インスタグラムのマネタイズ方法を視覚的に表示するインフォグラフィック。「マネタイズの種類」というタイトルで、アフィ（オレンジ）、コンサル（紺）、note（ミント）、サロン（赤ピンク）の4つのマネタイズ方法を異なるカラーのラベルとアイコン（プレゼント箱、ビジネスウーマン、ノート、人のアイコン）で表示。"
    },
    {
        "index": 244,
        "filename": "image_02.png",
        "description": "3つのインスタグラムジャンル選択のコンセプト紹介。左側に「ジャンル選び」「ジャンル選びの3つのチェック」「SNSのマーケティング」というテーマ、右側に「プロフィール設定」「ジャンル別の立ち位置」「フォロワー層の設定」というテーマで、ジャンル選定の重要なポイントを示す3つのセクションで構成。"
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

    print(f"\n✓ Batch 225-244 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
