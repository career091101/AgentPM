---
id: "FOUNDER_199"
title: "Guy Podjarny - Snyk"
category: "founder"
tier: "vc_backed"
type: "case_study"
version: "2.0"
created_at: "2026-01-02"
updated_at: "2026-01-02"
tags: ["developer-security", "DevSecOps", "open-source", "freemium", "PLG", "Israel", "cybersecurity", "B2B-SaaS"]

# 基本情報
founder:
  name: "Guy Podjarny"
  birth_year: null  # 情報源なし
  nationality: "Israel"
  education: "情報源なし（技術系バックグラウンド）"
  prior_experience: "Akamai CTO（Web Experience事業部）、Blaze.io共同創業者兼CTO（2012年Akamaiに買収）、AppScan/AppShield創業者（Web Application Security）"

company:
  name: "Snyk"
  founded_year: 2015
  industry: "Developer Security / DevSecOps / SaaS"
  current_status: "active"
  valuation: "$7.4B（2022年12月Series G）"
  employees: 1162  # 2024年末時点

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: 25  # 推定: Developer toolsセグメント標準、定性情報より（「開発者コミュニティと対話」「developer-first」アプローチ）
    problem_commonality: 85  # 推定: npm依存関係脆弱性は全Node.js開発者の課題、オープンソース依存管理は業界共通
    wtp_confirmed: true  # Freemiumモデルで無料→有料転換を実証、2年で初回$100K ARR達成
    urgency_score: 9  # サプライチェーン攻撃の増加、セキュリティ規制強化により緊急性極めて高い
    validation_method: "Freemiumローンチでの市場検証 + 開発者コミュニティフィードバック + 初期顧客の有料転換"
  psf:
    ten_x_axes:
      - axis: "開発者ワークフローへの統合"
        multiplier: 10  # 従来ツールは独立したスキャナー → SnykはIDE/CLI/CI/CDに直接統合
      - axis: "修復時間（MTTR）"
        multiplier: 5  # 平均84%のMTTR削減を実現
      - axis: "誤検知率"
        multiplier: 3  # AI駆動で誤検知を大幅削減、開発者の信頼獲得
      - axis: "使いやすさ"
        multiplier: 10  # セキュリティ専門家不要、開発者が自力で使用可能
    mvp_type: "freemium_cli"  # 2015年10月にCLIツール「Snyk Stranger」をベータローンチ、無料ダウンロード可能
    initial_cvr: null  # 2016年7月にpaywall導入も失敗、具体的CVRデータなし
    uvp_clarity: 10  # "Developer-first security"は極めて明確
    competitive_advantage: "開発者ワークフロー統合・Freemiumモデル・世界最大の脆弱性DB・AI駆動の優先順位付け"
  pivot:
    occurred: true
    pivot_count: 1
    pivot_trigger: "go_to_market"
    original_idea: "開発者向けself-serveセキュリティツール（開発者=ユーザー=バイヤー想定）"
    pivoted_to: "Developer-first + Security team買収モデル（開発者=ユーザー、セキュリティチーム=バイヤー）"

# クロスリファレンス
cross_reference:
  app_id: "N/A"
  sns_id: "N/A"
  newsletter_id: "N/A"
  related_founders: ["Assaf Hefetz", "Danny Grander", "Peter McKay"]

# 品質管理
quality:
  fact_check: "pass"
  sources_count: 12
  last_verified: "2026-01-02"
  primary_sources:
    - "Snyk Official Website - Contributors/Guy Podjarny"
    - "Contrary Research - Snyk Business Breakdown & Founding Story"
    - "Unusual Ventures - How Snyk found product-market fit"
    - "Accel - To build a community, you need to focus much more on the user than on the buyer"
    - "Heavybit - Guy Podjarny Interview"
    - "Changelog - Founders Talk #71 with Guy Podjarny"
    - "Sacra - Snyk at $300M ARR"
    - "Calcalistech - Snyk growth metrics 2024"
    - "TechCrunch - Snyk Series E funding"
    - "SVB - From seed financing to unicorn"
    - "Tracxn - Snyk Funding Rounds"
    - "Snyk Documentation - Product Features"
---

# Guy Podjarny - Snyk

## 1. 基本情報

| 項目 | 内容 |
|------|------|
| 創業者 | Guy Podjarny（President & Chairman）、Assaf Hefetz（CTO）、Danny Grander（ex-Co-Founder） |
| 生年 | 情報源なし |
| 国籍 | イスラエル |
| 学歴 | 情報源なし |
| 創業前経験 | Akamai CTO（Web Experience事業部）、Blaze.io共同創業者兼CTO（2012年Akamaiに買収、2015年まで在籍）、AppScan/AppShield創業者（Web Application Firewall、DAST/SASTの先駆者） |
| 企業名 | Snyk |
| 創業年 | 2015年 |
| 業界 | Developer Security / DevSecOps / SaaS |
| 現在の状況 | active（IPO準備中） |
| 評価額 | $7.4B（2022年12月Series G）、ARR $343M（2025年推定）、顧客数約4,500社（2024年末） |

**注**: 3名の共同創業者は全員、イスラエル国防軍（IDF）のUnit 8200（SIGINT部隊）出身。Guy Podjarnyは2019年7月にPeter McKayにCEOを譲り、自身はPresident & Chairmanに。

## 2. 創業ストーリー

### 2.1 課題発見（需要発見）

**着想源（2015年以前）**:
- Akamai CTOおよびBlaze.io創業者としてWeb Application Securityに長年従事
- AppScan（DAST）、AppScan Dev Edition（SAST）、AppShield（Web Application Firewall）を開発した実績
- セキュリティツールが「セキュリティ専門家向け」に設計されており、開発者が使わない・使えない問題を認識
- "The way to get developers to embrace security is to build a developer-tool company, not a security company"（セキュリティ会社ではなく開発者ツール会社を作るべき）という信念に到達

**市場環境の変化**:
- オープンソース依存関係の爆発的増加（npmエコシステムの拡大）
- 開発者がサードパーティライブラリに依存する度合いが急激に上昇
- 依存関係の脆弱性追跡が開発者にとって「uncomfortable（不快）な問題」だが避けられない課題に

**初期の仮説**:
- 開発者が日常的に使うツール（CLI、IDE、GitHub）に統合されたセキュリティツールであれば採用される
- オープンソースコミュニティ、特にNode.js/npmエコシステムから始めれば開発者の支持を得られる

### 2.2 CPF検証（Customer Problem Fit）

**インタビュー/顧客検証**:
- 実施数: 推定25件（開発者ツール業界標準、定性情報より）
- 手法: オープンソース開発者コミュニティとの対話、Node.jsエコシステム内での課題ヒアリング
- 発見した課題の共通点:
  - npmパッケージの依存関係脆弱性を追跡する手段がない
  - セキュリティツールは専門知識を要求し、開発者のワークフローを妨げる
  - 既存のセキュリティチームは開発速度を遅らせる「ゲート」として認識されている

**3U検証**:
- **Unworkable（現状では解決不可能）**: 従来のセキュリティツールは独立したスキャナーであり、開発者の日常ワークフローに組み込まれていない
- **Unavoidable（避けられない）**: サプライチェーン攻撃の増加、規制強化（GDPR、SOC2等）により脆弱性管理は必須に
- **Urgent（緊急性が高い）**: 極めて高い（9/10）。大規模なセキュリティ侵害がニュースになる頻度が増加

**支払い意思（WTP）**:
- 確認方法: Freemiumモデルでのローンチ → 2016年7月にpaywall導入（約$100/月/開発者）
- 初回の結果: Self-serve paid planは失敗。開発者は使用するが購入しない（User ≠ Buyer問題）
- 学び: 開発者（ユーザー）とセキュリティチーム（バイヤー）の分離を認識し、GTM戦略をピボット

### 2.3 VC反応と資金調達

**初期VC反応（2015年）**:
- VC懐疑論: "Developers won't care about security"（開発者はセキュリティに関心を持たない）
- "There's no money to be made in developer tooling"（開発者ツールで儲からない）
- Guy Podjarnyと共同創業者はこれらの懐疑論を乗り越え、信念を貫く

**資金調達履歴**:

| ラウンド | 年 | 金額 | 主要投資家 | 評価額 |
|---------|---|------|-----------|--------|
| Seed | 2016年1月 | $3M | Boldstart Ventures | - |
| Series A | 2018年3月 | $7M | Boldstart Ventures、Canaan Partners、Heavybit | $100M |
| Series B | 2018年9月 | $22M | Accel、GV、Boldstart | $100M |
| Series C | 2019年12月 | $70M | Coatue、Tiger Global、Stripes | $500M |
| Series D | 2020年1月 | $150M | Stripes、Coatue、Tiger Global、Salesforce Ventures | $1B（ユニコーン達成） |
| Series E | 2021年3月 | $300M | Accel、Tiger Global、Coatue、Addition、BlackRock | $4.7B |
| Series F | 2021年9月 | $530M | Sands Capital、Tiger Global | $8.5B |
| Series G | 2022年12月 | $196.5M | QIA、Evolution Equity Partners、G Squared | $7.4B |

**累計調達額**: $1.32B（17ラウンド、76投資家）

### 2.4 PSF検証（Problem Solution Fit）

**10倍優位性**:

| 軸 | 従来の解決策（独立セキュリティツール） | Snykソリューション | 倍率 |
|---|------------|-----------------|------|
| ワークフロー統合 | 独立したスキャナー、開発ワークフローの外 | IDE/CLI/CI/CD/GitHubに直接統合 | 10x |
| 修復時間（MTTR） | 数週間〜数ヶ月 | 平均84%削減、数日〜数時間 | 5x |
| 誤検知率 | 高い誤検知でアラート疲労 | AI駆動で誤検知を大幅削減 | 3x |
| 使いやすさ | セキュリティ専門家が必要 | 開発者が自力で使用可能 | 10x |
| コンテキスト提供 | CVE番号のみ | 到達可能性分析、EPSS/CVSSスコア、自動修正PR | 5x |

**MVP**:
- タイプ: Freemium CLI Tool（2015年10月ローンチ）
- 名称: "Snyk Stranger"（無料ダウンロード可能なCLIツール）
- 機能: Node.js依存関係グラフの可視化 + 脆弱性発見
- 初期トラクション:
  - 2015年12月までに約1,000ダウンロード
  - ユーザー登録フローなし、Twitterでフィードバック収集
  - 2016年1月にユーザー登録フロー追加、"wizard"で自動修正機能を実装
  - 2016年夏に約5,000登録ユーザー

**UVP（独自の価値提案）**:
- "Developer-first security"（開発者ファーストのセキュリティ）
- "Find and fix vulnerabilities in your code, open source dependencies, containers, and infrastructure as code"
- セキュリティを開発者の障害ではなく、開発ワークフローの自然な一部にする

**競合との差別化**:
- **Veracode、Checkmarx**: セキュリティチーム向け、重い・遅い・高額
- **Snyk**: 開発者向け、軽量・高速・Freemium
- **Black Duck（Synopsys）**: SCA特化だがワークフロー統合が弱い
- **Snyk**: SCA + SAST + Container + IaC + 統合ワークフロー

## 3. ピボット/失敗経験

### 3.1 初期の失敗

**Self-Serve Paywall失敗（2016年7月）**:
- 約5,000登録ユーザーを獲得後、$100/月/開発者のpaid tierを導入
- 結果: **spectacular failure**（大失敗）
- 原因:
  - ユーザー（開発者）とバイヤー（セキュリティチーム）が異なる
  - 開発者個人は予算を持っていない
  - セキュリティチームは開発者ツールの存在を知らない

**2年間の低成長期（2016-2018）**:
- 初回$100K ARRに到達するまで2年間かかる
- 推定登録ユーザー数: 50,000人（しかし収益化できず）

### 3.2 ピボット

**元のアイデア**:
- 開発者向けself-serveセキュリティツール
- 想定: 開発者 = ユーザー = バイヤー

**ピボット後**:
- Developer-first + Security team買収モデル
- 認識: 開発者 = ユーザー、セキュリティチーム = バイヤー

**きっかけ**:
- 2016年7月のpaywall失敗
- Guy Podjarnyの気づき: "The most common problem that founders face at this point is that they come to the discussion with potential customers from their technical perspective. But customers do not care about their product. Customers care about their problem and whether you can solve it or not."
- セキュリティチームへのアウトリーチ開始: 課題評価、メッセージング調整

**具体的変更**:
1. **マーケティング**: 開発者向け + セキュリティチーム向けの二重戦略
2. **営業**: Enterpriseセールスチーム構築（2018年以降）
3. **プロダクト**: セキュリティチームのニーズ（コンプライアンスレポート、ポリシー管理）を追加
4. **プライシング**: Team/Enterprise tierの強化

**学び**:
- "Sales and marketing are a product in their own right, and they also require iteration"（営業とマーケティングもプロダクトと同様に反復改善が必要）
- ストーリーテリングの重要性: 技術的特徴ではなく、顧客の課題解決にフォーカス

## 4. 成長戦略

### 4.1 初期トラクション獲得

**Freemium戦略**:
- オープンソースプロジェクトは永久無料
- 小規模チーム向けに無料枠を提供（参入障壁を極限まで下げる）
- 一定の利用量を超えるとpaywall（Pro: $25/month/developer〜）

**コミュニティ主導成長**:
- GitHub統合で自動PR作成（脆弱性修正の提案）
- CLI/IDEプラグイン（VS Code、IntelliJ、Eclipse等）で開発者の日常ワークフローに統合
- Twitter、Slack、開発者カンファレンスでのアウトリーチ

**SEOとコンテンツマーケティング**:
- 世界最大の脆弱性データベース（Snyk Vulnerability DB）を無料公開
- 開発者がGoogle検索で「npm vulnerability」「CVE-XXXX-XXXX」を検索するとSnykがヒット
- 技術ブログ、ポッドキャスト（The Secure Developer）でソートリーダーシップ確立

### 4.2 フライホイール

```
無料ユーザー獲得（CLI/GitHub統合）
    ↓
脆弱性スキャン・自動PR体験
    ↓
開発者が社内で共有（バイラル）
    ↓
チームでの採用拡大
    ↓
セキュリティチームが可視性を求める
    ↓
Enterprise契約へ転換
    ↓
収益でプロダクト改善（AI強化、新機能）
    ↓
さらに多くの開発者を惹きつける → フライホイール加速
```

### 4.3 スケール戦略

**Product-Led Growth (PLG)**:
- 開発者が勝手に使い始める（無料）
- プロダクト体験が営業・マーケティングの役割を果たす
- ボトムアップ採用 → トップダウン契約化

**製品拡張（Land and Expand）**:
- 2015年: Snyk Open Source（SCA）
- 2020年: Snyk Container（コンテナセキュリティ）
- 2021年: Snyk Code（SAST、$100M ARR達成）
- 2022年: Snyk Infrastructure as Code（IaC）
- 2023年: Snyk AppRisk（Enterprise-Scale Application Risk Management）
- 2024年: AI統合（DeepCode AI、AutoFix）

**Enterpriseセールス強化**:
- 2023年時点で売上の約20%がEnterprise
- Fortune 500企業の多数が利用
- 専門の営業チーム構築、Customer Success体制強化

**グローバル展開**:
- 本社: 米国ボストン（2021年から）
- オフィス: イスラエル、ロンドン、東京、シンガポール等
- 100以上の言語・プラットフォーム対応

### 4.4 主要マイルストーン

| 年 | イベント | 評価額/指標 |
|----|--------|------------|
| 2015 | Snyk創業、ベータローンチ | - |
| 2016 | Seed $3M（Boldstart） | - |
| 2018 | Series A $7M、Series B $22M | $100M評価額 |
| 2019 | Series C $70M | $500M評価額 |
| 2020 | Series D $150M、ユニコーン達成 | $1B評価額 |
| 2021 | Series E $300M、Series F $530M | $4.7B → $8.5B評価額 |
| 2022 | Series G $196.5M | $7.4B評価額 |
| 2023 | ARR $300M超達成、人員削減10% | - |
| 2024 | ARR $305M、顧客数4,478社、従業員1,162人 | - |
| 2025 | ARR $343M（推定）、IPO準備 | - |

## 5. 使用ツール・サービス

| カテゴリ | ツール/アプローチ |
|---------|-----------------|
| ビジネスモデル | Freemium → Team → Enterprise |
| 成長 | PLG、コミュニティ主導、SEO、GitHub統合 |
| マーケティング | 脆弱性DB公開、技術ブログ、ポッドキャスト（The Secure Developer） |
| プロダクト | CLI、IDE統合（VS Code、IntelliJ等）、CI/CD統合、GitHub Actions |
| 技術スタック | DeepCode AI（脆弱性分析・優先順位付け）、世界最大の脆弱性データベース |
| 資金調達 | Boldstart Ventures、Accel、GV、Tiger Global、Coatue、Sands Capital |
| パートナーシップ | GitHub、GitLab、Docker Hub、AWS、Google Cloud、Azure |

## 6. 成功要因分析

### 6.1 主要成功要因

1. **課題への深い理解**: Guy PodjarnyはWeb Application Security分野で20年以上の経験。開発者がセキュリティツールを嫌う理由を熟知
2. **Developer-First哲学**: セキュリティ会社ではなく開発者ツール会社として構築
3. **Freemium + PLG**: 開発者が無料で試用開始 → バイラル → Enterprise契約の流れを確立
4. **GTMピボットの速さ**: 2016年のpaywall失敗後、User≠Buyer問題を認識し、1年以内にGTM戦略をピボット
5. **製品拡張戦略**: SCAから始めてSAST、Container、IaC、AppRiskへ展開し、Developer Security Platformに進化
6. **コミュニティ構築**: オープンソース開発者コミュニティとの深い関係構築

### 6.2 タイミング要因

- 2015年はnpmエコシステムが爆発的成長期（依存関係の複雑化）
- サプライチェーン攻撃の顕在化（2017年Equifax侵害、2020年SolarWinds等）
- DevOpsからDevSecOpsへのシフトトレンド
- CI/CD普及でセキュリティ自動化の必要性が高まる
- 規制強化（GDPR、CCPA、SOC2等）でセキュリティ投資が急増

### 6.3 差別化要因

- **ターゲット市場**: セキュリティチーム向けツール → 開発者向けツール
- **ビジネスモデル**: 高額エンタープライズライセンス → Freemium + PLG
- **ワークフロー統合**: 独立スキャナー → IDE/CLI/CI/CD統合
- **UX**: セキュリティ専門家向け複雑UI → 開発者向けシンプルUI
- **修復提案**: CVE番号のみ → 自動修正PR + 到達可能性分析 + 優先順位付け

## 7. 日本市場適用性

| 観点 | スコア (1-5) | コメント |
|------|-------------|---------|
| 市場ニーズ | 5 | 日本でもDevSecOpsニーズは高く、サプライチェーン攻撃への懸念は共通 |
| 競合状況 | 3 | Snyk自体が日本進出済み。国内ではSHIFT SECURITYなども存在 |
| ローカライズ容易性 | 4 | 日本語UI対応は必須だが、技術的には問題なし |
| 再現性 | 3 | 類似プラットフォーム構築は困難だが、特化型（例：Rust専用、Go専用）は可能 |
| **総合** | 4 | Developer-first哲学は普遍的に適用可能 |

## 8. orchestrate-phase1への示唆

### 8.1 需要発見（/discover-demand）

- **ドメイン専門性の重要性**: Guy Podjarnyは20年のセキュリティ経験から課題を深く理解
- **Non-Consumer市場への着目**: 既存セキュリティツールを「使えない」開発者という非消費者層を発見
- **オープンソースコミュニティとの対話**: Node.js/npmエコシステム内で課題を検証

### 8.2 CPF検証（/validate-cpf）

- **Freemiumでの検証**: 無料提供で需要の存在を確認後、有料化で支払い意思を検証
- **User≠Buyer問題の早期発見**: paywall失敗を通じて、2層の顧客（開発者とセキュリティチーム）を認識
- **ピボットの速さ**: 失敗を認識後1年以内にGTM戦略をピボット

### 8.3 PSF検証（/validate-10x）

- **10倍優位性の明確化**: ワークフロー統合10倍、MTTR削減5倍、使いやすさ10倍
- **Developer Experience重視**: セキュリティツールをDX（Developer Experience）の問題として再定義
- **自動化**: 手動スキャンではなく、CI/CDパイプラインへの自動統合

### 8.4 スコアカード（/startup-scorecard）

| 評価軸 | スコア | 根拠 |
|--------|--------|------|
| 課題の深刻度 | 9/10 | サプライチェーン攻撃は企業存続に関わる重大リスク |
| 市場規模 | 10/10 | 全世界の開発者2,700万人、DevSecOps市場は急成長中 |
| 10倍優位性 | 9/10 | ワークフロー統合、MTTR削減、使いやすさで圧倒的優位 |
| 創業者適合性 | 10/10 | 20年のセキュリティ経験、Akamai CTO、Blaze.io創業・売却実績 |
| 実行力 | 9/10 | GTMピボット成功、PLG確立、$7.4B評価額達成 |

## 9. 事業アイデア候補

この事例から着想を得られる日本向けビジネスアイデア:

1. **日本語コードベース特化セキュリティ**: 日本語変数名・コメント対応のSASTツール（既存ツールは英語前提）

2. **Rust/Go専用セキュリティプラットフォーム**: 特定言語に特化し、Snykより深い分析を提供

3. **製造業向けIoT/OTセキュリティ**: 日本の強い製造業向けに、組み込みシステム・産業機器の脆弱性管理

4. **金融機関向けDevSecOpsプラットフォーム**: 日本の厳しい金融規制（FISC等）に特化したセキュリティツール

5. **中小企業向け簡易版Snyk**: 大企業向けSnykを簡略化し、中小企業でも導入可能な低価格版

6. **AI生成コードのセキュリティ監査**: Copilot/Cursorなど生成AIが書いたコードの自動脆弱性チェック

7. **コンプライアンス自動化SaaS**: GDPR、SOC2、FISC等の規制対応を自動化

## 10. 創業者語録

> "The way to get developers to embrace security is to build a developer-tool company, not a security company."
> （開発者にセキュリティを受け入れてもらうには、セキュリティ会社ではなく開発者ツール会社を作るべきだ）

> "The most common problem that founders face at this point is that they come to the discussion with potential customers from their technical perspective. But customers do not care about their product. Customers care about their problem and whether you can solve it or not."
> （創業者が最も陥りやすい問題は、技術的視点で顧客と話すことだ。しかし顧客はあなたのプロダクトに関心はない。顧客は自分の課題と、あなたがそれを解決できるかどうかにしか関心がない）

> "Sales and marketing are a product in their own right, and they also require iteration."
> （営業とマーケティングもプロダクトそのものであり、反復改善が必要だ）

> "To build a community, you need to focus much more on the user than on the buyer."
> （コミュニティを構築するには、バイヤーよりもユーザーに注力すべきだ）

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|-------|
| 創業年（Snyk: 2015年） | ✅ PASS | Wikipedia、Contrary Research、複数メディア |
| 評価額（$7.4B、2022年12月Series G） | ✅ PASS | TechCrunch、Snyk公式、Tracxn |
| ARR $343M（2025年推定） | ✅ PASS | Sacra、GetLatka |
| 顧客数4,478社（2024年末） | ✅ PASS | Calcalistech、GetLatka |
| Paywall失敗（2016年7月） | ✅ PASS | Unusual Ventures、Accel、Contrary Research |
| Guy Podjarny Akamai CTO経歴 | ✅ PASS | Heavybit、Snyk公式、Changelog |
| Blaze.io創業・買収（2012年Akamaiに買収） | ✅ PASS | Changelog、Snyk公式 |
| 共同創業者（Assaf Hefetz、Danny Grander） | ✅ PASS | Wikipedia、Tracxn、複数メディア |
| IDF Unit 8200出身 | ✅ PASS | Calcalistech、複数メディア |
| Snyk Code ARR $100M達成 | ✅ PASS | Calcalistech |

**凡例**: ✅ PASS（2ソース以上確認）、⚠️ WARN（1ソースのみ）、❌ FAIL（確認不可）

## 参照ソース

1. [Snyk Official - Guy Podjarny Contributor Page](https://snyk.io/contributors/guy-podjarny/)
2. [Contrary Research - Snyk Business Breakdown & Founding Story](https://research.contrary.com/company/snyk)
3. [Unusual Ventures - How Snyk found product-market fit](https://www.unusual.vc/post/how-snyk-found-product-market-fit-guy-podjarny-on-building-a-dev-centric-security-company)
4. [Accel - To build a community, you need to focus much more on the user than on the buyer](https://www.accel.com/noteworthies/to-build-a-community-you-need-to-focus-much-more-on-the-user-than-on-the-buyer-snyks-guy-podjarny)
5. [Heavybit - Building a Dev-First Security Unicorn](https://www.heavybit.com/library/video/building-a-dev-first-security-unicorn-fireside-with-snyk-founder-guy-podjarny)
6. [Changelog - Founders Talk #71 with Guy Podjarny](https://changelog.com/founderstalk/71)
7. [Sacra - Snyk at $300M ARR](https://sacra.com/research/snyk-at-300m-arr/)
8. [Calcalistech - Snyk's growth slows sharply in 2024](https://www.calcalistech.com/ctechnews/article/684uz2na8)
9. [TechCrunch - Snyk raises $300M at $4.7B valuation](https://techcrunch.com/2021/03/10/snyk-raises-300-million-at-a-4-7-billion-valuation-as-employees-cash-in-and-the-security-company-beefs-up/)
10. [SVB - From seed financing to unicorn](https://www.svb.com/startup-insights/startup-growth/snyk-from-seed-financing-to-unicorn)
11. [Tracxn - Snyk Funding Rounds](https://tracxn.com/d/companies/snyk/__R962gE3cLhPYE6YfvOOI_C7Ek9zrtlGPOgVeCjDvLBI/funding-and-investors)
12. [Snyk Documentation - What's Snyk](https://docs.snyk.io/discover-snyk/whats-snyk)
