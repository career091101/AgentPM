#!/usr/bin/env python3
"""
Batch 1845-1864の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1845-1864の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1845,
        "filename": "image_11.png",
        "description": "インスタグラムのストーリーとフィードでの教育方法についてのユーザーからの質問スクリーンショット。基本的な商品販売ドリルやオンライン講義の方法についての相談内容。"
    },
    {
        "index": 1846,
        "filename": "image_12.png",
        "description": "ローカルビジネス（地方医療クリニック）のInstagram運用についての相談。初期段階でのフォロワー増加施策と月間投稿戦略の質問内容。"
    },
    {
        "index": 1847,
        "filename": "image_13.png",
        "description": "地域セグメント戦略とローカルビジネスのInstagram広告配信についてのアドバイス。クリニック開設前のプロモーション方法と広告配信タイミングの説明。"
    },
    {
        "index": 1848,
        "filename": "image_14.png",
        "description": "TikTokとYouTubeなどの複数プラットフォーム展開についての質問と回答。リール動画の再利用方法とプラットフォーム別最適化の具体的なテクニック。"
    },
    {
        "index": 1849,
        "filename": "image_15.png",
        "description": "スポーツ系アカウント運用と高利益化についてのユーザー相談。月70万円の売上を達成したビジネスアカウントの具体的な事例紹介。"
    },
    {
        "index": 1850,
        "filename": "image_16.png",
        "description": "マネタイズ方法の多様性（ブレインやコンサルティング販売）についての選択肢紹介。自分のコンテンツに合わせた収益化パターンの決定方法。"
    },
    {
        "index": 1851,
        "filename": "image_17.png",
        "description": "就活系アカウント運用とマネタイズの詳細についての質問と回答。月100万円の売上を目指す就活ジャンルの具体的なアプローチ方法。"
    },
    {
        "index": 1852,
        "filename": "image_18.png",
        "description": "Instagramアカウント設計の相談内容。恋愛系アカウントの取扱いと初期段階でのターゲット層の有効活用についてのアドバイス。"
    },
    {
        "index": 1853,
        "filename": "image_19.png",
        "description": "リール動画制作のテクニックについてのユーザーからの詳細な質問。YouTube動画の切り抜き方法と画像・内容編集の具体的なプロセス。"
    },
    {
        "index": 1854,
        "filename": "image_20.png",
        "description": "既存アカウント改善と新規アカウント立ち上げの判断についての相談。フォロワー数別の戦略見直しポイントとアカウント再構築の時期判断基準。"
    },
    {
        "index": 1855,
        "filename": "image_21.png",
        "description": "Instagramアカウント運用の悩みに対する改善提案。ストーリー間隔の調整やリール投稿の実践方法についての具体的なガイダンス。"
    },
    {
        "index": 1856,
        "filename": "image_22.png",
        "description": "新規フォロワー獲得戦略についての質問。セグメント分析を活かしたターゲット層の拡大方法と初期段階でのアカウント改善提案。"
    },
    {
        "index": 1857,
        "filename": "image_23.png",
        "description": "フォロワー数増加に関する相談と改善アドバイス。セグメント機能の活用やリール動画の継続投稿による成長戦略の説明。"
    },
    {
        "index": 1858,
        "filename": "image_24.png",
        "description": "ビジネス系Instagramアカウント運用による月50～100万円の売上実績例。ジャンル選定とフォロワー層の特性別マネタイズ方法。"
    },
    {
        "index": 1859,
        "filename": "image_25.png",
        "description": "複数プラットフォームでの同時展開戦略についての相談。TwitterとInstagramの連携運用とジャンル別のビジネス規模の目安。"
    },
    {
        "index": 1860,
        "filename": "image_26.png",
        "description": "Twitter運用とフォロワー企画の効果的な方法についての質問。テンプレート配布による見込み客の獲得と期限付きキャンペーンの設計方法。"
    },
    {
        "index": 1861,
        "filename": "image_27.png",
        "description": "フォロワー増加に関する最低限のハードルと企画実施の判断基準についての説明。ビジネス・ナンバ系アカウントの本質的な成長メカニズム。"
    },
    {
        "index": 1862,
        "filename": "image_28.png",
        "description": "Twitter運用についてのユーザーからの多角的な質問。フリーランスへの転職支援やコーチングビジネス展開の事例紹介。"
    },
    {
        "index": 1863,
        "filename": "image_29.png",
        "description": "フリーランス転職相談とアカウント構築についての質問内容。個人のスキル売却やコンサルティング商品の開発についての相談プロセス。"
    },
    {
        "index": 1864,
        "filename": "image_30.png",
        "description": "フリーランス向けのビジネス相談内容。ターゲット設定やペンチマーク分析を含む商品設計とコーチング商品開発のポイント。"
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

    print(f"\n✓ Batch 1845-1864 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
