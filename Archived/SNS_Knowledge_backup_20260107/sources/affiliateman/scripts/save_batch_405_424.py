#!/usr/bin/env python3
"""
Batch 405-424の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 405-424の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 405,
        "filename": "image_37.png",
        "description": "ユーザー「けくん」からの質問と「K」からの回答。目標設定の方法やロードマップ作成について、1つの形を作ってそれを金銭にする方法について相談している。"
    },
    {
        "index": 406,
        "filename": "image_38.png",
        "description": "ユーザー「ゆうとゆうと」の投稿。1ヶ月でフォロワー300人、ストーリー閲覧率25%を達成。マネタイズ方法についてDMで相談している状況を説明している。"
    },
    {
        "index": 407,
        "filename": "image_39.png",
        "description": "ユーザー「けくん」の回答。note販売、アフィリエイト、フォロワー増やし方に関する複数のセクションで対応を説明。関連するInstagramアカウントも紹介している。"
    },
    {
        "index": 408,
        "filename": "image_40.png",
        "description": "ユーザー「ゆうとゆうと」からの相談内容。復帰したコンサル内容について、インスタアカウント成功の仕組みについて質問を受けている。"
    },
    {
        "index": 409,
        "filename": "image_41.png",
        "description": "ユーザー「Shun」からの質問。2万5000人のZ世代向けファッション系アカウントを運用中で、Sheinのアフィリエイト活用やマネタイズ方法について相談している。"
    },
    {
        "index": 410,
        "filename": "image_42.png",
        "description": "ユーザー「けくん」の回答。Sheinとのコラボについて、商品単価や報酬の観点からアドバイスを提供。クッキー保有期間や成果について説明している。"
    },
    {
        "index": 411,
        "filename": "image_43.png",
        "description": "ユーザー「Erika Suzuki」からの質問。旅行系アカウントとコスメ系アカウント両方を運用中。フォロワー増やし方やアフィリエイト戦略について相談している。"
    },
    {
        "index": 412,
        "filename": "image_44.png",
        "description": "ユーザー「Erika Suzuki」への回答続き。マネタイズ方法やフォロワー（ファン化）向けのアドバイス。関連するInstagramアカウントのリンク紹介も含まれている。"
    },
    {
        "index": 413,
        "filename": "image_45.png",
        "description": "美容系アカウント戦略についての相談内容。プロフィール記載やコスメの具体的な展開方法、LINEへの誘導戦略について記載されている。"
    },
    {
        "index": 414,
        "filename": "image_46.png",
        "description": "ユーザー「ai」からの質問。調子が悪かったアカウントのリーチが落ちている原因について相談している。フォロー増加が減った状況について相談内容を詳述している。"
    },
    {
        "index": 415,
        "filename": "image_47.png",
        "description": "ユーザー「けくん」からの「ai」への回答。アカウント再構築の戦略について説明。ジャンル内での問題解決と復帰のための具体的なアドバイスを提供している。"
    },
    {
        "index": 416,
        "filename": "image_48.png",
        "description": "ユーザー「るる」からの相談。6000人のフォロワーを持つ美容ジャンルアカウント。ダイエット成功経験と美容関連の複数ジャンル構成についての相談内容。"
    },
    {
        "index": 417,
        "filename": "image_49.png",
        "description": "ユーザー「けくん」からの「るる」への回答。ジャンル選定と振抜け戦略について詳細に説明。複数ジャンルの組み合わせと専門領域の作り方についてアドバイスしている。"
    },
    {
        "index": 418,
        "filename": "image_50.png",
        "description": "ユーザー「ゆーし」からの質問。Twitterで紹介されたExcelジャンルについて、Instagramでの活用開始を希望。運用方針について相談している。"
    },
    {
        "index": 419,
        "filename": "image_51.png",
        "description": "ユーザー「けくん」からの「ゆーし」への回答。Excelジャンルのアカウント構築について、ベースとなるアカ情報と投稿頻度について説明している。"
    },
    {
        "index": 420,
        "filename": "image_52.png",
        "description": "ユーザー「みゆきち」からの相談。発酵食品関連の新規アカウント作成とロールモデル研究。健康関連のジャンル理解についての相談内容を記載している。"
    },
    {
        "index": 421,
        "filename": "image_53.png",
        "description": "ユーザー「けくん」からの「みゆきち」への回答。ペルソナ設定の重要性と、発酵食品ジャンルでのスキル構築についてアドバイスを提供している。"
    },
    {
        "index": 422,
        "filename": "image_54.png",
        "description": "ユーザー「星野昌彦」からの質問。メンション依頼や課題ある副業アカウントについて相談。トリドルマーケティングやASPの固定費条件について質問している。"
    },
    {
        "index": 423,
        "filename": "image_55.png",
        "description": "ユーザー「けくん」からの「星野昌彦」への回答。ツイッタービジネスアカウント運用とDMでのコンサル提供について詳しく説明。情報収集とジャンル選定の戦略をアドバイスしている。"
    },
    {
        "index": 424,
        "filename": "image_56.png",
        "description": "ユーザー「りょう」からの相談。食品ジャンルのアカウント運用でダイエットコンサル売上について相談。アフィリエイト施策の具体的な内容質問を記載している。"
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

    print(f"\n✓ Batch 405-424 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
