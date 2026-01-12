#!/usr/bin/env python3
"""
Batch 1025-1044の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1025-1044の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1025,
        "filename": "image_201.png",
        "description": "インスタグラムDMでの質問内容。アカウント運用に関する相談や、noteの使い方についてのコメント会話スクリーンショット。"
    },
    {
        "index": 1026,
        "filename": "image_202.png",
        "description": "インスタグラムDMの返信例。フォロワー限定特典の配布やnoteについての具体的なアドバイス内容。"
    },
    {
        "index": 1027,
        "filename": "image_203.png",
        "description": "ユウタさんからのDM質問。高単価商品の売上向上やセールス方法についての質問と、KくんのアドバイスのDM会話。"
    },
    {
        "index": 1028,
        "filename": "image_204.png",
        "description": "たいがさんからのジャンル選択についての相談。自分の経験やスキルセットに基づいたジャンル選択アドバイスのDM会話。"
    },
    {
        "index": 1029,
        "filename": "image_205.png",
        "description": "Romuさんからのnote利用についての質問。メンバーシップ機能やnote販売についてのDM質問と、KくんのDM返信内容。"
    },
    {
        "index": 1030,
        "filename": "image_206.png",
        "description": "かけるさんからのDM質問。K くんの公式ラインの活用方法やセールス講座についてのメッセージ会話。"
    },
    {
        "index": 1031,
        "filename": "image_207.png",
        "description": "かけるさんからのDM返信。教育動画配信やクロージング、プレゼント配信などのフロー構築についてのアドバイス内容。"
    },
    {
        "index": 1032,
        "filename": "image_208.png",
        "description": "Kくんからのかけるさんへの返信。LINEの導入やアカウント構築、販売仕組みについての詳細なアドバイス内容。"
    },
    {
        "index": 1033,
        "filename": "image_209.png",
        "description": "Kくんからのかけるさんへの続き。PC購入やターゲット設定についてのビジネス的なアドバイスメッセージ。"
    },
    {
        "index": 1034,
        "filename": "image_214.png",
        "description": "SNS攻略サロン関連のバナー。「最大限に使いこなそう」というタイトルで、Q&Aや方向指示、教育サービスのイラスト付き案内画像。"
    },
    {
        "index": 1035,
        "filename": "image_01.png",
        "description": "Instagram/Twitter/TikTokの投稿作成ツール紹介バナー。CapCutとCanvaの製品ロゴとキャラクター付きのツール説明画像。"
    },
    {
        "index": 1036,
        "filename": "image_02.png",
        "description": "インスタグラムDMの質問内容。初期アカウント設定についての相談と、Kくんのアドバイスコメント。"
    },
    {
        "index": 1037,
        "filename": "image_03.png",
        "description": "まなさんからの転職ジャンル相談。元HSP資質での転職経験から、キャリアについてのアドバイスDM会話。"
    },
    {
        "index": 1038,
        "filename": "image_04.png",
        "description": "おおしろさんからのアカウント運営について相談。4ヶ月利用したアカウント状況とアドバイスリクエストのDM。"
    },
    {
        "index": 1039,
        "filename": "image_05.png",
        "description": "構さんからの複数アカウント運営についての相談。2つのアカウント戦略とリール数の伸び悩みについてのDM質問。"
    },
    {
        "index": 1040,
        "filename": "image_06.png",
        "description": "Kくんからのアカウントコンセプト提案。ベビー服レビューや無印食品アカウントの具体的なペルソナ設定例。"
    },
    {
        "index": 1041,
        "filename": "image_07.png",
        "description": "Kくんからのコンセプト修正案。新コンセプトの詳細説明と、デザイン・配色についてのアドバイス内容。"
    },
    {
        "index": 1042,
        "filename": "image_08.png",
        "description": "Kくんの続きの返信。新コンセプト構案の反映方法とデザイン配色に関するアドバイスメッセージ。"
    },
    {
        "index": 1043,
        "filename": "image_09.png",
        "description": "Sさんからのメンズコスメアカウント構築についての相談。タイムラインのマネタイズ方法についてのDM。"
    },
    {
        "index": 1044,
        "filename": "image_10.png",
        "description": "Kくんからのメンズコスメマネタイズ方法説明。アフィリエイトやウーミーからの案件取得などの具体的な手段提案。"
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

    print(f"\n✓ Batch 1025-1044 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
