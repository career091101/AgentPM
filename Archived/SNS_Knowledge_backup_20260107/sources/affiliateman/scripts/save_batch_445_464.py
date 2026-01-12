#!/usr/bin/env python3
"""
Batch 445-464の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 445-464の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 445,
        "filename": "image_77.png",
        "description": "Instagramでのコンテンツ企画について、ハッシュタグやTTPを活用する質問への回答スクリーンショット。ユーザーKくんが、コンテンツ格納サイトを網羅すること、また以下2つについて言及している：伸びているハッシュタグをTTP、掲載されている情報をTTP。"
    },
    {
        "index": 446,
        "filename": "image_78.png",
        "description": "整骨院のInstagramストーリー投稿について、スタンプアクション機能の活用に関する質問と回答。左側は整骨院のストーリーで施術メニューを表示、右側は回転しないお寿司のストーリーで美味しいという投稿例を表示している。"
    },
    {
        "index": 447,
        "filename": "image_79.png",
        "description": "ストーリー投稿について、タップするメリットと押さないメリット、またタップ数を絵文字で増やすことについての詳細な説明コメント。一つの軸として「押して欲しいリール投稿に指する」か「押さないと指す」かで分類している。"
    },
    {
        "index": 448,
        "filename": "image_80.png",
        "description": "Instagramストーリーズの表示画面。「2023年版 インスタアルゴリズム最新解説してほしい人」というテキストが中央に黄色ラインで囲まれており、ハートマークの絵文字をタップするよう促すデザイン。"
    },
    {
        "index": 449,
        "filename": "image_81.png",
        "description": "美容系Instagramアカウントについて、アカウント作りを直すべきかについての質問。属人性が重要なアカウントにおいて、マネタイズ苦戦の原因を分析する回答コメント。"
    },
    {
        "index": 450,
        "filename": "image_82.png",
        "description": "Instagramストーリー閲覧率が5%以下に落ちている場合の改善施策について、問題率が20%戻らなければ作り直すべきという回答。年齢層別のマネタイズ苦戦について分析する複数のコメント。"
    },
    {
        "index": 451,
        "filename": "image_83.png",
        "description": "Instagramアカウント「そうた_renai」のプロフィール分析について、40日で達成した目標やターゲット（25歳女性）の詳細情報が記載されている。プロフアクセス率の改善施策についての複数の回答コメント。"
    },
    {
        "index": 452,
        "filename": "image_84.png",
        "description": "Instagramアカウント「そうた_renai」の投稿分析について、プロフアクセス率が0.23%から2.4%に改善した事例。タイトル変更、フォント変更、文字量調整による改善結果を示している。"
    },
    {
        "index": 453,
        "filename": "image_85.png",
        "description": "Instagramのプロフアクセス率改善施策についての追加アドバイス。10枚目プロフィール誘導スライド変更、フォント変更、文字量調整などで改善できるという回答コメント。"
    },
    {
        "index": 454,
        "filename": "image_86.png",
        "description": "新規Instagramアカウントの企画について、介護業とペット業との組み合わせの質問。介護のモダイ的な感じと、ペットパターンという2つのコンセプト提案に対する回答。"
    },
    {
        "index": 455,
        "filename": "image_87.png",
        "description": "新規アカウント開設に伴うアドバイスコメント。アドラーの理学心理学を心理学に応用するアプローチ、及び介護業界への参入方法についての複数の提案。"
    },
    {
        "index": 456,
        "filename": "image_88.png",
        "description": "教育アカウント「ボトラ兄弟」のプロフィール分析。アドラー心理学と失敗円滑子育てをテーマにしたアカウント設定についての詳細分析とアドバイス。"
    },
    {
        "index": 457,
        "filename": "image_89.png",
        "description": "Instagramアカウント「そうた」に対する投稿分析とプロフアクセス率改善についてのアドバイス。フロアクセス率を高める施策について、タイトルやフォント改善に関する提案。"
    },
    {
        "index": 458,
        "filename": "image_90.png",
        "description": "Instagramアカウント「かずなな」の恋愛系アカウント運用についての質問と回答。ターゲット設定（彼氏と上手くいっていない女性）と賃問の振り方についての複数の提案。"
    },
    {
        "index": 459,
        "filename": "image_91.png",
        "description": "Instagramストーリー投稿について、選んだジャンルで伸せるかについての質問。個別ジャンルとマネタイズ可能性についてのアドバイスコメント。"
    },
    {
        "index": 460,
        "filename": "image_92.png",
        "description": "Instagramアカウント「みみか」のサロン参加質問について、ジャンル選定と人物面の両側面についての回答。自分自身に信力がない場合のアカウント構築方法についてのアドバイス。"
    },
    {
        "index": 461,
        "filename": "image_93.png",
        "description": "Instagramアカウント「みみか」への詳細なアドバイスコメント。自身の人属面の課題を克服するための具体的なアプローチと、ジャンル選定についての提案。"
    },
    {
        "index": 462,
        "filename": "image_94.png",
        "description": "Instagram初心者向けのジャンル選定についての質問と複数のアカウント例。漫画紹介、子供向け食、ノマドカフェ、転職IT人材特化などのコンセプト事例を提示。"
    },
    {
        "index": 463,
        "filename": "image_95.png",
        "description": "Instagram転職系ジャンルについての提案。転職アフィリキャンセルと漫画系ジャンルについての複数の選択肢についての詳細なアドバイス。"
    },
    {
        "index": 464,
        "filename": "image_96.png",
        "description": "Instagram転職系アカウントの詳細説明と外注についてのアドバイス。転職系ジャンルの詳細、漫画系アカウント、外注の方向性についての複数の提案と説明。"
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

    print(f"\n✓ Batch 445-464 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
