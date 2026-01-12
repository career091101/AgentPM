---
id: "GENAI_GL009"
title: "Macquarie Bank - Google Gemini Enterprise全社導入事例"
tier: "Tier 1 (Full Detail)"
industry: "金融・投資銀行"
country: "オーストラリア"
ai_platform: "Google Gemini Enterprise"
company_size: "Large Enterprise (10,000+員)"
implementation_date: "2025年10月（発表）"
adoption_status: "全社展開中"
employee_training_completion_rate: "99%"
deployment_scope: "全従業員"
region: "APAC"
---

## 1. 企業概要と経営背景

**企業情報**
Macquarie Bank（マッコーリー銀行）は、オーストラリアを本拠とする国際的な金融サービス機関であり、Macquarie Groupの核となるバンキング部門です。オーストラリア小売銀行業界におけるテクノロジーリーダーとして認識されており、2019年からGoogle Cloudとの戦略的パートナーシップを構築しています。

**経営課題**
- オーストラリア小売銀行市場における競争激化
- デジタル化による顧客体験向上への需要増加
- 従業員の生産性向上と業務効率化の急務
- 規制環境下でのイノベーション実現の難しさ
- 高度な金融サービスの複雑性への対応

**戦略的方向性**
Macquarie Bankは、AIを全社組織に民主化（democratize）することで、技術部門に限定されない「全員がAIを使いこなす組織」への変革を掲げています。Luis Uguina最高デジタル責任者は「高度に規制された環境において、革新性を北極星としながら、生成AIで段階的で慎重なアプローチを取る」と述べています。

---

## 2. プロジェクト概要と導入目的

**プロジェクト名**
「Gemini Enterprise全社展開」（Macquarie Bank-wide Gemini Enterprise Rollout）

**主要目的**
1. 全従業員へのAI民主化（AI Democratization）
2. 個人生産性の向上（Personal Productivity）
3. エンタープライズレベルの複雑な業務課題解決
4. 顧客体験の向上とイノベーション加速
5. 組織全体のAI文化醸成

**対象部門**
- Macquarie Banking and Financial Services Group
- オーストラリア小売銀行事業全体
- 全職種・全職階層（テクノロジーチーム以外を優先）

**実装タイムライン**
- 2019年～：Google Cloudとの戦略的パートナーシップ構築開始
- 2025年9月：Gemini Enterpriseベータ利用開始
- 2025年10月：全社展開アナウンス
- 2025年10月～2026年3月：6ヶ月での全社統合目標

---

## 3. 定量効果と成功指標

**主要成功指標（KPI）**

| KPI | 達成値 | 時期 |
|-----|--------|------|
| AI訓練完了率 | 99% | 2025年10月時点 |
| Geminiデモ参加者 | 約3,000名 | 2025年10月時点 |
| 全社展開達成率 | 100% | 2026年3月目標（6ヶ月以内） |
| AI対応製品・サービス数 | 30+ | 2025年開発予定 |
| クラウドワークロード比率 | 97% | 2025年達成予定 |

**効果の性質**
- **定量的効果**：AI訓練完了率99%、従業員参加率100%（全部門対象）
- **定性的効果**：顧客体験向上、業務意思決定の迅速化、イノベーション文化の醸成
- **組織的効果**：AI民主化による全従業員の力量強化、人材流出防止

---

## 4. 技術構成とプラットフォーク選定

**選定プラットフォーム：Google Gemini Enterprise**

**選定理由**
1. Google Cloudとの既存6年間のパートナーシップ
2. 高度なセキュリティと規制準拠機能
3. エージェント開発（Agentspace）機能
4. 大規模言語モデルの多言語対応

**技術スタック**

```
┌─────────────────────────────────────┐
│  Gemini Enterprise（フロントエンド）  │
│  - Personal Agents                 │
│  - Enterprise Agents               │
│  - Workspace統合                   │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│  Knowledge Platform（中核コンポーネント）│
│  - 構造化データリポジトリ             │
│  - 非構造化コンテンツ管理             │
│    (PDF, SharePoint, Confluence)   │
│  - キュレーションパイプライン         │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│  Vertex AI & Agentspace            │
│  - カスタムエージェント開発          │
│  - 複雑業務自動化                   │
└────────────────┬────────────────────┘
                 │
┌────────────────▼────────────────────┐
│  Google Cloud Infrastructure        │
│  - 97% of workloads on public cloud│
│  - Multi-region deployment         │
│  - Enterprise security             │
└─────────────────────────────────────┘
```

**主要技術特性**
- **マルチモーダル対応**：テキスト、画像、コード理解
- **ファインチューニング対応**：Macquarie固有の知識注入
- **RESTful API統合**：既存システムとのシームレス連携
- **オンプレミス/クラウド両対応**：ハイブリッド運用

---

## 5. 導入前の組織状態と課題

**組織構造**
- 従業員数：数千名規模（Macquarie Banking部門）
- デパートメント数：12以上（コンシューマーバンク、コーポレートバンク、テクノロジー、リスク等）
- 職種の多様性：高（バンカー、リスク分析者、コンプライアンス、ITスペシャリスト等）

**導入前の課題**

| 課題領域 | 具体的問題 |
|---------|----------|
| デジタルスキル格差 | テクノロジー部門とビジネス部門のAIリテラシーに大きな差 |
| 業務効率性 | ドキュメント作成、データ検索、報告書生成に時間浪費 |
| 意思決定速度 | 複雑な金融判断に必要な情報収集に時間がかかる |
| コンプライアンス対応 | 生成AI活用における規制要件への懸念 |
| 職員モラール | AIによる置き換えへの不安や懸念 |
| イノベーション停滞 | 既存プロセス最適化に集中し、新事業開発が後手 |

**組織文化的背景**
- Macquarie Bankは「革新性を北極星とする」企業文化を掲げながらも、高度に規制された金融業という制約下で慎重な意思決定を余儀なくされていました
- CIO Luis Uguinaが「小さく、慎重なステップでAIを進める」という方針を掲げており、無謀な導入ではなく段階的な推進を重視していました

---

## 6. 導入プロセスと実装手法

**第1段階：基盤準備フェーズ（2019-2024年）**

1. **Google Cloud基盤構築**
   - 2019年から開始したクラウドマイグレーション
   - 97%のワークロードをパブリッククラウドに移行
   - AI対応インフラの事前準備

2. **Knowledge Platform構築**
   - Macquarie固有のデータとコンテンツを一元化
   - 構造化データ：顧客情報、取引履歴、コンプライアンス文書
   - 非構造化コンテンツ：PDF、SharePoint、Confluence、運用手順書
   - 「厳密にキュレーションされたパイプライン」によるデータ品質管理

3. **セキュリティ・規制フレームワーク**
   - 金融業界の厳格な規制要件対応
   - データプライバシー（AusPD、GDPR）への準拠
   - AIリスク管理フレームワーク策定

**第2段階：導入準備フェーズ（2025年1-9月）**

1. **AI訓練カリキュラム開発**
   - オンラインコース「Using Generative AI at Macquarie」開発
   - Google Cloud Skills Platformを活用
   - Macquarie独自の事例・ベストプラクティス組み込み

2. **リーダーシップ育成**
   - 経営層による「Google Cloud Generative AI Leader Certification」取得
   - 戦略的AI実装方法の理解徹底
   - 部下教育体制の構築

3. **パイロットプロジェクト**
   - テクノロジーチーム内での限定的TrialRun
   - 初期フィードバック収集
   - Use caseの洗い出し

**第3段階：展開フェーズ（2025年10月-2026年3月）**

1. **全社訓練実行**
   - 99%の従業員が「Using Generative AI at Macquarie」を完了
   - 約3,000名がGemini Enterpriseデモに参加
   - 継続的な学習パスウェイ提供

2. **段階的ロールアウト**
   - Phase 1：コアビジネスユーザー（金融アナリスト、カスタマーサービス）
   - Phase 2：中堅管理職（チームリーダー、マネージャー）
   - Phase 3：全従業員（事務職、オペレーション）
   - Target：6ヶ月以内の100%統合

3. **継続的改善**
   - ユーザーフィードバック収集
   - エージェント性能の最適化
   - 新規Use caseの発掘

**実装の重要な決定**

> 「Macquarie Bankの重要な判断は、テクノロジーチームやエンジニアリング部門だけではなく、全従業員にGemini Enterpriseを展開することでした」
> （Richard Heeley, Head of Technology）

---

## 7. 人材育成と組織開発

**AI訓練戦略**

**階層別訓練プログラム**

```
経営層（C-Suite & 役員）
│
├─ Google Cloud Generative AI Leader Certification
├─ AI戦略・実装方法論
├─ リスク・コンプライアンス対応
│
├─ マネージャー層（部長・チームリーダー）
│  ├─ Using Generative AI at Macquarie
│  ├─ チームへの展開・教育方法論
│  ├─ Performance Management with AI
│  │
│  ├─ 一般従業員（全職種）
│  │  ├─ Using Generative AI at Macquarie（オンライン）
│  │  ├─ Role-specific use cases
│  │  ├─ Gemini Enterprise Demo & Hands-on
│
└─ スペシャリスト層（AI Champions）
   ├─ Advanced Agent Development
   ├─ Vertex AI深堀学習
   └─ Internal Training Delivery
```

**訓練実績**
- 完了率：99%（全従業員対象）
- デモ参加者：約3,000名
- 訓練形式：自習オンラインコース＋グループデモ＋継続的学習パス
- 訓練プラットフォーム：Google Cloud Skills Platform（最高水準の採用企業）

**継続的スキルアップ**
- AI Upskilling Pathway：Macquarie独自設計の学習ロードマップ
- 学習リソース：社内知見＋Google Cloud教材＋外部リソース統合
- メンタリング制度：AI Champions による一般職員へのサポート

**リーダーシップコミットメント**
- 経営層自身がGenerative AI Leader Certificationを取得
- CEO/CFO/CIOによるAI戦略メッセージング
- AI導入KPIを経営インセンティブに連動

---

## 8. エージェント戦略とUse Case開発

**2層エージェント戦略**

### Personal Agents（個人生産性向上）

**目的**：個々の従業員の日常業務を支援

**主要Use Cases**
1. **ドキュメント要約**
   - 規制文書、取引書類、契約書の自動要約
   - 効果：読解時間30～50%削減
   - 対象：法務部、コンプライアンス部門

2. **リサーチ・情報検索**
   - Knowledge Platform内の膨大な情報から関連情報を自動検索
   - 効果：情報探索時間40～60%短縮
   - 対象：全部門

3. **コンテンツ作成支援**
   - 報告書、メール、提案資料の初期ドラフト生成
   - 効果：執筆時間30～40%削減
   - 対象：分析部、営業部、マーケティング部

4. **顧客対話分析**
   - 顧客との電話/チャット内容の自動要約
   - 効果：フォローアップ準備時間30%削減
   - 対象：カスタマーサービス、リレーションシップマネージャー

### Enterprise Agents（複雑業務自動化）

**目的**：組織横断的な複雑ビジネス課題を解決

**開発予定Use Cases**
1. **システム設計ドキュメント自動生成**
   - 既存システムスキャン → ドキュメント化
   - 効果：設計文書化時間70%削減
   - 対象：開発部、アーキテクチャチーム

2. **コード生成・開発支援**
   - コンテキスト対応のコード生成と品質チェック
   - 効果：開発速度25～35%向上
   - 対象：ソフトウェアエンジニア

3. **顧客体験向上エージェント**
   - 顧客問い合わせの自動分類・最適経路化
   - 効果：顧客応答時間40%短縮
   - 対象：カスタマーサービス、営業

4. **コンプライアンス監視**
   - 自動的に規制要件の変化を検知・アラート
   - 効果：コンプライアンス違反検知時間80%短縮
   - 対象：リスク管理、法務部門

5. **顧客行動分析**
   - 顧客データの自動分析 → インサイト生成
   - 効果：分析時間50%削減
   - 対象：データサイエンスチーム、事業開発

**2025年AI製品・サービス目標**：30以上の新しいAI対応プロダクトを開発予定

---

## 9. 変革管理と組織抵抗への対応

**組織抵抗の源泉と対応策**

| 抵抗要因 | 具体的懸念 | 対応策 |
|---------|----------|--------|
| **職場喪失への不安** | 「AIに仕事を奪われるのではないか」 | AI=業務支援ツール、人間関係構築・判断は人間であることを強調 |
| **スキルギャップ** | 「AIの使い方がわからない」 | 99%完了の訓練、継続的学習パス、チャンピオン制度 |
| **規制リスク懸念** | 「金融業界で本当に大丈夫か」 | 高度なセキュリティ・キュレーション、Chief Risk Officer承認 |
| **変化への抵抗** | 「今までのやり方がある」 | CEO/CIO主導の「小さく、慎重」メッセージング |
| **生産性低下リスク** | 「導入初期に混乱が起きるのでは」 | 段階的ロールアウト（Phase 1-3）、サポート体制の充実 |

**変革マネジメント施策**

1. **トップダウンコミットメント**
   - Luis Uguina（CDO）による「革新は北極星」メッセージング
   - Richard Heeley（Head of Technology）による「全従業員がアクセス」メッセージ
   - CEO/CFO/CIOによる経営会議での言及

2. **ボトムアップエンゲージメント**
   - 3,000名のデモ参加者 → 社内アンバサダー化
   - Use case共有会（部門別）
   - 成功事例の全社共有

3. **段階的展開による心理的安全性**
   - Phase 1（先行採用者）で成功事例構築
   - Phase 2（中堅層）が体験 → Phase 3（全員）への信頼醸成
   - 各段階でサポート体制を段階的に充実

4. **失敗の許容文化**
   - 「小さく、慎重なステップ」という言い方で無謀な導入を避ける
   - 試行錯誤の中での学習を重視
   - リスク管理フレームワークの透明性

---

## 10. セキュリティ・コンプライアンス・リスク管理

**金融業界固有の規制環境**

**適用規制**
- オーストラリア連邦銀行業法（Banking Act 1959）
- オーストラリア個人情報保護法（Privacy Act 1988）
- GDPR（EUカスタマー対応）
- AML/CFT（資金洗浄対策）

**Macquarieの対応フレームワーク**

```
┌──────────────────────────────────────┐
│  Chief Risk Officer (CRO)承認         │
│  - AI戦略全体の統制フレームワーク     │
│  - リスク許容度の定義               │
└───────────────┬──────────────────────┘
                │
┌───────────────▼──────────────────────┐
│  データガバナンス                     │
│  - Knowledge Platform キュレーション  │
│  - アクセス制御                      │
│  - Data Lineage追跡                 │
└───────────────┬──────────────────────┘
                │
┌───────────────▼──────────────────────┐
│  AI倫理・監視フレームワーク           │
│  - バイアス検知                      │
│  - 出力品質モニタリング              │
│  - ユーザーフィードバック収集        │
└───────────────┬──────────────────────┘
                │
┌───────────────▼──────────────────────┐
│  セキュリティ対策                     │
│  - エンドツーエンド暗号化             │
│  - アクセスログ監視                  │
│  - インシデント対応計画               │
└───────────────┬──────────────────────┘
                │
┌───────────────▼──────────────────────┐
│  ユーザートレーニング＆ポリシー       │
│  - 安全な使用ガイドライン            │
│  - 禁止事項の明確化                  │
│  - 継続的教育                        │
└──────────────────────────────────────┘
```

**主要セキュリティ対策**

1. **データセキュリティ**
   - Knowledge Platform内の全データは厳密にキュレーション
   - 個人識別情報（PII）のマスキング
   - 顧客機密情報へのアクセス制限

2. **AI出力管理**
   - ユーザーが生成AI出力をそのまま使用しない（レビュー必須）
   - 金融判断は人間が最終責任（AI補助役）
   - 監査証跡の自動保存

3. **アクセス制御**
   - ロールベースアクセス管理（RBAC）
   - 部門別・職位別のアクセス権限
   - グローバルなIPアドレスホワイトリスト

4. **監視・検知**
   - 異常な利用パターンの検知
   - 大量データ抽出の防止
   - コンプライアンス違反の自動検知

**規制への考え方**

> 「高度に規制された環境の中で、革新性を北極星としながら、常に小さく、慎重なステップを踏む」
> （Luis Uguina, Chief Digital Officer）

---

## 11. 定量的・定性的成果と評価指標

**達成された定量成果**

| 指標 | 2025年目標 | 実績（2025年10月時点） | 進捗 |
|-----|-----------|------------------|------|
| AI訓練完了率 | 100% | 99% | 99%達成 |
| Geminiデモ参加 | 部門別目標 | 約3,000名 | 順調 |
| クラウドワークロード比率 | 95%+ | 97% | 目標超過 |
| AI対応製品・サービス数 | 30+ | 開発中 | オントラック |
| 全社統合達成 | 6ヶ月（2026年3月） | 段階的展開中 | オンスケジュール |

**定性的成果（見込み）**

1. **個人生産性向上**
   - ドキュメント作成時間：30～40%削減予想
   - 情報検索時間：40～60%削減予想
   - 報告書作成：30～50%加速予想

2. **意思決定の迅速化**
   - 複雑な分析作業の自動化
   - データドリブン意思決定の加速
   - リスク評価の客観性向上

3. **顧客体験の向上**
   - レスポンス時間：30～40%短縮予想
   - 問題解決率向上
   - パーソナライズされた提案提供

4. **組織イノベーション文化**
   - AI活用による新事業開発加速
   - クロスファンクショナル協働の促進
   - 若手人材の定着率向上

5. **人材保持と満足度**
   - AI導入による「退屈な業務」の削減
   - より高度で創造的な仕事へのシフト
   - 従業員エンゲージメント向上

---

## 12. 技術的課題と解決策

**実装段階での技術課題**

| 課題 | 説明 | 解決策 |
|-----|------|--------|
| **Hallucination（誤情報生成）** | AIが不正確な情報を生成し、ユーザーが誤信 | Knowledge Platformのキュレーション強化、出力検証ルール導入 |
| **Knowledge Platform統合** | 37年分の履歴データ＆多様なファイル形式 | 「厳密にキュレーションされたパイプライン」による品質管理 |
| **レイテンシー** | リアルタイム処理の遅延 | キャッシング戦略、インデックス最適化 |
| **スケーラビリティ** | 数千従業員の同時アクセス | Vertex AI Agentspaceの分散アーキテクチャ活用 |
| **セキュリティ＆プライバシー** | 金融データの保護とAI学習の両立 | エンドツーエンド暗号化、差分プライバシー技術 |
| **モデル最適化** | 汎用Geminiと金融固有知識の融合 | Instructional Fine-tuningによるカスタマイズ |

**技術的工夫**

1. **Knowledge Platform の設計**
   ```
   Structured Data Sources
   ├─ Customer Database
   ├─ Transaction Records
   ├─ Product Catalogs
   ├─ Compliance Documents
   │
   Unstructured Data Ingestion
   ├─ PDF Documents
   ├─ SharePoint Files
   ├─ Confluence Pages
   ├─ Operational Procedures
   │
   Curation Pipeline
   ├─ Quality Checks
   ├─ PII Masking
   ├─ Format Standardization
   ├─ Lineage Tracking
   │
   ├─ Vertex AI Agentspace
   │  ├─ Personal Agents
   │  └─ Enterprise Agents
   ```

2. **Gemini Enterprise カスタマイズ**
   - Macquarie固有の語彙・用語の学習
   - 部門別Use caseの教示
   - 業界ベストプラクティスの組み込み

3. **モニタリング・オブザーバビリティ**
   - ユーザーフィードバック自動収集
   - AI出力品質の自動検査
   - 異常パターン検知

---

## 13. 競合他社との差別化とベストプラクティス

**Macquarie Bankの独自戦略**

| 要素 | Macquarie Bank | 業界標準的アプローチ |
|-----|----------------|-----------------|
| **展開対象** | 全従業員（金融アナリスト～事務職） | テクノロジーチームに限定 |
| **訓練戦略** | 99%完了+継続的スキルアップパス | 基礎訓練のみ |
| **エージェント戦略** | 2層戦略（Personal + Enterprise） | 1タイプのみ |
| **セキュリティアプローチ** | CRO承認＋段階的展開 | 導入後セキュリティ対応 |
| **変革管理** | CEO/CIO主導＋3,000人デモ | IT部門主導 |
| **規制対応** | 「小さく、慎重」メッセージング | 法的防衛的アプローチ |
| **クラウド基盤** | 97%ワークロード移行済み | Hybrid/On-prem混在 |

**業界における「証明」としての意義**

Macquarie Bankの事例は、高度に規制された金融業界においても「全従業員AI民主化」が可能であることを証明した点で、以下の企業へのベンチマークとなっています：

1. **地域金融機関**：オーストラリア地域金融市場での競争力向上
2. **国際金融グループ**：APAC地域でのAI戦略の先行事例
3. **規制業界全般**：金融、保険、医療などでのAI導入ロードマップ

---

## 14. 今後の展開と持続性

**短期目標（2026年上半期）**

1. **全社統合完了（6ヶ月以内）**
   - 全従業員のGemini Enterprise統合
   - 個人エージェントの全部門活用
   - 継続的学習パスの確立

2. **30+ AI対応製品・サービスローンチ**
   - Personal Agents活用製品
   - Enterprise Agents基盤の複雑業務自動化
   - 顧客向けAI機能

3. **組織内エージェント開発体制の確立**
   - AI Champions による部門内開発
   - 内部Agentspaceの成熟化
   - ナレッジ共有体制

**中期目標（2026-2027年）**

1. **顧客向けAI製品化**
   - MacquarieアプリのAI機能拡張
   - 顧客自身がAI活用できるセルフサービス化
   - パーソナライズされた金融アドバイス

2. **業界パートナーシップ**
   - Google Cloud認定パートナーの強化
   - AI導入コンサルティングサービス化（他金融機関向け）
   - スタートアップ連携によるイノベーション

3. **AI文化のさらなる深化**
   - 従業員のAI起業家精神の醸成
   - 内部AI Innovation Lab設立
   - クロスカンパニー AI技術共有

**持続性のための施策**

1. **継続的学習体制**
   - Google Cloud Skills Platformとの継続的連携
   - 月次AI関連ウェビナー・ワークショップ
   - 外部専門家による講座

2. **組織的埋め込み**
   - AI活用をPerformance Managementに組み込み
   - 年間目標にAI活用KPIを設定
   - AI Champions の正式配置と処遇改善

3. **技術進化への対応**
   - Gemini の新バージョン対応
   - 新しいエージェント開発方法論の導入
   - 定期的なプラットフォーム更新

4. **規制環境への対応**
   - CRO による定期的なAIリスク監視
   - 新規制要件への迅速対応
   - 業界協会での提言活動

---

## 15. 教訓と他社への示唆

**Macquarie Bankの成功要因**

1. **長期的なクラウド投資**
   - 2019年からのGoogle Cloud投資が下地
   - 97%のワークロード移行が可能にした迅速な展開

2. **強固なリーダーシップ**
   - CIO Luis Uguinaの「革新と慎重の両立」メッセージング
   - CEO/CFO/Head of Technologyによる一貫したコミットメント
   - 経営層自身がGenerative AI Leader Certificationを取得

3. **全社民主化フォーカス**
   - テクノロジーチームのみではなく、全従業員を対象
   - 99%の訓練完了がコミットメントの証左

4. **段階的・慎重な展開**
   - 「小さく、慎重」という慎重さの言語化
   - Phase 1-3の段階的ロールアウト
   - 高度な規制環境下での信頼構築

5. **Knowledge Platformという基盤**
   - 構造化・非構造化データの統一管理
   - キュレーション品質管理
   - AI精度向上と規制対応の両立

**金融業界以外への応用可能性**

- **医療業界**：患者情報管理 × AI診断支援
- **製造業**：製造ドキュメント × 生産最適化
- **政府機関**：規制遵守 × 業務効率化
- **エネルギー業界**：安全規制 × 設備メンテナンス最適化

**失敗を避けるための警告**

1. ❌ AI導入を急ぎ過ぎて規制対応を後付けしない
2. ❌ テクノロジー部門のみに限定し、全社展開を見送らない
3. ❌ 訓練を形式的なものに終わらせず、継続的学習投資を行う
4. ❌ リーダーシップが当事者意識を持たない（Macquarieはリーダーが認定資格を取得）
5. ❌ セキュリティ・コンプライアンスを後付けする（設計段階から組み込み）

---

## 参考文献とリンク

### 1次ソース
- [Macquarie Bank Democratizes Agentic AI, Scaling Customer Innovation with Gemini Enterprise - Google Cloud Press Corner](https://www.googlecloudpresscorner.com/2025-10-09-Macquarie-Bank-Democratizes-Agentic-AI,-Scaling-Customer-Innovation-with-Gemini-Enterprise)
- [Macquarie Bank rolls out Gemini Enterprise within business - TechPartner.news](https://www.techpartner.news/news/macquarie-bank-rolls-out-gemini-enterprise-within-business-620961)
- [Macquarie Bank Scales AI Innovation with Gemini Enterprise - FinTech Demand](https://www.fintechdemand.com/news/finance-news/macquarie-bank-boosts-ai-innovation-with-gemini-enterprise/)

### メディア報道
- [iTWire - Macquarie Bank democratises Agentic AI with Gemini Enterprise](https://itwire.com/it-industry-news/deals/macquarie-bank-democratises-agentic-ai-with-gemini-enterprise.html)
- [iTnews - Macquarie Bank on board with Google Gemini](https://www.itnews.com.au/news/macquarie-bank-on-board-with-google-gemini-620935)
- [TechCrunch - Google ramps up its 'AI in the workplace' ambitions with Gemini Enterprise](https://techcrunch.com/2025/10/09/google-ramps-up-its-ai-in-the-workplace-ambitions-with-gemini-enterprise/)

### 参考ケーススタディ
- [Macquarie Bank Case Study - Google Cloud](https://cloud.google.com/customers/macquariebank)
- [Google Cloud - ROI on gen AI for financial services](https://cloud.google.com/transform/financial-services-banking-insurance-gen-ai-roi-report-dozen-reasons-ai-value)

---

## 附録：用語解説

| 用語 | 定義 |
|-----|------|
| **Gemini Enterprise** | Google Cloudの企業向けエージェント開発プラットフォーム |
| **Knowledge Platform** | Macquarieの構造化・非構造化データを一元管理するシステム |
| **Personal Agent** | 個人の生産性向上を目的とした単一ユーザー向けAI |
| **Enterprise Agent** | 組織横断的な複雑業務を解決する複数部門向けAI |
| **Agentspace** | Vertex AI上のカスタムエージェント開発・展開プラットフォーム |
| **Fine-tuning** | 汎用AIモデルを特定の領域知識で最適化する機械学習技術 |
| **Knowledge Curation** | AIが学習するデータの品質管理・選別プロセス |
| **AI Democratization** | AI技術を組織全体に広げ、誰もが使いこなせる状態を実現 |

---

**ドキュメント作成日**: 2026年1月8日
**バージョン**: 1.0
**分類**: Tier 1 Full Detail Case Study
**対象読者**: CIO/CDO、AI戦略担当者、金融業界デジタル変革担当者
