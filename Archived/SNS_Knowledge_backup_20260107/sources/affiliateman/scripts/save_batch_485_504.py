#!/usr/bin/env python3
"""
Batch 485-504の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 485-504の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 485,
        "filename": "image_117.png",
        "description": "インスタグラムのDMスレッド画面。ユーザーシュウダイ.noterから「これ詳細聞きたいです!!!」というコメントと、複数のジャンル情報（駅名、不動産、私立大学、新築販売など）が表示されている。12月31日のタイムスタンプが見える。"
    },
    {
        "index": 486,
        "filename": "image_118.png",
        "description": "茶トラ兄弟からのコメント。ペット系漫画ブログでのマネタイズについてアドバイスを求めているフォロワーに対し、ブログ、YouTube、グッズ販売など複数の収益手段の選択肢を提案している。"
    },
    {
        "index": 487,
        "filename": "image_119.png",
        "description": "茶トラ兄弟からのコメント。ペット系漫画での停滞時の立場から、コンテンツ販売や猫のしけ相談でのマネタイズ幅の広がり、および参考アカウント情報が記載されている。"
    },
    {
        "index": 488,
        "filename": "image_120.png",
        "description": "むじユーザーからの質問。インスタグラムで薬剤師のアカウントを始めたがプロフィール設計と投稿内容について迷っているという相談。KKん回答が始まっている。"
    },
    {
        "index": 489,
        "filename": "image_121.png",
        "description": "KZユーザーからの質問。メンズコスメアカウントについてのリール作成や類似アカウント参考資料、TikTokでのコンテンツ展開について質問している。"
    },
    {
        "index": 490,
        "filename": "image_122.png",
        "description": "KKんからKZへの返信。メンズコスメのコンセプト設定について、カテゴリー分けや髪・スキンケアなどの具体的な提案をしている。"
    },
    {
        "index": 491,
        "filename": "image_123.png",
        "description": "ゆーじユーザーからの質問。外資系トップ企業経験を活かしたExcel資料作成やフィード・リール投稿、高フォロワーアカウントについてアドバイスを求めている。"
    },
    {
        "index": 492,
        "filename": "image_124.png",
        "description": "KKんからゆーじへの返信。女子大生向けアカウントについてのフォロワー数やリール戦略、フォロワー層へのアプローチ方法を指南している。"
    },
    {
        "index": 493,
        "filename": "image_125.png",
        "description": "ふみかユーザーからの質問。女子大生向け自分磨きアカウントについて、プロフィール設計と投稿内容への不安が述べられている。"
    },
    {
        "index": 494,
        "filename": "image_126.png",
        "description": "ふみかからのコメント。アカウントのターゲット設定について、プロフィール見直しや美容・ファッション関連のコンテンツ展開の課題が記載されている。"
    },
    {
        "index": 495,
        "filename": "image_127.png",
        "description": "KKんからふみかへの返信。アカウント参考資料のリンクを提供し、参加するコンテンツの質問に応じている。"
    },
    {
        "index": 496,
        "filename": "image_128.png",
        "description": "はしきんユーザーからの質問。インスタグラムの店舗集客について、投稿素材やハイライト素材が不足しているため、アカウントの開設に向けたタグ戦略が必要という相談。"
    },
    {
        "index": 497,
        "filename": "image_129.png",
        "description": "はしきんからのコメント。地域タグの使用方法について、都道府県名や市町村別の活用法、美容系アカウントでの地域タグ発信について質問している。"
    },
    {
        "index": 498,
        "filename": "image_130.png",
        "description": "はしきんからのコメント。地域タグ発信カテゴリーと骨盤矯正などのタグについての質問、およびベストな発信内容のハッシュタグ活用法の説明。"
    },
    {
        "index": 499,
        "filename": "image_131.png",
        "description": "そねユーザーからの質問。インスタグラムのリール再生数について、以前の投稿からの振り返りと現在の状況についての相談。複数のリール画像が表示されている。"
    },
    {
        "index": 500,
        "filename": "image_132.png",
        "description": "Koichiユーザーからの質問。TikTokの振BAN対策とラブホテルを題材にした動画についての相談。KKんからのアドバイスが記載されている。"
    },
    {
        "index": 501,
        "filename": "image_133.png",
        "description": "りょうユーザーからの質問。インスタグラムのダイエットアカウントについて、TikTokでのマネタイズ方法やTwitterでの告知について相談している。"
    },
    {
        "index": 502,
        "filename": "image_134.png",
        "description": "シンユーザーからの質問。メンズ美容アカウント運用について、顔出しに関する懸念やマネタイズ方法、参考となる実例アカウント情報が記載されている。"
    },
    {
        "index": 503,
        "filename": "image_135.png",
        "description": "saユーザーからの質問。TikTokで1投稿目で100万回再生、2投稿目以降の再生数低下の理由について、エンゲージメントとコメント数の関係の分析を求めている。"
    },
    {
        "index": 504,
        "filename": "image_136.png",
        "description": "Matsuユーザーからの質問。男性向けテーマでのTikTok・インスタグラム運用について、ダイエット・香水・整髪料などの紹介について相談。UKからの返信も表示されている。"
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

    print(f"\n✓ Batch 485-504 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
