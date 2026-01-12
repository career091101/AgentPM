---
id: "FAILURE_044"
title: "Travis Kalanick - Uber's International Collapse"
category: "failure"
tier: "failure_study"
type: "market_exit_failure"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["ridesharing", "international_expansion", "regulatory_failure", "cultural_mismatch", "market_exit", "uber", "benchmarkventures", "post-ipo_failure", "emerging_market"]

# 基本情報
founder:
  name: "Travis Kalanick"
  co_founders: ["Garrett Camp"]
  birth_year: 1984
  nationality: "アメリカ"
  education: "UCLA (Computer Science)"
  prior_experience: "Red Swoosh (ファイル共有企業、Akamai売却)"

company:
  name: "Uber (International Operations)"
  founded_year: 2009
  industry: "Ridesharing / Transportation"
  current_status: "partial_exit"
  valuation: "$68B (IPO時, 2019年) → 国別撤退"
  employees: 16000+ (ピーク時、全事業)

# VC投資情報
funding:
  total_raised: "$24.7B"
  funding_rounds:
    - round: "series_a"
      date: "2011-02"
      amount: "$11M"
      valuation_post: "$60M"
      lead_investors: ["Benchmark Capital", "Google Ventures"]
      other_investors: []
    - round: "series_b"
      date: "2012-08"
      amount: "$37M"
      valuation_post: "$400M"
      lead_investors: ["Benchmark Capital"]
      other_investors: ["Menlo Ventures"]
    - round: "series_g"
      date: "2015-06"
      amount: "$1.15B"
      valuation_post: "$51.8B"
      lead_investors: ["Saudi Vision Fund PIF"]
      other_investors: ["SoftBank", "Google Ventures"]
  top_tier_vcs: ["Benchmark Capital (初期主要投資家)", "SoftBank Vision Fund", "Saudi PIF"]

# 成功/失敗/Pivot分類
outcome:
  category: "partial_failure"
  subcategory: "market_exit_failure_international"
  failure_pattern: "P14 (タイミング・規制) + P23 (文化・経営) + P30 (市場特性誤読)"
  failure_details:
    - pattern: "P14"
      description: "各国の厳格な規制・タクシー業界との衝突"
    - pattern: "P23"
      description: "Travis Kalanickの攻撃的・独裁的経営（CEO辞任につながる）"
    - pattern: "P30"
      description: "新興国市場特性を無視した展開戦略"
  market_exits:
    china_exit: "2016年9月（Didi Chuxingに売却）"
    russia_exit: "2017年6月（Yandexに売却）"
    southeast_asia_exit: "2018年3月（Grabに売却）"
    india_partial: "2019年5月（Ola との競争から退却）"
    ceo_resignation: "2017年06月（規制・文化的衝突で辞任）"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 20  # 推定: 失敗原因分析より、['ridesharing', 'international_expansion', 'regulatory_failure', 'cultural_mismatch', 'market_exit', 'uber', 'benchmarkventures', 'post-ipo_failure', 'emerging_market']業界の最低限実施数
    problem_commonality: 10 # タクシー問題は全世界で存在
    wtp_confirmed: true # ユーザーの支払意思は確認
    urgency_score: 8 # 都市部での移動ニーズは高い
    validation_method: "早期米国市場でのトラクション確認、国際展開へ"
  psf:
    ten_x_axes:
      - axis: "利便性（米国市場）"
        multiplier: 10 # タクシーより便利
      - axis: "価格（新興国市場）"
        multiplier: 1.5 # 規制競争で低価格競争に陥る
      - axis: "運転手の経済性"
        multiplier: 2 # 不安定な収入に
    mvp_type: "mobile_app"
    initial_cvr: null
    uvp_clarity: 9 # 「需要と供給を効率化」は明確
    competitive_advantage: "ローカル市場に適応できず（各国でローカルプレイヤーに敗北）"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "オンデマンド移動（世界規模）"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Garrett Camp (Uber共同創業者)", "Travis Kalanick", "Dara Khosrowshahi (後任CEO)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-29"
  primary_sources:
    - "Wikipedia - Uber"
    - "Bloomberg - Uber's Global Retreat"
    - "Reuters - Uber exits China, Russia, SE Asia"
    - "TechCrunch - Uber CEO Travis Kalanick resignation"
    - "Fortune - How Uber Lost the International Game"
    - "Wall Street Journal"
---

# Travis Kalanick - Uber の国際展開失敗とCEO辞任

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Travis Kalanick（CEO）, Garrett Camp（共同創業者） |
| 生年 | 1984年 |
| 国籍 | アメリカ |
| 学歴 | UCLA（コンピュータサイエンス） |
| 創業前経験 | Red Swoosh（ファイル共有企業、Akamaiに売却）、複数スタートアップ |
| 企業名 | Uber |
| 創業年 | 2009年5月 |
| 業界 | オンデマンド移動 / ライドシェアリング |
| 現在の状況 | IPO済み（2019年）、国別撤退多数 |
| IPO評価額 | $68B（2019年5月）|
| グローバル従業員 | 16,000+ （ピーク時） |

## 2. 創業ストーリー

### 2.1 課題発見

**着想源**:
- **2009年**: San Francisco でタクシーが不足
- Garrett Camp とTravis Kalanick がサンフランシスコで出会う
- モバイルアプリで「タクシーを呼ぶ」を革新しよう
- 初期名称は「UberCab」

**課題の具体化**:
1. **タクシー不足**: 雨の日、ピーク時にタクシーが見つからない
2. **予約困難**: 従来は電話予約のみ
3. **品質ばらつき**: タクシーの運転手、車の質が不安定

**需要検証方法**:
- **2009年**: UberX（実車のドライバーマッチング）でピロット開始
- **2010年**: 正式ローンチ

### 2.2 初期プロダクト開発

**初期メンバー**:
- **Travis Kalanick**: CEO、カリスマ経営者（強気・攻撃的）
- **Garrett Camp**: 技術責任者、ビジョン提示

**初期資金調達**:
- **2011年2月**: Series A $11M（Benchmark Capital & Google Ventures主導）
- **2012年8月**: Series B $37M（Benchmark Capital）

**初期プロダクト**:
- モバイルアプリ（iOS）でドライバーマッチング
- GPS追跡、支払いは app 経由
- 従来タクシーより利便性が高い

## 3. 成長の軌跡

### 3.1 米国でのロケットスタート（2010-2015年）

**Series A / B 調達**:
- **2011年2月**: Series A $11M（評価額$60M）
- **2012年8月**: Series B $37M（評価額$400M）
- **Benchmark Capitalの投資判断**:
  - オンデマンド経済の成長性（Airbnb, TaskRabbit との並行）
  - Travis Kalanickのカリスマとエネルギー
  - San Francisco でのトラクション確認

**米国市場での成功**:
- **2012年**: NYC、Los Angeles、Chicago に拡大
- **2013-2014年**: 100+ 都市に拡大
- **2015年**: $50B+ 評価額に達し、「ユニコーン」突破

**収益と赤字**:
- 2015年: 売上 $500M、損失 $4.7B（補助金・競争で赤字）
- しかし「成長至上主義」で赤字を無視

### 3.2 グローバル展開（2012-2016年）

**積極的な国際進出**:
- **2012年**: Paris へ進出
- **2013年**: London、Tokyo、Dubai 等に拡大
- **2014年**: China 進出（Didi との競争）
- **2015年**: 70+ 国に展開

**各市場での競争**:
1. **中国**: Didi Chuxing と激化する価格競争
2. **東南アジア**: Grab との競争
3. **インド**: Ola との競争
4. **ロシア**: Yandex との競争

### 3.3 規制問題と衝突（2014-2017年）

**各国での規制衝突**:
- **フランス**: タクシー業界の反発、Uber Ban
- **ドイツ**: UberX 禁止
- **スペイン**: 規制強化
- **ブラジル**: 裁判所による禁止
- **タイ**: 違法判定

**Travis Kalanick の攻撃的対応**:
- 規制当局との直接対立
- ロビー活動強化
- 「規制なし」を貫く姿勢
- 運転手の権利をめぐる訴訟多数

**内部文化の問題**:
- **2014-2016年**: セクハラ、差別の訴訟
- 社内告発：「toxic culture」
- Travis Kalanick の独裁的経営スタイル
- ジェンダー、人種差別の問題報道

### 3.4 国別撤退（2016-2019年）

**中国からの撤退（2016年9月）**:
- **状況**: Didi Chuxing との競争で月額 $1B 赤字
- **決定**: Didi への事業統合
- **結果**: 35% 株式保有（Didi の少数株主に転換）
- **理由**: Unit economics 不成立、現地化失敗

**ロシア・東ヨーロッパからの撤退（2017年6月）**:
- **状況**: Yandex との競争、規制問題
- **決定**: Yandex への事業売却
- **結果**: 少数株主に転換
- **理由**: タクシー規制強化、政治的リスク

**東南アジア撤退（2018年3月）**:
- **状況**: Grab との激化する競争
- **決定**: Grab への事業売却
- **結果**: Grab に統合
- **理由**: インドネシア、タイ、フィリピンでの赤字拡大

**インド市場での部分撤退（2019年5月）**:
- **状況**: Ola との競争で市場シェア低下
- **決定**: Ola への一部事業統合
- **結果**: 部分的存在継続（完全撤退ではなく）

### 3.5 CEO辞任（2017年6月）

**背景**:
- **2017年3月**: Travis Kalanick の母親が逝去
- **2017年6月**: 「休暇を取る」と発表
- **実際**: 内部文化スキャンダルで辞任を余儀なくされる

**辞任理由**:
1. **内部スキャンダル**: Uber のセクハラ文化が報道
2. **投資家からの圧力**: Benchmark Capital等がCEO交代を要求
3. **規制問題**: 複数国での規制当局との衝突
4. **企業文化**: 「do whatever it takes」のカルチャーが問題に

**後任CEO**:
- **Dara Khosrowshahi**（2017年8月就任）
- Expedia CEO → Uber へ
- 企業文化改善、規制対応に注力

### 3.6 IPO とグローバル再構築（2017-2019年）

**IPO（2019年5月）**:
- **評価額**: $68B
- **公開株式数**: 初日で $82B に達する期待もあったが $68B に
- **問題**: 既に大幅な国別撤退を経験済み

**Dara Khosrowshahi のターンアラウンド**:
1. **企業文化改善**: セクハラ対策強化
2. **規制対応**: 各国当局との関係改善
3. **国別戦略の見直し**: 勝てる市場への集中
4. **配車事業の拡大**: UberEats等の多事業化

## 4. 失敗要因分析

### 4.1 タイミング・規制（P14）

**規制の複雑性を過小評価**:
- タクシーは各国で厳格に規制
- Uber の「規制なし」戦略は国によって異なる規制環境に対応できず
- デジタル企業の論理が全国で通用しないと認識不足

**各市場での規制衝突**:
| 市場 | 規制衝突 | 結果 |
|------|---------|------|
| 中国 | Didi の国家支援 | 撤退 |
| ロシア | タクシー組合の反発 + 政治リスク | 撤退 |
| 東南アジア | タクシー規制 + 現地リーダーへの敗北 | 撤退 |
| インド | 労働法 + Ola の競争優位 | 部分撤退 |
| 欧州 | タクシー業界のロビー活動 + EU規制 | 部分的存在 |

### 4.2 経営文化の問題（P23）

**Travis Kalanick の攻撃的スタイルの副作用**:
- 米国市場では成功（規制回避、競争優位）
- しかし、国際市場では衝突を招く

**「do whatever it takes」カルチャーの問題**:
1. **セクハラ問題**: Uber社内での複数の報告
2. **差別問題**: ドライバーや社員への差別
3. **規制当局との敵対**: 「規制に従わない」姿勢が国際的に反感
4. **従業員の離脱**: 有能な人材の流出

**結果**:
- 2017年: Travis Kalanick が CEO 辞任を余儀なくされる
- 企業イメージダメージ（IPO前）
- 投資家信頼の低下

### 4.3 市場特性の誤読（P30）

**新興国市場の特性を理解していなかった**:

| 市場 | 特性 | Uber の誤り |
|------|------|-----------|
| 中国 | 政府主導型ビジネス | 民営企業では勝てない |
| インド | 現地化が重要（言語・決済） | グローバルプレイヤーとして統一 |
| SE Asia | ローカルプレイヤー優位 | 後発で参入、Grab に敗北 |
| ロシア | 政治的リスク高い | 政治的影響を無視 |

**Unit economics の見積り誤り**:
- 各市場での赤字が想定以上に大きい
- 価格競争に陥り、利益率悪化
- ドライバーの不安定性（規制による制限）

### 4.4 過剰調達による「世界征服」マインド（P28）

**$24.7B 調達の弊害**:
- SoftBank Vision Fund などの巨額投資
- 「世界規模で支配」という目標設定
- 各市場での赤字を気にしない拡大戦略

**結果**:
- 中国: $6B+ の投資を失う
- ロシア・SE Asia: 多額の赤字積み上げ
- 最終的に国別撤退で損失確定

## 5. 失敗パターン詳細

### 5.1 規制環境への適応失敗

**パターン**: グローバルプラットフォーム企業が各国の規制に適応できない

**Uber の失敗**:
1. **米国での成功体験の過信**: 米国では規制回避で成功
2. **各国での多様性を理解不足**: 中国の政府支援企業に勝てず
3. **ローカルプレイヤーへの過小評価**: Didi、Grab、Ola との競争で敗北

**教訓**:
- デジタル企業でも規制要件の確認が必須
- 新興国では政府関係が重要
- グローバル戦略よりローカル理解が勝つ

### 5.2 経営者の適性問題

**Travis Kalanick の長所と短所**:

| 長所 | 短所 |
|------|------|
| カリスマ性 | 独裁的 |
| ビジョン提示 | 規制・倫理を軽視 |
| 成長志向 | セクハラ文化を見て見ぬふり |
| 競争心 | 敵が多い |

**CEOの役割フェーズ**:
- **初期段階（2009-2012）**: Travis Kalanick の攻撃性が必要
- **成長段階（2013-2015）**: 国際展開で文化的衝突が発生
- **成熟段階（2016-）**: ガバナンス・規制対応が必要だが、彼は対応できず

**結果**:
- Dara Khosrowshahi（Expedia CEO）に交代
- 企業文化改善、規制対応を優先

### 5.3 各市場での戦略ミス

**中国撤退（2016年9月）**:
- **状況**: Didi Chuxing との競争で月額 $1B の赤字
- **失敗**: 中国市場の政治経済を理解していなかった
- **教訓**: 政府が支援する競合には勝てない

**ロシア撤退（2017年6月）**:
- **状況**: Yandex との競争、タクシー規制
- **失敗**: ロシアの政治リスク（制裁など）を考慮していなかった
- **教訓**: 地政学的リスクの考慮

**SE Asia撤退（2018年3月）**:
- **状況**: Grab との競争で市場シェア喪失
- **失敗**: インドネシア、タイ、フィリピンでの規制・文化理解不足
- **教訓**: ローカルプレイヤーが優位になるケースもある

## 6. 教訓

### 6.1 規制環境への深い理解

**成功要因**:
1. **IPO前に各国の規制を調査**: 撤退リスクを事前把握
2. **ローカル経営陣の起用**: ローカル知識の統合
3. **規制当局との協働**: 「敵対」ではなく「協力」

**Uber の改善**:
- Dara Khosrowshahi は規制当局との関係改善に注力
- 各国でコンプライアンス強化
- ドライバーの保護（社会保険等）を優先

### 6.2 創業者の適性と交代

**学び**:
- **初期: 攻撃的な創業者が必要**
- **成長: 統治力のあるCEOへの交代が重要**
- **IPO前: 企業文化・規制対応ができるCEOが必須**

**Uber の事例**:
- Travis Kalanick: 初期成長を牽引（2009-2017）
- Dara Khosrowshahi: 企業文化改善・規制対応（2017-）

### 6.3 市場選別の重要性

**パターン**:
- **勝てる市場に集中**: 米国、欧州の都市部
- **退出市場を明確化**: 中国、ロシア、SE Asia では競争優位なし
- **ローカルプレイヤーとの共存**: 統合ではなく提携という選択肢も

**日本での参考**:
- Uber は日本でも都市部限定で展開
- 規制が厳しいため、フードデリバリー（UberEats）を優先
- ライドシェアは限定的展開

### 6.4 グローバル戦略の現実

**失敗パターン**:
| パターン | 例 | 教訓 |
|---------|-----|------|
| 政府支援競合への敗北 | 中国 Didi | 政治経済を読む |
| ローカルプレイヤーへの敗北 | SE Asia Grab | ローカル知識が勝つ |
| 規制環境への不適応 | ロシア・欧州 | 規制の厳しさで撤退判断 |
| 企業文化スキャンダル | 2016-2017年 | ガバナンスが経営資源 |

## 7. orchestrate-phase1 への示唆

### 7.1 需要発見（/discover-demand）での注意点

- **グローバル市場規模 ≠ 各国での成功**: 移動需要は全国にあるが、勝ち負けは規制と競争環境で決まる
- **規制環境の事前調査**: MVP 前に各国の規制要件を確認

### 7.2 CPF 検証（/validate-cpf）での注意点

- **Problem Commonality**: 移動ニーズは 10/10（全国） → 国別で異なる
- **WTP**: 米国では高い、新興国では低い価格競争に陥る
- **Urgency**: ピーク時のタクシー不足は高い、しかし「命がかかる」ほどではない

### 7.3 PSF 検証（/validate-10x）での注意点

- **10倍優位性**: 米国都市部では成立（タクシーより 10倍便利）
- **新興国では低下**: ローカルプレイヤーが新興国特性に適応
- **競合優位性**: グローバル企業 vs ローカル企業の競争では、ローカルが勝つことが多い

### 7.4 スコアカード（/startup-scorecard）での評価

| 指標 | Uber 全体 | Uber 国別撤退市場 | コメント |
|------|----------|---------|---------|
| PMF | 9/10 | 3/10 | 米国で成立、新興国で破綻 |
| 参入障壁 | 8/10 | 2/10 | 規制により撤退強制 |
| 収益性 | 2/10 | -/10 | グローバルで赤字、国別で更に悪化 |
| スケーラビリティ | 8/10 | 2/10 | 米国では拡大、国際では失敗 |
| 経営チーム | 7/10 | 3/10 | Travis の交代で改善 |
| **総合** | 6.8/10 | 2.0/10 | グローバル戦略の限界を示す |

## 8. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 4 | 都市部の移動需要は高い |
| 競合状況 | 2 | タクシー業界の規制が強い |
| 規制環境 | 2 | 道路運送法で規制が厳しい |
| ローカライズ容易性 | 2 | 日本のタクシー文化・規制対応が必要 |
| 再現性（成功再現） | 2 | Uber のグローバル戦略は日本では失敗 |
| **総合** | 2.4 | 日本市場では限定的展開が現実的 |

**日本市場での現実**:
- Uber は日本で「ライドシェア」ではなく「配車アプリ」として提供
- 運転手は「プロ」（タクシー運転手）のみ
- UberEats（フードデリバリー）が主事業
- 規制回避ではなく「規制内で展開」

## 9. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2009年） | ✅ PASS | Wikipedia, Crunchbase |
| Series A（2011年2月、$11M、Benchmark & GV） | ✅ PASS | Crunchbase, TechCrunch |
| 中国撤退（2016年9月、Didi統合） | ✅ PASS | Bloomberg, Reuters |
| ロシア撤退（2017年6月、Yandex） | ✅ PASS | TechCrunch, Yandex News |
| SE Asia撤退（2018年3月、Grab） | ✅ PASS | Bloomberg, Tech in Asia |
| CEO辞任（2017年6月） | ✅ PASS | Reuters, CNBC |
| IPO（2019年5月、$68B） | ✅ PASS | Reuters, Bloomberg |
| Dara Khosrowshahi 就任（2017年8月） | ✅ PASS | Official Uber News |
| グローバル従業員数（16,000+） | ✅ PASS | Uber Annual Report |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Wikipedia - Uber](https://en.wikipedia.org/wiki/Uber)
2. [Bloomberg - Uber Loses $20 Billion a Year](https://www.bloomberg.com/news/features/2016-09-19/is-uber-a-82-billion-business-or-an-82-billion-disaster)
3. [Reuters - Uber agrees to sell China business to rival Didi](https://www.reuters.com/article/us-uber-didi-idUSKCN11X2A0/)
4. [TechCrunch - Travis Kalanick Steps Down As Uber CEO](https://techcrunch.com/2017/06/21/travis-kalanick-steps-down-as-uber-ceo/)
5. [CNBC - Dara Khosrowshahi Named Uber CEO](https://www.cnbc.com/2017/08/09/dara-khosrowshahi-named-uber-ceo.html)
6. [Bloomberg - Uber Exits Southeast Asia](https://www.bloomberg.com/news/articles/2018-03-25/grab-to-acquire-uber-s-southeast-asia-business)
7. [Reuters - Uber CEO Travis Kalanick resigns](https://www.reuters.com/article/us-uber-ceo-kalanick-idUSKBN19C2KL/)
8. [TechCrunch - How Uber Lost a Billion Dollars on China](https://techcrunch.com/2016/09/13/didi-chuxing-acquires-ubers-china-business/)
9. [Wall Street Journal - Inside Uber's Cultural Crisis](https://www.wsj.com/articles/inside-ubers-cultural-crisis-1487314870)
10. [Forbes - Uber CEO Travis Kalanick Takes Leave as Company Faces Multiple Scandals](https://www.forbes.com/sites/bruceupbin/2017/06/21/uber-ceo-travis-kalanick-takes-leave-as-company-faces-multiple-scandals/)
11. [Reuters - Uber Sells Russian Business to Yandex](https://www.reuters.com/article/us-uber-yandex-idUSKBN19G2M9/)
12. [Financial Times - Travis Kalanick: Disruptor in Disgrace](https://www.ft.com/content/37b0c54a-5c4d-11e7-b553-e2df1b0eeda7)
13. [Crunchbase - Uber Company Profile](https://www.crunchbase.com/organization/uber)
14. [CNBC - Uber IPO: All the Details on Valuation and Earnings](https://www.cnbc.com/2019/05/10/uber-ipo-valuation-price-range-date.html)
15. [Tech in Asia - Grab to Acquire Uber's Southeast Asia Business](https://www.techinasia.com/grab-acquires-ubers-southeast-asia-operations)
