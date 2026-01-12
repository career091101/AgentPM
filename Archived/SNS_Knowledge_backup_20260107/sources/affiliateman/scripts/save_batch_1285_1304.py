#!/usr/bin/env python3
"""
Batch 1285-1304の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
2025-12-29実行
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1285-1304の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1285,
        "filename": "image_105.png",
        "description": "Instagramのコメント欄。ユーザー「ryu」がK君に、コミュニティ作りやスラック導入についての質問をしている。サロンのセキュリティ面やメアド認証に関する複数の質問が記載されている。"
    },
    {
        "index": 1286,
        "filename": "image_106.png",
        "description": "K君による長めの返信。公式ラインでの無料コンテンツ配布、公式ラインでのサロン告知、サロン登録についての段階的な説明が記載されている。"
    },
    {
        "index": 1287,
        "filename": "image_107.png",
        "description": "Instagram投稿内のテキスト。月額制サロン導入についての質問で、スクエアやペライチ、ストライプなどのサービス選択やカード情報管理について記載。"
    },
    {
        "index": 1288,
        "filename": "image_108.png",
        "description": "ユーザー「りく」からの新規相談投稿。100日婚活企画をテーマにした新規アカウント開設、20-30代向けの婚活・旅行ジャンル、ビジネス系マネタイズについての質問。"
    },
    {
        "index": 1289,
        "filename": "image_109.png",
        "description": "K君からりくへの返信。マネタイズ方法についての複数オプション、カップル向けコンテンツ、マッチングアプリ活用についての説明。"
    },
    {
        "index": 1290,
        "filename": "image_110.png",
        "description": "ユーザー「T」からの初心者向け質問。美容サロンアカウント、Twitter経営、複数アカウント運用の3つについてアドバイスを求めている。"
    },
    {
        "index": 1291,
        "filename": "image_111.png",
        "description": "K君からの返信。美容フェイシャルサロン関連のInstagramアカウント紹介、Twitter経営者ビジネス系説明、コンサル提案についての記載。"
    },
    {
        "index": 1292,
        "filename": "image_112.png",
        "description": "ユーザー「れん.くく」からの相談。Twitter恋愛アカウント運営でのインプレッション課題、マネタイズ方法についての複数の質問が表示されている。"
    },
    {
        "index": 1293,
        "filename": "image_113.png",
        "description": "ユーザー「そら」からの詳細な相談。iPhone便利術発信で、メイン垢フォロワー3万、TikTok3.5万、マネタイズで月50万達成についての説明。"
    },
    {
        "index": 1294,
        "filename": "image_114.png",
        "description": "K君からそらへの返信。月50万到達のマネタイズ方法、資産性重視の戦略、ビジネス系展開、アフィリエイト活用についての詳細アドバイス。"
    },
    {
        "index": 1295,
        "filename": "image_115.png",
        "description": "ユーザー「L」からの質問。Twitter有料noteビジネス化について、Tips商品の作成方法と競馬予想サロン運営・マネタイズについて記載。"
    },
    {
        "index": 1296,
        "filename": "image_116.png",
        "description": "K君からLへの返信。SNSを活用した競馬ジャンル稼ぎ方、Tips販売戦略、Tipsビジネスの上げ方についての詳細説明。"
    },
    {
        "index": 1297,
        "filename": "image_117.png",
        "description": "ユーザー「しば」からの質問。プログラミング学習ジャンルでのマネタイズ、Twitterでの発信、noteでの販売実績についての複数相談。"
    },
    {
        "index": 1298,
        "filename": "image_118.png",
        "description": "K君からの長い返信。プログラミング学習ジャンル月100万超のマネタイズ戦略、ジャンル選択、相対的メリットについての詳細説明。"
    },
    {
        "index": 1299,
        "filename": "image_119.png",
        "description": "Skill Hacksプログラミング講座の広告。動画でプログラミングを学べるオンラインスクールのロゴとキャッチコピー表示。"
    },
    {
        "index": 1300,
        "filename": "image_120.png",
        "description": "複数ユーザーとのコメント返信。K君とユーザー間でのLINE相談、noteプレゼント、無料コンテンツ配布についての質問と回答。"
    },
    {
        "index": 1301,
        "filename": "image_121.png",
        "description": "ユーザー「しば」からのTwitter・noteアカウント情報投稿。プログラミング学習ジャンル、Twitter・note販売についての自身の実績説明。"
    },
    {
        "index": 1302,
        "filename": "image_122.png",
        "description": "K君からのプログラミング教材提案。Skill Hacksオンラインスクール、月100目標達成、note販売上げ方についての詳細アドバイス。"
    },
    {
        "index": 1303,
        "filename": "image_123.png",
        "description": "ユーザーとマーティーのTwitter投稿連携。Twitter Tips販売での月100万稼ぎ方、マネタイズ戦略、ビジネス系ツイート発信についての説明。"
    },
    {
        "index": 1304,
        "filename": "image_124.png",
        "description": "ユーザー「すや」からの相談。iPad便利術をテーマにしたInstagram運用、マネタイズ方法、月収目標設定についての質問内容。"
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

    print(f"\n✓ Batch 1285-1304 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
