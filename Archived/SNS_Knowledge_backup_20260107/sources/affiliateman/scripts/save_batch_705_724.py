#!/usr/bin/env python3
"""
Batch 705-724の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
【2023年2月】質疑応答のまとめ記事から20枚
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 705-724の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 705,
        "filename": "image_105.png",
        "description": "K君へのコンサルティング相談を受けたユーザーこうへいからの感謝と相談内容をまとめた投稿。フォロワー増加やコミュニケーション活性化についてのアドバイスを記載。"
    },
    {
        "index": 706,
        "filename": "image_106.png",
        "description": "りょうかユーザーからの長文の相談投稿。アカウント開設の迷いや恋愛垢とビジネス垢の使い分けについてのマッチングアプリ関連の悩み相談。"
    },
    {
        "index": 707,
        "filename": "image_107.png",
        "description": "K君へのアドバイス回答投稿。アカウント開設の初期段階でのメッション選びやリール集約についての具体的なコンサルティング内容。"
    },
    {
        "index": 708,
        "filename": "image_108.png",
        "description": "りょうかユーザーとK君の間での複数コメントの相談応答。大学生の恋愛問題について具体的なアドバイスと相手の質問に対する返答。"
    },
    {
        "index": 709,
        "filename": "image_109.png",
        "description": "Naoユーザーからの質問コメント。27歳女性のマネタイズと複数のコンセプト設定、カフェ紹介とリール数獲得の関連についての相談。"
    },
    {
        "index": 710,
        "filename": "image_110.png",
        "description": "K君からNaoへの回答。20代30代女性向けの転職相談コンセプト設定とテーザー女性向け転職についてのコンサル提案。"
    },
    {
        "index": 711,
        "filename": "image_111.png",
        "description": "きよユーザーからの新規開設相談。ジャンル選定中で、複数のコンセプト（自分磨き・中古車情報・撮影など）の中から選びたいというもの。"
    },
    {
        "index": 712,
        "filename": "image_112.png",
        "description": "K君からきよへの回答。台数対象アフィリエイトとコンセプトのマッチングについての具体的なアドバイス。"
    },
    {
        "index": 713,
        "filename": "image_113.png",
        "description": "きよユーザーからの追加質問。男性向けスキンケアアカウントのコンセプト設定で、複数の悩みを抱えている状況についての相談。"
    },
    {
        "index": 714,
        "filename": "image_114.png",
        "description": "K君からの回答とレコメンダー紹介。男性美容向けアカウントの実例（kooki_mens_skincare、satoru_san96など）を提示。"
    },
    {
        "index": 715,
        "filename": "image_115.png",
        "description": "ふみユーザーからの新規開設相談。メンズ美容と家づくりの2つのジャンルで迷っている状況についての質問。"
    },
    {
        "index": 716,
        "filename": "image_116.png",
        "description": "K君からふみへの回答。メンズ美容コンセプトと家づくりコンセプトについての判断基準とアドバイス。"
    },
    {
        "index": 717,
        "filename": "image_117.png",
        "description": "りょうかユーザーからのDMコンサル経験についての質問。Instagramでダイエットアカウントと事業アカウントの開設経験分享。"
    },
    {
        "index": 718,
        "filename": "image_118.png",
        "description": "K君からりょうかへの回答。ビジネス系発信とTwitterフォロワーの質についての考察とアドバイス。"
    },
    {
        "index": 719,
        "filename": "image_119.png",
        "description": "だいユーザーからのダイエットアカウント開設相談。リサーチ項目や研究方法についての詳細な質問。"
    },
    {
        "index": 720,
        "filename": "image_120.png",
        "description": "K君からだいへの回答。コンセプト・アカウント開設前のリサーチ方法についての具体的なガイダンス。"
    },
    {
        "index": 721,
        "filename": "image_121.png",
        "description": "コタローユーザーからの相談。身元不詳の相手をターゲットとした悩みと自己肯定感向上の課題についての投稿。"
    },
    {
        "index": 722,
        "filename": "image_122.png",
        "description": "K君からコタローへの回答。プロフィール・ターゲット設定と投稿内容分析の重要性についてのアドバイス。"
    },
    {
        "index": 723,
        "filename": "image_123.png",
        "description": "コタローユーザーからの追加質問。改行後のターゲット設定と参考になるアカウントについての相談。"
    },
    {
        "index": 724,
        "filename": "image_124.png",
        "description": "K君からコタローへの最終回答。プロフィール改編・投稿内容分析・参考アカウントリストについての総合的なアドバイス。"
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

    print(f"\n✓ Batch 705-724 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
