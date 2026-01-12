#!/usr/bin/env python3
"""
Batch 1045-1064の画像説明を保存
「2023年4月質疑応答のまとめ」の記事から実際に読み込んだ詳細説明
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 1045-1064の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1045,
        "filename": "image_11.png",
        "description": "インスタグラムユーザーKくんからの質問。マネタイズ幅やフォロワー施策のどちらが優先かについて、複数の視点から戦略を解説するコメント。"
    },
    {
        "index": 1046,
        "filename": "image_12.png",
        "description": "Capcut使用可能性と仕事用副アカウント設定に関する質問。編集アプリ認識やカテゴリ相談の詳細な回答。"
    },
    {
        "index": 1047,
        "filename": "image_13.png",
        "description": "makoto tanishiからの質問詳細。ハッシュタグ20-25個の最適性、アカウント伸ばし方について、フォロワー760人の健康系アカウントの初期段階での戦略についての複数項目の質問。"
    },
    {
        "index": 1048,
        "filename": "image_14.png",
        "description": "ハッシュタグ戦略と関連アカウント運用についての詳細な回答。初期リーチ、ハッシュタグリーチ数、エンゲージメント見直しなどの実践的なアドバイス。"
    },
    {
        "index": 1049,
        "filename": "image_15.png",
        "description": "ジャンル認知度向上とKくんのマネタイズ戦略に関する具体的なアドバイス。フォロワー数別のアプローチと発見タブへの露出を高める方法。"
    },
    {
        "index": 1050,
        "filename": "image_16.png",
        "description": "SNS王子様の公開アドバイス。フォロワー2000人のタイミングでのストーリー閲覧率改善策とメンション・リール強化のメッセージ内容。"
    },
    {
        "index": 1051,
        "filename": "image_17.png",
        "description": "りつのコンサルアドバイス。新規振興についての質問と回答を含む長文コメント。フォロワー2000人目指しての施策や投稿時間の工夫についての内容。"
    },
    {
        "index": 1052,
        "filename": "image_18.png",
        "description": "りつからの新規振興メリットと運用方法に関する詳細な解説。フォロワー300人規模から2000人への成長戦略についての複数質問への回答。"
    },
    {
        "index": 1053,
        "filename": "image_19.png",
        "description": "けい（転職ジャンル）からの質問と詳細なアドバイス。新規振興23人増加、ストーリー閲覧数、フォロワー転換率の改善についての実体験ベースの回答。"
    },
    {
        "index": 1054,
        "filename": "image_20.png",
        "description": "KくんからのアカウントコンセプトとSNS戦略に関する詳細な回答。転職エージェント系の課題と運用方針、マネタイズの可能性についての多角的な解説。"
    },
    {
        "index": 1055,
        "filename": "image_21.png",
        "description": "すたーくからのスピ系アカウント運用質問。マネタイズ方針の選定、ハッシュタグ最適化、アカウント分析などについての複数項目の質問コメント。"
    },
    {
        "index": 1056,
        "filename": "image_22.png",
        "description": "9ノーべーからの質問回答。女性恋愛系アカウント選択、マネタイズプラン考察、初期段階でのタロット活用法についての詳細な回答。"
    },
    {
        "index": 1057,
        "filename": "image_23.png",
        "description": "トポロの転職ジャンル相談。フォロワー23人増加への課題と運用改善、スレッド詳細解説、メンション戦略についての実践的なアドバイス。"
    },
    {
        "index": 1058,
        "filename": "image_24.png",
        "description": "Kくんからのエンジニアターゲットアカウントとマネタイズ戦略。月20-30万の目標設定、ジャンル分析、フォロワー伸ばし方についての体系的な解答。"
    },
    {
        "index": 1059,
        "filename": "image_25.png",
        "description": "新規振興の考え方とフィード強化戦略。月100チャレンジの活用、リール攻略、外部誘導によるフォロワー増加の実践的なアドバイス。"
    },
    {
        "index": 1060,
        "filename": "image_26.png",
        "description": "マネタイズ月20-30万の実現方法。現在のアフィリエイト方向性とアカウント最適化、フォロワー数による段階的なアプローチの説明。"
    },
    {
        "index": 1061,
        "filename": "image_27.png",
        "description": "Slackチャネルでのノート引用とK くんへのメンション。タクト対話と対読動画視聴についての通知内容。"
    },
    {
        "index": 1062,
        "filename": "image_28.png",
        "description": "KAZUKIのメンズ美容アカウント紹介とペルソナ分析。20-25歳男性向け振袖コンサル、ターゲット特定とコンテンツ戦略の詳細。"
    },
    {
        "index": 1063,
        "filename": "image_29.png",
        "description": "KAZUKIアカウントのプロフィール課題。ミスター準グランプリ権威性の活用、フォロワー増加方法、投稿内容改善についての質問。"
    },
    {
        "index": 1064,
        "filename": "image_30.png",
        "description": "Twitterコンサル考察とマッチングアプリ戦略。ミスター準グランプリのTwitter展開、外見改善コンサル、Instagram同期についての複数質問への回答。"
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

    print(f"\n✓ Batch 1045-1064 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
