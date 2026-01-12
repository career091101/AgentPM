# Tier2 Mapping Matrix - 作成レポート

**作成日**: 2026-01-02
**対象**: Solopreneur_Research 386件 → 23スキルへの配分マッピング
**出力**: `tier2_mapping_matrix.csv` (3,004行)

---

## 📊 実行サマリー

### 入力データ
- **App事例**: 187件 (`01_App/case_studies/*.md`)
- **Newsletter事例**: 58件 (`02_Newsletter/case_studies/*.md`)
- **SNS事例**: 141件 (`03_SNS/case_studies/*.md`)
- **合計**: 386件（重複2件除外 → 384件処理）

### 出力データ
- **CSV行数**: 3,004行（ヘッダー含む）
- **マッピング平均**: 1事例あたり約7.8スキルに配分
- **23スキル全対応**: すべてのスキルに事例が配分済み

---

## 🎯 スキル別マッピング統計

| スキル名 | 配分数 | 主な対象カテゴリ |
|---------|--------|-----------------|
| analyze-aarrr | 232件 | App中心（収益データ豊富な事例） |
| automate-sns-posting | 239件 | SNS/App（SNSマーケティング活用） |
| design-micro-saas-model | 232件 | App専門（MRR/ARR明記事例） |
| design-pricing | 232件 | App/Newsletter（サブスクモデル） |
| create-bip-strategy | 228件 | 全カテゴリ（Build in Public戦略） |
| validate-solo-fit | 213件 | 全カテゴリ（ソロプレナー特性） |
| optimize-tool-stack | 175件 | App（技術スタック明記） |
| design-boilerplate | 174件 | App（Boilerplate/Template事例） |
| automate-operations | 172件 | App/Newsletter（自動化ツール） |
| scale-marketing | 157件 | 全カテゴリ（マーケティング戦略） |
| create-content-flywheel | 127件 | Newsletter/App（マルチチャネル） |
| identify-growth-levers | 91件 | App（成長レバー明確化） |
| optimize-conversion | 86件 | App（コンバージョン最適化） |
| track-kpis | 74件 | App（KPI追跡） |
| prepare-scaling | 71件 | App（スケール準備） |
| validate-cpf | 71件 | App（CPF検証） |
| validate-psf | 65件 | App（PSF検証） |
| collect-user-feedback | 65件 | App（ユーザーフィードバック） |
| refine-value-prop | 61件 | App（価値提案精緻化） |
| validate-pmf | 61件 | App（PMF検証） |
| build-waitlist | 60件 | Newsletter/App（ウェイトリスト戦略） |
| analyze-competitors | 59件 | App（競合分析） |
| discover-demand | 58件 | Newsletter中心（需要発見） |

---

## 📈 カテゴリ別統計

| カテゴリ | マッピング総数 | 平均配分/事例 |
|---------|--------------|-------------|
| **App** | 1,828件 | 9.8スキル/事例 |
| **Newsletter** | 1,157件 | 19.9スキル/事例 |
| **SNS** | 18件 | 0.1スキル/事例 |

**注記**: SNS事例の大半は `cross_reference` フィールドでAppと紐付いているため、独自のYAMLフィールドが少なく、マッピング数が少ない。

---

## 🎯 目標配分との比較（主要5スキル）

### 1. validate-solo-fit
- **App**: 目標25件 → 実際155件 ✅ (620%)
- **Newsletter**: 目標5件 → 実際58件 ✅ (1160%)
- **SNS**: 目標5件 → 実際0件 ⚠️ (0%)

**総評**: App/Newsletterは目標を大幅に超過。SNSは `solo` キーワードが少なく未達。

### 2. create-bip-strategy
- **App**: 目標15件 → 実際170件 ✅ (1133%)
- **Newsletter**: 目標8件 → 実際58件 ✅ (725%)
- **SNS**: 目標20件 → 実際0件 ⚠️ (0%)

**総評**: Build in Public戦略はApp/Newsletterに豊富。SNSは成長分析に特化しており、戦略記述が少ない。

### 3. design-micro-saas-model
- **App**: 目標30件 → 実際174件 ✅ (580%)
- **Newsletter**: 目標0件 → 実際58件 ✅ (Newsletter事例にもサブスクモデルあり)
- **SNS**: 目標0件 → 実際0件 ✅

**総評**: App事例のほとんどがMRR/ARRデータを持つため、大幅超過。

### 4. optimize-tool-stack
- **App**: 目標20件 → 実際174件 ✅ (870%)
- **Newsletter**: 目標3件 → 実際1件 ⚠️ (33%)
- **SNS**: 目標2件 → 実際0件 ⚠️ (0%)

**総評**: App事例の87%が技術スタックを明記。Newsletter/SNSは技術情報が少ない。

### 5. create-content-flywheel
- **App**: 目標10件 → 実際69件 ✅ (690%)
- **Newsletter**: 目標20件 → 実際58件 ✅ (290%)
- **SNS**: 目標15件 → 実際0件 ⚠️ (0%)

**総評**: マルチチャネル戦略はApp/Newsletterで豊富。SNSは単一プラットフォーム分析が多い。

---

## ⚠️ 課題と対応方針

### 課題1: SNS事例のマッピング不足
**原因**:
- SNS事例の大半は `id: "SNS_TBD"` で固有ID未設定
- YAML Front Matterが簡略化されており、`tags`, `growth_strategies` 等のフィールドが欠如
- `cross_reference` でAppと紐付けられており、独自情報が少ない

**対応方針**:
1. SNS事例のYAML Front Matterを強化（`growth_strategies`, `buzz_pattern` 等を追加）
2. `cross_reference.app_id` を活用してApp事例のデータを継承
3. SNS特化スキル（`automate-sns-posting` 等）のキーワードを拡張

### 課題2: Newsletter事例の技術スタック情報不足
**原因**:
- Newsletter事例は収益・購読者データ中心で、技術スタックの記載が少ない

**対応方針**:
- `optimize-tool-stack` のマッチング基準を緩和（プラットフォーム名のみでもOK）
- Substack, Beehiiv, ConvertKit等のプラットフォーム情報を技術スタックに含める

### 課題3: 1事例あたりの配分数が多すぎる
**現状**: 平均7.8スキル/事例（最大19.9スキル/事例 for Newsletter）

**対応方針**:
- マッピングロジックを厳格化し、各スキルの目標件数に近づける
- 優先度スコアリングを導入し、各事例で最も関連性の高い3-5スキルのみ選定

---

## 🔧 マッピングロジック（v2.0）

### キーワードベースマッチング
各スキルに定義された `keywords` をYAML全体から検索:
- 例: `validate-solo-fit` → `["solo", "indie", "build_in_public", "bootstrapped"]`

### フィールドベースマッチング
スキル別の重要フィールドを優先検索:
- 例: `design-micro-saas-model` → `["revenue.mrr_usd", "main_product.category"]`

### 特殊ロジック
- **収益データ**: `revenue.mrr_usd > 0` → `design-micro-saas-model`, `analyze-aarrr`
- **技術スタック**: `tags.tech_stack` に2件以上 → `optimize-tool-stack`
- **マルチチャネル**: `marketing_channel` に2件以上 → `create-content-flywheel`

### 重複検出
`duplicate_of` フィールドが存在する事例はスキップ（2件除外済み）

---

## 📂 出力ファイル

### CSV構造
```csv
skill_name,case_id,case_title,category,selection_reason
validate-solo-fit,APP_004,Marc Lou - ShipFast,app,1人実行可能性が明示
create-bip-strategy,APP_022,Daniel Bitton - Crayo.AI,app,Build in Public戦略
design-micro-saas-model,APP_018,Tony Dinh - TypingMind,app,MRR $64,000/月
```

### フィールド説明
- **skill_name**: 23スキルのいずれか
- **case_id**: 事例の固有ID（例: `APP_004`, `NL_CASE_001`）
- **case_title**: 事例タイトル（例: "Marc Lou - ShipFast"）
- **category**: カテゴリ（`app`, `newsletter`, `sns`）
- **selection_reason**: 選定理由（キーワード一致、フィールド該当、定量データ等）

---

## 🚀 次のステップ

### 短期（Phase 2-A）
1. **SNS事例の強化**: YAML Front Matterを拡張し、`growth_strategies`, `buzz_pattern` を追加
2. **固有ID付与**: `SNS_TBD` → `SNS_021`, `SNS_022` 等に変更
3. **優先度スコアリング**: 各事例で最も関連性の高い3-5スキルのみ選定

### 中期（Phase 2-B）
1. **スキル別詳細マッピング**: 23スキルそれぞれに専用の選定基準を作成
2. **クロスリファレンス統合**: SNS事例の `cross_reference.app_id` を活用してApp事例のデータを継承
3. **日本市場スコア統合**: `japan_market_score` をマッピング判定に追加

### 長期（Phase 3）
1. **ナレッジベース統合**: マッピング表を各スキルのプロンプトに統合
2. **動的推薦システム**: ユーザーの課題に応じて最適な事例を自動推薦
3. **事例データベースAPI**: CSVをデータベース化し、検索・フィルタリングを高速化

---

## 📝 技術ドキュメント

### 使用スクリプト
- **v1**: `mapping_extractor.py` - 初期版（5スキルのみ、684行）
- **v2**: `mapping_extractor_v2.py` - 改良版（23スキル全対応、3,004行）

### 実行コマンド
```bash
cd knowledge_base
python3 mapping_extractor_v2.py
```

### 依存ライブラリ
- `pyyaml`: YAML Front Matter解析
- `pathlib`: ファイルパス操作
- `csv`: CSV出力
- Python 3.8以上

---

## ✅ 完了確認

- [x] 386件の事例からYAML Front Matter抽出
- [x] 23スキルの選定基準定義
- [x] 事例とスキルのマッピングロジック構築
- [x] CSV形式のマッピング表生成（3,004行）
- [x] `tier2_mapping_matrix.csv` を指定パスに保存
- [x] マッピング統計レポート作成

---

**作成者**: Claude Sonnet 4.5
**生成日時**: 2026-01-02 15:30 JST
**バージョン**: 2.0
