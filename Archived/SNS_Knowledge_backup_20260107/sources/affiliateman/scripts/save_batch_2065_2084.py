#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2065, "filename": "image_14.png", "description": "紅葉の風景や動物、花のクローズアップなど四季の自然風景を集めたコラージュ画像。"},
    {"index": 2066, "filename": "image_15.png", "description": "TikTokアカウント「jgtakeizu」のプロフィール画面とその投稿コンテンツの一覧表示。"},
    {"index": 2067, "filename": "image_16.png", "description": "TikTokアカウント「iyupi___.20_」のプロフィール画面と、テキスト入りの動画コンテンツ一覧。"},
    {"index": 2068, "filename": "image_17.png", "description": "「naotaro_lifehack」というApple・PC関連情報発信のTikTokアカウントのプロフィール及び動画ライブラリ。"},
    {"index": 2069, "filename": "image_18.png", "description": "「mesico_japan」という美髪・髪型情報を発信するTikTokアカウントのプロフィール及びコンテンツ一覧。"},
    {"index": 2070, "filename": "image_19.png", "description": "香水・美容系コンテンツを発信する「coloria_magazine」のTikTokアカウント画面とコンテンツの動画サムネイル。"},
    {"index": 2071, "filename": "image_20.png", "description": "「kaiketsux」というメンズ美容情報アカウントのTikTokプロフィール及び動画コンテンツ一覧。"},
    {"index": 2072, "filename": "image_21.png", "description": "「tsubasa_kyoduka」というダイエット食事指導アカウントのTikTokプロフィール及び料理動画コンテンツ一覧。"},
    {"index": 2073, "filename": "image_22.png", "description": "「TIKTOKバズる特徴」というテキストとロケットアイコンを背景に「商品紹介アカで無双する」と「飽きられない最強のテーマ」を説明する図解。"},
    {"index": 2074, "filename": "image_23.png", "description": "「TIKTOKバズる動画例」というテキストの下に「バズを生み出す動画構成」と「ファーストビューの重要性」を説明する図解。"},
    {"index": 2075, "filename": "image_24.png", "description": "「2023年TikTok攻略」というテキストと「フォロワー伸ばし方」1万人フォロワー目指そうという説明画像。"},
    {"index": 2076, "filename": "image_01.png", "description": "「Twitterマネタイズ施策」と「1投稿で20万円売上達成」を訴求するバナー画像。売上UPのマネタイズ動線が記載されている。"},
    {"index": 2077, "filename": "image_02.png", "description": "Twitterで3月1日に122,180円の売上を達成した実績を示す画面。2,980円のサロン商品が41人/日購入された成果を記載。"},
    {"index": 2078, "filename": "image_03.png", "description": "不動産ジャンルのインスタ攻略方法と、月100目指しマネタイズで稼ぐ人への参入推奨を説明するTwitterスクリーンショット。"},
    {"index": 2079, "filename": "image_04.png", "description": "「フォロリツ企画」として無料記事プレゼント経由でサロン商品を入れ込むTwitterマネタイズの動線を図解した画像。"},
    {"index": 2080, "filename": "image_05.png", "description": "スーツを着た女性の横顔イラスト。Twitterマネタイズ施策記事のイメージキャラクターイラスト。"},
    {"index": 2081, "filename": "image_06.jpg", "description": "短髪でスーツ姿の女性の横向きイラスト。ビジネス向けのキャラクターデザイン。"},
    {"index": 2082, "filename": "image_07.png", "description": "不動産ジャンルのマネタイズ方法「事前告知→本企画」で12万imp、4万impの成果を出した具体的なTwitter運用事例を示す画像。"},
    {"index": 2083, "filename": "image_08.jpg", "description": "短髪でスーツ姿の女性の横向きイラスト。複数のTwitterマネタイズ記事で使用される共通キャラクター。"},
    {"index": 2084, "filename": "image_09.png", "description": "「LINE公式で告知」から「バズらしたい投稿」へ、「K くんプレゼン配布」経由でバズを加速させるTwitterマネタイズ戦略図。"},
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

    print(f"\n✓ Batch 2065-2084 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
