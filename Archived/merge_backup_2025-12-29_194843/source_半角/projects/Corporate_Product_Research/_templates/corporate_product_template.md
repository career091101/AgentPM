---
id: "CORP_SXXX" # or "CORP_FXXX" for failure
title: "製品名 - リクルート"
category: "corporate_product"
tier: "global_ma" # global_ma | mega_hit | saas | domestic_ma | new_business | clear_withdrawal | ma_failure | strategic_exit
type: "success" # success | failure
version: "1.0"
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
tags: []

# 基本情報
product:
  name: ""
  name_ja: ""
  parent_company: "Recruit Holdings"
  division: ""  # リクルート内の事業部門
  launched_year: null
  industry: ""
  current_status: "" # active | acquired | shutdown | merged
  revenue: ""  # 直近の売上（公開されている場合）
  valuation: ""  # M&A金額 or 評価額
  users: null  # ユーザー数

# M&A情報（該当する場合）
acquisition:
  occurred: false
  acquisition_year: null
  acquisition_price: ""  # $XXB, $XXM
  founder: ""
  original_company: ""
  integration_status: "" # success | partial | failure

# リクルート撤退基準（失敗事例のみ）
withdrawal:
  occurred: false
  withdrawal_year: null
  duration_months: null  # 創業から撤退までの月数
  reason: ""  # 3年単月黒字未達成 | 5年累損解消未達成 | 戦略的判断 | 市場縮小 | 競合激化
  three_year_profitability: null  # true/false/null（3年で単月黒字達成したか）
  five_year_cumulative_loss: null  # true/false/null（5年で累損解消したか）
  final_status: ""  # 完全撤退 | 売却 | 統合 | 縮小継続

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: null  # %値 or null
    wtp_confirmed: null  # true/false/null
    urgency_score: null  # 1-10 or null
    validation_method: ""  # 企業内検証/市場調査/ユーザーインタビュー等
  psf:
    ten_x_axes:
      - axis: ""
        multiplier: null
    mvp_type: ""  # concierge | wizard_of_oz | landing_page | prototype | other
    initial_cvr: null
    uvp_clarity: null  # 1-10 or null
    competitive_advantage: ""
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: ""
    original_idea: ""
    pivoted_to: ""

# リクルート製品特有フィールド
recruit_specific:
  leveraged_assets:  # 活用したリクルートの既存資産
    - asset_type: ""  # 営業網 | ブランド | データベース | プラットフォーム
      description: ""
  synergy_with_existing:  # 既存事業とのシナジー
    - business: ""
      synergy_type: ""  # データ連携 | クロスセル | ブランド共鳴
  internal_resistance: ""  # 社内抵抗の有無と内容

# クロスリファレンス
cross_reference:
  founder_id: "N/A"  # 創業者がFounder_Researchにいる場合
  related_products: []  # 関連するリクルート製品
  competitor_products: []  # 主要競合製品

# 品質管理
quality:
  fact_check: "pass" # pass | warn | fail
  sources_count: 0
  last_verified: "YYYY-MM-DD"
  primary_sources: []
---

# {製品名}

## 1. 基本情報

| 項目 | 内容 | ソース |
|------|------|--------|
| 製品名 | | |
| 運営企業 | リクルートホールディングス | |
| 事業部 | | |
| ローンチ年 | | |
| 撤退年（該当時） | | |
| 買収年（M&A時） | | |
| 買収額 | | |
| 現在の状況 | active/withdrawn/merged | |
| ピーク売上 | | |
| ピークユーザー数 | | |

## 2. 製品開発ストーリー

### 2.1 課題発見

**着想源**:
-

**Ring提案制度**（該当時）:
-

### 2.2 CPF検証（orchestrate-phase1基準）

**CPF達成判定**:

| 指標 | 目標 | 実績 | 判定 | エビデンス |
|------|------|------|:----:|----------|
| インタビュー数 | 20人以上 | XX人 | ✅/⚠️/❌ | |
| 課題共通率 | 70%以上 | XX% | ✅/⚠️/❌ | |
| WTP確認 | 50%以上 | XX% | ✅/⚠️/❌ | |
| 緊急性 | 7/10以上 | X.X/10 | ✅/⚠️/❌ | |

**総合判定**: ✅ CPF達成 / ⚠️ 要改善 / ❌ 未達成

**検証手法**:
-

### 2.3 PSF検証（10倍優位性）

**10倍優位性の検証**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 | エビデンス |
|---|------------|-----------------|------|----------|
| 時間 | | | | |
| コスト | | | | |
| 使いやすさ | | | | |

**達成軸数**: X軸（目標2軸以上）
**PSF達成判定**: ✅ 達成 / ⚠️ 要改善 / ❌ 未達成

**MVP**:
- タイプ:
- 初期反応:

**UVP**:
-

## 3. ピボット/失敗経験

### 3.1 初期の失敗

-

### 3.2 ピボット（該当する場合）

- 元のアイデア:
- ピボット後:
- きっかけ:
- 学び:

### 3.3 リクルート撤退基準の検証（失敗事例のみ）

**撤退判断のタイムライン**:
- 創業: YYYY年MM月
- 3年経過時点（YYYY年MM月）:
  - 単月黒字達成: ✅ / ❌
  - 判断: 継続 / 撤退検討開始
- 5年経過時点（YYYY年MM月）:
  - 累損解消: ✅ / ❌
  - 最終判断: 継続 / 撤退決定

**撤退理由の分析**:
| 要因 | 詳細 |
|------|------|
| 市場要因 | |
| 競合要因 | |
| 内部要因 | |
| リクルート基準 | 3年単月黒字未達成 / 5年累損解消未達成 |

**撤退後の処理**:
- 完全撤退 / 売却 / 統合 / 縮小継続
- 撤退による損失額: XX億円
- 撤退による学び:

## 4. 成長戦略

### 4.1 初期トラクション

-

### 4.2 フライホイール

-

### 4.3 スケール戦略

-

### 4.4 リクルート資産の活用

**活用した既存資産**:

| 資産タイプ | 具体的な活用方法 | 効果 |
|----------|---------------|------|
| 営業網 | | |
| ブランド | | |
| データベース | | |
| プラットフォーム | | |

**既存事業とのシナジー**:

| 既存事業 | シナジータイプ | 具体的な連携 |
|---------|-------------|------------|
| | データ連携 | |
| | クロスセル | |
| | ブランド共鳴 | |

## 5. M&A戦略（該当時）

### 5.1 買収理由

-

### 5.2 統合プロセス

-

### 5.3 シナジー効果

-

## 6. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | |
| マーケティング | |
| 分析 | |

## 7. 成功/失敗要因分析

### 7.1 主要成功要因（成功時）

1.
2.
3.

### 7.2 失敗要因（失敗時）

| フェーズ | 失敗要因 | 具体的内容 |
|---------|---------|----------|
| CPF | | |
| PSF | | |
| PMF | | |
| 戦略 | | |

## 8. orchestrate-phase1への示唆

### 8.1 /discover-demand への学び

-

### 8.2 /validate-cpf への学び

-

### 8.3 /validate-10x への学び

-

### 8.4 /startup-scorecard への学び

-

## 9. 他業界適用性

| 業界 | 適用可能性 | コメント |
|------|----------|---------|
| | | |

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| ローンチ年 | ✅/⚠️/❌ | |
| 買収額 | ✅/⚠️/❌ | |
| 撤退年 | ✅/⚠️/❌ | |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1.
2.
3.
