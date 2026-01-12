#!/usr/bin/env python3
"""
テクニカル分析エージェント
8種類のテクニカル指標を計算し、統合シグナルを生成
"""

import json
import math
from datetime import datetime

def calculate_ema(values, period):
    """指数移動平均（EMA）を計算"""
    multiplier = 2 / (period + 1)
    ema = values[0]

    for value in values[1:]:
        ema = (value - ema) * multiplier + ema

    return ema

def calculate_sma(values):
    """単純移動平均（SMA）を計算"""
    return sum(values) / len(values)

def technical_analysis():
    """テクニカル分析のメイン処理"""

    # データ読み込み
    with open('data/sources/2026-01-02/market_data.json', 'r') as f:
        data = json.load(f)

    current_price = data['current_price']['price']
    historical_data = data['historical_data']

    print("📊 テクニカル分析開始")
    print(f"   現在価格: {current_price:,.2f}円")
    print(f"   データポイント数: {len(historical_data)}")
    print()

    # 最新250日分を抽出（約1年）
    recent_data = historical_data[-250:]
    closes = [d['close'] for d in recent_data]
    highs = [d['high'] for d in recent_data]
    lows = [d['low'] for d in recent_data]
    volumes = [d['volume'] for d in recent_data]

    results = {}

    # ============================================
    # 1. 移動平均線（SMA50, SMA200）
    # ============================================
    print("1️⃣  移動平均線を計算中...")

    sma50 = calculate_sma(closes[-50:])
    sma200 = calculate_sma(closes[-200:])

    # シグナル判定
    if sma50 > sma200 and current_price > sma50:
        ma_signal = "買い"
        ma_strength = 2.0
        ma_detail = "ゴールデンクロス維持、価格がSMA50上"
    elif sma50 < sma200 and current_price < sma50:
        ma_signal = "売り"
        ma_strength = 2.0
        ma_detail = "デッドクロス、価格がSMA50下"
    elif current_price > sma50:
        ma_signal = "やや買い"
        ma_strength = 1.5
        ma_detail = "価格がSMA50上"
    elif current_price < sma50:
        ma_signal = "やや売り"
        ma_strength = 1.5
        ma_detail = "価格がSMA50下"
    else:
        ma_signal = "中立"
        ma_strength = 1.0
        ma_detail = "価格がSMA50付近"

    results['ma'] = {
        'sma50': round(sma50, 2),
        'sma200': round(sma200, 2),
        'signal': ma_signal,
        'strength': ma_strength,
        'detail': ma_detail
    }

    print(f"   SMA50: {sma50:,.2f}円")
    print(f"   SMA200: {sma200:,.2f}円")
    print(f"   シグナル: {ma_signal}")
    print()

    # ============================================
    # 2. MACD
    # ============================================
    print("2️⃣  MACDを計算中...")

    # EMA12とEMA26を計算
    ema12 = calculate_ema(closes[-26:], 12)
    ema26 = calculate_ema(closes[-26:], 26)

    macd = ema12 - ema26

    # Signal lineは簡易計算（本来はMACDの9日EMA）
    macd_values = []
    for i in range(9, 27):
        e12 = calculate_ema(closes[-i:], 12)
        e26 = calculate_ema(closes[-i:], 26)
        macd_values.append(e12 - e26)

    signal = calculate_ema(macd_values, 9)
    histogram = macd - signal

    # シグナル判定
    if macd > signal and macd > 0:
        macd_signal = "買い"
        macd_strength = 1.8
        macd_detail = "ゴールデンクロス、プラス圏"
    elif macd > signal and macd < 0:
        macd_signal = "やや買い"
        macd_strength = 1.5
        macd_detail = "ゴールデンクロス、マイナス圏"
    elif macd < signal and macd < 0:
        macd_signal = "売り"
        macd_strength = 1.8
        macd_detail = "デッドクロス、マイナス圏"
    elif macd < signal and macd > 0:
        macd_signal = "やや売り"
        macd_strength = 1.5
        macd_detail = "デッドクロス、プラス圏"
    else:
        macd_signal = "中立"
        macd_strength = 1.0
        macd_detail = "横ばい"

    results['macd'] = {
        'macd': round(macd, 2),
        'signal': round(signal, 2),
        'histogram': round(histogram, 2),
        'signal_type': macd_signal,
        'strength': macd_strength,
        'detail': macd_detail
    }

    print(f"   MACD: {macd:.2f}")
    print(f"   Signal: {signal:.2f}")
    print(f"   シグナル: {macd_signal}")
    print()

    # ============================================
    # 3. RSI（14日）
    # ============================================
    print("3️⃣  RSIを計算中...")

    gains = []
    losses = []

    for i in range(1, 15):
        change = closes[-i] - closes[-i-1]
        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    avg_gain = sum(gains) / 14
    avg_loss = sum(losses) / 14

    if avg_loss == 0:
        rsi = 100
    else:
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))

    # シグナル判定
    if rsi > 70:
        rsi_signal = "売り"
        rsi_strength = 1.6
        rsi_detail = "買われすぎ（RSI > 70）"
    elif rsi < 30:
        rsi_signal = "買い"
        rsi_strength = 1.6
        rsi_detail = "売られすぎ（RSI < 30）"
    elif 50 < rsi < 70:
        rsi_signal = "やや買い"
        rsi_strength = 1.3
        rsi_detail = "強気エリア（50-70）"
    elif 30 < rsi < 50:
        rsi_signal = "やや売り"
        rsi_strength = 1.3
        rsi_detail = "弱気エリア（30-50）"
    else:
        rsi_signal = "中立"
        rsi_strength = 1.0
        rsi_detail = "中立エリア"

    results['rsi'] = {
        'value': round(rsi, 2),
        'signal': rsi_signal,
        'strength': rsi_strength,
        'detail': rsi_detail
    }

    print(f"   RSI: {rsi:.2f}")
    print(f"   シグナル: {rsi_signal}")
    print()

    # ============================================
    # 4. ボリンジャーバンド（20日、2σ）
    # ============================================
    print("4️⃣  ボリンジャーバンドを計算中...")

    sma20 = calculate_sma(closes[-20:])
    variance = sum([(c - sma20)**2 for c in closes[-20:]]) / 20
    std_dev = math.sqrt(variance)

    upper_band = sma20 + (2 * std_dev)
    lower_band = sma20 - (2 * std_dev)

    # シグナル判定
    if current_price > upper_band:
        bb_signal = "売り"
        bb_strength = 1.4
        bb_detail = "上限バンドタッチ（買われすぎ）"
    elif current_price < lower_band:
        bb_signal = "買い"
        bb_strength = 1.4
        bb_detail = "下限バンドタッチ（売られすぎ）"
    elif current_price > sma20:
        bb_signal = "やや買い"
        bb_strength = 1.2
        bb_detail = "上半分（SMA20以上）"
    elif current_price < sma20:
        bb_signal = "やや売り"
        bb_strength = 1.2
        bb_detail = "下半分（SMA20以下）"
    else:
        bb_signal = "中立"
        bb_strength = 1.0
        bb_detail = "中心線付近"

    results['bb'] = {
        'upper': round(upper_band, 2),
        'middle': round(sma20, 2),
        'lower': round(lower_band, 2),
        'signal': bb_signal,
        'strength': bb_strength,
        'detail': bb_detail
    }

    print(f"   上限: {upper_band:,.2f}円")
    print(f"   中心線: {sma20:,.2f}円")
    print(f"   下限: {lower_band:,.2f}円")
    print(f"   シグナル: {bb_signal}")
    print()

    # ============================================
    # 5. ATR（14日）
    # ============================================
    print("5️⃣  ATRを計算中...")

    true_ranges = []

    for i in range(1, 15):
        high = highs[-i]
        low = lows[-i]
        prev_close = closes[-i-1]

        tr = max(
            high - low,
            abs(high - prev_close),
            abs(low - prev_close)
        )
        true_ranges.append(tr)

    atr = sum(true_ranges) / 14
    volatility_pct = (atr / current_price) * 100

    if volatility_pct > 3:
        volatility_level = "高"
    elif volatility_pct > 2:
        volatility_level = "中"
    else:
        volatility_level = "低"

    results['atr'] = {
        'value': round(atr, 2),
        'volatility_pct': round(volatility_pct, 2),
        'level': volatility_level
    }

    print(f"   ATR: {atr:,.2f}円")
    print(f"   ボラティリティ: {volatility_pct:.2f}%（{volatility_level}）")
    print()

    # ============================================
    # 6. 出来高分析
    # ============================================
    print("6️⃣  出来高分析中...")

    avg_volume = sum(volumes[-20:]) / 20
    latest_volume = volumes[-1]
    volume_ratio = latest_volume / avg_volume

    if volume_ratio > 1.5:
        volume_strength = "強い"
        volume_signal = "トレンド継続"
    elif volume_ratio > 1.2:
        volume_strength = "中程度"
        volume_signal = "トレンド継続"
    else:
        volume_strength = "弱い"
        volume_signal = "トレンド弱化"

    results['volume'] = {
        'latest': latest_volume,
        'average': int(avg_volume),
        'ratio': round(volume_ratio, 2),
        'strength': volume_strength,
        'signal': volume_signal
    }

    print(f"   最新出来高: {latest_volume:,}")
    print(f"   平均出来高: {avg_volume:,.0f}")
    print(f"   出来高比率: {volume_ratio:.2f}倍（{volume_strength}）")
    print()

    # ============================================
    # 7. VWMA（20日）
    # ============================================
    print("7️⃣  VWMAを計算中...")

    numerator = sum([closes[-20+i] * volumes[-20+i] for i in range(20)])
    denominator = sum(volumes[-20:])
    vwma20 = numerator / denominator

    if current_price > vwma20:
        vwma_signal = "買い"
        vwma_strength = 1.5
        vwma_detail = "価格がVWMA以上"
    elif current_price < vwma20:
        vwma_signal = "売り"
        vwma_strength = 1.5
        vwma_detail = "価格がVWMA以下"
    else:
        vwma_signal = "中立"
        vwma_strength = 1.0
        vwma_detail = "価格がVWMA付近"

    results['vwma'] = {
        'value': round(vwma20, 2),
        'signal': vwma_signal,
        'strength': vwma_strength,
        'detail': vwma_detail
    }

    print(f"   VWMA: {vwma20:,.2f}円")
    print(f"   シグナル: {vwma_signal}")
    print()

    # ============================================
    # 8. ストキャスティクス（14日）
    # ============================================
    print("8️⃣  ストキャスティクスを計算中...")

    highest_high = max(highs[-14:])
    lowest_low = min(lows[-14:])

    k_value = ((current_price - lowest_low) / (highest_high - lowest_low)) * 100

    if k_value > 80:
        stoch_signal = "売り"
        stoch_strength = 1.4
        stoch_detail = "買われすぎ（%K > 80）"
    elif k_value < 20:
        stoch_signal = "買い"
        stoch_strength = 1.4
        stoch_detail = "売られすぎ（%K < 20）"
    else:
        stoch_signal = "中立"
        stoch_strength = 1.0
        stoch_detail = "中立エリア（20-80）"

    results['stoch'] = {
        'k_value': round(k_value, 2),
        'signal': stoch_signal,
        'strength': stoch_strength,
        'detail': stoch_detail
    }

    print(f"   %K: {k_value:.2f}")
    print(f"   シグナル: {stoch_signal}")
    print()

    # ============================================
    # シグナル統合
    # ============================================
    print("🔄 シグナル統合中...")

    WEIGHTS = {
        'ma': 2.0,
        'macd': 1.8,
        'rsi': 1.6,
        'bb': 1.4,
        'vwma': 1.5,
        'stoch': 1.4
    }

    buy_score = 0
    sell_score = 0

    # 各指標のスコア集計
    for key, weight in WEIGHTS.items():
        signal = results[key]['signal']

        if signal == "買い":
            buy_score += weight * 2.0
        elif signal == "やや買い":
            buy_score += weight * 1.0
        elif signal == "売り":
            sell_score += weight * 2.0
        elif signal == "やや売り":
            sell_score += weight * 1.0

    total_weight = sum(WEIGHTS.values())
    net_score = (buy_score - sell_score) / total_weight

    # 総合シグナル判定
    if net_score > 0.3:
        overall_signal = "強気"
        confidence = min(100, int(net_score * 100))
        direction = "買い"
    elif net_score > 0.1:
        overall_signal = "やや強気"
        confidence = min(100, int(net_score * 80))
        direction = "買い"
    elif net_score < -0.3:
        overall_signal = "弱気"
        confidence = min(100, int(abs(net_score) * 100))
        direction = "売り"
    elif net_score < -0.1:
        overall_signal = "やや弱気"
        confidence = min(100, int(abs(net_score) * 80))
        direction = "売り"
    else:
        overall_signal = "中立"
        confidence = 50
        direction = "見送り"

    results['overall'] = {
        'signal': overall_signal,
        'confidence': confidence,
        'direction': direction,
        'net_score': round(net_score, 3),
        'buy_score': round(buy_score, 2),
        'sell_score': round(sell_score, 2)
    }

    print(f"   総合シグナル: {overall_signal}（信頼度: {confidence}%）")
    print(f"   推奨方向: {direction}")
    print(f"   買いスコア: {buy_score:.2f}")
    print(f"   売りスコア: {sell_score:.2f}")
    print(f"   ネットスコア: {net_score:.3f}")
    print()

    # ============================================
    # 価格目標算出
    # ============================================
    print("🎯 価格目標算出中...")

    atr_value = results['atr']['value']

    if direction == "買い":
        entry_price = current_price * 0.998  # -0.2%押し目
        exit_price = current_price + (2 * atr_value)
        stop_loss = entry_price - atr_value
    elif direction == "売り":
        entry_price = current_price * 1.002  # +0.2%戻り売り
        exit_price = current_price - (2 * atr_value)
        stop_loss = entry_price + atr_value
    else:
        entry_price = current_price
        exit_price = current_price
        stop_loss = current_price

    if direction in ["買い", "売り"]:
        risk = abs(entry_price - stop_loss)
        reward = abs(exit_price - entry_price)
        risk_reward_ratio = reward / risk if risk > 0 else 0

        expected_return = ((exit_price - entry_price) / entry_price) * 100
        max_risk = ((stop_loss - entry_price) / entry_price) * 100
    else:
        risk_reward_ratio = 0
        expected_return = 0
        max_risk = 0

    results['pricing'] = {
        'entry': round(entry_price, 2),
        'exit': round(exit_price, 2),
        'stop_loss': round(stop_loss, 2),
        'risk_reward_ratio': round(risk_reward_ratio, 2),
        'expected_return': round(expected_return, 2),
        'max_risk': round(max_risk, 2)
    }

    print(f"   エントリー: {entry_price:,.2f}円")
    print(f"   目標価格: {exit_price:,.2f}円（{expected_return:+.2f}%）")
    print(f"   ストップロス: {stop_loss:,.2f}円（{max_risk:.2f}%）")
    print(f"   R:R比率: 1:{risk_reward_ratio:.2f}")
    print()

    # ============================================
    # JSON保存
    # ============================================
    output_data = {
        'timestamp': datetime.now().isoformat(),
        'current_price': current_price,
        'indicators': results
    }

    output_file = 'data/results/2026-01-02/technical_analysis.json'
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"✅ テクニカル分析完了")
    print(f"   出力ファイル: {output_file}")

    return results

if __name__ == "__main__":
    technical_analysis()
