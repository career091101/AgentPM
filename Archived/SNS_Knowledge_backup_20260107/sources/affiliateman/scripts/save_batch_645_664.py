#!/usr/bin/env python3
"""
Batch 645-664の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
【2023年2月】質疑応答のまとめ記事から20枚
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 645-664の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 645,
        "filename": "image_45.png",
        "description": "K君とかつお旅ユーザーの返信スレッド。年齢と情報提供についてのやり取りと、InstagramのDM営業戦略についての質問と回答。"
    },
    {
        "index": 646,
        "filename": "image_46.png",
        "description": "omoユーザーのドライヘッドスパサロン運営相談。集客方法（Instagramタグラム）と予約フロー（LINE登録）についての詳細質問。"
    },
    {
        "index": 647,
        "filename": "image_47.png",
        "description": "omoユーザーへのK君の詳細回答。ドライヘッドスパサロンのターゲット分析（女性特化・個人サロン vs 鍼灸サロン）と戦略について。"
    },
    {
        "index": 648,
        "filename": "image_48.png",
        "description": "omoユーザーへの追加アドバイス。Zoomグループコンサル参加の提案と、アカウント参考例（ideal.meguro他）の提示。"
    },
    {
        "index": 649,
        "filename": "image_49.png",
        "description": "K君のomoへの継続アドバイス。プロフィール改編の重要性、テーザー女性向けビジネス、コンセプト設定についての戦略。"
    },
    {
        "index": 650,
        "filename": "image_50.png",
        "description": "K君のomoへの最終回答。シャンル10選の紹介と、発信者がターゲットとなるジャンル選定についての具体的アドバイス。"
    },
    {
        "index": 651,
        "filename": "image_51.png",
        "description": "ミントユーザーの企業Instagramマネタイズ相談。個人アカウントと企業アカウントの使い分けについての3つの質問。"
    },
    {
        "index": 652,
        "filename": "image_52.png",
        "description": "K君のミントへの回答。企業アカウント選用の理由と、個人サロン vs 鍼灸サロンの差別化ポイントについて。"
    },
    {
        "index": 653,
        "filename": "image_53.png",
        "description": "ひなユーザーのセラピストスクール講師相談。クライアントアカウント運用とセラピスト講師参考例についての複数質問。"
    },
    {
        "index": 654,
        "filename": "image_54.png",
        "description": "K君のひなへの詳細回答。セラピストスクール講師向けの投稿内容カテゴリ（技術面・売上・参考アカウント）についての指導。"
    },
    {
        "index": 655,
        "filename": "image_55.png",
        "description": "もなユーザーの入会者相談。マネタイズ戦略とコンセプト設定、子育てジャンル運用についての詳細な長文質問。"
    },
    {
        "index": 656,
        "filename": "image_56.png",
        "description": "K君のもなへの回答。マネタイズ方法（PR・アフィリエイト vs コンテンツ販売）とコンセプト設定についての具体的戦略。"
    },
    {
        "index": 657,
        "filename": "image_57.png",
        "description": "もなユーザーへの追加アドバイス。コンテンツ販売の商品設計に関するYouTube動画参考例と、noteコンサル活用について。"
    },
    {
        "index": 658,
        "filename": "image_58.png",
        "description": "もなユーザーへの継続相談。投稿内容の改善とアフィリエイト子育てジャンル選定についての質問と回答スレッド。"
    },
    {
        "index": 659,
        "filename": "image_59.png",
        "description": "ぶるぶるユーザーのiPhoneアプリ動画投稿相談。iPhone2アプリ6ガジェット活用と、Instagramとテラスの投稿戦略についての質問。"
    },
    {
        "index": 660,
        "filename": "image_60.png",
        "description": "りょうユーザーのアフィリエイト相談。ガジェット系アフィリエイトの選択肢（ミイダス・VIEW・アプリDL）と成果地点の説明。"
    },
    {
        "index": 661,
        "filename": "image_61.png",
        "description": "しんやユーザーの新規アカウント開設相談。アカウント目的設定と自己啓発コーチング、ターゲット設定についての3つの質問。"
    },
    {
        "index": 662,
        "filename": "image_62.png",
        "description": "K君のしんやへの詳細回答。ニーズ選定・自己啓発コーチング・自己啓発ジャンル選択肢（恋愛系・仕事系など）についての戦略。"
    },
    {
        "index": 663,
        "filename": "image_63.png",
        "description": "おゆきユーザーの新規会話。フォロー戦略とフォロワー周り、不動産物件情報発信についての4つの具体的質問。"
    },
    {
        "index": 664,
        "filename": "image_64.png",
        "description": "K君のおゆきへの回答。フォロー戦略の重要性と、参考資料（Instagram参考例とaffiliatemanサイト）の提示。"
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

    print(f"\n✓ Batch 645-664 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
