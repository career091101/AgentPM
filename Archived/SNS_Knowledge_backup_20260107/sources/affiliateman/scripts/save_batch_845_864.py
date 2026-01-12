#!/usr/bin/env python3
"""
Batch 845-864の画像説明を保存
インデックス845-864（20枚）の詳細説明を生成・更新
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 845-864の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 845,
        "filename": "image_21.png",
        "description": "インスタグラムのコメント欄での質疑応答スレッド。アカウント「おゆき」からの初期質問と、それに対する複数ユーザーの回答が表示されている。フィード投稿の戦略やリール投稿の効果的な運用方法について議論している。"
    },
    {
        "index": 846,
        "filename": "image_22.png",
        "description": "インスタグラムのコメント返信スレッド。ユーザー「みりん」がインスタアカウント運用についての質問に対して、KくんがDM送付を勧める回答を提示している。ファミリー向けアカウント運用戦略について言及。"
    },
    {
        "index": 847,
        "filename": "image_23.png",
        "description": "インスタグラムのコメント欄での返信。KくんがTwitterとインスタの使い分けについて回答し、YouTube動画リンク（youtu.be/vEUepyG867M）を提示して戦略を詳説している。"
    },
    {
        "index": 848,
        "filename": "image_24.png",
        "description": "ASAKA（複数ユーザー）からのアカウントジャンル選定についての相談とKくんの詳細な回答。ビジネス系アカウント構築における優先順位（効率性、自分に関連するもの、今後の人生設計）や参考アカウントリンク（miku_insta...など）を提示。"
    },
    {
        "index": 849,
        "filename": "image_25.png",
        "description": "SNS攻略サロンでの質疑応答。ASAKAがサロンの充実度について褒め、Kくんがビジネス系アカウント参考例として複数のインスタグラムアカウントリンク（takeshi.blogwriter、haru.tenshoku、wakaru_syukatsuyなど）を紹介している。"
    },
    {
        "index": 850,
        "filename": "image_26.png",
        "description": "Kくんからの詳細なアドバイス。インスタ運用で555%の女性フォロワー確保と月5万円稼ぐための具体的な戦略、SNS別の使い分け、複数の参考アカウントリンク（sns_freelance_aya、kurage_affiなど）を提示。"
    },
    {
        "index": 851,
        "filename": "image_27.png",
        "description": "吉田からの問い合わせ。インスタアカウント立ち上げについての相談で、想定アカウント（夜職系のターゲット）、初期段階での戦略（Kくんのslack記録参照）、フォロワー増加方法についての質問内容を記載。"
    },
    {
        "index": 852,
        "filename": "image_28.png",
        "description": "Kくんから吉田への詳細な返信。初期フォロワー確保戦略、メッション設計、ハイライト機能の活用方法、リール投稿の最適な運用方法（初期段階での特殊な扱いなど）について具体的に説明。"
    },
    {
        "index": 853,
        "filename": "image_29.png",
        "description": "Tくんからの新規質問。インスタ運用開始時期、SNS兼用の可能性、受ける案件の条件についての相談内容。Kくんがアファイ視点での具体的な回答を提供。"
    },
    {
        "index": 854,
        "filename": "image_30.png",
        "description": "Kくんの回答内容。アファイ3000円-5000円のnoteを主軸にした戦略、アカウント初期段階からのフィード投稿・リール活用戦略、転職ジャンルの参考アカウント（haru.tenshoku、wakaru_syukatsuなど）を説明。"
    },
    {
        "index": 855,
        "filename": "image_31.png",
        "description": "Tくんからの転職エージェント化に関する質問と、Kくんの詳細な実例による説明。フォロワーの質の確保方法、転職オンラインでの情報発信、ストーリーズの活用による信頼構築戦略を提示。"
    },
    {
        "index": 856,
        "filename": "image_32.png",
        "description": "Tくんとしのぶの会話。転職ジャンル向けのスペース活用や「参考」ハッシュタグ設定に関する議論、並びに転職エージェント化の実現に向けた質的フォロワー確保メソッドの相談。"
    },
    {
        "index": 857,
        "filename": "image_33.png",
        "description": "れんくらしからの複数の相談。フォロワー伸び悩み（1.8万人）、マネタイズ導線の不明確さ、プロフィール説明の改善についてKくんが段階的な診断とアカウント選用アドバイスを提供。"
    },
    {
        "index": 858,
        "filename": "image_34.png",
        "description": "れんくらしへのKくんの詳細アドバイス。マネタイズ導線の強化、売上から逆算した市場分析、転職系アフィリエイト活用方法、参考アカウント（mark_zubora_creatorなど）の紹介。"
    },
    {
        "index": 859,
        "filename": "image_35.png",
        "description": "ふみからの複数質問。アラッサー男性向けアカウント（タロット占い）構築における視聴層確保、アラッサー特有の心理特性を活用したコンテンツ企画についてKくんが回答。"
    },
    {
        "index": 860,
        "filename": "image_36.png",
        "description": "ふみへのKくんの詳細な回答。フォロワー参考例からの学習（10万人以上など）、自分との同一性の活用方法、月別フォロワー属性分析などのデータ駆動型マネタイズ戦略を説明。"
    },
    {
        "index": 861,
        "filename": "image_37.png",
        "description": "なつ副業ブログからのディーラー運用相談。Line予約との組み合わせ戦略、インスタ運用時の集客課題についてKくんが概要レベルでの改善提案を複数提示。"
    },
    {
        "index": 862,
        "filename": "image_38.png",
        "description": "なつ副業ブログとのやり取り継続。インスタ運用の具体的な課題（フォロワー伸び悩み、売上停滞）について、スストーリーズの活用方法やDM運用の改善、参考アカウント例（super.jumbo_cardealer、netztoyotamieなど）を提示。"
    },
    {
        "index": 863,
        "filename": "image_39.png",
        "description": "ビタミンアカウントの相談。発見欄への進出困難さ、フォロワー伸び悩み（500を超えたレベル）、メディア系から美容系へのシフトについてKくんが診断と対策（ストーリー運用30-40%、DMアプローチなど）を提示。"
    },
    {
        "index": 864,
        "filename": "image_40.png",
        "description": "きなこからの参入ジャンル相談。タロット占いアカウント構築における視聴者分析（占い恋愛系、タレント系、占い×恋愛系の混合）と、各ジャンル別のアカウント戦略についてKくんがフレームワークを提示。"
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

    print(f"\n✓ Batch 845-864 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
