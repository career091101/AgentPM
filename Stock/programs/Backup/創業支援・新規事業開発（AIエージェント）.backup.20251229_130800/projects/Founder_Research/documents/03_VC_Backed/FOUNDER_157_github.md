---
id: "FOUNDER_157"
title: "Tom Preston-Werner & Chris Wanstrath - GitHub"
category: "founder"
tier: "vc_backed"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["developer-tools", "open-source", "collaboration", "Microsoft買収", "a16z", "$7.5B-exit"]

# 基本情報
founder:
  name: "Tom Preston-Werner & Chris Wanstrath"
  birth_year: 1979 # Preston-Werner推定
  nationality: "アメリカ"
  education: "Harvey Mudd College中退(Preston-Werner) / University of Cincinnati中退(Wanstrath)"
  prior_experience: "Gravatar創業者(Preston-Werner) / CNET Networks・GameSpot(Wanstrath)"

company:
  name: "GitHub"
  founded_year: 2008
  industry: "開発者ツール / コード管理 / オープンソース"
  current_status: "acquired"
  valuation: "$7.5B（Microsoft買収時、2018年）"
  employees: 600+ # 買収時

# VC投資情報
funding:
  total_raised: "$350M"
  funding_rounds:
    - round: "series_a"
      date: "2012-07-09"
      amount: "$100M"
      valuation_post: "不明"
      lead_investors: ["Andreessen Horowitz"]
      other_investors: []
  top_tier_vcs: ["Andreessen Horowitz"]

# 成功/失敗/Pivot分類
outcome:
  category: "success"
  subcategory: "exit_success"
  exit_details:
    acquirer: "Microsoft"
    acquisition_amount: "$7.5B"
    acquisition_date: "2018-10-26"
    employees_at_exit: 600+
    a16z_return: "$1B+"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 95 # Ruby on Railsコミュニティで共通の課題
    wtp_confirmed: true
    urgency_score: 8
    validation_method: "Ruby on Rails meetupでの対話、開発者コミュニティでの反応"
  psf:
    ten_x_axes:
      - axis: "導入障壁"
        multiplier: 10
      - axis: "コラボレーション速度"
        multiplier: 10
      - axis: "ソーシャル機能"
        multiplier: 100
      - axis: "UX"
        multiplier: 5
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 10
    competitive_advantage: "Git + ソーシャル + 美しいUX"
  pivot:
    occurred: false
    pivot_count: 0

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-28"
  primary_sources:
    - "TechCrunch"
    - "a16z公式"
    - "Fortune"
    - "Wikipedia"
    - "CNBC"
---

# Tom Preston-Werner & Chris Wanstrath - GitHub

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Tom Preston-Werner & Chris Wanstrath（共同創業者: PJ Hyett） |
| 生年 | Preston-Werner: 1979年頃 / Wanstrath: 1985年3月13日 |
| 国籍 | アメリカ |
| 学歴 | Preston-Werner: Harvey Mudd College中退 / Wanstrath: University of Cincinnati（英語専攻）中退 |
| 創業前経験 | Preston-Werner: Gravatar創業、Powerset / Wanstrath: CNET Networks、GameSpot、Ruby on Railsコンサルティング |
| 企業名 | GitHub |
| 創業年 | 2008年4月10日 |
| 業界 | 開発者ツール / コード管理 / オープンソースホスティング |
| 現在の状況 | Microsoftに買収（2018年10月26日、$7.5B） |
| 評価額/時価総額 | $7.5B（買収時） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- 2007年10月、Chris WanstrathとTom Preston-WernerがサンフランシスコのRuby on Rails meetupで出会う
- スポーツバーで飲みながら「Gitのホスティングサービスがない」という課題について議論
- Ruby on Railsコミュニティでは、Gitの利用が増えていたが、SourceForgeのような中央集約型ホスティングサービスが存在しなかった

**課題の具体化**:
1. **Gitホスティングインフラの欠如**: 当時、Gitリポジトリをホストする良い選択肢がなく、利用の大きな障壁となっていた
2. **ソーシャル機能の欠如**: SourceForgeは配布には便利だったが、開発者向けの「ソーシャルネットワーク」が存在しなかった
3. **コラボレーション機能の不足**: Gitはコラボレーティブなソフトウェア開発を容易にしたが、それを実現するプラットフォームがなかった
4. **ユーザーエクスペリエンスの低さ**: 既存のGitoriousなどは基本的な機能はあったが、UXが粗末でエンタープライズレベルの洗練度がなかった

**需要検証方法**:
- Ruby on Railsコミュニティ内での対話
- 既存ツール（SourceForge、Gitorious）の利用状況分析
- 開発者たちの実際のペインポイントの観察

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 明確なインタビュー数は不明だが、Ruby on Rails meetupでの継続的な対話
- 手法: 開発者コミュニティとの直接対話、フィードバック収集
- 発見した課題の共通点:
  - Gitリポジトリのホスティング場所がない
  - コードレビューやコラボレーションのためのプラットフォームが不足
  - オープンソースプロジェクトの「ホーム」となる場所が必要

**3U検証**:
- **Unworkable（現状では解決不可能）**: 既存のツールではGitの分散型の特性を活かしたコラボレーションが困難
- **Unavoidable（避けられない）**: オープンソース開発の増加により、コードホスティングとコラボレーションは必須
- **Urgent（緊急性が高い）**: Ruby on RailsコミュニティでのGit採用が急速に進んでおり、即座の解決策が求められていた

**支払い意思（WTP）**:
- 確認方法: フリーミアムモデル（パブリックリポジトリは無料、プライベートは有料）
- 結果: 2009年2月時点で既に有料プランを提供し、収益を確保

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | GitHubのソリューション | 倍率 |
|---|------------|-----------------|------|
| 導入障壁 | 複雑なサーバー設定、インフラ管理 | サインアップのみで即利用可能 | 10x |
| コラボレーション速度 | メーリングリスト、パッチファイル | プルリクエスト、コードレビュー | 10x |
| ソーシャル機能 | なし（分散型のみ） | フォロー、Watch、Star、ネットワーク効果 | 100x |
| UX | コマンドラインのみ | モダンなWebインターフェース | 5x |
| 発見可能性 | 検索困難 | Explore、Trending、トピック機能 | 10x |

**MVP**:
- タイプ: プロトタイプ（Webアプリケーション）
- 初期反応: 2008年4月のローンチから急速に成長
- CVR: フリーミアムモデルのため、無料ユーザーから有料への転換率は不明だが、収益は年300%成長

**ローンチと初期トラクション**:
- **2008年1月**: プライベートベータ版公開
- **2008年4月10日**: 一般公開
- **2009年2月**: 46,000以上のパブリックリポジトリ（前月だけで約17,000が追加）
- **2009年7月**: 100,000ユーザー、90,000パブリックリポジトリ（5ヶ月で95%増加）
- **2010年7月**: 100万リポジトリ達成
- **2011年末**: 200万リポジトリ、SourceForge、Google Code、Microsoft CodePlexを超える

**UVP（独自の価値提案）**:
- "Social coding" - コードをソーシャルにする
- 誰でも簡単にオープンソースプロジェクトにコントリビュートできる
- 開発者のための「ソーシャルネットワーク」

**競合との差別化**:
- **vs SourceForge**: モダンなUI、Git特化、ソーシャル機能
- **vs Gitorious**: 洗練されたUX、スケーラビリティ、エンタープライズレベルの品質
- **vs Google Code**: Git対応、コミュニティ機能、開発者ファースト

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- **週末プロジェクトとしてスタート**: 当初は「副業」として構想、フルタイムでコミットするまでに時間がかかった
- **収益化の遅れ**: 初期は無料提供のみで、有料プランの導入に時間を要した
- **スケーリングの課題**: 急激な成長によるインフラとサポートの負担

### 3.2 重要な転換点

**4年間の自己資金運営**:
- 2008年〜2012年の4年間、外部資金を受け入れずに成長
- 個人開発者と企業から月額料金を徴収してビジネスを維持
- 2012年時点で年間収益成長率300%を達成

**a16z投資の決断（2012年）**:
- エンタープライズ市場への本格進出を決定
- $100Mの資金調達を実施（a16z史上最大のSeries A投資）
- Peter Levineが取締役として参画

## 4. 成長戦略

### 4.1 初期トラクション獲得

**コミュニティ主導の成長**:
- Ruby on Railsコミュニティからスタート
- 口コミ（Word-of-Mouth）による純粋な有機的成長
- 広告費ゼロで100,000ユーザーを1年で獲得

**オープンソースの力**:
- オープンソースプロジェクトを無料でホスト
- Rails自体がGitHubに移行し、信頼性を証明
- 開発者の「デフォルト選択」となる

### 4.2 フライホイール

```
開発者がGitHubでリポジトリを公開
       ↓
他の開発者がプロジェクトを発見
       ↓
コントリビューション（プルリクエスト）
       ↓
プロジェクトの品質向上
       ↓
より多くの開発者が参加
       ↓
ネットワーク効果が強化
       ↓
GitHubがデファクトスタンダードに
```

**ネットワーク効果の種類**:
1. **直接ネットワーク効果**: ユーザーが増えるほどコラボレーションの機会が増加
2. **データネットワーク効果**: リポジトリが増えるほど、検索・発見の価値が向上
3. **マーケットプレイスネットワーク効果**: 開発者と企業のマッチング

### 4.3 スケール戦略

**フリーミアムモデル**:
- パブリックリポジトリ: 完全無料（永久）
- プライベートリポジトリ: 有料プラン
- 企業向けプラン: GitHub Enterprise

**エンタープライズ進出（2012年以降）**:
- a16z投資後、エンタープライズ市場に本格参入
- GitHub Enterpriseのリリース
- 大企業への営業体制強化

**グローバル展開**:
- 世界中の開発者コミュニティに浸透
- 多言語対応、各地域での開発者イベント

### 4.4 バリューチェーン

1. **リポジトリホスティング**: コードの保存と管理
2. **コラボレーション機能**: プルリクエスト、Issues、プロジェクト管理
3. **コードレビュー**: 品質管理とナレッジシェア
4. **CI/CD統合**: GitHub Actions
5. **セキュリティ**: Dependabot、セキュリティアラート
6. **パッケージ管理**: GitHub Packages
7. **ドキュメンテーション**: GitHub Pages
8. **エンタープライズソリューション**: GitHub Enterprise

## 4.5 資金調達履歴

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Series A | 2012-07-09 | $100M | 不明 | Andreessen Horowitz | - |
| Series B | 2015-07-29 | $250M | $2B | Sequoia Capital | a16z（フォローオン） |

**総資金調達額**: $350M

**主要VCパートナー**:
- **Peter Levine** (Andreessen Horowitz): Series Aをリード、取締役に就任
- **Roelof Botha** (Sequoia Capital): Series Bに参加

### 資金使途と成長への影響

**Series A（$100M、2012年）**:
- プロダクト開発: GitHub Enterpriseの開発
- エンタープライズ営業チームの構築
- インフラのスケーリング
- 成長結果: 2012年時点で年間収益成長率300%

**Series B（$250M、2015年）**:
- グローバル展開の加速
- セキュリティ機能の強化
- 開発者ツールの拡充

### VC関係の構築

**a16z選考突破**:
- 2012年1月、GitHubチーム（Wanstrath, Preston-Werner, Hyett, Chacon）がa16zを訪問
- 数ヶ月にわたる対話を経て、2012年7月に投資決定
- a16zにとって史上最大のSeries A投資（$100M）
- Peter Levineが「農場全体を賭ける（betting the farm）」と表現

**投資家との関係維持**:
- Peter Levineが取締役として積極的に経営に関与
- エンタープライズ市場への戦略転換を支援
- Microsoft買収時（2018年）、a16zは$100M投資から$1B以上のリターンを獲得（10倍以上）

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | Ruby on Rails（初期）、Go、C、Shell |
| インフラ | AWS、自社データセンター |
| データベース | MySQL、Redis |
| 検索 | Elasticsearch |
| バージョン管理 | Git（当然） |
| 監視 | 自社開発ツール |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **開発者ファーストの文化**: 開発者自身が開発者のためにプロダクトを構築
2. **ネットワーク効果の最大化**: ソーシャル機能によるバイラル成長
3. **フリーミアムモデル**: オープンソースを無料にすることで圧倒的な普及を実現
4. **タイミング**: Gitの普及とオープンソースブームの波に乗る
5. **コミュニティ主導**: 口コミだけで100,000ユーザーを獲得

### 6.2 タイミング要因

- **Gitの普及期（2007-2010）**: Linuxカーネル開発で採用されたGitが開発者に浸透し始めた時期
- **オープンソースの台頭**: Ruby on Rails、jQuery、Node.jsなどのオープンソースプロジェクトが急増
- **ソーシャルメディアの興隆**: Facebook、Twitterなどのソーシャル機能が一般化
- **クラウドインフラの成熟**: AWSの登場により、スケーラブルなWebサービスの構築が容易に

### 6.3 差別化要因

- **Social Coding**: コードをソーシャルにするという独自のコンセプト
- **美しいUX**: 開発者ツールとしては異例のデザイン性
- **プルリクエスト**: コードレビューとコントリビューションを簡単にする革新的な機能
- **オープンソースへの貢献**: 自らもオープンソースツール（Jekyll、Hubot等）を公開

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本でもGitHubは開発者のデファクトスタンダード |
| 競合状況 | 4 | GitLab、Bitbucketなどの競合はいるが、GitHubが圧倒的シェア |
| ローカライズ容易性 | 5 | コードは言語を超える、日本語UIも提供済み |
| 再現性 | 3 | ネットワーク効果とタイミングが重要で再現は困難 |
| **総合** | 4.3 | 開発者コミュニティ主導の成長戦略は日本でも有効 |

**日本市場での実績**:
- 日本のソフトウェア企業の多くがGitHubを採用
- 日本語ドキュメントとサポートが充実
- 日本のオープンソースコミュニティでも標準プラットフォーム

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **コミュニティ内の対話**: Ruby on Rails meetupでの開発者同士の会話から課題を発見
- **既存ツールの不満**: SourceForge、Gitoriousなど既存ソリューションの限界を観察
- **隣接市場の観察**: ソーシャルメディア（Facebook、Twitter）の成功をコード管理に適用

### 8.2 CPF検証（/validate-cpf）

- **コミュニティでの継続的な対話**: Ruby on Rails meetupを通じた課題の共通性確認
- **3U検証**: Git採用の増加により、ホスティングとコラボレーションの課題は緊急性が高かった
- **支払い意思**: フリーミアムモデルで初期からマネタイズに成功

### 8.3 PSF検証（/validate-10x）

- **10倍優位性**: 導入障壁の10倍削減、ソーシャル機能の100倍向上
- **MVP**: プライベートベータ→一般公開で段階的に検証
- **初期トラクション**: 1年で100,000ユーザー、5ヶ月で95%成長

### 8.4 スコアカード（/startup-scorecard）

| 評価項目 | スコア | 根拠 |
|---------|-------|------|
| 問題の明確さ | 10/10 | 開発者自身が経験していた課題 |
| 差別化 | 10/10 | ソーシャル機能とUXで圧倒的差別化 |
| ユーザーエンゲージメント | 10/10 | デイリーアクティブユーザー、リポジトリ数の急増 |
| PMF兆候 | 10/10 | 1年で100,000ユーザー、口コミのみでの成長 |
| ネットワーク効果 | 10/10 | ユーザーとリポジトリの増加が価値を加速 |

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **デザイナー向けの「GitHub」**: Figmaのようなツールとコラボレーション機能を統合した、デザイン版GitHubを構築
2. **ノーコード開発者向けプラットフォーム**: ノーコードツールで作成したアプリのバージョン管理とコラボレーションを実現
3. **エンタープライズ内製化支援プラットフォーム**: 日本企業の内製開発を支援する、GitHub Enterpriseのローカライズ版に特化したサービス
4. **教育機関向けコードレビュープラットフォーム**: プログラミング教育でのコードレビューと課題管理に特化したツール

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2008年4月10日） | ✅ PASS | Wikipedia, TechCrunch, GitHub Blog |
| a16z投資額（$100M、2012年） | ✅ PASS | TechCrunch, Fortune, a16z公式 |
| Microsoft買収額（$7.5B、2018年） | ✅ PASS | CNBC, Microsoft公式発表, a16z公式 |
| 100,000ユーザー（2009年7月） | ✅ PASS | Wikipedia Timeline, Nira.com |
| a16zリターン（$1B+） | ✅ PASS | Fortune記事 |
| Series A史上最大（a16z） | ✅ PASS | TechCrunch, Fortune |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [TechCrunch - GitHub Pours Energies into Enterprise (2012/7/9)](https://techcrunch.com/2012/07/09/github-pours-energies-into-enterprise-raises-100-million-from-power-vc-andreesen-horowitz/)
2. [Fortune - Why Andreessen Horowitz Wrote GitHub's First Big Check Back in 2012 (2018/6/4)](https://fortune.com/2018/06/04/microsoft-github-andreessen-horowitz/)
3. [a16z - Microsoft Buys GitHub](https://a16z.com/microsoft-buys-github/)
4. [a16z - GitHub Announcement](https://a16z.com/announcement/github/)
5. [CNBC - Chris Wanstrath co-founded GitHub (2018/6/4)](https://www.cnbc.com/2018/06/04/chris-wanstrath-co-founded-github-which-microsoft-bought-for-billions.html)
6. [Wikipedia - Tom Preston-Werner](https://en.wikipedia.org/wiki/Tom_Preston-Werner)
7. [Wikipedia - Chris Wanstrath](https://en.wikipedia.org/wiki/Chris_Wanstrath)
8. [Wikipedia - Timeline of GitHub](https://en.wikipedia.org/wiki/Timeline_of_GitHub)
9. [Nira - How GitHub Democratized Coding](https://nira.com/github-history/)
10. [GitHub Blog - Building GitHub with Ruby and Rails](https://github.blog/engineering/architecture-optimization/building-github-with-ruby-and-rails/)
11. [University of Cincinnati Magazine - Chris Wanstrath shares his story](https://magazine.uc.edu/editors_picks/recent_features/wanstrath.html)
12. [Tom Preston-Werner - How I Turned Down $300,000 from Microsoft](https://tom.preston-werner.com/2008/10/18/how-i-turned-down-300k.html)
13. [Timelines - Timeline of GitHub](https://timelines.issarice.com/wiki/Timeline_of_GitHub)
14. [DEV Community - Engineering Open Source Communities with DevEx](https://dev.to/jerdog/its-not-rocket-science-its-a-flywheel-engineering-open-source-communities-with-devex-4id2)
15. [The State of the Octoverse - The global developer community](https://octoverse.github.com/2022/developer-community)
