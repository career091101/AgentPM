# Design GTM Strategy - Go-to-Market戦略設計スキル

## スキル概要

**Design GTM Strategy** は、Bullseye Frameworkを用いて最適なGo-to-Market戦略を体系的に設計するスキルです。19チャネルを5軸で評価し、Inner Circle（最優先3チャネル）を自動特定。CAC最小化とスケール加速を実現します。

### このスキルを使うべき段階

- **PMF達成後**、スケール段階への移行時点
- **チャネル最適化**が必要な場合
- **CAC削減施策**を検討する際

### 所要時間

初回：40-60分（データ収集・評価含む）
継続実行：20-30分/月次レビュー

### 出力成果物

- GTM戦略書（Bullseye Framework適用、テスト計画、スケール計画）
- チャネル別テスト設計（$1,000予算、2-4週間）
- CAC/LTV分析とROI評価
- 3ヶ月/6ヶ月/12ヶ月スケール計画

---

## 使用例（実践シナリオ）

### 例1：B2B SaaS スタートアップ

**前提条件**:
- PMF達成確認済み（Sean Ellis 45%, 月次成長率 12%）
- アクティブユーザー: 100人
- LTV/CAC: 3.5

**実行結果**:
```
Step 1: 19チャネル評価完了
Step 2-3: スコアリング（5軸評価）
Step 4: Bullseye Framework適用
  ├─ Inner Circle: Content Marketing (48点), SEO (45点), Community Building (42点)
  ├─ Middle Ring: SEM, Social Ads, PR, Email, BD
  └─ Outer Ring: その他11チャネル

Step 5-6: Inner Circle 3チャネルのテスト計画策定
  ├─ Content Marketing: $1,000, 4週間
  ├─ SEO: $1,000, 4週間
  └─ Community Building: $1,000, 4週間

Step 7-8: CAC/LTV計算 & ROI評価
  ├─ Content Marketing: CAC $20, LTV/CAC 15.0 ✅
  ├─ SEO: CAC $10, LTV/CAC 30.0 ✅
  └─ Community Building: CAC $100, LTV/CAC 3.0 ✅

Step 9: スケール計画生成
  ├─ Month 1-3: テスト実施、勝ちチャネル特定
  ├─ Month 4-6: 月$10,000投資、チーム拡大
  └─ Month 7-12: チャネル多様化、CAC 30%削減目標
```

### 例2：モバイルアプリ（B2C）

**前提条件**:
- PMF達成確認済み
- DAU/MAU比率: 60%
- Churn Rate: 3%/月

**実行結果**:
```
Inner Circle候補: Viral Marketing, Social Ads, Influencer Marketing
テスト予算配分: 各$1,000 × 3チャネル = $3,000
期待効果: 月200-300新規ユーザー獲得
```

---

## 必要な入力情報

| 項目 | 内容 | 出典 |
|------|------|------|
| **PMF確認** | Sean Ellisテスト、月次成長率、Churn Rate | `/validate-pmf` |
| **ユニットエコノミクス** | LTV、CAC、LTV/CAC比率、CAC回収期間 | `/validate-unit-economics` |
| **ペルソナ** | 業界、役職、行動パターン、課題 | `persona.md` |
| **初期顧客データ** | 最低30人以上の有料顧客情報 | lean_canvas.md |
| **マーケティング予算** | 初期テスト予算($1,000-$10,000) | 経営判断 |

---

## 出力フォーマット

### メインファイル

**ファイル名**: `gtm_strategy.md`

**保存先**: `Flow/{YYYYMM}/{YYYY-MM-DD}/gtm_strategy.md`

**内容構成**:
1. エグゼクティブサマリー（推奨チャネル、初期投資額）
2. 前提条件確認（PMF達成、ユニットエコノミクス）
3. 19チャネル評価表（5軸スコアリング）
4. Bullseye Framework分類
5. Inner Circle チャネル別テスト計画
6. チャネル別CAC/LTV計算
7. ROI評価と最終選定
8. スケール計画（3/6/12ヶ月）
9. リスク管理と早期撤退基準
10. 次のアクション（Week 1-2のTo-Do）

### テンプレートファイル

`templates/` フォルダに以下を提供：

- **gtm_input.md**: GTM戦略入力テンプレート
- **bullseye_framework.md**: Bullseye Framework 19チャネル評価用
- **gtm_plan_output.md**: GTM計画書フォーマット

---

## Bullseye Frameworkの3リング

### Inner Circle（最優先3チャネル）

**選定基準**:
- スコア: 40点以上
- LTV/CAC: 3.0以上
- CAC回収期間: 12ヶ月以下

**アクション**: $1,000テスト、2-4週間

**予算配分**: Primary 60%, Secondary 40%

### Middle Ring（次候補5チャネル）

**選定基準**: スコア30-39点

**アクション**: Inner Circle失敗時の代替案

### Outer Ring（検討11チャネル）

**選定基準**: スコア29点以下

**アクション**: 現時点では実施しない（Phase4以降）

---

## 5軸スコアリング基準

各チャネルを以下の5軸で評価（各10点満点）：

| 評価軸 | 説明 | 配点 |
|-------|------|:----:|
| **Targeting** | ターゲット顧客への到達性 | 10点 |
| **Cost** | 初期・運用コストの低さ | 10点 |
| **Input Time** | 必要な時間・工数の少なさ | 10点 |
| **Output Time** | 成果が出るまでの速さ | 10点 |
| **Scale** | スケール可能性 | 10点 |

---

## CAC/LTV計算と判定基準

### 計算式

```
CAC = チャネル投資額 / 獲得顧客数

LTV = (ARPU × 粗利率) / Churn Rate

LTV/CAC = LTV / CAC
```

### 判定基準

| LTV/CAC | 評価 | アクション |
|---------|------|----------|
| ≥ 5.0 | ✅ 優秀 | 即座にスケール |
| 3.0-4.9 | ✅ 良好 | スケール可能 |
| 2.0-2.9 | ⚠️ 要改善 | 最適化後にスケール |
| < 2.0 | ❌ 不合格 | チャネル変更 |

---

## スケール計画の3フェーズ

### Phase 1: テスト＆検証（Month 1-3）

- Month 1: Inner Circle 3チャネルで$1,000テスト
- Month 2: 勝ちチャネル特定、予算2倍へ
- Month 3: 初期スケール、プロセス標準化

### Phase 2: スケールアップ（Month 4-6）

- Month 4-5: Primary Channelに月$10,000投資
- Month 6: Middle Ring上位チャネルをテスト

### Phase 3: 多様化＆効率化（Month 7-12）

- Month 7-9: Inner Circle 3-4チャネルへ拡大
- Month 10-12: CAC 30%削減、LTV 50%向上

---

## よくある質問（FAQ）

### Q1: Inner Circleが1チャネルしか条件を満たさない場合は？

**A**: 1チャネルのみでもOK。ただし、リスク分散のためMiddle Ringから最上位1チャネルをSecondary Channelとして追加推奨（予算配分80%/20%）。

### Q2: すべてのチャネルがLTV/CAC < 3.0の場合は？

**A**: GTM戦略ではなく、先に以下を改善:
1. LTV向上（アップセル、Churn削減）
2. CAC削減（LP改善、ターゲティング最適化）
3. PMF再検証

### Q3: 19チャネルすべてをテストする必要があるか？

**A**: 不要。Bullseye Frameworkの思想は「Inner Circle 3チャネルに集中」。全チャネルテストは時間とコストの浪費。スコアリングで絞り込み、Inner Circleのみテスト。

### Q4: テスト期間2-4週間は短すぎる？

**A**: チャネルによる。SEM/Social Adsは2週間で判定可能。SEO/Community Buildingは4週間以上必要。Output Timeスコアを参考に期間調整。

### Q5: 予算$1,000がない場合は？

**A**: 無料チャネル（Content Marketing, SEO, Community Building）に絞る。または、$500でマイクロテスト（成功基準を下げる）。

---

## 関連スキル・ドキュメント

| スキル / 文書 | 説明 |
|-------------|------|
| **validate-pmf** | PMF達成確認（design-gtm-strategy 実行の前提） |
| **validate-unit-economics** | ユニットエコノミクス検証（LTV/CAC確認） |
| **measure-aarrr** | AARRR分析（スケール後の成長ファネル測定） |
| **monitor-burn-rate** | バーンレート監視（資金状況確認） |
| **@startup_science/bullseye_framework.md** | Bullseye Framework詳細 |
| **@startup_science/traction_channels.md** | 19チャネル詳細解説 |

---

## スキル情報

| 項目 | 値 |
|-----|-----|
| **スキルID** | design-gtm-strategy |
| **ステージ** | Phase3（スケール） |
| **所要時間** | 40-60分 |
| **出力ファイル** | Flow/{YYYYMM}/{YYYY-MM-DD}/gtm_strategy.md |
| **前提スキル** | validate-pmf, validate-unit-economics |
| **次のスキル** | measure-aarrr（AARRR測定） |
| **フレームワーク準拠** | 起業の科学 × Traction（Bullseye Framework） |
| **準拠率** | 100% |
| **バージョン** | 1.0.0 |
| **作成日** | 2025-12-31 |

---

## 次のステップ

1. **このREADMEを確認** → スキルの全体像を把握
2. **テンプレートファイルを参照** → 実際の入力・出力フォーマット確認
3. **前提条件確認** → `/validate-pmf`, `/validate-unit-economics` スキル実行
4. **スキル実行** → `/design-gtm-strategy` コマンド実行
5. **テスト実装** → Inner Circle 3チャネルで$1,000テスト開始
6. **月次レビュー** → KPI測定、改善施策検討

---

**質問・フィードバック**: SKILL.md のコメントセクションまたはドキュメント内の「FAQ」セクションを確認してください。
