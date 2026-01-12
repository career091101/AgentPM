#!/usr/bin/env python3
"""
Batch 1225-1244の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
【2023年5月】質疑応答のまとめ記事
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1225-1244の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1225,
        "filename": "image_45.png",
        "description": "インスタグラムDMの恋愛・メンズ美容相談コメント。「モテ★メンズ美容」から「その他」という属性に関する返信で、恋愛指南に関する質問応答が表示されている。"
    },
    {
        "index": 1226,
        "filename": "image_46.png",
        "description": "Kくんというユーザーからの質問メッセージ。プログ×SNSジャンルのハイライトやアフィ記事の始め方などについて質問している内容。"
    },
    {
        "index": 1227,
        "filename": "image_47.png",
        "description": "Kくんへの回答コメント。AI関連情報の発信、ブログ×SNSジャンル選択、ASP企業広告掲載についての3つの質問に対する詳細な回答が記載されている。"
    },
    {
        "index": 1228,
        "filename": "image_48.png",
        "description": "さちこというユーザーのInstagramプロフィール質問。ストーリーズのスウィープ投稿とドリンク商品の売上を伸ばすための運用方法について質問している。"
    },
    {
        "index": 1229,
        "filename": "image_49.png",
        "description": "Kくんのリプライ。伸びについてのコンセプト確立やフォロー率向上の戦略など、運用改善の多角的なアドバイスが含まれている。"
    },
    {
        "index": 1230,
        "filename": "image_50.png",
        "description": "さくらいというユーザーからのサロン入店に関する質問。インスタ発信初期のジャンル選択やマネタイズ方法についての相談内容が表示されている。"
    },
    {
        "index": 1231,
        "filename": "image_51.png",
        "description": "Kくんによる回答コメント。ジャンル選択時の重要性やビジネス系アフィについて、初心者向けの具体的なアドバイスが記載されている。"
    },
    {
        "index": 1232,
        "filename": "image_52.png",
        "description": "RukaというユーザーのInstagramアカウント相談。恋愛・美容ジャンルでの投稿内容やフォロワー増加の課題について質問している。"
    },
    {
        "index": 1233,
        "filename": "image_53.png",
        "description": "Kくんのリプライ。恋愛・美容ジャンルの発信初期戦略やコンテンツ統一性、プロフィール改善についての詳細なアドバイスが含まれている。"
    },
    {
        "index": 1234,
        "filename": "image_54.png",
        "description": "トマトというユーザーのファッション初期設定に関する質問。プチプラコーデや育児テーマのアフィ売上について相談している。"
    },
    {
        "index": 1235,
        "filename": "image_55.png",
        "description": "Kくんの回答。ファッション系アフィの戦略やマネタイズ難易度、ニッチ層への提供価値についての実践的なアドバイスが記載されている。"
    },
    {
        "index": 1236,
        "filename": "image_56.png",
        "description": "るかというユーザーからのDM質導に関する質問。アカウント運用経過やフォロワー増加の悩みについての相談が表示されている。"
    },
    {
        "index": 1237,
        "filename": "image_57.png",
        "description": "Kくんのリプライ。初期フィード投稿から1、2ヶ月経過の段階での運用改善策やコンセプト統一性についての指導内容。"
    },
    {
        "index": 1238,
        "filename": "image_58.png",
        "description": "ちゃこというユーザーのストーリーズ反応率向上に関する質問。フォロワー800人での運用課題や反応率改善方法について相談している。"
    },
    {
        "index": 1239,
        "filename": "image_59.png",
        "description": "Kくんとちゃこのやり取り。ストーリーズ間隔や反応率改善のテクニック、コメント周りの施策についての実践的なアドバイス内容。"
    },
    {
        "index": 1240,
        "filename": "image_60.png",
        "description": "あおいというユーザーのグルメ系アカウント運用相談。フォロワー5000人の達成とマネタイズ施策についての質問が記載されている。"
    },
    {
        "index": 1241,
        "filename": "image_61.png",
        "description": "Kくんの回答。グルメ系マネタイズの難易度や他のジャンル併用戦略、店舗営業の観点からのアドバイスが含まれている。"
    },
    {
        "index": 1242,
        "filename": "image_62.png",
        "description": "るるというユーザーのリール投稿とInstagram運用について。ミニマリスト関連の投稿内容や自分のキャラ設定についての質問が表示されている。"
    },
    {
        "index": 1243,
        "filename": "image_63.png",
        "description": "Kくんとるるのやり取り。ジャンル変更やターゲット設定、初期段階での自力リール制作の重要性についての指導内容。"
    },
    {
        "index": 1244,
        "filename": "image_64.png",
        "description": "Kくんとマーティーのやり取り。インスタ発信初期段階でのジャンル選択やビジネス系アフィアカウント構築についての具体的なアドバイス。"
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

    print(f"\n✓ Batch 1225-1244 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
