#!/usr/bin/env python3
"""
Batch 1385-1404の画像説明を保存
【2023年6月】質疑応答のまとめ の image_63-82（20枚）
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

# Batch 1385-1404の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 1385,
        "filename": "image_63.png",
        "description": "インスタグラムのコメント欄でのやり取り。さわさんからの質問に対するくくんの回答スレッド。FacebookやTikTokの同時投稿、capcut編集時の音声挿入、snaptikでのアイコンなしの保存など複数の技術的な質問が出されている。"
    },
    {
        "index": 1386,
        "filename": "image_64.png",
        "description": "Twitterモーメント機能に関する質問と回答。さかまっちがTwitterモーメント作成方法について相談し、くくんが手順や注意点を説明している投稿スクリーンショット。"
    },
    {
        "index": 1387,
        "filename": "image_65.png",
        "description": "ブログ開設相談のスレッド。月収100万達成希望に関するCVについての質問と、まるさんやくくんの回答。ブログ執筆方法やnote移行についての情報共有。"
    },
    {
        "index": 1388,
        "filename": "image_66.png",
        "description": "Twitterプロフィールの紹介。dontoutsideというユーザーが、20歳の大学生から起業して年収を上げた実績を紹介している。Twitter運用やハイスペ美女など多様なコンテンツでフォロワーを獲得。"
    },
    {
        "index": 1389,
        "filename": "image_67.png",
        "description": "インスタグラムコメント欄での回答スレッド。yoshi yoshiユーザーがTwitterフォロワー5000人のオンラインサロン運営について質問し、くくんがオープンチャットの活用やロコミ施策の実績について回答。"
    },
    {
        "index": 1390,
        "filename": "image_68.png",
        "description": "Romuユーザーの質問に対するくくんの回答。Twitterアカウント方向性についてのアドバイスで、プロフィール情報や発信内容の具体例（会社員、年収1000万目標、転職、SNS副業）を紹介。"
    },
    {
        "index": 1391,
        "filename": "image_69.png",
        "description": "ルベウスからの質問とくくんの回答。SNS集客コンテンツ販売についてのアドバイスと、フォロワー企画のポリーム問題への対応方法についての実績共有。"
    },
    {
        "index": 1392,
        "filename": "image_70.png",
        "description": "ゆんユーザーからの質問と詳細な回答。サロン運営経験、Twitterやブログでの販売方法、料金設定、特典企画など多角的なビジネス展開についての長文アドバイス。"
    },
    {
        "index": 1393,
        "filename": "image_71.png",
        "description": "ゆんユーザーの継続的な質問に対するくくんの詳細回答。アメブロやTwitter運用での収入獲得方法、オプチャ活用、note販売実績など具体的なビジネス経験を共有。"
    },
    {
        "index": 1394,
        "filename": "image_72.png",
        "description": "インスタグラムコメント返信。くくんがアメブロ月10万円稼ぎ方法とアメブロ完全攻略についてのBrain教材宣伝、及びアメブロポジショニングについての実績を説明。"
    },
    {
        "index": 1395,
        "filename": "image_73.png",
        "description": "ゆんユーザーからの長文の相談内容。アメブロが空いている、主婦ジャンルで稼げないというお悩みについてのくくんによる親身なアドバイスと実体験の共有。"
    },
    {
        "index": 1396,
        "filename": "image_74.png",
        "description": "アメブロ運用についての質問と回答。アメブロペインスレート記事販売、Twitterアフィリエイト実績、楽天ルームについての収入獲得方法に関する詳細な説明。"
    },
    {
        "index": 1397,
        "filename": "image_75.png",
        "description": "アメブロ月10万達成方法についての具体的なアドバイス。ゆんが記した数値実績やTwitterプレイ作成、Brain記事販売、販売期限付き企画などの戦略について詳細に説明。"
    },
    {
        "index": 1398,
        "filename": "image_76.png",
        "description": "くくんからのアメブロ運用に関する複数の具体的な回答。オプチャ活用、販売記事についての相談、キャンバのSNS運用、月100ポジショニング方法についての実践的なアドバイス。"
    },
    {
        "index": 1399,
        "filename": "image_77.png",
        "description": "Brain教材の販売戦略についての質問と回答。くくんが記事宣伝ツイートの工夫やTwitter並行運営についてのアドバイスと、期間限定セール戦略について説明。"
    },
    {
        "index": 1400,
        "filename": "image_78.png",
        "description": "アメブロプレイン作成やTwitter副業についての詳細な質問回答。tipsとの販売月、ブロガー仕事内容についての相談と、くくんによる親身で実践的なアドバイス。"
    },
    {
        "index": 1401,
        "filename": "image_79.png",
        "description": "Brain教材ガイドの販売宣伝画像。アメブロ完全攻略ガイド（0円から月3万円ロードマップ）のBrain販売告知で、Brain公式による推奨・販売開始2日で300部突破の実績掲載。"
    },
    {
        "index": 1402,
        "filename": "image_80.png",
        "description": "ゆんユーザーからの長文コメント。K くんへの感謝、アメブロ運用についての学習状況、ファン化エキスパート講座受講や実績PRについてのお悩み相談と学習進捗の共有。"
    },
    {
        "index": 1403,
        "filename": "image_81.png",
        "description": "アメブロプレイン販売についての具体的な質問と、くくんによる詳細な回答スレッド。販売記事の扱い方やBrain改修について、tipsとの連携や初販売時の価格設定についての実践的なアドバイス。"
    },
    {
        "index": 1404,
        "filename": "image_82.png",
        "description": "インスタグラムコメント欄での大学初心者向けの相談。アメブロ空いている理由やブログポジショニングについての質問に対するくくんの長文回答と実績共有。"
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

    print(f"\n✓ Batch 1385-1404 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
