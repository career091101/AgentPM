#!/usr/bin/env python3
"""
Batch 1005-1024の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
記事: 【2023年3月】質疑応答のまとめ（Instagram Q&A回答集）
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1005-1024の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1005,
        "filename": "image_181.png",
        "description": "K くんの質問に対する回答コメント。Twitter+インスタのマルチ運用で5000円程度のツイート作成から始めるアドバイスと、自動生成でなくスレッド形式で効果を高める方法の説明。"
    },
    {
        "index": 1006,
        "filename": "image_182.png",
        "description": "K くんによる質問1。出会い系インスタとTwitterの使い分けについて、マッチングアプリ攻略とメイン発信テーマの関連性を質問。"
    },
    {
        "index": 1007,
        "filename": "image_183.png",
        "description": "吉田からの詳細な回答。ラッテックルーキーのアフィリエイト文章改善方法や、プロフ導導線での文章体系設計、就活系インスタ運用でのファン化策について。"
    },
    {
        "index": 1008,
        "filename": "image_184.png",
        "description": "K くんへの回答続き。プロフィールからリンク先導線での文章体系、転職系インスタ活用の基礎ステップと具体的なマネタイズポイント説明。"
    },
    {
        "index": 1009,
        "filename": "image_185.png",
        "description": "ステラボール（セドリコンサル）からの質問。note作成時の構成・文章作成相談と、セドリジャンルで有益情報発信する3つの方法について。"
    },
    {
        "index": 1010,
        "filename": "image_186.png",
        "description": "K くん回答。セドリジャンルでの情報発信の3つの方法、noteコンサル後の想定と店舗運営との関連性、有名ブランド活用方法の説明。"
    },
    {
        "index": 1011,
        "filename": "image_187.png",
        "description": "Ayaka（収益10-20万ライバー向け情報発信中）からの質問。Twitterフォロワー増加方法とInstagram現況（36人フォロワー）からのランク上げ情報発信。"
    },
    {
        "index": 1012,
        "filename": "image_188.png",
        "description": "K くんによるAyakaへのマルチ運用回答。Twitterフォロワー増加ステップと、Instagramプロフ最適化、リール活用でのファン化について詳細説明。"
    },
    {
        "index": 1013,
        "filename": "image_189.png",
        "description": "Ayakaの回答感謝とInstagramでの成功事例共有。芸能人名言投稿でフォロワー10万増加、Twitterリバーコンサル活用でのフォロワー20人近く増加実績。"
    },
    {
        "index": 1014,
        "filename": "image_190.png",
        "description": "つき（ディズニーグッズメアアカウント36人フォロワー）からの質問。Instagramディズニー関連アカウント運用でのマネタイズ方法についての相談。"
    },
    {
        "index": 1015,
        "filename": "image_191.png",
        "description": "つきへのK くん回答。ディズニーテーマ運用でのTweet活用、ホテルライク家作りでのフォロワー4万人達成事例の紹介と、サジーのマネタイズ方法の説明。"
    },
    {
        "index": 1016,
        "filename": "image_192.png",
        "description": "mina（不動産ジャンル LINE資料使用）からの質問。Instagramでのホテルライク家紹介からのマネタイズについて、リール活用での効果測定相談。"
    },
    {
        "index": 1017,
        "filename": "image_193.png",
        "description": "K くんからmina向け回答。不動産ジャンルのLINEコンサル活用、フォーム活用、成果地点分析での発信方法とコンサル化の戦略説明。"
    },
    {
        "index": 1018,
        "filename": "image_194.png",
        "description": "まつもと（Discord コミュニティ構築中）からの質問。Discordコミュニティ運営の具体的な相談。Slack利用との比較やChat GPT活用での運営効率化の相談。"
    },
    {
        "index": 1019,
        "filename": "image_195.png",
        "description": "K くんからまつもと向け回答。Discord機能とSlack比較、メッセージ管理機能説明。Slackへの移管と計測機能、コンサル運営でのリーダーシップについて。"
    },
    {
        "index": 1020,
        "filename": "image_196.png",
        "description": "ナンミカ（フェムケアアカウント TikTok14万人）からの質問。Femmecareアイテム（Amazon アソシエイト）とオンラインビルでのマネタイズについて相談。"
    },
    {
        "index": 1021,
        "filename": "image_197.png",
        "description": "K くんからナンミカ向け回答。フェムケア市場でのAmazonアソシエイト活用、楽天マイルーム推奨理由、Amazonと楽天比較分析での戦略説明。"
    },
    {
        "index": 1022,
        "filename": "image_198.png",
        "description": "ナンミカの追加質問とK くん回答。PMS改善note活用、TikTok戦略相談での見出し作成要件。Twitter アカウント と TikTok アイコン統一相談。"
    },
    {
        "index": 1023,
        "filename": "image_199.png",
        "description": "ぶる（アカウントコンセプト『転職×婚活』で転職しながら婚活中）からの質問。転職キーワード「転職術」「婚活術」でのアカウント説明とマネタイズポイント相談。"
    },
    {
        "index": 1024,
        "filename": "image_200.png",
        "description": "K くんからぶる向け回答。Twitter モテ弁論でのビジネス系女性×男性狙い、女性転職でのInstagram 活動のコンセプト統一と具体的なアカウント例リスト紹介。"
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

    print(f"\n✓ Batch 1005-1024 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
