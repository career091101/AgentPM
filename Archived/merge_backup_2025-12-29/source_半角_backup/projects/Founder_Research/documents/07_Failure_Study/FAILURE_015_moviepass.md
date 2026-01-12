---
id: "FAILURE_015"
title: "Stacy Spikes & Hamet Watt - MoviePass (Unit Economics Failure)"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["entertainment", "subscription", "failure", "unit economics", "burn rate"]

# 基本情報
founder:
  name: "Stacy Spikes & Hamet Watt"
  birth_year: null
  nationality: "アメリカ"
  education: null
  prior_experience: "Spikes: Miramax, Urbanworld Film Festival創業者"

company:
  name: "MoviePass"
  founded_year: 2011
  industry: "Entertainment / Subscription / Cinema"
  current_status: "bankrupt"
  valuation: "$500M（ピーク時）→ 破産"
  employees: 100+

# VC投資情報
funding:
  total_raised: "$300M+"
  funding_rounds:
    - round: "seed"
      date: "2011"
      amount: "$1.9M"
      lead_investors: ["True Ventures", "AOL Ventures"]
    - round: "majority_stake"
      date: "2017-08"
      amount: "$27M"
      lead_investors: ["Helios and Matheson Analytics"]
      note: "Helios and Mathesonが92%株式取得"
    - round: "additional_funding"
      date: "2017-2018"
      amount: "$300M+"
      investors: ["Helios and Matheson Analytics"]
  top_tier_vcs: ["True Ventures"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "unit_economics_bankruptcy"
  failure_pattern: "P13 + P11 + P28"
  failure_details:
    shutdown_date: "2019-09"
    total_funding_burned: "$300M+"
    peak_valuation: "$500M"
    liquidation_value: "ほぼゼロ"
    employees_affected: "100+"
    bankruptcy_date: "2020-01"
  failure_patterns:
    - code: "P13"
      name: "スケールしないモデル"
      description: "月額$9.95で映画見放題、しかし1回視聴で$12コスト→使えば使うほど赤字"
    - code: "P11"
      name: "バーンレート"
      description: "月$20M-$40M損失、資金枯渇"
    - code: "P28"
      name: "過剰調達"
      description: "$300M+調達したが、ビジネスモデル自体が破綻"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 70
    wtp_confirmed: true
    urgency_score: 5
    validation_method: "ユーザー需要は高いが、ビジネスモデルが破綻"
  psf:
    ten_x_axes:
      - axis: "価格"
        multiplier: 10  # 月額$9.95は従来の1/10
      - axis: "利便性"
        multiplier: 3
      - axis: "持続可能性"
        multiplier: -10  # ビジネスモデルが破綻
    mvp_type: "full_product"
    initial_cvr: null
    uvp_clarity: 10  # 「月額$9.95で映画見放題」は明確だが、持続不可能
    competitive_advantage: "なし（劣悪なUnit Economics）"
  pivot:
    occurred: false
    pivot_count: 0

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []
  related_cases: ["FAILURE_014 (Theranos - Fraud)", "FAILURE_009 (Quibi - PMF Failure)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "Business Insider"
    - "TechCrunch"
    - "The Verge"
    - "Wikipedia"
---

# Stacy Spikes & Hamet Watt - MoviePass（Unit Economics Failure）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Stacy Spikes & Hamet Watt |
| 企業名 | MoviePass |
| 創業年 | 2011年 |
| 業界 | エンターテインメント / サブスクリプション / 映画館 |
| 破産日 | 2020年1月 |
| 総調達額 | $300M+ |
| ピーク評価額 | $500M |

## 2. 創業ストーリーとビジネスモデル

### 2.1 初期モデル（2011-2017年）

**コンセプト**: 月額サブスクリプションで映画館に通い放題

**初期価格**: $30-$50/月
- ニューヨーク、サンフランシスコ等の都市部から開始
- 映画愛好家向けのニッチサービス
- 会員数: 2万人程度

### 2.2 Helios and Matheson買収（2017年8月）

**買収内容**:
- Helios and Matheson Analyticsが92%株式取得
- $27M投資
- CEO Mitch Loweが就任（元Netflix、元Redbox）

**価格破壊**: 月額$9.95
- 2017年8月、月額を$9.95に値下げ
- 「1日1映画まで見放題」
- 爆発的な会員数増加

## 3. Unit Economicsの破綻

### 3.1 コスト構造

**映画館へのチケット代**:
- 1回視聴あたり平均$12
- MoviePassが映画館に全額支払い
- ユーザーが月2回以上見れば赤字

**計算例**:
- 月額収入: $9.95
- 月1回視聴: $12コスト → 損失$2.05
- 月2回視聴: $24コスト → 損失$14.05
- 月3回視聴: $36コスト → 損失$26.05

**ヘビーユーザーほど損失大**:
- 映画愛好家は月10回以上視聴
- 1人あたり月$100+の損失

### 3.2 会員数急増

| 時期 | 会員数 | 月次損失 |
|------|--------|---------|
| 2017年7月 | 20,000 | 小額 |
| 2017年12月 | 400,000 | $20M+ |
| 2018年6月 | 3,000,000 | $40M+ |

**燃焼率**: 月$20M-$40M

## 4. 破綻の経緯

### 4.1 現金枯渇（2018年）

**2018年7月**: サービス一時停止
- 現金が枯渇し、映画館へのチケット代支払い不可
- ユーザーがアプリでチケット購入できず
- Helios and Mathesonが緊急で$5M融資

**制限の追加**:
- 人気映画の除外
- 視聴回数制限（月3回まで）
- ピーク時間帯の制限

**ユーザー離反**:
- サービス品質低下
- 会員数減少
- 悪評の拡散

### 4.2 破産（2019-2020年）

**2019年9月**: サービス停止
- 会員数は数十万人まで減少
- 現金枯渇、資金調達不可

**2020年1月**: Chapter 7破産申請
- 資産清算
- 債権者への支払い不可

## 5. 失敗パターン分析

### 5.1 P13: スケールしないモデル

**ビジネスモデルの根本的欠陥**:
- 使えば使うほど損失増加
- スケールすればするほど赤字拡大
- 劣悪なUnit Economics

**映画館との交渉失敗**:
- MoviePassは映画館に割引を要求
- しかし映画館は拒否（AMC、Regal等）
- MoviePassが全額負担し続ける

### 5.2 P11: バーンレート

**月次損失**: $20M-$40M
- 年間$240M-$480M損失
- 持続不可能

**資金調達依存**:
- Helios and Mathesonが追加資金投入
- しかし株価暴落（$3,000 → $0.01）
- 資金調達不可に

### 5.3 P28: 過剰調達

**$300M+調達**:
- しかしビジネスモデル自体が破綻
- 調達資金は損失補填のみ
- 黒字化の道筋なし

## 6. なぜ失敗したか

### 6.1 成長優先の誤り

**「成長すれば解決する」という幻想**:
- 会員数300万人達成
- しかし損失は拡大するのみ
- データ販売、広告等の副収入も微々たるもの

### 6.2 映画館との力関係

**映画館の拒否**:
- AMC、Regal等の大手が非協力的
- MoviePassへの割引拒否
- 独自サブスクリプション開始（AMC A-List等）

### 6.3 競合の出現

**映画館チェーンの対抗策**:
- **AMC A-List**: 月$19.95で週3回（持続可能な価格）
- **Regal Unlimited**: 月$18-$23
- これらは映画館自身のサービスなのでコスト構造が異なる

## 7. 教訓

### 7.1 Unit Economicsの検証

**成長前に検証必須**:
- 1顧客あたりの利益（LTV - CAC）
- スケールしても利益が出るか
- 劣悪なUnit Economicsはスケールで悪化

### 7.2 サプライヤーとの関係

**パワーバランス**:
- 映画館が協力しなければ成立しない
- 割引交渉の失敗
- バリューチェーン全体での win-win 必須

### 7.3 価格戦略

**赤字価格での成長は危険**:
- 月額$9.95は持続不可能
- 適正価格（$20-$30）なら生存可能だった
- しかしユーザー数は減少

## 8. Stacy Spikes復活（2021年）

**MoviePass再買収**:
- 2021年、創業者Stacy Spikesが破産資産から再買収
- 新モデル: クレジットベース（従量課金）
- 月額$10-$40（視聴回数に応じて）

**持続可能なモデル**:
- 見放題ではなく、視聴回数に応じた課金
- Unit Economicsが健全

## 9. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2011年） | ✅ PASS | Wikipedia、TechCrunch、Business Insider |
| 月額$9.95（2017年8月） | ✅ PASS | The Verge、Business Insider |
| ピーク会員数（300万人） | ✅ PASS | Business Insider、TechCrunch |
| 破産日（2020年1月） | ✅ PASS | TechCrunch、Wikipedia |
| 総調達額（$300M+） | ✅ PASS | Crunchbase、TechCrunch |

## 10. 参照ソース

1. [Business Insider - MoviePass Timeline](https://www.businessinsider.com/moviepass-history-timeline-2019-9)
2. [TechCrunch - MoviePass Shutdown](https://techcrunch.com/2019/09/14/moviepass-is-shutting-down/)
3. [The Verge - MoviePass Collapse](https://www.theverge.com/2019/9/19/20872984/moviepass-shutdown-subscription-movies-helios-matheson)
4. [Wikipedia - MoviePass](https://en.wikipedia.org/wiki/MoviePass)
5. [Crunchbase - MoviePass](https://www.crunchbase.com/organization/moviepass)
6. [Business Insider - Unit Economics](https://www.businessinsider.com/moviepass-unit-economics-2018-2)
7. [Forbes - MoviePass Failure](https://www.forbes.com/sites/danafeldman/2019/09/19/moviepass-shuts-down/)
8. [CNBC - MoviePass Cash Crunch](https://www.cnbc.com/2018/07/27/moviepass-ran-out-of-cash-service-goes-dark.html)
9. [The Hollywood Reporter - MoviePass Bankruptcy](https://www.hollywoodreporter.com/business/business-news/moviepass-parent-company-files-bankruptcy-1267749/)
10. [Variety - MoviePass Relaunch](https://variety.com/2022/film/news/moviepass-relaunch-beta-1235355026/)
11. [TechCrunch - Stacy Spikes Buys Back MoviePass](https://techcrunch.com/2021/11/23/moviepass-founder-stacy-spikes-buys-back-the-company/)
12. [Business Insider - AMC A-List](https://www.businessinsider.com/amc-a-list-subscription-service-2018-6)

