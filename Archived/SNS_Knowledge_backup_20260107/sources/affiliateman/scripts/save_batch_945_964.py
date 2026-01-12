#!/usr/bin/env python3
"""
Batch 945-964の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
記事: 【2023年3月】質疑応答のまとめ (20枚)
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 945-964の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 945,
        "filename": "image_121.png",
        "description": "インスタグラムのコメント欄。ユーザー「ふみ」がアラサー向けコンテンツのアラサーママver.での運用や、アラサーママからのコンサルティング活用について質問している。"
    },
    {
        "index": 946,
        "filename": "image_122.png",
        "description": "Instagram DM画面。ユーザー「栗」がバイトアカウント作成で投稿し、バイトジャンルのアカウントを見つけ、デザインでターゲットを女子学生にするか質問。K君（回答者）が複数ジャンルの運用を検討するよう提案。"
    },
    {
        "index": 947,
        "filename": "image_123.png",
        "description": "ユーザー「まさと」のコメント。滋賀県のおかけ系アカウントについての質問と、YouTubeビデオ視聴の提案を含む。K君が滋賀のテーマ選択やPR要件について回答。"
    },
    {
        "index": 948,
        "filename": "image_124.png",
        "description": "K君の回答欄。滋賀県の観光地ガイド作成や運用方法について詳細に説明。リール投稿との組み合わせやフォロワー増加戦略を提案。"
    },
    {
        "index": 949,
        "filename": "image_125.png",
        "description": "ユーザー「うしまします」のコメント。企業アカウント運用のためのエンゲージメント向上やフォロワー増加方法について質問。K君がDM数やストーリー閲覧率などの施策を説明。"
    },
    {
        "index": 950,
        "filename": "image_126.png",
        "description": "ユーザー「フミ」の転職経験に関する相談。夫の転職や年収、キャリア計画について質問。ターゲット年齢層の検討についてのK君の回答。"
    },
    {
        "index": 951,
        "filename": "image_127.png",
        "description": "K君の詳細回答。転職アカウントの発信者・コンサル候補・ターゲット年齢層の設定について、複数パターンを提案する説明。"
    },
    {
        "index": 952,
        "filename": "image_128.png",
        "description": "ユーザー「Romu」のコメント。転職キャリアやメンタルトレーニングの概念についての質問スレッド。複数ジャンルのビジネスアカウント最適化について議論。"
    },
    {
        "index": 953,
        "filename": "image_129.png",
        "description": "Romu氏の詳細なプロフィール。Web系企業からの転職経験、フリーランス経験を持つ32歳（転職当時29歳）のHSS型HSP。ストーリーズで得情報発信の考え方を説明。"
    },
    {
        "index": 954,
        "filename": "image_130.png",
        "description": "ユーザー「りょう」のコメント。Instagramビジネス運用について、ターゲット層に対するアカウント内容やマネタイズ方法の提案を求めている。"
    },
    {
        "index": 955,
        "filename": "image_131.png",
        "description": "K君の回答。パーソナルトレーナーの集客戦略について、複数ジャンルの組み合わせやコンサル活用のメリットを詳細に説明。"
    },
    {
        "index": 956,
        "filename": "image_132.png",
        "description": "りょう氏とK君の会話。アカウント運用のアドバイス、ハイライトの役割、フォロワー増加とコンサルティングの関係についての論議。"
    },
    {
        "index": 957,
        "filename": "image_133.png",
        "description": "K君の長文説明。リール作成でのフォロワー獲得戦略、文字や音声の活用、ビジネスジャンルでのリール活用方法について詳細なアドバイス。"
    },
    {
        "index": 958,
        "filename": "image_134.png",
        "description": "K君の継続回答。ハイライト活用法、アカウント初期段階でのコンサル記載なし戦略、フォロワー層のターゲティングについての説明。"
    },
    {
        "index": 959,
        "filename": "image_135.png",
        "description": "りょう氏の追加質問。ダイエットアカウントとビジネスアカウントの流れの違いについて。K君がDMでのアプローチ方法を提案。"
    },
    {
        "index": 960,
        "filename": "image_136.png",
        "description": "りょう氏とK君の会話。アカウント採用基準の決め方、YES/NOで対応するDM返答方法についてのディスカッション。"
    },
    {
        "index": 961,
        "filename": "image_137.png",
        "description": "Hideki Otani氏の質問。同棲カップルのアカウント作成や収益化についての相談。複数マネタイズ戦略（マネーフォワード、マッチングアプリなど）を列挙。"
    },
    {
        "index": 962,
        "filename": "image_138.png",
        "description": "K君のHideki Otani氏への回答。アカウント初期設定での1つのテーマ選定方法や、ジャンル分岐による複数テーマ運用の提案。"
    },
    {
        "index": 963,
        "filename": "image_139.png",
        "description": "ユーザー「ペイ」のコメント。サロン参加による転職ジャンルの設定や、キャリアジャンル・Web業界・小ジャンルの分類について質問。"
    },
    {
        "index": 964,
        "filename": "image_140.png",
        "description": "ペイ氏の詳細質問。転職ジャンルの細分化について（Web業界未経験からの転職に特化など）。Instagramアカウント設定に関するアドバイスを求めている。"
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

    print(f"\n✓ Batch 945-964 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
