#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2027, "filename": "image_02.jpg", "description": "スーツを着た男性の横顔イラスト。黒髪と赤いネクタイが特徴のビジネスキャラクターの描写。"},
    {"index": 2028, "filename": "image_03.jpg", "description": "TikTokアカウント初期段階における「バズる→フォロワー増加」の循環メカニズムを図解した説明画像。"},
    {"index": 2029, "filename": "image_04.jpg", "description": "TikTokフォロワー増加時のエンゲージメント向上を示す流れ図。投稿→いいね/コメント→フォロワー増加の相互作用を解説。"},
    {"index": 2030, "filename": "image_05.png", "description": "ターゲット設定を示すテキスト「コンセプト設計」と標的アイコンのシンプルなグラフィック。"},
    {"index": 2031, "filename": "image_06.jpg", "description": "TikTok検索機能のUIスクリーンショット。参入ジャンル検索と男性アカウント（@kaito_wolf_512）のプロフィール画面を並べて表示。"},
    {"index": 2032, "filename": "image_07.png", "description": "「バズる投稿」というテキストとロケットアイコンが描かれたタイトルグラフィック。"},
    {"index": 2033, "filename": "image_08.png", "description": "「応用編」というテキストと惑星アイコンが描かれたセクション見出しグラフィック。"},
    {"index": 2034, "filename": "image_09.jpg", "description": "TikTok上の美容・スキンケア関連バズ動画サムネイルの集合画像。複数のコンテンツが格子状に配置され1位と2位が強調表示。"},
    {"index": 2035, "filename": "image_10.png", "description": "「TIKTOKバズる動画例」と「バズを生み出す動画構成」「ファーストビューの重要性」をテキストで示した説明スライド。"},
    {"index": 2036, "filename": "image_11.png", "description": "「TIKTOK バズる特徴」「商品紹介アカで無双する」「飽きられない最強のテーマ」を階段状に配置したテキストスライド。"},
    {"index": 2037, "filename": "image_12.png", "description": "「2023年TikTok攻略」「稼げるおすすめジャンル」「ジャンル選定の理解」とTikTokロゴとキャラクターが描かれた攻略ガイドタイトル画像。"},
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

    print(f"\n✓ Batch 2027-2037 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
