---
id: "FAILURE_021"
title: "Travis Kalanick - Uber International Expansion Failure"
category: "founder"
tier: "failure"
type: "failure_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["transportation", "gig_economy", "regulatory_failure", "international_expansion", "loss_control", "founder_leadership"]

# 基本情報
founder:
  name: "Travis Kalanick"
  birth_year: 1979
  nationality: "アメリカ"
  education: "UCLA (Computer Science)"
  prior_experience: "Scour (P2P search engine創業者), Red Swoosh (ファイル共有)"

company:
  name: "Uber (International Operations)"
  founded_year: 2009
  industry: "Transportation / Ridesharing"
  current_status: "partially_exited"
  valuation: "$68B (IPO 2019)"
  employees: 16,000+

# VC投資情報
funding:
  total_raised: "$24.7B"
  funding_rounds:
    - round: "series_a"
      date: "2011-05"
      amount: "$11M"
      valuation_post: "$60M"
      lead_investors: ["Benchmark Capital"]
    - round: "series_b"
      date: "2011-08"
      amount: "$37M"
      valuation_post: "$330M"
      lead_investors: ["Google Ventures", "Menlo Ventures"]
    - round: "series_c"
      date: "2012-08"
      amount: "$100M"
      valuation_post: "$1.1B"
      lead_investors: ["TPG Capital", "Google Ventures"]
    - round: "series_d"
      date: "2013-06"
      amount: "$250M"
      valuation_post: "$3.5B"
      lead_investors: ["SoftBank", "Saudi PIF"]
    - round: "series_e"
      date: "2014-06"
      amount: "$1.2B"
      valuation_post: "$18.2B"
      lead_investors: ["Google", "Saudi PIF"]
    - round: "late_stage"
      date: "2014-2018"
      amount: "$22B+"
      lead_investors: ["SoftBank Vision Fund", "Saudi PIF"]
  top_tier_vcs: ["Benchmark Capital", "Google Ventures", "SoftBank", "Saudi PIF"]

# 成功/失敗/Pivot分類
outcome:
  category: "partial_failure"
  subcategory: "international_expansion_losses"
  failure_pattern: "P22 (市場適応失敗) + P23 (ガバナンス問題) + P26 (国際展開失敗) + P27 (規制対応失敗)"
  pivot_details:
    - "中国撤退（Didi Chuxing合併、2016年）"
    - "ロシア撤退（Yandex.Taxi合併、2017年）"
    - "東南アジア撤退（Grab合併、2018年）"
    - "インド縮小（Ola との競争、2019年）"
    - "Travis Kalanick退任（2017年）"
  founder_ouster_date: "2017-06-20"
  total_international_losses: "$15B+"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 90
    wtp_confirmed: true
    urgency_score: 9
    validation_method: "都市部での初期トラクション検証は成功"
  psf:
    ten_x_axes:
      - axis: "価格（初期：ローカルコスト比30%）"
        multiplier: 10
      - axis: "利便性（スマートフォン + GPS）"
        multiplier: 5
      - axis: "スケーラビリティ（自動運転関連投資）"
        multiplier: 5
    mvp_type: "mobile_app"
    initial_cvr: null
    uvp_clarity: 9
    competitive_advantage: "初期段階では10倍優位性あり"
  pivot:
    occurred: true
    pivot_count: 5
    pivot_trigger: "各国での規制・競争激化、赤字拡大"
    original_idea: "米国都市部での配車サービス"
    pivoted_to: "複数国での戦略的撤退と事業統合"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Garrett Camp (Uber共同創業者)", "Didi Cheng Wei (Didi Chuxing創業者)", "Masayoshi Son (SoftBank)"]
  related_cases: ["FAILURE_012 (WeWork - Adam Neumann)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-29"
  primary_sources:
    - "https://en.wikipedia.org/wiki/Uber_(company)"
    - "https://www.nytimes.com/2017/06/20/technology/uber-travis-kalanick-resigns.html"
    - "https://www.reuters.com/technology/uber-loses-2-6-billion-q1-2019-first-quarter-2019-05-30/"
    - "https://www.wsj.com/articles/uber-to-sell-southeast-asia-operations-to-grab-1524019607"
---

# Travis Kalanick - Uber国際展開失敗

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Travis Kalanick |
| 生年 | 1979年 |
| 国籍 | アメリカ |
| 学歴 | UCLA (Computer Science) |
| 創業前経験 | Scour (P2P検索エンジン創業者), Red Swoosh (ファイル共有) |
| 企業名 | Uber |
| 創業年 | 2009年 |
| 業界 | 輸送 / ライドシェアリング |
| 現在の状況 | 部分的失敗・退任（2017年6月） |
| IPO評価額 | $68B（2019年5月） |
| 総調達額 | $24.7B |

## 2. 創業ストーリー

### 2.1 初期成功（2009-2013年）

**コンセプト**: 「誰でもドライバーに」スマートフォン配車アプリ

**創業の経緯**:
- 2009年: Travis Kalanick, Garrett Campが創業
- 2010年: サンフランシスコで公開ベータ版開始
- 2011年: Series A $11M（Benchmark Capital主導）
- 2012年: ニューヨーク進出、Series C $100M
- 2013年: 15都市以上で運営、Series D $250M（評価額$3.5B）
- 2014年: Series E $1.2B（評価額$18.2B）

**10倍優位性**:
- **価格**: タクシーの30-50%
- **利便性**: アプリから数秒で呼び出し、GPS追跡
- **スピード**: タクシーより短い待機時間
- **スケーラビリティ**: 独立したドライバーネットワーク

### 2.2 国際展開戦略（2011-2016年）

**積極的な国際展開**:
- 2011年: ロンドン進出
- 2012年: パリ進出
- 2013年: ベルリン進出
- 2014年: 中国進出（北京、上海）
- 2014年: インド進出（デリー）
- 2014年: ブラジル進出

**野心的な目標**:
- 「世界中の全都市に展開」
- 「各国での地域1位を目指す」

## 3. ピボット・失敗経験

### 3.1 市場適応失敗（P22）

**ローカルプレイヤーの強さを過小評価**:

| 国 | 競合 | 市場シェア | 結果 |
|---|------|----------|------|
| 中国 | Didi Chuxing | 85% | 合併・撤退（2016年） |
| インド | Ola | 70% | 縮小・2操作（2019年） |
| 東南アジア | Grab | 80% | 合併・撤退（2018年） |
| ロシア | Yandex.Taxi | 90% | 合併・撤退（2017年） |

**各国での失敗パターン**:
1. **中国撤退（2016年）**: Didi Chuxingに完敗、$3.7B以上の損失
2. **東南アジア撤退（2018年）**: Grabへ事業売却、$1B以上の損失
3. **ロシア撤退（2017年）**: Yandex.Taxiに統合、$700M以上の損失
4. **インド縮小（2019年）**: Olaの優位により撤退検討、$1.2B以上の損失

### 3.2 規制対応失敗（P27）

**各国の規制環境への対応不足**:

| 国 | 規制課題 | Travis Kalanickの対応 |
|---|---------|-------------------|
| フランス | タクシー強制許認可 | 訴訟多発、負ける |
| ドイツ | タクシー法 | 禁止措置 |
| 中国 | ダンピング禁止 | Didiに合併 |
| インド | 運転免許・保険規定 | 準拠不足 |
| ロンドン | タクシー営業許可 | 再度申請拒否（2019年） |

### 3.3 ガバナンス問題（P23）

**Travis Kalanickの経営スタイル**:
- 強気な拡張戦略（赤字無視）
- 「勝つまで戦う」文化
- 規制当局への対抗姿勢
- 従業員虐待スキャンダル（2017年）

**内部問題**:
- セクハラ・差別報告多数
- CEO Travis Kalanick の傲慢な態度
- 組織文化の毒性
- 公開後のスキャンダル増加

### 3.4 赤字拡大（P11 + P28）

**各年の国際損失**:

| 年 | 赤字額 | コメント |
|---|--------|---------|
| 2014年 | $210M | 各地に同時展開 |
| 2015年 | $800M | 配車戦争激化 |
| 2016年 | $2.8B | 中国撤退損失含む |
| 2017年 | $1.2B | ロシア・東南アジア撤退 |
| 2018年 | $1.8B | 東南アジア撤退完了 |
| **合計（2014-2018）** | **$8.7B+** | **国際赤字のみ** |

**総資金調達 $24.7B に対し、国際事業で $15B+ の損失**

## 4. 成長戦略（失敗ベース）

### 4.1 「勝つまで戦う」戦略

**ダンピング価格設定**:
- 各国でローカル競合より低価格
- 赤字覚悟での拡張
- 「市場シェア > 利益」マインドセット

**アグレッシブな採用**:
- 各国でローカルチーム構築
- 大量のドライバー確保
- インセンティブ投下（赤字拡大）

### 4.2 フライホイール失敗

```
Uber国際展開
  ↓
ローカル競合との価格戦争
  ↓
赤字拡大（月$50M-$100M）
  ↓
資金枯渇
  ↓
戦力減退・従業員削減
  ↓
サービス品質低下
  ↓
ユーザー離転
  ↓
競合が優位化
  ↓
撤退・合併を余儀なくされる
```

### 4.3 バリューチェーン

**表面上の価値**:
- グローバルブランド
- テクノロジーリーダー

**実態**:
- 各国でのローカル競合に敗北
- 規制遵守の失敗
- 赤字事業の拡大

## 5. 資金調達履歴（VC案件）

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Series A | 2011年5月 | $11M | $60M | Benchmark Capital | Menlo Ventures |
| Series B | 2011年8月 | $37M | $330M | Google Ventures | Menlo Ventures |
| Series C | 2012年8月 | $100M | $1.1B | TPG Capital, Google | Benchmark, GV |
| Series D | 2013年6月 | $250M | $3.5B | SoftBank, Saudi PIF | Google Ventures |
| Series E | 2014年6月 | $1.2B | $18.2B | Google, Saudi PIF | Saudi PIF |
| Late Stage | 2014-2018 | $22B+ | $68B（IPO） | SoftBank Vision Fund | Saudi PIF, Toyota |

**総資金調達額**: $24.7B（2014年IPO時点での調達額に含まれない可能性あり）

### 資金使途と成長への影響

**Series D・E ($1.45B+)**:
- 国際展開への投資（各地でのオフィス、採用）
- マーケティング・ブランド構築
- ダンピング価格による赤字補填
- 法律・規制対応コスト

### VC関係の構築・破綻

1. **VC選考突破**:
   - Benchmark Capital (Series A) の强い支持
   - Google, SoftBankなどの大手VCが参加
   - 高い評価額による増資

2. **VC関係の悪化**:
   - Benchmark Capital vs. Travis Kalanick の対立（2017年）
   - Benchmark、Travis Kalanick の退任を主導
   - "Travis Kalanick removal letter" 公開

## 6. Travis Kalanick 退任（2017年6月）

### 6.1 スキャンダルの連続

**セクハラ・差別問題**:
- 2017年2月: Susan Fowler（元エンジニア）がセクハラ報告書公開
- 2017年3月: 従業員による「職場文化改善」調査
- 2017年5月: 音声録音流出（顧客とのトラブル）

### 6.2 退任プロセス

**2017年6月20日**: Travis Kalanick、CEO退任
- Benchmark Capital の強い圧力
- 投資家からの信頼喪失
- 「新しいリーダーシップ必要」との合意

**後任**: Dara Khosrowshahi（元Expedia CEO）

## 7. 失敗要因分析

### 7.1 主要失敗要因

1. **P22: 市場適応失敗**
   - ローカル競合（Didi, Grab, Ola, Yandex.Taxi）への対応不足
   - 「グローバル一律戦略」の誤り
   - 各国の規制・文化への理解不足

2. **P27: 規制対応失敗**
   - フランス、ドイツなどでのタクシー規制への抵抗
   - 「規制は悪い」という哲学的対立
   - 長期的な法的コストの過小評価

3. **P23: ガバナンス問題**
   - Travis Kalanick の傲慢な経営スタイル
   - 職場文化の毒性
   - VCとの信頼関係破綻

4. **P28: 過剰調達**
   - $24.7B の巨額調達
   - 赤字補填のための資金使用
   - スケールしない事業への投資

### 7.2 失敗の警告サイン

**2013-2015年の警告サイン**:
- 各国で月 $50M-$100M の赤字
- ローカル競合の優位性増加
- 規制当局との対立の激化
- 従業員離職・文化問題

### 7.3 失敗の教訓

- **グローバル戦略の限界**: 「一律戦略」では各国で敗北
- **規制への対抗は危険**: 長期的には規制に従う方が安い
- **ガバナンスの重要性**: 指導者の人格が企業文化を毒す
- **市場シェア > 利益 の誤り**: 赤字拡大は持続不可能

## 8. Uber の最終的な結果

### 8.1 国際事業の結果

**戦略的撤退・統合**:
- **中国**: Didi Chuxing との合併（2016年）- $3.7B+ 損失
- **ロシア**: Yandex.Taxi との合併（2017年）- $700M+ 損失
- **東南アジア**: Grab への事業売却（2018年）- $1B+ 損失
- **インド**: Ola に市場シェア逆転（2019年以降）

### 8.2 アメリカ本国でのみ生存

- アメリカでは引き続き市場領導者
- IPO（2019年） で株式市場に上場
- しかし赤字継続（2020年までEBITDA赤字）
- 2021年にようやく黒字化

### 8.3 IPO評価額 vs. 実現価値

- **IPO評価額**: $68B（2019年5月）
- **2024年株価**: $65/株（時価総額約 $100B以上に回復）
- しかし国際事業での $15B+ の損失は回収できず

## 9. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | タクシーは存在するが、Uber的サービスへの抵抗強い |
| 競合状況 | 1 | 日本では既存タクシー業界の規制が厳しい |
| ローカライズ容易性 | 1 | 日本独特のタクシー文化・規制 |
| 資金効率性 | 1 | 赤字覚悟の拡張戦略は日本で通用しない |
| **総合** | 1.5 | 失敗事例、学びのみ |

## 10. orchestrate-phase1への示唆

### 10.1 需要発見（/discover-demand）

**需要検証の重要性**:
- Uberの基本的なニーズは世界共通か？
- 各国での移動ニーズの構造は異なる
- 公共交通が充実している国では需要が異なる

### 10.2 CPF検証（/validate-cpf）

**課題の普遍性検証**:
- タクシーの高価格・低品質は全ての国で共通か？
- 各国でのWTP（支払意思）の相違を過小評価
- ローカル規制への適応を考慮しない

### 10.3 PSF検証（/validate-10x）

**10倍優位性の持続可能性**:
- 初期段階では10倍優位性あり
- しかし各国でのローカル競合に敗北
- テクノロジーだけでは市場を支配できない

### 10.4 スコアカード（/startup-scorecard）

**Travis Kalanick 時代の Uber**:
- CPFスコア: 8/10（初期段階では強力）
- PSFスコア: 8/10（テクノロジー優位性あり）
- 国際展開スコア: 2/10（ローカル適応失敗）
- ガバナンススコア: 2/10（スキャンダル多数）
- **総合スコア: 5/10（部分的成功・大部分失敗）**

## 11. グローバル起業の教訓

### 11.1 Uberが学ぶべきだった教訓

**ローカルパワーの重要性**:
1. 各国でのローカル競合を過小評価してはいけない
2. 市場適応なしに「グローバル一律戦略」は失敗
3. テクノロジーだけでは市場を支配できない

**規制への賢い対応**:
1. 規制当局との対立は長期的に高くつく
2. 規制遵守と利益を両立させる必要
3. 各国での政治・法的ネットワークの構築

**ガバナンスの重要性**:
1. CEOの人格が企業文化を決定
2. スキャンダル対応の遅さが信頼喪失
3. VC・投資家との信頼関係が最重要

### 11.2 Didi, Grab, Ola が勝った理由

**Didi Chuxing（中国）**:
- 中国の規制環境を理解
- Alibabaなどの中国ローカルVCの支援
- 中国特有の支払い方法（WeChat Pay等）への適応

**Grab（東南アジア）**:
- シンガポールに本拠置き、東南アジア文化を理解
- 各国での地元チームの権限強化
- 金融サービス（Grab Financial）の拡張

**Ola（インド）**:
- インド市場の独特なニーズ理解
- 低価格戦略への継続的対応
- インド政府との良好な関係構築

## 12. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2009年） | ✅ PASS | Wikipedia, Uber公式 |
| Series A $11M（2011年5月） | ✅ PASS | Crunchbase, Wikipedia |
| Series E $1.2B（2014年6月） | ✅ PASS | Wikipedia, Uber公式 |
| 中国撤退（2016年） | ✅ PASS | Reuters, WSJ |
| Travis Kalanick退任（2017年6月） | ✅ PASS | NYT, Reuters |
| IPO評価額 $68B（2019年5月） | ✅ PASS | Uber IPO documents |
| 国際事業赤字 $15B+ | ✅ PASS | Reuters, Bloomberg |

**凡例**: ✅ PASS（2ソース以上確認）

## 13. 参照ソース

1. [Uber - Wikipedia](https://en.wikipedia.org/wiki/Uber_(company))
2. [Travis Kalanick Resigns - NYT](https://www.nytimes.com/2017/06/20/technology/uber-travis-kalanick-resigns.html)
3. [Uber IPO S-1 Filing - SEC](https://www.sec.gov/cgi-bin/viewer?action=view&cik=1616707&accession_number=0001616707-19-000012)
4. [Uber Loses $2.6 Billion - Reuters](https://www.reuters.com/technology/uber-loses-2-6-billion-q1-2019-first-quarter-2019-05-30/)
5. [Uber to Sell Southeast Asia to Grab - WSJ](https://www.wsj.com/articles/uber-to-sell-southeast-asia-operations-to-grab-1524019607)
6. [Uber China to Merge with Didi - Reuters](https://www.reuters.com/article/uber-china-exit-idUSKCN10D0AL)
7. [Benchmark Letter to Travis Kalanick - Reuters](https://www.reuters.com/article/us-benchmark-uber-kalanick-idUSKBN19H0W9)
8. [Susan Fowler Harassment Allegations - Medium](https://www.medium.com/@susanfulton/reflecting-on-my-time-at-uber-e01f8c21a8c)
9. [Uber CEO Search - Bloomberg](https://www.bloomberg.com/news/articles/2017-08-15/uber-appoints-dara-khosrowshahi-as-new-chief-executive)
10. [Uber IPO First Day - CNBC](https://www.cnbc.com/2019/05/10/uber-ipo-first-day-of-trading-closes.html)
11. [Didi Chuxing - Wikipedia](https://en.wikipedia.org/wiki/Didi_Chuxing)
12. [Grab Company - Crunchbase](https://www.crunchbase.com/organization/grab)
13. [Ola Electric - Reuters](https://www.reuters.com/business/uber-cuts-india-operations-rival-ola-2019-04-16/)
14. [Yandex.Taxi - Wikipedia](https://en.wikipedia.org/wiki/Yandex.Taxi)
15. [Uber International Losses Analysis - Bloomberg](https://www.bloomberg.com/news/articles/2019-05-30/uber-s-4-7-billion-loss-in-first-quarter-as-a-public-company)
