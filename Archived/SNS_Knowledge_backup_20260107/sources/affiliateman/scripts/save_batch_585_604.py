#!/usr/bin/env python3
"""
Batch 585-604の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 585-604の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 585,
        "filename": "image_41.png",
        "description": "【2023年1月】質疑応答まとめの記事内でのユーザー質問スレッド。フォローの仕組みやDMフォローなどのInstagram運用に関する複数の相談事項が列挙されている。"
    },
    {
        "index": 586,
        "filename": "image_42.png",
        "description": "Twitter上の@るるというユーザーによる25日前のツイート返信。副業コンサルの受注方法やTikTokでのジャンル選択、SNS戦略についての具体的なアドバイスが記載されている。"
    },
    {
        "index": 587,
        "filename": "image_43.png",
        "description": "Kくんからの相談に対する回答。単発コンサルの価格設定（1ヶ月5万円、3ヶ月14万円、6ヶ月28万円）と、ビジネスアカウントのコンセプト構築について説明している。"
    },
    {
        "index": 588,
        "filename": "image_44.png",
        "description": "一ヶ月コンサルの具体的な内容と3ヶ月目のゴール設定についての説明。外見・内面・会話の3つの項目で女性の魅力を高めるコンサルティング方法が提示されている。"
    },
    {
        "index": 589,
        "filename": "image_45.png",
        "description": "ビジネス系SNSコンサル歴4年間の経験と、外見改善系コンサルティングについての説明。KくんがSNS運用で成功してきた軌跡と、教えるアウトプットについて述べられている。"
    },
    {
        "index": 590,
        "filename": "image_46.png",
        "description": "けんとというユーザーからの賃貸不動産ビジネスについての相談。地方都市での不動産ビジネス成功要因と、公式LINEでのリード育成戦略についての質問が含まれている。"
    },
    {
        "index": 591,
        "filename": "image_47.png",
        "description": "ひなというユーザーからの有益な情報請求と、リサーチについての質問。ベンチマークの見つけ方やダイエットアカウント運用時の優位性確保についての問い合わせ。"
    },
    {
        "index": 592,
        "filename": "image_48.png",
        "description": "マークという利用者からのASP公式による発表資料に関する質問。平均商品200万円くらいの高単価商品と定期購買3000円以上の商品の報酬額についての具体例が列挙。"
    },
    {
        "index": 593,
        "filename": "image_49.png",
        "description": "マークへの回答。成果地点の浅いケースと、CVRの最適化についてのアドバイス。美容整形やクリニックでの無料カウンセリングから報酬発生までの流れについて説明している。"
    },
    {
        "index": 594,
        "filename": "image_50.png",
        "description": "りつかというユーザーからの新規アカウント設計についての相談。子育てジャンルのコンセプト決定やSNS選択、マネタイズ方法についての質問が含まれている。"
    },
    {
        "index": 595,
        "filename": "image_51.png",
        "description": "りつかへのアドバイス。発信SNS選択やリリース時期、初期フォロワー確保方法についての具体的なアドバイス。Twitterから始めるメリットが説明されている。"
    },
    {
        "index": 596,
        "filename": "image_52.png",
        "description": "有料コンサルと面談形式についての質問と、noteでのオフラインサロン立ち上げに関する相談。月額月間コミュニティサービスの活用方法が述べられている。"
    },
    {
        "index": 597,
        "filename": "image_53.png",
        "description": "しんたろうというユーザーからの『twitter×恋愛系』ジャンルについての相談。2023年からの流行傾向と、女性ターゲットの設定についての質問。"
    },
    {
        "index": 598,
        "filename": "image_54.png",
        "description": "shintarouへの具体的な回答。TikTok活用を含むジャンル選択のポイントと、恋愛マッチングアプリ攻略時のSNS活用戦略についてのアドバイス。"
    },
    {
        "index": 599,
        "filename": "image_55.png",
        "description": "たつきというユーザーからのアフィリエイト事業開始時のジャンル選択についての相談。ビジネス系、ダイエット系、恋愛系ジャンルにおけるスキルと経験の重要性が議論されている。"
    },
    {
        "index": 600,
        "filename": "image_59.png",
        "description": "SNS攻略サロン限定の『12月のKくんのアウトプット』を示す青色バナー。インスタ、TikTok、Twitterの3つのプラットフォームでの発信内容をまとめたサムネイル画像。"
    },
    {
        "index": 601,
        "filename": "image_01.png",
        "description": "【2023年2月】質疑応答のまとめ記事の冒頭。インスタでのプレゼント企画について、複数の相談質問が寄せられていることが示唆されている。"
    },
    {
        "index": 602,
        "filename": "image_02.png",
        "description": "ひなたというユーザーからのプレゼント企画と画像配布に関する複数の質問。アカウント分け戦略とプレゼント配布方法の色々なパターンについて質問。"
    },
    {
        "index": 603,
        "filename": "image_03.png",
        "description": "Kくんからの回答。プレキャンについてのDM手動返信の仕組みや、istep活用によるDM自動応対についての説明が含まれている。"
    },
    {
        "index": 604,
        "filename": "image_04.png",
        "description": "ハナというユーザーからの施設系アカウント設計について。勉強系アカウントのアカウント分け戦略と、ライティングやデザイン面でのスキル習得についての相談。"
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

    print(f"\n✓ Batch 585-604 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
