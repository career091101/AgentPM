---
id: "FRAMEWORK_AARRR_001"
title: "AARRR (Pirate Metrics)"
title_ja: "AARRR（海賊指標）"
category: "framework"
type: "framework"
source_book: "起業の科学"
chapter: "STEP 4"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"

tags:
  stage:
    - pmf
    - scale
  concepts:
    - aarrr
    - pirate_metrics
    - growth_metrics
    - funnel_analysis
  related_frameworks:
    - pmf
    - balance_scorecard
  disciplines:
    - growth_hacking
    - analytics

framework:
  components_count: 5
  metrics:
    - name: "Acquisition (獲得)"
      description: "どうやって顧客を獲得するか"
    - name: "Activation (活性化)"
      description: "初回体験は良いか"
    - name: "Retention (継続)"
      description: "顧客は戻ってくるか"
    - name: "Referral (紹介)"
      description: "顧客が他人に勧めるか"
    - name: "Revenue (収益)"
      description: "どうやって儲けるか"
  priority_order: "Retention → Activation → Acquisition → Revenue → Referral"

dependencies:
  requires:
    - CONCEPT_PMF_001
  enables:
    - CONCEPT_SCALE_001

skills:
  applicable:
    - growth_analysis
    - funnel_optimization
  triggers:
    - "AARRR分析"
    - "海賊指標"
    - "グロース分析"

quality:
  fact_check: "pass"
  sources_count: 3
  last_verified: "2025-12-28"

priority: "high"
---

# AARRR (Pirate Metrics)

> **出典**: 田所雅之「起業の科学」STEP 4、Dave McClure "Startup Metrics for Pirates"
> **関連**: [[CONCEPT_PMF_001]], [[FRAMEWORK_BALANCE_SCORECARD_001]]

---

## 1. 定義

**AARRR (Pirate Metrics)** は、スタートアップの成長を測定・最適化する5つの指標フレームワーク。

**5つのステージ**:
1. **Acquisition (獲得)**: どうやって顧客を獲得するか
2. **Activation (活性化)**: 初回体験は良いか
3. **Retention (継続)**: 顧客は戻ってくるか
4. **Referral (紹介)**: 顧客が他人に勧めるか
5. **Revenue (収益)**: どうやって儲けるか

**由来**: A-A-R-R-R → 海賊の「アー！」に似ている → Pirate Metrics

**重要な原則**:
> "Focus on Retention first, not Acquisition."
> （獲得ではなく、継続を最優先せよ）

---

## 2. なぜ重要か

### 2.1 Vanity Metrics（虚栄の指標）の罠

**よくある間違い**:
- ダウンロード数1万達成！🎉
- → でもDAU（デイリーアクティブユーザー）は100人
- → 99%が使っていない

**Vanity Metricsの例**:
- ❌ ダウンロード数（使われているとは限らない）
- ❌ PV（ページビュー）（価値を生んでいるか不明）
- ❌ 登録ユーザー数（アクティブユーザーか不明）

**AARRRの効果**:
- ✅ ファネル全体を可視化
- ✅ ボトルネックを特定
- ✅ 実際の成長を測定

---

### 2.2 最適化の優先順位

**間違った優先順位**:
1. Acquisition（獲得）→ 広告費投入
2. → でもRetention（継続）が低い
3. → 穴の空いたバケツに水を注ぐ

**正しい優先順位**:
1. **Retention（継続）**: 顧客が戻ってくるか
2. **Activation（活性化）**: 初回体験を改善
3. **Acquisition（獲得）**: 集客を増やす
4. **Revenue（収益）**: マネタイズ
5. **Referral（紹介）**: 口コミ

**理由**: Retention低い状態でAcquisition増やしても無駄

---

## 3. 5つの指標の詳細

### 3.1 Acquisition (獲得)

**定義**: どうやって顧客を獲得するか

**主要指標**:

| 指標 | 計算式 | 目標値 |
|------|--------|--------|
| **Traffic（訪問数）** | ユニークビジター数 | - |
| **CAC（顧客獲得コスト）** | マーケ費用 ÷ 新規顧客数 | <LTV/3 |
| **CVR（コンバージョン率）** | 登録数 ÷ 訪問数 | 2-5% |
| **チャネル別CVR** | チャネルごとのCVR | - |

**チャネル別測定**:

| チャネル | CVR | CAC | 特徴 |
|----------|-----|-----|------|
| **Organic（SEO）** | 3-5% | $10-50 | 長期資産 |
| **Paid（広告）** | 1-3% | $50-200 | スケール可 |
| **Referral（紹介）** | 5-10% | $0-20 | 最高品質 |
| **Social（SNS）** | 1-2% | $20-100 | ブランド構築 |

**改善施策**:
- SEO最適化（キーワード、コンテンツ）
- ランディングページA/Bテスト
- 紹介プログラム（Referral獲得も兼ねる）

---

### 3.2 Activation (活性化)

**定義**: 初回体験で価値を感じたか

**主要指標**:

| 指標 | 計算式 | 目標値 |
|------|--------|--------|
| **Aha Moment到達率** | 価値体験ユーザー ÷ 登録ユーザー | 40%+ |
| **Time to Value** | 登録 → 価値体験までの時間 | 短いほど良い |
| **Onboarding完了率** | チュートリアル完了 ÷ 登録 | 60%+ |

**Aha Momentの定義例**:

| プロダクト | Aha Moment |
|-----------|------------|
| **Facebook** | 10日以内に7人の友達追加 |
| **Slack** | チーム内で2,000メッセージ送信 |
| **Dropbox** | 1つのファイルをフォルダに保存 |
| **Twitter** | 30人フォロー |

**計測方法**:
1. 価値体験アクションを定義
2. ユーザー行動ログ分析
3. Aha Moment到達ユーザーのRetention測定
4. 未到達ユーザーと比較

**改善施策**:
- オンボーディングフロー改善
- チュートリアル動画追加
- パーソナライズされた初期設定

---

### 3.3 Retention (継続)

**定義**: 顧客が戻ってくるか

**最重要指標**:

| 指標 | 計算式 | 目標値 |
|------|--------|--------|
| **Day 1 Retention** | D1アクティブ ÷ 登録 | 40%+ |
| **Day 7 Retention** | D7アクティブ ÷ 登録 | 20%+ |
| **Day 30 Retention** | D30アクティブ ÷ 登録 | 10%+ |
| **Cohort Retention** | コホート別の継続率 | フラット化 |

参照: [[CONCEPT_RETENTION_001]]

**Retention Curve（継続率曲線）**:

```
100% │●
     │  ●
 50% │    ●
     │      ●___●___●___  ← Good (フラット化)
     │
     │    ●
     │  ●
  0% │●                   ← Bad (ゼロに向かう)
     └─────────────────────
      D1  D7  D14  D30
```

**Good Retention**:
- 初期は下がるが、ある時点でフラット化
- → コアユーザーが定着

**Bad Retention**:
- ずっと下がり続ける
- → PMF未達成

**改善施策**:
- プッシュ通知（リエンゲージメント）
- メール自動化（ドリップキャンペーン）
- 機能改善（離脱理由分析）

---

### 3.4 Referral (紹介)

**定義**: 顧客が他人に勧めるか

**主要指標**:

| 指標 | 計算式 | 目標値 |
|------|--------|--------|
| **K-factor（バイラル係数）** | (招待数) × (受諾率) | 1.0+ |
| **NPS** | 推奨者% - 批判者% | 50+ |
| **紹介率** | 紹介経由ユーザー ÷ 全ユーザー | 20%+ |

参照: [[CONCEPT_NPS_001]]

**K-factor計算例**:
```
1ユーザーが平均5人招待
招待受諾率20%
→ K-factor = 5 × 0.2 = 1.0

K > 1.0: バイラル成長（指数関数的）
K = 0.5-1.0: 健全な成長
K < 0.5: 紹介不足
```

**Referral Programの例**:

| プロダクト | インセンティブ | 結果 |
|-----------|---------------|------|
| **Dropbox** | 紹介で500MB無料 | ユーザー数3900%増 |
| **Uber** | 紹介で$10クーポン | 初期成長の主要ドライバー |
| **PayPal** | 紹介で$10 | 月7-10%成長 |

**改善施策**:
- 紹介プログラム導入
- シェアボタン設置
- NPS調査→改善

---

### 3.5 Revenue (収益)

**定義**: どうやって儲けるか

**主要指標**:

| 指標 | 計算式 | 目標値 |
|------|--------|--------|
| **ARPU** | 総収益 ÷ ユーザー数 | - |
| **LTV** | ARPU ÷ Churn Rate | >CAC×3 |
| **LTV/CAC** | LTV ÷ CAC | 3.0+ |
| **Payback Period** | CAC ÷ (ARPU/月) | <12ヶ月 |

**収益モデル別**:

| モデル | 主要指標 | 目標 |
|--------|---------|------|
| **SaaS** | MRR成長率 | 10%+/月 |
| **Eコマース** | AOV（平均注文額） | - |
| **広告** | eCPM | - |
| **マーケットプレイス** | GMV（流通総額） | - |

**改善施策**:
- アップセル・クロスセル
- プライシング最適化
- 上位プラン追加

---

## 4. AARRRファネル分析

### 4.1 ファネル可視化

```
1000人  ┃ Acquisition (獲得)
        ┃
        ↓ CVR 3%
  30人  ┃ Activation (活性化)
        ┃
        ↓ Aha Moment 40%
  12人  ┃ Retention (継続)
        ┃
        ↓ D30 Retention 50%
   6人  ┃ Referral (紹介)
        ┃
        ↓ K-factor 0.5
   3人  ┃ Revenue (収益)
```

**ボトルネック特定**:
- CVR 3% → 業界平均5% → **要改善**
- Aha Moment 40% → **ボトルネック**
- その他は健全

**優先順位**: Activationを最優先で改善

---

### 4.2 コホート分析

**コホート定義**: 同じ時期に登録したユーザーグループ

| コホート | D1 | D7 | D30 | 改善 |
|---------|----|----|-----|------|
| 2025/01 | 40% | 20% | 10% | - |
| 2025/02 | 45% | 25% | 15% | ✅ +5% |
| 2025/03 | 50% | 30% | 20% | ✅ +5% |

**分析**:
- コホートごとにRetention改善
- → プロダクト改善の効果が見える

---

## 5. ステージ別AARRR戦略

### 5.1 CPF/PSF段階（PMF前）

**優先順位**:
1. **Retention**: まず使い続けてもらう
2. **Activation**: 初回体験を磨く
3. Acquisition: 最小限（友人・知人のみ）

**KPI**:
- Retention: D7 20%+
- Activation: Aha Moment 40%+

### 5.2 PMF段階

**優先順位**:
1. **Retention**: フラット化確認
2. **Referral**: 口コミ発生
3. **Acquisition**: Organic成長

**KPI**:
- Retention: D30フラット
- NPS: 50+
- K-factor: 0.5+

### 5.3 スケール段階

**優先順位**:
1. **Acquisition**: スケール投資
2. **Revenue**: マネタイズ最適化
3. Referral: プログラム強化

**KPI**:
- CAC: LTV/3以下
- LTV/CAC: 3.0+
- K-factor: 1.0+

---

## 6. よくある間違い

| 間違い | 症状 | 対策 |
|--------|------|------|
| **Acquisition優先** | Retention低いまま広告投下 | Retention優先 |
| **全指標同時改善** | リソース分散 | ボトルネック1つに集中 |
| **測定のみ** | 数字見て終わり | 改善アクション必須 |
| **短期視点** | 週次で一喜一憂 | 月次・コホート分析 |

---

## 7. 事例

### 7.1 成功事例: Dropbox

| ステージ | 施策 | 結果 |
|---------|------|------|
| **Acquisition** | Explainer Video | ウェイトリスト7万人 |
| **Activation** | シンプルなD&D | Aha Moment到達率60% |
| **Retention** | ファイル同期が必須に | D30 Retention 40% |
| **Referral** | 紹介で500MB | K-factor 1.5（バイラル） |
| **Revenue** | フリーミアム | 4%が有料転換 |

**結果**: 2008-2010年で400万→2500万ユーザー

---

### 7.2 失敗から学ぶ: 某SNSアプリ

| ステージ | 状況 | 問題 |
|---------|------|------|
| **Acquisition** | 広告で100万DL | ✅ OK |
| **Activation** | Aha Moment 10% | ❌ ボトルネック |
| **Retention** | D7 5% | ❌ 穴の空いたバケツ |
| **Referral** | K-factor 0.1 | ❌ 口コミなし |
| **Revenue** | マネタイズ未実装 | - |

**失敗理由**:
- Retention低いままAcquisition投資
- 広告費だけ消費、成長せず
- 1年で終了

---

## 8. AARRRダッシュボード例

```markdown
# AARRR Dashboard (2025年3月)

## Acquisition (獲得)
- Traffic: 10,000 UV
- 登録数: 300人 (CVR 3%)
- CAC: $50

## Activation (活性化)
- Aha Moment到達: 120人 (40%)
- Onboarding完了: 180人 (60%)

## Retention (継続)
- D1: 40% (120人)
- D7: 25% (75人)
- D30: 15% (45人)

## Referral (紹介)
- NPS: 55
- K-factor: 0.6
- 紹介経由: 50人 (17%)

## Revenue (収益)
- MRR: $5,000
- ARPU: $50/月
- LTV/CAC: 2.5 (要改善)

## ボトルネック
🚨 **Activation (40%)** が最大のボトルネック
→ 優先施策: オンボーディング改善
```

---

## 9. 関連概念

| 概念 | 関係性 | リンク |
|------|--------|--------|
| PMF | AARRRでPMF測定 | [[CONCEPT_PMF_001]] |
| Retention | AARRRのR | [[CONCEPT_RETENTION_001]] |
| NPS | ReferralのR | [[CONCEPT_NPS_001]] |
| Balance Scorecard | 顧客視点と重複 | [[FRAMEWORK_BALANCE_SCORECARD_001]] |

---

## クイックリファレンス

```
定義: スタートアップ成長を測定・最適化する5指標
目的: ファネル全体の可視化、ボトルネック特定
所要時間: 初回3-5日（計測設定）、レビュー1時間/週

5つのステージ:
1. Acquisition (獲得): CAC, CVR
2. Activation (活性化): Aha Moment到達率
3. Retention (継続): D1/D7/D30 Retention
4. Referral (紹介): K-factor, NPS
5. Revenue (収益): LTV/CAC

最適化の優先順位:
1. Retention（継続）← 最優先
2. Activation（活性化）
3. Acquisition（獲得）
4. Revenue（収益）
5. Referral（紹介）

重要な原則:
「Retentionを優先せよ。穴の空いたバケツに水を注ぐな」
```

---

**ファイル情報**
- 作成日: 2025-12-28
- 最終更新: 2025-12-28
- バージョン: 1.0
