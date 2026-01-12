#!/usr/bin/env python3
"""
戦略統合エージェント
3エージェント（テクニカル・エリオット波動・センチメント）の分析結果を統合
"""

import json
from datetime import datetime

def strategy_synthesizer():
    """戦略統合のメイン処理"""

    print("🔄 戦略統合開始")
    print()

    # ============================================
    # STEP 1: 各エージェントの分析結果読み込み
    # ============================================
    print("1️⃣  各エージェントの分析結果読み込み中...")

    with open('data/results/2026-01-02/technical_analysis.json', 'r') as f:
        technical = json.load(f)

    with open('data/results/2026-01-02/elliott_wave_analysis.json', 'r') as f:
        elliott = json.load(f)

    with open('data/results/2026-01-02/sentiment_analysis.json', 'r') as f:
        sentiment = json.load(f)

    # 各エージェントのシグナル抽出
    tech_data = technical['indicators']['overall']
    tech_pricing = technical['indicators']['pricing']

    elliott_data = elliott['analysis']['intermediate']
    elliott_trade = elliott['analysis']['trade']

    sent_data = sentiment['indicators']['overall']

    print(f"   テクニカル: {tech_data['signal']}（信頼度{tech_data['confidence']}%）")
    print(f"   エリオット波動: {elliott_data['direction']}（確度{elliott_data['confidence']}%）")
    print(f"   センチメント: {sent_data['sentiment']}（信頼度{sent_data['confidence']}%）")
    print()

    # ============================================
    # STEP 2: シグナル統合
    # ============================================
    print("2️⃣  シグナル統合中...")

    # 各エージェントの重み設定
    AGENT_WEIGHTS = {
        'technical': 2.0,      # テクニカル分析（最重要）
        'elliott': 1.8,        # エリオット波動
        'sentiment': 1.2       # センチメント分析（補助的）
    }

    # シグナルを数値化
    def signal_to_score(signal, signal_type='technical'):
        if signal_type == 'technical':
            if signal == "強気":
                return 2.0
            elif signal == "やや強気":
                return 1.0
            elif signal == "中立":
                return 0.0
            elif signal == "やや弱気":
                return -1.0
            elif signal == "弱気":
                return -2.0
        elif signal_type == 'elliott':
            if "Up" in signal:
                return 2.0
            elif "Correction" in signal:
                return 0.5  # 調整待ちは弱い買いシグナル
            elif "Down" in signal:
                return -2.0
        elif signal_type == 'sentiment':
            if signal == "強気":
                return 2.0
            elif signal == "やや強気":
                return 1.0
            elif signal == "中立":
                return 0.0
            elif signal == "やや弱気":
                return -1.0
            elif signal == "弱気":
                return -2.0
        return 0.0

    # スコア計算
    technical_score = signal_to_score(tech_data['signal'], 'technical')
    elliott_score = signal_to_score(elliott_data['direction'], 'elliott')
    sentiment_score = signal_to_score(sent_data['sentiment'], 'sentiment')

    # 重み付けスコア
    weighted_score = (
        technical_score * AGENT_WEIGHTS['technical'] +
        elliott_score * AGENT_WEIGHTS['elliott'] +
        sentiment_score * AGENT_WEIGHTS['sentiment']
    )

    # 総重み
    total_weight = sum(AGENT_WEIGHTS.values())

    # 正規化スコア（-1.0 ~ +1.0）
    normalized_score = weighted_score / (total_weight * 2.0)

    # 総合シグナル判定
    if normalized_score > 0.4:
        overall_signal = "買い"
        overall_confidence = min(100, int(normalized_score * 100 + 50))
    elif normalized_score > 0.1:
        overall_signal = "やや買い"
        overall_confidence = min(100, int(normalized_score * 80 + 40))
    elif normalized_score < -0.4:
        overall_signal = "売り"
        overall_confidence = min(100, int(abs(normalized_score) * 100 + 50))
    elif normalized_score < -0.1:
        overall_signal = "やや売り"
        overall_confidence = min(100, int(abs(normalized_score) * 80 + 40))
    else:
        overall_signal = "中立"
        overall_confidence = 50

    agent_scores = {
        'technical': {
            'signal': tech_data['signal'],
            'confidence': tech_data['confidence'],
            'weight': AGENT_WEIGHTS['technical'],
            'score': technical_score * AGENT_WEIGHTS['technical']
        },
        'elliott': {
            'signal': elliott_data['direction'],
            'confidence': elliott_data['confidence'],
            'weight': AGENT_WEIGHTS['elliott'],
            'score': elliott_score * AGENT_WEIGHTS['elliott']
        },
        'sentiment': {
            'signal': sent_data['sentiment'],
            'confidence': sent_data['confidence'],
            'weight': AGENT_WEIGHTS['sentiment'],
            'score': sentiment_score * AGENT_WEIGHTS['sentiment']
        }
    }

    print(f"   テクニカルスコア: {technical_score * AGENT_WEIGHTS['technical']:.2f}")
    print(f"   エリオットスコア: {elliott_score * AGENT_WEIGHTS['elliott']:.2f}")
    print(f"   センチメントスコア: {sentiment_score * AGENT_WEIGHTS['sentiment']:.2f}")
    print(f"   総合スコア: {weighted_score:.2f} / {total_weight * 2.0:.2f}")
    print(f"   正規化スコア: {normalized_score:.3f}")
    print(f"   統合判定: {overall_signal}（信頼度{overall_confidence}%）")
    print()

    # ============================================
    # STEP 3: 価格目標統合
    # ============================================
    print("3️⃣  価格目標統合中...")

    if overall_signal in ["買い", "やや買い"]:
        # エントリー価格の加重平均
        tech_entry = tech_pricing['entry']
        elliott_entry = (elliott_trade['entry_range'][0] + elliott_trade['entry_range'][1]) / 2 if elliott_trade['entry_range'] else tech_entry

        weighted_entry = (
            tech_entry * AGENT_WEIGHTS['technical'] +
            elliott_entry * AGENT_WEIGHTS['elliott']
        ) / (AGENT_WEIGHTS['technical'] + AGENT_WEIGHTS['elliott'])

        # 目標価格（最も保守的な値を採用）
        targets = [tech_pricing['exit'], elliott_trade['target']] if elliott_trade['target'] else [tech_pricing['exit']]
        target_price = min(targets)

        # ストップロス（最も近い値を採用 = リスク最小化）
        stops = [tech_pricing['stop_loss'], elliott_trade['stop_loss']] if elliott_trade['stop_loss'] else [tech_pricing['stop_loss']]
        stop_loss = max(stops)  # エントリーから最も近い

    elif overall_signal in ["売り", "やや売り"]:
        # 売りシグナル（ショート）
        weighted_entry = tech_entry
        target_price = max(targets) if targets else None
        stop_loss = min(stops) if stops else None

    else:
        # 中立シグナル（トレード非推奨）
        weighted_entry = None
        target_price = None
        stop_loss = None

    if weighted_entry and target_price and stop_loss:
        print(f"   エントリー価格: {weighted_entry:,.2f}円")
        print(f"   目標価格: {target_price:,.2f}円")
        print(f"   ストップロス: {stop_loss:,.2f}円")
    else:
        print("   ⚠️ 中立シグナル、価格目標なし")

    print()

    # ============================================
    # STEP 4: リスク・リワード比率算出
    # ============================================
    print("4️⃣  リスク・リワード比率算出中...")

    if weighted_entry and target_price and stop_loss:
        # リスク（損失幅）
        risk = abs(weighted_entry - stop_loss)

        # リワード（利益幅）
        reward = abs(target_price - weighted_entry)

        # リスク・リワード比率
        risk_reward_ratio = reward / risk if risk > 0 else 0

        # 期待リターン（%）
        expected_return = ((target_price - weighted_entry) / weighted_entry) * 100

        # 最大リスク（%）
        max_risk = ((weighted_entry - stop_loss) / weighted_entry) * 100

        # 期待値（勝率を仮定）
        win_rate = overall_confidence / 100
        lose_rate = 1 - win_rate

        expected_value = (win_rate * expected_return) + (lose_rate * (-max_risk))

        print(f"   リスク幅: {risk:,.2f}円（{max_risk:.2f}%）")
        print(f"   リワード幅: {reward:,.2f}円（{expected_return:.2f}%）")
        print(f"   R:R比率: 1:{risk_reward_ratio:.2f}")
        print(f"   期待値: {expected_value:+.2f}%")
    else:
        risk_reward_ratio = None
        expected_return = None
        max_risk = None
        expected_value = None
        print("   ⚠️ リスク・リワード比率計算不可")

    print()

    # ============================================
    # STEP 5: 実行可能性評価
    # ============================================
    print("5️⃣  実行可能性評価中...")

    # 市場流動性評価
    liquidity_score = "高"
    liquidity_note = "日経平均先物は24時間取引可能、出来高も十分"

    # ボラティリティ評価
    atr_pct = technical['indicators']['atr']['volatility_pct']

    if atr_pct > 3:
        volatility_level = "高"
        volatility_note = "高ボラティリティ、スリッページリスク大"
    elif atr_pct > 2:
        volatility_level = "中"
        volatility_note = "通常のボラティリティ、実行可能"
    else:
        volatility_level = "低"
        volatility_note = "低ボラティリティ、スプレッド小"

    # 実行難易度
    if risk_reward_ratio and risk_reward_ratio > 1.5:
        execution_difficulty = "低"
        execution_note = "明確なエントリー/エグジットポイント、実行容易"
    elif risk_reward_ratio and risk_reward_ratio > 1.0:
        execution_difficulty = "中"
        execution_note = "実行可能だが、タイミング重要"
    else:
        execution_difficulty = "高"
        execution_note = "リスク・リワード比率不利、実行非推奨"

    # 総合実行可能性
    if liquidity_score == "高" and volatility_level in ["低", "中"] and execution_difficulty in ["低", "中"]:
        overall_feasibility = "高"
    else:
        overall_feasibility = "中"

    print(f"   市場流動性: {liquidity_score}")
    print(f"   ボラティリティ: {volatility_level}（ATR {atr_pct:.2f}%）")
    print(f"   実行難易度: {execution_difficulty}")
    print(f"   総合実行可能性: {overall_feasibility}")
    print()

    # ============================================
    # JSON保存
    # ============================================
    output_data = {
        'timestamp': datetime.now().isoformat(),
        'overall': {
            'signal': overall_signal,
            'confidence': overall_confidence,
            'normalized_score': round(normalized_score, 3)
        },
        'agent_scores': agent_scores,
        'pricing': {
            'entry': round(weighted_entry, 2) if weighted_entry else None,
            'target': round(target_price, 2) if target_price else None,
            'stop_loss': round(stop_loss, 2) if stop_loss else None
        },
        'risk_reward': {
            'ratio': round(risk_reward_ratio, 2) if risk_reward_ratio else None,
            'expected_return': round(expected_return, 2) if expected_return else None,
            'max_risk': round(max_risk, 2) if max_risk else None,
            'expected_value': round(expected_value, 2) if expected_value else None
        },
        'feasibility': {
            'liquidity': liquidity_score,
            'volatility': volatility_level,
            'execution_difficulty': execution_difficulty,
            'overall': overall_feasibility
        }
    }

    output_file = 'data/results/2026-01-02/synthesized_strategy.json'
    import os
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"✅ 戦略統合完了")
    print(f"   出力ファイル: {output_file}")

    return output_data

if __name__ == "__main__":
    strategy_synthesizer()
