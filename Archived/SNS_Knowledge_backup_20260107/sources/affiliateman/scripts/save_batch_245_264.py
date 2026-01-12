#!/usr/bin/env python3
"""
Batch 245-264の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
記事: インスタの稼ぎやすいジャンルとマネタイズ施策の例
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 245-264の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 245,
        "filename": "image_03.png",
        "description": "月100万円以上を稼ぐインスタジャンルの9つの分類。恋愛、ビジネス、子育てハウツー、転職、外見改善、夫婦関係改善、副業、セクテク、営業テクニックを色分けして表示。"
    },
    {
        "index": 246,
        "filename": "image_04.png",
        "description": "恋愛ジャンルのマネタイズ方法。アフィリエイト（街コン予約・婚活サービス・大人のおもちゃ・マッチングアプリ）、note（復縁系・モテ系・付き合う系・セクテク系）、コンサル（悩み解決コンサル・単発/長期コンサル）の3軸。"
    },
    {
        "index": 247,
        "filename": "image_05.png",
        "description": "ビジネスジャンルのマネタイズ方法。アフィリエイト（ツール系・ASP会員登録・ドメイン/サーバー）、note（インスタ・TIKTOK・Twitter・運用代行・ライティング）、コンサル（悩み解決コンサル・単発/長期コンサル）。"
    },
    {
        "index": 248,
        "filename": "image_06.png",
        "description": "子育てコンサルジャンルのマネタイズ方法。アフィリエイト（教育系・その他子育て案件）、note（教育系・自己肯定感・夫婦関係改善）、コンサル（悩み解決コンサル・単発/長期コンサル）。"
    },
    {
        "index": 249,
        "filename": "image_07.png",
        "description": "転職ジャンルのマネタイズ方法。アフィリエイト（転職アプリ・転職エージェント）、note（年収UP系・転職攻略・営業術・仕事術）、コンサル（転職コンサル・営業コンサル・キャリアコンサル）。"
    },
    {
        "index": 250,
        "filename": "image_08.png",
        "description": "外見コンサルジャンルのマネタイズ方法。アフィリエイト（美容整形・ダイエット・メンズコスメ・ファッション・マッチングアプリ）、note（垢抜けnote・モテnote）、コンサル（垢抜けコンサル・モテコンサル）。"
    },
    {
        "index": 251,
        "filename": "image_09.png",
        "description": "夫婦関係改善ジャンルのマネタイズ方法。アフィリエイト（アダルトアイテム）、note（セクテク・自己肯定感・夫婦関係改善）、コンサル（夫婦関係改善・セクテク）。"
    },
    {
        "index": 252,
        "filename": "image_10.png",
        "description": "セクテクジャンルのマネタイズ方法。アフィリエイト（アダルトアイテム）、note（フェラnote・脳イキnote・中イキnote・キスイキnote）、コンサル（セクテク）。"
    },
    {
        "index": 253,
        "filename": "image_11.png",
        "description": "営業テクニックジャンルのマネタイズ方法。アフィリエイト（ビジネス系アフィ）、note（営業攻略note・接待攻略note・仕事攻略note・会話術note）、コンサル（営業コンサル）。"
    },
    {
        "index": 254,
        "filename": "image_12.png",
        "description": "山頂に旗が立つイラスト。インスタグラムマネタイズにおけるゴール到達を象徴するビジュアル。"
    },
    {
        "index": 255,
        "filename": "image_13.jpg",
        "description": "赤いビジネススーツを着た女性の上半身イラスト。プロフェッショナルキャリアウーマンを象徴するポートレート。"
    },
    {
        "index": 256,
        "filename": "image_14.png",
        "description": "Twitterアカウント「kくん（火、永久凍結しました涙）」(@kkk_cun)のツイート。マネタイズの軸について、メイン：長期コンサル、サブ①：noteやtips、サブ②：アフィと記載。"
    },
    {
        "index": 257,
        "filename": "image_15.png",
        "description": "黄金色の木のイラスト。3つの金貨がなっている枝を持つ金銭象徴的なビジュアル。マネタイズ戦略の豊かさを表現。"
    },
    {
        "index": 258,
        "filename": "image_16.png",
        "description": "女性のビジネスプロフィールアイコン。紺色のジャケット、赤いネクタイ、黒い髪の女性キャラクター。ビジネスジャンル執筆者を象徴。"
    },
    {
        "index": 259,
        "filename": "image_17.jpg",
        "description": "女性のビジネスプロフィールアイコン。紺色のジャケット、赤いネクタイ、黒い髪の女性キャラクター。"
    },
    {
        "index": 260,
        "filename": "image_18.png",
        "description": "バックエンド商品誘導フロー。24時間限定DMで無料質問受け付け可という固定ピン、無料占いのハイライト（B・C・D）、無料コンサルへの誘導フロー図解。"
    },
    {
        "index": 261,
        "filename": "image_19.png",
        "description": "黄金の王冠のアイコン。中央に大きな赤い宝石、両側に小さな赤い宝石が付いた豪華な王冠を表現。"
    },
    {
        "index": 262,
        "filename": "image_20.jpg",
        "description": "女性のビジネスプロフィールアイコン。紺色のジャケット、赤いネクタイの女性キャラクター。"
    },
    {
        "index": 263,
        "filename": "image_21.jpg",
        "description": "女性のビジネスプロフィールアイコン。紺色のジャケット、赤いネクタイ、黒い髪の女性キャラクター。"
    },
    {
        "index": 264,
        "filename": "image_22.png",
        "description": "月100万円の稼ぎの構造図解。値段10万円/月から3つの軸に分岐：商品単価（商談数、申込み数）、商談数（DM数、ライブ数、ストーリー数）、成約率が記載。"
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

    print(f"\n✓ Batch 245-264 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
