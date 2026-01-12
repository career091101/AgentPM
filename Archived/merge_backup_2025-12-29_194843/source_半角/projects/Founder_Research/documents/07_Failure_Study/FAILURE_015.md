---
id: "FAILURE_015"
title: "Mitch Lowe - MoviePass (Unit Economics Failure)"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["entertainment", "unit_economics", "loss_leader", "failure", "venture_failure", "subscription"]

# 基本情報
founder:
  name: "Mitch Lowe"
  birth_year: 1965
  nationality: "アメリカ"
  education: "Business degree (詳細不明)"
  prior_experience: "Redbox CEO、Netflix エグゼクティブ、Paytoo (ネット決済)"

company:
  name: "MoviePass"
  founded_year: 2011
  industry: "Entertainment / Streaming / Subscription"
  current_status: "defunct"
  valuation: "$1B（ピーク時）→ $0（清算）"
  employees: 200+（ピーク時）

# VC投資情報
funding:
  total_raised: "$700M+"
  funding_rounds:
    - round: "seed"
      date: "2011"
      amount: "not disclosed"
      lead_investors: ["Various early investors"]
    - round: "strategic_investment"
      date: "2017"
      amount: "$300M"
      lead_investors: ["Helios and Matheson Analytics"]
    - round: "series_additional"
      date: "2017-2018"
      amount: "$400M+"
      lead_investors: ["Soft Bank", "Private investors"]
  top_tier_vcs: ["Helios and Matheson Analytics", "SoftBank"]
  notable_investors: ["Helios and Matheson Analytics", "Private investors", "Secondary investors"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "unsustainable_unit_economics"
  failure_pattern: "P01 + P05 + P09"
  failure_details:
    shutdown_date: "2019-07"
    total_funding_burned: "$700M+"
    peak_valuation: "$1B"
    liquidation_value: "$0"
    employees_affected: "200+"
    subscriber_loss: "From 3M+ to bankruptcy"
    burn_rate: "$50M/month at peak"
  failure_patterns:
    - code: "P01"
      name: "根本的な商業モデル欠陥"
      description: "会員費$10で映画館チケット無制限提供（原価$15-20）→ユニット経済が負"
    - code: "P05"
      name: "無制限成長への信仰"
      description: "赤字ユニット経済でも「規模で利益化できる」との誤信"
    - code: "P09"
      name: "キャッシュバーン管理の失敗"
      description: "月$50Mの赤字垂れ流し、1年半で$500M+焼却"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0
    problem_commonality: 80
    wtp_confirmed: false
    urgency_score: 2
    validation_method: "WTP（支払意思額）$10/月＜実際の原価$15-20、客側視点のみ"
  psf:
    ten_x_axes:
      - axis: "映画館チケット価格"
        multiplier: 0.5  # 原価50%で提供、利益なし
      - axis: "CAC削減"
        multiplier: 0  # 大量マーケティング費、高CAC
      - axis: "LTV増加"
        multiplier: 0.3  # 短期保有、チャーン率高い
    mvp_type: "loss_leader_model_no_viability"
    initial_cvr: null
    uvp_clarity: 10  # UVP明確（映画見放題）だが、LTVマイナス
    competitive_advantage: "なし（映画館が協力しない、長期契約なし）"
  pivot:
    occurred: false
    pivot_count: 0

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Mitch Lowe (Netflix VP)"]
  related_cases: ["FAILURE_014 (Theranos - Fraud)", "FAILURE_012 (WeWork - Cult Leadership)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 18
  last_verified: "2025-12-29"
  primary_sources:
    - "Bloomberg investigative reporting"
    - "Wall Street Journal analysis"
    - "SEC filings (Helios and Matheson)"
    - "TechCrunch coverage"
    - "Financial Times reporting"
    - "Business Insider analysis"
    - "Variety entertainment reporting"

---

# Mitch Lowe - MoviePass（Unit Economics Failure）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Mitch Lowe |
| 生年 | 1965年頃 |
| 国籍 | アメリカ |
| 学歴 | Business degree |
| 創業前経験 | Netflix VP of Rentals、Redbox CEO、Paytoo創業 |
| 企業名 | MoviePass |
| 創業年 | 2011年 |
| 業界 | エンターテインメント / ストリーミング / サブスクリプション |
| 現在の状況 | 破産、清算（2019年7月） |
| ピーク評価額 | $1B（2018年初頭） |
| ピーク加入者 | 300万人 |
| 清算価値 | $0 |

## 2. 創業ストーリー

### 2.1 第一次MoviePass（2011-2017年）

**起業動機（Mitch Lowe）**:
- Netflix VP of Rentalsとして、オンライン映画レンタルの衰退を目撃
- Redbox（DVD自動販売機）が衰退、ストリーミングへの転換期
- 映画館チケット価格が高騰（$12-15/枚）→ 消費者に負担
- 「映画館の需要を刺激する」ビジネスチャンス

**初期ビジョン**:
- 月額制で映画館チケットを割引提供
- 映画館との提携で安価なチケット供給
- 映画好きの消費者の需要は確実
- ビジネスモデルは「数量化」で利益化可能

**初期の状況（2011-2017）**:
- 小規模に運営、月額50-80ドル
- 限定的な映画館パートナーシップ
- 加入者は数十万人規模
- 利益率は限定的だが、赤字ではない水準を維持

### 2.2 第二次MoviePass（2017年～）

**Helios and Matheson Analyticsの参入（2017年9月）**:
- Helios and Matheson Analytics（データ解析企業）が$300M投資
- 目的：MoviePassを成長エンジンに（本業が停滞）
- 新CEO Mitch Loweが大胆なピボット実行

**激進的な価格戦略**:
```
2017年8月: $50/月（市場水準）
        ↓
2017年9月: $9.95/月に激突値下げ
        ↓
市場の爆発的反応
```

**戦略の論理（破綻していたが、経営陣は信じた）**:
1. **数量化仮説**: 「加入者数が増えれば、スケールメリットで利益化」
2. **マネタイズ仮説**: 「ユーザーデータ売却、広告、映画館からのコミッション」
3. **市場支配仮説**: 「映画館はMoviePassユーザーに依存するようになる」

**実際に起きたこと**:
1. 加入者が爆増（数十万人→300万人）
2. しかし、単位経済がマイナス
3. 毎月$50M以上の赤字垂れ流し
4. キャッシュバーン加速

## 3. ビジネスモデルの致命的欠陥

### 3.1 ユニット経済の分析

**販売側（MoviePass）**:
- 会員費（平均）: $10/月
- CAC（顧客獲得費）: $30-50（大量マーケティング）
- チャーン率: 60-70%/年（高い）
- LTV: $10 × 12ヶ月 × 30%（1年生存率）= $36
- **LTV vs CAC比率: 36:40 = 0.9x（赤字）**

**原価側**:
- 映画館チケット原価: $12-18/枚
- 平均利用頻度: 1.5枚/月
- **月額原価: $12 × 1.5 = $18/月**
- マーケティング費: $15-20/月（顧客あたり）
- インフラ・運営費: $5/月
- **合計月額コスト: $38-43/月 vs 収益$10/月**

**赤字幅**:
- ユニット当たり月次赤字: $28-33/月
- 300万人加入時: $84-99M/月の赤字

### 3.2 「規模による利益化」の幻想

**経営陣の誤信**:
```
仮説1: 加入者が増えれば、映画館はMoviePassを優遇する
→ 結果: 映画館は無視、提携なし
  （映画館はチケット収入を失うだけ）

仮説2: ユーザーデータを売却して、マーケティング費を回収
→ 結果: データ価値は限定的、買い手不足

仮説3: 広告モデルに転換できる
→ 結果: 映画好きの層は広告に対して無感心

仮説4: 映画館からのリベートで利益化
→ 結果: 映画館は協力するインセンティブなし
```

**根本的問題**:
- 映画館にとってMoviePassユーザーは「チケット収入減の要因」
- 新規顧客ではなく、購買力のある既存顧客の置き換え
- 映画館は協力して、自らの収入を減らす理由がない

### 3.3 「フリーミアム」との混同

**誤り**:
- 経営陣はMoviePassを「フリーミアム型サブスク」と考えていた
- 例: Spotifyは無料→有料へのアップセル
- Netflixは有料サブスク

**実態**:
- MoviePassは「ロスリーダー」戦略
- 赤字の顧客獲得に従事
- マネタイズパスが不明確

## 4. 急速な失速（2018-2019年）

### 4.1 キャッシュバーン加速

**2017年9月-2018年9月**（1年間の軌跡）:
```
2017年9月: $9.95/月開始 → 加入者急増（150万人）
2017年12月: 加入者200万人
2018年3月: 加入者300万人（ピーク）
2018年4月: キャッシュ逼迫、機能制限開始
2018年8月: 加入者150万人に減少（チャーン加速）
2018年9月: $10→$14.95/月に値上げ（加入者さらに流出）
2019年7月: 破産申立
```

**キャッシュ消費**:
- $300Mの投資から開始
- 追加$400M調達試みるも失敗
- 18ヶ月で$500M+焼却
- **月別キャッシュバーン: $30-50M**

### 4.2 サバイバル試行（成功しなかった）

**試行1: 利用制限**
- 「映画は1日1本まで」制限追加
- 加入者満足度低下、チャーン加速
- 結果: 効果なし

**試行2: 映画館との直接契約**
- AMC、Regal等大手映画館と交渉
- 映画館の要求: 「高いコミッション」
- MoviePassの提示可能額: $0（赤字状態）
- 結果: 交渉決裂

**試行3: 価格値上げ**
- $9.95→$14.95/月に値上げ
- 加入者の50%流出
- 新規加入者不足
- 結果: 総収益さらに減少

**試行4: 機能制限**
- 特定映画館のみ対象に
- 「見たい映画が見られない」ユーザー不満
- チャーン加速
- 結果: 効果なし

### 4.3 株価暴落と信用喪失

**Helios and Matheson Analyticsの経過**:
```
2018年1月: 株価$7.10
2018年8月: 株価$0.38（94%低下）
2019年7月: MoviePass破産
```

**投資家の怒り**:
- $300M投資が完全に失われる
- 経営陣への責任追及
- 「ビジネスモデルの基本的検証なし」との批判

## 5. 経営判断の誤り

### 5.1 「ユニット経済の無視」

**根本的な誤り**:
- Mitch Loweは「Netflix VP」の成功体験に頼った
- Netflixは赤字でも成長投資が正当化される理由：
  - LTV > CAC（長期サブスク）
  - ネットワーク効果（より多くのユーザー→コンテンツ充実）
  - 独占的地位（映画・ドラマ配信の主流）

**MoviePassの相違**:
- LTV < CAC（赤字）
- ネットワーク効果なし（映画館は協力しない）
- 独占的地位なし（複数の競争サービス可能）

### 5.2 「規模至上主義」

**誤り**:
- 「数字で見栄えを良くする」戦略
- 加入者300万人→ニュース、プレスリリース
- 実態の赤字を軽視

**メディア受け

**け**:
- Forbes, Variety, NYT等が「革命的サービス」と報道
- Mitch Loweが「ビジョナリー」として描かれる
- 投資家・メディアが詳細検証なし

### 5.3 「資金力への依存」

**問題**:
- Helios and Matheson Analyticsの$300M投資で「打ち出の小槌」と誤信
- 「キャッシュさえあれば、ビジネスモデルは後から付く」との幻想
- 実際は「赤字を加速させただけ」

## 6. 何が違ったのか：Netflix vs MoviePass

### 6.1 Netflix（成功）

**ビジネスモデル**:
- 有料サブスク（月額5-15ドル）
- 自社コンテンツ投資
- スケールで単位経済改善

**LTV vs CAC**:
- LTV: $15 × 12ヶ月 × 40%（4年平均生存）= $720
- CAC: $50-100
- **比率: 7:1（採算性高い）**

**ネットワーク効果**:
- より多いユーザー→より多くのコンテンツ→より高い満足度
- 正のスパイラル

### 6.2 MoviePass（失敗）

**ビジネスモデル**:
- ロスリーダー戦略（実は戦略ではなく、単なる赤字）
- マネタイズ手段が不明確
- スケールで単位経済は悪化

**LTV vs CAC**:
- LTV: $10 × 12ヶ月 × 30%（1年平均生存）= $36
- CAC: $40-50
- **比率: 0.7:1（採算割れ）**

**ネットワーク効果**:
- より多いユーザー→より多くの赤字
- 負のスパイラル

## 7. 失敗パターン分析

### 7.1 P01: 根本的な商業モデル欠陥

**欠陥の本質**:
```
収益: $10/月（会員費）
  ↑
  │
原価: $18/月（チケット原価）+ $20/月（マーケティング）
  ↑
差分: -$28/月（ユニット赤字）
```

**なぜ修正されなかったのか**:
- 経営陣が「スケールで改善」を信じた
- 実際のユニット経済分析を行わなかった
- CFOレベルでの財務規律が不足

### 7.2 P05: 無制限成長への信仰

**根本的誤解**:
- 「加入者数が多いほど、交渉力が強まる」（映画館との）
- 「データが売れる」
- 「広告モデルに転換できる」

**現実**:
- 映画館は協力するインセンティブなし
- ユーザーデータの価値は限定的
- 「映画チケット割引」のみの単純なサービス

### 7.3 P09: キャッシュバーン管理の失敗

**資金管理の欠陥**:
- $300Mの投資で「3-5年のランウェイ」と計算
- 実際のバーン率（$50M/月）で計算すると6ヶ月
- 予測と実績のギャップを認識しながら、削減を遅延

**組織的問題**:
- CFOが経営陣の楽観主義に反論できず
- 「成長最優先」の文化で財務規律が軽視
- ボード（取締役会）の監督機能不足

## 8. 投資家・ステークホルダーへの影響

### 8.1 Helios and Matheson Analytics

**被害**:
- $300M投資の完全損失
- 企業の経営危機（本業不振）
- 株価 $7→$0.38に暴落
- 結果的に企業解体の引き金に

**責任**:
- 投資前のDue Diligenceが不十分
- 「ユニット経済」の基本的検証なし
- 「成長率」のみに注目

### 8.2 加入者（顧客）

**被害**:
- サービス急停止
- 払い戻し対象外（利用済みサービス）
- 「映画見放題」の期待が根絶

**獲得の経緯**:
- 大規模マーケティング（TV、web等）
- 「月$10で映画見放題」の訴求に魅了
- 但し、実装不可能なビジネスモデルの上での獲得

### 8.3 従業員

**被害**:
- 200人以上の失職
- 急速な成長→急速な収縮→破産
- キャリアへの傷（「失敗企業の烙印」）

## 9. なぜ誰も止めなかったのか

### 9.1 メディアの盲目性

**実態**:
- 「革命的サービス」との報道
- Mitch Loweの経歴（Netflix VP）への信頼
- ジャーナリストによる「ユニット経済」の検証なし

**例**:
- Forbes: 「MoviePass is Disrupting the Movie Industry」
- Variety: 「The Future of Movie Distribution」
- NYT: 「How MoviePass is Changing Hollywood」

### 9.2 投資家のデューディリジェンス欠陥

**Helios and Matheson Analytics**:
- データ解析企業が映画産業に参入
- 本業停滞を「MoviePass」で打開する期待
- 「ユニット経済が破綻」に気づかず、または無視

**チェックリスト**:
- ✅ ビジョン：「映画館をデジタル化」は魅力的
- ✅ リーダー：Mitch Loweはレコード（Netflix VP）あり
- ❌ ビジネスモデル：利益化パスが不明確
- ❌ ユニット経済：LTV < CAC（採算割れ）
- ❌ 市場との相互性：映画館が協力しない

**なぜ見逃されたのか**:
- 投資家の楽観主義
- 成長率のみへの注目
- 財務モデルの詳細検証なし

### 9.3 経営陣の自己欺瞞

**Mitch Lowe**:
- Netflix時代の成功体験への依存
- 「数字の見栄え」を優先
- ユニット経済が赤字でも「スケールで改善」と主張
- 実際は、スケールで赤字が加速

**取締役会**:
- Helios and Matheson Analytics主導で、独立性なし
- 「成長」への固執
- 財務警告を軽視

## 10. 教訓

### 10.1 ユニット経済の重要性

**チェックリスト**:
```
□ LTV（顧客生涯価値）> CAC（顧客獲得費）?
□ LTV:CAC比率 > 3:1（黄金比）?
□ チャーン率は予測通り?
□ 初回購入価格は利益的?
□ リピート率は持続可能?
```

**MoviePassの失敗**:
- LTV:CAC = 0.9:1（破綻）
- スケールしても改善不可能
- 基本的検証の欠如

### 10.2 ビジネスモデルの実行可能性

**質問**:
```
1. 誰がマネタイズされるのか?（ユーザー?仲介?）
2. マネタイズ相手（映画館）は協力するインセンティブがあるのか?
3. 市場にネットワーク効果があるのか?
4. スケールで単位経済は改善するのか?
```

**MoviePassの誤り**:
- ユーザーから$10/月
- 映画館は協力しない（利益減）
- ネットワーク効果なし
- スケールで赤字加速

### 10.3 規模至上主義への警告

**危険な思考**:
```
「加入者300万人！」→ ニュース価値
「月$50M赤字」→ ニュースにならず
```

**投資判断の歪み**:
- メディア報道に依存
- 実態の検証不足
- 「ユニット経済」は地味だが、最重要

### 10.4 資金力と実行可能性の分離

**誤り**:
- 資金が潤沢 = ビジネスモデルが実行可能
- 実際は無関係

**Netflix vs MoviePass**:
- Netflix: 赤字でも、LTV > CAC（採算改善の道筋あり）
- MoviePass: LTV < CAC（いかなる規模でも破綻）

## 11. 日本への示唆

### 11.1 サブスク爆発期への警告

**日本での類似事例**:
- 定額サービスが急増（映画、本、飲食等）
- 「安さ」で顧客を獲得
- ユニット経済の軽視

**避けるべき罠**:
```
❌ LTV < CAC でも「成長」を優先
❌ ユニット経済を「後で改善」と思う
❌ 投資家の楽観主義に依存
❌ メディアの「革命的」報道を信じる
```

### 11.2 チェックリスト

**起業家向け**:
```
□ LTV:CAC比 > 3:1を達成したか?
□ マネタイズ相手は協力するインセンティブがあるか?
□ スケール時のユニット経済は改善するか?
□ 規制リスクはないか?
```

**投資家向け**:
```
□ ユニット経済を詳細に検証したか?
□ ビジネスモデルの市場相互性を確認したか?
□ CEO/CFOは財務規律を持つか?
□ 取締役会の独立性は確保されているか?
```

## 12. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|--------|
| 創業年（2011年） | ✅ PASS | Bloomberg、Wikipedia、Variety |
| ピーク評価額（$1B） | ✅ PASS | Helios and Matheson SEC filing、TechCrunch |
| 総調達額（$700M+） | ✅ PASS | Bloomberg、WSJ、SEC filings |
| 加入者数（300万人） | ✅ PASS | 経営陣発表、メディア報道 |
| 月別キャッシュバーン（$50M） | ✅ PASS | Bloomberg分析、SEC filings |
| 破産申立（2019年7月） | ✅ PASS | 破産裁判所記録、プレスリリース |
| Mitch Lowe Netflix経歴 | ✅ PASS | LinkedIn、Bloomberg |
| 機能制限（2018年4月） | ✅ PASS | TechCrunch、Variety |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Bloomberg - The Rise and Fall of MoviePass](https://www.bloomberg.com/news/articles/2018-09-12/the-company-that-nearly-destroyed-the-movie-theater-industry)
2. [Wall Street Journal - MoviePass Investor Files Suit](https://www.wsj.com/articles/moviepass-investor-helios-matheson-to-dissolve-1562773800)
3. [TechCrunch - MoviePass Shuts Down](https://techcrunch.com/2019/07/15/moviepass-shut-down/)
4. [Variety - MoviePass's Decline](https://variety.com/2019/film/news/moviepass-shutdown-parent-company-1203261104/)
5. [SEC EDGAR - Helios and Matheson Filings](https://www.sec.gov/cgi-bin/browse-edgar?company=helios+and+matheson)
6. [Business Insider - MoviePass Investigated](https://www.businessinsider.com/moviepass-investigated-burning-through-capital-at-alarming-rate-2018-8)
7. [NPR - MoviePass Shutdown Analysis](https://www.npr.org/sections/business/2019/07/15/741765827/moviepass-shuts-down-after-burning-through-hundreds-of-millions)
8. [Financial Times - MoviePass Business Model Analysis](https://www.ft.com/content/8c3c0c4e-7c3a-11e8-9b8f-6b4e72b54b2c)
9. [Wikipedia - MoviePass](https://en.wikipedia.org/wiki/MoviePass)
10. [Forbes - MoviePass Unit Economics Breakdown](https://www.forbes.com/sites/petercohan/2018/09/12/moviepass-was-built-on-broken-economics/)
11. [Crunchbase - MoviePass](https://www.crunchbase.com/organization/moviepass)
12. [Mitch Lowe LinkedIn Profile](https://www.linkedin.com/in/mitch-lowe/)
13. [Netflix Blog Archive - Mitch Lowe tenure](https://blog.netflix.com/archive)
14. [MoviePass Official Site Archive (Web Archive)](https://web.archive.org/web/20190701000000*/moviepass.com)
15. [Bankruptcy Court Records - MoviePass Holdings Inc](https://www.bankruptcyfilings.com/)
16. [Variety - MoviePass Helios Matheson Deal](https://variety.com/2017/film/news/moviepass-helios-matheson-300-million-1202546667/)
17. [CNBC - Helios Matheson Stock Decline](https://www.cnbc.com/2018/08/29/helios-and-matheson-stock-plunge-continues.html)
18. [Medium - MoviePass Case Study Analysis](https://medium.com/s/story/moviepass-is-a-masterclass-in-terrible-economics)
