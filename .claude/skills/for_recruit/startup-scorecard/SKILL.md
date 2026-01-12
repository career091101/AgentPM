---
name: startup-scorecard
description: |
  スタートアップの健全性を4視点で評価するスコアカード作成スキル（ForRecruit特化版）。Financial（財務）/Customer（顧客）/Internal Process（業務プロセス）/Learning & Growth（学習・成長）の4視点を各10点評価（計40点満点）。Ring制度評価項目を反映し、社内リソース活用度・既存事業シナジーを追加評価。

  ForRecruit調整:
  - Ring制度評価項目の統合（Ring 1-3各段階の達成基準）
  - 社内リソース活用評価（6カテゴリ20点満点）
  - 既存事業シナジー評価（カニバリゼーション回避、クロスセル効果）
  - 総合80点満点（4視点40点+社内リソース20点+シナジー20点）

  使用タイミング：
  - Ring 1-3各段階での健全性評価
  - Phase1完了時の総合評価
  - 役員承認申請前の最終チェック

  所要時間：30-50分（社内リソース評価含む）
  出力：scorecard_forrecruit.md
---

# Startup Scorecard Skill (ForRecruit Edition)

スタートアップの健全性を6視点で評価するスコアカード作成Skill（ForRecruit特化版）。4視点評価（40点）+社内リソース活用（20点）+既存事業シナジー（20点）= 総合80点満点。

---

## このSkillでできること

1. **6視点評価**: Financial/Customer/Internal Process/Learning & Growth/社内リソース活用/既存事業シナジーを評価
2. **総合判定**: 80点満点でRing制度各段階の健全性を判定
3. **弱点特定**: スコアが低い視点を特定し改善案を提示
4. **Ring段階判定**: Ring 1/2/3のどの段階にいるか判定
5. **次のアクション提案**: Ring制度に基づいた次のステップを明確化

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 全成果物（`documents/`, `mvp/`）、`ring_criteria_diagnosis.md` |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/5_monitoring/scorecard_forrecruit.md` |
| **次のSkill** | `/validate-ring-criteria`（Ring移行判定） or `/build-approval-deck`（役員承認申請） |

---

## Domain-Specific Knowledge (from Recruit_Product_Research)

### Success Patterns

**1. Airレジ（スコアカード成功事例）**
- **Financial**: 価格設定妥当（基本無料、初期費用100倍削減）、収益モデル明確（周辺機器・連携サービス）、3年黒字達成
- **Customer**: ペルソナ明確（中小飲食店・小売店）、課題裏付け（Problem Commonality 75%）、UVP刺さり度高（初期費用0円、導入1日）
- **Internal Process**: フライホイール設計（営業網2,000名活用）、MVP完成（ホットペッパー既存顧客30社PoC）、10倍優位性4軸
- **Learning & Growth**: ドキュメント整備、仮説検証サイクル（3ヶ月Ring 1達成）、改善アクション実行
- **社内リソース活用**: 営業網+顧客基盤+ブランド力（3種活用、PMFスコア8.8）
- **既存事業シナジー**: Airペイ・Airキャッシュへのクロスセル57%、カニバリゼーションなし

**2. Geppo（スコアカード成功事例）**
- **Financial**: 価格設定妥当（月額500円/人、業界標準1,000円の半額）、収益モデル明確（サブスク+運用代行）、3年黒字達成
- **Customer**: ペルソナ明確（人事部門）、課題裏付け（Problem Commonality 80%、離職率20% → 10%改善）、UVP刺さり度高（回答負荷10倍削減）
- **Internal Process**: フライホイール設計（社内先行運用4年）、MVP完成（リクルート1,200名PoC）、10倍優位性2軸（回答負荷10倍削減、継続率98%）
- **Learning & Growth**: ドキュメント整備、仮説検証サイクル（社内4年改善）、改善アクション実行
- **社内リソース活用**: 顧客基盤+ブランド力+データ資産（3種活用、PMFスコア8.8）
- **既存事業シナジー**: 人事領域で既存事業なし、カニバリゼーションリスク0

**3. Airペイ（スコアカード成功事例）**
- **Financial**: 価格設定妥当（決済手数料2.48-3.74%、業界最安級）、収益モデル明確（決済手数料）、3年黒字達成
- **Customer**: ペルソナ明確（小規模店舗）、課題裏付け（Problem Commonality 85%）、UVP刺さり度高（初期費用0円、81種決済対応）
- **Internal Process**: フライホイール設計（Airレジ90.4万顧客基盤活用）、MVP完成（Airレジ既存顧客PoC）、10倍優位性4軸
- **Learning & Growth**: ドキュメント整備、仮説検証サイクル（6ヶ月Ring 1達成）、改善アクション実行
- **社内リソース活用**: 営業網+顧客基盤+ブランド力+データ資産（4種活用、PMFスコア8.8以上）
- **既存事業シナジー**: Airレジからのクロスセル57%（業界標準5-15%の4-11倍）、エコシステム固定化

### Common Pitfalls

**失敗パターン1: 社内リソース活用不足**
- **CODE.SCORE**: 資産活用0種 → PMFスコア5.2、成功率25%
- **教訓**: 3種以上活用でPMFスコア8.8、成功率100%

**失敗パターン2: 既存事業カニバリゼーション**
- **スタディサプリ個別指導**: ベーシックコース2,178円が優秀すぎる → 個別指導10,780円が売れない → 1.5年で撤退
- **教訓**: 既存製品との差別化を10倍規模で設計、価格差に見合う価値証明

**失敗パターン3: CPF検証不足**
- **リクルートDMPフォロー**: 採用担当者へのヒアリング10件のみ → 市場ニーズ過大評価 → Ring 1承認後にピボット → 撤退
- **教訓**: 30件以上のUser Researchを徹底、Problem Commonality 70%以上を確保

### Quantitative Benchmarks

**Financial視点**:
- 価格設定妥当性: 競合比最安級（Airペイ決済手数料最安、Geppo月額500円）、初期費用0円（Airレジ、Airペイ）
- 収益モデル明確性: 3年黒字達成（Airレジ、Airペイ、Geppo、スタディサプリ）
- Unit Economics: LTV/CAC 10-30倍（Airレジ15-30倍、Airペイ10-15倍、Geppo 20倍）

**Customer視点**:
- ペルソナ明確性: 明確なターゲット設定（Airレジ：中小飲食店・小売店、Geppo：人事部門）
- 課題裏付け（3U）: Problem Commonality 70-85%（Airレジ75%、Airペイ85%、Geppo 80%）
- UVP刺さり度: 10倍優位性2軸以上（Airレジ4軸、Airペイ4軸、Geppo 2軸）

**Internal Process視点**:
- フライホイール設計: 営業網活用、クロスセル戦略（Airレジ→Airペイ 57%）
- MVP完成: 社内PoC実施（Geppo リクルート1,200名、Airレジ ホットペッパー既存顧客30社）
- 10倍優位性: 2軸以上（Airレジ4軸、Airペイ4軸、Geppo 2軸）

**Learning & Growth視点**:
- ドキュメント整備: 成果物完備、フレームワーク準拠
- 仮説検証サイクル: Ring 1達成期間3-6ヶ月（Airレジ3ヶ月、Airペイ6ヶ月）
- 改善アクション実行: 社内先行運用による継続改善（Geppo 4年）

**社内リソース活用視点**:
- 3種以上活用: PMFスコア8.8、成功率100%（Airレジ、Airペイ、Geppo）
- 1-2種活用: PMFスコア7.5、成功率80%（SUUMO、じゃらん、スタディサプリ）
- 0種活用: PMFスコア5.2、成功率25%（CODE.SCORE、termhub）

**既存事業シナジー視点**:
- クロスセル率: 57%（Airレジ→Airペイ、業界標準5-15%の4-11倍）
- カニバリゼーション回避: 既存製品との差別化10倍規模（スタサプ個別指導失敗の教訓）
- エコシステム固定化: Airシリーズ連携、リクルートID統合

### Best Practices

1. **Ring 1（CPF検証）のベストプラクティス**:
   - 既存顧客基盤30-100社ヒアリング（低コスト、高信頼性フィードバック）
   - Problem Commonality 70%以上を目標
   - イントレプレナーFIF評価: 社歴5年以上、社内実績ありの信頼できる人材

2. **Ring 2（PSF検証）のベストプラクティス**:
   - 社内リソース3種以上活用（既存顧客基盤、営業網、ブランド力）でPMFスコア8.8、成功率100%
   - 10倍優位性2軸以上構築（コスト、時間、手数料等の複合軸）
   - MVP完成、社内PoC実施で承認確率向上

3. **Ring 3（PMF検証）のベストプラクティス**:
   - 外部顧客獲得1,000社/人（ベンチマーク: Airレジ1年で10万店舗）
   - 3年黒字・5年累損解消計画の定量的ロードマップ作成
   - Unit Economics健全性: LTV/CAC 10-30倍、Churn率10-15%以下

### Reference

- 詳細: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/analysis/integrated_analysis_report.md`
- 個別事例: `@Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_ForRecruit/Recruit_Product_Research/documents/SUCCESS/`

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 30-50分

### 自動実行ステップ

1. 全成果物の存在確認
2. Financial視点評価（10点）
3. Customer視点評価（10点）
4. Internal Process視点評価（10点）
5. Learning & Growth視点評価（10点）
6. **社内リソース活用評価（20点）**
7. **既存事業シナジー評価（20点）**
8. 総合判定（80点満点）
9. 弱点特定・改善案提示
10. Ring段階判定（Ring 1/2/3）
11. 次のアクション提案
12. 成果物出力

### 6視点評価基準（ForRecruit版）

**Financial視点（10点満点）**:
- 価格設定の妥当性（4点）: 競合比最安級、初期費用0円等
- 収益モデルの明確性（3点）: 3年黒字計画、Unit Economics健全性
- コスト構造の把握（3点）: 固定費・変動費の試算、社内リソース活用によるコスト削減

**Customer視点（10点満点）**:
- ペルソナの明確性（3点）: 明確なターゲット設定
- 課題の裏付け（3U）（4点）: Problem Commonality 70%以上
- UVPの刺さり度（3点）: 10倍優位性2軸以上

**Internal Process視点（10点満点）**:
- フライホイール設計（3点）: 営業網活用、クロスセル戦略
- MVP選定・構築（4点）: 社内PoC実施
- 10倍優位性の確認（3点）: 2軸以上

**Learning & Growth視点（10点満点）**:
- ドキュメント整備（4点）: 成果物完備、フレームワーク準拠
- 仮説検証サイクル（3点）: Ring達成期間3-6ヶ月
- 改善アクションの実行（3点）: 社内先行運用による継続改善

**社内リソース活用視点（20点満点）**:
| 資産タイプ | 配点 | 評価基準 |
|----------|-----|---------|
| 営業網 | 4点 | ホットペッパー2,000名等の活用状況 |
| 既存顧客基盤 | 4点 | クロスセル率、既存顧客へのアプローチ |
| ブランド力 | 3点 | リクルートブランド信頼性活用 |
| データ資産 | 3点 | 決済データ、顧客データ活用 |
| プラットフォーム | 3点 | Airシリーズ連携、リクルートID統合 |
| インフラ | 3点 | リクルートクラウド基盤活用 |

**総合評価**:
- 3種以上活用（12点以上）: 期待PMFスコア8.8、成功率100%
- 1-2種活用（4-11点）: 期待PMFスコア7.5、成功率80%
- 0種活用（0-3点）: 期待PMFスコア5.2、成功率25%

**既存事業シナジー視点（20点満点）**:
| 評価軸 | 配点 | 評価基準 |
|-------|-----|---------|
| カニバリゼーション回避 | 8点 | 既存製品との差別化10倍規模、価格差に見合う価値証明 |
| クロスセル効果 | 8点 | クロスセル率57%目標（Airレジ→Airペイ実績）、既存顧客への誘導施策 |
| エコシステム固定化 | 4点 | 複数サービス連携、リクルートID統合、スイッチングコスト構築 |

**総合評価**:
- カニバリゼーションリスクなし + クロスセル率50%以上: 16点以上
- カニバリゼーションリスク低 + クロスセル率20-50%: 10-15点
- カニバリゼーションリスク高 or クロスセル率20%未満: 0-9点

### 判定基準（ForRecruit版）

**総合判定（80点満点）**:
- 64-80点: ✅ 健全 → Ring移行・役員承認申請可
- 40-63点: ⚠️ 要改善 → 低スコア視点を改善
- 0-39点: ❌ 要見直し → Phase1再実行

**Ring段階判定**:
- Ring 1（CPF検証）: Customer視点 ≥ 6点 + 社内リソース活用 ≥ 4点
- Ring 2（PSF検証）: Internal Process視点 ≥ 6点 + 社内リソース活用 ≥ 8点 + 既存事業シナジー ≥ 10点
- Ring 3（PMF検証）: Financial視点 ≥ 6点 + 実績データあり + 社内リソース活用 ≥ 12点 + 既存事業シナジー ≥ 16点

---

## エラーハンドリング

（Origin版と同様のValidation + Graceful Degradationパターン、ForRecruit視点評価を追加）

### データ検証失敗時のGraceful Degradation

**必須項目チェック**:
- [ ] Financial視点データ（価格設定、収益モデル、コスト構造）
- [ ] Customer視点データ（ペルソナ、課題裏付け、UVP）
- [ ] Internal Process視点データ（フライホイール、MVP、10倍優位性）
- [ ] Learning & Growth視点データ（ドキュメント整備、仮説検証サイクル）
- [ ] **社内リソース活用データ（6種資産の活用状況）**
- [ ] **既存事業シナジーデータ（カニバリゼーション、クロスセル）**

**判定ロジック**:

| 必須項目充足率 | 対応 |
|-------------|------|
| 100% | 通常スコアカード評価、80点満点 |
| 75-99% | 警告表示 + 部分スコアカード評価 + 続行 |
| <75% | エラー報告 + 停止 |

---

## 成果物フォーマット

```markdown
# スタートアップスコアカード（ForRecruit Edition）

**作成日**: [YYYY-MM-DD]
**対象プロジェクト**: [プロジェクト名]
**総合判定**: ✅ 健全（64-80点） / ⚠️ 要改善（40-63点） / ❌ 要見直し（0-39点）
**Ring段階**: Ring 1 / Ring 2 / Ring 3
**Ring移行**: [可 / 要改善 / 不可]

---

## エグゼクティブサマリー

### 総合スコア: [XX/80点]

| 視点 | スコア | 評価 |
|------|:------:|:----:|
| Financial | X/10点 | ✅/⚠️/❌ |
| Customer | X/10点 | ✅/⚠️/❌ |
| Internal Process | X/10点 | ✅/⚠️/❌ |
| Learning & Growth | X/10点 | ✅/⚠️/❌ |
| **社内リソース活用** | **XX/20点** | ✅/⚠️/❌ |
| **既存事業シナジー** | **XX/20点** | ✅/⚠️/❌ |

**判定理由**:
[6視点の状況から総合判定の根拠を記載]

**ForRecruit Benchmark比較**:
- Airレジ: Financial 9/10、Customer 9/10、Internal Process 10/10、L&G 9/10、社内リソース 16/20、シナジー 18/20、合計 71/80
- Airペイ: Financial 9/10、Customer 10/10、Internal Process 10/10、L&G 9/10、社内リソース 18/20、シナジー 20/20、合計 76/80
- Geppo: Financial 9/10、Customer 10/10、Internal Process 8/10、L&G 10/10、社内リソース 16/20、シナジー 20/20、合計 73/80
- あなたのプロジェクト: [比較コメント]

---

## 詳細分析

### 視点1: Financial（10点満点）

**評価**: X/10点

**内訳**:
- 価格設定の妥当性: X/4点
  - 評価: [競合比最安級 / 標準価格 / 高価格]
  - 根拠: [具体的な価格戦略、競合比較]
  - ForRecruit Benchmark: Airペイ決済手数料最安、Geppo月額500円（業界標準1,000円の半額）

- 収益モデルの明確性: X/3点
  - 評価: [明確 / やや曖昧 / 不明確]
  - 根拠: [3年黒字計画、Unit Economics健全性]
  - ForRecruit Benchmark: Airレジ・Airペイ・Geppo・スタディサプリ すべて3年黒字達成

- コスト構造の把握: X/3点
  - 評価: [詳細把握 / 概算 / 未把握]
  - 根拠: [固定費・変動費の試算、社内リソース活用によるコスト削減]
  - ForRecruit Benchmark: 営業網活用でCAC 1-2万円（競合の1/5〜1/10）

**改善推奨**:
- [具体的な改善施策]

---

### 視点2: Customer（10点満点）

**評価**: X/10点

**内訳**:
- ペルソナの明確性: X/3点
  - 評価: [明確 / やや曖昧 / 不明確]
  - 根拠: [ターゲット設定の具体性]
  - ForRecruit Benchmark: Airレジ（中小飲食店・小売店）、Geppo（人事部門）

- 課題の裏付け（3U）: X/4点
  - 評価: [強い裏付け / 中程度 / 弱い]
  - 根拠: [Problem Commonality XX%、User Research XX件]
  - ForRecruit Benchmark: Airレジ75%、Airペイ85%、Geppo 80%

- UVPの刺さり度: X/3点
  - 評価: [強い / 中程度 / 弱い]
  - 根拠: [10倍優位性X軸]
  - ForRecruit Benchmark: Airレジ4軸、Airペイ4軸、Geppo 2軸

**改善推奨**:
- [具体的な改善施策]

---

### 視点3: Internal Process（10点満点）

**評価**: X/10点

**内訳**:
- フライホイール設計: X/3点
  - 評価: [完全 / 部分的 / 未設計]
  - 根拠: [営業網活用、クロスセル戦略]
  - ForRecruit Benchmark: Airレジ（営業網2,000名活用）、Airペイ（クロスセル57%）

- MVP選定・構築: X/4点
  - 評価: [完成 / 構築中 / 未着手]
  - 根拠: [社内PoC実施状況]
  - ForRecruit Benchmark: Geppo（リクルート1,200名）、Airレジ（ホットペッパー既存顧客30社）

- 10倍優位性の確認: X/3点
  - 評価: [2軸以上 / 1軸 / 0軸]
  - 根拠: [競合優位性の具体的内容]
  - ForRecruit Benchmark: Airレジ4軸、Airペイ4軸、Geppo 2軸

**改善推奨**:
- [具体的な改善施策]

---

### 視点4: Learning & Growth（10点満点）

**評価**: X/10点

**内訳**:
- ドキュメント整備: X/4点
  - 評価: [完備 / 部分的 / 不十分]
  - 根拠: [成果物完備状況、フレームワーク準拠]
  - ForRecruit Benchmark: 成功製品すべてドキュメント完備

- 仮説検証サイクル: X/3点
  - 評価: [高速 / 標準 / 遅い]
  - 根拠: [Ring達成期間]
  - ForRecruit Benchmark: Airレジ3ヶ月、Airペイ6ヶ月、Geppo社内4年

- 改善アクションの実行: X/3点
  - 評価: [継続的 / 断続的 / 未実施]
  - 根拠: [社内先行運用、継続改善]
  - ForRecruit Benchmark: Geppo社内先行運用4年、継続改善

**改善推奨**:
- [具体的な改善施策]

---

### 視点5: 社内リソース活用（20点満点）

**評価**: XX/20点

**内訳**:
| 資産タイプ | 活用状況 | スコア | 評価基準 |
|----------|---------|:------:|---------|
| 営業網 | [活用 / 未活用] | X/4点 | ホットペッパー2,000名等の活用状況 |
| 既存顧客基盤 | [活用 / 未活用] | X/4点 | クロスセル率、既存顧客へのアプローチ |
| ブランド力 | [活用 / 未活用] | X/3点 | リクルートブランド信頼性活用 |
| データ資産 | [活用 / 未活用] | X/3点 | 決済データ、顧客データ活用 |
| プラットフォーム | [活用 / 未活用] | X/3点 | Airシリーズ連携、リクルートID統合 |
| インフラ | [活用 / 未活用] | X/3点 | リクルートクラウド基盤活用 |

**総合評価**:
- 資産活用数: X種
- 期待PMFスコア: X.X（Recruit_Product_Research分析結果）
- 期待成功率: XX%

**ForRecruit Benchmark比較**:
| 資産活用数 | 期待PMFスコア | 期待成功率 | 代表製品 | スコア目安 |
|----------|------------|----------|---------|----------|
| **3種以上** | **8.8** | **100%** | Airレジ、Airペイ、Geppo | **12-20点** |
| **1-2種** | **7.5** | **80%** | SUUMO、じゃらん、スタディサプリ | **4-11点** |
| **0種** | **5.2** | **25%** | CODE.SCORE、termhub | **0-3点** |
| **あなたのプロジェクト** | **X.X** | **XX%** | - | **XX点** |

**改善推奨**:
- [資産活用が3種未満の場合の具体的施策]

---

### 視点6: 既存事業シナジー（20点満点）

**評価**: XX/20点

**内訳**:
- カニバリゼーション回避: X/8点
  - 評価: [リスクなし / リスク低 / リスク高]
  - 根拠: [既存製品との差別化10倍規模、価格差に見合う価値証明]
  - ForRecruit Benchmark: Geppo（人事領域で既存事業なし、リスク0）、スタサプ個別指導失敗（ベーシックコース2,178円が優秀すぎる）

- クロスセル効果: X/8点
  - 評価: [高い / 中程度 / 低い]
  - 根拠: [クロスセル率XX%、既存顧客への誘導施策]
  - ForRecruit Benchmark: Airレジ→Airペイ 57%（業界標準5-15%の4-11倍）

- エコシステム固定化: X/4点
  - 評価: [強い / 中程度 / 弱い]
  - 根拠: [複数サービス連携、リクルートID統合、スイッチングコスト構築]
  - ForRecruit Benchmark: Airシリーズ連携、リクルートID統合

**改善推奨**:
- [具体的な改善施策]

---

## Ring段階判定

### 現在のRing段階: Ring X

**判定根拠**:
- Ring 1（CPF検証）: Customer視点 X/10点（基準6点） + 社内リソース活用 XX/20点（基準4点） → [✅ 達成 / ❌ 未達成]
- Ring 2（PSF検証）: Internal Process視点 X/10点（基準6点） + 社内リソース活用 XX/20点（基準8点） + 既存事業シナジー XX/20点（基準10点） → [✅ 達成 / ❌ 未達成]
- Ring 3（PMF検証）: Financial視点 X/10点（基準6点） + 実績データあり + 社内リソース活用 XX/20点（基準12点） + 既存事業シナジー XX/20点（基準16点） → [✅ 達成 / ❌ 未達成]

**ForRecruit成功事例との比較**:
| 製品 | Ring 1達成期間 | Ring 2達成期間 | Ring 3達成期間 | スコア（推定） |
|------|--------------|--------------|--------------|--------------|
| Airレジ | 3ヶ月 | 6ヶ月 | 1年 | 71/80 |
| Airペイ | 6ヶ月 | 1年 | 1年 | 76/80 |
| Geppo | 社内先行運用 | 1年 | 2年 | 73/80 |
| あなたのプロジェクト | - | - | - | XX/80 |

---

## 次のアクション

### Ring移行判定: [Ring X → Ring Y 移行可 / 要改善 / 移行不可]

**即時実行推奨**:
1. [アクション1]
2. [アクション2]
3. [アクション3]

**中期施策（1-3ヶ月）**:
1. [施策1]
2. [施策2]
3. [施策3]

**Ring移行準備**:
- `/validate-ring-criteria` で詳細なRing基準チェック
- `/build-approval-deck` で役員承認用資料作成（Ring 3移行時）

---

## メタデータ

| 項目 | 内容 |
|-----|------|
| 作成日 | [YYYY-MM-DD] |
| 実行Skill | `/startup-scorecard` (ForRecruit Edition) |
| フレームワーク | バランススコアカード + Ring制度 |
| 準拠率 | 100% |
| 次の更新予定 | [Ring移行後 / 3ヶ月後] |
| Research統合 | Recruit_Product_Research 31製品分析 |
| Benchmark製品 | Airレジ、Airペイ、Geppo |
```

---

## Knowledge Base参照

- バランススコアカード: `@startup_science/02_frameworks/balance_scorecard/scorecard_overview.md`
- Ring制度: `@Founder_Agent_ForRecruit/README.md`
- **ForRecruit Research**: `@Recruit_Product_Research/analysis/integrated_analysis_report.md`
- **ForRecruit成功事例**: `@Recruit_Product_Research/documents/SUCCESS/`
- **エラーハンドリング**: `.claude/skills/_shared/error_handling_patterns.md`

---

## ForRecruit Knowledge Base Reference

### 評価基準・フレームワーク
- CPF/PSF/PMF基準: @.claude/skills/_shared/recruit_specific_frameworks.md#cpf-evaluation
- Ring制度詳細: @.claude/skills/_shared/recruit_specific_frameworks.md#ring-system
- 社内リソース活用: @.claude/skills/_shared/recruit_specific_frameworks.md#resource-leverage
- ForRecruit評価基準: @.claude/skills/_shared/knowledge_base.md#forrecruit-evaluation

### 事例参照
- 成功パターン（Tier 1-4）: @.claude/skills/_shared/case_reference_for_recruit.md#success-patterns
- 失敗パターン: @.claude/skills/_shared/case_reference_for_recruit.md#failure-patterns
- スキル別推奨事例: @.claude/skills/_shared/case_reference_for_recruit.md#skill-mapping-startup-scorecard
- 総合80点満点評価: @.claude/skills/_shared/recruit_specific_frameworks.md#scorecard-criteria

### 全体参照
- ForRecruit全体概要: @.claude/skills/_shared/knowledge_base.md#forrecruit-edition
- Ring制度ステージゲート: @.claude/skills/_shared/knowledge_base.md#ring-stage-gates
- 撤退基準: @.claude/skills/_shared/knowledge_base.md#withdrawal-criteria

---
## 注意事項

1. **ForRecruit特化調整**:
   - 総合80点満点（4視点40点+社内リソース20点+シナジー20点）
   - Ring制度評価項目の統合（Ring 1-3各段階の達成基準）
   - 社内リソース活用3種以上でPMFスコア8.8、成功率100%
   - 既存事業カニバリゼーション回避必須

2. **成功製品スコア目安**:
   - Airレジ: 71/80点（Financial 9、Customer 9、Internal Process 10、L&G 9、社内リソース 16、シナジー 18）
   - Airペイ: 76/80点（Financial 9、Customer 10、Internal Process 10、L&G 9、社内リソース 18、シナジー 20）
   - Geppo: 73/80点（Financial 9、Customer 10、Internal Process 8、L&G 10、社内リソース 16、シナジー 20）

3. **Ring移行基準**:
   - Ring 1 → Ring 2: 社内リソース活用4点以上（1種以上）
   - Ring 2 → Ring 3: 社内リソース活用8点以上（2種以上） + 既存事業シナジー10点以上
   - Ring 3承認: 社内リソース活用12点以上（3種以上） + 既存事業シナジー16点以上

---

## 更新履歴

- 2026-01-02: ForRecruit特化版として新規作成、Recruit_Product_Research 31製品分析統合
- 総合80点満点化（4視点40点+社内リソース20点+シナジー20点）
- Ring制度評価項目の統合
- 社内リソース活用評価追加（6カテゴリ）
- 既存事業シナジー評価追加（カニバリゼーション、クロスセル、エコシステム）
- ForRecruit Benchmark追加（Airレジ、Airペイ、Geppo）
- Domain-Specific Knowledgeセクション追加（15事例統合）
