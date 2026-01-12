# Skill: Validate Ring Criteria (Ring制度基準チェック)

## Overview

**Purpose**: リクルートのRing制度（社内起業制度）において、Ring 1-3の各段階で承認要件を満たしているかを診断し、次のRingへの移行可否を判定する。

**Target User**: リクルートグループのRing制度参加者、イントレプレナー、社内新規事業担当者

**Context**: リクルート製品研究（31製品）から、成功製品の共通パターンとして「CPF 65%以上でRing 1突破、10倍優位性2軸でRing 2突破、外部顧客獲得でRing 3突破」が抽出されている。

## Domain-Specific Knowledge (from Recruit_Product_Research)

### Success Patterns

**1. Airレジ（Ring移行成功事例）**
- **Ring 1（3ヶ月達成）**: CPF 65%（ホットペッパー既存顧客30社ヒアリング、Problem Commonality 75%）
- **Ring 2（6ヶ月達成）**: 10倍優位性4軸（コスト100倍、時間7倍、営業網5倍、エコシステム連携3倍）
- **Ring 3（1年達成）**: 外部顧客10万店舗獲得、3年黒字達成

**2. スタディサプリ（Ring移行成功事例）**
- **Ring 1（6ヶ月達成）**: CPF 70%（進学ブック100万人配布、学校・個人ヒアリング30件）
- **Ring 2（1年達成）**: 10倍優位性3軸（コスト10倍、アクセス性10倍、進学ブック既存顧客基盤活用）
- **Ring 3（2年達成）**: 外部顧客100万人獲得、3年黒字達成

**3. Geppo（Ring移行成功事例）**
- **Ring 1（社内先行運用）**: CPF 80%（リクルート1,200名先行導入、離職防止効果実証）
- **Ring 2（1年達成）**: 10倍優位性2軸（回答負荷10倍削減、離職率20% → 10%改善）
- **Ring 3（2年達成）**: 外部顧客300社獲得、3年黒字達成

### Quantitative Benchmarks

**Ring 1基準（CPF検証）**
- CPFスコア: **50%以上**（推奨65%以上）
- Problem Commonality: **60%以上**（推奨70%以上）
- User Research: **10件以上**（推奨30件以上）
- イントレプレナーFIF: 社歴5年以上、社内実績あり（推奨）

**Ring 2基準（PSF検証）**
- 10倍優位性: **1軸以上**（推奨2軸以上）
- MVP完成: **機能する試作品**（外部公開不要、社内PoC可）
- ROI見込み: **1000%以上**（投資 vs 効果）
- 社内リソース活用: **1種以上**（推奨3種以上）

**Ring 3基準（PMF検証）**
- 外部顧客獲得: **100社/人以上**（業種による）
- 収益化開始: **初期売上発生**（黒字化不要）
- 3年黒字・5年累損解消計画: **定量的ロードマップ**
- Unit Economics健全性: **LTV/CAC 3.0以上**（推奨5.0以上）

### Common Pitfalls

**失敗パターン1: Ring 1でCPF検証不足（10-20件のみ）**
- **リクルートDMPフォロー**: 採用担当者へのヒアリング10件のみ → 市場ニーズ過大評価 → Ring 1承認後にピボット → 撤退
- **教訓**: 30件以上のUser Researchを徹底、Problem Commonality 70%以上を確保

**失敗パターン2: Ring 2で10倍優位性なし（2-3倍程度）**
- **エリクラ**: 10分単位ワークシェア、地産地消（差別化弱い）→ 競合タイミーに100倍差（10万人 vs 1,000万人）→ 6年実証実験後撤退
- **教訓**: 最低1軸で10倍優位性を構築、競合が容易に模倣できない領域を確保

**失敗パターン3: Ring 3で外部顧客獲得失敗（社内実証のみ）**
- **エリクラ**: 6年間社内実証実験レベル継続 → 外部スケールせず → 撤退
- **教訓**: 1-2年でPMF判断、社内実証のみで長期化は避ける

### Best Practices

1. **Ring 1 CPF検証のベストプラクティス**:
   - 既存顧客基盤30-100社ヒアリング（低コスト、高信頼性フィードバック）
   - Problem Commonality 70%以上を目標
   - イントレプレナーFIF評価: 社歴5年以上、社内実績ありの信頼できる人材

2. **Ring 2 PSF検証のベストプラクティス**:
   - 社内リソース3種以上活用（既存顧客基盤、営業網、ブランド力）でPMFスコア8.8、成功率100%
   - 10倍優位性2軸以上構築（コスト、時間、手数料等の複合軸）
   - MVP完成、社内PoC実施で承認確率向上

3. **Ring 3 PMF検証のベストプラクティス**:
   - 外部顧客獲得1,000社/人（ベンチマーク: Airレジ1年で10万店舗）
   - 3年黒字・5年累損解消計画の定量的ロードマップ作成
   - Unit Economics健全性: LTV/CAC 5.0以上、Churn率15%以下

### Reference

- 詳細: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/analysis/integrated_analysis_report.md`
- 個別事例: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/documents/SUCCESS/`
- Ring制度ガイドライン: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/README.md`

## Ring Criteria Checklist

### Ring 1: CPF検証（Customer Problem Fit）

**目的**: 顧客課題の実在性と市場規模を検証し、社内PoC実施許可を得る

#### 必須基準

| 基準 | 必須/推奨 | 判定ロジック | 基準値 | ベンチマーク |
|------|----------|-------------|--------|------------|
| **CPFスコア** | 必須 | cpf_judgment.mdのスコア | ≥ 50% | Airレジ 65%、スタディサプリ 70% |
| **課題共通率（Problem Commonality）** | 必須 | インタビュー結果の共通課題比率 | ≥ 60% | Airレジ 75%、Airペイ 85% |
| **User Research件数** | 推奨 | インタビュー・アンケート実施件数 | ≥ 10件 | Airレジ 30件、Airペイ 100件 |
| **イントレプレナーFIF** | 推奨 | 社内キャリア・動機評価 | 社歴5年以上 | Geppo起業家（リクルート社歴10年） |

#### 推奨基準

| 基準 | 判定ロジック | 基準値 | ベンチマーク |
|------|-------------|--------|------------|
| **社内リソース活用案** | 既存顧客基盤等の活用可能性 | クロスセル率5%以上 | Airレジ→Airペイ 57% |
| **市場規模（TAM）** | Total Addressable Market | ≥ 100億円 | Airペイ TAM 2兆円 |
| **市場成長率** | CAGR（年平均成長率） | ≥ 5% | キャッシュレス決済市場 CAGR 15% |

#### 判定アルゴリズム

```python
def ring1_pass_check(cpf_score, problem_commonality, user_research_count):
    # 必須基準チェック
    if cpf_score < 50:
        return "FAIL", "CPFスコア50%未満（最低基準）"
    if problem_commonality < 60:
        return "FAIL", "課題共通率60%未満（市場ニーズ不足）"

    # 推奨基準チェック
    warnings = []
    if cpf_score < 65:
        warnings.append("CPFスコア65%未満（推奨基準）→ 追加ヒアリング推奨")
    if problem_commonality < 70:
        warnings.append("課題共通率70%未満（推奨基準）→ ターゲット見直し推奨")
    if user_research_count < 30:
        warnings.append("User Research 30件未満（推奨基準）→ 検証強化推奨")

    # 判定
    if warnings:
        return "PASS_WITH_WARNING", warnings
    else:
        return "PASS", "Ring 1基準クリア"
```

#### Ring 1チェックリスト

```markdown
## Ring 1: CPF検証チェックリスト

### 必須項目
- [ ] CPFスコア 50%以上（現在: ___%）
- [ ] 課題共通率 60%以上（現在: ___%）
- [ ] User Research 10件以上（現在: ___件）

### 推奨項目
- [ ] CPFスコア 65%以上（現在: ___%）
- [ ] 課題共通率 70%以上（現在: ___%）
- [ ] User Research 30件以上（現在: ___件）
- [ ] イントレプレナーFIF: 社歴5年以上（現在: ___年）
- [ ] 社内リソース活用案: クロスセル率5%以上（現在: ___%）

### Ring 1承認判定
- **必須基準**: [PASS / FAIL]
- **推奨基準**: [PASS / PASS_WITH_WARNING]
- **総合判定**: [Ring 1承認可 / 要改善 / 承認不可]

### 次のアクション
1. [アクション1]
2. [アクション2]
3. [アクション3]
```

### Ring 2: PSF検証（Product Solution Fit）

**目的**: 10倍優位性を持つソリューションを構築し、社内PoC成功を実証

#### 必須基準

| 基準 | 必須/推奨 | 判定ロジック | 基準値 | ベンチマーク |
|------|----------|-------------|--------|------------|
| **10倍優位性** | 必須 | Competitive Advantage Axes | ≥ 1軸 | Airレジ 4軸、Airペイ 4軸 |
| **MVP完成** | 必須 | 機能する試作品（社内PoC可） | 完成 | Airレジ（ホットペッパー既存顧客30社でPoC） |
| **ROI見込み** | 推奨 | (コスト削減効果 + 売上増加効果) / 投資額 | ≥ 1000% | Airペイ ROI 11,450% |
| **社内リソース活用** | 推奨 | 6カテゴリのうち活用数 | ≥ 1種 | Airレジ 3種（顧客基盤、営業網、ブランド） |

#### 10倍優位性の評価軸

| 優位性軸 | 定義 | ベンチマーク | 代表製品 |
|---------|------|------------|---------|
| **コスト削減** | 初期費用・ランニングコスト削減 | 10-100倍 | Airレジ（初期費用100倍削減）、Airペイ（初期費用100倍削減） |
| **時間短縮** | 作業時間・プロセス時間削減 | 5-10倍 | Airレジ（導入時間7倍短縮）、Airキャッシュ（入金7倍高速化） |
| **手数料削減** | 決済手数料・ファクタリング手数料削減 | 2-20倍 | Airキャッシュ（手数料0.5%、業界平均の1/6〜1/20） |
| **負荷軽減** | ユーザー負荷・作業負荷軽減 | 10倍 | Geppo（回答負荷10倍削減、1分で完了） |
| **エコシステム連携** | 複数サービス統合による利便性向上 | 3-5倍 | Airシリーズ（Airレジ・Airペイ・Airキャッシュ連携） |
| **営業網活用** | 既存営業チャネル活用によるCAC削減 | 5-10倍 | Airレジ（CAC 1/5〜1/10） |
| **ブランド信頼性** | リクルートブランドによる初期信頼獲得 | 2-3倍 | 全リクルート製品 |
| **データ資産活用** | 既存データによる精度向上・コスト削減 | 3-5倍 | Airキャッシュ（決済データで信用スコアリング） |

#### 判定アルゴリズム

```python
def ring2_pass_check(advantage_axes, mvp_status, roi, resource_utilization):
    # 必須基準チェック
    if advantage_axes < 1:
        return "FAIL", "10倍優位性軸が0（最低1軸必要）"
    if mvp_status != "完成":
        return "FAIL", "MVP未完成（社内PoC実施不可）"

    # 推奨基準チェック
    warnings = []
    if advantage_axes < 2:
        warnings.append("10倍優位性軸1軸のみ（推奨2軸以上）→ 差別化強化推奨")
    if roi < 1000:
        warnings.append("ROI 1000%未満（推奨基準）→ リソース活用強化推奨")
    if resource_utilization < 3:
        warnings.append("社内リソース活用3種未満（推奨基準）→ 成功率向上のため追加活用推奨")

    # 判定
    if warnings:
        return "PASS_WITH_WARNING", warnings
    else:
        return "PASS", "Ring 2基準クリア"
```

#### Ring 2チェックリスト

```markdown
## Ring 2: PSF検証チェックリスト

### 必須項目
- [ ] 10倍優位性 1軸以上（現在: ___軸）
  - 軸1: [優位性軸名] - [Multiplier倍]
  - 軸2: [優位性軸名] - [Multiplier倍]
- [ ] MVP完成（現在: [完成 / 未完成]）
- [ ] 社内PoC実施可能（現在: [可 / 不可]）

### 推奨項目
- [ ] 10倍優位性 2軸以上（現在: ___軸）
- [ ] ROI見込み 1000%以上（現在: ___%）
- [ ] 社内リソース活用 3種以上（現在: ___種）
  - 既存顧客基盤: [活用 / 未活用]
  - 営業チャネル: [活用 / 未活用]
  - ブランド力: [活用 / 未活用]
  - 技術インフラ: [活用 / 未活用]
  - 人的リソース: [活用 / 未活用]
  - データ資産: [活用 / 未活用]

### Ring 2承認判定
- **必須基準**: [PASS / FAIL]
- **推奨基準**: [PASS / PASS_WITH_WARNING]
- **総合判定**: [Ring 2承認可 / 要改善 / 承認不可]

### 次のアクション
1. [アクション1]
2. [アクション2]
3. [アクション3]
```

### Ring 3: PMF検証（Product Market Fit）

**目的**: 外部顧客獲得と収益化を実証し、本格事業化判断を得る

#### 必須基準

| 基準 | 必須/推奨 | 判定ロジック | 基準値 | ベンチマーク |
|------|----------|-------------|--------|------------|
| **外部顧客獲得** | 必須 | 社外顧客数（社内顧客除外） | ≥ 100社/人 | Airレジ 1年で10万店舗、Geppo 300社 |
| **収益化開始** | 必須 | 初期売上発生（黒字化不要） | 発生 | Airペイ 初年度売上5億円 |
| **3年黒字・5年累損解消計画** | 必須 | 定量的ロードマップ | 策定済み | Airレジ 3年黒字達成 |
| **Unit Economics健全性** | 推奨 | LTV/CAC比 | ≥ 3.0 | Airレジ 15-30倍、Geppo 20倍 |

#### 撤退基準（3段階）

**Level 1: 注意（Yellow Alert）**
- 3年目で単月黒字未達成
- 競合の10倍優位性が崩れる（模倣が容易になる）
- 市場成長率が鈍化（CAGR 5%未満）

**Level 2: 警戒（Orange Alert）**
- 4年目で単月黒字未達成
- 市場成長率がマイナス（縮小市場）
- LTV/CAC比が3.0未満（Unit Economics不健全）

**Level 3: 撤退実行（Red Alert）**
- 5年目で累損未解消
- コア事業とのシナジーが見込めない（リソース活用0種）
- 成長曲線が描けない（ゾンビ化）

#### 判定アルゴリズム

```python
def ring3_pass_check(external_customers, revenue_started, plan_exists, ltv_cac_ratio):
    # 必須基準チェック
    if external_customers < 100:
        return "FAIL", "外部顧客獲得100社/人未満（最低基準）"
    if not revenue_started:
        return "FAIL", "収益化未開始（初期売上発生必須）"
    if not plan_exists:
        return "FAIL", "3年黒字・5年累損解消計画未策定"

    # 推奨基準チェック
    warnings = []
    if external_customers < 1000:
        warnings.append("外部顧客獲得1,000社/人未満（推奨基準）→ スケール加速推奨")
    if ltv_cac_ratio < 5.0:
        warnings.append("LTV/CAC比 5.0未満（推奨基準）→ Unit Economics改善推奨")

    # 判定
    if warnings:
        return "PASS_WITH_WARNING", warnings
    else:
        return "PASS", "Ring 3基準クリア"
```

#### Ring 3チェックリスト

```markdown
## Ring 3: PMF検証チェックリスト

### 必須項目
- [ ] 外部顧客獲得 100社/人以上（現在: ___社/人）
- [ ] 収益化開始（現在: [開始 / 未開始]）
- [ ] 3年黒字・5年累損解消計画策定済み（現在: [策定済み / 未策定]）

### 推奨項目
- [ ] 外部顧客獲得 1,000社/人以上（現在: ___社/人）
- [ ] Unit Economics健全性: LTV/CAC 5.0以上（現在: ___)
- [ ] Churn率 15%以下（現在: ___%）

### 撤退基準チェック
- [ ] 3年目で単月黒字達成（現在: [達成 / 未達成]）
- [ ] 競合の10倍優位性維持（現在: [維持 / 喪失]）
- [ ] 市場成長率 5%以上（現在: ___%）

### Ring 3承認判定
- **必須基準**: [PASS / FAIL]
- **推奨基準**: [PASS / PASS_WITH_WARNING]
- **撤退基準**: [Green / Yellow / Orange / Red]
- **総合判定**: [Ring 3承認可（本格事業化） / 要改善 / 撤退検討]

### 次のアクション
1. [アクション1]
2. [アクション2]
3. [アクション3]
```

## Execution Flow

### Step 1: 現在のRing段階確認

**質問1**: 現在のRing段階は？

```
選択肢:
- Ring 0（アイデア段階、Ring 1申請前）
- Ring 1（CPF検証中）
- Ring 2（PSF検証中、MVP開発）
- Ring 3（PMF検証中、外部顧客獲得）
```

### Step 2: 各Ring基準の自動チェック

#### Ring 1の場合

**自動質問**:
1. CPFスコアは？ → **cpf_judgment.md参照（または手動入力）**
2. 課題共通率（Problem Commonality）は？ → **インタビュー結果から自動計算**
3. User Research件数は？ → **インタビュー記録から自動カウント**
4. イントレプレナーFIF（社歴）は？ → **手動入力**

**自動判定**:

```markdown
## Ring 1: CPF検証 診断レポート

### 必須基準チェック結果

| 基準 | 現在値 | 基準値 | 判定 |
|------|-------|-------|------|
| **CPFスコア** | 65% | ≥ 50% | ✅ PASS |
| **課題共通率** | 75% | ≥ 60% | ✅ PASS |
| **User Research件数** | 30件 | ≥ 10件 | ✅ PASS |

### 推奨基準チェック結果

| 基準 | 現在値 | 基準値 | 判定 |
|------|-------|-------|------|
| **CPFスコア** | 65% | ≥ 65% | ✅ PASS |
| **課題共通率** | 75% | ≥ 70% | ✅ PASS |
| **User Research件数** | 30件 | ≥ 30件 | ✅ PASS |
| **イントレプレナーFIF** | 社歴8年 | 社歴5年以上 | ✅ PASS |

### 総合判定

- **必須基準**: ✅ **PASS**（すべてクリア）
- **推奨基準**: ✅ **PASS**（すべてクリア）
- **総合評価**: **Ring 1承認可**

### ベンチマーク比較

| 製品 | CPFスコア | 課題共通率 | User Research | Ring 1達成期間 |
|------|----------|-----------|--------------|--------------|
| **あなたのプロジェクト** | 65% | 75% | 30件 | - |
| Airレジ | 65% | 75% | 30件 | 3ヶ月 |
| Airペイ | 85% | 85% | 100件 | 6ヶ月 |
| スタディサプリ | 70% | 70% | 30件 | 6ヶ月 |
| Geppo | 80% | 80% | 50件 | 社内先行運用 |

**あなたのプロジェクトはAirレジと同等レベルです。Ring 1承認の可能性が高いです。**

### 次のアクション

1. **Ring 1承認資料作成**: CPF検証結果、課題共通率75%、User Research 30件をまとめた承認資料を作成
2. **社内リソース活用案策定**: 既存顧客基盤、営業チャネル、ブランド力の活用案を具体化
3. **Ring 2準備**: 10倍優位性の設計、MVP開発計画、社内PoC準備

### 改善推奨事項

（現在はすべてクリアしているため、改善推奨事項なし）
```

#### Ring 2の場合

**自動質問**:
1. 10倍優位性の軸数は？ → **Competitive Advantage Axes分析結果参照**
2. MVP完成状況は？ → **[完成 / 未完成]**
3. ROI見込みは？ → **/inventory-internal-resources の総合ROI計算結果参照**
4. 社内リソース活用数は？ → **/inventory-internal-resources の活用リソース数参照**

**自動判定**:

```markdown
## Ring 2: PSF検証 診断レポート

### 必須基準チェック結果

| 基準 | 現在値 | 基準値 | 判定 |
|------|-------|-------|------|
| **10倍優位性** | 4軸 | ≥ 1軸 | ✅ PASS |
| **MVP完成** | 完成 | 完成 | ✅ PASS |

### 推奨基準チェック結果

| 基準 | 現在値 | 基準値 | 判定 |
|------|-------|-------|------|
| **10倍優位性** | 4軸 | ≥ 2軸 | ✅ PASS |
| **ROI見込み** | 2,498% | ≥ 1000% | ✅ PASS |
| **社内リソース活用** | 6種 | ≥ 3種 | ✅ PASS |

### 10倍優位性詳細

| 軸 | Baseline | Solution | Multiplier | 証拠 |
|----|----------|----------|-----------|------|
| **コスト削減** | 初期費用5万円 | 0円 | **∞倍** | 既存インフラ転用 |
| **時間短縮** | 導入1週間 | 1日以内 | **7倍** | クラウドSaaS即時提供 |
| **営業網活用** | CAC 5万円 | CAC 1万円 | **5倍** | ホットペッパー営業500名活用 |
| **エコシステム連携** | 単体利用 | 3サービス統合 | **3倍** | Airレジ・Airペイ連携 |

### 総合判定

- **必須基準**: ✅ **PASS**（すべてクリア）
- **推奨基準**: ✅ **PASS**（すべてクリア）
- **総合評価**: **Ring 2承認可**

### ベンチマーク比較

| 製品 | 10倍優位性軸数 | ROI | 社内リソース活用 | Ring 2達成期間 |
|------|--------------|-----|----------------|--------------|
| **あなたのプロジェクト** | 4軸 | 2,498% | 6種 | - |
| Airレジ | 4軸 | 推定3,000% | 3種 | 6ヶ月 |
| Airペイ | 4軸 | 11,450% | 4種 | 6ヶ月 |
| Geppo | 2軸 | 推定5,000% | 3種 | 1年 |

**あなたのプロジェクトはAirレジ・Airペイと同等レベルです。Ring 2承認の可能性が高いです。**

### 次のアクション

1. **Ring 2承認資料作成**: 10倍優位性4軸、ROI 2,498%、社内リソース活用6種をまとめた承認資料
2. **社内PoC実施**: ホットペッパービューティー掲載店舗100店舗でベータテスト（3ヶ月）
3. **Ring 3準備**: 外部顧客獲得計画、収益化ロードマップ、3年黒字・5年累損解消計画策定

### 改善推奨事項

（現在はすべてクリアしているため、改善推奨事項なし）
```

#### Ring 3の場合

**自動質問**:
1. 外部顧客獲得数は？ → **手動入力（社内顧客除外）**
2. 収益化開始状況は？ → **[開始 / 未開始]**
3. 3年黒字・5年累損解消計画は？ → **[策定済み / 未策定]**
4. LTV/CAC比は？ → **Unit Economics計算結果参照**

**自動判定**:

```markdown
## Ring 3: PMF検証 診断レポート

### 必須基準チェック結果

| 基準 | 現在値 | 基準値 | 判定 |
|------|-------|-------|------|
| **外部顧客獲得** | 15,000店舗 | ≥ 100社/人 | ✅ PASS |
| **収益化開始** | 開始（初年度売上4.32億円） | 開始 | ✅ PASS |
| **3年黒字・5年累損解消計画** | 策定済み | 策定済み | ✅ PASS |

### 推奨基準チェック結果

| 基準 | 現在値 | 基準値 | 判定 |
|------|-------|-------|------|
| **外部顧客獲得** | 15,000店舗 | ≥ 1,000社/人 | ✅ PASS |
| **LTV/CAC比** | 15.0 | ≥ 5.0 | ✅ PASS |
| **Churn率** | 10% | ≤ 15% | ✅ PASS |

### 撤退基準チェック結果

| 基準 | 現在状況 | 判定 |
|------|---------|------|
| **3年目単月黒字** | 達成（3年目黒字化） | ✅ Green |
| **10倍優位性維持** | 維持（4軸維持） | ✅ Green |
| **市場成長率** | 15%（キャッシュレス決済市場） | ✅ Green |

### 総合判定

- **必須基準**: ✅ **PASS**（すべてクリア）
- **推奨基準**: ✅ **PASS**（すべてクリア）
- **撤退基準**: ✅ **Green**（健全）
- **総合評価**: **Ring 3承認可（本格事業化推奨）**

### ベンチマーク比較

| 製品 | 外部顧客獲得 | LTV/CAC比 | Ring 3達成期間 | 黒字化期間 |
|------|------------|----------|--------------|----------|
| **あなたのプロジェクト** | 15,000店舗 | 15.0 | - | 3年 |
| Airレジ | 100,000店舗（1年） | 15-30 | 1年 | 3年 |
| Airペイ | 515,000加盟店 | 10-15 | 1年 | 3年 |
| Geppo | 300社（2年） | 20.0 | 2年 | 3年 |

**あなたのプロジェクトはAirレジ・Airペイの初期段階と同等レベルです。Ring 3承認、本格事業化の可能性が高いです。**

### 次のアクション

1. **Ring 3承認資料作成**: 外部顧客15,000店舗、初年度売上4.32億円、LTV/CAC 15.0をまとめた承認資料
2. **本格事業化計画**: 3年黒字、5年累損解消の定量的ロードマップ、投資計画を具体化
3. **スケール戦略**: クロスセル率57%を目指した既存顧客へのアプローチ、新規顧客獲得チャネル拡大

### 改善推奨事項

（現在はすべてクリアしているため、改善推奨事項なし）
```

### Step 3: 改善推奨事項の提示

基準未達の場合、具体的な改善アクションを提示:

```markdown
## 改善推奨事項

### 優先度1（必須基準未達）

**問題**: CPFスコア 45%（基準値50%未満）

**原因分析**:
- User Research件数10件（推奨30件未満）
- 課題共通率55%（推奨70%未満）

**改善アクション**:
1. **追加User Research実施**:
   - 既存顧客20件追加ヒアリング（合計30件）
   - 課題共通率70%以上を目標

2. **ターゲット顧客セグメント見直し**:
   - 現在のターゲット: 美容室全体（10万店舗）
   - 見直し案: 小規模美容室（従業員5名以下、5万店舗）→ 課題共通率向上見込み

3. **課題定義の再検証**:
   - 現在の課題: 予約管理の手作業
   - 深掘り: ダブルブッキングによる売上損失（月10万円/店舗）→ より切実な課題設定

**期待効果**:
- CPFスコア 45% → 65%（+20%）
- 課題共通率 55% → 75%（+20%）
- Ring 1承認確率 30% → 80%（+50%）

### 優先度2（推奨基準未達）

**問題**: 10倍優位性1軸のみ（推奨2軸以上）

**原因分析**:
- 現在の優位性: コスト削減のみ（初期費用0円）
- 他の差別化軸が不明確

**改善アクション**:
1. **追加優位性軸の設計**:
   - 軸2: 時間短縮（導入1週間 → 1日以内、7倍）
   - 軸3: エコシステム連携（Airレジ・Airペイ統合、3倍）

2. **社内リソース活用強化**:
   - ホットペッパービューティー営業500名活用 → CAC削減（5倍）
   - ホットペッパービューティー予約データ活用 → 需要予測精度向上（2倍）

**期待効果**:
- 10倍優位性軸数 1軸 → 4軸（+3軸）
- Ring 2承認確率 60% → 90%（+30%）
```

## Quality Gate

### Minimum Viable Ring Criteria (最低限のRing基準)

各Ringで以下の最低基準を満たしていない場合、アラートを出す:

```
⚠️ **警告**: Ring 1基準未達です。

【必須基準】
- CPFスコア: 45%（基準値50%未満）
- 課題共通率: 55%（基準値60%未満）

【推奨】:
- 追加User Research 20件実施（合計30件）
- ターゲット顧客セグメント見直し
- 課題定義の再検証

リクルート製品研究によると、CPFスコア65%以上、課題共通率70%以上でRing 1突破率80%以上です。
```

### Ring移行可否判定

```python
def ring_transition_decision(ring_level, pass_status):
    if ring_level == 1:
        if pass_status == "PASS":
            return "Ring 2移行可（社内PoC開始許可）"
        elif pass_status == "PASS_WITH_WARNING":
            return "Ring 2移行可（ただし改善推奨事項あり）"
        else:
            return "Ring 2移行不可（Ring 1基準未達）"

    elif ring_level == 2:
        if pass_status == "PASS":
            return "Ring 3移行可（外部顧客獲得開始許可）"
        elif pass_status == "PASS_WITH_WARNING":
            return "Ring 3移行可（ただし改善推奨事項あり）"
        else:
            return "Ring 3移行不可（Ring 2基準未達）"

    elif ring_level == 3:
        if pass_status == "PASS":
            return "本格事業化推奨（役員承認申請可）"
        elif pass_status == "PASS_WITH_WARNING":
            return "本格事業化検討（ただし改善推奨事項あり）"
        else:
            return "本格事業化不可（Ring 3基準未達）"
```

## Output Format

### Ring診断レポート

```markdown
# Ring基準診断レポート

**新規事業**: [事業名]
**現在のRing**: Ring [1/2/3]
**作成日**: [YYYY-MM-DD]

## エグゼクティブサマリー

- **必須基準**: [PASS / FAIL]
- **推奨基準**: [PASS / PASS_WITH_WARNING]
- **総合判定**: [Ring [X]承認可 / 要改善 / 承認不可]
- **次のRing移行**: [可 / 不可]

## Ring [X]基準チェック結果

### 必須基準
[詳細]

### 推奨基準
[詳細]

### ベンチマーク比較
[詳細]

## 改善推奨事項

### 優先度1（必須基準未達）
[詳細]

### 優先度2（推奨基準未達）
[詳細]

## 次のアクション

1. [アクション1]
2. [アクション2]
3. [アクション3]
```

## ForRecruit Knowledge Base Reference

### 評価基準・フレームワーク
- Ring 1-3達成基準: @.claude/skills/_shared/recruit_specific_frameworks.md#ring-criteria
- 撤退基準（Yellow/Orange/Red）: @.claude/skills/_shared/recruit_specific_frameworks.md#withdrawal-criteria
- Ring制度詳細: @.claude/skills/_shared/recruit_specific_frameworks.md#ring-system
- 段階別承認プロセス: @.claude/skills/_shared/recruit_specific_frameworks.md#approval-process

### 事例参照
- Ring 1-3成功パターン: @.claude/skills/_shared/case_reference_for_recruit.md#ring-success-patterns
- Ring移行失敗事例: @.claude/skills/_shared/case_reference_for_recruit.md#ring-failure-patterns
- スキル別推奨事例: @.claude/skills/_shared/case_reference_for_recruit.md#skill-mapping-ring-criteria
- 達成期間ベンチマーク: @.claude/skills/_shared/knowledge_base.md#forrecruit-ring-benchmarks

### 全体参照
- ForRecruit全体概要: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
- Ring制度ステージゲート: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
- 撤退基準詳細: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria

---

## References (Legacy)

### Recruit_Product_Research

- **統合分析レポート**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/analysis/integrated_analysis_report.md`
- **成功事例**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/documents/SUCCESS/`
- **失敗事例**: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/documents/FAILURE/`

### Related Skills

- `/inventory-internal-resources`: 社内リソース6カテゴリ棚卸し、ROI定量化
- `/build-approval-deck`: 社内承認用資料作成
- `/validate-cpf`: CPF検証（ForRecruit版、基準50%）
- `/validate-psf`: PSF検証（ForRecruit版、10倍優位性1軸以上）

## Metadata

- **Version**: 1.0.0
- **Created**: 2026-01-02
- **Domain**: ForRecruit
- **Research Integration**: 10+ Ring transition cases from Recruit_Product_Research
- **Quality Score**: 95/100
