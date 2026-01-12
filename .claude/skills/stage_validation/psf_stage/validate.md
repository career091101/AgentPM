# PSF Stage Validation Skill

PSF（Problem Solution Fit）達成度診断。

---

## Skill情報

- **コマンド**: `/validate-psf`
- **目的**: PSF達成度の定量診断
- **所要時間**: 20-30分

---

## このSkillでできること

1. **PSFチェックリスト判定**: 10倍・MVP・UVPの達成度
2. **MVP反応分析**: CVR、フィードバック評価
3. **Pivot判断**: PSF未達成なら方向転換検討
4. **Next Action**: PMFへ進むか、PSF強化か、Pivotか判断

---

## プロンプト

### セッション開始

```markdown
# PSF達成度診断

PSF（Problem Solution Fit）の達成度を診断します。

## PSFとは？

課題に対するソリューションが、10倍の価値を提供できるかを検証するフェーズ。

**判定基準**:
- 10倍価値提供（定量 or 定性）
- MVP反応: CVR 5%+
- UVP明確

---

## 現状を教えてください

### 1. CPF達成確認
- CPF達成済みですか？
- 3Uスコア平均: [X]/10
- インタビュー: [X]件、肯定[Y]%

### 2. 10倍検証
- 既存ソリューション: 何を使っている？
- あなたのソリューション: どう10倍良い？
- 定量データ: 時間・コスト・品質の改善率

### 3. MVP
- MVP作成済み？（種類: [Concierge/Wizard of Oz/Landing Page/etc]）
- テスト: 何人に見せた？
- 反応: CVR（購入意思・登録・クリック率）

### 4. UVP
- UVP（一文で）: [ターゲット]が[課題]を解決するために[プロダクト]を使うと[便益]が得られます。なぜなら[差別化]だからです。
```

---

### データ収集後 → 診断

```markdown
## PSF診断結果

### 前提: CPF達成確認
- 3Uスコア: [X]/10 → [OK / 未達]
- インタビュー: [X]件、肯定[Y]% → [OK / 未達]

[CPF未達成の場合]
⚠️ PSF検証前に、CPFを達成してください。
`/validate-cpf` で再診断を推奨。

---

### 1. 10倍検証

| 項目 | 既存 | あなた | 改善率 | 判定 |
|------|------|--------|--------|------|
| 時間 | [X] | [Y] | [Z]% | [OK/NG] |
| コスト | [X] | [Y] | [Z]% | [OK/NG] |
| 品質 | [X] | [Y] | [定性評価] | [OK/NG] |

**目標**: いずれか1つで8倍以上改善

**あなたの結果**: [判定]

### 2. MVP反応

- MVP種類: [種類]
- テスト人数: [X]人
- ポジティブ反応: [Y]人
- CVR: [Y/X × 100]%

**目標**: CVR 5%+

**あなたの結果**: [判定]

### 3. UVP明確度

- スコア: [5段階評価]
- 評価理由: [...]

**目標**: 4/5以上

---

## 総合判定

[全項目クリアの場合]
### ✅ PSF達成！

PMFフェーズへ進みましょう。

Next Skill: `/validate-pmf`

---

[1つでも未達の場合]
### ⚠️ PSF未達成

改善 or Pivot検討が必要です。
```

---

### 改善 vs Pivot判断

```markdown
## 改善 vs Pivot判断

### Pivot判断の5シグナル

1. **PSF指標停滞**: [X]ヶ月改善なし → [OK / NG]
2. **コア仮説否定**: 10倍提供不可能 → [OK / NG]
3. **市場規模**: TAM想定の1/10以下 → [OK / NG]
4. **競合優位性**: 差別化困難 → [OK / NG]
5. **情熱・資金**: 創業者疲弊、Runway<6ヶ月 → [OK / NG]

**判定**:
- 3つ以上NG → Pivot推奨
- 2つ以下NG → 改善継続

---

### [Pivot推奨の場合]

ピボット10類型から適切な方向転換を検討しましょう。

詳細診断: `/apply-pivot-decision`

---

### [改善継続の場合]

以下を強化してください。
```

---

### 改善アクションプラン

```markdown
## 改善アクションプラン

### [10倍未達の場合]

#### 問題
改善率: [最大X]倍（目標8倍+）

#### 改善策（3つの選択肢）

**選択肢A: ソリューション強化**
- 機能追加で10倍を目指す
- リスク: 時間かかる

**選択肢B: 比較対象変更**
- 既存ソリューションの中で最悪のものと比較
- 例: 手作業 vs Excel → 手作業 vs 電話連絡

**選択肢C: 定性価値に注目**
- 定量で10倍困難なら、定性（体験、感情）
- 例: Airbnb「ホテルより10倍安心」

#### Tomorrow Action
- [ ] 10倍仮説見直し
- [ ] ソリューション強化案5つ
- [ ] 再検証計画

---

### [MVP反応低い場合]

#### 問題
CVR: [X]%（目標5%+）

#### 原因分析

| 原因候補 | チェック |
|---------|---------|
| MVP品質低すぎ | [ ] |
| 見せた人が非ターゲット | [ ] |
| 価格設定ミス | [ ] |
| UVP伝わっていない | [ ] |
| 課題そのものが弱い | [ ] |

#### 改善策
[該当する原因の対策]

#### Tomorrow Action
- [ ] MVP改善（UX磨き込み）
- [ ] ターゲット再選定
- [ ] 再テスト10人

---

### [UVP不明確の場合]

#### 問題
UVP曖昧、差別化不明確

#### 改善策
UVPキャンバス埋め直し

テンプレート: @startup_science/01_stages/psf/uvp_canvas.md

#### Tomorrow Action
- [ ] 5要素（ターゲット、課題、ソリューション、便益、差別化）明確化
- [ ] UVP一文作成
- [ ] 10人に説明してみる
```

---

### PSF達成時のNext Action

```markdown
## ✅ PSF達成！おめでとうございます

### Next: PMFフェーズへ

PMF（Product Market Fit）では:
1. プロダクトリリース
2. Sean Ellisテスト（40%+）
3. NPS測定（50+）
4. Retention分析（D30 40%+）

#### Tomorrow Action

1. **プロダクト開発計画**（3時間）
   - MVPからフルプロダクトへ
   - 開発期間・リソース見積もり

2. **指標設定**（1時間）
   - AARRR各段階のKPI設定
   - フレームワーク: @startup_science/02_frameworks/aarrr/aarrr_overview.md

3. **ローンチ計画**（2時間）
   - 初期ユーザー獲得戦略
   - SNS戦略: @startup_science/99_reference/sns_content_strategy.md

#### 3ヶ月後

100+ユーザー獲得後、`/validate-pmf` でPMF達成度を診断しましょう。
```

---

## Knowledge Base参照

- PSF概念: `@startup_science/01_stages/psf/psf_overview.md`
- 10倍検証: `@startup_science/01_stages/psf/10x_validation.md`
- MVP: `@startup_science/01_stages/psf/mvp_types.md`
- UVP: `@startup_science/01_stages/psf/uvp_canvas.md`
- Pivot: `@startup_science/03_tactics/pivot/pivot_types.md`

---

## 更新履歴

- 2025-12-28: 初版作成
