#!/usr/bin/env python3
"""
Batch 345-364の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 345-364の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 345,
        "filename": "image_72.png",
        "description": "SNS運用知識まとめのタイトル画像（2022年10月分）。紫と白のデザインに、「超役立つ情報」というキャッチコピーと企業のイラストが配置されている。"
    },
    {
        "index": 346,
        "filename": "image_01.png",
        "description": "Instagram/Twitter/TikTok質問回答まとめのタイトル画像。複数の質問マークが右側に配置され、「2022年10月分」と記載されている。"
    },
    {
        "index": 347,
        "filename": "image_02.png",
        "description": "ジムコンセプトに関するInstagram DM質問への詳細回答。40代女性向けダイエット情報やアカウント運用方法について複数行の説明文が記述されている。"
    },
    {
        "index": 348,
        "filename": "image_03.png",
        "description": "ビフォーアフター投稿やハイライト設定に関する複数の質問と回答スレッド。固定ピンやメンション方法についての具体的なアドバイスが含まれている。"
    },
    {
        "index": 349,
        "filename": "image_04.png",
        "description": "コンテンツ販売方法に関する質問スレッド。note販売とインスタ販売のジャンル選定について、複合的なアカウント運用戦略を説明している。"
    },
    {
        "index": 350,
        "filename": "image_05.png",
        "description": "Twitter利用法に関する複数の質問回答。アニメグッズアカウントの運用法やマネタイズ戦略について、note販売やASP登録の観点から解説している。"
    },
    {
        "index": 351,
        "filename": "image_06.png",
        "description": "ネタバレ対策やハッシュタグ活用に関する説明。インスタのメタタグやテキスト検索最適化についての詳細アドバイスが記載されている。"
    },
    {
        "index": 352,
        "filename": "image_07.png",
        "description": "リアル感出し方やプライベート画像活用に関する質問回答。ストーリーズ投稿やフォロワーのファン化戦略についての実践的なコンサルティング内容。"
    },
    {
        "index": 353,
        "filename": "image_08.png",
        "description": "ジャンル選定やアカウント概要設計に関する質問スレッド。ニーズマイン設定や主婦向けカフェ情報発信のマネタイズ方法を解説している。"
    },
    {
        "index": 354,
        "filename": "image_09.png",
        "description": "エンタメ系インスタマネタイズに関する複数の質問と回答。U-NEXT等のVODサービスアフィリエイト活用方法や推奨ジャンル戦略を説明している。"
    },
    {
        "index": 355,
        "filename": "image_10.png",
        "description": "Twitterマネタイズに関する質問回答。アニメ関連コンテンツのASP登録やnote販売の具体的な収入例（コンサル1時間10000円等）を記述。"
    },
    {
        "index": 356,
        "filename": "image_11.png",
        "description": "インスタアフィリエイト選定に関する詳細説明。資産運用ジャンルの各種アカウント（シロハル、楽天証券等）とマネタイズ方法を一覧化している。"
    },
    {
        "index": 357,
        "filename": "image_12.png",
        "description": "マネタイズ戦略に関する複雑な質問回答スレッド。アフィ選定の重要性やコンセプトマイン設定についての実践的なコンサルティング内容。"
    },
    {
        "index": 358,
        "filename": "image_13.png",
        "description": "エンタメ系インスタの映画紹介マネタイズについて。U-NEXTやVODアフィリエイト活用法と、競争激化への対応戦略を解説している。"
    },
    {
        "index": 359,
        "filename": "image_14.png",
        "description": "インスタグラム女性ユーザー向けマネタイズについて。韓国ファッション、コスメ、美容アカウントの具体的なASP・アフィ案件を提示している。"
    },
    {
        "index": 360,
        "filename": "image_15.png",
        "description": "アニメ系インスタマネタイズの実例。U-NEXTなどのVODアフィ登録手順や、映画館クレジットカード、au スマートパス等の案件を列挙している。"
    },
    {
        "index": 361,
        "filename": "image_16.png",
        "description": "2022年以降始めるべきインスタ・ツイッタージャンル解説。マネタイズ戦略、心理コンセプト、およびジャンル選定上の悩みに対する明確な解答を提供。"
    },
    {
        "index": 362,
        "filename": "image_17.png",
        "description": "インスタ投稿のアルゴリズムとハッシュタグ戦略に関する質問回答。検索需要の重要性と、投稿内容の最適化方法について詳細に説明している。"
    },
    {
        "index": 363,
        "filename": "image_18.png",
        "description": "インスタグラムアカウント分析画面のスクリーンショット。フォロワー数169,469、リーチ6,032、フォロワー増163,437などのインサイト数値を表示。"
    },
    {
        "index": 364,
        "filename": "image_19.png",
        "description": "Twitter/TikTok質問回答まとめのタイトル画像（2022年7-9月分）。質問マークのアイコンと「質問回答まとめ」のテキストが配置されている。"
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

    print(f"\n✓ Batch 345-364 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
