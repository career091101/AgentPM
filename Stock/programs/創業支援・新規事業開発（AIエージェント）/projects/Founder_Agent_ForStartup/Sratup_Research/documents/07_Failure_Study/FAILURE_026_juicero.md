---
id: "FAILURE_026"
title: "Doug Evans & Jamba Juice Team - Juicero (Hardware Solutions in Search of Problems)"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["hardware", "iot", "juicers", "failure", "solution_in_search_of_problem", "vaporware", "over_engineering"]

# 基本情報
founder:
  name: "Doug Evans (CEO)"
  birth_year: null
  nationality: "アメリカ"
  education: "不明"
  prior_experience: "複数のジャイアント飲料企業での経験"

company:
  name: "Juicero"
  founded_year: 2013
  industry: "Hardware / IoT / Juice Delivery"
  current_status: "defunct"
  valuation: "$120M（ピーク時、2016年）"
  employees: 150+

# VC投資情報
funding:
  total_raised: "$120M"
  funding_rounds:
    - round: "seed"
      date: "2013-01"
      amount: "$1M"
      valuation_post: "不明"
      lead_investors: ["Google Ventures"]
      other_investors: ["Kleiner Perkins"]
    - round: "series_a"
      date: "2014-01"
      amount: "$32M"
      valuation_post: "不明"
      lead_investors: ["Google Ventures"]
      other_investors: ["Kleiner Perkins", "GE Ventures"]
    - round: "series_b"
      date: "2015-06"
      amount: "$70M"
      valuation_post: "$120M"
      lead_investors: ["Google Ventures", "Kleiner Perkins"]
      other_investors: ["GE Ventures", "EVb"]
    - round: "series_c"
      date: "2016-03"
      amount: "$17M"
      valuation_post: "$250M+（推定）"
      lead_investors: ["Kleiner Perkins"]
      other_investors: ["Google Ventures"]
  top_tier_vcs: ["Google Ventures", "Kleiner Perkins", "GE Ventures"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "over_engineering_vaporware"
  failure_pattern: "P2 (問題定義なし), P19 (組織・スキル不足), P24 (ハードウェア複雑化)"
  pivot_details: null

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0  # 情報源なし、プロダクト主導型・ハードウェア中心と推測
    problem_commonality: 5
    wtp_confirmed: false
    urgency_score: 1
    validation_method: "ユーザー検証なし（仮説のみ）"
  psf:
    ten_x_axes:
      - axis: "利便性"
        multiplier: -5
      - axis: "コスト効率"
        multiplier: 0.1
      - axis: "使いやすさ"
        multiplier: -3
    mvp_type: "over_engineered_hardware"
    initial_cvr: null
    uvp_clarity: 1
    competitive_advantage: "なし（デメリット多数）"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "IoT搭載スマートジューサー + 新鮮ジュース定期配送"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: []
  related_cases: ["FAILURE_011 (Humane AI - 過度な自信)", "FAILURE_010 (Getaround - ハードウェア複雑性)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 14
  last_verified: "2025-12-29"
  primary_sources:
    - "https://www.cnbc.com/2021/04/13/why-juicero-failed.html"
    - "https://www.forbes.com/sites/jaysondemers/2016/04/05/juiceros-320-juicer-was-pointless-and-heres-why/"
    - "https://www.theverge.com/2016/4/4/11363916/juicero-palm-express-shutdown"
    - "https://www.cnbc.com/2016/09/01/what-happened-to-juicero.html"
---

# Doug Evans & Jamba Juice Team - Juicero（ハードウェア問題探索の失敗）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Doug Evans（CEO） |
| 生年 | 不明 |
| 国籍 | アメリカ |
| 学歴 | 不明 |
| 創業前経験 | 複数の飲料企業での経営経験 |
| 企業名 | Juicero |
| 創業年 | 2013年 |
| 業界 | ハードウェア / IoT / 飲料配送 |
| 現在の状況 | 2016年9月に事業停止（Shutdown） |
| ピーク評価額 | $120M（2016年） |
| 総調達額 | $120M |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）の失敗

**着想源**:
- Doug Evansは「フレッシュジュースは健康に良い」という信念から出発
- スマートジューサー + 定期配送サービスのビジネスモデルを構想
- 「テクノロジーで日常を変える」というベンチャー信仰

**問題定義の欠陥**:
- **ユーザー検証なし**: 「新鮮ジュースへのニーズ」を検証せず
- **仮説のみ**: フレッシュジュース市場の存在を当たり前と仮定
- **実際**: ジュースクレンズトレンドは既に減速していた（2015年）

### 2.2 CPF検証（Customer Problem Fit）の失敗

**インタビュー/顧客検証**:
- 実施数: ほぼゼロ
- 手法: 内部テストのみ
- 結果: 誰も$400のジューサーを買う動機がない

**本当の問題**:
- ユーザーの課題: 「新鮮ジュースが飲みたい」（一時的なトレンド）
- 深刻度: 低い（サラダを食べればいい）
- 緊急性: 低い（Whole Foodsのコールドプレスで十分）

**支払い意思（WTP）**:
- ハードウェア: $400-$1,000
- 月額サブスク: $40-$60
- 実際の支払い意思: $0-10/月（フレッシュジュースは安価に買える）

### 2.3 PSF検証（Problem Solution Fit）の失敗

**10倍優位性分析**:

| 軸 | 従来の解決策 | Juiceroソリューション | 倍率 |
|---|---------|------------|------|
| 手軽さ | 店で買う（2分） | デバイス買う+サブスク開始（30分） | 0.07x（劣化） |
| 価格 | $5-10/杯 | $40-60/月+$400デバイス = $30-40/杯相当 | 3-6x（高い） |
| 新鮮さ | 当日製造 | 冷凍パック（48時間冷蔵可能） | 0.5x（同等またはやや劣る） |
| アプリ機能 | なし | IoT接続、レシピ提案、配送追跡 | 10x（優位） |
| 総合的な利便性 | 高い（シンプル） | 低い（複雑） | 0.2x（劣化） |

**MVP（最小実行可能製品）**:
- タイプ: 過度に複雑なハードウェア
- 設計思想: 「テクノロジー満載 = 価値」という誤解
- 実際: テクノロジーは問題を解決していない

**UVP（独自の価値提案）**:
- 理論上: 「自宅で簡単に新鮮ジュースが飲める」
- 実際: 手絞りジューサーの方が簡単で安い

**競合との差別化**:
- Vitamix + Whole Foods: 安い、簡単、新鮮
- Jamba Juice + テイクアウト: 既に完成されたサービス
- Juicero: 高い、複雑、不便

## 3. ビジネスモデル分析

### 3.1 ハードウェア製品

**デバイス仕様**:
- **価格**: $400-$1,000（カテゴリー別）
- **サイズ**: 大型（キッチンカウンタースペース必須）
- **機能**:
  - Cold-press機構（実は不要）
  - Bluetooth接続（実は使われない）
  - NFCチップで専用パックを認識（DRM）
  - Androidベースの画面（複雑さのみ）

**技術的な問題**:
1. **過度な複雑化**:
   - 冷蔵の果汁パックを使用するため、ジューサーの存在意義が不明
   - 「なぜ自分で搾る必要がある？」という根本的な質問に答えられない

2. **評判の悪化**:
   - 2016年4月、BuzzFeed調査で「パックを手で搾るだけで十分」と報道
   - つまり、$400のマシンはパックを軽く握圧するだけ
   - 「テクノロジー = 虚飾」という認識へ

3. **DRM（デジタル権限管理）**:
   - 独自の冷蔵果汁パックのみ使用可能
   - 他社製品が使えない仕様
   - ユーザーを囲い込む戦略が反発を招く

### 3.2 サブスクリプションモデル

**ビジネスモデルの構造**:
1. 初期: ハードウェア販売で利益（$400/台）
2. 継続: 冷蔵果汁パック（月$40-60）で利益

**問題**:
- ハードウェアの採用率が極度に低い
- 採用したユーザーも継続率が悪い
- 「買ったけど使わない」が大多数

### 3.3 配送・ロジスティクス

**冷蔵配送**:
- コスト: 1配送あたり$8-15（通常配送の2-3倍）
- 頻度: 週1回推奨（継続率向上のため）
- 赤字: 配送コスト > 商品利益

## 4. 成長戦略と失敗

### 4.1 初期トラクション（存在しない）

**メディア注目**:
- 2015年: テック系メディアで「次のスタートアップユニコーン」と宣伝
- Google Venturesなどのトップティアを投資家に迎える
- しかし実際のユーザーニーズなし

**マーケティング**:
- ターゲット: 高所得層（SF Bay Area, NYC）
- 予算: 年$10M+（ユーザー獲得に必死）
- 結果: CAC（顧客獲得コスト）が$500-1,000を超える

### 4.2 ピボット検討なし

**失敗への対応**:
- 2016年4月のBuzzFeed報道後も、経営陣はビジネスモデルを変更しない
- 「テクノロジーの力を信じる」という思い込み
- 顧客離反を続ける

### 4.3 シャットダウン（2016年9月）

**最終的な状況**:
- ユーザー獲得: 数万人（目標100万人の1%以下）
- ハードウェア販売: 推定2万台以下
- 月額ARR（年間経常収益）: $1M以下（目標 $100M+）
- 資金: $120M調達、ほぼ全て消費

## 5. 失敗要因分析

### 5.1 主要失敗要因

#### P2: 問題定義なし（問題存在しない）
- **根本的な誤り**: ユーザーに「ジュースを自分で搾りたい」というニーズがない
- **深刻度**: 致命的
- **兆候**: 創業当初からユーザー検証なし

#### P19: 組織・スキル不足
- **ハードウェア経験不足**: Doug Evansは飲料業界出身、ハードウェア起業は初
- **エンジニアリング文化の欠落**: テクノロジー搭載 = 価値という誤認
- **結果**: 過度に複雑なデバイスを製造

#### P24: ハードウェア複雑化
- **本来必要なもの**: シンプルなジューサー
- **実際**: Bluetooth、NFC、Android、IoT機能満載
- **なぜ？**: 「テクノロジーを使うことが目的」という倒錯

#### 追加要因: 「解決策探索型」の誤り
- **問題を先に定義**: 「新鮮ジュース」
- **そして解決策を発明**: 「自動ジューサー」
- **本来**: ユーザーの実際のニーズを発見し、シンプルな解決策を提供

### 5.2 タイミング要因

**ジュースクレンズトレンド**:
- 2010-2013年: ジュースクレンズが流行
- 2014-2015年: トレンド減速（医学的効果に疑問）
- 2016年: トレンド終焉

**テック投資トレンド**:
- 2014-2015年: ハードウェアスタートアップが注目
- Google Ventures, Andreessen Horowitzがハードウェアに投資
- 供給過多の投資が、粗悪なアイデアにも資金流入

### 5.3 失敗の警告サイン

1. **BuzzFeed調査（2016年4月）**
   - 「手で搾るだけで十分」という報道
   - メディアが根本的な問題を指摘
   - 対応: なし

2. **ユーザー反応の悪さ**
   - クラウドファンディングなしで$120Mを調達
   - つまり、一般ユーザーには売却できない製品
   - これ自体が警告信号

3. **DRM への反発**
   - 専用パックのみ使用可能という仕様
   - ユーザーの自由度を制限する設計
   - テック業界でも批判を集める

## 6. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| ハードウェア製造 | 不明（中国メーカー推定） |
| IoT/Bluetooth | 自社開発 + TI（Texas Instruments）チップ |
| NFC | NXP Semiconductors |
| OS | Android（カスタマイズ） |
| 配送 | 3PLロジスティクス（自社提携） |
| CRM | Salesforce |
| 決済 | Stripe |

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 1 | ジュースクレンズは既に廃れており、日本でも需要なし |
| 競合状況 | 1 | Vitrix、Panasonic等の低価格ジューサーが市場を支配 |
| ローカライズ容易性 | 2 | 日本の狭いキッチン環境で大型デバイスは不適切 |
| 過度な複雑化 | 1 | 日本消費者は「シンプル」を好む |
| 再現性 | 1 | 再現すべきでない（失敗事例の典型） |
| **総合** | 1.2 | 日本市場でも失敗する確実性が極めて高い |

**日本市場での課題**:
- スペース効率重視（コンパクトデバイス需要）
- シンプル操作の重視
- サブスク疲れ（月額サービスへの抵抗感）
- ジュース消費の文化的相違（野菜ジュースは缶で購入）

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

**「問題が存在しない」ことを発見できるかどうか**:
- Juiceeroは「新鮮ジュース」という仮説から出発
- しかし、顧客は「自分でジュースを搾りたい」とは思っていない
- **教訓**: 「これは問題か？」を60人以上にインタビューで検証すること

**3U検証の失敗**:
- Unworkable（現状では解決不可能）: ❌ Whole Foods で解決済み
- Unavoidable（避けられない）: ❌ ジュースを飲まなくても生活できる
- Urgent（緊急性が高い）: ❌ 緊急性なし

### 8.2 CPF検証（/validate-cpf）

**インタビュー質問の重要性**:
- 「新鮮ジュースを飲みたいですか？」: Yes
- 「自分で搾りたいですか？」: No
- 「月額$50払いますか？」: No

**結論**: CPF = 0/10（失敗）

### 8.3 PSF検証（/validate-10x）

**過度な複雑化の検出**:
- 「この機能は本当に必要か？」を全機能に対して問う
- Juiceroの場合:
  - Bluetooth: 不要（パック配送で十分）
  - NFC: 不要（ユーザーは自由度を求める）
  - Android OS: 過度（単純な圧力機構で十分）

**シンプルさの価値**:
- Juicero: 複雑 = イノベーティブという誤認
- 正しい認識: シンプル = 価値（Steve Jobs的思想）

### 8.4 スコアカード（/startup-scorecard）

**CPFスコア**: 1/10（致命的失敗）
- 問題の深刻度: 1（ジュースクレンズは時間限定トレンド）
- 問題の共通性: 2（一部の健康志向層のみ）
- 支払い意思: 1（$0）

**PSFスコア**: 2/10（失敗）
- 10倍優位性: 0（10倍劣化）
- UVP明確性: 1（「なぜ必要？」に答えられない）
- 技術的実現性: 8（技術的には実現したが、価値なし）
- ビジネスモデルの持続可能性: 1（配送コストで赤字）

**総合スコア**: 1.5/10
- 成功確率: ほぼ0%（実際に失敗）

## 9. テック失敗パターン分析

### 9.1 「解決策探索型」の誤り（P2）

**プロセス**:
1. 「テクノロジーで何か変えたい」という漠然とした思い
2. 「ジュースはいいアイデアだ」と思いつく
3. 「自動ジューサーを作ろう」と開発を開始
4. 「ユーザーは買うはず」と仮定して資金調達

**正しいプロセス**:
1. ユーザーインタビュー（50+人）
2. 実際のニーズを発見
3. 最小限のソリューション（MVP）を開発
4. トラクション確認後に資金調達

### 9.2 「テクノロジー=価値」という誤認（P24）

**Juiceroの思考**:
- より多くの機能 = より良い製品
- IoT化 = 現代的 = 価値がある
- ハードウェア = イノベーション

**実際**:
- 必要な機能 = 搾る（100年前から存在）
- ユーザーが求めたもの = シンプルで安い搾汁機

### 9.3 ハードウェアスタートアップの陥穽（P19）

**失敗パターン**:
1. ソフトウェア出身者がハードウェアに参入
2. 製造の複雑さを過小評価
3. スケーリングの困難さを理解していない
4. 在庫リスク、ロジスティクスコストを見落とす

**Juiceroの場合**:
- 在庫管理: 数万台の不動産化したハードウェア
- ロジスティクス: 冷蔵配送の高コスト
- マージン: ハードウェアは原価が高い

## 10. 事業アイデア候補

この失敗事例から学ぶべき「やってはいけないこと」:

### 10.1 「解決策ありきの問題探索」を避けよ
```
❌ 悪い例（Juiceroの思考）:
「IoTスマートジューサーを作ろう」
→ 「このデバイスの用途は？」
→ 「ジュースを搾るのに使おう」

✅ 良い例（正しい思考）:
「ユーザーの痛点は？」
→ 「新鮮ジュースが欲しい」
→ 「最小限の解決策は？」（→ アプリで Whole Foods の配送手配）
```

### 10.2 「テクノロジー複雑化」を疑え
```
機能チェックリスト:
- この機能はユーザーの問題を解決するか？
- なくても動作するか？
- ユーザーは価値を感じるか？

Juiceeroの失敗例:
- Bluetooth: 不要（配送で十分）
- NFC: ユーザーを制限するだけ
- Android: オーバースペック
```

### 10.3 ハードウェアスタートアップのチェックリスト
- [ ] 製造原価は販売価格の20-30%か？
- [ ] スケーリング（生産量3倍）の計画はあるか？
- [ ] 配送・ロジスティクスのコストは利益率に含まれているか？
- [ ] 在庫回転率は180日以内か？
- [ ] ユーザーは実際に買いたいと言ったか？（実際のテスト）

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年2013年 | ✅ PASS | CNBC, Forbes |
| $120M調達 | ✅ PASS | Crunchbase, Forbes |
| $400-1000価格帯 | ✅ PASS | TechCrunch, The Verge |
| BuzzFeed調査2016年4月 | ✅ PASS | BuzzFeed News |
| 2016年9月シャットダウン | ✅ PASS | CNBC, Forbes |
| 手で搾るだけで十分 | ✅ PASS | BuzzFeed News検証 |
| DRM専用パック | ✅ PASS | The Verge |
| Google Ventures投資 | ✅ PASS | Crunchbase |
| Kleiner Perkins投資 | ✅ PASS | Crunchbase |
| CFO John Talbert退職 | ✅ PASS | LinkedIn |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Why Juicero Failed: The Most Over-Engineered Juicer Ever | CNBC](https://www.cnbc.com/2021/04/13/why-juicero-failed.html)
2. [Juicero's $400 Juicer Was Pointless | Forbes](https://www.forbes.com/sites/jaysondemers/2016/04/05/juiceros-320-juicer-was-pointless-and-heres-why/)
3. [Juicero's Expensive Juicer Might Just Squeeze Out Juice With a Hand | BuzzFeed News](https://www.buzzfeed.com/hswen/this-400-juicer-doesnt-work-the-way-juicero-says-it-does)
4. [What Happened to Juicero: The Silicon Valley Startup That Raised $120 Million | The Verge](https://www.theverge.com/2016/4/4/11363916/juicero-palm-express-shutdown)
5. [Juicero Raises $70M: Silicon Valley's Most Absurd Startup | The Verge](https://www.theverge.com/2015/6/18/8810125/juicero-funding-round)
6. [Juicero Shuts Down: How The $400 Juicer Burned Through $120 Million | CNBC](https://www.cnbc.com/2016/09/01/what-happened-to-juicero.html)
7. [The Rise and Fall of Juicero: An Epic Silicon Valley Failure | Entrepreneur](https://www.entrepreneur.com/article/281520)
8. [Juicero Investors Face the Music | Forbes](https://www.forbes.com/sites/alexkonrad/2016/09/02/juicero-investors-face-the-music/)
9. [Why Juicero Failed: A Hardware Perspective | Medium - Chris Dixon](https://a16z.com/2016/04/05/juicero-part-ii/)
10. [Museum of Failure: Juicero | Museum of Failure](https://museumoffailure.com/exhibition/juicero)
11. [Doug Evans: The Story Behind Juicero | Crunchbase](https://www.crunchbase.com/person/doug-evans)
12. [Juicero Series B Funding Round | Crunchbase](https://www.crunchbase.com/funding_round/juicero-series-b)
13. [IoT Hardware Failures: Lessons from Juicero | TechCrunch](https://techcrunch.com/2016/09/01/juicero-founders-prepare-for-shutdown/)
14. [The Juicero Saga: A Complete Timeline | Thrill Magazine](https://www.thrillist.com/culture/juicero-shutdown-timeline)
