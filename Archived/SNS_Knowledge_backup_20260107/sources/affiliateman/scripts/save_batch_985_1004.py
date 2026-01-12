#!/usr/bin/env python3
"""
Batch 985-1004の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 985-1004の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 985,
        "filename": "image_161.png",
        "description": "KKさんの初期の質問投稿。月額2980円と29800円での売上目標の違いについて質問し、有名な情報数と皆さんへの濃密な回答をサロンメンバーに共有している。"
    },
    {
        "index": 986,
        "filename": "image_162.png",
        "description": "KKさんの回答。Twitter投稿の黄金時間が20時～21時であることを説明し、投稿のいいねの伸びやすさを検討する重要性を述べている。"
    },
    {
        "index": 987,
        "filename": "image_163.png",
        "description": "KK社による投稿タイミングと戦略に関するアドバイス。フォロワー企画でのCDM活用やBANリスク、プロフィールへのリンク設置方法など複数の質問に対応している。"
    },
    {
        "index": 988,
        "filename": "image_164.png",
        "description": "ななか氏からのコンテンツ販売とTwitter活用に関する質問。動画制作での行動や手段選びについて相談し、TikTokとインスタのショート動画施策の違いについて議論している。"
    },
    {
        "index": 989,
        "filename": "image_165.png",
        "description": "ひなた氏からのAI占いサイト拡散方法と広告に関する3つの質問。Twitter、サロンの拡散依頼、占いアカウント拡散依頼、広告について具体的なアドバイスを求めている。"
    },
    {
        "index": 990,
        "filename": "image_166.png",
        "description": "KKさんからのアドバイス。サービス作成背景とchatGPT活用、マネタイズポイント（アドセンス・ASP案件・楽天アフィ・LINE誘導）についての戦略説明。"
    },
    {
        "index": 991,
        "filename": "image_167.png",
        "description": "びよ氏からのセドリ系発信に関する質問。毎日ツイート10本、月1くらいで企画ツイート、LINE誘導でコンサル売却を検討している状況を述べている。"
    },
    {
        "index": 992,
        "filename": "image_168.png",
        "description": "KK社による回答。ビジネス系アカウント戦略について、アドセンスやASP案件、楽天アフィ、LINE誘導でのマネタイズ方法を詳細に説明している。"
    },
    {
        "index": 993,
        "filename": "image_169.png",
        "description": "たろー氏からの転職系ブログのSNS集客戦略に関する相談。現在100記事の転職ブログでSNS集客を模索し、残念ながら順位が落ちたため施策相談をしている。"
    },
    {
        "index": 994,
        "filename": "image_170.png",
        "description": "KK社による詳しい回答とアドバイス。転職系ブログの成功アカウント事例紹介と、インスタ活用によるcupcutでのショート動画作成やマネタイズ戦略を提案している。"
    },
    {
        "index": 995,
        "filename": "image_171.png",
        "description": "ぼみお氏からのTwitter恋愛系発信とフォロワー伸び悩みに関する相談。現在2000インプで500フォロワーしかいない状況への改善策を求めている。"
    },
    {
        "index": 996,
        "filename": "image_172.png",
        "description": "よしみ氏からの飲食店OEMカビ取り剤販売とTikTok運用に関する質問。ディリスオーヤマのペンテーク活用やTikTok・楽天での販売方法を相談している。"
    },
    {
        "index": 997,
        "filename": "image_173.png",
        "description": "ST氏からの月額変動に関する質問。2月からTikTokでフォロワー数が急増している理由がアルゴリズム変化なのか、エンゲージメント低下が原因なのかを質問している。"
    },
    {
        "index": 998,
        "filename": "image_174.png",
        "description": "吉田氏からのアフィリエイト戦略に関する5つの質問。noteやプレインを購入してアフィリエイトする際の注意点や、TikTok・Twitter連動でのマネタイズ方法を相談している。"
    },
    {
        "index": 999,
        "filename": "image_175.png",
        "description": "KK社によるアフィリエイトコンサル戦略の詳しい説明。noteの活用、ブランディング、高額コンサル売却のコツ、SNSマネタイズ手法について複数の事例と共に解説している。"
    },
    {
        "index": 1000,
        "filename": "image_176.png",
        "description": "こうき氏からの新規SNSアカウント立ち上げとジャンル選定に関する相談。YouTube、FX仮想通貨なども検討中で、SNS集客とビジネス系ジャンル参入について悩んでいる。"
    },
    {
        "index": 1001,
        "filename": "image_177.png",
        "description": "KK社によるビジネス系アカウント戦略のアドバイス。Twitterが最適であることを説明し、マネタイズはサロンやnoteといった具体的な施策を提案している。"
    },
    {
        "index": 1002,
        "filename": "image_178.png",
        "description": "たろー氏からの転職・恋愛系ブログのSNS流入と相談。SNS集客に関する戦略相談やフォロワー増加施策、アフィリエイト売上確保方法について質問している。"
    },
    {
        "index": 1003,
        "filename": "image_179.png",
        "description": "KK社による詳しい回答。ビジネス系参入とジャンル選定アドバイス、SNS流入対策と相談におけるフォロワー数別の対応戦略を説明している。"
    },
    {
        "index": 1004,
        "filename": "image_180.png",
        "description": "KK社による最終的なアドバイス。出会い系のセルフ作成困難さとアダルト色への配慮、招数調査とフォロワー施策の重要性を述べている。"
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

    print(f"\n✓ Batch 985-1004 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
