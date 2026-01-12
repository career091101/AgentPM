---
title: "Batch 2-3 品質スコアリング最終レポート"
date: 2025-12-29
project: Founder_Research
category: Quality Assurance
tags:
  - quality-scoring
  - batch-processing
  - fact-check
  - automated-qa
  - founder-research
summary: |
  Batch 2-3（18ファイル）の自動品質スコアリング実行結果。平均スコア83.9/100、Fact Check Pass率100%を達成。
  Grade分布はA:4、B:6、C:8、平均ソース数13.6件、平均10x axes 3.2軸の高品質を確認。
  品質基準（Fact Check 100%、平均ソース12+件）を達成し、Stock移行可能と判定。
---

# Batch 2-3 品質スコアリング最終レポート

## エグゼクティブサマリー

**実行日時**: 2025-12-29 11:30  
**対象**: Batch 2-3（18ファイル）  
**平均スコア**: **83.9/100**  
**Fact Check Pass率**: **100% (18/18)**  
**品質判定**: ✅ **合格** （Stock移行可能）

### ハイライト

- **Grade A（95-90点）**: 4ファイル（22%）
- **Grade B（89-80点）**: 6ファイル（33%）
- **Grade C（79-70点）**: 8ファイル（44%）
- **平均ソース数**: 13.6件（目標12件以上）
- **平均10x axes**: 3.2軸
- **Null率**: 89%（16/18ファイルにNull存在、改善余地あり）

---

## Batch 2（7ファイル）詳細結果

| ファイル名 | スコア | Grade | Nulls | Sources | FC | Axes |
|-----------|------:|:-----:|:-----:|:-------:|:--:|:----:|
| FOUNDER_151_airbnb.md | 95 | A | 0 | 15 | ✅ | 4 |
| FOUNDER_152_coinbase.md | 92 | A | 0 | 12 | ✅ | 4 |
| FOUNDER_352_eric_yuan_zoom.md | 90 | A | 2 | 18 | ✅ | 4 |
| FOUNDER_157_github.md | 90 | A | 2 | 15 | ✅ | 4 |
| FOUNDER_351_jan_koum_whatsapp.md | 87 | B | 2 | 15 | ✅ | 3 |
| FOUNDER_355_coinbase.md | 87 | B | 2 | 12 | ✅ | 4 |
| FAILURE_008_jawbone.md | 79 | C | 3 | 12 | ✅ | 3 |

**Batch 2平均スコア**: 87.1/100

---

## Batch 3（11ファイル）詳細結果

| ファイル名 | スコア | Grade | Nulls | Sources | FC | Axes |
|-----------|------:|:-----:|:-----:|:-------:|:--:|:----:|
| EMERGING_001_stability_ai.md | 87 | B | 2 | 15 | ✅ | 3 |
| PIVOT_004_box.md | 84 | B | 2 | 13 | ✅ | 3 |
| PIVOT_005_jasper_ai.md | 84 | B | 1 | 12 | ✅ | 2 |
| FAILURE_009_quibi.md | 82 | B | 4 | 15 | ✅ | 3 |
| FAILURE_010_getaround.md | 79 | C | 4 | 13 | ✅ | 3 |
| FAILURE_011_humane_ai.md | 79 | C | 4 | 12 | ✅ | 3 |
| FOUNDER_159_palantir.md | 79 | C | 4 | 14 | ✅ | 3 |
| FOUNDER_160_okta.md | 79 | C | 4 | 12 | ✅ | 3 |
| EMERGING_002_character_ai.md | 79 | C | 4 | 14 | ✅ | 3 |
| EMERGING_003_midjourney.md | 79 | C | 3 | 13 | ✅ | 3 |
| EMERGING_004_runway.md | 79 | C | 4 | 13 | ✅ | 3 |

**Batch 3平均スコア**: 81.7/100

---

## 統計サマリー

### 全体統計（18ファイル）

| 指標 | 値 |
|------|---:|
| 総ファイル数 | 18 |
| 平均スコア | 83.9/100 |
| Fact Check Pass率 | 100% (18/18) |
| 平均ソース数 | 13.6件 |
| 総Null数 | 47件 |
| Nullを含むファイル | 16件 (89%) |
| 平均10x axes | 3.2軸 |

### Grade分布

| Grade | ファイル数 | 割合 |
|:-----:|----------:|-----:|
| **A** (90-100) | 4 | 22% |
| **B** (80-89) | 6 | 33% |
| **C** (70-79) | 8 | 44% |
| **D** (60-69) | 0 | 0% |
| **F** (0-59) | 0 | 0% |

### スコア範囲別

| スコア範囲 | ファイル数 |
|-----------|----------:|
| 90-100点 | 4 |
| 80-89点 | 6 |
| 70-79点 | 8 |
| 60-69点 | 0 |
| 60点未満 | 0 |

---

## 品質メトリクス評価

### ✅ 達成項目

1. **Fact Check Pass率 100%**  
   全18ファイルがFact Checkをパス、データ信頼性が高い

2. **平均ソース数13.6件**  
   目標12件以上を達成、十分なエビデンス収集

3. **平均10x axes 3.2軸**  
   複数軸での分析が行われている

4. **Grade C以上100%**  
   全ファイルが70点以上、基準品質をクリア

### ⚠️ 改善余地あり

1. **Null率89%**  
   16/18ファイルにNull値が存在、データ完全性に改善余地

2. **Grade C割合44%**  
   半数近くが79点止まり、90点超えを増やす余地あり

3. **10x axes 2軸のファイル存在**  
   PIVOT_005_jasper_ai.mdは2軸のみ、3軸以上が望ましい

---

## カテゴリ別分析

### FOUNDER系（7ファイル）

- 平均スコア: **86.4/100**
- Grade A: 4ファイル（最高品質）
- Grade B: 2ファイル
- Grade C: 1ファイル

**評価**: ✅ **優秀** - Founderストーリーは全般的に高品質

### FAILURE系（4ファイル）

- 平均スコア: **79.8/100**
- Grade B: 1ファイル
- Grade C: 3ファイル

**評価**: ⚠️ **要改善** - 失敗ケースの情報収集が他カテゴリより少ない傾向

### PIVOT系（2ファイル）

- 平均スコア: **84.0/100**
- Grade B: 2ファイル

**評価**: ✅ **良好** - ピボット事例は安定した品質

### EMERGING系（4ファイル）

- 平均スコア: **81.0/100**
- Grade B: 1ファイル
- Grade C: 3ファイル

**評価**: ⚠️ **要改善** - 新興企業は情報が少なく、Null率高い

---

## 推奨アクション

### Priority High

1. **Null値補完プロジェクト**  
   - 対象: 16ファイル（Null含む）
   - アクション: 追加リサーチで欠損データ補完
   - 期待効果: 平均スコア83.9 → 90+へ向上

2. **FAILURE系強化**  
   - 対象: FAILURE_008, 010, 011（79点）
   - アクション: 失敗要因の深掘りリサーチ
   - 期待効果: Grade C → B以上へ

### Priority Medium

3. **EMERGING系情報拡充**  
   - 対象: Character AI, Midjourney, Runway（79点）
   - アクション: 2024-2025年の最新情報追加
   - 期待効果: 時系列データ充実

4. **10x axes拡張**  
   - 対象: PIVOT_005_jasper_ai.md（2軸）
   - アクション: 追加軸（Usability, Adoption Barrier）の分析
   - 期待効果: 3軸以上達成

---

## 結論

Batch 2-3（18ファイル）は**平均スコア83.9/100、Fact Check Pass率100%**を達成し、
**品質基準を満たし、Stock移行可能**と判定します。

**Grade A（22%）、Grade B（33%）、Grade C（44%）**の分布は健全であり、
Founder Research プロジェクトの高い研究品質を示しています。

Null率89%の改善により、平均スコア90+への向上が見込まれます。
次回バッチではNull補完を優先事項として実施を推奨します。

---

**生成日時**: 2025-12-31  
**統合元ファイル**:  
- quality_scores_batch2_3.txt
- batch2_3_quality_scores_final.txt

**移行先**: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Research/analysis/quality_reports.md
