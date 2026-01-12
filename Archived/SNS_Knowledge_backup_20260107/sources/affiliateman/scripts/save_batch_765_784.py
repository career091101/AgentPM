#!/usr/bin/env python3
"""
Batch 765-784の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 765-784の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 765,
        "filename": "image_165.png",
        "description": "質問者KKくんが2ヶ月前に投稿した質問「楽天アフィは、やたら半粒化したアカウントじゃないと感じしいので、薄利多売なので、大量に売らないといけなくてフォロアー数に起因するので僕はあんまやっていいですね」に対する詳細な回答スレッド。楽天アフィの特性について複数ユーザーからのコメント。"
    },
    {
        "index": 766,
        "filename": "image_166.png",
        "description": "Instagramの新機能やハイライト活用に関する質問への回答。フォロワーを伸ばすコンサル、アカのコンセプト、売り方に関する相談の交流内容。LINE公式アカウント、HSP関連、オンラインサロン立ち上げについての助言。"
    },
    {
        "index": 767,
        "filename": "image_167.png",
        "description": "質問者たけるからの投稿「いつもご質問にお答えありがとうございます」への複数回答。自己肯定感の低さ、恋愛の自己肯定感に関する質問、サロン運営のコンセプト設計についての詳細な相談と回答。"
    },
    {
        "index": 768,
        "filename": "image_168.png",
        "description": "【Q1】「JKくんだったら『VIEW』はどういった訴求をしますか？」という質問に対して、KKくんの詳細な戦略的アドバイス。ハイライト機能の月間閲覧数増加、ストーリーズ活用、商品購入数増加への効果説明。"
    },
    {
        "index": 769,
        "filename": "image_169.png",
        "description": "iPhone系アカウントのフォロワー流入最適化に関する複数の質問と回答。ビジネスアカウントの戦略、イコン活用についての相談内容。ジジツツコンサルの効果や実績についての議論。"
    },
    {
        "index": 770,
        "filename": "image_170.png",
        "description": "質問者たけるからのInstagram運用に関する最新の質問への回答。自己肯定感の上げ方、コンセプト構築、料理ジャンルの宮田。蒸気すれた注とコンサル売却について。"
    },
    {
        "index": 771,
        "filename": "image_171.png",
        "description": "KKくんによる恋愛系ジャンル運用の具体的なアドバイス。別ジャンルのアドバイス、インスタマイン方、『Brain』やコンテンツについての詳細説明。ビジネスアカウント運営戦略。"
    },
    {
        "index": 772,
        "filename": "image_172.png",
        "description": "KKくんが「【Q1.】JKくんだったら『VIEW』はどういった訴求をしますか？」への詳細な回答。ハイライト活用方法、ストーリーズ配置、商品購入数増加戦略、フォロー単価の説明。"
    },
    {
        "index": 773,
        "filename": "image_173.png",
        "description": "複数の質問者からのコンテンツコンバーター、SEOコンサルタント関連の質問への回答。検索結果、参考アカウント紹介（ココナラ、Resume.id、Notebookなど）。SNSアカウント調査結果。"
    },
    {
        "index": 774,
        "filename": "image_174.png",
        "description": "SNSアカウント戦略についての詳細なアドバイス。インフルエンサーの負担軽減、SNス心理などのニュアンス説明。Google検索との連携、体験記の重要性。SEOコンサルタント専門知識。"
    },
    {
        "index": 775,
        "filename": "image_175.png",
        "description": "片山勇太（Twitter名『ウィピー』）による質問への回答。SNSの複数メディア運営、インフルエンサー育成、コンテンツコンバーター育成についての詳細な考え方と戦略。"
    },
    {
        "index": 776,
        "filename": "image_176.png",
        "description": "ペインポイント、参考アカウント情報。コンテンツコンバーター関連リンク集（複数のNote URL、Resume.id、Coconala など）。SNS運用とブログ連携の実践的な相談内容。"
    },
    {
        "index": 777,
        "filename": "image_177.png",
        "description": "KKくんへの大大さんの投稿。SNSアカウント戦略、別ジャンル相談についての質問と複数ユーザーからの回答スレッド。BrainやコンテンツCovert戦略についての交流。"
    },
    {
        "index": 778,
        "filename": "image_178.png",
        "description": "大大さんの投稿「SNSデカインスタ/tikok/ツイッター）もってるSNSの影響力があり、自分のSNSの投稿をブログに変換してほしいSNS方を持っている人の問い合わせ」への詳細な回答交流。"
    },
    {
        "index": 779,
        "filename": "image_179.png",
        "description": "KKくんによる大大さんへのSNS運用戦略アドバイス。複数SNSの活用方法、コンテンツコンバーター利用、ブログSEO戦略の詳細な説明。LPコンバーター育成についての相談。"
    },
    {
        "index": 780,
        "filename": "image_180.png",
        "description": "じんからの質問への複数回答スレッド。LINE公式アカウント運用、コンサルビジネス高額商品售却についての具体的なアドバイス。Twitter とnote運営の相乗効果説明。"
    },
    {
        "index": 781,
        "filename": "image_181.png",
        "description": "やまこー2ヶ月前の投稿。Twitter対女性恋愛系、HSP自己肯定感テーマ相談。もてたい男性向けと対男性の性別ターゲット相談。情報混在、恋愛金銭についての複雑な質問。"
    },
    {
        "index": 782,
        "filename": "image_182.png",
        "description": "KKくんの恋愛系ジャンル運用への回答。参入ジャンル選択、バズせやすこと、フォロワー伸びやすさについての説明。ターゲットやコンセプトについての詳細なアドバイス。"
    },
    {
        "index": 783,
        "filename": "image_183.png",
        "description": "ぶるからの転職活動関連の質問への複数回答。ベンチマークアカウント情報、転職エージェント紹介（ハイキャリ、AC Recruitment、ランスタッド）。転職ビジネス系フォロワー推奨。"
    },
    {
        "index": 784,
        "filename": "image_184.png",
        "description": "おやつラボからの質問への回答スレッド。コンサル的な内容相談、note販売における適切な価格帯設定、ダイエットジャンルアカウント戦略の詳細な指導。"
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

    print(f"\n✓ Batch 765-784 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
