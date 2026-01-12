#!/usr/bin/env python3
"""
最適投稿時間予測スクリプト
過去90日のデータから時間帯・曜日別パフォーマンスを分析
"""

import sqlite3
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict


# ベースパス
BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "analytics.db"
OUTPUT_DIR = BASE_DIR / "data" / "predictions"


def load_historical_data(platform: str = None, days: int = 90) -> pd.DataFrame:
    """過去データを読み込み"""
    conn = sqlite3.connect(DB_PATH)

    if platform:
        query = f"""
            SELECT
                post_id,
                platform,
                published_at,
                impressions,
                engagement_rate
            FROM analytics
            WHERE platform = ? AND DATE(published_at) >= DATE('now', '-{days} days')
        """
        df = pd.read_sql_query(query, conn, params=(platform,))
    else:
        query = f"""
            SELECT
                post_id,
                platform,
                published_at,
                impressions,
                engagement_rate
            FROM analytics
            WHERE DATE(published_at) >= DATE('now', '-{days} days')
        """
        df = pd.read_sql_query(query, conn)

    conn.close()

    if not df.empty:
        df['published_at'] = pd.to_datetime(df['published_at'])
        df['hour'] = df['published_at'].dt.hour
        df['weekday'] = df['published_at'].dt.dayofweek  # 0=月曜, 6=日曜
        df['weekday_name'] = df['published_at'].dt.day_name()

    return df


def create_heatmap(df: pd.DataFrame, platform: str) -> go.Figure:
    """時間帯×曜日のヒートマップ作成"""
    # 時間帯×曜日の平均impressions
    heatmap_data = df.pivot_table(
        values='impressions',
        index='hour',
        columns='weekday',
        aggfunc='mean'
    )

    # 曜日名に変換
    weekday_names = ['月', '火', '水', '木', '金', '土', '日']
    heatmap_data.columns = [weekday_names[i] for i in heatmap_data.columns]

    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=heatmap_data.columns,
        y=heatmap_data.index,
        colorscale='YlOrRd',
        text=heatmap_data.values.round(0),
        texttemplate='%{text:,.0f}',
        textfont={"size": 10},
        colorbar=dict(title="平均<br>impressions")
    ))

    fig.update_layout(
        title=f'{platform.upper()} - 時間帯×曜日別 平均インプレッション',
        xaxis_title='曜日',
        yaxis_title='時間帯',
        height=600
    )

    return fig


def predict_optimal_time(df: pd.DataFrame, platform: str) -> Dict:
    """最適投稿時間を予測"""
    # 時間帯×曜日の平均impressions
    heatmap_data = df.pivot_table(
        values='impressions',
        index='hour',
        columns='weekday',
        aggfunc='mean'
    )

    # 最大値のインデックス取得
    max_idx = heatmap_data.stack().idxmax()
    optimal_hour = max_idx[0]
    optimal_weekday = max_idx[1]

    # 期待impressions
    expected_impressions = heatmap_data.loc[optimal_hour, optimal_weekday]

    # 曜日名
    weekday_names = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

    # Top 3時間帯
    top_3_times = heatmap_data.stack().nlargest(3)
    top_3_list = []
    for (hour, weekday), impressions in top_3_times.items():
        top_3_list.append({
            "hour": hour,
            "weekday": weekday_names[weekday],
            "expected_impressions": impressions
        })

    # Worst 3時間帯
    worst_3_times = heatmap_data.stack().nsmallest(3)
    worst_3_list = []
    for (hour, weekday), impressions in worst_3_times.items():
        worst_3_list.append({
            "hour": hour,
            "weekday": weekday_names[weekday],
            "expected_impressions": impressions
        })

    return {
        "platform": platform,
        "optimal_hour": optimal_hour,
        "optimal_weekday": weekday_names[optimal_weekday],
        "expected_impressions": expected_impressions,
        "top_3_times": top_3_list,
        "worst_3_times": worst_3_list
    }


def generate_prediction_report(predictions: Dict, output_path: Path):
    """予測レポート生成（Markdown）"""
    report = f"""# 最適投稿時間予測レポート

**生成日時**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## 🎯 {predictions['platform'].upper()} - 最適投稿時間

### 最推奨時間
- **曜日**: {predictions['optimal_weekday']}
- **時間帯**: {predictions['optimal_hour']}:00
- **期待インプレッション**: {predictions['expected_impressions']:,.0f}

---

## 🏆 Top 3 推奨時間帯

| Rank | 曜日 | 時間帯 | 期待impressions |
|------|------|--------|----------------|
"""

    for i, time_slot in enumerate(predictions['top_3_times'], 1):
        report += f"| {i} | {time_slot['weekday']} | {time_slot['hour']}:00 | {time_slot['expected_impressions']:,.0f} |\n"

    report += """
---

## ⚠️ Worst 3 避けるべき時間帯

| Rank | 曜日 | 時間帯 | 期待impressions |
|------|------|--------|----------------|
"""

    for i, time_slot in enumerate(predictions['worst_3_times'], 1):
        report += f"| {i} | {time_slot['weekday']} | {time_slot['hour']}:00 | {time_slot['expected_impressions']:,.0f} |\n"

    report += """
---

## 📝 推奨アクション

1. **優先投稿時間**: {optimal_weekday} {optimal_hour}:00に投稿をスケジュール
2. **避けるべき時間**: {worst_weekday} {worst_hour}:00の投稿を避ける
3. **A/Bテスト**: Top 3時間帯で複数パターンをテスト

---

**次回更新**: 1週間後（データ蓄積により精度向上）
""".format(
        optimal_weekday=predictions['optimal_weekday'],
        optimal_hour=predictions['optimal_hour'],
        worst_weekday=predictions['worst_3_times'][0]['weekday'],
        worst_hour=predictions['worst_3_times'][0]['hour']
    )

    # ファイル出力
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"✅ 予測レポート生成完了: {output_path}")


def main():
    """メイン処理"""
    print("\n" + "=" * 80)
    print("🔮 最適投稿時間予測開始")
    print("=" * 80)
    print(f"実行時刻: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # 出力ディレクトリ作成
    OUTPUT_DIR.mkdir(exist_ok=True)

    # プラットフォームリスト
    platforms = ["facebook", "linkedin", "twitter", "threads"]

    for platform in platforms:
        print(f"\n📊 {platform.upper()} - データ読み込み中...")

        # データ読み込み
        df = load_historical_data(platform=platform, days=90)

        if df.empty:
            print(f"   ⚠️  データが不足しています。スキップします。")
            continue

        print(f"   データ件数: {len(df)}件")

        # 最適時間予測
        print(f"🔮 最適投稿時間を予測中...")
        predictions = predict_optimal_time(df, platform)

        print(f"   最適時間: {predictions['optimal_weekday']} {predictions['optimal_hour']}:00")
        print(f"   期待impressions: {predictions['expected_impressions']:,.0f}")

        # ヒートマップ生成
        print(f"📈 ヒートマップを生成中...")
        fig = create_heatmap(df, platform)
        heatmap_path = OUTPUT_DIR / f"heatmap_{platform}_{datetime.now().strftime('%Y%m%d')}.html"
        fig.write_html(str(heatmap_path))
        print(f"   保存完了: {heatmap_path}")

        # レポート生成
        print(f"📝 予測レポートを生成中...")
        report_path = OUTPUT_DIR / f"prediction_{platform}_{datetime.now().strftime('%Y%m%d')}.md"
        generate_prediction_report(predictions, report_path)

    print("\n" + "=" * 80)
    print("✅ 最適投稿時間予測完了")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
