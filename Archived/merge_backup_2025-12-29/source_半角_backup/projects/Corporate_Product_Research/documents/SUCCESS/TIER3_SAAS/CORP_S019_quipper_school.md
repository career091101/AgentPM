---
id: "CORP_S019"
title: "Quipper School - リクルート"
category: "corporate_product"
tier: "saas" # TIER3_SAAS
type: "success"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["EdTech", "新興国展開", "M&A", "オンライン教育", "フリーミアム", "B2B2C"]

# 基本情報
product:
  name: "Quipper School / Quipper Video"
  name_ja: "クイッパー・スクール / クイッパー・ビデオ"
  parent_company: "Recruit Holdings"
  division: "リクルート（旧：リクルートマーケティングパートナーズ）"
  launched_year: 2010
  industry: "教育テクノロジー（EdTech）"
  current_status: "active" # 2021年組織再編後も海外では継続運営
  revenue: "非公開（リクルートHD統合後は単体開示なし）"
  valuation: "約47.7億円（買収時）"
  users: 300 # 万人（生徒）、教師20万人以上

# M&A情報
acquisition:
  occurred: true
  acquisition_year: 2015
  acquisition_price: "$40M（約47.7億円）"
  founder: "渡辺雅之（Masayuki Watanabe）"
  original_company: "Quipper Limited（英国・ロンドン）"
  integration_status: "success" # 2021年組織再編で各国現地法人化

# リクルート撤退基準（失敗事例のみ）
withdrawal:
  occurred: false
  withdrawal_year: null
  duration_months: null
  reason: ""
  three_year_profitability: null
  five_year_cumulative_loss: null
  final_status: ""

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null # 具体的数値は非公開
    problem_commonality: 75 # インドネシアでは高校生700万人中75%が塾・予備校利用不可
    wtp_confirmed: true # 月額500円程度のQuipper Videoが受け入れられた
    urgency_score: 8 # 教育格差は新興国で深刻な社会課題
    validation_method: "新興国市場での実地調査、教師へのヒアリング、学校訪問営業"
  psf:
    ten_x_axes:
      - axis: "コスト"
        multiplier: 10 # 従来の塾・予備校と比較して月額500円は1/10以下
      - axis: "アクセス性"
        multiplier: 10 # オンラインで地方・農村部からもアクセス可能
      - axis: "スケーラビリティ"
        multiplier: 100 # デジタルプラットフォームで一気に数百万ユーザーに展開
    mvp_type: "concierge + landing_page" # 無料版Quipper Schoolで教師を獲得→有料版Quipper Videoへ誘導
    initial_cvr: null # 具体的数値は非公開（フリーミアムモデル）
    uvp_clarity: 9 # "教育格差解消"という明確なミッション
    competitive_advantage: "新興国特化のローカライズ、無料教師向けツールによるネットワーク効果、リクルートの営業力"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: ""
    original_idea: "オンライン教育プラットフォーム"
    pivoted_to: ""

# リクルート製品特有フィールド
recruit_specific:
  leveraged_assets:
    - asset_type: "営業網"
      description: "スタディサプリで培った学校訪問営業ノウハウを海外展開。インドネシアで営業チーム500人まで拡大"
    - asset_type: "ブランド"
      description: "リクルートの企業信頼性を活用し、政府・教育機関との連携を促進"
    - asset_type: "データベース"
      description: "スタディサプリの教育コンテンツ制作・配信ノウハウを移植"
    - asset_type: "プラットフォーム"
      description: "日本の受験サプリ（後のスタディサプリ）のマネタイズモデル（月額980円→現地では500円）を適用"
  synergy_with_existing:
    - business: "スタディサプリ"
      synergy_type: "データ連携・ノウハウ共有"
      description: "動画配信技術、マネタイズモデル、営業手法を相互活用。2021年以降は技術基盤を統合"
    - business: "リクルート全社"
      synergy_type: "ブランド共鳴"
      description: "リクルートの「個人の可能性を最大化する」理念と教育格差解消ミッションが合致"
  internal_resistance: "特筆すべき記載なし。創業者渡辺氏とリクルート側のビジョン・価値観が一致していたため円滑に統合"

# クロスリファレンス
cross_reference:
  founder_id: "N/A" # 渡辺雅之は本調査対象外（DeNA共同創業者としては別途調査対象の可能性あり）
  related_products: ["スタディサプリ（国内）", "受験サプリ（スタディサプリの前身）"]
  competitor_products: ["Coursera", "Khan Academy", "Udemy", "Ruangguru（インドネシア）"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "リクルート公式ブログ（教育格差解消目指すQuipper）"
    - "Business Insider Japan（リクルートの仕組みが海外でも圧倒的成長を果たす理由）"
    - "Quipper Japan公式（組織再編に関するお知らせ）"
    - "マールオンライン（M&A速報）"
    - "EdTech Media（買収報道）"
    - "NewsPicks（渡辺雅之インタビュー）"
---

# Quipper School / Quipper Video

## 1. 基本情報

| 項目 | 内容 | ソース |
|------|------|--------|
| 製品名 | Quipper School（教師向け）/ Quipper Video（生徒向け） | [EdTech Media](https://edtech-media.com/archives/5441) |
| 運営企業 | リクルートホールディングス（2015年買収、2021年組織再編） | [Quipper Japan公式](https://www.quipper.com/jp/news/759/) |
| 事業部 | リクルート（旧：リクルートマーケティングパートナーズ） | [マールオンライン](https://www.marr.jp/genre/topics/news/entry/30846) |
| ローンチ年 | 2010年（ロンドン） | [Crunchbase](https://www.crunchbase.com/person/masayuki-watanabe) |
| 撤退年（該当時） | なし（2021年組織再編で英国法人は清算、海外現地法人は継続） | [Quipper Japan公式](https://www.quipper.com/jp/news/759/) |
| 買収年（M&A時） | 2015年4月1日 | [起業tv](https://kigyotv.jp/news/quipper/) |
| 買収額 | 約47.7億円（$40M） | [EdTech Media](https://edtech-media.com/archives/5441), [The Bridge](https://thebridge.jp/en/2015/07/quipper-acquired-by-recruit-holdings) |
| 現在の状況 | active（インドネシア・フィリピンで継続運営中、2024年も活動確認） | [Quipper Blog Indonesia](https://www.quipper.com/id/blog/quipper-land/quipper-info/quipper-championship-2023-2024-mengejar-keunggulan-membuktikan-potensi-dan-menggapai-prestasi/) |
| ピークユーザー数 | 生徒300万人以上、教師20万人以上（8カ国展開時） | [リクルート公式](https://www.recruit.co.jp/blog/service/20180820_150.html) |

## 2. 製品開発ストーリー

### 2.1 課題発見

**着想源**:
- 創業者の渡辺雅之氏は京都大学在学中に20カ国以上の途上国を訪問し、難民支援NPO活動に参加
- 経済格差と教育問題に強い関心を持つようになる
- マッキンゼー、DeNA共同創業（1999年）を経て、2010年に英国ロンドンでQuipper創業
- フィリピン、インドネシアなど新興国では都市部と地方・農村部で教育インフラに大きな格差
- インドネシアでは高校生約700万人のうち75%が経済的・地域的理由で塾・予備校を利用できず

**Ring提案制度**（該当時）:
- 該当なし（外部企業をM&Aで買収）

### 2.2 CPF検証（orchestrate-phase1基準）

**CPF達成判定**:

| 指標 | 目標 | 実績 | 判定 | エビデンス |
|------|------|------|:----:|----------|
| インタビュー数 | 20人以上 | 数千校訪問 | ✅ | インドネシアで7,000校訪問、フィリピンで1,300校導入 |
| 課題共通率 | 70%以上 | 75% | ✅ | インドネシア高校生の75%が塾・予備校利用不可 |
| WTP確認 | 50%以上 | 高い | ✅ | 月額500円のQuipper Videoが広く受け入れられた |
| 緊急性 | 7/10以上 | 8/10 | ✅ | 政府が教育改革を国家課題と位置づけ、COVID-19で急速に需要拡大 |

**総合判定**: ✅ CPF達成

**検証手法**:
- 新興国市場での実地調査と学校訪問営業（地道な足腰のアプローチ）
- 教師向け無料ツール「Quipper School」を先行提供し、教育現場のペインポイントを収集
- フィリピン、インドネシア、メキシコで段階的に展開し、各国のニーズを検証
- 2015年時点でインドネシアでの検索ワードランキング4位を獲得するほど認知度が向上

### 2.3 PSF検証（10倍優位性）

**10倍優位性の検証**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 | エビデンス |
|---|------------|-----------------|------|----------|
| コスト | 月額数千円〜数万円の塾・予備校 | 月額500円のQuipper Video | 10x | インドネシア・フィリピンでの価格設定 |
| アクセス性 | 都市部に限定された塾・予備校 | オンラインでどこからでもアクセス可能 | 10x | 地方・農村部の生徒も利用可能に |
| スケーラビリティ | 物理的教室の制約 | デジタルで数百万人に同時提供 | 100x | 約2年で生徒300万人、教師20万人に拡大 |

**達成軸数**: 3軸（目標2軸以上）
**PSF達成判定**: ✅ 達成

**MVP**:
- タイプ: Concierge + Landing Page + Freemium
- 初期アプローチ: 教師向け無料ツール「Quipper School」を先行提供し、宿題・課題管理を効率化
- 生徒向け有料サービス「Quipper Video」へ誘導するフリーミアムモデル
- 初期反応: 2014年立ち上げから約2年で生徒300万人、教師20万人に拡大

**UVP**:
- "世界中のどこにいても質の高い教育を受けられる"
- 教師向け無料ツールで学校を取り込み、生徒向け有料動画で収益化
- 各国カリキュラムに完全対応したローカライズコンテンツ
- 現地のカリスマ講師による動画授業（月額500円）

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- **マネタイズの課題**: 買収当時（2015年）、フィリピンとインドネシアで無料サービスを展開していたがマネタイズができていなかった
- **組織力の不足**: 営業力、マーケティング力といった組織力が課題だった
- **リクルート買収により解決**: スタディサプリの月額980円モデルを適用し、現地では月額500円でマネタイズに成功

### 3.2 ピボット（該当する場合）

- 元のアイデア: -（該当なし）
- ピボット後: -
- きっかけ: -
- 学び: 無料ツールでネットワーク効果を生み出し、有料サービスへ転換するフリーミアムモデルの有効性

### 3.3 リクルート撤退基準の検証（失敗事例のみ）

該当なし（成功事例）

## 4. 成長戦略

### 4.1 初期トラクション

- 2010年ロンドンで創業
- 2014年にオンラインラーニングプラットフォーム「Quipper School」をグローバル展開開始
- 約2年で生徒会員約300万人、教師会員約20万人へと成長
- 2015年、インドネシアで検索ワードランキング年間4位を獲得
- フィリピン、インドネシアで圧倒的な急成長

### 4.2 フライホイール

```
教師向け無料ツール提供
    ↓
学校・教師の利用拡大
    ↓
生徒への認知度向上
    ↓
生徒が有料動画サービスに登録
    ↓
収益でコンテンツ拡充
    ↓
さらに教師・学校が増える
    ↓（ループ）
```

- **ネットワーク効果**: 教師が増えるほど生徒も増え、生徒が増えるほど教師も増える
- **政府連携**: インドネシア政府がジャカルタ市の推奨オンライン教育サービスに認定（2020年COVID-19対応）
- **ブランド効果**: フィリピンで「国家の歴史上、最大の教育改革」のサポートと位置づけ

### 4.3 スケール戦略

- **地道な営業活動**: リクルートの営業力を活用し、インドネシアで営業チーム500人まで拡大
- **ローカライズの徹底**: 各国のカリキュラムに合わせたコンテンツ制作、現地カリスマ講師の起用
- **B2B2Cモデル**: 学校・教師を経由して生徒にリーチ
- **マルチプロダクト展開**: Quipper School（教師向け）とQuipper Video（生徒向け）の2本柱

### 4.4 リクルート資産の活用

**活用した既存資産**:

| 資産タイプ | 具体的な活用方法 | 効果 |
|----------|---------------|------|
| 営業網 | スタディサプリで培った学校訪問営業ノウハウを海外展開。インドネシアで営業チーム500人規模に拡大 | 短期間で数千校への導入実現 |
| ブランド | リクルートの企業信頼性を活用し、政府・教育機関との連携を促進 | インドネシア政府認証、フィリピン政府連携 |
| データベース | スタディサプリの教育コンテンツ制作・配信ノウハウを移植 | 高品質な動画コンテンツの短期間での制作 |
| プラットフォーム | 日本の受験サプリのマネタイズモデル（月額980円→現地では500円）を適用 | マネタイズの早期実現 |

**既存事業とのシナジー**:

| 既存事業 | シナジータイプ | 具体的な連携 |
|---------|-------------|------------|
| スタディサプリ | データ連携・ノウハウ共有 | 動画配信技術、マネタイズモデル、営業手法を相互活用。2021年以降は技術基盤を統合 |
| リクルート全社 | ブランド共鳴 | リクルートの「個人の可能性を最大化する」理念と教育格差解消ミッションが合致 |

## 5. M&A戦略（該当時）

### 5.1 買収理由

1. **共通のビジョン**: 「教育環境格差の解消」という共通テーマでビジョン・価値観が一致
2. **エンジニアリング能力の強化**: スタディサプリのインタラクティブ化に必要なエンジニアリング能力を獲得
3. **海外展開の加速**: 既にフィリピン、インドネシアで展開していたQuipperを買収し、海外市場への即座の参入
4. **タイミング**: 2015年時点でQuipperはインドネシアで検索ワード年間4位を獲得するほど認知度が高く、成長の兆しが明確

### 5.2 統合プロセス

- **2015年4月**: リクルートマーケティングパートナーズがQuipper Limitedを47.7億円で買収
- **2015年〜2020年**: 日本ではスタディサプリと技術・ノウハウを共有、海外ではQuipperブランドで展開
- **2021年4月**: リクルートマーケティングパートナーズがリクルート本体に統合
- **2021年10月**: Quipper Limited（英国法人）を組織再編により清算
  - 日本事業: リクルート本体へ吸収
  - フィリピン事業: Quipper Philippines Inc.（新設100%子会社）へ移管
  - インドネシア事業: PT Quipper Edukasi Indonesia（100%子会社化）へ移管
- **目的**: 現地に根ざしたスピーディーな意思決定と事業運営の強化

### 5.3 シナジー効果

1. **ノウハウの相互活用**: スタディサプリの受験ノウハウ、動画制作技術をQuipper Videoに移植
2. **営業力の展開**: スタディサプリで100人の営業担当が全国5,000校を訪問した手法を海外展開
3. **マネタイズの実現**: 買収前は無料サービスのみだったが、月額500円の有料モデルで収益化
4. **技術基盤の統合**: 2021年以降、スタディサプリ/Quipperで技術基盤を統合し、開発効率を向上

## 6. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | AWS（Gravitonへ移行）、モバイルアプリ（iOS/Android） |
| 配信 | 動画ストリーミング技術、CDN |
| 分析 | 学習データ分析、教師向けダッシュボード |
| マーケティング | SEO（インドネシアで検索ワード4位）、学校訪問営業 |

## 7. 成功/失敗要因分析

### 7.1 主要成功要因（成功時）

1. **明確なミッション**: 教育格差解消という社会課題に対する強いコミットメント
2. **フリーミアムモデル**: 教師向け無料ツールでネットワーク効果を生み出し、生徒向け有料サービスで収益化
3. **ローカライズの徹底**: 各国カリキュラムに完全対応、現地カリスマ講師の起用、現地目線のオペレーション
4. **リクルートの営業力**: 地道な学校訪問営業で短期間に数千校への導入実現
5. **政府連携**: インドネシア政府認証、フィリピン政府との連携により信頼性向上
6. **タイミング**: COVID-19によるオンライン教育需要の急拡大に対応

## 8. orchestrate-phase1への示唆

### 8.1 /discover-demand への学び

- **新興国市場の課題発見**: 先進国では当たり前の教育インフラが新興国では不足している点に着目
- **75%という高い課題共通率**: インドネシア高校生の75%が塾・予備校を利用できないという明確なデータ
- **政府レベルの緊急性**: 国家課題として教育改革が位置づけられている

### 8.2 /validate-cpf への学び

- **地道な学校訪問**: 数千校を訪問し、教師・学校のペインポイントを直接ヒアリング
- **無料ツールでの検証**: Quipper Schoolを無料提供し、教師の課題（宿題・課題管理の負担）を検証
- **段階的展開**: フィリピン→インドネシア→メキシコと段階的に展開し、各国でCPFを検証

### 8.3 /validate-10x への学び

- **コスト10倍**: 従来の塾・予備校と比較して月額500円は1/10以下のコスト
- **アクセス性10倍**: オンラインで地方・農村部からもアクセス可能
- **スケーラビリティ100倍**: デジタルプラットフォームで一気に数百万ユーザーに展開
- **3軸での10倍達成**: コスト、アクセス性、スケーラビリティの3軸で10倍以上の優位性を実現

### 8.4 /startup-scorecard への学び

- **フリーミアムモデルの有効性**: 無料ツールでネットワーク効果を生み出し、有料サービスへ転換
- **B2B2Cの威力**: 学校・教師を経由して生徒にリーチすることで信頼性と普及速度を向上
- **ローカライズの重要性**: 各国の文化・カリキュラムに徹底的に適応することが成功の鍵
- **M&A後の統合**: リクルートのリソース（営業力、ブランド、ノウハウ）を活用しつつ、現地目線を維持

## 9. 他業界適用性

| 業界 | 適用可能性 | コメント |
|------|----------|---------|
| 医療・ヘルスケア | 高 | 新興国での医療格差解消、オンライン診療・遠隔医療に応用可能 |
| 金融・フィンテック | 高 | 銀行口座を持たない層へのマイクロファイナンス、モバイル決済 |
| 農業・アグリテック | 中 | 農業技術のオンライン教育、IoTセンサーによる遠隔農業支援 |
| 人材・キャリア教育 | 高 | 新興国での職業訓練、スキルアップ支援 |

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| ローンチ年（2010年） | ✅ | [Crunchbase](https://www.crunchbase.com/person/masayuki-watanabe), [Wikipedia](https://en.wikipedia.org/wiki/Quipper_(company)) |
| 買収額（47.7億円/$40M） | ✅ | [EdTech Media](https://edtech-media.com/archives/5441), [The Bridge](https://thebridge.jp/en/2015/07/quipper-acquired-by-recruit-holdings) |
| 買収年（2015年4月） | ✅ | [起業tv](https://kigyotv.jp/news/quipper/), [リクルート公式](https://www.recruit.co.jp/blog/service/20180820_150.html) |
| ユーザー数（生徒300万人、教師20万人） | ✅ | [リクルート公式](https://www.recruit.co.jp/blog/service/20180820_150.html), [NewsPicks](https://newspicks.com/news/1863914/body/) |
| 組織再編（2021年10月） | ✅ | [Quipper Japan公式](https://www.quipper.com/jp/news/759/), [マールオンライン](https://www.marr.jp/genre/topics/news/entry/30846) |
| 現在も運営中（2024年） | ✅ | [Quipper Blog Indonesia](https://www.quipper.com/id/blog/quipper-land/quipper-info/quipper-championship-2023-2024-mengejar-keunggulan-membuktikan-potensi-dan-menggapai-prestasi/), [Technophile](https://technophileph.com/2023/03/19/quipper-revolutionizes-education-through-edtech-and-ai/) |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [リクルート公式ブログ - 教育格差解消目指すQuipper](https://www.recruit.co.jp/blog/service/20180820_150.html)
2. [Business Insider Japan - リクルートの仕組みが海外でも圧倒的成長を果たす理由](https://www.businessinsider.jp/post-105603)
3. [Quipper Japan公式 - 組織再編に関するお知らせ](https://www.quipper.com/jp/news/759/)
4. [マールオンライン - リクルートHD傘下Quipper社、組織再編を実施し清算へ](https://www.marr.jp/genre/topics/news/entry/30846)
5. [EdTech Media - リクルート、Quipperを約48億円で買収](https://edtech-media.com/archives/5441)
6. [起業tv - リクルートが47.7億円で買収！Quipperとは？](https://kigyotv.jp/news/quipper/)
7. [The Bridge - Japan's Recruit Holdings acquires UK-based edutech startup Quipper for $40M](https://thebridge.jp/en/2015/07/quipper-acquired-by-recruit-holdings)
8. [NewsPicks - 7カ国で生徒は300万人。リクルートは教育市場でも勝てるのか](https://newspicks.com/news/1863914/body/)
9. [リクルート公式 - やる気最大化の仕組みで成長したQuipperインドネシア](https://www.recruit.co.jp/blog/service/20180824_151.html)
10. [スタディサプリBRAND SITE - インドネシア政府が推奨オンライン教育サービスに認定](https://brand.studysapuri.jp/casestudy/article/quipper-b2b-indonesia-casestudy-public-introduction-jakarta/)
11. [Quipper Blog Indonesia - Quipper Championship 2023/2024](https://www.quipper.com/id/blog/quipper-land/quipper-info/quipper-championship-2023-2024-mengejar-keunggulan-membuktikan-potensi-dan-menggapai-prestasi/)
12. [Crunchbase - Masayuki Watanabe Profile](https://www.crunchbase.com/person/masayuki-watanabe)
