---
id: "FOUNDER_082"
title: "Evan Spiegel - Snapchat / Snap Inc."
category: "founder"
tier: "unicorn"
type: "case_study"
version: "2.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["social-media", "ephemeral-messaging", "Gen-Z", "mobile-first", "AR", "消える写真", "VC-backed", "IPO"]

# 基本情報
founder:
  name: "Evan Thomas Spiegel"
  birth_year: 1990
  nationality: "アメリカ"
  education: "スタンフォード大学プロダクトデザイン専攻（2018年卒業）"
  prior_experience: "Red Bullマーケティングインターン、Intuit（TxtWebプロジェクト）、ケープタウンでキャリア講師"

company:
  name: "Snap Inc."
  founded_year: 2011
  industry: "ソーシャルメディア / エフェメラルメッセージング"
  current_status: "ipo"
  valuation: "IPO時$24B（2017年）/ 現在約$12B（2025年）"
  employees: 4911

# VC投資情報
funding:
  total_raised: "$3.4B（IPO前）+ $3.4B（IPO）= $6.8B"
  funding_rounds:
    - round: "seed"
      date: "2012-05"
      amount: "$485K"
      valuation_post: "不明"
      lead_investors: ["Lightspeed Venture Partners"]
      other_investors: []
    - round: "series_a"
      date: "2013-02"
      amount: "$13.5M"
      valuation_post: "$70M"
      lead_investors: ["Benchmark Capital"]
      other_investors: ["Lightspeed Venture Partners", "General Catalyst"]
    - round: "series_b"
      date: "2013-06"
      amount: "$80M"
      valuation_post: "$800M"
      lead_investors: ["IVP"]
      other_investors: ["SV Angel", "Benchmark", "Lightspeed"]
    - round: "series_c"
      date: "2014-12"
      amount: "$485M"
      valuation_post: "$10B"
      lead_investors: ["Kleiner Perkins"]
      other_investors: ["Yahoo", "Alibaba"]
    - round: "series_f"
      date: "2016-05"
      amount: "$1.8B"
      valuation_post: "$20B"
      lead_investors: ["Fidelity", "General Atlantic"]
      other_investors: []
    - round: "ipo"
      date: "2017-03-02"
      amount: "$3.4B"
      valuation_post: "$24B"
      lead_investors: ["Morgan Stanley", "Goldman Sachs"]
      other_investors: []
  top_tier_vcs: ["Lightspeed Venture Partners", "Benchmark Capital", "Kleiner Perkins", "IVP", "General Catalyst"]

# 成功/失敗/Pivot分類
outcome:
  category: "success"
  subcategory: "ipo_success"
  failure_pattern: ""
  pivot_details:
    count: 3
    major_pivots:
      - id: "pivot_1"
        trigger: "market_shift"
        date: "2011-09"
        decision_speed: "2ヶ月"
        before:
          idea: "自己消滅型写真共有アプリ「Picaboo」"
          target_market: "スタンフォード大学生"
          business_model: "無料アプリ、収益モデル未定"
          cpf_score: 3
        after:
          idea: "「Snapchat」にリブランド、ターゲット変更"
          hypothesis: "高校生市場の方が「消える写真」のニーズが高い"
        resources_preserved:
          team: "Evan Spiegel & Bobby Murphy（Reggie Brownを除名）"
          technology: "iOS アプリ基盤そのまま活用"
          investors: "未調達段階のため該当なし"
        validation_process:
          - stage: "リブランド実施"
            duration: "1ヶ月"
            result: "徐々にユーザー増加開始"
      - id: "pivot_2"
        trigger: "market_shift"
        date: "2013-10"
        decision_speed: "6ヶ月の開発期間"
        before:
          idea: "1対1の消える写真メッセージング"
          target_market: "高校生・大学生の個人間コミュニケーション"
          business_model: "広告モデル検討中"
          cpf_score: 8
        after:
          idea: "Stories機能追加（24時間表示の連続投稿）"
          hypothesis: "より広範な共有ニーズに応える"
        resources_preserved:
          team: "全員継続"
          technology: "コア機能（一時性）を保持しながら拡張"
          investors: "Benchmark、Lightspeedが継続支援"
        validation_process:
          - stage: "Stories機能ローンチ"
            duration: "即時"
            result: "2014年6月までにStoriesが主要機能化（1日10億回再生超）"
      - id: "pivot_3"
        trigger: "psf_failure"
        date: "2017-11"
        decision_speed: "減損処理までに約6ヶ月"
        before:
          idea: "消費者向けウェアラブルカメラ「Spectacles」"
          target_market: "Snapchatユーザー全般"
          business_model: "$130での販売"
          cpf_score: 4
        after:
          idea: "開発者向けARプラットフォームへシフト"
          hypothesis: "ハードウェア直販ではなくエコシステム構築"
        resources_preserved:
          team: "AR開発チーム維持"
          technology: "ARレンズ技術を次世代製品に活用"
          investors: "上場済み、株主への説明責任"
        validation_process:
          - stage: "Spectacles販売停止・減損処理"
            duration: "2017年末"
            result: "$40M減損処理、22万台販売で終了"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 25  # 推定: 友人・家族約20人 + ショッピングモールでの直接ピッチ5人以上（出典: Inc.com, Frederick.ai）
    problem_commonality: 30  # 推定: 米国高校生（2012年時点スマホ普及率約30-35%）のうち、ソーシャルメディアの永続性に不安を感じる層（出典: Cornell Networks, Benchhacks）
    wtp_confirmed: true  # 初期無料→広告モデル→Snapchat+サブスク（2024年$500M超）で収益化確認（出典: Wikipedia, Snap IR）
    urgency_score: 8  # デジタルタトゥー問題、就職活動前のSNS投稿削除の緊急性
    validation_method: "プロトタイプ配布 + 友人家族テスト + ショッピングモール直接ピッチ + 高校生コミュニティでの観察"
  psf:
    ten_x_axes:
      - axis: "プライバシー"
        multiplier: 10
      - axis: "心理的負担軽減"
        multiplier: 5
      - axis: "リアルタイム性"
        multiplier: 3
    mvp_type: "prototype"
    initial_cvr: 0.70  # 推定: 3,000 DAU（2012年初頭）→ 30,000 DAU（同月末）、月間10倍成長（出典: Cornell Networks, Benchhacks）
    uvp_clarity: 9
    competitive_advantage: "一時的なコンテンツ共有による心理的解放と安心感"
  pivot:
    occurred: true
    pivot_count: 3
    pivot_trigger: "market_shift"
    original_idea: "Picaboo（自己消滅型写真共有）"
    pivoted_to: "Snapchat + Stories機能によるソーシャルプラットフォーム化"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Mark Zuckerberg", "Kevin Systrom", "Bobby Murphy", "Reggie Brown"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 18
  last_verified: "2025-12-29"
  primary_sources:
    - "TechCrunch - Snapchat Raises $13.5M Series A Led By Benchmark (2013)"
    - "TechCrunch - How Reggie Brown invented Snapchat (2018)"
    - "TechCrunch - Snapchat Gets Its Own Timeline With Stories (2013)"
    - "CNBC - Snapchat IPO First Day Trading (2017)"
    - "CNN Business - Snapchat rejected Facebook's $3B offer (2013)"
    - "Cornell Networks - How Snapchat Gained Success By Going Viral At High Schools"
    - "Inc.com - How Snapchat's First Investor Found Snapchat"
    - "Inc.com - Don't Credit Sexting: How Snapchat Actually Took Off"
    - "Benchhacks - Snapchat Growth Study"
    - "Snap Inc. Investor Relations - Q4 2024 Results"
    - "Wikipedia - Evan Spiegel"
    - "Wikipedia - Snapchat"
    - "Frederick.ai - Founder Story: Evan Spiegel of Snapchat"
    - "Buildd.co - Evan Spiegel Biography"
    - "Entrepreneurship Handbook - Startup Lessons from Snapchat CEO"
    - "Lightspeed Venture Partners - Snap Portfolio"
    - "GetPIN.xyz - Inside the Deal: Snapchat"
    - "FoundersToday - Snap Inc.'s Remarkable Journey in Fundraising"
---

# Evan Spiegel - Snapchat / Snap Inc.

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Evan Thomas Spiegel（共同創業者：Bobby Murphy、Reggie Brown） |
| 生年 | 1990年6月4日 |
| 国籍 | アメリカ |
| 学歴 | スタンフォード大学プロダクトデザイン専攻（2018年卒業、一時中退後復学） |
| 創業前経験 | Red Bullマーケティングインターン、Intuit（TxtWebプロジェクト）、南アフリカ・ケープタウンでキャリア講師 |
| 企業名 | Snap Inc.（旧Snapchat Inc.） |
| 創業年 | 2011年（Picabooとして7月ローンチ、9月にSnapchatへ改名） |
| 業界 | ソーシャルメディア / エフェメラルメッセージング / AR |
| 現在の状況 | NYSE上場（2017年3月IPO）、DAU 4.6億人超（2025年） |
| 評価額/時価総額 | IPO時$24B / 現在約$12B（2025年1月時点） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- 2011年4月、スタンフォード大学のプロダクトデザインクラス「Design and Business Factors」にて、友愛会の仲間Reggie Brownが「消えてなくなる写真を送れたらいいのに（I wish I could send disappearing photos）」とアイデアを提案
- 当時、学生たちは就職面接前にFacebookやInstagramの恥ずかしい投稿を削除するために奔走していた
- 永続的なデジタル記録（デジタルタトゥー）がもたらすリスクと心理的負担に着目
- Spiegelは自身のクラスプロジェクトとしてこのアイデアを採用（後にReggie Brownとの法的紛争に発展）

**需要検証方法**:
- プロトタイプ「Picaboo」をiOSアプリとして開発
- 友人・家族約20人に初期配布してフィードバック収集
- ショッピングモールでフライヤーを配布し、直接ピッチ（5人以上と推定）
- スタンフォード大学コミュニティでのテスト

**初期の反応**:
- **スタンフォード学生**: クラスメイトから冷ややかな反応、コンセプトを嘲笑される
  - 「消える写真」は政府スパイや不適切な用途向けという印象を持たれた
  - クラスプレゼンでは批判的な評価を受けた
- **2011年夏終了時点**: わずか127ユーザーで成長停滞
- **2011年末〜2012年初頭**: Spiegelの母親が親戚の高校生に紹介 → 南カリフォルニアの高校で爆発的に拡散開始

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 25件（推定）
  - 友人・家族への初期配布: 約20人
  - ショッピングモールでの直接ピッチ: 5人以上
  - 高校生ユーザーへの非公式フォローアップ: 数十人規模（正確な数は不明）
- 手法: プロトタイプ配布 + 直接ピッチ + ユーザー行動観察
- 発見した課題の共通点:
  - **ソーシャルメディアの永続性への不安**: 就職活動や人間関係への悪影響懸念
  - **編集・キュレーションされたコンテンツへのプレッシャー**: Instagram的な「完璧な写真」文化への疲弊
  - **素のコミュニケーションへの渇望**: 「授業中にこっそりメモを回す」ような自然なやり取りを求めていた

**3U検証**:
- **Unworkable（現状では解決不可能）**:
  - Facebook、Instagram、Twitterなど既存SNSは全て永続的な記録を前提としていた
  - 一度投稿したコンテンツは完全削除が困難（サーバー保存、第三者保存等）
- **Unavoidable（避けられない）**:
  - デジタルネイティブ世代にとってソーシャルメディアは生活インフラ
  - 友人とのコミュニケーション手段として不可欠
- **Urgent（緊急性が高い）**:
  - 就職活動における「デジタルタトゥー」問題が顕在化
  - 企業の採用担当者がSNSをチェックする時代に突入
  - 高校生・大学生は日常的に写真共有したいが、将来への影響を恐れていた

**支払い意思（WTP）**:
- 確認方法:
  - 初期は無料アプリとしてリリース、広告モデルを後に導入（2015年頃〜）
  - 2022年: 有料サブスクリプション「Snapchat+」開始
- 結果:
  - Snapchat+が2024年に年間$500M超の収益達成
  - DAU 4.6億人のうち約1,200万人が有料会員（約2.6%のコンバージョン率）

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | Snapchat | 倍率 |
|---|------------|----------|------|
| プライバシー | Facebook/Instagram（永続的投稿、削除困難） | 1-10秒で自動消滅、記録に残らない | **10x** |
| 心理的負担 | 完璧な写真・キャプションを求めるプレッシャー | 素の瞬間を共有、消えるので気軽 | **5x** |
| リアルタイム性 | キュレーションされた投稿、時間をかけて編集 | 瞬間的なコミュニケーション、その場で撮影・送信 | **3x** |
| ターゲット適合性 | 全年齢向け汎用SNS、親世代も利用 | 10代向けに最適化、親に見られない安心感 | **5x** |
| 使いやすさ | 複雑なプライバシー設定、投稿前の確認 | シンプルなUI、タップするだけで送信 | **2x** |

**MVP**:
- タイプ: プロトタイプ（iOS アプリ「Picaboo」→「Snapchat」）
- 開発期間: 約3ヶ月（2011年4月アイデア → 7月ローンチ）
- 初期機能: 写真撮影 + 1-10秒のタイマー設定 + 自動消滅のみ
- 初期反応:
  - 2011年7月（Picaboo）: 127ユーザーで停滞
  - 2011年9月（Snapchat改名後）: 徐々に増加開始
  - 2011年12月: 2,000ユーザー
  - 2012年1月: 20,000ユーザー（10倍成長）
  - 2012年4月: 100,000ユーザー（4ヶ月で5倍成長）
  - 2012年10月: 1,000,000ユーザー、毎秒231枚の写真処理
- CVR: 初期は正式なCVRデータなし
  - ただし、ユーザーは「毎日、一日中使用」する高いエンゲージメントを示した
  - 月間継続率は推定70%以上（急激な成長曲線から逆算）

**UVP（独自の価値提案）**:
- **「消える写真」による心理的解放**: 将来への影響を心配せずに共有できる
- **素の瞬間を共有できる安心感**: 完璧さを求めない、ありのままのコミュニケーション
- **10代の「授業中にこっそりメモを回す」体験のデジタル再現**: 秘密を共有する特別感

**競合との差別化**:
- **vs Facebook/Instagram**: 永続的 vs 一時的、キュレーション vs リアルタイム
- **vs SMS/MMS**: テキスト中心 vs 写真中心、記録が残る vs 消える
- **vs iMessage**: 汎用的 vs 写真特化、既読通知のみ vs スクリーンショット通知

## 3. ピボット/失敗経験

### 3.1 初期の失敗

**1. Picabooとしてのローンチ失敗（2011年7月〜9月）**
- 初期ダウンロード数は極めて少なく、127ユーザーで2ヶ月間停滞
- 「消える写真」コンセプトは市場に理解されず、不適切用途のイメージが先行
- 共同創業者間の対立が表面化
  - Reggie Brownがアイデアの発案者として自己主張
  - Evan SpiegelとBobby MurphyがReggie Brownを追放（後に$157.5Mの和解金支払い）

**2. ターゲット設定の誤り（2011年7月〜12月）**
- 当初は大学生（スタンフォードコミュニティ）向けにマーケティング
- スタンフォード学生からの冷ややかな反応に直面
  - 「消える写真 = 不適切な用途」という偏見
  - 大学生は既にFacebook、Instagramに深く依存
- **真のターゲット（高校生）の発見**:
  - 2011年末、Spiegelの母親が親戚の高校生に紹介
  - 南カリフォルニアの高校で爆発的に拡散
  - 高校生は「親に見られない」「記録に残らない」価値を即座に理解

**3. Spectacles失敗（2016年11月〜2017年）**
- ウェアラブルカメラ「Spectacles」を$130で販売開始
  - コンセプト: Snapchat投稿用の一人称視点カメラグラス
  - 限定販売（自動販売機型ポップアップストア）で話題性を狙う
- 結果:
  - 2017年末に**$40Mの未販売在庫を減損処理**
  - 販売台数わずか22万台（目標の1/10以下）
  - ハードウェアビジネスの難しさを痛感
- 学び:
  - ソフトウェア企業がハードウェアに進出する際の課題
  - ニッチ製品の需要予測の難しさ
  - AR技術自体は有望だが、消費者向け販売モデルは再考が必要

### 3.2 ピボット（該当する場合）

**ピボット1: Picaboo → Snapchat（2011年9月）**
- **元のアイデア**: 自己消滅型写真共有アプリ「Picaboo」
- **ピボット後**: 「Snapchat」にリブランド、マーケティング戦略を高校生向けに変更
- **きっかけ**:
  - 既存商標「Picaboo」との競合懸念
  - 127ユーザーでの停滞を打破するフレッシュスタート
  - 大学生市場での失敗を受けた方向転換
- **学び**:
  - ブランド名の重要性（「Snapchat」は直感的で覚えやすい）
  - 市場再アプローチの有効性（ターゲット変更 + リブランド）
  - 失敗を認めて素早く方向転換する重要性

**ピボット2: 1対1メッセージ → Stories（2013年10月3日）**
- **元のアイデア**: 個人間での消える写真送信
- **ピボット後**: 「Stories」機能追加（24時間表示される連続投稿）
- **きっかけ**:
  - ユーザーがより広い共有（1対多）を求めていた
  - 友人グループ全体に一度に共有したいニーズ
  - エンゲージメント向上のための機能拡張
- **成果**:
  - 2014年6月: Storiesが1対1メッセージを超えて主要機能化
  - 1日10億回以上の再生数達成
  - 後にInstagram、Facebook、WhatsAppが模倣する影響力
- **学び**:
  - コア機能（一時性）を保ちながらユースケースを拡張
  - ユーザー行動の観察から新機能を発想
  - プラットフォームとしての進化の重要性

**ピボット3: ハードウェア戦略の転換（2017年以降）**
- **元のアイデア**: 消費者向けウェアラブル「Spectacles」の大量販売
- **ピボット後**: 開発者向けARプラットフォーム + 企業向けSpectacles
- **きっかけ**:
  - 消費者市場での失敗（$40M減損）
  - ARレンズ機能の成功（企業スポンサー付きレンズの収益化）
  - ハードウェア直販の限界認識
- **学び**:
  - ハードウェア事業の難しさ（在庫リスク、製造コスト、流通）
  - ARエコシステム構築の重要性（デバイス販売よりプラットフォーム）
  - B2C失敗をB2B/B2B2Cモデルに転換

## 4. 成長戦略

### 4.1 初期トラクション獲得

**偶発的バイラル成長（2011年末〜2012年）**:
- **きっかけ**: Spiegelの母親が知人（親戚）に紹介 → その子供（高校生）が学校で拡散
- **地理的拡大**: LA近郊の1つの高校 → 南カリフォルニア全域の高校 → 全米の高校・大学
- **体験価値**: 「授業中にこっそりメモを回す」デジタル版として10代に刺さった
- **成長の仕組み**:
  - 密なコミュニティ（高校のクラス、部活）内で瞬時に拡散
  - 友人全員が使っていないと価値がないネットワーク効果
  - 「親に見られない」という価値が高校生に特に響いた

**成長チャネル構成**（2012年時点の推定）:
- 口コミ: 68%（友人からの直接紹介）
- 招待機能: 19%（アプリ内の友達招待）
- プレス報道: 9%（TechCrunch等の記事）
- その他: 4%（App Store検索等）

**急成長の軌跡**:
- 2011年12月: 2,000ユーザー
- 2012年1月: 20,000ユーザー（月間10倍成長）
- 2012年4月: 100,000ユーザー（3ヶ月で5倍成長）
- 2012年5月: 毎秒25枚の写真送信（Lightspeed $485K調達直前）
- 2012年10月: 1,000,000ユーザー、毎秒231枚の写真処理
- 2012年11月: 累計10億枚の写真共有達成
- 2012年12月: 1日2,000万枚の写真送信
- 2013年2月: 1日6,000万枚の写真送信（Series A $13.5M調達発表時）

### 4.2 フライホイール

```
高校生Aが友達B,C,Dを招待
    ↓
密なコミュニティ（クラス、部活）内で急速拡散
    ↓
エンゲージメント向上（毎日、一日中使用）
    ↓
隣接する高校・大学へ波及（兄弟、先輩後輩経由）
    ↓
若年層のデファクトスタンダード化
    ↓
さらなる友達招待（ネットワーク効果の強化）
    ↓
Stories機能でプラットフォーム化（広告収益化）
    ↓
資金調達 → プロダクト改善 → ユーザー体験向上
    ↓
（最初に戻る）
```

### 4.3 スケール戦略

**フェーズ1: シードステージ（2011年〜2012年5月）**
- 自己資金 + 友人からの少額調達でPicaboo開発
- ユーザー増加に伴うサーバー費用の問題に直面
- **2012年5月: Lightspeed Venture Partnersから$485K調達**
  - リード投資家: Jeremy Liew（Lightspeed）
  - きっかけ: Liewのパートナー Barry Eggersの娘がSnapchatを使用していた
  - 使途: サーバー費用の問題解決 + iOS開発リソース増強

**フェーズ2: シリーズA（2013年2月）**
- **Benchmark Capitalから$13.5M調達**
  - Post-Money評価額: $70M
  - リード投資家: Mitch Lasky（Benchmark）
  - 他の投資家: Lightspeed、General Catalyst
  - 調達時のトラクション: 1日6,000万枚の写真送信
- 使途:
  - エンジニアリングチーム拡大
  - Androidアプリ開発（2012年10月にリリース済みだが改善）
  - サーバーインフラ強化

**フェーズ3: シリーズB〜C（2013年6月〜2014年12月）**
- **Series B（2013年6月）: $80M @ $800M評価額**
  - リード: IVP
  - Facebook $3B買収オファー拒否（2013年11月）直前
- **Series C（2014年12月）: $485M @ $10B評価額**
  - リード: Kleiner Perkins
  - Yahoo、Alibabaも参加
  - 評価額が1年で12.5倍に急上昇

**フェーズ4: 大型買収拒否（2013年11月）**
- **Facebook（Mark Zuckerberg）からの$3B買収オファーを拒否**
  - 当時、Snapchatは創業わずか2年、評価額$800M程度
  - Spiegelのコメント: 「短期的な利益のためにビジョンを売るのは面白くない」
  - 独立路線での成長を選択
- 影響:
  - FacebookはInstagram Stories（2016年8月）でSnapchatを模倣
  - Snapchatの成長率が一時82%減速（TechCrunch報道）
  - しかし独立企業として2017年IPOを達成

**フェーズ5: IPO（2017年3月2日）**
- **NYSE上場、ティッカーシンボル: SNAP**
  - 公募価格: $17/株
  - 初日終値: $24.48/株（+44%）
  - 時価総額: 初日$33B、公募時点$24B
  - 調達額: $3.4B（米国テックIPOとしてはFacebook以来最大）
  - 主幹事: Morgan Stanley、Goldman Sachs
- 特徴:
  - 議決権のない株式（Class A）のみを公開（創業者支配の維持）
  - 初の赤字上場大型テックIPO

### 4.4 バリューチェーン

```
[コンテンツ作成]
    ↓
ユーザーが写真・動画を撮影（ARレンズ使用）
    ↓
[配信]
    ↓
1対1メッセージ or Stories投稿
    ↓
[消費]
    ↓
受信者が閲覧（1-10秒 or 24時間）
    ↓
[収益化]
    ↓
① 広告（Snap Ads、Sponsored Lenses、Discover）
② Snapchat+サブスクリプション
③ Spectacles等ハードウェア販売（現在は縮小）
```

## 4.5 資金調達履歴（VC案件のみ）

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Seed | 2012年5月 | $485K | 不明 | Lightspeed Venture Partners | - |
| Series A | 2013年2月 | $13.5M | $70M | Benchmark Capital | Lightspeed, General Catalyst |
| Series B | 2013年6月 | $80M | $800M | IVP | SV Angel, Benchmark, Lightspeed |
| Series C | 2014年12月 | $485M | $10B | Kleiner Perkins | Yahoo, Alibaba |
| Series D | 2015年2月 | $約200M | $15B | Alibaba | - |
| Series F | 2016年5月 | $1.8B | $20B | Fidelity, General Atlantic | - |
| IPO | 2017年3月 | $3.4B | $24B（公募）/ $33B（初日終値） | Morgan Stanley, Goldman Sachs | - |

**総資金調達額（IPO前）**: 約$3.4B
**総資金調達額（IPO含む）**: 約$6.8B

### 主要VCパートナー

**Lightspeed Venture Partners（初期投資家）**:
- 投資時期: 2012年5月（Seed $485K）
- 投資家: Jeremy Liew、Barry Eggers
- リターン: IPO時点で約200倍以上（$485K → $100M超の保有価値推定）
- きっかけ: Eggersの娘がSnapchatを使用していることを発見

**Benchmark Capital（Series Aリード）**:
- 投資時期: 2013年2月（Series A $13.5M @ $70M評価額）
- 投資家: Mitch Lasky
- リターン: IPO時点で約220倍以上
- Laskyの役割: Snapchat取締役として戦略的助言

**Kleiner Perkins（Series Cリード）**:
- 投資時期: 2014年12月（Series C $485M @ $10B評価額）
- リターン: IPO時点で約2.4倍

### 資金使途と成長への影響

**Seed $485K（2012年5月）**:
- サーバーインフラ: AWS費用の支払い（ユーザー急増でコスト増大）
- iOS開発リソース: エンジニア1-2名採用
- 成長結果:
  - 2012年5月: 25枚/秒 → 2012年11月: 231枚/秒（約9倍）
  - ユーザー数: 100,000 → 1,000,000（10倍）

**Series A $13.5M（2013年2月）**:
- プロダクト開発: Androidアプリ改善、Stories機能開発着手
- マーケティング: ブランド認知向上（ただし主に口コミ依存）
- チーム拡大: エンジニア10名 → 30名規模へ
- 成長結果:
  - 1日の写真送信数: 6,000万枚 → 4億枚（2013年末、約6.7倍）
  - ユーザー数: 数百万 → 数千万規模

**Series B $80M（2013年6月）**:
- Stories機能開発: 2013年10月リリースに向けた開発
- サーバーインフラ: 写真・動画処理能力の大幅強化
- 成長結果:
  - Stories機能が2014年6月までに主要機能化
  - 1日10億回以上の再生数

**Series C $485M（2014年12月）**:
- Discover機能開発: メディアパートナーシップ構築
- 広告プラットフォーム構築: 収益化インフラ
- グローバル展開: 欧州・アジア市場への拡大
- 成長結果:
  - DAU: 1億人 → 2億人（2015年末）

**Series F $1.8B（2016年5月）**:
- IPO準備: 内部統制、IR体制構築
- Spectacles開発: ハードウェア事業への進出（後に失敗）
- AR技術投資: レンズ機能の高度化

### VC関係の構築

**1. YC/VC選考突破**:
- Snapchatは**Y Combinatorには参加せず**（スタンフォード出身のため独自ルート）
- Lightspeed Venture Partnersとの出会い:
  - Barry Eggersの娘がSnapchatを使用
  - Jeremy Liewが100,000ユーザー未満の時点でアプリをダウンロード
  - Liewが直接Spiegelにコンタクト（プロダクト主導の発見）
- 初期ピッチの特徴:
  - 「消える写真」という革新的コンセプト
  - 高いユーザーエンゲージメント（毎日使用）
  - 高校生市場での爆発的成長データ

**2. 投資家との関係維持**:
- Mitch Lasky（Benchmark）: 取締役として戦略的助言
  - 特にFacebook $3B買収オファー拒否の判断を支持
  - 長期ビジョンの重要性を強調
- Evan Spiegelのスタイル:
  - 投資家との定期的なコミュニケーション
  - ビジョンへの強いコミットメント（短期的利益より長期価値）
  - 独立路線の堅持（買収オファー拒否）

## 5. 使用ツール・サービス

| カテゴリ | ツール | 用途 |
|---------|-------|------|
| 開発 | iOS SDK、Android SDK | モバイルアプリ開発 |
| バックエンド | Google Cloud Platform（初期はAWS） | サーバーインフラ |
| 画像処理 | 独自開発 + OpenCV | AR レンズ、フィルター |
| データベース | Redis、Cassandra | ユーザーデータ、メッセージ管理 |
| マーケティング | 口コミ中心（広告予算ほぼゼロ） | 2012-2014年の成長期 |
| 分析 | 独自ダッシュボード | ユーザー行動分析 |
| コミュニケーション | Slack（推定） | 社内コミュニケーション |
| デザイン | Sketch、Figma（推定） | UI/UXデザイン |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **課題の本質的理解**:
   - 永続的なデジタル記録（デジタルタトゥー）に対する若者の潜在的不安を的確に捉えた
   - 表面的なニーズ（写真共有）ではなく、深層心理（心理的安全性）を解決

2. **ターゲットの絞り込み**:
   - 10代（特に高校生）という特定セグメントへの徹底的な集中
   - 大学生市場での失敗を素早く認識し、高校生へピボット

3. **口コミドリブン成長**:
   - 広告費をほぼかけずに高校コミュニティ内で爆発的に拡散
   - ネットワーク効果の最大化（友人全員が使わないと価値がない）

4. **コア機能への集中**:
   - 「消える」という一点に特化したシンプルなUX
   - 機能を増やさず、体験の質を磨く戦略

5. **タイミング**:
   - スマートフォン普及期（iPhone 4S、2011年）とデジタルネイティブ世代の台頭が合致
   - ソーシャルメディア疲れ（Facebook過剰共有への反動）の萌芽期

6. **大型買収オファーの拒否**:
   - Facebook $3B（2013年）を拒否し、独立路線を選択
   - 短期的利益より長期ビジョンを優先

7. **Stories機能の発明**:
   - 1対1メッセージから1対多のプラットフォームへの進化
   - 後にInstagram、Facebook、WhatsAppが模倣する影響力

### 6.2 タイミング要因

- **2011年**: iPhone 4Sリリース、前面カメラ搭載でセルフィー文化の誕生
- **2011-2012年**: モバイル写真共有の黎明期（Instagram 2010年創業）
- **2012-2013年**: ソーシャルメディア疲れの萌芽（Facebook過剰共有への反動）
- **2013年**: 「デジタルタトゥー」問題の社会的認知向上（就職活動での影響）
- **2012-2014年**: 10代のスマートフォン普及率急上昇期（25% → 75%）
- **2014-2016年**: 「消える」コンテンツの文化的受容（Stories機能の爆発的普及）

### 6.3 差別化要因

- **逆張り戦略**: 「すべてを記録する」風潮に対して「消える」を提案
- **心理的安全性**: 失敗を恐れずに共有できる環境の提供
- **世代特化**: 既存SNSが「親世代に見られる」問題を解決（10代の聖域）
- **プライバシー・バイ・デザイン**: プライバシーを後付けではなく、コア機能として設計
- **AR技術への早期投資**: レンズ機能で競合を大きくリード

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | LINEが強固なポジション、ただし10代のSNS多様化傾向あり |
| 競合状況 | 2 | LINE、Instagram、TikTokが既に浸透、Snapchatは苦戦 |
| ローカライズ容易性 | 4 | コンセプト自体は普遍的、UI/UX調整が必要 |
| 再現性 | 3 | 「消える」特化型サービスの余地はあるが差別化困難 |
| プライバシー意識 | 4 | 日本でもデジタルタトゥー問題は顕在化、ニーズあり |
| **総合** | 3.2 | 日本市場では類似コンセプト浸透済み、新規参入は困難 |

**日本市場での示唆**:
- LINEの「タイムライン削除」機能やInstagramの「親しい友達」機能が一部ニーズを吸収
- 「消える」メッセージングは日本文化（曖昧さ、察する文化）と親和性高い
- ただしSnapchat自体は日本で普及せず（言語障壁、ローカライズ不足）

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

**学びポイント**:
- **「永続的な記録」という既存前提を疑う逆張りアプローチ**
  - 既存SNSの共通前提（投稿は永続的）を覆す発想
  - 「当たり前」を疑うことで新市場を創出
- **大学生向け失敗 → 高校生で爆発という「真のターゲット発見」プロセス**
  - 初期仮説（大学生）が外れても諦めず、周辺セグメントを探索
  - Spiegelの母親経由での高校生市場発見（偶然を活かす）
- **友人・家族からの初期フィードバックの活用**
  - 127ユーザーでも「毎日、一日中使う」ユーザーの存在に着目
  - 少数の熱狂的ユーザーが将来の大規模成長を予兆

**適用方法**:
- 既存ソリューションの暗黙の前提（「〜すべき」「〜が当たり前」）を洗い出す
- 初期ターゲットが外れた場合、周辺セグメント（年齢、職業、地域等）を探索
- 少数でも高いエンゲージメントを示すユーザーがいれば、そのセグメントを深掘り

### 8.2 CPF検証（/validate-cpf）

**学びポイント**:
- **127ユーザーでも「毎日、一日中使う」熱狂的ユーザーの存在を重視**
  - ユーザー数（量）より使用頻度・深さ（質）を検証指標に
  - 少数でも熱狂的なら、そのセグメントには真のニーズがある
- **市場全体の反応より、コアユーザーの深いエンゲージメントに注目**
  - スタンフォード大学生の冷ややかな反応は無視
  - 高校生の「毎日使用」という行動に着目
- **ショッピングモールでの直接ピッチなど泥臭い検証活動**
  - フライヤー配布、直接対面での説明
  - オンライン調査だけでなく、リアルな反応を確認

**適用方法**:
- ユーザー数より使用頻度・深さを検証指標に（DAU/MAU比率、セッション時間等）
- 少数でも熱狂的なユーザーがいれば仮説は有望
- オンラインだけでなく、オフラインでの直接フィードバック収集も有効

### 8.3 PSF検証（/validate-10x）

**学びポイント**:
- **「プライバシー」軸で明確な10x優位性**
  - 1つの軸（プライバシー）で圧倒的優位性を確立
  - 多軸で平均的に優れるより、1軸で圧倒的に優れる方が強い
- **MVPは最小限の機能（写真送信 + 自動消滅）に絞り込み**
  - 余計な機能を削ぎ落とし、コア体験に集中
  - 初期は1対1メッセージのみ、Stories等は後から追加
- **Stories追加でコア価値を保ちながらユースケース拡張**
  - 「消える」というコア価値を薄めず、1対多の共有に対応
  - 機能追加がコア価値を強化する方向に設計

**適用方法**:
- 1つの軸（コスト、時間、使いやすさ等）で10x以上の優位性を確立してから拡張
- MVPは本当に必要最小限の機能のみ（Nice-to-haveは全て削除）
- 機能追加時はコア価値（Snapchatなら「一時性」）を薄めないよう注意

### 8.4 スコアカード（/startup-scorecard）

| 評価項目 | スコア | コメント |
|---------|-------|---------|
| 課題の深刻さ | 8/10 | デジタルタトゥー問題は潜在的だが本質的、就職活動等で顕在化 |
| 課題の共通性 | 7/10 | 高校生の30%が該当、ニッチだが十分な市場規模 |
| 10x優位性 | 9/10 | プライバシー軸で圧倒的差別化（永続 vs 一時） |
| 市場規模 | 10/10 | 全世界のモバイルユーザー（特に若年層）、TAM数兆ドル |
| 実行力 | 8/10 | MVP速度（3ヶ月）、$3B拒否の判断力、Storiesの発明 |
| タイミング | 9/10 | スマホ普及期と若年層のSNS疲れが合致 |
| チーム | 7/10 | 若年（21歳）だが、Stanford出身、プロダクトデザイン専攻 |
| トラクション | 9/10 | 月間10倍成長、高いエンゲージメント（毎日使用） |
| **総合** | **8.4/10** | 極めて高い成功確率、IPO成功も納得 |

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

**1. 「消える」就活/転職コミュニケーションアプリ**
- 課題: 就活生が企業に本音で質問できない（記録に残ると不利になる懸念）
- ソリューション: 企業と就活生の質問応答が24時間で消える
- 差別化: 記録に残らないため本音の情報交換が可能、企業側もカジュアルに回答可
- 収益化: 企業向け採用広告、プレミアム機能（過去の質問検索等）

**2. 一時的プロジェクトコラボレーションツール**
- 課題: プロジェクト終了後もデータが残り続ける（セキュリティリスク、ストレージコスト）
- ソリューション: プロジェクト終了後に全データが自動消滅するSlack/Notion代替
- 差別化: NDA不要の安全なブレスト環境、秘匿性の高いプロジェクトに最適
- 収益化: 企業向けSaaSサブスクリプション

**3. 高校生向け進路相談「消える」プラットフォーム**
- 課題: 高校生が進路について恥ずかしい質問をしづらい（記録に残る）
- ソリューション: 先輩・OBへの質問が24時間で消える形式
- 差別化: 恥ずかしい質問も気軽にできる、先輩側も気軽に回答可
- 収益化: 学校・塾向けライセンス、進学情報企業とのパートナーシップ

**4. 「消える」医療相談アプリ**
- 課題: 患者が恥ずかしい症状を相談しづらい（記録に残ると不安）
- ソリューション: 医師への質問・回答が24時間で消える（ただし同意があれば保存可）
- 差別化: プライバシー重視、気軽な相談を促進
- 収益化: 医療機関向けSaaS、オンライン診療への誘導

**5. 「消える」社内フィードバックツール**
- 課題: 社員が上司・同僚に本音でフィードバックできない
- ソリューション: 匿名 + 一時的なフィードバック（24時間で消える）
- 差別化: 心理的安全性を高め、建設的な対話を促進
- 収益化: 企業向けSaaSサブスクリプション、HRテックとの連携

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2011年） | PASS | Wikipedia、TechCrunch、Biography.com |
| IPO評価額（$24B） | PASS | CNBC、TechCrunch、Snap Inc. IR |
| Reggie Brown和解金（$157.5M） | PASS | TechCrunch、Bloomberg |
| DAU 4.6億人（2025年） | PASS | Snap Inc. IR、Business of Apps |
| Spectacles減損（$40M） | PASS | TechCrunch、CNBC |
| Facebook $3B買収オファー拒否 | PASS | CNN Business、Yahoo Finance、CNBC |
| Series A $13.5M @ $70M | PASS | TechCrunch、GetPIN.xyz |
| Lightspeed Seed $485K | PASS | Inc.com、Lightspeed公式サイト |
| 127ユーザー（2011年夏） | PASS | Cornell Networks、Benchhacks |
| 高校生市場での爆発的成長 | PASS | Cornell Networks、Inc.com、Benchhacks |
| Stories機能（2013年10月） | PASS | TechCrunch、Wikipedia |
| 1日6,000万枚送信（2013年2月） | PASS | TechCrunch Series A発表記事 |

**凡例**: PASS（2ソース以上確認）、WARN（1ソースのみ）、FAIL（確認不可）

## 参照ソース

1. [TechCrunch - Snapchat Raises $13.5M Series A Led By Benchmark](https://techcrunch.com/2013/02/08/snapchat-raises-13-5m-series-a-led-by-benchmark-now-sees-60m-snaps-sent-per-day/)
2. [TechCrunch - How Reggie Brown invented Snapchat](https://techcrunch.com/2018/02/10/the-birth-of-snapchat/)
3. [TechCrunch - Snapchat Gets Its Own Timeline With Stories](https://techcrunch.com/2013/10/03/snapchat-gets-its-own-timeline-with-snapchat-stories-24-hour-photo-video-tales/)
4. [CNBC - Snapchat IPO First Day Trading](https://www.cnbc.com/2017/03/02/snapchat-snap-open-trading-price-stock-ipo-first-day.html)
5. [CNN Business - Snapchat rejected Facebook's $3B offer](https://www.cnn.com/videos/business/2022/10/20/snapchat-facebook-buyout-offer-2013-vault-orig-ht.cnn-business)
6. [Cornell Networks - How Snapchat Gained Success By Going Viral At High Schools](https://blogs.cornell.edu/info2040/2019/11/16/how-snapchat-gained-success-by-going-viral-at-high-schools-across-los-angeles/)
7. [Inc.com - How Snapchat's First Investor Found Snapchat](https://www.inc.com/alyson-shontell/how-snapchat-investor-found-snapchat-before-anyone-else.html)
8. [Inc.com - Don't Credit Sexting: How Snapchat Actually Took Off](https://www.inc.com/christine-lagorio/real-origins-of-snapchat-growth.html)
9. [Benchhacks - Snapchat Growth Study](https://benchhacks.com/growthstudies/snapchat-growth-hacks.htm)
10. [Snap Inc. Investor Relations - Q4 2024 Results](https://investor.snap.com/news/news-details/2025/Snap-Inc.-Announces-Fourth-Quarter-and-Full-Year-2024-Financial-Results/default.aspx)
11. [Wikipedia - Evan Spiegel](https://en.wikipedia.org/wiki/Evan_Spiegel)
12. [Wikipedia - Snapchat](https://en.wikipedia.org/wiki/Snapchat)
13. [Frederick.ai - Founder Story: Evan Spiegel of Snapchat](https://www.frederick.ai/blog/evan-spiegel-snapchat)
14. [Buildd.co - Evan Spiegel Biography](https://buildd.co/startup/founder-stories/evan-spiegel)
15. [Entrepreneurship Handbook - Startup Lessons from Snapchat CEO](https://ehandbook.com/a-chat-with-evan-spiegel-snap-ceo-3db1cb6c7089)
16. [Lightspeed Venture Partners - Snap Portfolio](https://lsvp.com/company/snap/)
17. [GetPIN.xyz - Inside the Deal: Snapchat](https://www.getpin.xyz/post/inside-the-deal-snapchat)
18. [FoundersToday - Snap Inc.'s Remarkable Journey in Fundraising](https://www.founderstoday.news/fundraising-story-snap-inc/)
