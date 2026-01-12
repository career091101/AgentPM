# PMF Stage Validation Skill

PMF（Product Market Fit）達成度診断。

---

## Skill情報

- **コマンド**: `/validate-pmf`
- **目的**: PMF達成度の定量診断
- **所要時間**: 30-40分

---

## このSkillでできること

1. **PMF 3指標判定**: Sean Ellis・NPS・Retention
2. **Unit Economics診断**: LTV/CAC比率、Payback Period
3. **Scale判断**: スケール投資の可否判定
4. **Next Action**: Scaleへ進むか、PMF強化か判断

---

## プロンプト

### セッション開始

```markdown
# PMF達成度診断

PMF（Product Market Fit）の達成度を診断します。

## PMFとは？

プロダクトが市場にフィットし、顧客が手放せなくなった状態。

**判定基準（Parthenon神殿の3本柱）**:
1. Sean Ellisテスト: 40%+
2. NPS: 50+
3. D30 Retention: 40%+

---

## 現状を教えてください

### 0. 前提確認
- PSF達成済みですか？
- 総ユーザー数: [X]人（目標100+）
- 運用期間: [X]ヶ月

### 1. Sean Ellisテスト
「もしこのプロダクトが使えなくなったら、どう感じますか？」
- とても残念: [X]人
- まあ残念: [Y]人
- 残念ではない: [Z]人
- もう使っていない: [W]人

### 2. NPS
「このプロダクトを友人・同僚に勧める可能性は？」（0-10点）
- 9-10点（推奨者）: [X]人
- 7-8点（中立者）: [Y]人
- 0-6点（批判者）: [Z]人

### 3. Retention
- Day 1 Retention: [X]%
- Day 7 Retention: [X]%
- Day 30 Retention: [X]%

### 4. Unit Economics
- ARPU（月額単価）: $[X]
- Churn率（月次）: [X]%
- CAC（顧客獲得コスト）: $[X]
- Gross Margin: [X]%
```

---

### データ収集後 → 診断

```markdown
## PMF診断結果

### 前提チェック
- PSF達成: [OK / 未達]
- ユーザー数: [X]人 → [OK（100+） / 不足]
- 運用期間: [X]ヶ月 → [OK（3ヶ月+） / 短い]

[前提未達の場合]
⚠️ まずPSF達成、100ユーザー獲得を目指してください。
`/validate-psf` で再診断。

---

## PMF 3指標（Parthenon神殿）

### 1. Sean Ellisテスト

- とても残念: [X]人
- 回答総数: [Y]人
- **スコア**: [X/Y × 100]%

**目標**: 40%+

**判定**: [✅ 達成 / ❌ 未達]

### 2. NPS

- 推奨者（9-10点）: [X]%
- 批判者（0-6点）: [Y]%
- **NPS**: [X - Y]

**目標**: 50+

**判定**: [✅ 達成 / ❌ 未達]

### 3. Retention

| 指標 | 実績 | 目標 | 判定 |
|------|------|------|------|
| D1 Retention | [X]% | 40%+ | [OK/NG] |
| D7 Retention | [X]% | 20%+ | [OK/NG] |
| D30 Retention | [X]% | 40%+ | [OK/NG] |

**Retention Curve**: [Flattening / Smiling / Decaying]

**判定**: [✅ 達成 / ❌ 未達]

---

## 総合判定（PMF）

**達成度**: X/3指標

### [3/3達成の場合]
### 🎉 PMF達成！おめでとうございます！

Scaleフェーズへ進む準備ができています。

---

### [1-2/3達成の場合]
### ⚠️ PMF途中

あと一歩です。未達指標の改善に注力してください。

---

### [0/3達成の場合]
### ❌ PMF未達成

Pivot or PSF再検証を推奨します。
```

---

### Unit Economics診断

```markdown
## Unit Economics診断（スケール可能性判定）

### データから算出

**LTV計算**:
```
LTV = ARPU × Gross Margin / Churn率
    = $[ARPU] × [GM]% / [Churn]%
    = $[計算結果]
```

**LTV/CAC比率**:
```
LTV/CAC = $[LTV] / $[CAC] = [比率]
```

**Payback Period**:
```
Payback = CAC / (ARPU × Gross Margin)
        = $[CAC] / ($[ARPU] × [GM]%)
        = [X]ヶ月
```

---

### 判定

| 指標 | 実績 | 目標 | 判定 |
|------|------|------|------|
| LTV/CAC比率 | [X] | 3.0+ | [OK/NG] |
| Payback Period | [X]ヶ月 | 12ヶ月以内 | [OK/NG] |
| Gross Margin | [X]% | 70%+（SaaS） | [OK/NG] |

**スケール可能性**: [高 / 中 / 低]

---

### [スケール可能性: 高]
✅ Unit Economics健全。スケール投資GO！

### [スケール可能性: 中]
⚠️ 一部改善必要。効率化施策を実施してからスケール。

### [スケール可能性: 低]
❌ Unit Economics不健全。スケールすれば赤字拡大。
Retention改善・CAC削減が最優先。
```

---

### 改善アクションプラン

```markdown
## 改善アクションプラン

### [Sean Ellis未達の場合]

#### 問題
Sean Ellisスコア: [X]%（目標40%+）

#### 原因分析
- Aha Moment到達率が低い
- プロダクト価値が弱い
- ターゲットミスマッチ

#### 改善策
1. Aha Moment特定・到達率向上
2. コア機能の磨き込み
3. セグメント分析（熱狂ユーザーの共通点）

#### Tomorrow Action
- [ ] Aha Moment仮説設定
- [ ] オンボーディング改善
- [ ] 熱狂ユーザー10人インタビュー

---

### [NPS未達の場合]

#### 問題
NPS: [X]（目標50+）

#### 分類別分析
- 推奨者（9-10点）: [X]% → [増やす]
- 批判者（0-6点）: [Y]% → [減らす]

#### 改善策
1. Detractors削減（最優先）
   - 不満理由ヒアリング
   - トップ3課題の改善
2. Passives → Promoters転換
   - エンゲージメント強化

詳細: @startup_science/03_tactics/nps/nps_measurement.md

#### Tomorrow Action
- [ ] Detractors 10人にインタビュー
- [ ] 不満トップ3特定
- [ ] 改善施策3つ立案

---

### [Retention未達の場合]

#### 問題
D30 Retention: [X]%（目標40%+）

Retention Curve: [Decaying - PMF未達成パターン]

#### 改善策（3つの柱）
1. Aha Moment到達率向上
2. リエンゲージメント（プッシュ通知、メール）
3. 習慣化（デイリーアクティブ施策）

詳細: @startup_science/03_tactics/retention/retention_analysis.md

#### Tomorrow Action
- [ ] Aha Moment定義
- [ ] 到達率測定
- [ ] オンボーディング改善計画
- [ ] リエンゲージメントメール設計

---

### [Unit Economics悪化の場合]

#### 問題
LTV/CAC比率: [X]（目標3.0+）

#### 改善策（2つのアプローチ）

**アプローチA: LTV向上**
- Churn率低下（最優先）
- ARPU向上（アップセル、プラン改定）

**アプローチB: CAC削減**
- オーガニックチャネル強化（SEO、紹介）
- チャネル別CAC分析、低CACに集中

詳細: @startup_science/03_tactics/unit_economics/unit_eco_overview.md

#### Tomorrow Action
- [ ] Churn理由トップ3特定
- [ ] Retention改善施策
- [ ] CAC削減施策3つ
```

---

### PMF達成時のNext Action

```markdown
## 🎉 PMF達成！Scaleフェーズへ

### Scale準備（3ヶ月）

#### 1. Unit Economics最適化（1ヶ月）
- LTV/CAC比率 5.0+を目指す
- Payback Period 9ヶ月以内

#### 2. 成長エンジン構築（2ヶ月）
- AARRR最適化
  - Acquisition: チャネル拡大
  - Activation: Aha Moment到達率80%+
  - Retention: D30 50%+
  - Referral: 紹介プログラム導入
  - Revenue: Upsell/Cross-sell

フレームワーク: @startup_science/02_frameworks/aarrr/aarrr_overview.md

#### 3. 資金調達（任意）
- PMF証明データ準備
- Series A調達検討

---

### Tomorrow Action

1. **AARRR分析**（3時間）
   - `/apply-aarrr-analysis` で各指標を診断
   - ボトルネック特定

2. **成長計画**（2時間）
   - 3ヶ月後の目標設定
   - 施策ロードマップ

3. **チーム拡大計画**（1時間）
   - 採用ポジション定義
   - 組織体制設計

---

## おめでとうございます！

PMF達成は、スタートアップの最大の山場です。
ここからは成長加速フェーズ。

一緒にスケールを目指しましょう！
```

---

## Knowledge Base参照

- PMF概念: `@startup_science/01_stages/pmf/pmf_overview.md`
- NPS: `@startup_science/03_tactics/nps/nps_measurement.md`
- Retention: `@startup_science/03_tactics/retention/retention_analysis.md`
- Unit Economics: `@startup_science/03_tactics/unit_economics/unit_eco_overview.md`
- AARRR: `@startup_science/02_frameworks/aarrr/aarrr_overview.md`

---

## 更新履歴

- 2025-12-28: 初版作成
