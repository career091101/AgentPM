#!/usr/bin/env python3
"""
エリオット波動分析エージェント
Primary/Intermediate/Minor degreeの波動カウント + フィボナッチ目標算出
"""

import json
import math
from datetime import datetime

def find_peaks_and_troughs(data, window=10):
    """ピーク（高値）とトラフ（安値）を検出"""
    peaks = []
    troughs = []

    for i in range(window, len(data) - window):
        # ピーク検出
        is_peak = all(data[i]['high'] >= data[j]['high'] for j in range(i-window, i+window+1))
        if is_peak:
            peaks.append({'index': i, 'date': data[i]['date'], 'price': data[i]['high']})

        # トラフ検出
        is_trough = all(data[i]['low'] <= data[j]['low'] for j in range(i-window, i+window+1))
        if is_trough:
            troughs.append({'index': i, 'date': data[i]['date'], 'price': data[i]['low']})

    return peaks, troughs

def elliott_wave_analysis():
    """エリオット波動分析のメイン処理"""

    # データ読み込み
    with open('data/sources/2026-01-02/market_data.json', 'r') as f:
        data = json.load(f)

    current_price = data['current_price']['price']
    historical_data = data['historical_data']

    print("📈 エリオット波動分析開始")
    print(f"   現在価格: {current_price:,.2f}円")
    print(f"   データポイント数: {len(historical_data)}")
    print()

    results = {}

    # ============================================
    # STEP 1: Primary Degree（長期：5年分）
    # ============================================
    print("1️⃣  Primary Degree（長期トレンド）分析中...")

    # 全期間の主要な高値・安値
    all_highs = [d['high'] for d in historical_data]
    all_lows = [d['low'] for d in historical_data]

    major_low = min(all_lows)
    major_low_index = all_lows.index(major_low)
    major_low_date = historical_data[major_low_index]['date']

    major_high = max(all_highs)
    major_high_index = all_highs.index(major_high)
    major_high_date = historical_data[major_high_index]['date']

    # 大局的な波動判定
    if major_low_index < major_high_index and current_price > major_low * 1.3:
        primary_wave = "Wave (III) または (V)"
        primary_direction = "Up"
        primary_confidence = 70
        primary_description = f"2020年安値{major_low:,.0f}円から上昇トレンド継続中"
    else:
        primary_wave = "Wave (IV) Correction"
        primary_direction = "Correction"
        primary_confidence = 65
        primary_description = "大局的な調整局面"

    # Wave 1の長さ（最初の上昇）
    wave_1_length = major_high - major_low

    # Primary degreeのフィボナッチ目標
    primary_fibo_618 = major_low + (wave_1_length * 1.618)
    primary_fibo_100 = major_low + wave_1_length
    primary_fibo_161 = major_low + (wave_1_length * 2.618)

    results['primary'] = {
        'wave': primary_wave,
        'direction': primary_direction,
        'confidence': primary_confidence,
        'description': primary_description,
        'major_low': round(major_low, 2),
        'major_low_date': major_low_date,
        'major_high': round(major_high, 2),
        'major_high_date': major_high_date,
        'wave_1_length': round(wave_1_length, 2),
        'targets': {
            'fibo_100': round(primary_fibo_100, 2),
            'fibo_618': round(primary_fibo_618, 2),
            'fibo_161': round(primary_fibo_161, 2)
        }
    }

    print(f"   波動: {primary_wave}")
    print(f"   方向: {primary_direction}")
    print(f"   大局安値: {major_low:,.2f}円（{major_low_date}）")
    print(f"   大局高値: {major_high:,.2f}円（{major_high_date}）")
    print(f"   Wave 1長さ: {wave_1_length:,.2f}円")
    print()

    # ============================================
    # STEP 2: Intermediate Degree（中期：週足ベース）
    # ============================================
    print("2️⃣  Intermediate Degree（中期トレンド）分析中...")

    # 過去6ヶ月（約130営業日）
    intermediate_data = historical_data[-130:]
    inter_highs = [d['high'] for d in intermediate_data]
    inter_lows = [d['low'] for d in intermediate_data]

    intermediate_low = min(inter_lows)
    intermediate_low_index = inter_lows.index(intermediate_low)
    intermediate_low_date = intermediate_data[intermediate_low_index]['date']

    intermediate_high = max(inter_highs)
    intermediate_high_index = inter_highs.index(intermediate_high)
    intermediate_high_date = intermediate_data[intermediate_high_index]['date']

    # ピークとトラフを検出
    peaks, troughs = find_peaks_and_troughs(intermediate_data, window=5)

    # 波動カウント（簡易版：上昇波の数）
    if intermediate_low_index < intermediate_high_index:
        # 上昇トレンド
        wave_count = len([p for p in peaks if p['index'] > intermediate_low_index])

        if wave_count >= 5:
            intermediate_wave = "Wave (5) Final"
            intermediate_direction = "Up (completion risk)"
            intermediate_confidence = 65
            correction_type = None
        elif wave_count >= 3:
            intermediate_wave = "Wave (3) Impulse"
            intermediate_direction = "Up"
            intermediate_confidence = 75
            correction_type = None
        else:
            intermediate_wave = "Wave (1) Early"
            intermediate_direction = "Up (early stage)"
            intermediate_confidence = 60
            correction_type = None
    else:
        # 調整局面
        intermediate_wave = "Wave (4) Corrective"
        intermediate_direction = "Correction"
        intermediate_confidence = 70

        # 調整パターンの判定（簡易版）
        correction_depth = (intermediate_high - current_price) / (intermediate_high - intermediate_low)

        if correction_depth < 0.382:
            correction_type = "Shallow Correction (Zigzag)"
        elif correction_depth < 0.618:
            correction_type = "Normal Correction (Flat)"
        else:
            correction_type = "Deep Correction (Complex)"

    # Intermediate degreeのフィボナッチ
    inter_wave_length = intermediate_high - intermediate_low

    # 上昇目標（エクステンション）
    inter_fibo_100 = intermediate_low + inter_wave_length
    inter_fibo_618 = intermediate_low + (inter_wave_length * 1.618)
    inter_fibo_161 = intermediate_low + (inter_wave_length * 2.618)

    # 調整目標（リトレースメント）
    inter_retr_382 = intermediate_high - (inter_wave_length * 0.382)
    inter_retr_500 = intermediate_high - (inter_wave_length * 0.500)
    inter_retr_618 = intermediate_high - (inter_wave_length * 0.618)

    results['intermediate'] = {
        'wave': intermediate_wave,
        'direction': intermediate_direction,
        'confidence': intermediate_confidence,
        'correction_type': correction_type,
        'intermediate_low': round(intermediate_low, 2),
        'intermediate_low_date': intermediate_low_date,
        'intermediate_high': round(intermediate_high, 2),
        'intermediate_high_date': intermediate_high_date,
        'wave_count': wave_count if intermediate_low_index < intermediate_high_index else 0,
        'targets': {
            'fibo_100': round(inter_fibo_100, 2),
            'fibo_618': round(inter_fibo_618, 2),
            'fibo_161': round(inter_fibo_161, 2)
        },
        'retracements': {
            'fibo_382': round(inter_retr_382, 2),
            'fibo_500': round(inter_retr_500, 2),
            'fibo_618': round(inter_retr_618, 2)
        }
    }

    print(f"   波動: {intermediate_wave}")
    print(f"   方向: {intermediate_direction}")
    print(f"   中期安値: {intermediate_low:,.2f}円（{intermediate_low_date}）")
    print(f"   中期高値: {intermediate_high:,.2f}円（{intermediate_high_date}）")
    if correction_type:
        print(f"   調整パターン: {correction_type}")
    print()

    # ============================================
    # STEP 3: Minor Degree（短期：日足ベース）
    # ============================================
    print("3️⃣  Minor Degree（短期トレンド）分析中...")

    # 過去2ヶ月（約40営業日）
    minor_data = historical_data[-40:]
    minor_highs = [d['high'] for d in minor_data]
    minor_lows = [d['low'] for d in minor_data]

    minor_low = min(minor_lows)
    minor_low_index = minor_lows.index(minor_low)
    minor_low_date = minor_data[minor_low_index]['date']

    minor_high = max(minor_highs)
    minor_high_index = minor_highs.index(minor_high)
    minor_high_date = minor_data[minor_high_index]['date']

    # 短期波動カウント
    minor_peaks, minor_troughs = find_peaks_and_troughs(minor_data, window=3)

    if minor_low_index < minor_high_index:
        minor_wave_count = len([p for p in minor_peaks if p['index'] > minor_low_index])

        if minor_wave_count >= 5:
            minor_wave = "Wave v (completion)"
            minor_direction = "Up (near top)"
            minor_confidence = 65
        elif minor_wave_count >= 3:
            minor_wave = "Wave iii (middle)"
            minor_direction = "Up"
            minor_confidence = 70
        else:
            minor_wave = "Wave i (early)"
            minor_direction = "Up (early stage)"
            minor_confidence = 60
    else:
        minor_wave = "Wave c (corrective)"
        minor_direction = "Correction"
        minor_confidence = 65

    results['minor'] = {
        'wave': minor_wave,
        'direction': minor_direction,
        'confidence': minor_confidence,
        'minor_low': round(minor_low, 2),
        'minor_low_date': minor_low_date,
        'minor_high': round(minor_high, 2),
        'minor_high_date': minor_high_date,
        'wave_count': minor_wave_count if minor_low_index < minor_high_index else 0
    }

    print(f"   波動: {minor_wave}")
    print(f"   方向: {minor_direction}")
    print(f"   短期安値: {minor_low:,.2f}円（{minor_low_date}）")
    print(f"   短期高値: {minor_high:,.2f}円（{minor_high_date}）")
    print()

    # ============================================
    # STEP 4: サポート/レジスタンスレベル
    # ============================================
    print("4️⃣  サポート/レジスタンスレベル特定中...")

    support_levels = [
        {'price': round(intermediate_low, 2), 'description': 'Intermediate degree安値'},
        {'price': round(inter_retr_382, 2), 'description': 'フィボ38.2%リトレースメント'},
        {'price': round(inter_retr_500, 2), 'description': 'フィボ50.0%リトレースメント'},
        {'price': round(minor_low, 2), 'description': 'Minor degree安値'}
    ]

    resistance_levels = [
        {'price': round(intermediate_high, 2), 'description': '直近高値'},
        {'price': round(inter_fibo_618, 2), 'description': 'フィボ61.8%エクステンション'},
        {'price': round(inter_fibo_161, 2), 'description': 'フィボ161.8%エクステンション'}
    ]

    # 重複削除と並び替え
    support_levels = sorted(list({s['price']: s for s in support_levels}.values()), key=lambda x: x['price'], reverse=True)
    resistance_levels = sorted(list({r['price']: r for r in resistance_levels}.values()), key=lambda x: x['price'])

    results['levels'] = {
        'support': support_levels[:3],  # 上位3つ
        'resistance': resistance_levels[:3]  # 上位3つ
    }

    print(f"   サポート数: {len(support_levels[:3])}")
    print(f"   レジスタンス数: {len(resistance_levels[:3])}")
    print()

    # ============================================
    # STEP 5: シナリオ分析
    # ============================================
    print("5️⃣  シナリオ分析中...")

    # メインシナリオ
    if intermediate_direction == "Up":
        main_scenario = {
            'description': f"{intermediate_wave}が{int(inter_fibo_618):,}円まで上昇後、調整へ",
            'probability': 70,
            'targets': [int(inter_fibo_618), int(inter_fibo_161)],
            'invalidation': f"{int(intermediate_low):,}円割れ"
        }

        sub_scenario = {
            'description': f"Wave拡張で{int(inter_fibo_161):,}円到達後、急激な調整",
            'probability': 30,
            'targets': [int(inter_fibo_161)],
            'warning': "拡張波の後は急落リスク大"
        }

    else:  # Correction
        main_scenario = {
            'description': f"{correction_type}による調整が{int(inter_retr_382):,}円まで進行後、反転上昇",
            'probability': 70,
            'targets': [int(inter_retr_382)],
            'invalidation': f"{int(inter_retr_618):,}円割れ"
        }

        sub_scenario = {
            'description': f"複雑調整（Expanded Flat）で{int(inter_retr_618):,}円まで深掘り",
            'probability': 30,
            'targets': [int(inter_retr_618)],
            'warning': "深い調整に注意"
        }

    results['scenarios'] = {
        'main': main_scenario,
        'sub': sub_scenario
    }

    print(f"   メインシナリオ: {main_scenario['description']}")
    print(f"   サブシナリオ: {sub_scenario['description']}")
    print()

    # ============================================
    # STEP 6: トレード推奨
    # ============================================
    print("6️⃣  トレード推奨算出中...")

    if intermediate_direction == "Up":
        # 上昇波動
        entry_low = current_price * 0.99
        entry_high = current_price * 1.01
        target_price = inter_fibo_618
        stop_loss = intermediate_low
        direction = "買い"

    else:  # Correction
        if current_price > inter_retr_382:
            # 浅い調整で反転の可能性
            entry_low = inter_retr_382 * 0.99
            entry_high = inter_retr_382 * 1.01
            target_price = intermediate_high
            stop_loss = inter_retr_618
            direction = "買い（押し目待ち）"
        else:
            # 深い調整中、様子見推奨
            entry_low = None
            entry_high = None
            target_price = None
            stop_loss = None
            direction = "見送り"

    if entry_low and entry_high:
        expected_return = ((target_price - current_price) / current_price) * 100
        max_risk = ((stop_loss - current_price) / current_price) * 100
        risk_reward = abs(expected_return / max_risk) if max_risk != 0 else 0
    else:
        expected_return = 0
        max_risk = 0
        risk_reward = 0

    results['trade'] = {
        'direction': direction,
        'entry_range': [round(entry_low, 2), round(entry_high, 2)] if entry_low else None,
        'target': round(target_price, 2) if target_price else None,
        'stop_loss': round(stop_loss, 2) if stop_loss else None,
        'expected_return': round(expected_return, 2),
        'max_risk': round(max_risk, 2),
        'risk_reward_ratio': round(risk_reward, 2)
    }

    print(f"   推奨方向: {direction}")
    if entry_low:
        print(f"   エントリーレンジ: {entry_low:,.2f}-{entry_high:,.2f}円")
        print(f"   目標価格: {target_price:,.2f}円")
        print(f"   ストップロス: {stop_loss:,.2f}円")
        print(f"   R:R比率: 1:{risk_reward:.2f}")
    print()

    # ============================================
    # JSON保存
    # ============================================
    output_data = {
        'timestamp': datetime.now().isoformat(),
        'current_price': current_price,
        'analysis': results
    }

    output_file = 'data/results/2026-01-02/elliott_wave_analysis.json'
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"✅ エリオット波動分析完了")
    print(f"   出力ファイル: {output_file}")

    return results

if __name__ == "__main__":
    elliott_wave_analysis()
