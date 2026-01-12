---
id: "PIVOT_002"
title: "Steve Chen, Chad Hurley, Jawed Karim - YouTube"
category: "founder"
tier: "pivot"
type: "pivot_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["pivot", "video-sharing", "PayPal-Mafia", "dating-to-platform", "Google-acquisition", "viral-growth"]

# 基本情報
founder:
  name: "Steve Chen, Chad Hurley, Jawed Karim"
  birth_year:
    steve_chen: 1978
    chad_hurley: 1977
    jawed_karim: 1979
  nationality:
    steve_chen: "台湾系アメリカ人"
    chad_hurley: "アメリカ"
    jawed_karim: "ドイツ系アメリカ人"
  education:
    steve_chen: "イリノイ大学アーバナ・シャンペーン校（コンピュータサイエンス、中退）"
    chad_hurley: "インディアナ大学ペンシルベニア校（美術学士）"
    jawed_karim: "イリノイ大学アーバナ・シャンペーン校（コンピュータサイエンス）→ スタンフォード大学大学院"
  prior_experience: "全員がPayPal社員（PayPal Mafia）"

company:
  name: "YouTube"
  founded_year: 2005
  industry: "動画共有プラットフォーム"
  current_status: "acquired"
  valuation: "$1.65B（Google買収額）→ 現在推定$400B以上"
  employees: "創業時3名 → 買収時約65名"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: null
    wtp_confirmed: false
    urgency_score: 8
    validation_method: "MVP実験（デーティングサイトとして5日間運用）"
  psf:
    ten_x_axes:
      - axis: "動画視聴の容易さ"
        multiplier: 10
      - axis: "アップロード・共有の簡便性"
        multiplier: 10
      - axis: "埋め込み機能"
        multiplier: "無限大（競合は提供せず）"
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 10
    competitive_advantage: "Flash技術による即時再生、埋め込み可能なプレイヤー、シンプルなUI"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "cpf_failure"
    original_idea: "動画デーティングサイト（Tune In, Hook Up）"
    pivoted_to: "汎用動画共有プラットフォーム"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Elon Musk（PayPal）", "Peter Thiel（PayPal）", "Max Levchin（PayPal）"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia - YouTube"
    - "Wikipedia - History of YouTube"
    - "Sequoia Capital Podcast - Crucible Moments"
    - "Rolling Stone - YouTube Origins"
---

# Steve Chen, Chad Hurley, Jawed Karim - YouTube

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Steve Chen、Chad Hurley、Jawed Karim |
| 生年 | 1978年（Chen）、1977年（Hurley）、1979年（Karim） |
| 国籍 | 台湾系米国人（Chen）、米国（Hurley）、ドイツ系米国人（Karim） |
| 学歴 | イリノイ大学（Chen、Karim）、インディアナ大学（Hurley） |
| 創業前経験 | 全員PayPal社員（PayPal Mafia） |
| 企業名 | YouTube |
| 創業年 | 2005年2月14日（バレンタインデー） |
| 業界 | 動画共有プラットフォーム |
| 現在の状況 | Google傘下（2006年$1.65Bで買収） |
| 評価額/時価総額 | 買収時$1.65B → 現在推定$400B以上 |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- **Janet Jacksonの「Nipplegate」事件（2004年2月）**: スーパーボウルXXXVIIIのハーフタイムショーで起きた衣装トラブル映像をオンラインで見つけられなかった
- **2004年インド洋大津波**: ニュースで話題になっていた災害映像を簡単に見る方法がなかった
- **HotOrNot.comへの触発**: ユーザーが写真をアップロードして評価するサイトの動画版を構想

**需要検証方法**:
- 当初は「動画版デーティングサイト」として検証
- Craigslistで女性に$20を支払い、自己紹介動画をアップロードしてもらう広告を掲載
- **結果**: 5日間でアップロード数ゼロ → 需要がないことが判明

### 2.2 CPF検証（Customer Problem Fit）

**初期コンセプト「Tune In, Hook Up」の失敗**:
- 実施数: Craigslist広告による募集
- 手法: MVP（動画デーティングサイトのプロトタイプ）
- 発見した課題: デーティング動画をアップロードしたい人がいない

**3U検証（初期コンセプト）**:
- Unworkable（現状では解決不可能）: 動画デーティングは既存サービスで代替可能だった
- Unavoidable（避けられない）: デーティング動画は避けられる課題だった
- Urgent（緊急性が高い）: 緊急性なし

**支払い意思（WTP）**:
- 確認方法: $20のインセンティブを提供
- 結果: インセンティブがあっても参加者ゼロ

**ピボット後の真の課題発見**:
- 「動画を簡単に見つけて視聴したい」という普遍的な課題
- 「自分の動画を簡単に共有したい」という創作者の課題
- 当時の動画サイトは複雑で、Flash viewerのダウンロードやバッファリングが必要だった

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | YouTubeのソリューション | 倍率 |
|---|------------|-----------------|------|
| 視聴開始時間 | 数分のバッファリング、プラグインDL | 即時再生（Flash技術） | 10倍以上 |
| アップロード容易性 | 複雑な手順、ファイル形式制限 | シンプルなUI、自動変換 | 10倍以上 |
| 共有機能 | リンク送信のみ | 埋め込みコード提供 | 無限大 |
| 発見性 | 分散したサイト | 一箇所に集約 | 10倍以上 |
| コスト（視聴者） | 無料 | 無料 | 同等 |

**MVP**:
- タイプ: プロトタイプ（実際に動作する動画共有サイト）
- 初期反応: 最初の動画「Me at the zoo」（2005年4月23日）から急成長
- CVR: 明示的データなし、ただしバイラル成長が検証

**UVP（独自の価値提案）**:
- 「誰でも、どんな動画でも、簡単にアップロード・視聴・共有できる」
- 「Broadcast Yourself」（後のスローガン）

**競合との差別化**:
- **埋め込み機能**: 他社は自社サイトへのトラフィック維持とホスティングコストを理由に提供しなかった
- **Flash技術**: ブラウザ内で即座に再生可能
- **オープン性**: あらゆる動画を受け入れる姿勢

## 3. ピボット詳細

### 3.1 初期の失敗：デーティングサイト「Tune In, Hook Up」

**元のアイデア**:
- HotOrNot.comにインスパイアされた動画デーティングサービス
- スローガン: 「Tune In, Hook Up」（チューンして、つながる）
- 2005年2月14日（バレンタインデー）にドメイン登録

**失敗の詳細**:
- Craigslistで「動画をアップロードしてくれる女性に$20支払う」と広告
- 5日間運用して**アップロード数ゼロ**
- Jawed Karimの証言:「全体的に意味をなさなかった」

### 3.2 ピボットの決断

**きっかけ**:
- 5日間のゼロアップロードという明確な失敗データ
- Steve Chen:「OK、デーティングは忘れよう。あらゆる動画を受け入れよう」

**ピボットの種類**:
- **顧客セグメントピボット**: デーティング相手を探すユーザー → 動画を共有したいすべてのユーザー
- **課題ピボット**: 「理想の相手を見つけたい」→「動画を簡単に共有・視聴したい」
- **ソリューションピボット**: デーティング専用 → 汎用動画プラットフォーム

**学び**:
1. **市場からの即座のフィードバックを受け入れる**: 5日間という短期間で方向転換
2. **技術は維持してユースケースを変える**: 動画アップロード・再生技術はそのまま活用
3. **制約を外すことで市場が見つかる**: 「デーティング動画のみ」という制約を外した

### 3.3 ピボット後の成功要因

**技術的優位性の維持**:
- Adobe Flash技術によるブラウザ内即時再生
- PayPalの埋め込みボタン技術からの着想による「埋め込みコード」機能

**戦略的配布**:
- MySpace（当時2,500万ユーザーの最大SNS）への埋め込み許可
- 他社が避けた「外部サイトへの埋め込み」を積極的に許可
- ホスティングコスト増加と引き換えにブランド認知を獲得

**バイラル成長**:
- 2005年9月: Nike広告（ロナウジーニョ）が初の100万再生動画
- 2005年12月: SNL「Lazy Sunday」がアップロードされ、2日間で200万再生
- 「Lazy Sunday」後、YouTubeのトラフィックが1週間で83%増加

## 4. 成長戦略

### 4.1 初期トラクション獲得

**成長ドライバー**:
1. **MySpace埋め込み戦略**: 当時最大のSNSでの露出
2. **バイラルコンテンツ**: 「Lazy Sunday」がターニングポイント
3. **シンプルさ**: クリックするだけで再生、ドラマなし

**タイムライン**:
- 2005年4月23日: 最初の動画「Me at the zoo」アップロード
- 2005年12月15日: 正式ローンチ（「Lazy Sunday」の2日前）
- 2006年3月: 2,500万本以上の動画、1日2万件の新規アップロード
- 2006年7月: 1日1億再生、6.5万件の新規アップロード

### 4.2 フライホイール

```
動画アップロード増加
        ↓
視聴者増加（コンテンツが豊富に）
        ↓
埋め込み・共有が増加
        ↓
外部サイトからの流入増加
        ↓
クリエイター認知度向上
        ↓
さらにアップロード増加
        ↓
（繰り返し）
```

### 4.3 スケール戦略

**資金調達**:
- Sequoia CapitalからシリーズA $350万（Roelof Botha主導）
- シリーズB $800万（Sequoia Capital）
- Sequoiaの持分30% → 最終的に$4.95億の価値

**Google買収（2006年10月）**:
- 買収額: $16.5億（株式交換）
- ローンチからわずか18ヶ月での買収
- Google Videoとの競争に終止符

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 動画再生 | Adobe Flash Player |
| ホスティング | 自社インフラ → Google Cloud |
| 開発言語 | Python、MySQL |
| 資金調達 | Sequoia Capital |
| 配布 | MySpace埋め込み |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **即座のピボット判断**: 5日間のデータで方向転換を決断
2. **技術的イノベーション**: Flash技術による即時再生と埋め込み機能
3. **ネットワーク効果の活用**: MySpaceへの埋め込みでバイラル成長
4. **シンプルさへのこだわり**: 「クリックで再生」の徹底

### 6.2 タイミング要因

- **ブロードバンド普及期**: 2005年は高速インターネットが一般家庭に普及し始めた時期
- **SNSの台頭**: MySpaceが最盛期で、動画共有のプラットフォームとして最適
- **Flash技術の成熟**: ブラウザ内での動画再生が技術的に可能になった時期
- **バイラルコンテンツの需要**: 「Nipplegate」「津波映像」など、見たい動画がオンラインで見つからない時代

### 6.3 差別化要因

- **埋め込み許可**: 競合が避けた機能を積極的に提供
- **オープンなプラットフォーム**: あらゆる動画を受け入れ
- **クリエイターファースト**: 後のPartner Program（2007年）で収益化を可能に

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本でも動画共有需要は高い（ニコニコ動画が先行） |
| 競合状況 | 2 | YouTubeが既に圧倒的（再現困難） |
| ローカライズ容易性 | 5 | 動画は言語障壁が低い |
| 再現性 | 2 | プラットフォームビジネスは先行者優位 |
| **総合** | 3.5 | ピボット手法・成長戦略は参考になるが、同一事業の再現は困難 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

**YouTubeから学ぶ需要発見**:
- 自分自身の不満から出発（Nipplegate映像が見つからない）
- 既存サービス（HotOrNot）からの着想も有効
- **ただし、着想と検証は別**: デーティング動画の需要は実際にはなかった

### 8.2 CPF検証（/validate-cpf）

**YouTubeから学ぶCPF検証**:
- **5日間ルール**: 短期間で需要がないことを確認し、即座にピボット
- **インセンティブテスト**: $20を提供しても参加者ゼロ = 需要なしの明確なシグナル
- **Craigslist活用**: 低コストで初期ユーザーを募集する手法

### 8.3 PSF検証（/validate-10x）

**YouTubeから学ぶPSF検証**:
- **10倍軸の発見**: 視聴開始時間、共有容易性で圧倒的優位
- **埋め込み機能**: 競合が提供しない機能で「無限大」の優位性
- **シンプルさ**: 「クリックで再生」という究極のUX

### 8.4 スコアカード（/startup-scorecard）

| 評価項目 | YouTubeのスコア | コメント |
|---------|----------------|---------|
| 課題の緊急性 | 8/10 | 動画視聴需要は高かったが「緊急」ではない |
| 市場規模 | 10/10 | グローバル規模、制限なし |
| 10倍優位性 | 10/10 | 技術・UX・機能で圧倒 |
| ピボット柔軟性 | 10/10 | 5日間で方向転換 |
| チーム | 10/10 | PayPal Mafiaの経験とネットワーク |

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **業界特化型動画プラットフォーム**: 医療、法律、教育など特定業界向けの動画共有（YouTubeでは対応しにくいニーズ）
2. **ローカルコンテンツ集約**: 地域のイベント、ニュース、観光動画を集約するプラットフォーム
3. **B2B動画共有**: 社内研修、営業資料など企業向け動画の安全な共有サービス

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2005年2月14日） | PASS | Wikipedia、複数メディア |
| 買収額（$1.65B） | PASS | Wikipedia、Sequoia Capital |
| Lazy Sundayの影響 | PASS | Variety、Hollywood Reporter |
| デーティングサイトからのピボット | PASS | Sequoia Capital Podcast、複数メディア |
| 5日間アップロードゼロ | PASS | Rolling Stone、Feedough |

## 参照ソース

1. [YouTube - Wikipedia](https://en.wikipedia.org/wiki/YouTube)
2. [History of YouTube - Wikipedia](https://en.wikipedia.org/wiki/History_of_YouTube)
3. [YouTube ft. Steve Chen - Crucible Moments | Sequoia Capital](https://sequoiacap.com/podcast/crucible-moments-youtube/)
4. [YouTube Origins: How Nipplegate Created Streaming Site - Rolling Stone](https://www.rollingstone.com/culture/culture-features/youtube-origin-nipplegate-janet-jackson-justin-timberlake-949019/)
5. [This Dating Website Revolutionized The Way We Watch Videos - Feedough](https://www.feedough.com/youtube-history-business-strategy/)
6. [Steve Chen, Chad Hurley, Jawed Karim - YouTube | Founderoo](https://www.founderoo.co/playbooks/steve-chen-chad-hurley-jawed-karim-youtube)
7. [History of YouTube - How it All Began - VdoCipher](https://www.vdocipher.com/blog/history-of-youtube/)
8. ['Lazy Sunday' Turns 10 - Variety](https://variety.com/2015/tv/news/lazy-sunday-10th-anniversary-snl-1201657949/)
9. [Hollywood Flashback: SNL's 'Lazy Sunday' Put YouTube on the Map - Hollywood Reporter](https://www.hollywoodreporter.com/business/digital/hollywood-flashback-snls-lazy-sunday-put-youtube-map-2005-1044829/)
10. [Chad Hurley - Wikipedia](https://en.wikipedia.org/wiki/Chad_Hurley)
11. [Steve Chen - Wikipedia](https://en.wikipedia.org/wiki/Steve_Chen)
12. [Jawed Karim - Wikipedia](https://en.wikipedia.org/wiki/Jawed_Karim)
13. [YouTube rises above video competitors - Phys.org](https://phys.org/news/2006-06-youtube-video-competitors.html)
14. [The Evolution of YouTube Part 1: The Early Years - Digital Marketing Magazine](https://digitalmarketingmagazine.co.uk/social-media-marketing/the-evolution-of-youtube-part-1-the-early-years-2005-2007/4539)
15. [YouTube's Competitors: Why Vimeo & Dailymotion Never Made It - YT Views](https://www.ytviews.in/why-youtubes-competitors-vimeo-dailymotion-failed/)
