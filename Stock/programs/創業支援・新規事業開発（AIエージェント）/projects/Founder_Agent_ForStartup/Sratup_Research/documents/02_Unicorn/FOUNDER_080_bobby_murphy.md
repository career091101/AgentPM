---
id: "FOUNDER_080"
title: "Bobby Murphy - Snapchat/Snap Inc."
category: "founder"
tier: "unicorn"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["snapchat", "social-media", "ephemeral-messaging", "AR", "camera-company", "stanford"]

# 基本情報
founder:
  name: "Bobby Murphy"
  birth_year: 1988
  nationality: "アメリカ"
  education: "スタンフォード大学 数学・計算科学専攻 学士"
  prior_experience: "Revel Systems ソフトウェアエンジニア"

company:
  name: "Snap Inc."
  founded_year: 2011
  industry: "ソーシャルメディア / AR / カメラ"
  current_status: "ipo"
  valuation: "時価総額 約$18B（2024年）"
  employees: 4911 # 2024年12月末時点（出典: MacroTrends, Stock Analysis - 2023年5,289人から7.15%減）

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 20 # 推定: 友人・家族への初期配布約20人 + 南カリフォルニア高校生の行動観察（出典: Cornell Networks, BenchHacks）
    problem_commonality: 25 # 推定: 米国高校生人口約1,500万人のうちスマホ所有層（2012年時点約25%）（出典: Inc.com, Cornell Networks）
    wtp_confirmed: true # 初期無料→後に広告・Snapchat+サブスク（年間$500M超、2024年）で収益化確認（出典: Wikipedia, Snap IR）
    urgency_score: 7 # 高校生の日常コミュニケーションニーズ（FOUNDER_079と同様）
    validation_method: "プロトタイプ配布・口コミ拡散観察"
  psf:
    ten_x_axes:
      - axis: "プライバシー"
        multiplier: 10
      - axis: "気軽さ"
        multiplier: 5
    mvp_type: "prototype"
    initial_cvr: 0.64 # 推定: 127ユーザー（2011年夏）→ 3,000 DAU（2012年初頭）→ 30,000 DAU（同月末）、初期1ヶ月で約10倍成長（出典: Cornell Networks, BenchHacks）
    uvp_clarity: 9
    competitive_advantage: "消えるメッセージという新カテゴリ創出"
  pivot:
    occurred: true
    pivot_count: 2
    pivot_trigger: "market_shift"
    original_idea: "Picaboo（消える写真共有）"
    pivoted_to: "Snapchat（Z世代向けエフェメラルメッセージング）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Evan Spiegel", "Reggie Brown"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-28"
  primary_sources:
    - "Wikipedia - Bobby Murphy"
    - "TechCrunch"
    - "Forbes"
    - "CNBC"
    - "Snap Inc. Investor Relations"
---

# Bobby Murphy - Snapchat/Snap Inc.

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Bobby Murphy（Robert Cornelius Murphy） |
| 生年 | 1988年7月19日（カリフォルニア州バークレー） |
| 国籍 | アメリカ（母はフィリピン出身、父はアイルランド・スコットランド・イングランド系） |
| 学歴 | スタンフォード大学 数学・計算科学専攻（2010年卒） |
| 創業前経験 | Revel Systems ソフトウェアエンジニア（1年間） |
| 企業名 | Snap Inc.（旧Snapchat Inc.） |
| 創業年 | 2011年 |
| 業界 | ソーシャルメディア / AR / カメラテクノロジー |
| 現在の状況 | NYSE上場（2017年IPO） |
| 評価額/時価総額 | 約$18B（2024年時点） |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- 2011年4月、スタンフォード大学の同級生Reggie Brownが「送った写真が消えるアプリ」のアイデアをEvan Spiegelに提案
- SNSでの「永続する投稿」がもたらす心理的プレッシャーという課題に着目
- 若者が気軽にコミュニケーションできる場の欠如

**需要検証方法**:
- スタンフォード大学のフラタニティ（Kappa Sigma）メンバーへの初期配布
- 友人・家族約20人への限定リリース（2011年9月）
- ユーザー行動の観察（利用時間帯・頻度の分析）

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 正式なインタビュー数は不明
- 手法: プロトタイプ配布と行動観察
- 発見した課題の共通点: 若者は「残らない」コミュニケーションを求めていた

**3U検証**:
- Unworkable（現状では解決不可能）: 既存SNSでは全ての投稿が永続化され、自己検閲が発生
- Unavoidable（避けられない）: デジタルコミュニケーションは避けられないが、気軽さが欠如
- Urgent（緊急性が高い）: 高校生・大学生の日常コミュニケーションニーズ

**支払い意思（WTP）**:
- 確認方法: 初期は無料アプリとして配布、後に広告モデルで収益化
- 結果: 直接的なWTP検証は実施せず、エンゲージメント指標で代替検証

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 |
|---|------------|-----------------|------|
| プライバシー | Facebook/Instagram（永続投稿） | 消えるメッセージ | 10x |
| 気軽さ | 編集・加工が必要 | 素の自分を共有 | 5x |
| 心理的負担 | いいね数・フォロワー数のプレッシャー | 数値化されない交流 | 5x |
| リアルタイム性 | タイムライン形式 | 瞬間共有 | 3x |

**MVP**:
- タイプ: プロトタイプ（Picaboo）
- 初期反応: 2011年夏時点で127ユーザーのみ、トラクション低迷
- CVR: 初期は低調だったが、高校生への展開後に急成長

**UVP（独自の価値提案）**:
- 「消える」という新しいコミュニケーション体験
- 永続しないからこそ生まれる気軽さと本音

**競合との差別化**:
- Facebook/Instagramとは根本的に異なる「エフェメラル（一時的）」コンセプト
- 若者の「今この瞬間」を共有するニーズに特化

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- 2011年夏：Picabooとしてローンチするも127ユーザーで停滞
- ミレニアル世代への訴求が不発
- マーケティング施策の不足

### 3.2 ピボット（該当する場合）

- 元のアイデア: Picaboo（一般向け消える写真共有アプリ）
- ピボット後: Snapchat（Z世代の高校生・大学生向けメッセージングアプリ）
- きっかけ:
  - Spiegelの母がいとこ（高校生）にアプリを紹介
  - 南カリフォルニアの高校で急速に拡散（午前8時〜午後3時に利用ピーク）
  - 授業中のメモ交換代替ツールとして爆発的普及
- 学び: ターゲット顧客の再定義が成長の鍵

### 3.3 Reggie Brown訴訟

- 2013年2月：共同創業者Reggie Brownが訴訟提起
- 主張：アイデアの発案者としての権利と補償
- 2014年9月：和解成立
- 和解金：$157.5M（2017年IPO申請時に開示）

### 3.4 Spectacles（スマートグラス）の挫折

- 2016年：初代Spectacles発売
- 2017年：$40M相当の未販売在庫を償却
- 購入者の約50%が1ヶ月で使用停止
- 教訓：ハードウェアビジネスの難しさ、製品市場適合の重要性

## 4. 成長戦略

### 4.1 初期トラクション獲得

- 口コミ（Word of Mouth）: 成長チャネルの68%
- 招待機能: 19%
- メディア報道: 9%
- 高校・大学という密なコミュニティでの拡散

**成長タイムライン**:
- 2011年9月: 約20人のテストユーザー
- 2012年初頭: 3万DAU
- 2012年末: 100万DAU
- 2014年8月: 米国18歳の40%が毎日利用

### 4.2 フライホイール

```
ユーザーがSnapを送信
    ↓
受信者がアプリをダウンロード
    ↓
新規ユーザーが友人に送信
    ↓
コミュニティ内で急速拡散
    ↓
ネットワーク効果で価値向上
```

### 4.3 スケール戦略

**機能追加によるプラットフォーム化**:
- 2013年10月: Stories（24時間で消えるストーリー機能）
- 2015年1月: Discover（メディアパートナー11社との提携）
- 2015年: Lenses（ARフィルター機能）
- 2016年: Spectacles（ハードウェア展開）

**資金調達**:
- 2012年5月: $485K（Lightspeed Venture Partners）
- 2013年初頭: $13.5M Series A
- 2013年11月: Facebookからの$3B買収提案を拒否
- 2017年3月: IPO（$3.4B調達、時価総額$24B）

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| クラウド | Google Cloud Platform |
| 開発 | カスタムバックエンドアーキテクチャ |
| AR開発 | Lens Studio（自社開発） |
| 分析 | 内製分析基盤 |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **新カテゴリの創出**: 「消えるメッセージ」という既存にない価値提案
2. **ターゲット顧客の明確化**: Z世代高校生・大学生への集中
3. **技術と製品の融合**: Bobby Murphyの技術力とEvan Spiegelのプロダクトビジョン

### 6.2 タイミング要因

- 2011年末: iPhone 4S普及（フロントカメラ搭載）
- スマートフォンの高校生への浸透期
- SNS疲れ・プライバシー意識の高まり

### 6.3 差別化要因

- エフェメラル（一時的）というコンセプトの独自性
- 数値化されないコミュニケーション（いいね数非表示）
- カメラファーストのUI設計

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 3 | LINEの強い地位、消えるメッセージ需要は一定あり |
| 競合状況 | 2 | LINE、Instagram、TikTokが既に浸透 |
| ローカライズ容易性 | 4 | 言語対応のみで機能は普遍的 |
| 再現性 | 2 | プラットフォーム系は後発不利 |
| **総合** | 2.75 | 直接的な模倣より、エフェメラル概念の応用が有効 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **観察ベースの需要発見**: 利用時間帯パターン（8時〜15時）から高校生ニーズを発見
- **既存ソリューションの限界点**: 永続投稿への心理的プレッシャーという未言語化ニーズ
- **コミュニティ起点**: 密なコミュニティ（学校）での行動観察が重要

### 8.2 CPF検証（/validate-cpf）

- **行動データによる検証**: インタビューよりも実際の利用パターン分析を重視
- **ピボット準備**: 初期ターゲット（ミレニアル）から高校生へ柔軟に転換
- **課題の再定義**: 「写真共有」から「気軽なコミュニケーション」へ

### 8.3 PSF検証（/validate-10x）

- **新カテゴリ創出による10x**: 既存の延長線上ではなく、全く新しい価値軸を創出
- **シンプルなMVP**: 消える写真送信のみの最小機能でスタート
- **ネットワーク効果の活用**: 1人が使うと周囲にも波及する設計

### 8.4 スコアカード（/startup-scorecard）

- **市場規模**: ソーシャルメディア市場（巨大）
- **差別化**: エフェメラルという独自カテゴリ（10点）
- **チーム**: 技術（Murphy）とビジネス（Spiegel）の補完関係
- **タイミング**: スマートフォン普及期との合致（10点）
- **実行力**: $3B買収拒否という長期ビジョン

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **エフェメラル・ビジネスコミュニケーション**: Slackの消えるメッセージ特化版、心理的安全性の高い社内コミュニケーション
2. **消えるレビュー・フィードバックサービス**: 正直なフィードバックを促す一時的評価システム
3. **リアルタイム体験共有プラットフォーム**: イベント・旅行などの瞬間共有に特化したサービス

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2011年） | PASS | Wikipedia, TechCrunch, Crunchbase |
| IPO評価額（$24B） | PASS | CNBC, CNN Money |
| DAU（453M, 2024年Q4） | PASS | Statista, Business of Apps |
| Reggie Brown和解金（$157.5M） | PASS | TechCrunch, SEC Filing |
| Bobby Murphy純資産（$2.2B） | PASS | Forbes, Celebrity Net Worth |

**凡例**: PASS（2ソース以上確認）、WARN（1ソースのみ）、FAIL（確認不可）

## 参照ソース

1. [Bobby Murphy - Wikipedia](https://en.wikipedia.org/wiki/Bobby_Murphy)
2. [Snapchat paid Reggie Brown $157.5M - TechCrunch](https://techcrunch.com/2017/02/02/snapchat-reggie-brown/)
3. [Snapchat stock soars in Wall Street debut - CNN Money](https://money.cnn.com/2017/03/02/technology/snapchat-ipo/)
4. [Snap Inc. IPO - CNBC](https://www.cnbc.com/2017/03/02/snapchat-snap-open-trading-price-stock-ipo-first-day.html)
5. [How Snapchat Grew to Be a $25B Company - Better Founder](https://www.betterfounder.com/how-snapchat-grew-to-be-a-25b-company/)
6. [Snapchat Growth Study - BenchHacks](https://benchhacks.com/growthstudies/snapchat-growth-hacks.htm)
7. [Why Snapchat Spectacles failed - TechCrunch](https://techcrunch.com/2017/10/28/why-snapchat-spectacles-failed/)
8. [Snapchat daily active users 2025 - Statista](https://www.statista.com/statistics/545967/snapchat-app-dau/)
9. [Bobby Murphy Net Worth - Celebrity Net Worth](https://www.celebritynetworth.com/richest-businessmen/business-executives/bobby-murphy-net-worth/)
10. [Snap Inc. Investor Relations](https://investor.snap.com/overview/default.aspx)
11. [WSJ: Snapchat turned down $3 billion - CNBC](https://www.cnbc.com/2017/07/12/how-mark-zuckerberg-has-used-instagram-to-crush-evan-spiegels-snap.html)
12. [Snapchat Complete History - Greenlit Content](https://greenlitcontent.com/companies/snapchat-history)
13. [The History of Snapchat - Success Magazine](https://www.success.com/the-history-of-snapchat-how-disappearing-photos-changed-the-game/)
14. [Snapchat Launches Discover - TechCrunch](https://techcrunch.com/2015/01/27/snapchat-launches-discover/)
15. [How Snapchat Gained Success at High Schools - Cornell Networks Blog](https://blogs.cornell.edu/info2040/2019/11/16/how-snapchat-gained-success-by-going-viral-at-high-schools-across-los-angeles/)
