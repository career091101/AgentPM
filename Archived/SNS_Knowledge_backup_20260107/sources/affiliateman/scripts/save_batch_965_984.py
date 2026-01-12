#!/usr/bin/env python3
"""
Batch 965-984の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
【2023年3月質疑応答のまとめ】の記事から20枚
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 965-984の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 965,
        "filename": "image_141.png",
        "description": "Kくんのインスタグラムコメント。転職・ワーママ・ブラック企業苦しい・仕事術（スキルアップ）に関する質問に対して、アフィリエイトや個人ビジネス向けの転職エージェント活用の提案と、web業界への転職方針についてのアドバイス。"
    },
    {
        "index": 966,
        "filename": "image_142.png",
        "description": "Kくんのコメント継続。転職・職歴なし（就職したことがない層）向けの課題解決方法について、アドバイスを提供している。フリーターやニート、既卒向けの転職エージェント活用と、CV設計について詳細に説明。"
    },
    {
        "index": 967,
        "filename": "image_143.png",
        "description": "onigirlユーザーのコメント。アカウント運用改善のための質問に対して、Kくんが10個のポイントを指摘（やはじめ、さいあく、といった形式で具体的な改善案を提示）。投稿内容向けの訴求や、ハイライト活用のコツについての回答。"
    },
    {
        "index": 968,
        "filename": "image_144.png",
        "description": "あるくのコメント。キャラ付けについての質問に対して、Kくんが検証方法を提案。例としてInstagramアカウント（@shirowani_kotoba）と、リール・フィード投稿のコンテンツバリエーションについての具体的なアドバイス。"
    },
    {
        "index": 969,
        "filename": "image_145.png",
        "description": "Kくんの追加解説。キャラ活用から始まるアカウント、リール主体での新規リーチとフィードやストーリーズへの導導、及び商品紹介リールの活用戦略についての詳細なコンサルティング内容。"
    },
    {
        "index": 970,
        "filename": "image_146.png",
        "description": "あおいユーザーのコメント。グルメ系アカウント運用について質問。Kくんが仙台グルメカフェの実例を提示し、プロフィール兼施策、朝・夜のリール発信タイミングとグルメ系マネタイズについてアドバイス。"
    },
    {
        "index": 971,
        "filename": "image_147.png",
        "description": "Kくんのアカウント選定についての回答。アカウントコンセプト・プロフィール兼施策・朝夜の投稿タイミングという3つのポイントについて、簡潔に整理した説明を提供している。"
    },
    {
        "index": 972,
        "filename": "image_148.png",
        "description": "リト転職系ユーザーのコメント。転職系アカウント選定に関して、リール主体での新規リーチとフィードやストーリーズへの導導についての質問。Kくんが検証方法とマネタイズアプローチについて複数の事例を提示。"
    },
    {
        "index": 973,
        "filename": "image_149.png",
        "description": "おゆきユーザーのコメント。結婚・恋愛・趣味関連のアカウント運用について、メンション機能の使い方やハイライト設定についての具体的な質問と改善提案。"
    },
    {
        "index": 974,
        "filename": "image_150.png",
        "description": "Kくんの返答。結婚・恋愛系のマネタイズに関して、フォロワー数よりも拡散性が重要であること、及びマネタイズ施策の複数パターン（おうままレシピ、アラサー恋愛、楽天関連）を提案。"
    },
    {
        "index": 975,
        "filename": "image_151.png",
        "description": "まさとユーザーのコメント。初期段階での3つの悩み（ネタに困ること、構成・デザイン、まとめ振り）に対して、Kくんが動画リサーチ方法と仮説検証プロセスについて詳細に解説。"
    },
    {
        "index": 976,
        "filename": "image_152.png",
        "description": "香ユーザーのコメント。アカウント選定戦略について複数の質問（節約術・おうままレシピ・楽天など）。Kくんが各ジャンルの月5000～500万円の範囲のマネタイズアカウント事例を紹介。"
    },
    {
        "index": 977,
        "filename": "image_153.png",
        "description": "つるぎユーザーのコメント。マーケコンサルティングとしての知人のアカウント凍結と復活方法について。Kくんが複数通報対策とアカウント復活の可能性についての見解と、ビジネス系・マンアフィの活用戦略を提案。"
    },
    {
        "index": 978,
        "filename": "image_154.png",
        "description": "おゆきユーザーの追加質問。リール・メンション頻度、ハッシュタグ検索、インスタの使い方についての複数の疑問に対してKくんが詳細に解答している。"
    },
    {
        "index": 979,
        "filename": "image_155.png",
        "description": "Kくんの追加説明。リール・メンションの発信頻度と効果について、フィード投稿とストーリーズのタイミング・キャプションのキーワード選定の方法を詳細に解説。"
    },
    {
        "index": 980,
        "filename": "image_156.png",
        "description": "SNSの王子様に関する注記セクション。インスタメンション機能の説明とKくんのプロフィールリンク。ロゴ画像（Kくんのアイコン）を含むインスタグラム向けサービス紹介。"
    },
    {
        "index": 981,
        "filename": "image_157.png",
        "description": "ペイユーザーのコメント。初期アカウント運用についての複数の質問（フィード投稿タイミング、リール掲載タイミング、ストーリーズ投稿）に対して、Kくんが初期段階でのストーリーズ戦略とテストアプローチを提案。"
    },
    {
        "index": 982,
        "filename": "image_158.png",
        "description": "ななかユーザーのコメント。エロ系アカウント考案に関する複数の質問（オフOO系、拡散性）に対して、Kくんがフォロワー数と拡散性の関係、コンプライアンス対策についての詳細なアドバイス。"
    },
    {
        "index": 983,
        "filename": "image_159.png",
        "description": "ななかユーザーの追加質問。フォロー・購入の双方向指標とエンゲージメント低下の理由についての質問。Kくんがツイッターとインスタの投稿戦略の違いと、長期的なアカウント戦略についてのアドバイス。"
    },
    {
        "index": 984,
        "filename": "image_160.png",
        "description": "Dユーザーのコメント。Twitterアカウント発信に関する質問（https://twitter.com/ryo100days）とインスタとTwitterの戦略の違いについて。Kくんが講師業務とリトイート戦略、フォロワー増加の具体的な方法について提案。"
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

    print(f"\n✓ Batch 965-984 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
