#!/usr/bin/env python3
"""
SNS KPIダッシュボード（Streamlit）
リアルタイムでKPI可視化
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path


# ページ設定
st.set_page_config(
    page_title="SNS Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ベースパス
BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "data" / "analytics.db"


# データベース接続
@st.cache_data(ttl=300)  # 5分キャッシュ
def load_analytics_data(days=30):
    """アナリティクスデータを読み込み"""
    conn = sqlite3.connect(DB_PATH)

    query = f"""
        SELECT
            post_id,
            platform,
            DATE(published_at) as date,
            published_at,
            impressions,
            reach,
            likes,
            comments,
            shares,
            clicks,
            views,
            engagement_rate
        FROM analytics
        WHERE DATE(published_at) >= DATE('now', '-{days} days')
        ORDER BY published_at DESC
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    if not df.empty:
        df['published_at'] = pd.to_datetime(df['published_at'])
        df['date'] = pd.to_datetime(df['date'])

    return df


@st.cache_data(ttl=300)
def load_daily_summary(days=30):
    """日次サマリーを読み込み"""
    conn = sqlite3.connect(DB_PATH)

    query = f"""
        SELECT
            date,
            platform,
            total_posts,
            total_impressions,
            total_engagement,
            avg_engagement_rate,
            top_post_impressions
        FROM daily_summary
        WHERE DATE(date) >= DATE('now', '-{days} days')
        ORDER BY date DESC
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])

    return df


def main():
    """メイン処理"""

    # タイトル
    st.title("📊 SNS Analytics Dashboard")
    st.markdown("---")

    # サイドバー: 期間選択
    st.sidebar.header("📅 設定")
    period = st.sidebar.selectbox(
        "表示期間",
        [7, 14, 30, 60, 90],
        index=2,
        format_func=lambda x: f"過去{x}日間"
    )

    # データ読み込み
    df = load_analytics_data(days=period)
    df_summary = load_daily_summary(days=period)

    if df.empty:
        st.warning("⚠️ データがありません。`daily_analytics_collection.py`を実行してください。")
        return

    # KPI計算
    total_impressions = df['impressions'].sum()
    total_posts = len(df)
    avg_impressions = df['impressions'].mean()
    avg_engagement_rate = df['engagement_rate'].mean()
    total_engagement = (df['likes'] + df['comments'] + df['shares']).sum()

    # 目標設定
    GOAL_IMPRESSIONS_MONTHLY = 1_000_000
    days_in_period = period
    goal_for_period = GOAL_IMPRESSIONS_MONTHLY * (days_in_period / 30)
    achievement_rate = (total_impressions / goal_for_period) * 100 if goal_for_period > 0 else 0

    # ===== KPIカード =====
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            label="総インプレッション",
            value=f"{total_impressions:,.0f}",
            delta=f"目標: {goal_for_period:,.0f}"
        )

    with col2:
        st.metric(
            label="目標達成率",
            value=f"{achievement_rate:.1f}%",
            delta=f"{achievement_rate - 100:.1f}%" if achievement_rate < 100 else f"+{achievement_rate - 100:.1f}%"
        )

    with col3:
        st.metric(
            label="総投稿数",
            value=f"{total_posts}件",
            delta=f"{total_posts / (period / 30):.1f}件/月"
        )

    with col4:
        st.metric(
            label="平均imp/投稿",
            value=f"{avg_impressions:,.0f}",
            delta=f"目標: 11,111"
        )

    with col5:
        st.metric(
            label="平均エンゲージメント率",
            value=f"{avg_engagement_rate:.2f}%",
            delta=None
        )

    st.markdown("---")

    # ===== プラットフォーム別分析 =====
    st.header("📱 プラットフォーム別分析")

    col1, col2 = st.columns(2)

    with col1:
        # プラットフォーム別総impressions（棒グラフ）
        platform_summary = df.groupby('platform').agg({
            'impressions': 'sum',
            'post_id': 'count'
        }).reset_index()
        platform_summary.columns = ['platform', 'total_impressions', 'post_count']

        fig_platform = px.bar(
            platform_summary,
            x='platform',
            y='total_impressions',
            title='プラットフォーム別総インプレッション',
            color='platform',
            text='total_impressions'
        )
        fig_platform.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        st.plotly_chart(fig_platform, use_container_width=True)

    with col2:
        # プラットフォーム別平均imp/投稿（棒グラフ）
        platform_avg = df.groupby('platform')['impressions'].mean().reset_index()
        platform_avg.columns = ['platform', 'avg_impressions']

        fig_platform_avg = px.bar(
            platform_avg,
            x='platform',
            y='avg_impressions',
            title='プラットフォーム別平均imp/投稿',
            color='platform',
            text='avg_impressions'
        )
        fig_platform_avg.update_traces(texttemplate='%{text:,.0f}', textposition='outside')
        st.plotly_chart(fig_platform_avg, use_container_width=True)

    st.markdown("---")

    # ===== 日別推移 =====
    st.header("📈 日別推移")

    # 日別impressions推移（折れ線グラフ）
    daily_trend = df.groupby(['date', 'platform'])['impressions'].sum().reset_index()

    fig_daily_trend = px.line(
        daily_trend,
        x='date',
        y='impressions',
        color='platform',
        title='日別インプレッション推移',
        markers=True
    )
    st.plotly_chart(fig_daily_trend, use_container_width=True)

    st.markdown("---")

    # ===== Top 10 / Bottom 10投稿 =====
    st.header("🏆 投稿ランキング")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 10投稿")
        top_10 = df.nlargest(10, 'impressions')[['post_id', 'platform', 'date', 'impressions', 'engagement_rate']]
        top_10.index = range(1, 11)
        st.dataframe(top_10, use_container_width=True)

    with col2:
        st.subheader("Bottom 10投稿")
        bottom_10 = df.nsmallest(10, 'impressions')[['post_id', 'platform', 'date', 'impressions', 'engagement_rate']]
        bottom_10.index = range(1, 11)
        st.dataframe(bottom_10, use_container_width=True)

    st.markdown("---")

    # ===== エンゲージメント率分布 =====
    st.header("📊 エンゲージメント率分布")

    fig_engagement_dist = px.histogram(
        df,
        x='engagement_rate',
        nbins=30,
        title='エンゲージメント率分布（ヒストグラム）',
        color='platform',
        marginal='box'
    )
    st.plotly_chart(fig_engagement_dist, use_container_width=True)

    st.markdown("---")

    # ===== 目標達成ゲージ =====
    st.header("🎯 目標達成状況")

    # 月間換算
    monthly_impressions = total_impressions * (30 / period)

    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=monthly_impressions,
        delta={'reference': GOAL_IMPRESSIONS_MONTHLY},
        title={'text': "月間インプレッション（換算値）"},
        gauge={
            'axis': {'range': [0, GOAL_IMPRESSIONS_MONTHLY]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, GOAL_IMPRESSIONS_MONTHLY * 0.5], 'color': "lightgray"},
                {'range': [GOAL_IMPRESSIONS_MONTHLY * 0.5, GOAL_IMPRESSIONS_MONTHLY * 0.8], 'color': "yellow"},
                {'range': [GOAL_IMPRESSIONS_MONTHLY * 0.8, GOAL_IMPRESSIONS_MONTHLY], 'color': "lightgreen"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': GOAL_IMPRESSIONS_MONTHLY
            }
        }
    ))

    st.plotly_chart(fig_gauge, use_container_width=True)

    st.markdown("---")

    # ===== 生データ表示 =====
    with st.expander("📄 生データを表示"):
        st.dataframe(df, use_container_width=True)

    # フッター
    st.markdown("---")
    st.caption(f"最終更新: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
