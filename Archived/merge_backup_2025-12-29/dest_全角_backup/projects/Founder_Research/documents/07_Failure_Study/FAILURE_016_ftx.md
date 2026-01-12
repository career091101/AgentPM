---
id: "FAILURE_016"
title: "Sam Bankman-Fried - FTX"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["crypto", "fraud", "bankruptcy", "alameda_research", "sbf", "ftx", "fraud_conviction", "regulatory_failure"]

# 基本情報
founder:
  name: "Sam Bankman-Fried (SBF)"
  birth_year: 1992
  nationality: "アメリカ"
  education: "MIT (Physics)"
  prior_experience: "Jane Street Capital (Quant Trader)"

company:
  name: "FTX"
  founded_year: 2019
  industry: "Cryptocurrency Exchange"
  current_status: "bankrupt"
  valuation: "$32B (ピーク時、2022年1月) → 破産"
  employees: 300+ → 解雇

# VC投資情報
funding:
  total_raised: "$1.8B"
  funding_rounds:
    - round: "series_b"
      date: "2021-07-20"
      amount: "$900M"
      valuation_post: "$18B"
      lead_investors: ["Sequoia Capital", "Paradigm"]
      other_investors: ["SoftBank", "Tiger Global", "Temasek", "Third Point", "Ribbit Capital"]
    - round: "series_c"
      date: "2022-01-31"
      amount: "$400M"
      valuation_post: "$32B"
      lead_investors: ["SoftBank", "Tiger Global"]
      other_investors: ["Sequoia Capital", "Temasek", "Ontario Teachers' Pension Plan"]
  top_tier_vcs: ["Sequoia Capital", "SoftBank", "Tiger Global", "Temasek"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "fraud_bankruptcy"
  failure_pattern: "P16 (規制・詐欺) + P23 (ガバナンス問題) + P28 (過剰調達)"
  pivot_details: null
  shutdown_date: "2022-11-11"
  legal_outcome: "SBF有罪判決25年（2024年3月）"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 70
    wtp_confirmed: true
    urgency_score: 8
    validation_method: "取引所ローンチ後のトラクション検証"
  psf:
    ten_x_axes:
      - axis: "取引速度（詐欺前）"
        multiplier: 10
      - axis: "ユーザー体験（詐欺前）"
        multiplier: 5
    mvp_type: "web_app"
    initial_cvr: null
    uvp_clarity: 8
    competitive_advantage: "高速取引、低手数料（表面上）"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "仮想通貨取引所"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Changpeng Zhao (Binance)", "Brian Armstrong (Coinbase)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "https://www.justice.gov/archives/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes"
    - "https://en.wikipedia.org/wiki/Sam_Bankman-Fried"
    - "https://www.cnbc.com/2024/03/28/live-updates-ftx-founder-sam-bankman-fried-sentencing.html"
---

# Sam Bankman-Fried - FTX

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Sam Bankman-Fried (SBF) |
| 生年 | 1992年 |
| 国籍 | アメリカ |
| 学歴 | MIT (Physics) |
| 創業前経験 | Jane Street Capital (Quant Trader) |
| 企業名 | FTX |
| 創業年 | 2019年 |
| 業界 | 仮想通貨取引所 |
| 現在の状況 | 破産（2022年11月11日） |
| 評価額/時価総額 | $32B（ピーク時、2022年1月） → 破産 |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- Sam Bankman-Fried: Jane Street Capital（Quant Trader）
- 2017年: 仮想通貨アービトラージ（日本と米国の価格差を利用）
- 既存仮想通貨取引所の課題:
  - 取引速度遅い
  - 手数料高い
  - ユーザー体験悪い
- 「プロ投資家向け高速取引所」構想

**創業の経緯**:
- 2017年: Alameda Research設立（仮想通貨トレーディング会社）
- 2019年: FTX設立（仮想通貨取引所）
- 2021年: FTX US設立（米国向け）
- 2022年1月: 評価額$32B、業界第2位（Binanceに次ぐ）

**需要検証方法**:
- 2019年: FTX公開
- 2020-2021年: 急成長、1日100億ドル取引高
- しかし顧客資金をAlameda Researchに流用（詐欺）

### 2.2 CPF検証（Customer Problem Fit）

**3U検証（詐欺前）**:
- Unworkable（現状では解決不可能）: 既存取引所は遅い・手数料高い
- Unavoidable（避けられない）: 仮想通貨トレーダーは取引所必須
- Urgent（緊急性が高い）: 仮想通貨市場急成長

**支払い意思（WTP）**:
- 確認方法: 取引手数料
- 結果: 1日100億ドル取引高達成

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性（表面上）**:

| 軸 | 従来の解決策（Binance等） | FTX | 倍率 |
|---|------------|-----|------|
| 取引速度 | 遅い | 高速 | 10x |
| ユーザー体験 | 複雑 | 直感的UI | 5x |
| 手数料 | 高い | 低い | 2x |

**しかし実態は詐欺**:
- 顧客資金をAlameda Researchに流用
- $8B以上の顧客資金を不正使用

**UVP（表面上）**:
- プロ投資家向け高速取引所
- デリバティブ取引対応
- 低手数料

## 3. ピボット/失敗経験

### 3.1 初期の失敗

ピボットなし。創業時から詐欺スキーム構築。

### 3.2 詐欺・破産の詳細

**詐欺スキーム**:
1. **顧客資金流用**: FTX顧客資金をAlameda Researchに送金
2. **不正会計**: FTXコード改変、Alameda Researchへの無制限出金許可
3. **資金使途**:
   - Alameda Research損失補填
   - SBF個人投資（不動産、政治献金等）
   - 高額ローン返済

**破産プロセス**:
- 2022年11月2日: CoinDesk、FTXとAlameda Researchの不正会計報道
- 2022年11月6日: Binance CEO Changpeng Zhao、FTXトークン売却発表
- 2022年11月8日: FTX、顧客出金停止
- 2022年11月11日: FTX破産申請
- 顧客資金$8B以上消失

**刑事訴追**:
- 2022年12月12日: SBF逮捕（バハマ）
- 2023年11月2日: SBF有罪判決（7つの罪状）
- 2024年3月28日: SBF懲役25年判決、$11B没収

## 4. 成長戦略（詐欺ベース）

### 4.1 初期トラクション獲得

**マーケティング戦略**:
- Super Bowl広告（2022年、$6.5M）
- Miami Heat アリーナ命名権（$135M、19年契約）
- Tom Brady, Gisele Bündchen等のセレブリティ起用
- SBF「Effective Altruism」（効果的利他主義）イメージ戦略

### 4.2 フライホイール（詐欺ベース）

```
FTX顧客増加
  ↓
顧客資金預託
  ↓
Alameda Researchへ不正送金
  ↓
Alameda損失補填・SBF個人投資
  ↓
マーケティング投資（Super Bowl等）
  ↓
新規顧客増加
  ↓
（詐欺スキーム拡大）
```

### 4.3 スケール戦略（詐欺拡大）

**技術スケール**:
- FTXコード改変（Alameda無制限出金）
- 会計ソフトウェア不正

**ビジネススケール**:
- 2022年1月: 評価額$32B
- 1日100億ドル取引高
- しかし実態は顧客資金流用

### 4.4 バリューチェーン（詐欺ベース）

**収益源（表面上）**:
1. 取引手数料
2. デリバティブ手数料

**実態**:
- 顧客資金$8B以上を不正使用
- Alameda Research損失補填
- SBF個人投資（政治献金$40M+、不動産、高額ローン）

## 4.5 資金調達履歴（VC案件のみ）

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Series B | 2021年7月 | $900M | $18B | Sequoia Capital, Paradigm | SoftBank, Tiger Global, Temasek, Third Point, Ribbit Capital |
| Series C | 2022年1月 | $400M | $32B | SoftBank, Tiger Global | Sequoia Capital, Temasek, Ontario Teachers' Pension Plan |

**総資金調達額**: $1.8B
**主要VCパートナー**: Sequoia Capital, SoftBank, Tiger Global, Temasek

### 資金使途と成長への影響

**Series B + C ($1.3B)**:
- マーケティング（Super Bowl, Miami Heat）
- Alameda Research損失補填（不正）
- SBF個人投資（不正）

### VC関係の構築

1. **VC選考突破（詐欺ベース）**:
   - 急成長、1日100億ドル取引高
   - SBF「Effective Altruism」イメージ
   - Sequoia Capital等の大手VCが投資

2. **破産後のVC損失**:
   - Sequoia Capital: 投資全額損失、謝罪文書公開
   - SoftBank, Tiger Global, Temasek: 投資全額損失

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 取引所 | 独自開発（コード改変で詐欺） |
| 会計 | QuickBooks（不正使用） |
| マーケティング | Super Bowl広告, セレブリティ起用 |

## 6. 失敗要因分析

### 6.1 主要失敗要因

1. **P16: 規制・詐欺**
   - 顧客資金$8B以上を不正使用
   - FTXコード改変、Alameda無制限出金
   - 不正会計（QuickBooks使用）

2. **P23: ガバナンス問題**
   - SBF独裁、内部統制なし
   - 会計監査なし（破産管財人が指摘）
   - 取締役会機能不全

3. **P28: 過剰調達**
   - $1.8B調達、評価額$32B
   - マーケティング過剰投資（Super Bowl $6.5M等）
   - Alameda損失補填に顧客資金使用

### 6.2 詐欺の警告サイン

- Alameda ResearchとFTXの不自然な関係
- 会計監査なし
- SBF「Effective Altruism」イメージと実態の乖離
- 政治献金$40M+（規制回避目的）

### 6.3 失敗の教訓

- **規制遵守の重要性**: 仮想通貨業界でも規制必須
- **内部統制の重要性**: ガバナンス不足は詐欺につながる
- **VCデューデリジェンス**: Sequoia等も詐欺を見抜けず

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 1 | 詐欺事例、適用すべきでない |
| 競合状況 | 1 | 日本は仮想通貨規制厳しい |
| ローカライズ容易性 | 1 | 規制遵守できない |
| 再現性 | 1 | 詐欺、再現すべきでない |
| **総合** | 1 | 失敗事例、学びのみ |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

**詐欺ではない場合の需要検証**:
- 仮想通貨取引所の需要は実在
- しかし顧客資金流用は詐欺

### 8.2 CPF検証（/validate-cpf）

**課題の深さ検証（詐欺前）**:
- 既存取引所の遅さ、高手数料
- FTXは表面上は解決（実態は詐欺）

### 8.3 PSF検証（/validate-10x）

**10倍優位性（表面上）**:
- 取引速度: 10倍
- しかし実態は顧客資金流用

### 8.4 スコアカード（/startup-scorecard）

**詐欺前（表面上）**:
- CPFスコア: 7/10
- PSFスコア: 8/10
- 総合スコア: 7.5/10

**実態**:
- 詐欺スキーム、全て虚偽

## 11. 詐欺・破産の詳細（Section 11）

### 11.1 詐欺スキームの全体像

**FTX - Alameda Research資金流用**:
1. **コード改変**: FTXコードを改変、Alameda Researchに無制限出金許可
2. **顧客資金流用**: $8B以上の顧客資金をAlameda Researchに送金
3. **不正会計**: QuickBooksで不正会計、監査なし
4. **SBF個人使用**: 不動産、政治献金$40M+、高額ローン返済

### 11.2 破産詳細

**破産申請**:
- 2022年11月11日: FTX、Alameda Research、130+関連会社が破産申請
- 顧客資金$8B以上消失
- 100万人以上の債権者

**破産管財人報告**:
- 内部統制なし
- 会計監査なし
- SBF独裁

### 11.3 刑事訴追詳細

**起訴内容（7つの罪状）**:
1. Wire fraud（2件）
2. Conspiracy to commit wire fraud（2件）
3. Conspiracy to commit securities fraud（1件）
4. Conspiracy to commit commodities fraud（1件）
5. Conspiracy to commit money laundering（1件）

**判決**:
- 2024年3月28日: 懲役25年、$11B没収
- U.S. Attorney Damian Williams: 「史上最大規模の金融詐欺の1つ」

### 11.4 共犯者

**有罪判決**:
- Caroline Ellison（Alameda Research CEO）: 司法取引、証言
- Gary Wang（FTX CTO）: 司法取引、証言
- Nishad Singh（FTX Engineering Director）: 司法取引、証言

## 9. 事業アイデア候補

この失敗事例から学ぶべき「やってはいけないこと」:

1. **顧客資金の分別管理徹底**
   - FTXは顧客資金をAlameda Researchに流用
   - 日本の仮想通貨規制は分別管理必須

2. **内部統制・ガバナンス構築**
   - SBF独裁、内部統制なし
   - 取締役会、会計監査の重要性

3. **規制遵守の徹底**
   - 仮想通貨業界でも規制必須
   - 政治献金で規制回避は不可能

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年2019年 | ✅ PASS | Wikipedia, DOJ |
| $1.8B調達 | ✅ PASS | Wikipedia, CNBC |
| 評価額$32B（2022年1月） | ✅ PASS | Wikipedia, CNBC |
| 破産（2022年11月11日） | ✅ PASS | Wikipedia, DOJ |
| SBF懲役25年（2024年3月28日） | ✅ PASS | DOJ, CNBC, NPR |
| 顧客資金$8B流用 | ✅ PASS | DOJ, CNBC |
| $11B没収 | ✅ PASS | DOJ, CNBC |

**凡例**: ✅ PASS（2ソース以上確認）

## 参照ソース

1. [Samuel Bankman-Fried Sentenced to 25 Years | DOJ](https://www.justice.gov/archives/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes)
2. [Sam Bankman-Fried - Wikipedia](https://en.wikipedia.org/wiki/Sam_Bankman-Fried)
3. [Trial of Sam Bankman-Fried - Wikipedia](https://en.wikipedia.org/wiki/Trial_of_Sam_Bankman-Fried)
4. [SBF sentenced to 25 years, $11B forfeiture | CNBC](https://www.cnbc.com/2024/03/28/live-updates-ftx-founder-sam-bankman-fried-sentencing.html)
5. [FTX founder Sam Bankman-Fried gets 25 years | Banking Dive](https://www.bankingdive.com/news/sam-bankman-fried-25-years-prison-fraud-conspiracy-ftx-crypto-sbf-kaplan-alameda/711601/)
6. [Sam Bankman-Fried sentenced to 25 years | NPR](https://www.npr.org/2024/03/28/1241210300/sam-bankman-fried-ftx-sentencing-crimes-crypto-mogul-greed)
7. [Sam Bankman-Fried sentenced to 25 years | Marketplace](https://www.marketplace.org/story/2024/03/28/sam-bankman-fried-sentenced-to-25-years-in-prison)
8. [Why a 25-Year Sentence? | ACFE](https://www.acfe.com/acfe-insights-blog/blog-detail?s=sam-bankman-fried-sentencing-in-context)
9. [From Poster Boy to Posting Bail | Cassels](https://cassels.com/insights/from-poster-boy-to-posting-bail-sam-bankman-fried-gets-25-years-for-ftx-scandal/)
10. [Samuel Bankman-Fried Sentenced To 25 Years | DOJ SDNY](https://www.justice.gov/usao-sdny/pr/samuel-bankman-fried-sentenced-25-years-prison)
11. [FTX collapse - Wikipedia](https://en.wikipedia.org/wiki/Bankruptcy_of_FTX)
12. [Going Infinite: The Rise and Fall of a New Tycoon | Michael Lewis](https://www.amazon.com/Going-Infinite-Rise-Fall-Tycoon/dp/1324074337)
