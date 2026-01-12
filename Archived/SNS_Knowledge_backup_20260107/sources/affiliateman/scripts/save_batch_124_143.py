#!/usr/bin/env python3
"""
Batch 124-143の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 124-143の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 124,
        "filename": "image_08.png",
        "description": "「フォロワー増加の10施策 外部誘導でフォロワー爆伸び インスタ⇄Twitter フォロワー伸びた成功事例紹介」という青色のバナー画像。SNS間の相互送客によるフォロワー増加戦略を解説。"
    },
    {
        "index": 125,
        "filename": "image_09.png",
        "description": "「2023年インスタ攻略 ブルーオーシャン16選 今後伸びそうなお宝ジャンル」という紫色のバナー画像。競合が少ない有望ジャンルを紹介。"
    },
    {
        "index": 126,
        "filename": "image_10.png",
        "description": "「インスタ2023年伸びてるアカ 伸びているジャンルと収益方法 アカウント10選とマネタイズ施策」という赤と緑のバナー画像。成功アカウントの分析と収益化手法を解説。"
    },
    {
        "index": 127,
        "filename": "image_01.png",
        "description": "「インスタ不動産ジャンル 伸ばし方と収益動線 不動産ジャンルの稼ぎ方 不動産ジャンルの0→1の施策など紹介済」という茶色のバナー画像。不動産業界でのインスタグラム活用とマネタイズ戦略を解説。"
    },
    {
        "index": 128,
        "filename": "image_02.png",
        "description": "不動産ジャンルの収益性を示す図解。「フォロワー1000人で50〜100万円」「アカ作って1ヶ月で30万円達成!?」という2つの実績が表示され、高収益の可能性を訴求している。"
    },
    {
        "index": 129,
        "filename": "image_03.png",
        "description": "不動産物件のリール動画サムネイル8枚のコラージュ。美しい内装、白を基調とした部屋、田町や六本木など都内の物件が紹介されており、再生数が1674、1517、2022などと表示されている。"
    },
    {
        "index": 130,
        "filename": "image_04.png",
        "description": "価格タグのアイコンイラスト。青い値札に黄色の飾りがついたシンプルなデザインで、価格設定やマネタイズを象徴している。"
    },
    {
        "index": 131,
        "filename": "image_05.png",
        "description": "不動産アカウントの差別化戦略を示す図解。「地域特化」（東京・福岡の地図）と「ニーズ」（ペット可・同棲暮らし・音楽防音）を掛け算することでターゲットを絞り込む手法を視覚化している。"
    },
    {
        "index": 132,
        "filename": "image_06.png",
        "description": "リールからプロフィールへの導線設計を示す図解。リール動画→プロフィール（不動産太郎）への誘導フロー、「もっと詳しくたい人は問い合わせてね」というCTA、ハイライト活用が説明されている。"
    },
    {
        "index": 133,
        "filename": "image_07.png",
        "description": "「アカウント一言で伝える」をテーマにした4つのバナー例のコラージュ。デザイナー向け、おいしいお店紹介、SNSマーケ、心を軽くする雑貨屋など、異なるジャンルのアカウントコンセプトが並んでいる。"
    },
    {
        "index": 134,
        "filename": "image_08.png",
        "description": "「東京 不動産」でGoogle検索した際の店舗一覧画面。地図上に複数のピンが表示され、不動産会社のリストが営業時間や評価とともに表示されている。SEO対策の重要性を示す画像。"
    },
    {
        "index": 135,
        "filename": "image_09.png",
        "description": "at homeなどの賃貸物件検索サイトの結果一覧画面。複数の不動産会社が並び、営業時間・定休日・問い合わせボタンなどが表示されている。物件情報サイトへの掲載の重要性を示している。"
    },
    {
        "index": 136,
        "filename": "image_10.png",
        "description": "「インスタで稼げるジャンル 月100万円狙えるジャンル マネタイズ戦略を共有」という黄色とオレンジのバナー画像。高収益ジャンルと収益化手法を紹介する記事への導線。"
    },
    {
        "index": 137,
        "filename": "image_11.png",
        "description": "「インスタマネタイズ ガチで売れるストーリー施策 稼げる最強の施策まとめ」という黄色のバナー画像。ストーリー機能を活用した販売戦略を解説。"
    },
    {
        "index": 138,
        "filename": "image_12.png",
        "description": "「インスタ バズった事例紹介 トレンド攻略とリサーチ方法 バズるコンテンツ作成」という紫色のバナー画像。バイラルコンテンツの作成ノウハウを紹介。"
    },
    {
        "index": 139,
        "filename": "image_13.png",
        "description": "「インスタ2023年伸びてるアカ 伸びているジャンルと収益方法 アカウント10選とマネタイズ施策」という赤と緑のバナー画像。成功事例の分析と実践的な収益化手法を解説。"
    },
    {
        "index": 140,
        "filename": "image_14.png",
        "description": "「インスタ 尖ったアカウント 差別化されたコンセプト設計 コンセプト設計講座」という紫とピンクのバナー画像。独自性のあるアカウント作りの手法を解説。"
    },
    {
        "index": 141,
        "filename": "image_15.png",
        "description": "「2023年インスタ伸ばし方 フォロワーを伸ばす施策 目指せフォロワー1万人」という紫色のバナー画像。フォロワー1万人達成のための具体的な戦略を解説。"
    },
    {
        "index": 142,
        "filename": "image_01.png",
        "description": "「2023年インスタ攻略 伸びているジャンル31選 ニーズがあるジャンル理解」という紫色の大きなバナー画像。需要の高い31ジャンルを体系的に解説する記事のメインビジュアル。"
    },
    {
        "index": 143,
        "filename": "image_02.jpg",
        "description": "スーツを着た男性の横顔を描いたシンプルな線画イラスト。ビジネスパーソンやプロフェッショナルを象徴するイメージ。"
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

    print(f"\n✓ Batch 124-143 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
