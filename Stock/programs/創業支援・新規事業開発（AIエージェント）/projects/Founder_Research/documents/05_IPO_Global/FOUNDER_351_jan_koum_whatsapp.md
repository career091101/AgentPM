---
id: "FOUNDER_351"
title: "Jan Koum & Brian Acton - WhatsApp"
category: "founder"
tier: "legendary"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["sequoia_capital", "messaging", "mobile", "acquisition", "facebook", "immigrant_founder", "no_ads", "user_privacy"]

# 基本情報
founder:
  name: "Jan Koum (Co-founder), Brian Acton (Co-founder)"
  birth_year: 1976
  nationality: "Ukraine → USA (Jan Koum), USA (Brian Acton)"
  education: "San Jose State University (Koum - dropped out), Stanford University (Acton)"
  prior_experience: "Both worked at Yahoo! for 9+ years as engineers (1997-2007)"

company:
  name: "WhatsApp Inc."
  founded_year: 2009
  industry: "Mobile Messaging / Communication"
  current_status: "acquired"
  valuation: "$19B (Facebook acquisition, 2014)"
  employees: 55 (at acquisition)

# VC投資情報
funding:
  total_raised: "$60M"
  funding_rounds:
    - round: "seed"
      date: "2010-01-01"
      amount: "$257K"
      valuation_post: "不明"
      lead_investors: ["5 angels"]
      other_investors: []
    - round: "series_a"
      date: "2011-04-01"
      amount: "$8M"
      valuation_post: "$32M"
      lead_investors: ["Sequoia Capital (Jim Goetz)"]
      other_investors: []
    - round: "series_b"
      date: "2013-06-01"
      amount: "$52M"
      valuation_post: "$1.6B"
      lead_investors: ["Sequoia Capital"]
      other_investors: []
  top_tier_vcs: ["Sequoia Capital"]

# 成功/失敗/Pivot分類
outcome:
  category: "success"
  subcategory: "exit_success"
  exit_type: "acquisition"
  exit_date: "2014-02-19"
  exit_valuation: "$19B"
  acquirer: "Facebook (Meta)"
  exit_details: "$12B in Facebook stock + $4B cash + $3B restricted stock units"
  failure_pattern: ""
  pivot_details:
    count: 1
    major_pivots:
      - id: "pivot_001"
        trigger: "market_feedback"
        date: "2009-06-01"
        decision_speed: "3 months"
        before:
          idea: "Status update app (showing availability in contacts)"
          target_market: "iPhone users wanting to share status"
          business_model: "Unknown / ad-supported?"
          cpf_score: 3
        after:
          idea: "Free SMS alternative messaging app"
          hypothesis: "Users want to message each other, not just update status"
        resources_preserved:
          team: "Both founders stayed"
          technology: "Push notification infrastructure"
          investors: "Angel investors remained"
        validation_process:
          - stage: "organic_usage"
            duration: "3 months"
            result: "250K active users by end of 2009"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0
    problem_commonality: 75  # 推定: ['sequoia_capital', 'messaging', 'mobile', 'acquisition', 'facebook', 'immigrant_founder', 'no_ads', 'user_privacy']業界標準値、市場調査データ不足
    wtp_confirmed: true
    urgency_score: 8
    validation_method: "自己体験 + 友人グループでの実使用 + オーガニック成長観察"
  psf:
    ten_x_axes:
      - axis: "コスト"
        multiplier: 100
      - axis: "使いやすさ"
        multiplier: 5
      - axis: "導入障壁"
        multiplier: 3
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 9
    competitive_advantage: "完全無料、広告なし、シンプルなUI、プライバシー重視"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "market_feedback"
    original_idea: "ステータス更新アプリ"
    pivoted_to: "無料メッセージングアプリ（SMS代替）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-28"
  primary_sources:
    - "https://www.founderoo.co/playbooks/brian-acton-jan-koum-whatsapp-19-billion-business-that-started-with-rejection"
    - "https://www.bigtechontrial.com/p/the-bidding-war-how-sequoias-whisper"
    - "https://pitchbook.com/news/articles/facebooks-19b-acquisition-of-whatsapp-breaks-record"
    - "https://techcrunch.com/2015/02/19/crazy-like-a-facebook-fox/"
    - "https://en.wikipedia.org/wiki/WhatsApp"
---

# Jan Koum & Brian Acton - WhatsApp

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Jan Koum（メイン創業者）, Brian Acton（共同創業者） |
| 生年 | 1976年（Jan Koum） |
| 国籍 | ウクライナ→アメリカ（Koum）、アメリカ（Acton） |
| 学歴 | San Jose State University中退（Koum）、Stanford University（Acton） |
| 創業前経験 | Yahoo!でインフラエンジニアとして9年間勤務（1997-2007） |
| 企業名 | WhatsApp Inc. |
| 創業年 | 2009年 |
| 業界 | モバイルメッセージング/コミュニケーション |
| 現在の状況 | Facebook（Meta）に買収（2014年2月） |
| 評価額/時価総額 | $19B（買収時） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- **Jan Koumの原体験**: 1992年、16歳でウクライナからカリフォルニア州Mountain Viewに移住。母親とともに政府支援の2ベッドルームアパートに住み、食料配給券に頼る生活を送った。母親は癌と診断され、2000年に亡くなった
- **Yahoo!での経験**: 1997年にJan KoumがYahoo!にインフラエンジニアとして入社。Brian Actonと出会い、9年間一緒に働く。深夜のデバッグセッションと企業文化への不満を通じて絆を深めた
- **2007年の転機**: 両者ともYahoo!に幻滅し、2007年9月に退職。1年間南米を旅行し、フリスビーで遊びながら休暇を過ごした。両者ともFacebookに応募したが不採用
- **2009年1月**: KoumがiPhoneを購入し、7ヶ月前に開設されたApp Storeが全く新しいアプリ産業を生み出そうとしていることに気づいた
- **モバイルネットワークへの不満**: Koumは2000年代初頭のモバイルネットワークの信頼性の低さに不満を抱き、どんなネットワークでも動作するメッセージングプラットフォームを作りたいと考えた

**需要検証方法**:
- **形式的な顧客インタビューなし**: WhatsAppは伝統的な顧客検証手法を使用していない
- **自己使用による検証**: Koum自身と友人（特にロシア語話者の友人グループ）がSMSの代わりにWhatsAppをメッセージングツールとして使い始めた
- **オーガニック成長の観察**: ユーザーがステータスを更新するだけでなく、他のユーザーの更新に返信していることを発見。意図せず、SMSより高価な世界で無料メッセージングサービスを生み出していた

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 0（形式的なインタビューは実施せず）
- 手法: 自己体験 + 友人グループでの実使用 + オーガニック成長の観察
- 発見した課題の共通点:
  - SMSは高額（特に国際メッセージング）
  - キャリアによって料金体系が異なる
  - グループメッセージングが困難
  - プライバシーへの懸念（通信会社が全メッセージにアクセス可能）

**3U検証**:
- **Unworkable（現状では解決不可能）**: 8/10
  - SMSは1通あたり課金、国際メッセージは特に高額
  - グループメッセージングは技術的に制限あり
  - 既存の代替手段（Skype等）はデータ接続が必要で使いにくい

- **Unavoidable（避けられない）**: 9/10
  - モバイルコミュニケーションは現代生活に不可欠
  - 家族・友人との連絡手段として必須
  - ビジネスコミュニケーションにも必要

- **Urgent（緊急性が高い）**: 7/10
  - 毎日使用する必要がある
  - SMSコストは家計を圧迫（特に低所得者層）
  - リアルタイムコミュニケーションの必要性

**支払い意思（WTP）**:
- 確認方法:
  - 当初は無料提供（1年目）
  - 2年目以降$0.99/年の購読料を設定
  - 2016年に完全無料化
- 結果: ユーザーは少額（$1/年）であれば支払う意思あり、しかし無料化により爆発的成長を達成

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策（SMS） | WhatsApp | 倍率 |
|---|------------|-----------------|------|
| コスト | $0.10-0.25/メッセージ、国際SMS $0.50+ | $0（後に$0.99/年） | 100x+ |
| 時間 | 即時（ただし配信確認なし） | 即時 + 既読確認 | 1.5x |
| 使いやすさ | 電話番号のみ、文字数制限160文字 | 電話番号ベース、写真・動画共有可能 | 5x |
| 成果 | テキストのみ、グループ困難 | マルチメディア、簡単なグループチャット | 10x |
| 導入障壁 | キャリア契約必要 | アプリダウンロードのみ | 3x |

**MVP**:
- タイプ: Prototype（プロトタイプアプリ）
- 初期バージョン（V1.0, 2009年2月）:
  - ステータス更新機能のみ
  - 頻繁にクラッシュ
  - Koumは諦めようとしたがActonが「あと数ヶ月待って」と励ました
- V2.0（2009年8月）:
  - メッセージング機能を追加
  - Apple Push通知対応（2009年6月リリース）
  - アクティブユーザーが急増し250,000人に
- 初期反応: クラッシュ問題で低調 → Push通知対応後に急成長
- CVR: データなし（オーガニック成長のみ）

**UVP（独自の価値提案）**:
- **完全無料（後に$0.99/年）**: SMSと比較して圧倒的に安い
- **広告なし**: 「No Ads, No Games, No Gimmicks」を貫く
- **プライバシー重視**: エンドツーエンド暗号化、ユーザーデータを収集・販売しない
- **シンプルなUI**: 電話番号ベースで登録簡単、複雑な設定不要
- **クロスプラットフォーム**: iOS、Android、Windows Phone、BlackBerryに対応

**競合との差別化**:
- **Viber（2010年）**: 主に音声通話重視、WhatsAppはメッセージング特化
- **LINE（2011年）**: スタンプ・ゲーム等の追加機能多数、WhatsAppはシンプル維持
- **WeChat（2011年）**: 中国市場中心、多機能、WhatsAppはグローバル + シンプル
- **Kik（2009年）**: メールアドレス登録、若年層中心、WhatsAppは電話番号ベースで幅広い年齢層
- **BBM（BlackBerry Messenger）**: BlackBerryデバイス限定、WhatsAppはクロスプラットフォーム

## 3. ピボット/失敗経験

### 3.1 初期の失敗

**Facebook不採用（2007年）**:
- Yahoo!退職後、KoumとActonの両者がFacebookに応募
- 両者とも不採用
- 皮肉にも7年後にFacebookが$19BでWhatsAppを買収

**WhatsApp V1.0のクラッシュ問題（2009年2-5月）**:
- 初期バージョンは頻繁にクラッシュ
- ユーザー獲得が進まず
- Koumは諦めて新しい仕事を探そうとした
- Actonが「もう少し待って」と励まし、継続を決意

### 3.2 ピボット（該当する場合）

**ピボット: ステータス更新アプリ → メッセージングアプリ（2009年6月）**

- **元のアイデア**:
  - 連絡先メニューに表示されるステータス更新アプリ
  - ユーザーが「仕事中」「電話中」等のステータスを表示
  - SNS的な機能を想定

- **ピボット後**:
  - 無料SMS代替メッセージングアプリ
  - 個人間・グループメッセージング
  - マルチメディア共有（写真、動画、音声）

- **きっかけ**:
  - Apple Push通知機能のリリース（2009年6月）
  - ユーザーがステータスに返信する形でメッセージングを始めた
  - 「ユーザーはステータス更新だけでなく、互いにメッセージを送りたがっている」という気づき

- **学び**:
  - ユーザーの実際の使用パターンを観察することの重要性
  - 技術の進化（Push通知）が新しい可能性を開く
  - シンプルな機能に集中することで差別化できる
  - 広告なしモデルでも成長可能

## 4. 成長戦略

### 4.1 初期トラクション獲得

**オーガニック成長（2009-2011）**:
- **2009年8月**: WhatsApp 2.0リリース後、250,000アクティブユーザー
- **2011年初頭**: 米国Apple App Storeでトップ20アプリに
- **2011年10月**: 1日10億メッセージ処理
- **成長要因**:
  - ネットワーク効果: 友人が使っていると自分も使いたくなる
  - 口コミ: 広告なしのため完全に口コミベース
  - 国際展開: 多言語対応で世界中に拡大
  - シンプルさ: 電話番号ベースで登録簡単

**Jim Goetz（Sequoia Capital）との出会い（2010-2011）**:
- Goetzは8ヶ月間KoumとActonとの面会を試みた
- 当初VCを受け入れることに懐疑的だった創業者
- Goetzは「広告なし」の方針を尊重し、創業者の価値観に合致
- 2011年4月、Sequoia Capitalから$8M調達（15%以上の株式）

### 4.2 フライホイール

```
ユーザー増加
    ↓
ネットワーク効果（友人・家族が既に使用）
    ↓
新規ユーザーの導入障壁低下
    ↓
口コミによる拡散
    ↓
さらなるユーザー増加
```

**補強要素**:
- **プライバシー重視**: 広告なし、データ収集なしがユーザー信頼を獲得
- **クロスプラットフォーム**: どのデバイスでも使える汎用性
- **国際展開**: 多言語対応で新興国市場を開拓
- **シンプルさ**: 複雑な機能を追加せず、メッセージングに特化

### 4.3 スケール戦略

**爆発的成長期（2012-2014）**:
- **2012年4月**: 20億メッセージ/日
- **2012年8月**: 100億メッセージ/日
- **2013年2月**: 200M アクティブユーザー、50名のスタッフ
- **2013年6月**: 270億メッセージ/日（新記録）
- **2014年初頭**: 500M 月間アクティブユーザー
- **2014年2月（買収時）**: 465M 月間アクティブユーザー
- **2014年8月**: 600M+ アクティブユーザー

**スケール戦略の特徴**:
- **極めて少ないスタッフ**: 買収時わずか55名（1名あたり840万ユーザー）
- **インフラへの集中投資**: エンジニアリング重視、マーケティング費用ゼロ
- **プラットフォーム拡大**: iOS → Android → Windows Phone → BlackBerry → Web
- **新興国市場開拓**: インド、ブラジル、インドネシア等で爆発的成長

### 4.4 バリューチェーン

**技術スタック**:
- Erlang（サーバーサイド）: 高い並行処理能力
- FreeBSD（OS）: 安定性とパフォーマンス
- XMPP（プロトコル）: オープンスタンダードのメッセージングプロトコル
- SQLite（ローカルストレージ）: クライアント側のメッセージ保存

**運営モデル**:
- **最小限のスタッフ**: エンジニアリング中心の組織
- **広告なし**: ユーザー体験を最優先
- **サーバーコスト最適化**: 効率的なインフラ運用
- **顧客サポート**: 自動化とFAQで対応

## 4.5 資金調達履歴（VC案件のみ）

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Seed | 2010年 | $257K | 不明 | 5名のエンジェル投資家 | - |
| Series A | 2011年4月 | $8M | $32M | Sequoia Capital (Jim Goetz) | - |
| Series B | 2013年6月 | $52M | $1.6B | Sequoia Capital | - |

**総資金調達額**: $60M

**主要VCパートナー**:
- **Jim Goetz（Sequoia Capital）**: WhatsApp唯一のVCパートナー
- 取締役として参加
- 8ヶ月間創業者との面会を試み、信頼関係を構築
- 「広告なし」の方針を尊重

### 資金使途と成長への影響

**Series A（$8M, 2011年4月）**:
- **インフラ拡大**: サーバー容量増強、Erlangエンジニア採用
- **プラットフォーム拡大**: Android版開発（2010年8月開始済み）
- **成長結果**:
  - 2011年10月: 10億メッセージ/日達成
  - ARR: $0（広告なし、購読料なし） → 後に$0.99/年モデル導入

**Series B（$52M, 2013年6月）**:
- **グローバルインフラ**: 世界中のデータセンター拡充
- **エンジニア採用**: スタッフ50名体制に（それでも極少人数）
- **新機能開発**: 音声メッセージング、動画共有機能
- **成長結果**:
  - 2013年6月: 270億メッセージ/日
  - 2013年末: 400M+ 月間アクティブユーザー
  - ARR: 推定$10M-20M（$0.99/年 × 一部有料ユーザー）

### VC関係の構築

**1. Sequoia選考過程**:
- Jim Goetzが8ヶ月間追いかけた
- 創業者は当初VC受け入れに懐疑的（広告なしポリシーを守りたい）
- Goetzは「広告なし」を尊重し、創業者のビジョンに共感
- 2011年1月に初めて会合、4月に投資決定

**2. 投資家との関係維持**:
- Sequoiaのみを外部投資家として維持（他VCを入れず）
- Jim Goetzが取締役として積極関与
- 四半期ごとの戦略ミーティング
- M&A交渉でGoetzが重要な役割（Facebook、Googleとの交渉）

**3. Exit戦略**:
- 2013年後半からGoogle、Facebookが接触
- Jim Goetzが「ささやきキャンペーン」を主導し、複数企業間で競争を促進
- Google $10B オファー → Facebook $19B で決着
- Sequoiaの投資リターン: 約$3B（投資額$60Mに対し約50倍）

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発言語 | Erlang（サーバー）, Objective-C（iOS）, Java（Android） |
| サーバーOS | FreeBSD |
| プロトコル | XMPP（拡張版） |
| データベース | SQLite（クライアント側）, Mnesia（サーバー側） |
| クラウド | 独自データセンター（初期）→ AWS/自社DC混合 |
| 分析 | 独自開発の内部ツール |
| コミュニケーション | Email, WhatsApp自身（当然ながら） |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **ネットワーク効果の最大化**
   - 電話番号ベースで摩擦なく友人・家族を追加
   - 既存の連絡先をそのまま活用
   - クロスプラットフォーム対応で誰でも参加可能

2. **広告なし + プライバシー重視**
   - ユーザー体験を最優先
   - データ収集・販売をしない明確なポリシー
   - 「No Ads, No Games, No Gimmicks」の一貫性

3. **極めてシンプルなUX**
   - 複雑な機能を追加しない
   - メッセージング機能に特化
   - 誰でも直感的に使える

4. **オーガニック成長**
   - マーケティング費用ゼロ
   - 完全に口コミベース
   - 国際展開で新興国市場を開拓

5. **効率的な運営**
   - 買収時わずか55名のスタッフで465M ユーザー
   - 高度な技術力（Erlang使用）で少人数運営を実現
   - インフラコスト最適化

### 6.2 タイミング要因

- **スマートフォン普及期（2009-2014）**: iPhoneとAndroidの爆発的普及
- **データプラン普及**: モバイルデータが一般化し、データベースのメッセージングが可能に
- **SMS高コスト問題**: 特に国際SMSは依然として高額
- **Apple Push通知（2009年6月）**: リアルタイムメッセージングを可能にする技術革新
- **新興国市場の成長**: インド、ブラジル、インドネシア等でスマートフォン普及

### 6.3 差別化要因

- **完全無料 → 低価格（$0.99/年）**: 競合が広告モデルを採用する中、ユーザー課金モデル
- **プライバシーポリシー**: エンドツーエンド暗号化、データ収集なし
- **シンプルさ**: 機能追加競争に参加せず、メッセージングに特化
- **クロスプラットフォーム**: すべての主要OSに対応
- **Sequoia独占**: 他VCを入れず、Sequoiaのみとパートナーシップ

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | LINEが既に市場を独占、後発参入は困難 |
| 競合状況 | 2 | LINE、カカオトーク等が既に強固な地位 |
| ローカライズ容易性 | 4 | 技術的には容易だが、文化的差異（スタンプ文化等）に対応必要 |
| 再現性 | 3 | ネットワーク効果のある市場では先行者優位が極めて強い |
| **総合** | 3.0 | 日本では既にLINEが確立、WhatsAppのシンプルさは日本文化に合わない可能性 |

**日本市場への示唆**:
- ネットワーク効果が働く市場では先行者優位が極めて重要
- 日本市場は「シンプルさ」より「多機能」を好む傾向
- LINEのスタンプ文化、ゲーム統合等、日本独自のニーズが存在
- ただし、プライバシー重視の姿勢は今後重要性が増す可能性

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

**WhatsAppの需要発見プロセス**:
- 形式的な市場調査なし → 創業者自身の課題体験
- Jan Koumの移民体験 → 国際通信の重要性と高コストの実感
- Yahoo!時代のモバイル技術知識 → 技術的実現可能性の理解

**示唆**:
- 自己体験が最も強力な需要発見源となりうる
- 技術的バックグラウンドがあると実現可能性を評価しやすい
- グローバルな視点（移民体験）が新しい市場機会を発見させる

### 8.2 CPF検証（/validate-cpf）

**WhatsAppのCPF検証**:
- 形式的なインタビューゼロ
- 自己使用 + 友人グループでの実使用で検証
- オーガニック成長の観察でWTP確認

**示唆**:
- B2Cプロダクトでは「使ってもらう」ことが最良の検証
- 小規模な友人グループでのテストから始められる
- ユーザーの実際の使用パターンを観察することが重要
- 形式的なインタビューより実使用データの方が信頼性高い

**3U分析の適用**:
- **Unworkable**: SMS高コスト、グループメッセージング困難 → 明確な課題
- **Unavoidable**: モバイルコミュニケーションは現代生活に不可欠 → 高スコア
- **Urgent**: 毎日使用、コストが家計圧迫 → 高スコア

### 8.3 PSF検証（/validate-10x）

**WhatsAppの10倍優位性**:
- **コスト軸で100倍以上**: SMS $0.10-0.25 → WhatsApp $0（後に$0.99/年）
- **使いやすさで5倍**: 文字数制限なし、マルチメディア対応
- **導入障壁で3倍**: キャリア契約不要、アプリダウンロードのみ

**示唆**:
- 1つの軸で10倍以上の優位性があれば市場破壊可能
- WhatsAppの場合、コスト軸で100倍の優位性が決定的だった
- 複数の軸で小さな改善より、1軸での大きな改善の方が効果的

**MVP戦略**:
- V1.0は失敗（クラッシュ多発）→ 諦めずに継続
- V2.0でピボット（ステータス → メッセージング）→ 成功
- 技術変化（Push通知）を活用してMVPを進化

### 8.4 スコアカード（/startup-scorecard）

**WhatsAppのスコアカード評価**:

| 項目 | スコア | 根拠 |
|------|--------|------|
| 課題の深刻度 | 10/10 | SMS高コスト、グローバルコミュニケーション必須 |
| 市場規模 | 10/10 | 全世界のモバイルユーザーがターゲット |
| 10倍優位性 | 10/10 | コスト100倍、使いやすさ5倍 |
| ネットワーク効果 | 10/10 | 強力なネットワーク効果、先行者優位 |
| タイミング | 10/10 | スマートフォン普及期、データプラン一般化 |
| チーム | 9/10 | Yahoo!エンジニア、技術力高い、経営経験は少ない |
| ビジネスモデル | 7/10 | 初期は不明確、$0.99/年モデルも収益性低い |
| トラクション | 10/10 | オーガニック成長、マーケティング費用ゼロ |

**総合評価**: 76/80（95%）→ トップティアのスタートアップ

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **プライバシー重視型コミュニケーションアプリ（日本版Signal）**
   - LINE疲れ、データプライバシー懸念増加
   - 企業向けセキュアメッセージング
   - 医療、金融等の規制業界向け

2. **シニア向けシンプルメッセージングアプリ**
   - LINEは機能過多でシニアに複雑
   - 家族間コミュニケーション特化
   - 大きな文字、シンプルなUI、音声入力重視

3. **地域コミュニティ特化型メッセージング**
   - 町内会、PTAコミュニケーション
   - 災害時の連絡網
   - 高齢化地域の見守りネットワーク

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2009年） | ✅ PASS | Wikipedia, Founderoo, 複数記事 |
| 買収額（$19B） | ✅ PASS | PitchBook, TechCrunch, Facebook公式発表 |
| Sequoia投資額（Series A $8M） | ✅ PASS | 複数VC関連記事 |
| ユーザー数（買収時465M） | ✅ PASS | Business of Apps, Wikipedia |
| Jim Goetz追跡期間（8ヶ月） | ✅ PASS | Founderoo, Business of Business |
| Jan Koum移民背景 | ✅ PASS | Inc.com, 24/7 Wall St., 複数伝記記事 |
| 食料配給券使用 | ✅ PASS | BE Offices, Founder Billionaire |
| スタッフ数（買収時55名） | ⚠️ WARN | 50名と55名の記述が混在 |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ or 情報が若干矛盾）、❌ FAIL（確認不可）

## 参照ソース

1. [Brian Acton & Jan Koum · Whatsapp - Founderoo](https://www.founderoo.co/playbooks/brian-acton-jan-koum-whatsapp-19-billion-business-that-started-with-rejection)
2. [The Bidding War: How Sequoia's Whisper Campaign Led to A $19 Billion WhatsApp Buyout](https://www.bigtechontrial.com/p/the-bidding-war-how-sequoias-whisper)
3. [Facebook's $19B Acquisition of WhatsApp Breaks Record - PitchBook](https://pitchbook.com/news/articles/facebooks-19b-acquisition-of-whatsapp-breaks-record)
4. [A Year Later, $19 Billion For WhatsApp Doesn't Sound So Crazy - TechCrunch](https://techcrunch.com/2015/02/19/crazy-like-a-facebook-fox/)
5. [WhatsApp - Wikipedia](https://en.wikipedia.org/wiki/WhatsApp)
6. [The Rise of WhatsApp: Stats and Story Behind Its Global Success - TimelinesAI](https://timelines.ai/whatsapp-stats/)
7. [How Jan Koum Rose Up From Poverty to Sell His Business for $22B - Inc.com](https://www.inc.com/quora/how-jan-koum-rose-up-from-poverty-to-sell-his-business-for-22b.html)
8. [This Man Grew Up on Food Stamps, Now He's Worth $16 Billion - 24/7 Wall St.](https://247wallst.com/technology-3/2024/09/12/this-man-grew-up-on-food-stamps-now-hes-worth-16-billion/)
9. [WhatsApp co-founder: From food stamps to billionaire - BE Offices](https://www.beoffices.com/whatsapp-co-founder-from-food-stamps-to-billionaire)
10. [How Does WhatsApp Make Money? - Startupbooted](https://www.startupbooted.com/how-does-whatsapp-make-money)
11. [Jim Goetz - Wikipedia](https://en.wikipedia.org/wiki/Jim_Goetz)
12. [10 venture capitalists who made bold bets and scored massive returns - Business of Business](https://www.businessofbusiness.com/articles/10-bold-venture-capital-investments-massive-returns-Peter-Thiel-Jim-Goetz-Sequoia/)
13. [SMS Alternative: Viber vs WhatsApp - BSG Blog](https://bsg.world/blog/sms-alternative-viber-vs-whatsapp/)
14. [Jan Koum: The Inspirational Story of the Founder of WhatsApp - Leaders.com](https://leaders.com/articles/leaders-stories/jan-koum/)
15. [WhatsApp Revenue and Usage Statistics (2025) - Business of Apps](https://www.businessofapps.com/data/whatsapp-statistics/)
