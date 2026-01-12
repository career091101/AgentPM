#!/usr/bin/env python3
"""
Batch 1065-1084の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1065-1084の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1065,
        "filename": "image_31.png",
        "description": "Kくんからの質問：転職ジャンルに参入するための概念をWeb運用スキルで構築したい。20代でWebスキルを身につけ、未経験からの転職を目指す内容のアカウント戦略。"
    },
    {
        "index": 1066,
        "filename": "image_32.png",
        "description": "Kくんへの回答：Webスキル（動画編集・デザイン系）の発信と転職系はスキル分けした方がいい。WebスキルUPのスクールやNote、コンサルなどでマネタイズ。転職系アフィリエイトで別途マネタイズ。"
    },
    {
        "index": 1067,
        "filename": "image_33.png",
        "description": "じゅんこからの質問：Twitter HSP関連で3,200人フォロワー、Kindle本で月1万～2万円の売上。イングラムで発信も考えており、どちらのマネタイズ方法を選べばいいか迷っている。"
    },
    {
        "index": 1068,
        "filename": "image_34.png",
        "description": "Kくんからの回答：じゅんこのアカウント向けの発信はアリ。ポイントは人生を少し出すこと。転職系でお金資産運用系でも構得度可能。フォロワー1万人で月30～50円くらいが目安。"
    },
    {
        "index": 1069,
        "filename": "image_35.png",
        "description": "バツ（中身なし）マーク表示のシンプルな画像。記事内の区切り要素またはセクション分け表示。"
    },
    {
        "index": 1070,
        "filename": "image_36.png",
        "description": "まきからの質問：薬剤師資格でジャンル選定する場合、Instagramのアカウントマネタイズのゴールが見えない。低体脂肪率ダイエット・ボディメイクアカウントでマネタイズを模索中。"
    },
    {
        "index": 1071,
        "filename": "image_37.png",
        "description": "Kくんからの回答：薬剤師をベースにしたボディメイク系がおすすめ。月30～50円フォロワー単価。ダイエットアカウントは競合多いので、ボディメイク系のトレーニング3ヶ月コンサルで差別化。"
    },
    {
        "index": 1072,
        "filename": "image_38.png",
        "description": "あおいからの質問：インスタグラムのマネタイズについて。グルメ系アカウント運用で2,000人フォロワー超。今後のマネタイズ戦略について質問。"
    },
    {
        "index": 1073,
        "filename": "image_39.png",
        "description": "Kくんからの回答：あおいさん向けマネタイズ戦略。グルメ系は運用代行で稼ぐか、全く別ジャンル参入か検討。フォロワー1万人で月200円稼ぐ目安で戦略構築。"
    },
    {
        "index": 1074,
        "filename": "image_40.png",
        "description": "あおいへの詳細回答：詳細な営業内容と運用代行での月15～30万円の獲得可能性について説明。コンサル・プロデュースで別収益化。"
    },
    {
        "index": 1075,
        "filename": "image_41.png",
        "description": "椿からの質問：無印良品で現在1ヶ月約で転職24のフォロワー68人。Twitterで転職スキル発信を学び、インスタで無印特化の学びを実践中。具体的なマネタイズ方法について質問。"
    },
    {
        "index": 1076,
        "filename": "image_42.png",
        "description": "Kくんからの回答：椿のアカウント向けマネタイズ。フォロワー属性の見極めが重要。居性の悩みを把握してアカウントの売上方向を決定。月15万円単位での収益目標設定。"
    },
    {
        "index": 1077,
        "filename": "image_43.png",
        "description": "椿への継続回答：毎日投稿とフォロワーエンゲージメントについて。ポストの際に気をつけることなど、運用実務面でのアドバイス。"
    },
    {
        "index": 1078,
        "filename": "image_44.png",
        "description": "sana uからの質問：下記アカウントについて相談。登山・初心者向けの発信を検討している。マネタイズ戦略や商品選定について質問。"
    },
    {
        "index": 1079,
        "filename": "image_45.png",
        "description": "Kくんからの詳細回答：登山ジャンルの攻略法。ターゲット属性、アフィリエイト商品の選定、フォロワー1万人での月15～30万円売上の構造。"
    },
    {
        "index": 1080,
        "filename": "image_46.png",
        "description": "Kくんの継続回答：登山アカウントの商品選定ポイント。オンラインスクール・コンサル・Kindleなど複数マネタイズ戦略。フォロワー特性に応じた最適な方法選択。"
    },
    {
        "index": 1081,
        "filename": "image_47.png",
        "description": "sana uへのさらに詳細な回答：フォロワー関係性の構築と運用方法。体作りコンサル、LINE登録、オープンチャットでのコミュニケーション活用。"
    },
    {
        "index": 1082,
        "filename": "image_48.png",
        "description": "sana uへの補足回答：最初のオープンチャット有益情報提供とファンづくり。その後セミナーで有料化。エンゲージメント重視の運用戦略。"
    },
    {
        "index": 1083,
        "filename": "image_49.png",
        "description": "Kくんからの最終アドバイス：sana uのアカウント向けマネタイズ実装。高い利益率を実現するためのコンサルティング開始から成約までの流れ。"
    },
    {
        "index": 1084,
        "filename": "image_50.png",
        "description": "あずからの質問：就活系インスタ運用について。アカウントコンセプトと、リール・フォロワー戦略目安についての相談。2つの質問が記載。"
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

    print(f"\n✓ Batch 1065-1084 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
