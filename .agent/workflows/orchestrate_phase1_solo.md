---
description: Phase1全体を自動オーケストレーションし、MVP公開まで完全自律実行する（ソロプレナー版）
---
# Phase1 オーケストレーター（SolopreneurAgent版）

個人開発者・副業起業家向けのPhase1オーケストレーション。Solopreneur_Researchの事例を参照しながらMVP公開まで自律実行する。

## 概要

FounderAgentの `/orchestrate_phase1` をベースに、以下の拡張を加えたソロプレナー特化版：

1. **7ステップで事例参照** - Solopreneur_Researchから関連事例を自動参照
2. **収益目標の現実化** - 月100万円〜をターゲットに設定
3. **出力先の分離** - `projects/solo_ideas/` に出力
4. **専用ワークフロー追加** - 事例参照/マーケ戦略/収益計算

```text
┌─────────────────────────────────────────────────────────────────────┐
│  SolopreneurAgent Phase1 フロー v1.0                                │
├─────────────────────────────────────────────────────────────────────┤
│  0.   /five_perspectives       → 5つの眼分析                        │
│  0.5  /discover_demand         → 需要発見（任意）                   │
│  1.   /discover_idea           → アイデア発見【事例参照①】          │
│  1.2  /validate_founder_fit    → Founder Fit検証                   │
│  1.5  /create_mvv              → MVV定義                           │
│  2.   /create_lean_canvas    → リーンキャンバス【事例参照②】        │
│  2.3  /calculate_solo_economics → 収益シミュレーション【NEW】       │
│  2.5  /build_flywheel        → フライホイール【事例参照③】          │
│  3.   /define_persona        → ペルソナ定義                         │
│  4.   /validate_problem      → 課題検証                             │
│  4.3  /research_problem      → Web課題発見                          │
│  4.5  /simulate_interview    → 仮想インタビュー                     │
│  5.   /diagnose_cpf          → CPF判定                              │
│  5.5  /validate_10x          → 10倍検証【事例参照④】                │
│  6.   /diagnose_psf          → PSF判定                              │
│  7.   /build_lp              → LP構築【事例参照⑤】                  │
│  8.   /deploy_mvp            → デプロイ（スキップ可）               │
│  9.   /create_sns_content    → SNSコンテンツ                        │
│  9.5  /plan_solo_marketing   → ソロマーケ戦略【事例参照⑥・NEW】     │
│  10.  完了報告               → phase1_completion.md                 │
│  10.5 /startup_scorecard     → スコアカード【事例参照⑦】            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 前提条件

- Solopreneur_Research のデータが存在すること
  - `Solo_App/case_studies/` - 事例研究
  - `Solo_SNS/sns_targets_list.md` - SNS成功者リスト
  - `Solo_Newsletter/` - ニュースレター戦略

---

## アイデアフォルダ管理

### フォルダ構造（solo_ideas/）

```text
projects/solo_ideas/
├── index.md                    ← アイデア一覧
└── {id}_{name}/               ← アイデア単位フォルダ
    ├── metadata.yaml          ← ソロ用メタ情報
    ├── README.md
    ├── documents/
    │   ├── 1_initiating/
    │   ├── 2_discovery/
    │   ├── 3_planning/
    │   ├── 4_executing/
    │   ├── 5_monitoring/
    │   └── references/        ← 事例参照レポート【NEW】
    └── mvp/
```

### パス変数

| 変数 | 説明 | 例 |
|------|------|----| 
| `{SOLO_IDEA_FOLDER}` | アイデアフォルダのフルパス | `projects/solo_ideas/001_micro-saas` |
| `{RESEARCH_BASE}` | Solopreneur_Researchのパス | `projects/Solopreneur_Research/documents` |

---

## 実行手順

### STEP -1: アイデアフォルダ初期化
// turbo
```text
処理:
  1. solo_ideas/ 内の既存フォルダから次のIDを自動採番
  2. _templates/solo_idea_template/ からコピー
  3. metadata.yaml にソロプレナー用設定（target_mrr=1000000等）
出力:
  - {SOLO_IDEA_FOLDER}/metadata.yaml
  - {SOLO_IDEA_FOLDER}/README.md
  - {SOLO_IDEA_FOLDER}/documents/references/ ← 事例参照用
```

---

### STEP 1: アイデア発見【事例参照①】
// turbo
```text
ツール: /discover_idea を実行
追加処理:
  /reference_solo_cases category=product keywords="{探索分野}"
  → Solo_App から成功プロダクトカテゴリを参照
  → 「日本市場適用性スコア」が高い分野を優先提案
出力: {SOLO_IDEA_FOLDER}/documents/2_discovery/business_idea.md
       {SOLO_IDEA_FOLDER}/documents/references/solo_cases_product.md
```

**事例参照のポイント**:
- Pieter Levels, Marc Lou 等の成功プロダクト分野を参考
- 失敗プロダクト一覧から「避けるべきパターン」を学習

---

### STEP 2: リーンキャンバス【事例参照②】
// turbo
```text
ツール: /create_lean_canvas を実行
追加処理:
  /reference_solo_cases category=revenue keywords="{プロダクト種別}"
  → 収益モデル・チャネルの成功パターンを参照
出力: {SOLO_IDEA_FOLDER}/documents/2_discovery/lean_canvas.md
       {SOLO_IDEA_FOLDER}/documents/references/solo_cases_revenue.md
```

**事例参照のポイント**:
- サブスク vs 買い切り vs フリーミアムの選定参考
- 価格帯設定の参考値

---

### STEP 2.3: 収益シミュレーション【NEW】
// turbo
```text
ツール: /calculate_solo_economics を実行
入力: target_mrr=1000000, product_type={from lean_canvas}
出力: {SOLO_IDEA_FOLDER}/documents/3_planning/solo_economics.md
```

---

### STEP 2.5: フライホイール設計【事例参照③】
// turbo
```text
ツール: /build_flywheel を実行
追加処理:
  /reference_solo_cases category=growth keywords="成長戦略,リード獲得"
  → ニュースレター成長戦略から参照
出力: {SOLO_IDEA_FOLDER}/documents/2_discovery/flywheel.md
       {SOLO_IDEA_FOLDER}/documents/references/solo_cases_growth.md
```

---

### STEP 3-4.5: 標準フロー（事例参照なし）
// turbo
```text
以下は従来FounderAgentと同じ:
  - STEP 3: /define_persona
  - STEP 4: /validate_problem
  - STEP 4.3: /research_problem
  - STEP 4.5: /simulate_interview
  - STEP 5: /diagnose_cpf
```

---

### STEP 5.5: 10倍優位性検証【事例参照④】
// turbo
```text
ツール: /validate_10x を実行
追加処理:
  /reference_solo_cases category=product keywords="{競合分野}"
  → Solo_App の類似プロダクトをベンチマーク対象に
出力: {SOLO_IDEA_FOLDER}/documents/2_discovery/10x_validation.md
       → 参照レポートは既存のsolo_cases_product.mdを更新
```

---

### STEP 6: PSF判定（標準）
// turbo

---

### STEP 7: LP構築【事例参照⑤】
// turbo
```text
ツール: /build_lp を実行
追加処理:
  Solo_App成功事例のLPパターンを参照
  → 成功LPの共通要素（ヒーローセクション、UVP配置等）
出力: {SOLO_IDEA_FOLDER}/mvp/lp/
```

---

### STEP 9: SNSコンテンツ作成
// turbo
```text
ツール: /create_sns_content を実行
出力: {SOLO_IDEA_FOLDER}/mvp/sns_contents/
```

---

### STEP 9.5: ソロマーケ戦略【事例参照⑥・NEW】
// turbo
```text
ツール: /plan_solo_marketing を実行
入力: product_category={from lean_canvas}
追加処理:
  /reference_solo_cases category=marketing keywords="{プラットフォーム}"
  → Solo_SNS から成功者の戦略を参照
出力: {SOLO_IDEA_FOLDER}/documents/4_executing/solo_marketing_strategy.md
       {SOLO_IDEA_FOLDER}/documents/references/solo_cases_marketing.md
```

---

### STEP 10: 完了報告
// turbo
```text
出力: {SOLO_IDEA_FOLDER}/documents/4_executing/phase1_completion.md

内容（追加項目）:
  ## 参照した成功事例
  - プロダクト: {事例名}
  - マーケティング: {成功者名}
  - 収益モデル: {参考事例}
  
  ## ソロプレナー収益目標
  - 目標MRR: ¥1,000,000
  - 必要有料ユーザー: XX人
  - 推奨価格: $XX/月
```

---

### STEP 10.5: スコアカード【事例参照⑦】
// turbo
```text
ツール: /startup_scorecard を実行
追加処理:
  ソロプレナー収益ベンチマークを参照
  → 月100万円 / 月300万円 / 月1000万円 の目標設定
出力: {SOLO_IDEA_FOLDER}/documents/5_monitoring/scorecard.md
```

---

## 7ステップ事例参照サマリー

| # | ステップ | 参照カテゴリ | 参照データ | 出力 |
|---|---------|-------------|-----------|------|
| 1 | アイデア発見 | product | Solo_App | solo_cases_product.md |
| 2 | リーンキャンバス | revenue | Solo_App + Newsletter | solo_cases_revenue.md |
| 3 | フライホイール | growth | Newsletter戦略 | solo_cases_growth.md |
| 4 | 10倍検証 | product | Solo_App | (既存更新) |
| 5 | LP構築 | product | Solo_App | (参照のみ) |
| 6 | ソロマーケ戦略 | marketing | Solo_SNS | solo_cases_marketing.md |
| 7 | スコアカード | - | Solo_App収益 | (ベンチマーク参照) |

---

## 従来FounderAgentとの差分

| 項目 | FounderAgent | SolopreneurAgent |
|------|--------------|------------------|
| 出力先 | projects/ideas/ | projects/solo_ideas/ |
| 事例参照 | なし | 7ステップで参照 |
| 収益目標 | 年商1億円〜 | 月100万円〜 |
| 専用ワークフロー | なし | 3件追加 |
| ターゲット | CxO/新規事業担当 | 個人開発者/副業起業家 |

---

## 実行コマンド

```
/orchestrate_phase1_solo
```

---

## 変更履歴

| バージョン | 日付 | 変更内容 |
|-----------|------|---------|
| v1.0 | 2025-12-26 | 初版作成（FounderAgent v2.4ベース + ソロプレナー拡張） |
