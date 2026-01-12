---
id: "FOUNDER_004"
title: "Marc Andreessen - Netscape/a16z"
category: "founder"
tier: "legendary"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: [Web Browser, Venture Capital, Software, Serial Entrepreneur, Internet Pioneer]

# 基本情報
founder:
  name: "Marc Andreessen"
  birth_year: 1971
  nationality: "American"
  education: "University of Illinois at Urbana-Champaign (Computer Science)"
  prior_experience: "NCSA Mosaic共同開発者"

company:
  name: "Netscape / Andreessen Horowitz (a16z)"
  founded_year: 1994
  industry: "Web Browser / Venture Capital"
  current_status: "Netscape: 1999年AOLに売却 / a16z: active"
  valuation: "Netscape IPO時$2.9B / a16z AUM $46B"
  employees: 500+

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 95
    wtp_confirmed: true
    urgency_score: 9
    validation_method: "市場投入・即時採用"
  psf:
    ten_x_axes:
      - axis: "使いやすさ"
        multiplier: 10
      - axis: "グラフィカル表示"
        multiplier: 100
    mvp_type: "working_product"
    initial_cvr: null
    uvp_clarity: 10
    competitive_advantage: "インライン画像表示・JavaScript・SSL暗号化"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "Loudcloud破綻危機"
    original_idea: "クラウドインフラサービス"
    pivoted_to: "Opswareソフトウェア"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Jim Clark", "Ben Horowitz", "Eric Bina", "Brendan Eich"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia"
    - "Britannica"
    - "a16z.com"
    - "Internet History Podcast"
    - "Wall Street Journal"
---

# Marc Andreessen - Netscape/a16z

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Marc Andreessen |
| 生年 | 1971年7月9日 |
| 国籍 | アメリカ人 |
| 学歴 | イリノイ大学アーバナ・シャンペーン校（コンピュータサイエンス学士、1993年） |
| 創業前経験 | NCSA（国立スーパーコンピューティング応用センター）でMosaicブラウザ共同開発 |
| 企業名 | Netscape Communications (1994), Loudcloud/Opsware (1999), Andreessen Horowitz (2009) |
| 創業年 | Netscape: 1994年, a16z: 2009年 |
| 業界 | Webブラウザ / クラウドコンピューティング / ベンチャーキャピタル |
| 現在の状況 | a16z: 運用中（AUM $46B） |
| 評価額/時価総額 | Netscape IPO時: $2.9B, AOL買収時: $4.2B |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**Mosaicブラウザ開発（1992-1993年）**:
- イリノイ大学在学中、NCSAでパートタイム勤務
- 当時のWebブラウザは使いにくく、テキストと画像が別々のウィンドウで表示されていた
- ユーザーフレンドリーでグラフィカルなブラウザの必要性を認識

**Mosaic開発の決断**:
- 同僚のEric Binaを誘い、より使いやすいブラウザ開発に着手
- 世界初のインライン画像表示対応ブラウザを開発
- ハイパーリンクを青色、訪問済みリンクを紫色にする設計を導入（1993年頃）

**Jim Clarkとの出会い（1994年）**:
- 1993年卒業後、シリコンバレーでセキュリティ製品会社に勤務
- Silicon Graphics創業者Jim Clarkからメールを受信
- 「新会社を設立する予定。参加を検討してほしい」という内容
- ブレインストーミングの結果、「Mosaicキラー」を作ることを決定

### 2.2 CPF検証（Customer Problem Fit）

**課題の明確化**:
- 既存のWebブラウザは技術者向けで一般ユーザーには使いにくい
- インターネットの可能性は大きいが、アクセス手段が限られている
- 商用ブラウザが存在しない

**3U検証**:
- **Unworkable**: 既存ブラウザは画像を別ウィンドウで表示、操作が複雑
- **Unavoidable**: インターネットの商用化が進み、ブラウザは必須に
- **Urgent**: 市場の急成長に対応する必要あり

**支払い意思（WTP）**:
- 企業向けライセンス販売で収益化
- 4ヶ月でブラウザ市場の75%を獲得 → 強い需要を証明

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | Netscapeソリューション | 倍率 |
|---|------------|-----------------|------|
| 使いやすさ | コマンドライン的UI | グラフィカルUI | 10倍 |
| 画像表示 | 別ウィンドウ | インライン表示 | 100倍 |
| セキュリティ | なし | SSL暗号化 | ∞ |
| 動的機能 | 静的ページのみ | JavaScript対応 | 100倍 |

**MVP**:
- Mosaic Netscape 0.9: 1994年10月13日リリース
- リリース後4ヶ月でブラウザ市場の75%を獲得

**UVP（独自の価値提案）**:
- 「誰もが使えるWebブラウザ」
- 「セキュアなオンライン取引を可能に」

**技術革新**:
- JavaScript（Brendan Eich開発）: クライアントサイドスクリプティングを実現
- SSL（Secure Sockets Layer）: オンラインセキュリティの基盤を確立
- HTTP Cookie（Lou Montulli開発）: ユーザーセッション管理を可能に

### 2.4 Netscape IPO（1995年8月9日）

**IPO詳細**:
- 創業から約16ヶ月、利益ゼロの状態でIPO
- 当初価格$14 → 直前に$28に引き上げ
- 初値$71（需要過多で2時間取引開始できず）
- 終値$58.25 → 時価総額$2.9B
- 1995年末には株価$174に上昇

**Andreessenの持ち分**:
- IPO日終値で約$59M
- 1ヶ月後（株価$115時）: 260万株 × $115 = $287M
- 24歳でシリコンバレーのアイコンに

**歴史的意義**:
- Wall Street Journal: 「General Dynamicsが$2.7Bに到達するのに43年かかった。Netscapeは約1分で達成した」
- 「Netscape moment」という言葉の起源
- ドットコムバブルの引き金となったIPO

## 3. ブラウザ戦争と敗北

### 3.1 Microsoftとの競争（1995-1998）

**Microsoftの参入**:
- 1995年8月24日: Internet Explorer 1.0をWindows 95に同梱
- 1995年11月27日: Internet Explorer 2.0リリース
- 1995年12月7日（「真珠湾攻撃の日」）: IEを永久無料化宣言

**競争の激化**:
- 1995年中頃: Netscape市場シェア80%
- 1997年末: Netscape 51% vs IE 40%
- 1998年9月: IEがNetscapeを逆転

**Microsoftの戦術**:
- Windows OSにIEをバンドル
- Compaqに対しNetscapeプリインストール時のWindowsライセンス撤回を警告
- Microsoft幹部の発言: 「Netscapeの酸素供給を断つ」（1998年反トラスト裁判で証言）

### 3.2 AOLへの売却

**敗北と売却**:
- 1998年: 競争激化と市場シェア低下
- 1999年: AOLが$4.2Bで買収
- ブラウザコードをオープンソース化 → Mozillaプロジェクトへ → 後のFirefox誕生

**Andreessenの教訓**:
- 「Microsoftに潰された」経験
- 独占的プラットフォームの脅威を身をもって学ぶ
- 後のVC投資哲学に大きな影響

## 4. Loudcloud/Opswareの失敗と復活

### 4.1 Loudcloud創業（1999年）

**創業背景**:
- Andreessen、Ben Horowitz、Tim Howes、In Sik Rheeが共同創業
- クラウドコンピューティングの先駆け（IaaS/SaaSモデル）
- ドットコムバブルのピーク時にスタート

**IPOとバブル崩壊**:
- 2000年9月: IPO発表
- S-1提出書類: 過去6ヶ月の売上$1.94M、来年予測$75M
- 3週間で資金が尽きる状態でIPO強行
- $6で25Mシェア発行、$150M調達
- 営業損失$164.8M、売上$15.5M

### 4.2 危機と転換

**最大の危機（2002年初頭）**:
- 最大顧客（月$1M、売上の20%）が破綻
- 株価$0.35（時価総額$30M、現金残高$60Mの半分）
- 投資家がLoudcloudの破綻を予想

**ピボット（2001-2002年）**:
- 500-600人をレイオフ
- データセンター事業をEDSに売却
- ソフトウェア会社「Opsware」にピボット
- データセンター自動化ソフトウェアに注力

### 4.3 復活と売却

**8年間の苦闘**:
- ドットコムバブル崩壊を生き延びる
- ソフトウェア事業で黒字化
- 2007年: Hewlett-Packardが$1.6Bで買収

**Andreessenの持ち分**:
- Opsware売却で約$138M獲得

**学んだ教訓**:
- 「タイミングを間違えた」だけで諦めない
- 「タイミングが正しくなる別のビジネスにピボットする」
- この経験が後のa16z投資哲学の基盤に

## 5. Andreessen Horowitz（a16z）創業

### 5.1 創業背景（2009年）

**エンジェル投資家時代（2006-2010年）**:
- Andreessen、Horowitz両名で45社に$4M投資
- Twitter等に初期投資
- 「スーパーエンジェル」として認知

**a16z創業（2009年7月6日）**:
- 金融危機の真っ只中で新VCを設立
- 初期資金: $300M
- 支援者: Ron Conway、Peter Thiel等

**ユニークなアプローチ**:
- 従来VCモデル（資金提供のみ）からの脱却
- 「ホリスティックなスタートアップ支援」を標榜
- 元起業家がVCを運営する方が良いという哲学

### 5.2 成長軌跡

| 年 | AUM | 注目イベント |
|---|-----|------------|
| 2009 | $300M | 創業 |
| 2012 | $2.7B | 3ファンド運用 |
| 2025 | $46B | VC業界AUM1位 |

### 5.3 注目投資案件

| 企業 | 投資年 | 投資額 | リターン/結果 |
|------|-------|--------|-------------|
| Facebook | 2010 | $50M | 大成功（IPO前投資） |
| Twitter | 2011 | $80M | 大成功 |
| Airbnb | 2011 | $60M | IPO時$47B評価 |
| GitHub | 2012 | $100M | Microsoft買収で$1B+リターン |
| Coinbase | 2013 | $25M | IPO時$86B評価 |

## 6. VC投資哲学

### 6.1 コア哲学

**「Software is Eating the World」（2011年）**:
- Wall Street Journalに寄稿した有名エッセイ
- ソフトウェア企業があらゆる産業を変革するという予言
- 2021年時点: エンタープライズソフトウェア支出$600B（2011年比123%増）

**ポイント**:
- ソフトウェアは「強力で柔軟なツール」
- プロセス最適化、タスク自動化、新しい接続を可能に
- コンピューティングコストの低下がスケールを可能に

### 6.2 投資基準

**1. 非コンセンサス投資**:
- 「多くの人が疑うがうまくいく」アイデアに投資
- ミスプライスされたオプションを買う
- 「ベスト・カンパニーに投資する。ベスト・バーゲンではなく」

**2. 創業者重視**:
- 「結局、決断は人に関するものだ」
- ビジョン、ドメイン専門性、リーダーシップ、適応力を評価

**3. 市場規模と成長ポテンシャル**:
- 大きな市場での大きなブレークスルーに注力
- 年間約4,000社のうち200社が投資適格、うち15社が95%のリターンを生む

**4. プロダクト・マーケット・フィット（PMF）**:
- 「唯一重要なことはPMFを達成すること」
- PMFなし: 顧客が価値を感じない、口コミが広がらない、成長が遅い
- PMFあり: 「作れるだけ早く顧客が買う」「サーバーを増設するのが追いつかない」

### 6.3 投資スタイル

**ステージ不問**:
- Seed、Venture、Growthすべてに投資
- AI、バイオ・ヘルスケア、消費者、クリプト、エンタープライズ、フィンテック、ゲーム、インフラ等

**分散投資**:
- 年間数十〜数百社に投資
- 複数業界への分散
- 「リスク許容度が他社より大きい」

**長期視点**:
- 変革的企業の構築には時間がかかることを理解
- 複数の成長ステージを通じて支援

## 7. 成功要因分析

### 7.1 主要成功要因

1. **技術先見性**: Webブラウザ、クラウド、ソフトウェアの重要性を早期に認識
2. **失敗からの学び**: Netscape敗北、Loudcloud危機を糧に
3. **First Principles思考**: 既存の常識を疑い本質から考える
4. **ネットワーク構築**: シリコンバレー最強の人的ネットワーク

### 7.2 タイミング要因

- Mosaicブラウザ: Webの商用化黎明期
- Netscape: インターネット普及前夜
- a16z: 金融危機後の回復期（逆張り）

### 7.3 差別化要因

- 起業家経験を持つVC
- 包括的なポートフォリオ支援
- メディアカンパニーとしての発信力

## 8. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 4 | ソフトウェア・SaaS市場拡大中 |
| 競合状況 | 3 | VCは増加、差別化が必要 |
| ローカライズ容易性 | 4 | 投資哲学は普遍的 |
| 再現性 | 3 | 起業経験 + ネットワークが必要 |
| **総合** | 3.5 | 哲学とアプローチは参考になる |

## 9. orchestrate-phase1への示唆

### 9.1 需要発見（/discover-demand）

- **示唆**: 技術者として「自分が欲しいもの」を作る（Mosaicブラウザ）
- **適用**: 創業者自身の痛みを解決するプロダクト開発

### 9.2 CPF検証（/validate-cpf）

- **示唆**: 市場投入して即座にフィードバックを得る
- **適用**: 4ヶ月で75%シェア = 強いPMFの証拠

### 9.3 PSF検証（/validate-10x）

- **示唆**: 10倍優位性は「使いやすさ」と「新機能」で達成
- **適用**: インライン画像、JavaScript、SSLという複合的革新

### 9.4 スコアカード（/startup-scorecard）

- **示唆**: タイミングが間違っても諦めない（Loudcloud→Opsware）
- **適用**: ピボット能力と粘り強さの評価

## 10. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **日本版a16z**: 起業家経験者によるVC、包括的支援モデル
2. **エンタープライズSaaS**: 「ソフトウェアが世界を食べる」領域への投資・創業
3. **AI/クリプト特化ファンド**: a16zが注力する先端領域

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 生年月日（1971年7月9日） | ✓ | Wikipedia |
| Netscape創業（1994年4月） | ✓ | Wikipedia, Internet History Podcast |
| IPO日（1995年8月9日） | ✓ | Fortune, Yahoo Finance |
| IPO終値（$58.25） | ✓ | 複数ソース |
| AOL買収額（$4.2B） | ✓ | Wikipedia |
| Opsware売却額（$1.6B） | ✓ | Wikipedia, CNN |
| a16z創業日（2009年7月6日） | ✓ | Wikipedia |
| a16z AUM（$46B） | ✓ | Wikipedia（2025年7月時点） |

## 参照ソース

1. [Marc Andreessen - Wikipedia](https://en.wikipedia.org/wiki/Marc_Andreessen)
2. [Netscape - Wikipedia](https://en.wikipedia.org/wiki/Netscape)
3. [Andreessen Horowitz - Wikipedia](https://en.wikipedia.org/wiki/Andreessen_Horowitz)
4. [On The 20th Anniversary - An Oral History of Netscape's Founding | Internet History Podcast](https://www.internethistorypodcast.com/2014/04/on-the-20th-anniversary-an-oral-history-of-netscapes-founding/)
5. [20 Years On: Why Netscape's IPO Was the "Big Bang" of the Internet Era | Internet History Podcast](https://www.internethistorypodcast.com/2015/08/20-years-on-why-netscapes-ipo-was-the-big-bang-of-the-internet-era/)
6. [Marc Andreessen | Biography & Facts | Britannica](https://www.britannica.com/biography/Marc-Andreessen)
7. [Why Software Is Eating the World | Andreessen Horowitz](https://a16z.com/why-software-is-eating-the-world/)
8. [The only thing that matters | pmarchive](https://pmarchive.com/guide_to_startups_part4.html)
9. [A Deep Dive into Andreessen Horowitz's Investment Criteria | Press.farm](https://press.farm/andreessen-horowitzs-investment-criteria/)
10. [The History of Loudcloud: From Thriving to Spiraling | Shortform](https://www.shortform.com/blog/loudcloud/)
11. [Browser wars - Wikipedia](https://en.wikipedia.org/wiki/Browser_wars)
12. [Andreessen Horowitz (a16z) Overview | ByteBridge | Medium](https://bytebridge.medium.com/andreessen-horowitz-a16z-overview-5368fc16e084)
