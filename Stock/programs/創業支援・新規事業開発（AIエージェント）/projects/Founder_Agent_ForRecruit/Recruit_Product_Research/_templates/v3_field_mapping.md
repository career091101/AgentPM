# Corporate Product Research v3 Template - Field Mapping

## Overview

このドキュメントは、Founder Research テンプレートから Corporate Product Research v3 への適応マッピングを定義します。

**作成日**: 2025-12-30
**テンプレートバージョン**: v3.0
**総YAMLフィールド数**: 55
**総コンテンツセクション数**: 13
**総行数**: 834行

---

## YAMLフロントマター対応表（55フィールド）

### 基本メタデータ（10フィールド）

| Founder Research | Corporate Product v3 | 変更内容 |
|-----------------|---------------------|---------|
| id | id | CORP_SXXX/CORP_FXXX形式に変更 |
| title | title | "製品名 - 企業名"形式 |
| category: "founder" | category: "corporate_product" | 固定値変更 |
| tier | tier | 企業製品向けに再定義 |
| type | type | success/failure/pivotの3種 |
| version | version | v3.0 |
| created_at | created_at | 同じ |
| updated_at | updated_at | 同じ |
| tags | tags | 製品カテゴリ用に調整 |
| - | - | - |

### 製品情報（14フィールド）← founder（4フィールド）+ company（4フィールド）

| Founder Research | Corporate Product v3 | 適応内容 |
|-----------------|---------------------|---------|
| company.name | product.name | 製品名（英語） |
| - | product.name_ja | 製品名（日本語）※新規 |
| founder.name | product.product_manager | 創業者→PM/責任者 |
| - | product.division_leader | 事業部長※新規 |
| - | product.parent_company | 親会社※新規 |
| - | product.division | 事業部門※新規 |
| company.founded_year | product.launched_year | 創業年→ローンチ年 |
| company.current_status | product.current_status | 同じ概念 |
| - | product.monthly_active_users | MAU※新規 |
| - | product.market_share | 市場シェア※新規 |
| company.valuation | product.revenue_latest | 評価額→売上に変更 |
| - | product.valuation | M&A/評価額※新規 |
| company.employees | product.employees | 同じ |
| - | product.website_url | 公式URL※新規 |

### M&A情報（6フィールド）※新規カテゴリ

| Founder Research | Corporate Product v3 | 適応内容 |
|-----------------|---------------------|---------|
| - | acquisition.is_acquired | M&A有無※新規 |
| - | acquisition.acquisition_date | 買収日※新規 |
| - | acquisition.acquired_from | 買収元※新規 |
| - | acquisition.acquisition_price | 買収額※新規 |
| - | acquisition.integration_strategy | 統合戦略※新規 |
| - | acquisition.synergy_effects | シナジー※新規 |

### 撤退情報（9フィールド）← withdrawal（5フィールド）拡張

| Founder Research | Corporate Product v3 | 適応内容 |
|-----------------|---------------------|---------|
| outcome.category: "failure" | withdrawal.is_withdrawn | 撤退判定に変更 |
| - | withdrawal.shutdown_date | 撤退日※新規 |
| withdrawal.reason | withdrawal.shutdown_reason | リクルート基準に対応 |
| withdrawal.three_year_profitability | withdrawal.three_year_profitability | 同じ（リクルート基準） |
| withdrawal.five_year_cumulative_loss | withdrawal.five_year_cumulative_loss | 同じ（リクルート基準） |
| withdrawal.final_status | withdrawal.migration_path | より詳細に変更 |
| - | withdrawal.user_impact | ユーザー影響※新規 |
| - | withdrawal.lessons_learned | 教訓※新規 |
| - | withdrawal.successor_product | 後継製品※新規 |

### 市場・ビジネスモデル（8フィールド）※新規カテゴリ

| Founder Research | Corporate Product v3 | 適応内容 |
|-----------------|---------------------|---------|
| - | market.tam_size | TAM※新規 |
| - | market.sam_size | SAM※新規 |
| - | market.som_size | SOM※新規 |
| - | market.pricing_model | 価格モデル※新規 |
| - | market.average_revenue_per_user | ARPU※新規 |
| - | market.customer_acquisition_cost | CAC※新規 |
| - | market.lifetime_value | LTV※新規 |
| - | market.unit_economics_status | Unit Economics判定※新規 |

### orchestrate-phase1検証（12フィールド）← validation_data拡張

#### CPF検証（5フィールド）

| Founder Research | Corporate Product v3 | 適応内容 |
|-----------------|---------------------|---------|
| validation_data.cpf.interview_count | validation_data.cpf.user_research_count | インタビュー→ユーザーリサーチに拡張 |
| validation_data.cpf.problem_commonality | validation_data.cpf.market_need_percentage | 課題共通率→市場ニーズ率 |
| validation_data.cpf.wtp_confirmed | validation_data.cpf.wtp_confirmed | 同じ |
| validation_data.cpf.urgency_score | validation_data.cpf.urgency_score | 同じ |
| validation_data.cpf.validation_method | validation_data.cpf.validation_method | 企業内検証を追加 |

#### PMF検証（5フィールド）← PSF → PMFに変更

| Founder Research | Corporate Product v3 | 適応内容 |
|-----------------|---------------------|---------|
| validation_data.psf.ten_x_axes | validation_data.pmf.competitive_advantage_axes | PSF→PMFに名称変更、2倍でも可に緩和 |
| validation_data.psf.mvp_type | validation_data.pmf.mvp_type | 同じ |
| validation_data.psf.initial_cvr | - | 削除（pmf_scoreに統合） |
| validation_data.psf.uvp_clarity | validation_data.pmf.pmf_score | UVP明確性→PMFスコアに変更 |
| validation_data.psf.competitive_advantage | validation_data.pmf.market_timing_score | 競合優位性→市場タイミングに変更 |

#### Pivot情報（2フィールド）

| Founder Research | Corporate Product v3 | 適応内容 |
|-----------------|---------------------|---------|
| validation_data.pivot.* | validation_data.pivot.* | 同じ構造（5フィールド） |

### 企業固有資産（3フィールド）← recruit_specific拡張

| Founder Research | Corporate Product v3 | 適応内容 |
|-----------------|---------------------|---------|
| recruit_specific.leveraged_assets | corporate_assets.leveraged_assets | リクルート→企業全般に拡張 |
| recruit_specific.synergy_with_existing | corporate_assets.existing_synergies | 名称変更 |
| - | corporate_assets.cross_sell_opportunities | クロスセル機会※新規 |

### 品質管理（3フィールド）

| Founder Research | Corporate Product v3 | 適応内容 |
|-----------------|---------------------|---------|
| quality.fact_check | quality.fact_check | 同じ |
| quality.sources_count | quality.sources_count | 同じ |
| quality.last_verified | quality.last_verified | 同じ |
| quality.primary_sources | quality.primary_sources | 同じ |

### 削除フィールド

以下のFounder Research固有フィールドは削除：
- `founder.*`（birth_year, nationality, education, prior_experience）
- `funding.*`（資金調達情報は本文に記載）
- `cross_reference.*`（必要に応じて本文に記載）
- `outcome.*`（withdrawal/successフィールドに統合）

---

## コンテンツ構造対応表（13セクション）

| # | Founder Research | Corporate Product v3 | 行数 | 変更内容 |
|---|-----------------|---------------------|------|---------|
| 1 | 基本情報 | **エグゼクティブサマリー** | 50 | 新規追加。3分で理解できる製品概要 |
| 2 | 基本情報 | 基本情報 | 30 | 製品概要テーブル形式 |
| 3 | 創業ストーリー | 製品開発ストーリー | 80 | CPF/PMF検証プロセス含む |
| 4 | ピボット/失敗経験 | **ピボット/失敗/撤退分析** | 60 | 撤退分析を詳細化 |
| 5 | 成長戦略 | **成長戦略・スケール** | 70 | 企業資産活用の定量化を追加 |
| 6 | - | **M&A統合戦略** | 40 | 新規追加。M&A製品のみ |
| 7 | - | **ビジネスモデル・Unit Economics** | 50 | 新規追加。収益構造詳細 |
| 8 | 使用ツール・サービス | 技術スタック | 30 | より詳細な技術情報 |
| 9 | 成功要因分析 | 成功/失敗要因分析 | 60 | 5W1H分析追加 |
| 10 | orchestrate-phase1への示唆 | orchestrate-phase1への示唆 | 40 | CPF/PSF/10x learnings |
| 11 | 日本市場適用性 | 他業界適用性 | 30 | 日本市場+他業界に拡張 |
| 12 | ファクトチェック結果 | ファクトチェック結果 | 20 | ✅/⚠️/❌判定 |
| 13 | 参照ソース | **参照ソース（Tier別分類）** | 20 | Tier 1-5の階層化 |

### セクション別詳細

#### セクション1: エグゼクティブサマリー（新規）

**目的**: 製品の本質を3分で理解できるようにする

**内容**:
- 製品の本質（What, Who, Why）
- キーメトリクステーブル
- 成功/失敗の核心要因（3つ）
- orchestrate-phase1スコア
- 3分でわかる学び

**Founder Researchとの違い**: 完全に新規追加。エグゼクティブ向けのダッシュボード的役割。

#### セクション4: ピボット/失敗/撤退分析（拡張）

**Founder Researchからの変更**:
- 撤退分析を大幅に拡張（60行）
- 5W1H分析を追加
- リクルート撤退基準（3年単月黒字、5年累損解消）の検証
- 撤退タイムラインテーブル

#### セクション5: 成長戦略・スケール（拡張）

**Founder Researchからの変更**:
- 企業資産活用の定量化テーブルを追加
- シナジー効果の定量化
- Unit Economicsの詳細分析
- フライホイールの可視化

#### セクション6: M&A統合戦略（新規）

**目的**: M&A製品の統合プロセスを詳細分析

**内容**:
- 買収の背景
- 統合プロセス（タイムライン）
- シナジー効果の定量化（期待値 vs 実績）
- M&A成功判定

#### セクション7: ビジネスモデル・Unit Economics（新規）

**目的**: 収益構造とUnit Economicsを詳細分析

**内容**:
- 収益モデル詳細
- 市場規模・ポジショニング（TAM/SAM/SOM）
- Unit Economics詳細（CAC/LTV/NRR/Churn等）
- 主要KPIテーブル

#### セクション13: 参照ソース（拡張）

**Founder Researchからの変更**:
- Tier 1-5の階層化
- ソース品質分析の追加
- Tier別の信頼度定義

---

## テンプレート使用ガイド

### 記載優先度

**最重要（必須）**:
1. エグゼクティブサマリー（セクション1）
2. 基本情報（セクション2）
3. 製品開発ストーリー（セクション3）
4. 成功/失敗要因分析（セクション9）
5. orchestrate-phase1への示唆（セクション10）

**重要（可能な限り記載）**:
6. ピボット/失敗/撤退分析（セクション4）
7. 成長戦略・スケール（セクション5）
8. ビジネスモデル・Unit Economics（セクション7）
9. ファクトチェック結果（セクション12）

**該当時のみ記載**:
10. M&A統合戦略（セクション6）- M&A製品のみ
11. 技術スタック（セクション8）- 技術情報が入手可能な場合
12. 他業界適用性（セクション11）- 応用可能性がある場合

### YAMLフィールド記載基準

**必須フィールド（15）**:
- id, title, category, tier, type, version, created_at, updated_at, tags
- product.name, product.parent_company, product.launched_year, product.current_status
- quality.fact_check, quality.sources_count

**推奨フィールド（20）**:
- product.* （全14フィールド）
- validation_data.cpf.* （全5フィールド）
- quality.last_verified

**該当時のみ（20）**:
- acquisition.* （M&A製品のみ）
- withdrawal.* （撤退製品のみ）
- market.* （データが入手可能な場合）
- validation_data.pmf.* （検証データがある場合）
- corporate_assets.* （企業資産活用が明確な場合）

### 未確認情報の扱い

**YAMLフィールド**:
- 数値フィールド: `null`
- 文字列フィールド: `""` (空文字)
- ブール値: `null`

**本文**:
- 「（推定）」を明記
- 「（公開情報なし）」を明記
- 「（1ソースのみ）」を明記

**ファクトチェック結果**:
- ✅ PASS: 2ソース以上で確認
- ⚠️ WARN: 1ソースのみ、または推定値
- ❌ FAIL: 確認不可、情報なし

---

## v2からv3への主要変更点

### YAMLフロントマター

1. **フィールド数増加**: 約30フィールド → 55フィールド
2. **M&A情報カテゴリ追加**: acquisition.* 6フィールド
3. **市場情報カテゴリ追加**: market.* 8フィールド
4. **撤退情報拡張**: withdrawal.* 5フィールド → 9フィールド
5. **PMF検証追加**: validation_data.pmf.* 5フィールド

### コンテンツ構造

1. **エグゼクティブサマリー追加**: 3分で理解できる概要（50行）
2. **M&A統合戦略追加**: M&A製品向けセクション（40行）
3. **ビジネスモデル詳細追加**: Unit Economics詳細分析（50行）
4. **撤退分析拡張**: 5W1H分析、タイムライン追加（60行）
5. **企業資産活用の定量化**: 数値ベースの効果測定

### 品質向上

1. **ソース階層化**: Tier 1-5の分類
2. **ファクトチェック強化**: ✅/⚠️/❌判定
3. **定量化重視**: 可能な限り数値で効果を測定
4. **エビデンス必須**: 全ての主張にソースを明記

---

## テンプレート設計思想

### Founder Researchからの適応方針

1. **創業者 → 製品**: 主体を「人」から「製品」に変更
2. **VC調達 → 企業資産**: 資金源を「外部資金」から「企業資産」に変更
3. **PSF → PMF**: スタートアップ向けPSFから、企業製品向けPMFに変更
4. **10倍必須 → 2倍でも可**: 企業製品は既存資産活用で2-5倍でも勝てる
5. **撤退基準追加**: リクルート等の撤退基準（3年/5年ルール）を追加

### orchestrate-phase1対応

**CPF検証**:
- ユーザーリサーチ数: 20回以上（企業内検証含む）
- 市場ニーズ率: 70%以上
- WTP確認率: 50%以上
- 緊急性スコア: 7/10以上

**PMF検証**:
- 競合優位性: 2軸以上で2倍以上（理想は10倍）
- MVP検証: 各種MVPタイプに対応
- PMFスコア: 7/10以上
- 市場タイミング: 7/10以上

### 企業製品特有の考慮事項

1. **既存資産の活用**: 営業網/ブランド/データ/プラットフォーム
2. **シナジー効果**: 既存事業とのデータ連携/クロスセル
3. **撤退基準**: 3年単月黒字/5年累損解消ルール
4. **M&A統合**: 買収後の統合プロセスと効果測定
5. **Unit Economics**: LTV/CAC、NRR等の詳細分析

---

## 今後の拡張予定

### v3.1（次期マイナーアップデート）

1. **競合分析セクション追加**: 詳細な競合マトリクス
2. **カスタマーサクセス指標**: NPS、CSAT、CES等
3. **プロダクトロードマップ**: 過去と未来のロードマップ

### v4.0（次期メジャーアップデート）

1. **グローバル展開分析**: 海外市場への展開プロセス
2. **規制対応**: 業界規制、法律対応の詳細
3. **サステナビリティ**: ESG観点の評価

---

**ドキュメント作成**: 2025-12-30
**作成者**: Agent 1 (Template v3 Creator)
**テンプレートパス**: `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Corporate_Product_Research/_templates/corporate_product_research_v3_template.md`
