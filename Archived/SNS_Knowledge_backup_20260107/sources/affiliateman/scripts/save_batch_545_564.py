#!/usr/bin/env python3
"""
Batch 545-564の画像説明を保存
【2023年1月】質疑応答まとめ（Twitter・TikTok）
実際に画像を読み込んだ内容から詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 545-564の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 545,
        "filename": "image_01.png",
        "description": "「【2023年1月】質疑応答まとめ（Twitter・TikTok）」の記事のバナー画像。記事タイトルと関連する質問回答コンテンツのインデックスを視覚的に示すメインビジュアル。"
    },
    {
        "index": 546,
        "filename": "image_02.png",
        "description": "Twitterユーザー「joker」(@KKくん）による、Twitter×noteでの売上構築に関する最初の質問スレッド。note内のコンテンツ構築、フォロワー獲得のタイミング、質の高いコンテンツ発信についての具体的な相談。"
    },
    {
        "index": 547,
        "filename": "image_03.png",
        "description": "Twitterユーザー「Kくん」(@joker）からの返答。個人ブランド構築の重要性、プラットフォーム毎の戦略分化、note特化、インスタ特化など複数の特化路線の提案を示すテキスト。"
    },
    {
        "index": 548,
        "filename": "image_04.png",
        "description": "Twitterユーザー「どーぷ」（@KKくん）による、Twitter運用とマネタイズに関する二つの具体的な質問スレッド。借金対象キャッシュ化とnote・ブログでのマネタイズ戦略についての相談。"
    },
    {
        "index": 549,
        "filename": "image_05.png",
        "description": "「どーぷ」による追加質問。貯金ゼロからの資産形成とマインドセット構築、サイドビジネス系ファクタリング・証券などの具体的な相談内容を示すスレッド。"
    },
    {
        "index": 550,
        "filename": "image_06.png",
        "description": "Twitterユーザー「くろの」による、Twitter運用の初期段階についての相談。モーメント機能廃止、note・ブログ・ツイッターの特化戦略、ツイート戦略についての質問。"
    },
    {
        "index": 551,
        "filename": "image_07.png",
        "description": "「くろの」への返答。FireShot Captureのスクリーンショット、note活用の具体的なシナリオ、ブログでのアフィリエイト、プレイサイト活用についての複数の提案を含むスレッド。"
    },
    {
        "index": 552,
        "filename": "image_08.png",
        "description": "Twitterユーザー「るな」（@KKくん）による、インスタデザイン発信に関する質問。フォロワー増加の理由、デザイナー界限での認識差別について、実装内容とデザイン構築の悩みを述べるスレッド。"
    },
    {
        "index": 553,
        "filename": "image_09.png",
        "description": "「るな」への複数の回答。発信内容がデザイナー界限でバズっている理由、フォロワー減少の要因、プロフィール改善施策、1日1ツイートの投稿頻度についての具体的なアドバイス。"
    },
    {
        "index": 554,
        "filename": "image_10.png",
        "description": "Twitterユーザー「しろあん」（@KKくん）による、Twitterアカウントのフォロバ状況に関する長篇の相談。フォロワー1000-5500人の段階での悩み、新規アカウント作成とプロフ改善についての質問。"
    },
    {
        "index": 555,
        "filename": "image_11.png",
        "description": "「しろあん」の複数の返答とKKくんの回答。転生アカウントの戦略、1%以上の転生率、アフィリエイト運用、Twitter攻略の具体的なテクニックと事例の紹介。"
    },
    {
        "index": 556,
        "filename": "image_12.png",
        "description": "Twitterユーザー「じん」（@KKくん）による、Twitterアカウント設計に関する質問。外見コンサル、ビジネス系アカウント構築、ツイート内容とプロフィール連携についての相談スレッド。"
    },
    {
        "index": 557,
        "filename": "image_13.png",
        "description": "Twitterユーザー「L'n」（@KKくん）による、Twitter新規アカウント運用についての相談。2点質問として、外見コンサル、ビジネス系情報インプット、Twitter応援部屋でのフォロワー増加についての質問。"
    },
    {
        "index": 558,
        "filename": "image_14.png",
        "description": "Twitterスレッド内のテキスト説明。フォロワー増加の理由、SNS運用フガについてのK氏の複数の相談内容（共感、貫禄、複合分析）と、ビジネス系ジャンルの詳細戦略についての記述。"
    },
    {
        "index": 559,
        "filename": "image_15.png",
        "description": "Twitterユーザー「しゅん」（@KKくん）による、TikTokとインスタのマネタイズについての相談。ショート動画中心、占いアカウント運用、現在のマネタイズ導線の構築についての具体的な質問。"
    },
    {
        "index": 560,
        "filename": "image_16.png",
        "description": "「しゅん」への複数の回答。TikTok攻略の基本戦略、LINE公式導入、クレカのFP相談、占いジャンルの実例（@松盗歩など）とマネタイズ方法の提案を含むスレッド。"
    },
    {
        "index": 561,
        "filename": "image_17.png",
        "description": "Twitterスレッド内のテキスト記述。TikTok運用のリスト戦略、占い系アカウントのマネタイズ、有料鑑定、LINEコンサルの関連リンクと実例アカウント（@松盗歩）のTwitterプロフ紹介。"
    },
    {
        "index": 562,
        "filename": "image_18.png",
        "description": "Twitterユーザー「かな」（@KKくん）による、女性向けアフィリエイト運用についての質問。現在のアカウント状態、ZOOMでの20万円マネタイズ、ロードマップ設計についての相談。"
    },
    {
        "index": 563,
        "filename": "image_19.png",
        "description": "「かな」への複数の回答。パズルアプリ、マネタイズ戦略、OLのルーティン動画企画、6つの外見ケアテーマ（OLのタイトルルーティン、コスメ、美容ルーティンなど）の提案を含むスレッド。"
    },
    {
        "index": 564,
        "filename": "image_20.png",
        "description": "Twitterユーザー「よし」（@KKくん）による最後の質問スレッド。Twitter・インスタの女性向けコンサル運用、ZOOM成約、タロット占いの相談申し込みについての記述を含む結論セクション。"
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

    print(f"\n✓ Batch 545-564 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
