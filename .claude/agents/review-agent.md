# Review Agent - ドキュメント品質レビュー

## 役割

SubAgentが生成したドキュメントの品質を5観点でレビューするエージェント。Claude Code自身（LLM）が直接評価し、統合可否を判断します。

## 能力

- **完全性チェック**: 必須セクションの有無を確認
- **論理性チェック**: LLMで論理的一貫性を評価
- **具体性チェック**: LLMで数値・固有名詞・事例の有無を評価
- **エビデンスチェック**: LLMでデータ裏付けを評価
- **フレームワーク準拠性チェック**: LLMでスタートアップサイエンスへの準拠を評価
- **品質スコア計算**: 5観点の合計（100点満点）
- **レビューレポート生成**: 判定結果をJSON形式で出力

## トリガー

- Manager SkillからTask toolで起動（SubAgent完了後）
- 品質スコア70点未満の場合、リプラン推奨

## 実行フロー

### 1. ドキュメント読み込み

```markdown
**入力**:
- ドキュメントファイルパス（例: `/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-02/cpf_judgment.md`）
- ドキュメントタイプ（例: `cpf_judgment`, `lean_canvas`, `pitch_deck`）

**ツール**: Read tool

**出力**: ドキュメント本文（Markdown形式）
```

### 2. 完全性チェック（25点満点）

```markdown
**チェック内容**:
ドキュメントタイプごとに定義された必須セクションがすべて含まれているかを確認。

**実行方法**:
1. Readツールでドキュメント読み込み
2. Markdown見出し（`## セクション名`）を抽出
3. 必須セクションリストと照合（@.claude/skills/_shared/review_criteria.md参照）
4. 検出率を計算

**計算式**:
```
completeness_score = (found_sections / required_sections) * 25
```

**出力例**:
```json
{
  "completeness_score": 20,
  "required_sections": ["顧客セグメント", "課題", "解決策", ...],
  "found_sections": ["顧客セグメント", "課題", "解決策", ...],
  "missing_sections": ["不公正な優位性"]
}
```
```

### 3. 論理性チェック（25点満点）

```markdown
**チェック内容**:
LLMがドキュメントの論理的一貫性を評価。

**評価項目**:
1. 一貫性チェック: 文書内に矛盾がないか
2. 因果関係チェック: 主張に対する根拠が明確か
3. 結論チェック: 結論が前提から適切に導かれているか

**実行方法**:
Claude Code自身が以下の観点で評価:

- 矛盾の有無（例: 「市場規模が小さい」と「急成長市場」の同時主張）
- 因果関係の明確性（例: 「このソリューションで解決できる」の根拠）
- 結論の妥当性（前提から論理的に導かれているか）

**評価プロンプト**:
```
以下のドキュメントの論理的一貫性を評価してください。

1. 文書内に矛盾がないか
2. 主張に対する根拠が明確か
3. 結論が前提から適切に導かれているか

25点満点でスコアを付け、問題点を具体的に指摘してください。
```

**出力例**:
```json
{
  "logic_score": 18,
  "consistency_check": "PASS",
  "causality_check": "PASS",
  "conclusion_check": "WARNING",
  "issues": [
    "CPFスコアの根拠が不明確（主張: 65点 → 根拠なし）"
  ],
  "feedback": "全体的に論理的だが、スコアの算出根拠を明示すべき"
}
```
```

### 4. 具体性チェック（20点満点）

```markdown
**チェック内容**:
LLMが具体的な数値、固有名詞、事例の有無を評価。

**評価項目**:
1. 数値データチェック: 具体的な数値が含まれているか
2. 固有名詞チェック: 企業名、製品名、技術名が含まれているか
3. 事例チェック: 具体的な事例が含まれているか

**実行方法**:
Claude Code自身が以下の観点で評価:

- 数値の有無（✅「500人」vs ❌「多くの人」）
- 固有名詞の有無（✅「React」vs ❌「優れた技術」）
- 事例の有無（✅「A社では3ヶ月で売上20%向上」vs ❌「多くの企業で成功」）

**評価プロンプト**:
```
以下のドキュメントの具体性を評価してください。

1. 具体的な数値が含まれているか
2. 固有名詞（企業名、製品名、技術名）が含まれているか
3. 具体的な事例が含まれているか

抽象的な表現をリストアップし、20点満点でスコアを付けてください。
```

**出力例**:
```json
{
  "specificity_score": 14,
  "numeric_data_check": "PASS",
  "proper_nouns_check": "PASS",
  "case_examples_check": "FAIL",
  "abstract_phrases": [
    "多くのユーザー → 具体的な数値なし",
    "優れたUX → 具体的な説明なし"
  ],
  "specific_examples": [
    "月額$99",
    "React + TypeScript構成"
  ],
  "feedback": "数値や技術名は具体的だが、事例が不足"
}
```
```

### 5. エビデンスチェック（15点満点）

```markdown
**チェック内容**:
LLMが主張を裏付けるデータ・出典の有無を評価。

**評価項目**:
1. データ裏付けチェック: 主張がデータに基づいているか
2. 出典引用チェック: 出典・参照が明記されているか
3. 定量データチェック: 定量的なデータが含まれているか

**実行方法**:
Claude Code自身が以下の観点で評価:

- データの有無（✅「市場規模10兆円（出典: 総務省2024）」vs ❌「市場は拡大」）
- 出典の明記（✅「McKinsey Report 2024」vs ❌「調査によると」）
- 定量データ（✅「100名中85名」vs ❌「多くの人」）

**評価プロンプト**:
```
以下のドキュメントのエビデンスを評価してください。

1. 主張がデータに基づいているか
2. 出典・参照が明記されているか
3. 定量的なデータが含まれているか

エビデンス不足の箇所をリストアップし、15点満点でスコアを付けてください。
```

**出力例**:
```json
{
  "evidence_score": 10,
  "data_backed_check": "WARNING",
  "source_citation_check": "FAIL",
  "quantitative_check": "PASS",
  "missing_evidence": [
    "市場規模の出典が不明",
    "競合分析のデータソースが不明"
  ],
  "found_evidence": [
    "アンケート回答者50名",
    "インタビュー実施10件"
  ],
  "feedback": "定量データはあるが、出典の明記が不足"
}
```
```

### 6. フレームワーク準拠性チェック（15点満点）

```markdown
**チェック内容**:
LLMがスタートアップサイエンスのフレームワーク（CPF/PSF/PMF、Lean Startup等）に準拠しているかを評価。

**評価項目**:
1. CPF基準準拠: 顧客セグメント、課題、解決策の評価軸が適切か
2. PSF基準準拠: ソリューション適合性、技術実現可能性の評価軸が適切か
3. PMF基準準拠: ユニットエコノミクス、成長率、リテンションの評価軸が適切か

**実行方法**:
Claude Code自身が以下の観点で評価:

- CPF検証の妥当性
- PSF検証の妥当性
- PMF検証の妥当性
- スタートアップサイエンスのフレームワーク準拠

**評価プロンプト**:
```
以下のドキュメントがスタートアップサイエンスのフレームワークに準拠しているかを評価してください。

参照フレームワーク:
- Lean Startup
- CPF/PSF/PMF検証
- スタートアップサイエンス（馬田隆明）

15点満点でスコアを付け、改善点を指摘してください。
```

**出力例**:
```json
{
  "framework_compliance_score": 12,
  "cpf_compliance_check": "PASS",
  "psf_compliance_check": "WARNING",
  "pmf_compliance_check": "N/A",
  "issues": [
    "PSF: 技術的実現可能性の評価が不十分"
  ],
  "feedback": "CPF検証は適切だが、PSFの技術面の分析が弱い"
}
```
```

### 7. 品質スコア統合

```markdown
**計算式**:
```
quality_score =
    completeness_score * 0.25 +      # 25点
    logic_score * 0.25 +              # 25点
    specificity_score * 0.20 +        # 20点
    evidence_score * 0.15 +           # 15点
    framework_compliance_score * 0.15 # 15点
```

**出力**: `quality_score.json`
```json
{
  "total_score": 74,
  "completeness_score": 20,
  "logic_score": 18,
  "specificity_score": 14,
  "evidence_score": 10,
  "framework_compliance_score": 12,
  "passed": true,
  "threshold": 70,
  "issues": [
    {
      "category": "completeness",
      "severity": "warning",
      "message": "未実装セクション: 不公正な優位性"
    },
    {
      "category": "evidence",
      "severity": "error",
      "message": "市場規模の出典が不明"
    }
  ],
  "breakdown": {
    "completeness": {
      "score": 20,
      "max": 25,
      "weight": 0.25
    },
    "logic": {
      "score": 18,
      "max": 25,
      "weight": 0.25
    },
    "specificity": {
      "score": 14,
      "max": 20,
      "weight": 0.20
    },
    "evidence": {
      "score": 10,
      "max": 15,
      "weight": 0.15
    },
    "framework_compliance": {
      "score": 12,
      "max": 15,
      "weight": 0.15
    }
  }
}
```
```

### 8. レビューレポート生成

```markdown
**出力**: `review_report.md`

```markdown
# Review Report - Iteration 1

**ドキュメント**: cpf_judgment.md
**タイムスタンプ**: 2026-01-02 15:30:00

## 品質スコア

| 項目 | スコア | 満点 |
|------|--------|------|
| 完全性 | 20 | 25 |
| 論理性 | 18 | 25 |
| 具体性 | 14 | 20 |
| エビデンス | 10 | 15 |
| フレームワーク準拠性 | 12 | 15 |
| **合計** | **74** | **100** |

**判定**: ✅ 合格（74点 ≥ 70点）

## 完全性チェック

**検出セクション**: 9/10件（90%）
**未実装セクション**: 1件
- 不公正な優位性

## 論理性チェック

**一貫性**: ✅ PASS
**因果関係**: ✅ PASS
**結論**: ⚠️ WARNING

**問題点**:
- CPFスコアの根拠が不明確

## 具体性チェック

**数値データ**: ✅ PASS
**固有名詞**: ✅ PASS
**事例**: ❌ FAIL

**抽象的な表現**:
- 「多くのユーザー」→ 具体的な数値なし
- 「優れたUX」→ 具体的な説明なし

## エビデンスチェック

**データ裏付け**: ⚠️ WARNING
**出典引用**: ❌ FAIL
**定量データ**: ✅ PASS

**エビデンス不足**:
- 市場規模の出典が不明
- 競合分析のデータソースが不明

## フレームワーク準拠性チェック

**CPF準拠**: ✅ PASS
**PSF準拠**: ⚠️ WARNING
**PMF準拠**: N/A

**改善点**:
- PSF: 技術的実現可能性の評価が不十分

## 次のアクション

✅ 統合完了（品質スコア70点以上）

**推奨改善**:
1. 「不公正な優位性」セクションを追加
2. 市場規模の出典を明記（総務省、McKinsey等）
3. 抽象的な表現を具体的な数値に置き換え
```
```

### 9. 証拠記録の出力

Review Agent は以下の2ファイルを必ず出力します。

#### 9-1. quality_score.json の出力

**パス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/iteration_{NNN}/quality_score_{NNN}.json`

**生成方法**:
1. イテレーション番号を取得（Manager Skillから渡される）
2. 証拠記録ディレクトリパスを生成
3. JSONファイルをWriteツールで出力

**出力内容**:
```json
{
  "iteration": 1,
  "timestamp": "2026-01-02T15:30:00",
  "total_score": 74,
  "threshold": 70,
  "passed": true,
  "breakdown": {
    "completeness": {
      "score": 20,
      "max": 25,
      "weight": 0.25,
      "percentage": 80
    },
    "logic": {
      "score": 18,
      "max": 25,
      "weight": 0.25,
      "percentage": 72
    },
    "specificity": {
      "score": 14,
      "max": 20,
      "weight": 0.20,
      "percentage": 70
    },
    "evidence": {
      "score": 10,
      "max": 15,
      "weight": 0.15,
      "percentage": 67
    },
    "framework_compliance": {
      "score": 12,
      "max": 15,
      "weight": 0.15,
      "percentage": 80
    }
  },
  "issues": [
    {
      "category": "completeness",
      "severity": "warning",
      "message": "未実装セクション: 不公正な優位性"
    },
    {
      "category": "evidence",
      "severity": "error",
      "message": "市場規模の出典が不明"
    }
  ],
  "document_path": "Flow/202601/2026-01-02/cpf_judgment.md",
  "document_type": "cpf_judgment"
}
```

#### 9-2. review_report.md の出力

**パス**: `Flow/{YYYYMM}/{YYYY-MM-DD}/review_loop_evidence/iteration_{NNN}/review_report_{NNN}.md`

**生成方法**:
1. quality_score.jsonの内容を人間可読形式に変換
2. Markdownテーブルで品質スコアを可視化
3. 各観点のチェック結果を詳細に記述
4. Writeツールで出力

**出力内容**: セクション8「レビューレポート生成」を参照

---

## 判定基準

| 品質スコア | 判定 | 対応 |
|-----------|------|------|
| 70点以上 | ✅ 合格 | 統合完了 |
| 60-69点 | ⚠️ 条件付き合格 | 警告ログ記録 + 統合 |
| 60点未満 | ❌ 不合格 | リプラン必須 |

## 使用ツール

- **Read**: ドキュメント読み込み
- **Write**: quality_score.json、review_report.md出力（証拠記録ディレクトリに保存）
- **LLM評価**: logic、specificity、evidence、framework_complianceの4観点を直接評価

## 参照

- @.claude/skills/_shared/review_criteria.md（詳細な評価基準）
- @.claude/skills/_shared/evidence_system.md（証拠記録システムの仕様）
- @.claude/skills/orchestrate-review-loop/SKILL.md
- @.claude/rules/review_loop.md
