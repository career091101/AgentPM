# validate-pmf Failure Integration Report

**作成日**: 2026-01-03
**タスク**: Tier 3B PMF失敗事例の統合
**対象スキル**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_startup/validate-pmf/SKILL.md`
**実行エージェント**: Founder Agent ForStartup Edition - Failure Case Integration Agent

---

## 実行サマリー

### 統合した失敗事例
1. **Theranos**（P16+P23+P28 - 詐欺・規制失敗）
2. **CODE.SCORE**（PMF未達 - リクルート撤退事例）

### 追加セクション
- **Tier 3B: PMF失敗事例（ForStartup特化）**（約220行追加）
  - 失敗事例1: Theranos（詐欺・規制失敗）
  - 失敗事例2: CODE.SCORE（PMF未達・リクルート撤退）
  - Tier 3B 失敗事例のPMF診断への活用方法
  - validate-pmf実行時のチェックリスト（失敗回避）
  - 撤退判断の明確化（ForStartup基準）
  - Reference（Tier 3B失敗事例）

---

## 統合内容詳細

### 失敗事例1: Theranos（P16+P23+P28 - 詐欺・規制失敗）

#### 事例概要
- **企業名**: Theranos（Elizabeth Holmes創業、2003年設立）
- **事業内容**: 血液検査デバイス"Edison"（指先採血で200以上の検査項目）
- **失敗の経緯**: 技術不在のまま$700M+調達 → 2015年暴露 → 2018年解散 → 2022年Holmes有罪判決（禁固11年3ヶ月）
- **結果**: 評価額$9B → 清算価値$0、投資家損失$700M+

#### PMF失敗の詳細
1. **技術が存在しなかった（P23: 品質問題・詐欺）**: Edison機能せず、従来機器で代替、不正確な検査結果
2. **規制未遵守（P16: 規制・法的問題）**: FDA承認なし、CLIA違反、患者データ改ざん
3. **過剰調達（P28: Death by Overfunding）**: $700M+調達、技術検証なし、著名投資家の盲信

#### 定量データ（PMF未達成の証拠）
| 指標 | PMF達成基準（ForStartup） | Theranos実績 | 判定 |
|------|-------------------------|-------------|:----:|
| 技術的実証 | プロトタイプ動作 + 臨床試験データ | Edison機能せず、データ改ざん | ❌ |
| 外部顧客獲得 | 100社/人以上 | Walgreens 40店舗のみ（技術偽装） | ❌ |
| Sean Ellisテスト | 40%以上 | 実施不可能（技術不在） | ❌ |
| 規制承認 | FDA承認必須 | 未承認、CLIA違反 | ❌ |
| 継続率 | 40%以上 | データなし（検査結果不正） | ❌ |
| NPS | 50以上 | 測定不可能 | ❌ |
| 収益化 | 初期売上発生 | Walgreens提携だが技術偽装 | ❌ |

#### ForStartupへの教訓
1. **技術的検証の重要性**: ビジョンだけでは不十分、プロトタイプ動作確認必須、独立した専門家による検証
2. **規制遵守の厳守**: 医療・金融分野では規制ショートカット不可、FDA承認・CLIA遵守が最優先
3. **投資家デューディリジェンスの強化**: 著名投資家の盲信は危険、秘密主義（技術非公開）は警告サイン
4. **PMF検証の厳格化**: 外部顧客獲得100社/人以上、Sean Ellisテスト40%以上を厳格に適用

#### ソース
- @Founder_Research/documents/07_Failure_Study/FAILURE_014_theranos.md

---

### 失敗事例2: CODE.SCORE（PMF未達 - リクルート撤退事例）

#### 事例概要
- **企業名**: リクルートキャリア（Recruit Career）
- **製品名**: CODE.SCORE（コードスコア）
- **事業内容**: ITエンジニアスキル可視化サービス（コーディングテスト + ピープルアナリティクス）、法人向けB2B SaaS
- **失敗の経緯**: 2015年ローンチ（Yahoo! JAPAN導入）→ 2017年撤退判断（3年単月黒字未達）→ 2018年3月31日終了
- **結果**: サービス期間約3年、推定顧客50-100社、推定売上1.5億円、完全撤退

#### PMF失敗の詳細
1. **競合優位性の欠如（2-3倍優位性のみ、10倍なし）**: paiza（無料）、Track（低価格）に顧客流出
2. **3年単月黒字未達成（リクルート撤退基準）**: 2015年ローンチ → 2017年9月撤退判断 → 2018年3月終了
3. **市場タイミングのミスマッチ**: 黎明期参入だが無料サービス普及により有料B2Bモデル成立困難

#### 定量データ（PMF未達成の証拠）
| 指標 | PMF達成基準（ForStartup） | CODE.SCORE実績 | 判定 |
|------|-------------------------|---------------|:----:|
| 外部顧客獲得 | 100社/人以上 | 推定50-100社 | ⚠️/❌ |
| Sean Ellisテスト | 40%以上 | データなし | - |
| 月次成長率 | 10%/月以上 | 5-10% → 5%未満（成長鈍化） | ❌ |
| Churn Rate | 5%/月以下 | 推定20%/月 | ❌ |
| NPS | 50以上 | データなし | - |
| 収益化 | 初期売上発生 | 2015年度3,000万円、2017年度1.5億円 | ⚠️ |
| 3年黒字計画 | 策定済み | 未達成（営業利益率-20%） | ❌ |
| LTV/CAC | ≥ 3.0 | 1.2（ARPU 25万円、CAC 100万円） | ❌ |
| NRR | ≥ 100% | 80%（既存顧客の支出減） | ❌ |

#### ForStartupへの教訓
1. **無料競合市場での10倍優位性必須**: paiza（無料）vs CODE.SCORE（有料）では2-3倍優位性では不足
2. **B2B SaaSは継続率（NRR 100%以上）が必須**: 1回きりのスキル評価では継続的価値なし
3. **リクルート撤退基準の厳格性が損失拡大を防ぐ**: 3年単月黒字基準により早期撤退
4. **CPF検証での緊急性（3U検証）の重要性**: 3Uすべて✅でなければPMF達成困難
5. **ForStartup Benchmark比較の厳格化**: Airレジ1年10万店舗 vs CODE.SCORE 3年50-100社（200-2000倍の差）

#### ソース
- @Founder_Research/documents/WITHDRAWN/CODE.SCORE.md

---

## 追加機能: Tier 3B 失敗事例のPMF診断への活用方法

### validate-pmf実行時のチェックリスト（失敗回避）

#### Theranos型失敗の回避
- [ ] 技術的実証完了（プロトタイプ動作 + 第三者検証）
- [ ] 規制遵守確認（医療・金融分野ではFDA/金融庁承認必須）
- [ ] 査読論文・臨床試験データ存在
- [ ] 秘密主義でない（技術公開、内部告発者保護）
- [ ] 投資家の技術的デューディリジェンス実施済み

#### CODE.SCORE型失敗の回避
- [ ] 無料競合市場では10倍優位性必須（2-3倍では不足）
- [ ] 継続率検証（NRR ≥ 100%、月次Churn ≤ 5%）
- [ ] 緊急性確認（3U検証で「Urgent」が✅）
- [ ] LTV/CAC ≥ 3.0達成（健全なUnit Economics）
- [ ] 大手1社の成功が中小企業に再現可能か検証済み

### 撤退判断の明確化（ForStartup基準）

| 指標 | 撤退判断基準 | Theranos | CODE.SCORE | あなたのプロジェクト |
|------|------------|----------|-----------|-----------------|
| 技術的実証 | プロトタイプ未動作 | ❌（技術不在） | ✅（技術は動作） | - |
| 外部顧客獲得 | < 50社/人 | ❌（40店舗、偽装） | ⚠️（50-100社） | - |
| 月次成長率 | < 5%/月（3ヶ月連続） | - | ❌（5%未満） | - |
| Churn率 | > 10%/月（3ヶ月連続） | - | ❌（20%/月） | - |
| LTV/CAC | < 1.5 | - | ❌（1.2） | - |
| 3年単月黒字 | 未達成 | ❌（詐欺） | ❌（未達成） | - |
| 規制違反 | FDA/CLIA違反 | ❌（未承認） | - | - |

**判定ロジック**:
- 上記6指標のうち2つ以上❌ → 即座に撤退検討（`/pivot-decision`実行）
- Theranos型（技術不在 + 規制違反）→ 即座に撤退（倫理的責任）
- CODE.SCORE型（3年黒字未達）→ Pivot or 撤退（リクルート基準適用）

---

## 統合要件の達成状況

### ✅ 完了した要件

1. **既存のTier 2/Tier 3セクションを保持**:
   - ✅ Tier 2（成功事例: Airレジ、Airペイ、スタディサプリ、Geppo）を完全保持
   - ✅ Tier 3（VC-Backed Unicorn: Notion、Figma、Databricks）を完全保持

2. **新規セクション "Tier 3B: PMF失敗事例（ForStartup特化）" を追加**:
   - ✅ セクション追加完了（約220行）

3. **各失敗事例について以下を記載**:
   - ✅ **事例概要**: 企業名、事業内容、失敗の経緯（Theranos、CODE.SCORE）
   - ✅ **PMF失敗の詳細**: なぜPMFを達成できなかったのか（3つの理由を明確化）
   - ✅ **定量データ**: PMFスコア、評価額、調達額、期間、損失額（表形式で整理）
   - ✅ **失敗パターン**: P16（規制）、P23（品質）、P28（過剰調達）等を詳細分析
   - ✅ **教訓**: ForStartupのPMF検証に活かすべきポイント（4-5項目）

4. **ソース引用**: 各データに出典を明記
   - ✅ Theranos: `@Founder_Research/documents/07_Failure_Study/FAILURE_014_theranos.md`
   - ✅ CODE.SCORE: `@Founder_Research/documents/WITHDRAWN/CODE.SCORE.md`

5. **フォーマット統一**: 既存のTier 2/3と同じMarkdown形式
   - ✅ 見出しレベル統一（###、####）
   - ✅ 表形式統一（定量データ、判定列、ForStartup Benchmark比較）
   - ✅ チェックリスト形式統一

---

## 統合後のスキル構造

### validate-pmf/SKILL.md 全体構成

```
validate-pmf/SKILL.md
├── メタデータ（name, description, trigger_keywords等）
├── このSkillでできること
├── 入力・出力
├── Knowledge Base参照
├── Domain-Specific Knowledge (from Founder_Research)
│   ├── Success Patterns
│   │   ├── Tier 2 事例（成功事例: Airレジ、Airペイ、スタディサプリ、Geppo）
│   │   └── Tier 3 事例（VC-Backed Unicorn: Notion、Figma、Databricks）
│   ├── Common Pitfalls（失敗パターン1-3）
│   ├── Quantitative Benchmarks（外部顧客獲得、Sean Ellis、成長率、Churn、NPS、NDR、収益化）
│   ├── Best Practices
│   │   ├── Tier 2ベストプラクティス（成功事例）
│   │   └── Tier 3ベストプラクティス（VC-Backed Unicorn成功事例）
│   └── Reference
├── **Tier 3B: PMF失敗事例（ForStartup特化）** ← **新規追加**
│   ├── 失敗事例1: Theranos（P16+P23+P28 - 詐欺・規制失敗）
│   │   ├── 事例概要
│   │   ├── PMF失敗の詳細
│   │   ├── 定量データ（PMF未達成の証拠）
│   │   ├── 失敗パターン詳細
│   │   └── ForStartupへの教訓
│   ├── 失敗事例2: CODE.SCORE（PMF未達 - リクルート撤退事例）
│   │   ├── 事例概要
│   │   ├── PMF失敗の詳細
│   │   ├── 定量データ（PMF未達成の証拠）
│   │   ├── 失敗パターン詳細
│   │   └── ForStartupへの教訓
│   ├── Tier 3B 失敗事例のPMF診断への活用方法
│   │   ├── validate-pmf実行時のチェックリスト（失敗回避）
│   │   │   ├── Theranos型失敗の回避（5項目）
│   │   │   └── CODE.SCORE型失敗の回避（5項目）
│   │   └── 撤退判断の明確化（ForStartup基準）
│   │       ├── 判定表（6指標）
│   │       └── 判定ロジック
│   └── Reference（Tier 3B失敗事例）
├── PMF達成基準（ForStartup版）
├── Instructions（自動実行フロー: STEP 1-11）
├── 成果物フォーマット
├── ForStartup Knowledge Base Reference
├── 使用例
├── 成功基準
├── 注意事項
└── 更新履歴
```

---

## 品質チェック結果

### 1. 既存コンテンツの保持
- ✅ Tier 2成功事例（4事例）: 削除なし、変更なし
- ✅ Tier 3成功事例（3事例）: 削除なし、変更なし
- ✅ Common Pitfalls: 削除なし、変更なし
- ✅ Quantitative Benchmarks: 削除なし、変更なし
- ✅ Best Practices: 削除なし、変更なし

### 2. 新規セクションの品質
- ✅ Tier 3B追加: 約220行（失敗事例2件、活用方法、チェックリスト、判定表）
- ✅ フォーマット統一: 既存のTier 2/3と同じMarkdown形式
- ✅ 定量データ網羅: PMF達成基準（ForStartup）との比較表を両事例で作成
- ✅ 失敗パターン明確化: P16、P23、P28を詳細分析（Theranos）、CPF/PSF/PMF段階別に分析（CODE.SCORE）
- ✅ 教訓の具体性: 各事例で4-5項目、実行可能な提案
- ✅ ソース引用: 全データに出典を明記

### 3. 実用性の向上
- ✅ チェックリスト追加: validate-pmf実行時の失敗回避チェック（10項目）
- ✅ 撤退判断表追加: 6指標での定量的判定基準
- ✅ 判定ロジック追加: 2つ以上❌ → 即座に撤退検討

---

## 次のステップ

### 推奨アクション
1. **validate-pmf/SKILL.mdの検証**:
   - スキル実行時にTier 3B失敗事例が参照されるか確認
   - チェックリストが自動生成されるか確認
   - 撤退判断表が診断レポートに統合されるか確認

2. **他のスキルへの失敗事例統合**:
   - `/validate-cpf`: Theranos（CPF段階の虚偽）、CODE.SCORE（緊急性不足）
   - `/validate-10x`: CODE.SCORE（2-3倍優位性のみ）
   - `/pivot-decision`: 撤退判断基準の統一

3. **ForStartup Knowledge Baseへの統合**:
   - `.claude/skills/_shared/case_reference_for_startup.md#failure-patterns` への追加
   - 失敗パターン体系（P16、P23、P28）の詳細化

---

## メタデータ

| 項目 | 内容 |
|-----|------|
| 作成日 | 2026-01-03 |
| タスク実行時間 | 約30分 |
| 追加行数 | 約220行 |
| 統合事例数 | 2件（Theranos、CODE.SCORE） |
| ソース品質 | Tier 1-2（一次情報・公式第三者情報） |
| 次回更新予定 | 失敗事例3-5件追加時（WeWork、MoviePass等） |
| 担当エージェント | Founder Agent ForStartup Edition - Failure Case Integration Agent |

---

**完了**

Tier 3B: PMF失敗事例（ForStartup特化）の統合が完了しました。validate-pmf/SKILL.mdは、成功事例（Tier 2/3）と失敗事例（Tier 3B）の両方を統合し、ForStartupの厳格な検証基準に基づくPMF診断の精度が向上しました。
