---
id: "FAILURE_014"
title: "Piotr Szulczewski - Wish (ContextLogic)"
category: "failure"
tier: "failure_study"
type: "ipo_failure"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["ecommerce", "marketplace", "founders-fund", "ggv-capital", "formation-8", "ipo-failure", "quality-issues", "counterfeit", "unit-economics"]

# 基本情報
founder:
  name: "Piotr Szulczewski"
  co_founders: ["Danny Zhang"]
  birth_year: 1981
  nationality: "カナダ・ポーランド"
  education: "University of Waterloo（数学・コンピュータサイエンス）"
  prior_experience: "Google（4年間、広告アルゴリズム開発）"

company:
  name: "Wish (ContextLogic)"
  founded_year: 2010
  industry: "Eコマース / マーケットプレイス"
  current_status: "acquired"
  valuation: "$14B（IPO 2020年12月）→ $161M（Qoo10売却 2024年4月）"
  employees: null # ピーク時不明

# VC投資情報
funding:
  total_raised: "$1.7B"
  funding_rounds:
    - round: "seed"
      date: "2010-09"
      amount: "$1.7M"
      valuation_post: null
      lead_investors: ["Jeremy Stoppelman (Yelp CEO)"]
      other_investors: []
    - round: "series_a"
      date: "2011"
      amount: "$1.9M"
      valuation_post: null
      lead_investors: ["8VC (Joe Lonsdale)"]
      other_investors: ["Jerry Yang"]
    - round: "series_b"
      date: "2013"
      amount: null
      valuation_post: null
      lead_investors: ["GGV Capital"]
      other_investors: []
    - round: "series_b_extension"
      date: "2014-01"
      amount: "$19M"
      valuation_post: null
      lead_investors: ["GGV Capital", "Formation 8"]
      other_investors: ["Jerry Yang"]
    - round: "series_c"
      date: "2014-06"
      amount: "$50M"
      valuation_post: null
      lead_investors: ["Founders Fund"]
      other_investors: ["Formation 8", "GGV Capital", "Cherubic Ventures"]
    - round: "series_d"
      date: "2014"
      amount: "$100M"
      valuation_post: "$3B"
      lead_investors: ["DST Global"]
      other_investors: []
    - round: "series_h"
      date: "2019-08"
      amount: "$300M"
      valuation_post: "$11.2B"
      lead_investors: ["General Atlantic"]
      other_investors: []
  top_tier_vcs: ["Founders Fund（Series C主導）", "GGV Capital（Series B主導）", "Formation 8", "DST Global", "8VC"]

# 成功/失敗/Pivot分類
outcome:
  category: "failure"
  subcategory: "ipo_failure_fire_sale"
  failure_pattern: "P21+P26+P28+P14"
  failure_details:
    - pattern: "P21"
      description: "製品品質問題（偽物・粗悪品・安全基準違反）"
    - pattern: "P26"
      description: "ブランド価値毀損（'Wish = 偽物'のイメージ定着）"
    - pattern: "P28"
      description: "過剰調達（$1.7B調達、IPO評価額$14B → $161M売却）"
    - pattern: "P14"
      description: "タイミング（COVID後のeコマース需要減、規制強化）"
  ipo_failure:
    ipo_filed: "2020-11"
    ipo_date: "2020-12-16"
    ipo_price: "$24"
    ipo_valuation: "$14B"
    stock_decline: "97%"
    ceo_resigned: "2021-11"
    acquired_date: "2024-04-19"
    acquired_price: "$161M"
    acquired_by: "Qoo10"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 7 # 安価な商品需要は広範
    wtp_confirmed: true # 低価格志向ユーザーは存在
    urgency_score: 2 # 必需品ではない、娯楽的買い物
    validation_method: "急速拡大優先、品質管理不十分"
  psf:
    ten_x_axes:
      - axis: "価格"
        multiplier: 3 # Amazon等より60-80%安い
      - axis: "品質"
        multiplier: 0.3 # 偽物・粗悪品多数
      - axis: "配送速度"
        multiplier: 0.2 # 数週間～数ヶ月
      - axis: "信頼性"
        multiplier: 0.1 # 返品困難、偽物多数
    mvp_type: "marketplace"
    initial_cvr: null
    uvp_clarity: 7 # "激安"は明確だが品質犠牲
    competitive_advantage: "なし（中国製品の転売、参入障壁低い）"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: null
    original_idea: "モバイルファーストeコマースマーケットプレイス"
    pivoted_to: null

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Piotr Szulczewski", "Danny Zhang"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 18
  last_verified: "2025-12-29"
  primary_sources:
    - "Wikipedia"
    - "CNBC"
    - "Bloomberg"
    - "TechCrunch"
    - "CB Insights"
    - "8VC"
---

# Piotr Szulczewski - Wish (ContextLogic)（IPO後97%下落・品質問題分析）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Piotr Szulczewski（CEO）, Danny Zhang（CTO） |
| 生年 | 1981年 |
| 国籍 | カナダ・ポーランド |
| 学歴 | University of Waterloo（数学・コンピュータサイエンス） |
| 創業前経験 | Google（4年間、広告アルゴリズム開発、キーワード拡張機能プロトタイプ作成） |
| 企業名 | Wish (ContextLogic) |
| 創業年 | 2010年 |
| 業界 | Eコマース / マーケットプレイス |
| 現在の状況 | 売却（2024年4月Qoo10へ$161M） |
| 評価額/時価総額 | $14B（IPO 2020年12月）→ $161M（2024年売却、99%下落） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- **2004年**: University of WaterlooでDanny Zhangと出会う
- **2004年卒業直前**: Googleインターンシップ開始（23歳）
- **2004-2009年**: Google正社員として広告アルゴリズム開発
- **2009年**: 6ヶ月間自宅でコーディング、広告レコメンデーションプラットフォーム開発
- ユーザーのブラウジング行動から興味を予測するアルゴリズム

**課題の具体化**:
1. **高額なEコマース**: Amazon等の正規品は低所得層には高い
2. **モバイル最適化不足**: 2010年時点でモバイルEコマースは未発達
3. **中国製品の直接購入障壁**: 言語・決済・配送の問題

**需要検証方法**:
- **2010年9月**: ContextLogic設立、$1.7M調達（Yelp CEO Jeremy Stoppelmanら）
- **2011年5月**: Danny Zhangを旧友として勧誘、共同創業者に
- **2011年**: Wishwall.meとして再スタート（後にWish.comに改名）

### 2.2 プロダクト開発

**創業メンバー**:
- **Piotr Szulczewski**: CEO、アルゴリズム・戦略
- **Danny Zhang**: CTO、技術開発

**初期資金調達**:
- **2010年9月**: Seed $1.7M（Jeremy Stoppelman主導）
- **2011年**: Series A $1.9M（8VC Joe Lonsdale主導、Jerry Yang参加）

**初期プロダクト**:
- モバイルアプリファーストのマーケットプレイス
- 中国製品を中心に60-80%安価な商品を提供
- パーソナライズされたレコメンデーション（Googleでの経験活用）

## 3. 成長の軌跡

### 3.1 Founders Fund・トップティアVCとの出会い（2014年）

**Series C調達（2014年6月）**:
- **金額**: $50M
- **リード投資家**: Founders Fund（Geoff Lewis, Brian Singerman）
- **他投資家**: Formation 8, GGV Capital, Cherubic Ventures
- Joe Lonsdale（8VC）がFounders Fundに紹介

**Founders Fundの投資判断**:
- モバイルEコマースの成長性
- 低所得層向けの未開拓市場
- Piotr Szulczewskiの技術力（Googleアルゴリズム経験）

**その他トップティアVC**:
- **2013年**: GGV Capital主導Series B（Hans Tung）
- **2014年1月**: GGV Capital・Formation 8共同主導$19M
- **2014年**: DST Global主導Series D $100M（評価額$3B）
- **2019年8月**: General Atlantic主導Series H $300M（評価額$11.2B）

### 3.2 爆発的成長（2014-2020年）

**ユーザー数・GMV成長**:
- **2020年IPO時**: 月間アクティブユーザー107M、GMV $30B+
- グローバル展開（北米・欧州中心）
- モバイルアプリダウンロード数億超

**総調達額**:
- **$1.7B**（12ラウンド）

### 3.3 IPO（2020年12月）

**S-1提出・IPO実施（2020年11月～12月）**:
- **IPO日**: 2020年12月16日
- **IPO価格**: $24/株
- **調達額**: $1.1B
- **評価額**: $14B

**IPO初日の失敗**:
- **初値**: $22.75（IPO価格$24を下回る）
- **初日終値**: $22.05（IPO価格比8%下落）
- 2020年最悪のIPOデビューと報道

**S-1で露呈した問題**:
1. **収益性**: 2020年売上$2.54B、純損失$745M
2. **中国依存**: 94%の出品者が中国拠点
3. **配送遅延**: 数週間～数ヶ月
4. **品質問題**: 偽物・粗悪品の評判

### 3.4 株価暴落（2020-2024年）

**継続的下落**:
- **2020年12月IPO**: $24 → **2021年12月**: 約$6（75%下落）
- **2022年**: 約$2（IPO比92%下落）
- **2023年**: 約$0.70（IPO比97%下落）

**CEO辞任（2021年11月）**:
- Piotr Szulczewski、2022年2月1日付で退任発表
- 後任CEO: Vijay Talwar（2022年2月1日就任）

**収益崩壊**:
- **2020年**: 売上$2.54B
- **2021年**: 売上$2.09B（18%減）
- **2022年**: 売上$571M（73%減）
- **2023年**: 売上$287M（50%減）

**ユーザー流出**:
- **2020年IPO時**: 107M MAU
- **2021年末**: 74M MAU（31%減）
- **2022年末**: 20M MAU（IPO比81%減）

### 3.5 Qoo10への売却（2024年4月）

**売却発表（2024年2月）**:
- Qoo10へ$173Mで売却合意（最終調整後$161M）
- IPO評価額$14Bの1.2%（99%下落）

**売却完了（2024年4月19日）**:
- 株主承認（賛成97%）
- ContextLogicはWishの事業資産を売却、残余財産を株主に分配へ

## 4. 失敗要因分析

### 4.1 製品品質問題（P21）

**偽物・粗悪品の蔓延**:
- 94%の出品者が中国拠点、品質管理が不十分
- 欧州消費者団体Whichの調査: 電子機器・玩具のほぼ全てが安全基準不合格
- 偽物・違法品・危険品の販売報道多数

**顧客不満**:
- Trustpilot、HighYa等のレビューサイトで数百件の低評価
- 配送遅延（数ヶ月）、返品困難、未配達

**規制対応**:
- **2021年11月**: Google、フランスでWishアプリをApp Storeから削除
- **2021年11月**: Appleもフランスでアプリ削除
- フランス政府がGoogle等に要請（安全基準違反理由）

### 4.2 ブランド価値毀損（P26）

**"Wish = 偽物・粗悪品"イメージ定着**:
- ソーシャルメディアでWish購入品の失敗談が拡散
- ミーム化（"Wish版〇〇"は粗悪品の代名詞）
- 信頼性低下、リピート率低下

**高額マーケティング費用の浪費**:
- ユーザー獲得コスト（CAC）高騰
- 広告依存（ProductBoost）で短期流入、定着せず

### 4.3 過剰調達とバリュエーション崩壊（P28）

**$1.7B調達の弊害**:
- 評価額$11.2B（2019年）→ $14B（IPO 2020年）
- 現実的な事業価値を大幅に超過
- 「成長至上主義」で品質管理軽視

**IPO後の期待値ギャップ**:
- IPO価格$24は高すぎ、初日から下落
- 投資家の失望、売り圧力継続

### 4.4 タイミング（P14）

**COVID-19ブームの終焉**:
- 2020年はEコマース需要急増（巣ごもり需要）
- 2021年以降、実店舗回帰、競合激化
- Wishは品質で劣り、顧客流出

**規制強化**:
- 欧州・米国で消費者保護規制強化
- 偽物・安全基準違反への取り締まり
- Wishのビジネスモデルと相性悪化

### 4.5 ユニットエコノミクス問題

**コスト構造の悪化**:
- 長期配送（中国から直送）、配送コスト上昇
- 返品コスト負担
- マーケティング費用高騰

**収益構造の脆弱性**:
- 低価格商品（平均単価低い）
- 手数料率低い（中国出品者への配慮）
- 継続的赤字

## 4.6 資金調達履歴

| ラウンド | 時期 | 金額 | リード投資家 | 評価額 |
|---------|------|------|------------|--------|
| Seed | 2010-09 | $1.7M | Jeremy Stoppelman (Yelp CEO) | - |
| Series A | 2011 | $1.9M | **8VC (Joe Lonsdale)** | - |
| Series B | 2013 | - | **GGV Capital** | - |
| Series B拡張 | 2014-01 | $19M | **GGV Capital**, **Formation 8** | - |
| Series C | 2014-06 | $50M | **Founders Fund** | - |
| Series D | 2014 | $100M | DST Global | $3B |
| Series H | 2019-08 | $300M | General Atlantic | $11.2B |
| IPO | 2020-12 | $1.1B | - | $14B |
| 売却 | 2024-04 | - | Qoo10 | $161M |

### Founders Fundとの関係構築

**パートナー**: Geoff Lewis, Brian Singerman

**投資判断理由（2014年）**:
1. **モバイルファーストトレンド**: スマホEコマースの成長性
2. **未開拓市場**: 低所得層向けEコマース
3. **技術優位性**: Googleアルゴリズム経験活用

**Founders Fundのリターン**（推定）:
- Series C（2014年）: 評価額不明 → IPO $14B（大幅増）
- ただし、株価97%下落で最終リターンは限定的
- IPO前後で一部Exitした可能性

## 5. 教訓

### 5.1 品質管理の重要性

**成長 ≠ 成功**:
- Wishは107M MAUまで成長したが、品質問題で崩壊
- 短期的ユーザー獲得より、長期的満足度が重要

**ブランド価値は脆弱**:
- 一度"Wish = 粗悪品"イメージが定着すると回復困難
- 偽物・安全基準違反は致命的

### 5.2 サプライチェーン依存リスク

**中国依存94%の危険性**:
- 配送遅延（数週間～数ヶ月）
- 品質管理困難
- 地政学リスク

**マーケットプレイスの責任**:
- 出品者管理が不十分だとプラットフォーム全体が毀損

### 5.3 過剰調達のリスク

**評価額$14Bの弊害**:
- 現実的な事業価値を無視した拡大
- IPO価格が高すぎて下落必至
- 品質管理より成長を優先

### 5.4 規制対応の重要性

**欧州での失敗**:
- Google・Appleアプリストア削除は致命的
- 消費者保護規制を軽視

## 6. 日本市場への示唆

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | 安価な商品需要はあるが、品質重視の日本では不適 |
| 競合状況 | 2 | Amazon, 楽天, メルカリ等が優位 |
| ローカライズ容易性 | 1 | 日本は品質・配送速度重視、Wishモデルと不適合 |
| 再現性（成功再現） | 1 | Wishモデルは失敗、品質問題で破綻 |
| **総合** | 1.75 | Wishモデルは日本市場で失敗リスク極大 |

**日本市場での教訓**:
- 日本は品質重視、"安かろう悪かろう"は通用しない
- 配送速度期待値高い（翌日配送当然）、Wishの数週間は論外
- 消費者保護規制厳格、偽物・安全基準違反は致命的

## 7. orchestrate-phase1への示唆

### 7.1 需要発見（/discover-demand）での注意点

- **低価格需要 ≠ 粗悪品許容**: 安価でも品質基準は存在
- **ターゲット顧客の明確化**: 低所得層向けでも品質最低ラインを守る

### 7.2 CPF検証（/validate-cpf）での注意点

- **WTP（支払意思額）**: 低価格志向ユーザーでも品質閾値あり
- **継続利用率**: Wishは新規獲得できても定着せず
- **problem_commonality**: 安価商品需要は広範だが、品質問題で離脱

### 7.3 PSF検証（/validate-10x）での注意点

- **価格軸だけでは不十分**: Wishは価格3倍優位だが、品質0.3倍で総合劣位
- **複合評価が重要**: 価格・品質・配送速度・信頼性の総合
- **参入障壁低い**: 中国製品転売モデルは模倣容易

### 7.4 スコアカード（/startup-scorecard）での評価

| 指標 | Wishの事例 | スコア |
|------|-----------|--------|
| PMF | 短期的には成長、長期的には崩壊 | 3/10 |
| 参入障壁 | 低い（中国製品転売、模倣容易） | 2/10 |
| 収益性 | 継続的赤字、unit economics不成立 | 1/10 |
| スケーラビリティ | 拡大したが品質管理破綻 | 2/10 |
| ブランド価値 | 負のブランドイメージ | 1/10 |
| **総合** | 失敗モデル | **1.8/10** |

## 8. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2010年） | ✅ PASS | Wikipedia, CB Insights |
| Piotr Szulczewski生年（1981年） | ✅ PASS | Wikipedia, Mabumbe |
| University of Waterloo卒業（2004年） | ✅ PASS | Wikipedia, Mabumbe |
| Google勤務（2004-2009年） | ✅ PASS | Wikipedia, Entrepreneur Wiki |
| Seed $1.7M（2010年9月） | ✅ PASS | Wikipedia, CB Insights |
| Founders Fund Series C主導（2014年6月） | ✅ PASS | 8VC, Venture Capital Journal |
| Series H $300M、評価額$11.2B（2019年8月） | ✅ PASS | CNBC, CB Insights |
| IPO $24、評価額$14B（2020年12月16日） | ✅ PASS | CNBC, Bloomberg, TheStreet |
| IPO初日8%下落（$22.05終値） | ✅ PASS | CNBC, Fortune |
| CEO辞任（2021年11月発表） | ✅ PASS | Wikipedia, Retail Dive |
| 2022年売上$571M（73%減） | ✅ PASS | Companies Market Cap, Seeking Alpha |
| Qoo10へ$161M売却（2024年4月19日） | ✅ PASS | Bloomberg, Globe Newswire |
| 中国出品者94% | ✅ PASS | Yahoo Finance, Fool.com |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Wikipedia - Piotr Szulczewski](https://en.wikipedia.org/wiki/Piotr_Szulczewski)
2. [Wikipedia - Wish (company)](https://en.wikipedia.org/wiki/Wish_(company))
3. [CNBC - Wish IPO: Share price up to $22 to $24 per share at $14 billion valuation](https://www.cnbc.com/2020/12/07/wish-seeks-to-raise-1point1-billion-in-ipo.html)
4. [CNBC - Discount marketplace Wish slides after opening below IPO price](https://www.cnbc.com/2020/12/16/wish-ipo-stock-begins-trading-on-nasdaq.html)
5. [Bloomberg - ContextLogic Said to Near $173 Million Sale of Wish to Qoo10](https://www.bloomberg.com/news/articles/2024-02-12/contextlogic-said-to-near-173-million-sale-of-wish-to-qoo10)
6. [Globe Newswire - ContextLogic Completes Sale of Wish to Qoo10](https://www.globenewswire.com/news-release/2024/04/19/2866406/0/en/ContextLogic-Completes-Sale-of-Substantially-All-Operating-Assets-and-Liabilities-Associated-with-Wish-to-Qoo10.html)
7. [CB Insights - Wish Stock Price, Funding, Valuation](https://www.cbinsights.com/company/contextlogic-funding)
8. [8VC - Reflections on our investment in Wish](https://www.8vc.com/resources/reflections-on-our-investment-in-wish)
9. [Seeking Alpha - ContextLogic: $17 Billion To A Negative Enterprise Value](https://seekingalpha.com/article/4606249-contextlogic-17-billion-to-negative-enterprise-value-just-over-2-years)
10. [Fortune - Wish falls in 2020's worst debut for big U.S. IPO](https://fortune.com/2020/12/16/wish-ipo-worst-debut-for-big-u-s-ipo-2020/)
11. [The Motley Fool - Wish Stock Is Down 98% From Its High](https://www.fool.com/investing/2023/02/28/wish-stock-is-down-98-from-its-high-time-to-buy/)
12. [Companies Market Cap - ContextLogic Revenue](https://companiesmarketcap.com/contextlogic/revenue/)
13. [Retail Dive - Wish CEO to step down by February](https://www.retaildive.com/news/wish-ceo-to-step-down-by-february/609993/)
14. [Santa Monica Observer - Infamous for Counterfeits and Flawed Products](https://www.smobserved.com/story/2020/10/14/news/infamous-for-counterfeits-and-flawed-products-wishcom-has-filed-a-draft-with-sec-to-go-public/4969.html)
15. [PingWest - To regain growth, Wish tries to optimize logistics](https://en.pingwest.com/a/9674)
16. [ProductMint - The Wish Business Model](https://productmint.com/the-wish-business-model-how-does-wish-make-money/)
17. [Venture Capital Journal - GGV Capital and Formation8 back Wish](https://www.venturecapitaljournal.com/ggv-capital-and-formation8-back-wish/)
18. [Digital Commerce 360 - Wish to be acquired by Qoo10 for 1% of previous value](https://www.digitalcommerce360.com/2024/02/14/wish-acquired-by-qoo10-marketplaces-previous-value/)
