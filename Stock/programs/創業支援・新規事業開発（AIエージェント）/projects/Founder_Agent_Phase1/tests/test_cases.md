# Orchestrator × orchestrate_phase1 統合テスト - テストケース定義

## テスト環境

- **実装バージョン**: orchestrate_phase1統合版
- **AgentSkills**: 10セクション、27ルール
- **テスト日時**: 2025-12-29
- **テストツール**: Antigravity / Claude Code

---

## Test Case 1: Executor単体テスト（STEP_2）

### 目的
Executorがステップ別実行モードでリーンキャンバスを正しく生成できるか確認

### 前提条件
- AgentSkills.md（27ルール）が存在
- テスト用アイデア：「中小企業向けAI営業支援ツール」

### 入力パラメータ

```yaml
input:
  mode: "step_by_step"
  step_name: "STEP_2"
  context:
    idea_folder: "/path/to/test_idea_001"
    business_idea: "中小企業（従業員10-50名）向けのAI営業支援ツール。営業担当者の日報・商談記録を自動分析し、次のアクションを提案する。"
    previous_outputs:
      - "business_idea.md"
      - "mvv.md"
  agent_skills_path: "/path/to/AgentSkills.md"
```

### 期待される出力

**ファイル**: `{idea_folder}/documents/2_discovery/lean_canvas.md`

**内容**:
1. リーンキャンバス9ブロック全て記載
2. AgentSkills.md全セクション遵守:
   - セクション1: TAM/SAM/SOM、CAGR記載
   - セクション2: ターゲット顧客、ペルソナ行動タイムライン
   - セクション3: 3U+1検証、課題シーン、代替案3つ以上
   - セクション4: UVP一文、MVP種類、「なぜ今か」
   - セクション5: 既存代替品3つ、10倍改善軸
   - セクション6: マネタイズモデル、価格帯、フライホイール
   - セクション7: 現在フェーズ（Idea）、マイルストーン
   - セクション8: 初期ユーザー獲得方法
   - セクション9: 北極星指標
   - セクション10: LP事前登録30人目標

### 検証ポイント（チェックリスト）

- [ ] ファイルが正しいパスに生成された
- [ ] リーンキャンバス9ブロックが全て存在
- [ ] TAM/SAM/SOMが定量的に記載されている
- [ ] 市場成長率（CAGR）が記載されている
- [ ] ペルソナに1日の行動タイムラインが含まれる
- [ ] 課題が3U+1で検証可能な形式
- [ ] 既存代替案が3つ以上列挙されている
- [ ] UVPが一文で表現されている
- [ ] UVPに「なぜ今か」が含まれる
- [ ] MVP種類が明記されている
- [ ] 10倍改善軸が数値で示されている
- [ ] マネタイズモデルが明記されている
- [ ] 北極星指標が定義されている
- [ ] 仮説と事実が区別されている

### 成功基準
- 全チェックリスト項目が✅
- 生成時間が5分以内
- エラーなし

---

## Test Case 2: CPFゲート統合テスト

### 目的
STEP -1 → STEP 5のフル実行とCPFゲート判定の動作確認

### 前提条件
- orchestrate_phase1 Controller起動可能
- Orchestrator、Reviewers、Gatekeeper起動可能

### 入力パラメータ

```yaml
input:
  mode: "phase1"
  business_idea: "中小企業向けAI営業支援ツール"
  idea_folder: "/path/to/test_idea_cpf_001"
```

### 実行フロー

1. **Controller起動** → STEP -1 → STEP 4.5実行
2. **STEP 5実行** → cpf_diagnosis.md生成
3. **Orchestrator** → Reviewers並列呼び出し
4. **Gatekeeper判定**

### 期待される出力（PASSシナリオ）

```yaml
gatekeeper_result:
  gate_type: "CPF"
  iteration: 1
  score_summary:
    peter_thiel: 0
    yc: 0
    startup_science: 0
    total: 0
  verdict: "PASS"
  action: "PROCEED_TO_STEP_5.5"
```

**成果物**:
- `documents/1_initiating/`: 4ファイル
- `documents/2_discovery/`: 5ファイル
- `documents/3_planning/`: 2ファイル（interview_simulation.md, cpf_diagnosis.md）
- `reviews/cpf_gate/iteration_1/`: 4ファイル

### 検証ポイント（PASSシナリオ）

- [ ] STEP -1 → STEP 4.5が順次実行された
- [ ] 全11ファイルが生成された
- [ ] cpf_diagnosis.mdでCPFスコア60%以上
- [ ] Reviewers評価が並列で実施された
- [ ] total_score == 0
- [ ] verdict == "PASS"
- [ ] action == "PROCEED_TO_STEP_5.5"

### 期待される出力（FAILシナリオ）

```yaml
gatekeeper_result:
  gate_type: "CPF"
  iteration: 1
  score_summary:
    total: 15  # 0でない
  verdict: "FAIL"
  action: "UPDATE_AGENT_SKILLS_AND_RETRY"
  retry_info:
    retry_from_step: "STEP_1"
    reason: "CPF未達成。課題・顧客定義を再検討"
  updater_instructions:
    new_rules: [list]
```

### 検証ポイント（FAILシナリオ）

- [ ] total_score > 0
- [ ] verdict == "FAIL"
- [ ] Updaterが呼び出された
- [ ] AgentSkills.mdに新規ルールが追加された
- [ ] 更新履歴テーブルに記録された
- [ ] STEP 1から再実行された

### 検証ポイント（Human-in-the-Loopシナリオ）

**前提**: iteration == 5 and total_score > 0

- [ ] action == "HUMAN_IN_THE_LOOP"
- [ ] human_info.optionsが3つ存在
- [ ] recommendationが明記されている
- [ ] CPF未達成メッセージが表示される

---

## Test Case 3: PSFゲート統合テスト

### 目的
STEP 5.5 → STEP 6実行とPSFゲート判定の動作確認

### 前提条件
- CPFゲートPASS済み
- Controller再起動可能

### 入力パラメータ

```yaml
input:
  mode: "phase1"
  resume_from_gate: "PSF"
  idea_folder: "/path/to/test_idea_cpf_001"  # CPFゲートPASS済みフォルダ
```

### 実行フロー

1. **Controller再起動** → STEP 5.5, STEP 6実行
2. **STEP 6実行** → psf_diagnosis.md生成
3. **Orchestrator** → Reviewers並列呼び出し
4. **Gatekeeper判定**

### 期待される出力（PASSシナリオ）

```yaml
gatekeeper_result:
  gate_type: "PSF"
  score_summary:
    total: 0
  verdict: "PASS"
  action: "PROCEED_TO_STEP_7"
```

**成果物**:
- `documents/3_planning/10x_validation.md`
- `documents/3_planning/psf_diagnosis.md`
- `reviews/psf_gate/iteration_1/`: 4ファイル

### 検証ポイント（PASSシナリオ）

- [ ] STEP 5.5, STEP 6が実行された
- [ ] 10x_validation.mdで10倍優位性2軸以上
- [ ] psf_diagnosis.mdが生成された
- [ ] total_score == 0
- [ ] verdict == "PASS"
- [ ] action == "PROCEED_TO_STEP_7"

### 検証ポイント（FAILシナリオ）

- [ ] total_score > 0
- [ ] verdict == "FAIL"
- [ ] retry_info.retry_from_step == "STEP_2"
- [ ] Updaterが呼び出された
- [ ] STEP 2から再実行された

### 検証ポイント（Human-in-the-Loopシナリオ）

**前提**: iteration == 5 and total_score > 0

- [ ] action == "HUMAN_IN_THE_LOOP"
- [ ] human_info.optionsが4つ存在
- [ ] PSF未達成メッセージが表示される

---

## Test Case 4: エラーハンドリングテスト

### 目的
Controllerのエラーハンドリング（3回リトライ）の動作確認

### テストシナリオ

1. **ステップレベルエラー**
   - STEP 4で意図的にエラー発生
   - 3回リトライ実施確認
   - exponential backoff確認（1秒、2秒、4秒）

2. **致命的エラー**
   - Executor完全停止
   - ESCALATE_TO_ORCHESTRATOR確認

### 検証ポイント

- [ ] max_retries == 3
- [ ] backoff時間が正しい（1s, 2s, 4s）
- [ ] 3回失敗後にESCALATE
- [ ] エラー詳細が記録される

---

## テスト実行手順

### 環境セットアップ

1. テスト用ディレクトリ作成
```bash
mkdir -p /path/to/test_ideas/test_idea_001
mkdir -p /path/to/test_ideas/test_idea_cpf_001
```

2. AgentSkills.mdコピー
```bash
cp AgentSkills.md /path/to/test_ideas/test_idea_001/
```

### Test Case 1実行（Executor単体テスト）

```bash
# Antigravityで実行
antigravity run executor \
  --prompt system_prompts/02_executor_prompt.md \
  --input test_cases/executor_step2_input.yaml

# または Claude Codeで実行
# 02_executor_prompt.mdを読み込み、STEP_2を実行
```

### Test Case 2実行（CPFゲート統合テスト）

```bash
# Orchestratorを起動
antigravity run orchestrator \
  --prompt system_prompts/01_orchestrator_prompt.md \
  --mode phase1 \
  --input test_cases/cpf_gate_input.yaml
```

### Test Case 3実行（PSFゲート統合テスト）

```bash
# PSFゲートから再開
antigravity run orchestrator \
  --prompt system_prompts/01_orchestrator_prompt.md \
  --mode phase1 \
  --resume PSF \
  --input test_cases/psf_gate_input.yaml
```

---

## テスト結果記録テンプレート

```markdown
## テスト実行日時: YYYY-MM-DD HH:MM

### Test Case 1: Executor単体テスト
- 実行状態: ✅ PASS / ❌ FAIL
- 実行時間: X分Y秒
- 生成ファイル: lean_canvas.md
- チェックリスト: X/14項目PASS
- 備考:

### Test Case 2: CPFゲート統合テスト
- 実行状態: ✅ PASS / ❌ FAIL
- シナリオ: PASS / FAIL / Human-in-the-Loop
- 実行時間: X分Y秒
- iteration: X回
- 備考:

### Test Case 3: PSFゲート統合テスト
- 実行状態: ✅ PASS / ❌ FAIL
- シナリオ: PASS / FAIL / Human-in-the-Loop
- 実行時間: X分Y秒
- 備考:

### 発見された問題点
1.
2.

### 修正が必要な箇所
1.
2.
```
