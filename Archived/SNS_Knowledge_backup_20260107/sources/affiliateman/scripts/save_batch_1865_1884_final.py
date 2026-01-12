#!/usr/bin/env python3
import json
from pathlib import Path

OUTPUT_DIR = Path("/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNSノウハウ/affiliateman")

batch_descriptions = [
    {"index": 1865, "filename": "image_31.png", "description": "SNSコンサルのまさくん氏への質問スレッド。アカウント初期段階での技術投稿と恋愛ジャンルの戦略に関する3つの質問が記載されている。"},
    {"index": 1866, "filename": "image_32.png", "description": "まさくん氏の回答。50～100超えるアカの拡散における戦略と、恋愛系1万人到成後のマネタイズ方法について具体的なアドバイスが記載。"},
    {"index": 1867, "filename": "image_33.png", "description": "いと氏からのフォロー企画に関する質問スレッド。フォロワー獲得のための具体的な施策5項目がリスト化されている。"},
    {"index": 1868, "filename": "image_34.png", "description": "K氏からのCANVA図解作成に関する質問スレッド。インスタ使用とSNS使用のCANVA活用方法について複数の回答が表示。"},
    {"index": 1869, "filename": "image_35.png", "description": "しろみ氏からのビジネス相談スレッド。イラスト販売とコンテンツ販売を軸とした営業戦略とSNS運用に関する複数の質問と回答。"},
    {"index": 1870, "filename": "image_36.png", "description": "SNS運用戦略に関する複数の相談スレッド。フォロワー増加のための具体的なアカウント運用方法と投稿戦略についての質疑応答。"},
    {"index": 1871, "filename": "image_37.png", "description": "しろみ氏からのインフルエンサーマーケティングに関する質問。アイコン作成とインフルエンサー選定の関係性に関する複数の質問と回答が表示。"},
    {"index": 1872, "filename": "image_38.png", "description": "SNSアカウント運用に関する複数の質問スレッド。イラストレーターのアカウント運用戦略と影響力のあるアカウント作成方法についての回答。"},
    {"index": 1873, "filename": "image_39.png", "description": "トラキチ氏からのアカウント戦略相談スレッド。SNS×ブログ系の運用方針とフォロワー増加戦略について具体的なアドバイスが記載。"},
    {"index": 1874, "filename": "image_40.png", "description": "トラキチ氏の詳細な回答。フォロワー初期段階の運用戦略と、ジャンル選定における影響力の関係性についての長文説明。"},
    {"index": 1875, "filename": "image_41.png", "description": "つっちー氏からのTwitter運用相談スレッド。1ヶ月で1000.1500フォロワーを達成した事例をもとに、ジャンル選定と戦略についての質問。"},
    {"index": 1876, "filename": "image_42.png", "description": "つっちー氏の質問に対する複数ユーザーからのアドバイス。エロ系アカウント運用の失敗例と成功戦略についての実体験をもとにした回答。"},
    {"index": 1877, "filename": "image_43.png", "description": "ホトリ氏からのアカウントジャンル選定に関する質問。アカウント初期段階での最適なジャンル選択と、フォロワー0状態での戦略についての相談。"},
    {"index": 1878, "filename": "image_44.png", "description": "ホトリ氏への複数ユーザーからの回答スレッド。アカウント運用の基本的な戦略とマネタイズまでの動線に関する実践的なアドバイス群。"},
    {"index": 1879, "filename": "image_45.png", "description": "ko-ta氏からの詳細な事例紹介スレッド。ビジネス系アカウント立ち上げのアドバイスと、過去の起業サービス失敗例についての長文説明。"},
    {"index": 1880, "filename": "image_46.png", "description": "ゆきと氏からのXアカウント運用相談スレッド。マッチングアプリ系ジャンルのターゲット設定とアカウント構築戦略についての質問と回答。"},
    {"index": 1881, "filename": "image_47.png", "description": "複数ユーザーからのビジネス系アカウント運用に関する相談スレッド。サロンコンテンツやコンサルティングのマネタイズ戦略についての質疑応答群。"},
    {"index": 1882, "filename": "image_48.png", "description": "ゆきと氏からのマッチングアプリ系アカウント運用に関する長文相談。スクール検討と予算配分、フォロワー数拡大戦略についての複数の質問。"},
    {"index": 1883, "filename": "image_49.png", "description": "ゆきと氏への回答スレッド。マッチングアプリジャンルの基本的な攻略方法とジャンル選定の影響力についての実践的なアドバイス。"},
    {"index": 1884, "filename": "image_50.png", "description": "K氏からのアカウント運用に関する最終的な回答スレッド。マネタイズ戦略と女性ターゲットの確保に関する複数の認識確認と最後のアドバイス。"},
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

    print(f"\n✓ Batch 1865-1884 再処理完了")
    print(f"詳細説明済み: {completed}/{total} ({percentage:.1f}%)")
    print(f"残り: {remaining}枚")

if __name__ == "__main__":
    update_inventory_with_descriptions(batch_descriptions)
