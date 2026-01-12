---
id: "FOUNDER_076"
title: "Jawed Karim - YouTube"
category: "founder"
tier: "unicorn"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["video-sharing", "pivot", "paypal-mafia", "google-acquisition", "user-generated-content"]

# 基本情報
founder:
  name: "Jawed Karim"
  birth_year: 1979
  nationality: "ドイツ系アメリカ人（バングラデシュ/ドイツ）"
  education: "イリノイ大学アーバナ・シャンペーン校（コンピュータサイエンス学士）、スタンフォード大学（コンピュータサイエンス修士）"
  prior_experience: "PayPal エンジニア（リアルタイム不正検知システム開発）"

company:
  name: "YouTube"
  founded_year: 2005
  industry: "動画共有プラットフォーム"
  current_status: "acquired"
  valuation: "$1.65B（2006年Google買収時）"
  employees: 65  # Google買収時（2006年10月）

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0  # 推定: 正式な顧客インタビューなし、創業者体験とユーザー行動観察で検証
    problem_commonality: 50  # 推定: 2005年時点で米国ブロードバンド普及率50%（Pew Research）
    wtp_confirmed: false
    urgency_score: 8
    validation_method: "創業者自身の課題体験・市場観察"
  psf:
    ten_x_axes:
      - axis: "動画発見容易性"
        multiplier: 100
      - axis: "アップロード簡便性"
        multiplier: 50
      - axis: "共有・埋め込み容易性"
        multiplier: 100
    mvp_type: "prototype"
    initial_cvr: 0  # 無料サービス、CVR概念なし（広告モデル）
    uvp_clarity: 9
    competitive_advantage: "Flash Player活用・埋め込みコード・ユーザーフレンドリーUI"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "cpf_failure"
    original_idea: "動画版出会い系サイト"
    pivoted_to: "汎用動画共有プラットフォーム"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Chad Hurley", "Steve Chen"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia - Jawed Karim"
    - "Wikipedia - History of YouTube"
    - "Rolling Stone - YouTube Origins"
    - "Startup Grind - YouTube Story"
---

# Jawed Karim - YouTube

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Jawed Karim（共同創業者：Chad Hurley、Steve Chen） |
| 生年 | 1979年10月28日 |
| 国籍 | ドイツ系アメリカ人（父：バングラデシュ人研究者、母：ドイツ人科学者） |
| 学歴 | イリノイ大学（CS学士）、スタンフォード大学（CS修士 2007年） |
| 創業前経験 | PayPal エンジニア（リアルタイム不正検知システム設計） |
| 企業名 | YouTube |
| 創業年 | 2005年2月14日 |
| 業界 | 動画共有プラットフォーム |
| 現在の状況 | Googleが2006年11月に16.5億ドルで買収 |
| 評価額/時価総額 | $1.65B（買収時）、現在は推定$300B以上 |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- 2004年2月のスーパーボウルでのジャネット・ジャクソン「ニップルゲート」事件後、オンラインで動画クリップを見つけることが困難だった
- 2004年12月のインド洋津波の映像も同様にオンラインで見つけにくかった
- 創業者3人がシリコンバレーでの夕食中に動画を探す難しさについて議論

**需要検証方法**:
- 創業者自身が体験した課題（動画が見つからない）
- 「ニップルゲート」が2004年・2005年の最も検索されたイベントとなり、オンライン動画への需要が明確に存在

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 正式なインタビューは不明（創業者の個人体験が起点）
- 手法: 創業者自身の課題体験 + 市場観察
- 発見した課題の共通点: オンラインで動画を見つけること・共有することが極めて困難

**3U検証**:
- Unworkable（現状では解決不可能）: 当時の動画共有は技術的に複雑で一般ユーザーには困難
- Unavoidable（避けられない）: ブロードバンド普及で動画コンテンツへの需要が急増
- Urgent（緊急性が高い）: バイラルイベント（ニップルゲート、津波）発生時に動画を見たい需要が爆発

**支払い意思（WTP）**:
- 確認方法: 当初は広告モデルを想定
- 結果: ユーザー獲得優先で無料サービスとして展開

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | YouTubeのソリューション | 倍率 |
|---|------------|-----------------|------|
| 動画発見 | 複数サイト検索・リンク探し | 1つのプラットフォームで検索・閲覧 | 100x |
| アップロード | 技術知識必要・複数フォーマット対応困難 | シンプルなアップロード・自動変換 | 50x |
| 共有 | URLコピー・メール送信 | 埋め込みコード（MySpace等で利用可能） | 100x |
| 視聴 | プラグイン・ダウンロード必要 | Flash Playerでブラウザ内即時再生 | 30x |
| 導入障壁 | 技術知識・専用ソフト必要 | アカウント作成のみ | 50x |

**MVP**:
- タイプ: プロトタイプ（Webプラットフォーム）
- 初期反応: 2005年4月のベータ版公開から数ヶ月で1日30,000視聴
- CVR: 不明

**UVP（独自の価値提案）**:
- 「Broadcast Yourself」- 誰でも動画を世界に発信できる

**競合との差別化**:
- Google Video: 著作権問題で苦戦、商業化に失敗
- MySpace Video: YouTube埋め込み禁止で自滅（ユーザー反発で撤回）
- 差別化要因: 埋め込みコードによるバイラル性、ユーザーフレンドリーなUI

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- 当初は「動画版出会い系サイト」として構想（スローガン: "Tune In, Hook Up"）
- Craigslistで女性に$20-$100の報酬を提示して動画アップロードを依頼
- 最初の5日間で動画アップロードはゼロ

### 3.2 ピボット

- 元のアイデア: 動画版出会い系サイト（Hot or Notの動画版）
- ピボット後: 汎用動画共有プラットフォーム
- きっかけ: 出会い系動画が全く集まらなかったため、あらゆる動画を受け入れる方針に転換
- 学び: 「ユーザーにYouTubeが何であるかを定義させる」という発想

## 4. 成長戦略

### 4.1 初期トラクション獲得

- 2005年4月: ベータ版公開、1日30,000視聴
- 2005年9月: 初の100万視聴動画（ナイキ広告・ロナウジーニョ）
- 2005年12月: 正式ローンチ、1日200万視聴
- 2006年2月: Saturday Night Liveの「Lazy Sunday」で爆発的成長

### 4.2 フライホイール

1. ユーザーが動画をアップロード
2. 埋め込みコードでMySpace等に拡散
3. 視聴者がYouTubeに流入
4. 視聴者がアップローダーに転換
5. より多くのコンテンツが集まる

### 4.3 スケール戦略

- 2006年1月: 1日2,500万視聴
- 2006年3月: 2,500万本の動画、1日20,000アップロード
- 2006年7月: 1日1億視聴、65,000アップロード
- 2006年11月: Googleが$1.65Bで買収

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | Flash Player（動画再生）、MPEG-4 AVC |
| インフラ | 自社サーバー（後にGoogleインフラ） |
| マーケティング | 埋め込みコード（バイラル）、MySpace連携 |
| 資金調達 | Sequoia Capital（2005年11月 $3.5M、2006年4月 $8M） |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **タイミング**: ブロードバンド普及率が臨界点に達し、1Mbps以上で動画ストリーミングが実用的に
2. **技術選択**: Flash Playerの採用でほぼ全てのブラウザで動画再生可能
3. **埋め込み機能**: MySpace等への埋め込みでバイラル拡散
4. **ピボット判断**: 出会い系から汎用プラットフォームへの素早い転換
5. **ユーザー中心**: 「ユーザーに定義させる」という柔軟な姿勢

### 6.2 タイミング要因

- 2005年時点でグローバル平均ダウンロード速度が1Mbpsを超え、動画ストリーミングが実用的に
- Flash Playerの普及率が90%以上
- MySpace等のソーシャルメディアがユーザー生成コンテンツの受け皿として成長

### 6.3 差別化要因

- Google Video: 著作権対応に注力しすぎてユーザー体験が二の次
- MySpace Video: YouTube埋め込み禁止でユーザー反発
- YouTubeはユーザー体験を最優先し、シンプルさを追求

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | ニコニコ動画（2006年）が日本独自に成功 |
| 競合状況 | 3 | YouTube Japan、ニコニコ動画が既に存在 |
| ローカライズ容易性 | 4 | 言語対応は容易だが文化的差異あり |
| 再現性 | 3 | 動画プラットフォームは飽和状態 |
| **総合** | 3.5 | 新規参入は困難だがニッチ特化は可能 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- 創業者自身が体験した課題は最も確実な需要シグナル
- バイラルイベント（ニップルゲート）への大量検索は市場需要の証拠
- 「動画が見つからない」という単純だが普遍的な課題

### 8.2 CPF検証（/validate-cpf）

- 正式なインタビューなしでも創業者体験から課題を特定可能
- ただし出会い系サイトというCPF仮説は外れ、ピボットが必要だった
- ユーザーの行動観察（誰も出会い系動画をアップしない）が重要な検証

### 8.3 PSF検証（/validate-10x）

- 10倍優位性: アップロード・視聴・共有の全てで圧倒的改善
- 埋め込みコードという機能が100倍の共有容易性を実現
- 技術選択（Flash Player）がユニバーサルアクセスを保証

### 8.4 スコアカード（/startup-scorecard）

- ピボット能力: 出会い系失敗から即座に方向転換
- タイミング: ブロードバンド普及という外部要因と完璧に合致
- チーム: PayPal経験者3人の技術力・実行力
- フライホイール: 埋め込み→視聴→アップロードの好循環

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **ニッチ特化型動画プラットフォーム**: 特定業界（料理、DIY、教育等）に特化した動画共有
2. **ローカルコンテンツ発掘プラットフォーム**: 地方のイベント・観光動画の共有・発見
3. **B2B動画ナレッジ共有**: 企業内の動画マニュアル・ナレッジ共有プラットフォーム

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2005年2月14日） | PASS | Wikipedia、複数ソース |
| 買収額（$1.65B） | PASS | Wikipedia、複数ソース |
| 初動画（Me at the zoo）2005年4月23日 | PASS | Wikipedia、YouTube公式 |
| Karimの持株（137,443株・約$64M） | PASS | 複数ソース |
| ピボット（出会い系→汎用） | PASS | Startup Grind、複数ソース |

## 11. Jawed Karim のその後

### YouTube後のキャリア

- 2007年: スタンフォード大学でコンピュータサイエンス修士号取得
- 2008年3月: Y Ventures（旧Youniversity Ventures）設立（Keith Rabois、Kevin Hartzと共同）
- 2009年4月: Airbnbのシードラウンドに最初期の投資家として参加
- 投資先: Palantir、Reddit、Eventbrite等

### 現在の推定資産

- 推定純資産: 約$300M-$400M（2024年時点）
- Google株（株式分割後549,772株）の現在価値は$700M以上と推計される場合も
- 2019年: Chad Hurley、Steve Chenと共にエミー賞（生涯功労賞）受賞

## 参照ソース

1. [Jawed Karim - Wikipedia](https://en.wikipedia.org/wiki/Jawed_Karim)
2. [History of YouTube - Wikipedia](https://en.wikipedia.org/wiki/History_of_YouTube)
3. [YouTube Origin - Rolling Stone](https://www.rollingstone.com/culture/culture-features/youtube-origin-nipplegate-janet-jackson-justin-timberlake-949019/)
4. [YouTube: How a Failed Dating Website Created Success - Startup Grind](https://www.startupgrind.com/blog/youtube-how-a-failed-dating-website-created-success/)
5. [Jawed Karim Success Story - StartupTalky](https://startuptalky.com/jawed-karim-youtube/)
6. [YouTube History Timeline - Office Timeline](https://www.officetimeline.com/blog/youtube-history-timeline)
7. [Y Ventures - Crunchbase](https://www.crunchbase.com/organization/youniversity-ventures)
8. [Jawed Karim - University of Illinois](https://grainger.illinois.edu/alumni/hall-of-fame/Jawed-Karim)
9. [YouTube 20th Anniversary - Tubefilter](https://www.tubefilter.com/2025/02/11/youtube-founded-20-years-ago-february-2005/)
10. [Celebrity Net Worth - Jawed Karim](https://www.celebritynetworth.com/richest-businessmen/business-executives/jawed-karim-net-worth/)
