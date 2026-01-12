---
id: "FAILURE_012"
title: "Adam Neumann - WeWork"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["coworking", "real-estate", "benchmark-capital", "softbank", "ipo-failure", "governance", "overfunding", "founder-problem"]

# 基本情報
founder:
  name: "Adam Neumann"
  co_founders: ["Miguel McKelvey"]
  birth_year: 1979
  nationality: "イスラエル → アメリカ"
  education: "Baruch College（経営学、2003年卒業）"
  prior_experience: "Baby Kneepads起業（失敗）、イスラエル海軍士官候補生"

company:
  name: "WeWork"
  founded_year: 2010
  industry: "コワーキングスペース / 不動産 / オフィス賃貸"
  current_status: "bankrupt"
  valuation: "$47B（2019年1月ピーク）→ $270M（2023年破産前）"
  employees: 12500 # 2019年ピーク時

# VC投資情報
funding:
  total_raised: "$22B+"
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
  failure_pattern: "P12+P15+P28+P30"
  failure_details:
    - pattern: "P12"
      description: "PMF未達成（unit economicsが成立しない）"
    - pattern: "P15"
      description: "取締役会衝突（投資家がNeumann解任）"
    - pattern: "P28"
      description: "過剰調達（$22B調達、バリュエーション$47B崩壊）"
    - pattern: "P30"
      description: "創業者ガバナンス問題（利益相反、20倍議決権、独裁経営）"
  ipo_failure:
    ipo_filed: "2019-08-14"
    ipo_withdrawn: "2019-09-30"
    reason: "ガバナンス問題、継続的赤字、評価額過大"
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
  related_founders: ["Miguel McKelvey", "Masayoshi Son (SoftBank)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 18
  last_verified: "2025-12-29"
  quality_score: 92
  primary_sources:
    - "Wikipedia"
    - "CNBC"
    - "Wall Street Journal"
    - "New York Times"
    - "Forbes"
    - "TechCrunch"
    - "Bloomberg"
---

# Adam Neumann - WeWork（創業者ガバナンス失敗分析）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Adam Neumann（CEO）, Miguel McKelvey（Chief Culture Officer） |
| 生年 | 1979年（イスラエル） |
| 国籍 | イスラエル → アメリカ（2011年移住） |
| 学歴 | Baruch College（経営学、2003年卒業） |
| 創業前経験 | Baby Kneepads起業（2006年、失敗）、イスラエル海軍士官候補生 |
| 企業名 | WeWork |
| 創業年 | 2010年（Green Deskとして）、2010年にWeWorkへ改名 |
| 業界 | コワーキングスペース / 不動産 / オフィス賃貸 |
| 現在の状況 | 破産（2023年11月Chapter 11申請）、Neumann退任（2019年9月） |
| 評価額/時価総額 | $47B（2019年1月ピーク）→ $270M（2023年破産前） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- **2008年**: Adam NeumannとMiguel McKelveyがブルックリンのビル（154 Grand Street）で出会う
- Neumannは"Baby Kneepads"（赤ちゃん用膝当て）事業で失敗
- McKelveyは建築家で空間デザインに興味
- 二人は「コミュニティ」をテーマにしたオフィススペースを構想

**課題の具体化**:
1. **高額な賃貸**: ニューヨークのオフィス賃料は月$4,000-10,000（小規模）
2. **長期契約縛り**: 従来は5-10年契約のみ
3. **コミュニティ不足**: フリーランサー・スタートアップの孤立
4. **柔軟性不足**: 成長に応じたスペース拡大が困難

**需要検証方法**:
- **2008年**: ブルックリンで最初のコワーキングスペース「Green Desk」オープン
- 環境配慮型（LEED認証）コワーキング
- 即座に満室 → 需要確認
- **2010年**: Green Deskを売却し、WeWorkとして再スタート

### 2.2 CPF検証（Customer Problem Fit）

**初期顧客インタビュー**:
- 実施数: 不明（公式記録なし）
- Neumannはフリーランサー・スタートアップに直接営業
- SoHo、ブルックリンのクリエイティブ層をターゲット

**3U検証**:
- Unworkable（現状では解決不可能）: △ 長期契約なしではオフィス借りられない
- Unavoidable（避けられない）: △ スタートアップはオフィス必要
- Urgent（緊急性が高い）: △ オフィス探しは時間かかる

**支払い意思（WTP）**:
- 初期デスク価格: $450/月（ニューヨーク、2010年）
- 従来オフィス賃料の約60-70%
- しかし、unit economicsは成立せず（後述）

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策（賃貸オフィス） | 自社ソリューション（WeWork） | 倍率 |
|---|------------|-----------------|------|
| 柔軟性 | 5-10年契約 | 月単位契約 | 3x |
| コミュニティ | なし | メンバーイベント、ネットワーキング | 2x |
| デザイン | 無機質 | おしゃれ、ブランディング | 2x |
| 価格 | $6,000/月 | $450-2,000/月（デスクあたり） | 0.5x（実は高い） |
| インフラ | 自前設置 | WiFi、コーヒー、会議室込み | 1.5x |

**MVP**:
- タイプ: 物理的スペース（SoHo 1拠点）
- 初期反応: 満室（3-6ヶ月以内）
- CVR: 不明（初期は需要過多）

**UVP（独自の価値提案）**:
- **"We" = Community**: 「仕事場 ≠ オフィス」「コミュニティ空間」
- Neumannのカリスマ: "Elevate the world's consciousness"（世界の意識を高める）
- しかし、曖昧なビジョン → 後にガバナンス問題へ

**競合との差別化**:
- 初期（2010-2012年）: IWG（Regus）が主要競合
  - Regus: ビジネス向け、フォーマル
  - WeWork: クリエイティブ、カジュアル、コミュニティ重視
- しかし、参入障壁低く、競合増加

## 3. ピボット/失敗経験

### 3.1 初期の失敗

**Baby Kneepads（2006-2008年）**:
- Neumannの最初のスタートアップ
- 赤ちゃん用膝当て（クロール時の保護具）
- 失敗理由: 需要不足、単価低すぎ
- 教訓: 「コミュニティ」「大規模市場」への関心

**Green Desk売却（2008-2010年）**:
- Green Deskは成功したが、Neumannは売却を決断
- 理由: 「環境」より「コミュニティ」を重視
- McKelveyを説得し、WeWork立ち上げ

### 3.2 ピボット（該当する場合）

**ピボットなし**:
- WeWorkは一貫して「コワーキングスペース」事業
- しかし、Neumannは"The We Company"へ改名（2019年）
  - WeWork（オフィス）
  - WeLive（住居）
  - WeGrow（学校）
  - 「We」ブランドの拡大戦略
- IPO前に批判され、元の"WeWork"に戻す

## 4. 成長戦略

### 4.1 初期トラクション獲得

**Benchmark Capitalとの出会い（2012年6月）**:
- Series A: $17M（評価額$100M）
- Benchmarkパートナー: Bruce Dunlevie（推定）
- 投資判断理由:
  1. ニューヨーク・サンフランシスコで早期成功
  2. コワーキング市場の成長性
  3. Neumannのカリスマ性
- McKelveyが説得: 「評価額低いが、Benchmarkのブランド価値は高い」

**初期成長（2012-2014年）**:
- 2012年: 7拠点（ニューヨーク、サンフランシスコ）
- 2014年: 30拠点（ロサンゼルス、ロンドン拡大）
- 会員数: 15,000人（2014年）

### 4.2 フライホイール

**WeWorkのフライホイール（理想）**:
1. おしゃれなスペース → メンバー増加
2. メンバー増加 → コミュニティ活性化
3. コミュニティ活性化 → ブランド価値向上
4. ブランド価値向上 → 新規拠点開設容易
5. 新規拠点開設 → さらなるメンバー増加

**実際のフライホイール（失敗）**:
1. 過剰拡大 → 稼働率低下
2. 稼働率低下 → 赤字拡大
3. 赤字拡大 → 資金調達依存
4. 資金調達依存 → バリュエーション急上昇
5. バリュエーション急上昇 → IPO期待値過大
6. IPO失敗 → 崩壊

### 4.3 スケール戦略

**爆発的拡大（2014-2019年）**:

| 年 | 拠点数 | 会員数 | 評価額 |
|----|-------|--------|--------|
| 2014 | 30 | 15,000 | $1.5B |
| 2016 | 160 | 80,000 | $16B |
| 2018 | 485 | 400,000 | $45B |
| 2019年1月 | 528 | 527,000 | $47B |

**グローバル展開**:
- 2018年: 111都市（アメリカ、ヨーロッパ、アジア）
- 日本: 2018年進出（東京、大阪、福岡）
- 中国: 2016年進出（上海、北京）

**SoftBank Vision Fundの影響（2017-2019年）**:
- **2017年3月**: Series F $4.4B（評価額$20B）
- **2018年8月**: Series G $1B（評価額$45B）
- **総額**: $10B+（SoftBankから）
- Masayoshi Sonの戦略: 「世界征服」「急速拡大」
- Neumannは月$150M燃焼（2018年）

### 4.4 バリューチェーン

**収益源**:
1. デスク賃貸: $200-1,200/月（拠点により異なる）
2. 専用オフィス: $3,000-20,000/月
3. エンタープライズ契約: IBM, Microsoft等

**コスト構造（失敗要因）**:
1. **長期賃貸契約**: 10-15年契約（固定費）
2. **内装改装費**: 1拠点あたり$5-20M
3. **運営コスト**: 人件費、光熱費、イベント費
4. **売上 vs コスト**: 短期転貸（変動収益）vs 長期賃貸（固定費）

**unit economicsの崩壊**:
- 2018年: 売上$1.8B、損失$1.9B（売上を上回る赤字）
- 2019年上半期: 売上$1.5B、損失$690M
- 1拠点あたり: 黒字化まで2-4年かかる → 拡大すればするほど赤字

### 4.5 資金調達履歴（VC案件のみ）

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Series A | 2012-06 | $17M | $100M | **Benchmark Capital** | - |
| Series B | 2014-04 | $150M | $1.5B | J.P. Morgan | Benchmark Capital |
| Series C | 2014-06 | $40M | $5B | - | Wellington Management |
| Series D | 2014-12 | $355M | $5B | T. Rowe Price | - |
| Series E | 2016-03 | $430M | $16B | Legend Holdings | - |
| Series F | 2017-03 | $4.4B | $20B | **SoftBank Vision Fund** | - |
| Series G | 2018-08 | $1B | $45B | **SoftBank Vision Fund** | - |
| ピーク | 2019-01 | - | $47B | - | - |

**総資金調達額**: $22B+（債務含む）
**主要VCパートナー**:
- Benchmark Capital: Bruce Dunlevie（推定）
- SoftBank: Masayoshi Son（CEO）

### 資金使途と成長への影響

**Series A + B ($167M、2012-2014年)**:
- 拠点拡大: 7 → 30拠点
- ブランド構築: "We" "Community"マーケティング
- 成長結果: 評価額$100M → $1.5B（15倍）

**SoftBank資金（$10B+、2017-2019年）**:
- 拠点拡大: 160 → 528拠点（3.3倍）
- グローバル展開: 111都市
- 月$150M燃焼（異常な速度）
- 成長結果: 評価額$20B → $47B（2.35倍）
- しかし、unit economics崩壊

### VC関係の構築

**1. VC選考突破（Benchmark、2012年）**:
- Neumannのピッチ: "Elevate the world's consciousness"
- 初期トラクション: ニューヨーク、サンフランシスコで満室
- Benchmarkの評価: コワーキング市場の成長性、Neumannのカリスマ
- McKelveyの役割: 評価額交渉、Benchmarkブランド重視

**2. SoftBankとの関係（2017-2019年）**:
- Masayoshi SonとNeumannの出会い: 2016年
- Sonの評価: "Adam is a genius"（天才）
- 28分のミーティング → $4.4B投資決定（異例の速さ）
- Sonの戦略: 「世界征服」「急速拡大」
- Neumannへの影響: バリュエーション至上主義、現実離れ

**3. IPO準備と投資家の反乱（2019年）**:
- S-1提出（2019年8月14日）でガバナンス問題露呈
- Benchmark含む5投資家がNeumann解任要求
- Jamie Dimon（J.P. Morgan CEO）がNeumannを説得
- Neumann辞任（2019年9月24日）

**4. Benchmarkのリターン**:
- Series A（2012年）: $17M投資（$100M評価額）
- SoftBankへの株式売却: 推定$676.5M（2017-2019年）
- リターン: 約40倍（推定）
- しかし、IPO成功なら100倍以上だった可能性

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| CRM | Salesforce（会員管理） |
| コミュニケーション | Slack（内部）、メールマーケティング |
| 決済 | Stripe（会員費決済） |
| デザイン | 内製（McKelveyチーム） |
| マーケティング | Instagram、イベントマーケティング |
| 物件管理 | 独自システム（不動産管理） |

## 6. 失敗要因分析

### 6.1 主要失敗要因

**1. 創業者ガバナンス問題（P30: 新規パターン提案）**

**20倍議決権株式**:
- Neumannは20倍議決権株式を保有（dual-class stock）
- 実質的に取締役会を支配
- 投資家は反対できない構造

**利益相反取引**:
- **"We"商標売却**: Neumannが個人所有の"We"商標を会社に$5.9Mで売却
  - 批判殺到 → 返金
- **個人不動産取引**: WeWorkが賃貸する物件の一部をNeumann個人が所有
  - 家賃が直接Neumannに流れる構造
- **Gulfstream G650ジェット機**: $60Mのプライベートジェット購入（会社資金）
  - 機内で大麻吸引（違法行為）

**独裁的経営**:
- 批判的な従業員を解雇
- 取締役会の助言を無視
- Sonの"Yes Man"として振る舞う

**2. PMF未達成（P12）**

**unit economicsの崩壊**:
- コスト構造: 長期賃貸契約（10-15年）+ 内装改装費
- 収益構造: 短期転貸（月単位、年単位）
- 問題: 不況・景気後退時に稼働率低下 → 赤字拡大

**継続的赤字**:
- 2018年: 売上$1.8B、損失$1.9B
- 2019年上半期: 売上$1.5B、損失$690M
- 1拠点あたり黒字化: 2-4年（拡大優先で検証不足）

**3. 過剰調達（P28）**

**$22B調達の弊害**:
- バリュエーション$47Bは過大評価
- 「成長至上主義」（Growth-at-all-cost）
- unit economicsを無視した拡大
- 月$150M燃焼（異常）

**SoftBankの影響**:
- $10B+投資（Vision Fund）
- 「世界征服」を煽る
- 現実的な事業計画を無視
- Neumannの独裁を助長

**4. 取締役会衝突（P15）**

**投資家の反乱**:
- Benchmark含む5投資家がNeumann解任要求（2019年9月）
- Jamie Dimon（J.P. Morgan CEO）の説得
- Neumann辞任（2019年9月24日）
- 退職金: $1.7B（批判殺到）

### 6.2 タイミング要因

**COVID-19の直撃（2020年）**:
- 2020年以降、リモートワーク普及
- オフィス需要激減
- WeWorkの稼働率低下（致命的）

**WeWorkモデルの時代錯誤**:
- オフィス回帰の期待は裏切られた
- Zoom, Slack等のリモートワークツールが普及
- コワーキングスペース自体は需要あるが、WeWorkのunit economicsは崩壊

### 6.3 失敗の警告サイン

**S-1で露呈した問題（2019年8月14日）**:
1. **巨額損失**: 売上$1.8B、損失$1.9B
2. **ガバナンス問題**: 20倍議決権、利益相反取引
3. **"We"商標売却**: Neumannが$5.9Mで売却
4. **継続的赤字**: unit economics不成立

**投資家の懸念**:
- 評価額が高すぎる（$47B → $10B下方修正）
- ガバナンス問題
- Neumannの独裁
- 継続的赤字

**IPO撤回（2019年9月30日）**:
- 投資家の需要不足
- Neumann辞任（2019年9月24日）
- 後任CEO: Artie Minson, Sebastian Gunningham
- SoftBank $10B救済（評価額$8Bに下落）

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | コワーキング需要はあるが、WeWorkモデルは過剰 |
| 競合状況 | 2 | IWG（Regus）、国内コワーキングスペースが優位 |
| ローカライズ容易性 | 2 | 日本の不動産市場、賃貸慣行が異なる |
| 再現性（失敗回避） | 2 | unit economics確認すれば可能だが、Neumannモデルは危険 |
| **総合** | 2.25 | WeWorkモデルは日本でも失敗リスク高い |

**日本市場での教訓**:
- unit economicsの確認（長期賃貸 + 短期転貸は危険）
- コワーキングは成長市場だが、WeWorkモデルは不適
- 低コスト運営が鍵（IWGモデル）
- ガバナンス重視（創業者独裁を避ける）

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）での注意点

- **市場規模 ≠ 成功**: コワーキング市場は成長していたが、WeWorkモデルは不適
- **unit economics早期確認**: 1拠点あたりの収益性を確認
- **競合分析**: IWG（Regus）のunit economicsを比較

### 8.2 CPF検証（/validate-cpf）での注意点

- **WTP（支払意思額）**: WeWorkは価格設定が高すぎ、競合が安価
- **継続利用率**: 短期契約モデルは稼働率変動大
- **3U検証**: Urgency（緊急性）が低い場合、景気後退で崩壊

### 8.3 PSF検証（/validate-10x）での注意点

- **10倍優位性なし**: WeWorkは従来オフィスより柔軟だが、10倍優れてはいない
- **参入障壁低い**: 競合が容易に参入
- **UVP曖昧**: "We" "Community"は曖昧で差別化にならない

### 8.4 スコアカード（/startup-scorecard）での評価

**CPFスコア**: 5/10（微妙）
- 問題の深刻度: 5（オフィス探しは面倒だが、必須ではない）
- 市場規模: 7（コワーキング市場は成長中）
- 緊急性: 3（景気後退で需要減）

**PSFスコア**: 4/10（不十分）
- 10倍優位性: 2（柔軟性のみ、価格は劣る）
- UVP明確性: 5（"We"は曖昧）
- 技術的実現性: 8（物理的スペースなので実現容易）

**総合スコア**: 4.5/10
- 成功確率: 低い（unit economics不成立）
- **警告**: ガバナンス問題、過剰調達に注意

### 8.5 ガバナンスチェックリスト（新規提案）

**創業者ガバナンス問題の警告サイン**:
- [ ] 20倍議決権株式（dual-class stock）
- [ ] 利益相反取引（創業者が個人利益を得る構造）
- [ ] 批判的フィードバックの拒絶
- [ ] 取締役会の助言を無視
- [ ] 過剰な個人支出（プライベートジェット等）
- [ ] 違法行為（大麻吸引等）

**対策**:
- 投資家は取締役会で1/3以上の議席確保
- 利益相反取引の禁止条項
- 定期的なガバナンスレビュー
- 創業者の議決権制限（10倍以下）

## 9. 事業アイデア候補

**WeWork失敗から学ぶ「やってはいけないこと」**:

1. **unit economics無視の拡大**
   - 1拠点あたりの収益性確認必須
   - 黒字化まで2-4年 → 拡大速度調整

2. **過剰調達**
   - $22B調達 → 月$150M燃焼
   - 適正な調達額（PMF検証後）

3. **ガバナンス軽視**
   - 20倍議決権株式
   - 利益相反取引
   - 投資家の監視強化

4. **創業者カリスマ依存**
   - "Elevate the world's consciousness"は曖昧
   - 具体的な価値提案が必要

**逆張りアイデア: 低コストコワーキング**:
- unit economics重視（IWGモデル）
- 内装シンプル化（$1-3M/拠点）
- 長期契約推奨（稼働率安定）
- ガバナンス重視（創業者議決権制限）

## 10. Adam Neumannの現在（2025年）

**退職金と資産**:
- WeWorkから$1.7B退職金（2019年）
- 批判殺到したが、SoftBankが支払い
- 現在の純資産: 推定$2.3B（2025年）

**新規ベンチャー: Flow**:
- **2022年8月**: 新会社Flow発表
- 事業内容: 住居版WeWork（共同住宅）
- 資金調達: $350M（Andreessen Horowitz主導）
- 評価額: $1B（pre-money）
- 批判: 「WeWorkの失敗を繰り返すのか?」

**Neumannの教訓**:
- ガバナンス改善: Flowでは議決権制限
- unit economics重視（公表は未確認）
- しかし、住居市場でも同様のリスク

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2010年） | ✅ PASS | Wikipedia, CNBC |
| Series A（2012年6月、$17M、Benchmark主導） | ✅ PASS | Crunchbase, Forbes |
| 評価額$100M（Series A） | ✅ PASS | Crunchbase |
| 評価額$47B（2019年1月ピーク） | ✅ PASS | CNBC, Wall Street Journal |
| IPO撤回（2019年9月30日） | ✅ PASS | Wikipedia, New York Times |
| Neumann解任（2019年9月24日） | ✅ PASS | CNBC, Bloomberg |
| 退職金$1.7B | ✅ PASS | Forbes, Wall Street Journal |
| "We"商標売却$5.9M | ✅ PASS | New York Times, CNBC |
| 破産申請（2023年11月6日） | ✅ PASS | Wikipedia, TechCrunch |
| Benchmark売却$676.5M | ✅ PASS | Crunchbase News |
| Flow資金調達$350M | ✅ PASS | TechCrunch, Bloomberg |
| 20倍議決権株式 | ✅ PASS | S-1（SEC Filing）, Wall Street Journal |
| 総調達額$22B+ | ✅ PASS | Wikipedia, Crunchbase |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Wikipedia - WeWork](https://en.wikipedia.org/wiki/WeWork)
2. [Wikipedia - Adam Neumann](https://en.wikipedia.org/wiki/Adam_Neumann)
3. [CNBC - Ousted WeWork CEO Adam Neumann: $47 billion valuation went to his head](https://www.cnbc.com/2021/11/09/ousted-wework-ceo-adam-neumann-47-billion-valuation-went-to-his-head.html)
4. [Wall Street Journal - The Money Men Who Enabled Adam Neumann and the WeWork Debacle](https://www.wsj.com/articles/the-money-men-who-enabled-adam-neumann-and-the-wework-debacle-11569238305)
5. [New York Times - How Adam Neumann's Over-the-Top Style Built WeWork](https://www.nytimes.com/2019/09/18/business/wework-adam-neumann.html)
6. [Forbes - Adam Neumann's WeWork Disaster Was Years In The Making](https://www.forbes.com/sites/bizcarson/2019/09/24/adam-neumanns-wework-disaster-years-in-the-making/)
7. [Bloomberg - WeWork's Adam Neumann Steps Down as CEO](https://www.bloomberg.com/news/articles/2019-09-24/wework-s-neumann-to-step-down-as-ceo-amid-ipo-turmoil)
8. [TechCrunch - WeWork's bankruptcy is proof that its core business never actually worked](https://techcrunch.com/2023/11/07/wework-bankruptcy-business-bad/)
9. [TechCrunch - Adam Neumann's new residential startup Flow raises $350M](https://techcrunch.com/2022/08/15/adam-neumanns-new-residential-startup-flow-raises-350m/)
10. [Crunchbase - WeWork Company Profile](https://www.crunchbase.com/organization/wework)
11. [Crunchbase News - Report: Adam Neumann, Benchmark Unloaded $676.5M In WeWork Shares Before Failed IPO](https://news.crunchbase.com/startups/report-adam-neumann-benchmark-unloaded-676-5m-in-wework-shares-before-failed-ipo/)
12. [Forbes - WeWork's Neumann Scored $1.7 Billion From SoftBank-WeWork Deal](https://www.forbes.com/sites/sergeiklebnikov/2019/10/22/weworks-neumann-scored-17-billion-from-softbank-wework-deal/)
13. [SEC - WeWork S-1 Filing](https://www.sec.gov/Archives/edgar/data/1533523/000119312519220499/d781982ds1.htm)
14. [Business Insider - The Rise and Fall of Adam Neumann](https://www.businessinsider.com/wework-adam-neumann-timeline-2019-9)
15. [Vanity Fair - The Cult of WeWork](https://www.vanityfair.com/news/2019/11/the-cult-of-wework)
16. [Fast Company - Inside WeWork's Cult of Adam Neumann](https://www.fastcompany.com/90394048/inside-weworks-cult-of-adam-neumann)
17. [Hulu Documentary - WeWork: Or the Making and Breaking of a $47 Billion Unicorn](https://www.hulu.com/movie/wework-or-the-making-and-breaking-of-a-47-billion-unicorn-618186e6-bb4d-48c2-b0f0-52c9c1c7e34e)
18. [Apple TV+ Series - WeCrashed](https://tv.apple.com/us/show/wecrashed/umc.cmc.6qw605uv2rwbzotbjhzj1v07l)
