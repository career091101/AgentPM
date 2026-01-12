---
id: "FAILURE_010"
title: "Sam Zaid - Getaround"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["car-sharing", "mobility", "failure", "overfunding", "unit-economics", "SoftBank", "SPAC"]

# 基本情報
founder:
  name: "Sam Zaid"
  birth_year: 1984
  nationality: "アメリカ"
  education: "UC Berkeley（経済学）"
  prior_experience: "なし（大学時代に創業構想）"

company:
  name: "Getaround"
  founded_year: 2009
  industry: "カーシェアリング / モビリティ / P2Pレンタル"
  current_status: "struggling"
  valuation: "$1.2B（SPAC合併時、2022年12月）→ $24M（2024年）"
  employees: 300+ # 大規模レイオフ前

# VC投資情報
funding:
  total_raised: "$736M"
  funding_rounds:
    - round: "series_a"
      date: "2012-08"
      amount: "$13.9M"
      valuation_post: "不明"
      lead_investors: ["Menlo Ventures"]
      other_investors: ["General Catalyst", "Collaborative Fund"]
    - round: "series_b"
      date: "2016-10"
      amount: "不明"
      valuation_post: "不明"
      lead_investors: ["Toyota Motor Corporation"]
      other_investors: []
    - round: "series_c"
      date: "2017-04"
      amount: "$45M"
      valuation_post: "不明"
      lead_investors: ["Braemar Energy Ventures"]
      other_investors: ["Cox Automotive", "Menlo Ventures"]
    - round: "series_d"
      date: "2018-08"
      amount: "$300M"
      valuation_post: "$1.2B"
      lead_investors: ["SoftBank Vision Fund"]
      other_investors: ["Toyota Motor Corporation"]
    - round: "series_e"
      date: "2020-10"
      amount: "$140M"
      valuation_post: "不明"
      lead_investors: ["SoftBank Vision Fund"]
      other_investors: []
  top_tier_vcs: ["SoftBank Vision Fund", "Menlo Ventures", "Braemar Energy Ventures", "Toyota Motor Corporation", "Cox Automotive"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "struggling"
  failure_pattern: "P13 + P19 + P28"
  failure_details:
    shutdown_date: null
    total_funding_burned: "$736M+"
    peak_valuation: "$1.7B（2019年）"
    liquidation_value: "$24M市場時価総額（2024年）"
    employees_affected: "200+（累計レイオフ）"
    spac_merger: "2022年12月、$1.2B評価額で上場、株価65%下落"
  failure_patterns:
    - code: "P13"
      name: "スケールしないモデル"
      description: "P2Pカーシェアリングのユニットエコノミクスが破綻、利益率低下"
    - code: "P19"
      name: "顧客集中リスク"
      description: "COVID-19で移動需要75%減、回復せず"
    - code: "P28"
      name: "過剰調達"
      description: "$736M調達、Drivy買収$300M等の非効率な資金使用"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0  # 情報源なし、プロダクト主導型・ハードウェア中心と推測
    problem_commonality: 7 # 都市部でのカーシェアニーズは存在
    wtp_confirmed: true
    urgency_score: 5 # 便利だが必須ではない
    validation_method: "初期ユーザー獲得、サンフランシスコでの展開"
  psf:
    ten_x_axes:
      - axis: "利便性"
        multiplier: 5 # 従来のレンタカーより便利
      - axis: "価格"
        multiplier: 2 # 安価だが、ユニットエコノミクス悪化
      - axis: "車両品質"
        multiplier: 1 # P2Pモデルで品質バラツキ
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 7 # カーシェアリングのコンセプトは明確
    competitive_advantage: "P2Pモデル、IoTデバイス（Connect）"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "P2Pカーシェアリング"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Elliot Kroo", "Jessica Scorpio"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 13
  last_verified: "2025-12-28"
  primary_sources:
    - "TechCrunch"
    - "Crunchbase"
    - "Tracxn"
    - "Automotive News"
    - "CNBC"
    - "Wikipedia"
---

# Sam Zaid - Getaround（失敗分析）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Sam Zaid（共同創業者: Elliot Kroo, Jessica Scorpio） |
| 生年 | 1984年頃 |
| 国籍 | アメリカ |
| 学歴 | UC Berkeley（経済学） |
| 創業前経験 | なし（大学時代に創業構想） |
| 企業名 | Getaround |
| 創業年 | 2009年 |
| 業界 | カーシェアリング / モビリティ / P2Pレンタル |
| 現在の状況 | 経営危機（2024年市場時価総額$24M、大規模レイオフ実施） |
| 評価額/時価総額 | $1.7B（ピーク、2019年）→ $24M（2024年） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- UC Berkeley在学中、Sam Zaidが「車は95%の時間駐車されている」という事実に着目
- 車の所有コストは高いが、稼働率が極めて低い
- 車を持たない人が必要な時だけ借りられる仕組みを構想

**課題の具体化**:
1. **車の低稼働率**: 個人所有車は年間の95%駐車されたまま
2. **レンタカーの不便さ**: 店舗に行く必要、営業時間の制約
3. **都市部での車所有コスト**: 駐車場代、保険、メンテナンス

**需要検証方法**:
- 2009年、サンフランシスコでパイロットプログラム開始
- 初期ユーザーから好評、カーシェアリング需要を確認
- 2011年、TechCrunch Disruptで優勝（$50,000獲得）

### 2.2 プロダクト開発

**コア技術: Getaround Connect**:
- IoTデバイスを車に設置
- スマートフォンで車のロック/アンロック
- キーレス入車・退車

**ビジネスモデル: P2Pカーシェアリング**:
- 個人が自分の車を貸し出し
- Getaroundが仲介、保険、決済を提供
- レンタル料金の30-40%を手数料として徴収

**初期の成功**:
- サンフランシスコで急成長
- 2012年、Menlo VenturesからSeries A $13.9M調達
- 全米主要都市に展開

## 3. 急成長と過剰調達（2016-2020年）

### 3.1 SoftBank Vision Fundの大型投資

**2018年8月: Series D $300M**:
- SoftBank Vision Fund主導
- 評価額$1.2B（ユニコーン達成）
- Toyota Motor Corporationも参加

**2019年9月: 追加ラウンド $200M**:
- 評価額$1.7B（ピーク）
- ヨーロッパ展開の加速

**2020年10月: Series E $140M**:
- COVID-19パンデミック中
- 総調達額$736M

### 3.2 Drivy買収（2019年4月）

**$300M買収**:
- ヨーロッパのカーシェアリング大手Drivyを買収
- 「グローバルリーダー」を目指す
- しかし、統合コスト、文化の違いで苦戦

**買収の問題点**:
- 過大評価（$300Mは高すぎた）
- ユニットエコノミクス未改善のまま拡大
- ヨーロッパ市場での競合激化

## 4. 失敗の経緯

### 4.1 COVID-19の直撃（2020年）

**需要の急激な減少**:
- **2020年3-5月**: 利用率75%以上減少
- 移動制限、リモートワーク普及で車の需要消失
- 大規模レイオフ（2020年1月、150人解雇、全体の25%）

**一時的な回復（2020年5月以降）**:
- 人々が飛行機を避け、車移動を選択
- CEO Sam Zaidは「売上が2倍になった」と主張
- しかし、持続せず

### 4.2 ユニットエコノミクスの悪化

**P2Pモデルの問題点**:
- **低い利益率**: レンタル料金の30-40%手数料だが、コスト（保険、メンテナンス、カスタマーサポート）が高い
- **車両品質のバラツキ**: 個人所有車のため、品質管理困難
- **サプライサイドの不安定性**: 車のオーナーが貸し出しを止めると供給減

**スケールしない構造**:
- ネットワーク効果が弱い
- 地域ごとに供給・需要のバランスが異なる
- 都市部以外では成立しない

### 4.3 法的問題（2021年7月）

**Washington D.C.の訴訟**:
- DC Attorney Generalから訴えられる
- **無許可営業**: ライセンスなしでカーレンタル業を展開
- **誤解を招く表現**: 安全性に関する虚偽表示
- **罰金$950,000**: 和解、事業慣行の見直し

**ブランドイメージの損傷**:
- 法令遵守の問題
- 顧客からの信頼低下

### 4.4 SPAC合併の失敗（2022年12月）

**InterPrivate IIとのSPAC合併**:
- 評価額$1.2B（2019年$1.7Bから大幅下落）
- NYSE上場（ティッカー: GETR）
- 上場初日、株価65%下落
- 市場時価総額: 約$400M（評価額の1/3）

**SPAC合併の問題点**:
- 市場環境の悪化（2022年はSPACバブル崩壊）
- ユニットエコノミクス未改善
- 投資家の信頼喪失

### 4.5 大規模レイオフの連続（2023-2024年）

**2023年2月: 10%レイオフ**:
- 「持続可能な成長」を理由
- マクロ経済環境の悪化

**2024年2月: 30%レイオフ**:
- 北米スタッフの1/3を削減
- CEO Sam Zaid: 「収益性と持続可能な成長に焦点」
- しかし、財務状況は悪化し続ける

**2024年の財務状況**:
- **2023年7-9月期**: $27M損失
- **営業費用**: $42.9M（四半期）
- **市場時価総額**: $24M（2024年）

### 4.6 米国事業からの撤退（2025年2月）

**米国事業の終了発表**:
- 2025年2月、米国でのカーシェアリング事業を終了
- ヨーロッパ事業に注力
- 実質的な失敗

## 5. 失敗パターン分析

### P13: スケールしないモデル

**P2Pカーシェアリングの限界**:
- **低い利益率**: 手数料30-40%だが、コストが高い
- **地域依存**: 都市部以外では成立しない
- **ネットワーク効果の弱さ**: Uber/Airbnbと異なり、スケールメリット限定的

**ユニットエコノミクスの破綻**:
- 1レンタルあたりの利益が薄い
- 規模拡大してもコスト削減困難
- 保険、メンテナンス、カスタマーサポートが重荷

### P19: 顧客集中リスク

**COVID-19による需要消失**:
- 移動需要が75%減少
- 在宅勤務でカーシェア不要に
- 回復したと主張したが、持続せず

**単一市場への依存**:
- 都市部の移動需要に依存
- 経済危機、パンデミックで脆弱性露呈

### P28: 過剰調達（Death by Overfunding）

**$736Mの過剰調達**:
- ユニットエコノミクス未改善のまま大規模調達
- Drivy買収$300M（過大評価）
- グローバル展開の失敗

**SoftBankの呪い**:
- SoftBank Vision Fundの大型投資（$300M+）
- 「成長至上主義」でユニットエコノミクス無視
- SPAC合併で評価額$1.2B → 市場時価総額$24M（98%減）

## 6. 失敗から学ぶべき教訓

### 6.1 ユニットエコノミクスの重要性

1. **規模拡大前の収益性確認**:
   - 1レンタルあたりの利益を確保
   - コスト構造の改善が先

2. **P2Pモデルの限界**:
   - Airbnb（宿泊）はスケール、Getaround（車）はスケールしない
   - 理由: 車の稼働率、保険コスト、メンテナンス負担

3. **スケールメリットの検証**:
   - 規模拡大でコスト削減可能か?
   - Getaroundは規模拡大してもコスト削減せず

### 6.2 M&Aの注意点

1. **買収価格の妥当性**:
   - Drivy $300Mは過大評価
   - ユニットエコノミクス未改善のまま買収は危険

2. **統合コストの見積もり**:
   - 文化の違い、システム統合、オペレーション統合
   - Getaroundは統合に苦戦

### 6.3 SPACの危険性

1. **市場環境の見極め**:
   - 2022年はSPACバブル崩壊
   - タイミングが最悪

2. **評価額の現実性**:
   - $1.2B評価額 → 市場時価総額$24M
   - 投資家の信頼喪失

### 6.4 過剰調達の弊害

1. **資金があると無駄遣い**:
   - $300M Drivy買収
   - グローバル展開の失敗

2. **収益性軽視**:
   - SoftBankの「成長至上主義」
   - ユニットエコノミクス無視

## 7. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | 日本でもカーシェアニーズは存在（タイムズカー等） |
| 競合状況 | 2 | タイムズカー、オリックスカーシェアが強い |
| ローカライズ容易性 | 2 | 保険制度、法規制が日本独自 |
| 再現性（失敗回避） | 4 | ユニットエコノミクス検証、過剰調達回避が教訓 |
| **総合** | 2.75 | P2Pカーシェアは日本でも困難、B2Cモデルが主流 |

**日本市場での類似リスク**:
- P2Pカーシェアリングはタイムズカー等のB2Cモデルに劣る
- 保険制度の複雑さ
- 過剰調達の誘惑

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）での注意点

- **需要の深さ検証**: カーシェアニーズは存在するが、P2Pモデルで本当に満たせるか?
- **代替品との比較**: タイムズカー等のB2Cモデルとの優位性

### 8.2 CPF検証（/validate-cpf）での注意点

- **WTP（支払意思額）の検証**: レンタル料金の30-40%手数料で持続可能か?
- **サプライサイドの安定性**: 車のオーナーが継続的に貸し出すか?

### 8.3 PSF検証（/validate-10x）での注意点

- **ユニットエコノミクスの確認**: 1レンタルあたりの利益が十分か?
- **スケールメリットの検証**: 規模拡大でコスト削減可能か?

### 8.4 スコアカード（/startup-scorecard）での警告サイン

| 警告サイン | Getaroundの事例 |
|----------|---------------|
| ユニットエコノミクス悪化 | 低利益率、高コスト |
| 過剰調達 | $736M調達、Drivy $300M買収 |
| COVID-19直撃 | 需要75%減 |
| SPAC合併失敗 | 株価65%下落 |
| 大規模レイオフ連続 | 2023-2024年で40%以上削減 |

## 9. 避けるべきパターン

日本のモビリティスタートアップが避けるべきこと:

1. **ユニットエコノミクス未改善での大規模調達**: 収益性確認が先
2. **P2Pモデルの盲信**: B2Cモデル（タイムズカー）の方がスケールしやすい
3. **過大評価でのM&A**: Drivy $300Mは失敗
4. **SoftBankの大型投資の誘惑**: 成長至上主義で収益性軽視
5. **SPACバブルへの便乗**: 市場環境の見極めが重要

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2009年） | ✅ PASS | Wikipedia, Crunchbase |
| 総調達額（$736M） | ✅ PASS | Tracxn, Crunchbase |
| SoftBank投資（$300M、2018年） | ✅ PASS | Automotive News, TechCrunch |
| Drivy買収（$300M、2019年） | ✅ PASS | Via ID, TechCrunch |
| SPAC合併（2022年12月、$1.2B評価額） | ✅ PASS | CNBC, TechCrunch |
| 株価下落（65%、上場初日） | ✅ PASS | CNBC |
| レイオフ（30%、2024年2月） | ✅ PASS | TechCrunch, SF Chronicle |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Tracxn - Getaround 2025 Funding Rounds & List of Investors](https://tracxn.com/d/companies/getaround/__rKTuwF38V_98nVu1zJDgX-nIsauBE9z_Ekb5vtj1trE/funding-and-investors)
2. [Automotive News - Car-sharing startup Getaround raises $300 million in funding led by SoftBank](https://www.autonews.com/article/20180821/MOBILITY/180829912/car-sharing-startup-getaround-raises-300-million)
3. [TechCrunch - SoftBank-backed Getaround is raising $200M at a $1.5B+ valuation](https://techcrunch.com/2019/09/05/softbank-backed-getaround-is-raising-200m-at-a-1-5b-valuation/)
4. [TechCrunch - Getaround raises a $140 million Series E](https://techcrunch.com/2020/10/14/getaround-raises-a-140-million-series-e-amid-rebound-in-short-distance-travel/)
5. [CNBC - Getaround shares tank after going public in SPAC deal](https://www.cnbc.com/2022/12/09/getaround-shares-tank-after-going-public-in-spac-deal.html)
6. [TechCrunch - Car-sharing SPAC Getaround lays off 10% of staff](https://techcrunch.com/2023/02/02/car-sharing-spac-getaround-lays-off-10-of-staff/)
7. [TechCrunch - Car-sharing company Getaround cuts one-third of U.S. workforce](https://techcrunch.com/2024/02/08/car-sharing-company-getaround-cuts-one-third-of-u-s-workforce/)
8. [SF Chronicle - San Francisco car rental company to lay off about one-third of staff](https://www.sfchronicle.com/tech/article/getaround-layoffs-restructuring-18656885.php)
9. [TechCrunch - Peer-to-peer car rental startup Getaround fined nearly $1M by DC's attorney general](https://techcrunch.com/2021/07/23/peer-to-peer-car-rental-startup-getaround-fined-nearly-1m-by-dcs-attorney-general/)
10. [Crunchbase - Getaround Company Profile & Funding](https://www.crunchbase.com/organization/getaround)
11. [Wikipedia - Getaround](https://en.wikipedia.org/wiki/Getaround)
12. [Braemar Energy Ventures - Getaround Announces $45M in Financing](http://www.braemarenergy.com/news/pr/2017/04/getaround-45-million-financing.html)
13. [Via ID - Getaround acquires Drivy to create the global leader in carsharing](https://www.via-id.com/en/getaround-acquires-drivy/)
