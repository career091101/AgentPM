---
id: "CONCEPT_RETENTION_001"
title: "Retention Analysis (リテンション分析)"
title_ja: "リテンション分析"
category: "tactic"
type: "concept"
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
    - retention
    - churn
    - cohort_analysis
  related_frameworks:
    - pmf
    - aarrr
  disciplines:
    - product_analytics
    - growth

tactic:
  key_metrics:
    - name: "Day 1/7/30 Retention"
      description: "1日後/7日後/30日後の継続率"
    - name: "Cohort Retention"
      description: "コホート別継続率曲線"
    - name: "Churn Rate"
      description: "解約率"
  retention_curve_types:
    - "Smiling Curve (Good)"
    - "Flattening Curve (PMF達成)"
    - "Decaying Curve (Bad)"

dependencies:
  requires:
    - CONCEPT_PMF_001
  enables:
    - CONCEPT_SCALE_001

skills:
  applicable:
    - retention_analysis
    - cohort_analysis
  triggers:
    - "リテンション分析"
    - "継続率分析"

quality:
  fact_check: "pass"
  sources_count: 3
  last_verified: "2025-12-28"

priority: "critical"
---

# Retention Analysis (リテンション分析)

> **出典**: 田所雅之「起業の科学」STEP 4、Brian Balfour "Reforge Growth Series"
> **関連**: [[CONCEPT_PMF_001]], [[FRAMEWORK_AARRR_001]]

---

## 1. 定義

**Retention（リテンション）** は、顧客がプロダクトを使い続ける割合。**PMF達成の最重要指標**。

**Retention Curve（継続率曲線）**:
- 横軸: 経過日数（Day 1, 7, 14, 30...）
- 縦軸: 継続率（%）
- 曲線の形でPMF達成度が分かる

**Brian Balfourの名言**:
> "Retention is the single most important thing for growth."
> （リテンションが成長において最も重要）

---

## 2. なぜ重要か

### 2.1 PMF判定の決定打

**PMF達成の条件**:
- ✅ Retention Curveがフラット化
- ✅ Day 30 Retention 40%以上
- ✅ コホートごとに改善

**PMF未達成のサイン**:
- ❌ Retention Curveが下がり続ける
- ❌ Day 30 Retention 10%未満
- ❌ コホートが改善しない

参照: [[CONCEPT_PMF_001]]

---

### 2.2 成長の前提条件

**穴の空いたバケツの法則**:
```
Retention低い = 穴の空いたバケツ

新規100人獲得 → 90人解約 → 実質+10人
新規100人獲得 → 30人解約 → 実質+70人

Retention改善 = 穴を塞ぐ
```

**データ**:
- Retention 1%改善 = 成長率5%向上
- Retention優先 > Acquisition（獲得）優先

---

## 3. Retention Curveの3パターン

### 3.1 Flattening Curve（PMF達成）

```
100% │●
     │  ●
 50% │    ●
     │      ●___●___●___  ← フラット化！
     │
  0% └─────────────────────
      D1  D7  D14  D30  D60
```

**特徴**:
- 初期は下がるが、ある時点でフラット化
- コアユーザーが定着

**判定**: ✅ PMF達成

**事例**:
- Facebook: 10日で7人友達追加したユーザー
- Slack: 2,000メッセージ送信したチーム

---

### 3.2 Smiling Curve（理想）

```
100% │●
     │  ●
 50% │    ●
     │      ●
     │        ●___●___●___ ← フラット後、微増！
  0% └─────────────────────
      D1  D7  D14  D30  D60
```

**特徴**:
- フラット化後、継続率が上昇
- プロダクトが習慣化・必須化

**判定**: ✅ 超強力なPMF

**事例**:
- WhatsApp: 使えば使うほど友達増える
- LinkedIn: プロフィール充実で価値向上

---

### 3.3 Decaying Curve（PMF未達成）

```
100% │●
     │  ●
 50% │    ●
     │      ●
     │        ●
     │          ●
  0% │            ●        ← ゼロに向かう
     └─────────────────────
      D1  D7  D14  D30  D60
```

**特徴**:
- ずっと下がり続ける
- 最終的にゼロに

**判定**: ❌ PMF未達成

**原因**:
- プロダクトが課題を解決していない
- Aha Momentに到達していない
- 代替品で十分

**対策**: ピボット検討

---

## 4. Retention指標の詳細

### 4.1 Day X Retention

**定義**: 登録からX日後に戻ってきた割合

**計算式**:
```
Day X Retention = (X日後にアクティブなユーザー数) / (登録ユーザー数)
```

**例**:
```
100人登録
- Day 1: 40人アクティブ → D1 Retention 40%
- Day 7: 20人アクティブ → D7 Retention 20%
- Day 30: 10人アクティブ → D30 Retention 10%
```

**目標値（業種別）**:

| 業種 | D1 | D7 | D30 |
|------|----|----|-----|
| **SNS** | 60%+ | 30%+ | 15%+ |
| **SaaS** | 50%+ | 25%+ | 15%+ |
| **Eコマース** | 20%+ | 10%+ | 5%+ |
| **ゲーム** | 40%+ | 20%+ | 10%+ |

---

### 4.2 Cohort Retention

**定義**: 同じ時期に登録したユーザーグループ（コホート）の継続率

**コホート表**:

| コホート | D1 | D7 | D14 | D30 | D60 |
|---------|----|----|-----|-----|-----|
| 2025/01 | 40% | 20% | 15% | 10% | 8% |
| 2025/02 | 45% | 25% | 20% | 15% | 13% |
| 2025/03 | 50% | 30% | 25% | 20% | 18% |

**分析**:
- コホートごとに改善 → ✅ プロダクト改善が効いている
- コホート横ばい → ⚠️ 改善施策が効いていない
- コホート悪化 → ❌ プロダクト劣化

---

### 4.3 Churn Rate（解約率）

**定義**: 一定期間に解約したユーザーの割合

**計算式**:
```
Monthly Churn Rate = (月内解約ユーザー数) / (月初ユーザー数)
```

**目標値**:
- B2C SaaS: 5%以下/月
- B2B SaaS: 2%以下/月（年間20-25%）
- Eコマース: 10%以下/月

**逆数がLTV**:
```
Churn 5%/月 → 平均LT（顧客生涯） = 1/0.05 = 20ヶ月
```

---

## 5. Retention分析プロセス

### ステップ1: データ収集（計測設定）

**必要データ**:
- ユーザーID
- 登録日時
- アクティビティログ（ログイン、機能利用）

**ツール**:
- Mixpanel
- Amplitude
- Google Analytics 4

---

### ステップ2: Retention Curve作成

**手順**:
1. コホート定義（例: 2025/01登録ユーザー）
2. 各日のアクティブ率計算
3. グラフ化

**判定**:
- フラット化している → PMF有望
- 下がり続ける → PMF未達成

---

### ステップ3: セグメント分析

**切り口**:

| セグメント | D30 Retention | インサイト |
|-----------|--------------|----------|
| **Aha Moment到達** | 50% | 価値体験が鍵 |
| **未到達** | 5% | オンボーディング改善必須 |
| **機能A利用** | 60% | 機能Aがキラー機能 |
| **機能A未利用** | 10% | 利用促進が必要 |

---

### ステップ4: 離脱理由分析

**方法**:
1. 解約ユーザーにアンケート
2. カスタマーサポートログ分析
3. ユーザー行動ログ分析（最後の行動は?）

**離脱理由トップ3例**:
1. 使い方が分からない（30%）
2. 価値を感じない（25%）
3. 代替品に乗り換え（20%）

---

## 6. Retention改善施策

### 6.1 Aha Moment到達率向上

**目標**: 登録ユーザーの60%+がAha Momentに到達

**施策**:
- オンボーディングフロー改善
- チュートリアル動画
- パーソナライズされた初期設定

**事例（Facebook）**:
- Aha Moment: 10日で7人友達追加
- 施策: 友達推奨アルゴリズム強化
- 結果: D30 Retention 40% → 50%

参照: [[FRAMEWORK_AARRR_001]]（Activation）

---

### 6.2 リエンゲージメント

**プッシュ通知**:
- タイミング: 3日間ログインなし
- 内容: パーソナライズされた価値提示

**メール自動化（ドリップキャンペーン）**:
```
Day 1: ウェルカムメール
Day 3: 未ログイン → Tips紹介
Day 7: 未利用機能の紹介
Day 14: 成功事例紹介
Day 30: 特別オファー
```

**効果**: D30 Retention +5-10%

---

### 6.3 習慣化

**目標**: プロダクトを日常習慣に組み込む

**Nir Eyal "Hooked Model"**:
1. Trigger（きっかけ）: 通知、メール
2. Action（行動）: アプリ開く
3. Reward（報酬）: 価値体験
4. Investment（投資）: データ蓄積

**事例（Duolingo）**:
- Trigger: 毎日同じ時間にプッシュ通知
- Action: 5分レッスン
- Reward: ストリーク維持、バッジ獲得
- Investment: 学習データ蓄積

**結果**: D30 Retention 50%+

---

## 7. よくある間違い

| 間違い | 症状 | 対策 |
|--------|------|------|
| **Acquisition優先** | Retention低いまま広告投下 | Retention優先 |
| **全体平均のみ** | セグメント分析なし | セグメント別分析 |
| **短期視点** | D7だけ見る | D30, D60も見る |
| **改善しない** | 測定して終わり | 離脱理由分析→改善 |

---

## 8. 事例

### 8.1 成功事例: Slack

**Retention Curve**:
```
100% │●
     │  ●
 50% │    ●
     │      ●___●___●___  ← フラット化
     │
  0% └─────────────────────
      D1  D7  D14  D30
```

**Aha Moment**: 2,000メッセージ送信

**施策**:
- オンボーディング: チーム招待促進
- 習慣化: デスクトップ通知
- 統合: 他ツール連携（Googleドライブ等）

**結果**:
- D30 Retention: 50%+
- 2,000メッセージ到達チーム: 93%がアクティブ

---

### 8.2 失敗から学ぶ: 某ソーシャルゲーム

**Retention Curve**:
```
100% │●
     │  ●
 50% │      ●
     │          ●
  0% │              ●      ← ゼロに向かう
     └─────────────────────
      D1  D7  D14  D30
```

**問題**:
- D1 Retention: 20%（業界平均40%）
- D30 Retention: 2%

**原因**:
- チュートリアル長すぎる（30分）
- Aha Moment不明確
- 課金圧力強すぎる

**結果**: 1年でサービス終了

---

## 9. Retention改善ロードマップ

### 月1: 現状把握
- [ ] Retention Curve作成
- [ ] コホート分析
- [ ] セグメント分析
- [ ] 離脱理由調査

### 月2: Aha Moment最適化
- [ ] Aha Moment定義
- [ ] 到達率測定
- [ ] オンボーディング改善
- [ ] A/Bテスト

### 月3: リエンゲージメント
- [ ] プッシュ通知設計
- [ ] メール自動化
- [ ] A/Bテスト

### 月4-6: 習慣化
- [ ] デイリーアクティブ施策
- [ ] ストリーク機能追加
- [ ] ソーシャル要素追加

**目標**: D30 Retention 40%達成

---

## 10. ツール

| ツール | 用途 | 価格 |
|--------|------|------|
| **Mixpanel** | Retention分析 | $25/月〜 |
| **Amplitude** | コホート分析 | $49/月〜 |
| **Google Analytics 4** | 基本分析 | 無料 |
| **Heap** | 自動イベント収集 | $3,600/年〜 |

---

## 11. 関連概念

| 概念 | 関係性 | リンク |
|------|--------|--------|
| PMF | Retention = PMF測定指標 | [[CONCEPT_PMF_001]] |
| AARRR | RetentionのR | [[FRAMEWORK_AARRR_001]] |
| NPS | Retentionと相関 | [[CONCEPT_NPS_001]] |
| Churn | Retentionの逆 | - |

---

## クイックリファレンス

```
定義: 顧客がプロダクトを使い続ける割合
重要性: PMF達成の最重要指標
測定: Day 1/7/30 Retention, Cohort Retention

目標値:
- D1 Retention: 40%+
- D7 Retention: 20%+
- D30 Retention: 10%+ (PMFには40%+)

Retention Curveの3パターン:
1. Flattening（フラット化）→ PMF達成
2. Smiling（フラット後上昇）→ 超強力
3. Decaying（下がり続ける）→ PMF未達成

改善優先順位:
1. Aha Moment到達率向上
2. リエンゲージメント
3. 習慣化

重要な原則:
「Retention優先 > Acquisition優先」
「穴の空いたバケツに水を注ぐな」
```

---

**ファイル情報**
- 作成日: 2025-12-28
- 最終更新: 2025-12-28
- バージョン: 1.0
