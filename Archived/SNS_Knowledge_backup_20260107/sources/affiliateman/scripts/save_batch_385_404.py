#!/usr/bin/env python3
"""
Batch 385-404の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 385-404の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 385,
        "filename": "image_17.png",
        "description": "Instagramコメント欄でのアカウント設計に関する質問内容。宿泊施設のアカウント運用について、退職ジャンル特化アカウントと新しく恋愛占い恋愛コンサルのアカウント運用方法についてK君からアドバイスを求めている。"
    },
    {
        "index": 386,
        "filename": "image_18.png",
        "description": "K君による恋愛・占いジャンルのアカウント運用についての回答。4つのフィードバック内容が記載されている：固定ビンの設置、ロゴをキャラクター化する、ハイライト活用、文字入れの工夫。"
    },
    {
        "index": 387,
        "filename": "image_19.png",
        "description": "恋愛・占いジャンルのマネタイズに関する質問と回答。12月中に40の恋愛ジャンルアカウントが追加され、市場規模についての解説。アフィ、コンテンツ販売、コンサル、オンラインサロンなど4つのマネタイズ方法が記載されている。"
    },
    {
        "index": 388,
        "filename": "image_20.png",
        "description": "恋愛・占いジャンルのアカウント参入に関するK君の回答。市場規模の詳細説明とフォロワー数別の戦略が記載。女性ターゲットはフォロワー7万人くらい、男性ターゲットはフォロワー4万人くらいが目安であることが解説されている。"
    },
    {
        "index": 389,
        "filename": "image_21.png",
        "description": "ほみこからの質問で、毎日100-300人以上がコンスタントにフォローさせているが低速中であること、K君がシェアしてくれたストーリーへの返信PDM増が望まれていることが記載。他にフォロワー増加の『回復』施策についての質問も含まれている。"
    },
    {
        "index": 390,
        "filename": "image_22.png",
        "description": "もりからの複数質問：3点アカウント運用に関する具体的相談。宿泊施設のアカウントについてK君からのアドバイスを含む、運営15万人の月50円目指しやマネタイズ方法に関する質問内容。"
    },
    {
        "index": 391,
        "filename": "image_23.png",
        "description": "K君からもりへの回答。技術面でのフィードバック：転職特化アカウントの投稿手法改善、退職代行サービス関連の投稿、ハイライト設置、文字入れの工夫などが提案されている。"
    },
    {
        "index": 392,
        "filename": "image_24.png",
        "description": "恋愛・占いジャンルのアカウント参入に関する詳細説明。市場規模の見極め方、転職・就活関連ジャンルとの違い、女性・男性ターゲットのフォロワー数目安などが記載。"
    },
    {
        "index": 393,
        "filename": "image_25.png",
        "description": "K君からたくみへの回答。11月下旬から自分磨き・転換ジャンルでスタートした際の目標設定とマネタイズについてのアドバイス。月50万、100万円目指しについての具体的な金額と目標が記載されている。"
    },
    {
        "index": 394,
        "filename": "image_26.png",
        "description": "たくみからのアフィリエイト訴求タイミングに関する質問。1時間5000円くらいで恋愛相談ができるコンサル内容と、月50円目指しについての無料LINE勧誘、転換支援相談などの展開についての質問。"
    },
    {
        "index": 395,
        "filename": "image_27.png",
        "description": "kamiからの恋愛系リポストアカウント関連の質問。ハッシュタグ検索で恋愛系のリポストアカウントを見つけたいことについてK君にシェアを求めている。"
    },
    {
        "index": 396,
        "filename": "image_28.png",
        "description": "K君からkamiへの回答。ただ恋愛アカウントリポスト自体が難しいというアドバイスと、関連フォロワー確認方法が記載。恋愛アカウントをハッシュタグで確認する際の工夫について説明。"
    },
    {
        "index": 397,
        "filename": "image_29.png",
        "description": "たくみからの詳細な質問内容：アフィリエイト訴求のタイミング、マッチングアプリ訴求、フォロワー15万人で月10-15万円売上目安についての質問。コンテンツ販売やコンサルについての詳細説明も記載。"
    },
    {
        "index": 398,
        "filename": "image_30.png",
        "description": "やなせからのバックエンド関連の質問。LINEリスト取りで転換支援講座について質問している内容と、インスタのテーマ変更に関するマーケティング課題についての相談が記載。"
    },
    {
        "index": 399,
        "filename": "image_31.png",
        "description": "K君からやなせへの回答。マーケティングとテーマ変更の関係性や、エンゲージメント向上のための施策について詳しく説明。リール中心の運営とダイエットテーマについての提案が記載されている。"
    },
    {
        "index": 400,
        "filename": "image_32.png",
        "description": "ノースからの悩み相談：資産運用ジャンルでフォロワー14万人だが、10月から11月へのフォロワー減少対策についての質問。発見欄露出や関係性向上についての課題が記載されている。"
    },
    {
        "index": 401,
        "filename": "image_33.png",
        "description": "ほみこからの質問：インスタのピン付けで3個でどの程度の効果があるのか、ビン付けの活用方法についての質問が記載されている。"
    },
    {
        "index": 402,
        "filename": "image_34.png",
        "description": "やすからのダイエットアカウント関連の質問。無料プレゼント記載予定とフォロワー向け公式ラインについての施策、および無料ズームコンサルの募集タイミング、セールスまでの流れについての質問。"
    },
    {
        "index": 403,
        "filename": "image_35.png",
        "description": "やすからの詳細な質問：フェーズ1・2での募集方法、セールスまでの流れ、ズームコンサル応募時の事前ヒアリング、および収益設定についての複数フェーズの説明。"
    },
    {
        "index": 404,
        "filename": "image_36.png",
        "description": "やすからのコンサル前事前準備に関する長めの質問。ロードマップ作成方法、ダイエットロードマップの詳細説明、およびセールスプロセスの流れについてK君へのアドバイス求め。"
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

    print(f"\n✓ Batch 385-404 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
