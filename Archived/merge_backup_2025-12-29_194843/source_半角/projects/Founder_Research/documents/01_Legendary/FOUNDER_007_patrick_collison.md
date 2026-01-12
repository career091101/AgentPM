---
id: "FOUNDER_007"
title: "Patrick Collison - Stripe"
category: "founder"
tier: "legendary"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: [FinTech, Payments, Developer Tools, API, B2B, SaaS]

# 基本情報
founder:
  name: "Patrick Collison"
  birth_year: 1988
  nationality: "Irish"
  education: "MIT dropout"
  prior_experience: "Auctomatic創業者（$5Mで売却）"
  co_founder: "John Collison（弟）"

company:
  name: "Stripe"
  founded_year: 2010
  industry: "FinTech / Payments Infrastructure"
  current_status: "private"
  valuation: "$91.5B (2025年2月時点)"
  employees: 5493
  revenue: "$5.12B (2024年)"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 95
    wtp_confirmed: true
    urgency_score: 8
    validation_method: "創業者自身の経験・YC企業での検証"
  psf:
    ten_x_axes:
      - axis: "統合時間"
        multiplier: 100
      - axis: "開発者体験"
        multiplier: 10
    mvp_type: "api"
    initial_cvr: null
    uvp_clarity: 10
    competitive_advantage: "7行のコードで決済統合・開発者ファースト・即座の利用開始"
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
  related_founders: ["John Collison", "Elon Musk", "Peter Thiel", "Paul Graham"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia"
    - "Startup Grind"
    - "Y Combinator Library"
    - "TechCrunch"
    - "Stripe Newsroom"
---

# Patrick Collison - Stripe

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Patrick Collison（CEO）、John Collison（President） |
| 生年 | 1988年9月9日 |
| 国籍 | アイルランド |
| 学歴 | MIT中退（2009年） |
| 創業前経験 | Auctomatic創業（$5Mで売却、2008年） |
| 企業名 | Stripe |
| 創業年 | 2010年 |
| 業界 | FinTech / 決済インフラ |
| 現在の状況 | 未上場（IPO検討中） |
| 評価額 | $91.5B（2025年2月） |
| 従業員数 | 約5,500名 |
| 年間収益 | $5.12B（2024年） |

## 2. 創業ストーリー

### 2.1 生い立ち・神童時代

**アイルランドの田舎での成長**:
- アイルランド・ティペラリー州の小村Dromineerで生まれる
- 父Denis（電子技術者）、母Lily（微生物学者）
- 8歳でリムリック大学のコンピューターコースを受講
- 10歳からプログラミングを独学

**若き天才**:
- 2005年（16歳）: アイルランド Young Scientist of the Year 受賞
- LISP系プログラミング言語「Croma」を開発（AI・プログラミング分野）
- メアリー・マカリース大統領から賞金7,500ユーロとウォーターフォードクリスタルのトロフィーを授与
- 13歳でSATを受験、16歳でMITに入学

### 2.2 最初の起業: Auctomatic

**Y Combinator参加（Winter 2007）**:
- 弟Johnと共に「Shuppa」（アイルランド語で「店」の意）を創業
- Enterprise Irelandから資金調達できず、シリコンバレーへ移住
- Y Combinator参加後、オックスフォード卒のTaggar兄弟と合流し「Auctomatic」に改名
- eBay出品者向けの在庫管理・出品ツール

**早期イグジット**:
- 2008年3月（聖金曜日）: カナダのLive Current Mediaに$5Mで売却
- Patrick 19歳、John 17歳で億万長者に

### 2.3 課題発見（需要発見）

**着想源**:
- 2009年秋、Johnがハーバード大学に入学
- 2009年末、UC Berkeley主催のスタートアップイベントからの帰り道で議論
- Johnが「オンラインでお金を動かす簡単な方法」を作ることを提案

**自身の経験からの課題意識**:
- Auctomatic開発時、PayPalなど既存決済システムとの統合に苦労
- ウェブで決済を受け付けることが「なぜこんなに難しいのか」という疑問
- 銀行、決済プロセッサー、金融機関との複雑な関係構築が必要
- 煩雑な書類手続き、長期のオンボーディングプロセス

### 2.4 CPF検証（Customer Problem Fit）

**課題の明確化**:
- 2010年時点でオンライン決済の統合は「悪夢」だった
- 開発者が決済を実装するのに数週間〜数ヶ月かかっていた
- 既存システムは遅く、扱いにくく、開発者フレンドリーではなかった

**3U検証**:
- **Unworkable**: 既存の決済統合は複雑すぎて、多くのスタートアップが決済実装を後回しに
- **Unavoidable**: Eコマース・SaaS・マーケットプレイスの成長に決済は不可欠
- **Urgent**: モバイル決済・オンラインサービスの急速な成長

**支払い意思（WTP）**:
- 最初の顧客は友人のRoss Boucher（280 North）
- プロトタイプ完成から2週間で初の取引を実現
- Ross Boucherは後にStripeの初期社員に

**投資家の反応**:
- 2009-2010年当時、多くの投資家がStripeのアイデアを却下
- 理由: 開発者向けサービス、決済市場は既に混雑、パートナーシップ依存のビジネスモデル
- PayPalやSquareも「Stripeが解決する問題は十分大きくない」と判断

### 2.5 PSF検証（Problem Solution Fit）

**10倍優位性: 7行のコード革命**

| 軸 | 従来の解決策 | Stripeソリューション | 倍率 |
|---|------------|-----------------|------|
| 統合時間 | 数週間〜数ヶ月 | 数時間〜1日 | 100倍 |
| コード量 | 数百〜数千行 | 7行 | 100倍+ |
| 開発者体験 | 煩雑・ドキュメント不足 | シンプル・優れたドキュメント | 10倍 |
| オンボーディング | 書類手続き・審査 | 即座に利用開始 | 10倍+ |

**「7行のコード」の意味**:
- 2011年のランディングページでは9行のコードスニペットを掲載
- オプションのdescriptionとcard[cvc]を除くと視覚的に7行
- 実際の本番統合が7行という意味ではない
- しかし、クレジットカード処理という複雑な処理を数行のコードに凝縮し、即座に成功するChargeオブジェクトが返ってくる体験は「魔法のよう」だった

**MVP**:
- 2010年初頭にプロトタイプ開発開始
- 2010年秋からPatrickとJohnがフルタイムで取り組み
- 2011年9月29日: 一般公開

**UVP（独自の価値提案）**:
- 「ウェブとモバイルアプリの決済を簡単に」
- 開発者ファースト: 財務・オペレーション部門ではなく開発者をターゲット

**競合との差別化**:
- APIファースト設計
- 優れたドキュメンテーション
- 開発者コミュニティへのフォーカス
- 規制・銀行との複雑性を抽象化

## 3. 初期の成功と学び

### 3.1 Auctomatic での学び

- 19歳と17歳で$5Mのイグジット達成
- Y Combinatorエコシステムとの関係構築
- Paul Grahamとの繋がり（Lispへの共通の関心）
- スタートアップ運営の実践経験

### 3.2 Stripeでの早期検証

- プロトタイプ完成から2週間で初取引
- 6ヶ月後に「大きな何かを掴んでいる」と確信
- 求めていたユーザー体験を実現できることを確認
- 2010年秋からフルタイムコミット

## 4. 成長戦略

### 4.1 初期トラクション獲得: Collison Installation

**「Collison Installation」手法**:
- Y Combinator内で有名になった積極的な初期ユーザー獲得手法
- 通常の創業者: 「ベータ版を試してもらえますか？」→「リンクを送ります」
- Collison兄弟: 「いいですよ、ラップトップを貸してください」→ その場でセットアップ
- 消極的な待ちの姿勢ではなく、積極的に行動

**最初の10-30顧客**:
- Y Combinator企業から獲得
- Stripeは厳密にはYC W10ではなかったが、Auctomatic時代のYC経験を活用
- 最初の顧客Ross Boucher（280 North）は友人の創業者

### 4.2 成長哲学

**初期のマーケティング戦略**:
- 「良い・面白いと思うブログ記事を書き、良いプロダクトを作り、口コミで広がることを期待」
- 会社設立から2年以上、StackOverflowでの広告すら出さなかった
- プロダクト品質とユーザー体験に集中

**ニッチから拡大**:
- Y Combinatorエコシステムという小さく影響力のあるオーディエンスに集中
- スタートアップと共に成長（スタートアップが成功すればStripeへの支払いも増加）
- 若い企業が成功するにつれ、Stripeへの称賛と事例が広がる
- より大きな企業への営業機会が開ける

### 4.3 フライホイール

```
開発者採用
    ↓
優れた開発者体験 → スタートアップ顧客獲得 → スタートアップ成長
    ↓                                           ↓
口コミ拡散 ← Stripe事例増加 ← 決済処理量増加 ← 収益増加
    ↓
エンタープライズ顧客獲得 → さらなる規模拡大 → プラットフォーム拡張
```

### 4.4 資金調達

**主要ラウンド**:

| 時期 | ラウンド | 金額 | 主要投資家 | 評価額 |
|------|---------|------|-----------|-------|
| 2010 | Seed | - | Y Combinator | - |
| 2011 | Series A | $2M | Sequoia, a16z, Elon Musk, Peter Thiel | - |
| 2016 | - | - | CapitalG, General Catalyst | $9.2B |
| 2021 | Series H | - | - | $95B（ピーク） |
| 2023 | Series I | $6.87B | Thrive Capital | $50B |
| 2024 | - | $694M | - | $65B |
| 2025.2 | Tender | - | - | $91.5B |

**総調達額**: $9.81B（24ラウンド、119投資家）

### 4.5 現在の規模

- 決済処理量: $1.4T（2024年、前年比38%増）
- 顧客数: 130万以上のアクティブビジネス
- Fortune 100の約50%、Fortune 500の60%以上が利用
- AI企業（OpenAI、Anthropic、Perplexity、Mistral）がStripeを採用
- 2024年は初の通年黒字（FCF約$2.2B）

## 5. 企業文化

### 5.1 コアバリュー・原則

**Users First（ユーザー第一）**:
- Stripeに構築されたビジネスとその顧客への責任を認識
- すべての決定でユーザーニーズを中心に据える

**Move with Urgency and Focus（緊急性と集中を持って動く）**:
- アクションへのバイアスが学習を加速し、ユーザーを喜ばせる
- 最も重要なことに集中
- 素早く初期進捗を出し、最良の結果に向けて反復

**Curious（好奇心）**:
- 人、アイデア、未知への純粋な興味を持ってリード
- 他の視点を理解しようと努力
- 正しいことより調査することを優先

**Humble（謙虚さ）**:
- 傲慢でも自己満足でもない
- 包括的な環境を作る
- 現在のプラクティスに固執しない

### 5.2 採用哲学

**慎重かつゆっくり採用**:
- 最初の5人の採用に約2年かけた
- 有望な候補者と広範に協働してから採用決定
- 最初の10人の採用が不釣り合いに重要

**採用フィルター**:
- 知性、マインドセット、カルチャーアドを重視
- バックグラウンドだけでなく人物を見る
- 従業員に新規採用への拒否権を付与

**報酬哲学**:
- 初期社員にエクイティを広く分配
- 給与ではなくミッションで人を惹きつける
- 結果として通常より高い定着率

### 5.3 エンジニアリング文化

**クロスポリネーション（相互交流）**:
- 新規エンジニアは自分のチームに配属される前に、他のすべてのチームで何かをシップする
- より広いコンテキストを獲得させる
- サイロ化を防ぐ

**小さなチーム、高い品質**:
- 大きなチームが常に良いとは限らない
- Patrick: 「5人または10人を1年間」と言われたら「500kgまたは1000kgのエンジニア」と冗談で返す
- コード品質と直接的なフィードバックループを重視

**プロダクトファースト**:
- 開発者ニーズと信頼性に焦点
- 所有権とスピードを維持するための慎重な採用基準

### 5.4 「Yes And」文化

- 新しいアイデアにオープンで受容的な文化を維持
- ほとんどのアイデアが悪くても可能性を考えることを楽しむ
- 年次「Crazy Ideas」ドキュメント: 「おそらく悪いが、うまくいけば素晴らしい」アイデアを全員が投稿
- 非従来型の思考を表出させる

### 5.5 透明性

- すべての部門の情報に従業員がアクセス可能
- 社内メールコミュニケーションは全員に公開
- 連邦的理解、好奇心の充足、最良の意思決定を支援

## 6. 使用ツール・アプローチ

| カテゴリ | ツール/アプローチ |
|---------|-----------------|
| プロダクト | APIファースト設計、開発者ドキュメント重視 |
| マーケティング | コンテンツマーケティング、口コミ、開発者コミュニティ |
| 採用 | 慎重な採用、エクイティ分配、カルチャーフィット重視 |
| 組織 | 透明性、クロスチーム経験、小さなチーム |
| 資金調達 | 戦略的投資家（PayPal創業者、トップVC）|

## 7. 成功要因分析

### 7.1 主要成功要因

1. **自身の痛みからの課題発見**: Auctomatic開発時の決済統合の苦労から着想
2. **開発者ファースト**: 財務部門ではなく開発者をターゲットにした逆転の発想
3. **10倍の体験改善**: 7行のコードという象徴的なシンプルさ
4. **積極的な初期獲得**: Collison Installationによる即座のオンボーディング
5. **ネットワーク効果**: YCエコシステムからの拡大

### 7.2 タイミング要因

- モバイル決済・Eコマースの急成長期
- SaaS・サブスクリプションモデルの台頭
- スタートアップエコシステムの拡大
- クラウドインフラの成熟

### 7.3 差別化要因

- 競合が「開発者は小さな市場」と軽視した領域に集中
- 規制・銀行との複雑性を抽象化
- 継続的なプロダクト改善と拡張

## 8. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 4 | キャッシュレス推進、EC成長 |
| 競合状況 | 3 | PAY.JP、GMO-PG等が存在 |
| ローカライズ容易性 | 3 | 規制・銀行システムの違い |
| 再現性 | 4 | 開発者ファーストは適用可能 |
| **総合** | 3.5 | 開発者体験重視のアプローチは参考になる |

## 9. orchestrate-phase1への示唆

### 9.1 需要発見（/discover-demand）

- **示唆**: 自分自身が経験した課題から始める（Collisonは決済統合の苦労を経験）
- **適用**: 創業者が深く理解している領域で課題を探す

### 9.2 CPF検証（/validate-cpf）

- **示唆**: 周囲から「小さすぎる」と言われても、開発者コミュニティなど特定セグメントに集中
- **適用**: ニッチでも影響力のあるセグメントを最初のターゲットに

### 9.3 PSF検証（/validate-10x）

- **示唆**: 10倍優位性は「統合時間」と「開発者体験」で達成
- **適用**: 技術的複雑性を抽象化し、シンプルなインターフェースを提供

### 9.4 成長戦略

- **示唆**: Collison Installation - 積極的にその場でセットアップ
- **適用**: 「リンクを送ります」ではなく「今すぐ設定しましょう」

### 9.5 スコアカード（/startup-scorecard）

- **示唆**: 最初の顧客獲得後、6ヶ月で「大きな何か」を確信
- **適用**: 早期の定性的シグナルを重視

## 10. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **開発者向けSaaS API**: 複雑な日本固有のシステム（銀行API、行政手続き）をシンプルなAPIで提供
2. **B2B FinTechインフラ**: 日本の中小企業向け決済・請求管理の簡素化
3. **開発者コミュニティファースト**: 技術者向けサービスで口コミを活用

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 生年月日（1988年9月9日） | ✓ | Wikipedia |
| Young Scientist受賞（2005年、16歳） | ✓ | Wikipedia, Startup Grind |
| Auctomatic売却（$5M、2008年） | ✓ | Multiple sources |
| Stripe創業（2010年） | ✓ | Wikipedia, YC Library |
| 一般公開（2011年9月29日） | ✓ | Stripe Blog |
| Series A投資家（Musk, Thiel, Sequoia, a16z） | ✓ | Wikipedia |
| 評価額$91.5B（2025年2月） | ✓ | TechCrunch, Stripe Newsroom |
| 2024年収益$5.12B | ✓ | Sacra |
| 決済処理量$1.4T（2024年） | ✓ | TechCrunch |

## 参照ソース

1. [Patrick Collison - Wikipedia](https://en.wikipedia.org/wiki/Patrick_Collison)
2. [The Collison Brothers and Story Behind The Founding Of Stripe - Startup Grind](https://www.startupgrind.com/blog/the-collison-brothers-and-story-behind-the-founding-of-stripe/)
3. [Patrick & John Collison, Co-Founders of Stripe - Y Combinator](https://www.ycombinator.com/library/Kx-patrick-john-collison-co-founders-of-stripe)
4. [Stripe's payments APIs: The first 10 years - Stripe Blog](https://stripe.com/blog/payment-api-design)
5. [The First Few: Stripe - Just Go Grind](https://www.justgogrind.com/p/the-first-few-stripe)
6. [How Stripe Grows - How They Grow](https://www.howtheygrow.co/p/how-stripe-grows)
7. [An interview with Patrick Collison - High Growth Handbook](https://growth.eladgil.com/book/chapter-5-organizational-structure-and-hypergrowth/you-cant-delegate-culture-an-interview-with-patrick-collison/)
8. [Stripe finalizes tender sale at $91.5B valuation - TechCrunch](https://techcrunch.com/2025/02/27/stripe-finalizes-tender-sale-at-a-91-5b-valuation-says-payment-volumes-grew-to-1-4t-in-2024/)
9. [Stripe revenue, valuation & funding - Sacra](https://sacra.com/c/stripe/)
10. [Patrick Collison on Stripe & Early Stage Startup Principles - Unicorn Growth](https://www.unicorngrowth.io/p/patrick-collison-stripe-startup-principles)
11. [Inside Stripe's Engineering Culture - Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/stripe)
12. [Stripe announces tender offer - Stripe Newsroom](https://stripe.com/newsroom/news/employee-liquidity-feb-2025)
