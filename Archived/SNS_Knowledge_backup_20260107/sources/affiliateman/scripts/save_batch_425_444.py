#!/usr/bin/env python3
"""
Batch 425-444の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
12月質疑応答まとめ記事の画像処理
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 425-444の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 425,
        "filename": "image_57.png",
        "description": "フォロワー運用に関するInstagram質問への回答。顔出しなしでも属性売上は可能だが、半属人性の運用がおすすめという赤文字での説明。情報に価値があるジャンル（積み立てNISA・楽天攻略）はキャラクター運用でOK、それ以外は属人性を出したほうがいいと記載。"
    },
    {
        "index": 426,
        "filename": "image_58.png",
        "description": "Instagramのコメント欄。ユーザー「かずなな」による漫画ジャンルのストーリー閲覧率20%以下で40～50%に引き上げたいという質問と、複数のコメント返信が表示されている。"
    },
    {
        "index": 427,
        "filename": "image_59.png",
        "description": "Instagramコメント欄。ユーザー「かずなな」の質問に対する複数の返信。ストーリー閲覧率と関連した投稿戦略についてのDM相談や、ライブガイドの効果的な使い方についての議論が記載されている。"
    },
    {
        "index": 428,
        "filename": "image_60.png",
        "description": "Instagramコメント欄。ユーザー「せいぬ」の質問「月109万円の恋愛noter」という質問内容。複数の端末でのログイン問題や2段階認証についての相談が表示されている。"
    },
    {
        "index": 429,
        "filename": "image_61.png",
        "description": "Instagramコメント欄。K君による「せいぬ」さんへのアカウント管理に関する詳細なアドバイス。複数のアカウント端末管理やDM数の最適化、フォロワー数に関する具体的な施策が記載されている。"
    },
    {
        "index": 430,
        "filename": "image_62.png",
        "description": "Instagramコメント欄。ユーザー「だい」の質問。アカウント方向性についての相談と、トレーニングと食事に関するコンテンツについての質問が表示されている。"
    },
    {
        "index": 431,
        "filename": "image_63.png",
        "description": "Instagramコメント欄。ユーザー「kana」の質問。楽天roomのアフィ初めで報酬が場やしたくないという相談。インスタグラムのアカウント改善についてのアドバイスと属人性についての話が記載されている。"
    },
    {
        "index": 432,
        "filename": "image_64.png",
        "description": "Instagramコメント欄。ユーザー「kana」による屋人生についての質問と、K君からの属人生コンセプトについてのアドバイス。アカウント設計やジャンルの選択についての具体的な提案が記載されている。"
    },
    {
        "index": 433,
        "filename": "image_65.png",
        "description": "Instagramコメント欄。K君による「kana」さんへの返信。別ジャンルのアカウントフォローのテクニックやリール強化についての具体的なアドバイスが表示されている。"
    },
    {
        "index": 434,
        "filename": "image_66.png",
        "description": "Instagramコメント欄。ユーザー「keina」からの質問。ガーデニング系配信で収益化したい、おすすめの副業についての相談と具体的なアカウント名が記載されている。"
    },
    {
        "index": 435,
        "filename": "image_67.png",
        "description": "Instagramコメント欄。K君による「keina」さんへの回答。マネタイズの難易度やジャンル選択、初心者向けのガーデニング関連コンテンツ作成についての具体的なアドバイスが表示されている。"
    },
    {
        "index": 436,
        "filename": "image_68.png",
        "description": "Instagramコメント欄。ユーザー「Erika Suzuki」による旅行アカウント運用についての相談。温泉宿やホテルアカウントへの変更について、ハッシュタグやペンマーク戦略についての具体的な質問が記載されている。"
    },
    {
        "index": 437,
        "filename": "image_69.png",
        "description": "Instagramコメント欄。K君による「Erika Suzuki」さんへのアドバイス。ハグに関する下記参考資料の提示と、タグの選定についての具体的なガイドが表示されている。"
    },
    {
        "index": 438,
        "filename": "image_70.png",
        "description": "Instagramコメント欄。K君による「Erika Suzuki」さんへの継続アドバイス。旅行アカウントのキャラクター設定についての説明と、キャラクター運用がどのように機能するかについての詳細が記載されている。"
    },
    {
        "index": 439,
        "filename": "image_71.png",
        "description": "Instagramコメント欄。ユーザー「茶トラ兄弟」からのペット系アカウント運用についての質問。アフィリエイト戦略やコンセプト、参考アカウントについての相談が表示されている。"
    },
    {
        "index": 440,
        "filename": "image_72.png",
        "description": "Instagramコメント欄。K君による「茶トラ兄弟」さんへの返信。猫運用の具体的なコンセプト、ペット系アフィリエイト戦略、商品選択方法についての詳細なアドバイスが記載されている。"
    },
    {
        "index": 441,
        "filename": "image_73.png",
        "description": "Instagramコメント欄。ユーザー「もり」からのファッションアカウントとビジネス系アカウントの2つについてのアドバイス相談。フォロワー数や月間リーチ数といった具体的な数値が記載されている。"
    },
    {
        "index": 442,
        "filename": "image_74.png",
        "description": "Instagramコメント欄。K君による「もり」さんへの回答。ファッションアカウントのフォロワーファン化戦略やエンゲージメント率向上についての具体的なアドバイスが表示されている。"
    },
    {
        "index": 443,
        "filename": "image_75.png",
        "description": "Instagramコメント欄。K君による継続回答。ビジネス系アカウントの複数フォロワー活用やアクションスタンプの効果的な使い方についての具体的な施策が記載されている。"
    },
    {
        "index": 444,
        "filename": "image_76.png",
        "description": "Instagramコメント欄。ユーザー「星野」からの保険診断アプリ運用についての質問。ストーリー教育の必要性やアプリインストール施策についての相談が表示されている。"
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

    print(f"\n✓ Batch 425-444 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
