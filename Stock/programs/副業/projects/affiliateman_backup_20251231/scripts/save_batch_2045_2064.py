#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2045, "filename": "image_08.png", "description": "TikTok動画のファーストビュー最適化についての説明スライド。開始1秒のインパクト有無によって、視聴者が動画を最後まで見るか離脱するかが決まることを示した図解。"},
    {"index": 2046, "filename": "image_01.png", "description": "TikTok運用におけるバズるコンテンツの特徴と商品紹介アカウント戦略についてのスライド。「商品紹介アカで無双する」「飽きられない最強のテーマ」という2つのポイントを強調した目次画像。"},
    {"index": 2047, "filename": "image_02.jpg", "description": "ビジネススーツ姿の男性イラストを使用した、TikTok運用ガイドのキャラクター表現。プロフェッショナルな印象を与える人物アイコン。"},
    {"index": 2048, "filename": "image_03.png", "description": "動画の開始1秒における視聴者の反応を示す図表。目の大きさの強調で「インパクトなし」では離脱、「インパクトあり」では続き見るという2つのシナリオを比較。"},
    {"index": 2049, "filename": "image_04.png", "description": "TikTokでバズる動画例についての説明スライド。バズを生み出す動画構成におけるファーストビューの重要性を強調した、ロケット型のアイコンを使ったメインビジュアル。"},
    {"index": 2050, "filename": "image_05.png", "description": "2023年TikTok攻略における稼げるジャンル選定についての目次。金貨のアイコンと「稼げるおすすめジャンル」「ジャンル選定の理解」というテーマを掲載したスライド。"},
    {"index": 2051, "filename": "image_06.png", "description": "2023年TikTok攻略のフォロワー伸ばし方についての説明スライド。「1万人フォロワー目指そう」というターゲットを掲げ、成長戦略についての目次を示した画像。"},
    {"index": 2052, "filename": "image_01.png", "description": "TikTok伸びているおすすめジャンルまとめの記事タイトルスライド。金貨のアイコンと「2023年TikTok攻略」「稼げるおすすめジャンル」「ジャンル選定の理解」という3つのテーマを配置したメインビジュアル。"},
    {"index": 2053, "filename": "image_02.jpg", "description": "美容・コスメ関連のTikTokアカウント（@yami_yomichan）のスクリーンショット。スキンケア製品やメイク動画、食べ物などの関連コンテンツを投稿しているアカウントのグリッド表示。"},
    {"index": 2054, "filename": "image_03.png", "description": "ゴルフ関連のTikTokアカウント（yosshii.golf）のスクリーンショット。ゴルフレッスンやスイングテクニック、フレッシュネスについての動画を複数投稿しているアカウント。"},
    {"index": 2055, "filename": "image_04.png", "description": "食べ物レビューのTikTokアカウント（hagime-oyameri）のスクリーンショット。様々な食べ物について「〜これ！」などのキャッチフレーズ付きレビュー動画を投稿しているアカウント。"},
    {"index": 2056, "filename": "image_05.png", "description": "ガジェット・家電紹介のTikTokアカウント（gadgetomo）のスクリーンショット。新製品や便利グッズについての紹介動画を複数投稿しているアカウント。"},
    {"index": 2057, "filename": "image_06.png", "description": "転職・キャリアコンサルティングのTikTokアカウント（kuroki_ls）のスクリーンショット。転職ノウハウやキャリア相談について、黄色いテロップ付きで解説している動画アカウント。"},
    {"index": 2058, "filename": "image_07.png", "description": "女性向け起業・転職関連のTikTokアカウント（meganetensyoku）のスクリーンショット。転職活動や職業選択についての悩み相談やアドバイス動画を投稿しているアカウント。"},
    {"index": 2059, "filename": "image_08.png", "description": "食べ物紹介系のTikTokアカウント（mika0777）のスクリーンショット。様々な飲食店や食品についての紹介・レビュー動画を投稿しているアカウント。"},
    {"index": 2060, "filename": "image_09.png", "description": "暮らし・家事についてのTikTokアカウント（fuka.kurashi）のスクリーンショット。掃除、整理整頓、生活用品の使い方についての実践的な動画を投稿しているアカウント。"},
    {"index": 2061, "filename": "image_10.png", "description": "グルメ・飲食店紹介のTikTokアカウント（tokyo_foods）のスクリーンショット。東京の飲食店やメニューについての紹介動画を複数投稿しているアカウント。"},
    {"index": 2062, "filename": "image_11.png", "description": "旅行・観光地紹介のTikTokアカウント（neo.travelers）のスクリーンショット。全国の観光スポットや旅行先についての紹介動画を投稿しているアカウント。"},
    {"index": 2063, "filename": "image_12.png", "description": "キャッチコピーやテロップ効果を活用した複数ジャンルのTikTok動画サムネイルのグリッド表示。ビジネス、グルメ、旅行など様々なテーマの視聴者層を引き付ける動画のコレクション。"},
    {"index": 2064, "filename": "image_13.png", "description": "複数のTikTokアカウントが投稿した人気動画のサムネイルグリッド。グルメ、旅行、ライフスタイルなど多様なジャンルでバズった動画の集合表示。"},
]

def is_auto_generated(desc):
    patterns = [
        "インスタグラム運用に関する",
        "説明画像または投稿サムネイル",
        "運用に関する説明画像",
        "投稿用のサムネイル",
        "記事のバナー画像またはメインビジュアル",
        "関連コンテンツ",
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

    print(f"\n✓ Batch 2045-2064 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
