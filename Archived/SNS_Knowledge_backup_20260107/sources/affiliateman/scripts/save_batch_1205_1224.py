#!/usr/bin/env python3
"""
Batch 1205-1224の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1205-1224の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1205,
        "filename": "image_25.png",
        "description": "Instagram Q&A投稿のスクリーンショット。ユーザー「bstr」が大ジャンル×中ジャンル×小ジャンルの差別化について質問し、管理者が異なるジャンルの組み合わせパターンと各パターンの特徴を説明している。"
    },
    {
        "index": 1206,
        "filename": "image_26.png",
        "description": "参考情報として、質問者の属性（28歳ITエンジニア、2LDK住まい等）とユーザー「Kくん」からのアカウント運用に関する具体的なアドバイスコメントを表示している投稿画面。"
    },
    {
        "index": 1207,
        "filename": "image_27.png",
        "description": "ユーザー「ひなた_転職バイトお金モテ」からのInstagramアカウント（tensyoku_hinata）の紹介とフォロワー増加に関する相談コメント。転職系アカウントの運用課題を提示している。"
    },
    {
        "index": 1208,
        "filename": "image_28.png",
        "description": "ユーザー「Kくん」がコンテンツの質とフォロワー数の関係について説明し、リール・フィード・アカウントコンセプトの重要性を述べている投稿コメント。"
    },
    {
        "index": 1209,
        "filename": "image_29.png",
        "description": "ユーザー「るか」がTwitter（ツイート内容参照リンク付き）での直アフィ探し方とストーリー運用に関する質問をしている投稿。"
    },
    {
        "index": 1210,
        "filename": "image_30.png",
        "description": "管理者「Kくん」が直アフィ探しの基本的な方法（ツイート検索、サロン内情報共有）とASP関連の説明をしているコメント返信。"
    },
    {
        "index": 1211,
        "filename": "image_31.png",
        "description": "ユーザー「ひなた_転職バイトお金モテ」から切り抜き・リール配信・ストーリー活用に関する3点質問をしている投稿。"
    },
    {
        "index": 1212,
        "filename": "image_32.png",
        "description": "Kくんの詳細な回答で、グレーの切り抜きOK、リール運用の具体的戦略、アカウントコンセプト変更の可能性について説明するコメント。"
    },
    {
        "index": 1213,
        "filename": "image_33.png",
        "description": "ユーザー「ヘイ」がWebライター業と「ブログ×SNSジャンル」参入についての相談をしており、複数SNS展開とブログマネタイズの実績について質問している。"
    },
    {
        "index": 1214,
        "filename": "image_34.png",
        "description": "Kくんのアドバイスで、ブログマネタイズは固定ピンと実績、SNSは短期投資よりも長期構築を勧める内容のコメント返信。"
    },
    {
        "index": 1215,
        "filename": "image_35.png",
        "description": "ユーザー「そらね」が不動産Instagram・TikTokを10日で始めたことを報告し、フィード投稿とリール活用に関する相談をしている投稿。"
    },
    {
        "index": 1216,
        "filename": "image_36.png",
        "description": "Kくんがフィード投稿とリール投稿の運用戦略、シャドバン対策、コンテンツの再生回数伸び悩みについて具体的なアドバイスをしているコメント。"
    },
    {
        "index": 1217,
        "filename": "image_37.png",
        "description": "ユーザー「Kくん」が@そらねへの返信で、ハイライト・固定ピン見直し、シャドバン改善方法を提示するコメント。"
    },
    {
        "index": 1218,
        "filename": "image_38.png",
        "description": "Kくんがシャドバン対策として、Instagram・TikTok両方でフォロワー増やし、関連する見つけやすいコンテンツ作成を勧めるコメント返信。"
    },
    {
        "index": 1219,
        "filename": "image_39.png",
        "description": "ユーザー「そら」がInstagram運用失敗から改善を試みており、フィード投稿とリール両方の相談をしている投稿。"
    },
    {
        "index": 1220,
        "filename": "image_40.png",
        "description": "KくんがInstagram失敗の原因分析、フォロワー1000人達成のための段階的な投稿戦略をアドバイスしているコメント。"
    },
    {
        "index": 1221,
        "filename": "image_41.png",
        "description": "ユーザー「はや」がリール作成カバー・アカウントコンセプトに関する2点質問を投稿している。不動産アカウントの具体的な課題提示。"
    },
    {
        "index": 1222,
        "filename": "image_42.png",
        "description": "Kくんがリール作成時のサムネイルデザイン・カバー方法、8000人規模のアカウント運用について具体的にアドバイスするコメント。"
    },
    {
        "index": 1223,
        "filename": "image_43.png",
        "description": "ユーザー「です」がメンズ美容アカウントのコンセプト設定について相談し、30代の悩み対策×独身アラサーのニッチ戦略を提案している投稿。"
    },
    {
        "index": 1224,
        "filename": "image_44.png",
        "description": "Kくんがメンズ美容アカウントのコンセプト評価と改善提案、マネタイズ方法（note・アフィリエイト）について具体的にアドバイスするコメント。"
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

    print(f"\n✓ Batch 1205-1224 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
