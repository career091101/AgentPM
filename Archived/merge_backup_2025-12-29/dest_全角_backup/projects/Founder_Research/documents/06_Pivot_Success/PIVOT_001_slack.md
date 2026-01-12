---
id: "PIVOT_001"
title: "Stewart Butterfield - Slack (Glitch -> Slack ピボット事例)"
category: "founder"
tier: "pivot"
type: "pivot_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["pivot", "enterprise", "saas", "communication", "b2b", "unicorn", "acquisition"]

# 基本情報
founder:
  name: "Stewart Butterfield (Daniel Stewart Butterfield)"
  birth_year: 1973
  nationality: "カナダ"
  education: "University of Victoria (哲学学士, 1996), Clare College, Cambridge (哲学修士, 1998)"
  prior_experience: "Flickr共同創業者、Yahoo! General Manager"

company:
  name: "Slack Technologies"
  founded_year: 2013
  industry: "Enterprise SaaS / チームコミュニケーション"
  current_status: "acquired"
  valuation: "$27.7B (Salesforce買収価格, 2020年)"
  employees: 2000+

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: null
    wtp_confirmed: true
    urgency_score: 8
    validation_method: "内部ツール使用 -> 友人企業テスト -> ベータ招待"
  psf:
    ten_x_axes:
      - axis: "検索性"
        multiplier: 10
      - axis: "統合性"
        multiplier: 5
      - axis: "リアルタイム性"
        multiplier: 3
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 9
    competitive_advantage: "使いやすさ、統合機能、チャンネルベースのコミュニケーション"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "market_shift"
    original_idea: "Glitch（ソーシャルMMOゲーム）"
    pivoted_to: "Slack（チームコミュニケーションツール）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Stewart Butterfield (Flickr)", "Cal Henderson", "Eric Costello", "Serguei Mourachov"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-28"
  primary_sources: ["TechCrunch", "First Round Review", "Wikipedia", "Masters of Scale", "CNBC", "Failory"]
---

# Stewart Butterfield - Slack（Glitch -> Slack ピボット事例）

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Stewart Butterfield（Daniel Stewart Butterfield） |
| 生年 | 1973年3月21日 |
| 国籍 | カナダ |
| 学歴 | University of Victoria（哲学学士）、Clare College, Cambridge（哲学修士） |
| 創業前経験 | Flickr共同創業者、Yahoo! General Manager |
| 企業名 | Slack Technologies（旧Tiny Speck） |
| 創業年 | 2009年（Tiny Speck）、2013年（Slack） |
| 業界 | Enterprise SaaS / チームコミュニケーション |
| 現在の状況 | 2020年Salesforceに買収 |
| 評価額/買収価格 | $27.7B（約3兆円） |

### 共同創業者

| 名前 | 役割 | バックグラウンド |
|------|------|-----------------|
| Stewart Butterfield | CEO | Flickr共同創業者 |
| Cal Henderson | CTO | Flickr Chief Software Architect |
| Eric Costello | VP of Product | 元Flickr、クライアント開発（ニューヨーク拠点） |
| Serguei Mourachov | VP of Engineering | 元Flickr（バンクーバー拠点） |

## 2. 創業ストーリー

### 2.1 ピボット前：Glitch（2009-2012）

**Tiny Speckの設立**:
- 2009年、Stewart ButterfieldはFlickr売却後にTiny Speckを設立
- 目標：「Glitch」というソーシャルMMOゲームの開発
- 地理的に分散したチーム（バンクーバー、サンフランシスコ、ニューヨーク）

**Glitchの特徴**:
- 非戦闘型のMMO（Massively Multiplayer Online）ゲーム
- アート性の高い、ユニークなゲーム体験
- Facebookなどのウェブサイトでのプレイを想定

**資金調達**:
- 2010年：AccelとAndreessen Horowitzから$5M（シリーズA）
- Marc Andreessenは初期のエンジェル投資家

### 2.2 Glitchの失敗要因

**1. プラットフォーム選択の誤り**:
- Adobe Flashベースで開発
- モバイル（iPhone/Android）への移行が進む中、Flashの需要が急落
- 技術トレンドの変化に対応できず

**2. オンボーディングの失敗**:
- 革新的すぎてユーザーが理解できなかった
- 新規プレイヤーの定着率が低かった
- 「楽しさ」を発見する前にユーザーが離脱

**3. 市場規模の限界**:
- ニッチすぎるオーディエンス
- 収益化に必要なユーザー数に到達できず
- 開発コストに見合う規模を達成できなかった

**4. タイミングの問題**:
- 開発に時間がかかりすぎた
- 市場環境が変化（Flashからモバイルへ）
- Farmville等のソーシャルゲームブームが終焉

**Glitch閉鎖**:
- 2012年12月9日に正式閉鎖を発表

### 2.3 課題発見（需要発見）

**内部ツールの誕生**:
- 分散チームでのコミュニケーション課題を解決するため、独自のメッセージングツールを構築
- メール、チャット、各種アプリが散在し、情報管理が非効率
- 時間の浪費と誤解が頻発

**着想源**:
- 自分たちが直面していた「チームコミュニケーション」の課題
- 既存ツール（メール、IRC、HipChat等）への不満
- 内部ツールとして構築したものが、チーム全体で重宝されていた

**需要検証方法**:
- まず自社チームで使用（ドッグフーディング）
- チームメンバーからの強いポジティブフィードバック
- 「このツールがないと仕事ができない」という声

### 2.4 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数：友人企業6-10社からスタート
- 手法：実際にツールを使ってもらい、フィードバックを収集
- 初期テスト企業：Medium、Rdio、TGC、Cozy等

**発見した課題の共通点**:
- 情報が散在して検索できない
- リアルタイムコミュニケーションと非同期の両立が難しい
- ツール間の統合がない
- 新メンバーのオンボーディングが困難

**3U検証**:
- **Unworkable（現状では解決不可能）**: メールは検索性が低く、情報が埋もれる
- **Unavoidable（避けられない）**: リモートワーク・分散チームの増加で必須
- **Urgent（緊急性が高い）**: 日々の業務効率に直結する課題

**支払い意思（WTP）**:
- 確認方法：ベータユーザーからの熱狂的な反応
- 結果：ユーザーが自発的に他社に紹介、有料化への抵抗なし

### 2.5 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策（メール/IRC） | Slack | 倍率 |
|---|------------|-----------------|------|
| 検索性 | 数百件のメールから探す | チャンネル別・横断検索 | 10x |
| 統合性 | 各ツールを個別に確認 | 70+アプリとの連携 | 5x |
| リアルタイム性 | メール返信待ち | 即座にレスポンス | 3x |
| オンボーディング | 過去メールを転送 | チャンネル履歴を自動参照 | 5x |
| 使いやすさ | 複雑なメール設定 | シンプルなUI | 3x |

**MVP**:
- タイプ：プロトタイプ（内部ツールからの発展）
- 初期反応：「これがないと仕事できない」
- 2013年3月：自社チームでの本格使用開始
- 2013年6月：友人企業への招待開始

**UVP（独自の価値提案）**:
- 「チームコミュニケーションをシンプルに、楽しく、生産的に」
- チャンネルベースのオーガナイズ
- 強力な検索機能
- 多数のサードパーティ連携

**競合との差別化**:
- HipChatより直感的なUI
- メールより検索性が高い
- IRCより導入が簡単
- エンタープライズ向けセキュリティ

## 3. ピボット詳細

### 3.1 ピボット判断のタイミング

**意思決定のスピード**:
- Glitch閉鎖発表後、72時間以内にピボット方針を決定
- 2012年末にAndreessen Horowitzに報告
- 「1週間以内に確実にこのプランで進むことを決定した」（Butterfield）

**ピボット判断の根拠**:
1. 内部ツールへのチームの依存度が非常に高かった
2. 企業向けコミュニケーション市場に明確なギャップがあった
3. 既存の開発リソースとスキルを活用可能
4. 投資家からの理解と支援を獲得

### 3.2 投資家への説明

**Andreessen Horowitzへのピッチ（2012年末）**:
- 「うまくいけば、いつか$1億の売上に到達できる」と控えめに提案
- 投資家は継続を承認
- 既存の資金（Glitch開発用）を活用

**ピッチデッキ（2013年1月8日）**:
- コードネーム：/slack
- サブタイトル：「Help people use computers to work together, better」

**開発タイムライン計画**:
| マイルストーン | 時期 | 内容 |
|--------------|------|------|
| プロトタイプ | 2013年1月末 | 基本機能完成 |
| アルファ | 2013年2月末 | 信頼できる友人向け |
| プライベートベータ | 2013年4月中旬 | 知らない人も含む |
| オープンベータ | 2013年5月末 | 一般公開 |

### 3.3 ベータテスト戦略

**段階的な拡大**:
1. **2013年3月**：自社チームでの使用開始
2. **2013年6月**：友人企業6-10社への招待（Medium、Rdio、TGC、Cozy等）
3. **2013年8月**：プレビューリリース発表、初日8,000人がサインアップ要請
4. **2013年8月-2014年2月**：15,000ユーザーでフィードバック収集

**フィードバック収集方法**:
- 全てのメールに返信可能な設計
- ヘルプチケットを顧客ロイヤルティ向上の機会として活用
- ユーザーの声を即座に製品改善に反映
- 各段階で新たなチームを招待し、フィードバックを増幅

### 3.4 ピボットの学び

1. **内部ツールの可能性を見逃さない**：自分たちが使っているツールが他者にも価値を持つ可能性
2. **迅速な意思決定**：ピボットの判断を72時間で実行
3. **既存リソースの活用**：開発チーム、技術スタック、投資家関係を継続活用
4. **段階的検証**：いきなり全面展開せず、段階的にユーザーを拡大

## 4. 成長戦略

### 4.1 初期トラクション獲得

**ローンチ戦略（2014年2月）**:
- パブリックローンチ
- 24時間以内に8,000社がサインアップ
- 2週間で15,000ユーザー

**成長指標**:
| 時期 | DAU（日次アクティブユーザー） |
|------|---------------------------|
| 2014年2月（ローンチ時） | 15,000 |
| 2014年8月 | 171,000 |
| 2014年11月 | 285,000 |
| 2015年2月 | 500,000 |
| 2015年6月 | 1,100,000 |

### 4.2 フライホイール

```
優れたUX
    ↓
ユーザー満足度向上
    ↓
Word-of-Mouth拡散（Twitter Wall of Love）
    ↓
新規チーム獲得
    ↓
チーム内バイラル効果（1人導入 → チーム全体へ）
    ↓
フィードバック収集
    ↓
製品改善
    ↓
（ループ）
```

### 4.3 Twitter Wall of Love戦略

**概念**:
- 全てのポジティブなツイートを収集
- 別のTwitterアカウントで「Wall of Love」として公開
- ユーザーの生の声を社会的証明として活用

**効果**:
- ピア・ツー・ピアの信頼性
- 双方向の透明なコミュニケーション
- 24時間対応のTwitterカスタマーサポート（6人専任）

### 4.4 スケール戦略

**プロダクトレッドグロース（PLG）**:
- フリーミアムモデル採用
- 無料版で価値を体験 → 有料版へアップグレード
- 営業力に頼らず、製品自体が販売ドライバー

**バイラル係数の最大化**:
- 1人のユーザーがチーム全体を巻き込む
- 組織内での自然な拡散
- エンタープライズ向けセキュリティ・コンプライアンス機能

## 5. 資金調達履歴

| ラウンド | 時期 | 金額 | 評価額 | 主要投資家 |
|---------|------|------|--------|-----------|
| Seed（Tiny Speck） | 2009年 | - | - | Accel |
| Series A（Tiny Speck） | 2010年4月 | $5M | - | Andreessen Horowitz, Accel |
| Pivot資金 | 2013年 | $17M | - | Andreessen Horowitz, Accel, Social Capital |
| Series C | 2014年4月 | $42.75M | - | - |
| Series D | 2014年10月 | $120M | $1.2B | Kleiner Perkins, GV |
| Series E | 2015年3月 | - | $2.76B | - |
| Series F | 2017年9月 | - | $5.1B | - |
| Pre-IPO | 2018年 | - | $7B | - |
| Direct Listing | 2019年6月20日 | - | - | NYSE |
| Salesforce買収 | 2020年12月（発表）、2021年7月（完了） | $27.7B | - | - |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **自分たちの課題を解決**：ドッグフーディングにより、真のペインポイントを理解
2. **迅速なピボット判断**：72時間で意思決定、1週間で方針確定
3. **段階的な検証**：6社→15,000人→パブリックローンチと慎重に拡大
4. **ユーザーフィードバックへの徹底的対応**：全てのメールに返信、即座に改善
5. **プロダクトレッドグロース**：製品の価値で自然に拡散

### 6.2 タイミング要因

- **リモートワークの萌芽**：分散チームの増加
- **SaaSモデルの普及**：エンタープライズソフトウェアのクラウド移行
- **メール疲れ**：情報過多への解決策ニーズ
- **モバイルワークの拡大**：いつでもどこでもコミュニケーション

### 6.3 差別化要因

- **使いやすさ**：コンシューマー向け製品のようなUX
- **統合機能**：70以上のサードパーティ連携
- **チャンネルベース**：情報の整理と検索性
- **文化的要素**：絵文字、カスタムリアクション、遊び心

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本でもSlackは広く普及、リモートワーク需要増 |
| 競合状況 | 3 | Microsoft Teams、Chatwork、LINE WORKSと競合 |
| ローカライズ容易性 | 4 | UIはローカライズ可能、文化的適応は重要 |
| 再現性 | 3 | 大規模プラットフォーム構築は困難、ニッチ特化なら可能 |
| **総合** | 3.75 | 日本市場でのSaaSコミュニケーションツールは飽和気味 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **自分たちの課題から始める**：Butterfieldは自身のチームの課題を解決
- **内部ツールの商業化可能性を評価**：社内で重宝しているツールは外部にも価値がある可能性
- **市場の変化を観察**：Flash衰退、モバイル台頭などのトレンドを認識

### 8.2 CPF検証（/validate-cpf）

- **友人企業からスタート**：6-10社の信頼できる企業でテスト
- **段階的拡大**：いきなり大規模展開せず、フィードバックを得ながら拡大
- **熱狂度の測定**：「これがないと仕事できない」レベルの反応を目指す

### 8.3 PSF検証（/validate-10x）

- **10倍の改善軸を明確化**：検索性、統合性など具体的な改善点
- **既存ソリューションとの比較**：メール、IRC、HipChatとの違いを明確に
- **UVPの言語化**：「チームワークをシンプルに」

### 8.4 スコアカード（/startup-scorecard）

**ピボット成功の評価基準**:
- 迅速な意思決定（72時間以内）
- 既存リソース（チーム、技術、投資家）の活用
- 段階的検証プロセス
- ユーザーフィードバックへの即座対応
- プロダクトマーケットフィットの明確な兆候

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **業界特化型コミュニケーションツール**：医療、法律、建設など特定業界向けのSlackライクなツール
2. **非エンジニア向けコラボレーションツール**：技術者以外の業種（飲食、小売）向けの簡易チームツール
3. **内部ツールのプロダクト化支援**：企業の内部ツールを商用製品化するコンサルティング/開発サービス
4. **日本語特化の情報検索ツール**：日本語の曖昧検索、敬語対応を強化したビジネスチャット

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2009年Tiny Speck、2013年Slack） | PASS | Wikipedia、TechCrunch |
| Glitch閉鎖（2012年12月9日） | PASS | Failory、Wikipedia |
| 買収価格（$27.7B） | PASS | CNBC、TechCrunch |
| 初日8,000サインアップ | PASS | First Round Review、buildd.co |
| 共同創業者4名 | PASS | TechCrunch、buildingslack.com |
| ピボット判断72時間 | PASS | Masters of Scale |
| 2014年2月パブリックローンチ | PASS | 複数ソース |

**凡例**: PASS（2ソース以上確認）、WARN（1ソースのみ）、FAIL（確認不可）

## 参照ソース

1. [TechCrunch - The Slack origin story](https://techcrunch.com/2019/05/30/the-slack-origin-story/)
2. [First Round Review - From 0 to $1B - Slack's Founder Shares Their Epic Launch Strategy](https://review.firstround.com/from-0-to-1b-slacks-founder-shares-their-epic-launch-strategy/)
3. [Wikipedia - Stewart Butterfield](https://en.wikipedia.org/wiki/Stewart_Butterfield)
4. [Wikipedia - Slack Technologies](https://en.wikipedia.org/wiki/Slack_Technologies)
5. [Failory - What Happened to Glitch, the Social MMO Game?](https://www.failory.com/cemetery/glitch)
6. [Masters of Scale - The big pivot, with Stewart Butterfield](https://mastersofscale.com/stewart-butterfield-the-big-pivot/)
7. [CNBC - Salesforce buys Slack for $27.7 billion](https://www.cnbc.com/2020/12/01/salesforce-buys-slack-for-27point7-billion-in-cloud-companys-largest-deal.html)
8. [buildd.co - How Slack went from 0 to $1B valuation in just 8 months](https://buildd.co/marketing/slack-marketing-strategy)
9. [Building Slack - The death of Glitch, the birth of Slack](https://buildingslack.com/the-death-of-glitch-the-birth-of-slack/)
10. [Building Slack - Day 1](https://buildingslack.com/day-1/)
11. [StartupDevKit - Slack's Startup Story](https://startupdevkit.com/slacks-startup-story-a-remarkable-pivot-from-failing-startup-to-unicorn/)
12. [Founderli - How Slack Transformed From Gaming Failure to Billion Dollar Enterprise](https://www.founderli.com/post/how-slack-transformed-from-gaming-failure-to-billion-dollar-enterprise)
13. [Chattermill - The Slack Growth Hack: Making Word Of Mouth Work](https://chattermill.com/blog/the-slack-growth-hack)
14. [Slidebean - How much is Slack worth?](https://slidebean.com/story/how-much-is-slack-worth)
15. [Britannica Money - Stewart Butterfield](https://www.britannica.com/money/Stewart-Butterfield)
