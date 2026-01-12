#!/usr/bin/env python3
"""
Batch 1245-1264の画像説明を保存
インスタグラムコメント欄のQ&A画像に対する詳細な日本語説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1245-1264の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1245,
        "filename": "image_65.png",
        "description": "Instagramのコメント欄。ユーザー「ぶる」がTwitterとInstagramでのリプライとコメント方式の違いについて質問。Instagramでリプライを贈るとフィード投稿にコメントもする仕様について、ステップ施策の有無で使い分けるかについてのQ&A。"
    },
    {
        "index": 1246,
        "filename": "image_66.png",
        "description": "Instagramのコメント欄。ユーザー「ぶる」からのコメント続き。ツイッターとInstagramのコメント方式、リールでのコメント戦略についての質問と、回答者からのアドバイス。"
    },
    {
        "index": 1247,
        "filename": "image_67.png",
        "description": "Instagramのコメント欄。ユーザー「みい」がフォロワー数の変動とアカウント設定についての相談。近年フォロワー数が減少し、3ヶ月で現在950フォロワーほどとのこと。初期段階での施策とフォロワー減少への対策についてのQ&A。"
    },
    {
        "index": 1248,
        "filename": "image_68.png",
        "description": "Instagramのコメント欄。ユーザー「みい」から複数のフォロワー減少に関する質問。ホーム率、保存率、最近のリール改善についての相談と、フォロワーが減る理由に関する深掘り質問が含まれている。"
    },
    {
        "index": 1249,
        "filename": "image_69.png",
        "description": "Instagramのコメント欄。画像説明に関する提案。インサイト画面のスクショを添付するよう勧告されている。テーマとコンセプト設定、リールのメリットについての質問。"
    },
    {
        "index": 1250,
        "filename": "image_70.png",
        "description": "Instagramのコメント欄。ユーザー「ゆん」からのアカウント設定相談。アラフォー×転機をテーマに、ビジネス関連の美容・ライフスタイル商材をASPアフィリで販売目指すアカウント構想。"
    },
    {
        "index": 1251,
        "filename": "image_71.png",
        "description": "Instagramのコメント欄。ユーザー「ゆん」から5月ZOOMコンサルについて提案。YouTube「SNS攻略サロン限定」での5月ZOOMコンサル告知のスクショが含まれている。"
    },
    {
        "index": 1252,
        "filename": "image_72.png",
        "description": "Instagramのコメント欄。ユーザー「ルーク」からの看護職向けアカウント相談。看護師専門の情報発信アカウント運用に関する複数の質問と、看護職系インスタアカウント一覧の提案。"
    },
    {
        "index": 1253,
        "filename": "image_73.png",
        "description": "Instagramのコメント欄。Instagramのx（バツ）マークボタンについての質問と回答。アカウント運用に関する詳細な相談が続いている。"
    },
    {
        "index": 1254,
        "filename": "image_74.png",
        "description": "Instagramのコメント欄。ユーザー「よっし」からスリーコインズ商品紹介アカウント向けのコンセプト相談。フォロワー減少とアカウント方向性の見直しについてのQ&A。"
    },
    {
        "index": 1255,
        "filename": "image_75.png",
        "description": "Instagramのコメント欄。ユーザー「よっし」から5月Zoom初参加の報告とコンサル申し込みについての連絡。6月オプションコンサル希望についての相談。"
    },
    {
        "index": 1256,
        "filename": "image_76.png",
        "description": "Instagramのコメント欄。Twitter永久凍結に関する相談。ビジネス垢12月に凍結、永久凍結対象の詳細説明とTwitterアカウント復活方法についての質問。"
    },
    {
        "index": 1257,
        "filename": "image_77.png",
        "description": "Instagramのコメント欄。Twitter凍結に関する回答者からの詳細な対応方法説明。永久凍結時のメール異議申し立てと別電話番号での登録方法についての指導。"
    },
    {
        "index": 1258,
        "filename": "image_78.png",
        "description": "Instagramのコメント欄。Twitter凍結の詳細な対応方法。電話番号のロックと凍結解除の手続きについて、複数のケースを想定した説明。"
    },
    {
        "index": 1259,
        "filename": "image_79.png",
        "description": "Instagramのコメント欄。ユーザー「せいぬ seinunote」からTwitter凍結に関する複数の質問。ビジネス垢の凍結と復活方法についての詳細な疑問リスト。"
    },
    {
        "index": 1260,
        "filename": "image_80.png",
        "description": "Instagramのコメント欄。Twitter凍結対応に関する詳細な回答。永久凍結との区別、メールでの異議申し立て、電話番号登録時の手続きについての説明。"
    },
    {
        "index": 1261,
        "filename": "image_81.png",
        "description": "Instagramのコメント欄。Twitter凍結対応の追加質問。復活後のWi-Fi設定やログイン手続きについての細かい確認事項。"
    },
    {
        "index": 1262,
        "filename": "image_82.png",
        "description": "Instagramのコメント欄。ユーザー「かける」からダイエットコンサル向けTwitter発信についての相談。売上発生のツイート内容の工夫について、複数の質問。"
    },
    {
        "index": 1263,
        "filename": "image_83.png",
        "description": "Instagramのコメント欄。ユーザー「マーティー」からコンテンツ販売とコンサルビジネスについての複数の質問。noteやBrain販売、マネタイズ施策についての相談リスト。"
    },
    {
        "index": 1264,
        "filename": "image_84.png",
        "description": "Instagramのコメント欄。ユーザー「マーティー」からのコンテンツ販売に関する追加質問。マネタイズ施策、コンサル商品設計、Twitter活用方法についての複数の相談。"
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

    print(f"\n✓ Batch 1245-1264 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
