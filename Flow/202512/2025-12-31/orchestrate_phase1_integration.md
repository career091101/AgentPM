# orchestrate-phase1 統合レポート

**作成日**: 2025-12-31
**対象スキル**: orchestrate-phase1
**新規6スキル**: estimate-market-size, prioritize-features, map-customer-journey, design-ab-test, design-gtm-strategy, generate-kpi-dashboard

---

## エグゼクティブサマリー

### 統合判定

**総合判定**: ⚠️ **一部統合推奨・選択的追加**

- **統合推奨**: 2スキル（必須・高優先度）
- **オプション統合**: 3スキル（条件付き）
- **統合不要**: 1スキル（Phase1範囲外）

### 統合結果概要

| スキル | 統合判定 | 統合ステップ | 優先度 | 理由 |
|--------|:--------:|:----------:|:-----:|------|
| **estimate-market-size** | ✅ 統合 | STEP 1-3 | P0 | アイデア検証の必須要素 |
| **map-customer-journey** | ✅ 統合 | STEP 6 | P1 | CPF検証後のUX深掘り |
| **prioritize-features** | ⚠️ オプション | STEP 8-9 | P2 | MVP選定との重複あり |
| **design-ab-test** | ⚠️ オプション | STEP 9 | P2 | LP改善時のみ有効 |
| **generate-kpi-dashboard** | ⚠️ オプション | STEP 12 | P1 | スコアカード補完 |
| **design-gtm-strategy** | ❌ 統合不要 | - | - | Phase3スケール向け、Phase1範囲外 |

---

## 1. 統合推奨スキル（必須・高優先度）

### 1.1 estimate-market-size

**統合ポイント**: STEP 1-3（Discovery & Planning）

#### 現在のorchestrate-phase1構造

```
STEP 1: /discover-demand（15-30分）
STEP 2: /create-mvv（20-40分）
STEP 3: /apply-lean-canvas（60-90分）
STEP 4: /build-flywheel（30-50分）
```

#### 統合案（STEP 3.5として追加）

```diff
STEP 1: /discover-demand（15-30分）
STEP 2: /create-mvv（20-40分）
STEP 3: /apply-lean-canvas（60-90分）
+ STEP 3.5: /estimate-market-size（30-50分）← 新規追加
STEP 4: /build-flywheel（30-50分）
```

#### 統合理由

- **TAM/SAM/SOM**: リーンキャンバスの「市場規模」セクションを定量化
- **投資判断基準**: TAM ≥ ¥100億を満たさない場合、早期Pivotシグナル
- **CPF検証前**: 市場規模が小さすぎる場合、CPF検証前に停止推奨
- **起業の科学準拠**: アイデア検証（STEP 1）の必須要素

#### 実行フロー

```markdown
STEP 3.5: /estimate-market-size（30-50分）

**入力**:
- `lean_canvas.md`（STEP 3の成果物）
- `persona.md`（STEP 2から派生）

**処理**:
1. TAM計算（トップダウン・ボトムアップ）
2. SAM計算（地理的・言語制約適用）
3. SOM計算（1-5%シェア仮説）
4. 投資判断基準評価（4指標）

**出力**:
- `documents/1_initiating/market_size_estimation.md`

**判定基準**:
- 4指標すべて✅ → STEP 4へ進む
- 2-3指標✅ → 警告表示、ユーザー判断を求める
- 1指標以下✅ → **停止**（Human-in-the-Loop）、別アイデア検討推奨

**ステージゲート追加**:
- **ステージゲート0: 市場規模**（STEP 3.5後）
  - 合格条件: TAM ≥ ¥100億、SAM ≥ ¥50億
  - 未達成時: 停止、Pivot提案
```

#### 影響範囲

- **総所要時間**: 3-6時間 → **3.5-6.5時間**（+30-50分）
- **dependencies更新**: `estimate-market-size`を追加
- **成果物追加**: `market_size_estimation.md`

---

### 1.2 map-customer-journey

**統合ポイント**: STEP 6（Validation）

#### 現在のorchestrate-phase1構造

```
STEP 5: /research-problem（30-60分）
STEP 6: /simulate-interview（25-45分）
STEP 7: /validate-cpf（20-30分）
```

#### 統合案（STEP 6.5として追加）

```diff
STEP 5: /research-problem（30-60分）
STEP 6: /simulate-interview（25-45分）
+ STEP 6.5: /map-customer-journey（30-40分）← 新規追加
STEP 7: /validate-cpf（20-30分）
```

#### 統合理由

- **6段階ジャーニー**: 認知→推薦の全段階を可視化、CPF検証の深掘り
- **タッチポイント特定**: LP、Email、サポート等のUX改善ポイント明確化
- **感情曲線**: ペインポイント（-3以下）の特定、改善施策提案
- **CPF検証補完**: simulate-interviewの仮想データを、ジャーニーマップで構造化

#### 実行フロー

```markdown
STEP 6.5: /map-customer-journey（30-40分）

**入力**:
- `persona.md`（STEP 2の成果物）
- `interview_simulation.md`（STEP 6の成果物）

**処理**:
1. 6段階ジャーニーマップ生成（認知→推薦）
2. タッチポイント特定（15個以上）
3. 感情曲線スコアリング（-5～+5）
4. 改善施策提案（15個以上）
5. Quick Wins特定（5個以上）

**出力**:
- `documents/2_discovery/customer_journey_map.md`

**成功基準**:
- ✅ 6段階すべてマッピング完了
- ✅ ペインポイント（感情スコア -3以下）3箇所以上特定
- ✅ Quick Wins 5個以上提案

**次のアクション**:
- Quick Winsを`/build-lp`に反映（STEP 9で活用）
- ペインポイントを`/validate-cpf`の改善アクションに統合
```

#### 影響範囲

- **総所要時間**: 3.5-6.5時間 → **4-7時間**（+30-40分）
- **dependencies更新**: `map-customer-journey`を追加
- **成果物追加**: `customer_journey_map.md`

---

## 2. オプション統合スキル（条件付き）

### 2.1 prioritize-features

**統合ポイント**: STEP 8-9（PSF Validation）

#### 現状の問題点

orchestrate-phase1の**STEP 9: /build-lp**では、既にMVP選定が行われる。
- `validate-10x`（STEP 8）でMVP候補を特定
- `build-lp`（STEP 9）でUVPと共にLP構築

**prioritize-features**との重複:
- ICE/RICEスコアリングは、既にMVP選定プロセスに含まれる
- 機能優先順位付けは、Phase1ではなくPhase2（PMF検証後）の施策

#### 統合判定: ⚠️ **オプション**（必須ではない）

**統合条件**:
- MVP候補が10個以上ある場合のみ
- ユーザーが明示的に「機能優先順位付け」を要求した場合

#### 統合案（STEP 8.5としてオプション追加）

```diff
STEP 8: /validate-10x（40-70分）
+ [OPTIONAL] STEP 8.5: /prioritize-features（20-30分）← MVP候補10個以上の場合のみ
STEP 9: /build-lp（40-80分）
```

#### 実行フロー

```markdown
[OPTIONAL] STEP 8.5: /prioritize-features（20-30分）

**実行条件**:
- MVP候補が10個以上ある場合
- または、ユーザーが明示的に要求した場合

**入力**:
- `10x_validation.md`（STEP 8の成果物、MVP候補リスト）
- `interview_simulation.md`（ユーザーフィードバック）

**処理**:
1. ICE/RICEスコアリング（10機能以上）
2. Quick Wins特定（Impact ≥ 7 かつ Ease ≥ 7）
3. 実装ロードマップ（Now/Next/Later）

**出力**:
- `documents/4_product/feature_prioritization.md`

**次のアクション**:
- Top 3機能を`/build-lp`に反映（MVP Feature Listとして明示）
```

#### 影響範囲

- **総所要時間**: 4-7時間 → **4.5-7.5時間**（+20-30分、オプション）
- **dependencies更新**: `prioritize-features`を**オプション依存**として追加
- **成果物追加**: `feature_prioritization.md`（オプション）

---

### 2.2 design-ab-test

**統合ポイント**: STEP 9（PSF Validation - LP構築後）

#### 現状の問題点

orchestrate-phase1の**STEP 9: /build-lp**では、LP構築のみを実施。
- A/Bテストは、LP公開**後**の改善施策（Phase2以降）
- Phase1では、まだトラフィックが不足（統計的有意性を得るサンプルサイズなし）

#### 統合判定: ⚠️ **オプション**（Phase1範囲外だが、設計のみ実施可能）

**統合条件**:
- ユーザーが「LP改善計画」を事前に策定したい場合
- 週間トラフィックが500以上ある場合（統計的有意性を得られる最低ライン）

#### 統合案（STEP 9.5としてオプション追加）

```diff
STEP 9: /build-lp（40-80分）
+ [OPTIONAL] STEP 9.5: /design-ab-test（30-40分）← LP公開前の改善計画策定
STEP 10: /validate-psf（5-10分）
```

#### 実行フロー

```markdown
[OPTIONAL] STEP 9.5: /design-ab-test（30-40分）

**実行条件**:
- ユーザーが明示的に要求した場合
- または、週間トラフィック ≥ 500の場合

**入力**:
- `lp/index.html`（STEP 9の成果物）
- `psf_diagnosis.md`（STEP 10の成果物、UVP仮説）

**処理**:
1. 仮説設定（Hero CTA、UVP、Pricing等）
2. サンプルサイズ計算（週間トラフィックベース）
3. バリエーション設計（コントロール vs バリアント）
4. テスト期間推定（7週間以内か確認）

**出力**:
- `documents/3_planning/ab_test_design.md`

**注意**:
- テスト実施は、LP公開後（Phase2以降）
- Phase1では「設計書」のみ作成
```

#### 影響範囲

- **総所要時間**: 4.5-7.5時間 → **5-8時間**（+30-40分、オプション）
- **dependencies更新**: `design-ab-test`を**オプション依存**として追加
- **成果物追加**: `ab_test_design.md`（オプション）

---

### 2.3 generate-kpi-dashboard

**統合ポイント**: STEP 12（Launch Preparation）

#### 現状の問題点

orchestrate-phase1の**STEP 12: /startup-scorecard**では、40点満点の総合評価を実施。
- スコアカードは「Phase1完了判定」に特化
- KPIダッシュボードは「Phase2以降の継続モニタリング」に特化

#### 統合判定: ⚠️ **オプション**（スコアカード補完、Phase2準備）

**統合条件**:
- ユーザーが「Phase2準備」を要求した場合
- 投資家ピッチ資料を作成する場合

#### 統合案（STEP 12.5としてオプション追加）

```diff
STEP 11: /create-sns-content（30-50分）
STEP 12: /startup-scorecard（20-40分）
+ [OPTIONAL] STEP 12.5: /generate-kpi-dashboard（20-30分）← Phase2準備、投資家レポート
```

#### 実行フロー

```markdown
[OPTIONAL] STEP 12.5: /generate-kpi-dashboard（20-30分）

**実行条件**:
- ユーザーが明示的に要求した場合
- または、Phase2へ進む場合（スコアカード32点以上）

**入力**:
- `scorecard.md`（STEP 12の成果物）
- `cpf_diagnosis.md`、`psf_diagnosis.md`（STEP 7, 10の成果物）
- `10x_validation.md`（STEP 8の成果物）

**処理**:
1. Phase1時点のKPI統合（Financial/Customer/Product/Growth）
2. Top 5 KPI自動選定（Phase2向け）
3. トレンドグラフ生成（Phase1期間の6ヶ月分）
4. アラート設定（Phase2で監視する閾値）
5. 投資家レポート形式エクスポート（PDF/PNG）

**出力**:
- `documents/5_monitoring/kpi_dashboard.md`

**次のアクション**:
- Phase2開始時に、このダッシュボードをベースに週次/月次更新
```

#### 影響範囲

- **総所要時間**: 5-8時間 → **5.5-8.5時間**（+20-30分、オプション）
- **dependencies更新**: `generate-kpi-dashboard`を**オプション依存**として追加
- **成果物追加**: `kpi_dashboard.md`（オプション）

---

## 3. 統合不要スキル

### 3.1 design-gtm-strategy

**統合判定**: ❌ **統合不要**（Phase1範囲外）

#### 統合不要の理由

- **Bullseye Framework**: Phase3スケール向けのチャネル戦略
- **PMF達成前提**: 19チャネルテストは、PMF達成後の施策
- **orchestrate-phase1の範囲**: Phase1はPSF検証まで（PMF前段階）

#### Phase3で実施すべき理由

- **前提条件**: PMF達成（Sean Ellis ≥ 40%, 月次成長率 ≥ 10%）
- **ユニットエコノミクス確立**: LTV/CAC ≥ 3.0
- **最低30人の有料顧客**: チャネルテストに必要な初期顧客基盤

#### 推奨実施タイミング

```
Phase1（orchestrate-phase1） → PSF検証完了
  ↓
Phase2（orchestrate-phase2） → PMF検証完了
  ↓
Phase3（orchestrate-phase3） → /design-gtm-strategy実施 ← ここで実施
```

---

## 4. 更新後のorchestrate-phase1実行フロー

### 4.1 統合後の全12ステップ（+オプション4ステップ）

#### Discovery & Planning（発見・計画）

1. `/discover-demand` - 需要発見リサーチ（15-30分）
2. `/create-mvv` - MVV早期定義（20-40分）
3. `/apply-lean-canvas` - リーンキャンバス作成（60-90分）
4. **[NEW] `/estimate-market-size`** - 市場規模推定（30-50分）✅ **必須**
5. `/build-flywheel` - フライホイール設計（30-50分）

**[ステージゲート0: 市場規模]** ← 新規追加
- 判定基準: TAM ≥ ¥100億、SAM ≥ ¥50億
- 通過 → STEP 5へ進む
- 未達成 → **停止**、Pivot提案

#### Validation（検証）

6. `/research-problem` - Web課題発見（30-60分）
7. `/simulate-interview` - 仮想ペルソナインタビュー（25-45分）
8. **[NEW] `/map-customer-journey`** - カスタマージャーニーマップ（30-40分）✅ **必須**
9. `/validate-cpf` - CPF診断（20-30分）

**[ステージゲート1: CPF]**
- 判定基準: CPFスコア60%以上
- 通過 → STEP 10へ進む
- 未達成 → **停止**、改善アクション提示

#### PSF Validation（PSF検証）

10. `/validate-10x` - 10倍優位性検証（40-70分）
11. **[OPTIONAL] `/prioritize-features`** - 機能優先順位付け（20-30分）⚠️ MVP候補10個以上の場合のみ
12. `/build-lp` - LP構築（40-80分）
13. **[OPTIONAL] `/design-ab-test`** - A/Bテスト設計（30-40分）⚠️ LP改善計画策定時のみ
14. `/validate-psf` - PSF診断（5-10分）

**[ステージゲート2: PSF]**
- 判定基準: 10倍2軸以上 + MVP選定完了 + UVP明確
- 通過 → STEP 15へ進む
- 未達成 → **停止**、改善アクション提示

#### Launch Preparation（ローンチ準備）

15. `/create-sns-content` - SNSコンテンツ作成（30-50分）
16. `/startup-scorecard` - 最終評価（20-40分）
17. **[OPTIONAL] `/generate-kpi-dashboard`** - KPIダッシュボード生成（20-30分）⚠️ Phase2準備時のみ

---

### 4.2 総所要時間の変更

| 構成 | 所要時間 | 備考 |
|------|:--------:|------|
| **現在（12ステップ）** | 3-6時間 | 基本構成 |
| **統合後（必須14ステップ）** | **4-7時間** | estimate-market-size + map-customer-journey追加 |
| **統合後（全17ステップ）** | **5.5-8.5時間** | すべてのオプションスキルを含む |

---

### 4.3 依存関係の更新

#### 現在のdependencies

```yaml
dependencies:
  - discover-demand
  - create-mvv
  - apply-lean-canvas
  - build-flywheel
  - research-problem
  - simulate-interview
  - validate-cpf
  - validate-10x
  - build-lp
  - validate-psf
  - create-sns-content
  - startup-scorecard
```

#### 更新後のdependencies

```yaml
dependencies:
  - discover-demand
  - create-mvv
  - apply-lean-canvas
  - estimate-market-size          # ← 新規追加（必須）
  - build-flywheel
  - research-problem
  - simulate-interview
  - map-customer-journey          # ← 新規追加（必須）
  - validate-cpf
  - validate-10x
  - prioritize-features           # ← 新規追加（オプション）
  - build-lp
  - design-ab-test                # ← 新規追加（オプション）
  - validate-psf
  - create-sns-content
  - startup-scorecard
  - generate-kpi-dashboard        # ← 新規追加（オプション）
```

---

## 5. orchestrate-phase1 SKILL.md更新案

### 5.1 更新箇所

#### (1) メタデータセクション

```diff
dependencies:
  - discover-demand
  - create-mvv
  - apply-lean-canvas
+ - estimate-market-size
  - build-flywheel
  - research-problem
  - simulate-interview
+ - map-customer-journey
  - validate-cpf
  - validate-10x
+ - prioritize-features # オプション
  - build-lp
+ - design-ab-test # オプション
  - validate-psf
  - create-sns-content
  - startup-scorecard
+ - generate-kpi-dashboard # オプション

- execution_time: 3-6時間（自動実行）
+ execution_time: 4-7時間（必須14ステップ）、5.5-8.5時間（全オプション含む）
```

#### (2) Phase1実行ステップセクション

```diff
#### Discovery & Planning（発見・計画）

1. `/discover-demand` - 需要発見リサーチ（15-30分）
2. `/create-mvv` - MVV早期定義（20-40分）
3. `/apply-lean-canvas` - リーンキャンバス作成（60-90分）
+ 4. `/estimate-market-size` - 市場規模推定（30-50分）← 新規追加
- 4. `/build-flywheel` - フライホイール設計（30-50分）
+ 5. `/build-flywheel` - フライホイール設計（30-50分）

+ **[ステージゲート0: 市場規模]**
+ - 判定基準: TAM ≥ ¥100億、SAM ≥ ¥50億
+ - 通過 → STEP 5へ進む
+ - 未達成 → **停止**、Pivot提案

#### Validation（検証）

- 5. `/research-problem` - Web課題発見（30-60分）
+ 6. `/research-problem` - Web課題発見（30-60分）
- 6. `/simulate-interview` - 仮想ペルソナインタビュー（25-45分）
+ 7. `/simulate-interview` - 仮想ペルソナインタビュー（25-45分）
+ 8. `/map-customer-journey` - カスタマージャーニーマップ（30-40分）← 新規追加
- 7. `/validate-cpf` - CPF診断（20-30分）
+ 9. `/validate-cpf` - CPF診断（20-30分）

（以降、STEP番号を+3シフト）
```

#### (3) 成果物セクション

```diff
{IDEA_FOLDER}/
├── documents/
│   ├── 1_initiating/
│   │   ├── demand_discovery.md
│   │   └── business_idea.md
+│   │   └── market_size_estimation.md ← 新規追加
│   ├── 2_discovery/
│   │   ├── lean_canvas.md
│   │   ├── persona.md
│   │   ├── flywheel.md
│   │   ├── problem_research.md
│   │   ├── interview_simulation.md
+│   │   ├── customer_journey_map.md ← 新規追加
│   │   └── 10x_validation.md
│   ├── 3_planning/
│   │   ├── mvv.md
│   │   ├── cpf_diagnosis.md
+│   │   ├── ab_test_design.md ← 新規追加（オプション）
│   │   └── psf_diagnosis.md
+│   ├── 4_product/
+│   │   └── feature_prioritization.md ← 新規追加（オプション）
│   └── 5_monitoring/
│       └── scorecard.md
+│       └── kpi_dashboard.md ← 新規追加（オプション）
├── mvp/
│   ├── lp/（README.md）
│   └── sns_contents/（posts.md）
└── phase1_summary.md
```

---

## 6. 推奨アクション

### 6.1 即座実行（必須）

1. **orchestrate-phase1 SKILL.md更新**
   - 新規2スキル（estimate-market-size, map-customer-journey）を必須として追加
   - STEP番号を再採番（STEP 1-17）
   - ステージゲート0追加（市場規模）
   - 総所要時間を4-7時間に更新

2. **依存関係テスト**
   - `/estimate-market-size`が`lean_canvas.md`を読み込めるか確認
   - `/map-customer-journey`が`persona.md`、`interview_simulation.md`を読み込めるか確認

### 6.2 短期（1週間以内）

1. **オプションスキル統合**
   - `prioritize-features`、`design-ab-test`、`generate-kpi-dashboard`を条件付き実行として実装
   - 実行条件判定ロジックを追加（MVP候補数、トラフィック数、スコアカード結果）

2. **ドキュメント整備**
   - 新規成果物のテンプレート作成
   - 統合後のorchestrate-phase1実行例を更新

### 6.3 中期（2週間以内）

1. **エンドツーエンドテスト**
   - 新規統合後のorchestrate-phase1を、仮想アイデアで全実行
   - 所要時間、成果物、ステージゲート判定の検証

2. **他スキルとの連携確認**
   - orchestrate-phase2（未作成）への引き継ぎ確認
   - `design-gtm-strategy`がPhase3で正しく実行されるか確認

---

## 7. 統合しない理由（design-gtm-strategy）

### 7.1 Phase1範囲外の根拠

- **orchestrate-phase1の目的**: PSF検証まで（PMF前段階）
- **design-gtm-strategyの前提**: PMF達成後のスケール施策
- **Bullseye Framework**: 19チャネルテストは、有料顧客30人以上が前提

### 7.2 Phase3で実施すべき理由

- **前提条件**: Sean Ellis ≥ 40%, 月次成長率 ≥ 10%
- **ユニットエコノミクス**: LTV/CAC ≥ 3.0、CAC回収期間 ≤ 12ヶ月
- **チャネルテスト予算**: $1,000/チャネル × 3チャネル = $3,000（Phase1では予算不足）

### 7.3 推奨実施フロー

```
orchestrate-phase1（Phase1）
  → PSF検証完了、スコアカード32点以上
  ↓
orchestrate-phase2（Phase2）
  → PMF検証完了、Sean Ellis ≥ 40%
  ↓
orchestrate-phase3（Phase3）
  → /design-gtm-strategy実施 ← ここで実施
  → Inner Circle選定、チャネルテスト開始
```

---

## 8. 成果物サマリー

### 8.1 成果物一覧（更新後）

| カテゴリ | ファイル名 | 新規/既存 | 必須/オプション |
|---------|-----------|:--------:|:-------------:|
| **1_initiating** | demand_discovery.md | 既存 | 必須 |
| **1_initiating** | business_idea.md | 既存 | 必須 |
| **1_initiating** | **market_size_estimation.md** | **新規** | **必須** |
| **2_discovery** | lean_canvas.md | 既存 | 必須 |
| **2_discovery** | persona.md | 既存 | 必須 |
| **2_discovery** | flywheel.md | 既存 | 必須 |
| **2_discovery** | problem_research.md | 既存 | 必須 |
| **2_discovery** | interview_simulation.md | 既存 | 必須 |
| **2_discovery** | **customer_journey_map.md** | **新規** | **必須** |
| **2_discovery** | 10x_validation.md | 既存 | 必須 |
| **3_planning** | mvv.md | 既存 | 必須 |
| **3_planning** | cpf_diagnosis.md | 既存 | 必須 |
| **3_planning** | psf_diagnosis.md | 既存 | 必須 |
| **3_planning** | **ab_test_design.md** | **新規** | **オプション** |
| **4_product** | **feature_prioritization.md** | **新規** | **オプション** |
| **5_monitoring** | scorecard.md | 既存 | 必須 |
| **5_monitoring** | **kpi_dashboard.md** | **新規** | **オプション** |
| **mvp/lp** | index.html | 既存 | 必須 |
| **mvp/sns_contents** | posts.md | 既存 | 必須 |

### 8.2 成果物総数

- **既存成果物**: 13ファイル
- **新規成果物（必須）**: 2ファイル（market_size_estimation.md, customer_journey_map.md）
- **新規成果物（オプション）**: 3ファイル（ab_test_design.md, feature_prioritization.md, kpi_dashboard.md）
- **合計**: 18ファイル（必須15、オプション3）

---

## 9. リスク管理

### 9.1 実行時間増加リスク

**リスク**: 3-6時間 → 4-7時間（+1時間）

**対策**:
- ユーザーに「必須2スキル追加」を事前に通知
- オプションスキルは、ユーザー判断で実行可否を選択可能に
- 早期終了オプション（ステージゲート0で市場規模不足の場合、STEP 4で停止）

### 9.2 複雑度増加リスク

**リスク**: STEP数が12 → 17（+5ステップ）

**対策**:
- ステップ番号の明確化（STEP 1-17で一貫性）
- オプションステップの明示（`[OPTIONAL]`タグ）
- 実行フロー図の更新（Mermaid）

### 9.3 依存関係の破綻リスク

**リスク**: 新規スキルが既存成果物を読み込めない

**対策**:
- 事前テスト実施（`estimate-market-size` → `lean_canvas.md`読み込み）
- エラーハンドリング強化（成果物が存在しない場合の代替処理）

---

## 10. 次のステップ

### 10.1 即座実行

1. ✅ **orchestrate-phase1 SKILL.md更新**（本レポート完成後、即座実施）
   - 新規2スキル（必須）を統合
   - STEP番号再採番
   - ステージゲート0追加

2. ⏳ **依存関係テスト**（1日以内）
   - `/estimate-market-size`の動作確認
   - `/map-customer-journey`の動作確認

### 10.2 短期（1週間以内）

3. ⏳ **オプションスキル統合**（3日以内）
   - `prioritize-features`、`design-ab-test`、`generate-kpi-dashboard`を条件付き実行として実装

4. ⏳ **ドキュメント更新**（1週間以内）
   - 新規成果物テンプレート作成
   - orchestrate-phase1実行例更新

### 10.3 中期（2週間以内）

5. ⏳ **エンドツーエンドテスト**（2週間以内）
   - 仮想アイデアで全STEP実行
   - 所要時間、成果物、ステージゲート判定の検証

---

## 付録: 統合前後の比較表

| 項目 | 統合前 | 統合後（必須のみ） | 統合後（全オプション含む） |
|-----|--------|------------------|------------------------|
| **ステップ数** | 12 | 14 | 17 |
| **所要時間** | 3-6時間 | 4-7時間 | 5.5-8.5時間 |
| **依存スキル数** | 12 | 14 | 17 |
| **ステージゲート数** | 2 | 3 | 3 |
| **成果物数** | 13 | 15 | 18 |
| **起業の科学準拠率** | 100% | 100% | 100% |

---

**作成者**: Claude Sonnet 4.5
**作成日**: 2025-12-31
**ステータス**: ✅ 完了
**次のアクション**: orchestrate-phase1 SKILL.md更新
