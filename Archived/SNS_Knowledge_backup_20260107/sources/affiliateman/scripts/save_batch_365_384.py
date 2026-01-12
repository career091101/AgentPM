#!/usr/bin/env python3
"""
Batch 365-384の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 365-384の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 365,
        "filename": "image_20.png",
        "description": "SNS攻略サロン限定の11月度質疑応答まとめタイトル画像。ロケット・惑星アイコンとともに「インスタ/TIKTOK/Twitter」の対応プラットフォーム表記、キャラクターイラスト付き。"
    },
    {
        "index": 366,
        "filename": "image_21.png",
        "description": "SNSの有益情報公開と運用知識まとめのタイトル。2022年7-9月分のSNS運用役立ち情報をまとめたコンテンツの表紙。パープル背景に笑顔のキャラクターイラスト付き。"
    },
    {
        "index": 367,
        "filename": "image_22.png",
        "description": "SNS運用知識まとめのタイトル。2022年10月分のSNS運用超役立ち情報をまとめた資料の表紙。パープル背景に笑顔のキャラクターと惑星アイコン付き。"
    },
    {
        "index": 368,
        "filename": "image_23.png",
        "description": "Instagramに関する質問回答まとめのタイトル。2022年7-9月分のインスタグラム質疑応答を集約した資料。疑問符アイコンとキャラクターイラスト付き。"
    },
    {
        "index": 369,
        "filename": "image_01.png",
        "description": "SNS攻略サロン限定の12月度質疑応答まとめタイトル。サンタクロースキャラクターと赤いドット装飾、「インスタ/TIKTOK/Twitter」対応プラットフォーム表記。"
    },
    {
        "index": 370,
        "filename": "image_02.png",
        "description": "インスタグラムのリール運用に関するフォロワー増加技についての質問と回答。動画リール8本再生でフォロワー獲得の実例と、シャドウバンの可能性についての相談スレッド。"
    },
    {
        "index": 371,
        "filename": "image_03.png",
        "description": "ガーデニング系アカウント運用についての相談スレッド。月20万円稼ぐアカウント構築の相談、フォロワー数と収益化の関連性、SNSツール活用についての質問と回答。"
    },
    {
        "index": 372,
        "filename": "image_04.jpg",
        "description": "ビジネス向けスーツを着た女性の半身イラスト。シンプルなミニマルデザインで、プロフェッショナルなビジネスパーソンの象徴。"
    },
    {
        "index": 373,
        "filename": "image_05.png",
        "description": "不動産投資系アカウント構築についての質問スレッド。ターゲット設定、投資用不動産の所有者層への発信方法、インスタとSNS媒体の選択についての相談。"
    },
    {
        "index": 374,
        "filename": "image_06.png",
        "description": "フォロワー獲得施策についての質問と回答。ストーリーのメッションでのアカウント紹介、フォロワー数と質の関連性、キャラクター選択による集客効果について。"
    },
    {
        "index": 375,
        "filename": "image_07.png",
        "description": "夫婦関係改善アカウント構築についての相談スレッド。ターゲット設定、アウトプット方法、ジャンル市場規模、プロダクト販売戦略についての具体的なアドバイス。"
    },
    {
        "index": 376,
        "filename": "image_08.png",
        "description": "夫婦関係改善ジャンルのマネタイズについての相談。ジャンルの難易度、アフィ活用方法、オフライン展開、参加者募集のポイント等についての詳細な回答。"
    },
    {
        "index": 377,
        "filename": "image_09.png",
        "description": "ジャンル市場規模とマネタイズ効率についての相談。ジャンル選択の重要性、コンテンツ形式、アスリート系投稿の収益化についての戦略的なアドバイス。"
    },
    {
        "index": 378,
        "filename": "image_10.png",
        "description": "スポーツトレーナーのマネタイズについての長文相談スレッド。タイトル設定、ジャンルの難易度、投稿内容の専門性維持についての詳細な回答内容。"
    },
    {
        "index": 379,
        "filename": "image_11.png",
        "description": "スポーツトレーナーアカウントのタイトル・コンテンツ方針についての回答。ジャンル競争状況、マネタイズの容易性、サムネ修正提案についての具体的なアドバイス。"
    },
    {
        "index": 380,
        "filename": "image_12.png",
        "description": "ダイエット関連投稿の構成と運用方針についての相談。科学的根拠の必要性、アスリート専用テーマ、自己体験レベルでの発信についての回答。"
    },
    {
        "index": 381,
        "filename": "image_13.png",
        "description": "ペット系（犬）の投稿マネタイズについての相談。インスタ・TikTok運用の具体的な相談、PR企画以外のマネタイズ方法についての質問スレッド。"
    },
    {
        "index": 382,
        "filename": "image_14.png",
        "description": "ペット系アカウントのマネタイズ戦略についての回答。ドックフード・ペット用品アフィリエイト、ペットホテル紹介、教育コンテンツ販売についての具体案。"
    },
    {
        "index": 383,
        "filename": "image_15.png",
        "description": "ペット系利用者の質問への詳細な回答。参考アカウント紹介（いぬちず、かんと、ペット関連）、コンテンツ切り口とテーマ選定についての具体的なアドバイス。"
    },
    {
        "index": 384,
        "filename": "image_16.png",
        "description": "マネタイズの構成要素と運用ポイント（続き）。画像形式の重要性、個業者向け・アスリート向けコンテンツの区別化についての詳細な戦略説明。"
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

    print(f"\n✓ Batch 365-384 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
