---
id: "CORP_F003"
title: "ATND - リクルート"
category: "corporate_product"
tier: "clear_withdrawal"
type: "failure"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["event_management", "tech_community", "free_service", "API", "recruit_mtl"]

# 基本情報
product:
  name: "ATND"
  name_ja: "アテンド"
  parent_company: "Recruit Holdings"
  division: "Recruit Career (旧: Media Technology Lab)"
  launched_year: 2008
  industry: "Event Management / Community Platform"
  current_status: "shutdown"
  revenue: "非公開"
  valuation: "N/A"
  users: "非公開"

# M&A情報（該当する場合）
acquisition:
  occurred: false
  acquisition_year: null
  acquisition_price: ""
  founder: ""
  original_company: ""
  integration_status: ""

# リクルート撤退基準（失敗事例のみ）
withdrawal:
  occurred: true
  withdrawal_year: 2020
  duration_months: 140  # 2008年9月〜2020年4月 (約11年8ヶ月)
  reason: "顧客満足サービス提供困難・リクルート規模感での収益化困難"
  three_year_profitability: false
  five_year_cumulative_loss: false
  final_status: "完全撤退"

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: null
    wtp_confirmed: null
    urgency_score: null
    validation_method: "社内ニーズ起点（Media Technology Lab自身のイベント運営課題）"
  psf:
    ten_x_axes:
      - axis: "使いやすさ"
        multiplier: null
      - axis: "コスト"
        multiplier: "∞（完全無料）"
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 8
    competitive_advantage: "完全無料・API提供・エンジニアコミュニティ特化"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "マネタイズ試行の失敗"
    original_idea: "無料イベント管理ツール"
    pivoted_to: "eventATND（決済機能付き有料版）→失敗→無料版継続"

# リクルート製品特有フィールド
recruit_specific:
  leveraged_assets:
    - asset_type: "技術力"
      description: "Media Technology LabのOpenID認証技術・API設計ノウハウ"
    - asset_type: "ブランド"
      description: "リクルートブランドによる初期信頼獲得"
  synergy_with_existing:
    - business: "なし"
      synergy_type: ""
  internal_resistance: "収益化困難による事業継続判断の遅れ（11年間継続）"

# クロスリファレンス
cross_reference:
  founder_id: "N/A"
  related_products: ["eventATND"]
  competitor_products: ["Peatix", "Connpass", "Doorkeeper", "Zusaar", "EventRegist"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 8
  last_verified: "2025-12-28"
  primary_sources:
    - "ITmedia NEWS - ATND終了記事"
    - "Internet Watch - ATND終了発表記事"
    - "The Startup - ATND撤退理由分析"
    - "SlideShare - ATND開発プレゼン（Internet Week 2008）"
    - "ITmedia NEWS - eventATND終了記事"
    - "Recruit Holdings - eventATNDプレスリリース"
    - "KickSwitch - ATNDベータ卒業記事"
    - "Diamond - リクルート撤退基準記事"
---

# ATND（アテンド）

## 1. 基本情報

| 項目 | 内容 | ソース |
|------|------|--------|
| 製品名 | ATND（アテンド） | ITmedia NEWS |
| 運営企業 | リクルートホールディングス | ITmedia NEWS |
| 事業部 | リクルートキャリア（開発：Media Technology Lab） | SlideShare |
| ローンチ年 | 2008年9月 | ITmedia NEWS, SlideShare |
| 撤退年（該当時） | 2020年4月14日 | ITmedia NEWS |
| 買収年（M&A時） | N/A | - |
| 買収額 | N/A | - |
| 現在の状況 | withdrawn（完全撤退） | ITmedia NEWS |
| ピーク売上 | 非公開 | ITmedia NEWS |
| ピークユーザー数 | 非公開（リクルートキャリアが非公開方針） | ITmedia NEWS |

## 2. 製品開発ストーリー

### 2.1 課題発見

**着想源**:
- Media Technology Labが技術セミナーや実イベントで研究成果を積極的に外部公開する際、参加者登録システムが必要だった
- 個人情報管理の課題により、イベント毎にカスタムフォームを作成する非効率な運用が発生
- 自らの課題を解決するためのツールとして内部開発がスタート

**Ring提案制度**（該当時）:
- 該当なし（Media Technology Labの自主開発プロジェクト）

### 2.2 CPF検証（orchestrate-phase1基準）

**CPF達成判定**:

| 指標 | 目標 | 実績 | 判定 | エビデンス |
|------|------|------|:----:|----------|
| インタビュー数 | 20人以上 | 不明 | ⚠️ | 社内ニーズ起点 |
| 課題共通率 | 70%以上 | 不明 | ⚠️ | エンジニアコミュニティで高い共通課題認識 |
| WTP確認 | 50%以上 | 0% | ❌ | 無料サービス前提 |
| 緊急性 | 7/10以上 | 不明 | ⚠️ | イベント運営時に必須 |

**総合判定**: ⚠️ CPF要改善（課題は存在したがWTP未検証）

**検証手法**:
- 社内ニーズ起点での開発（Media Technology Lab自身の課題解決）
- エンジニアコミュニティへのベータ版提供によるフィードバック収集
- OpenID認証の使いやすさ検証（Internet Week 2008で発表）

### 2.3 PSF検証（10倍優位性）

**10倍優位性の検証**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 | エビデンス |
|---|------------|-----------------|------|----------|
| コスト | イベント毎にフォーム作成・有料ツール利用 | 完全無料 | ∞ | 無料提供 |
| 使いやすさ | OpenID意識が強く使いづらい | OpenIDを意識させない認証 | 5x | SlideShare資料 |
| 開発者体験 | API提供なし | オープンAPI提供 | 10x+ | API公開 |

**達成軸数**: 3軸（目標2軸以上）
**PSF達成判定**: ✅ 達成

**MVP**:
- タイプ: prototype（ベータ版として長期運用）
- 初期反応: エンジニアコミュニティで高評価・デファクトスタンダード化

**UVP**:
- 完全無料のイベント管理ツール
- エンジニアに特化した使いやすさ
- オープンAPI提供による拡張性

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- **課題**: 無料サービスのため収益化の道筋が不明確
- **対応**: 2011年12月にeventATND（決済機能付き）をリリース
- **結果**: 決済機能利用者が想定を下回り、2014年3月31日にeventATNDを終了

### 3.2 ピボット（該当する場合）

- **元のアイデア**: 無料イベント管理ツール（ATND）
- **ピボット後**: eventATND（イベント告知から決済まで一元管理）
- **きっかけ**: 収益化の必要性・リクルート規模感でのビジネス化要求
- **学び**:
  - 無料コミュニティサービスに後から決済機能を追加しても受け入れられない
  - ID連携の課題（ATNDとeventATNDの統合困難）
  - エンジニアコミュニティは無料文化が強い

### 3.3 リクルート撤退基準の検証（失敗事例のみ）

**撤退判断のタイムライン**:
- 創業: 2008年9月
- 3年経過時点（2011年9月）:
  - 単月黒字達成: ❌（無料サービスのため収益ゼロ）
  - 判断: 継続＋収益化施策（eventATND開発開始）
- 5年経過時点（2013年9月）:
  - 累損解消: ❌（eventATND失敗により収益化困難）
  - 最終判断: 継続（コミュニティ貢献重視）
- 11年8ヶ月後（2020年4月14日）:
  - 最終判断: 撤退決定

**撤退理由の分析**:
| 要因 | 詳細 |
|------|------|
| 市場要因 | Peatix・Connpass等の競合台頭、無料サービス市場の飽和 |
| 競合要因 | Connpass（無料特化）・Peatix（決済機能）による市場分断 |
| 内部要因 | 収益化困難・リクルート規模感に見合わない事業規模 |
| リクルート基準 | 3年単月黒字未達成・5年累損解消未達成・11年間収益化不可 |

**撤退後の処理**:
- 完全撤退（サービス終了）
- 撤退による損失額: 非公開
- 撤退による学び:
  - 無料サービスでのコミュニティ構築と収益化は両立困難
  - リクルート規模感では小規模サービスの継続判断が遅れる
  - 後発競合（Peatix等）の決済特化戦略が有効だった

**リクルート撤退基準との整合性**:
- 公式基準: 「3年単月黒字・5年累損解消」
- ATND実績: 11年間継続するも収益化失敗
- 判断の遅れ: 通常3-5年で判断すべきところ、11年継続
- 撤退理由: 「顧客に満足してもらえるサービスの提供が困難」（公式発表）
- 実質理由: 「リクルートの規模感に対して全然儲からない」（業界分析）

## 4. 成長戦略

### 4.1 初期トラクション

- 2008年9月: ベータ版リリース
- エンジニアコミュニティで急速に普及
- テック系イベント・勉強会のデファクトスタンダードに成長
- 約7年間ベータ版として運用（2015年頃に正式版へ）

### 4.2 フライホイール

1. エンジニアが無料でイベント作成
2. 参加者が簡単に登録（OpenID認証）
3. イベント情報がコミュニティに拡散
4. 新規主催者が流入
5. （1に戻る）

**課題**: 収益化の仕組みがフライホイールに組み込まれていない

### 4.3 スケール戦略

- **技術戦略**: オープンAPI提供による外部サービス連携
- **コミュニティ戦略**: エンジニアコミュニティとの密接な関係構築
- **無料戦略**: 完全無料による市場シェア獲得
- **失敗**: 収益化戦略の欠如・後発競合の決済特化戦略に敗北

### 4.4 リクルート資産の活用

**活用した既存資産**:

| 資産タイプ | 具体的な活用方法 | 効果 |
|----------|---------------|------|
| 技術力 | Media Technology LabのOpenID認証技術 | 使いやすい認証実現 |
| 開発力 | 社内エンジニアリソース | 高品質なAPI提供 |
| ブランド | リクルートブランド | 初期信頼獲得 |

**既存事業とのシナジー**:

| 既存事業 | シナジータイプ | 具体的な連携 |
|---------|-------------|------------|
| なし | - | 単独事業として運営 |

**シナジー不在の課題**:
- リクルート主要事業（HR・住宅・飲食等）との連携なし
- 孤立した無料サービスとして収益化困難
- リクルート全体の戦略との整合性欠如

## 5. M&A戦略（該当時）

N/A（自社開発製品）

## 6. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | OpenID認証技術 |
| インフラ | リクルート社内インフラ |
| API | オープンAPI提供（ATND API） |

## 7. 成功/失敗要因分析

### 7.1 主要成功要因（成功時）

該当なし（撤退事例）

### 7.2 失敗要因（失敗時）

| フェーズ | 失敗要因 | 具体的内容 |
|---------|---------|----------|
| CPF | WTP未検証 | 無料前提でスタート・支払意思の検証なし |
| PSF | 収益化機能なし | 10倍優位性は達成も収益モデルが欠如 |
| PMF | 後発競合の台頭 | Peatix（決済特化）・Connpass（無料特化）に市場分断 |
| 戦略 | ピボット失敗 | eventATNDの決済機能が受け入れられず |
| 組織 | リクルート基準不適合 | 11年継続も3年単月黒字・5年累損解消未達成 |

**失敗の本質**:
1. **WTP未検証**: 無料サービス前提で収益化の道筋なし
2. **遅すぎたピボット**: 3年後にeventATNDで収益化試行も失敗
3. **市場分断**: 無料（Connpass）と決済（Peatix）で競合に挟まれる
4. **リクルート規模感との不一致**: 小規模コミュニティサービスは継続困難
5. **撤退判断の遅れ**: 5年で判断すべきところ11年継続

## 8. orchestrate-phase1への示唆

### 8.1 /discover-demand への学び

- **学び1**: 社内ニーズ起点は初期検証に有効だが、外部市場のWTP検証が必須
- **学び2**: エンジニアコミュニティは無料文化が強く、後から有料化は困難
- **アクション**: 初期からマネタイズ仮説を組み込む

### 8.2 /validate-cpf への学び

- **学び1**: 課題の存在とWTPは別物・無料で満足されても事業化できない
- **学び2**: 「顧客が喜ぶ」≠「事業として成立」の典型例
- **アクション**: CPF検証時に必ずWTP（支払意思）を確認

### 8.3 /validate-10x への学び

- **学び1**: 10倍優位性を達成しても収益化機能がなければ事業化失敗
- **学び2**: 「完全無料」は10倍優位性だが持続可能性がない
- **アクション**: PSF検証時にビジネスモデルの10倍優位性も検証

### 8.4 /startup-scorecard への学び

- **学び1**: リクルート撤退基準（3年単月黒字・5年累損解消）の重要性
- **学び2**: 11年継続は異例・通常5年で撤退判断すべき
- **学び3**: 「顧客満足サービス提供困難」は建前・実態は「儲からない」
- **アクション**: 3年時点での収益性を必達目標とする

## 9. 他業界適用性

| 業界 | 適用可能性 | コメント |
|------|----------|---------|
| コミュニティプラットフォーム | 高 | 無料サービスの収益化困難という教訓 |
| SaaS | 高 | Freemiumモデルの失敗事例として参考 |
| マーケットプレイス | 中 | 決済機能後付けの困難さ |
| エンタープライズ | 低 | コミュニティ特化の事例 |

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| ローンチ年（2008年9月） | ✅ | ITmedia NEWS, SlideShare |
| 撤退年（2020年4月14日） | ✅ | ITmedia NEWS, Internet Watch |
| eventATND開始（2011年12月） | ✅ | Recruit Holdings PR, Internet Watch |
| eventATND終了（2014年3月） | ✅ | ITmedia NEWS |
| 撤退理由（顧客満足提供困難） | ✅ | ITmedia NEWS（公式発表） |
| 撤退理由（収益化困難） | ✅ | The Startup（業界分析） |
| ユーザー数 | ⚠️ | 非公開（ITmedia NEWS） |
| リクルート撤退基準（3年・5年） | ✅ | Diamond記事 |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみまたは非公開）、❌ FAIL（確認不可）

## 参照ソース

1. [「ATND」4月に終了 「満足いただけるサービスの提供が困難」 開始から11年 - ITmedia NEWS](https://www.itmedia.co.jp/news/articles/2001/16/news097.html)
2. [テック系イベント支援サービス「ATND」、4月14日を最後にサービスを終了すると発表 - INTERNET Watch](https://internet.watch.impress.co.jp/docs/yajiuma/1229168.html)
3. [ATND撤退理由はリクルートの企業文化にあり？ | The Startup](http://thestartup.jp/?p=9638)
4. [ATND - Recruit Media Technology Labs (Internet Week 2008) - SlideShare](https://www.slideshare.net/kawa0117/atnd-presentation)
5. [イベント参加者管理サービス「eventATND」3月末に終了 「ATND」は継続 - ITmedia NEWS](https://www.itmedia.co.jp/news/articles/1402/18/news067.html)
6. [リクルートのソーシャル・チケッティングサービス『eventATND』登場 - リクルートホールディングス](https://oldrelease.recruit-holdings.co.jp/news_data/release/2011/1202_1386)
7. [リクルートのアテンド（ATND）がベータじゃなくなってた - KickSwitch](http://kick-switch.com/web/atnd_event/)
8. [リクルートが「黒字の新規事業」でも見切る訳、爆発的成長を実現する撤退判断基準とは - Diamond](https://diamond.jp/articles/-/307237)
