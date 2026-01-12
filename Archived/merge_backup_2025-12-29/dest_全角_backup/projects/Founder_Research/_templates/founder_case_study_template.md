---
id: "FOUNDER_XXX"
title: "創業者名 - 企業名"
category: "founder"
tier: "legendary" # legendary | unicorn | vc_backed | ipo_japan | ipo_global | pivot | failure | emerging
type: "case_study" # case_study | pivot_study | failure_study
version: "1.0"
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
tags: []

# 基本情報
founder:
  name: ""
  birth_year: null
  nationality: ""
  education: ""
  prior_experience: ""

company:
  name: ""
  founded_year: null
  industry: ""
  current_status: "" # active | acquired | ipo | shutdown
  valuation: "" # $XXB, $XXM, or "不明"
  employees: null

# VC投資情報（新規追加）
funding:
  total_raised: "" # "$XXM" or "不明"
  funding_rounds:
    - round: "" # seed | series_a | series_b | series_c | series_d
      date: "" # YYYY-MM-DD
      amount: "" # $XXM
      valuation_post: "" # $XXM (post-money valuation)
      lead_investors: []
      other_investors: []
  top_tier_vcs: [] # Y Combinator, Sequoia, a16z等

# 成功/失敗/Pivot分類（新規追加）
outcome:
  category: "" # success | failure | pivot
  subcategory: "" # exit_success | growth_success | shutdown | pivot_success等
  failure_pattern: "" # P11-P30（失敗時のみ）
  pivot_details: # pivot時のみ
    count: 0
    major_pivots:
      - id: ""
        trigger: "" # cpf_failure | psf_failure | market_shift
        date: ""
        decision_speed: ""
        before:
          idea: ""
          target_market: ""
          business_model: ""
          cpf_score: null
        after:
          idea: ""
          hypothesis: ""
        resources_preserved:
          team: ""
          technology: ""
          investors: ""
        validation_process:
          - stage: ""
            duration: ""
            result: ""

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null # 数値 or null（不明）
    problem_commonality: null # %値 or null
    wtp_confirmed: null # true/false/null
    urgency_score: null # 1-10 or null
    validation_method: "" # インタビュー/サーベイ/プロトタイプ等
  psf:
    ten_x_axes:
      - axis: ""
        multiplier: null
    mvp_type: "" # concierge | wizard_of_oz | landing_page | prototype | other
    initial_cvr: null # %値 or null
    uvp_clarity: null # 1-10 or null
    competitive_advantage: ""
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: "" # cpf_failure | psf_failure | market_shift | other
    original_idea: ""
    pivoted_to: ""

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []

# 品質管理
quality:
  fact_check: "pass" # pass | warn | fail
  sources_count: 0
  last_verified: "YYYY-MM-DD"
  primary_sources: []
---

# {創業者名} - {企業名}

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | |
| 生年 | |
| 国籍 | |
| 学歴 | |
| 創業前経験 | |
| 企業名 | |
| 創業年 | |
| 業界 | |
| 現在の状況 | |
| 評価額/時価総額 | |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- どのような課題に気づいたか
- なぜその課題に着目したか

**需要検証方法**:
- 市場調査の方法
- 初期の反応

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数:
- 手法:
- 発見した課題の共通点:

**3U検証**:
- Unworkable（現状では解決不可能）:
- Unavoidable（避けられない）:
- Urgent（緊急性が高い）:

**支払い意思（WTP）**:
- 確認方法:
- 結果:

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 |
|---|------------|-----------------|------|
| 時間 | | | |
| コスト | | | |
| 使いやすさ | | | |
| 成果 | | | |
| 導入障壁 | | | |

**MVP**:
- タイプ:
- 初期反応:
- CVR:

**UVP（独自の価値提案）**:
-

**競合との差別化**:
-

## 3. ピボット/失敗経験

### 3.1 初期の失敗

-

### 3.2 ピボット（該当する場合）

- 元のアイデア:
- ピボット後:
- きっかけ:
- 学び:

## 4. 成長戦略

### 4.1 初期トラクション獲得

-

### 4.2 フライホイール

-

### 4.3 スケール戦略

-

### 4.4 バリューチェーン

-

## 4.5 資金調達履歴（VC案件のみ）

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Seed | | | | | |
| Series A | | | | | |
| Series B | | | | | |

**総資金調達額**: $XXM
**主要VCパートナー**:

### 資金使途と成長への影響

**Series A（$XXM）**:
- プロダクト開発:
- マーケティング:
- 成長結果: ARR $XM → $YM（XX ヶ月）

### VC関係の構築

1. **YC/VC選考突破**:
2. **投資家との関係維持**:

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | |
| マーケティング | |
| 分析 | |
| コミュニケーション | |

## 6. 成功要因分析

### 6.1 主要成功要因

1.
2.
3.

### 6.2 タイミング要因

-

### 6.3 差別化要因

-

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | | |
| 競合状況 | | |
| ローカライズ容易性 | | |
| 再現性 | | |
| **総合** | | |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

-

### 8.2 CPF検証（/validate-cpf）

-

### 8.3 PSF検証（/validate-10x）

-

### 8.4 スコアカード（/startup-scorecard）

-

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1.
2.
3.

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年 | | |
| 評価額 | | |
| 成長データ | | |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1.
2.
3.
