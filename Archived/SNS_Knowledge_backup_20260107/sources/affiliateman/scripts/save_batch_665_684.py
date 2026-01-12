#!/usr/bin/env python3
"""
Batch 665-684の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 665-684の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 665,
        "filename": "image_65.png",
        "description": "インスタグラム運用についての質疑応答。固定ピンの活用方法やメンション戦略、グリッド分割アプリの使用方法など複数の質問と回答がテキストで表示されている。"
    },
    {
        "index": 666,
        "filename": "image_66.png",
        "description": "おゆきさん（@kくん）の2ヶ月前の投稿で、グリッド分割投稿とビン留めについての質問が表示。アカウント設定時に約3枚×7列の15投稿をしていることについての相談内容。"
    },
    {
        "index": 667,
        "filename": "image_67.png",
        "description": "kkくん（@おゆき）への回答で、ビン留めする投稿について3枚作成して3段構成で投稿する方法が説明されている。インスタグラムの投稿リールの使用方法についても記載。"
    },
    {
        "index": 668,
        "filename": "image_68.png",
        "description": "だいさんの質問で15投稿リール戦略についての説明。毎日投稿が理想だが2日に一度でもいいこと、アカウント分析との関係性が解説されている。"
    },
    {
        "index": 669,
        "filename": "image_69.png",
        "description": "ねこさん（@Kくん）の初心者向けの質問で、SEOアフィリエイト検索ワード戦略やインスタの検索数調べ方についての複数の相談が含まれている。"
    },
    {
        "index": 670,
        "filename": "image_70.png",
        "description": "kkくんの回答で、フォロワー1万人以上のアカウントが信頼できることやSEOキーワード選定、ジャンル検索方法についての説明が記載。"
    },
    {
        "index": 671,
        "filename": "image_71.png",
        "description": "投稿内容の読み方やプロフィール強化方法についての説明。ストーリー間隔やフォロワー削除対策などの質問への回答がテキストで表示。"
    },
    {
        "index": 672,
        "filename": "image_72.png",
        "description": "カナさん（@Kくん）の質問で、女性向けアカウント作成や恋愛系ジャンルの運営についての相談。ハイライト活用やリール強化方法についても記載。"
    },
    {
        "index": 673,
        "filename": "image_73.png",
        "description": "ツイッター運用についての説明で、リール強化やフォロワー増加戦略、リール内の価値観の見せ方についての複数の質問と回答。"
    },
    {
        "index": 674,
        "filename": "image_74.png",
        "description": "KKくん（@カナ）の投稿で、動画見直しやメッセージ受け取り、自動返信機能、DM自動定型コメント機能やLINE誘導の仕組みについての説明。"
    },
    {
        "index": 675,
        "filename": "image_75.png",
        "description": "おゆきさんの投稿で、グリッド投稿の作成方法やリール投稿、フィードとリールの違い、ストーリーの使い方についての4つの質問が記載。"
    },
    {
        "index": 676,
        "filename": "image_76.png",
        "description": "Rockyさん（占い系2.5万フォロワー、恋愛占いTikTok1万、Instagram8000以上）のプロフィール説明。スピ系ジャンルのデザインやアイコン、文字量についての改善提案。"
    },
    {
        "index": 677,
        "filename": "image_77.png",
        "description": "吉田さん（@Kくん）の質問で、不動産業代行についてのTikTok運用相談やInstagram新規アカウント活用方法についての複数の相談内容。"
    },
    {
        "index": 678,
        "filename": "image_78.png",
        "description": "Kkくんの回答で、不動産投資アカウント運用やInstagram新規アカウント広告活用、フォロワーの見込み客化についての説明。"
    },
    {
        "index": 679,
        "filename": "image_79.png",
        "description": "りょうかさん（@Kくん）の投稿で、女子大生向けのマッチングアプリ・ソロ活について複数の質問内容が記載。HSPやマネタイズについての相談。"
    },
    {
        "index": 680,
        "filename": "image_80.png",
        "description": "Kkくんの回答で、大学生活ライフハックのテーマやマネタイズ方法について、アプリ選定やアカウント運用戦略についての詳細な説明。"
    },
    {
        "index": 681,
        "filename": "image_81.png",
        "description": "おゆきさんの4つの質問で、フィードとリールの使い分けやフォロー水栓について、キャップカットのテンプレート活用についての相談。"
    },
    {
        "index": 682,
        "filename": "image_82.png",
        "description": "Kkくんの回答で、フィードリール毎日投稿方法や風水恋愛アカウント運用についての説明。リール定数Impやフィード投稿戦略についても記載。"
    },
    {
        "index": 683,
        "filename": "image_83.png",
        "description": "ねこさんの質問で、フォロワー500人程度の新規アカウント運用について。ストーリーズ活用やDM活用戦略についての複数の相談内容。"
    },
    {
        "index": 684,
        "filename": "image_84.png",
        "description": "マサさん（美容室経営者、@Kくん）の質問で、キッズカット関連のマネタイズについて。自宅カット用ハサミやメーカー広告、フィード投稿戦略についての相談内容。"
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
            print(f"[{idx}] {inventory[idx].get('filename', 'unknown')}: 説明更新")

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

    print(f"\n✓ Batch 665-684 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
