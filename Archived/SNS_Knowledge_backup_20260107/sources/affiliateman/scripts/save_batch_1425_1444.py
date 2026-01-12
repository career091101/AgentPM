#!/usr/bin/env python3
"""
Batch 1425-1444の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1425-1444の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1425,
        "filename": "image_103.png",
        "description": "アフィリエイター「るる」による1ヶ月前のコンテンツ販売・コンサル関連の質問。ハンドメイド作家で活動3日目の購入経験と月2円稼ぐための課題について相談。"
    },
    {
        "index": 1426,
        "filename": "image_104.png",
        "description": "K君による教材販売と稼ぐ系アカウント構築のアドバイス。月50万円相当の稼ぎを目指す教材開発、オープンチャット活用、コンテンツ販売による売上拡大戦略を詳細に説明。"
    },
    {
        "index": 1427,
        "filename": "image_105.png",
        "description": "A子による教材販売開始の報告。3日先行販売で通常価格から10,000円オフの販売開始、24時間で32名購入、Twitter730人・Instagram570人・LINE95人のフォロワー状況を共有。"
    },
    {
        "index": 1428,
        "filename": "image_106.png",
        "description": "K君によるニッチジャンルでのポジション取得と教材販売戦略のアドバイス。マネタイズ構造、新規購入者の掘り起こし、月100人規模の見込み客創出の手法を説明。"
    },
    {
        "index": 1429,
        "filename": "image_107.png",
        "description": "K君による教材販売と実績作りの重要性に関するアドバイス。オープンチャット経由のコンサル人数増加、毎月投稿ペースでサロン誘導、LINE施策の組み合わせについての解説。"
    },
    {
        "index": 1430,
        "filename": "image_108.png",
        "description": "K君による企業マネタイズ戦略に関するアドバイス。セミナー動画とアーカイブ化の戦略、フォロワー企画の見直し、オープンチャット限定ZOOM相談について具体的な指導。"
    },
    {
        "index": 1431,
        "filename": "image_109.png",
        "description": "A子による複数プラットフォーム運用に関する報告と質問。オープンチャット8名・個別オプチャ3名の顧客状況、セミナー動画とアーカイブ化戦略、初期段階でのチャネル選択の指南。"
    },
    {
        "index": 1432,
        "filename": "image_110.png",
        "description": "こはく（20代転職者）による業務アカウント相談。TikTokでの転職発信によるフォロワー1000人達成戦略、オープンチャット導入による短期的なイメージ作成と顧客化の指導。"
    },
    {
        "index": 1433,
        "filename": "image_111.png",
        "description": "K君によるTikTok転職アカウント戦略のアドバイス。公式リールからオープンチャット参加による顧客化、TikTok-Instagram連携、低リスク副業戦略についての詳細解説。"
    },
    {
        "index": 1434,
        "filename": "image_112.png",
        "description": "公式カラコン通販メイリー（23日前）による顧客相談。EC事業の設定、Instagram20名フォロワーの商品認知課題、TikTok300フォロワーの状況と差別化戦略についての解説。"
    },
    {
        "index": 1435,
        "filename": "image_113.png",
        "description": "K君によるカラコンビジネス向けのマネタイズ戦略。中国語アカウント活用、Instagram差別化戦略、マッチングアプリの女性獲得層への販売戦略を詳細に提案。"
    },
    {
        "index": 1436,
        "filename": "image_114.png",
        "description": "ぜらによるTikTok恋愛コンテンツでの副業相談。1000フォロワー到達とマネタイズ検討、tips作成の課題（マッチングアプリ・ナンパ経験不足）、モデルシャネル攻略に関する質問。"
    },
    {
        "index": 1437,
        "filename": "image_115.png",
        "description": "K君によるTikTok恋愛ジャンルのマネタイズアドバイス。マッチングアプリ攻略、ナンパスキル習得、大手デキ講習による月120万円達成、フォロワー3000人による月100万円の実例を紹介。"
    },
    {
        "index": 1438,
        "filename": "image_116.png",
        "description": "K君による恋愛コンテンツマネタイズの補足。女性恋愛ジャンル、RTAサロン利用による売上拡大、Twitter連携による高単価販売、コンサル化による月250万円達成の事例説明。"
    },
    {
        "index": 1439,
        "filename": "image_117.png",
        "description": "アネホによるTwitter恋愛・モテ系マネタイズ相談。夜職美女モデルの発信コンセプト設定、ChatGPTプロンプト活用、マネタイズ施策の複合実行についての複数の質問。"
    },
    {
        "index": 1440,
        "filename": "image_118.png",
        "description": "K君による夜職美女アカウントのマネタイズ戦略。Twitter2000名・noteフォロワー500名・noteメンバーシップ22万円売上の実績、ビジネス系とのハイブリッド運用についての指導。"
    },
    {
        "index": 1441,
        "filename": "image_119.png",
        "description": "tkによる金融（株式投資）ジャンルのマネタイズ相談。Twitter2000名・noteフォロワー500名・noteメンバーシップ22万円売上、LTVライフタイムバリュー改善戦略についての課題提示。"
    },
    {
        "index": 1442,
        "filename": "image_120.png",
        "description": "K君による金融ジャンルマネタイズの回答。ビジネス系アカウントの広角性、Twitter・note併用、LTVライフタイムバリュー改善の方向性についてのアドバイス。"
    },
    {
        "index": 1443,
        "filename": "image_121.png",
        "description": "やまによるInstagramマネタイズ方法についての質問。ジャンル選択段階でのK君への相談、サウナジャンル参入についてのポジション取得と商品化の指導。"
    },
    {
        "index": 1444,
        "filename": "image_122.png",
        "description": "K君によるサウナジャンル・美容ジャンルのマネタイズ戦略。Tinder攻略、複合ジャンルマネタイズ、40代男性向けのアフィリ訴求、ストーリーにおける個人性・フォロワー年代別構成の考察。"
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

    print(f"\n✓ Batch 1425-1444 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
