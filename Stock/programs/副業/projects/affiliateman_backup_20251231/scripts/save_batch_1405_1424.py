#!/usr/bin/env python3
"""
Batch 1405-1424の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1405-1424の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1405,
        "filename": "image_83.png",
        "description": "アメブロ記事の特典に関する質問と回答。記事内の特典アメブロ記事をプレゼント時に販売中止にできるか、別途販売できるかなどの質問とそれに対するK君の詳しい回答。"
    },
    {
        "index": 1406,
        "filename": "image_84.png",
        "description": "K君による稼ぐ系のプロフィール設計に関するアドバイス。フォロワー数よりも有料商材のブランドを重視する重要性と、Brainでの販売戦略に関する詳細な解説。"
    },
    {
        "index": 1407,
        "filename": "image_85.png",
        "description": "ゆんによるアメブロ記事掲載とBrainアカウント運用に関する複雑な質問と、それに対するK君による充実した回答。アメブロと別事業との記事リンク設定の工夫やアメブロ記事の記載方法に関する詳細。"
    },
    {
        "index": 1408,
        "filename": "image_86.png",
        "description": "tips販売とアメブロの関係性に関する質問応答。Twitterでの宣伝タイミングや記事非公開化による収益チャンス喪失の懸念と、K君のログインカテゴリ表示の仕組みについての説明。"
    },
    {
        "index": 1409,
        "filename": "image_87.png",
        "description": "Tipsログイン時のカテゴリ表示と他者の記事表示に関する質問。ビジネスカテゴリでのシロウさんのTwitterアフィリエイト記事表示について、K君がコンテンツ運営の課題を指摘。"
    },
    {
        "index": 1410,
        "filename": "image_88.png",
        "description": "aoiユーザーによるTwitterフォローアップの質問と、K君の充実した回答。無料LINE配布戦略、Tipsでのサムネ画像の成果レポート写真撮載、アフィリエイト施策など多面的なアドバイス。"
    },
    {
        "index": 1411,
        "filename": "image_89.png",
        "description": "aoiによる無料プレゼントコンテンツの販売可能性と、YouTube・note併用戦略に関する質問。K君が有料販売でのコンテンツレベル設定と情報販売の収益化について詳しく解説。"
    },
    {
        "index": 1412,
        "filename": "image_90.png",
        "description": "aoiがTwitterアフィリエイトでの実績報告。noteでのフォロワー施策や無料LINE配布戦略、YouTubeマネタイズの検討など複数の収益施策を同時進行中。"
    },
    {
        "index": 1413,
        "filename": "image_91.png",
        "description": "あおによるTwitterアカウント設計に関する複数の質問。ChatGPTプロンプト活用法、初期記事内容の戦略、投稿とフォロー併行時の注意点について、K君が実践的なアドバイスを提供。"
    },
    {
        "index": 1414,
        "filename": "image_92.png",
        "description": "K君によるChatGPT活用とTwitter戦略に関する回答。インスタリールとGPT活用の連携、ChatGPTプロンプト集の重要性、リンク設定の工夫について詳細に解説。"
    },
    {
        "index": 1415,
        "filename": "image_93.png",
        "description": "あおとK君のTwitter戦略に関する対話。GPXインスタリール100万再生の理論や投稿と固定ツイートの役割分担、AIツール活用による時間短縮の工夫。"
    },
    {
        "index": 1416,
        "filename": "image_94.png",
        "description": "ブログとnote併用戦略に関する質問。AIインスタ化による運用効率化、コンテンツ販売とnoteの位置付け、コドックツール紹介に関するやり取り。"
    },
    {
        "index": 1417,
        "filename": "image_95.png",
        "description": "あいすからのTwitterフォロワー施策に関する相談。「お手数ですが」と丁寧に投げかけた複数の質問について、K君が充実したアドバイスを提供。"
    },
    {
        "index": 1418,
        "filename": "image_96.png",
        "description": "あいすからのコンテンツ運営に関する実践的な質問。ブログメリット・コンテンツ販売・noteマネタイズなど、包括的な収益化戦略に関するK君の詳細回答。"
    },
    {
        "index": 1419,
        "filename": "image_97.png",
        "description": "ありいすによるTikTok運用の課題相談。TikTokでのペルソナ設定困難さ、AI美女マネタイズ戦略、Instagramビジネスアカウント活用との違いについてK君が実例を交えて解説。"
    },
    {
        "index": 1420,
        "filename": "image_98.png",
        "description": "ふっきーによるTikTok基本設定に関する質問。メンズコスメジャンル参入時のポイント、アカウント作成時の注意点、音声系・美容系ジャンル選択に関するアドバイス。"
    },
    {
        "index": 1421,
        "filename": "image_99.png",
        "description": "みのによるInstagram運用とコンサルティング戦略に関する相談。月5万円収益達成、ノウハウ販売と集客戦略、Brain・コンテンツ販売を通じた売上拡大の道筋について詳細に協議。"
    },
    {
        "index": 1422,
        "filename": "image_100.png",
        "description": "K君によるみのの相談への回答。アドバイス実行による成果、売上構成の多面化、コンテンツ販売と有料noteの使い分けについての具体的なガイダンス。"
    },
    {
        "index": 1423,
        "filename": "image_101.png",
        "description": "K君によるTwitterアフィリエイトと固定ツイート戦略に関する解説。アカウント凍結リスク、リード獲得戦略、noteでの高単価販売に関する実践的なアドバイス。"
    },
    {
        "index": 1424,
        "filename": "image_102.png",
        "description": "アカウント凍結対策とクラウドワークス・SNS運用に関する総合的なQ&A。ハイリスク行動の回避、低リスク副業戦略、Instagramビジネス教材売上と販売チャネル最適化について。"
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

    print(f"\n✓ Batch 1405-1424 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
