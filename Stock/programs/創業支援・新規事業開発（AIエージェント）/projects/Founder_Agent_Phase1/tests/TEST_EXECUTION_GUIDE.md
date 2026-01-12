# 統合テスト実行ガイド

## 概要

Orchestrator × orchestrate_phase1 統合実装の動作確認を3段階で実施します。

---

## 事前準備

### 1. ファイル確認

以下の6ファイルが最新版であることを確認：

- [x] `AgentSkills.md` (27ルール、10セクション)
- [x] `system_prompts/01_orchestrator_prompt.md` (Phase1統合モード追加)
- [x] `system_prompts/02_executor_prompt.md` (ステップ別実行追加)
- [x] `system_prompts/06_gatekeeper_prompt.md` (フェーズゲート追加)
- [x] `system_prompts/07_updater_prompt.md` (10セクション対応)
- [x] `system_prompts/08_orchestrate_phase1_controller.md` (新規作成)

### 2. テスト環境準備

```bash
# テストディレクトリ作成
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1

# tests ディレクトリ確認
ls tests/
# 期待: test_cases.md, test_input_executor_step2.yaml, TEST_EXECUTION_GUIDE.md

# test_ideas ディレクトリ作成
mkdir -p tests/test_ideas/test_idea_001
mkdir -p tests/test_ideas/test_idea_cpf_001
```

---

## Test 1: Executor単体テスト（15分）

### 目的
Executorがステップ別実行モードでリーンキャンバスを生成できるか確認

### 実行方法（Antigravity）

```bash
# Antigravityでワークフロー実行
antigravity run /create_lean_canvas \
  --context "中小企業向けAI営業支援ツール" \
  --agent-skills AgentSkills.md
```

### 実行方法（Claude Code）

Claude Codeでマルチエージェントとして実行する場合：

1. **Executorエージェント起動**
   ```
   system_prompts/02_executor_prompt.md を参照
   ```

2. **入力データ渡し**
   ```yaml
   mode: "step_by_step"
   step_name: "STEP_2"
   context: (test_input_executor_step2.yaml参照)
   ```

3. **実行コマンド（疑似）**
   ```
   "AgentSkills.mdの27ルールを遵守して、
   中小企業向けAI営業支援ツールのリーンキャンバスを作成してください。
   STEP_2（/create_lean_canvas）を実行します。"
   ```

### 検証手順

1. **生成ファイル確認**
   ```bash
   # ファイル存在確認
   ls tests/test_ideas/test_idea_001/documents/2_discovery/lean_canvas.md
   ```

2. **内容チェック（test_cases.md参照）**
   - [ ] リーンキャンバス9ブロック全て存在
   - [ ] TAM/SAM/SOM記載（数値あり）
   - [ ] CAGR記載
   - [ ] ペルソナに1日の行動タイムライン
   - [ ] 課題が3U+1形式
   - [ ] 既存代替案3つ以上
   - [ ] UVP一文 + 「なぜ今か」
   - [ ] MVP種類明記
   - [ ] 10倍改善軸（数値）
   - [ ] マネタイズモデル
   - [ ] 北極星指標

3. **結果記録**
   ```bash
   # 結果をtest_results.mdに記録
   echo "## Test 1: Executor単体テスト" >> tests/test_results.md
   echo "- 実行日時: $(date)" >> tests/test_results.md
   echo "- 結果: PASS/FAIL" >> tests/test_results.md
   echo "- チェックリスト: X/14項目" >> tests/test_results.md
   ```

### 期待される出力例

`lean_canvas.md` の一部：

```markdown
# リーンキャンバス - AI営業アシスタント「SalesGPT」

## 課題 (Problem)
1. **日報入力の手間**（3U+1: ✅切実、✅不可避、✅今すぐ、✅代替なし）
   - 発生シーン: 営業担当者が外回りから帰社後、1日30分かけて日報入力
   - 発生頻度: 日次
   - 感情強度: 7/10（面倒、時間の無駄）

## 顧客セグメント (Customer Segments)
- **ターゲット**: BtoB営業を行う中小企業（従業員10-50名）
- **ペルソナ**:
  - 名前: 田中太郎（35歳、営業課長）
  - 1日の行動タイムライン:
    - 09:00: 出社、メール確認
    - 10:00: 顧客訪問（3件/日）
    - 18:00: 帰社、日報入力（30分）← **課題発生**
    - 19:00: 退社

## 独自の価値提案 (UVP)
**音声3分で完了するAI日報作成で、営業の本質業務に集中できる時間を生み出す。なぜ今か：生成AI普及で音声認識精度が実用レベルに到達したため。**

## 市場分析
- **TAM（総市場）**: 日本の中小企業数380万社 × 営業担当者5名 × 年間1.2万円 = 2,280億円
- **SAM（対象市場）**: BtoB営業企業（全体の30%）= 684億円
- **SOM（獲得可能市場）**: 初年度0.1% = 6.8億円
- **CAGR**: 15%（中小企業DX市場成長率）

## 10倍優位性
- **軸1: 時間削減** - 30分 → 3分（10倍改善）
- **軸2: 使いやすさ** - SFAの1/10の学習時間

## マネタイズモデル
- 月額980円/ユーザー（SaaS）
- 年間契約で20%割引
- LTV目標: 12ヶ月 × 980円 × 0.8（割引） = 9,408円/ユーザー

## 北極星指標
- 週次アクティブユーザー数（WAU）
```

---

## Test 2: CPFゲート統合テスト（30分）

### 目的
STEP -1 → STEP 5のフル実行とCPFゲート判定の動作確認

### 実行方法（Antigravity）

```bash
# orchestrate_phase1 ワークフロー実行
antigravity run /orchestrate_phase1 \
  --idea "中小企業向けAI営業支援ツール" \
  --stop-at cpf_gate
```

### 実行方法（Claude Code）

1. **Orchestrator起動**
   ```
   system_prompts/01_orchestrator_prompt.md を参照
   mode: "phase1"
   ```

2. **実行コマンド（疑似）**
   ```
   "Phase1統合モードで、中小企業向けAI営業支援ツールのビジネスアイデアを
   STEP -1からSTEP 5（CPFゲート）まで実行してください。"
   ```

### 検証手順

1. **成果物確認**
   ```bash
   # 生成ファイル数確認
   find tests/test_ideas/test_idea_cpf_001/documents -name "*.md" | wc -l
   # 期待: 11ファイル
   ```

2. **CPFゲート判定確認**
   ```bash
   cat tests/test_ideas/test_idea_cpf_001/reviews/cpf_gate/iteration_1/gatekeeper_result.yaml
   ```

3. **チェックリスト**
   - [ ] STEP -1〜4.5が実行された
   - [ ] cpf_diagnosis.mdが生成された
   - [ ] CPFスコア60%以上（PASS条件）
   - [ ] Reviewers評価ファイル3つ存在
   - [ ] gatekeeper_result.yaml存在
   - [ ] verdict: "PASS" または "FAIL"
   - [ ] total_score記録

### PASSシナリオの期待出力

`gatekeeper_result.yaml`:
```yaml
gatekeeper_result:
  timestamp: "2025-12-29T14:30:00Z"
  iteration: 1
  gate_type: "CPF"
  score_summary:
    peter_thiel: 0
    yc: 0
    startup_science: 0
    total: 0
  verdict: "PASS"
  action: "PROCEED_TO_STEP_5.5"
```

### FAILシナリオの期待出力

```yaml
gatekeeper_result:
  verdict: "FAIL"
  action: "UPDATE_AGENT_SKILLS_AND_RETRY"
  retry_info:
    retry_from_step: "STEP_1"
    reason: "CPF未達成。課題・顧客定義を再検討"
  updater_instructions:
    new_rules:
      - "ペルソナの課題発生シーンを具体的に記述せよ（時刻、場所、感情を含む）"
```

---

## Test 3: PSFゲート統合テスト（30分）

### 目的
STEP 5.5 → STEP 6実行とPSFゲート判定の動作確認

### 前提条件
- Test 2でCPFゲートPASS済み

### 実行方法（Antigravity）

```bash
# CPFゲートPASS後、PSFゲートまで実行
antigravity run /orchestrate_phase1 \
  --resume-from cpf_gate \
  --idea-folder tests/test_ideas/test_idea_cpf_001 \
  --stop-at psf_gate
```

### 検証手順

1. **成果物確認**
   ```bash
   # 追加ファイル確認
   ls tests/test_ideas/test_idea_cpf_001/documents/3_planning/
   # 期待: 10x_validation.md, psf_diagnosis.md
   ```

2. **PSFゲート判定確認**
   ```bash
   cat tests/test_ideas/test_idea_cpf_001/reviews/psf_gate/iteration_1/gatekeeper_result.yaml
   ```

3. **チェックリスト**
   - [ ] 10x_validation.mdで10倍優位性2軸以上
   - [ ] psf_diagnosis.md生成
   - [ ] Reviewers評価ファイル3つ存在
   - [ ] verdict: "PASS" または "FAIL"
   - [ ] PASSの場合、action: "PROCEED_TO_STEP_7"

### 期待される出力

`10x_validation.md` の一部：
```markdown
# 10倍優位性検証

## 軸1: 時間削減
- 既存: SFA手動入力 30分/日
- 当社: 音声入力 3分/日
- **改善倍率: 10倍**

## 軸2: 学習時間
- 既存: SFA導入研修 10時間
- 当社: チュートリアル 1時間
- **改善倍率: 10倍**

## 結論
✅ 10倍優位性を2軸で達成
```

---

## トラブルシューティング

### 問題1: Executorがファイルを生成しない

**原因**: AgentSkills.mdのパスが正しくない

**解決策**:
```bash
# パス確認
echo $AGENT_SKILLS_PATH
# 絶対パスに修正
```

### 問題2: CPFゲートで無限ループ

**原因**: total_scoreが常に0以外

**解決策**:
- Reviewersの評価基準を確認
- cpf_diagnosis.mdの内容を確認
- iteration上限（5回）を確認

### 問題3: AgentSkills.mdが50ルール超過

**原因**: Updaterのルール統合が機能していない

**解決策**:
- 07_updater_prompt.mdの統合ロジック確認
- 手動でルール統合実施

---

## テスト完了後のアクション

### 全テストPASSの場合

1. **テスト結果をコミット**
   ```bash
   git add tests/
   git commit -m "test: 統合テスト完了 - 全テストPASS"
   ```

2. **次のステップ**
   - E2Eテスト（完全自動実行）
   - ドキュメント整備

### テスト失敗の場合

1. **問題点を記録**
   - test_results.mdに詳細記載
   - 失敗したチェックリスト項目

2. **修正実施**
   - 該当プロンプトファイルを修正
   - 再テスト

3. **イシュー作成**（必要に応じて）
   ```markdown
   ## Issue: [問題の概要]

   ### 再現手順
   1.
   2.

   ### 期待される動作

   ### 実際の動作

   ### 修正案
   ```

---

## テスト結果記録

テスト実施後、以下のファイルに結果を記録：

`tests/test_results.md`

```markdown
# 統合テスト実行結果

## 実施日時: 2025-12-29 14:00

## Test 1: Executor単体テスト
- ✅ PASS / ❌ FAIL
- 実行時間: X分Y秒
- チェックリスト: X/14項目PASS
- 備考:

## Test 2: CPFゲート統合テスト
- ✅ PASS / ❌ FAIL
- シナリオ: PASS / FAIL / Human-in-the-Loop
- iteration: X回
- 備考:

## Test 3: PSFゲート統合テスト
- ✅ PASS / ❌ FAIL
- 10倍優位性軸数: X軸
- 備考:

## 総合評価
- 全体結果: ✅ 全PASS / ⚠️ 一部FAIL / ❌ 全FAIL
- 発見された問題: X件
- 次のアクション:
```
