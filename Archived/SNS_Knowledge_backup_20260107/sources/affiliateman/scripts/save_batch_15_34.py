#!/usr/bin/env python3
"""
Batch 15-34の画像説明を保存
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 15-34の画像説明
batch_descriptions = [
    {
        "index": 15,
        "filename": "image_10.png",
        "description": "ドン・キホーテで買える「後悔なしコスメ14選」と「ドンキで買える最高スキンケア」の2つの商品紹介画像。化粧水や美容液などのスキンケア商品が多数掲載されている。"
    },
    {
        "index": 16,
        "filename": "image_11.png",
        "description": "ミスタードーナツのカロリー比較表と寿司ローダイエット（カロリー比較）の2つの画像。ドーナツや寿司の種類別カロリーが詳細に記載されている。"
    },
    {
        "index": 17,
        "filename": "image_12.png",
        "description": "「保存版 ユニバ周辺 ホテル8選」と「サービスがすごい ディズニー周辺ホテル」の2つのホテル紹介画像。テーマパーク周辺の宿泊施設を比較している。"
    },
    {
        "index": 18,
        "filename": "image_13.png",
        "description": "「UNIQLO U 気になるアイテム7選 明日発売」と「GU 絶対買いのモテコーデ」の2つのファッション紹介画像。ユニクロとGUの商品を紹介している。"
    },
    {
        "index": 19,
        "filename": "image_14.png",
        "description": "「アディダス半額祭」「KALDI購入品（コレ全員もらえる）」「しまむら 昨年即完売 激安」の3つのショッピング情報画像。セールやお得な商品を紹介している。"
    },
    {
        "index": 20,
        "filename": "image_15.png",
        "description": "デスクワークやリモートワークをする女性3人のイラスト。パソコンで作業している様子が描かれている。"
    },
    {
        "index": 21,
        "filename": "image_16.png",
        "description": "無印良品、UNIQLO、マクドナルドのロゴと「みんなが知っているワード＋ある重要要素」という組み合わせを示す図解。バズるコンテンツ作成の法則を説明している。"
    },
    {
        "index": 22,
        "filename": "image_17.png",
        "description": "データ分析（円グラフと%）、設定（歯車）、調査（虫眼鏡とグラフ）を表す3つのアイコンイラスト。ビジネスやマーケティングの分析作業を象徴している。"
    },
    {
        "index": 23,
        "filename": "image_18.png",
        "description": "「入居時やるべき 洗面所編」と「入居時やるべき お風呂編」の2つの生活Tips画像。新居入居時の準備作業を解説している。"
    },
    {
        "index": 24,
        "filename": "image_19.png",
        "description": "「インスタ2023年伸びてるアカ 伸びているジャンルと収益方法 アカウント10選とマネタイズ施策」という赤と緑のバナー画像。インスタグラム成長戦略を紹介。"
    },
    {
        "index": 25,
        "filename": "image_20.png",
        "description": "「2023年インスタ伸ばし方 フォロワーを伸ばす施策 目指せフォロワー1万人」という紫のバナー画像。インスタグラムのフォロワー増加施策を解説。"
    },
    {
        "index": 26,
        "filename": "image_21.png",
        "description": "「フォロワー増加の10施策 外部誘導でフォロワー爆伸び インスタ⇄Twitter【フォロワー伸びた成功事例紹介】」という青のバナー画像。SNS間の相互誘導戦略を紹介。"
    },
    {
        "index": 27,
        "filename": "image_22.png",
        "description": "「2023年インスタ攻略 ストーリー閲覧率爆伸び 1週間 7%→38%」という紫のバナー画像。インスタグラムストーリーの閲覧率向上事例を示している。"
    },
    {
        "index": 28,
        "filename": "image_23.png",
        "description": "「SNSのマネタイズ事例 DMで商品を売る施策例 僕の成功事例紹介」という黄色のバナー画像。SNSを使った販売手法を解説。"
    },
    {
        "index": 29,
        "filename": "image_24.png",
        "description": "「インスタ バズった事例紹介 トレンド攻略とリサーチ方法 バズるコンテンツ作成」という紫のバナー画像。バイラルコンテンツの作成方法を紹介。"
    },
    {
        "index": 30,
        "filename": "image_01.png",
        "description": "「2023年インスタ攻略 ストーリー閲覧率爆伸び 1週間 7%→38%」という紫のバナー画像（大きな全画面表示版）。ストーリー機能の効果的な活用法を解説。"
    },
    {
        "index": 31,
        "filename": "image_02.png",
        "description": "ストーリー閲覧率の成長グラフ。1日目7%から始まり、施策(1)で4日目に18%、施策(2)で7日目に38%へ爆伸びする過程を示している。"
    },
    {
        "index": 32,
        "filename": "image_03.png",
        "description": "インスタグラムアプリのスマホ画面イメージ。ストーリー左側の配置位置とホーム画面1番上の重要性を赤枠で強調している。"
    },
    {
        "index": 33,
        "filename": "image_04.png",
        "description": "ストーリー閲覧率の成長推移グラフ。施策(1)実施で18%に到達し、施策(2)実施で38%まで爆伸びする過程を折れ線グラフで表示。"
    },
    {
        "index": 34,
        "filename": "image_05.png",
        "description": "ストーリー閲覧率の成長推移グラフ（グレーアウトバージョン）。施策(2)の部分が淡色表示されており、次のステップを示唆している。"
    }
]

def update_inventory_with_descriptions(batch_descriptions):
    """image_inventory_progress.jsonを読み込み、説明を追加"""

    # 進捗ファイルを読み込み
    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'
    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    # 説明を追加
    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {inventory[idx]['filename']}: 説明追加")

    # 進捗状況を表示
    total = len(inventory)
    completed = sum(1 for item in inventory if item.get('description'))
    remaining = total - completed

    print(f"\n進捗: {completed}/{total} 完了 (残り{remaining}件)")
    print(f"完了率: {completed/total*100:.1f}%")

    # 進捗ファイルを更新
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 進捗保存: {progress_file.name}")

    return inventory

if __name__ == "__main__":
    inventory = update_inventory_with_descriptions(batch_descriptions)
