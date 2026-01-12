#!/usr/bin/env python3
"""
Batch 625-644の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 625-644の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 625,
        "filename": "image_25.png",
        "description": "Kくんと@フミによるインスタ参入シャネルに関する質問応答。ブログとSNSやハイライトの収益化方法について、SNSでのハイライト作成のコツと投稿戦略が記載されている。"
    },
    {
        "index": 626,
        "filename": "image_26.png",
        "description": "Kくんが@フミへのアドバイスで、SNS×ブログで稼ぐ方法やシェアしたいコンセプト、書籍推薦（書籍のURL掲載）について説明している。"
    },
    {
        "index": 627,
        "filename": "image_27.png",
        "description": "フミと@Kくんの対話で、ブログ運営のハイライト作成と段階的な成長、書籍推薦とアカウント設定に関する相談が示されている。"
    },
    {
        "index": 628,
        "filename": "image_28.png",
        "description": "nutsとKくんの質問応答で、料理レシピサロンのイメージ作成に関する課題とその解決方法（イメージの差別化や独特性）について説明している。"
    },
    {
        "index": 629,
        "filename": "image_29.png",
        "description": "Instagramのストーリー投稿一覧画面。Kくんが開設している「料理レシピサロン」関連のハイライトが表示されており、毎月売上ターゲットと会員数が記載されている。"
    },
    {
        "index": 630,
        "filename": "image_30.png",
        "description": "Kくんとnutsの質問応答。ビジネス系サロン運営の戦略（マネタイズ方法、顧客チャネル、会員獲得方法）とTwitterフォロワー5000人以上の必要性について記載されている。"
    },
    {
        "index": 631,
        "filename": "image_31.png",
        "description": "Kくんがnutsへ説明した、ダイエットスイーツレシピのPW情報と、リーチ拡大施策（1）〜（3）のフォロワー増やす方法が記載されている。"
    },
    {
        "index": 632,
        "filename": "image_32.png",
        "description": "ごろうへいとKくんの質問応答で、インスタとTikTok活用のアドバイスと、フォロワー月間60000人→1500人の達成事例及び施策が説明されている。"
    },
    {
        "index": 633,
        "filename": "image_33.png",
        "description": "Kくんと@ごろうへいの対話で、TikTok運用に関するアドバイス（バズやすい投稿戦略、フォロワー増加の工夫、ハッシュタグの活用）が記載されている。"
    },
    {
        "index": 634,
        "filename": "image_34.png",
        "description": "Romuが@Kくんに相談した、ペットアカウント（Instagram115万人、YouTube7200万人）のマネタイズ戦略に関する質問が記載されている。"
    },
    {
        "index": 635,
        "filename": "image_35.png",
        "description": "Kくんが@Romuへ、ペット系アフィリエイト（ドックフード、ペット保険、A8netやnoteの活用）とマネタイズ方法について詳細に説明している。"
    },
    {
        "index": 636,
        "filename": "image_36.png",
        "description": "aiが@Kくんへシャンル変更に関する質問。自己啓発系のハッシュタグの選定と占いジャンルのコンセプト決定について相談している。"
    },
    {
        "index": 637,
        "filename": "image_37.png",
        "description": "Kくんが@aiへ、ジャンル変更時のスクリーニング方法と新規アプローチのコンサルティング、フォロワー層のエンゲージメント向上について回答している。"
    },
    {
        "index": 638,
        "filename": "image_38.png",
        "description": "aiとKくんの対話で、アカウントIDの切り替え判断基準と占いジャンルの投稿戦略、フォロワーのリーチ拡大に関する相談が記載されている。"
    },
    {
        "index": 639,
        "filename": "image_39.png",
        "description": "homeが@Kくんへ、ダイエットアカウント運営に関する質問。ストーリーのリアクションボタン（2択）と質問・リンクタップ数が多い理由について相談している。"
    },
    {
        "index": 640,
        "filename": "image_40.png",
        "description": "Kくんが@homeへ、iStepの導入方法（LINE登録、自動DMメッセージ配信）とフィード投稿の「保存」コメント活用、固定ピンの使い方について説明している。"
    },
    {
        "index": 641,
        "filename": "image_41.png",
        "description": "homeと@Kくんの対話で、ダイエットジャンルのテーマ選定（ビフォーアフター、新規視聴者向けフォローアップ）とフォロワー増加の工夫について説明している。"
    },
    {
        "index": 642,
        "filename": "image_42.png",
        "description": "かっぱ旅と@Kくんの相談で、海外旅行×女性一人旅向けコンセプトのフォロワーターゲット設定と30〜35歳向けの旅行コンテンツ戦略が記載されている。"
    },
    {
        "index": 643,
        "filename": "image_43.png",
        "description": "Kくんがかっぱ旅へ、海外旅行アカウントのターゲット層定義と年齢設定の判断基準、フォロワーのDMからのコミュニケーション方法について詳細に回答している。"
    },
    {
        "index": 644,
        "filename": "image_44.png",
        "description": "かっぱ旅と@Kくんの継続的な相談で、アカウント年齢層の設定判断とテーマ転換時の施策、フォロワー層の拡大戦略に関する具体的なアドバイスが記載されている。"
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

    print(f"\n✓ Batch 625-644 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
