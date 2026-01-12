---
id: "FOUNDER_084"
title: "Frank Slootman - Snowflake / ServiceNow / Data Domain"
category: "founder"
tier: "unicorn"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["growth-ceo", "enterprise-saas", "data-cloud", "three-ipo", "turnaround", "performance-culture"]

# 基本情報
founder:
  name: "Frank Slootman"
  birth_year: 1958
  nationality: "オランダ（米国在住）"
  education: "Erasmus University Rotterdam 経済学学士・経営学博士"
  prior_experience: "Compuware GM、Borland Software SVP"

company:
  name: "Snowflake Inc."
  founded_year: 2012
  industry: "クラウドデータプラットフォーム / エンタープライズSaaS"
  current_status: "ipo"
  valuation: "$77B（時価総額、2024年12月時点）"
  employees: 7004

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: null
    wtp_confirmed: true
    urgency_score: 9
    validation_method: "エンタープライズ顧客との直接対話、既存ペインポイント分析"
  psf:
    ten_x_axes:
      - axis: "スケーラビリティ"
        multiplier: 10
      - axis: "データ共有の容易さ"
        multiplier: 10
      - axis: "運用管理の自動化"
        multiplier: 5
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 9
    competitive_advantage: "ストレージ・コンピュート分離アーキテクチャ、マルチクラウド対応"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: ""
    original_idea: ""
    pivoted_to: ""

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Benoit Dageville", "Thierry Cruanes", "Marcin Zukowski", "Fred Luddy"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia - Frank Slootman"
    - "Sequoia Capital - Frank Slootman Is No Snowflake"
    - "SEC S-1 Filing - Snowflake"
    - "MacroTrends - Snowflake Financial Data"
---

# Frank Slootman - Snowflake / ServiceNow / Data Domain

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者/経営者 | Frank Slootman（グロースCEO） |
| 生年 | 1958年 |
| 国籍 | オランダ（米国在住） |
| 学歴 | Erasmus University Rotterdam 経済学学士・経営学博士 |
| 創業前経験 | Compuware GM（7年）、Borland Software SVP |
| 企業名 | Snowflake Inc.（2019-2024 CEO）、ServiceNow（2011-2017 CEO）、Data Domain（2003-2009 CEO） |
| Snowflake創業年 | 2012年（創業者：Dageville、Cruanes、Zukowski） |
| 業界 | クラウドデータプラットフォーム |
| 現在の状況 | 上場（2020年9月16日 NYSE: SNOW） |
| 時価総額 | 約$77B（2024年12月時点） |

**注記**: Frank Slootmanは創業者ではなく「グロースCEO」として知られる。本人も「自分を真のアントレプレナーとは考えていない。会社を創業したことは一度もない」と述べている。しかし、Data Domain、ServiceNow、Snowflakeの3社をIPOに導き、いずれも大成功を収めた稀有な経営者である。

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- Snowflakeの創業者（Dageville、Cruanes）はOracle出身のデータアーキテクトで、従来のオンプレミス・クラウドデータプラットフォームの限界を直接体験
- 既存ソリューションのスケーラビリティ問題、複雑な管理、増大するデータ量への対応不足を認識
- 2012年当時、これらの要素をクラウドに移行するというアイデアは非常にラディカルだった

**需要検証方法**:
- エンタープライズ顧客が抱えるデータウェアハウスの課題を技術的観点から分析
- ほぼすべての組織がいずれクラウド戦略を採用するという確信

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 具体的な数値は非公開
- 手法: エンタープライズ顧客との直接対話、技術的課題の深掘り
- 発見した課題の共通点:
  - 既存データウェアハウスのスケーラビリティ限界
  - ストレージとコンピュートの分離ができない非効率性
  - 複雑な管理運用の負担
  - 半構造化データ対応の困難さ

**3U検証**:
- Unworkable（現状では解決不可能）: 従来のアーキテクチャではクラウドネイティブな柔軟性を実現できない
- Unavoidable（避けられない）: データ量の爆発的増加により、すべての企業がこの課題に直面
- Urgent（緊急性が高い）: デジタルトランスフォーメーションの加速により即座の対応が必要

**支払い意思（WTP）**:
- 確認方法: エンタープライズ顧客との契約、消費ベースの価格モデルへの反応
- 結果: ネットリテンション率158%（2020年7月時点）が強いWTPを証明

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策（AWS Redshift等） | Snowflakeソリューション | 倍率 |
|---|------------|-----------------|------|
| スケーラビリティ | 固定クラスターサイズ | 無制限のスケールアップ/ダウン | 10x |
| データ共有 | 複雑なETL・データコピー必要 | ゼロコピーデータ共有 | 10x |
| 運用管理 | 手動でのバキューム・圧縮必要 | 完全自動化 | 5x |
| マルチクラウド | 単一クラウドにロック | AWS/Azure/GCP対応 | 3x |
| 半構造化データ | 追加拡張が必要 | ネイティブサポート | 5x |

**MVP**:
- タイプ: プロトタイプ（クラウドネイティブデータウェアハウス）
- 初期反応: エンタープライズ顧客から強い関心
- CVR: 顧客数が2019年7月の1,547社から2020年7月の3,117社へ100%以上成長

**UVP（独自の価値提案）**:
- ストレージとコンピュートを分離したクラウドネイティブアーキテクチャ
- 消費ベースの価格モデルによるコスト最適化
- シームレスなデータ共有機能

**競合との差別化**:
- AWS Redshiftと比較して、マルチクラウド対応とデータ共有の容易さで優位
- 自動化により運用負担を大幅削減
- 市場シェア19.96%で業界トップ（Redshiftは14.87%）

## 3. ピボット/失敗経験

### 3.1 初期の失敗・課題

**Data Domain時代（2003-2009）**:
- 参画時は顧客ゼロ、収益ゼロ、キャッシュバーン状態
- 倒産を避けるための資金調達が必要な状況
- 典型的な「キャズム超え」の課題に直面

**ServiceNow時代（2011-2017）**:
- 参画時、会社は「90日で倒産」の危機
- 売上は約1億ドルに達していたが、インフラが自社の成功に潰されかけていた
- Slootmanは「毎朝メールをチェックするのが怖かった」と回想
- クラウドインフラの刷新が緊急課題

### 3.2 ピボット（該当する場合）

- 元のアイデア: 該当なし（Snowflakeは創業時のビジョンを維持）
- ServiceNowでの戦略変更: ヘルプデスク管理からIT部門全体のワークフローシステムへ拡張
- きっかけ: より大きなTAM（Total Addressable Market）の発見
- 学び: 製品を深化させることで既存顧客からの収益を拡大

## 4. 成長戦略

### 4.1 初期トラクション獲得

**Slootmanの共通アプローチ（3社共通）**:
- 「ドライバー」を採用し「パッセンジャー」を排除
- 経験よりも適性（ハングリーさ、好奇心、キャリアへのフラストレーション）を重視
- 極端な集中力（machine focus）の徹底

**Snowflake具体策**:
- エンタープライズ顧客への集中
- 消費ベース価格モデルによる参入障壁の低減
- 2019年6月のSnowflake Data Exchange立ち上げによるネットワーク効果創出

### 4.2 フライホイール

```
顧客獲得 → データ蓄積 → データ共有機能活用 → ネットワーク効果 → 更なる顧客獲得
    ↓
消費量増加 → 収益拡大 → 製品投資 → 機能強化
```

- ネットリテンション率158%が示す強力なエクスパンション
- $100万以上の顧客が22社から56社へ増加（2019-2020年）

### 4.3 スケール戦略

**Frank Slootmanの「Amp It Up」フレームワーク**:

1. **期待値を上げる（Raise Expectations）**: 平凡さに宣戦布告、現状維持を打破
2. **緊急性を高める（Increase Urgency）**: リーダーがペースを設定。「1週間後ではなく明日か明後日」
3. **強度を高める（Elevate Intensity）**: ハードプッシュしながらフォーカスとエネルギーを維持

**具体的成果**:
- Data Domain: 収益$800K（2004年）→ $275M（2008年）、EMCに$2.4Bで売却
- ServiceNow: 収益$93M（2011年）→ $1.4B（2016年）、14倍成長
- Snowflake: 史上最大のソフトウェアIPO、$3.36B調達、初日株価112%上昇

## 5. 使用ツール・サービス

| カテゴリ | ツール/アプローチ |
|---------|-------|
| 技術基盤 | クラウドネイティブアーキテクチャ（AWS/Azure/GCP） |
| 価格戦略 | 消費ベースモデル（Usage-based pricing） |
| GTM戦略 | エンタープライズ直販 + パートナーエコシステム |
| 文化形成 | 「Amp It Up」パフォーマンスカルチャー |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **優れた実行力**: 戦略よりも実行が重要。優れた実行は優れた戦略より稀
2. **パフォーマンスカルチャー**: 高速度、高基準、狭いフォーカスを徹底
3. **適切なタイミングでの参画**: 製品市場適合後、スケール前のフェーズで参画
4. **エンタープライズフォーカス**: 大企業顧客への集中による高単価実現

### 6.2 タイミング要因

- クラウドコンピューティングの成熟（2012-2019年）
- デジタルトランスフォーメーションの加速
- データ量の爆発的増加
- リモートワーク普及によるクラウドニーズ拡大（2020年）

### 6.3 差別化要因

- 3社IPOという実績に基づく信頼性
- Warren BuffettのBerkshire Hathawayが$250M投資（テック企業への稀有な投資）
- Salesforceも$250M投資

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本企業のDXニーズは高い |
| 競合状況 | 3 | AWS、Azure、GCPが強い |
| ローカライズ容易性 | 3 | エンタープライズ向けは日本語対応必須 |
| 再現性 | 2 | Slootman型CEOの発掘は困難 |
| **総合** | 3 | ビジネスモデルは適用可能だが人材面で課題 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- 技術的課題を深く理解した専門家による課題発見が有効
- 既存ソリューションの限界を具体的に特定
- 「すべての組織がいずれ直面する課題」を見極める

### 8.2 CPF検証（/validate-cpf）

- エンタープライズ顧客との直接対話を重視
- 3U（Unworkable, Unavoidable, Urgent）の検証
- 技術的課題と業務課題の両面から検証

### 8.3 PSF検証（/validate-10x）

- 複数軸での10倍優位性の実現（Snowflakeはスケーラビリティとデータ共有で10x）
- 消費ベース価格モデルによるWTPの明確化
- ネットリテンション率による継続的なPSF検証

### 8.4 スコアカード（/startup-scorecard）

- 実行力を重視したスコアリング
- パフォーマンスカルチャーの評価
- リーダーシップの質の評価

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **日本企業向けデータ統合プラットフォーム**: 日本特有の業務システム（SAP/Oracle EBS以外の基幹系）からのデータ統合
2. **消費ベースSaaSモデルの普及**: 従来の席数課金から消費ベースへの移行支援
3. **エンタープライズ向けグロースCEOマッチング**: スケール段階の企業とグロースCEO人材のマッチング

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 生年（1958年） | ✅ PASS | Wikipedia、複数メディア |
| Snowflake IPO規模（$3.36B） | ✅ PASS | CNN Business、Fortune |
| ServiceNow収益成長（14倍） | ✅ PASS | Sequoia Capital、Wikipedia |
| Data Domain売却額（$2.4B） | ✅ PASS | Wikipedia、Sequoia Capital |
| Snowflake時価総額（$77B） | ✅ PASS | MacroTrends、Stock Analysis |
| 従業員数（7,004人/2024年） | ✅ PASS | MacroTrends、SEC Filing |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Wikipedia - Frank Slootman](https://en.wikipedia.org/wiki/Frank_Slootman)
2. [Sequoia Capital - Frank Slootman Is No Snowflake](https://sequoiacap.com/article/frank-slootman-spotlight/)
3. [CNN Business - Snowflake shares more than double](https://edition.cnn.com/2020/09/16/investing/snowflake-ipo)
4. [Fortune - Meet Snowflake, one of the buzziest tech IPOs ever](https://fortune.com/2020/09/15/snowflake-ipo-database-oracle-frank-slootman/)
5. [MacroTrends - Snowflake Market Cap](https://www.macrotrends.net/stocks/charts/SNOW/snowflake/market-cap)
6. [SEC S-1 Filing - Snowflake](https://www.sec.gov/Archives/edgar/data/1640147/000162828020013010/snowflakes-1.htm)
7. [Quartr - Frank Slootman Beyond Snowflake](https://quartr.com/insights/business-philosophy/frank-slootman-beyond-snowflake-one-of-the-most-respected-ceos)
8. [Sequoia Capital - The ServiceNow Story Podcast](https://sequoiacap.com/podcast/crucible-moments-servicenow/)
9. [CNBC - Snowflake valued at $12.4 billion](https://www.cnbc.com/2020/02/07/snowflake-valued-at-12point4-billion-as-salesforce-ventures-invests.html)
10. [Bigeye - A brief history of Snowflake](https://www.bigeye.com/blog/a-brief-history-of-snowflake)
11. [BMC - Snowflake vs Redshift](https://www.bmc.com/blogs/aws-redshift-vs-snowflake/)
12. [Admired Leadership - Amp It Up Book Summary](https://admiredleadership.com/book-summaries/amp-it-up/)
