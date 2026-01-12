---
id: "FAILURE_015"
title: "Lucas Duplan - Clinkle"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["fintech", "mobile-payments", "failure", "overfunding", "Stanford", "leadership", "PMF"]

# 基本情報
founder:
  name: "Lucas Duplan"
  birth_year: 1991 # 推定（2011年創業時19歳）
  nationality: "アメリカ"
  education: "Stanford University (B.S. Computer Science, 2012年、3年で卒業)"
  prior_experience: "StartX、Highland Capital Summer@Highland（加速プログラム）"

company:
  name: "Clinkle"
  founded_year: 2011
  industry: "フィンテック / モバイル決済 / 学生向け金融"
  current_status: "shutdown"
  valuation: "不明（調達額$30M）"
  employees: 70 # ピーク時、シャットダウン時は12名

# VC投資情報
funding:
  total_raised: "$30M"
  funding_rounds:
    - round: "seed"
      date: "2013-06"
      amount: "$25M"
      valuation_post: "不明"
      lead_investors: ["Accel Partners"]
      other_investors: ["Andreessen Horowitz", "Index Ventures", "Intel", "Intuit", "Peter Thiel", "Marc Benioff", "Diane Greene", "Mendel Rosenblum", "Owen Van Natta"]
    - round: "seed_extension"
      date: "2013-09"
      amount: "$5M"
      valuation_post: "不明"
      lead_investors: ["StartX Fund"]
      other_investors: ["Richard Branson"]
  top_tier_vcs: ["Andreessen Horowitz", "Accel Partners", "Index Ventures", "Peter Thiel", "Marc Benioff"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "shutdown"
  failure_pattern: "P02 + P12 + P28"
  failure_details:
    shutdown_date: "2016-05"
    total_funding_burned: "$30M"
    peak_valuation: "不明"
    liquidation_value: "ほぼゼロ（投資家への返金なし）"
    employees_affected: "70+"
    months_to_failure: 60 # 2011-2016年、実質プロダクトローンチ失敗
  failure_patterns:
    - code: "P02"
      name: "リーダーシップ問題"
      description: "24歳の初回創業者が大規模チームを管理できず、マイクロマネジメントと意思決定の不透明さで大量離職"
    - code: "P12"
      name: "PMF未達成のまま調達"
      description: "プロトタイプのみで$25M調達、市場検証なし、ユーザーニーズとミスマッチ"
    - code: "P28"
      name: "過剰調達（史上最大Seed）"
      description: "$25M Seedは当時史上最大、コンバーチブルノート構造で取締役会監督なし、焦点分散と高コスト体質"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0 # スタンフォードでのベータテストのみ、市場検証なし
    problem_commonality: null
    wtp_confirmed: false
    urgency_score: 3 # モバイル決済の需要はあるが、既存ソリューション（Square, Venmo）で満たされていた
    validation_method: "スタンフォードキャンパスでのベータテストのみ"
  psf:
    ten_x_axes:
      - axis: "決済技術（超音波Aerolink）"
        multiplier: 1.5 # 独自技術だが、NFCより優れていたわけではない
      - axis: "報酬システム"
        multiplier: 0.5 # ギミック的、ユーザーニーズとミスマッチ
      - axis: "ソーシャル機能"
        multiplier: 0.3 # Venmoに完敗
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 2 # コンセプトは不明瞭、頻繁に変更
    competitive_advantage: "超音波決済技術（Aerolink）、しかし競合優位性不足"
  pivot:
    occurred: true
    pivot_count: 2
    pivot_trigger: "プロダクト失敗、大量離職"
    original_idea: "超音波モバイル決済"
    pivoted_to: "デビットカード報酬システム → Treats（リファラルSDK）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Lucas Duplan"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 18
  last_verified: "2025-12-29"
  primary_sources:
    - "TechCrunch"
    - "Wikipedia"
    - "Inc.com"
    - "Business Insider"
    - "Entrepreneur"
    - "Forbes"
    - "Medium (TheBigCollapse)"
    - "Smartware Advisors"
    - "Harvard Business School (Platform RCTOM)"
    - "Dazeinfo"
---

# Lucas Duplan - Clinkle（失敗分析）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Lucas Duplan |
| 生年 | 1991年（推定） |
| 国籍 | アメリカ |
| 学歴 | Stanford University（B.S. Computer Science、2012年、3年で卒業） |
| 創業前経験 | StartX、Highland Capital Summer@Highland（加速プログラム） |
| 企業名 | Clinkle |
| 創業年 | 2011年（Duplan 19歳時） |
| 業界 | フィンテック / モバイル決済 / 学生向け金融 |
| 現在の状況 | 閉鎖（2016年5月、実質的にプロダクトローンチ失敗） |
| 評価額/時価総額 | 不明（総調達額$30M、清算価値ほぼゼロ） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- **2010年（19歳）**: Duplanはスタンフォード1年生の夏にロンドンへ留学
- ロンドンで飛行機を降りた直後、空腹で昼食を買いたかったが、新しい通貨での支払いに苦労
- 「スマートフォンから商店にシームレスに支払えるアプリがあればいいのに」と着想

**課題の具体化**:
1. **現金・カードの不便さ**: 特に国際旅行時の通貨変換の煩雑さ
2. **学生間の割り勘問題**: スタンフォードの学生が現金で割り勘するのは不便
3. **モバイル決済の未成熟**: 2011年当時、モバイル決済はまだ黎明期

**需要検証方法**:
- **スタンフォード内でのアイデア検証**: 教授Mehran Sahami（入門プログラミング講師）の指導を受ける
- **起業コース履修**: 最終学年でProfessor Charles Eesleyの起業コースに参加、仲間を集める
- **加速プログラム**: Highland Capital's Summer@Highland（2011年7月、$15,000助成金）、StartX（非営利加速プログラム）
- **2011年9月8日**: StartXのDemo Dayで初めて公開プレゼン

**初期の問題点**:
- **市場検証不足**: スタンフォードキャンパス内の限定的なベータテストのみ
- **ユーザーインタビューなし**: 創業者の仮説と周囲の友人の意見のみ
- **既存競合の軽視**: Square（2009年創業）、Venmo（2009年創業）が既に市場を開拓中

### 2.2 プロダクト開発

**初期コンセプト（2011-2013）**:
- **超音波決済技術「Aerolink」**: NFCの代替として、スマートフォンのスピーカーとマイクを使った高周波音による決済
- **P2P送金**: Venmo類似の友人間送金機能
- **報酬システム**: 決済時にポイントやギフトを獲得

**技術的特徴**:
- **超音波通信**: 特別なハードウェア不要、既存のスマートフォンで動作
- **インフラ優位性**: 小売店側の新しいハードウェア導入不要（理論上）
- **秘密主義**: 技術詳細を公開せず、NDAsを多用

**開発の遅延**:
- **2011-2013年**: 2年間にわたる開発、プロトタイプのみ
- **完全機能版の不在**: $25M調達時点でも、デモのみで完全機能版なし
- **過度なUI設計**: UIデザインに過度な時間を費やし、市場投入が遅延

**価格設定**:
- 当初無料を想定、後にデビットカード年会費を検討

## 3. 失敗の経緯

### 3.1 史上最大Seed調達と異常な期待（2013年6月）

**$25M Seed Round（史上最大）**:
- **2013年6月27日**: $25M Seed調達発表（当時Silicon Valley史上最大のSeedラウンド）
- **リード投資家**: Accel Partners（Jim Breyerが個人投資も）
- **その他投資家**: Andreessen Horowitz, Index Ventures, Intel, Intuit, Peter Thiel, Marc Benioff, Diane Greene, Mendel Rosenblum, Owen Van Natta

**構造的問題**:
- **コンバーチブルノート（転換社債）構造**: エクイティではなく、取締役会への投資家参加なし
- **監督の欠如**: Duplanは取締役会なしで、投資家の監督を受けずに経営
- **50人チームで$25M調達**: プロトタイプのみ、スタンフォードでのベータテストのみで巨額調達

**追加調達**:
- **2013年9月**: 追加$5M（StartX Fund、Richard Branson）
- **総調達額**: $30M

**メディアの過熱**:
- 「次世代のSquareキラー」として注目
- しかし、プロダクトの詳細は一切非公開
- NDA（秘密保持契約）を社員・投資家に強制

### 3.2 組織の崩壊（2013年12月）

**大量解雇（2013年12月）**:
- **30人以上が退職**: Business Insiderが報道
- **16人を解雇**: 全社員の約25%（オペレーション、グロース、人事部門）
- **わずか6ヶ月後**: $25M調達からわずか6ヶ月で大量解雇

**幹部の大量離職**:
- **Chi-Chao Chang（元Yahoo幹部）**: 入社1日で退職
- **Barry McCarthy（COO）**: 2014年3月に辞任
- **CFOとVP Engineering**: 2015年にApple M&A情報リークで解雇

**社員数の推移**:
- **ピーク時**: 70人
- **2015年**: 12人（大量辞任と解雇の結果）

### 3.3 リーダーシップの問題

**Duplanのマネジメントスタイル**:
- **マイクロマネジメント**: 明確なプロダクトロードマップなしで、細部に過度に介入
- **意思決定の不透明性**: 重大なプロダクト変更を単独で決定し、エンジニアに事後報告
- **オフィスに不在**: 自室に閉じこもるか、オフサイトで過ごすことが多い
- **情報の隠蔽**: 社員・投資家に重要情報を共有せず

**内部文化の問題**:
- **全体会議でのコメント**: 「我々はGoogleではない。Googleでは人々が自転車で笑顔で移動している。我々は海兵隊のようなものだ」
- **ヒエラルキーの明確化**: CEO Duplanは社員から離れ、閉鎖的
- **COO Barry McCarthyの暴言**: 部下に怒鳴ることが頻繁
- **オプション補償の曖昧さ**: 多くの社員がオプション条件の不明瞭さに不満

**Glassdoorレビュー**:
- 「これまでで最悪の職場体験」
- 「意思決定が一貫せず、リーダーシップが現実から乖離」

### 3.4 プロダクトローンチの失敗（2014年9月）

**ついにローンチ（2014年9月23日）**:
- **3年越しのローンチ**: 2011年創業から3年後
- **限定的リリース**: iOSとAndroidアプリ、一部大学のみ

**プロダクトの内容**:
- **超音波決済は見送り**: Aerolinkは実装されず
- **P2P送金**: Venmo類似の機能
- **プリペイドVisaカード**: Clinkleブランドのデビットカード
- **報酬システム「Treats」**: カード利用でギフトを獲得（ギミック的）

**問題点**:
- **差別化不足**: Venmo, Square Cash, PayPalと同等の機能のみ
- **超音波技術の不在**: 最大のセールスポイントが実装されず
- **報酬システムの不人気**: ユーザーが求めるのはシンプルな送金機能、ギミックではない
- **バイラル性ゼロ**: 話題にならず、ユーザー獲得失敗

### 3.5 ピボットとTreats（2015年1月）

**Treatsへの初回ピボット（2015年1月）**:
- 超音波決済、デビットカードを諦め、報酬プログラムに特化
- ユーザーが友人を招待すると、スロットマシン風のギミックで報酬獲得
- しかし、これも市場に受け入れられず

**さらなる崩壊（2015年5月）**:
- **7人が同時辞任**: CEO Duplanへの抗議で、同日に7人が辞職
- **チーム崩壊**: 残りはコンサルタント中心の12人以下
- TechCrunchが「Clinkle Implodes（崩壊）」と報道

### 3.6 最終ピボットとシャットダウン（2015年12月-2016年5月）

**Treats SDK（2015年12月）**:
- **B2B SDK**: 他のアプリがリファラル報酬システムを統合できるSDK
- Duplanは30%の手数料を徴収するビジネスモデル
- しかし、Duplanの失敗の評判で、クライアント獲得できず

**Clinkleブランドの隠蔽**:
- TreatsのウェブサイトにClinkleの名前を掲載せず（利用規約のみ）
- 創業者ピッチでもClinkleを言及せず

**シャットダウン（2016年5月）**:
- **2016年1月**: Forbesが「投資家が資金返還を要求」と報道
- **2016年5月**: ウェブサイトが消失、事実上のシャットダウン
- **投資家への返金**: なし（$30M全額消失）

## 4. 失敗パターン分析

### P02: リーダーシップ問題

**初回創業者の経験不足**:
- **19歳で創業**: 2011年、スタンフォード在学中に創業
- **24歳で$25M調達**: 巨額資金の管理経験なし
- **マネジメント経験ゼロ**: 70人規模の組織を管理できず

**マイクロマネジメントと不透明性**:
- 明確なビジョンなしで細部に介入
- 重大な意思決定を単独で行い、事後報告
- 社員・投資家に情報を共有せず、NDAで口封じ

**文化的ミスマッチ**:
- 「海兵隊」発言で、スタートアップ文化を否定
- トップダウンのヒエラルキー、閉鎖的な経営
- 社員のフィードバックを無視

**結果**:
- 幹部が1日で辞任（Chi-Chao Chang）
- COOが辞任（Barry McCarthy）
- 7人が同時辞職（2015年5月）
- 社員数が70人→12人に激減

### P12: PMF未達成のまま調達

**市場検証の欠如**:
- スタンフォードキャンパス内のベータテストのみ
- ユーザーインタビューなし
- プロトタイプのみで$25M調達

**PMFの誤解**:
- 「モバイル決済の不便さ」は本当にペインポイントか?
- Square, Venmo等の既存ソリューションで既に満たされていた
- 超音波決済は技術的にクールだが、ユーザーが求めていたわけではない

**競合分析の不足**:
- **Square（2009年創業）**: 小規模商店向けPOS、既に広く普及
- **Venmo（2009年創業）**: P2P送金、学生・若者に人気
- **PayPal**: オンライン決済の巨人
- **Square Cash, Google Wallet**: 2013年時点で競争激化

**Clinkleの立ち位置不明**:
- 超音波決済は結局実装されず
- P2P送金はVenmoのコピー
- 報酬システムはギミック的
- 差別化ポイントなし

**結果**:
- ローンチ後、ユーザー獲得失敗
- バイラル化ゼロ
- 3年の開発期間中に競合が市場を制覇

### P28: 過剰調達（Death by Overfunding）

**$25M Seedの弊害**:
- **当時史上最大**: 2013年6月時点でSilicon Valley史上最大のSeedラウンド
- **期待値の肥大化**: メディア・投資家の過度な期待
- **焦点の分散**: 超音波決済、P2P送金、報酬システム、デビットカードなど、全てを同時に開発

**コンバーチブルノート構造の問題**:
- **取締役会なし**: エクイティではなくコンバーチブルノート（転換社債）で調達
- **監督の欠如**: 投資家が取締役会に参加せず、Duplanに監督権限なし
- **説明責任の欠如**: 資金使途、進捗報告の義務が弱い

**非効率な資金使用**:
- **70人体制**: PMF前に70人雇用
- **高コスト体質**: オフィス、採用、マーケティングに過度な支出
- **3年の開発遅延**: UI設計、プロダクト改訂に時間を浪費

**投資家の期待プレッシャー**:
- $25M調達 → 「次のSquare」として期待される
- 現実的なIPOや買収の可能性低下
- ピボットやダウンサイジングの柔軟性なし（投資家の期待を裏切れない）

**結果**:
- $30M全額消失
- 投資家への返金なし
- Forbesが「Hall of Shame（恥の殿堂）」にDuplanを選出

## 5. 失敗から学ぶべき教訓

### 5.1 PMF検証の重要性

1. **仮説検証なしの大規模調達は危険**:
   - プロトタイプのみで$25M調達は時期尚早
   - 小規模MVP → ユーザー検証 → PMF達成 → 本格調達の順序を守る

2. **ユーザーインタビューの必須性**:
   - スタンフォードの友人の意見だけでは不十分
   - 最低50-100人のターゲットユーザーに深堀りインタビュー
   - 「モバイル決済の不便さ」は本当に深刻な問題か?

3. **競合分析の徹底**:
   - Square, Venmoが既に市場を開拓済み
   - 超音波決済は本当に10倍優れているか? （答え: NO）
   - 差別化ポイントが技術的に「クール」なだけでは不十分

### 5.2 リーダーシップの教訓

1. **初回創業者の自己認識**:
   - 19歳、マネジメント経験ゼロで$25M調達は無謀
   - 経験豊富なCOO, CFOを雇うべき（しかし、彼らも辞任した）
   - メンター、アドバイザーの助言を真摯に受け入れる

2. **透明性と情報共有**:
   - NDAで社員・投資家を縛るのは不信感を生む
   - 重要な意思決定は事前に共有し、フィードバックを得る
   - 「秘密主義」はプレスリリースには有効だが、組織には毒

3. **文化の構築**:
   - 「海兵隊」ではなく、協力的なスタートアップ文化
   - トップダウンではなく、ボトムアップのフィードバック
   - 社員のモチベーション、エンゲージメントを重視

### 5.3 調達構造の教訓

1. **コンバーチブルノートの危険性**:
   - 取締役会なし = 監督なし = 暴走リスク
   - エクイティで調達し、投資家を取締役会に入れる
   - 説明責任、透明性の確保

2. **適正な調達額**:
   - PMF前に$25Mは過剰
   - $1-3M程度のSeedで、MVP検証に集中
   - PMF達成後にSeries Aで本格調達

3. **投資家の選び方**:
   - 「有名VC」だけでなく、「手を動かすVC」を選ぶ
   - Andreessen Horowitz等のトップティアVCでも、取締役会なしでは機能しない
   - StartXのような加速プログラムはメンターシップが有効

### 5.4 プロダクト開発の教訓

1. **技術優先の危険性**:
   - 超音波決済は技術的にクールだが、ユーザーニーズとミスマッチ
   - NFCでもQRでも、ユーザーには違いがない
   - 「技術で差別化」ではなく「価値で差別化」

2. **開発速度の重要性**:
   - 3年の開発期間は長すぎる
   - 競合（Venmo, Square Cash）が市場を制覇
   - MVP → ローンチ → 改善の高速サイクル

3. **ソーシャル機能の重要性**:
   - Venmoはソーシャルフィード、絵文字で若者に人気
   - Clinkleは報酬ギミックに注力、ソーシャル要素が弱い
   - 決済アプリはネットワーク効果が命

## 6. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | 日本でもモバイル決済需要はあるが、PayPay, LINE Payが主流 |
| 競合状況 | 1 | PayPay, LINE Pay, 楽天Pay, d払い等が強い |
| ローカライズ容易性 | 2 | 決済システムは規制・インフラが国ごとに異なる |
| 再現性（失敗回避） | 5 | 失敗パターンから学ぶべき教訓が極めて多い |
| **総合** | 2.75 | 過剰調達とPMF不足の典型的失敗例 |

**日本市場での類似リスク**:
- モバイル決済市場は既にレッドオーシャン（PayPay等が独占）
- 技術的差別化（超音波決済等）はユーザーには不要
- 過剰調達は焦点分散と高コスト体質を生む

## 7. orchestrate-phase1への示唆

### 7.1 需要発見（/discover-demand）での注意点

- **創業者の体験を盲信しない**: Duplanのロンドンでの体験は個人的なペイン、市場全体のペインではない
- **既存ソリューションの検証**: Square, Venmo等で既に満たされている可能性
- **ペインポイントの深さ**: 「決済の不便さ」は本当に深刻か? 既存カードで十分では?

### 7.2 CPF検証（/validate-cpf）での注意点

- **ターゲットユーザーへのインタビュー必須**: スタンフォードの友人だけでは不十分
- **最低50-100人**: 学生、一般消費者、国際旅行者など、幅広いセグメント
- **WTP（支払意思額）**: 無料のVenmo, PayPayがある中で、有料や手数料を払うか?

### 7.3 PSF検証（/validate-10x）での注意点

- **10倍の優位性が必要**: 超音波決済はNFCやQRと比較して10倍優れているか? （答え: NO）
- **技術的優位性 ≠ ユーザー価値**: 技術がクールでも、ユーザー体験が10倍良くなければ無意味
- **ネットワーク効果**: 決済アプリは友人・商店の導入が必須、初期のクリティカルマスが重要

### 7.4 スコアカード（/startup-scorecard）での警告サイン

| 警告サイン | Clinkleの事例 |
|----------|------------|
| PMF検証なし | スタンフォードベータテストのみ、市場検証なし |
| 過剰調達 | $25M Seed、当時史上最大 |
| リーダーシップ問題 | 19歳の初回創業者、マネジメント経験ゼロ |
| 取締役会なし | コンバーチブルノート構造、投資家監督なし |
| 競合優位性不足 | Venmo, Squareに劣る |
| 開発遅延 | 3年間、プロダクトローンチ失敗 |
| 大量離職 | 70人→12人、幹部が1日で辞任 |

## 8. 避けるべきパターン

日本のスタートアップが避けるべきこと:

1. **市場検証なしの大規模調達**: PMF前に$25Mは狂気の沙汰
2. **コンバーチブルノート構造の乱用**: 取締役会なしで監督を受けないのは危険
3. **初回創業者の過信**: 19歳で$25M調達は無謀、経験者のサポート必須
4. **技術優先のプロダクト開発**: 超音波決済はクールだが、ユーザーニーズとミスマッチ
5. **秘密主義の過度な使用**: NDAで社員・投資家を縛るのは不信感を生む
6. **競合分析の不足**: Square, Venmoという強力な競合を軽視
7. **組織文化の軽視**: 「海兵隊」発言で社員のエンゲージメントを破壊

## 9. Lucas Duplanのコメントと業界の反応

**Duplanのコメント（公開情報なし）**:
- Clinkleシャットダウン後、公式なコメントなし
- メディアからの取材を拒否

**2018年以降の動向**:
- **Universal Recognition Token**: ブロックチェーンベースの企業報酬マーケットプレイスに投資
- **ベンチャーキャピタルファンド**: 報道によると、投資ファンド設立（LinkedInには記載なし）
- **低姿勢**: LinkedInプロフィールはTreatsの創業者としてのみ記載、Clinkle言及なし

**業界の反応**:
- **Forbes**: 2022年、Duplanを「Hall of Shame（恥の殿堂）」に選出、「取り消したい10選」に含む
- **TechCrunch**: 「Clinkle Implodes（崩壊）」と報道
- **Business Insider**: 「Stanford出身の21歳が$30M調達し、全てを吹き飛ばした」
- **ハーバードビジネススクール**: ケーススタディ「1年で有望なユニコーンから完全な失敗へ」

**教訓としての位置づけ**:
- Clinkleは過剰調達、PMF不足、リーダーシップ問題の三重苦の典型例
- ビジネススクール、スタートアップ加速プログラムで「避けるべき事例」として教材化
- Silicon Valleyの「ハイプ（過度な期待）」の危険性を象徴

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2011年） | ✅ PASS | Wikipedia, Business Insider |
| 総調達額（$30M） | ✅ PASS | TechCrunch, Wikipedia, Fortune |
| Seed額（$25M、史上最大） | ✅ PASS | Business Insider, Fortune, AllThingsD |
| Seed調達日（2013年6月） | ✅ PASS | Fortune, AllThingsD |
| シャットダウン時期（2016年5月） | ✅ PASS | Wikipedia, Dazeinfo |
| 大量解雇（2013年12月、30人以上） | ✅ PASS | TechCrunch, Wikipedia |
| 7人同時辞職（2015年5月） | ✅ PASS | TechCrunch |
| 超音波決済技術「Aerolink」 | ✅ PASS | MIT Technology Review, TechCrunch |
| コンバーチブルノート構造 | ⚠️ WARN | 複数ソースで間接的に確認、直接確認は1ソースのみ |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [TechCrunch - Clinkle Implodes As Employees Quit In Protest Of CEO](https://techcrunch.com/2015/05/15/clunk/)
2. [TechCrunch - Payments Startup Clinkle Lays Off A Quarter Of Its Staff](https://techcrunch.com/2013/12/09/payments-startup-clinkle-lays-off-a-quarter-of-its-staff/)
3. [TechCrunch - Flaming Wreckage Of Clinkle Rebuilds As A Referral Service](https://techcrunch.com/2015/12/29/i-know-you-thought-it-was-dead-but/)
4. [Inc.com - Inside Clinkle: A Stanford Kid Got $30 Million and Then Everything Blew Up](https://www.inc.com/alyson-shontell/inside-story-clinkle-silicon-valley-disaster.html)
5. [Business Insider - A SILICON VALLEY DISASTER: A 21-Year-Old Stanford Kid Got $30 Million, Then Everything Blew Up](https://www.businessinsider.in/A-SILICON-VALLEY-DISASTER-A-21-Year-Old-Stanford-Kid-Got-30-Million-Then-Everything-Blew-Up/articleshow/33783802.cms)
6. [Wikipedia - Clinkle](https://en.wikipedia.org/wiki/Clinkle)
7. [Fortune - Clinkle raises $25 million to kill Square](https://fortune.com/2013/06/27/clinkle-raises-25-million-to-kill-square/)
8. [AllThingsD - Pressure on Payments Startup Clinkle as It Raises $25 million Round](https://allthingsd.com/20130627/pressure-is-on-stealth-payments-startup-clinkle-as-it-raises-25-million-from-big-name-investors/)
9. [Entrepreneur - $30 Million Disaster: What Went Wrong at Clinkle](https://www.entrepreneur.com/business-news/30-million-disaster-what-went-wrong-at-clinkle/233084)
10. [Medium (TheBigCollapse) - Clinkle: How a $30 Million Hype Machine Crashed Before Takeoff](https://medium.com/@thebigcollapse/clinkle-how-a-30-million-hype-machine-crashed-before-takeoff-a97a0d442881)
11. [Smartware Advisors - Case Study: Clinkle & the Cost of Misjudging Product-Market Fit](https://www.smartwareadvisors.com/pages/case-study-clinkle-the-pitfalls-of-misjudging-product-market-fit)
12. [Harvard Business School - Clinkle: How to go from a soon-to-be unicorn to complete failure in one year](https://d3.harvard.edu/platform-rctom/submission/clinkle-how-to-go-from-a-soon-to-be-unicorn-to-complete-failure-in-one-year/)
13. [Dazeinfo - The Curious Case of Clinkle: A startup that raised $30 Million, backed by Richard Branson, but failed measurably!](https://dazeinfo.com/2016/01/27/curious-startup-story-silicon-valley-clinkles-journey-payment-startup-sdk/)
14. [NextShark - Bad Entrepreneurs: 8 Reasons Clinkle's Lucas Duplan is the Worst Startup Founder Ever](https://nextshark.com/8-reasons-clinkles-lucas-duplan-is-the-worst-startup-founder-ever)
15. [POGEO - Clinkle Lucas Duplan: The Rise and Fall of Silicon Valley's $25M Startup](https://pogeo.co.uk/clinkle-lucas-duplan/)
16. [MIT Technology Review - Why Some Are Turning to Sound for Mobile Payments and More](https://www.technologyreview.com/2013/08/20/176938/why-some-are-turning-to-sound-for-mobile-payments-and-more)
17. [Yahoo Finance - The founder of notorious failed startup Clinkle is reportedly coming back with a blockchain project](https://finance.yahoo.com/news/founder-notorious-failed-startup-clinkle-231345945.html)
18. [Report On The Nation - Why Tech Startups Fail And How To Avoid It: Lessons From Clinkle](https://reportonthenation.com/2023/07/27/why-tech-startups-fail-and-how-to-avoid-it-lessons-from-clinkle/)
