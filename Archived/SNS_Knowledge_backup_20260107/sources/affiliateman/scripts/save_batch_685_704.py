#!/usr/bin/env python3
"""
Batch 685-704の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 685-704の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 685,
        "filename": "image_85.png",
        "description": "マサ（@マサ）からの質問。42投稿でフォロワー5000人以上目指すについて相談。ママタイズについてのアドバイス。"
    },
    {
        "index": 686,
        "filename": "image_86.png",
        "description": "やまくち（@Kくん）からの質問。SNS×アフィリエイトのジャンル併用やテーマの融合、並行アカウントについて3つの質問。"
    },
    {
        "index": 687,
        "filename": "image_87.png",
        "description": "おゆき（@Kくん）からの質問。フィードとリール動画の比率や投稿内容、デザインについての質問。"
    },
    {
        "index": 688,
        "filename": "image_88.png",
        "description": "Kくん（@おゆき）からの回答。正方形と縦長のアスペクト比、タイミング、ハイライト編集、フォロワー5000人での戦略について詳細にアドバイス。"
    },
    {
        "index": 689,
        "filename": "image_89.png",
        "description": "てぃん（Excel時短術）からの大手アカのストーリーズメンションについての質問。3点の課題をまとめた相談。"
    },
    {
        "index": 690,
        "filename": "image_90.png",
        "description": "Kくん（@てぃん）からの回答。ストーリー周数による変動や前提介紹の重要性、数字の参考値（1万人10-20人前後など）を提示。"
    },
    {
        "index": 691,
        "filename": "image_91.png",
        "description": "質問への回答続き。2点目のフォロワー増加数について、ストーリーの枚数や内容による影響を説明。"
    },
    {
        "index": 692,
        "filename": "image_92.png",
        "description": "3点目の質問への回答。ハイライトの自己紹介参考例やタグの利用、ストーリー紹介の効果について指導。"
    },
    {
        "index": 693,
        "filename": "image_93.png",
        "description": "おゆき（@Kくん）からの新しい質問。フィード投稿の頻度と投稿タイミング、Twitterでのインスタコンシェルジュ投稿について相談。"
    },
    {
        "index": 694,
        "filename": "image_94.png",
        "description": "Kくん（@おゆき）からの回答。毎日投稿やタイミング戦略、ストーリーとフィードの役割分担、リール投稿について詳しく説明。"
    },
    {
        "index": 695,
        "filename": "image_95.png",
        "description": "おゆき（@Kくん）からのさらなる質問。毎日投稿の負担や1日欠かすことの影響について相談。"
    },
    {
        "index": 696,
        "filename": "image_96.png",
        "description": "ねこ（@Kくん）からの質問。ジャンル認識についてのタブ表示と発見タブの関係性について詳細に相談。"
    },
    {
        "index": 697,
        "filename": "image_97.png",
        "description": "Kくん（@ねこ）からの回答。ジャンル認識の複数説、発見タブのパワーと関係性、複数ジャンル使用時の戦略について説明。"
    },
    {
        "index": 698,
        "filename": "image_98.png",
        "description": "ジャンル認識についてのさらなるアドバイス。ターゲットと自分のジャンルのズレ、コメント戦略について継続的なガイダンス。"
    },
    {
        "index": 699,
        "filename": "image_99.png",
        "description": "ミント（@Kくん）からの質問。note×SNS、note×SNSコンセプト、ビジネス系の副業立ち上げについて3つの相談事項。"
    },
    {
        "index": 700,
        "filename": "image_100.png",
        "description": "Kくん（@ミント）からの回答。note×SNSコンセプトについて、複数フォロー層の活用法、セールス戦略について指導。"
    },
    {
        "index": 701,
        "filename": "image_101.png",
        "description": "note×SNSの更なる説明。note×SNS商品での収益化、長期・短期コンサルメニューについての具体例。"
    },
    {
        "index": 702,
        "filename": "image_102.png",
        "description": "おゆき（@Kくん）からのリール動画作成についての質問。リール作成の難しさや宣伝感についての相談。"
    },
    {
        "index": 703,
        "filename": "image_103.png",
        "description": "おゆき（@Kくん）からの続く質問。ストーリーズ初期のコンテンツ製作やハイライト編集について追加相談。"
    },
    {
        "index": 704,
        "filename": "image_104.png",
        "description": "うだ戦わない起業（@Kくん）からの質問。インスタのキャプションについて、検索とキーワード、リールのキャプション文について相談。"
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

    print(f"\n✓ Batch 685-704 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
