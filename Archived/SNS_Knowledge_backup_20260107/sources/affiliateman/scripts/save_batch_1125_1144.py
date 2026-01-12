#!/usr/bin/env python3
"""
Batch 1125-1144の画像説明を保存
実際に画像を読み込んで詳細な説明を生成（【2023年4月】質疑応答のまとめ記事 20枚）
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1125-1144の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1125,
        "filename": "image_91.png",
        "description": "Instagramコメント機能での質問・相談内容の例。usagiユーザーがコスメ系アカウント運用について、リーチ強化・コンセプト設計・ルール運用などの多角的な相談をしている質問スクリーンショット。"
    },
    {
        "index": 1126,
        "filename": "image_92.png",
        "description": "ぶろぶろユーザーがTikTok→LINE誘導・Twitter×TikTok戦略について相談した回答内容。フォロワー5000程度でのリリット活用法や、複数SNSの連携活用方法を詳しく説明している。"
    },
    {
        "index": 1127,
        "filename": "image_93.png",
        "description": "ぶろぶろユーザーのTwitter凍結に関する相談と、CC運営からのアカウント復旧方法・DM送信頻度制限などについての回答内容。"
    },
    {
        "index": 1128,
        "filename": "image_94.png",
        "description": "ぶろぶろユーザーがTwitterアカウント凍結期間中の対策・フリーランスアカウント運用についての相談内容。DMメッセージ制限やツイモーター結論などについて質問している。"
    },
    {
        "index": 1129,
        "filename": "image_95.png",
        "description": "トヨユーザーがnoteのPV減少についてTwitterアルゴリズム変更の影響を相談。Twitterimpの要因・投稿タイミング・コンテンツ内容に関する複数の質問が含まれている。"
    },
    {
        "index": 1130,
        "filename": "image_96.png",
        "description": "吉田ユーザーが転職アカウントTwitter運用について、初心的な質問と教育投稿の入れ始めについて相談している複数の質問スクリーンショット。"
    },
    {
        "index": 1131,
        "filename": "image_97.png",
        "description": "吉田ユーザーへの回答内容。フォロワーが個人以上になれば教育の投稿を入れ始める・他SNS比較・ハンドルの高さについての詳しい解説。"
    },
    {
        "index": 1132,
        "filename": "image_98.png",
        "description": "CC運営からの転職系アカウント運用についての詳細な回答。他SNSとTwitterの併用戦略・ティーク形式・プレゼント企画などについて多角的なアドバイスを提供している。"
    },
    {
        "index": 1133,
        "filename": "image_99.png",
        "description": "moto運営（Twitter転職採用アカウント）のプロフィール情報。1987年生まれで、リクルートやベンチャー企業での転職経験、著書「転職と副業のかけ算」などを紹介している。"
    },
    {
        "index": 1134,
        "filename": "image_100.png",
        "description": "吉田ユーザーへの詳細な回答。集客フロー（TikTok→Twitter→LINE教育）・LINE追加前のLP選定・各プラットフォームのコンテンツ戦略の違いについて詳しく説明している。"
    },
    {
        "index": 1135,
        "filename": "image_101.png",
        "description": "CC運営からの追加回答。TikTokでの集客→Twitterでの流入→LINE相談の流れ、LP選定基準、ブログ活用方法についての詳細な解説。"
    },
    {
        "index": 1136,
        "filename": "image_102.png",
        "description": "KKくんからぶろぶろユーザーへの回答。集客フロー・タキトさんの対談動画の紹介・ライティング×マーケティング領域のコンテンツについての提案。"
    },
    {
        "index": 1137,
        "filename": "image_103.png",
        "description": "ぶろぶろユーザーへの有志投稿の作り方についての回答内容。内容をメモに書いてスクショ・リプライ誘導・プロフィール誘導などの具体的な戦略を複数提案している。"
    },
    {
        "index": 1138,
        "filename": "image_104.png",
        "description": "Romuユーザーが投資撮影・LINE取得ベストプラクティスについて相談した内容。プロフィール・noteプレゼント・リツイート式でのLINE誘導などの3つの施策について説明。"
    },
    {
        "index": 1139,
        "filename": "image_105.png",
        "description": "Romuユーザーへの回答。Twitter・YouTubeの併用戦略・アドサーの選定方法・Web/SNS系での発信ジャンルについての詳細なアドバイス。"
    },
    {
        "index": 1140,
        "filename": "image_106.png",
        "description": "CC運営からRomuユーザーへの回答。YouTubeチャンネルマネタイズ・ファンの属性分析・販売商品の選定方法についての詳しい戦略説明。"
    },
    {
        "index": 1141,
        "filename": "image_107.png",
        "description": "KKくんからマーティーユーザーへの回答。Kindleコンサル・講座構成・シニア向けWebビジネス・LP制作ライティングについての複数の相談への答え。"
    },
    {
        "index": 1142,
        "filename": "image_108.png",
        "description": "マーティーユーザーへの詳細な回答。アイコン修正・キャラ選定・参考アカウント紹介・ライティング極めについてのアドバイス。"
    },
    {
        "index": 1143,
        "filename": "image_109.png",
        "description": "KKくん・マーティーユーザー間での複数の相談回答。LP制作ライティング・アイコンの重要性・ニッチジャンル選定・セルフコンサル活用などについての対話内容。"
    },
    {
        "index": 1144,
        "filename": "image_110.png",
        "description": "きなこユーザーがTikTok×インスタグラム融合・エポスカードアフィリエイト・マネタイズ戦略について相談した内容。CVRや最適なサロン選定についての複数の質問スクリーンショット。"
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

    print(f"\n✓ Batch 1125-1144 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
