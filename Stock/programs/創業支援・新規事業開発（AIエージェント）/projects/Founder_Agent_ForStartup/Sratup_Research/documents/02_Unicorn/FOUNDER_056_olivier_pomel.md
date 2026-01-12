---
id: "FOUNDER_056"
title: "Olivier Pomel - Datadog"
category: "founder"
tier: "unicorn"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["DevOps", "Observability", "SaaS", "B2B", "クラウド監視", "PLG"]

# 基本情報
founder:
  name: "Olivier Pomel"
  birth_year: 1976
  nationality: "フランス"
  education: "Ecole Centrale Paris (現CentraleSupelec) コンピュータサイエンス修士"
  prior_experience: "IBM Research、複数のインターネットスタートアップ、Wireless Generation VP of Technology、VLC media player共同開発者"

company:
  name: "Datadog"
  founded_year: 2010
  industry: "クラウド監視・オブザーバビリティ"
  current_status: "ipo"
  valuation: "$48B (2025年12月時点の時価総額)"
  employees: 6500

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: null
    wtp_confirmed: true
    urgency_score: 9
    validation_method: "6ヶ月間コードを書かずに顧客ヒアリングに集中"
  psf:
    ten_x_axes:
      - axis: "統合性"
        multiplier: 10
      - axis: "導入スピード"
        multiplier: 5
      - axis: "チーム間可視性"
        multiplier: 10
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 9
    competitive_advantage: "Dev/Ops統合、単一プラットフォーム、700+インテグレーション"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: ""
    original_idea: "DevとOpsチーム間のサイロを解消する監視ツール"
    pivoted_to: ""

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Alexis Le-Quoc (共同創業者)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "SaaStr - The First $100,000,000 ARR at Datadog"
    - "TechCrunch - Datadog and New York"
    - "Internet History Podcast"
    - "Datadog公式サイト"
---

# Olivier Pomel - Datadog

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Olivier Pomel |
| 生年 | 1976年頃（2025年時点で48歳） |
| 国籍 | フランス |
| 学歴 | Ecole Centrale Paris（現CentraleSupelec）コンピュータサイエンス修士 |
| 創業前経験 | VLC media player共同開発者、IBM Research、Wireless Generation VP of Technology |
| 企業名 | Datadog |
| 創業年 | 2010年 |
| 業界 | クラウド監視・オブザーバビリティ |
| 現在の状況 | 上場（NASDAQ: DDOG、2019年IPO） |
| 評価額/時価総額 | 約$48B（2025年12月時点） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- Olivier PomelとAlexis Le-Quocは、Ecole Centrale Parisで学部時代に出会い、その後Wireless Generationで約9年間一緒に働いた
- Pomelは開発チームを率い、Le-Quocは運用チームを率いていた。良い友人関係にもかかわらず、2年後には両チームは対立関係に陥った
- 開発チームは運用チームを批判し、運用チームも開発チームを批判する「指差し合い」が日常化
- この開発と運用の対立（Dev vs Ops）という問題を自ら体験し、解決の必要性を痛感

**需要検証方法**:
- 2010年創業時、最初の6ヶ月間は一切コードを書かなかった
- 「何も売るものがない状態だと、誰もが喜んで話してくれる。素晴らしい企業の素晴らしい人々が何時間も費やして、彼らの問題、何がうまくいっていて何がうまくいっていないかを説明してくれる」
- ニューヨークを拠点とし、シリコンバレーのVCからの資金調達に苦労したことが、逆に顧客に集中せざるを得ない状況を作った

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 6ヶ月間の集中的な顧客ヒアリング（具体的な件数は非公開）
- 手法: 対面インタビュー、潜在顧客との深い対話
- 発見した課題の共通点:
  - 開発者と運用チームが同じシステムを異なる視点で見ている
  - チーム間でデータやインサイトを共有する手段がない
  - クラウド移行に伴い、従来のモニタリングツールでは対応できない

**3U検証**:
- Unworkable（現状では解決不可能）: 従来のモニタリングツールはオンプレミス向けで、クラウドネイティブなインフラには対応不可
- Unavoidable（避けられない）: クラウド移行が加速する中、DevとOpsの協業は必須に
- Urgent（緊急性が高い）: システムダウンは即座に収益損失につながる

**支払い意思（WTP）**:
- 確認方法: ベータ顧客からの早期フィードバック
- 結果: 2012年のGA前から顧客が押し寄せ、Series A調達後すぐに強いトラクションを獲得

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | Datadogソリューション | 倍率 |
|---|------------|-----------------|------|
| 統合性 | ツールがサイロ化、Dev/Ops別々のダッシュボード | 単一プラットフォームで全データを相関分析 | 10x |
| 導入スピード | 数日〜数週間の導入期間 | 1時間以内に価値を実感 | 5x |
| チーム間可視性 | チームごとに異なるビュー | Single Pane of Glass | 10x |
| インテグレーション | 限定的なサードパーティ連携 | 700+（現在は1,000+）インテグレーション | 10x |
| クラウド対応 | オンプレミス中心 | クラウドネイティブ設計 | 10x |

**MVP**:
- タイプ: プロトタイプ（シンプルなエージェントとダッシュボード）
- 初期反応: クローズドアルファで厳選した企業・人材にテスト、その後ワイドベータで急拡大
- CVR: 非公開（ただしフリーミアムモデルで$100K+顧客が収益の80%を占める構造に発展）

**UVP（独自の価値提案）**:
- DevとOpsを統合し、チーム間のサイロを解消する単一プラットフォーム
- メトリクス、トレース、ログをリアルタイムで相関分析
- クラウド移行を加速するインフラ監視

**競合との差別化**:
- Splunk、New Relicがオンプレミス/APM中心だったのに対し、Datadogはインフラ監視から開始しクラウドネイティブに設計
- 統合プラットフォームアプローチにより、ポイントソリューションの組み合わせより優れた体験を提供

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- **資金調達の苦戦**: 西海岸のVCは話を聞いてくれず、東海岸のVCはインフラ領域を十分理解していなかった
- **立地のハンディキャップ**: 「ニューヨークでインフラスタートアップを始めるのは精神的な障害だと思われていた」とVCから言われた
- **市場認知の欠如**: DevOpsという概念がまだ一般的でなかった2010年に創業

### 3.2 ピボット（該当する場合）

- 元のアイデア: DevとOpsのサイロを解消する監視ツール
- ピボット後: 該当なし（当初のビジョンを一貫して追求）
- きっかけ: N/A
- 学び: 「資金不足だったことで効率的なビジネスを構築せざるを得なくなり、顧客との接点を早期から頻繁に持つことができた」

## 4. 成長戦略

### 4.1 初期トラクション獲得

- AWS、Linux、主要データベース、一般的なミドルウェア向けインテグレーションでクラウドネイティブスタートアップから採用開始
- 簡単なインストールとセルフサーブのサインアップで低摩擦の導入を実現
- 2012年のGA時点で10-15人のチーム規模

### 4.2 フライホイール

1. **コンテンツマーケティング + カンファレンス** → インバウンド顧客獲得
2. **プロダクトレッドグロース（PLG）** → フリーミアムから始まり、使い込むほど価値を実感
3. **インテグレーション拡大** → より多くの技術スタックをカバー → より多くの顧客が導入
4. **Land & Expand** → 小規模から導入し、成功に応じて拡大（Net Revenue Retention 115%超）
5. **消費量ベースの課金** → 顧客の成長に応じて収益も成長

### 4.3 スケール戦略

- **製品ラインの拡大**: インフラ監視 → APM → ログ管理 → セキュリティ → 統合オブザーバビリティプラットフォーム
- **エンタープライズ向け強化**: $100K+顧客が収益の80%を占める
- **グローバル展開**: 33カ国にオフィス展開（NY、Boston、Denver、SF、Paris、Dublin、Amsterdam、Sydney、Tokyo、Singapore等）

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | 自社プラットフォーム |
| デザイン | Figma（デザインシステム構築に活用） |
| インフラ | AWS、クラウドネイティブアーキテクチャ |
| マーケティング | コンテンツマーケティング、DASH（自社カンファレンス） |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **自ら体験した課題を解決**: Dev vs Opsの対立を9年間体験し、課題を深く理解
2. **顧客中心のアプローチ**: 6ヶ月間コードを書かずに顧客ヒアリングに集中
3. **適切なタイミング**: DevOpsムーブメントとクラウド移行の波に乗った
4. **統合プラットフォーム戦略**: ポイントソリューションではなく統合ソリューションを構築
5. **PLGモデル**: フリーミアムからエンタープライズまでシームレスな成長パス

### 6.2 タイミング要因

- 2010年創業時、DevOpsとクラウド移行という2つのメガトレンドが同時に発生
- 「正しいプロダクトを正しいタイミングで持っていた。多くは運だった」とPomel自身が認めている
- 2012年のGA時にDevOpsが急速に普及し始め、Datadogが主要な選択肢として認知された

### 6.3 差別化要因

- **Single Pane of Glass**: 開発、運用、セキュリティ、ビジネスチームが同じデータを共有
- **圧倒的なインテグレーション数**: 1,000+インテグレーションで事実上あらゆる技術スタックに対応
- **クラウドネイティブ設計**: レガシーシステムの制約がなく、最新のクラウドインフラに最適化

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本企業のクラウド移行が加速中、DevOps導入ニーズ高い |
| 競合状況 | 4 | Datadog自体が日本進出済み、New Relic等と競争 |
| ローカライズ容易性 | 3 | 技術ツールのため言語障壁は比較的低い |
| 再現性 | 3 | 同様の統合プラットフォームを構築するには大規模投資が必要 |
| **総合** | 4 | DevOps/オブザーバビリティ領域は日本でも成長市場 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **6ヶ月間コードを書かない**: 創業初期に顧客ヒアリングに集中する重要性
- **自らの痛みを起点にする**: 9年間体験した課題だからこそ深い理解があった
- **資金制約を逆手に**: 資金がないからこそ顧客との対話に集中できた

### 8.2 CPF検証（/validate-cpf）

- **「何も売らない」状態での対話**: 製品がないと顧客は本音で課題を話してくれる
- **3U検証の実践**: クラウド移行で既存ツールが使えない（Unworkable）、DevOps協業が必須（Unavoidable）、ダウンタイムは即損失（Urgent）
- **初期顧客の厳選**: クローズドアルファで最高の企業・人材にテスト

### 8.3 PSF検証（/validate-10x）

- **統合性での10x**: サイロ化したツールを統合プラットフォームで置き換え
- **1時間以内の価値実感**: 複雑な製品でも素早く価値を体感できる設計
- **Land & Expand**: 小さく始めて拡大する戦略でCVR向上

### 8.4 スコアカード（/startup-scorecard）

- **市場タイミング**: 10点 - DevOps + クラウド移行の波に完璧に乗った
- **創業者適合**: 10点 - 9年間の経験で課題を熟知
- **顧客検証**: 9点 - 6ヶ月の徹底的なヒアリング
- **競合優位性**: 9点 - 統合プラットフォームと1000+インテグレーション
- **ビジネスモデル**: 9点 - PLG + 消費量ベース課金 + Land & Expand

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **日本企業向けDevOpsコンサルティング + ツール**: 日本企業特有の組織文化（縦割り）を踏まえたDev/Ops統合支援
2. **中小企業向け軽量オブザーバビリティ**: Datadogより安価で導入しやすい監視ツール
3. **特定業界向け統合モニタリング**: 製造業IoT、金融システム等、業界特化型のオブザーバビリティ

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2010年） | ✅ PASS | Datadog公式、Wikipedia、TechCrunch |
| IPO年（2019年） | ✅ PASS | NASDAQ、Bloomberg、複数報道 |
| 時価総額（約$48B） | ✅ PASS | MacroTrends、Stock Analysis（2025年12月時点） |
| 従業員数（6,500人） | ✅ PASS | MacroTrends（2024年12月時点） |
| 6ヶ月間コードを書かなかった | ✅ PASS | SaaStr、複数インタビュー |
| VLC media player共同開発者 | ✅ PASS | Datadog公式、The Org |

**凡例**: ✅ PASS（2ソース以上確認）

## 参照ソース

1. [SaaStr - The First $100,000,000 ARR at Datadog](https://www.saastr.com/the-first-100000000-arr-at-datadog-how-founder-ceo-olivier-pomel-built-a-customer-centric-monitoring-giant/)
2. [TechCrunch - Datadog and New York](https://techcrunch.com/2018/04/21/datadog-and-new-york/)
3. [Internet History Podcast - Olivier Pomel](https://www.internethistorypodcast.com/2025/12/olivier-pomel-datadog-co-founder-and-ceo/)
4. [Datadog Leadership Page](https://www.datadoghq.com/about/leadership/)
5. [Growfers - The Incredible Rise of Datadog](https://growfers.com/story/datadog/)
6. [RTP Global - Building Datadog Against the Odds](https://rtp.vc/building-datadog-against-the-odds/)
7. [MacroTrends - Datadog Market Cap](https://www.macrotrends.net/stocks/charts/DDOG/datadog/market-cap)
8. [MacroTrends - Datadog Employees](https://www.macrotrends.net/stocks/charts/DDOG/datadog/number-of-employees)
9. [Aakash Gupta - Datadog PLG Analysis](https://www.aakashg.com/datadog/)
10. [Square Peg - Datadog's Defensible Advantage](https://www.squarepeg.vc/blog/datadogs-defensible-advantage)
11. [Datadog Wikipedia](https://en.wikipedia.org/wiki/Datadog)
12. [NASDAQ - Datadog IPO](https://www.nasdaq.com/articles/datadog-fetches-$8.7-billion-valuation-pricing-ipo-above-the-range-at-$27-2019-09-18)
