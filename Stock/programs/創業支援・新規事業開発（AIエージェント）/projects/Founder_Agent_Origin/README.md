# Founder Agent - Origin（オリジン版）

**バージョン**: 1.0
**最終更新**: 2025-12-30
**ベース**: 起業の科学（田所雅之著）

---

## 概要

Founder Agent Originは、「起業の科学」の体系的フレームワークをベースとした、ビジネスアイデア検証の基本版です。CPF（Customer Problem Fit）→ PSF（Problem Solution Fit）→ PMF（Product Market Fit）の段階的検証プロセスを自動化します。

---

## 対象ユーザー

- スタートアップ創業者（全般）
- 初めて起業する方
- 体系的なフレームワークで検証したい方
- 19フレームワークを活用したい方

---

## 主な機能

### 1. Phase1全自動実行（orchestrate-phase1）

**所要時間**: 3-6時間
**12ステップ**:
1. 需要発見リサーチ
2. MVV早期定義
3. リーンキャンバス作成
4. フライホイール設計
5. Web課題発見
6. 仮想ペルソナインタビュー
7. CPF診断（ステージゲート1）
8. 10倍優位性検証
9. LP構築
10. PSF診断（ステージゲート2）
11. SNSコンテンツ作成
12. 最終評価（スコアカード）

### 2. ステージゲート管理

**CPFステージゲート**:
- 総合スコア60%以上（推奨80%以上）
- 3U各項目8点以上
- インタビュー20人以上

**PSFステージゲート**:
- 10倍優位性2軸以上（推奨3軸以上）
- MVP類型選定完了
- UVP刺さり度28/40以上（推奨35/40以上）

### 3. 19フレームワーク統合

**ステージ別フレームワーク**:
- Idea: FIF、5つの眼、MVV
- CPF: ペルソナ、3U、顧客インタビュー
- PSF: 10倍検証、MVP10類型、UVPキャンバス
- PMF: NPS、Retention、AARRR
- Scale: Unit Economics、DEAR、Balance Scorecard

---

## ディレクトリ構造

```
Founder_Agent_Origin/
├── documents/          # 成果物
│   ├── 1_initiating/
│   ├── 2_discovery/
│   ├── 3_planning/
│   ├── 4_executing/
│   └── 5_monitoring/
├── mvp/                # MVP関連
│   ├── lp/
│   └── sns_contents/
├── system_prompts/     # システムプロンプト
│   ├── 01_orchestrator_prompt.md
│   ├── 02_executor_prompt.md
│   ├── 03_reviewer_peter_thiel_prompt.md
│   ├── 04_reviewer_yc_prompt.md
│   ├── 05_reviewer_startup_science_prompt.md
│   ├── 06_gatekeeper_prompt.md
│   └── 07_updater_prompt.md
└── README.md (このファイル)
```

---

## 使用方法

### 基本フロー

```bash
# Phase1全自動実行
/orchestrate-phase1

# 個別検証
/validate-cpf    # CPF検証
/validate-psf    # PSF検証
/validate-pmf    # PMF検証

# フレームワーク適用
/apply-lean-canvas        # リーンキャンバス作成
/create-mvv               # MVV定義
/build-flywheel           # フライホイール設計
/validate-10x             # 10倍優位性検証
```

### 成果物の確認

```bash
# スコアカード（総合評価）
documents/5_monitoring/scorecard.md

# CPF診断結果
documents/3_planning/cpf_diagnosis.md

# PSF診断結果
documents/3_planning/psf_diagnosis.md

# リーンキャンバス
documents/2_discovery/lean_canvas.md
```

---

## 派生バリアント

Originをベースに、ドメイン特化版が4つ存在します：

| バリアント | 特化領域 | 主な違い |
|-----------|---------|---------|
| **ForStartup** | VC調達・スケールアップ | CPF基準厳格化（70%）、10倍3軸必須 |
| **ForRecruit** | 企業内新規事業 | CPF基準緩和（50%）、社内リソース活用 |
| **ForSolo** | ソロプレナー | コスト最小化、利益率重視 |
| **ForGenAI** | 生成AIプロダクト | 最新技術即時反映、Product Hunt戦略 |

---

## 評価基準

### スコアカード（40点満点）

| 評価項目 | 配点 | 合格基準 |
|---------|------|---------|
| 市場機会 | 8点 | 6点以上 |
| 課題の切実度（CPF） | 8点 | 6点以上 |
| ソリューション（PSF） | 8点 | 6点以上 |
| ビジネスモデル | 6点 | 4点以上 |
| 実行可能性 | 6点 | 4点以上 |
| 独自性・競争優位 | 4点 | 3点以上 |

**判定**:
- 32-40点: ✅ Phase1完了 → Phase2へ進む
- 20-31点: ⚠️ 要改善 → 低スコア視点を改善後、再評価
- 0-19点: ❌ 要再実行 → Phase1を最初からやり直し

---

## テスト結果（2025-12-29）

### test_idea_001

- **CPFスコア**: 72%（✅ 合格: 60%以上）
- **PSFスコア**: 88%（✅ 合格: 80%以上）
- **10倍優位性**: 3軸達成（✅ 合格: 2軸以上）
- **総合スコア**: 35/40点（✅ Phase1完了）

**検証結果**: Founder Agent Originは実用レベルで動作することを確認

---

## 参考リソース

### 起業の科学フレームワーク

**Base Path**:
`/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/startup_science/`

**主要ドキュメント**:
- `_index/master_index.md` - 19フレームワーク一覧
- `_index/cross_reference.md` - 依存関係
- `01_stages/` - ステージ別概念（CPF, PSF, PMF）
- `02_frameworks/` - 横断的フレームワーク
- `03_tactics/` - 実践戦術

### AgentSkills

**Base Path**:
`/Users/yuichi/AIPM/aipm_v0/.claude/skills/`

**主要スキル**:
- `orchestrate-phase1/` - Phase1統括
- `validate-cpf/`, `validate-psf/`, `validate-pmf/` - 各ステージ検証
- `discover-demand/`, `create-mvv/`, `build-flywheel/` - 個別スキル

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2025-12-30 | 1.0 | 初版作成（基盤構築フェーズ） |

---

## ライセンス

このエージェントは「起業の科学」（田所雅之著）の体系的フレームワークをベースにしています。
