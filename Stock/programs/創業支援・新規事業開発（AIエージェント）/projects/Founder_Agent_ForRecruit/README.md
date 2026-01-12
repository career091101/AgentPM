# Founder Agent - ForRecruit（企業内新規事業特化版）

**バージョン**: 1.0
**最終更新**: 2025-12-30
**ベース**: Founder Agent Origin + 企業内新規事業最適化

---

## 概要

Founder Agent ForRecruitは、リクルートグループなど大企業内での新規事業立ち上げに特化した版です。社内リソース活用、承認プロセス最適化、「Ring制度」のような社内起業制度に対応しています。

---

## 対象ユーザー

- 企業内起業家（イントレプレナー）
- リクルートRing制度参加者
- 大企業の新規事業開発部門
- 社内ベンチャー立ち上げ担当者

---

## Originとの主な違い

### 1. 緩和されたステージゲート基準

| 基準 | Origin | ForRecruit | 理由 |
|------|--------|-----------|------|
| **CPFスコア** | 60%以上 | **50%以上** | 社内検証・PoC前提のため緩和 |
| **10倍優位性** | 2軸以上 | **1軸以上** | 社内リソース活用で十分 |
| **インタビュー件数** | 20人 | **10人** | 社内ネットワーク活用で効率化 |

### 2. 追加フレームワーク

- **社内承認プロセス設計** - 役員承認、予算承認のステップ明確化
- **社内リソース棚卸し** - 既存顧客基盤、技術、ブランド活用
- **Ring制度準拠** - リクルート社内起業制度の基準対応
- **イントレプレナーFIF** - 社内でのキャリア、動機、実行力評価

### 3. 社内特化機能

- **社内調整計画** - ステークホルダーマップ、合意形成戦略
- **既存事業とのシナジー分析** - 既存顧客へのクロスセル機会評価
- **予算獲得プレゼン** - 社内向けピッチデッキ（VC版とは異なる）

---

## 特化機能

### 1. Ring制度対応

**Stage Gate対応**:
| リクルートRing | Founder Agent | 基準 |
|--------------|---------------|------|
| **Ring 1** | CPF検証 | スコア50%以上 |
| **Ring 2** | PSF検証 | MVP完成、社内PoC |
| **Ring 3** | PMF検証 | 外部顧客獲得、収益化開始 |

### 2. 社内リソース活用テンプレート

**活用可能リソース**:
- 既存顧客基盤（XX万社/人）
- 営業チャネル（既存営業網）
- ブランド力（認知度活用）
- 技術インフラ（システム、データ）
- 人的リソース（社内公募）

### 3. 承認プロセス最適化

**典型的な承認フロー**:
1. 課長承認（CPF検証結果）
2. 部長承認（PSF検証結果、予算要求）
3. 事業部長承認（PoC実施許可）
4. 役員承認（本格展開・事業化判断）

---

## ディレクトリ構造

```
Founder_Agent_ForRecruit/
├── documents/
│   ├── 1_initiating/
│   ├── 2_discovery/
│   ├── 3_planning/
│   ├── 4_executing/
│   ├── 5_monitoring/
│   └── internal_approval/   # 社内承認関連（追加）
│       ├── stakeholder_map.md
│       ├── approval_deck.md
│       └── resource_inventory.md
├── mvp/
├── system_prompts/
├── domain_config.yaml
└── README.md (このファイル)
```

---

## 使用方法

### ForRecruit特化スキル

```bash
# 社内承認プレゼン作成
/build-approval-deck

# 社内リソース棚卸し
/inventory-internal-resources

# ステークホルダー分析
/analyze-stakeholders

# Ring制度準拠チェック
/validate-ring-criteria
```

---

## 評価基準（Originよりも緩和・社内評価重視）

| 評価項目 | Origin基準 | ForRecruit基準 | 理由 |
|---------|-----------|---------------|------|
| 市場機会 | 6点以上 | **5点以上** | 社内シナジー評価も加味 |
| 課題の切実度 | 6点以上 | **4点以上** | 社内PoC前提 |
| 独自性・競争優位 | 3点以上 | **2点以上** | 社内リソース活用で補完 |

---

## 参考リソース（Originに追加）

### 企業内新規事業

- **Corporate_Product_Research** - 大企業の新規事業事例
- **Ring制度ガイドライン** - リクルート社内起業制度の詳細
- **イントレプレナー成功事例** - 社内起業家のケーススタディ

---

---

## 23スキル一覧

ForRecruit Editionは、Phase 1（Batch 1-3）で作成された18スキルとPhase 2（Batch 5-6）で作成された5スキルの合計23スキルを提供します。

### Batch 1（5スキル）- Discovery & Validation Foundation

| スキル | 説明 | 主要機能 |
|--------|------|---------|
| `/build-approval-deck` | Ring段階別承認デッキ生成 | 課長・部長・役員向けプレゼン資料作成 |
| `/inventory-internal-resources` | 社内リソース6カテゴリ棚卸し | 営業網、顧客基盤、ブランド、データ、プラットフォーム、インフラの活用度評価 |
| `/validate-ring-criteria` | Ring 1-3基準診断 | 各Ring段階の達成基準チェック |
| `/discover-demand` | 市場機会発見（ForRecruit版） | 既存顧客基盤活用、社内ニーズ分析 |
| `/research-problem` | 課題深堀り（ForRecruit版） | 社内インタビュー10人、顧客課題の定量化 |

### Batch 2（6スキル）- Stage Gate Validation

| スキル | 説明 | 主要機能 |
|--------|------|---------|
| `/validate-cpf` | CPFスコア50%基準（ForRecruit版） | 社内PoC前提の緩和基準、Ring 1対応 |
| `/validate-psf` | PSF検証（1軸10倍優位性） | MVP完成、社内PoC実施、Ring 2対応 |
| `/validate-pmf` | PMF検証（外部顧客獲得） | 外部顧客100社以上、Ring 3対応 |
| `/validate-10x` | 10倍優位性診断（1軸以上） | 社内リソース活用による競争優位性評価 |
| `/simulate-interview` | 社内ネットワーク活用インタビュー | 10人インタビューで効率的な仮説検証 |
| `/research-competitors` | 既存事業との差別化分析 | カニバリゼーション回避、シナジー評価 |

### Batch 3（7スキル）- Growth & Orchestration

| スキル | 説明 | 主要機能 |
|--------|------|---------|
| `/orchestrate-phase1-recruit` | **ForRecruit統合フロー** | 23スキルのオーケストレーション、Ring制度ステージゲート管理 |
| `/build-flywheel` | 社内エコシステム連携（ForRecruit版） | 既存製品とのクロスセル戦略、LTV 3-5倍向上 |
| `/create-mvv` | 企業価値観整合性チェック | リクルート6つの価値観との整合性評価 |
| `/analyze-aarrr` | 社内KPI最適化 | 社内外顧客統合評価、Ring 3基準準拠 |
| `/startup-scorecard` | Ring制度評価項目対応 | 総合80点満点評価（4視点40点 + 社内リソース20点 + シナジー20点） |
| `/build-lp` | 社内向けランディングページ | 社内実績活用、2段階CTA（社内ベータ + 外部顧客） |
| `/design-pricing` | 社内価格設定戦略 | 基本無料モデル検討、クロスセル戦略 |

### Phase 2 Batch 5（2スキル・P0）- Risk Management

| スキル | 優先度 | 説明 | 主要機能 |
|--------|--------|------|---------|
| `/validate-cannibalization` | P0 | カニバリゼーション評価 | 5次元評価（顧客40%、価値30%、チャネル20%、収益10%、社内政治）、Red/Orange/Yellow/Green判定、Ring承認への影響分析、失敗の26%を事前回避 |
| `/analyze-competitive-moat` | P0 | 競争優位性持続可能性分析 | Economic Moat 5次元評価（ネットワーク、スイッチング、ブランド、コスト、独自資産）、Moat Score 0-10点判定、Ring 2/3基準チェック（6.0/8.0）、Warren Buffett理論適用 |

### Phase 2 Batch 6（3スキル・P1-P2）- Strategic Decision Support

| スキル | 優先度 | 説明 | 主要機能 |
|--------|--------|------|---------|
| `/design-exit-strategy` | P1 | 撤退戦略設計 | 3層Alert早期警告（Yellow/Orange/Red）、撤退戦略6要素、早期撤退の定量的メリット（2年累損2億円 vs 6年15億円）、リソース再配分80%、次の成功率60% |
| `/build-synergy-map` | P1 | 4象限シナジーマップ作成 | カニバリゼーション vs シナジーの2軸評価、6カテゴリ60点満点評価、クロスセル効果定量化（Airペイ57%）、3種以上活用で成功率100%、ROI 8,500% |
| `/validate-market-timing` | P2 | 市場タイミング検証 | 5次元市場タイミング評価（技術成熟度、顧客準備度、競合状況、規制環境、市場成長率）、Too Early/Too Late判定、失敗の21%を事前回避 |

---

## オーケストレーション: `/orchestrate-phase1-recruit`

ForRecruit Edition の中核スキル。18スキルを5フェーズで段階的に実行し、Ring制度のステージゲートを管理します。

### 5フェーズフロー

```
PHASE 1: Discovery & Planning（5スキル）
├── /discover-demand          - 市場機会発見
├── /research-problem          - 課題深堀り
├── /simulate-interview        - 社内インタビュー
├── /inventory-internal-resources  - リソース棚卸し
└── /research-competitors      - 競合分析
         ↓
PHASE 2: CPF Validation（3スキル + Ring 1ゲート）
├── /validate-cpf              - CPF 50%以上
├── /build-approval-deck       - 課長承認デッキ
└── /validate-ring-criteria    - Ring 1基準チェック
         ↓ [Ring 1承認: 課長、予算50-100万円]
         ↓
PHASE 3: PSF Validation（4スキル + Ring 2ゲート）
├── /validate-psf              - PSF検証
├── /validate-10x              - 10倍優位性1軸以上
├── /create-mvv                - 企業価値観整合性
└── /build-flywheel            - エコシステム連携
         ↓ [Ring 2承認: 部長・事業部長、予算500-1,000万円]
         ↓
PHASE 4: PMF Validation（4スキル + Ring 3ゲート）
├── /validate-pmf              - 外部顧客100社以上
├── /analyze-aarrr             - AARRR指標評価
├── /startup-scorecard         - Ring制度評価80点満点
└── /build-lp                  - ランディングページ
         ↓ [Ring 3承認: 役員、予算5,000万円-3億円]
         ↓
PHASE 5: Launch Preparation（2スキル）
├── /design-pricing            - 価格戦略
└── /build-approval-deck       - 最終承認デッキ
```

### ステージゲート管理

各PhaseでRing基準を満たさない場合、自動的にリトライまたは代替手段を提案します。

---

## Ring制度スキルマッピング

| Ring段階 | 必須スキル | 達成基準 | 承認者 | 予算規模 |
|---------|----------|---------|--------|---------|
| **Ring 1** | `/validate-cpf`<br>`/validate-ring-criteria`<br>`/build-approval-deck` | CPF 50%以上<br>社内PoC計画<br>課長承認 | 課長 | 50-100万円 |
| **Ring 2** | `/validate-psf`<br>`/validate-10x`<br>`/inventory-internal-resources`<br>`/create-mvv` | 10倍優位性1軸以上<br>MVP完成<br>社内PoC実施<br>企業価値観整合性 | 部長・事業部長 | 500-1,000万円 |
| **Ring 3** | `/validate-pmf`<br>`/startup-scorecard`<br>`/analyze-aarrr`<br>`/build-lp` | 外部顧客100社以上<br>総合評価65点以上<br>3年黒字計画<br>LTV/CAC 10倍以上 | 役員 | 5,000万円-3億円 |

---

## 使用方法

### 基本的な使い方

```bash
# オーケストレーションで全フロー実行（推奨）
/orchestrate-phase1-recruit

# 個別スキル実行例
/validate-cpf
/build-approval-deck
/inventory-internal-resources
```

### 実行例: Ring 1達成まで

```bash
# Step 1: 市場機会発見と課題分析
/discover-demand
/research-problem

# Step 2: 社内リソース棚卸し
/inventory-internal-resources

# Step 3: CPF検証（50%基準）
/validate-cpf

# Step 4: 課長承認デッキ作成
/build-approval-deck

# Step 5: Ring 1基準チェック
/validate-ring-criteria
```

---

## 統合統計（Phase 1 + Phase 2累計）

| 項目 | 実績値 | 詳細 |
|------|--------|------|
| **総スキル数** | **23スキル** | Phase 1: 18 (Batch 1: 5, Batch 2: 6, Batch 3: 7) + Phase 2: 5 (Batch 5: 2, Batch 6: 3) |
| **統合事例数** | **286件** | Phase 1: 268, Phase 2: 18（進行中製品10件詳細化 + 外部ベンチマーク8件） |
| **平均品質スコア** | **97.3/100** | Phase 1: 93.2, Phase 2: 97.2, Final Quality Checkpoint: 97.3 |
| **実行時間** | **12時間** | 並列実行による効率化率57.1%（シーケンシャル想定28時間 → 並列12時間） |
| **データソース** | **700件** | Recruit_Product_Research (104件) + Startup_Research (596件) |

### 主要統合事例

**成功パターン**:
- **Airシリーズ**: エコシステム連携、クロスセル率57%、LTV 3-5倍、ROI 8,500%
- **Geppo**: 社内先行導入モデル、回答率96%、継続率98%、Moat Score 7.8（Moderate Moat）
- **Airレジ**: 基本無料モデル、90.4万店舗獲得、Moat Score 8.6（Deep Moat）、市場タイミング適切（2013年タブレットPOS黎明期）
- **SUUMO**: 不動産エコシステム、ブランド統合、Moat Score 8.2（Deep Moat）

**失敗パターン**:
- **スタディサプリ個別指導**: カニバリゼーション失敗事例（価格差5倍、カニバリ重複率80%）
- **エリクラ**: 社内依存からの脱却失敗、市場タイミング誤り（Too Early、2014年ギグエコノミー未成熟）、累損10億円
- **CAREER CARVER**: カニバリゼーション（既存リクルートエージェントと重複80%）、市場タイミング誤り（Too Late、2012年後発参入）、累損18億円
- **CODE.SCORE**: 競争優位性持続性不足（Moat Score 3.2、No Moat）、撤退判断遅延（6年継続）、累損15億円

---

## トラブルシューティング

### よくあるエラーと対処法

#### Q1: CPFスコアが50%に届かない

**症状**: `/validate-cpf` 実行時、スコア40%前後で不合格

**原因**:
- User Research回数不足（15回未満）
- 課題共通率が低い（60%未満）
- 支払い意思が不明確

**対処法**:
1. User Researchを追加実施（最低15回、推奨20回以上）
2. インタビュー対象を絞り込み（課題を持つセグメントに集中）
3. 具体的な支払い意思確認（「いくらなら払うか」を明確に質問）

**参考**: Ring 1成功パターンTop 5の平均CPFスコア73.6%を目指す

**成功事例**: Airペイ（CPF 70%、User Research 100回、課題共通率85%）

---

#### Q2: 社内リソース活用ROIが1000%に届かない

**症状**: `/inventory-internal-resources` 実行時、ROI 500%程度

**原因**:
- リソース活用カテゴリが1種類のみ
- 定量化が不十分（コスト削減額を過小評価）

**対処法**:
1. 複数カテゴリの組み合わせを検討（例: 顧客基盤 + 営業チャネル）
2. コスト削減額を詳細に試算（人件費、開発費、マーケティング費等）
3. クロスセル効果を定量化（既存顧客への転用率 × 顧客数）

**参考**: Airレジ ROI 11,450%（決済基盤 + 顧客基盤 + 営業網の3種類活用）

**成功事例**: Airペイ（ROI 11,450%、リクルート資産20点満点、営業網2,000名活用）

---

#### Q3: Ring 1承認が通らない

**症状**: `/build-approval-deck` で作成したデッキで課長承認が得られない

**原因**:
- CPFスコアが不十分（50%ギリギリ）
- 社内リソース活用が不明確
- 次のステップが曖昧

**対処法**:
1. CPFスコアを60%以上に引き上げ（安全マージン）
2. 社内リソース活用の具体的プランを明記（どの部署のどのリソースをいつ使うか）
3. Ring 1検証計画を詳細化（3-6ヶ月の具体的スケジュール、予算内訳）

**参考**: Ring 1成功パターン平均達成期間4.2ヶ月、予算50-100万円

**成功事例**: Airレジ（Ring 1達成2-3ヶ月、CPF 65%、予算80万円）

---

#### Q4: 10倍優位性が見つからない

**症状**: `/validate-10x` 実行時、8軸すべて5倍未満

**原因**:
- 競合との差別化が不十分
- 社内リソース活用の優位性を見落としている

**対処法**:
1. 社内リソース軸を重点評価（既存事業の顧客基盤、営業網、ブランド力）
2. 既存事業とのシナジーを定量化（クロスセル率、コスト削減額）
3. 10倍優位性の定義を再確認（「10倍速い」「10倍安い」「10倍便利」等）

**参考**: Airレジ 4軸10倍優位性（コスト100倍削減、導入時間7倍短縮、営業網5倍活用、エコシステム3倍統合）

**成功事例**: Airペイ（4軸優位性: 初期費用100倍、対応ブランド16倍、手数料6倍削減、データ資産活用）

---

#### Q5: PMFスコアが7.0に届かない

**症状**: `/validate-pmf` 実行時、スコア6.5前後で不合格

**原因**:
- 外部顧客獲得数が不足（100社未満）
- NPS（Net Promoter Score）が低い（50未満）
- LTV/CAC比が10.0未満

**対処法**:
1. 外部顧客獲得を加速（社内PoC完了後、積極的な営業展開）
2. 顧客満足度向上施策（NPS 50以上を目指す）
3. CAC削減施策（社内営業網活用、クロスセル強化）

**参考**: Ring 3成功パターン平均PMFスコア8.7、外部顧客1,340社、LTV/CAC 21.6倍

**成功事例**: Geppo（外部顧客2年300社、NPS 60-70、継続率98%、LTV/CAC 20倍）

---

#### Q6: オーケストレーション実行中にエラー

**症状**: `/orchestrate-phase1-recruit` 実行中、特定スキルでエラー停止

**原因**:
- 前提条件未達成（例: CPF検証前にPSF検証を実行）
- 必須データ欠損

**対処法**:
1. エラーメッセージを確認し、どのスキルで停止したか特定
2. 該当スキルの前提条件を確認（Ring 1-3のステージゲート）
3. 個別スキルを手動実行し、エラー原因を特定

**参考**: オーケストレーションは5フェーズ順次実行（Discovery → CPF → PSF → PMF → Launch）

**典型的なエラー**:
- Phase 2でCPF 50%未満: Ring 1承認不可 → Discovery（Phase 1）に戻り再検証
- Phase 3で10倍優位性0軸: Ring 2承認不可 → PSF再設計
- Phase 4で外部顧客50社未満: Ring 3承認不可 → 営業戦略見直し

---

#### Q7: 社内承認プロセスで関係部署の合意が得られない

**症状**: ステークホルダー調整が難航、Ring 2-3承認が遅延

**原因**:
- ステークホルダーマップ不足
- 既存事業とのカニバリゼーション懸念
- 予算配分の不透明性

**対処法**:
1. `/inventory-internal-resources` でステークホルダーマップ詳細化
2. 既存事業とのシナジー明確化（カニバリゼーションではなく補完関係）
3. 予算配分の透明化（各部署への貢献度を定量化）

**参考**: Airシリーズは既存営業網2,000名を活用し、営業部門とのWin-Win関係構築

**成功事例**: Airペイ（ホットペッパーグルメ営業網転用、営業部門へのインセンティブ設計）

---

#### Q8: 既存事業とのカニバリゼーション問題

**症状**: 新規事業が既存事業の顧客を奪う懸念で承認が通らない

**原因**:
- 既存事業とのターゲット重複
- 差別化が不明確

**対処法**:
1. ターゲットセグメントの明確な分離（既存顧客と新規顧客の定義）
2. 価格差に見合う価値提供（既存製品を補完する高付加価値機能）
3. クロスセル戦略の提示（既存顧客へのアップセル機会）

**参考**: スタディサプリ個別指導失敗事例（ベーシック2,178円 vs 個別指導10,780円、5倍差に見合う価値提供できず）

**成功事例**: Airシリーズ（Airレジ → Airペイ → Airキャッシュのクロスセル率57%、カニバリではなく拡張）

---

### 問い合わせ先

上記で解決しない場合は、以下を確認してください:
- 詳細ドキュメント: `@.claude/skills/_shared/knowledge_base.md`
- 事例カタログ: `@.claude/skills/_shared/case_reference_for_recruit.md`
- フレームワーク詳細: `@.claude/skills/_shared/recruit_specific_frameworks.md`

---

## 共通ナレッジベース

ForRecruit Editionの全スキルは以下の共通ナレッジベースを参照します：

| ドキュメント | パス | 内容 |
|------------|------|------|
| **ナレッジベース（拡張版）** | `@.claude/skills/_shared/knowledge_base.md` | ForRecruit特化の評価基準、Ring制度フレームワーク |
| **事例カタログ** | `@.claude/skills/_shared/case_reference_for_recruit.md` | 86件の成功・失敗事例、スキル別推奨事例 |
| **Ring制度フレームワーク** | `@.claude/skills/_shared/recruit_specific_frameworks.md` | Ring 1-3達成基準、社内承認プロセス、リソース活用評価 |

### 参照例

各スキル内で以下のように参照されています：

```markdown
## Domain-Specific Knowledge (from Recruit_Product_Research)

### Success Patterns
- Airレジ: 基本無料モデル、90.4万店舗獲得
- Geppo: 社内1,200名先行導入、回答率96%

### Common Pitfalls
- スタディサプリ個別指導: 自社製品カニバリゼーション
- エリクラ: 社内依存からの脱却失敗

### Quantitative Benchmarks
- クロスセル率: 57%（業界標準5-15%の4-11倍）
- LTV向上: 3-5倍
- Churn率: 1/2〜1/3

### Reference
- 詳細: @Recruit_Product_Research/documents/SUCCESS/CORP_S009_airレジ.md
```

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2026-01-02 | 1.2 | **Phase 2完成**: 23スキル一覧追加（Phase 2: 5スキル）、統合統計更新（286事例、品質スコア97.3/100）、Phase 2スキル詳細追加（カニバリゼーション、競争優位性、撤退戦略、シナジーマップ、市場タイミング）、ForRecruit Edition完成宣言 |
| 2026-01-02 | 1.1 | 18スキル一覧追加、オーケストレーション説明追加、Ring制度スキルマッピング追加、統合統計追加、共通ナレッジベース参照追加 |
| 2025-12-30 | 1.0 | 初版作成（ForRecruit特化版） |
