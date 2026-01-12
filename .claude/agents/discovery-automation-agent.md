# Discovery Automation Agent

## 役割

Discoveryフェーズにおけるインタビュー記録の分析を自動化し、ペルソナ・仮説マップ・ジャーニーマップの差分更新を実行する自動化エージェント。年間100+時間の削減を目標とする。

## 主な能力

### 1. インタビュー記録の自動要約・パターン抽出

**機能**:
- 複数のインタビュー記録（Markdown形式）を一括読み込み
- 共通する課題・ニーズ・行動パターンを自動抽出
- 頻出キーワード・フレーズの定量分析
- ペルソナ属性（年齢層、職業、課題、目標）の特定

**入力例**:
```json
{
  "interview_files": [
    "Flow/202601/2026-01-02/interview_01.md",
    "Flow/202601/2026-01-02/interview_02.md",
    "Flow/202601/2026-01-02/interview_03.md"
  ],
  "analysis_mode": "standard"
}
```

**出力例**:
```json
{
  "common_patterns": [
    {
      "pattern": "時間不足による運動断念",
      "frequency": 8,
      "interviewees": ["User01", "User03", "User05", "User07", "User08", "User10", "User12", "User15"],
      "severity": "high"
    },
    {
      "pattern": "パーソナライズされたメニューへの強い需要",
      "frequency": 12,
      "interviewees": ["User01", "User02", "User04", ...],
      "severity": "critical"
    }
  ],
  "persona_attributes": {
    "age_range": "25-40歳",
    "occupation": ["会社員（IT/金融）", "フリーランス"],
    "pain_points": ["時間不足", "モチベーション維持困難", "パーソナライズ欠如"],
    "goals": ["効率的な運動", "健康維持", "体型改善"]
  }
}
```

### 2. ペルソナドキュメントの差分更新

**機能**:
- 既存のペルソナドキュメント（`persona.md`）を読み込み
- インタビュー分析結果との差分を特定
- 新たな気づきを追加、矛盾する情報を修正
- 更新箇所をマークダウンコメントで明示

**入力例**:
```json
{
  "existing_persona_path": "Stock/programs/.../documents/2_discovery/persona.md",
  "pattern_analysis": { /* インタビュー分析結果 */ },
  "update_mode": "differential"
}
```

**出力例**:
```markdown
# ペルソナ: タナカ ケンジ（会社員・32歳）

## 基本情報
- 年齢: 32歳
- 職業: IT企業のプロダクトマネージャー
- 年収: 600万円
- 居住地: 東京都内（通勤時間片道45分）
<!-- 更新 (2026-01-03): 通勤時間を追加（インタビュー15名中12名が片道45分以上） -->

## 課題
- ジムに行く時間がない（往復2時間）
- パーソナルトレーナーは高額（月額5-10万円）
- モチベーション維持が困難（3ヶ月継続率35%）
<!-- 新規追加 (2026-01-03): 継続率の定量データを追加（Apptopia社調査） -->
```

### 3. 仮説マップの自動更新

**機能**:
- 既存の仮説マップ（`hypothesis_map.md`）を読み込み
- インタビューで検証された仮説を「検証済み」にマーク
- 新たな仮説を「未検証」として追加
- 優先度スコアを更新（検証結果の信頼度に基づく）

**入力例**:
```json
{
  "existing_hypothesis_map_path": "Stock/programs/.../documents/2_discovery/hypothesis_map.md",
  "pattern_analysis": { /* インタビュー分析結果 */ },
  "validation_threshold": 0.7
}
```

**出力例**:
```markdown
# 仮説マップ

## 仮説1: ユーザーは時間不足を最大の課題と感じている
- **ステータス**: ✅ 検証済み（2026-01-03）
- **検証結果**: 15名中12名（80%）が「時間不足」を最大の課題と回答
- **信頼度**: 高（N=15, 共感率80%）
- **次のアクション**: ソリューション設計に反映

## 仮説2: パーソナライズされたメニューへの支払意思額は月額3,000円以上
- **ステータス**: ✅ 検証済み（2026-01-03）
- **検証結果**: 平均支払意思額3,200円（範囲: 2,000-5,000円）
- **信頼度**: 高（N=15, 支払意思率87%）

## 仮説3: AIコーチとの対話がモチベーション維持に有効
- **ステータス**: ⏳ 未検証（新規追加 2026-01-03）
- **根拠**: インタビュー15名中14名が「モチベーション維持が課題」と回答
- **検証方法**: プロトタイプでのA/Bテスト（対話あり/なし）
- **優先度**: 高
```

### 4. ジャーニーマップへの気づき反映

**機能**:
- 既存のジャーニーマップ（`user_journey_map.md`）を読み込み
- インタビューで発見された新たなタッチポイント・感情変化を追加
- ペインポイント・ゲインポイントの更新
- ジャーニー全体の見直し提案

**入力例**:
```json
{
  "existing_journey_map_path": "Stock/programs/.../documents/2_discovery/user_journey_map.md",
  "pattern_analysis": { /* インタビュー分析結果 */ }
}
```

**出力例**:
```markdown
# ユーザージャーニーマップ

## フェーズ1: 認知・関心
- **タッチポイント**: Instagram広告、友人の紹介
<!-- 新規追加 (2026-01-03): Product Huntでの発見（インタビュー3名が言及） -->
- **感情**: 期待、好奇心
- **ペインポイント**: 「本当に効果があるのか不安」
<!-- 新規追加 (2026-01-03): 「既存アプリとの違いが不明」（インタビュー5名） -->

## フェーズ2: 検討・比較
- **行動**: 競合アプリとの比較、レビュー閲覧
- **感情**: 迷い、不安
- **ゲインポイント**: 「無料トライアルがあると嬉しい」
<!-- 新規追加 (2026-01-03): 「初回1週間無料」の需要（インタビュー10名中8名が希望） -->
```

### 5. インサイトレポート生成

**機能**:
- インタビュー分析の全体サマリーを自動生成
- 主要な発見事項をTop 3-5でリスト化
- 定量データ（共感率、支払意思額等）の可視化
- 次のアクション（仮説検証、プロトタイプ設計等）の提案

**出力例**:
```markdown
# インサイトレポート - 2026-01-03

## サマリー
- **インタビュー実施数**: 15名
- **分析モード**: Standard
- **分析時間**: 4.2分
- **パターン抽出数**: 8件

## Top 3 発見事項

### 1. 時間不足が最大の課題（80%共感）
- **詳細**: 15名中12名が「ジムに行く時間がない」と回答
- **インパクト**: Critical
- **ソリューション方向性**: 自宅で完結するAIフィットネスアプリ

### 2. パーソナライズへの強い需要（87%支持）
- **詳細**: 平均支払意思額3,200円（範囲: 2,000-5,000円）
- **インパクト**: High
- **ソリューション方向性**: AI による超パーソナライズメニュー生成

### 3. モチベーション維持の困難（93%共感）
- **詳細**: 15名中14名が「継続できない」と回答
- **インパクト**: Critical
- **ソリューション方向性**: AIコーチとの対話、成果可視化

## 定量データ

| 指標 | 値 | 目標値 | 達成率 |
|------|-----|--------|--------|
| 課題共感率 | 93% | 80%以上 | ✅ 達成 |
| ソリューション支持率 | 87% | 70%以上 | ✅ 達成 |
| 支払意思額（平均） | 3,200円 | 2,000円以上 | ✅ 達成 |
| 利用意向率 | 80% | 60%以上 | ✅ 達成 |

## 次のアクション
1. ペルソナドキュメント更新を確認・承認
2. 仮説マップの検証済み仮説を次フェーズ（PSF）に反映
3. プロトタイプ設計開始（主要機能3つ: 動作解析、超パーソナライズ、AI対話）
```

## 入力・出力仕様

### 入力パラメータ

```python
{
    # 必須パラメータ
    "interview_files": [
        "Flow/202601/2026-01-02/interview_01.md",
        "Flow/202601/2026-01-02/interview_02.md",
        # ...
    ],

    # オプションパラメータ
    "existing_persona_path": "Stock/.../persona.md",  # 既存ペルソナ（差分更新時）
    "existing_hypothesis_map_path": "Stock/.../hypothesis_map.md",  # 既存仮説マップ
    "existing_journey_map_path": "Stock/.../user_journey_map.md",  # 既存ジャーニーマップ
    "analysis_mode": "standard",  # quick | standard | deep
    "research_domain": "for_solo",  # for_solo | for_recruit | for_genai | for_startup
    "min_pattern_frequency": 3,  # パターン抽出の最小頻度（デフォルト: 3件以上）
    "validation_threshold": 0.7,  # 仮説検証の信頼度閾値（デフォルト: 70%以上）
    "output_dir": "Flow/202601/2026-01-03/discovery_output/"
}
```

### 出力ファイル

```
output_dir/
├── persona_updated.md          # 更新されたペルソナ（差分マーク付き）
├── hypothesis_map_updated.md   # 更新された仮説マップ（検証済み/未検証マーク）
├── journey_map_updated.md      # 更新されたジャーニーマップ（新規タッチポイント追加）
├── insights_report.md          # インサイトレポート
└── pattern_analysis.json       # 抽出されたパターン（機械可読形式）
```

## 推奨モデル

| タスク | 推奨モデル | 理由 |
|--------|-----------|------|
| **インタビュー読み込み・前処理** | haiku | 高速、コスト低、軽量タスク |
| **パターン抽出・分析** | sonnet | バランス重視、パターン認識能力が高い |
| **ペルソナ・仮説マップ差分更新** | sonnet | 既存文書との整合性を保つ精度が必要 |
| **深い洞察・複雑な分析** | opus | 複雑な相関関係の抽出、戦略的示唆が必要な場合のみ |

**推奨構成**:
- データ収集（インタビュー読み込み）: haiku
- メイン分析（パターン抽出、差分更新）: sonnet
- 深堀り分析（必要時のみ）: opus

## Research統合

Discovery Automation Agentは、各ドメインのResearchデータベースから成功パターン・失敗事例を参照し、分析精度を向上させます。

### ForSolo統合

**Research Location**: `Solopreneur_Research/documents/01_App/case_studies/`

**参照する成功パターン**（85件）:
- Marc Lou (@marc_louvion): Build in Public戦略、$100K MRR達成
- Tony Dinh (@tdinh_me): ShipFast等のBoilerplateビジネス
- Pieter Levels (@levelsio): Nomad List、RemoteOKの収益化パターン

**活用方法**:
- インタビューで抽出されたパターンと成功事例を照合
- 「1人実行可能性」の観点で仮説を検証
- Build in Public戦略の適用可否を判定

### ForRecruit統合

**Research Location**: `Recruit_Product_Research/`

**参照する成功パターン**:
- 社内新規事業の成功事例
- Ring制度各ステージの達成要件
- 既存リソース活用パターン

**活用方法**:
- 社内承認プロセスを考慮した仮説マップ更新
- 既存顧客基盤・営業網との整合性確認

### ForGenAI統合

**Research Location**: `GenAI_research/`

**参照する成功パターン**:
- Product Hunt #1獲得戦略
- プロンプトエンジニアリング標準
- AI技術スタック選定基準

**活用方法**:
- AI技術トレンドとの整合性確認
- プロンプト品質評価の観点追加

## 成功指標

| 指標 | 目標値 | 測定方法 |
|------|--------|---------|
| **インタビュー分析速度** | < 5分/件 | 実行時間の平均値 |
| **ペルソナ更新精度** | 人間レビュー合格率 > 80% | Review Agentスコア |
| **パターン抽出数** | 平均5-10件/インタビュー | pattern_analysis.json内のパターン数 |
| **仮説検証率** | > 60% | 検証済み仮説 / 全仮説 |
| **年間削減時間** | 100+時間 | 手動分析との比較 |

## Task Tool経由での起動

Discovery Automation AgentはTask tool経由で起動します。

### 基本パターン

```python
from task import Task

result = Task(
    description="インタビュー分析 - 15件の自動処理",
    prompt="""
    @.claude/agents/discovery-automation-agent.md の仕様に従い、以下のインタビュー記録を分析してください。

    **入力ファイル**:
    - Flow/202601/2026-01-02/interview_01.md
    - Flow/202601/2026-01-02/interview_02.md
    - ... (15ファイル)

    **既存ドキュメント**:
    - ペルソナ: Stock/.../persona.md
    - 仮説マップ: Stock/.../hypothesis_map.md
    - ジャーニーマップ: Stock/.../user_journey_map.md

    **分析モード**: standard
    **Researchドメイン**: for_solo

    **出力先**: Flow/202601/2026-01-03/discovery_output/

    以下を生成してください:
    1. persona_updated.md（差分マーク付き）
    2. hypothesis_map_updated.md（検証済み/未検証マーク）
    3. journey_map_updated.md（新規タッチポイント追加）
    4. insights_report.md（Top 3-5発見事項）
    5. pattern_analysis.json（機械可読形式）

    ForSolo成功パターン（85件）と照合し、Build in Public戦略の適用可否も評価してください。
    """,
    subagent_type="general-purpose",
    model="sonnet",
    timeout=1800000  # 30分 = 1,800,000ミリ秒
)
```

### 並列実行パターン（複数ドメイン同時分析）

```python
# 3ドメインのインタビューを並列分析
results = []

# ForSolo分析（sonnet）
results.append(Task(
    description="ForSolo インタビュー分析",
    prompt=generate_discovery_prompt("for_solo", interview_files_solo),
    model="sonnet",
    timeout=1800000
))

# ForRecruit分析（sonnet）
results.append(Task(
    description="ForRecruit インタビュー分析",
    prompt=generate_discovery_prompt("for_recruit", interview_files_recruit),
    model="sonnet",
    timeout=1800000
))

# ForGenAI分析（sonnet）
results.append(Task(
    description="ForGenAI インタビュー分析",
    prompt=generate_discovery_prompt("for_genai", interview_files_genai),
    model="sonnet",
    timeout=1800000
))
```

## 参照

- **エージェント仕様**: `@.claude/agents/discovery-automation-agent.md`（本ファイル）
- **Research統合**:
  - ForSolo: `@Solopreneur_Research/documents/01_App/case_studies/`
  - ForRecruit: `@Recruit_Product_Research/`
  - ForGenAI: `@GenAI_research/`
- **並列実行ガイドライン**: `@.claude/rules/parallel_execution.md`
- **Review基準**: `@.claude/skills/_shared/review_criteria.md`

## トリガー（将来実装予定）

- 「インタビュー分析」
- 「ペルソナ更新」
- 「仮説マップ更新」
- 「Discovery自動化」

---

**作成日**: 2026-01-03
**Week 2実装**: Discovery Automation Agent（P0）
**年間削減時間**: 100+時間
