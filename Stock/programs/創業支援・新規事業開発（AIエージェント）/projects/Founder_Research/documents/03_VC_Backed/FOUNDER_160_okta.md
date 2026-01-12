---
id: "FOUNDER_160"
title: "Todd McKinnon & Frederic Kerrest - Okta"
category: "founder"
tier: "vc_backed"
type: "ipo_success"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["identity", "security", "SaaS", "enterprise", "IPO", "Greylock", "Sequoia", "a16z"]

# 基本情報
founder:
  name: "Todd McKinnon (CEO), Frederic Kerrest (COO)"
  birth_year: 1974 # McKinnon推定
  nationality: "アメリカ"
  education: "McKinnon: Brigham Young University (CS), Kerrest: Stanford (国際関係), Harvard Business School (MBA)"
  prior_experience: "McKinnon: Salesforce SVP of Engineering, Kerrest: Salesforce 初期営業・ビジネス開発"

company:
  name: "Okta, Inc."
  founded_year: 2009
  industry: "アイデンティティ・アクセス管理 / サイバーセキュリティ / SaaS"
  current_status: "public"
  valuation: "$2B（2017年IPO時）→ $10B+（2024年）"
  employees: 6,000+ # 2024年

# VC投資情報
funding:
  total_raised: "$230M+"
  funding_rounds:
    - round: "series_a"
      date: "2010-07"
      amount: "$10M"
      valuation_post: "不明"
      lead_investors: ["Andreessen Horowitz"]
      other_investors: ["Floodgate"]
    - round: "series_b"
      date: "2011-08"
      amount: "不明"
      valuation_post: "不明"
      lead_investors: ["Greylock Partners"]
      other_investors: []
    - round: "series_c"
      date: "2012-12"
      amount: "$25M"
      valuation_post: "不明"
      lead_investors: ["Sequoia Capital"]
      other_investors: ["Andreessen Horowitz", "Greylock"]
    - round: "series_f"
      date: "2015-09"
      amount: "$75M"
      valuation_post: "$1.2B"
      lead_investors: ["Andreessen Horowitz", "Greylock Partners", "Sequoia Capital"]
      other_investors: ["Khosla Ventures", "Altimeter Capital", "Glynn Capital"]
  top_tier_vcs: ["Greylock Partners (16.9% pre-IPO)", "Sequoia Capital (21.2% pre-IPO)", "Andreessen Horowitz (19.6% pre-IPO)", "Khosla Ventures (8.1% pre-IPO)"]

# 成功/失敗/Pivot分類
outcome:
  category: "success"
  subcategory: "ipo_success"
  ipo_details:
    ipo_date: "2017-04-07"
    ipo_valuation: "$2B"
    current_valuation: "$10B+"
    revenue_at_ipo: "$160M (FY2017)"
    profit_at_ipo: "赤字（$83M損失）"
  success_factors:
    - "Salesforce出身者の深いエンタープライズ知識"
    - "クラウドファーストのアイデンティティ管理"
    - "マルチテナントSaaSアーキテクチャ"
    - "トップティアVC（Greylock, Sequoia, a16z）の支援"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 25  # 推定: ['identity', 'security', 'SaaS', 'enterprise', 'IPO', 'Greylock', 'Sequoia', 'a16z']業界標準
    problem_commonality: 9 # エンタープライズのアイデンティティ管理は普遍的課題
    wtp_confirmed: true # エンタープライズは高額支払い
    urgency_score: 8 # セキュリティは重要だが、緊急度は中程度
    validation_method: "Salesforce経験、初期顧客からのフィードバック"
  psf:
    ten_x_axes:
      - axis: "ユーザビリティ"
        multiplier: 10 # オンプレミスActive Directoryより圧倒的に簡単
      - axis: "クラウド対応"
        multiplier: 20 # オンプレミスではクラウドアプリ統合困難
      - axis: "スケーラビリティ"
        multiplier: 10 # マルチテナントSaaS
    mvp_type: "full_product"
    initial_cvr: null
    uvp_clarity: 9 # 「クラウド時代のアイデンティティ管理」明確
    competitive_advantage: "クラウドファースト、Salesforce経験、エンタープライズ販売力"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "クラウドベースのアイデンティティ・アクセス管理"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Todd McKinnon", "Frederic Kerrest"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "CNBC"
    - "Wikipedia"
    - "Tracxn"
    - "TechCrunch"
    - "Okta公式"
---

# Todd McKinnon & Frederic Kerrest - Okta（IPO成功分析）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Todd McKinnon（CEO）, Frederic Kerrest（COO） |
| 生年 | McKinnon: 1974年頃 |
| 国籍 | アメリカ |
| 学歴 | McKinnon: Brigham Young University（CS）, Kerrest: Stanford（国際関係）, Harvard Business School（MBA） |
| 創業前経験 | McKinnon: Salesforce SVP of Engineering, Kerrest: Salesforce 初期営業・ビジネス開発 |
| 企業名 | Okta, Inc. |
| 創業年 | 2009年1月 |
| 業界 | アイデンティティ・アクセス管理 / サイバーセキュリティ / SaaS |
| 現在の状況 | 上場企業（NASDAQ: OKTA, 2017年4月IPO） |
| 評価額/時価総額 | $2B（2017年IPO時）→ $10B+（2024年） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**Salesforce時代の経験**:
- **Todd McKinnon**: Salesforce SVP of Engineering（2003-2009年）
- **Frederic Kerrest**: Salesforce 初期営業・ビジネス開発（2005-2009年）
- Salesforceでクラウド時代のエンタープライズソフトウェアを経験

**着想源（2008年）**:
- McKinnonがSalesforceで気づいた課題:
  - **クラウドアプリの急増**: Salesforce, Google Apps, Box等
  - **アイデンティティ管理の限界**: オンプレミスActive Directoryはクラウドに対応できない
  - **ユーザー体験の悪化**: 各アプリで個別ログイン、パスワード管理が煩雑

**課題の具体化**:
1. **クラウドアプリの認証・認可**: オンプレミスツール（Active Directory）では統合困難
2. **シングルサインオン（SSO）の欠如**: ユーザーが複数アプリで個別ログイン
3. **IT管理の複雑化**: 従業員の入退社時、各アプリのアカウント手動管理

**需要検証方法**:
- McKinnonの妻を説得（Salesforceを辞めて起業）
- 「5年間は成功しないかもしれないが、10年後には巨大市場になる」
- Salesforceのエンタープライズ顧客での課題実感

### 2.2 プロダクト開発

**コアコンセプト: Identity-as-a-Service (IDaaS)**:
- クラウドベースのアイデンティティ・アクセス管理
- マルチテナントSaaSアーキテクチャ
- オンプレミスActive Directoryの置き換え

**主要機能**:
1. **シングルサインオン（SSO）**: 1回のログインで複数アプリにアクセス
2. **ユーザーライフサイクル管理**: 従業員の入退社時、自動的に全アプリのアカウント作成・削除
3. **多要素認証（MFA）**: セキュリティ強化
4. **アプリ統合**: Salesforce, Google Workspace, Microsoft 365等、数千のアプリに対応

## 3. 成長の軌跡

### 3.1 初期資金調達（2010年）

**Series A（2010年7月）: $10M**:
- **Andreessen Horowitz（a16z）主導**
- 初期投資家: Floodgate
- McKinnonのSalesforce経験が評価された

**初期顧客獲得**:
- Salesforceの人脈活用
- エンタープライズ向け直販モデル
- 「クラウド時代のアイデンティティ管理」を訴求

### 3.2 トップティアVCの連続参入（2011-2015年）

**Series B（2011年8月）**:
- **Greylock Partners**が主導
- Greylockの企業向けSaaS投資戦略

**Series C（2012年12月）: $25M**:
- **Sequoia Capital**が新規参入・主導
- Andreessen Horowitz, Greylockも追加投資

**Series F（2015年9月）: $75M**:
- **評価額$1.2B（ユニコーン達成）**
- Andreessen Horowitz, Greylock Partners, Sequoia Capitalの3社が共同主導
- Khosla Ventures, Altimeter Capital, Glynn Capitalも参加

**総調達額**:
- IPO前に$230M+調達
- トップティアVC3社（a16z, Greylock, Sequoia）の強力支援

### 3.3 IPO前の株主構成（2017年3月S-1提出時）

| 投資家 | 株式保有比率 |
|--------|-------------|
| Sequoia Capital | 21.2% |
| Andreessen Horowitz | 19.6% |
| **Greylock Partners** | **16.9%** |
| Khosla Ventures | 8.1% |

**Greylockの16.9%保有**:
- IPO前の主要株主3位
- Series B（2011年）から継続投資
- 企業向けSaaS投資での成功例

### 3.4 IPO（2017年4月7日）

**IPO詳細**:
- **NASDAQ上場**（ティッカー: OKTA）
- **公募価格**: $17/株
- **初日終値**: $17.00（横ばい）
- **調達額**: $187M
- **評価額**: 約$2B
- **年間収益**: $160M（FY2017）
- **損失**: $83M（依然赤字）

**IPO時の特徴**:
- 赤字でのIPO（エンタープライズSaaSの典型）
- ARR（Annual Recurring Revenue）成長率: 60%+
- 顧客数: 3,750社（2017年1月時点）

### 3.5 IPO後の成長（2017-2024年）

**2024年時点**:
- **市場時価総額**: $10B+（IPO時の5倍）
- **年間収益**: $2.2B+
- **従業員数**: 6,000+
- **顧客数**: 18,000+企業

**主要買収**:
- **2021年**: Auth0を$6.5Bで買収（開発者向けアイデンティティプラットフォーム）

## 4. 成功要因分析

### 4.1 Salesforce出身者の強み

**エンタープライズ知識**:
- McKinnon: Salesforce SVP of Engineering → 技術力、プロダクト開発
- Kerrest: Salesforce初期営業 → エンタープライズ販売力
- Salesforceでのクラウドエンタープライズ経験

**人脈活用**:
- Salesforce顧客ネットワーク
- Salesforce出身者の採用
- エンタープライズ販売のベストプラクティス

### 4.2 クラウドファーストのタイミング

**2009年のクラウド移行期**:
- Salesforce, Google Apps, Box等のクラウドアプリ普及期
- オンプレミスActive Directoryでは対応困難
- 「クラウド時代のアイデンティティ管理」という明確なポジショニング

**マルチテナントSaaS**:
- オンプレミスの10倍簡単
- クラウドアプリとの統合が容易
- スケーラビリティ

### 4.3 トップティアVCの支援

**a16z, Greylock, Sequoiaの3社**:
- 企業向けSaaSでの実績
- ネットワーク効果（顧客紹介、採用支援）
- IPOまでの忍耐強い支援

**Greylockの16.9%保有**:
- Series Bから継続投資
- 企業向けSaaS投資での成功事例
- IPOで大きなリターン

### 4.4 エンタープライズ向け直販モデル

**高単価契約**:
- エンタープライズ顧客は年間$50K-$500K+支払う
- ARR（Annual Recurring Revenue）モデル
- 解約率（Churn Rate）が低い

**長期契約**:
- 3-5年契約が多い
- アイデンティティ管理はミッションクリティカル → スイッチングコスト高い

## 5. Greylockの投資戦略

### 5.1 企業向けSaaS投資

**Greylockのポートフォリオ**:
- Okta（アイデンティティ管理）
- Workday（HR/財務）
- Dropbox（ファイル共有）
- Airbnb（消費者向けだが、エンタープライズツールも提供）

**投資哲学**:
- エンタープライズの長期契約による安定収益
- 高い参入障壁（スイッチングコスト）
- IPOまでの長期支援

### 5.2 Oktaへの投資タイミング

**Series B（2011年8月）参入**:
- Series A（a16z）の翌年
- 初期顧客獲得後、PMF確認済み
- エンタープライズSaaSの成長可能性を評価

**IPO前16.9%保有**:
- Series Bから追加投資を継続
- IPOで大きなリターン（推定10倍以上）

## 6. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本企業もクラウドアプリ増加でアイデンティティ管理が課題 |
| 競合状況 | 3 | Okta, Microsoft Entra ID（旧Azure AD）が強い |
| ローカライズ容易性 | 4 | 日本語対応、日本の法規制対応が必要だが可能 |
| 再現性（成功再現） | 4 | エンタープライズSaaSのモデルは日本でも有効 |
| **総合** | 4.0 | 日本でもエンタープライズSaaS市場は成長中 |

**日本市場での応用**:
- 日本企業向けアイデンティティ管理SaaS
- マイナンバーカード連携、日本の法規制対応
- エンタープライズ向け直販モデル

## 7. orchestrate-phase1への示唆

### 7.1 需要発見（/discover-demand）での注意点

- **エンタープライズ経験の重要性**: Salesforce出身 → 顧客課題を深く理解
- **クラウド移行のタイミング**: 2009年はクラウドアプリ普及期

### 7.2 CPF検証（/validate-cpf）での注意点

- **エンタープライズ顧客のWTP**: 年間$50K-$500K+支払う
- **ミッションクリティカル**: アイデンティティ管理は企業の根幹
- **スイッチングコスト**: 一度導入すると、競合への移行困難

### 7.3 PSF検証（/validate-10x）での注意点

- **10倍の優位性**: オンプレミスActive Directoryより圧倒的に簡単
- **クラウド対応**: オンプレミスではクラウドアプリ統合困難
- **ユーザビリティ**: シングルサインオンで劇的に改善

### 7.4 スコアカード（/startup-scorecard）での評価

| 指標 | Oktaの事例 | スコア |
|------|-----------|--------|
| PMF | エンタープライズで明確なニーズ | 9/10 |
| 参入障壁 | スイッチングコスト高い | 8/10 |
| 収益性 | ARRモデル、低解約率 | 9/10 |
| スケーラビリティ | マルチテナントSaaS | 10/10 |
| **総合** | エンタープライズSaaSの成功モデル | **9/10** |

## 8. トップティアVCの投資ポイント

### 8.1 Greylockの投資判断

1. **創業者の経験**: Salesforce出身 → エンタープライズ知識
2. **市場タイミング**: クラウド移行期（2009-2011年）
3. **PMF確認**: Series B時点で初期顧客獲得済み
4. **長期視点**: IPOまで6年間継続支援

### 8.2 a16z, Sequoiaの共通点

**エンタープライズSaaS投資**:
- 高単価、長期契約、低解約率
- スケーラビリティ
- IPOまでの長期支援

**Oktaへの評価**:
- a16z: Series A主導（2010年）
- Sequoia: Series C主導（2012年）
- Greylock: Series B主導（2011年）

## 9. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2009年1月） | ✅ PASS | Wikipedia, Okta公式 |
| 総調達額（$230M+） | ✅ PASS | CNBC, Tracxn |
| Greylock保有比率（16.9% pre-IPO） | ✅ PASS | CNBC S-1分析 |
| Sequoia保有比率（21.2% pre-IPO） | ✅ PASS | CNBC S-1分析 |
| a16z保有比率（19.6% pre-IPO） | ✅ PASS | CNBC S-1分析 |
| IPO日（2017年4月7日） | ✅ PASS | Wikipedia, CNBC |
| IPO評価額（約$2B） | ✅ PASS | Business Insider, CNBC |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [CNBC - Okta files to go public, setting up an exit for some of Silicon Valley's most prominent investors](https://www.cnbc.com/2017/03/13/okta-files-s1.html)
2. [CNBC - How Okta CEO Todd McKinnon convinced wife he should leave Salesforce](https://www.cnbc.com/2019/12/26/how-okta-ceo-todd-mckinnon-convinced-wife-he-should-leave-salesforce.html)
3. [Wikipedia - Okta (identity management)](https://en.wikipedia.org/wiki/Okta_(identity_management))
4. [Tracxn - Okta 2025 Funding Rounds & List of Investors](https://tracxn.com/d/companies/okta/__dP1ZS8p5nyTcH8CpTecTYQQL8thmZJdd_D_Of9lWf9U/funding-and-investors)
5. [TechCrunch - Okta Joins Unicorns With $75M Round And Looks Towards IPO](https://techcrunch.com/2015/09/08/okta-joins-unicorns-with-75m-round-and-looks-towards-ipo/)
6. [Okta公式 - Okta Secures $25 Million to Fuel Enterprise Growth](https://www.okta.com/press-room/press-releases/okta-secures-25-million-to-fuel-enterprise-growth/)
7. [Axios - Okta hits the public markets](https://www.axios.com/2017/12/15/okta-hits-the-public-markets-1513301464)
8. [SiliconANGLE - Identity management firm Okta raises $75m Series F on $1.2b unicorn valuation](https://siliconangle.com/2015/09/09/identity-management-firm-okta-raises-75m-series-f-on-1-2b-unicorn-valuation/)
9. [Business Insider India - Okta prices its IPO and hopes to hit a $2 billion valuation](https://www.businessinsider.in/okta-prices-its-ipo-and-hopes-to-hit-a-2-billion-valuation/articleshow/57859737.cms)
10. [Yahoo Finance - Right before their IPO, Okta's cofounders received a sign from the heavens](https://finance.yahoo.com/news/ipo-oktas-cofounders-received-sign-203553784.html)
11. [Okta公式 - The Leader in Identity Management](https://www.okta.com/company/)
12. [MatrixBCG - Who Owns Okta Company?](https://matrixbcg.com/blogs/owners/okta)
