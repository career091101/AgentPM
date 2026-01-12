#!/usr/bin/env python3
"""
Batch 885-904の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 885-904の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 885,
        "filename": "image_61.png",
        "description": "インスタグラムコメント欄でのユーザー「サキ」による質問と回答。子育て向けアカウント立ち上げについて、心理テストを使った毎日投稿と他のテーマの組み合わせについてアドバイスを求めている。"
    },
    {
        "index": 886,
        "filename": "image_62.png",
        "description": "インスタグラムコメント欄での複数ユーザーとK君の会話。TikTok活用やショート動画制作、インスタへのリール転用、プロフィール最適化に関する質問と回答が記載されている。"
    },
    {
        "index": 887,
        "filename": "image_63.png",
        "description": "きなこユーザーからの「占い恋愛」をテーマにしたアカウント立ち上げについての質問。ハッシュタグの選定方法やイメージ選択について複数の質問が記載されている。"
    },
    {
        "index": 888,
        "filename": "image_64.png",
        "description": "K君からのコメント回答。タグ付けの基礎、アカウントコンセプトと占いの関係性、InstagramのInsightSuiteツール活用についてのアドバイスが記載されている。"
    },
    {
        "index": 889,
        "filename": "image_65.png",
        "description": "しゃずユーザーからの「転職」「お金」をテーマにしたアカウント立ち上げについての質問。ターゲット設定やプロフィール設計について複数の具体的な質問が記載されている。"
    },
    {
        "index": 890,
        "filename": "image_66.png",
        "description": "K君からのコメント回答。転職・お金テーマのターゲット層（20代独身女性）の定義、プロフィール構成、キャッチコピー活用についてのアドバイスが記載されている。"
    },
    {
        "index": 891,
        "filename": "image_67.png",
        "description": "インスタグラムコメント欄でのやり取り。アカウントのサブテーマ決定、アカウント分けについて、またターゲット層の定義に関する複数の質問と回答が記載されている。"
    },
    {
        "index": 892,
        "filename": "image_68.png",
        "description": "おゆきユーザーからの質問。婚活系と自営業主の妻というテーマでアカウント並行作成について、アイコン選定やターゲット定義に関する具体的な質問が記載されている。"
    },
    {
        "index": 893,
        "filename": "image_69.png",
        "description": "K君からの回答。2つのテーマを扱う際のポジショニング、ファンの獲得戦略、エンタメ性の活用についてのアドバイスと具体的なアカウント例が記載されている。"
    },
    {
        "index": 894,
        "filename": "image_70.png",
        "description": "インスタグラムコメント欄でのユーザーとK君の会話。メッセージ機能の活用、アカウント戦略の個別相談についての質問と、オンラインサロンを目指している人についての言及が記載されている。"
    },
    {
        "index": 895,
        "filename": "image_71.png",
        "description": "りユーザーからのアカウント立ち上げ相談。フリーランス向けアカウントのコンセプト定義、マネタイズ方法についての複数の質問が記載されている。"
    },
    {
        "index": 896,
        "filename": "image_72.png",
        "description": "K君からのコメント回答。フリーランス向けアカウントのマネタイズ戦略（note販売、講座販売）、note営のコミュニティ機能活用についてのアドバイスが記載されている。"
    },
    {
        "index": 897,
        "filename": "image_73.png",
        "description": "bユーザーからの質問。インスタとLINEを組み合わせたマーケティング戦略についての相談が記載されている。"
    },
    {
        "index": 898,
        "filename": "image_74.png",
        "description": "インスタグラムコメント欄でのdユーザーとK君の会話。マネタイズポイント、フリーランス×SNSマーケ戦略、コンテンツ販売についての複数の質問と詳細な回答が記載されている。"
    },
    {
        "index": 899,
        "filename": "image_75.png",
        "description": "K君からのコメント回答。ビジネス系ジャンル向けのアフィリエイト活用、マネタイズの段階的アプローチについてのアドバイスが記載されている。"
    },
    {
        "index": 900,
        "filename": "image_76.png",
        "description": "平良信人ユーザーからの質問。医療関係での働きながらのインスタ・TikTok運用、ジャンル選定についての相談とK君からのアドバイスが記載されている。"
    },
    {
        "index": 901,
        "filename": "image_77.png",
        "description": "K君からのコメント回答。けっこうニッチなテーマでのアカウント戦略、ジャンル参入についてのアドバイスと具体的なアカウント例（医療系、健康系など）が記載されている。"
    },
    {
        "index": 902,
        "filename": "image_78.png",
        "description": "インスタグラムコメント欄での複数ユーザーとK君の会話。パーソナルトレーナー向けのアカウント戦略、ジャンルの細分化についての質問と詳細な回答が記載されている。"
    },
    {
        "index": 903,
        "filename": "image_79.png",
        "description": "K君からのコメント回答。ニッチなジャンル参入の戦略、商品市場の見つけ方、キズナシートの活用方法についてのアドバイスが記載されている。"
    },
    {
        "index": 904,
        "filename": "image_80.png",
        "description": "インスタグラムコメント欄でのユーザーとK君の最終段階の会話。アカウント構築の総合的なアドバイス、ジャンル選定の意思決定支援についての質問と詳細な回答が記載されている。"
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

    print(f"\n✓ Batch 885-904 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
