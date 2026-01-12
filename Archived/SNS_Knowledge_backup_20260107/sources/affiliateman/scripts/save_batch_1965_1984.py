#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 1965, "filename": "image_06.png", "description": "Twitterアカウント「ゆいの恋愛テクニック」の恋愛・性の悩み相談と実践的な恋愛テクニック伝授サービスの紹介スクリーンショット。"},
    {"index": 1966, "filename": "image_07.png", "description": "「2023年Twitter攻略 フォロワー伸ばし方」のバナー画像。青と赤のテンプレートデザインで1万人フォロワー目指そうというメッセージ。"},
    {"index": 1967, "filename": "image_08.png", "description": "「フォロワー増加の10施策」と「外部誘導でフォロワー爆伸び」と「インスタTwitter フォロワー伸びた成功事例紹介」の3つの見出しを含む説明画像。"},
    {"index": 1968, "filename": "image_09.png", "description": "「超絶バズる!!!」「初心者でもバズる」「Twitterのバズ構文 バズる型100選」と大きく表記された、初心者向けTwitterバズテクニック集のメインバナー。"},
    {"index": 1969, "filename": "image_10.png", "description": "Twitterの恋愛ジャンル関連で稼げるアフィリエイト案件として、おすすめASP案件とおすすめアフィ案件をまとめた図解。"},
    {"index": 1970, "filename": "image_11.png", "description": "Twitterマネタイズ施策で「1投稿で20万円売上達成」の実例と売上UPのマネタイズ動線や売上UP投稿とマネタイズ誘導施策の説明。"},
    {"index": 1971, "filename": "image_12.png", "description": "SNSのマネタイズ事例として「DMで商品を売る施策例」の俺の成功事例紹介を示すイラスト付きの説明画像。"},
    {"index": 1972, "filename": "image_01.png", "description": "「超絶バズる!!!」「初心者でもバズる」というテキストとTwitterロゴ、上昇矢印、キャラクターイラストを組み合わせた、Twitterバズ構文100選のメインタイトル画像。"},
    {"index": 1973, "filename": "image_02.jpg", "description": "紺色のスーツを着た短髪の女性キャラクターのシンプルなミニマル風イラスト。"},
    {"index": 1974, "filename": "image_03.png", "description": "K君🔥永久凍結したツイートのTwitterアナリティクス画面。過去28日間のツイートインプレッション、プロフィールアクセス、@ツイート、フォロワー数の変動グラフを表示。"},
    {"index": 1975, "filename": "image_04.png", "description": "K君🔥永久凍結した別のツイートのTwitterアナリティクス画面。127ツイート、2,963,734インプレッション、47,457プロフィールアクセスなどの28日間の変動データを表示。"},
    {"index": 1976, "filename": "image_05.png", "description": "「直アフィできる最強の案件」として、SpotifyやWeWork、キャンパなど複数のASP案件を一覧にした図解。頭・中身・最後に分類されたASP案件の特徴を説明。"},
    {"index": 1977, "filename": "image_06.jpg", "description": "紺色のスーツと赤ネクタイを着た短髪の男性キャラクターのシンプルなミニマル風ビジネス人物イラスト。"},
    {"index": 1978, "filename": "image_07.png", "description": "Twitter恋愛ジャンルで稼ぐための「変わった稼げるアフィ案件」として、おすすめASP案件とおすすめアフィ案件をまとめた説明画像。"},
    {"index": 1979, "filename": "image_08.jpg", "description": "紺色のスーツと赤ネクタイを着た短髪の男性キャラクターのシンプルなミニマル風ビジネス人物イラスト。"},
    {"index": 1980, "filename": "image_09.png", "description": "「インパクトがある入り」というテーマで、恋愛ジャンルで成果を出すための2つのバズ構文例を赤と薄い青の枠で表示した説明スライド。"},
    {"index": 1981, "filename": "image_10.png", "description": "TwitterユーザーK君🔥永久凍結した簡潔なメッセージツイートのスクリーンショット。ダイエットジャンルで取れる案件や美容整形のアフィリエイト案件を説明。"},
    {"index": 1982, "filename": "image_11.jpg", "description": "紺色のスーツと赤ネクタイを着た短髪の男性キャラクターのシンプルなミニマル風ビジネス人物イラスト。"},
    {"index": 1983, "filename": "image_12.png", "description": "Twitter運用で月150万先月稼いだアカウントのインスタ夫婦改善アカウント実績と、フォロワー数よりマネタイズ方法が重要という内容のツイートスクリーンショット。"},
    {"index": 1984, "filename": "image_13.png", "description": "アクセル先生@axcel0901のツイート。節約重視でお金を増やすための「簡単」「仲間」など実践的な5つの条件を記載した金銭管理テクニックの説明。"},
]

def is_auto_generated(desc):
    patterns = [
        "インスタグラム運用に関する",
        "説明画像または投稿サムネイル",
        "運用に関する説明画像",
        "投稿用のサムネイル",
    ]
    return any(p in desc for p in patterns)

def update_inventory_with_descriptions(batch_descriptions):
    progress_file = OUTPUT_DIR / 'image_inventory_progress.json'

    with open(progress_file, 'r', encoding='utf-8') as f:
        inventory = json.load(f)

    for desc in batch_descriptions:
        idx = desc['index']
        if idx < len(inventory):
            inventory[idx]['description'] = desc['description']
            print(f"[{idx}] {desc['filename']}: 説明更新")

    completed = sum(1 for item in inventory if not is_auto_generated(item.get('description', '')))
    total = len(inventory)
    remaining = total - completed
    percentage = (completed / total) * 100

    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Batch 1965-1984 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
