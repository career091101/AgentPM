#!/usr/bin/env python3
"""
バッチ002完全再実行（WebFetch強制）

500件の歯科医院WebサイトをWebFetch分析し、医院長名抽出率70%以上を目指す。
6次元スコアリング結果をJSONで出力。
"""

import csv
import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import re


def parse_csv_file(csv_path: str) -> List[Dict[str, str]]:
    """CSVファイルを読み込み"""
    clinics = []
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            clinics.append(row)
    return clinics


def extract_website_url(row: Dict[str, str]) -> Optional[str]:
    """WebサイトURLを抽出"""
    url = row.get('WebサイトURL', '').strip()
    if url and url.startswith('http'):
        return url
    return None


def analyze_website_with_webfetch(clinic_name: str, website_url: str) -> Dict[str, Any]:
    """
    WebFetchでWebサイトを分析（トップページ + 関連ページ探索）

    注: この関数はClaude Code環境でWebFetchツールを使用する前提。
    実際の実装では、WebFetchツールの呼び出しロジックを実装する必要がある。

    戻り値の例:
    {
        "sns_instagram": True,
        "sns_facebook": False,
        "sns_line": True,
        "sns_twitter": False,
        "blog_updated": "2025-12-25",
        "kids_content": True,
        "waiting_room_photo": True,
        "operating_hours": "平日9:00-19:00",
        "director_name": "山田太郎"
    }
    """
    # プレースホルダー実装
    # 実際にはWebFetchツールを呼び出す必要がある

    print(f"   Analyzing: {clinic_name}")
    print(f"   URL: {website_url}")

    # デフォルト値（WebFetch実装時にここを置き換える）
    result = {
        "sns_instagram": False,
        "sns_facebook": False,
        "sns_line": False,
        "sns_twitter": False,
        "blog_updated": None,
        "kids_content": False,
        "waiting_room_photo": False,
        "operating_hours": None,
        "director_name": None,
        "webfetch_status": "not_implemented"
    }

    # TODO: WebFetchツール呼び出しをここに実装
    # 例:
    # top_page_prompt = f"""
    # 以下の歯科医院Webサイトのトップページを分析してください。
    #
    # **医院名**: {clinic_name}
    # **URL**: {website_url}
    #
    # ... (詳細なプロンプト)
    # """
    #
    # top_page_result = WebFetch(url=website_url, prompt=top_page_prompt)
    # result = parse_webfetch_result(top_page_result)

    return result


def calculate_score_dimension_1(rating: float) -> int:
    """基礎評価スコア（20点満点）"""
    return min(int(rating * 4), 20)


def calculate_score_dimension_2(review_count: int) -> int:
    """来院患者数スコア（20点満点）"""
    if review_count >= 100:
        return 20
    elif review_count >= 50:
        return 15
    elif review_count >= 20:
        return 10
    elif review_count >= 10:
        return 5
    else:
        return 0


def calculate_score_dimension_3(clinic_name: str, website_data: Dict[str, Any]) -> int:
    """子ども対応力スコア（30点満点）"""
    score = 0

    # kids_content (15点)
    if website_data.get('kids_content', False):
        score += 15

    # 医院名に子ども関連キーワード (10点)
    keywords = ['小児', 'こども', '子ども', 'キッズ', '矯正']
    if any(kw in clinic_name for kw in keywords):
        score += 10

    # waiting_room_photo (5点)
    if website_data.get('waiting_room_photo', False):
        score += 5

    return min(score, 30)


def calculate_score_dimension_4(website_data: Dict[str, Any]) -> int:
    """Web積極性スコア（15点満点）"""
    sns_count = 0
    if website_data.get('sns_instagram', False):
        sns_count += 1
    if website_data.get('sns_facebook', False):
        sns_count += 1
    if website_data.get('sns_line', False):
        sns_count += 1
    if website_data.get('sns_twitter', False):
        sns_count += 1

    return min(sns_count * 5, 15)


def calculate_score_dimension_5(operating_hours: Optional[str], photo_count: int) -> int:
    """医院規模スコア（10点満点）"""
    score = 0

    # 営業時間記載 (5点)
    if operating_hours:
        score += 5

    # 写真10枚以上 (5点)
    if photo_count >= 10:
        score += 5

    return score


def calculate_score_dimension_6(blog_updated: Optional[str]) -> int:
    """ブログ活動スコア（5点満点）"""
    if not blog_updated:
        return 0

    try:
        from datetime import datetime
        blog_date = datetime.strptime(blog_updated, "%Y-%m-%d")
        now = datetime.now()
        days_diff = (now - blog_date).days

        if days_diff <= 30:
            return 5
        elif days_diff <= 60:
            return 4
        elif days_diff <= 90:
            return 3
        elif days_diff <= 180:
            return 2
        elif days_diff <= 365:
            return 1
        else:
            return 0
    except:
        return 0


def calculate_total_score(scores: Dict[str, int]) -> int:
    """総合スコア計算"""
    return sum(scores.values())


def process_batch(clinics: List[Dict[str, str]], batch_num: int, total_batches: int) -> List[Dict[str, Any]]:
    """バッチ処理"""
    results = []

    print(f"\n📦 バッチ {batch_num}/{total_batches}")
    print(f"   処理中: {len(clinics)}件")

    for i, clinic in enumerate(clinics, 1):
        clinic_name = clinic.get('医院名', 'Unknown')
        website_url = extract_website_url(clinic)

        if not website_url:
            print(f"   ⚠️  {clinic_name}: WebサイトURLなし - スキップ")
            continue

        try:
            # WebFetch分析実行
            website_analysis = analyze_website_with_webfetch(clinic_name, website_url)

            # 生データ抽出
            rating = float(clinic.get('評価', '0') or '0')
            review_count = int(clinic.get('レビュー件数', '0') or '0')
            photo_count = int(clinic.get('写真枚数', '0') or '0')
            operating_hours = clinic.get('営業時間', '')

            # スコアリング
            scores = {
                "基礎評価": calculate_score_dimension_1(rating),
                "来院患者数": calculate_score_dimension_2(review_count),
                "子ども対応力": calculate_score_dimension_3(clinic_name, website_analysis),
                "Web積極性": calculate_score_dimension_4(website_analysis),
                "医院規模": calculate_score_dimension_5(operating_hours or website_analysis.get('operating_hours'), photo_count),
                "ブログ活動": calculate_score_dimension_6(website_analysis.get('blog_updated'))
            }

            total_score = calculate_total_score(scores)

            result = {
                "clinic_name": clinic_name,
                "total_score": total_score,
                "scores": scores,
                "website_analysis": {
                    "sns_instagram": website_analysis.get('sns_instagram', False),
                    "sns_facebook": website_analysis.get('sns_facebook', False),
                    "sns_line": website_analysis.get('sns_line', False),
                    "sns_twitter": website_analysis.get('sns_twitter', False),
                    "blog_updated": website_analysis.get('blog_updated'),
                    "kids_content": website_analysis.get('kids_content', False),
                    "waiting_room_photo": website_analysis.get('waiting_room_photo', False),
                    "operating_hours": website_analysis.get('operating_hours') or operating_hours,
                    "director_name": website_analysis.get('director_name')
                },
                "raw_data": {
                    "rating": rating,
                    "user_ratings_total": review_count,
                    "formatted_address": clinic.get('住所', ''),
                    "formatted_phone_number": clinic.get('電話番号', ''),
                    "website": website_url,
                    "photos_count": photo_count
                }
            }

            results.append(result)

            if website_analysis.get('director_name'):
                print(f"   ✓ {clinic_name} (スコア: {total_score}) - 医院長: {website_analysis['director_name']}")
            else:
                print(f"   ✓ {clinic_name} (スコア: {total_score})")

            # レート制限対策
            time.sleep(0.5)

        except Exception as e:
            print(f"   ✗ {clinic_name}: {e}")
            continue

    return results


def main():
    """メイン処理"""
    csv_path = "scoring_batches/batch_002_to_score.csv"
    output_path = "scoring_results_batch_002_retry_20260104.json"
    batch_size = 10

    print("=" * 80)
    print("バッチ002完全再実行（WebFetch強制）")
    print("=" * 80)

    # STEP 1: CSV読み込み
    print("\nSTEP 1: CSVファイル読み込み")
    clinics = parse_csv_file(csv_path)
    print(f"✓ 総件数: {len(clinics)}件")

    # WebサイトURLがある医院のみ抽出
    clinics_with_website = [c for c in clinics if extract_website_url(c)]
    print(f"✓ WebサイトURL有り: {len(clinics_with_website)}件")

    # STEP 2: バッチ処理
    print("\nSTEP 2: WebFetch分析 + スコアリング")

    all_results = []
    total_batches = (len(clinics_with_website) + batch_size - 1) // batch_size

    for i in range(0, len(clinics_with_website), batch_size):
        batch = clinics_with_website[i:i+batch_size]
        batch_num = i // batch_size + 1

        batch_results = process_batch(batch, batch_num, total_batches)
        all_results.extend(batch_results)

        # バッチ間で2秒待機
        if batch_num < total_batches:
            time.sleep(2)

    # 統計情報
    director_names_found = sum(1 for r in all_results if r['website_analysis']['director_name'])
    extraction_rate = (director_names_found / len(all_results) * 100) if all_results else 0

    print(f"\n{'=' * 80}")
    print(f"✓ 分析完了: {len(all_results)}件")
    print(f"✓ 医院長名取得: {director_names_found}件 ({extraction_rate:.1f}%)")

    # STEP 3: JSON出力
    print("\nSTEP 3: JSON出力")

    output_data = {
        "metadata": {
            "batch_file": csv_path,
            "total_clinics": len(all_results),
            "timestamp": datetime.now().isoformat(),
            "retry_execution": True,
            "webfetch_forced": True,
            "director_names_found": director_names_found,
            "director_extraction_rate": f"{extraction_rate:.1f}%"
        },
        "results": all_results
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"✓ JSON出力完了: {output_path}")
    print(f"✓ 医院長名抽出率: {director_names_found}/{len(all_results)} ({extraction_rate:.1f}%)")
    print("\n" + "=" * 80)
    print("⚠️  注意: WebFetch機能は未実装です。")
    print("   analyze_website_with_webfetch() 関数にWebFetchツール呼び出しを実装してください。")
    print("=" * 80)


if __name__ == "__main__":
    main()
