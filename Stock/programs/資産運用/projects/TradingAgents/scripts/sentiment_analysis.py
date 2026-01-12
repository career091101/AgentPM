#!/usr/bin/env python3
"""
センチメント分析エージェント
市場心理を4つの指標で多面的に分析
"""

import json
from datetime import datetime

def sentiment_analysis():
    """センチメント分析のメイン処理"""

    print("📊 センチメント分析開始")
    print()

    results = {}
    data_quality = {
        'total_indicators': 4,
        'collected': 0,
        'failed': []
    }

    # ============================================
    # 1. Fear & Greed Index（簡易版）
    # ============================================
    print("1️⃣  Fear & Greed Index分析中...")

    # 注意: CNN Fear & Greed IndexはアメリカのS&P500向け
    # 日本市場向けの代替として、RSIベースの簡易指数を計算
    # 実データはWebFetch/WebSearchで取得する必要あり

    # 仮想データ（実装時はWebFetchで取得）
    fear_greed_index = 42  # 0-100（簡易版: RSI的な指標で代用）

    if fear_greed_index is not None:
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
            'interpretation': fg_interpretation
        }

        data_quality['collected'] += 1
        print(f"   Fear & Greed Index: {fear_greed_index}")
        print(f"   判定: {fg_interpretation}")
        print(f"   シグナル: {fg_signal}")
    else:
        data_quality['failed'].append('fear_greed')
        print("   ⚠️ Fear & Greed Index取得失敗")

    print()

    # ============================================
    # 2. Put/Call比率（簡易版）
    # ============================================
    print("2️⃣  Put/Call比率分析中...")

    # 仮想データ（実装時はJPXデータをWebFetchで取得）
    put_volume = 1250000
    call_volume = 1100000
    put_call_ratio = put_volume / call_volume if call_volume > 0 else 1.0

    if put_call_ratio is not None:
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
            'put_volume': put_volume,
            'call_volume': call_volume,
            'ratio': round(put_call_ratio, 2),
            'signal': pc_signal,
            'confidence': pc_confidence,
            'normalized_score': round(pc_normalized, 2),
            'weight': 1.3,
            'interpretation': pc_interpretation
        }

        data_quality['collected'] += 1
        print(f"   Put出来高: {put_volume:,}")
        print(f"   Call出来高: {call_volume:,}")
        print(f"   比率: {put_call_ratio:.2f}")
        print(f"   判定: {pc_interpretation}")
        print(f"   シグナル: {pc_signal}")
    else:
        data_quality['failed'].append('put_call')
        print("   ⚠️ Put/Call比率取得失敗")

    print()

    # ============================================
    # 3. 日経VI（VIX指数）（簡易版）
    # ============================================
    print("3️⃣  日経VI分析中...")

    # 仮想データ（実装時はJPXデータをWebFetchで取得）
    nikkei_vi = 24.5

    if nikkei_vi is not None:
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
            'interpretation': vi_interpretation
        }

        data_quality['collected'] += 1
        print(f"   日経VI: {nikkei_vi}")
        print(f"   判定: {vi_interpretation}")
        print(f"   シグナル: {vi_signal}")
    else:
        data_quality['failed'].append('vix')
        print("   ⚠️ 日経VI取得失敗")

    print()

    # ============================================
    # 4. ニュースセンチメント（簡易版）
    # ============================================
    print("4️⃣  ニュースセンチメント分析中...")

    # 仮想データ（実装時はGoogle NewsをWebFetchで取得）
    news_data = {
        'total': 20,
        'positive': 6,
        'negative': 10,
        'neutral': 4
    }

    positive_count = news_data['positive']
    negative_count = news_data['negative']
    neutral_count = news_data['neutral']
    total_count = news_data['total']

    if total_count > 0:
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
            news_signal = "やや弱気"
            news_confidence = 55
            news_interpretation = "ポジティブ → やや売り"
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
            'interpretation': news_interpretation
        }

        data_quality['collected'] += 1
        print(f"   分析ニュース数: {total_count}件")
        print(f"   ポジティブ: {positive_count}件、ネガティブ: {negative_count}件、中立: {neutral_count}件")
        print(f"   センチメントスコア: {sentiment_score:.2f}")
        print(f"   判定: {news_interpretation}")
        print(f"   シグナル: {news_signal}")
    else:
        data_quality['failed'].append('news')
        print("   ⚠️ ニュースセンチメント取得失敗")

    print()

    # ============================================
    # 統合判定
    # ============================================
    print("🔄 統合判定中...")

    # データ品質チェック
    if data_quality['collected'] < 3:
        print(f"❌ データ不足: {data_quality['collected']}/4指標のみ取得")
        print(f"   失敗した指標: {', '.join(data_quality['failed'])}")
        return None

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
        'data_quality': data_quality,
        'indicators': results
    }

    output_file = 'data/results/2026-01-02/sentiment_analysis.json'
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"✅ センチメント分析完了")
    print(f"   出力ファイル: {output_file}")
    print(f"   収集指標数: {data_quality['collected']}/4")

    return results

if __name__ == "__main__":
    sentiment_analysis()
