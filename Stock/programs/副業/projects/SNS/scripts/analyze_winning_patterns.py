#!/usr/bin/env python3
"""
勝ちパターン自動分析スクリプト
トップ/ボトム投稿の5W1H分析を自動化
"""

import sqlite3
import pandas as pd
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List


# ベースパス
BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "analytics.db"
OUTPUT_DIR = BASE_DIR / "data" / "insights"


def load_top_bottom_posts(period_days=30, top_n=10, bottom_n=10) -> Dict:
    """トップ/ボトム投稿を取得"""
    conn = sqlite3.connect(DB_PATH)

    # トップ投稿
    query_top = f"""
        SELECT
            post_id,
            platform,
            published_at,
            impressions,
            reach,
            likes,
            comments,
            shares,
            engagement_rate,
            raw_data
        FROM analytics
        WHERE DATE(published_at) >= DATE('now', '-{period_days} days')
        ORDER BY impressions DESC
        LIMIT {top_n}
    """

    df_top = pd.read_sql_query(query_top, conn)

    # ボトム投稿
    query_bottom = f"""
        SELECT
            post_id,
            platform,
            published_at,
            impressions,
            reach,
            likes,
            comments,
            shares,
            engagement_rate,
            raw_data
        FROM analytics
        WHERE DATE(published_at) >= DATE('now', '-{period_days} days')
        ORDER BY impressions ASC
        LIMIT {bottom_n}
    """

    df_bottom = pd.read_sql_query(query_bottom, conn)

    conn.close()

    return {
        "top_posts": df_top.to_dict('records'),
        "bottom_posts": df_bottom.to_dict('records')
    }


def analyze_5w1h(post: Dict) -> Dict:
    """
    5W1H分析を実施

    What: トピック分類
    When: 投稿時間帯、曜日
    Why: タイムリー性、意外性
    How: 文体、文字数
    """
    published_at = pd.to_datetime(post['published_at'])

    analysis = {
        "post_id": post['post_id'],
        "platform": post['platform'],
        "impressions": post['impressions'],
        "engagement_rate": post['engagement_rate'],

        # When分析
        "weekday": published_at.strftime("%A"),  # Monday, Tuesday...
        "weekday_num": published_at.weekday(),   # 0=月曜, 6=日曜
        "hour": published_at.hour,
        "time_slot": get_time_slot(published_at.hour),

        # What分析（トピック分類は後でLLM活用）
        "topic": "未分類",  # TODO: LLM分析

        # Why分析（勝ちパターン判定）
        "has_shocking_numbers": False,  # TODO: コンテンツ分析
        "has_authority_citation": False,  # TODO: コンテンツ分析
        "is_ceo_oriented": False,  # TODO: コンテンツ分析

        # How分析
        "character_count": 0,  # TODO: コンテンツ分析
        "has_image": False,  # TODO: コンテンツ分析
        "has_video": False,  # TODO: コンテンツ分析
    }

    return analysis


def get_time_slot(hour: int) -> str:
    """時間帯スロット取得"""
    if 0 <= hour < 6:
        return "深夜(0-6時)"
    elif 6 <= hour < 12:
        return "午前(6-12時)"
    elif 12 <= hour < 18:
        return "午後(12-18時)"
    else:
        return "夜(18-24時)"


def analyze_time_performance(posts: List[Dict]) -> pd.DataFrame:
    """時間帯・曜日別パフォーマンス分析"""
    analyses = [analyze_5w1h(post) for post in posts]
    df = pd.DataFrame(analyses)

    # 時間帯×曜日のクロス集計
    pivot_time = df.pivot_table(
        values='impressions',
        index='time_slot',
        columns='weekday',
        aggfunc='mean'
    )

    return pivot_time


def identify_winning_patterns(top_posts: List[Dict]) -> Dict:
    """勝ちパターンの特定"""
    analyses = [analyze_5w1h(post) for post in top_posts]
    df = pd.DataFrame(analyses)

    # 最頻出時間帯
    top_time_slot = df['time_slot'].mode()[0] if not df.empty else "不明"

    # 最頻出曜日
    top_weekday = df['weekday'].mode()[0] if not df.empty else "不明"

    # プラットフォーム別パフォーマンス
    platform_performance = df.groupby('platform')['impressions'].mean().to_dict()

    patterns = {
        "optimal_time_slot": top_time_slot,
        "optimal_weekday": top_weekday,
        "platform_performance": platform_performance,
        "avg_impressions": df['impressions'].mean(),
        "avg_engagement_rate": df['engagement_rate'].mean(),
    }

    return patterns


def identify_anti_patterns(bottom_posts: List[Dict]) -> Dict:
    """アンチパターンの特定"""
    analyses = [analyze_5w1h(post) for post in bottom_posts]
    df = pd.DataFrame(analyses)

    # 失敗時間帯
    worst_time_slot = df['time_slot'].mode()[0] if not df.empty else "不明"

    # 失敗曜日
    worst_weekday = df['weekday'].mode()[0] if not df.empty else "不明"

    anti_patterns = {
        "worst_time_slot": worst_time_slot,
        "worst_weekday": worst_weekday,
        "avg_impressions": df['impressions'].mean(),
        "avg_engagement_rate": df['engagement_rate'].mean(),
    }

    return anti_patterns


def generate_insights_report(
    top_posts: List[Dict],
    bottom_posts: List[Dict],
    winning_patterns: Dict,
    anti_patterns: Dict,
    output_path: Path
):
    """インサイトレポート生成（Markdown）"""
    report = f"""# SNS投稿分析レポート

**生成日時**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 📊 サマリー

### トップ10投稿の特徴
- **平均インプレッション**: {winning_patterns['avg_impressions']:,.0f}
- **平均エンゲージメント率**: {winning_patterns['avg_engagement_rate']:.2f}%
- **最適時間帯**: {winning_patterns['optimal_time_slot']}
- **最適曜日**: {winning_patterns['optimal_weekday']}

### ボトム10投稿の特徴
- **平均インプレッション**: {anti_patterns['avg_impressions']:,.0f}
- **平均エンゲージメント率**: {anti_patterns['avg_engagement_rate']:.2f}%
- **失敗時間帯**: {anti_patterns['worst_time_slot']}
- **失敗曜日**: {anti_patterns['worst_weekday']}

---

## 🏆 トップ10投稿詳細

| Rank | Platform | Impressions | ER (%) | 投稿日時 |
|------|----------|-------------|--------|----------|
"""

    for i, post in enumerate(top_posts, 1):
        dt = pd.to_datetime(post['published_at'])
        report += f"| {i} | {post['platform']} | {post['impressions']:,} | {post['engagement_rate']:.2f} | {dt.strftime('%Y-%m-%d %H:%M')} |\n"

    report += """
---

## ⚠️ ボトム10投稿詳細

| Rank | Platform | Impressions | ER (%) | 投稿日時 |
|------|----------|-------------|--------|----------|
"""

    for i, post in enumerate(bottom_posts, 1):
        dt = pd.to_datetime(post['published_at'])
        report += f"| {i} | {post['platform']} | {post['impressions']:,} | {post['engagement_rate']:.2f} | {dt.strftime('%Y-%m-%d %H:%M')} |\n"

    report += """
---

## 🎯 推奨アクション

### 勝ちパターン活用
1. **最適投稿時間帯**: {optimal_time_slot}に投稿
2. **最適曜日**: {optimal_weekday}を優先
3. **プラットフォーム最適化**: {best_platform}を強化

### アンチパターン回避
1. **避けるべき時間帯**: {worst_time_slot}
2. **避けるべき曜日**: {worst_weekday}

---

**次回更新**: 1週間後
""".format(
        optimal_time_slot=winning_patterns['optimal_time_slot'],
        optimal_weekday=winning_patterns['optimal_weekday'],
        best_platform=max(winning_patterns['platform_performance'], key=winning_patterns['platform_performance'].get),
        worst_time_slot=anti_patterns['worst_time_slot'],
        worst_weekday=anti_patterns['worst_weekday']
    )

    # ファイル出力
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✅ インサイトレポート生成完了: {output_path}")


def main():
    """メイン処理"""
    print("\n" + "=" * 80)
    print("🔍 勝ちパターン自動分析開始")
    print("=" * 80)
    print(f"実行時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # 出力ディレクトリ作成
    OUTPUT_DIR.mkdir(exist_ok=True)

    # データ取得
    print("📊 トップ/ボトム投稿を取得中...")
    data = load_top_bottom_posts(period_days=30, top_n=10, bottom_n=10)

    top_posts = data['top_posts']
    bottom_posts = data['bottom_posts']

    print(f"   トップ投稿: {len(top_posts)}件")
    print(f"   ボトム投稿: {len(bottom_posts)}件\n")

    if not top_posts:
        print("⚠️ データが不足しています。`daily_analytics_collection.py`を実行してください。")
        return

    # 勝ちパターン分析
    print("🏆 勝ちパターンを分析中...")
    winning_patterns = identify_winning_patterns(top_posts)
    print(f"   最適時間帯: {winning_patterns['optimal_time_slot']}")
    print(f"   最適曜日: {winning_patterns['optimal_weekday']}\n")

    # アンチパターン分析
    print("⚠️  アンチパターンを分析中...")
    anti_patterns = identify_anti_patterns(bottom_posts)
    print(f"   失敗時間帯: {anti_patterns['worst_time_slot']}")
    print(f"   失敗曜日: {anti_patterns['worst_weekday']}\n")

    # 時間帯パフォーマンス分析
    print("📈 時間帯パフォーマンスを分析中...")
    time_performance = analyze_time_performance(top_posts + bottom_posts)
    print(time_performance)
    print()

    # レポート生成
    print("📝 インサイトレポートを生成中...")
    report_path = OUTPUT_DIR / f"insights_report_{datetime.now().strftime('%Y%m%d')}.md"
    generate_insights_report(top_posts, bottom_posts, winning_patterns, anti_patterns, report_path)

    # JSON出力
    json_path = OUTPUT_DIR / f"insights_data_{datetime.now().strftime('%Y%m%d')}.json"
    insights_data = {
        "generated_at": datetime.now().isoformat(),
        "winning_patterns": winning_patterns,
        "anti_patterns": anti_patterns,
        "top_posts": [
            {k: v for k, v in post.items() if k != 'raw_data'}
            for post in top_posts
        ],
        "bottom_posts": [
            {k: v for k, v in post.items() if k != 'raw_data'}
            for post in bottom_posts
        ]
    }

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(insights_data, f, indent=2, ensure_ascii=False)

    print(f"✅ JSONデータ保存完了: {json_path}")

    print("\n" + "=" * 80)
    print("✅ 勝ちパターン分析完了")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
