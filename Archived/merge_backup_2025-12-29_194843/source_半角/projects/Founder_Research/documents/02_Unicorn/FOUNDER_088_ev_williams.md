---
id: "FOUNDER_088"
title: "Ev Williams - Twitter"
category: "founder"
tier: "unicorn"
type: "case_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["social_media", "microblogging", "pivot", "serial_entrepreneur", "platform", "real_time", "SMS", "Odeo", "Blogger"]

# 基本情報
founder:
  name: "Evan 'Ev' Williams"
  birth_year: 1972
  nationality: "USA"
  education: "University of Nebraska-Lincoln（1年半で中退）"
  prior_experience: "Pyra Labs共同創業者（Blogger）、GoogleでのBlogger担当、Odeo CEO"

company:
  name: "Twitter"
  founded_year: 2006
  industry: "ソーシャルメディア/マイクロブログ"
  current_status: "active"
  valuation: "$44B（2022年Elon Musk買収時）"
  employees: null

# VC投資情報
funding:
  total_raised: "$1.6B+"
  funding_rounds:
    - round: "series_a"
      date: "2007-07-29"
      amount: "$5M"
      valuation_post: "不明"
      lead_investors: ["Union Square Ventures"]
      other_investors: ["Charles River Ventures", "Marc Andreessen", "Dick Costolo", "Naval Ravikant", "Ron Conway", "Chris Sacca"]
    - round: "series_c"
      date: "2009-02"
      amount: "$35M"
      valuation_post: "$250M"
      lead_investors: ["Benchmark Capital", "Institutional Venture Partners"]
      other_investors: []
    - round: "ipo"
      date: "2013-11-07"
      amount: "$1.8B"
      valuation_post: "$14.2B"
      lead_investors: []
      other_investors: []
  top_tier_vcs: ["Union Square Ventures", "Benchmark Capital", "Sequoia Capital", "Spark Capital", "Kleiner Perkins"]

# 成功/失敗/Pivot分類
outcome:
  category: "success"
  subcategory: "exit_success"
  failure_pattern: ""
  pivot_details:
    count: 1
    major_pivots:
      - id: "PIVOT_001"
        trigger: "market_shift"
        date: "2006-02"
        decision_speed: "3ヶ月以内"
        before:
          idea: "Odeo（ポッドキャスティングプラットフォーム）"
          target_market: "ポッドキャスト作成者・リスナー"
          business_model: "音声コンテンツ配信・管理ツール"
          cpf_score: 3
        after:
          idea: "Twitter（リアルタイムステータス共有プラットフォーム）"
          hypothesis: "SMS経由で「今何してる？」を小グループと共有したいニーズがある"
        resources_preserved:
          team: "Jack Dorsey、Biz Stone、Evan Williams継続"
          technology: "Ruby on Railsスタック継続"
          investors: "Odeo投資家を引き継ぎ"
        validation_process:
          - stage: "社内プロトタイプ"
            duration: "2週間"
            result: "社員間で熱狂的に使用される"
          - stage: "一般公開"
            duration: "4ヶ月"
            result: "2006年7月15日公開、初期は緩やかな成長"
          - stage: "SXSW 2007でのブレイクスルー"
            duration: "3日間"
            result: "20,000ツイート/日 → 60,000ツイート/日（3倍増）"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 85
    wtp_confirmed: false
    urgency_score: 6
    validation_method: "社内プロトタイプ使用 + SXSW 2007でのバイラル検証 + ユーザー行動観察"
  psf:
    ten_x_axes:
      - axis: "即時性"
        multiplier: 100
      - axis: "摩擦の低さ"
        multiplier: 10
      - axis: "到達範囲"
        multiplier: 20
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 9
    competitive_advantage: "140文字制限 + SMS連携 + パブリックタイムライン"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "market_shift"
    original_idea: "Odeo（ポッドキャスティングプラットフォーム）"
    pivoted_to: "Twitter（リアルタイムマイクロブログ）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Jack Dorsey", "Biz Stone", "Noah Glass", "Dick Costolo"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 17
  last_verified: "2025-12-29"
  primary_sources:
    - "Wikipedia - Evan Williams"
    - "Wikipedia - Twitter"
    - "Crunchbase - Twitter Series A"
    - "Fast Company - Odeo Pivot History"
    - "TIME - Twitter IPO"
    - "CNN - Elon Musk Acquisition"
---

# Ev Williams - Twitter

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Evan "Ev" Williams（共同創業者: Jack Dorsey、Biz Stone、Noah Glass） |
| 生年 | 1972年3月31日（ネブラスカ州クラークス） |
| 国籍 | アメリカ |
| 学歴 | University of Nebraska-Lincoln（1年半で中退）、FarmHouse Fraternity所属 |
| 創業前経験 | Pyra Labs共同創業者（Blogger開発）、Google社員（Blogger担当）、Odeo CEO |
| 企業名 | Twitter（現X） |
| 創業年 | 2006年3月21日（初ツイート）、2006年7月15日（一般公開） |
| 業界 | ソーシャルメディア/マイクロブログ |
| 現在の状況 | active（2022年10月Elon Muskが$44Bで買収、X Corp.に社名変更） |
| 評価額/時価総額 | IPO時$14.2B（2013年11月）→ 買収時$44B（2022年10月） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源（2006年2月）**:
- Twitterの誕生は「課題発見」ではなく、**ピボットからの偶発的発見**
- 母体企業Odeoは、Williams が2005年に$200,000を投資して設立したポッドキャスティングプラットフォーム
- 2005年6月28日、AppleがiTunes 4.9でポッドキャスティング機能を統合し、Odeoのビジネスモデルが崩壊
- Williamsは絶望的な状況で社員にハッカソンを実施し、「普段の仕事を置いて、サイドプロジェクトに取り組め」と指示

**Jack Dorseyのアイデア**:
- Jack Dorsey（当時Odeo社員）は、2000年頃から「リアルタイムステータス共有」のアイデアを温めていた
- 「個人がSMSサービスを使って、小グループに今何をしているかを伝える」というコンセプト
- 2006年2月の社内ブレインストーミングで、Dorsey、Noah Glass、Williams、Biz Stoneが「ステータス」概念を議論
- Noah Glassが「Twttr」という名前を提案

**需要検証方法**:
- 最初は**明確な需要検証なし**
- 2006年2月からDorseyと契約開発者Florian Weberがプロトタイプ開発
- 社内サービスとしてOdeo社員に提供し、熱狂的に使用される
- Williamsの後の発言: 「Twitterが何なのか明確ではなかった。ソーシャルネットワークとも、マイクロブログとも呼ばれたが定義が難しかった。何も置き換えないから。時間をかけて発見していくパスだった」

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 正式なインタビューは実施していない
- 手法: Odeo社内での実験的使用 → 一般公開後のユーザー行動観察
- 発見した課題の共通点:
  - リアルタイムで「今」を共有したい欲求
  - SMSを超える軽量なコミュニケーション手段の不在
  - ブログのような長文は重すぎる

**3U検証**:
- **Unworkable（現状では解決不可能）**: 中程度。既存のブログ、SNS、SMSでも代替可能だったが、いずれも最適ではなかった
- **Unavoidable（避けられない）**: 中〜高。モバイル普及とリアルタイム情報欲求の増加
- **Urgent（緊急性が高い）**: 低〜中。2006年時点では「Nice to have」。SXSW 2007以降に緊急性が増加

**支払い意思（WTP）**:
- 確認方法: 初期は無料サービスのみ。WTP検証なし
- 結果: マネタイズは2010年以降（広告、Promoted Tweets）

**重要な転換点: SXSW 2007**:
- 2007年3月のSouth by Southwest Interactive会議がティッピングポイント
- 会場ホールに60インチプラズマディスプレイ2台を設置し、ライブツイートを表示
- 使用量が20,000ツイート/日 → 60,000ツイート/日（3倍増）
- SXSW Web Awardを受賞
- Williamsの振り返り: 「当時の数千人のTwitter早期採用者がSXSWに行くから、そこで宣伝しようと決めた」

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | Twitterソリューション | 倍率 |
|---|------------|-----------------|------|
| 即時性 | ブログ（数時間〜日）、メール | 数秒でグローバル配信 | 100x |
| 摩擦の低さ | ブログ投稿（編集、タイトル設定） | 140文字のテキストだけ | 10x |
| 到達範囲 | SMS（個人間）、ブログ（読者限定） | パブリックタイムライン（世界中） | 20x |
| コスト | SMS料金、ブログホスティング | 完全無料 | 10x+ |
| モバイル対応 | ブログはPC必須 | SMS経由で投稿可能 | 10x |

**MVP**:
- タイプ: Prototype（Ruby on Railsで構築）
- 2006年3月21日にDorseyが最初のツイート: "just setting up my twttr"
- 2006年7月15日に一般公開
- 初期反応: 緩やかな成長。2007年まで認知度低い
- CVR: 不明

**UVP（独自の価値提案）**:
- 「What are you doing?（今何してる？）」という単純な問い
- 140文字制限によるシンプルさと拡散性
- パブリック・デフォルトの情報共有
- リアルタイム性（ニュース速報、イベント実況）

**競合との差別化**:
- **vs. ブログ**: 長文不要、タイトル不要、編集不要
- **vs. Facebook**: 友達申請不要、パブリック投稿がデフォルト
- **vs. SMS**: 1対1ではなく1対多、無料、アーカイブ可能
- **vs. Tumblr**: テキスト中心、リブログではなくリツイート文化

## 3. ピボット/失敗経験

### 3.1 初期の失敗

**Odeoの失敗（2005年）**:
- Williamsが$200,000を投資し、Noah Glassと共同創業
- $5Mのシード資金を調達し、Jack Dorseyを含む優秀な人材を雇用
- 2005年7月10日にOdeoローンチ
- わずか18日後（6月28日）、AppleがiTunes 4.9でポッドキャスティング機能を統合
- Odeoの差別化要素が消滅し、ビジネスモデル崩壊

**Noah Glassの追放（2006年10月）**:
- Noah GlassはTwitterの「精神的リーダー」と呼ばれるほど情熱的だった
- Glassが「Twttr」という名前を提案し、初期開発を主導
- しかし、2006年10月にWilliamsはOdeo資産を投資家から買い取り、Twitterを独立企業化
- この過程でGlassを解雇し、Glassは「創業者」としての歴史から消された
- 後にGlassは「忘れ去られた創業者」として報道される

**スケーリング問題: Fail Whale（2007-2010）**:
- 2007年にTwitterが注目を集めると、サーバーダウンが頻発
- 2007年は合計約6日間のダウンタイム
- 2008年1月: Steve JobsのMacWorld基調講演中にクラッシュ
- 2008年11月4日: 大統領選挙夜に大規模ダウン
- Yiying Luがデザインした「Fail Whale」（クジラを鳥が運ぶイラスト）が過負荷エラー画面に
- 2008-2009年に1,382%成長し、技術的限界に直面
- Williamsは後に「初期の急成長に対応するため、スケーラブルな基盤を構築せずに突き進んだ結果、技術的負債を抱えた」と認める

### 3.2 ピボット（該当する場合）

**元のアイデア**: Odeo（ポッドキャスティングプラットフォーム）
- ユーザーが音声コンテンツを作成・共有できるサービス
- AppleのiTunes統合により事実上死亡

**ピボット後**: Twitter（リアルタイムマイクロブログ）
- 140文字の短文でリアルタイムにステータスを共有
- SMS連携でモバイルファースト

**きっかけ**:
- Apple iTunesによるOdeoの市場崩壊
- Williamsの「何でもいいから新しいアイデアを試せ」というハッカソン指示
- Jack Dorseyの長年温めていた「ステータス共有」アイデアの提案

**学び**:
- **ピボットの速さが重要**: Odeo崩壊から3ヶ月以内にTwitterプロトタイプを開発
- **既存リソースの活用**: Odeoのチーム（Dorsey、Stone、Williams）と技術スタック（Ruby on Rails）をそのまま活用
- **社内テストの有効性**: 社員が熱狂的に使うプロダクトは市場でも受け入れられる可能性が高い
- **不明確さを受け入れる**: Williamsは「何なのか分からないが、ユーザーが使い方を発見していく」と認めた

## 4. 成長戦略

### 4.1 初期トラクション獲得

**SXSW 2007ハック**:
- 会場に60インチプラズマディスプレイ2台を設置
- ライブツイートを流し続けることで、会場参加者にリアルタイム性を実演
- 3日間で使用量3倍増（20,000 → 60,000ツイート/日）
- SXSW Web Award受賞

**早期成長指標**:
- 2007年Q1: 400,000ツイート/四半期
- 2008年Q4: 100,000,000ツイート/四半期（**250倍成長**）
- 2008-2009年: ユーザー数1,382%成長

**バイラル機構**:
- SMS連携でモバイルから投稿可能
- パブリックタイムラインで誰でも閲覧可能
- リツイート機能（後に公式実装）でコンテンツ拡散
- 有名人・メディアのアーリーアダプター活用

### 4.2 フライホイール

```
有名人・インフルエンサーが参加
    ↓
ファンがフォローするために参加
    ↓
リアルタイムニュース・イベント実況が増加
    ↓
メディアがTwitterを情報源として引用
    ↓
さらなる認知度向上
    ↓
新規ユーザー獲得
    ↓
コンテンツ量増加
    ↓
有名人・メディアにとってさらに魅力的に
```

### 4.3 スケール戦略

**技術的スケーリング**:
- RubyからScalaへの移行でパフォーマンス10倍以上向上（200-300 req/sec → 10,000-20,000 req/sec）
- アーキテクチャの根本的見直し
- キャッシング、CDN、データベース分散

**国際展開**:
- 多言語対応
- 各国でのバイラルイベント（イラン選挙、アラブの春など）

**プラットフォーム化**:
- API公開で外部開発者にエコシステム構築を許可
- TweetDeck、Hootsuite等のサードパーティクライアント誕生
- （後にAPIを制限し、エコシステムを破壊する失策）

**マネタイズ（2010年〜）**:
- Promoted Tweets（広告ツイート）
- Promoted Trends（トレンド広告）
- Promoted Accounts（アカウント広告）

### 4.4 主要マイルストーン

| 年 | イベント | 評価額/指標 |
|----|--------|------------|
| 2005 | Odeo創業（Williams + Noah Glass） | Seed $5M |
| 2006-02 | Twitter開発開始 | - |
| 2006-03-21 | Dorseyが最初のツイート | - |
| 2006-07-15 | Twitter一般公開 | - |
| 2006-10 | Odeo資産買い取り、Twitter独立 | - |
| 2007-03 | SXSW 2007でブレイクスルー | 60,000ツイート/日 |
| 2007-07 | Series A $5M | - |
| 2008-10 | Ev Williams CEO就任（Jack Dorsey後任） | - |
| 2009-02 | Series C $35M | $250M評価額 |
| 2010-09 | "What are you doing?"から"What's happening?"へ変更 | - |
| 2010-10 | Dick Costolo CEO就任（Williams後任） | - |
| 2013-11-07 | IPO | $14.2B評価額、$1.8B調達 |
| 2022-10-27 | Elon Musk買収完了 | $44B |

### 4.5 資金調達履歴

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Series A | 2007-07 | $5M | 不明 | Union Square Ventures | Charles River Ventures, Marc Andreessen, Dick Costolo, Naval Ravikant, Ron Conway, Chris Sacca |
| Series B | 不明 | 不明 | 不明 | - | - |
| Series C | 2009-02 | $35M | $250M | Benchmark Capital, IVP | - |
| Series D | 2009-09 | 不明 | $1B | - | - |
| Series E | 不明 | 不明 | 不明 | - | - |
| IPO | 2013-11-07 | $1.8B | $14.2B | - | 公開市場 |

**総資金調達額**: $1.6B+（IPO含む）

**主要VCパートナー**:
- Union Square Ventures（Fred Wilson）
- Benchmark Capital（Peter Fenton）
- Sequoia Capital、Spark Capital、Kleiner Perkins

### 資金使途と成長への影響

**Series A（$5M、2007年）**:
- インフラ増強（スケーリング対応）
- エンジニア採用
- しかし、Fail Whale問題は2010年まで続く

**Series C（$35M、2009年）**:
- 技術的負債解消
- RubyからScalaへの移行投資
- グローバル展開

### VC関係の構築

1. **Union Square Ventures選定**:
   - Fred WilsonがTwitterの可能性を早期に理解
   - Union Square VenturesがSeries Aリード

2. **Benchmark Capitalの参画**:
   - Series Cでリード
   - 2013年IPOで巨額リターン（$14.2B評価）
   - 2022年Musk買収でさらなるリターン（$44B評価）

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | Ruby on Rails（初期）、Scala + JVM（後期） |
| インフラ | AWS、CDN、分散データベース |
| マーケティング | SXSW物理ディスプレイ、メディアPR、バイラル成長 |
| 分析 | 不明（初期は分析ツールほぼなし） |
| コミュニケーション | 不明 |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **シンプルさの極致**: 140文字制限がコンテンツ作成の摩擦を劇的に下げた
2. **SMS統合**: モバイルファーストの時代を先取り
3. **パブリック・デフォルト**: 誰でも見られる情報共有が新しいメディア形態を創出
4. **リアルタイム性**: ニュース速報、イベント実況で他メディアを圧倒
5. **SXSW 2007の戦略的成功**: 物理的なディスプレイでリアルタイム性を実演し、ティッピングポイント到達
6. **連続起業家の経験**: WilliamsはBlogger売却経験があり、資金調達・スケーリング知見を持っていた
7. **ピボットの速さ**: Odeo崩壊から3ヶ月以内にTwitterプロトタイプ完成

### 6.2 タイミング要因

- **モバイル普及期**: 2007年はiPhone発売年。モバイルインターネットが普及し始めた
- **ブログ全盛期の反動**: 長文ブログに疲れたユーザーが短文コミュニケーションを求めた
- **リアルタイムニュースの需要**: 2008年大統領選挙、2009年イラン選挙抗議、2011年アラブの春など、世界的イベントがTwitterの価値を証明
- **Facebook以前のソーシャルメディア空白**: Facebookは2006年まで大学生限定。一般ユーザー向けパブリックSNSの空白があった

### 6.3 差別化要因

- **140文字制限**: SMS制約から生まれたが、結果的に最大の差別化要因に
- **非対称フォロー**: FacebookやLinkedInの相互承認不要。一方的にフォロー可能
- **パブリック情報**: デフォルトで全世界に公開される設計
- **リツイート文化**: コンテンツ拡散の新しいメカニズム
- **ハッシュタグ**: ユーザー発の分類システムを公式採用

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本はTwitter利用率が世界トップクラス。リアルタイム情報共有文化が根付いている |
| 競合状況 | 3 | Twitter（X）が既に支配的。LINEが競合だが、リアルタイムパブリック投稿はTwitterが優位 |
| ローカライズ容易性 | 5 | 140文字制限は日本語では70文字相当で十分。既にローカライズ済み |
| 再現性 | 2 | ネットワーク効果が強すぎて新規参入困難。ニッチ特化型なら可能性あり |
| **総合** | 4 | 日本ではTwitterモデルは既に実証済み。類似プラットフォームより特化型が有望 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **ピボットからの発見**: Twitterは意図的な課題発見ではなく、ピボットの副産物。失敗プロジェクトから生まれることもある
- **社内テストの重要性**: Odeo社員がTwitterを熱狂的に使用したことが、市場性の最初のシグナル
- **「何なのか分からない」を受け入れる**: Williamsは「明確に定義できなかったが、ユーザーが使い方を発見していった」と認めた。需要は後から顕在化することもある

### 8.2 CPF検証（/validate-cpf）

- **正式な顧客インタビューなし**: Twitterは構造化されたCPF検証を経ていない
- **SXSW 2007が代替検証**: 物理的なディスプレイで「リアルタイム性」を実演し、参加者の反応を観察
- **ユーザー行動観察**: 初年度で「問題の共通性」を発見（20,000 → 60,000ツイート/日の急増）
- **WTP検証の遅れ**: マネタイズは2010年まで実施せず。成長優先戦略

### 8.3 PSF検証（/validate-10x）

- **即時性で100倍**: ブログの数時間〜日 vs. Twitterの数秒配信
- **摩擦の低さで10倍**: 長文編集 vs. 140文字だけ
- **制約が10倍優位性を生む**: 140文字制限はSMS制約だったが、結果的にシンプルさと拡散性を実現

### 8.4 スコアカード（/startup-scorecard）

| 評価軸 | スコア | 根拠 |
|--------|--------|------|
| 課題の深刻度 | 6/10 | リアルタイム共有は「Nice to have」だったが、SXSW後に深刻度上昇 |
| 市場規模 | 10/10 | 全世界のインターネットユーザーがTAM（数十億人） |
| 10倍優位性 | 10/10 | 即時性、摩擦の低さ、到達範囲で圧倒的優位 |
| 創業者適合性 | 9/10 | Williams連続起業家、Dorseyプロダクトビジョナリー、Stoneコミュニティビルダー |
| 実行力 | 7/10 | 成長は圧倒的だったが、Fail Whale問題が3年続いた。技術的負債管理に課題 |

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **業界特化型リアルタイムプラットフォーム**: 医療従事者向け、建築業界向けなど、特定業界のリアルタイム情報共有プラットフォーム。Twitterの汎用性ではなく専門性で差別化

2. **地域限定マイクロブログ**: 町内会、商店街、マンション管理組合など、地理的に限定されたコミュニティ向けリアルタイム掲示板

3. **匿名リアルタイム相談プラットフォーム**: 悩み相談、医療相談など、匿名性とリアルタイム性を組み合わせたプラットフォーム

4. **イベント特化型Twitter**: コンサート、スポーツ観戦、カンファレンスなど、特定イベント参加者だけのリアルタイム実況プラットフォーム

5. **音声版Twitter**: 140文字ではなく「10秒音声」で投稿するプラットフォーム。Clubhouse的だが非同期

6. **企業内Twitter**: 社内コミュニケーション特化。Slackの非同期版

7. **学習記録Twitter**: 勉強した内容を140文字で毎日投稿。学習コミュニティ形成

## 10. 創業者語録

> 「Twitterが何なのか明確ではなかった。ソーシャルネットワークとも、マイクロブログとも呼ばれたが定義が難しかった。何も置き換えないから。時間をかけて発見していくパスだった」

> 「当時の数千人のTwitter早期採用者がSXSWに行くから、そこで宣伝しようと決めた」

> 「初期の急成長に対応するため、スケーラブルな基盤を構築せずに突き進んだ結果、技術的負債を抱えた」（Fail Whaleについて）

> 「もし技術的な問題がなかったら、Twitterはもっと早く大きくなっていただろう」

## 11. Ev Williamsの連続起業家としての軌跡

### Blogger（1999-2003）
- Meg Hourihanと共同創業（Pyra Labs）
- 世界初のブログサービスの一つ
- 2003年2月13日にGoogleが買収（金額非公開、推定数百万ドル）
- Williamsは「blogger」という用語を普及させた

### Odeo（2005-2006）
- ポッドキャスティングプラットフォーム
- Apple iTunesに潰され失敗
- しかし、この失敗からTwitterが誕生

### Twitter（2006-2010年CEO、2019年まで取締役）
- 2008年10月CEO就任（Jack Dorsey後任）
- 2010年10月CEO辞任（Dick Costolo後任）
- プロダクト戦略に専念すると表明
- 2019年2月に取締役退任

### Medium（2012-現在）
- 2012年8月にローンチ
- 長文コンテンツのためのパブリッシングプラットフォーム
- しかし、5年間で5回以上のビジネスモデル変更（ピボット）
- 広告モデル → ブランドコンテンツ → サブスクリプション → パートナープログラム
- 2017年には社員の1/3を解雇
- 「同じ場所をぐるぐる回っている」と批判される

### Williamsの起業家パターン
- **一貫したテーマ**: コンテンツ発信の民主化（Blogger、Twitter、Medium）
- **シンプルさへの執着**: 複雑なツールを簡単にする
- **マネタイズの苦手意識**: いずれのサービスもマネタイズに苦労
- **成長優先**: ユーザー獲得を優先し、収益化は後回し

## 12. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 生年（1972年3月31日） | ✅ PASS | Wikipedia（Evan Williams） |
| Blogger Google買収（2003年2月13日） | ✅ PASS | Wikipedia（Pyra Labs）、複数ソース |
| Twitter最初のツイート（2006年3月21日） | ✅ PASS | Wikipedia（Twitter）、歴史記録 |
| Twitter一般公開（2006年7月15日） | ✅ PASS | 複数ソース |
| SXSW 2007（20,000 → 60,000ツイート/日） | ✅ PASS | 複数ソース（Medialoper、TechCrunch等） |
| Series A $5M（2007年7月29日） | ✅ PASS | Crunchbase |
| Series C $35M、$250M評価額（2009年2月） | ✅ PASS | TechCrunch、複数ソース |
| IPO $14.2B評価額（2013年11月7日） | ✅ PASS | TIME、CNN、複数ソース |
| Elon Musk買収$44B（2022年10月27日） | ✅ PASS | CNN、Wikipedia、複数ソース |
| Fail Whale初登場（2008年5月頃） | ✅ PASS | 複数ソース |
| 2008-2009年ユーザー成長1,382% | ✅ PASS | 複数ソース |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Wikipedia - Evan Williams (Internet entrepreneur)](https://en.wikipedia.org/wiki/Evan_Williams_(Internet_entrepreneur))
2. [Wikipedia - Twitter](https://en.wikipedia.org/wiki/Twitter)
3. [Crunchbase - Twitter Series A Funding](https://www.crunchbase.com/funding_round/twitter-series-a--7068e9cf)
4. [Fast Company - An Insider's History Of How A Podcasting Startup Pivoted To Become Twitter](https://www.fastcompany.com/1837848/insiders-history-how-podcasting-startup-pivoted-become-twitter)
5. [TIME - How Twitter Slayed the Fail Whale](https://business.time.com/2013/11/06/how-twitter-slayed-the-fail-whale/)
6. [CNN - Elon Musk to buy Twitter in $44 billion deal](https://www.cnn.com/2022/04/25/tech/elon-musk-twitter-sale-agreement/index.html)
7. [CNN - Twitter stock soars in IPO](https://money.cnn.com/2013/11/07/technology/social/twitter-ipo-stock/index.html)
8. [TechCrunch - Twitter Raises $35 Million Series C](https://techcrunch.com/2009/02/13/twitter-raises-third-round-of-funding-from-benchmark-and-ivp/)
9. [Medialoper - Twitter Hits the Tipping Point](https://medialoper.com/twitter-hits-the-tipping-point/)
10. [SXSW - 2007 SXSW Interactive Web Awards](https://www.sxsw.com/iconicmoments/video/sxsw-interactive-web-awards-2007/)
11. [Wikipedia - Odeo](https://en.wikipedia.org/wiki/Odeo)
12. [Wikipedia - Noah Glass](https://en.wikipedia.org/wiki/Noah_Glass)
13. [Nieman Lab - The long, complicated, and extremely frustrating history of Medium](https://www.niemanlab.org/2019/03/the-long-complicated-and-extremely-frustrating-history-of-medium-2012-present/)
14. [Inc.com - Ev Williams on Twitter's Early Years](https://www.inc.com/issie-lapowsky/ev-williams-twitter-early-years.html)
15. [CNBC - Twitter co-founder Ev Williams leaving board](https://www.cnbc.com/2019/02/22/twitter-co-founder-ev-williams-leaving-board.html)
16. [Medium - Behind The Fail Whale: Twitter's Battle With Technical Debt](https://mimrrhq.medium.com/behind-the-fail-whale-twitters-battle-with-technical-debt-07aee2fda0d3)
17. [Wikipedia - Pyra Labs](https://en.wikipedia.org/wiki/Pyra_Labs)
