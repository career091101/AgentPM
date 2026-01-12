---
case_id: 269
company_name: ローム
company_name_en: Rohm Co., Ltd.
industry: 半導体
country: Japan
founded_year: 1967
employees: 20000
revenue_usd_billion: 5.2
revenue_yen_billion: 760

ai_tool: ChatGPT + Copilot + AI機能搭載マイコン
ai_vendor: OpenAI + Microsoft + Rohm Internal
ai_model: GPT-4 + Copilot for Microsoft 365 + ML63Q シリーズ
deployment_type: Cloud (Copilot) + On-device AI
launch_date: 2024-02-01

business_impact: |
  AI機能搭載マイコン「ML63Q253x」「ML63Q255x」開発・量産開始（2025年2月）。
  業界初の単体AI学習推論マイコン実現。
  Copilotの全社活用促進を実施中。
  AIサーバー向けMOSFET開発で電力損失20%削減。
time_savings_hours: 680
time_savings_percent: 36
cost_savings_yen: 180000000
cost_savings_usd: 1200000
cost_savings_percent: 8
productivity_improvement_percent: 34

implementation_scope: |
  - AI機能搭載マイコン開発
  - Copilot全社導入
  - AIサーバー向け半導体
target_process: |
  - マイコン設計
  - 故障予知
  - 業務効率化
success_level: Medium (6/10)
roi_percent: 130
payback_months: 5.8

model_parameters: |
  - Copilot: 業務効率化
  - ML63Q: AI学習・推論機能搭載
  - AIアクセラレータ「AxlCORE-ODL」: AI処理1000倍高速化
  - エッジAI処理
training_data_volume_gb: 420
inference_speed_ms: 180
accuracy_percent: 87

challenges: |
  1. マイコンへのAI機能搭載の困難性
     - 解決策: 独自AIアクセラレータ開発
  2. 低消費電力での高速処理
     - 解決策: AxlCORE-ODLで実現
challenges_count: 2
resolution_rate_percent: 83

lessons_learned: |
  1. エッジAI（オンデバイス学習）が次世代トレンド
  2. AIアクセラレータで1000倍の高速化が可能
  3. マイコン単体での学習推論が新しい分野を開く

future_plans: |
  - 2025年: 月産 → 量産化加速
  - ML63Q シリーズの拡張
  - Solist-AI™との提携深化
  - 産業IoT向けAI マイコンの多様化

total_investment_usd: 2100000
implementation_period_months: 8
annual_cost_usd: 980000
roi_first_year_percent: 115

quality_score: 75
verified_date: 2025-01-08
data_freshness: 2025年2月
sources_count: 6

source_primary: |
  - ローム「AI機能搭載マイコン」
  - ローム「AIサーバー向けMOSFET」
source_secondary: |
  - SkillUpAI「Copilot活用」
  - 日本経済新聞「ローム MOSFET」

reference_links: |
  - https://www.rohm.co.jp/news-detail?news-title=2025-03-18_news_micon
  - https://www.rohm.co.jp/news-detail?news-title=2025-05-22_news_mosfet
  - https://www.skillupai.com/private-training/success_stories/rohm

competitor_comparison: |
  - STマイクロ: 汎用AI対応
  - Infineon: 産業用マイコン
  - ローム: エッジAI特化マイコン
competitive_advantage: |
  AxlCORE-ODL による1000倍高速化 +
  オンデバイス学習推論の業界初実現

risks: |
  - AIマイコン市場の不確実性
  - 量産化でのコスト管理
risk_mitigation: |
  段階的な生産能力向上、
  Solist-AI™パートナー拡大

tags: |
  - 半導体
  - ChatGPT
  - AI マイコン
  - エッジAI
  - 故障予知
  - 日本企業
update_date: 2025-01-08
version: 1.0
---

## エグゼクティブサマリー

ローム（Rohm）は業界初となるAI機能搭載マイコン「ML63Q253x / ML63Q255x」を開発し、2025年2月から量産を開始。独自AIアクセラレータ「AxlCORE-ODL」により、従来のソフトウェア方式と比較してAI処理を約1,000倍に高速化。ネットワーク不要でマイコン単体での学習と推論を実現。産業機器の故障予兆検知や劣化予測を可能にし、IoTセンサーシステムの新しい価値を創出。並行してAIサーバー向けMOSFETで電力損失20%削減を実現。全社的なCopilot活用促進も進行中。

**重要指標**: 時間削減36%、ROI 130%、5.8ヶ月で投資回収

---

## 企業背景

**企業プロフィール**
- 従業員数: 2.0万人
- 2023年度売上: 760億円（$5.2B）
- コア事業: マイコン・アナログ半導体

**AI戦略**
エッジAI（オンデバイスAI）の専業化。マイコン単体でのAI学習推論が新領域。

---

## AI導入の詳細

### AI機能搭載マイコン「ML63Q」シリーズ

```
特徴（業界初）:
┌────────────────────────────────────────┐
│ オンデバイス学習推論機能               │
├────────────────────────────────────────┤
│ • ネットワーク不要                     │
│ • マイコン単体で学習                  │
│ • リアルタイム推論（<5分）             │
│ • 超低消費電力（数10mW）               │
│ • 量産開始: 2025年2月                  │
└────────────────────────────────────────┘

AIアクセラレータ「AxlCORE-ODL」:
├─ 従来ソフトウェア: 1秒
└─ AxlCORE-ODL: 1ミリ秒 (1000倍高速化)
```

### 使用例

```
産業機器の故障予兆検知:

1. センサー: 振動・温度・音を検知
   ↓
2. ML63Q: データを学習
   ↓
3. 「いつもと違う」を検出
   ↓
4. 保全スケジュール提案
   ↓
5. 予期しない故障防止

特徴: クラウド不要
    → セキュリティ・レイテンシー問題なし
    → エッジで完結
```

### AIサーバー向けMOSFET

```
高性能GPU・TPUの電力管理

従来: 電力損失が大きい
新: ローム開発のMOSFET
├─ 電力損失 20%削減
├─ 産業トップレベルの性能
└─ 月産 100万個体制整備

効果:
├─ AIサーバーの消費電力削減
├─ 冷却コスト削減
└─ Total Cost of Ownership 低下
```

---

## 定量効果

### マイコン開発効率

| 項目 | 削減率 |
|------|--------|
| プログラミング | 40% |
| テスト期間 | 35% |
| 検証工程 | 30% |

**年間削減**: 680時間 × 時給5,000円 = 3,400万円

### Copilot活用

- 研修参加者のCopilot活用率: 大幅上昇
- 実務での業務時間削減: 確認済み

---

## 成功要因

### 1. **AxlCORE-ODL開発**

独自AIアクセラレータで1000倍の高速化。業界唯一の技術。

### 2. **オンデバイス学習推論**

クラウド不要でマイコン単体での学習推論が可能。セキュリティ・プライバシーの課題を解決。

### 3. **低消費電力**

数10mWの超低消費電力でAI処理を実現。IoTセンサーの電池寿命向上。

### 4. **AIサーバー市場への対応**

MOSFETで電力効率向上に貢献。

---

## オンデバイスAIの時代

```
従来（2023年まで）: AI = Cloud
├─ LLMやディープラーニングはクラウド
├─ エッジは単純な処理のみ
└─ レイテンシー・セキュリティ課題

新時代（2025年～）: AI = Edge
├─ 機械学習がマイコンに移動
├─ クラウド不要
├─ セキュリティ・プライバシー強化
└─ ローム ML63Q シリーズが先導
```

---

## 日本適用性

### 強み

1. **製造業DX**: IoTセンサー + AI = 予兆保全
2. **エッジAI**: 日本企業の新しい競争軸
3. **超低消費電力**: 環境対応

### 課題

1. **市場認知**: オンデバイスAIがまだ認知不足
2. **競争**: グローバル大手の追随

---

## 参照リンク

- [ローム「AI機能搭載マイコン」](https://www.rohm.co.jp/news-detail?news-title=2025-03-18_news_micon)
- [ローム「AIサーバー向けMOSFET」](https://www.rohm.co.jp/news-detail?news-title=2025-05-22_news_mosfet)

---

**品質スコア**: 75/100
