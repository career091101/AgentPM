# AARRR Analysis Skill

AARRR（Pirate Metrics）指標分析とボトルネック特定。

---

## Skill情報

- **コマンド**: `/apply-aarrr-analysis`
- **目的**: 成長ファネルのボトルネック特定
- **所要時間**: 30分

---

## プロンプト

### セッション開始

```markdown
# AARRR分析セッション

AARRR（Pirate Metrics）の各指標を測定し、ボトルネックを特定します。

## AARRRとは？

成長を測定する5段階指標:
1. Acquisition（獲得）
2. Activation（活性化）
3. Retention（継続）
4. Referral（紹介）
5. Revenue（収益）

**重要**: 優先順位は **Retention > Activation > Acquisition**

---

## 現状データを教えてください

### Acquisition（獲得）
- 月間新規ユーザー数: [X]人
- 主要チャネル: [SEO / SNS / 広告 / etc]
- CAC（顧客獲得コスト）: $[X]

### Activation（活性化）
- Aha Moment定義: [例: 初の10件タスク作成]
- Aha Moment到達率: [X]%
- オンボーディング完了率: [X]%

### Retention（継続）
- D1 Retention: [X]%
- D7 Retention: [X]%
- D30 Retention: [X]%
- Churn率（月次）: [X]%

### Referral（紹介）
- 紹介プログラム: [あり / なし]
- バイラル係数（K-factor）: [X]
- 紹介経由ユーザー率: [X]%

### Revenue（収益）
- ARPU（月額単価）: $[X]
- 有料転換率: [X]%
- LTV: $[X]
```

---

### データ分析

```markdown
## AARRR分析結果

### 1. Acquisition（獲得）

**実績**:
- 月間新規: [X]人
- CAC: $[Y]

**判定**:
- [OK / 改善必要]

**ベンチマーク**:
- B2B SaaS: CAC $500-3,000

---

### 2. Activation（活性化）

**実績**:
- Aha Moment到達率: [X]%

**判定**:
- 60%+: ✅ 優秀
- 40-59%: ⚠️ 改善余地
- <40%: ❌ 要改善

**あなたの判定**: [判定]

---

### 3. Retention（継続）

**実績**:
- D30 Retention: [X]%

**Retention Curve**: [Flattening / Smiling / Decaying]

**判定**:
- 40%+: ✅ PMF達成
- 20-39%: ⚠️ PMF途中
- <20%: ❌ PMF未達成

**あなたの判定**: [判定]

---

### 4. Referral（紹介）

**実績**:
- バイラル係数: [X]

**判定**:
- 1.0+: ✅ 指数関数的成長
- 0.5-0.9: ⚠️ 成長寄与あり
- <0.5: ❌ 紹介機能不足

**あなたの判定**: [判定]

---

### 5. Revenue（収益）

**実績**:
- ARPU: $[X]
- LTV/CAC: [Y]

**判定**:
- LTV/CAC 3.0+: ✅ 健全
- 1.0-3.0: ⚠️ 要改善
- <1.0: ❌ 赤字

**あなたの判定**: [判定]

---

## ボトルネック特定

最も改善が必要な指標: **[X]**

理由: [なぜこれが最大のボトルネックか]

---

## 優先順位付け

### 優先度1: [最重要指標]
- 現状: [データ]
- 目標: [目標値]
- Gap: [差分]

### 優先度2: [次点]
...

### 優先度3: [その次]
...
```

---

### 改善アクションプラン

```markdown
## 改善アクションプラン

### [Retentionがボトルネックの場合]

#### 施策
1. Aha Moment到達率向上（最優先）
2. リエンゲージメント（プッシュ通知、メール）
3. 習慣化施策

詳細: @startup_science/03_tactics/retention/retention_analysis.md

#### Tomorrow Action
- [ ] Aha Moment定義・測定
- [ ] オンボーディング改善3案
- [ ] リエンゲージメントメール設計

---

### [Activationがボトルネックの場合]

#### 施策
1. オンボーディングフロー改善
2. チュートリアル動画作成
3. パーソナライズ

#### Tomorrow Action
- [ ] オンボーディング離脱ポイント特定
- [ ] チュートリアル設計
- [ ] A/Bテスト計画

---

### [Acquisitionがボトルネックの場合]

⚠️ **注意**: Acquisition改善は、Retention解決後に実施すべき

理由: 「穴の空いたバケツに水を注ぐな」

まずRetention改善 → 次にAcquisition拡大

---

## 継続測定

### ダッシュボード設定
- [ ] AARRRダッシュボード作成（Googleスプレッドシート）
- [ ] 週次更新ルール化
- [ ] 月次レビューMTG設定

### ツール
- Mixpanel, Amplitude, Google Analytics 4

詳細: @startup_science/02_frameworks/aarrr/aarrr_overview.md
```

---

## Knowledge Base参照

- AARRR: `@startup_science/02_frameworks/aarrr/aarrr_overview.md`
- Retention: `@startup_science/03_tactics/retention/retention_analysis.md`
- Unit Economics: `@startup_science/03_tactics/unit_economics/unit_eco_overview.md`

---

## 更新履歴

- 2025-12-28: 初版作成
