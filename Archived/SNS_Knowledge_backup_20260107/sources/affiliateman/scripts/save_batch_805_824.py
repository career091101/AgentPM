#!/usr/bin/env python3
"""
Batch 805-824の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 805-824の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 805,
        "filename": "image_205.png",
        "description": "InstagramのDM質問機能の画面スクショ。「下記だいなアプリ活用している人です！」と問い合わせに関する複数の質問・回答スレッド。記事【2023年2月】質疑応答のまとめの関連コンテンツ。"
    },
    {
        "index": 806,
        "filename": "image_206.png",
        "description": "アフィリエイトの詳細な説明図。「アフィの諸求方法」「Price2alert」「ルエンサー（秘）情報収集テク」など複数のツールと利用方法が図解されている。無料ツールと有料ツールの活用例を示すコンテンツ。"
    },
    {
        "index": 807,
        "filename": "image_207.png",
        "description": "楽天アフィリエイト商品選定のコツに関する説明図。Price2alertツールを使った「売れ筋商品」と「3万個以上売れた化粧水」の価格推移グラフが表示されている。"
    },
    {
        "index": 808,
        "filename": "image_208.png",
        "description": "アフィリエイト活動に関するDM質問と回答スレッド。販売戦略について「毎月の値下げ」「セール前後の売上変動」について詳しく説明されている。"
    },
    {
        "index": 809,
        "filename": "image_209.png",
        "description": "アフィリエイト活動の売上戦略に関するDM質問・回答。セール前後での価格変動、グラフでのチェック方法、メルカリやAmazonでの売上工夫について解説。"
    },
    {
        "index": 810,
        "filename": "image_210.png",
        "description": "ユーザー「はろ」からのChatGPT活用とツール販売に関する質問。ChatGPTで自動化ツール作成→販売、1件3000～5000円で売る活用例について説明されている。"
    },
    {
        "index": 811,
        "filename": "image_211.png",
        "description": "「つばき」ユーザーのNFTブログ・仮想通貨・Twitterに関する相談スレッド。11月仮想通貨・NFTブログで36万円稼いだ実績や競争力、ファンを増やす戦略について質問。"
    },
    {
        "index": 812,
        "filename": "image_212.png",
        "description": "トヨ（@トヨ）ユーザーのマネタイズ戦略に関する質問。一昨日のツイートの下に記載されたツイート内容や、ツイートアナリティクスの画面が表示されている。"
    },
    {
        "index": 813,
        "filename": "image_213.png",
        "description": "Twitterユーザー「トヨ」のマネタイズ関連の質問に対する回答。Noteの売却戦略、エロ本ジャンルの利益化、英語ブログ運営について詳しく説明されている。"
    },
    {
        "index": 814,
        "filename": "image_214.png",
        "description": "英語学習・TOEIC・ビジネス系ジャンルに関する複数ユーザーの質問コーナー。個人的な意見やコンサル具体例、ニーズの捉え方について回答されている。"
    },
    {
        "index": 815,
        "filename": "image_215.png",
        "description": "ユーザー「Kan」のアフィリエイト相談。サロンメンバー向けのアフィリエイト提携例と報酬情報を示した図解。不動産・確定申告・AI競馬など複数のアフィ案件が紹介されている。"
    },
    {
        "index": 816,
        "filename": "image_216.png",
        "description": "ユーザー「吉田」からの転職・キャリアに関する相談。EPCの高さ、ASP選定戦略、SNSアカウント運営目標の設定方法について複数の質問と回答。"
    },
    {
        "index": 817,
        "filename": "image_217.png",
        "description": "転職・就活アフィリエイト相談への詳細な回答。ASP選定方法、ランキング戦略、ネイティブアド運用など実践的なアドバイスが記載されている。"
    },
    {
        "index": 818,
        "filename": "image_218.png",
        "description": "ユーザー「吉田」のアフィリエイトプログラム審査と売上目標に関する追加質問。ASP連携、フォーム最適化、キャリアコンサル戦略について詳しく解説。"
    },
    {
        "index": 819,
        "filename": "image_219.png",
        "description": "ユーザー「RN」からのボルトガル語アカウント運営に関する質問。ポルトガル語ブログ・SNS運用、マネタイズ方法、フォロワー数に関する相談。"
    },
    {
        "index": 820,
        "filename": "image_220.png",
        "description": "トヨ（@トヨ）ユーザーのマネタイズ戦略に関する提案。英語ジャンルとビジネス系の比較、Noteマネタイズの有効性について図解を含め説明されている。"
    },
    {
        "index": 821,
        "filename": "image_221.png",
        "description": "トヨ（@トヨ）のツイートアナリティクス画面と、マネタイズに関する追加質問。Noteの売却戦略、英語ブログとエロ本ジャンルでのマネタイズ方法の実例。"
    },
    {
        "index": 822,
        "filename": "image_222.png",
        "description": "ユーザー「かける」と「トヨ」のコンテンツ戦略に関する相談スレッド。エロ本ジャンルとビジネス系の比較、Note売却の有効性、英語ブログ運営について。"
    },
    {
        "index": 823,
        "filename": "image_223.png",
        "description": "トヨ（@トヨ）ユーザーとコンサルのやり取り。Noteマネタイズ、英語ブログの運営、TOEIC学習とコンサル活動の組み合わせについて詳しく解説。"
    },
    {
        "index": 824,
        "filename": "image_227.png",
        "description": "「SNS攻略サロンの使い方 / 最大限に使いこなそう」というタイトルの図解。Q&Aのマーク、提携金の矢印、ZOOMウェビナー、複数ジャンルのアイコンが示されている。"
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

    print(f"\n✓ Batch 805-824 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
