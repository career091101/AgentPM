#!/usr/bin/env python3
"""
Batch 505-524の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
【12月】質疑応答まとめ記事から20枚
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 505-524の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 505,
        "filename": "image_137.png",
        "description": "U.Kユーザーの返信スレッド。「外部誘導意識しつつ、DM営業としてみます」という男性向け恋愛アカウント運用に関する質問と回答。フォロワーを増やすための戦略についての会話。"
    },
    {
        "index": 506,
        "filename": "image_138.png",
        "description": "ぼみおユーザーの質問スレッド。Twitter運用での収益化に関する相談で、選択代行活用についてKくんが基本的な考え方を説明している画像。"
    },
    {
        "index": 507,
        "filename": "image_139.png",
        "description": "りょうユーザーの質問。Instagramのダイエットアカウント運用とTwitter発信について、どちらを優先すべきかについてKくんが回答している会話スレッド。"
    },
    {
        "index": 508,
        "filename": "image_140.png",
        "description": "りょうユーザーの返信。アカウント作成やInstagramとTwitterの連携戦略について、Kくんが詳細に説明している長めのテキストスレッド。"
    },
    {
        "index": 509,
        "filename": "image_141.png",
        "description": "ぼみおユーザーの質問。フォロワー状況（imp300～500程度、画像系投稿500～10000程度）とフォロワー企画についての具体的な相談内容。"
    },
    {
        "index": 510,
        "filename": "image_142.png",
        "description": "Kくんのぼみおへの回答。フォロワー状態の分析や、質問への具体的なアドバイスを記載したテキスト応答スレッド。"
    },
    {
        "index": 511,
        "filename": "image_143.png",
        "description": "ぼみおユーザーの返信。Kくんの提案に対する感謝と、フォロワーシナジー構築について質問を続けている会話。"
    },
    {
        "index": 512,
        "filename": "image_144.png",
        "description": "Toyoユーザーのnoteリリース報告。Twitterで質問への回答として、note公開とその活用戦略についてのやり取り。"
    },
    {
        "index": 513,
        "filename": "image_145.png",
        "description": "せいめ月109万円の恋愛noteユーザーの質問。TwitterアルゴリズムやKくんの運用戦略について具体的な相談内容を記載。"
    },
    {
        "index": 514,
        "filename": "image_146.png",
        "description": "Kくんのせいめ月109万円の恋愛noteへの詳細回答。Twitterでのプロフィール運用やツイート施策の具体的なステップを説明。"
    },
    {
        "index": 515,
        "filename": "image_147.png",
        "description": "ToyoユーザーとKくんのマネタイズ戦略についての会話スレッド。noteリリースのタイミングや販売方法について複数のTweet参照リンク付き。"
    },
    {
        "index": 516,
        "filename": "image_148.png",
        "description": "うにせユーザーの質問。Twitterアカウント@kahoko_0の予約ツイートと自動投稿戦略、アフィリエイト利用についての相談。"
    },
    {
        "index": 517,
        "filename": "image_149.png",
        "description": "Kくんのうにせへの回答。自動アカウント運用のコンテンツ販売での収益化や、Twitter運用初期段階でのスタート方法についての詳細説明。"
    },
    {
        "index": 518,
        "filename": "image_150.png",
        "description": "うにせユーザーの3つの具体的な質問。①自動アカウントでのコンテンツ販売可否、②Twitter運用初期段階でのスタート、③Twitter知識ゼロからのスタート方法。"
    },
    {
        "index": 519,
        "filename": "image_151.png",
        "description": "うにせユーザーへの返信。実績についての質問で、100日でフォロワーOO人増えたケースと、実績をもとにした施策決定について説明。"
    },
    {
        "index": 520,
        "filename": "image_152.png",
        "description": "涼ユーザーの禁煙に関する相談とSNS Twitter発信について、新たに禁煙アカウントを作成してやるかについての質問。"
    },
    {
        "index": 521,
        "filename": "image_153.png",
        "description": "やなせユーザーの質問。参入ジャンル判断（メンタル系、自己啓発、HSP、うつ病）について、マネタイズの難易度に関する相談スレッド。"
    },
    {
        "index": 522,
        "filename": "image_154.png",
        "description": "Kくんのやなせへの回答。HSPやうつ病の自己啓発について、自身が定義を上げるコンサルやマネタイズ戦略についての詳細説明。"
    },
    {
        "index": 523,
        "filename": "image_155.png",
        "description": "やなせユーザーのnoteと情報商材についての質問。noteリリース月の売上目安（月5～3万のイメージ）とバックエンド販売についての相談。"
    },
    {
        "index": 524,
        "filename": "image_156.png",
        "description": "やなせユーザーの最終質問。グラウドワークスでの『セクシー系Twitterアカウント運用』での単価と工数に関する具体的な費用見積り相談。"
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

    print(f"\n✓ Batch 505-524 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
