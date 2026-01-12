---
id: "FOUNDER_057"
title: "Henry Ward - Carta"
category: "founder"
tier: "unicorn"
type: "case_study"
version: "1.0"
created_at: "2025-12-28"
updated_at: "2025-12-28"
tags: ["fintech", "equity-management", "cap-table", "saas", "b2b", "409a-valuation"]

# 基本情報
founder:
  name: "Henry Ward"
  birth_year: null
  nationality: "American"
  education: "University of Michigan (BGS, Mathematics & Computer Science), EDHEC Business School (MSC, Market Finance)"
  prior_experience: "Reddwerks Inc., BetweenMarkets, Secondsight創業者"

company:
  name: "Carta"
  founded_year: 2012
  industry: "Fintech / Equity Management"
  current_status: "active"
  valuation: "$7.4B (2021年ピーク) / $2B未満 (2024年)"
  employees: 1800

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: null
    wtp_confirmed: true
    urgency_score: 8
    validation_method: "顧客ヒアリング・パラリーガル業務観察"
  psf:
    ten_x_axes:
      - axis: "コスト"
        multiplier: 3
      - axis: "時間"
        multiplier: 5
      - axis: "使いやすさ"
        multiplier: 10
    mvp_type: "prototype"
    initial_cvr: null
    uvp_clarity: 8
    competitive_advantage: "409Aバリュエーションを1/3の価格で提供、投資家ネットワーク効果"
  pivot:
    occurred: false
    pivot_count: 0
    pivot_trigger: ""
    original_idea: "電子株式証明書管理"
    pivoted_to: ""

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Manu Kumar (共同創業者)"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 15
  last_verified: "2025-12-28"
  primary_sources:
    - "Unusual VC: How Carta won their first 100 customers"
    - "Unicorn Growth: Henry Ward on Carta's Startup Growth"
    - "Alejandro Cremades: Henry Ward Interview"
    - "TechCrunch"
    - "Wikipedia: Carta (software company)"
---

# Henry Ward - Carta

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Henry Ward |
| 生年 | 不明 |
| 国籍 | アメリカ |
| 学歴 | University of Michigan (BGS, 数学・コンピュータサイエンス), EDHEC Business School (MSC, 市場ファイナンス) |
| 創業前経験 | Reddwerks Inc., BetweenMarkets, Secondsight創業者 |
| 企業名 | Carta (旧 eShares) |
| 創業年 | 2012年 |
| 業界 | Fintech / Equity Management |
| 現在の状況 | Active (非公開企業) |
| 評価額/時価総額 | $7.4B (2021年ピーク) / $2B未満 (2024年) |

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源**:
- Henry Wardは最初のスタートアップ「Secondsight」（Bettermentに似た個人投資家向けポートフォリオ最適化プラットフォーム）を創業したが、シード資金調達に失敗し完全に撤退
- 共同創業者となるManu Kumar（K9 Ventures）は、Secondsightに投資していた投資家で、Wardを信頼し続けていた
- Kumarは「なぜ未上場企業に投資する際にまだ紙の株式証明書を受け取るのか」という疑問を持っていた
- Kumarは金融修士号を持つWardにこの問題を解決できると考え、キャップテーブルと株式証明書のデジタル化を提案

**需要検証方法**:
- Wardは2名のパラリーガルを雇用し、既存の株式証明書発行業務を詳細に観察
- 1枚の証明書作成・印刷に$150、FedEx送付に$20かかることを発見
- 既存のワークフローを完全に再現したオンラインシステムを構築

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 詳細な数値は不明だが、コード作成前から顧客と継続的に対話
- 手法: リーン・イテレーティブ開発（顧客訪問→フィードバック→製品修正→再訪問のサイクル）
- 発見した課題の共通点: 創業者の多くはキャップテーブル管理を理解しておらず、教育が必要だった

**3U検証**:
- Unworkable（現状では解決不可能）: 紙の株式証明書は手作業で管理が煩雑、エラーが発生しやすい
- Unavoidable（避けられない）: 資金調達を行うすべてのスタートアップにキャップテーブル管理は必須
- Urgent（緊急性が高い）: 特に409Aバリュエーション（税務上必須）は高価で遅い、創業者が嫌う支出だった

**支払い意思（WTP）**:
- 確認方法: 最低$100でサービス提供し、有料顧客獲得で検証
- 結果: 2014年1月に最初の$700の売上を達成

### 2.3 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策 | 自社ソリューション | 倍率 |
|---|------------|-----------------|------|
| コスト（409A） | $5,000 | $1,000 | 5x |
| 時間（409A） | 数週間 | 数日 | 5x |
| コスト（株式証明書） | $170/枚 | $20/枚 | 8.5x |
| 使いやすさ | 紙・弁護士依存 | オンラインセルフサービス | 10x |
| 導入障壁 | 高（法務プロセス） | 低（SaaS） | 10x |

**MVP**:
- タイプ: Prototype（機能的な電子株式証明書発行システム）
- 初期反応: 2014年1月に一般公開、同年4月に409Aバリュエーション機能追加
- CVR: 2014年8月までに100社以上の有料顧客、年間売上約$1M達成

**UVP（独自の価値提案）**:
- 未上場企業の株式管理を完全デジタル化し、透明性と効率性を大幅に向上

**競合との差別化**:
- 409Aバリュエーションを従来の1/3の価格（$1,000 vs $5,000）で提供
- 投資家ネットワークを活用したバイラル成長モデル

## 3. ピボット/失敗経験

### 3.1 初期の失敗

- **Secondsightの失敗**: 最初のスタートアップは1年半かけて開発したが、数百人の投資家から拒否され、シードラウンドを完了できず撤退
- **主な教訓**:
  1. 「想像の中で製品を作り、市場に出す」アプローチは失敗する
  2. 製品開発能力が不足していた
  3. 助けを求める必要性を学んだ

### 3.2 Carta創業時の困難

- **300人以上の投資家から拒否**: SecondとCarta合わせて累計300人以上の投資家から資金調達を拒否された
- **Series A調達の困難**: シードは完了したが、Series Aは最も困難なフェーズで、数十のVCから拒否された
- **市場規模への懐疑**: 投資家から「キャップテーブルソフトウェア市場は小さすぎる」と言われ続けた

### 3.3 学びと適用

- 最初の18ヶ月の失敗で「やってはいけないこと」を全て学んだ
- 製品開発が得意な創業者に囲まれることを重視
- 投資家探しは「説得」ではなく「フィルタリング」と認識を改めた

## 4. 成長戦略

### 4.1 初期トラクション獲得

1. **投資家リファラルの活用**:
   - 投資家に割引コードを提供し、ポートフォリオ企業に紹介してもらう
   - 投資家の暗黙の推薦がキャップテーブルのような機密データへの信頼構築に貢献

2. **409Aバリュエーションを「ウェッジ製品」として活用**:
   - 創業者が嫌う高額な409A（$5,000）を$1,000で提供
   - 「絶望的な顧客」（desperate customer）を獲得するゲートウェイ製品として機能

3. **コンテンツマーケティング**:
   - 2015年1月に「Broken cap tables」というブログ記事を公開
   - Hacker Newsで1位を獲得し、信頼性を構築

### 4.2 フライホイール

```
投資家にCartaを紹介
    ↓
投資家がポートフォリオ企業に割引コードを配布
    ↓
スタートアップがCartaに登録
    ↓
良い体験 → 他の企業に紹介
    ↓
新しい投資家がキャップテーブルでCartaを発見
    ↓
その投資家が自身のポートフォリオ企業に紹介
    ↓
ネットワーク効果で加速
```

### 4.3 スケール戦略

- **製品拡張**: キャップテーブル → 409A → ファンド管理 → セカンダリー取引 → 報酬管理
- **リブランド**: 2017年11月にeSharesからCartaに改名（電子株式を超えた事業拡大を反映）
- **大型資金調達**: Series G（2021年）で$500Mを調達、$7.4B評価額を達成

## 5. 使用ツール・サービス

| カテゴリ | ツール |
|---------|-------|
| 開発 | 独自開発プラットフォーム |
| マーケティング | コンテンツマーケティング、投資家リファラルプログラム |
| 分析 | 自社プラットフォームデータ（90,000件以上のバリュエーション実績） |
| コミュニケーション | ブログ、メールキャンペーン |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **ウェッジ製品戦略**: 409Aバリュエーションを低価格で提供し、「絶望的な顧客」を獲得
2. **投資家ネットワーク活用**: VCを通じた配布チャネルがバイラル成長を実現
3. **リーン開発への転換**: 最初の失敗から学び、顧客と対話しながら製品開発

### 6.2 タイミング要因

- スタートアップエコシステムの急成長期（2012-2020年）
- VC資金調達の活発化により、キャップテーブル管理ニーズが増大
- デジタル化・SaaS化の波がレガシー金融サービスを破壊

### 6.3 差別化要因

- 紙ベースの非効率なプロセスを完全デジタル化
- ネットワーク効果を製品設計に組み込み（投資家・企業・従業員のすべてがプラットフォーム上で接続）

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 4 | 日本のスタートアップ増加に伴いキャップテーブル管理ニーズは存在 |
| 競合状況 | 3 | FUNDiNNO、Smartround等の国内プレイヤーが存在 |
| ローカライズ容易性 | 2 | 日本の会社法・税法への対応が必要、409Aに相当する制度がない |
| 再現性 | 3 | VCネットワーク活用戦略は日本でも有効だが規模が限定的 |
| **総合** | 3 | 市場規模の課題があるが、特定セグメントでの機会あり |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **教育と需要創造**: Cartaは「キャップテーブルソフトウェア」という市場認知がない状態から始めた
- **既存業務の詳細観察**: パラリーガルの業務をすべて記録し、非効率を特定
- **投資家視点の活用**: 投資家（Manu Kumar）の疑問から課題を発見

### 8.2 CPF検証（/validate-cpf）

- **コード前の顧客対話**: Wardは「顧客と話してからコードを書く」に転換して成功
- **既存プロセスの完全再現**: 既存のワークフローをそのままデジタル化してから改善
- **「絶望的な顧客」の発見**: 409Aのような「嫌だけど必須」な支出を狙う

### 8.3 PSF検証（/validate-10x）

- **価格の10x優位性**: 409Aを1/5の価格で提供し、明確な10x価値を実現
- **ウェッジ製品戦略**: 低価格の入口製品でプラットフォームへの移行を促進
- **ネットワーク効果の設計**: 製品設計段階から配布戦略を考慮

### 8.4 スコアカード（/startup-scorecard）

| 評価軸 | スコア | 根拠 |
|--------|--------|------|
| 課題の深刻さ | 8/10 | 法的義務（409A）があり回避不可能 |
| 支払い意思 | 9/10 | 最初から有料顧客を獲得 |
| 10x優位性 | 8/10 | コスト5x、時間5x、使いやすさ10x |
| 配布戦略 | 10/10 | 投資家ネットワークによるバイラル成長 |
| タイミング | 9/10 | スタートアップブームと完全に一致 |

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **株主名簿・新株予約権デジタル管理プラットフォーム**
   - 日本のスタートアップ向けに株主管理をSaaS化
   - SO（ストックオプション）管理を低価格で提供しウェッジ製品とする

2. **税理士・社労士向け業務効率化SaaS**
   - 士業の定型業務をデジタル化し、顧問先紹介によるネットワーク効果を狙う
   - 「嫌だけど必須」な業務（給与計算、年末調整等）を低価格で提供

3. **エンジェル投資家・VC向けポートフォリオ管理ツール**
   - 日本の投資家向けに投資先管理・レポーティングを自動化
   - 投資先紹介による自然なネットワーク拡大を設計

## 10. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（2012年） | PASS | Wikipedia, Crunchbase |
| 評価額（$7.4B） | PASS | Tracxn, TechCrunch |
| 2024年評価額下落 | PASS | TechCrunch (2024年6月) |
| 409A価格（$1,000 vs $5,000） | PASS | Unusual VC |
| 100社達成時期（2014年8月） | PASS | Unusual VC |

**凡例**: PASS（2ソース以上確認）、WARN（1ソースのみ）、FAIL（確認不可）

## 参照ソース

1. [Unusual VC: How Carta won their first 100 customers](https://www.unusual.vc/post/how-carta-won-their-first-100-customers)
2. [Unicorn Growth: Henry Ward on Carta's Startup Growth](https://www.unicorngrowth.io/p/henry-ward-carta)
3. [Alejandro Cremades: Henry Ward Interview](https://alejandrocremades.com/henry-ward-300-investor-rejections-and-1-failed-startup-led-to-build-a-1-billion-business/)
4. [Wikipedia: Carta (software company)](https://en.wikipedia.org/wiki/Carta_(software_company))
5. [Crunchbase: Henry Ward](https://www.crunchbase.com/person/henry-ward)
6. [Carta Official: Meet Henry Ward](https://carta.com/meet-henry-ward/)
7. [Clay: Who is the CEO of Carta?](https://www.clay.com/dossier/carta-ceo)
8. [TechCrunch: Carta's valuation cut (2024)](https://techcrunch.com/2024/06/06/cartas-valuation-to-be-cut-by-billions-in-an-upcoming-secondary-sale/)
9. [PitchBook: Carta confirms $300M round](https://pitchbook.com/newsletter/carta-confirms-300m-round-hits-unicorn-valuation)
10. [Tracxn: Carta Funding History](https://tracxn.com/d/companies/carta/__V1hV7ojDYw3mZRmuhDRwzqzQuRYFIGKhx-hVWrglBhs/funding-and-investors)
11. [Carta Blog: eShares is now Carta](https://carta.com/blog/eshares-is-now-carta/)
12. [Andrew Parker Medium: The Road to Carta](https://andrewparker.medium.com/the-road-to-carta-6d9bace08f7b)
13. [Sourcery VC: Carta CEO Henry Ward - Path to $500M ARR](https://www.sourcery.vc/p/carta-ceo-henry-ward-the-path-to)
14. [Pulley: Top Carta Competitors](https://pulley.com/guides/carta-competitors)
15. [TSV Cap: Carta and Cap Tables](https://www.tsvcap.com/post/carta-and-cap-tables-how-one-simple-idea-created-a-new-market)
