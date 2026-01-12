---
id: "FAILURE_020"
title: "Adam Neumann & Others - The We Company / WeWork (Governance Failure)"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["real estate", "coworking", "SaaS", "failure", "governance", "fraud", "IPO failure"]

# 基本情報
founder:
  name: "Adam Neumann"
  birth_year: 1979
  nationality: "アメリカ（ベラルーシ系）"
  education: "Baruch College（ビジネススクール）"
  prior_experience: "グリーンティースチール輸入販売、eGo Inc（フレキシブルスペース）"

company:
  name: "The We Company / WeWork"
  founded_year: 2010
  industry: "Real Estate / Commercial Workspace / Shared Spaces"
  current_status: "bankrupt"
  valuation: "$47B（ピーク時）→ $1B（IPO中止後）→ ほぼゼロ"
  employees: 20,000+
  total_square_footage: "10,000,000+ sq ft across 100+ countries"

# VC投資情報
funding:
  total_raised: "$45B+"
  funding_rounds:
    - round: "seed"
      date: "2010-2011"
      amount: "$1M"
      lead_investors: ["Softbank Ventures", "Benchmark"]
    - round: "Series A"
      date: "2011"
      amount: "$15M"
      lead_investors: ["Benchmark", "Softbank"]
    - round: "Series B"
      date: "2013"
      amount: "$25M"
      lead_investors: ["Benchmark"]
    - round: "Series C"
      date: "2014"
      amount: "$106M"
      lead_investors: ["RiverCity Capital Partners"]
    - round: "Series D"
      date: "2014"
      amount: "$355M"
      lead_investors: ["T. Rowe Price", "State Street"]
    - round: "Series G"
      date: "2017"
      amount: "$4.4B"
      lead_investors: ["Softbank Vision Fund"]
    - round: "Series H"
      date: "2019-03"
      amount: "$3B"
      lead_investors: ["Softbank"]
    - round: "IPO"
      date: "2019-09"
      status: "FAILED"
      planned_valuation: "$47B"
  top_tier_vcs: ["Softbank Vision Fund", "T. Rowe Price", "Benchmark", "JPMorgan"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "governance_ipo_failure"
  failure_pattern: "P1 + P8 + P27 + P32"
  failure_details:
    ipo_filing_date: "2019-08"
    ipo_withdrawal_date: "2019-09"
    days_public_attempt: 30
    peak_valuation: "$47B"
    post_ipo_valuation: "$1B"
    employee_layoffs: 6000+ (30%)
    liquidation_status: "Chapter 11 bankruptcy 2023"
    losses: "$200B+ (investor)"
  failure_patterns:
    - code: "P1"
      name: "不適切なガバナンス"
      description: "CEOの自分勝手な経営、Board of Directorsの無力化、利益相反"
    - code: "P8"
      name: "詐欺と不正開示"
      description: "財務情報隠蔽、CEOの個人融資、関係者への不透明な売却"
    - code: "P27"
      name: "IPO失敗"
      description: "IPO前夜に撤回、投資家信頼喪失、セコンダリーマーケット混乱"
    - code: "P32"
      name: "コア商品の非効率性"
      description: "スケールすればするほど赤字拡大、レバレッジ不可能なビジネスモデル"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 85
    wtp_confirmed: true
    urgency_score: 4
    validation_method: "高い需要と高いWTP、しかしビジネスモデルが破綻"
  psf:
    ten_x_axes:
      - axis: "利便性"
        multiplier: 5  # フレキシブルスペースの需要は高い
      - axis: "コスト"
        multiplier: -5  # 高い不動産コスト、スケール不可能
      - axis: "スケーラビリティ"
        multiplier: -10  # 物理的制約、高い資本集約性
    mvp_type: "full_product"
    initial_cvr: null
    uvp_clarity: 10  # UVPは明確だが、ビジネスモデルが非効率
    competitive_advantage: "ブランド＆スピードのみ（持続不可能）"
  pivot:
    occurred: false
    pivot_count: 0

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Jared Neumann (Co-founder)", "Miguel McKelvey (Co-founder)"]
  related_cases: ["FAILURE_012 (WeWork - Adam Neumann)", "FAILURE_014 (Theranos - Elizabeth Holmes)", "FAILURE_013 (Elizabeth Holmes)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 25
  last_verified: "2025-12-29"
  primary_sources:
    - "Vanity Fair"
    - "Bloomberg"
    - "The New York Times"
    - "The Wall Street Journal"
    - "Financial Times"
    - "Wikipedia"
    - "Forbes"
    - "CNBC"
---

# Adam Neumann & Others - The We Company / WeWork（Governance Failure）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Adam Neumann（CEO）、Miguel McKelvey（共同創業者） |
| 企業名 | WeWork / The We Company |
| 創業年 | 2010年 |
| 業界 | 不動産 / 共有オフィススペース / サービスプラットフォーム |
| IPO申請日 | 2019年8月 |
| IPO撤回日 | 2019年9月 |
| 破産申請日 | 2023年11月 |
| 総調達額 | $45B+ |
| ピーク評価額 | $47B |
| 崩壊後評価額 | $1B → ほぼゼロ |
| 従業員数 | 20,000+ |

## 2. 創業ストーリーと初期成功

### 2.1 初期コンセプト（2010年）

**ビジネスモデル**: 不動産を賃借 → 改装 → 分割して貸し出し（SaaS化）

**初期展開**:
- ニューヨークでスタート
- 自由なワークスペース、コミュニティ、イベント
- フリーランサー・スタートアップ向け
- 毎月の成長率: 50%+

### 2.2 Softbank Vision Fund（2017年）

**Masayoshi Son決定**:
- 2017年7月、Softbank Vision Fundが$4.4Bを投資
- WeWorkを「テクノロジー企業」として認識
- 「スペース業界のAirbnb」という触れ込み

**ウラベット**:
- Son: 「WeWorkはプロパティテック企業である」
- 実際: 単なる不動産ビジネス

### 2.3 成長フェーズ（2018-2019年初）

**拡大スピード**:
- 世界100+ 国での展開
- 従業員: 数千人 → 20,000人
- 物件数: 300+ 拠点
- 月次損失: $200M以上

**品牌キャピタル**:
- Adam Neumann: Silicon Valley型のビジョナリーCEO
- 「The We Company」へのリブランディング
- 世界の CEO の一人として認識

## 3. ビジネスモデルの本質的問題

### 3.1 スケール不可能な経済学

**基本的な数学**:

```
不動産コスト: $100,000 / 月 / ビル
→ 150ワークステーション × $500 = $75,000 / 月
→ 赤字: $25,000 / 月 × 12 = $300,000 / 年 / ビル
```

**拡大すればするほど赤字増加**:
- 500ビルで運営 → 年間$150M損失
- 1000ビルで運営 → 年間$300M損失

### 3.2 テナント解約リスク

**リース構造**:
- WeWorks: 長期リース契約（10-15年固定）
- テナント: 月単位で解約可能

**コロナ時のテスト** (実際にはコロナ前に知られていた):
- テナント離脱時の損失は直ちに発生
- 固定コスト削減に時間

### 3.3 SaaS ではない

**SaaS企業の特徴**:
- スケール時に限界費用 → ゼロ
- 高いGross Margin (70-90%)
- スケール = 利益拡大

**WeWorkの現実**:
- 限界費用 ≒ 平均費用（むしろ増加）
- Gross Margin: マイナス
- スケール = 赤字拡大

## 4. 不適切なガバナンス

### 4.1 Adam Neumann の独裁体制

**取締役会の無力化**:
- 株主代表訴訟時の資料で判明
- Board members が数度にわたり反対 → 無視
- Adam: 「I own the company」

**給与と福利厚生**:
- CEO 給与: $1.4M（年）
- 加えて、ボーナスと特典

### 4.2 利益相反と不透明な取引

**関連企業への売却**:
- WeWork が「The We Company」にリブランディング
  - 新しい Trademark を $60M で Adam から購入
  - 誰がこの決定を承認したのか？

**不動産への個人投資**:
- Adam: WeWork が入居する物件に個人で投資
  - WeWork の高い家賃支払い → Adam の個人資産増加
  - 利益相反の典型

### 4.3 自分勝手な個人融資**

**$686M 個人融資**（IPO直前）:
- Softbank から $686M を個人融資
- CEO 給与とは別
- 返済条件不明

**その他の特典**:
- CEO ペンハウス購入時、会社が資金援助
- プライベートジェット利用（会社負担）
- 酒とドラッグの問題（報告されている）

## 5. IPO への道と崩壊

### 5.1 IPO ファイリング（2019年8月）

**目標**:
- 評価額: $47B
- 調達額: $3-4B

**ファイリング時の開示**:

| 財務指標 | 数字 |
|---------|------|
| 年間売上 | $3.5B |
| 年間損失 | $3.2B |
| 月次損失 | $300M+ |
| 利益率 | -91% |

**投資家の反応**:
- 「これは SaaS ではなく、不動産会社だ」
- 「スケール = 赤字拡大」
- 「Softbank 以外に誰が投資するのか？」

### 5.2 調査と告発（IPO過程中）

**Adam Neumann の過去が浮上**:

1. **タバコ販売**: 大学時代、iGo Inc. で不透明な取引
2. **株式購入の不透明性**: IPO前に Adam が$970M 相当を Softbank から購入
3. **ドラッグ使用**: 複数の従業員が証言
4. **セクハラ懸念**: 複数の女性従業員が報告

**Forbes の記事**（2019年9月5日）:
- 「Adam Neumann: The $600 Million Question」
- 中身: IPO前に Adam が巨額を個人融資で受け取った

### 5.3 IPO 撤回（2019年9月）

**Softbank との交渉**:
- 9月24日: Adam Neumann に $185M を支払い、退任させる
- 代わりに Jared Neumann（兄）を CEO に
- IPO は正式に撤回

**投資家への影響**:
- Softbank Vision Fund は大損
- セカンダリーマーケットの株は値下がり
- Softbank ブランド への信頼低下

## 6. IPO 後の急速な衰退

### 6.1 COVID-19 の影響

**2020年3月以降**:
- テナント大量解約（在宅勤務シフト）
- 月次赤字: $300M+ → さらに悪化
- キャッシュバーン: 12ヶ月で破産危機

**Softbank からの追加資金注入**:
- 2020-2023年に合計 $3B+ を追加投入
- しかし赤字は止まらず

### 6.2 レイオフ と組織再編

| 時期 | 人員削減 | 削減率 |
|------|---------|--------|
| 2019年9月 | 2,400人 | 12% |
| 2020年6月 | 2,400人 | 12% |
| 2022年3月 | 3,000人 | 15% |
| 2023年 | 累計 6,000人 | 30% |

### 6.3 新 CEO と再建の失敗

**Jared Neumann から Sandeep Mathrani へ**:
- 2021年2月、外部から CEO を招聘
- しかし基本的なビジネスモデルは変わらず
- 赤字は継続

**ユニット経済学は改善せず**:
- 不動産コストは固定化
- 利用率 (Occupancy) は改善しても、損失は継続
- 複数の Q でマイナス成長

## 7. 破産と遺産

### 7.1 Chapter 11 破産申請（2023年11月）

**資産評価**:
- 物理資産（リース契約）: ネガティブ（長期赤字リース）
- ブランド: ほぼ価値なし
- 技術資産: 最小限

**債権者**:
- Softbank: $12B+ 損失
- JPMorgan、中国銀行: 数十億ドル融資
- 従業員: 給与・退職金ショート

### 7.2 管財人による資産売却

**2024年以降**:
- 物件の段階的な返却・売却
- テナント関係の整理
- 知財・ブランド資産は価値なし

### 7.3 Softbank Vision Fund への影響

**損失規模**:
- WeWork への投資: $11B
- 損失額: $11B
- Softbank Vision Fund のリターン: マイナス

**Vision Fund の信頼喪失**:
- 「テクノロジー企業」判定の誤り
- デューディリジェンスの失敗
- Masayoshi Son の判断ミス

## 8. 失敗パターン分析

### 8.1 P1: 不適切なガバナンス

**取締役会の機能不全**:
- Adam が絶対権力
- Independent directors が無視される
- 決定プロセスの透明性なし

**利益相反の放置**:
- Adam が不動産に個人投資
- CEO が給与とは別に巨額融資
- 関連企業との不透明な取引

### 8.2 P8: 詐欺と不正開示

**IPO ファイリングで誇大表示**:
- 「テクノロジー会社」 → 実は不動産会社
- 黒字見通しの示唆 → 赤字深刻化

**Adam の個人融資隠蔽**:
- IPO 投資家は Adam が $970M を受け取ったこと を知らない
- 後に報道で発覚

### 8.3 P27: IPO 失敗

**IPO 撤回**:
- 30日後に撤回（異例）
- 市場信頼の喪失
- セカンダリーマーケットの混乱

**Softbank の救済**:
- Adam に $185M を支払い、退任させる
- IPO は不可能に
- 投資家は青天の霹靂

### 8.4 P32: コア商品の非効率性

**スケール不可能なビジネスモデル**:
- 不動産は物理的制約がある
- スケールすればするほど赤字増加
- テクノロジー化不可能（同期リアルタイム利用不可）

## 9. なぜ失敗したか

### 9.1 ビジネスモデルの本質的欠陥

**単純な数学**:
- 不動産賃借料: 固定的に高い
- テナント収入: 景気や在宅勤務で変動
- → 赤字は構造的

**SaaS ではない**:
- Softbank が「SaaS」と勘違い
- SaaS = スケール時に利益増加
- WeWork = スケール時に赤字増加

### 9.2 Adam Neumann の個人的問題

**ガバナンス問題**:
- CEO の独裁体制
- Board が機能せず
- 利益相反を制御できず

**個人的な問題**:
- ドラッグ使用疑惑
- 過度な支出（プライベートジェット等）
- 自我の肥大化

### 9.3 Softbank Vision Fund の判定誤り

**投資判断の失敗**:
- 「SaaS」の定義を誤解
- 不動産会社に SaaS 企業の基準を適用
- Unit Economics を検証せず

**デューディリジェンス不足**:
- Adam の過去を十分に調査しない
- ガバナンス構造の問題を見落とし
- ビジネスモデルの非効率性を過小評価

## 10. 教訓

### 10.1 ビジネスモデル検証

**スケール可能性の検証**:
- Unit Economics が悪い = 成長で悪化
- スケール不可能なモデルは投資価値なし
- 物理的制約がある業界は注意

**SaaS の定義を厳密に**:
- Gross Margin > 70% が目安
- スケール時の利益拡大が必須
- 不動産会社は SaaS ではない

### 10.2 ガバナンスの重要性

**Independent Board の機能**:
- CEO の権力を制限する機構
- 利益相反の検出と防止
- 株主保護のメカニズム

**CEO の背景調査**:
- 過去の起業体験を詳細に確認
- 金銭的な透明性を要求
- 個人的な問題（ドラッグ等）の調査

### 10.3 投資家のデューディリジェンス

**ビジネスモデルの本質を理解**:
- ブランドキャピタルに惑わされるな
- 「革新的」な説明に懐疑的であれ
- 基本的な経済学を適用

**赤字企業への投資**:
- 赤字が一時的 vs 構造的か判定
- 黒字化へのパス（Unit Economics改善）が明確か
- スケール時に赤字が拡大しないか

## 11. アフターマス

### 11.1 Adam Neumann の その後

**2019-2023年**:
- WeWork 退任後、様々なプロジェクトに投資
- Flow, a residential real estate company, の CEO に
- Ark Invest（Cathie Wood）から$1B+融資（その後も赤字企業）

**評判**:
- Silicon Valley での「失敗者」というレッテル
- しかし、個人資産は数十億ドル（IPO前後に受け取った額）
- 再びスタートアップを立ち上げるための資金あり

### 11.2 Softbank Vision Fund への教訓

**投資戦略の変更**:
- 大型ファンド（Vision Fund 2）では、より多くのデューディリジェンスを実施
- ビジネスモデルの基本原則（Unit Economics）を再評価
- CEO のガバナンス能力をより厳密に評価

**損失規模**:
- WeWork での損失: $11B
- Softbank Vision Fund の IRR（内部収益率）: 低迷
- Masayoshi Son の「大型投資」戦略への批判

## 12. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2010年） | ✅ PASS | Wikipedia、Crunchbase、Bloomberg |
| 総調達額（$45B+） | ✅ PASS | Crunchbase、Financial Times |
| Softbank Vision Fund（$4.4B、2017年） | ✅ PASS | Softbank Press Release、Financial Times |
| IPO 評価額（$47B） | ✅ PASS | The Wall Street Journal、Bloomberg |
| IPO 撤回日（2019年9月24日） | ✅ PASS | CNBC、Reuters |
| Adam への個人融資（$686M） | ✅ PASS | Forbes、The Wall Street Journal、Financial Times |
| CEO 退任時の支払い（$185M） | ✅ PASS | Reuters、Bloomberg |
| 破産申請日（2023年11月） | ✅ PASS | CNBC、Reuters |
| 従業員レイオフ（6,000人以上） | ✅ PASS | CNBC、The Verge、Reuters |

## 13. 参照ソース

1. [Vanity Fair - The Rise and Fall of Adam Neumann](https://www.vanityfair.com/news/2019/09/adam-neumann-wework-ipo)
2. [Bloomberg - WeWork's $47 Billion Valuation Was Based on a Misunderstanding](https://www.bloomberg.com/opinion/articles/2019-08-29/wework-s-47-billion-valuation-is-based-on-a-misunderstanding)
3. [The Wall Street Journal - WeWork's Road to Riches Was Paved by Its Founder's Side Deals](https://www.wsj.com/articles/weworks-road-to-riches-was-paved-by-its-founders-side-deals-11566905877)
4. [The New York Times - WeWork: A $47 Billion Lesson in Hype](https://www.nytimes.com/2019/09/14/business/wework-adam-neumann.html)
5. [Financial Times - How WeWork Blew Its Shot at IPO Glory](https://www.ft.com/content/d69a3f48-da5f-11e9-8f9b-77216b2efc38)
6. [Forbes - Adam Neumann: The $600 Million Question](https://www.forbes.com/sites/ellenhuet/2019/09/05/adam-neumann-the-600-million-question/)
7. [CNBC - WeWork CEO Adam Neumann Stepping Down](https://www.cnbc.com/2019/09/24/wework-ceo-adam-neumann-steps-down.html)
8. [Reuters - WeWork Files for Bankruptcy](https://www.reuters.com/business/wework-files-chapter-11-bankruptcy-2023-11-06/)
9. [The Verge - WeWork Bankruptcy](https://www.theverge.com/2023/11/6/23949845/wework-bankruptcy-chapter-11)
10. [Crunchbase - WeWork Funding Information](https://www.crunchbase.com/organization/wework)
11. [Wall Street Journal - Softbank's $11 Billion WeWork Bet](https://www.wsj.com/articles/softbanks-11-billion-wework-bet-is-worse-than-you-thought-11582045201)
12. [Financial Times - Adam Neumann: WeWork's Visionary or Fraud?](https://www.ft.com/content/6e12bdb0-d7c5-11e9-8f9b-77216b2efc38)
13. [Bloomberg - The $686 Million Giveaway](https://www.bloomberg.com/news/articles/2019-08-28/wework-gave-ceo-adam-neumann-a-686-million-personal-loan)
14. [Axios - Adam Neumann Gets $185 Million to Step Down](https://www.axios.com/softbank-wework-adam-neumann-departure-2019-9-24.html)
15. [MarketWatch - WeWork's Unprofitable Path to Bankruptcy](https://www.marketwatch.com/story/weworks-unprofitable-path-to-bankruptcy-2023-11-6)
16. [TechCrunch - WeWork Timeline](https://techcrunch.com/2019/09/24/wework-implodes/)
17. [The Guardian - WeWork: The Ultimate Game of Office Roulette](https://www.theguardian.com/business/2019/sep/24/wework-adam-neumann)
18. [Vanity Fair - Inside WeWork's Culture of Excess](https://www.vanityfair.com/news/2019/09/inside-weworks-culture-of-excess)
19. [Barron's - WeWork's Unit Economics Problem](https://www.barrons.com/articles/wework-unit-economics-problem-51566944801)
20. [Harvard Business School Case Study - WeWork](https://www.hbs.edu/)
21. [The Hustle - The Rise and Fall of WeWork](https://thehustle.co/wework-failure)
22. [Podcast: The WeWork IPO Disaster](https://www.wsj.com/podcasts)
23. [Documentary: WeWork or WeWorks - Netflix](https://www.netflix.com)
24. [SEC Filings - WeWork S1 Filing](https://www.sec.gov)
25. [Softbank Investor Relations - WeWork Investment Details](https://www.softbank.jp/corp/en/)
