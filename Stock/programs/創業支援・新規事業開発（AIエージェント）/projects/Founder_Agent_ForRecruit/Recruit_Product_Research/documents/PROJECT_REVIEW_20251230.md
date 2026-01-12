# Corporate_Product_Research プロジェクト見直しレポート

**作成日**: 2025-12-30
**作成者**: Claude (プロジェクト見直し)
**目的**: 既存調査成果物の全体把握と真に不足している要素の特定

---

## エグゼクティブサマリー

### 重大な認識ミス

**誤認**: 68製品の調査ノートがすべて低品質で、ゼロから再調査が必要
**実態**: **2層構造**が存在し、25製品は既に高品質調査完了、68製品は基本調査のみ

### プロジェクト構造の全体像

```
Corporate_Product_Research/
├── documents/
│   ├── SUCCESS/              # 高品質調査（15製品）★完成★
│   │   ├── TIER1_GLOBAL_MA/  (10製品: Indeed, Glassdoor等)
│   │   ├── TIER2_MEGA_HIT/   (SUUMO, ゼクシィ等)
│   │   ├── TIER3_SAAS/       (21製品)
│   │   ├── TIER4_DOMESTIC_MA/
│   │   └── TIER5_NEW_BUSINESS/ (29製品)
│   └── FAILURE/              # 高品質調査（10製品）★完成★
│       ├── TIER6_CLEAR_WITHDRAWAL/ (17製品: ぽんぱれモール、R25等)
│       ├── TIER7_MA_FAILURE/
│       ├── TIER7_STRATEGIC_RESTRUCTURE/
│       └── TIER8_STRATEGIC_EXIT/ (2製品)
├── analysis/
│   ├── research_notes_68/    # 基本調査（68製品）★要改善★
│   ├── cpf_patterns/         # CPFパターン分析（6パターン）★完成★
│   ├── psf_patterns/         # PSFパターン分析（6パターン）★完成★
│   ├── quality_reports/      # 品質レポート（7レポート）★完成★
│   └── withdrawal_analysis/  # 撤退分析★完成★
└── _templates/               # テンプレート（新規作成）
    ├── corporate_product_research_v3_template.md ★今回作成★
    ├── corporate_research_guidelines.md ★今回作成★
    └── quality_scoring_criteria.md ★今回作成★
```

---

## 詳細分析

### 1. 高品質調査（25製品）- ★完成済み★

#### 基本情報
- **ファイル数**: 25件（SUCCESS 15件、FAILURE 10件）
- **平均行数**: 500-600行
- **平均ソース数**: 17.1件（目標10件を大幅に超過）
- **品質評価**: EXCELLENT（総合判定）

#### 品質指標
| 指標 | 目標 | 実績 | 判定 |
|------|------|------|:----:|
| データ整合性 | 100% | 100% | ✅ |
| テンプレート準拠度 | 90%以上 | 99.1% | ✅ |
| PASS基準達成率（SUCCESS） | 100% | 100% | ✅ |
| 平均ソース数 | 10以上 | 17.1 | ✅ |
| ファクトチェックPASS率 | 90%以上 | 100% | ✅ |

#### YAMLフロントマター構造
```yaml
---
id: "CORP_SXXX"
title: "製品名 - 企業名"
category: "corporate_product"
tier: "mega_hit" | "global_ma" | "saas" | "clear_withdrawal" | ...
type: "success" | "failure"
version: "1.0"
tags: []

# 基本情報
product:
  name: ""
  parent_company: "Recruit Holdings"
  launched_year: null
  revenue: ""
  users: null

# orchestrate-phase1対応フィールド
validation_data:
  cpf:
    interview_count: null
    problem_commonality: 85
    wtp_confirmed: true
    urgency_score: 8
  psf:
    ten_x_axes:
      - axis: "情報の一覧性"
        multiplier: 10
  pivot:
    occurred: true
    pivot_count: 1

# リクルート製品特有フィールド
recruit_specific:
  leveraged_assets: []
  synergy_with_existing: []

quality:
  fact_check: "pass"
  sources_count: 20
---
```

#### コンテンツセクション構造（10-11セクション）
1. 基本情報
2. 製品開発ストーリー
   - 2.1 課題発見
   - 2.2 CPF検証（orchestrate-phase1基準）
   - 2.3 PSF検証（10倍優位性）
3. ピボット/失敗経験
4. 成長戦略
   - 4.1 初期トラクション
   - 4.2 フライホイール
   - 4.3 スケール戦略
   - 4.4 リクルート資産の活用
5. M&A戦略（該当時）
6. 使用ツール・サービス
7. 成功/失敗要因分析
8. orchestrate-phase1への示唆
9. 他業界適用性
10. ファクトチェック結果
11. 参照ソース

#### 完成済み製品例
**SUCCESS（15製品）**:
- TIER1_GLOBAL_MA: Indeed, Glassdoor, Indeed Prime等（10製品）
- TIER2_MEGA_HIT: SUUMO, ゼクシィ, ホットペッパーグルメ等
- TIER3_SAAS: スタディサプリ, Airレジ等
- TIER5_NEW_BUSINESS: じゃらん, リクナビ等

**FAILURE（10製品）**:
- TIER6_CLEAR_WITHDRAWAL: ぽんぱれモール, R25, ATND, ナースフル等
- TIER8_STRATEGIC_EXIT: ISIZE等

---

### 2. 基本調査（68製品）- ★要改善★

#### 基本情報
- **ファイル数**: 68件（official 48件、withdrawn 20件）
- **平均行数**: 70行（目標500行の14%）
- **平均ソース数**: 10.52件（official）、4.60件（withdrawn）
- **品質評価**: 基本情報のみ、多数の「不明」項目

#### Research Note v2形式（10セクション）
```markdown
# Research Note v2: 製品名

- 区分: `official` or `withdrawn`
- コード: `air/s03`
- sources_count: `10`

## 1. 基本情報（テンプレの表形式＋ソース列）
## 2. 主要事実テーブル（事実→根拠URL×2）
## 3. 提供価値/対象（一次情報の引用中心）
## 4. 料金/プラン（一次情報）
## 5. 規約/プライバシー（一次情報）
## 6. FAQ/サポート（一次情報）
## 7. 事例/導入実績（一次情報 or 信頼できる第三者）
## 8. 競合（第三者ソース）
## 9. 時系列（開始/終了/重要発表）
## 10. 未解決点（不明を明示して次工程へ渡す）
## 参照ソース
```

#### 問題点
1. **YAMLメタデータなし**: orchestrate-phase1対応フィールドなし
2. **多数の「不明」項目**: 対象ユーザー、競合、時系列等が不明
3. **CPF/PSF検証なし**: 検証データが記載されていない
4. **10倍優位性分析なし**: 競合優位性の定量化なし
5. **リクルート資産分析なし**: 既存資産活用の分析なし
6. **Unit Economicsなし**: LTV/CAC、チャーンレート等の記載なし
7. **ファクトチェック表なし**: データの信頼性検証なし

#### 対象製品（68件）
**Official（48件）**:
- Airシリーズ: Airレジ、Airペイ、Airリザーブ等（17件）
- Beauty: サロンボード、ホットペッパービューティー等（3件）
- Gourmet: ホットペッパーグルメ、レストランボード等（3件）
- Housing: SUUMO関連サービス（6件）
- Marriage: ゼクシィ関連サービス（3件）
- Study: スタディサプリ関連（4件）
- Travel: じゃらん関連（3件）
- Work: リクルートエージェント（1件）
- Car: カーセンサー（1件）
- RD（その他）: タブルーム、リクルートカード等（7件）

**Withdrawn（20件）**:
- CODE.SCORE、HELPMAN JAPAN、SUUMOリフォームストア、termhub等
- じゃらんナビ札幌、エイビーロード、チラシ部!、ポイコポイント等
- リクナビDMPフォロー、リクナビHRTech勤怠/評価管理等
- スタディサプリ個別指導塾等

---

### 3. 分析成果物（★完成済み★）

#### CPFパターン分析（6パターン）
1. P1_アナログ業務の非効率性.md
2. P2_情報の非対称性解消.md
3. P3_地域経済格差の解消.md
4. P4_マッチング効率の革命.md
5. P5_時間場所の制約解放.md
6. P6_意思決定支援の不足.md

#### PSFパターン分析（6パターン）
1. PSF1_コスト破壊型.md
2. PSF2_時間革命型.md
3. PSF3_アクセス革命型.md
4. PSF4_情報革命型.md
5. PSF5_更新速度革命型.md
6. PSF6_マッチング精度革命型.md

#### 品質レポート（7レポート）
1. quality_report_20250129.md（総合レポート）
2. phase1_data_integrity_report.md
3. phase2_frontmatter_failure.md
4. phase2_sections_failure.md
5. phase2_sections_success.md
6. phase3_pass_criteria_failure.md
7. phase3_pass_criteria_success.md

#### その他分析
- withdrawal_analysis/recruit_withdrawal_criteria.md（撤退基準分析）
- research_audit_68.md（68製品監査レポート）

---

## 品質ギャップ分析

### 高品質調査（25製品）vs 基本調査（68製品）

| 項目 | 高品質調査（25製品） | 基本調査（68製品） | ギャップ |
|------|---------------------|-------------------|---------|
| **平均行数** | 500-600行 | 70行 | **7-8倍** |
| **YAMLメタデータ** | orchestrate-phase1対応 | なし | **完全欠落** |
| **セクション数** | 10-11セクション | 10セクション | 同等 |
| **ソース数** | 平均17.1件 | 10.52件（official） | 1.6倍 |
| **CPF検証** | 詳細分析あり | なし | **完全欠落** |
| **PSF検証** | 10倍優位性分析あり | なし | **完全欠落** |
| **リクルート資産** | 活用分析あり | なし | **完全欠落** |
| **Unit Economics** | LTV/CAC等あり | なし | **完全欠落** |
| **ファクトチェック** | PASS率100% | なし | **完全欠落** |
| **「不明」項目** | ほぼなし | 多数 | **大量** |

---

## 私が作成した成果物の評価

### Phase 0: 準備（5エージェント）

| Agent | 成果物 | 評価 | 既存との関係 |
|-------|--------|------|------------|
| Agent 1 | Template v3 (834行) | ⚠️ 重複 | 既存テンプレートと類似、PSF→PMF用語変更 |
| Agent 2 | Research Guidelines (1,147行) | ✅ 有用 | 既存になし、90分調査プロセスは新規 |
| Agent 3 | Quality Scoring (900行) | ✅ 有用 | 既存になし、100点満点基準は新規 |
| Agent 4 | Product Prioritization (700行) | ❌ 不要 | 68製品は既に存在、優先順位付け不要 |
| Agent 5 | Implementation Plan (960行) | ❌ 要修正 | ゼロからの再調査計画で重複作業 |

### Phase 1: パイロット（3エージェント）

| Agent | 成果物 | 評価 | 問題点 |
|-------|--------|------|--------|
| Agent 6 | Airペイ v3 (88点) | ⚠️ 重複 | research_notes_68/official_Airペイ.mdと重複 |
| Agent 7 | CODE.SCORE v3 (87点) | ⚠️ 重複 | research_notes_68/withdrawn_CODE.SCORE.mdと重複 |
| Agent 8 | Geppo v3 (90点) | ⚠️ 重複 | research_notes_68/official_Geppo.mdと重複 |

**判定**: 高品質だが、既存68製品の基本調査と重複している

---

## 真に不足している要素

### 1. 68製品の品質向上（★最優先★）

**現状**: 70行の基本調査（Research Note v2）
**目標**: 500行の高品質調査（documents/SUCCESS, FAILUREレベル）

**不足要素**:
1. YAMLフロントマター（orchestrate-phase1対応フィールド）
2. CPF検証データ（interview_count、problem_commonality、wtp_confirmed）
3. PSF検証データ（10倍優位性、MVP、UVP）
4. リクルート資産活用分析
5. Unit Economics分析（LTV/CAC、チャーンレート等）
6. 成功/失敗要因の深掘り
7. orchestrate-phase1への示唆
8. ファクトチェック表

### 2. 品質スコアリングシステム（★新規★）

**現状**: 既存25製品には品質スコアなし
**提案**: 100点満点の客観的品質評価システム（Agent 3作成済み）

**適用対象**:
- 既存25製品に品質スコアを付与
- 68製品の改善後に品質スコアを付与
- 合計93製品の品質ランク付け（Tier S/A/B/C/D）

### 3. Tier分類の整理（★混乱解消★）

**現状の問題**:
- 既存TIER1-8（成功度分類）
- 私の提案Tier 1-3（優先度分類）
- 混乱を招く命名

**解決策**:
- 既存のTIER1-8を維持（SUCCESS/FAILUREの分類軸）
- 優先度分類は削除、またはPriorityという別名に変更

### 4. テンプレートの統一（★要調整★）

**現状**:
- 既存テンプレート: orchestrate-phase1対応、PSF重視
- v3テンプレート: 55フィールド、PMF重視

**解決策**:
- 既存テンプレートをベースに、v3の有用要素を統合
- PSF/PMF用語の統一
- 68製品改善に使用するテンプレートを確定

---

## 新しい実装計画の提案

### オプションA: 68製品の段階的品質向上

**アプローチ**: 既存68製品を25製品レベルに引き上げる

**Phase 0**: 準備（完了済み）
- ✅ Template v3作成
- ✅ Research Guidelines作成
- ✅ Quality Scoring作成

**Phase 1**: パイロット（3製品）
- 既存research_notes_68から3製品を選定
- v3テンプレートを適用して高品質化
- 500行、85点以上を達成

**Phase 2-5**: バッチ処理（65製品）
- 5エージェント並列で段階的に処理
- 各製品を70行→500行に拡充
- orchestrate-phase1対応フィールドを追加

### オプションB: 既存25製品の拡充 + 68製品の選別改善

**アプローチ**: 既存25製品に品質スコア付与、68製品から優先度高いもののみ改善

**Phase 1**: 既存25製品の品質スコアリング
- 100点満点で評価
- Tier S/A/B分類

**Phase 2**: 68製品から優先度高い15-20製品を選定
- データ可用性、戦略的重要性で選定
- 高品質調査に引き上げ

**Phase 3**: 残り製品は基本調査として維持
- 70行レベルでも価値がある製品は維持

### オプションC: 既存成果物の活用と補完

**アプローチ**: 重複作業を避け、既存成果物を最大活用

**Phase 1**: 重複排除
- Phase 1で作成したAirペイ、CODE.SCORE、Geppoの価値ある部分のみ抽出
- 既存research_notes_68に統合

**Phase 2**: テンプレート統一
- 既存テンプレート + v3の良い要素を統合
- 68製品改善用の統一テンプレート確定

**Phase 3**: 68製品の段階的改善
- 優先度A（20製品）: 完全高品質化
- 優先度B（30製品）: 中程度改善
- 優先度C（18製品）: 基本調査維持

---

## 推奨アクション

### 即時アクション
1. ユーザーに3つのオプション（A/B/C）を提示
2. 選択されたオプションに基づき実装計画を確定
3. 重複ファイル（Phase 1作成分）の扱いを決定

### 重要な確認事項
1. 68製品すべてを高品質化する必要があるか？
2. 既存25製品との統合方針（別ディレクトリ維持 or 統合）
3. Tier分類の整理方針（TIER1-8維持 or 変更）
4. テンプレート統一の方針（既存ベース or v3ベース or 統合）

---

## 結論

**認識の修正**:
- 68製品はゼロからの調査ではなく、基本調査（70行）の品質向上が真のミッション
- 既存25製品は極めて高品質で、ベンチマークとして活用可能
- Phase 0-1で作成した成果物は一部有用だが、重複部分も多い

**次のステップ**:
ユーザーにオプションA/B/Cを提示し、選択に基づき新しい実装計画を策定する。
