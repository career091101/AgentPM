# Founder_Research 調査ガイドライン

最終更新: 2025-12-28
バージョン: 1.0

## 目的

このガイドラインは、Founder_Researchプロジェクトにおけるケーススタディ調査の品質を担保するための指針です。特に以下の2つのフィールドの記載基準を明確化します：

- **interview_count**: インタビュー実施数
- **problem_commonality**: 課題の共通性（%値）

---

## 1. interview_count 調査方法

### 1.1 優先情報源（優先度順）

1. **創業者の自伝・公式ブログ**
   - 例: "We interviewed 50 customers before building anything"
   - 信頼性: 最高（一次情報）

2. **書籍・ケーススタディ記事**
   - 例: "The Lean Startup" (Eric Ries), "Zero to One" (Peter Thiel)
   - 信頼性: 高

3. **インタビュー記事・ポッドキャスト**
   - 例: Y Combinator Startup School, Indie Hackers, Masters of Scale
   - 信頼性: 中〜高

4. **企業公式ドキュメント・IR資料**
   - 例: IPO目論見書、アニュアルレポート
   - 信頼性: 中

5. **業界レポート・メディア記事**
   - 例: TechCrunch, Forbes, Wall Street Journal
   - 信頼性: 中

### 1.2 記載基準

#### ケース1: 明示的な記載がある場合

創業者が具体的な数値を述べている場合、そのまま記載：

```yaml
interview_count: 50  # 例（要出典）: "We interviewed 50 customers before building anything"
interview_count: 100 # 例（要出典）: "We talked to over 100 companies"
interview_count: 20  # 例（要出典）: "I interviewed 20 creators"
```

**ソース記載例**:
```yaml
primary_sources:
  - "一次ソースのタイトル（例: Founder interview / 公式ブログ / 公式書籍）"
  - "https://example.com/..."
```

#### ケース2: 推定可能な場合

具体的な数値は無いが、実施したことが明記されている場合、保守的に推定：

```yaml
# "多くの顧客にインタビューした" → 最低20件と推定
interview_count: 20  # 推定: 定性情報より（"interviewed many customers"）

# "Lean Startup手法を実践" → 典型的に20-30件
interview_count: 25  # 推定: Lean Startup手法の標準実施数

# "徹底的な顧客調査を実施" + B2B SaaS → 業界標準は20-30社
interview_count: 25  # 推定: B2B SaaS業界標準
```

**推定基準表**:

| 記載内容 | 推定値 | 根拠 |
|---------|-------|------|
| "many customers" | 20 | 最低限の定性調査 |
| "extensive research" | 30 | Lean Startup標準 |
| "hundreds of interviews" | 100 | 明示的な大規模調査 |
| Lean Startup実践 | 25 | 手法の典型値 |
| B2B SaaS標準 | 25 | 業界ベンチマーク |
| Consumer標準 | 50 | 業界ベンチマーク |

#### ケース3: 情報源が全くない場合

インタビュー実施の記載が見当たらない場合、`0` を記載し、コメントで理由を明記：

```yaml
interview_count: 0  # 情報源なし、市場調査・アナリティクスのみと推測
interview_count: 0  # 技術者主導、プロダクトファースト（例: Instagram MVP）
```

**重要**: `null`のまま残さない！必ず `0` または推定値を記載する。

---

## 2. problem_commonality 調査方法

### 2.1 定義

**problem_commonality**: ターゲット市場において、その課題を抱える人の割合（%値）

例:
- （例）都市部居住者のうち「車を持たない/持ちたくない」割合
- （例）中小企業のうち「営業×マーケ連携に課題」割合
- （例）ナレッジワーカーのうち「ツール分散に不満」割合
  - ※上記の数値は出典が確認できた場合のみ記載（出典なしの断定は禁止）

### 2.2 優先情報源

1. **市場調査レポート・統計データ**
   - 例: Gartner, Forrester, McKinsey, Statista
   - 信頼性: 最高

2. **業界団体の調査**
   - 例: JASDAQ, 中小企業庁, SaaS業界団体
   - 信頼性: 高

3. **創業者のブログ・プレゼン資料**
   - 例: "90% of our target market has this problem"
   - 信頼性: 中〜高

4. **TAM/SAM/SOM分析**
   - 例: IPO目論見書の市場規模セクション
   - 信頼性: 中

### 2.3 記載基準

#### ケース1: 市場調査データがある場合

統計データから直接算出:

```yaml
problem_commonality: 80  # 例（要出典）: 調査レポートより算出（URLと該当箇所を必ず残す）
problem_commonality: 90  # 例（要出典）: 調査レポートより算出
problem_commonality: 75  # 例（要出典）: 統計データより算出
```

#### ケース2: TAM/SAM/SOMから逆算

```yaml
# 例: Airbnb
# TAM（都市部居住者）: 10億人
# SAM（旅行する人）: 5億人 → 50%
# SOM（Airbnb潜在顧客）: 2億人 → 20%（宿泊コスト重視層）

problem_commonality: 20  # 推定: 旅行者のうち宿泊コスト重視層の割合
```

#### ケース3: 業界ベンチマークから推定

具体的なデータがない場合、業界標準から推定:

| 業界 | 典型的な課題共通性 | 根拠 |
|------|-----------------|------|
| B2B SaaS（生産性） | 60-70% | 大半の企業が生産性課題を認識 |
| B2B SaaS（ニッチ） | 20-30% | 特定業界・職種に限定 |
| Consumer（大衆向け） | 50-70% | 広範なペインポイント |
| Consumer（ニッチ） | 10-20% | 特定セグメント |
| Developer Tools | 30-50% | 開発者の共通課題 |

```yaml
# 例: Notion（B2B SaaS、生産性）
problem_commonality: 65  # 推定: B2B生産性ツールの業界標準

# 例: Figma（Developer Tools、デザイナー向け）
problem_commonality: 40  # 推定: デザイナーの協業課題の共通性
```

#### ケース4: 定性情報のみの場合

保守的に推定し、コメントで根拠を記載:

```yaml
problem_commonality: 50  # 保守的推定: "多くのユーザーが課題を感じている"との記載のみ
problem_commonality: 30  # 保守的推定: "一部のパワーユーザーに深刻な課題"との記載
```

**重要**: `null`のまま残さない！必ず推定値を記載する。

---

## 3. その他の重要フィールド

### 3.1 wtp_confirmed (支払い意思)

```yaml
# 確認できた場合
wtp_confirmed: true  # プレオーダー、ベータ課金、ウェイトリスト等で確認

# 確認できなかった場合
wtp_confirmed: false  # 無料版のみでローンチ、MVP段階では無償提供
```

### 3.2 ten_x_axes (10倍優位性)

最低1軸、理想的には2-3軸記載:

```yaml
ten_x_axes:
  - axis: "コスト"
    multiplier: 10  # 従来$50/月 → $5/月
  - axis: "使いやすさ"
    multiplier: 12  # セットアップ1時間 → 5分
```

### 3.3 primary_sources

必ず3件以上のソースを記載:

```yaml
primary_sources:
  - "Founder interview（例: YC Interview 2013）"
  - "Airbnb S-1 Filing (SEC)"
  - "How Airbnb Started - Paul Graham Essay"
```

---

## 4. 調査プロセス（推奨ワークフロー）

### Step 1: 基本情報収集（10分）
1. Wikipedia で基本情報確認
2. Crunchbase/PitchBook で企業データ確認
3. 公式サイト・LinkedIn で現状確認

### Step 2: interview_count調査（20分）
1. Google検索: `"[founder name]" interview customer`
2. YouTube検索: `[founder name] startup story`
3. 書籍確認（該当する場合）
4. 結果を記載（明示 or 推定 or 0）

### Step 3: problem_commonality調査（20分）
1. Google検索: `"[problem]" market size statistics`
2. Gartner/Forrester/Statista 検索
3. IPO目論見書確認（該当する場合）
4. 結果を記載（統計 or TAM逆算 or 業界標準 or 保守的推定）

### Step 4: その他フィールド調査（30分）
1. 10倍優位性の特定
2. MVPタイプの確認
3. ピボット歴の確認

### Step 5: ファクトチェック（10分）
1. 最低3つのソースで裏付け
2. `fact_check: "pass"` を設定

**総所要時間**: 約90分/件

---

## 5. 品質チェックリスト

調査完了前に必ず確認:

- [ ] **interview_count**: 数値 or 0（nullのまま残さない）
- [ ] **problem_commonality**: %値（nullのまま残さない）
- [ ] **wtp_confirmed**: true/false 明記
- [ ] **ten_x_axes**: 最低1軸記載
- [ ] **mvp_type**: 記載
- [ ] **primary_sources**: 3件以上
- [ ] **fact_check**: pass確認
- [ ] **コメント**: 推定値には必ず根拠コメント

---

## 6. よくある質問（FAQ）

### Q1: interview_countが全く見つからない場合は？

A: `0` を記載し、コメントで理由を明記してください：
```yaml
interview_count: 0  # 情報源なし、プロダクト主導型スタートアップと推測
```

### Q2: problem_commonalityが推定困難な場合は？

A: 業界標準の50%を使用し、保守的推定である旨を記載：
```yaml
problem_commonality: 50  # 保守的推定: 定性情報のみ、業界標準を適用
```

### Q3: 複数のソースで数値が異なる場合は？

A: 最も信頼性の高いソースを採用し、他のソースもprimary_sourcesに記載：
```yaml
interview_count: 50  # 採用した一次ソース（最も信頼性高）
# 他のソースでは"40-60件"との記載もあり
```

### Q4: 日本企業の場合、英語ソースが少ない場合は？

A: 日本語ソースでも可。IRやメディアインタビューを活用：
```yaml
primary_sources:
  - "前澤友作 日経ビジネスインタビュー 2019年"
  - "ZOZO IR資料 2020年度"
  - "創業ストーリー（公式ブログ）"
```

---

## 7. バッチ調査時の効率化

### 同一業界の連続調査

同じ業界を連続で調査する際の効率化テクニック:

1. **共通ソースの事前準備**
   - Gartner SaaS Market Report → SaaS企業全体で使用
   - Forrester B2B Report → B2B企業全体で使用

2. **業界標準値の活用**
   - 参考値（経験則・要検証）: B2B SaaSの初期推定として `interview_count=25` など
   - 参考値（経験則・要検証）: Consumerの初期推定として `interview_count=50` など
   - ※「業界標準」を名乗る数値は、可能な限り統計/調査レポートで裏付ける

3. **テンプレートの再利用**
   - 10倍軸パターンが業界内で類似（SaaS: コスト/使いやすさ/統合性）

---

## 8. データ品質スコアリング

各フィールドの配点（100点満点）:

| フィールド | 配点 | 条件 |
|-----------|------|------|
| interview_count記載 | 10点 | 数値 or 推定値あり |
| problem_commonality記載 | 10点 | 数値 or 推定値あり |
| wtp_confirmed記載 | 10点 | true/false明記 |
| ten_x_axes記載 | 15点 | 2軸以上 |
| mvp_type記載 | 10点 | 具体的な記載 |
| primary_sources | 15点 | 3件以上 |
| fact_check pass | 30点 | pass判定 |
| **合計** | **100点** | |

**目標**: 平均85点以上

---

## 更新履歴

| 日時 | 更新内容 | 更新者 |
|------|---------|-------|
| 2025-12-28 | 初版作成 | Claude Code |

---

最終更新: 2025-12-28
バージョン: 1.0
