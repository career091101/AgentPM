---
id: "FOUNDER_077"
title: "Chad Hurley - YouTube"
category: "founder"
tier: "unicorn"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["video-sharing", "platform", "paypal-mafia", "google-acquisition", "pivot"]

# 基本情報
founder:
  name: "Chad Hurley"
  birth_year: 1977
  nationality: "アメリカ"
  education: "Indiana University of Pennsylvania（美術学士、1999年）"
  prior_experience: "PayPal（UIデザイナー、ロゴデザイン担当）"

company:
  name: "YouTube"
  founded_year: 2005
  industry: "動画共有プラットフォーム / オンラインメディア"
  current_status: "acquired"
  valuation: "$1.65B（買収時）/ 現在$550B相当"
  employees: 65（買収時）

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0  # 推定: 正式な顧客インタビューなし、プロトタイプで検証
    problem_commonality: 50  # 推定: 2005年時点で米国ブロードバンド普及率50%（Pew Research）
    wtp_confirmed: false  # 無料サービスとして開始（広告モデル）
    urgency_score: 8  # ブロードバンド普及期、SNS台頭による動画需要急増
    validation_method: "プロトタイプ・ユーザー観察"
  psf:
    ten_x_axes:
      - axis: "使いやすさ"
        multiplier: 10
      - axis: "アクセシビリティ"
        multiplier: 10
      - axis: "共有容易性"
        multiplier: 10
    mvp_type: "prototype"
    initial_cvr: 0  # 無料サービス、CVR概念なし（広告モデル）
    uvp_clarity: 9
    competitive_advantage: "Flashベース動画再生、埋め込み機能、無料ホスティング"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "cpf_failure"
    original_idea: "動画デートサイト（Tune In, Hook Up）"
    pivoted_to: "汎用動画共有プラットフォーム"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Steve Chen", "Jawed Karim"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia - Chad Hurley"
    - "Wikipedia - YouTube"
    - "TechCrunch"
    - "Fortune"
    - "Startup Archive"
---

# Chad Hurley - YouTube

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Chad Hurley（チャド・ハーリー） |
| 生年 | 1977年1月24日 |
| 国籍 | アメリカ（ペンシルベニア州バーズボロ出身） |
| 学歴 | Indiana University of Pennsylvania 美術学士（1999年） |
| 創業前経験 | PayPal UIデザイナー（PayPalロゴをデザイン） |
| 企業名 | YouTube |
| 創業年 | 2005年2月 |
| 業界 | 動画共有プラットフォーム |
| 現在の状況 | 2006年Google買収（$1.65B） |
| 評価額/時価総額 | 買収時$1.65B / 現在$550B相当 |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- 2005年初頭、Steve Chenのアパートでのディナーパーティーで撮影した動画を共有しようとした際、ファイルサイズが大きすぎてメール添付できず、ウェブへのアップロードにも何時間もかかるという問題に直面
- 当時、オンラインで動画を簡単に共有する方法が存在しなかった
- 注：Jawed Karimはこのディナーパーティーの話は「マーケティング用に作られた消化しやすいストーリー」と後に証言

**需要検証方法**:
- PayPal時代の同僚（Steve Chen、Jawed Karim）との議論
- 初期は動画デートサイト「Tune In, Hook Up」として構想
- ユーザーが動画プロフィールをアップロードして出会いを見つけるサービス

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 公式な顧客インタビュー数は不明
- 手法: プロトタイプによる実験的検証
- 発見した課題の共通点: 動画共有の困難さは広範な問題だった

**3U検証**:
- Unworkable（現状では解決不可能）: 当時の動画共有は技術的に非常に困難。ファイル形式の互換性、帯域幅、再生環境の問題
- Unavoidable（避けられない）: インターネットの普及とともに動画コンテンツ需要は必然的に増加
- Urgent（緊急性が高い）: ブロードバンド普及により動画消費への欲求が高まっていた

**支払い意思（WTP）**:
- 確認方法: 無料サービスとして開始（広告モデル）
- 結果: ユーザーは無料で動画をアップロード・視聴する意思があることを確認

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | YouTubeソリューション | 倍率 |
|---|------------|-----------------|------|
| アップロード時間 | 数時間 | 数分 | 10x+ |
| 共有方法 | メール添付（サイズ制限） | URL共有・埋め込み | 10x+ |
| 再生互換性 | プラグイン依存 | Flash（普及率95%+） | 10x+ |
| コスト | サーバー費用必要 | 完全無料 | 無限大 |
| 導入障壁 | 技術知識必要 | ワンクリック | 10x+ |

**MVP**:
- タイプ: Flashベースの動画共有プロトタイプ
- 初期反応: 2005年4月23日に最初の動画「Me at the zoo」をJawed Karimがアップロード
- CVR: 2005年12月時点で1日800万視聴達成

**UVP（独自の価値提案）**:
- 「誰でも簡単に動画をアップロード・共有・埋め込みできる」
- ブラウザさえあれば追加ソフト不要で動画再生可能

**競合との差別化**:
- 埋め込みコード提供（他サイトは自社トラフィック維持のため避けていた）
- Flash Playerによるブラウザ互換性（95%以上のPCで再生可能）
- ファイル形式の自動変換（ユーザーは形式を気にする必要なし）

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- 当初の動画デートサイト「Tune In, Hook Up」構想は完全に失敗
- Jawed Karimの証言：「実際のデート動画を集めるのに必死で、Craigslistに頼るほどだった」
- 動画デートサービスとしてのトラクションは皆無

### 3.2 ピボット（該当する場合）

- 元のアイデア: 動画デートサイト「Tune In, Hook Up」（2005年2月、バレンタインデーにドメイン登録）
- ピボット後: 汎用動画共有プラットフォーム「YouTube」
- きっかけ: 動画デートへの需要がないことを認識し、より広い用途の動画共有に転換
- 学び: 特定用途に限定せず、ユーザーが自由に使えるプラットフォームの方が成長ポテンシャルが高い

## 4. 成長戦略

### 4.1 初期トラクション獲得

- **MySpace連携**: 2005年当時2,500万ユーザーを誇るMySpaceで動画埋め込みを可能に
- MySpaceはYouTubeトラフィックの20%以上を供給
- **埋め込み機能のバイラル効果**: PayPalで学んだ「ウェブサイトへの埋め込みボタン」戦略を動画に応用
- **SNL「Lazy Sunday」効果**: 2005年12月のSNL動画がYouTubeで200万回以上再生され、週間トラフィック83%増加

### 4.2 フライホイール

1. ユーザーが動画をアップロード
2. 埋め込みコードで他サイト（MySpace等）に拡散
3. 視聴者がYouTubeを発見
4. 新規ユーザーとして動画をアップロード
5. さらなる拡散...（繰り返し）

### 4.3 スケール戦略

- 2005年5月: ベータ版ローンチ
- 2005年12月: 1日800万視聴達成
- 2006年7月: 1日1億視聴達成（オンライン動画視聴の60%を占有）
- 2006年10月: Google $1.65Bで買収
- 買収時従業員数: わずか65名

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 動画技術 | Macromedia Flash Player（FLV形式） |
| インフラ | 自社サーバー（買収時65名で運用） |
| マーケティング | MySpace連携、埋め込みコード配布 |
| 資金調達 | Sequoia Capital（$11.5M調達） |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **PayPal経験の活用**: 埋め込み可能なウィジェット戦略をPayPalから学び、動画埋め込みに応用
2. **技術的優位性**: Flash Playerの普及率を活用し、追加インストール不要の視聴体験を実現
3. **ピボットの判断力**: 動画デートサイトが失敗と判断し、迅速に汎用プラットフォームへ転換
4. **ユーザーファースト**: 他社が避けた埋め込み機能を無料提供し、ブランド認知を優先

### 6.2 タイミング要因

- ブロードバンド普及率の急上昇（2005年時点で米国家庭の約50%）
- MySpaceなどSNSの台頭によるユーザー生成コンテンツ需要
- Flash Playerの95%以上のPC普及率
- デジタルカメラ・カムコーダーの一般化

### 6.3 差別化要因

- 競合が恐れた「埋め込み」を積極採用
- ファイル形式を気にせずアップロード可能
- 完全無料のホスティング・帯域幅提供
- シンプルなUI（Chad Hurleyのデザイン経験活用）

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本でもYouTubeは圧倒的シェア |
| 競合状況 | 2 | ニコニコ動画など独自プラットフォーム存在 |
| ローカライズ容易性 | 4 | 動画プラットフォームは言語依存度低い |
| 再現性 | 2 | 動画ホスティングのインフラコストが障壁 |
| **総合** | 3.25 | プラットフォーム型は資本力必要 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- 自身の体験から課題を発見（動画共有の困難さ）
- 初期仮説（動画デート）が失敗しても、根本課題（動画共有）は有効だった
- **教訓**: 課題の抽象度を上げることで、より大きな市場を発見できる

### 8.2 CPF検証（/validate-cpf）

- 正式なインタビューより、実際のプロトタイプで検証
- 動画デートサイトの失敗から「特定用途限定」の危険性を学習
- **教訓**: 早期に実物で検証し、需要がなければ素早くピボット

### 8.3 PSF検証（/validate-10x）

- 10倍優位性: アップロード時間、共有容易性、再生互換性で圧倒的優位
- MVP: Flash動画プレイヤー + 埋め込みコード
- **教訓**: 技術的優位性（Flash普及率活用）と戦略的優位性（埋め込み許可）の組み合わせ

### 8.4 スコアカード（/startup-scorecard）

| 項目 | 評価 | 理由 |
|------|------|------|
| 市場規模 | 10/10 | 全インターネットユーザーが対象 |
| 課題深刻度 | 8/10 | 動画共有は当時非常に困難 |
| 解決策優位性 | 10/10 | 複数軸で10倍以上の改善 |
| チーム | 9/10 | PayPal出身、デザイン+技術+ビジネス |
| タイミング | 10/10 | ブロードバンド普及、SNS台頭 |

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **企業向け動画ナレッジベース**: 社内動画を簡単に共有・検索できるB2Bプラットフォーム（YouTube的UXで社内研修・ナレッジ共有）

2. **縦型動画編集・共有プラットフォーム**: TikTok/Reels時代の縦型動画に特化した、日本語UIの編集・投稿ツール

3. **ニッチ特化型動画コミュニティ**: 特定業界（医療、建設、農業等）向けの動画共有+Q&Aプラットフォーム

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2005年） | PASS | Wikipedia、複数メディア |
| 買収額（$1.65B） | PASS | Google公式、複数メディア |
| 1日1億視聴（2006年7月） | PASS | Wikipedia History of YouTube |
| 動画デートサイトからのピボット | PASS | Startup Archive、複数インタビュー |

## 11. Chad Hurley のその後

### YouTube後の活動
- 2010年: YouTubeのCEOを退任（アドバイザーとして継続）
- 2011年: Steve Chenと共にAVOS Systems設立（Delicious買収）
- 2013年: MixBit（モバイル動画編集アプリ）ローンチ
- 2018年: MixBitをBlueJeansに売却
- 2019年: GreenPark Sports共同創業（ライブファンタジースポーツ）

### 投資活動
- Golden State Warriors（NBA）のマイノリティオーナー（2010年〜、4回の優勝）
- Los Angeles Football Club（MLS）のマイノリティオーナー（2014年〜）

### 現在の純資産
- 推定$700M（2025年時点）

## 参照ソース

1. [Wikipedia - Chad Hurley](https://en.wikipedia.org/wiki/Chad_Hurley)
2. [Wikipedia - YouTube](https://en.wikipedia.org/wiki/YouTube)
3. [Wikipedia - History of YouTube](https://en.wikipedia.org/wiki/History_of_YouTube)
4. [Startup Archive - YouTube Virality Hack](https://www.startuparchive.org/p/youtube-founder-chad-hurley-explains-the-virality-hack-he-stole-from-paypal)
5. [Fortune - YouTube Founders Sale](https://fortune.com/2025/07/25/youtube-cofounders-chad-hurley-steven-chen-sold-google-net-millions-but-now-worth-over-500-billion/)
6. [TechCrunch - YouTube Co-Founders Split](https://techcrunch.com/2014/06/06/youtube-co-founders-break-up-as-chad-hurley-spins-out-his-own-company-and-steve-chen-joins-google-ventures/)
7. [The Fact Base - YouTube Dating Site Origin](https://thefactbase.com/youtube-was-originally-launched-as-a-dating-site-its-slogan-was-tune-in-hook-up/)
8. [Hollywood Reporter - Lazy Sunday YouTube](https://www.hollywoodreporter.com/business/digital/hollywood-flashback-snls-lazy-sunday-put-youtube-map-2005-1044829/)
9. [Tubefilter - Me at the Zoo 20 Years](https://www.tubefilter.com/2025/04/23/20-years-youtube-me-at-the-zoo-2005-jawed-karim/)
10. [Business of Apps - YouTube Statistics](https://www.businessofapps.com/data/youtube-statistics/)
11. [Celebrity Net Worth - Chad Hurley](https://www.celebritynetworth.com/richest-businessmen/ceos/chad-hurley-net-worth/)
12. [Bizcommunity - 20 Years of YouTube Innovations](https://www.bizcommunity.com/article/20-years-of-youtube-8-key-innovations-that-have-helped-the-video-platform-achieve-its-success-032985a)
