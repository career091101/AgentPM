---
id: "FOUNDER_177"
title: "Bryan Helmig - Zapier"
category: "founder"
tier: "vc_backed"
type: "case_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["zapier", "automation", "integration", "remote_work", "bootstrap", "yc_s12", "saas", "api", "developer_platform"]

# 基本情報
founder:
  name: "Bryan Helmig"
  birth_year: null  # 推定1987年頃（2005年入学より）
  nationality: "アメリカ"
  education: "University of Missouri-Columbia, Finance (2005-2011)"
  prior_experience: "Veterans United Home Loans - Product Dev/Manager"

company:
  name: "Zapier"
  founded_year: 2011
  industry: "SaaS / Integration Platform / Automation"
  current_status: "active"
  valuation: "$5B (2021年二次市場取引)"
  employees: 1000

# VC投資情報
funding:
  total_raised: "$1.4M"
  funding_rounds:
    - round: "seed"
      date: "2012-10-01"
      amount: "$1.3M"
      valuation_post: "不明"
      lead_investors: ["Bessemer Venture Partners"]
      other_investors: ["Y Combinator", "Draper Fisher Jurvetson", "Sequoia Capital (2014追加投資)"]
  top_tier_vcs: ["Y Combinator", "Bessemer Venture Partners", "Sequoia Capital"]

# 成功/失敗/Pivot分類
outcome:
  category: "success"
  subcategory: "growth_success"
  failure_pattern: ""
  pivot_details:
    count: 0
    major_pivots: []
    resources_preserved:
      team: ""
      technology: ""
      investors: ""
    validation_process: []

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 50  # 推定: フォーラム訪問、Skypeコール、初期顧客との対話
    problem_commonality: 60  # 推定: SMBの60%がアプリ統合に課題
    wtp_confirmed: true  # ベータアクセス$100で確認
    urgency_score: 7  # 手動統合作業の時間コストが深刻
    validation_method: "フォーラムリサーチ、有料ベータ、ランディングページテスト"
  psf:
    ten_x_axes:
      - axis: "時間"
        multiplier: 10  # 手動統合数時間 → Zapierで数分
      - axis: "技術障壁"
        multiplier: 15  # コーディング不要、ノーコード
      - axis: "コスト"
        multiplier: 8  # カスタム開発$10K+ → Zapier月額$20-600
    mvp_type: "concierge"  # 初期は手動サポート、Skypeで個別対応
    initial_cvr: 50  # フォーラムリンクからの訪問者の50%が登録
    uvp_clarity: 9  # "Make the internet work for you"
    competitive_advantage: "開発者プラットフォーム、SEO、ネットワーク効果、リモート文化"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: ""
    original_idea: "API Mixer（スタートアップウィークエンドの初期名称）"
    pivoted_to: "Zapier（名称変更のみ、コンセプトは一貫）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["FOUNDER_001", "FOUNDER_178"]  # Wade Foster, Mike Knoop

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-29"
  primary_sources:
    - "Bryan Helmig LinkedIn: https://www.linkedin.com/in/bryanhelmig/"
    - "Changelog Founders Talk #55: Side hustle to $35M ARR at Zapier"
    - "How They Grow: How Zapier Grows - Automating Growth"
    - "Contrary Research: Zapier Business Breakdown & Founding Story"
    - "IT Visionaries Podcast: Interview with Bryan Helmig"
    - "Developer Tea Podcast: Interview with Bryan Helmig (Part 1 & 2)"
    - "TechZing #319: Bryan Helmig - Zapier: The First 10 Customers"
    - "Zapier Blog: The Anatomy of a Sale - Andrew Warner"
    - "Y Combinator: Building APIs for AI with Bryan Helmig"
    - "Zapier Engineering Blog: The CTO Journey at a Small Startup"
    - "YouTeam: Managing a Fully Remote Dev Team Interview"
    - "Sacra: Zapier revenue, valuation & funding"
    - "HowTheyGrow.co: Zapier Growth Strategy Analysis"
    - "Wikipedia: Zapier"
    - "Crunchbase: Bryan Helmig Profile"
---

# Bryan Helmig - Zapier

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Bryan Helmig |
| 生年 | 推定1987年頃（2005年大学入学より逆算） |
| 国籍 | アメリカ（ミズーリ州セントルイス近郊出身） |
| 学歴 | University of Missouri-Columbia, Finance専攻 (2005-2011) |
| 創業前経験 | Veterans United Home Loans - Product Dev/Manager |
| 企業名 | Zapier |
| 創業年 | 2011年10月（Startup Weekend） |
| 業界 | SaaS / Integration Platform / Automation |
| 現在の状況 | 稼働中（CTO兼共同創業者） |
| 評価額/時価総額 | $5B（2021年二次市場取引、Sequoia/Steadfast） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- Bryan HelmigはVeterans United Home LoansでProduct Dev/Managerとして勤務中、フリーランスの副業でウェブプロジェクトを手がけていた
- 共同創業者のWade Fosterも同様に副業でクライアントワークを行う中、「異なるアプリを連携させたい」という要望が繰り返し発生することに気づいた
- 2011年5月、Wade FosterがVeterans United Home Loansでメールマーケティングマネージャーとして100万通以上のメールとローンステータスを同期する際、手動での統合作業に8ヶ月を費やし、深刻な課題を実感
- Hacker Newsで知り合ったBryan Helmigと、共通の友人Mike Knoopとともに「アプリ同士を会話させる」というアイデアに着手

**需要検証方法**:
- 2011年9月30日-10月2日、ミズーリ州コロンビアのStartup Weekendでプロトタイプを2日間で構築
- 当時の名称は「API Mixer」で、ハッカソンで優勝し$2,000と初期検証を獲得
- Wade FosterはEvernote、Salesforce、Dropboxなどの人気SaaSのヘルプフォーラムを訪問し、ユーザーが「どのような統合機能を求めているか」を手動でリサーチ
- 各リクエストに対し、技術的な選択肢（API利用）を提示しつつZapierのデモリンクを紹介する戦略を展開
- この手法により、フォーラムからの訪問者の約50%がコンバージョン（メールアドレス登録）し、真剣な需要を確認

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 推定50件以上（フォーラムでの対話、Skype通話、初期ベータユーザーとの1on1）
- 手法:
  - Wade Fosterがフォーラムで具体的な統合ニーズを聞き取り
  - 初期ベータユーザーに対してSkype通話を「できるだけ多く」予約し、欲しい統合機能をヒアリング
  - 各顧客のワークフローを手動でサポートし、フィードバックを収集
- 発見した課題の共通点:
  - SMBは複数のSaaSツールを利用しているが、データ同期が手動かつ非効率
  - APIを使ったカスタム統合は技術者が必要で、中小企業には費用対効果が悪い（$10K+の開発費）
  - 統合作業に週あたり数時間から数十時間を浪費している

**3U検証**:
- Unworkable（現状では解決不可能）:
  - 非技術者がAPI統合を自力で構築するのは不可能
  - カスタム開発は中小企業の予算を超える
  - 各SaaSベンダーがネイティブ統合を提供するとは限らない
- Unavoidable（避けられない）:
  - SaaSツールの普及により、複数アプリの利用は避けられないトレンド
  - データサイロ化は業務効率を阻害し、手動同期は必然的に発生
  - 競合他社もSaaSスタックを活用するため、統合は競争上の必須要件
- Urgent（緊急性が高い）:
  - 手動作業による時間コストが毎日発生
  - ヒューマンエラーによるデータ不整合がビジネスリスク
  - 市場の変化が速く、業務の自動化遅れは機会損失に直結

**支払い意思（WTP）**:
- 確認方法:
  - ベータアクセスに$1、$5、$100の異なる価格帯を設定し、顧客の本気度を測定
  - 2011年11月、起業家Andrew Warner（Mixergyホスト）が$100でベータアクセスを購入し、初の有料顧客となる
  - 一週間後には12人以上が有料でベータに参加
- 結果:
  - WTP確認済み（true）
  - 「クレジットカードを入力するのは、本当に役立つと思った時だけ」（Bryan Helmig）という原則を実証
  - 有料ベータにより「タイヤキッカー」を排除し、真剣な顧客からの質の高いフィードバックを獲得
  - ベータ期間中の価格は最終的に$5-10に落ち着き、ローンチ時には月額課金モデルへ移行

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 |
|---|------------|-----------------|------|
| 時間 | カスタムAPI統合開発に数週間〜数ヶ月 | Zapierで数分〜数時間で設定 | 10x |
| コスト | 開発者雇用で$10K-50K+ | 月額$20-600（フリーミアム） | 8x |
| 使いやすさ | コーディングスキル必須、技術者依存 | ノーコードUI、誰でも設定可能 | 15x |
| 成果 | 限定的な統合（1対1） | 6,500+アプリの組み合わせ（N対N） | 20x |
| 導入障壁 | 開発環境、API知識、保守運用が必要 | ブラウザのみ、即座に利用開始 | 12x |

**MVP**:
- タイプ: Concierge MVP（初期は手動サポート）
- 初期反応:
  - Startup Weekendで2日間のプロトタイプが優勝し、コンセプトを検証
  - ローンチ前にフォーラム経由で10,000件のメールアドレスを収集
  - 2011年12月時点で25の統合機能、10K人のウェイトリストを達成
  - Andrew Warnerが初回購入後、Twitterで公開推薦し、大きなトラフィックを獲得
- CVR:
  - フォーラムリンクからの訪問者の約50%がコンバージョン（Wade Foster証言）
  - 有料ベータ登録により、真剣度の高いユーザーを効率的に獲得

**UVP（独自の価値提案）**:
- "Make the internet work for you" - インターネットをあなたのために働かせる
- ノーコードで誰でも使える自動化プラットフォーム
- 6,500+のアプリ統合により、あらゆる業務フローを自動化
- 技術者不要で、プロシューマーが自らワークフローを構築できる
- リモートファーストの企業文化により、グローバルに分散したチームを実現

**競合との差別化**:
- **IFTTT vs Zapier**: IFTTTが個人向けスマートホーム自動化に特化する一方、Zapierはビジネス向けSaaS統合に注力
- **開発者プラットフォーム**: 2012年8月、サードパーティ開発者が統合を構築できるプラットフォームを公開し、ネットワーク効果を創出
- **SEO戦略**: アプリ間統合ページ（例: "Salesforce to Trello"）を自動生成し、オーガニック検索で月間850万訪問者を獲得
- **リモートワーク文化**: 2011年から完全リモート、17タイムゾーン・42カ国に従業員を配置し、オフィスコストを削減
- **資本効率**: $1.4Mの資金調達で$250M ARRを達成（ARR対資金調達比率178倍）

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- **YC初回申請で不合格**: 2011年のStartup Weekend直後にY Combinatorに申請したが、「不完全なプロダクト、顧客ゼロ、実績なし」で却下
- **学びと対応**: 6ヶ月間顧客獲得に注力し、1,000人以上の有料ユーザーを獲得した上で再申請
- **結果**: 2012年夏、YC S12バッチに合格し、3人全員がフルタイムでZapierにコミット

### 3.2 ピボット（該当する場合）

- 元のアイデア: 「API Mixer」という名称でスタート
- ピボット後: 「Zapier」にブランド名を変更
- きっかけ: ブランディングとマーケティング戦略の一環
- 学び: コアコンセプト（アプリ統合自動化）は一貫しており、実質的なピボットは発生せず。名称変更のみ。

## 4. 成長戦略

### 4.1 初期トラクション獲得

- **フォーラムマーケティング**: Wade Fosterが人気SaaSのヘルプフォーラムで統合リクエストを探し、Zapierのリンクを提供（50%CVR）
- **有料ベータ戦略**: $1-100の価格帯でベータアクセスを販売し、真剣な顧客を選別
- **ローンチ前ウェイトリスト**: フォーラム経由で10,000件のメールアドレスを収集
- **初期顧客との密接な関係**: Skype通話で個別サポート、顧客ごとにカスタム統合を手動構築
- **Andrew Warnerの推薦**: 初の有料顧客がTwitterで公開推薦し、大きな露出を獲得

### 4.2 フライホイール

```
[開発者がアプリ統合を構築]
  ↓
[統合数が増加し、ユーザー価値が向上]
  ↓
[ユーザー数増加により、開発者にとっての魅力が向上]
  ↓
[パートナーがZapierページにリンクし、SEO強化]
  ↓
[オーガニック検索からの新規ユーザー獲得]
  ↓
[さらに多くの開発者が統合を構築]
  ↓
（繰り返し）
```

- **クロスサイドネットワーク効果**: 開発者とユーザーの相互強化ループ
- **SEOフライホイール**: 統合ページが自動生成され、検索トラフィックが増加
- **コマーケティング**: パートナー企業がZapier統合を自社サイトで宣伝し、双方に利益

### 4.3 スケール戦略

- **開発者プラットフォーム（2012年8月）**: サードパーティが統合を構築できるプラットフォームを公開し、35の基本統合から6,500+へ拡大
- **プログラマティックSEO**: アプリ間統合ページを自動生成し、月間850万訪問者（50%がオーガニック）
- **フリーミアムモデル**: 無料プランで300万ユーザーを獲得し、10万件の有料顧客に転換
- **リモートファーストの拡大**: オフィス不要で世界中から優秀な人材を採用、コスト効率を最大化
- **PLG + セールス**: 2020年頃から、大企業向けにセールスチームを導入し、エンタープライズ市場にも対応
- **AI統合（2023年〜）**: ChatGPTプラグイン、Zapier AIによる自然言語での自動化構築を導入

### 4.4 バリューチェーン

```
[統合パートナー（アプリベンダー）]
  ↓
[Zapier開発者プラットフォーム]
  ↓
[Zapierプラットフォーム（6,500+統合）]
  ↓
[フリーミアムユーザー（300万）]
  ↓
[有料顧客（10万）]
  ↓
[コンテンツマーケティング・SEO]
  ↓
[新規パートナー獲得]
  ↓
（繰り返し）
```

## 4.5 資金調達履歴（VC案件のみ）

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| YC Batch | 2012-05 | $15K-20K | 不明 | Y Combinator | - |
| Seed | 2012-10 | $1.3M | 不明 | Bessemer Venture Partners | DFJ, Angels |
| Additional | 2014-11 | 不明 | 不明 | Sequoia Capital | - |
| 二次市場 | 2021-01 | 不明 | $5B | Sequoia, Steadfast | - |

**総資金調達額**: $1.4M（シードまで）
**主要VCパートナー**:
- Y Combinator (2012)
- Bessemer Venture Partners (2012)
- Sequoia Capital (2014, 2021)
- Draper Fisher Jurvetson (2012)

### 資金使途と成長への影響

**Seed（$1.3M、2012年10月）**:
- プロダクト開発: 開発者プラットフォームの構築、統合数の拡大
- 初期採用: カスタマーサポート担当1名、エンジニア2名を段階的に採用
- マーケティング: コンテンツマーケティング、SEO強化（大規模な広告費は投入せず）
- 成長結果: 2013年末〜2014年初頭に黒字化達成、以降は外部資金調達なし

**ARR成長（自己資本で達成）**:
- 2014年: 黒字化
- 2015年: 600K顧客獲得
- 2021年: $140M ARR
- 2023年: $250M ARR
- 2024年: $310M ARR
- 2025年予測: $400M ARR

### VC関係の構築

1. **YC/VC選考突破**:
   - 初回申請では不合格（プロダクト未完成、顧客ゼロ）
   - 6ヶ月で1,000人以上の有料ユーザーを獲得し、再申請で合格
   - YC期間中に開発者プラットフォームをローンチし、スケーラビリティを実証

2. **投資家との関係維持**:
   - 2012年のシード調達後、追加のシリーズA/B/Cを実施せず
   - 2014年にSequoia Capitalが追加投資（詳細非公開）
   - 2021年、Sequoia/Steadfastが二次市場で株式購入（$5B評価）
   - 創業者は80%以上の株式を保持し、コントロールを維持

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | Python, Django, PostgreSQL, Redis, AWS |
| マーケティング | SEO（プログラマティック生成）, コンテンツマーケティング, フォーラム |
| 分析 | Google Analytics, Mixpanel（推定） |
| コミュニケーション | Slack, Zoom, Donut（ランダムペアリング） |
| プロジェクト管理 | GitHub, Linear（推定） |
| カスタマーサポート | Help Scout, Intercom（推定） |
| リモートワーク | Zapier（自社製品）, Slack, Zoom, Notion（推定） |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **資本効率の極大化**: $1.4Mで$250M ARRを達成（ARR/資金調達比率178倍）
2. **開発者プラットフォームによるネットワーク効果**: サードパーティが統合を構築し、統合数が指数関数的に増加
3. **プログラマティックSEO**: 統合ページの自動生成により、オーガニック検索で月間850万訪問者を獲得
4. **リモートファースト文化**: オフィス不要で世界中から優秀な人材を採用、固定費を削減
5. **顧客中心主義**: 初期顧客に対するConcierge MVPアプローチで、プロダクトフィットを精密に検証
6. **フリーミアムモデル**: 無料プランで市場を拡大し、有料転換で収益化

### 6.2 タイミング要因

- **SaaS普及期（2011年）**: Salesforce, Dropbox, Evernote等のSaaSが普及し、統合ニーズが急増
- **API経済の台頭**: 多くのSaaSがAPIを公開し始め、サードパーティ統合が技術的に可能に
- **ノーコード運動の先駆け**: 非技術者でもツールを構築できるノーコード/ローコードトレンドの初期段階
- **リモートワークの普及前**: 2011年時点で完全リモートは珍しく、競合優位性として機能
- **YC S12バッチ**: Airbnb, Dropbox等のYC卒業生がスケールし、YCブランドが強化されていた時期

### 6.3 差別化要因

- **技術障壁の除去**: ノーコードUIにより、非技術者でもAPI統合を構築可能
- **統合数の圧倒的優位**: 6,500+のアプリ統合（競合IFTTTは900+）
- **ビジネスフォーカス**: IFTTTが個人向けに対し、Zapierはビジネス/SMB向けに特化
- **コミュニティドリブン**: 開発者プラットフォームでコミュニティが自ら価値を創出
- **カスタマーサポート**: 全従業員がサポート対応をローテーションし、「最も顧客に寄り添う」企業文化を構築

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 4 | 日本企業もSaaS利用が増加し、統合ニーズは高い。ただし、オンプレミス文化が残る企業も多い |
| 競合状況 | 3 | 国内にはiPaaS競合が少ないが、大手ITベンダー（NTTデータ等）が同領域に参入 |
| ローカライズ容易性 | 3 | 日本語UIは必須。国内SaaS（freee, SmartHR等）との統合が課題 |
| 再現性 | 4 | 開発者プラットフォーム戦略は再現可能。SEO戦略も有効。リモート文化は日本でも浸透中 |
| **総合** | 3.5 | 高い市場ニーズと再現性がある一方、ローカライズと競合対策が鍵 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **フォーラムリサーチの応用**: Stack Overflow、Qiita、Redditなどのコミュニティで「困っていること」を直接観察
- **既存ツールのヘルプページ分析**: 既存SaaSのFAQやフォーラムで、ユーザーが「足りない機能」を探す
- **有料ウェイトリストで本気度測定**: ベータアクセスに少額課金し、タイヤキッカーを排除

### 8.2 CPF検証（/validate-cpf）

- **3U検証の徹底**: Zapierは「非技術者がAPI統合できない」という Unworkable な課題を解決
- **WTP確認**: ベータアクセス$100で支払い意思を確認し、課題の深刻度を検証
- **Concierge MVPの活用**: 初期は手動サポートで顧客ニーズを深く理解し、プロダクトに反映

### 8.3 PSF検証（/validate-10x）

- **10倍軸の特定**: Zapierは「時間」「コスト」「技術障壁」で10倍以上の優位性を実現
- **ネットワーク効果の設計**: 開発者プラットフォームで、ユーザーが増えるほど価値が向上する仕組みを構築
- **フリーミアムでの初期CVR測定**: 無料プランで市場を拡大し、有料転換率を継続的に改善

### 8.4 スコアカード（/startup-scorecard）

- **CPFスコア**: 9/10（深刻な課題、高いWTP、広範な市場）
- **PSFスコア**: 10/10（10倍優位性、明確なUVP、強力な差別化）
- **成長可能性**: 10/10（ネットワーク効果、プログラマティックSEO、資本効率）
- **実行力**: 9/10（リモート文化、迅速な顧客対応、継続的な改善）

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **日本版Zapier for 中小企業**:
   - freee、SmartHR、kintone等の国内SaaSを統合するノーコードプラットフォーム
   - ターゲット: 日本の中小企業（特に製造業、地方企業）
   - 差別化: 日本語サポート、オンプレミス連携オプション

2. **自治体向け業務自動化プラットフォーム**:
   - 自治体の複雑な業務フロー（住民票、申請書等）をノーコードで自動化
   - ターゲット: 地方自治体、公共団体
   - 差別化: 法令遵守、セキュリティ対応、マイナンバー連携

3. **EC統合プラットフォーム**:
   - 楽天、Amazon、Yahoo!ショッピング等の複数ECモールを一元管理
   - ターゲット: 中小EC事業者
   - 差別化: 在庫連携、受注管理、配送追跡の自動化

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2011年10月） | ✅ PASS | Wikipedia, Contrary Research, Changelog Podcast |
| 評価額（$5B, 2021年） | ✅ PASS | Sacra, PitchBook, Crunchbase |
| 資金調達額（$1.4M） | ✅ PASS | HowTheyGrow, Contrary Research, Sacra |
| ARR $310M（2024年） | ✅ PASS | Sacra, SQ Magazine, Latka |
| 統合数（6,500+） | ✅ PASS | Zapier公式サイト, Contrary Research |
| YC S12バッチ | ✅ PASS | Y Combinator公式サイト |
| 初期顧客Andrew Warner | ✅ PASS | Zapier公式ブログ, Changelog Podcast |
| フォーラムCVR 50% | ✅ PASS | HowTheyGrow, Contrary Research |
| リモート従業員1,000人 | ✅ PASS | Zapier採用ページ, Arc.dev |
| Bryan HelmigのCTO就任 | ✅ PASS | LinkedIn, Crunchbase, IT Visionaries Podcast |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. Bryan Helmig LinkedIn: https://www.linkedin.com/in/bryanhelmig/
2. Changelog Founders Talk #55: Side hustle to $35M ARR at Zapier with Bryan Helmig
3. HowTheyGrow: How Zapier Grows - Automating Growth (Jaryd Hermann)
4. Contrary Research: Zapier Business Breakdown & Founding Story
5. IT Visionaries Podcast: There's a Zap For That - Interview with Bryan Helmig
6. Developer Tea Podcast: Interview with Bryan Helmig (Part 1 & 2, March 2019)
7. TechZing #319: Bryan Helmig - Zapier: The First 10 Customers
8. Zapier Blog: The Anatomy of a Sale - How Andrew Warner Became Our First Paying Customer
9. Y Combinator: Building APIs for AI with Bryan Helmig
10. Zapier Engineering Blog: The CTO Journey at a Small Startup
11. YouTeam: Managing a Fully Remote Dev Team - Interview with Bryan Helmig
12. Sacra: Zapier revenue, valuation & funding
13. Wikipedia: Zapier
14. Crunchbase: Bryan Helmig Profile
15. SQ Magazine: Zapier Statistics 2025
