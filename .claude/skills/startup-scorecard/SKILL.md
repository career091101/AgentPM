---
name: startup-scorecard
description: |
  スタートアップの健全性を4視点で評価するスコアカード作成スキル。Financial（財務）/Customer（顧客）/Internal Process（業務プロセス）/Learning & Growth（学習・成長）の4視点を各10点評価（計40点満点）。Phase1完了度を判定し、弱点特定・改善案提示、ステージ判定（CPF/PSF/PMF）、次のアクションを明確化します。

  使用タイミング：
  - Phase1完了時の総合評価
  - 現状の健全性を確認したい
  - 次のアクションを明確化したい

  所要時間：20-40分（自動実行）
  出力：scorecard.md
---

# Startup Scorecard Skill

スタートアップの健全性を4視点で評価するスコアカード作成Skill。

---

## このSkillでできること

1. **4視点評価**: Financial/Customer/Internal Process/Learning & Growthを各10点評価
2. **総合判定**: 40点満点でPhase1の健全性を判定
3. **弱点特定**: スコアが低い視点を特定し改善案を提示
4. **ステージ判定**: CPF/PSF/PMFのどのステージにいるか判定
5. **次のアクション提案**: 次に何をすべきかを明確化

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 全成果物（`documents/`, `mvp/`） |
| **出力** | `Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/5_monitoring/scorecard.md` |
| **次のSkill** | `/orchestrate-phase1`（再実行） or Phase2へ |

---

## Instructions

**実行モード**: 自律実行（対話なし）
**推定所要時間**: 20-40分

### 自動実行ステップ

1. 全成果物の存在確認
2. Financial視点評価（10点）
3. Customer視点評価（10点）
4. Internal Process視点評価（10点）
5. Learning & Growth視点評価（10点）
6. 総合判定（40点満点）
7. 弱点特定・改善案提示
8. ステージ判定（CPF/PSF/PMF）
9. 次のアクション提案
10. 成果物出力

### 4視点評価基準（Phase1）

**Financial視点（10点満点）**:
- 価格設定の妥当性（4点）
- 収益モデルの明確性（3点）
- コスト構造の把握（3点）

**Customer視点（10点満点）**:
- ペルソナの明確性（3点）
- 課題の裏付け（3U）（4点）
- UVPの刺さり度（3点）

**Internal Process視点（10点満点）**:
- フライホイール設計（3点）
- MVP選定・構築（4点）
- 10倍優位性の確認（3点）

**Learning & Growth視点（10点満点）**:
- ドキュメント整備（4点）
- 仮説検証サイクル（3点）
- 改善アクションの実行（3点）

### 判定基準

**総合判定**:
- 32-40点: ✅ 健全 → Phase2（CPF検証実施）へ進む
- 20-31点: ⚠️ 要改善 → 低スコア視点を改善
- 0-19点: ❌ 要見直し → Phase1を再実行

**ステージ判定**:
- CPF: Customer視点 ≥ 6点
- PSF: Internal Process視点 ≥ 6点
- PMF: Financial視点 ≥ 6点 + 実績データあり

---

## エラーハンドリング

### データ検証失敗時のGraceful Degradation

**適用パターン**: Validation + Graceful Degradation

**必須項目チェック**:
- [ ] Financial視点データ（価格設定、収益モデル、コスト構造）
- [ ] Customer視点データ（ペルソナ、課題裏付け、UVP）
- [ ] Internal Process視点データ（フライホイール、MVP、10倍優位性）
- [ ] Learning & Growth視点データ（ドキュメント整備、仮説検証サイクル）

**判定ロジック**:

| 必須項目充足率 | 対応 |
|-------------|------|
| 100% | 通常スコアカード評価、40点満点 |
| 75-99% | 警告表示 + 部分スコアカード評価 + 続行 |
| <75% | エラー報告 + 停止 |

**警告表示例** (75-99%):
```yaml
status: warning
message: "フライホイール設計が存在しません。Internal Process視点の評価精度が低下します。"
partial_score: true
missing_data: ["flywheel.md"]
available_perspectives: ["Financial", "Customer", "Learning & Growth"]
unavailable_perspectives: ["Internal Process（部分評価）"]
action: "部分スコアカード評価継続"
recommendation: "/build-flywheel を実行してフライホイールを設計することを推奨"
```

**エラー報告例** (<75%):
```yaml
status: error
error_code: VALIDATION_ERROR
message: "スコアカード評価に必要な成果物が不足しています（充足率: 60%）"
skill_name: "/startup-scorecard"
step: "STEP 1: 全成果物の存在確認"
timestamp: "2026-01-01 16:00:00"
details:
  missing_files:
    - "persona.md"
    - "lean_canvas.md"
    - "cpf_judgment.md"
  sufficiency_rate: "60%"
action: "Human-in-the-Loop"
next_steps:
  - "Phase1の成果物を作成してください（/orchestrate-phase1）"
  - "または個別スキルを実行してください"
  - "完了後、/startup-scorecard を再実行してください"
```

### ファイル読み込み失敗時のフォールバック戦略

**フォールバック階層**:

```markdown
**STEP 1: 全成果物の存在確認**

**視点1: Financial（10点満点）**
- 必須: lean_canvas.md（Revenue Streams/Cost Structure）
- フォールバック: mvv.md、demand_discovery.md
- 全失敗 → 0点（警告表示）

**視点2: Customer（10点満点）**
- 必須: persona.md, cpf_judgment.md, problem_research.md
- フォールバック: demand_discovery.md
- 全失敗 → エラー報告（最重要視点のため）

**視点3: Internal Process（10点満点）**
- 必須: flywheel.md, 10x_validation.md, lean_canvas.md（Solution）
- フォールバック: mvv.md
- 全失敗 → 0点（警告表示）

**視点4: Learning & Growth（10点満点）**
- 必須: documents/フォルダ内のファイル一覧
- フォールバック: なし（ドキュメント数のカウントのみ）
- 全失敗 → 部分評価（改善アクション有無のみ）
```

### 標準エラーレスポンス形式

**エラー1: Customer視点データ欠落時**

```markdown
## ❌ エラー発生

**スキル**: `/startup-scorecard`
**ステップ**: STEP 2: Customer視点評価
**時刻**: 2026-01-01 16:00:22

### エラー内容
スコアカード評価に必要なCustomer視点データが存在しません。

### 欠落ファイル
- ❌ `persona.md` - ペルソナ定義（必須）
- ❌ `cpf_judgment.md` - CPF判定結果（必須）
- ❌ `problem_research.md` - 課題裏付け（必須）

### 試みた操作
- persona.md 読み込み → ❌ 存在しない
- cpf_judgment.md 読み込み → ❌ 存在しない
- フォールバック: demand_discovery.md → ❌ 存在しない

### 次のアクション
1. `/create-persona` を実行してペルソナを作成してください
2. `/simulate-interview` を実行してインタビューを実施してください
3. `/validate-cpf` を実行してCPF判定を実施してください
4. 完了後、`/startup-scorecard` を再実行してください

---
**エラーコード**: VALIDATION_ERROR
**サポート**: `.claude/skills/_shared/error_handling_patterns.md#3-データ検証失敗`
```

**エラー2: 総合スコアが基準未達時**

```markdown
## ⚠️ Human-in-the-Loop: ユーザー判断が必要です

**状況**: スコアカード基準未達

### 現在の状態
- 総合スコア: 25/40点（62.5%）
- 判定: ⚠️ 要改善

### スコア詳細
| 視点 | スコア | 評価 |
|------|:------:|:----:|
| Financial | 5/10点 | ⚠️ 要改善 |
| Customer | 8/10点 | ✅ 良好 |
| Internal Process | 6/10点 | ⚠️ 要改善 |
| Learning & Growth | 6/10点 | ⚠️ 要改善 |

### 低スコア項目の詳細

#### Financial視点（5/10点）
- 価格設定の妥当性: 2/4点（競合価格との比較が不十分）
- 収益モデルの明確性: 1/3点（マネタイズ戦略が曖昧）
- コスト構造の把握: 2/3点（固定費/変動費の試算あり）

#### Internal Process視点（6/10点）
- フライホイール設計: 2/3点（完全性に課題）
- MVP選定・構築: 2/4点（未構築）
- 10倍優位性の確認: 2/3点（1軸のみ達成）

### 推奨アクション（選択肢）
1. **Financial視点を改善** （優先度高）
   - 価格設定の根拠を明確化（競合比較、WTP分析）
   - 収益モデルを詳細化（月次売上予測）
   - 推定時間: 1-2時間
   - 期待効果: スコア 25点→30点

2. **Internal Process視点を改善** （優先度中）
   - フライホイールの完全性を修正
   - 10倍優位性を2軸以上に拡大
   - 推定時間: 1.5-2.5時間
   - 期待効果: スコア 25点→31点

3. **両方を改善** （推奨）
   - Financial + Internal Processを並行実施
   - 推定時間: 2-4時間
   - 期待効果: スコア 25点→35点+ → Phase2へ進行可能

4. **条件付きで進行**
   - リスク: Phase2で失敗する可能性30%
   - 推定時間: そのまま継続（1-2時間）

### どの選択肢を選びますか？
（番号で回答してください: 1/2/3/4）
```

### Human-in-the-Loop トリガー条件

以下のケースで自動停止し、ユーザー判断を仰ぐ：

1. **Customer視点データ欠落**
   - persona.md、cpf_judgment.md、problem_research.mdのすべてが存在しない
   - → エラー報告（最重要視点のため）

2. **データ充足率 <75%**
   - 4視点の必須項目の75%未満しか揃っていない
   - → エラー報告

3. **総合スコア 20-31点（要改善）**
   - 40点満点中20-31点
   - → Human-in-the-Loop（改善アクション提示）

4. **総合スコア 0-19点（要見直し）**
   - 40点満点中19点以下
   - → Human-in-the-Loop（Phase1再実行推奨）

5. **個別視点が極端に低い**
   - いずれかの視点が3点以下（10点満点）
   - → Human-in-the-Loop（該当視点の再設計推奨）

### 期待効果

- **エラー原因特定時間**: 15分 → 3分
- **データ検証エラー**: 20% → 5%
- **スコア未達時の次アクション明確化**: 0% → 100%
- **不要なPhase2進行の防止**: 100%

---

## Knowledge Base参照

- バランススコアカード: `@startup_science/02_frameworks/balance_scorecard/scorecard_overview.md`
- CPF概念: `@startup_science/01_stages/cpf/cpf_overview.md`
- PSF概念: `@startup_science/01_stages/psf/psf_overview.md`
- PMF概念: `@startup_science/01_stages/pmf/pmf_overview.md`
- **エラーハンドリング**: `.claude/skills/_shared/error_handling_patterns.md`
