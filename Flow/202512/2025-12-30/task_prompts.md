# Claude Code実行用タスクプロンプト

**生成日時**: 2025-12-30 14:35
**対象**: daily_tasks.yaml の全タスク（37個）

**✨ 使い方**:
1. 各タスクの「📋 実行用プロンプト」セクションのコードブロックを見つける
2. コードブロック全体を選択してコピー
3. Claude Codeに貼り付けて実行

---

## 起業の科学準拠確認タスク（12ステップ）

### T004-1: 起業の科学の全章・全節の構造を抽出

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 起業の科学の全章・全節の構造を抽出

## 目的
起業の科学の書籍内容を構造化し、全章・全節の構造を抽出する。

## 対象ファイル
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/PDF/起業の科学_full.md`
- `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/PDF/起業大全_full.md`

## 手順
1. 上記2つのMarkdownファイルを読み込む
2. 各章（Chapter）のタイトルと番号を抽出
3. 各節（Section）のタイトルと番号を抽出
4. 階層構造を維持したまま整理
5. 以下の形式でレポートを作成して保存:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/startup_science_structure.md`

**内容フォーマット**:
```markdown
# 起業の科学 構造抽出レポート

**生成日時**: 2025-12-30
**対象書籍**: 起業の科学、起業大全

## 全体構造

### 起業の科学
- Chapter 1: [タイトル]
  - Section 1.1: [タイトル]
  - Section 1.2: [タイトル]
- Chapter 2: [タイトル]
  ...

### 起業大全
- Chapter 1: [タイトル]
  ...
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-2: 各章節のキーコンセプトをリストアップ

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 各章節のキーコンセプトをリストアップ

## 目的
起業の科学の各章節から重要なコンセプト・フレームワークを抽出する。

## 前提
T004-1で抽出した `startup_science_structure.md` を参照

## 手順
1. `startup_science_structure.md` を読み込む
2. 起業の科学と起業大全の本文を読み込む
3. 各章節について以下を抽出:
   - キーコンセプト（概念・考え方）
   - フレームワーク（CPF, PSF, MVV等）
   - 実践手法（具体的なアクション）
   - メトリクス（測定指標）
4. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/startup_science_key_concepts.md`

**内容フォーマット**:
```markdown
# 起業の科学 キーコンセプト一覧

## Chapter 1: [タイトル]

### Section 1.1: [タイトル]
- **キーコンセプト**: [概念名] - [説明]
- **フレームワーク**: [フレームワーク名] - [目的]
- **実践手法**: [手法名] - [具体的アクション]
- **メトリクス**: [指標名] - [測定方法]

### Section 1.2: [タイトル]
...
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-3: 既存16個のスキル（README.md記載）との対応関係をマッピング

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 既存16個のスキルとの対応関係をマッピング

## 目的
既存のFounder Agentスキル（16個）が、起業の科学のどの章節・コンセプトに対応するか明確化する。

## 対象ファイル
- `/Users/yuichi/AIPM/aipm_v0/.claude/skills/README.md` - 既存スキル一覧
- `startup_science_key_concepts.md` - T004-2で作成

## 既存16個のスキル
1. `/orchestrate-phase1` - Phase1全自動実行
2. `/discover-demand` - 需要発見リサーチ
3. `/create-mvv` - MVV早期定義
4. `/build-flywheel` - フライホイール設計
5. `/create-persona` - ペルソナ作成
6. `/research-problem` - Web課題発見
7. `/research-competitors` - 競合調査
8. `/simulate-interview` - 仮想ペルソナインタビュー
9. `/validate-cpf` - CPF検証
10. `/validate-10x` - 10倍優位性検証
11. `/validate-psf` - PSF検証
12. `/validate-unit-economics` - Unit Economics検証
13. `/build-lp` - LP構築
14. `/create-sns-content` - SNSコンテンツ作成
15. `/startup-scorecard` - スタートアップ・スコアカード
16. `/pivot-decision` - ピボット判断支援

## 手順
1. 各スキルの SKILL.md を読み込み、機能と目的を確認
2. `startup_science_key_concepts.md` を参照
3. 各スキルが対応する章節・コンセプトをマッピング
4. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/skill_mapping.md`

**内容フォーマット**:
```markdown
# スキル→起業の科学 対応マップ

## スキル一覧と対応関係

### `/orchestrate-phase1` - Phase1全自動実行
- **対応章**: Chapter X: [タイトル]
- **対応節**: Section X.Y: [タイトル]
- **対応コンセプト**: [コンセプト名]
- **対応フレームワーク**: [フレームワーク名]
- **カバレッジ評価**: 完全/部分的/未対応

### `/discover-demand` - 需要発見リサーチ
...

## サマリー
- **完全対応スキル**: X個
- **部分的対応スキル**: X個
- **対応不明スキル**: X個
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-4: カバーされていない章節を特定

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: カバーされていない章節を特定

## 目的
起業の科学の内容のうち、既存スキルでカバーされていない章節を特定する。

## 前提
- `startup_science_key_concepts.md` - T004-2で作成
- `skill_mapping.md` - T004-3で作成

## 手順
1. 両ファイルを読み込む
2. 起業の科学の全章節リストを作成
3. 既存スキルでカバーされている章節をマーク
4. カバーされていない章節を抽出
5. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/uncovered_sections.md`

**内容フォーマット**:
```markdown
# 未カバー章節リスト

## 完全未カバーの章節（スキル未実装）

### Chapter X, Section X.Y: [タイトル]
- **キーコンセプト**: [概念名]
- **フレームワーク**: [フレームワーク名]
- **ビジネスインパクト**: 高/中/低（後で評価）
- **理由**: [なぜカバーされていないか]

## 部分的カバーの章節（改善余地あり）

### Chapter X, Section X.Y: [タイトル]
- **現在のカバレッジ**: [既存スキル名]
- **不足要素**: [何が足りないか]
- **改善案**: [どう改善するか]

## サマリー
- **完全未カバー**: X章節
- **部分的カバー**: X章節
- **完全カバー**: X章節
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-5: /orchestrate-phase1 の12ステップを詳細確認

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: /orchestrate-phase1 の12ステップを詳細確認

## 目的
メインオーケストレーター `/orchestrate-phase1` の12ステップを詳細に分析する。

## 対象ファイル
`/Users/yuichi/AIPM/aipm_v0/.claude/skills/orchestrate-phase1/SKILL.md`

## 手順
1. SKILL.md を読み込む
2. 12ステップの内容を抽出:
   - 各ステップ名
   - 実行内容
   - 呼び出すサブスキル
   - 期待成果物
   - ステージゲート条件
3. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/orchestrate_phase1_analysis.md`

**内容フォーマット**:
```markdown
# /orchestrate-phase1 詳細分析

## 12ステップ構成

### Step 1: [ステップ名]
- **実行内容**: [何をするか]
- **呼び出すサブスキル**: [スキル名]
- **期待成果物**: [ファイル名または状態]
- **ステージゲート**: [判定基準]
- **所要時間**: [目安時間]

### Step 2: [ステップ名]
...

## ステージゲート一覧
1. **CPF判定** (Step X後)
   - 判定基準: [基準]
   - 未達時アクション: [何をするか]

2. **PSF判定** (Step Y後)
   - 判定基準: [基準]
   - 未達時アクション: [何をするか]
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-6: 各ステップが起業の科学のどのフレームワークに対応するか明記

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 各ステップが起業の科学のどのフレームワークに対応するか明記

## 目的
/orchestrate-phase1 の12ステップが、起業の科学のどのフレームワークに対応するか明確化する。

## 前提
- `orchestrate_phase1_analysis.md` - T004-5で作成
- `startup_science_key_concepts.md` - T004-2で作成

## 手順
1. 両ファイルを読み込む
2. 各ステップについて対応するフレームワークを特定
3. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/framework_implementation_status.md`

**内容フォーマット**:
```markdown
# Phase1ステップ→起業の科学フレームワーク対応表

## ステップ別対応関係

### Step 1: [ステップ名]
- **対応フレームワーク**: [フレームワーク名]
- **対応章節**: Chapter X, Section X.Y
- **実装状況**: 完全実装/部分実装/未実装
- **備考**: [補足情報]

### Step 2: [ステップ名]
...

## フレームワーク別実装状況

### CPF (Customer Problem Fit)
- **対応ステップ**: Step X, Step Y
- **実装状況**: 完全実装
- **検証方法**: [検証手法]

### PSF (Problem Solution Fit)
- **対応ステップ**: Step X, Step Y
- **実装状況**: 部分実装
- **不足要素**: [何が足りないか]

## サマリー
- **完全実装フレームワーク**: X個
- **部分実装フレームワーク**: X個
- **未実装フレームワーク**: X個
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-7: 重要フレームワーク（CPF/PSF/MVV/10x/Unit Economics等）の実装状況を確認

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 重要フレームワークの実装状況を確認

## 目的
起業の科学の重要フレームワークの実装状況を詳細に確認する。

## 対象フレームワーク
1. CPF (Customer Problem Fit)
2. PSF (Problem Solution Fit)
3. PMF (Product Market Fit)
4. MVV (Mission/Vision/Values)
5. 10x優位性
6. Unit Economics
7. リーンキャンバス
8. AARRR (海賊指標)
9. 5つの眼（市場分析）
10. ピボット判断基準

## 前提
- `framework_implementation_status.md` - T004-6で作成
- 各スキルのSKILL.md

## 手順
1. 各フレームワークについて以下を調査:
   - 対応する既存スキル
   - 実装されている機能
   - 実装されていない機能
   - 検証方法の有無
2. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/framework_detailed_status.md`

**内容フォーマット**:
```markdown
# 重要フレームワーク実装状況詳細レポート

## 1. CPF (Customer Problem Fit)

### 既存実装
- **対応スキル**: `/validate-cpf`
- **実装機能**:
  - [機能1]
  - [機能2]
- **検証方法**: [検証手法]

### 未実装要素
- [不足要素1]
- [不足要素2]

### 起業の科学での定義
- **Chapter**: X
- **Section**: X.Y
- **キーポイント**: [重要な点]

### 実装評価
- **カバレッジ**: 80% (完全実装に近い)
- **優先度**: 高/中/低
- **改善提案**: [具体的な改善案]

## 2. PSF (Problem Solution Fit)
...

## サマリー表

| フレームワーク | 対応スキル | カバレッジ | 優先度 | 状態 |
|--------------|----------|----------|--------|------|
| CPF | /validate-cpf | 80% | 高 | 部分実装 |
| PSF | /validate-psf | 70% | 高 | 部分実装 |
| MVV | /create-mvv | 90% | 中 | 完全実装 |
...
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-8: 未実装のフレームワークをリストアップ

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 未実装のフレームワークをリストアップ

## 目的
起業の科学に記載されているが、既存スキルで実装されていないフレームワークを特定する。

## 前提
- `framework_detailed_status.md` - T004-7で作成
- `uncovered_sections.md` - T004-4で作成

## 手順
1. 両ファイルを読み込む
2. 未実装または部分実装のフレームワークを抽出
3. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/unimplemented_frameworks.md`

**内容フォーマット**:
```markdown
# 未実装フレームワークリスト

## 完全未実装フレームワーク

### 1. [フレームワーク名]
- **起業の科学での位置**: Chapter X, Section X.Y
- **目的**: [何のためのフレームワークか]
- **主要機能**:
  - [機能1]
  - [機能2]
- **必要な入力**: [何が必要か]
- **期待される出力**: [何が得られるか]
- **ビジネスインパクト**: 高/中/低
- **実装難易度**: 高/中/低

### 2. [フレームワーク名]
...

## 部分実装フレームワーク（改善が必要）

### 1. [フレームワーク名]
- **既存スキル**: [スキル名]
- **実装済み機能**: [機能リスト]
- **未実装機能**: [不足機能リスト]
- **改善による効果**: [どう改善されるか]
- **ビジネスインパクト**: 高/中/低
- **実装難易度**: 高/中/低

## サマリー
- **完全未実装**: X個
- **部分実装**: X個
- **高インパクト未実装**: X個
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-9: 各不足領域のビジネスインパクトを評価（高/中/低）

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 各不足領域のビジネスインパクトを評価

## 目的
未実装フレームワークのビジネスインパクトを定量的に評価する。

## 前提
`unimplemented_frameworks.md` - T004-8で作成

## 評価基準（ビジネスインパクト）
- **高**: スタートアップの成否に直結する重要フレームワーク（CPF/PSF/PMF等）
- **中**: 成功確率を高めるが必須ではないフレームワーク（AARRR、Unit Economics等）
- **低**: あると便利だが優先度が低いフレームワーク

## 手順
1. `unimplemented_frameworks.md` を読み込む
2. 各フレームワークについて以下を評価:
   - Phase1完遂への寄与度
   - ステージゲート（CPF/PSF）への影響度
   - スタートアップの失敗回避への寄与度
3. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/business_impact_evaluation.md`

**内容フォーマット**:
```markdown
# 未実装フレームワーク ビジネスインパクト評価

## 高インパクトフレームワーク（優先実装推奨）

### 1. [フレームワーク名]
- **インパクト評価**: 高
- **評価理由**:
  - Phase1完遂への寄与: [具体的な理由]
  - ステージゲートへの影響: [CPF/PSFのどちらに影響するか]
  - 失敗回避への寄与: [どのような失敗を回避できるか]
- **実装しない場合のリスク**: [リスク内容]
- **推定ROI**: 高/中/低

### 2. [フレームワーク名]
...

## 中インパクトフレームワーク

### 1. [フレームワーク名]
- **インパクト評価**: 中
- **評価理由**: [理由]
...

## 低インパクトフレームワーク

### 1. [フレームワーク名]
- **インパクト評価**: 低
- **評価理由**: [理由]
...

## サマリー
- **高インパクト**: X個
- **中インパクト**: X個
- **低インパクト**: X個
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-10: 実装難易度を評価（高/中/低）

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 実装難易度を評価

## 目的
未実装フレームワークの実装難易度を技術的観点から評価する。

## 前提
`business_impact_evaluation.md` - T004-9で作成

## 評価基準（実装難易度）
- **高**: 複数の外部API連携、複雑なアルゴリズム、大規模データ処理が必要
- **中**: 既存スキルの拡張または中程度のロジック実装が必要
- **低**: 既存パターンの応用または簡単なプロンプト追加で実装可能

## 手順
1. `business_impact_evaluation.md` を読み込む
2. 各フレームワークについて以下を評価:
   - 必要な技術スタック
   - 既存スキルの再利用可能性
   - 外部依存性
   - 実装工数（人日）
3. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/implementation_difficulty_evaluation.md`

**内容フォーマット**:
```markdown
# 未実装フレームワーク 実装難易度評価

## 低難易度フレームワーク（早期実装可能）

### 1. [フレームワーク名]
- **難易度評価**: 低
- **技術的理由**:
  - 必要技術: [技術スタック]
  - 既存スキル再利用: [再利用可能なスキル名]
  - 外部依存: なし/最小限
- **実装工数**: X人日
- **実装アプローチ**: [具体的な実装方法]
- **技術的リスク**: 低/中/高

### 2. [フレームワーク名]
...

## 中難易度フレームワーク

### 1. [フレームワーク名]
- **難易度評価**: 中
- **技術的理由**: [理由]
- **実装工数**: X人日
...

## 高難易度フレームワーク

### 1. [フレームワーク名]
- **難易度評価**: 高
- **技術的理由**: [理由]
- **実装工数**: X人日
- **技術的課題**: [解決すべき課題]
...

## サマリー
- **低難易度**: X個（合計X人日）
- **中難易度**: X個（合計X人日）
- **高難易度**: X個（合計X人日）
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-11: 優先順位マトリクスを作成（インパクト高×難易度低を優先）

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 優先順位マトリクスを作成

## 目的
ビジネスインパクトと実装難易度の2軸で優先順位マトリクスを作成する。

## 前提
- `business_impact_evaluation.md` - T004-9で作成
- `implementation_difficulty_evaluation.md` - T004-10で作成

## 手順
1. 両ファイルを読み込む
2. 各フレームワークをビジネスインパクト×実装難易度でマッピング
3. 優先順位を決定（インパクト高×難易度低 > インパクト高×難易度中 > ...）
4. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/priority_matrix.md`

**内容フォーマット**:
```markdown
# 未実装フレームワーク優先順位マトリクス

## 優先順位マトリクス図

         高難易度          中難易度          低難易度
       ┌─────────────┬─────────────┬─────────────┐
高     │  [F3]       │  [F1]       │  [F4] ★最優先
イ     │             │             │             │
ン     ├─────────────┼─────────────┼─────────────┤
パ  中 │  [F5]       │  [F2]       │  [F6]       │
ク     │             │             │             │
ト     ├─────────────┼─────────────┼─────────────┤
   低 │  [F7]       │  [F8]       │  [F9]       │
     │             │             │             │
       └─────────────┴─────────────┴─────────────┘

## 優先順位別フレームワークリスト

### 【優先度1】高インパクト × 低難易度（最優先実装）

#### 1. [フレームワーク名]
- **ビジネスインパクト**: 高
- **実装難易度**: 低
- **実装工数**: X人日
- **推奨実装時期**: 即時
- **期待効果**: [具体的な効果]

### 【優先度2】高インパクト × 中難易度

#### 1. [フレームワーク名]
...

### 【優先度3】中インパクト × 低難易度

### 【優先度4】高インパクト × 高難易度（長期計画）

### 【優先度5】中インパクト × 中難易度

### 【優先度6】低インパクト（実装保留）

## 実装ロードマップ提案

### Phase 1（即時実装）: 優先度1のフレームワーク
- [フレームワーク1] - X人日
- [フレームワーク2] - X人日
- **合計工数**: X人日

### Phase 2（短期実装）: 優先度2-3のフレームワーク
- [フレームワーク3] - X人日
...
- **合計工数**: X人日

### Phase 3（長期実装）: 優先度4以降
- [フレームワーク5] - X人日
...
- **合計工数**: X人日
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する
```

---

### T004-12: 上位3-5個の追加スキル設計書（skill_design.md）を作成

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 上位3-5個の追加スキル設計書を作成

## 目的
優先順位マトリクスの上位3-5個について、実装可能なスキル設計書を作成する。

## 前提
`priority_matrix.md` - T004-11で作成

## 手順
1. `priority_matrix.md` から優先度1の上位3-5個を抽出
2. 各フレームワークについて詳細設計を作成
3. 以下の形式で設計書を作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/skill_design.md`

**内容フォーマット**:
```markdown
# 追加スキル設計書（上位3-5個）

**作成日**: 2025-12-30
**対象**: 優先度1（高インパクト×低難易度）の上位3-5個

---

## スキル1: /[スキル名]

### 基本情報
- **フレームワーク名**: [フレームワーク名]
- **目的**: [何のためのスキルか]
- **対応する起業の科学**: Chapter X, Section X.Y
- **優先度**: 1（高インパクト×低難易度）
- **実装工数**: X人日

### 機能仕様

#### 入力
- [入力パラメータ1]: [説明]
- [入力パラメータ2]: [説明]

#### 処理フロー
1. [ステップ1の処理内容]
2. [ステップ2の処理内容]
3. [ステップ3の処理内容]

#### 出力
- **成果物ファイル**: `[ファイル名].md`
- **出力形式**: Markdown/YAML/JSON
- **出力内容**:
  - [出力項目1]
  - [出力項目2]

### 技術仕様

#### 依存スキル
- [既存スキル1]: [どう利用するか]
- [既存スキル2]: [どう利用するか]

#### 外部API/ツール
- [API名]: [用途]

#### ファイル構成
.claude/skills/[スキル名]/
├── SKILL.md           # スキル定義
├── system_prompt.md   # システムプロンプト
└── examples/          # 実行例
    └── example_output.md

### プロンプト設計（draft）

# [スキル名]

あなたは起業の科学に基づく[フレームワーク名]の専門家です。

## 目的
[目的を明記]

## 手順
1. [ステップ1]
2. [ステップ2]
3. [ステップ3]

## 出力形式
[出力フォーマットを明記]

## 評価基準
[成功基準を明記]

### 実装計画

#### Phase 1: プロトタイプ（X時間）
- [ ] SKILL.md作成
- [ ] システムプロンプト作成
- [ ] 簡易テスト実行

#### Phase 2: 本実装（X時間）
- [ ] エラーハンドリング追加
- [ ] 既存スキルとの統合
- [ ] ドキュメント整備

#### Phase 3: テスト・検証（X時間）
- [ ] 実データでのテスト
- [ ] ユーザーフィードバック収集
- [ ] 改善実施

### 期待効果
- [効果1]: [定量的な効果]
- [効果2]: [定性的な効果]

### リスクと対策
- **リスク1**: [リスク内容]
  - **対策**: [対策内容]

---

## スキル2: /[スキル名]
...

## スキル3: /[スキル名]
...

## 実装優先順序
1. **最優先**: [スキル名] - [理由]
2. [スキル名] - [理由]
3. [スキル名] - [理由]

## 全体実装スケジュール
- **Week 1**: スキル1のプロトタイプ
- **Week 2**: スキル1の本実装 + スキル2のプロトタイプ
- **Week 3**: スキル2の本実装 + スキル3のプロトタイプ
- **Week 4**: スキル3の本実装 + 全体テスト
```

## 完了基準
全12ステップの成果物ファイル（マッピング表、未実装リスト、設計書等）が存在する

## 最終確認
以下の全12ステップの成果物が揃っていることを確認:
1. startup_science_structure.md
2. startup_science_key_concepts.md
3. skill_mapping.md
4. uncovered_sections.md
5. orchestrate_phase1_analysis.md
6. framework_implementation_status.md
7. framework_detailed_status.md
8. unimplemented_frameworks.md
9. business_impact_evaluation.md
10. implementation_difficulty_evaluation.md
11. priority_matrix.md
12. skill_design.md
```

---

## YouTubeトランスクリプト→GenAI_Research統合タスク（6ステップ）

### T005-1: YouTube動画トランスクリプトファイルの所在を確認

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: YouTube動画トランスクリプトファイルの所在を確認

## 目的
既存のYouTube動画トランスクリプトファイルを発見し、一覧化する。

## 想定パス
`/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/references/transcripts/`

## 手順
1. 上記ディレクトリをGlobで検索
2. 全トランスクリプトファイル（.md, .txt等）をリストアップ
3. 各ファイルについて以下を確認:
   - ファイル名
   - ファイルサイズ
   - 作成日時
   - 内容のプレビュー（最初の100行）
4. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/transcript_inventory.md`

**内容フォーマット**:
```markdown
# YouTube動画トランスクリプト所在確認レポート

**調査日時**: 2025-12-30
**対象ディレクトリ**: transcripts/

## 発見ファイル一覧

### 1. [ファイル名]
- **パス**: [絶対パス]
- **サイズ**: XXX KB
- **作成日時**: YYYY-MM-DD
- **内容プレビュー**:
  [最初の10行]
- **推定トピック**: [トピック推測]

### 2. [ファイル名]
...

## サマリー
- **総ファイル数**: X個
- **総サイズ**: XXX KB
- **主要トピック**: [トピックリスト]
```

## 完了基準
GenAI_Research/index.yamlが存在し、全トランスクリプトにメタデータが付与されている
```

---

### T005-2: トランスクリプトから重要トピックを抽出

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: トランスクリプトから重要トピックを抽出

## 目的
各トランスクリプトから重要なトピック（技術、ユースケース、ベストプラクティス、話者の知見）を抽出する。

## 前提
`transcript_inventory.md` - T005-1で作成

## 手順
1. `transcript_inventory.md` を読み込み、全トランスクリプトファイルを取得
2. 各トランスクリプトファイルを読み込む
3. 以下を抽出:
   - **技術トピック**: GenAI関連技術（LLM, RAG, Fine-tuning等）
   - **ユースケース**: 実際の活用事例
   - **ベストプラクティス**: 推奨される手法・パターン
   - **話者の知見**: 独自の洞察・アドバイス
4. 以下の形式でレポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/transcript_topics.md`

**内容フォーマット**:
```markdown
# トランスクリプト重要トピック抽出レポート

## トランスクリプト1: [ファイル名]

### 技術トピック
- **LLM**: [具体的な内容]
- **RAG**: [具体的な内容]
- **プロンプトエンジニアリング**: [具体的な内容]

### ユースケース
1. [ユースケース1]: [説明]
2. [ユースケース2]: [説明]

### ベストプラクティス
- [プラクティス1]: [詳細]
- [プラクティス2]: [詳細]

### 話者の知見
- [知見1]: [詳細]
- [知見2]: [詳細]

## トランスクリプト2: [ファイル名]
...

## 横断的トピック分析

### 頻出技術トピック
1. **LLM**: X個のトランスクリプトで言及
2. **RAG**: X個のトランスクリプトで言及
...

### 頻出ユースケース
1. **スタートアップ支援**: X個のトランスクリプトで言及
...
```

## 完了基準
GenAI_Research/index.yamlが存在し、全トランスクリプトにメタデータが付与されている
```

---

### T005-3: GenAI_Research/ フォルダ構造を作成

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: GenAI_Research/ フォルダ構造を作成

## 目的
GenAI_Researchフォルダの構造を設計・作成する。

## 前提
`transcript_topics.md` - T005-2で作成

## フォルダ構造（提案）
GenAI_Research/
├── index.yaml                 # 統合インデックス
├── topics/                    # トピック別
│   ├── llm/                  # LLM関連
│   ├── rag/                  # RAG関連
│   ├── prompt_engineering/   # プロンプトエンジニアリング
│   ├── fine_tuning/          # ファインチューニング
│   └── agents/               # エージェント設計
├── technologies/              # 技術別
│   ├── openai/
│   ├── anthropic/
│   ├── langchain/
│   └── llamaindex/
├── use_cases/                 # ユースケース別
│   ├── startup_support/
│   ├── product_development/
│   ├── customer_research/
│   └── content_generation/
├── speakers/                  # 話者別
│   ├── [speaker1_name]/
│   └── [speaker2_name]/
└── transcripts/               # 元トランスクリプト（メタデータ付き）
    ├── transcript_001.md
    └── transcript_002.md

## 手順
1. 上記フォルダ構造を `/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/GenAI_Research/` に作成
2. 各カテゴリに README.md を配置
3. 以下の形式でフォルダ構造レポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/genai_research_structure.md`

**内容フォーマット**:
```markdown
# GenAI_Research フォルダ構造

**作成日**: 2025-12-30
**ベースパス**: /Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/GenAI_Research/

## フォルダツリー
[フォルダ構造を記載]

## 各フォルダの役割

### topics/
トピック別にトランスクリプト内容を分類。各トピックフォルダには関連するトランスクリプトへのリンクを含むREADME.mdを配置。

### technologies/
特定の技術・ツール別に情報を整理。実装例やベストプラクティスを集約。

### use_cases/
ユースケース別に分類。スタートアップ支援、プロダクト開発等の実践的な活用方法。

### speakers/
話者別にトランスクリプトを整理。専門家の知見を追跡しやすくする。

### transcripts/
元のトランスクリプトファイルにメタデータを追加して保存。index.yamlから参照。
```

## 完了基準
GenAI_Research/index.yamlが存在し、全トランスクリプトにメタデータが付与されている
```

---

### T005-4: 各トランスクリプトにLLM読み込み用メタデータを追加

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 各トランスクリプトにLLM読み込み用メタデータを追加

## 目的
各トランスクリプトファイルにLLMが読み込みやすいメタデータを追加する。

## 前提
- `transcript_inventory.md` - T005-1で作成
- `transcript_topics.md` - T005-2で作成
- GenAI_Research/フォルダ構造 - T005-3で作成

## メタデータ項目
- **video_url**: 動画URL
- **title**: 動画タイトル
- **speaker**: 話者名
- **date**: 公開日
- **duration**: 動画時間
- **topic_tags**: トピックタグ（#GenAI #Startup等）
- **summary**: 要約（3-5行）
- **key_points**: キーポイント（箇条書き5-10個）
- **related_frameworks**: 関連する起業の科学フレームワーク（あれば）
- **technologies_mentioned**: 言及された技術リスト
- **use_cases**: ユースケースリスト

## 手順
1. 各トランスクリプトファイルを読み込む
2. 内容を分析してメタデータを生成
3. 以下の形式でメタデータ付きトランスクリプトを作成し、`GenAI_Research/transcripts/` に保存:

**ファイル名**: `GenAI_Research/transcripts/transcript_XXX.md`

**内容フォーマット**:
```markdown
---
metadata:
  video_url: "https://youtube.com/watch?v=XXXXX"
  title: "[動画タイトル]"
  speaker: "[話者名]"
  date: "2025-XX-XX"
  duration: "XX:XX"
  topic_tags:
    - "#GenAI"
    - "#Startup"
    - "#ProductDevelopment"
  summary: |
    [3-5行の要約]
  key_points:
    - "[キーポイント1]"
    - "[キーポイント2]"
    - "[キーポイント3]"
    - "[キーポイント4]"
    - "[キーポイント5]"
  related_frameworks:
    - "CPF (Customer Problem Fit)"
    - "PSF (Problem Solution Fit)"
  technologies_mentioned:
    - "OpenAI GPT-4"
    - "LangChain"
    - "RAG"
  use_cases:
    - "スタートアップ支援"
    - "プロダクト開発"
---

# [動画タイトル]

## 概要
[要約]

## トランスクリプト本文
[元のトランスクリプト内容]

## 関連リソース
- 動画URL: [URL]
- 関連フレームワーク: [フレームワークリスト]
```

4. 処理レポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/transcript_metadata_report.md`

**内容フォーマット**:
```markdown
# トランスクリプトメタデータ追加レポート

**処理日**: 2025-12-30
**処理ファイル数**: X個

## 処理済みトランスクリプト

### 1. transcript_001.md
- **元ファイル**: [元パス]
- **保存先**: GenAI_Research/transcripts/transcript_001.md
- **トピックタグ**: #GenAI, #Startup
- **関連フレームワーク**: CPF, PSF

### 2. transcript_002.md
...

## メタデータ統計
- **総トピックタグ数**: X個
- **頻出タグ**: #GenAI (X件), #Startup (X件)
- **関連フレームワーク**: CPF (X件), PSF (X件)
```

## 完了基準
GenAI_Research/index.yamlが存在し、全トランスクリプトにメタデータが付与されている
```

---

### T005-5: トランスクリプト内容を適切なカテゴリに分類して配置

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: トランスクリプト内容を適切なカテゴリに分類して配置

## 目的
メタデータ付きトランスクリプトを topics/ technologies/ use_cases/ speakers/ の各カテゴリに分類・配置する。

## 前提
- GenAI_Research/transcripts/ のメタデータ付きトランスクリプト - T005-4で作成
- GenAI_Research/ フォルダ構造 - T005-3で作成

## 手順
1. 各トランスクリプトのメタデータを読み込む
2. topic_tags, technologies_mentioned, use_cases, speaker を基に分類
3. 各カテゴリフォルダに以下のファイルを作成:
   - カテゴリ別README.md（そのカテゴリの概要と関連トランスクリプトリスト）
   - トランスクリプトへの参照リスト

### 例: topics/llm/README.md フォーマット
```markdown
# LLM (Large Language Models)

## 概要
大規模言語モデルに関するトランスクリプトを集約。

## 関連トランスクリプト

### 1. [動画タイトル]
- **ファイル**: ../../transcripts/transcript_001.md
- **話者**: [話者名]
- **日付**: 2025-XX-XX
- **キーポイント**:
  - [ポイント1]
  - [ポイント2]

### 2. [動画タイトル]
...

## 主要トピック
- GPT-4の活用方法
- プロンプトエンジニアリング
- LLMの限界と対策
```

4. 全カテゴリについて同様の処理を実行
5. 分類レポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/transcript_classification_report.md`

**内容フォーマット**:
```markdown
# トランスクリプト分類配置レポート

**処理日**: 2025-12-30

## カテゴリ別配置状況

### topics/
- **llm/**: X個のトランスクリプト
- **rag/**: X個のトランスクリプト
- **prompt_engineering/**: X個のトランスクリプト
...

### technologies/
- **openai/**: X個のトランスクリプト
- **anthropic/**: X個のトランスクリプト
...

### use_cases/
- **startup_support/**: X個のトランスクリプト
- **product_development/**: X個のトランスクリプト
...

### speakers/
- **[speaker1]/**: X個のトランスクリプト
- **[speaker2]/**: X個のトランスクリプト
...

## 作成ファイル一覧
- topics/llm/README.md
- topics/rag/README.md
...
（全カテゴリREADME.md）
```

## 完了基準
GenAI_Research/index.yamlが存在し、全トランスクリプトにメタデータが付与されている
```

---

### T005-6: 統合インデックス（index.yaml）を作成（メタデータ検索可能な構造）

**📋 実行用プロンプト（以下のコードブロックをコピー）**:

```
# タスク: 統合インデックス（index.yaml）を作成

## 目的
GenAI_Research全体のメタデータ検索可能な統合インデックスを作成する。

## 前提
- GenAI_Research/transcripts/ のメタデータ付きトランスクリプト - T005-4で作成
- 各カテゴリフォルダのREADME.md - T005-5で作成

## 手順
1. 全トランスクリプトのメタデータを収集
2. 以下の形式でindex.yamlを作成:

**ファイル名**: `GenAI_Research/index.yaml`

**内容フォーマット**:
```yaml
# GenAI_Research 統合インデックス

metadata:
  created_at: "2025-12-30"
  total_transcripts: 10
  last_updated: "2025-12-30"
  version: "1.0"

transcripts:
  - id: "transcript_001"
    title: "[動画タイトル]"
    file_path: "transcripts/transcript_001.md"
    video_url: "https://youtube.com/watch?v=XXXXX"
    speaker: "[話者名]"
    date: "2025-XX-XX"
    duration: "XX:XX"
    topic_tags:
      - "GenAI"
      - "Startup"
      - "ProductDevelopment"
    summary: |
      [3-5行の要約]
    key_points:
      - "[キーポイント1]"
      - "[キーポイント2]"
      - "[キーポイント3]"
    related_frameworks:
      - "CPF"
      - "PSF"
    technologies_mentioned:
      - "OpenAI GPT-4"
      - "LangChain"
    use_cases:
      - "startup_support"
      - "product_development"
    categories:
      topics:
        - "llm"
        - "rag"
      technologies:
        - "openai"
        - "langchain"
      use_cases:
        - "startup_support"
      speakers:
        - "[speaker_name]"

  - id: "transcript_002"
    ...

# カテゴリ別インデックス
categories:
  topics:
    llm:
      description: "大規模言語モデル関連"
      transcript_count: 5
      transcript_ids:
        - "transcript_001"
        - "transcript_003"
    rag:
      description: "Retrieval-Augmented Generation関連"
      transcript_count: 3
      transcript_ids:
        - "transcript_002"

  technologies:
    openai:
      description: "OpenAI関連技術"
      transcript_count: 4
      transcript_ids:
        - "transcript_001"

  use_cases:
    startup_support:
      description: "スタートアップ支援"
      transcript_count: 6
      transcript_ids:
        - "transcript_001"

  speakers:
    "[speaker1_name]":
      transcript_count: 3
      transcript_ids:
        - "transcript_001"

# タグクラウド（頻出トピック）
tag_cloud:
  - tag: "GenAI"
    count: 8
  - tag: "Startup"
    count: 6
  - tag: "LLM"
    count: 5

# 関連フレームワーク統計
framework_stats:
  - framework: "CPF"
    mention_count: 4
  - framework: "PSF"
    mention_count: 3
```

3. index.yamlの検証レポートを作成:

**ファイル名**: `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-30/index_yaml_report.md`

**内容フォーマット**:
```markdown
# index.yaml 作成完了レポート

**作成日**: 2025-12-30
**ファイルパス**: GenAI_Research/index.yaml

## インデックス統計
- **総トランスクリプト数**: X個
- **総トピックカテゴリ数**: X個
- **総テクノロジーカテゴリ数**: X個
- **総ユースケースカテゴリ数**: X個
- **総話者数**: X人

## 検索可能フィールド
- topic_tags
- technologies_mentioned
- use_cases
- related_frameworks
- speaker
- date

## 使用例

### トピックタグで検索
grep -A 20 "GenAI" GenAI_Research/index.yaml

### 関連フレームワークで検索
grep -B 5 -A 5 "CPF" GenAI_Research/index.yaml

## 検証結果
- ✅ 全トランスクリプトがインデックスに登録されている
- ✅ 全カテゴリがインデックスに反映されている
- ✅ メタデータの整合性が確認された
```

## 完了基準
GenAI_Research/index.yamlが存在し、全トランスクリプトにメタデータが付与されている

## 最終確認
以下の全6ステップの成果物が揃っていることを確認:
1. transcript_inventory.md
2. transcript_topics.md
3. genai_research_structure.md + GenAI_Research/フォルダ一式
4. transcript_metadata_report.md + GenAI_Research/transcripts/*.md
5. transcript_classification_report.md + 各カテゴリREADME.md
6. index_yaml_report.md + GenAI_Research/index.yaml
```

---

## 実行順序の推奨

### 起業の科学準拠確認タスク（T004-1 ～ T004-12）
**推奨**: 順番通りに実行（各ステップが前ステップの成果物に依存）

1. T004-1 → T004-2 → T004-3 → T004-4（構造抽出とマッピング）
2. T004-5 → T004-6 → T004-7 → T004-8（Phase1分析とフレームワーク確認）
3. T004-9 → T004-10 → T004-11 → T004-12（評価と優先順位付け）

### YouTubeトランスクリプトタスク（T005-1 ～ T005-6）
**推奨**: 順番通りに実行（各ステップが前ステップの成果物に依存）

1. T005-1 → T005-2（トランスクリプト発見とトピック抽出）
2. T005-3（フォルダ構造作成）
3. T005-4 → T005-5 → T005-6（メタデータ追加と分類・インデックス化）

---

## T006-1～T006-6: GenAI_research フォルダLLM最適化

### タスク概要

GenAI_researchフォルダをLLMが効率的に読み込めるように構造化する（6ステップ）

### 実行プロンプト

```
@/Users/yuichi/AIPM/aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/GenAI_research

【目的】
GenAI_researchフォルダをLLMが読み込みやすいように構造化し、メタデータとインデックスを作成する

【実行手順】

## STEP 1: 現状調査（T006-1）
1. GenAI_researchフォルダの構造を確認
   - ファイル一覧（ls -R）
   - ファイルサイズ（du -sh）
   - ファイル形式の分布
2. 現状レポート作成（structure_analysis.md）

## STEP 2: フォルダ構造設計（T006-2）
1. LLM最適化フォルダ構造を設計
   - topics/ - トピック別（AI技術、ビジネス応用、倫理等）
   - technologies/ - 技術別（LLM、Diffusion、RL等）
   - use_cases/ - ユースケース別（開発、マーケティング、教育等）
   - speakers/ - 話者別（専門家、企業リーダー等）
   - raw/ - 元データ保管
2. フォルダ構造図作成（folder_structure.md）

## STEP 3: メタデータ追加（T006-3）
各ファイルにYAMLフロントマターでメタデータ追加：
```yaml
---
title: "ファイルタイトル"
date: "YYYY-MM-DD"
source_url: "元のURL（あれば）"
speaker: "話者名"
tags: ["GenAI", "Startup", "ProductDev"]
summary: |
  3-5行の要約
  主要なポイントを簡潔に
key_points:
  - キーポイント1
  - キーポイント2
  - キーポイント3
  - キーポイント4
  - キーポイント5
related_frameworks:
  - "関連する起業の科学フレームワーク（あれば）"
---
```

## STEP 4: ファイル再配置（T006-4）
1. 設計したフォルダ構造を作成
2. 各ファイルを適切なカテゴリに配置
   - 複数カテゴリに該当する場合はシンボリックリンク使用
3. 元ファイルはraw/フォルダに保管

## STEP 5: インデックス作成（T006-5）
index.yamlファイル作成（全ファイルのメタデータ集約）：
```yaml
metadata_version: "1.0"
last_updated: "YYYY-MM-DD"
total_files: 100
categories:
  topics:
    - name: "AI技術"
      file_count: 25
      files:
        - path: "topics/ai_technology/file1.md"
          title: "..."
          tags: [...]
  technologies:
    - name: "LLM"
      file_count: 30
      files: [...]
  # ...
search_index:
  - keyword: "LLM"
    files: ["path1", "path2"]
  - keyword: "Fine-tuning"
    files: ["path3", "path4"]
```

## STEP 6: README作成（T006-6）
README.md作成（フォルダ使い方ガイド）：
1. フォルダ構造説明
2. メタデータフォーマット説明
3. 検索方法（タグ検索、キーワード検索）
4. LLMプロンプト例：
   - "topics/配下のAI技術関連ファイルを要約して"
   - "tags:GenAIの記事から起業の科学に関連する洞察を抽出して"

【完了条件】
- index.yamlファイルが存在する
- 全ファイルにメタデータ（タイトル、日付、タグ、要約）が付与されている
- README.mdにLLMプロンプト例が3つ以上記載されている

【納品物】
1. structure_analysis.md（現状分析レポート）
2. folder_structure.md（フォルダ構造設計図）
3. index.yaml（統合インデックス）
4. README.md（使い方ガイド）
5. 構造化されたGenAI_researchフォルダ
```

---

## T007-1～T007-6: LIFEisBeautiful 分析

### タスク概要

LIFEisBeautifulから、AIトレンド・未来社会洞察・投資手法を分析（6ステップ）

### 実行プロンプト

```
【目的】
LIFEisBeautifulのコンテンツから以下3トピックを分析：
1. AIトレンド（技術、応用事例、予測）
2. 未来社会洞察（社会変化、価値観、ライフスタイル）
3. 投資手法（投資哲学、銘柄選定、ポートフォリオ）

【実行手順】

## STEP 1: コンテンツ所在確認（T007-1）
1. LIFEisBeautifulのコンテンツを検索
   - Grep検索: `grep -r "LIFEisBeautiful" /Users/yuichi/AIPM/aipm_v0/`
   - ファイル、フォルダ、URL等を全て特定
2. コンテンツ一覧レポート作成（sources_list.md）

## STEP 2: AIトレンド抽出（T007-2）
1. AI関連コンテンツを抽出
   - キーワード: AI、機械学習、LLM、GenAI、AGI、自動化、等
2. 以下の観点で整理：
   - 現在のトレンド技術
   - 具体的な応用事例
   - 将来予測・展望
3. AIトレンドレポート作成（ai_trends.md）

## STEP 3: 未来社会洞察抽出（T007-3）
1. 未来社会関連コンテンツを抽出
   - キーワード: 未来、社会変化、価値観、ライフスタイル、働き方、等
2. 以下の観点で整理：
   - 社会構造の変化
   - 価値観・ライフスタイルの変化
   - 新しい働き方・生き方
3. 未来社会洞察レポート作成（future_society.md）

## STEP 4: 投資手法抽出（T007-4）
1. 投資関連コンテンツを抽出
   - キーワード: 投資、銘柄、ポートフォリオ、資産運用、等
2. 以下の観点で整理：
   - 投資哲学・基本方針
   - 銘柄選定基準
   - ポートフォリオ構築方法
   - リスク管理
3. 投資手法レポート作成（investment_methods.md）

## STEP 5: トピック別分析レポート作成（T007-5）
各トピックの分析レポート作成（3ファイル）：
- ai_trends_analysis.md
- future_society_analysis.md
- investment_methods_analysis.md

各レポートに含める内容：
1. エグゼクティブサマリー（3-5行）
2. 主要キーポイント（5-10個）
3. 具体例・引用（3つ以上）
4. 考察・洞察
5. 参照元リスト

## STEP 6: 統合分析レポート作成（T007-6）
integrated_analysis.md作成：
1. 3トピックの統合サマリー
2. トピック間の相互関連性
   - AIトレンド × 未来社会 の関係
   - AIトレンド × 投資手法 の関係
   - 未来社会 × 投資手法 の関係
3. 具体的アクション推奨（各トピックごとに3つ以上）
   - AI活用のアクション
   - ライフスタイル変革のアクション
   - 投資戦略のアクション

【完了条件】
- 分析レポート（3トピック以上）が存在する
- 各トピックに具体的な投資アクション推奨が記載されている
- integrated_analysis.mdに3トピック統合分析が記載されている

【納品物】
1. sources_list.md（コンテンツ一覧）
2. ai_trends_analysis.md（AIトレンド分析）
3. future_society_analysis.md（未来社会洞察分析）
4. investment_methods_analysis.md（投資手法分析）
5. integrated_analysis.md（統合分析レポート）
```

---

## T008-1～T008-11: 落合ノート分析（Pattern A + B）

### タスク概要

落合ノートからAI未来予測・トレンド・社会洞察を抽出（11ステップ）

### 実行プロンプト

```
【目的】
落合ノートから以下を分析：
- Pattern A: テーマ別抽出（AI技術、未来予測、社会変化等）
- Pattern B: 時系列分析（技術進化の変遷、予測トレンドの可視化）

【実行手順】

## ============ Pattern A: テーマ別抽出（T008-1～T008-6）============

## STEP 1: コンテンツ所在確認（T008-1）
1. 落合ノートのコンテンツを検索
   - Grep検索: `grep -r "落合" /Users/yuichi/AIPM/aipm_v0/`
   - ファイル、フォルダ、フォーマット等を全て特定
2. コンテンツ一覧レポート作成（ochiai_sources.md）

## STEP 2: 主要テーマ抽出（T008-2）
1. 全コンテンツを読み込み、主要テーマを抽出（5テーマ以上）
   例：
   - AI技術の進化
   - デジタルツイン/メタバース
   - 未来予測手法
   - 社会構造の変化
   - 人間とAIの共生
   - 教育/研究の未来
   - 都市/空間デザイン
2. テーマ一覧作成（themes_list.md）

## STEP 3: コンテンツグルーピング（T008-3）
1. 各テーマごとに関連コンテンツをグルーピング
2. テーマ別ファイルマッピング作成（theme_mapping.yaml）

## STEP 4: テーマ別フォルダ構造作成（T008-4）
1. フォルダ構造を作成
   - AI_Technology/
   - Future_Prediction/
   - Social_Change/
   - Human_AI_Symbiosis/
   - Education_Research/
   - 等（5フォルダ以上）
2. 各テーマのREADME.md作成

## STEP 5: テーマ別分析レポート作成（T008-5）
各テーマの分析レポート作成（5ファイル以上）：
- ai_technology_analysis.md
- future_prediction_analysis.md
- social_change_analysis.md
- 等

各レポートに含める内容：
1. テーマ概要（3-5行）
2. 主要ポイント（5-10個）
3. 具体例・引用（落合氏の発言から3つ以上）
4. 洞察・考察
5. 参照元リスト

## STEP 6: テーマ横断統合レポート作成（T008-6）
cross_theme_analysis.md作成：
1. 全テーマの統合サマリー
2. テーマ間の関連性マップ
3. 総合洞察（AIと社会の未来像）

## ============ Pattern B: 時系列分析（T008-7～T008-11）============

## STEP 7: 日付・時期情報抽出（T008-7）
1. 全コンテンツから日付・時期情報を抽出
2. タイムスタンプ付きコンテンツリスト作成（timeline_data.yaml）

## STEP 8: 時系列整理（T008-8）
1. コンテンツを時系列順に整理（3期間以上）
   例：
   - 過去（2010-2019）: 初期のAI/VR研究
   - 現在（2020-2024）: GenAI革命期
   - 未来（2025-2035）: AGI/シンギュラリティ予測
2. 期間別フォルダ作成（Past/Present/Future/）

## STEP 9: 期間別主要トレンド抽出（T008-9）
各期間の主要トレンド抽出：
1. 技術進化（どの技術が登場・発展したか）
2. 社会変化（どんな社会変化が起きたか/起きると予測されたか）
3. 予測の変遷（未来予測がどう変化したか）
4. 期間別トレンドレポート作成（3ファイル）

## STEP 10: 予測トレンド可視化（T008-10）
1. 3つ以上のトレンドを可視化
   例：
   - 技術進化曲線（AI性能の指数関数的成長）
   - 社会変化マップ（働き方/教育/都市の変化）
   - 未来予測チャート（AGI到達時期の予測変遷）
2. Markdown/Mermaid図で可視化
3. trend_visualizations.md作成

## STEP 11: 時系列分析レポート作成（T008-11）
timeline_analysis.md作成：
1. トレンドの変遷サマリー
2. 予測の精度検証（過去の予測と現実の比較）
3. 今後の展望（2025-2035の予測）
4. 投資/ビジネスへの示唆

【完了条件（Pattern A）】
- テーマ別抽出レポート（5テーマ以上）が存在する
- 各テーマに具体例と引用が含まれている
- cross_theme_analysis.mdが存在する

【完了条件（Pattern B）】
- 時系列レポート（3期間以上）が存在する
- 予測トレンドグラフ（3トレンド以上）が存在する
- timeline_analysis.mdが存在する

【納品物】
1. ochiai_sources.md（コンテンツ一覧）
2. themes_list.md（テーマ一覧）
3. theme_mapping.yaml（テーマ別マッピング）
4. 5テーマ以上の分析レポート
5. cross_theme_analysis.md（テーマ横断統合）
6. timeline_data.yaml（時系列データ）
7. 3期間以上のトレンドレポート
8. trend_visualizations.md（トレンド可視化）
9. timeline_analysis.md（時系列分析レポート）
```

---

## T009-1～T009-7: FounderResearch フォルダマージ

### タスク概要

2つのFounderResearchフォルダを安全にマージ（7ステップ）

### 実行プロンプト

```
【目的】
2つのFounderResearchフォルダを差分確認しながら安全にマージする

【実行手順】

## STEP 1: フォルダ所在確認（T009-1）
1. 2つのFounderResearchフォルダを検索
   ```bash
   find /Users/yuichi/AIPM/aipm_v0 -type d -name "*FounderResearch*"
   ```
2. 各フォルダのパスを記録（folder_paths.md）

## STEP 2: 内容比較（T009-2）
1. 各フォルダのファイル一覧作成
   ```bash
   ls -lR [folder1] > folder1_contents.txt
   ls -lR [folder2] > folder2_contents.txt
   ```
2. ファイル数、総サイズ、最終更新日を比較
3. 差分リスト作成
   - 両方に存在するファイル（重複）
   - フォルダ1のみ存在
   - フォルダ2のみ存在
4. 差分分析レポート作成（diff_analysis.md）

## STEP 3: マージ戦略決定（T009-3）
1. どちらをベースフォルダにするか決定
   - 最新更新日のフォルダ
   - ファイル数が多いフォルダ
   - または、新規フォルダを作成
2. ファイル名重複の解決方法決定
   - 最新ファイルを採用
   - 両方保持（ファイル名に_v1, _v2追加）
   - diff確認して手動判断
3. マージ戦略書作成（merge_strategy.md）

## STEP 4: バックアップ作成（T009-4）
1. バックアップフォルダ作成
   ```bash
   mkdir -p /Users/yuichi/AIPM/aipm_v0/Archived/FounderResearch_Backup_20251230
   ```
2. 両フォルダをタイムスタンプ付きでバックアップ
   ```bash
   cp -r [folder1] /Users/yuichi/AIPM/aipm_v0/Archived/FounderResearch_Backup_20251230/folder1
   cp -r [folder2] /Users/yuichi/AIPM/aipm_v0/Archived/FounderResearch_Backup_20251230/folder2
   ```
3. バックアップ完了確認

## STEP 5: ファイルマージ実行（T009-5）
1. ベースフォルダにユニークファイルをコピー
   ```bash
   # フォルダ2のユニークファイルをフォルダ1にコピー
   rsync -av --ignore-existing [folder2]/ [folder1]/
   ```
2. 重複ファイルの処理
   - 最新ファイルで上書き、または
   - 両方保持（ファイル名変更）
3. マージ実行ログ作成（merge_execution.log）

## STEP 6: マージ検証（T009-6）
1. 全ファイルの存在確認
   - バックアップフォルダ1のファイル数
   - バックアップフォルダ2のファイル数
   - マージ後フォルダのファイル数
   - 数式: merged_count >= max(folder1_count, folder2_count)
2. 重複確認（同名ファイルが適切に処理されているか）
3. データロス確認（消失ファイルがないか）
4. 検証レポート作成（verification_report.md）

## STEP 7: マージ完了レポート作成（T009-7）
merge_completion_report.md作成：
1. マージ戦略サマリー
2. 処理内容
   - ベースフォルダ
   - コピーしたファイル数
   - 重複処理したファイル数
3. ファイル数統計
   - フォルダ1: XXファイル
   - フォルダ2: XXファイル
   - マージ後: XXファイル
4. 差分サマリー
   - ユニークファイル: XX個
   - 重複ファイル: XX個（処理方法記載）
5. バックアップパス
6. 次のアクション（古いフォルダ削除等）

【完了条件】
- マージ完了レポートが存在する
- バックアップフォルダが存在する
- 単一のFounderResearchフォルダに統合されている
- データロスがゼロ

【納品物】
1. folder_paths.md（フォルダパス記録）
2. diff_analysis.md（差分分析）
3. merge_strategy.md（マージ戦略）
4. merge_execution.log（実行ログ）
5. verification_report.md（検証レポート）
6. merge_completion_report.md（完了レポート）
7. バックアップフォルダ（Archived/FounderResearch_Backup_20251230/）
8. 統合されたFounderResearchフォルダ
```

---

## タスク実行順序の推奨

### 並列実行可能なタスクグループ

以下のタスクグループは相互依存がないため、並列実行可能：

1. **T006（GenAI_research最適化）** - 独立実行可能
2. **T007（LIFEisBeautiful分析）** - 独立実行可能
3. **T008（落合ノート分析）** - 独立実行可能
4. **T009（FounderResearchマージ）** - 独立実行可能

### 順次実行が必要なタスク（各グループ内）

各タスクグループ内では順序依存あり：

- **T006**: 1→2→3→4→5→6の順
- **T007**: 1→2→3→4→5→6の順
- **T008**: 1→2→3→4→5→6（Pattern A）、7→8→9→10→11（Pattern B）の順
- **T009**: 1→2→3→4→5→6→7の順

---

**作成完了**: 2025-12-30 15:35
**対象タスク数**: 48個（T004: 12個 + T005: 6個 + T006: 6個 + T007: 6個 + T008: 11個 + T009: 7個）
