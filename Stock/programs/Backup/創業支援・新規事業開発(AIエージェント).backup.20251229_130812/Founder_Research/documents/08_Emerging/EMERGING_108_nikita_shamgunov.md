---
id: "EMERGING_108"
title: "Nikita Shamgunov - SingleStore"
category: "founder"
tier: "emerging"
type: "case_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["database", "real-time_analytics", "distributed_systems", "in-memory_database", "y_combinator", "microsoft", "facebook"]

# 基本情報
founder:
  name: "Nikita Shamgunov"
  birth_year: null
  nationality: "Russian-American"
  education: "PhD in Computer Science"
  prior_experience: "Microsoft SQL Server (5+ years), Facebook Infrastructure Engineer, ACM Programming Contest World Medalist"

company:
  name: "SingleStore (formerly MemSQL)"
  founded_year: 2011
  industry: "Database / Real-time Analytics"
  current_status: "acquired_by_pe"
  valuation: "$1.3B (2022年時点)"
  employees: 300+

# VC投資情報
funding:
  total_raised: "$558M"
  funding_rounds:
    - round: "seed"
      date: "2011"
      amount: "不明"
      valuation_post: "不明"
      lead_investors: ["Y Combinator"]
      other_investors: []
    - round: "series_a"
      date: "2013-05"
      amount: "$5M"
      valuation_post: "不明"
      lead_investors: ["Khosla Ventures"]
      other_investors: ["First Round Capital"]
    - round: "series_b"
      date: "2014-01"
      amount: "$35M"
      valuation_post: "不明"
      lead_investors: ["Accel"]
      other_investors: ["Khosla Ventures", "Data Collective"]
    - round: "series_c"
      date: "2017-06"
      amount: "$36M"
      valuation_post: "不明"
      lead_investors: ["REV Venture Capital", "Caffeinated Capital"]
      other_investors: ["Accel", "Khosla Ventures", "Data Collective"]
    - round: "series_d"
      date: "2018-12"
      amount: "$50M"
      valuation_post: "不明"
      lead_investors: ["GV (Google Ventures)"]
      other_investors: ["Glynn Capital", "Dell Technologies Capital"]
    - round: "series_e"
      date: "2020-12"
      amount: "$80M"
      valuation_post: "$940M"
      lead_investors: ["Insight Partners"]
      other_investors: []
    - round: "series_f"
      date: "2021-09"
      amount: "$80M"
      valuation_post: "$940M"
      lead_investors: ["Prosperity7 Ventures"]
      other_investors: []
    - round: "series_f_extension"
      date: "2022-10"
      amount: "$146M"
      valuation_post: "$1.3B"
      lead_investors: ["Goldman Sachs"]
      other_investors: []
  top_tier_vcs: ["Accel", "GV (Google Ventures)", "Khosla Ventures", "Goldman Sachs"]

# 成功/失敗/Pivot分類
outcome:
  category: "pivot"
  subcategory: "product_pivot_success"
  failure_pattern: null
  pivot_details:
    count: 2
    major_pivots:
      - id: "memory_to_hybrid"
        trigger: "market_feedback"
        date: "2016-2018"
        decision_speed: "24ヶ月"
        before:
          idea: "インメモリ専用データベース（MemSQL）"
          target_market: "高速トランザクション処理が必要な企業"
          business_model: "エンタープライズライセンス"
          cpf_score: 7
        after:
          idea: "ハイブリッド分散SQLデータベース（メモリ+ディスク）"
          hypothesis: "OLTPとOLAPを統合した単一プラットフォームが必要"
        resources_preserved:
          team: "コアエンジニアリングチーム維持"
          technology: "分散アーキテクチャと高速SQL処理エンジン"
          investors: "全投資家継続参加"
        validation_process:
          - stage: "顧客フィードバック収集"
            duration: "6ヶ月"
            result: "99%の収益がインメモリ以外のユースケースから"
          - stage: "ハイブリッドアーキテクチャ開発"
            duration: "18ヶ月"
            result: "ディスク+メモリ統合成功"
      - id: "rebrand_to_singlestore"
        trigger: "product_evolution"
        date: "2020-10"
        decision_speed: "即時"
        before:
          idea: "MemSQL（メモリ中心のブランディング）"
          target_market: "高速処理が必要な大企業"
          business_model: "エンタープライズライセンス"
          cpf_score: 8
        after:
          idea: "SingleStore（統合データプラットフォーム）"
          hypothesis: "単一プラットフォームでOLTP+OLAP+分析+AIを実現"
        resources_preserved:
          team: "全チーム維持"
          technology: "全技術資産維持"
          investors: "全投資家継続"
        validation_process:
          - stage: "ブランド変更発表"
            duration: "1ヶ月"
            result: "顧客混乱なし、ポジショニング明確化"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 90
    wtp_confirmed: true
    urgency_score: 9
    validation_method: "大手企業（Dell, GE, Comcast）との直接契約"
  psf:
    ten_x_axes:
      - axis: "クエリ速度"
        multiplier: 100
      - axis: "スケーラビリティ"
        multiplier: 50
      - axis: "データ統合"
        multiplier: 20
    mvp_type: "enterprise_pilot"
    initial_cvr: null
    uvp_clarity: 9
    competitive_advantage: "インメモリ+ディスクハイブリッド、OLTP+OLAP統合、リアルタイム分析"
  pivot:
    occurred: true
    pivot_count: 2
    pivot_trigger: "customer_feedback"
    original_idea: "インメモリ専用高速データベース"
    pivoted_to: "ハイブリッド分散SQLデータベースプラットフォーム"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Eric Frenkiel (SingleStore Co-founder)", "Sam Madden (MIT Database Research)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 18
  last_verified: "2025-12-29"
  primary_sources:
    - "https://www.ycombinator.com/companies/singlestore"
    - "https://techcrunch.com/2020/12/08/singlestore-formerly-memsql-raises-80m-to-integrate-and-leverage-companies-disparate-data-silos/"
    - "https://www.crunchbase.com/organization/memsql"
    - "https://en.wikipedia.org/wiki/SingleStore"
---

# Nikita Shamgunov - SingleStore

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Nikita Shamgunov |
| 生年 | 不明 |
| 国籍 | ロシア系アメリカ人 |
| 学歴 | コンピュータサイエンス博士号（BS, MS, PhD） |
| 創業前経験 | Microsoft SQL Server（5年以上）、Facebook インフラエンジニア、ACMプログラミングコンテスト世界メダリスト |
| 企業名 | SingleStore（旧MemSQL） |
| 創業年 | 2011年 |
| 業界 | データベース / リアルタイム分析 |
| 現在の状況 | PE買収済（Vector Capital、2025年9月） |
| 評価額/時価総額 | $1.3B（2022年）|

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- Microsoft SQL Serverでの5年以上の経験から、従来のデータベースアーキテクチャの限界を認識
- Facebookのインフラエンジニアとして、スケールする分散システムの必要性を実感
- RAM価格の低下とマルチコアプロセッサの普及により、インメモリデータベースが実現可能に
- 既存データベース（Oracle, MySQL）は10-20年前の技術で設計され、現代のハードウェアを活用できていない

**需要検証方法**:
- Y Combinator応募前に、大手企業（銀行、通信会社）にヒアリング
- リアルタイム分析と高速トランザクション処理の両方が必要な企業が多数存在
- 既存ソリューション（Oracle RAC、MySQL Cluster）はコストが高く、複雑で、スケールしない

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 推定30+（大手銀行、通信会社、EC企業）
- 手法: 直接訪問、技術デモ、パイロットプロジェクト
- 発見した課題の共通点:
  - 既存データベースではリアルタイム分析が不可能（バッチ処理で数時間遅延）
  - OLTPとOLAPを別システムで運用するコストと複雑性
  - データ量増加に対するスケーラビリティ問題

**3U検証**:
- Unworkable（現状では解決不可能）: 既存データベースではミリ秒単位のリアルタイム分析が技術的に不可能
- Unavoidable（避けられない）: データ量は指数関数的に増加し、リアルタイム意思決定が競争優位性の鍵
- Urgent（緊急性が高い）: 競合企業がリアルタイムデータ活用で優位に立つリスク

**支払い意思（WTP）**:
- 確認方法: エンタープライズパイロット契約（初期顧客: Zynga, Comcast, Akamai）
- 結果: 年間$100K-$1M+の契約が複数成立（2013-2014年）

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 |
|---|------------|-----------------|------|
| クエリ速度 | MySQL: 数秒〜数分 | SingleStore: ミリ秒単位 | 100x |
| スケーラビリティ | シャーディングで手動管理 | 自動分散、線形スケール | 50x |
| データ統合 | OLTP/OLAP分離、ETL必要 | 単一プラットフォーム | 20x |
| 同時実行性 | ロック競合で性能劣化 | MVCC + ロックフリー | 10x |
| 運用コスト | DBA必須、複雑な設定 | クラウドネイティブ、自動化 | 5x |

**MVP**:
- タイプ: Enterprise Pilot（Zyngaとの初期契約）
- 初期反応: 2012年、Zyngaのゲーム分析で既存MySQL比100倍高速化
- CVR: パイロット顧客の80%が本契約に移行

**UVP（独自の価値提案）**:
- インメモリ処理による100倍高速なクエリ実行
- 分散アーキテクチャによる線形スケーラビリティ
- OLTP（トランザクション）とOLAP（分析）を単一システムで実行
- SQL互換性（既存アプリケーションの移行が容易）
- クラウドネイティブ（AWS, Azure, GCPで利用可能）

**競合との差別化**:
- Oracle: 高額ライセンス、レガシーアーキテクチャ
- MySQL/PostgreSQL: シングルノードの限界、分析性能不足
- MongoDB: SQL非対応、トランザクション性能不足
- SingleStore: インメモリ+ディスクハイブリッド、OLTP+OLAP統合、SQL互換

## 3. ピボット/失敗経験

### 3.1 初期の失敗

**技術的賭けの誤算**:
- 創業時、RAMが主要ストレージになると予測（フラッシュメモリではなく）
- 実際にはSSD（フラッシュメモリ）の価格が急速に低下し、RAM価格は予想より下がらず
- 「MemSQL」という名前がインメモリ専用という誤解を生み、市場機会を制限

**顧客フィードバックによる発見**:
- 2017年時点で、収益の99%がインメモリ以外のユースケースから
- 顧客は高速性を求めていたが、コスト効率も重要視
- CEO就任時（2017年）のARRは約$7M、成長が停滞

### 3.2 ピボット（該当する場合）

#### ピボット1: インメモリ専用→ハイブリッド分散データベース（2016-2018年）

- **元のアイデア**: MemSQL - インメモリ専用高速データベース
- **ピボット後**: ハイブリッド分散SQLデータベース（メモリ+ディスク統合）
- **きっかけ**: 顧客の99%がインメモリ以外のユースケースで利用している事実
- **学び**:
  - 顧客は「最速」よりも「十分速くてコスト効率が良い」を求める
  - 単一機能（インメモリ）ではなく、統合プラットフォームが真のニーズ
  - プロダクト名とポジショニングの重要性

**ピボット詳細**:
- アーキテクチャ改良: カラムストア（分析用）とロウストア（トランザクション用）の統合
- ディスクベースストレージのサポート追加（コスト削減）
- リアルタイムデータ取り込み（Kafka, S3統合）
- 結果: ARR $7M → $40M（2017-2020年）

#### ピボット2: MemSQL → SingleStore リブランディング（2020年10月）

- **元のアイデア**: MemSQL（メモリ中心のブランド）
- **ピボット後**: SingleStore（統合データプラットフォーム）
- **きっかけ**: プロダクトの進化（OLTP+OLAP+分析+AI統合）
- **学び**:
  - ブランド名は顧客の認識を制限する（「MemSQL = インメモリ専用」という誤解）
  - リブランディングはポジショニング戦略の重要な一部
  - 「Single」は「統合」を意味し、複数システムを置き換える価値を明確化

**ピボット詳細**:
- 2020年10月27日にMemSQLからSingleStoreに正式改名
- 新ブランドメッセージ: "One Platform for All Data Workloads"
- 同時に$80M Series E調達（Insight Partnersリード）
- 結果: ブランド認知向上、ARR $100M+達成（2023年）

## 4. 成長戦略

### 4.1 初期トラクション獲得

**Y Combinator期間（2011年）**:
- Y Combinatorに採択され、オフィスで1年間寝泊まりしながら開発
- デモデーで投資家の注目を集める
- Khosla Ventures主導でSeries A $5M調達（2013年）

**初期顧客獲得**:
- 2012年: Zyngaがパイロット顧客（ゲーム分析で100倍高速化）
- 2013年: 正式版リリース（v1.0）
- 2014年: Comcast, Akamai等の大手企業が採用
- フリーミアムモデル導入（128GB以下は無料）

### 4.2 フライホイール

```
大手企業パイロット成功
  ↓
ケーススタディ公開（Dell 100x高速化等）
  ↓
エンタープライズ営業の信頼性向上
  ↓
新規顧客獲得（Fortune 100企業）
  ↓
ARR成長 → 追加資金調達
  ↓
プロダクト改善（クラウドネイティブ化等）
  ↓
顧客満足度向上（NPS 70+）
  ↓
リファラル増加
  ↓
（最初に戻る）
```

### 4.3 スケール戦略

**技術スケール**:
- 2015年: Spark統合（ビッグデータエコシステム参入）
- 2018年: Kubernetesサポート（クラウドネイティブ化）
- 2019年: SingleStore Managed Service（フルマネージド版）
- 2021年: ベクトル検索サポート（AI/ML対応）
- 2023年: SingleStore Kai（MongoDB互換API）

**ビジネススケール**:
- 2017年: Nikita ShamgunovがCEO就任、ARR $7M
- 2020年: ARR $40M達成、リブランディング
- 2023年: ARR $110M達成
- 2025年: ARR $123M、YoY成長率23%

**パートナーシップ**:
- AWS, Azure, Google Cloud Marketplaceで提供
- Dell Technologies Capitalから戦略投資
- IBM、Google Venturesから投資

### 4.4 バリューチェーン

**収益源**:
1. SingleStore Managed Service（クラウドSaaS）- 従量課金
2. SingleStore DB（セルフホスト）- 年間サブスクリプション
3. エンタープライズサポート契約
4. プロフェッショナルサービス（移行支援、最適化コンサル）

**コスト構造**:
- R&D（主要コスト）: データベースエンジン改良、新機能開発
- クラウドインフラ（AWS, GCP, Azure）
- エンタープライズ営業チーム（Fortune 100顧客対応）
- カスタマーサクセス

## 4.5 資金調達履歴（VC案件のみ）

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Seed | 2011 | 不明 | 不明 | Y Combinator | - |
| Series A | 2013年5月 | $5M | 不明 | Khosla Ventures | First Round Capital |
| Series B | 2014年1月 | $35M | 不明 | Accel | Khosla, Data Collective |
| Series C | 2017年6月 | $36M | 不明 | REV, Caffeinated | Accel, Khosla |
| Series D | 2018年12月 | $50M | 不明 | GV (Google) | Glynn, Dell Tech Capital |
| Series E | 2020年12月 | $80M | $940M | Insight Partners | - |
| Series F | 2021年9月 | $80M | $940M | Prosperity7 | - |
| Series F Ext | 2022年10月 | $146M | $1.3B | Goldman Sachs | - |

**総資金調達額**: $558M（一部ソースでは$464M）
**主要VCパートナー**: Accel, GV, Khosla Ventures, Goldman Sachs

### 資金使途と成長への影響

**Series A-B ($40M, 2013-2014)**:
- プロダクト開発: コアエンジンの安定化、SQL互換性向上
- 初期顧客獲得: エンタープライズ営業チーム構築
- 成長結果: 顧客数 5 → 50+、Fortune 500企業が採用開始

**Series C-D ($86M, 2017-2018)**:
- ハイブリッドアーキテクチャ開発（メモリ+ディスク）
- クラウドネイティブ化（Kubernetes対応）
- 成長結果: ARR $7M → $40M

**Series E-F ($306M, 2020-2022)**:
- SingleStore Managed Service開発（フルマネージド版）
- グローバル展開（EMEA, APACセールス強化）
- 成長結果: ARR $40M → $110M+

### VC関係の構築

1. **Y Combinator突破**:
   - 分散システムとデータベースの深い技術的専門性
   - Microsoft, Facebookでの実績が信頼を構築
   - ACMプログラミングコンテスト世界メダルが技術力の証明

2. **Tier 1 VC調達成功**:
   - Khosla Ventures: データベース分野への投資実績（MongoDB等）
   - Accel: エンタープライズSaaS専門（Slack, Atlassian等）
   - GV (Google): 技術検証能力、Google内部利用検討

3. **PE買収（2025年9月）**:
   - Vector Capitalが買収（IPOではなくPE Exit）
   - ARR $123M、成長率23%の段階
   - エンタープライズ市場での安定成長を評価

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | C++, Python, Kubernetes, Docker |
| インフラ | AWS, Azure, Google Cloud, Kafka |
| 分析 | Tableau, Looker（統合パートナー） |
| コミュニケーション | Slack, Zoom |
| セールス | Salesforce, HubSpot |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **創業者の技術的深さ**
   - Microsoft SQL Serverでの5年以上の経験
   - Facebookでの大規模分散システム構築経験
   - ACMプログラミングコンテスト世界メダリストの実力

2. **タイミングの完璧さ**
   - RAM価格低下とマルチコアCPU普及（2010年代）
   - ビッグデータブーム（Hadoop, Spark時代）
   - リアルタイム分析への企業ニーズ急増

3. **ピボット能力**
   - 顧客フィードバックを素早く取り入れ
   - インメモリ専用→ハイブリッドへの技術転換
   - MemSQL→SingleStoreリブランディング

4. **エンタープライズ営業力**
   - Fortune 100企業の50%以上が顧客（銀行、通信、小売）
   - 高額契約（年間$100K-$1M+）の獲得能力
   - カスタマーサクセスによる継続率90%+

### 6.2 タイミング要因

- **ビッグデータブーム（2010-2015年）**: Hadoop, Sparkエコシステムの成長
- **クラウド普及（2015-2020年）**: AWS, Azure, GCPでのマネージドサービス需要
- **AI/MLブーム（2020-2025年）**: リアルタイムデータパイプラインの重要性増加

### 6.3 差別化要因

- **技術的優位性**: インメモリ+ディスクハイブリッド、OLTP+OLAP統合
- **SQL互換性**: 既存アプリケーション移行の容易さ
- **エンタープライズ対応**: セキュリティ、コンプライアンス、24/7サポート

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 金融、通信、小売でリアルタイム分析ニーズ高い |
| 競合状況 | 4 | Oracle, MySQLが強いがレガシー化 |
| ローカライズ容易性 | 3 | エンタープライズ営業が必要、日本語サポート必須 |
| 再現性 | 3 | 高度な分散システム技術が必要 |
| **総合** | 3.75 | ニーズは高いが、技術的ハードルとエンタープライズ営業が課題 |

**日本市場での課題**:
- エンタープライズ営業チームの構築（日本の大企業は意思決定が遅い）
- Oracle, SQL Serverからの移行障壁（レガシーシステム依存）
- 高度な分散システムエンジニアの不足

**日本市場での機会**:
- 金融業界（リアルタイム不正検知、高速取引）
- 通信業界（リアルタイムネットワーク分析）
- EC/小売（リアルタイムレコメンデーション、在庫最適化）
- 製造業（IoTデータのリアルタイム分析）

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

**エンタープライズ顧客への直接アプローチ**:
- Y Combinator前に大手企業（銀行、通信）にヒアリング
- 既存ソリューションのコストと性能問題を定量化
- パイロットプロジェクトで具体的なROIを証明

**学び**:
- B2Bエンタープライズは初期から顧客と密接に協業
- フリーミアムモデルで試用障壁を下げる（128GB以下無料）
- ケーススタディ公開で信頼性を構築（Dell 100x高速化等）

### 8.2 CPF検証（/validate-cpf）

**課題の深さ検証**:
- 既存データベースでリアルタイム分析が「技術的に不可能」
- OLTPとOLAPを別システムで運用するコスト（年間数百万ドル）
- データ量増加（年間50%+）に既存システムが対応不可

**学び**:
- エンタープライズ顧客は「10倍速い」だけでは不十分
- コスト削減（TCO）とシンプル化（運用負荷）が重要
- パイロットで定量的ROIを証明（具体的な秒数、コスト削減額）

### 8.3 PSF検証（/validate-10x）

**10倍優位性の実証**:
- クエリ速度: 100倍高速（MySQL比）
- スケーラビリティ: 50倍（自動分散 vs 手動シャーディング）
- データ統合: 20倍（OLTP+OLAP統合 vs 分離システム）

**学び**:
- 複数軸で10倍を達成（単一軸では不十分）
- 顧客ケーススタディで具体的数値を公開（Dell 100x, Nikkei 13,500x）
- 技術的優位性だけでなく、ビジネスROIを強調

### 8.4 スコアカード（/startup-scorecard）

**CPFスコア**: 9/10
- 問題の深刻度: 10（リアルタイム分析が技術的に不可能）
- 市場規模: 9（グローバルデータベース市場$80B+）
- 緊急性: 8（データ量増加で既存システムが限界）

**PSFスコア**: 9/10
- 10倍優位性: 10（速度100x, スケール50x, 統合20x）
- UVP明確性: 9（OLTP+OLAP統合、リアルタイム分析）
- 技術的実現性: 8（高度な分散システム技術必要）

**総合スコア**: 9/10
- 成功確率: 非常に高（技術力、市場ニーズ、資金調達全て優秀）

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **日本企業向けリアルタイムデータ分析SaaS**
   - SingleStoreをバックエンドに利用
   - 金融、通信、小売向け業界特化型
   - 日本語UI、24/7日本語サポート

2. **レガシーデータベース移行コンサルティング**
   - Oracle, SQL ServerからSingleStore移行支援
   - パイロットプロジェクトでROI証明
   - 継続的最適化サービス

3. **IoT/製造業向けリアルタイム分析プラットフォーム**
   - 工場IoTデータのリアルタイム可視化
   - 予知保全、品質管理
   - SingleStore + Edge Computing統合

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年2011 | ✅ PASS | Y Combinator, Wikipedia |
| Series F $146M | ✅ PASS | TechCrunch, Crunchbase |
| 評価額$1.3B | ✅ PASS | PitchBook, Sacra |
| ARR $123M (2025) | ✅ PASS | Blocks and Files |
| PE買収 (2025年9月) | ✅ PASS | Blocks and Files, The Register |
| Microsoft SQL Server経験 | ✅ PASS | Dataversity, O'Reilly |
| Facebook経験 | ✅ PASS | Crunchbase, HackerNoon |
| ACMメダリスト | ✅ PASS | Speakerpedia, All American Speakers |
| Y Combinator | ✅ PASS | Y Combinator公式 |
| Dell 100x高速化 | ✅ PASS | SingleStore公式, BryteFlow |
| Nikkei 13,500x改善 | ✅ PASS | BryteFlow, SingleStore Case Studies |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [SingleStore | Y Combinator](https://www.ycombinator.com/companies/singlestore)
2. [SingleStore, formerly MemSQL, raises $80M | TechCrunch](https://techcrunch.com/2020/12/08/singlestore-formerly-memsql-raises-80m-to-integrate-and-leverage-companies-disparate-data-silos/)
3. [SingleStore - Wikipedia](https://en.wikipedia.org/wiki/SingleStore)
4. [SingleStore - Crunchbase](https://www.crunchbase.com/organization/memsql)
5. [Nikita Shamgunov - DATAVERSITY](https://www.dataversity.net/contributors/nikita-shamgunov/)
6. [Founder Interviews: Nikita Shamgunov of MemSQL | HackerNoon](https://hackernoon.com/founder-interviews-nikita-shamgunov-of-memsql-8a9ca8d33552)
7. [Building a Modern Database: Nikita Shamgunov on Postgres and Beyond | Madrona](https://www.madrona.com/building-a-modern-database-neon-nikita-shamgunov-serverless-postgres/)
8. [SingleStore sidesteps into private equity ownership | Blocks and Files](https://blocksandfiles.com/2025/09/17/singlestore-sidesteps-into-private-equity-ownership/)
9. [SingleStore revenue, valuation & funding | Sacra](https://sacra.com/c/singlestore/)
10. [SingleStore DB - Real-Time Analytics Made Easy | BryteFlow](https://bryteflow.com/singlestore-db-easy-real-time-analytics/)
11. [SingleStore 2025 Company Profile | PitchBook](https://pitchbook.com/profiles/company/52376-95)
12. [SingleStore launched cloud business after third attempt | The Register](https://www.theregister.com/2024/07/08/singlestore_cloud_business/)
13. [Nikita Shamgunov - Speakerpedia](https://speakerpedia.com/speakers/nikita-shamgunov)
14. [SingleStore at Scale and our Series C | SingleStore Blog](https://www.singlestore.com/blog/memsql-raises-series-c/)
15. [SingleStore Customers | CB Insights](https://www.cbinsights.com/company/memsql/customers)
16. [Made on SingleStore: Customers-Analysts-Partners | SingleStore](https://www.singlestore.com/made-on/)
17. [A blazingly fast database in a data-driven world | IBM](https://www.ibm.com/think/insights/a-blazingly-fast-database-in-a-data-driven-world)
18. [SingleStore - Tracxn](https://tracxn.com/d/companies/singlestore/__byfSPh1-9VebbAhcIzT1TQZV-GnENiNV5XvVZ4hyfuY/funding-and-investors)
