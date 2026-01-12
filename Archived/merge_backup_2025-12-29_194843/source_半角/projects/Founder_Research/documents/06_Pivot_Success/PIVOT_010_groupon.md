---
id: "PIVOT_010"
title: "Andrew Mason - Groupon (The Point -> Groupon ピボット事例)"
category: "founder"
tier: "pivot"
type: "pivot_study"
version: "1.0"
created_at: "2025-12-29"
updated_at: "2025-12-29"
tags: ["pivot", "e-commerce", "local_commerce", "collective_buying", "b2c", "ipo"]

# 基本情報
founder:
  name: "Andrew Mason"
  birth_year: 1981
  nationality: "アメリカ"
  education: "Northwestern University (音楽学士, 2003)"
  prior_experience: "Eric Lefkofskyのもとでウェブデザイナー、Northwestern University公共政策修士課程在学中に起業"

company:
  name: "Groupon"
  founded_year: 2008
  industry: "ローカルコマース / 集団購入"
  current_status: "active"
  valuation: "$12.7B (IPO時, 2011年11月) → 現在$500M程度"
  employees: 6000+ (2023年)

# VC投資情報
funding:
  total_raised: "$1.14B+"
  funding_rounds:
    - round: "seed"
      date: "2007-11-01"
      amount: "$1M"
      valuation_post: "不明"
      lead_investors: ["Eric Lefkofsky"]
      other_investors: []
    - round: "series_a"
      date: "2008-11-01"
      amount: "$4.8M"
      valuation_post: "不明"
      lead_investors: ["New Enterprise Associates"]
      other_investors: ["Eric Lefkofsky", "Accel"]
    - round: "series_b"
      date: "2010-04-01"
      amount: "$135M"
      valuation_post: "$1.35B"
      lead_investors: ["DST Global"]
      other_investors: ["NEA", "Accel", "Battery Ventures"]
    - round: "series_d"
      date: "2011-01-01"
      amount: "$950M"
      valuation_post: "$4.75B"
      lead_investors: ["DST Global", "Andreessen Horowitz"]
      other_investors: ["TCV", "Silver Lake", "Kleiner Perkins", "Greylock"]
  top_tier_vcs: ["Andreessen Horowitz", "Kleiner Perkins", "Greylock Partners", "Accel", "NEA"]

# 成功/失敗/Pivot分類
outcome:
  category: "pivot"
  subcategory: "pivot_success"
  failure_pattern: ""
  pivot_details:
    count: 1
    major_pivots:
      - id: "thepoint_to_groupon"
        trigger: "cpf_failure"
        date: "2008-10"
        decision_speed: "3ヶ月（2008年夏～11月）"
        before:
          idea: "The Point - 集団行動プラットフォーム（社会運動・請願・集団購入）"
          target_market: "社会活動家、コミュニティオーガナイザー"
          business_model: "不明確（収益化モデル未確立）"
          cpf_score: 2
        after:
          idea: "Groupon - 地元商店向けの集団購入クーポン（Deal of the Day）"
          hypothesis: "消費者は大幅割引に魅力を感じ、商店は新規顧客獲得のために割引を提供する"
        resources_preserved:
          team: "Andrew Mason、Eric Lefkofsky、Brad Keywell（共同創業者）維持"
          technology: "集団購入の「ティッピングポイント」メカニズムを転用"
          investors: "Eric Lefkofsky、New Enterprise Associates継続支援"
        validation_process:
          - stage: "ローカルテスト（シカゴ）"
            duration: "2008年11月～2009年3月"
            result: "初日でピザ配達20枚のクーポン販売、強い需要確認"
          - stage: "シカゴ拡大"
            duration: "2009年4月～12月"
            result: "月次売上$11M到達（2010年1月）"
          - stage: "全米展開"
            duration: "2010年～2011年"
            result: "150都市展開、売上$800M（2010年末）"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 0 # 情報源なし
    problem_commonality: 55 # Consumer向け、業界ベンチマーク
    wtp_confirmed: true
    urgency_score: 7
    validation_method: "実験的クーポン販売 -> 需要確認 -> 急速拡大"
  psf:
    ten_x_axes:
      - axis: "割引率"
        multiplier: 5
      - axis: "発見容易性"
        multiplier: 3
      - axis: "新規顧客獲得コスト"
        multiplier: 10
    mvp_type: "concierge"
    initial_cvr: null
    uvp_clarity: 9
    competitive_advantage: "地元商店との直接交渉、50%以上の大幅割引、限定感（24時間限定）"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "cpf_failure"
    original_idea: "The Point（集団行動プラットフォーム）"
    pivoted_to: "Groupon（集団購入クーポン）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Eric Lefkofsky", "Brad Keywell", "Marc Andreessen"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-29"
  primary_sources: ["Wikipedia", "TechCrunch", "CNBC", "Britannica Money", "Chicago Magazine", "Mixergy"]
---

# Andrew Mason - Groupon（The Point -> Groupon ピボット事例）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Andrew Mason |
| 生年 | 1981年 |
| 国籍 | アメリカ |
| 学歴 | Northwestern University（音楽学士, 2003） |
| 創業前経験 | Eric Lefkofskyのもとでウェブデザイナー、Northwestern University公共政策修士課程在学中に起業 |
| 企業名 | Groupon（旧The Point） |
| 創業年 | 2007年（The Point）、2008年11月（Groupon） |
| 業界 | ローカルコマース / 集団購入 |
| 現在の状況 | 上場企業（NASDAQ: GRPN） |
| 評価額/時価総額 | IPO時$12.7B（2011年11月） → 現在$500M程度 |

### 共同創業者・主要メンバー

| 名前 | 役割 | バックグラウンド |
|------|------|-----------------|
| Andrew Mason | CEO（2008-2013） | Northwestern大学音楽専攻、公共政策修士課程中退 |
| Eric Lefkofsky | 会長・投資家 | 連続起業家、Groupon前にInnerWorkingsなど創業 |
| Brad Keywell | 共同創業者 | Eric Lefkofskyの共同創業パートナー |

## 2. 創業ストーリー

### 2.1 ピボット前：The Point（2007-2008）

**The Point設立の背景**:
- 2007年、Andrew MasonはNorthwestern University公共政策修士課程在学中
- メンターのEric Lefkofskyから$1Mのシード資金を獲得し、The Pointを創業
- プロジェクト名は、Malcolm Gladwellの著書『The Tipping Point』に着想を得た

**The Pointの構想**:
- 「集団行動プラットフォーム」- 人々が力を合わせて社会課題を解決
- ティッピングポイント（臨界点）の概念を活用
- 目標人数・金額に到達して初めてアクションが実行される仕組み

**The Pointの機能**:
- オンライン請願
- 募金キャンペーン
- ボイコット運動
- 集団購入（Group Buying）

**The Pointの失敗要因**:

1. **コンセプトが抽象的すぎた**:
   - 「社会変革」という目的が広範すぎてマーケティングが困難
   - ユーザーが使い方を理解できなかった
   - 明確なユースケースの欠如

2. **収益化モデルが不明確**:
   - 社会運動プラットフォームとしての収益源が見えない
   - 慈善活動からどのように利益を上げるか不明

3. **トラクション不足**:
   - ユーザー数が伸びない
   - エンゲージメントが低い
   - 投資家へのアピールが弱い

4. **機能の分散**:
   - 集団行動、請願、集団購入など用途が多すぎて焦点が定まらない
   - ユーザーが何のためのサービスか理解しづらい

**興味深いユースケース**:
- Masonは冗談で「シカゴに巨大ドームを建設して冬の寒さから守る」というキャンペーンを立ち上げ
- 一部のユーザーが$5,000～$10,000を pledge
- しかし、こうしたユースケースはビジネスにはつながらなかった

### 2.2 ピボットのきっかけ（2008年夏～秋）

**データから見えたインサイト**:
- The Pointで最も人気のあった機能は「集団購入（Group Buying）」
- ユーザーが商品やサービスを集団で購入し、割引を獲得する行動に強い関心
- 社会活動より、実利的なメリットに反応

**転機となった観察**:
- ユーザーは社会運動よりも「お得な買い物」に興味があった
- 集団購入の「ティッピングポイント」メカニズムは機能していた
- 小売業者との連携可能性を発見

**Eric Lefkofskyの助言**:
- Eric Lefkofskyは、集団購入に焦点を絞ることを提案
- 「The Pointはあまりに抽象的でマーケティングできない。Grouponコンセプトに絞るべきだ」
- 収益化可能なビジネスモデルへの転換を促した

### 2.3 Grouponへの転換（2008年10月～11月）

**ピボット決定プロセス**:
- 2008年夏、The Pointの成長停滞を認識
- 2008年10月、集団購入に特化することを決定
- 2008年11月、「Groupon」としてサービス開始

**名前の由来**:
- "Group" + "Coupon" = Groupon
- シンプルで分かりやすいコンセプト

**初期の実験（シカゴ）**:
- 初日のDeal：The Pointのオフィスがあるビルの1階のピザ店
- $25のピザ配達を$13で提供
- 20枚のクーポンが販売され、強い需要を確認

**初期のオペレーション**:
- 手作業で地元のレストラン・小売店と交渉
- Andrew Mason自身が営業担当として商店を訪問
- PDFクーポンをメールで送信（手動）
- WordPressブログで1日1件のDealを紹介

### 2.4 課題発見（需要発見）

**消費者側の課題**:
- 地元の新しい店やサービスを発見する手段が限られている
- 高額なサービス（スパ、レストラン、アクティビティ）を試すハードルが高い
- 大幅割引があれば新しい体験にチャレンジしたい

**商店側の課題**:
- 新規顧客獲得コストが高い
- 広告予算が限られている
- リピーター獲得の仕組みがない
- 空席・在庫の有効活用ができていない

**着想源**:
- The Pointでの集団購入機能のトラクション
- Malcolm Gladwellの「ティッピングポイント」理論
- 中国の集団購入サイト（Tuangoなど）の成功事例を参考

### 2.5 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数：0件（正式なインタビューは実施せず）
- 手法：実験的にクーポンを販売し、需要を直接測定
- 発見した課題の共通点：大幅割引への強いニーズ、新しい体験への関心

**3U検証**:
- **Unworkable（現状では解決不可能）**: 地元の小規模店舗は大規模広告を打てない
- **Unavoidable（避けられない）**: 消費者は常に節約とお得な情報を求めている
- **Urgent（緊急性が高）**: 不況下（2008年金融危機）で節約志向が強まっていた

**支払い意思（WTP）**:
- 確認方法：実際にクーポンを販売
- 結果：初日から20枚販売、その後急速に拡大
- タイミング：2008年リーマンショック後の不況で、節約志向が高まっていた

### 2.6 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | Groupon | 倍率 |
|---|------------|-----------------|------|
| 割引率 | 10-20%クーポン | 50-90%割引 | 5x |
| 発見容易性 | 地元新聞、チラシ | 1日1件のメール配信 | 3x |
| 新規顧客獲得コスト | $50-100/顧客 | $5-10/顧客（売上シェア） | 10x |
| リスク削減 | 前払い必須 | 最低購入数未達なら不成立 | 3x |
| 話題性 | 通常の広告 | 口コミ・SNS拡散 | 5x |

**MVP**:
- タイプ：Concierge MVP（手作業で運営）
- 初期反応：シカゴで強い需要、口コミで拡散
- 2009年1月時点で月次売上$11M達成

**UVP（独自の価値提案）**:
- **消費者向け**：「毎日、あなたの街で最高のお得情報を1件だけお届け」
- **商店向け**：「新規顧客を大量に獲得し、成果報酬型で広告費を削減」

**競合との差別化**:
- **従来のクーポンサイト**: 大量のクーポンで選択に迷う → Grouponは1日1件で迷わない
- **新聞広告**: 幅広い層に届くが効果測定困難 → Grouponは販売数で即座に効果測定
- **Google AdWords**: クリック課金で費用がかさむ → Grouponは成果報酬型

## 3. ピボット詳細

### 3.1 ピボット判断のタイミング

**意思決定のスピード**:
- 2008年夏：The Pointの成長停滞を認識
- 2008年10月：Grouponコンセプトに集中することを決定
- 2008年11月：Groupon正式ローンチ
- **意思決定期間：約3ヶ月**

**ピボット判断の根拠**:
1. The Pointで集団購入が最も人気のある機能だった
2. 収益化モデルが明確（売上の50%を手数料として徴収）
3. 地元商店との連携で実証済みのニーズ
4. 2008年金融危機で節約志向が高まっていた

### 3.2 投資家への説明

**Eric Lefkofskyの反応**:
- The Pointの投資家であり、Grouponピボットを強く支持
- 「The Pointはマーケティングが難しすぎる。Grouponなら分かりやすい」
- 追加資金を提供（Series A: $4.8M, 2008年11月）

**New Enterprise Associates（NEA）の参加**:
- Series Aラウンドでリード投資家として参加
- Grouponの急成長を評価し、継続支援

### 3.3 ピボット後の初期成長

**地理的拡大戦略**:
| 時期 | 展開都市数 | 主な都市 |
|------|----------|---------|
| 2008年11月 | 1 | シカゴ |
| 2009年6月 | 12 | ボストン、ニューヨーク、ロサンゼルス等 |
| 2010年1月 | 30+ | 全米主要都市 |
| 2010年12月 | 150+ | 北米全域 |

**売上成長**:
| 時期 | 月次売上 | 前年比 |
|------|---------|-------|
| 2009年1月 | $11M | - |
| 2010年1月 | $11M | - |
| 2010年6月 | $30M+ | - |
| 2011年1月 | $89M | +709% |

**ユーザー成長**:
- 2010年：3,500万登録ユーザー
- 2011年：8,310万登録ユーザー（+228%成長）
- ピーク時：月間100万人以上の新規登録

### 3.4 「史上最速の成長企業」

**記録的な成長スピード**:
- ローンチから16ヶ月で評価額$1B到達（当時最速）
- Zynga（3年）を上回る成長スピード
- 2010年末時点で売上$800M達成（Forbes、Wall Street Journal報道）

**「$1Bまでの最速企業」としての評価**:
- 2010年12月時点で「史上最も早く$1Bの売上に到達する企業」と評価
- 実際には2011年に売上$1.6B達成

### 3.5 ピボットの学び

1. **最も使われている機能に注目**：The Pointで最も人気のあった集団購入に焦点
2. **収益化モデルの明確化**：社会運動 → 明確な手数料モデル
3. **タイミングの重要性**：2008年金融危機で節約志向が追い風
4. **シンプルなコンセプト**：抽象的な「社会変革」→ 分かりやすい「毎日お得」
5. **迅速な検証**：3ヶ月で意思決定、初日から販売開始

## 4. 成長戦略

### 4.1 初期トラクション獲得

**シカゴでのローカル実証（2008年11月～2009年3月）**:
- The Pointオフィスビル1階のピザ店からスタート
- 1日1件のDealをWordPressブログで紹介
- メールリストで配信（初期は手動）

**口コミ成長エンジン**:
- ユーザーがDealを友人にシェア → 紹介ボーナス
- SNS拡散（Facebook、Twitter）
- 「Deal of the Day」の限定感がFOMO（見逃しへの恐怖）を生む

**地域拡大戦略**:
1. シカゴで成功モデル確立
2. 主要都市（ニューヨーク、ボストン、LA）へ展開
3. 各都市に営業チームを配置
4. 地元商店との関係構築

### 4.2 フライホイール

```
魅力的な大幅割引Deal
    ↓
消費者登録・購入
    ↓
メール配信リスト拡大
    ↓
商店への提案力向上（「10万人にリーチ可能」）
    ↓
より良いDealを交渉
    ↓
口コミ・SNS拡散
    ↓
新規ユーザー獲得
    ↓
（ループ）
```

### 4.3 スケール戦略

**営業組織の急拡大**:
- 各都市に営業チームを配置
- 地元商店との直接交渉
- 2010年時点で数千人の営業担当者を雇用

**FOMO（Fear of Missing Out）マーケティング**:
- 24時間限定のDeal
- 数量限定
- タイムカウントダウン
- 「売り切れ御免」の緊迫感

**国際展開**:
- 2010年：ヨーロッパ、アジア、南米へ展開
- 買収による急速な国際化（類似サービスを買収）
- 2010年末時点：35以上の国、500以上の都市

**プロダクト拡張**:
- Groupon Goods（物販）
- Groupon Getaways（旅行）
- Groupon Reserve（レストラン予約）

### 4.4 バリューチェーン

**Grouponのビジネスモデル**:
1. 商店と交渉し、50-90%割引のDealを設定
2. Grouponサイト・メールで宣伝
3. 消費者が購入（前払い）
4. 売上の50%をGrouponが手数料として取得
5. 残り50%を商店に支払い

**商店にとってのメリット**:
- 新規顧客を大量獲得
- 成果報酬型（売れた分だけ支払い）
- リピーター獲得のチャンス
- 空席・在庫の有効活用

**消費者にとってのメリット**:
- 50-90%の大幅割引
- 新しい体験の発見
- リスク低減（最低購入数未達なら返金）

## 5. 資金調達履歴

| ラウンド | 時期 | 金額 | Post-Money評価額 | リード投資家 | 主要投資家 |
|---------|------|------|----------------|------------|----------|
| Seed（The Point） | 2007年11月 | $1M | - | Eric Lefkofsky | - |
| Series A | 2008年11月 | $4.8M | - | New Enterprise Associates | Eric Lefkofsky, Accel |
| Series B | 2010年4月 | $135M | $1.35B | DST Global | NEA, Accel, Battery Ventures |
| Series D | 2011年1月 | $950M | $4.75B | DST Global, Andreessen Horowitz | TCV, Silver Lake, Kleiner Perkins, Greylock |
| IPO | 2011年11月4日 | $700M | $12.7B | - | NASDAQ上場 |

**総資金調達額**: $1.14B+（IPO前）

**主要VCパートナー**:
- Andreessen Horowitz（Marc Andreessen: 「オフライン商店へのインターネットマーケティングの扉を開いた」）
- Kleiner Perkins
- Greylock Partners
- Accel
- New Enterprise Associates

### 資金使途と成長への影響

**Series B（$135M, 2010年4月）**:
- 地理的拡大：30都市 → 150都市
- 営業チーム拡大
- 国際展開開始
- 成長結果：売上$11M/月 → $89M/月（10ヶ月後）

**Series D（$950M, 2011年1月）**:
- 史上最大級のVCラウンド（当時）
- 国際M&A（欧州・アジアの競合買収）
- マーケティング強化
- プロダクト拡張（Groupon Goods等）

### VC関係の構築

1. **初期投資家Eric Lefkofskyの重要性**:
   - The Pointから継続支援
   - ピボット判断を後押し
   - 追加ラウンドでも継続投資

2. **Marc Andreessenの支援**:
   - 2011年、Andreessen HorowitzがSeries Dに参加
   - Marc Andreessen: 「オフライン商店にインターネットをマーケティングチャネルとして提供する公式を解明した」
   - Groupon、Facebook、Twitter、Zyngaの全てに投資（当時最も評価額の高いソーシャルメディア企業4社）

## 6. IPOとその後

### 6.1 IPO（2011年11月）

**IPO詳細**:
- 2011年11月4日、NASDAQ上場
- ティッカー：GRPN
- 初値：$28/株
- 初日終値：$26.11/株
- 調達額：$700M
- 評価額：$12.7B
- Google IPO（2004年）以来最大のインターネット企業IPO

**初日パフォーマンス**:
- 初値から-6.75%下落
- IPOバブル懸念が台頭

### 6.2 IPO後の課題

**成長の鈍化**:
- 2012年以降、成長率が低下
- 新規ユーザー獲得コストの上昇
- リピート率の低さ

**ビジネスモデルの持続可能性への疑問**:
- 商店側の不満：クーポン利用者の多くがリピーターにならない
- 採算性の悪化：大幅割引で利益が出ない
- 評判の悪化：「クーポン乞食」を集めるサービス

**会計処理の問題**:
- 売上計上方法に関する批判
- SEC（証券取引委員会）の調査

**Andrew Masonの退任**:
- 2013年2月、取締役会によりCEO解任
- 株価が大幅下落したことが要因
- Masonは退任時にユーモラスなメモを社員に送信（「I was fired today.」）

### 6.3 現在の状況

**Grouponの現状（2023年時点）**:
- 株価：IPO時$28 → 現在$10前後（-64%）
- 時価総額：$12.7B → $500M程度
- 依然として営業中だが、全盛期の勢いは失われている

**Andrew Masonのその後**:
- Detour（オーディオツアーアプリ）創業（2015年）→ Boseに買収（2018年）
- Descript（音声・動画編集ツール）創業（2017年）→ 評価額$1B以上に成長

## 7. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 初期開発 | WordPress（ブログ）、手作業のメール配信 |
| 決済 | PayPal、Stripe |
| メールマーケティング | 独自開発システム（後にMailChimp等） |
| CRM | Salesforce |
| 分析 | Google Analytics |
| コミュニケーション | メール、Slack（後期） |

## 8. 成功要因分析

### 8.1 主要成功要因

1. **明確な価値提案**：「50%以上割引」というシンプルで魅力的なオファー
2. **タイミング**：2008年金融危機後の節約志向
3. **両面市場の構築**：消費者と商店の両方にメリット
4. **FOMO戦略**：24時間限定、数量限定で緊迫感を演出
5. **迅速なピボット**：The Pointの失敗を3ヶ月で判断し転換
6. **地域密着型営業**：各都市に営業チームを配置し、地元商店と関係構築

### 8.2 タイミング要因

- **2008年リーマンショック**：消費者の節約志向が高まった
- **スマートフォン普及**：モバイルでクーポンを表示・利用
- **SNSの台頭**：Facebook、Twitterでのバイラル拡散
- **ローカルビジネスのデジタル化**：地元商店がオンラインマーケティングに関心

### 8.3 差別化要因

- **1日1件のシンプルさ**：選択肢過多を避け、意思決定を簡単に
- **大幅割引（50-90%）**：他のクーポンサイトを圧倒する割引率
- **ティッピングポイント**：最低購入数に達しない場合は不成立（リスク低減）
- **成果報酬型**：商店は売れた分だけ支払い

## 9. 失敗要因分析（IPO後の衰退）

### 9.1 持続可能性の欠如

**商店側の問題**:
- クーポン利用者の多くが1回限りの利用
- リピート率が低く、長期的な顧客獲得につながらない
- 大幅割引で利益が出ない
- ブランド価値の低下（「安売り店」のイメージ）

**消費者側の問題**:
- 新しいDealに慣れてしまい、魅力が低下
- メール配信の頻度が高すぎて疲弊
- 類似サービスの乱立で競争激化

### 9.2 過度な拡大

**成長優先の問題**:
- 急速な地域拡大で品質管理が低下
- 営業チームの質のばらつき
- 粗悪なDealの増加

**国際展開の失敗**:
- 各国の文化・市場の違いを十分に理解せず
- 買収した企業の統合に失敗

### 9.3 競合の台頭

- LivingSocial、Google Offers、Amazon Localなど競合が乱立
- 差別化が困難になり、価格競争に
- Facebookのローカル広告機能がGrouponの価値を代替

## 10. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 4 | 日本でも節約志向は強い、ポンパレモール（リクルート）が類似サービス |
| 競合状況 | 2 | 食べログ、ホットペッパー、ぐるなびなど既存プレイヤーが強い |
| ローカライズ容易性 | 3 | ビジネスモデルは適用可能だが、営業文化の違いあり |
| 再現性 | 2 | 初期の成功は再現可能だが、長期的な持続性が課題 |
| **総合** | 2.75 | 初期成功は可能だが、長期的なビジネスとしては難易度高い |

## 11. orchestrate-phase1への示唆

### 11.1 需要発見（/discover-demand）

- **最も使われている機能に注目**：The Pointで集団購入が最も人気 → Grouponに集中
- **タイミングを見極める**：2008年金融危機が節約志向を加速
- **マクロトレンドを活用**：不況、スマートフォン普及、SNS台頭

### 11.2 CPF検証（/validate-cpf）

- **実験的にMVPを販売**：正式なインタビューより、実際に販売して需要を測定
- **初日から収益化**：ピザクーポン20枚販売で需要確認
- **3U検証**：不況下で「Urgent（緊急性）」が特に高かった

### 11.3 PSF検証（/validate-10x）

- **明確な10倍改善**：新規顧客獲得コスト$100 → $10（10倍改善）
- **シンプルなUVP**：「毎日、最高のお得情報を1件だけ」
- **FOMO要素**：24時間限定、数量限定で緊迫感

### 11.4 スコアカード（/startup-scorecard）

**ピボット成功の評価基準**:
- ✅ 迅速な意思決定（3ヶ月でピボット）
- ✅ 既存リソースの活用（ティッピングポイント機構を転用）
- ✅ 明確な収益化モデル（手数料50%）
- ✅ 初日から検証（ピザクーポン販売）
- ⚠️ 長期的持続性（IPO後に衰退）

**ピボット判断のポイント**:
1. 最も人気のある機能を特定
2. 収益化モデルを明確化
3. マクロトレンドを味方につける
4. 迅速に検証（3ヶ月以内）

## 12. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **業界特化型クーポン**：美容・エステ特化、フィットネス特化など垂直統合型
2. **サブスクリプション型お得情報**：月額制で毎日お得情報を配信（食べログプレミアムの進化版）
3. **地方特化型Deal**：地方都市の商店街活性化に特化したGrouponモデル
4. **B2B版Groupon**：企業向けオフィス用品・サービスの集団購入
5. **リピーター特化型**：1回限りでなく、リピート利用を前提とした割引モデル

## 13. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| The Point創業（2007年） | ✅ PASS | Wikipedia、Britannica Money |
| Grouponローンチ（2008年11月） | ✅ PASS | TechCrunch、Chicago Magazine |
| 評価額$1B到達（16ヶ月） | ✅ PASS | CNBC、Qz.com |
| Series D調達額（$950M） | ✅ PASS | TechCrunch、Vator |
| IPO評価額（$12.7B） | ✅ PASS | Wikipedia、CNBC |
| 2010年売上$800M | ✅ PASS | Forbes、WSJ（Groupon社発表） |
| Andrew Mason解任（2013年2月） | ✅ PASS | 複数ソース |
| Marc Andreessen投資（2011年） | ✅ PASS | TechCrunch、Wikipedia |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Wikipedia - Andrew Mason](https://en.wikipedia.org/wiki/Andrew_Mason)
2. [Wikipedia - Groupon](https://en.wikipedia.org/wiki/Groupon)
3. [Britannica Money - Andrew Mason](https://www.britannica.com/money/Andrew-Mason)
4. [TechCrunch - Groupon Raises, Like, A Billion Dollars](https://techcrunch.com/2011/01/10/groupon-raises-like-a-billion-dollars/)
5. [CNBC - Groupon May Be Fastest-Growing Company Ever](https://www.cnbc.com/2010/12/01/groupon-may-be-fastestgrowing-company-ever.html)
6. [Chicago Magazine - On Groupon and its founder, Andrew Mason](https://www.chicagomag.com/Chicago-Magazine/August-2010/On-Groupon-and-its-founder-Andrew-Mason/)
7. [Mixergy - The Story Of Groupon: From Failure To An Industry-Changing, Profit Machine](https://mixergy.com/interviews/andrew-mason-groupon-interview/)
8. [Canvas Business Model - What is Brief History of Groupon Company?](https://canvasbusinessmodel.com/blogs/brief-history/groupon-brief-history)
9. [The Growth Playbook - How Groupon became the "fastest growing company ever"](https://thegrowthplaybook.substack.com/p/how-groupon-became-the-fastest-growing)
10. [Vator - Groupon closes monstrous $950M round](https://vator.tv/news/2011-01-10-groupon-closes-monstrous-950m-round)
11. [Qz.com - Groupon is still the fastest company to reach a billion-dollar valuation](https://qz.com/398090/groupon-still-the-fastest-company-to-reach-a-unicorn-billion-dollar-valuation)
12. [The Startup Graveyard - Groupon: The Fastest Growing Startup in History](https://www.thestartupgraveyard.com/p/groupon)
13. [Social Media Today - 10 Questions with Andrew Mason of ThePoint.com](https://www.socialmediatoday.com/content/10-questions-andrew-mason-thepointcom)
14. [TechCrunch - Is Groupon Worth $25 Billion?](https://techcrunch.com/2011/03/17/groupon-25-billion/)
15. [Wikipedia - Andreessen Horowitz](https://en.wikipedia.org/wiki/Andreessen_Horowitz)
