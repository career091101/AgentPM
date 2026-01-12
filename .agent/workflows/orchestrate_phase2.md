---
description: Phase2（PMF達成）を自律オーケストレーションする
---
# Phase2 オーケストレーター

Phase1（MVP公開）完了後、PMF（Product-Market Fit）達成までを自律的に実行するマスターワークフロー。

> [!IMPORTANT]
> **起業の科学の教え**: PMFは「顧客が熱狂し、自動的に口コミが広がる状態」
> Sean Ellisテストで「非常に残念」40%以上がゴール

## 概要

```text
┌─────────────────────────────────────────────────────────────────────┐
│  Phase2 オーケストレーション フロー v1.0                             │
├─────────────────────────────────────────────────────────────────────┤
│  1.   実顧客インタビュー準備  → interview_guide.md                  │
│  2.   プロダクト改善サイクル  → improvement_log.md                  │
│  3.   /manage_customer_success → customer_success.md                │
│  4.   リテンション分析       → retention_analysis.md               │
│  5.   NPS測定               → nps_report.md                        │
│  6.   Sean Ellisテスト      → sean_ellis_test.md                   │
│  7.   /diagnose_pmf         → pmf_diagnosis.md                     │
│       └─ ❌未達成 → 改善サイクルへ戻る                              │
│  8.   /build_flywheel       → flywheel.md（本格版）                │
│  9.   /prevent_premature_scaling → premature_scaling_check.md      │
│  10.  Phase2完了報告        → phase2_completion.md                 │
└─────────────────────────────────────────────────────────────────────┘
```

## 前提条件

- Phase1完了（MVP公開済み）
- 実ユーザーが存在する
- 最低限のトラクションがある

---

## STEP 1: 実顧客インタビュー準備【必須】

```text
ツール: /generate_interview_guide を実行
入力: Phase1の成果物
出力: {IDEA_FOLDER}/documents/4_executing/interview_guide.md
```

**目的**: 20人以上の実顧客インタビューを計画・実施

**完了条件**:
- インタビュー計画が完成
- 質問リストが準備されている
- 記録テンプレートが用意されている

> [!WARNING]
> **Phase2の核心**: 仮想インタビューでは不十分。
> 実顧客の生の声なしにPMFは達成できません。

---

## STEP 2: プロダクト改善サイクル【反復】

```markdown
## 改善サイクル（週次）

### Step 2.1: フィードバック収集
- ユーザーインタビュー結果
- サポート問い合わせ分析
- 行動ログ分析
- NPS/CSATコメント

### Step 2.2: 課題優先順位付け
| 課題 | 影響度 | 緊急度 | 対応難易度 | 優先度 |
|------|:------:|:------:|:---------:|:------:|
| [課題1] | 高/中/低 | 高/中/低 | 高/中/低 | [順位] |

### Step 2.3: 改善実装
- 週次リリースサイクル
- 小さく素早く検証

### Step 2.4: 効果測定
- リリース前後の指標比較
- ユーザーフィードバック確認
```

**出力**: `{IDEA_FOLDER}/documents/4_executing/improvement_log.md`

---

## STEP 3: カスタマーサクセス設計【PMF前でも開始】

```text
ツール: /manage_customer_success を実行
入力: persona.md, 顧客データ
出力: {IDEA_FOLDER}/documents/4_executing/customer_success.md
```

**目的**: DEARモデルでヘルススコアを設計し、チャーンを防止

---

## STEP 4: リテンション分析【週次】

```markdown
## リテンション分析

### コホート分析
| 契約月 | Week1 | Week2 | Week4 | Week8 | Week12 |
|--------|:-----:|:-----:|:-----:|:-----:|:------:|
| [月1] | 100% | [%] | [%] | [%] | [%] |
| [月2] | 100% | [%] | [%] | [%] | - |

### 40%ルール判定
- **目標**: 長期リテンション率 40%以上で平坦化
- **現状**: [X]%
- **トレンド**: 📈/➡️/📉

### 離脱分析
| 離脱タイミング | 割合 | 主な理由 | 対策 |
|--------------|:----:|---------|------|
| Week 1 | [%] | [理由] | [対策] |
| Week 2-4 | [%] | [理由] | [対策] |
```

**出力**: `{IDEA_FOLDER}/documents/5_monitoring/retention_analysis.md`

---

## STEP 5: NPS測定【月次】

```markdown
## NPS測定

### 質問
「このプロダクトを友人や同僚に薦める可能性は？（0-10点）」

### 結果
| カテゴリ | スコア範囲 | 人数 | 割合 |
|---------|:---------:|:----:|:----:|
| 推奨者（Promoter） | 9-10 | [数] | [%] |
| 中立者（Passive） | 7-8 | [数] | [%] |
| 批判者（Detractor） | 0-6 | [数] | [%] |

### NPS計算
```
NPS = 推奨者% - 批判者% = [X]
```

### 判定
- **目標**: NPS 40以上
- **現状**: [X]
```

**出力**: `{IDEA_FOLDER}/documents/5_monitoring/nps_report.md`

---

## STEP 6: Sean Ellisテスト【月次】

```markdown
## Sean Ellisテスト

### 質問
「このプロダクトが使えなくなったらどう思いますか？」

### 結果
| 回答 | 人数 | 割合 |
|-----|:----:|:----:|
| 非常に残念 | [数] | [%] |
| やや残念 | [数] | [%] |
| 残念ではない | [数] | [%] |
| もう使っていない | [数] | [%] |

### 判定
- **PMF基準**: 「非常に残念」40%以上
- **現状**: [X]%
- **判定**: ✅PMF達成 / ❌PMF未達成

### 「非常に残念」回答者の共通点分析
| 属性 | 共通点 |
|------|--------|
| 業種 | [共通点] |
| 規模 | [共通点] |
| 利用頻度 | [共通点] |
| 利用機能 | [共通点] |
```

**出力**: `{IDEA_FOLDER}/documents/5_monitoring/sean_ellis_test.md`

---

## STEP 7: PMF達成判定【ゲート】

```text
ツール: /diagnose_pmf を実行
入力: 全Phase2成果物
出力: {IDEA_FOLDER}/documents/5_monitoring/pmf_diagnosis.md
```

### 判定ロジック

| 結果 | 条件 | 次のアクション |
|------|------|--------------| 
| ✅ PMF達成 | 5項目中4項目以上達成 | STEP 8へ進行 |
| ⚠️ PMF達成間近 | 5項目中2-3項目達成 | 改善サイクル継続 |
| ❌ PMF未達成 | 5項目中1項目以下 | ピボット検討 or 継続 |

> [!CAUTION]
> **PMF未達成の場合**: STEP 2-6を繰り返す
> 3ヶ月改善しても達成できない場合は `/decide_pivot` を検討

---

## STEP 8: フライホイール本格設計【PMF達成後】

```text
ツール: /build_flywheel を実行（本格版）
入力: PMF達成時の成功パターン
出力: {IDEA_FOLDER}/documents/3_planning/flywheel_v2.md
```

**目的**: PMFで発見した成功パターンを持続的成長の仕組みに

---

## STEP 9: スケール前チェック【PMF達成後】

```text
ツール: /prevent_premature_scaling を実行
入力: 事業・組織状況
出力: {IDEA_FOLDER}/documents/5_monitoring/premature_scaling_check.md
```

**目的**: スケールに入る前の最終健全性チェック

---

## STEP 10: Phase2完了報告【自動実行】

```markdown
# Phase2 完了レポート

**完了日時**: [日時]
**所要期間**: [期間]

## PMF達成状況

| 指標 | 目標 | 達成値 | 判定 |
|------|------|--------|:----:|
| Sean Ellisテスト | 40%+ | [X]% | ✅/❌ |
| リテンション（40%ルール） | 40%+ | [X]% | ✅/❌ |
| NPS | 40+ | [X] | ✅/❌ |
| 口コミ獲得 | あり | [状況] | ✅/❌ |
| LTV/CAC | 3+ | [X] | ✅/❌ |

## 成功パターン
[PMFに至った要因分析]

## Phase3への推奨事項
- スケール戦略
- 組織拡大計画
- 資金調達計画
```

**出力**: `{IDEA_FOLDER}/documents/5_monitoring/phase2_completion.md`

---

## 完了条件

- [ ] 実顧客インタビューを20人以上実施した
- [ ] 改善サイクルを最低3回実施した
- [ ] カスタマーサクセスを設計した
- [ ] リテンション分析を実施した
- [ ] NPSを測定した
- [ ] Sean Ellisテストを実施した
- [ ] PMF診断を実施した
- [ ] Phase2完了レポートを作成した

---

**出典**: 田所雅之「起業の科学」「起業大全」
