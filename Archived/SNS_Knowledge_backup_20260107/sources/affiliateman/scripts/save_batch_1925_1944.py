#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 1925, "filename": "image_91.png", "description": "Instagramのコメント欄に投稿された質問と回答のスクリーンショット。ユーザーひろ氏によるキャリアアップコンサルについての相談と、Kくんによる転職エージェント活用のアドバイスが記載されている。"},
    {"index": 1926, "filename": "image_92.png", "description": "Instagramの質問回答スクリーンショット。フォロワー5000人達成に関する褒辞と、キャリアップコンサルについての個別相談が表示されている。"},
    {"index": 1927, "filename": "image_93.png", "description": "Instagramの質問回答スクリーンショット。トヨ氏によるTwitterのリリース方法とLINE200人に対する販売戦略についての具体的なアドバイスが記載されている。"},
    {"index": 1928, "filename": "image_94.png", "description": "Instagramの質問回答スクリーンショット。Kくんによる長文ツイート作成やノウハウ系ツイートのリリース方法についての回答が表示されている。"},
    {"index": 1929, "filename": "image_95.png", "description": "Instagramの質問回答スクリーンショット。せいぬ氏によるUnivaPay×Appsについての質問と、Kくんによるテンプレート利用やアプリ導入についての詳細な回答が記載されている。"},
    {"index": 1930, "filename": "image_96.png", "description": "Instagramの質問回答スクリーンショット。Kくんによるappsの導入とチェックボックス機能、アフィリンク発行についてのアドバイスが表示されている。"},
    {"index": 1931, "filename": "image_97.png", "description": "Instagramの質問回答スクリーンショット。LPでの審査出しと決済リンク作成、セミナー売上やLP作成の最適な方法についての質疑応答が記載されている。"},
    {"index": 1932, "filename": "image_98.png", "description": "Instagramの質問回答スクリーンショット。LPとセミナーの決済リンク関連、Univapay×USTAGEの利用率についてのKくんとせいぬ氏の問答が表示されている。"},
    {"index": 1933, "filename": "image_99.png", "description": "Instagramの質問回答スクリーンショット。なおみ氏によるダイエット企画とコンセプト設計、フォロワー100万人を目指すビジネス戦略についての詳細な相談が記載されている。"},
    {"index": 1934, "filename": "image_100.png", "description": "Instagramの質問回答スクリーンショット。なおみ氏によるマーク博士の動画評価とリスト販売戦略、アカウント運用方針についてのKくんの回答が表示されている。"},
    {"index": 1935, "filename": "image_101.png", "description": "Instagramの質問回答スクリーンショット。sana u氏による占い系ジャンルでの実績と失恋テーマを中心とした運用戦略、ダイエットコンサル展開についての詳細が記載されている。"},
    {"index": 1936, "filename": "image_102.png", "description": "Instagramの質問回答スクリーンショット。Kくんによるダイエットコンサル運用と恋愛ジャンル、TikTokの再生回数最適化についてのアドバイスが表示されている。"},
    {"index": 1937, "filename": "image_104.png", "description": "紫色背景のバナー画像。「SNS運用 超役立つ情報」と「SNS運用知識まとめ【2022年10月分】」のテキストと、笑顔のキャラクターイラストが配置されている。"},
    {"index": 1938, "filename": "image_106.png", "description": "緑色背景のバナー画像。「SNS攻略サロンの醍醐味」「Slack過去の有益情報まとめ」というテキストと、Slackロゴ、援助ポーズのキャラクターが描かれている。"},
    {"index": 1939, "filename": "image_107.png", "description": "インスタグラムのバナー画像。「2023年最新インスタグラム 伸びてるアカ1200選」と「伸びてるアカ厳選」「収益動線も解説」「稼げるジャンル理解」という3つの特徴が記載されている。"},
    {"index": 1940, "filename": "image_01.png", "description": "青色背景のTwitter関連バナー画像。「2023年 Twitter攻略 フォロワー伸ばし方」というタイトルと「1万人フォロワー目指そう」のテキスト、ロケットのイラストが配置されている。"},
    {"index": 1941, "filename": "image_02.jpg", "description": "Twitter検索画面とアカウントプロフィール画面の図解。おすすめのInstagramアカウント検索方法を示すスクリーンショットで、アカウント欄の検索フローが赤枠で強調されている。"},
    {"index": 1942, "filename": "image_03.jpg", "description": "Twitterのインスタグラム攻略ツール紹介スクリーンショット。「Kくん | SNSの攻略」アカウントの概要と、フォロワー獲得の具体的な施策（SNS運用1ヶ月目：100フォロワー、4ヶ月目：YouTube4 TikTok3 Twitter1）が記載されている。"},
    {"index": 1943, "filename": "image_04.jpg", "description": "Twitterのアカウント情報を示すスプレッドシート。アカウント名、URL、フォロワー数、投稿内容に関する列が表示され、エヌケン（2.1万人）、たくと（8900人）、ひろり（2000人）などのアカウント情報が一覧化されている。"},
    {"index": 1944, "filename": "image_05.png", "description": "Twitterアカウントのデータ一覧表。アカウント名、URL、フォロワー数列と、各アカウントが投稿しているツイート種類（ツイート①②③④⑤）が記載された追跡管理用のスプレッドシート。"},
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

    print(f"\n✓ Batch 1925-1944 完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
