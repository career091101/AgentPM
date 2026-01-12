#!/usr/bin/env python3
"""
Batch 605-624の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 605-624の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 605,
        "filename": "image_05.png",
        "description": "ほっしんさんのInstagramへの質問コメント。「いつもお世話になっています。インスタのコンサルの相場についてくらくらいのか教えてもらえますか？」という質問内容。"
    },
    {
        "index": 606,
        "filename": "image_06.png",
        "description": "じんさんの返信コメント。インスタコンサル料金について「個人の場合は月2回ZOOMチャットで質問放題で月5-10万円、法人の場合は月10-15万円」という具体的な料金表。"
    },
    {
        "index": 607,
        "filename": "image_07.png",
        "description": "KくんへのInstagramコメント回答。レシピや料理関連アカウントについての質問で、フィード投稿の初期段階での指標設定や料理作りのコツについての詳細なアドバイス内容。"
    },
    {
        "index": 608,
        "filename": "image_08.png",
        "description": "じんさんとKくんの複数行のInstagram質問応答。ASP業者（seedup、WLAZZ）の比較と初心者向けのアフィリエイト開始タイミングについての相談と回答。"
    },
    {
        "index": 609,
        "filename": "image_09.png",
        "description": "KくんからのInstagram長めのコメント。フォロワー数とアフィリエイト販売の関係性、サロンでのトラブル解決方法、ストーリーズでのフォロワーの悩み解決についての質問内容。"
    },
    {
        "index": 610,
        "filename": "image_10.png",
        "description": "もりりさんの質問コメント。ホスト用のインスタ活用とホストアカウント設計についての質問で、3つの異なるアカウントコンセプト提案が含まれている。"
    },
    {
        "index": 611,
        "filename": "image_11.png",
        "description": "KくんのInstagram長文コメント。ホストアカウント設計、TikTok活用、ビジネス系アカウントについての詳細なアドバイスと複数の参考アカウントリンク。"
    },
    {
        "index": 612,
        "filename": "image_12.png",
        "description": "ノースさんの質問。投資アカウント運用についての相談で、現状のフォロワー数と目標の不一致、投資系アカウントの実績ベース運用についての悩み。"
    },
    {
        "index": 613,
        "filename": "image_13.png",
        "description": "KくんのInstagram回答。ビジネスアカ運用についての4つの具体的な施策提案：ストーリー→ブログ→DM流入、固定ビジン活用、サムネ活用、複数質問の集約戦略。"
    },
    {
        "index": 614,
        "filename": "image_14.png",
        "description": "ゆうさんの質問。インスタ使用開始12月でフォロワー27人という現状から、自己肯定感UP向けママ向けアカウント方針の悩みと改善相談。"
    },
    {
        "index": 615,
        "filename": "image_15.png",
        "description": "KくんのInstagram返信。ゆうさんのアカウント方針について3つの質問を投げかけて、より具体的な方向性の検討を促すアドバイス内容。"
    },
    {
        "index": 616,
        "filename": "image_16.png",
        "description": "ゆうさんとKくんのInstagram質問応答。フィード投稿5件限定条件でのImpを重視する運用方針と、リール強化による成功事例についての対話。"
    },
    {
        "index": 617,
        "filename": "image_17.png",
        "description": "ゆーたさんのInstagram質問。自分の定義購入間関係がTwitterで言及されたことについての質問と言葉選びについての相談内容。"
    },
    {
        "index": 618,
        "filename": "image_18.png",
        "description": "てぃんさんの質問。ExcelやShorcut活用によるCTA画像シンプル化と、フォロー転換率改善についての相談内容で、フォロー数改善方法の複数提案。"
    },
    {
        "index": 619,
        "filename": "image_19.png",
        "description": "てぃんさんのInstagram質問。フォロワー100人規模での発見タブ登場見込みと初期段階での動画投稿戦略についてのKくんへの質問。"
    },
    {
        "index": 620,
        "filename": "image_20.png",
        "description": "Sさんの質問。インスタアルゴリズム最近の変更とフォロワー増加についての相談で、リール活用法とInstagramアルゴリズム変化への対応についての疑問。"
    },
    {
        "index": 621,
        "filename": "image_21.png",
        "description": "KくんのInstagram返信。リール強化の効果と既存フォロワー向けの投稿バランスについてのアドバイス、及びアカウント改善方針についての具体的なコメント。"
    },
    {
        "index": 622,
        "filename": "image_22.png",
        "description": "SさんとのInstagram複数行のやり取り。アカウントの細かい改善点についての質問と、テーマに一貫性を持たせる改善方針についての提案内容。"
    },
    {
        "index": 623,
        "filename": "image_23.png",
        "description": "りゅうさんの質問。不動産業界のInstagram活用についての相談で、不動産関係の代行や撮影に関する業務内容についての詳細な質問内容。"
    },
    {
        "index": 624,
        "filename": "image_24.png",
        "description": "りゅうさんとKくんのInstagram質問応答。不動産業界のInstagram運用方針とリール・動画編集の外注やオーディエンス設定についての詳細な対話。"
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

    print(f"\n✓ Batch 605-624 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
