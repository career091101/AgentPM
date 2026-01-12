#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2005, "filename": "image_14.png", "description": "Twitter運用ツール解説。Canva、デザイン研究所、Excelなど、SNS投稿作成に使える3つのツール（CANVA、デザイン、エクセル）を比較した図解。"},
    {"index": 2006, "filename": "image_15.png", "description": "書籍紹介の図解。毎週本を紹介するTwitterアカウント2つと読書で人生が豊かになるテーマのアカウント事例を表示。"},
    {"index": 2007, "filename": "image_16.png", "description": "資産運用ジャンルの稼ぎ方解説。ポイ活（FX的なアカウント）と資産運用（ネオキングボイなど）の2つのジャンルの成功アカウント例を紹介。"},
    {"index": 2008, "filename": "image_17.png", "description": "Twitterフォロワー増加戦略を示すバナー。外部誘導でフォロワー爆伸び、インスタ×Twitter、フォロワーが伸びた成功事例紹介の3つのポイント。"},
    {"index": 2009, "filename": "image_18.png", "description": "Twitter商品販売戦略の紹介。少ないフォロワー（月100万稼げる）でマネタイズできる方法を、KくんとコンサルX営業という2つのキャラで説明。"},
    {"index": 2010, "filename": "image_19.png", "description": "SNSマネタイズ事例の図解。DMで商品を売る施策例と、僕の成功事例紹介（黄色背景）で、DM営業による売上創出方法を説明。"},
    {"index": 2011, "filename": "image_20.png", "description": "超売れるツイート10選の説明。商品が売れる投稿パターン、note/アフィ/コンサルが売れるツイートの型を10選で紹介する青系バナー。"},
    {"index": 2012, "filename": "image_21.png", "description": "Twitterバズ戦略完全版の告知。1日で4000人フォロワー増加を実現したツイート戦略を特別公開するという、黒背景の派手なプロモーション画像。"},
    {"index": 2013, "filename": "image_22.png", "description": "2023年Twitter攻略フォロワー伸ばし方のタイトルバナー。1万人フォロワー目指そうというターゲットを設定し、青系デザインで視認性を確保。"},
    {"index": 2014, "filename": "image_01.png", "description": "Twitter/TikTokに関する質問回答まとめの紹介バナー。2022年7-9月分の質問を集約したコンテンツで、色付きの質問マークが視認性を高める紫系デザイン。"},
    {"index": 2015, "filename": "image_02.png", "description": "Twitter悩み系投稿の解決策図解。男の体目当てという悩みから、悩み解決法として誘導し、体だけでなく愛される彼女になるためのnote販売を説明する画像。"},
    {"index": 2016, "filename": "image_03.png", "description": "TikTokアフィリエイトプロジェクト案内の画面キャプチャ。無料記事導読・2無料記事教育・3有料商品伏線・4発売前の煽りという4つのステップを赤文字で強調。"},
    {"index": 2017, "filename": "image_04.png", "description": "TikTokアフィリエイト商品販売戦略の説明。初回10部半額で希少性を出し、10部が売り切れている過程を共有して購買意欲を上げるというセールス戦略図解。"},
    {"index": 2018, "filename": "image_05.png", "description": "メンズコスメジャンルのTikTok投稿画像。複数のコスメ動画とメンズコスメ関連のTikTok投稿をスクリーンショット形式で表示した参考事例。"},
    {"index": 2019, "filename": "image_06.jpg", "description": "女性キャラクターのシンプルなアニメ風イラスト。金髪で青いドレスを着た、親しみやすいデザインのアバター画像。"},
    {"index": 2020, "filename": "image_07.png", "description": "SNS攻略サロン限定の11月質疑回答まとめバナー。インスタ/TIKTOK/Twitterの3プラットフォーム対応の質問集約コンテンツを青系デザインで表現。"},
    {"index": 2021, "filename": "image_08.png", "description": "Instagramに関する質問回答まとめのタイトルバナー。2022年7-9月分の質問をまとめたコンテンツで、紫系背景に質問マークを配置した視認性高いデザイン。"},
    {"index": 2022, "filename": "image_09.png", "description": "SNS有益情報公開・役立つ情報タイトルの説明バナー。2022年7-9月分のSNS運用情報をまとめたコンテンツで、紫背景に宇宙系アイコンで視認性確保。"},
    {"index": 2023, "filename": "image_10.png", "description": "Instagram/Twitter/TikTok質問回答まとめのバナー。2022年10月分の複数SNS質問を集約した参考資料で、紫系背景に色付き質問マークを配置。"},
    {"index": 2024, "filename": "image_11.png", "description": "空白/シンプルなプレースホルダー画像。装飾や文字がない空白のグラフィック。"}
]

def is_auto_generated(desc):
    patterns = [
        "インスタグラム運用に関する",
        "説明画像または投稿サムネイル",
        "運用に関する説明画像",
        "投稿用のサムネイル",
    ]
    return any(p in desc for p in patterns)

def update_inventory_with_descriptions(batch_descriptions):
    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'

    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {desc['filename']}: 説明更新")

    completed = sum(1 for item in inventory if not is_auto_generated(item.get('description', '')))
    total = len(inventory)
    remaining = total - completed
    percentage = (completed / total) * 100

    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Batch 2005-2024 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
