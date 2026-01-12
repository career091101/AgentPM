#!/usr/bin/env python3
"""
Batch 1745-1764の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1745-1764の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1745,
        "filename": "image_62.png",
        "description": "Instagram運用に関するDM相談のスクリーンショット。ユーザーがChatGPTの活用方法や難易度の低いジャンル選定についての質問に対する回答が表示されている。"
    },
    {
        "index": 1746,
        "filename": "image_63.png",
        "description": "Instagram運用の初期段階におけるフォロワー目標設定と商品選定についての相談スクリーンショット。フォロワー1000人以上達成による収益化の具体的なアドバイスが記載されている。"
    },
    {
        "index": 1747,
        "filename": "image_64.png",
        "description": "新規ユーザーのInstagramジャンル選定と運用戦略についての質問。22歳男性のプロフィール情報とマネタイズ目標、AIやビジネス系ジャンルへの適性について説明されている。"
    },
    {
        "index": 1748,
        "filename": "image_65.png",
        "description": "TikTok動画と回答を模した質疑応答。マッチングアプリ攻略のテーマについて、女性向けトークや実例を交えた具体的なコンテンツ設計のアドバイスが含まれている。"
    },
    {
        "index": 1749,
        "filename": "image_66.png",
        "description": "Instagram運用についての複数の質問と回答をまとめたテキスト形式のスクリーンショット。マッチングアプリジャンルの成功パターンとTikTokのジャンル選定についての実務的ガイドが表示されている。"
    },
    {
        "index": 1750,
        "filename": "image_67.png",
        "description": "マッチングアプリ攻略ジャンルの専門知識と実戦的なコンテンツ企画についての回答テキスト。恋愛系のリール作成方法とフォロワー層の心理分析についての詳細説明が記載されている。"
    },
    {
        "index": 1751,
        "filename": "image_68.png",
        "description": "Instagramコンセプト設定に関する複数の相談をまとめたスクリーンショット。恋愛ジャンルでのアカウント立ち上げ時の重要な判断軸についてのアドバイスが表示されている。"
    },
    {
        "index": 1752,
        "filename": "image_69.png",
        "description": "商品選定とマネタイズ戦略についての詳細な回答テキスト。無料診断から有料コンサルティングへの流れと、ジャンル選定時の稼ぎやすさについての説明が記載されている。"
    },
    {
        "index": 1753,
        "filename": "image_70.png",
        "description": "女性ターゲット層のInstagramアカウント戦略についての相談スクリーンショット。ジャンル選定とペルソナ設定、フォロワー層の心理についての実践的なアドバイスが含まれている。"
    },
    {
        "index": 1754,
        "filename": "image_71.png",
        "description": "複数のInstagramアカウント運用時のリール作成と投稿戦略についての回答。タイミング最適化とフォロワー増加の具体的な方法についてのガイドが表示されている。"
    },
    {
        "index": 1755,
        "filename": "image_72.png",
        "description": "初期段階のコーチングアカウント運用についての相談スクリーンショット。ジャンル選定から無料個別相談、有料Note提供までの流れについてのアドバイスが記載されている。"
    },
    {
        "index": 1756,
        "filename": "image_73.png",
        "description": "女性ターゲット向けInstagramアカウントの方向性についての質問と回答。夫婦ジャンルと恋愛ジャンルの選択、パートナーシップ定義についての詳細な説明が表示されている。"
    },
    {
        "index": 1757,
        "filename": "image_74.png",
        "description": "子育てと恋愛系ジャンルのInstagramアカウント戦略についての相談。複数ジャンルの同時運用とクライアント属性についてのアドバイスが記載されている。"
    },
    {
        "index": 1758,
        "filename": "image_75.png",
        "description": "子育てジャンルのInstagramアカウント運用についての詳細な回答テキスト。ペルソナ設定と具体的なコンテンツ企画、マネタイズ戦略についての実践的ガイドが表示されている。"
    },
    {
        "index": 1759,
        "filename": "image_76.png",
        "description": "マイホーム資金を目指すアカウント運用についての複数の質問と回答。異なる経歴や環境のユーザーからの相談内容と、実践的なジャンル選定のアドバイスが含まれている。"
    },
    {
        "index": 1760,
        "filename": "image_77.png",
        "description": "Instagram運用の目標設定と実績についての相談スクリーンショット。年100万円達成目標に関する具体的な質問と、投稿本数やアカウント戦略についてのアドバイスが記載されている。"
    },
    {
        "index": 1761,
        "filename": "image_78.png",
        "description": "恋愛系Instagramアカウントのアフィリエイト商品紹介とリール・フィード活用についての相談。初期段階の戦略とクライアント獲得方法についての実践的な説明が表示されている。"
    },
    {
        "index": 1762,
        "filename": "image_79.png",
        "description": "恋愛ジャンルのInstagram初期運用についての詳細な回答テキスト。リール作成方法とフォロワー獲得基準、ジャンル選定時の重要なポイントについてのガイドが記載されている。"
    },
    {
        "index": 1763,
        "filename": "image_80.png",
        "description": "複数のジャンル検討とアカウント初期設定についての相談スクリーンショット。子育てやダイエット、看護師転職などのジャンルに関する質問と実践的なアドバイスが含まれている。"
    },
    {
        "index": 1764,
        "filename": "image_81.png",
        "description": "Instagram運用の基本的なジャンル選定とマネタイズ戦略についての回答テキスト。子育てやダイエット関連のコンテンツ企画と、これらジャンルの収益性についての詳細な説明が記載されている。"
    },
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

    print(f"\n✓ Batch 1745-1764 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
