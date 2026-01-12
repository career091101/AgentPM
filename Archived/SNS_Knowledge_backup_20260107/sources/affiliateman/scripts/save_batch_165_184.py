#!/usr/bin/env python3
"""
Batch 165-184の画像説明を保存
実際に画像を読み込んで詳細な説明を生成
"""

import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/affiliateman")

# Batch 165-184の画像説明（実際に読み込んだ内容）
batch_descriptions = [
    {
        "index": 165,
        "filename": "image_24.png",
        "description": "インスタグラムアカウント「renai_kyoshitsu」のプロフィール画面。恋愛教室というテーマで投稿1145件、フォロワー2.2万人を抱えており、女性の恋愛についての悩み相談や関連情報を発信している。"
    },
    {
        "index": 166,
        "filename": "image_25.png",
        "description": "ジャニーズ情報を発信するアカウント「johnnys_infogram」とジャニオタ向けのアカウント「j_otachan」の紹介。フォロワー数が3.4万人と5.8万人を持つジャニーズ関連アカウントの事例。"
    },
    {
        "index": 167,
        "filename": "image_26.png",
        "description": "ディズニー情報を発信する個人ブログアカウント「disneypak_maru3」と、ディズニー専門情報メディア「disney_uranania」の紹介。フォロワー数は2.1万人と9.8万人で、ディズニーファン向けのコンテンツを提供している。"
    },
    {
        "index": 168,
        "filename": "image_27.png",
        "description": "音楽プレイリスト情報を発信する「himekuri_playlist」と「playlist_of」というアカウントの説明。心地よいシューエーション向けのプレイリストを提供し、フォロワー数は2.4万人と18.8万人。"
    },
    {
        "index": 169,
        "filename": "image_28.png",
        "description": "エヌケンリテラシー教育アカウント「nken.moneyliteracy」と、お金の話を発信する「okanno_chie」の紹介。社会人1年目で知るべきお金知識や資産運用情報を提供しており、フォロワー数は2.7万人と3.7万人。"
    },
    {
        "index": 170,
        "filename": "image_29.png",
        "description": "Excel初心者向けアカウント「riena.excel」と、オフィスワーカー向けアカウント「officeworker_plus」の紹介。Excelスキルや仕事術に関する情報を提供し、フォロワー数は14.5万人と3.6万人。"
    },
    {
        "index": 171,
        "filename": "image_30.png",
        "description": "大学生向け勉強アカウント「annpi_s」と「college_lab」の紹介。大学生活に関する勉強方法や情報を提供し、フォロワー数は9.5万人と1.4万人を持つ教育系アカウント。"
    },
    {
        "index": 172,
        "filename": "image_31.png",
        "description": "手刺繍初心者向けアカウント「bukiccho_hitsuji」、iPad加工術を発信する「happy_mechan」、iPhoneアプリ紹介の「marie_okawa」の3つのアカウント紹介。フォロワーは10.7万人、4177人、2.6万人。"
    },
    {
        "index": 173,
        "filename": "image_32.png",
        "description": "2023年インスタ攻略記事のセクション「バズる投稿作成方法」。全SNSで活用可能なテクニックについてのタイトルスライド。"
    },
    {
        "index": 174,
        "filename": "image_33.png",
        "description": "2023年インスタ攻略記事のセクション「コンセプト設計基礎」。圧倒的な差別化をするための基本戦略についてのタイトルスライド。"
    },
    {
        "index": 175,
        "filename": "image_34.png",
        "description": "2023年以降のインスタ運用に関する「稼ぐために必要な知識」セクション。稼げるアカウント特徴についてのタイトルスライド。"
    },
    {
        "index": 176,
        "filename": "image_35.png",
        "description": "インスタで稼げるジャンル「月100万円狙えるジャンル」について、マネタイズ戦略を共有するセクションのタイトルスライド。"
    },
    {
        "index": 177,
        "filename": "image_36.png",
        "description": "インスタ2023年伸びてるアカウント紹介の「伸びているジャンルと収益方法」セクション。アカウント10選とマネタイズ施策についてのタイトルスライド。"
    },
    {
        "index": 178,
        "filename": "image_37.png",
        "description": "インスタ不動産ジャンル攻略のセクション「伸ばし方と収益戦線」と「不動産ジャンルの稼ぎ方」について、施策と紹介手法をまとめたタイトルスライド。"
    },
    {
        "index": 179,
        "filename": "image_01.png",
        "description": "2023年ブルーオシャン16選の記事。今後伸びそうなお宝ジャンルについて、インスタで成長機会のあるテーマを紹介するメインビジュアル。"
    },
    {
        "index": 180,
        "filename": "image_02.png",
        "description": "テーマAに興味あるとテーマAの発信アカウントの違いを示す図解。インスタユーザーと発信アカウントの属性の差別化を視覚的に表現している。"
    },
    {
        "index": 181,
        "filename": "image_03.png",
        "description": "妊活ジャンルの紹介スライド。妊活についての情報提供アカウント、妊活メディア、妊活回覧板などのジャンル分類を示している。"
    },
    {
        "index": 182,
        "filename": "image_04.png",
        "description": "看護師ジャンルのインスタアカウント紹介スライド。看護師7年目の大学病院勤務から派遣までの関連アカウント複数の紹介。"
    },
    {
        "index": 183,
        "filename": "image_05.png",
        "description": "就活ジャンルのインスタアカウント紹介。就活情報をメインに発信する複数のアカウント、採用記事、採用攻略テクニック発信者の紹介。"
    },
    {
        "index": 184,
        "filename": "image_06.png",
        "description": "メンヘラ就活、採用ちゃんずなどの就活関連アカウント紹介スライド。就職支援情報と採用攻略情報を発信するアカウントの詳細情報を表示。"
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

    print(f"\n✓ Batch 165-184 完了")
    print(f"詳細説明済み: {completed}/{total} ({completed/total*100:.1f}%)")
    print(f"残り: {total-completed}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
