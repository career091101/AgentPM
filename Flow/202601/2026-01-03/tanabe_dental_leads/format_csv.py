#!/usr/bin/env python3
"""
CSVフォーマット修正スクリプト

変更内容:
1. 住所から「日本、」と「〒郵便番号 」を削除
2. カラム順序を変更（郵便番号、住所を前に）
"""

import csv
import re
from pathlib import Path


def clean_address(address, postal_code):
    """
    住所から「日本、」と「〒郵便番号 」を削除

    Args:
        address: 元の住所文字列
        postal_code: 郵便番号

    Returns:
        クリーンな住所文字列
    """
    # 「日本、」を削除
    cleaned = address.replace('日本、', '')

    # 「〒郵便番号 」を削除
    if postal_code:
        cleaned = cleaned.replace(f'〒{postal_code} ', '')
        cleaned = cleaned.replace(f'〒{postal_code}', '')

    return cleaned.strip()


def reorder_columns(input_csv, output_csv):
    """
    CSVのカラム順序を変更

    変更後の順序:
    スコア, 医院名, 医院長名, 郵便番号, 住所, その他...
    """

    # CSV読み込み
    with open(input_csv, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("❌ CSVファイルが空です")
        return

    # 住所をクリーン化
    for row in rows:
        row['住所'] = clean_address(row['住所'], row.get('郵便番号', ''))

    # 新しいカラム順序
    new_fieldnames = [
        'スコア',
        '医院名',
        '医院長名',
        '郵便番号',
        '住所',
        '基礎評価',
        '来院患者数',
        '子ども対応力',
        'Web積極性',
        '医院規模',
        'ブログ活動',
        '営業時間',
        'ブログ更新日',
        '電話番号',
        'WebサイトURL',
        '評価',
        'レビュー件数',
        '診療科目タグ',
        '写真枚数',
        'SNS連携',
        '子ども対応力スコア',
        'Google Maps URL'
    ]

    # 新しいCSV書き込み
    with open(output_csv, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=new_fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✓ フォーマット完了: {output_csv}")
    print(f"  処理件数: {len(rows)}件")

    # サンプル表示（最初の2行）
    print("\n--- サンプル（最初の2行）---")
    for i, row in enumerate(rows[:2], 1):
        print(f"\n{i}. {row['医院名']}")
        print(f"   郵便番号: {row['郵便番号']}")
        print(f"   住所: {row['住所']}")


def main():
    # 最新のサブエージェント版CSVを処理
    input_csv = Path('test_dental_leads_complete_subagent_20260103_230000.csv')
    output_csv = Path('test_dental_leads_formatted_20260103_230000.csv')

    if not input_csv.exists():
        print(f"❌ 入力ファイルが見つかりません: {input_csv}")
        return

    reorder_columns(input_csv, output_csv)


if __name__ == '__main__':
    main()
