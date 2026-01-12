---
id: "FOUNDER_064"
title: "Emmett Shear - Twitch"
category: "founder"
tier: "unicorn"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["live-streaming", "gaming", "pivot", "Y Combinator", "Amazon acquisition"]

# 基本情報
founder:
  name: "Emmett Shear"
  birth_year: 1983
  nationality: "アメリカ"
  education: "Yale大学 コンピュータサイエンス学部卒業（2005年）"
  prior_experience: "Kiko Calendar共同創業者、Justin.tv共同創業者"

company:
  name: "Twitch"
  founded_year: 2011
  industry: "ライブストリーミング / ゲーム配信"
  current_status: "acquired"
  valuation: "$970M（Amazon買収時）"
  employees: null

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: null
    wtp_confirmed: true
    urgency_score: 8
    validation_method: "ユーザー電話インタビュー、データ分析、自身のゲーマー体験"
  psf:
    ten_x_axes:
      - axis: "ゲーマー特化のUX"
        multiplier: 10
      - axis: "リアルタイムチャット体験"
        multiplier: 5
      - axis: "著作権問題の回避"
        multiplier: 3
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 9
    competitive_advantage: "ゲーム配信専門プラットフォーム、コミュニティ中心設計、ストリーマーとの直接対話"
  pivot:
    occurred: true
    pivot_count: 2
    pivot_trigger: "market_shift"
    original_idea: "Kiko Calendar（オンラインカレンダー）"
    pivoted_to: "Justin.tv（ライフストリーミング）→ Twitch（ゲーム配信）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Justin Kan", "Michael Seibel", "Kyle Vogt"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia"
    - "TechCrunch"
    - "Y Combinator Library"
    - "How I Built This Podcast"
    - "Mixergy Interview"
    - "Data Science Weekly"
---

# Emmett Shear - Twitch

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Emmett Shear |
| 生年 | 1983年 |
| 国籍 | アメリカ |
| 学歴 | Yale大学 コンピュータサイエンス学部卒業（2005年） |
| 創業前経験 | Kiko Calendar共同創業者（Y Combinator 2005）、Justin.tv共同創業者 |
| 企業名 | Twitch |
| 創業年 | 2011年（Justin.tvからスピンオフ） |
| 業界 | ライブストリーミング / ゲーム配信 |
| 現在の状況 | 2014年Amazonに買収 |
| 評価額/時価総額 | $970M（買収時）、推定$46B（2024年時点でのAmazon内部評価） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- Shear自身が熱心なゲーマーであり、特にStarcraft 2を「取り憑かれたように」プレイしていた
- 2009年頃、ゲーマーたちがJustin.tvでStarcraft 2のベータ版をストリーミングし始め、その視聴に没頭した
- Justin.tv上でゲーミングカテゴリが急速に成長し、最も人気のあるコンテンツになっていることに気づいた

**需要検証方法**:
- Justin.tvのデータ分析により、ゲームカテゴリがスポーツに次いで急成長していることを発見
- コンテンツ制作者への電話インタビューを実施し、ニーズを直接確認
- 自身のゲーマーとしての体験を通じた一次情報の収集

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 具体的な数値は不明だが、継続的にユーザーへの電話インタビューを実施
- 手法: コンテンツ制作者（ストリーマー）への直接電話、データ分析
- 発見した課題の共通点:
  - 汎用ストリーミングプラットフォームではゲーマー特有のニーズに対応できない
  - ゲーム実況に特化した機能（低遅延チャット、ゲーム別カテゴリ等）が必要
  - コミュニティ形成とマネタイズの仕組みが求められていた

**3U検証**:
- Unworkable（現状では解決不可能）: YouTubeは録画動画中心で、リアルタイム視聴体験を提供できなかった
- Unavoidable（避けられない）: eSportsの急成長により、ゲーム配信の需要は避けられない流れだった
- Urgent（緊急性が高い）: 既にJustin.tv上でゲーム配信が爆発的に伸びており、専門プラットフォームの需要が顕在化していた

**支払い意思（WTP）**:
- 確認方法: サブスクリプションボタンの導入、広告収益モデルの実験
- 結果: 2011年4月にDay9tvが最初のサブスクライバーボタンを獲得し、課金意欲を確認

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 |
|---|------------|-----------------|------|
| ゲーマー特化UX | YouTube（汎用動画プラットフォーム） | ゲーム配信専門設計、ゲーム別カテゴリ | 10x |
| リアルタイム対話 | コメント欄（非同期） | 低遅延ライブチャット | 5x |
| コミュニティ形成 | 一方向的な視聴体験 | ストリーマー中心のコミュニティ構築 | 5x |
| マネタイズ | 広告収益のみ | サブスクリプション、投げ銭、広告の複合 | 3x |
| 著作権問題 | スポーツ等は著作権侵害リスク | ゲームスタジオはストリーミングを歓迎 | 無限大 |

**MVP**:
- タイプ: プロトタイプ（Justin.tvのゲームカテゴリを独立サイトとしてスピンオフ）
- 初期反応: ローンチから数ヶ月で10億分以上の視聴時間を達成
- CVR: 具体的な数値は不明

**UVP（独自の価値提案）**:
- 「ゲーマーのためのゲーマーによるライブ配信プラットフォーム」
- リアルタイムチャットを通じた視聴者とストリーマーの双方向対話
- ゲームコミュニティに特化した機能とカルチャー

**競合との差別化**:
- YouTubeが録画動画中心だったのに対し、ライブ配信に特化
- ゲーミング専門のコミュニティとカルチャーを構築
- ストリーマーとの直接的な関係構築とマネタイズ支援

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- **Kiko Calendar（2005-2006年）**: Y Combinator第1期に参加し、オンラインカレンダーを開発。しかしGoogleカレンダーのリリースにより競争力を失い、eBayで$258,000で売却
- **資金難**: Justin.tv初期、エンジェル投資が集まらず、ShearとJustin Kanはそれぞれ$15,000（ほぼ全財産）を会社に貸し付けて生き延びた
- **プロダクトビジョンの迷走**: Justin.tvショーの終了後、ユーザーと話すことを怠り、一時的に方向性を見失った

### 3.2 ピボット（該当する場合）

- 元のアイデア: Kiko Calendar（オンラインカレンダー）→ Justin.tv（ライフストリーミング）
- ピボット後: Twitch（ゲーム配信専門プラットフォーム）
- きっかけ:
  - Justin.tvでゲームカテゴリが最も急成長していたデータを発見
  - スポーツストリーミングに関する著作権訴訟の増加
  - ゲームスタジオがストリーミングを歓迎し、著作権問題がないことを確認
  - Shear自身がStarcraft 2の配信を「取り憑かれたように」視聴していた経験
- 学び:
  - データに基づく意思決定の重要性（Justin.tvでは直感で動いていたが、Twitchではデータ主導に転換）
  - ユーザーと継続的に話すことの重要性
  - 自分自身がユーザーであることの強み

## 4. 成長戦略

### 4.1 初期トラクション獲得

- Justin.tv既存ユーザーベースからのスピンオフにより、初日から視聴者を確保
- ゲームパブリッシャー（EA、Activision、Ubisoft等）との戦略的パートナーシップ
- ゲームへのTwitch配信機能の直接統合
- 最初の1年で月間320万ユニークユーザーを達成

### 4.2 フライホイール

```
より多くのストリーマー
    ↓
より多様で質の高いコンテンツ
    ↓
より多くの視聴者
    ↓
ストリーマーの収益増加
    ↓
より多くのストリーマー参入
    ↓
コミュニティの成長と深化
```

### 4.3 スケール戦略

- 2012年に$15M、2013年に$20Mの資金調達
- 主要ゲームパブリッシャーとの公式パートナーシップ締結
- eSportsイベントの公式配信プラットフォームとしての地位確立
- 2014年2月時点で米国内インターネットトラフィック第4位（Netflix、Google、Appleに次ぐ）

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | 自社開発のストリーミングインフラ |
| マーケティング | パートナーシップ主導、オーガニックグロース |
| 分析 | 自社構築のデータ分析基盤、A/Bテスト |
| コミュニケーション | ユーザーへの直接電話インタビュー |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **創業者のドメイン知識**: Shear自身が熱心なゲーマーであり、ユーザーのニーズを深く理解していた
2. **データドリブンな意思決定**: Justin.tvの失敗から学び、Twitchでは初日からデータを重視した製品開発を実施
3. **コミュニティ中心設計**: 視聴者とストリーマーの双方向対話を実現するチャット機能により、強固なコミュニティを構築

### 6.2 タイミング要因

- eSportsの急成長期と完璧に一致
- ブロードバンドの普及により高品質ストリーミングが可能に
- ゲーム実況文化の萌芽期に市場参入
- YouTubeがまだライブ配信に本格参入していなかった

### 6.3 差別化要因

- ゲーム配信専門という明確なポジショニング
- リアルタイムチャットによる独自のコミュニティカルチャー
- ストリーマーへのマネタイズ支援（サブスクリプション、広告収益分配）
- ゲームパブリッシャーとの良好な関係（著作権問題なし）

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 4 | 日本でもゲーム実況は人気だが、ニコニコ動画やYouTubeが先行 |
| 競合状況 | 2 | YouTube、ニコニコ、OPENREC等が既に存在 |
| ローカライズ容易性 | 3 | Twitchは日本に参入済みだが、ローカルコンテンツが課題 |
| 再現性 | 3 | 既存プラットフォームからのスピンオフ戦略は参考になる |
| **総合** | 3 | 日本市場では既存プレイヤーとの差別化が重要 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **自身がユーザーであることの価値**: Shearは自分自身が熱心なゲーマーだったため、ユーザーのペインを深く理解できた
- **データの中に需要が隠れている**: Justin.tvのゲームカテゴリの成長データが、Twitchの着想源となった
- **既存プロダクトの予想外の使われ方に注目**: 想定外のユースケースが新規事業の種になることがある

### 8.2 CPF検証（/validate-cpf）

- **コンテンツ制作者への直接電話**: Shearは「ゲーム空間で最も重要なのはコンテンツ制作者」と考え、彼らに直接電話してニーズを確認した
- **定性と定量の両輪**: ユーザーインタビュー（定性）とデータ分析（定量）を組み合わせた検証
- **著作権リスクの事前確認**: ゲームスタジオがストリーミングを歓迎していることを確認し、法的リスクを回避

### 8.3 PSF検証（/validate-10x）

- **専門特化による10倍優位性**: 汎用プラットフォーム（YouTube）に対し、ゲーム配信専門という特化で差別化
- **リアルタイムインタラクション**: 非同期コメントではなく、ライブチャットという新しい体験を提供
- **最小限のMVP**: Justin.tvのゲームカテゴリをそのままスピンオフし、最速で市場検証

### 8.4 スコアカード（/startup-scorecard）

- **市場タイミング**: eSports成長期と完璧に一致（タイミングスコア高）
- **創業者適性**: 自身がヘビーユーザー（ドメイン知識スコア高）
- **ピボット実行力**: Kiko→Justin.tv→Twitchと2回の成功ピボット（実行力スコア高）
- **データ活用**: Justin.tvの失敗から学び、データドリブン経営を確立

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **VTuber特化ライブプラットフォーム**: 日本発のVTuber文化に特化した配信プラットフォーム。VTuber向けツール、ファンコミュニティ機能を統合
2. **eスポーツ教育プラットフォーム**: プロゲーマーによるコーチング、リプレイ分析、コミュニティ学習を組み合わせたサービス
3. **ニッチ趣味特化ライブコマース**: 特定趣味（例：プラモデル、釣り、盆栽）に特化したライブコマース。専門家とファンのコミュニティ形成
4. **リアルタイム共同視聴サービス**: アニメ、映画等のリアルタイム共同視聴とチャットを組み合わせたソーシャル視聴体験

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2011年） | PASS | Wikipedia, TechCrunch, Y Combinator |
| 買収額（$970M） | PASS | GeekWire, Amazon発表 |
| 創業者Yale大学卒業（2005年） | PASS | Wikipedia, Famous Birthdays |
| Justin.tvからのスピンオフ（2011年6月） | PASS | Wikipedia, Failory |
| 月間5500万ユーザー（買収時） | PASS | TechCrunch, Business of Apps |

**凡例**: PASS（2ソース以上確認）、WARN（1ソースのみ）、FAIL（確認不可）

## 参照ソース

1. [Emmett Shear - Wikipedia](https://en.wikipedia.org/wiki/Emmett_Shear)
2. [Emmett Shear, Co-Founder of Twitch - Y Combinator Library](https://www.ycombinator.com/library/KM-emmett-shear-co-founder-of-twitch)
3. [TwitchTV: How To Pivot When The First Vision Falters - Mixergy](https://mixergy.com/interviews/emmett-shear-twitchtv-interview/)
4. [CEO Perspective: Emmett Shear Interview - Data Science Weekly](https://www.datascienceweekly.org/data-scientist-interviews/data-science-twitch-ceo-perspective-emmett-shear-interview)
5. [Amazon's $970M acquisition of Twitch - GeekWire](https://www.geekwire.com/2014/amazon-acquires-twitch-970m/)
6. [What Happened to Justin.tv - Failory](https://www.failory.com/cemetery/justin-tv)
7. [How to Run a User Interview by Twitch CEO Emmett Shear - Medium](https://medium.com/fastrecap/how-to-run-a-user-interview-by-twitch-ceo-emmett-shear-b43e8a76738c)
8. [Twitch Revenue and Usage Statistics - Business of Apps](https://www.businessofapps.com/data/twitch-statistics/)
9. [Twitch Interactive: The Streaming Market War - Ivey Business Review](https://www.iveybusinessreview.ca/magazine/articles/twitch-streaming-market-war)
10. [Ex-Twitch CEO Emmett Shear is founding an AI startup backed by a16z - TechCrunch](https://techcrunch.com/2024/12/19/ex-twitch-ceo-emmett-shear-is-founding-an-ai-startup-backed-by-a16z/)
11. [Scaling without losing focus on meaningful metrics - Mixpanel](https://mixpanel.com/blog/scaling-without-losing-focus-on-meaningful-metrics-how-twitch-gets-it-right/)
12. [Kiko - Y Combinator](https://www.ycombinator.com/companies/kiko)
