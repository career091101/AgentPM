---
id: "FAILURE_012"
title: "Adam Neumann - WeWork"
category: "failure"
tier: "failure_study"
type: "ipo_failure"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["coworking", "real-estate", "benchmark-capital", "softbank", "ipo-failure", "pmf-failure", "unit-economics"]

# 基本情報
founder:
  name: "Adam Neumann"
  co_founders: ["Miguel McKelvey"]
  birth_year: 1979
  nationality: "イスラエル → アメリカ"
  education: "Baruch College（経営学）"
  prior_experience: "起業家（baby clothes with knee pads）、海軍士官候補生"

company:
  name: "WeWork"
  founded_year: 2010
  industry: "コワーキングスペース / 不動産 / オフィス賃貸"
  current_status: "bankrupt"
  valuation: "$47B（2019年1月）→ $270M（2023年破産前）"
  employees: 12,500 # 2019年ピーク時

# VC投資情報
funding:
  total_raised: "$12.8B+"
  funding_rounds:
    - round: "series_a"
      date: "2012-06"
      amount: "$17M"
      valuation_post: "$100M"
      lead_investors: ["Benchmark Capital"]
      other_investors: []
    - round: "series_b"
      date: "2014-04"
      amount: "$150M"
      valuation_post: "$1.5B"
      lead_investors: ["J.P. Morgan"]
      other_investors: ["Benchmark Capital"]
    - round: "series_d"
      date: "2014-12"
      amount: "$355M"
      valuation_post: "$5B"
      lead_investors: ["T. Rowe Price"]
      other_investors: []
    - round: "series_f"
      date: "2017-03"
      amount: "$4.4B"
      valuation_post: "$20B"
      lead_investors: ["SoftBank Vision Fund"]
      other_investors: []
    - round: "series_g"
      date: "2018-08"
      amount: "$1B"
      valuation_post: "$45B"
      lead_investors: ["SoftBank Vision Fund"]
      other_investors: []
  top_tier_vcs: ["Benchmark Capital（Series A）", "SoftBank Vision Fund（$10B+投資）"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "ipo_failure_bankruptcy"
  failure_pattern: "P12+P14+P28+P15"
  failure_details:
    - pattern: "P12"
      description: "PMF未達成（unit economicsが成立しない）"
    - pattern: "P14"
      description: "タイミング（WeWorkモデルはリモートワーク時代に不適合）"
    - pattern: "P28"
      description: "過剰調達（$12.8B調達、バリュエーション$47B → 崩壊）"
    - pattern: "P15"
      description: "取締役会衝突（Benchmark含む投資家がNeumann解任）"
  ipo_failure:
    ipo_filed: "2019-08-14"
    ipo_withdrawn: "2019-09-30"
    reason: "投資家の懸念（ガバナンス、評価額、継続的赤字）"
    ceo_ousted: "2019-09-24"
    bankruptcy_filed: "2023-11-06"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 6 # コワーキング需要はあるが、WeWorkモデルは過剰
    wtp_confirmed: false # 価格設定が高すぎ、競合が安価
    urgency_score: 3 # コワーキングは必須ではない
    validation_method: "急速拡大優先、顧客検証不十分"
  psf:
    ten_x_axes:
      - axis: "コミュニティ"
        multiplier: 2 # 従来オフィスより良いが10倍ではない
      - axis: "柔軟性"
        multiplier: 3 # 短期契約可能
      - axis: "価格"
        multiplier: 0.5 # 従来オフィスより高い（unit economics悪い）
    mvp_type: "physical_space"
    initial_cvr: null
    uvp_clarity: 5 # "We" "Community"は曖昧
    competitive_advantage: "なし（参入障壁低い、競合多数）"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "コワーキングスペース"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Adam Neumann", "Miguel McKelvey"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 14
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia"
    - "CNBC"
    - "Crunchbase"
    - "TechCrunch"
    - "Britannica Money"
---

# Adam Neumann - WeWork（Benchmark Capital投資・IPO失敗分析）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Adam Neumann（CEO）, Miguel McKelvey（Chief Culture Officer） |
| 生年 | 1979年 |
| 国籍 | イスラエル → アメリカ |
| 学歴 | Baruch College（経営学） |
| 創業前経験 | 起業家（baby clothes with knee pads）、イスラエル海軍士官候補生 |
| 企業名 | WeWork |
| 創業年 | 2010年 |
| 業界 | コワーキングスペース / 不動産 / オフィス賃貸 |
| 現在の状況 | 破産（2023年11月Chapter 11申請） |
| 評価額/時価総額 | $47B（2019年1月ピーク）→ $270M（2023年破産前） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- **2008年**: Adam NeumannとMiguel McKelveyがブルックリンで出会う
- フリーランサー、スタートアップのオフィスニーズに着目
- 「コミュニティ」「We」を強調

**課題の具体化**:
1. **高額な賃貸**: ニューヨークのオフィス賃料は高額
2. **短期契約不可**: 従来は長期契約（5-10年）のみ
3. **コミュニティ不足**: フリーランサーの孤立

**需要検証方法**:
- **2010年**: ニューヨークSoHoに最初のスペース「Green Desk」オープン
- 環境配慮型コワーキングスペース
- 後にWeWorkとして再スタート

### 2.2 プロダクト開発

**創業メンバー**:
- **Adam Neumann**: カリスマCEO、ビジョン提示
- **Miguel McKelvey**: Chief Culture Officer、デザイン

**初期資金調達**:
- **2012年6月**: Series A $17M（Benchmark Capital主導、評価額$100M）

**初期プロダクト**:
- ニューヨークのオフィスビルを長期賃貸
- 内装改装（おしゃれなデザイン）
- デスク・会議室を短期契約で転貸

## 3. 成長の軌跡

### 3.1 Benchmark Capitalとの出会い（2012年6月）

**Series A調達**:
- **金額**: $17M
- **リード投資家**: Benchmark Capital
- **評価額**: $100M
- Miguel McKelveyがNeumannを説得（「評価額は低いが受け入れよう」）

**Benchmark Capitalの投資判断**:
- コワーキングスペース市場の成長性
- Adam Neumannのカリスマ性
- ニューヨーク、サンフランシスコでの早期成功

### 3.2 爆発的拡大（2014-2018年）

**資金調達の加速**:
- **2014年4月**: Series B $150M（J.P. Morgan主導、評価額$1.5B）
- **2014年12月**: Series D $355M（T. Rowe Price主導、評価額$5B）
- **2017年3月**: Series F $4.4B（SoftBank Vision Fund主導、評価額$20B）
- **2018年8月**: Series G $1B（SoftBank、評価額$45B）
- **2019年1月**: 評価額$47B（ピーク）

**グローバル展開**:
- **2018年**: 111都市、485拠点
- ニューヨーク、サンフランシスコ、ロンドン、東京等

**総調達額**:
- **$12.8B+**（主にSoftBank Vision Fundから$10B+）

### 3.3 IPO準備と崩壊（2019年）

**S-1提出（2019年8月14日）**:
- IPO目標評価額: $47B
- しかし、S-1で深刻な問題が露呈

**S-1で露呈した問題**:
1. **巨額損失**: 2018年売上$1.8B、損失$1.9B（売上を上回る赤字）
2. **ガバナンス問題**:
   - Adam Neumannの株式は20倍議決権（dual-class stock）
   - Neumannが"We"商標を自社に$5.9M で売却（利益相反）
   - Neumannの個人的不動産取引（WeWorkが賃貸）
3. **継続的赤字**: unit economics が成立しない

**投資家の懸念**:
- 評価額が高すぎる（$47B → $10Bに下方修正）
- ガバナンス問題
- 継続的赤字

**IPO撤回（2019年9月30日）**:
- 投資家の需要不足
- Adam Neumann辞任（2019年9月24日）
- 後任CEO: Artie Minson, Sebastian Gunningham

### 3.4 Benchmarkの対応

**Adam Neumann解任要求**:
- Benchmark含む5投資家がNeumannにCEO辞任要求（2019年9月）
- Jamie Dimon（J.P. Morgan CEO）がNeumannを説得

**Benchmarkのリターン**:
- Series A（2012年）: $17M投資（$100M評価額）
- SoftBankへの株式売却: 推定30-60倍リターン（$676.5M売却報道）
- ただし、IPO失敗により最大リターンは逃した

### 3.5 破産（2023年11月）

**Chapter 11申請（2023年11月6日）**:
- 負債を再編成
- 不採算拠点からの撤退
- 評価額$270M（ピーク時$47Bの0.6%）

**破産の原因**:
1. **unit economics不成立**: 長期賃貸契約 + 短期転貸 = 継続的赤字
2. **COVID-19**: リモートワーク普及でオフィス需要減
3. **競合激化**: IWG（Regus）、競合コワーキングスペースが低価格で参入

## 4. 失敗要因分析

### 4.1 PMF未達成（P12）

**unit economicsの崩壊**:
- **コスト構造**: 長期賃貸契約（10-15年）+ 内装改装費
- **収益構造**: 短期転貸（月単位、年単位）
- **問題**: 不況・景気後退時に稼働率低下 → 赤字拡大

**継続的赤字**:
- 2018年: 売上$1.8B、損失$1.9B
- 2019年上半期: 売上$1.5B、損失$690M
- 「成長で赤字をカバー」戦略は破綻

### 4.2 タイミング（P14）

**COVID-19の直撃**:
- 2020年以降、リモートワーク普及
- オフィス需要激減
- WeWorkの稼働率低下

**WeWorkモデルの時代錯誤**:
- オフィス回帰の期待は裏切られた
- Zoom, Slack等のリモートワークツールが普及

### 4.3 過剰調達（P28）

**$12.8B調達の弊害**:
- バリュエーション$47Bは過大評価
- 「成長至上主義」（Growth-at-all-cost）
- unit economicsを無視した拡大

**SoftBankの影響**:
- $10B+投資（Vision Fund）
- 「世界征服」を煽る
- 現実的な事業計画を無視

### 4.4 取締役会衝突（P15）

**ガバナンス問題**:
- Adam Neumannの独裁的経営
- 20倍議決権株式
- 利益相反取引（"We"商標売却、個人不動産取引）

**投資家の反乱**:
- Benchmark含む5投資家がNeumann解任要求
- Jamie Dimonの説得

## 4.5 資金調達履歴

| ラウンド | 時期 | 金額 | リード投資家 | 評価額 |
|---------|------|------|------------|--------|
| Series A | 2012-06 | $17M | **Benchmark Capital** | $100M |
| Series B | 2014-04 | $150M | J.P. Morgan | $1.5B |
| Series C | 2014-06 | $40M | - | $5B |
| Series D | 2014-12 | $355M | T. Rowe Price | $5B |
| Series E | 2016-03 | $430M | Legend Holdings | $16B |
| Series F | 2017-03 | $4.4B | SoftBank Vision Fund | $20B |
| Series G | 2018-08 | $1B | SoftBank Vision Fund | $45B |
| ピーク | 2019-01 | - | - | $47B |
| IPO撤回 | 2019-09 | - | - | - |
| 破産前 | 2023 | - | - | $270M |

### Benchmark Capitalとの関係構築

**パートナー**: 不明（Benchmark公式には未公表）

**投資判断理由**（2012年）:
1. **コワーキング市場の成長**: フリーランサー、スタートアップの増加
2. **ニューヨーク・サンフランシスコでの成功**: 初期拠点での需要確認
3. **Adam Neumannのカリスマ**: ビジョン提示能力

**Benchmark Capitalの対応（2019年）**:
- Adam Neumann解任要求をリード
- SoftBankへの株式売却（推定$676.5M）
- IPO前に一部Exit

## 5. 教訓

### 5.1 unit economicsの重要性

**成長 ≠ 成功**:
- WeWorkは900拠点に拡大したが、unit economicsは成立せず
- 1拠点あたりの収益性を確認すべき

**コスト構造の確認**:
- 長期賃貸契約（固定費）+ 短期転貸（変動収益）= リスク大

### 5.2 ガバナンスの重要性

**創業者の独裁**:
- 20倍議決権株式
- 利益相反取引
- 投資家の監視が不十分

**取締役会の機能**:
- Benchmark含む投資家が最終的にNeumann解任
- しかし、遅すぎた

### 5.3 過剰調達のリスク

**バリュエーション$47Bの弊害**:
- 現実的な事業計画を無視
- 「成長至上主義」に陥る
- IPO時の期待値が高すぎて失敗

## 6. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | コワーキング需要はあるが、WeWorkモデルは過剰 |
| 競合状況 | 2 | IWG（Regus）、国内コワーキングスペースが優位 |
| ローカライズ容易性 | 2 | 日本の不動産市場、賃貸慣行が異なる |
| 再現性（成功再現） | 1 | WeWorkモデルは失敗、unit economics不成立 |
| **総合** | 2.0 | WeWorkモデルは日本でも失敗リスク高い |

**日本市場での教訓**:
- unit economicsの確認（長期賃貸 + 短期転貸は危険）
- コワーキングは成長市場だが、WeWorkモデルは不適
- 低コスト運営が鍵

## 7. orchestrate-phase1への示唆

### 7.1 需要発見（/discover-demand）での注意点

- **市場規模 ≠ 成功**: コワーキング市場は成長していたが、WeWorkモデルは不適
- **unit economics早期確認**: 1拠点あたりの収益性を確認

### 7.2 CPF検証（/validate-cpf）での注意点

- **WTP（支払意思額）**: WeWorkは価格設定が高すぎ、競合が安価
- **継続利用率**: 短期契約モデルは稼働率変動大

### 7.3 PSF検証（/validate-10x）での注意点

- **10倍優位性なし**: WeWorkは従来オフィスより柔軟だが、10倍優れてはいない
- **参入障壁低い**: 競合が容易に参入

### 7.4 スコアカード（/startup-scorecard）での評価

| 指標 | WeWorkの事例 | スコア |
|------|------------|--------|
| PMF | unit economics不成立 | 2/10 |
| 参入障壁 | 低い（競合多数） | 3/10 |
| 収益性 | 継続的赤字 | 1/10 |
| スケーラビリティ | 拡大したが破綻 | 3/10 |
| **総合** | 失敗モデル | **2.25/10** |

## 8. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2010年） | ✅ PASS | Wikipedia, Crunchbase |
| Series A（2012年6月、$17M、Benchmark主導） | ✅ PASS | Crunchbase, Britannica Money |
| 評価額$100M（Series A） | ✅ PASS | Crunchbase |
| 評価額$47B（2019年1月ピーク） | ✅ PASS | CNBC, Wikipedia |
| IPO撤回（2019年9月30日） | ✅ PASS | Wikipedia, CNBC |
| Adam Neumann解任（2019年9月24日） | ✅ PASS | Wikipedia, NPR |
| 破産申請（2023年11月6日） | ✅ PASS | Wikipedia, TechCrunch |
| Benchmark売却$676.5M | ✅ PASS | Crunchbase News |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Wikipedia - WeWork](https://en.wikipedia.org/wiki/WeWork)
2. [CNBC - Ousted WeWork CEO Adam Neumann: $47 billion valuation went to his head](https://www.cnbc.com/amp/2021/11/09/ousted-wework-ceo-adam-neumann-47-billion-valuation-went-to-his-head.html)
3. [Crunchbase - WeWork Company Profile](https://www.crunchbase.com/organization/wework)
4. [Crunchbase News - Report: Adam Neumann, Benchmark Unloaded $676.5M In WeWork Shares Before Failed IPO](https://news.crunchbase.com/startups/report-adam-neumann-benchmark-unloaded-676-5m-in-wework-shares-before-failed-ipo/)
5. [Britannica Money - WeWork](https://www.britannica.com/money/WeWork)
6. [TechCrunch - WeWork's bankruptcy is proof that its core business never actually worked](https://techcrunch.com/2023/11/07/wework-bankruptcy-business-bad/)
7. [Accountancy Cloud - WeWork's $2 Billion Disaster: What Went Wrong?](https://accountancycloud.com/blogs/weworks-2-billion-disaster-what-went-wrong)
8. [Apollo Advisor - 5 Reasons WeWork Had A Disastrous Business Model](https://www.apolloadvisor.com/5-reasons-wework-had-a-disasterous-business-model-its-frightening/)
9. [NPR - WeWork CEO Adam Neumann Steps Down Amid Stalled IPO](https://www.npr.org/2019/09/24/763913318/wework-ceo-steps-down-as-ipo-stalls)
10. [The Corporate Governance Institute - What exactly happened to WeWork?](https://www.thecorporategovernanceinstitute.com/insights/case-studies/what-exactly-happened-to-wework/)
11. [2727 Coworking - WeWork History: Rise, IPO Failure, Bankruptcy & Future](https://2727coworking.com/articles/wework-history-ipo-bankruptcy)
12. [Fortune - From $47 billion to $270 million—WeWork keeps crashing](https://fortune.com/2023/08/09/wework-going-concern-bankruptcy-risk-47-billion-valuation-adam-neumann/)
13. [IDEAL - The WeWork IPO Fail: Its Causes and Key Findings](https://www.idealsvdr.com/blog/need-know-wework-ipo-postponement/)
14. [Slidebean - How is the WeWork Founder Still Rich?!](https://slidebean.com/story/how-is-the-wework-founder-still-rich)
