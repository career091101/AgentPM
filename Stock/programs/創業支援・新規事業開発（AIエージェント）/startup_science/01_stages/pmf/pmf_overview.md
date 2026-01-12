---
id: "CONCEPT_PMF_001"
title: "Product Market Fit (PMF)"
title_ja: "プロダクトマーケットフィット"
category: "stage"
type: "concept"
source_book: "起業の科学"
chapter: "STEP 4"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"

tags:
  stage:
    - pmf
  concepts:
    - product_market_fit
    - market_validation
    - customer_traction
  related_frameworks:
    - sean_ellis_test
    - nps
    - retention_curve
    - aarrr
  disciplines:
    - lean_startup
    - customer_development

dependencies:
  requires:
    - CONCEPT_PSF_001
    - CONCEPT_CPF_001
  enables:
    - CONCEPT_SCALE_001
    - FRAMEWORK_UNITECO_001

skills:
  applicable:
    - startup_validation
    - pmf_check
    - investor_pitch
  triggers:
    - "PMF達成判定"
    - "PMFチェック"
    - "PMF検証"
    - "プロダクトマーケットフィット"

quality:
  fact_check: "pass"
  sources_count: 3
  last_verified: "2025-12-28"

priority: "critical"
---

# Product Market Fit (PMF)

> **出典**: 田所雅之「起業の科学」STEP 4
> **関連概念**: [[CONCEPT_CPF_001]], [[CONCEPT_PSF_001]], [[CONCEPT_SCALE_001]]

---

## 1. 定義

**Product Market Fit (PMF)** とは、「顧客が本当に欲しがるプロダクトを作れた状態」を指す。

Marc Andreessen の定義:
> "Product/market fit means being in a good market with a product that can satisfy that market."

PMFを達成すると、以下の現象が起こる：
- 顧客が熱狂し、自動的に口コミが広がる
- プロダクトが「引っ張られる (Pull)」感覚
- 成長が加速し始める

## 2. なぜ重要か

スタートアップ最大の失敗原因は「市場にニーズがなかった」（42%）。PMFの未達成がこの原因の根幹。

**PMF前とPMF後の違い**:

| 観点 | PMF前 | PMF後 |
|------|-------|-------|
| 成長 | プッシュ型（営業で無理やり売る） | プル型（顧客が勝手に来る） |
| 口コミ | 起きない | 自然発生的に起きる |
| チャーン率 | 高い（5%以上/月） | 低い（5%以下/月） |
| 資金調達 | 困難 | 容易になる |

## 3. 構成要素: PMFパルテノン神殿

PMFは一気に達成されるものではなく、段階的に積み上げていく：

```
        ┌─────────────────────────────────┐
        │    真のPMF (MOAT構築)           │ 屋根
        └─────────────────────────────────┘
        ┌─────────────────────────────────┐
        │  熱狂の再現性・チャネル検証      │ 3階
        └─────────────────────────────────┘
        ┌─────────────────────────────────┐
        │  PSF (Value Proposition検証)    │ 2階
        └─────────────────────────────────┘
        ┌─────────────────────────────────┐
        │  CPF (Customer Problem検証)     │ 1階
        └─────────────────────────────────┘
        ┌─────────────────────────────────┐
        │ Vision / Founder-Issue-Fit      │ 土台
        └─────────────────────────────────┘
```

各階層をスキップせず、順番に積み上げることが重要。

## 4. 判定基準・指標

### 4.1 定量指標

| 指標 | PMF達成基準 | 測定方法 |
|------|-----------|----------|
| **Sean Ellisテスト** | 40%以上が「非常に残念」 | 「このプロダクトが使えなくなったらどう思いますか?」 |
| **月次成長率** | 10%+/月 | MRR成長率を計測 |
| **NPS (Net Promoter Score)** | 50以上 | 推奨度を10段階で測定 |
| **Churn Rate** | 5%以下/月 | 解約率 |
| **LTV/CAC** | 3倍以上 | 顧客生涯価値 ÷ 顧客獲得コスト |
| **リテンション率** | 40%以上 (4週後) | 4週間後の継続率 |

### 4.2 定性指標

- [ ] 顧客が熱狂している（「これがないと困る」という声）
- [ ] 口コミで自然にユーザーが増えている
- [ ] ユーザーが他人に勧めている
- [ ] 競合に乗り換えようとしない
- [ ] ユーザーコミュニティが自発的に形成されている

## 5. 実践ステップ

### PMF達成までのプロセス

1. **ステップ1: CPF達成**
   - 顧客の課題を深く理解する
   - 3U検証（Unsolved/Urgent/Expensive）を行う

2. **ステップ2: PSF達成**
   - 課題に対する適切なソリューションを見つける
   - 10倍改善を実現する

3. **ステップ3: PMF検証**
   - Sean Ellisテストを実施
   - リテンション曲線を分析
   - NPS測定

4. **ステップ4: PMF改善ループ**
   - ユーザーフィードバックを収集
   - プロダクトを磨き込む
   - 指標を継続的にモニタリング

5. **ステップ5: MOAT構築**
   - ネットワーク効果の構築
   - データによる優位性
   - ブランド確立

## 6. よくある失敗パターン

| パターン | 症状 | 対策 |
|---------|------|------|
| **見せかけのPMF** | 営業で無理やり売っているだけ | プッシュなしでも成長するか確認 |
| **早すぎるスケール** | PMF前に大量採用・広告投下 | Sean Ellisテスト40%以上を確認してからスケール |
| **指標の誤解** | ダウンロード数だけ見ている | リテンション・エンゲージメントを重視 |
| **ピボット恐怖症** | PMF未達成なのに同じ方向で努力 | 3ヶ月改善しなければピボット検討 |
| **複数ペルソナ狙い** | 全員に気に入られようとする | 1つのペルソナでPMF達成してから拡大 |

## 7. 事例

### 7.1 成功事例

- **Airbnb**:
  - CPF: 旅行者の宿泊コスト削減ニーズ
  - PSF: 写真品質向上で10倍改善
  - PMF達成: 口コミで成長、リテンション率向上
  - 参照: [[CASE_AIRBNB_001]]

- **Zoom**:
  - CPF: ビデオ会議の品質・使いやすさ課題
  - PSF: ワンクリック参加で10倍簡単に
  - PMF達成: NPS 72、月次成長率20%
  - 参照: [[CASE_ZOOM_001]]

### 7.2 失敗事例

- **セブンドリーマーズ (ランドロイド)**:
  - 技術は凄いがPMF未達成
  - 価格が高すぎて顧客が買わない
  - PMF前に100億円調達し空中分解
  - 参照: [[CASE_SEVEN_DREAMERS_001]]

### 7.3 ソロプレナー事例（関連）

| 人物 | プロダクト | PMF達成方法 | リンク |
|------|----------|-----------|--------|
| Pieter Levels | PhotoAI | Build in Publicで熱狂的ファン獲得 | [[APP_003]] |
| AJ | Carrd | フリーミアムでリテンション40%超 | [[APP_087]] |
| Marc Lou | ShipFast | 開発者向けニッチでNPS高値 | [[APP_085]] |

## 8. 関連概念

| 概念 | 関係性 | リンク |
|------|--------|--------|
| CPF (Customer Problem Fit) | 前提 | [[CONCEPT_CPF_001]] |
| PSF (Problem Solution Fit) | 前提 | [[CONCEPT_PSF_001]] |
| Sean Ellisテスト | PMF測定手法 | [[CONCEPT_SEAN_ELLIS_001]] |
| NPS | 顧客満足度指標 | [[CONCEPT_NPS_001]] |
| リテンション | 継続率指標 | [[CONCEPT_RETENTION_001]] |
| ユニットエコノミクス | PMF後の経済性 | [[CONCEPT_UNITECO_001]] |
| スケール | PMF後のステップ | [[CONCEPT_SCALE_001]] |
| ピボット | PMF未達成時の方向転換 | [[TACTIC_PIVOT_001]] |

---

## クイックリファレンス

```
定義: 顧客が本当に欲しがるプロダクトを作れた状態
判定基準: Sean Ellisテスト40%以上、リテンション率40%以上、NPS 50以上
次のステップ: ユニットエコノミクス確認 → スケール準備
```

---

**ファイル情報**
- 作成日: 2025-12-28
- 最終更新: 2025-12-28
- バージョン: 1.0
