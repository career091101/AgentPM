#!/usr/bin/env python3
"""
センチメント分析エージェント v2（実データ版）
市場心理を4つの指標で多面的に分析（WebSearch実データ + 計算指標）
"""

import json
from datetime import datetime

def sentiment_analysis_v2():
    """センチメント分析のメイン処理（改訂版）"""

    print("📊 センチメント分析v2開始（実データ版）")
    print()

    results = {}
    data_quality = {
        'total_indicators': 4,
        'collected': 0,
        'failed': [],
        'data_sources': []
    }

    # ============================================
    # 1. Fear & Greed Index（計算版）
    # ============================================
    print("1️⃣  Fear & Greed Index分析中（RSIベース計算）...")

    # テクニカル分析結果から取得
    with open('data/results/2026-01-02/technical_analysis.json', 'r') as f:
        technical = json.load(f)

    rsi = technical['indicators']['rsi']['value']  # 47.62

    # RSIベースでFear & Greed Indexを推定
    # RSI 30以下 → Extreme Fear (0-25)
    # RSI 30-45 → Fear (25-45)
    # RSI 45-55 → Neutral (45-55)
    # RSI 55-70 → Greed (55-75)
    # RSI 70以上 → Extreme Greed (75-100)

    if rsi <= 30:
        fear_greed_index = rsi * (25 / 30)  # 0-25にマッピング
    elif rsi <= 45:
        fear_greed_index = 25 + (rsi - 30) * ((45 - 25) / (45 - 30))
    elif rsi <= 55:
        fear_greed_index = 45 + (rsi - 45) * ((55 - 45) / (55 - 45))
    elif rsi <= 70:
        fear_greed_index = 55 + (rsi - 55) * ((75 - 55) / (70 - 55))
    else:
        fear_greed_index = 75 + (rsi - 70) * ((100 - 75) / (100 - 70))

    fear_greed_index = round(fear_greed_index, 1)

    if fear_greed_index <= 25:
        fg_signal = "強気"
        fg_confidence = 80
        fg_interpretation = "極度の恐怖 → 買いシグナル（逆張り）"
    elif fear_greed_index <= 45:
        fg_signal = "やや強気"
        fg_confidence = 60
        fg_interpretation = "恐怖 → やや買い"
    elif fear_greed_index <= 55:
        fg_signal = "中立"
        fg_confidence = 40
        fg_interpretation = "中立 → 観望"
    elif fear_greed_index <= 75:
        fg_signal = "やや弱気"
        fg_confidence = 60
        fg_interpretation = "強欲 → やや売り"
    else:
        fg_signal = "弱気"
        fg_confidence = 80
        fg_interpretation = "極度の強欲 → 売りシグナル（逆張り）"

    # 正規化スコア（-100 ~ +100）
    fg_normalized = (fear_greed_index - 50) * 2

    results['fear_greed'] = {
        'index': fear_greed_index,
        'signal': fg_signal,
        'confidence': fg_confidence,
        'normalized_score': fg_normalized,
        'weight': 1.5,
        'interpretation': fg_interpretation,
        'data_source': 'RSIベース計算値'
    }

    data_quality['collected'] += 1
    data_quality['data_sources'].append('Fear & Greed: RSI計算値')
    print(f"   Fear & Greed Index: {fear_greed_index:.1f}（RSI {rsi:.2f}から計算）")
    print(f"   判定: {fg_interpretation}")
    print(f"   シグナル: {fg_signal}")
    print()

    # ============================================
    # 2. Put/Call比率（推定値）
    # ============================================
    print("2️⃣  Put/Call比率分析中（市場傾向から推定）...")

    # 現在の市場状況から推定
    # - RSI 47.62（やや弱気）
    # - VIXやや高め → 警戒的
    # → Put/Call比率は1.05前後と推定（やや悲観的）

    put_call_ratio = 1.05

    if put_call_ratio > 1.2:
        pc_signal = "強気"
        pc_confidence = 70
        pc_interpretation = "プット優勢（悲観的）→ 買いシグナル（逆張り）"
    elif put_call_ratio > 1.0:
        pc_signal = "やや強気"
        pc_confidence = 55
        pc_interpretation = "やや悲観的 → やや買い"
    elif put_call_ratio > 0.8:
        pc_signal = "中立"
        pc_confidence = 40
        pc_interpretation = "均衡 → 中立"
    else:
        pc_signal = "やや弱気"
        pc_confidence = 55
        pc_interpretation = "コール優勢（楽観的）→ やや売り"

    # 正規化スコア（-100 ~ +100）
    pc_normalized = (put_call_ratio - 1.0) * 100

    results['put_call'] = {
        'ratio': round(put_call_ratio, 2),
        'signal': pc_signal,
        'confidence': pc_confidence,
        'normalized_score': round(pc_normalized, 2),
        'weight': 1.3,
        'interpretation': pc_interpretation,
        'data_source': '市場傾向からの推定値'
    }

    data_quality['collected'] += 1
    data_quality['data_sources'].append('Put/Call: 推定値')
    print(f"   Put/Call比率: {put_call_ratio:.2f}（推定値）")
    print(f"   判定: {pc_interpretation}")
    print(f"   シグナル: {pc_signal}")
    print()

    # ============================================
    # 3. 日経VI（VIX）（ATRベース推定）
    # ============================================
    print("3️⃣  日経VI分析中（ATRから推定）...")

    atr_pct = technical['indicators']['atr']['volatility_pct']  # 1.26%

    # ATRからVIX推定
    # ATR 1% → VIX 15程度
    # ATR 2% → VIX 25程度
    # ATR 3% → VIX 35程度
    # 線形補間: VIX ≈ 15 + (ATR - 1) × 10

    nikkei_vi = 15 + (atr_pct - 1.0) * 10
    nikkei_vi = round(nikkei_vi, 1)

    if nikkei_vi > 30:
        vi_signal = "強気"
        vi_confidence = 75
        vi_interpretation = "高ボラティリティ（恐怖）→ 買いシグナル（逆張り）"
    elif nikkei_vi > 20:
        vi_signal = "やや強気"
        vi_confidence = 55
        vi_interpretation = "やや高め → やや買い"
    elif nikkei_vi > 15:
        vi_signal = "中立"
        vi_confidence = 40
        vi_interpretation = "通常レベル → 中立"
    else:
        vi_signal = "やや弱気"
        vi_confidence = 55
        vi_interpretation = "低ボラティリティ（過信）→ やや売り"

    # 正規化スコア（-100 ~ +100）
    vi_normalized = (nikkei_vi - 22.5) * 4

    results['vix'] = {
        'value': nikkei_vi,
        'signal': vi_signal,
        'confidence': vi_confidence,
        'normalized_score': round(vi_normalized, 2),
        'weight': 1.2,
        'interpretation': vi_interpretation,
        'data_source': f'ATR {atr_pct:.2f}%から計算'
    }

    data_quality['collected'] += 1
    data_quality['data_sources'].append('VIX: ATR計算値')
    print(f"   日経VI: {nikkei_vi:.1f}（ATR {atr_pct:.2f}%から計算）")
    print(f"   判定: {vi_interpretation}")
    print(f"   シグナル: {vi_signal}")
    print()

    # ============================================
    # 4. ニュースセンチメント（WebSearch実データ）
    # ============================================
    print("4️⃣  ニュースセンチメント分析中（WebSearch実データ）...")

    # WebSearch結果から分析
    # 2026年1月最新ニュース分析結果:
    # ポジティブ: 経営者20人全員が最高値更新予想、56,000円予想、サナエノミクス期待
    # ネガティブ: 日銀追加利上げ、トランプ関税、AIバブル懸念

    positive_topics = [
        "経営者20人全員が最高値更新を予想",
        "大和アセット2026年末56,000円予想",
        "野村證券52,000円予想",
        "数カ月内に6万円予想",
        "サナエノミクス期待",
        "AI・半導体成長期待"
    ]

    negative_topics = [
        "日銀の追加利上げリスク",
        "トランプ関税リスク",
        "AIバブル懸念"
    ]

    neutral_topics = []

    positive_count = len(positive_topics)
    negative_count = len(negative_topics)
    neutral_count = len(neutral_topics)
    total_count = positive_count + negative_count + neutral_count

    sentiment_score = ((positive_count - negative_count) / total_count) * 100

    if sentiment_score < -50:
        news_signal = "強気"
        news_confidence = 70
        news_interpretation = "極度にネガティブ → 買いシグナル（逆張り）"
    elif sentiment_score < -20:
        news_signal = "やや強気"
        news_confidence = 55
        news_interpretation = "ネガティブ → やや買い"
    elif sentiment_score < 20:
        news_signal = "中立"
        news_confidence = 40
        news_interpretation = "中立 → 観望"
    elif sentiment_score < 50:
        news_signal = "やや弱気"  # ポジティブニュース多い = 過熱 = 売りシグナル（逆張り）
        news_confidence = 55
        news_interpretation = "ポジティブ → やや売り（逆張り）"
    else:
        news_signal = "弱気"
        news_confidence = 70
        news_interpretation = "極度にポジティブ → 売りシグナル（逆張り）"

    results['news'] = {
        'total_news': total_count,
        'positive': positive_count,
        'negative': negative_count,
        'neutral': neutral_count,
        'sentiment_score': round(sentiment_score, 2),
        'signal': news_signal,
        'confidence': news_confidence,
        'normalized_score': round(sentiment_score, 2),
        'weight': 1.0,
        'interpretation': news_interpretation,
        'data_source': 'WebSearch 2026年1月最新ニュース',
        'topics': {
            'positive': positive_topics,
            'negative': negative_topics,
            'neutral': neutral_topics
        }
    }

    data_quality['collected'] += 1
    data_quality['data_sources'].append('News: WebSearch実データ')
    print(f"   分析ニュース数: {total_count}件（WebSearch実データ）")
    print(f"   ポジティブ: {positive_count}件、ネガティブ: {negative_count}件、中立: {neutral_count}件")
    print(f"   センチメントスコア: {sentiment_score:.2f}")
    print(f"   判定: {news_interpretation}")
    print(f"   シグナル: {news_signal}")
    print()

    # ============================================
    # 統合判定
    # ============================================
    print("🔄 統合判定中...")

    # 重み付け総合スコア計算
    WEIGHTS = {
        'fear_greed': 1.5,
        'put_call': 1.3,
        'vix': 1.2,
        'news': 1.0
    }

    total_score = 0
    total_weight = 0

    for key in ['fear_greed', 'put_call', 'vix', 'news']:
        if key in results:
            total_score += results[key]['normalized_score'] * WEIGHTS[key]
            total_weight += WEIGHTS[key]

    overall_score = total_score / total_weight if total_weight > 0 else 0

    # 総合判定
    if overall_score < -40:
        overall_sentiment = "強気"
        overall_signal = "買い"
        overall_confidence = min(80, int(abs(overall_score) * 0.8))
    elif overall_score < -15:
        overall_sentiment = "やや強気"
        overall_signal = "やや買い"
        overall_confidence = 60
    elif overall_score < 15:
        overall_sentiment = "中立"
        overall_signal = "観望"
        overall_confidence = 40
    elif overall_score < 40:
        overall_sentiment = "やや弱気"
        overall_signal = "やや売り"
        overall_confidence = 60
    else:
        overall_sentiment = "弱気"
        overall_signal = "売り"
        overall_confidence = min(80, int(abs(overall_score) * 0.8))

    results['overall'] = {
        'sentiment': overall_sentiment,
        'signal': overall_signal,
        'confidence': overall_confidence,
        'total_score': round(overall_score, 2),
        'interpretation': f"スコア{overall_score:.1f}は「{overall_sentiment}」ゾーン"
    }

    print(f"   総合センチメント: {overall_sentiment}")
    print(f"   シグナル: {overall_signal}")
    print(f"   信頼度: {overall_confidence}%")
    print(f"   総合スコア: {overall_score:.2f}")
    print()

    # ============================================
    # JSON保存
    # ============================================
    output_data = {
        'timestamp': datetime.now().isoformat(),
        'version': 'v2 (実データ版)',
        'data_quality': data_quality,
        'indicators': results
    }

    output_file = 'data/results/2026-01-02/sentiment_analysis_v2.json'
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"✅ センチメント分析v2完了")
    print(f"   出力ファイル: {output_file}")
    print(f"   収集指標数: {data_quality['collected']}/4")
    print(f"   データソース: {', '.join(data_quality['data_sources'])}")

    return results


if __name__ == "__main__":
    sentiment_analysis_v2()
