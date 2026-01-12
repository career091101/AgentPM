#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 2105, "filename": "image_11.png", "description": "「2023年Twitter攻略/フォロワー伸ばし方」と「1万人フォロワー目指そう」というテキストが配置された青と白のバナースライド。ロケットアイコンと営業スーツの男性キャラクターを含む。"},
    {"index": 2106, "filename": "image_12.png", "description": "「Twitterの0→1攻略/フォロワーUP成功事例」と「アカ初期の最強施策」というテキストを強調した青いバナー。成長を示す赤い矢印アイコンと営業男性イラスト。"},
    {"index": 2107, "filename": "image_13.png", "description": "「Twitterの恋愛ジャンル/変わった稼げるアフィ案件」というタイトルが赤地に表示されたスライド。生姜焼きキャラクターアイコンと「おすすめASP案件」「おすすめアフィ案件まとめ」の箇条書き。"},
    {"index": 2108, "filename": "image_14.png", "description": "「商品が売れる投稿！！/超売れるツイートの型10選」というタイトルが青いバナーに表示されたスライド。note/アフィ/コンサルが売れる商品例を示すテキスト付き。"},
    {"index": 2109, "filename": "image_01.png", "description": "「2023年インスタ伸ばし方/フォロワーを伸ばす施策」というテキストが紫地に配置されたメインビジュアル。ロケットアイコン、Instagramロゴ、「目指せフォロワー1万人」テキスト、営業男性キャラクター。"},
    {"index": 2110, "filename": "image_02.jpg", "description": "黒髪で短髪、紺色スーツに赤いネクタイを着用したビジネスマンのシンプルなイラスト。プロフェッショナルな人物アイコン。"},
    {"index": 2111, "filename": "image_03.jpg", "description": "黒髪で短髪、紺色スーツに赤いネクタイを着用したビジネスマンのシンプルなイラスト。プロフェッショナルな人物アイコン。"},
    {"index": 2112, "filename": "image_04.png", "description": "ユーザーのInstagram行動履歴から最適なコンテンツ表示メカニズムを説明するスライド。美容系の投稿好きなユーザーと、発見欄に表示されるコスメ関連コンテンツの流れを図解。"},
    {"index": 2113, "filename": "image_05.png", "description": "グルメ好きな太郎さんのInstagram発見欄流入メカニズムを5ステップで示した図解。ハート、グルメアカウント検索から発見欄への掲載までのプロセス。"},
    {"index": 2114, "filename": "image_06.png", "description": "Instagramの発見タブ検索機能を説明するスライド。行動履歴に基づいて最適なコンテンツを表示する仕組みと、ユーザーごとに異なるコンテンツが表示される点を強調。"},
    {"index": 2115, "filename": "image_07.png", "description": "Instagramの発見タブ検索から特定ユーザーの発見タブ上位表示までのプロセスを解説する図表。グルメ関連投稿がグルメ系アカウント500個と比較される過程を示すスライド。"},
    {"index": 2116, "filename": "image_08.png", "description": "Instagramアカウント流入数を示すピラミッド図。発見タブ上位25アカウント、発見タブ500アカウント、数千以上のグルメアカウントの階層構造。"},
    {"index": 2117, "filename": "image_09.png", "description": "Instagramフィード上でのバズ投稿の種類と拡散メカニズムを示すチャート。「コンテンツ投稿」「フォロワーのストーリーズ表示」「フォロー数反応と類似投稿の推薦」など6つのステップを数字付きで表示。"},
    {"index": 2118, "filename": "image_10.png", "description": "Instagramのストーリーズ位置とタイムラインの重要性を説明するスライド。スマートフォン画面にストーリーズ1番左側とタイムラインのトップ表示位置を数字で強調。"},
    {"index": 2119, "filename": "image_11.png", "description": "Instagramアルゴリズムにおいて重要とされるエンゲージメント指標を3つ列挙したスライド。保存数（高重要度）、コメント数（中重要度）、いいね/シェア（低重要度）をピラミッド型で表示。"},
    {"index": 2120, "filename": "image_12.png", "description": "Instagram フォロワー増加の一般的な成長トレンドを示すグラフ。2月から7月にかけてフォロワー数が0から20,000に伸びる曲線グラフ。"},
    {"index": 2121, "filename": "image_13.png", "description": "Instagramアカウント流入の仕組みを3ステップで示す図解。発見タブ/ハッシュタグ→インスタアカウント→ストーリーズライブ/DM返し→フォロー/フォロワーの質が高い既存ユーザーへの転換。"},
    {"index": 2122, "filename": "image_14.png", "description": "Instagram フォロワー増加の成長グラフに(C)(D)と(A)(B)のラベルが付された段階別表示。2月から7月にかけてフォロワー数が段階的に伸びるパターンを示すグラフ。"},
    {"index": 2123, "filename": "image_15.png", "description": "Instagramフォロワーの理想的なトップ画面構成を解説するスライド。ストーリーズ1番左側とタイムライントップという2つの重要な表示位置を図解で説明。"},
    {"index": 2124, "filename": "image_16.png", "description": "Instagram フォロワー増加の成長グラフに(C)(D)と(A)(B)のラベルが付された段階別表示。期間軸は2月1日から7月1日、フォロワー数は0から20,000までのスケール。"},
]

def is_auto_generated(desc):
    patterns = [
        "インスタグラム運用に関する",
        "説明画像または投稿サムネイル",
        "運用に関する説明画像",
        "投稿用のサムネイル",
        "記事のバナー画像またはメインビジュアル",
        "関連コンテンツ",
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

    print(f"\n✓ Batch 2105-2124 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
