# Completion Judge Agent

Flow→Stock自動確定システムのPhase 2を担当する、ドキュメント完成度判定エージェント。

## 役割と目的

**役割**: FlowディレクトリのドキュメントをPMBOK 7フェーズに基づいて分類し、完成度を100点満点で評価して、Stock移行可否を判定する。

**目的**:
- PMBOK Phase自動検出（7フェーズ対応）
- 完成度スコアリング（5観点評価）
- メタデータJSON生成（Phase 3へのデータ連携）
- 品質ゲート判定（70点以上 = 自動移行対象）

**実行モデル**: `sonnet`（バランス重視、10分タイムアウト）

**実行方式**: Task tool経由で起動

```python
Task(
    subagent_type="general-purpose",
    model="sonnet",
    timeout=600000,  # 10分
    prompt="@.claude/agents/completion-judge-agent.md に従い評価..."
)
```

## PMBOK Phase検出ロジック

### トリガーワード辞書

ドキュメント内のキーワードを検出してPMBOK Phase決定。複数マッチの場合は最も頻出するフェーズを採用。

```python
PHASE_KEYWORDS = {
    "Initiating": {
        "primary": [
            "プロジェクト憲章", "project charter",
            "ステークホルダー登録簿", "stakeholder register",
            "プログラム定義", "program definition"
        ],
        "secondary": [
            "プロジェクト目的", "project purpose",
            "ビジョン", "vision",
            "スコープ概要", "scope overview"
        ]
    },
    "Discovery": {
        "primary": [
            "ペルソナ", "persona",
            "ユーザージャーニーマップ", "user journey map",
            "仮説マップ", "assumption map",
            "課題定義", "problem statement"
        ],
        "secondary": [
            "ユーザーストーリー", "user story",
            "ペインポイント", "pain point",
            "タッチポイント", "touchpoint"
        ]
    },
    "Research": {
        "primary": [
            "顧客調査", "customer research",
            "競合調査", "competitor research",
            "市場規模推定", "market size estimation",
            "デスクリサーチ", "desk research"
        ],
        "secondary": [
            "TAM", "SAM", "SOM",
            "インサイト", "insight",
            "調査結果", "research findings"
        ]
    },
    "Planning": {
        "primary": [
            "WBS", "work breakdown structure",
            "PRD", "product requirements document",
            "プロダクトバックログ", "product backlog",
            "リスク計画", "risk plan"
        ],
        "secondary": [
            "ワークパッケージ", "work package",
            "成果物一覧", "deliverables",
            "依存関係", "dependencies"
        ]
    },
    "Executing": {
        "primary": [
            "開発計画", "development plan",
            "ストーリー実装", "story implementation",
            "スプリントゴール", "sprint goal",
            "今日のタスク", "daily tasks"
        ],
        "secondary": [
            "アーキテクチャ", "architecture",
            "技術スタック", "tech stack",
            "デプロイメント", "deployment"
        ]
    },
    "Monitoring": {
        "primary": [
            "ステータスレポート", "status report",
            "変更要求", "change request",
            "進捗サマリー", "progress summary"
        ],
        "secondary": [
            "課題・リスク", "issues and risks",
            "KPI", "メトリクス", "metrics",
            "バーンダウンチャート", "burndown chart"
        ]
    },
    "Closing": {
        "primary": [
            "レッスンズラーンド", "lessons learned",
            "移行文書", "transition document",
            "振り返り", "retrospective"
        ],
        "secondary": [
            "成功事例", "success stories",
            "改善提案", "improvement suggestions",
            "運用手順", "operational procedures"
        ]
    }
}
```

### ドキュメントタイプ検出

Phase検出後、ファイル名とコンテンツからドキュメントタイプを特定。

```python
DOCUMENT_TYPE_PATTERNS = {
    "Initiating": {
        "project_charter": ["project_charter", "プロジェクト憲章", "charter"],
        "stakeholder_analysis": ["stakeholder", "ステークホルダー"],
        "program_definition": ["program_definition", "プログラム定義"]
    },
    "Discovery": {
        "persona": ["persona", "ペルソナ"],
        "user_journey_map": ["journey_map", "ジャーニーマップ"],
        "assumption_map": ["assumption", "仮説マップ"],
        "problem_statement": ["problem_statement", "課題定義"],
        "solution_definition": ["solution_definition", "ソリューション定義"],
        "validation_plan": ["validation_plan", "検証計画"]
    },
    "Research": {
        "customer_research": ["customer_research", "顧客調査"],
        "competitor_research": ["competitor_research", "競合調査"],
        "desk_research": ["desk_research", "デスクリサーチ"],
        "market_size_estimation": ["market_size", "市場規模"]
    },
    "Planning": {
        "wbs": ["wbs", "work_breakdown"],
        "product_backlog": ["product_backlog", "バックログ"],
        "risk_plan": ["risk_plan", "リスク計画"],
        "project_scope": ["project_scope", "スコープ記述"],
        "prd": ["prd", "product_requirements"],
        "product_roadmap": ["roadmap", "ロードマップ"]
    },
    "Executing": {
        "development_plan": ["development_plan", "開発計画"],
        "story_implementation": ["story_implementation", "ストーリー実装"],
        "sprint_goal": ["sprint_goal", "スプリント"],
        "daily_tasks": ["daily_tasks", "今日のタスク"]
    },
    "Monitoring": {
        "status_report": ["status_report", "ステータス"],
        "change_request": ["change_request", "変更要求"]
    },
    "Closing": {
        "lessons_learned": ["lessons_learned", "レッスンズラーンド"],
        "transition_document": ["transition_document", "移行文書"]
    }
}
```

### Phase検出アルゴリズム

```python
def detect_pmbok_phase(file_content: str, file_name: str) -> tuple[str, str]:
    """
    PMBOK Phaseとドキュメントタイプを検出

    Returns:
        (pmbok_phase, document_type): 例 ("Initiating", "project_charter")
    """
    # Step 1: ファイル名からヒント取得
    file_hints = []
    for phase, doc_types in DOCUMENT_TYPE_PATTERNS.items():
        for doc_type, patterns in doc_types.items():
            for pattern in patterns:
                if pattern.lower() in file_name.lower():
                    file_hints.append((phase, doc_type))

    # Step 2: コンテンツからキーワード検出
    phase_scores = {}
    for phase, keywords in PHASE_KEYWORDS.items():
        score = 0
        # Primary keywords: 10点/個
        for kw in keywords["primary"]:
            score += file_content.lower().count(kw.lower()) * 10
        # Secondary keywords: 3点/個
        for kw in keywords["secondary"]:
            score += file_content.lower().count(kw.lower()) * 3
        phase_scores[phase] = score

    # Step 3: 最高スコアのPhaseを採用
    detected_phase = max(phase_scores, key=phase_scores.get)

    # Step 4: ドキュメントタイプ特定
    if file_hints:
        # ファイル名ヒントがあれば優先
        for phase, doc_type in file_hints:
            if phase == detected_phase:
                return detected_phase, doc_type

    # ファイル名ヒントがなければコンテンツ解析
    doc_type = detect_document_type(file_content, detected_phase)

    return detected_phase, doc_type

def detect_document_type(content: str, phase: str) -> str:
    """
    ドキュメントタイプをコンテンツから特定
    """
    doc_scores = {}
    for doc_type, patterns in DOCUMENT_TYPE_PATTERNS[phase].items():
        score = 0
        for pattern in patterns:
            score += content.lower().count(pattern.lower())
        doc_scores[doc_type] = score

    # 最高スコアのドキュメントタイプを返す
    if max(doc_scores.values()) > 0:
        return max(doc_scores, key=doc_scores.get)
    else:
        # デフォルト: 各Phaseの最初のドキュメントタイプ
        return list(DOCUMENT_TYPE_PATTERNS[phase].keys())[0]
```

## 100点スコアリングシステム

### 5観点評価

完成度を5つの観点で評価し、重み付き合計で100点満点のスコアを算出。

```python
def calculate_completion_score(
    file_content: str,
    pmbok_phase: str,
    document_type: str,
    pmbok_sections_yaml: dict
) -> dict:
    """
    完成度スコアを5観点で評価

    Returns:
        {
            "required_sections_present": float,  # 30点満点
            "content_quality": float,            # 25点満点
            "pmbok_compliance": float,           # 20点満点
            "evidence_quality": float,           # 15点満点
            "metadata_completeness": float,      # 10点満点
            "total_score": float                 # 100点満点
        }
    """
    # pmbok_sections.yamlから必須セクション取得
    doc_spec = pmbok_sections_yaml[pmbok_phase][document_type]
    required_sections = doc_spec["required_sections"]
    optional_sections = doc_spec.get("optional_sections", [])

    # 観点1: 必須セクション存在（30点）
    sections_score = evaluate_required_sections(
        file_content, required_sections, optional_sections
    )

    # 観点2: コンテンツ品質（25点）
    quality_score = evaluate_content_quality(file_content)

    # 観点3: PMBOK準拠度（20点）
    compliance_score = evaluate_pmbok_compliance(
        file_content, pmbok_phase, document_type
    )

    # 観点4: エビデンス品質（15点）
    evidence_score = evaluate_evidence_quality(file_content)

    # 観点5: メタデータ完全性（10点）
    metadata_score = evaluate_metadata_completeness(file_content)

    # 総合スコア算出（重み付き合計）
    total_score = (
        sections_score * 0.30 +
        quality_score * 0.25 +
        compliance_score * 0.20 +
        evidence_score * 0.15 +
        metadata_score * 0.10
    )

    return {
        "required_sections_present": sections_score,
        "content_quality": quality_score,
        "pmbok_compliance": compliance_score,
        "evidence_quality": evidence_score,
        "metadata_completeness": metadata_score,
        "total_score": total_score
    }
```

### 観点1: 必須セクション存在（30点）

```python
def evaluate_required_sections(
    content: str,
    required_sections: list,
    optional_sections: list
) -> float:
    """
    必須セクション存在を評価（30点満点）

    採点基準:
    - 必須セクション100%存在: 30点
    - 必須セクション80%存在: 24点
    - 必須セクション60%存在: 18点
    - 必須セクション50%未満: 15点未満（不合格）
    """
    # 必須セクションの存在確認
    found_required = 0
    for section in required_sections:
        if section in content:
            found_required += 1

    required_ratio = found_required / len(required_sections)

    # 任意セクションのボーナス
    found_optional = 0
    for section in optional_sections:
        if section in content:
            found_optional += 1

    optional_bonus = min(found_optional / max(len(optional_sections), 1) * 5, 5)

    # 基礎点（必須セクション比率）
    base_score = required_ratio * 25

    # 総合点 = 基礎点 + 任意セクションボーナス
    return min(base_score + optional_bonus, 30.0)
```

### 観点2: コンテンツ品質（25点）

```python
def evaluate_content_quality(content: str) -> float:
    """
    コンテンツ品質を評価（25点満点）

    評価項目:
    - 文字数（500文字以上）: 5点
    - セクション見出し（## または ### 使用）: 5点
    - 箇条書き（- または 1. 使用）: 5点
    - 表やコードブロック存在: 5点
    - 具体的な数値・データ存在: 5点
    """
    score = 0.0

    # 文字数チェック（500文字以上）
    if len(content) >= 500:
        score += 5.0
    elif len(content) >= 300:
        score += 3.0
    elif len(content) >= 100:
        score += 1.0

    # セクション見出しチェック
    if "##" in content or "###" in content:
        score += 5.0

    # 箇条書きチェック
    if "- " in content or re.search(r"\d+\. ", content):
        score += 5.0

    # 表・コードブロックチェック
    if "|" in content or "```" in content:
        score += 5.0

    # 具体的数値・データチェック
    if re.search(r"\d+%", content) or re.search(r"\$\d+", content) or re.search(r"\d+件", content):
        score += 5.0

    return score
```

### 観点3: PMBOK準拠度（20点）

```python
def evaluate_pmbok_compliance(
    content: str,
    pmbok_phase: str,
    document_type: str
) -> float:
    """
    PMBOK準拠度を評価（20点満点）

    評価項目:
    - Phase固有キーワード存在: 10点
    - PMBOK用語の正確な使用: 5点
    - フォーマット一貫性: 5点
    """
    score = 0.0

    # Phase固有キーワード存在
    phase_keywords = PHASE_KEYWORDS[pmbok_phase]["primary"]
    keyword_count = 0
    for kw in phase_keywords:
        if kw in content:
            keyword_count += 1

    score += min(keyword_count / len(phase_keywords) * 10, 10.0)

    # PMBOK用語の正確な使用
    pmbok_terms = [
        "成果物", "deliverable",
        "ステークホルダー", "stakeholder",
        "スコープ", "scope",
        "リスク", "risk",
        "マイルストーン", "milestone"
    ]
    term_count = sum(1 for term in pmbok_terms if term in content)
    score += min(term_count / 5 * 5, 5.0)

    # フォーマット一貫性（Markdown形式）
    if content.startswith("# "):
        score += 2.5
    if "\n## " in content:
        score += 2.5

    return score
```

### 観点4: エビデンス品質（15点）

```python
def evaluate_evidence_quality(content: str) -> float:
    """
    エビデンス品質を評価（15点満点）

    評価項目:
    - 引用・参照元明記: 5点
    - データソース記載: 5点
    - 根拠となる数値・統計: 5点
    """
    score = 0.0

    # 引用・参照元明記
    if "参照:" in content or "出典:" in content or "引用:" in content:
        score += 5.0
    elif "URL" in content or "http" in content:
        score += 3.0

    # データソース記載
    if "調査結果" in content or "アンケート" in content or "インタビュー" in content:
        score += 5.0

    # 根拠となる数値・統計
    numeric_patterns = [
        r"\d+%",  # パーセンテージ
        r"\d+件",  # 件数
        r"\d+人",  # 人数
        r"\d+社",  # 社数
        r"\$\d+",  # 金額
    ]
    numeric_count = sum(1 for pattern in numeric_patterns if re.search(pattern, content))
    score += min(numeric_count * 1.5, 5.0)

    return score
```

### 観点5: メタデータ完全性（10点）

```python
def evaluate_metadata_completeness(content: str) -> float:
    """
    メタデータ完全性を評価（10点満点）

    評価項目:
    - タイトル（# 見出し）: 3点
    - 作成日時記載: 2点
    - バージョン情報: 2点
    - 作成者情報: 3点
    """
    score = 0.0

    # タイトル
    if content.startswith("# "):
        score += 3.0

    # 作成日時
    if "作成日" in content or "更新日" in content or re.search(r"\d{4}-\d{2}-\d{2}", content):
        score += 2.0

    # バージョン情報
    if "version" in content.lower() or "v1" in content.lower() or "バージョン" in content:
        score += 2.0

    # 作成者情報
    if "作成者" in content or "担当者" in content or "author" in content.lower():
        score += 3.0

    return score
```

## メタデータJSON生成

### 出力フォーマット

```python
def generate_metadata_json(
    file_path: str,
    pmbok_phase: str,
    document_type: str,
    completion_score: float,
    score_details: dict,
    project_id: str
) -> dict:
    """
    メタデータJSONを生成（Phase 3で使用）

    Returns:
        {
            "file_path": str,
            "pmbok_phase": str,
            "document_type": str,
            "completion_score": float,
            "score_details": dict,
            "migration_eligible": bool,
            "migration_status": str,
            "target_stock_path": str,
            "project_id": str,
            "timestamp": str
        }
    """
    # 移行可否判定
    if completion_score >= 70:
        migration_eligible = True
        migration_status = "auto_migrate"
    elif completion_score >= 60:
        migration_eligible = True
        migration_status = "migrate_with_warning"
    else:
        migration_eligible = False
        migration_status = "improve_required"

    # Stock移行先パス生成
    target_stock_path = f"Stock/programs/{project_id}/documents/{pmbok_phase.lower()}/{document_type}.md"

    return {
        "file_path": file_path,
        "pmbok_phase": pmbok_phase,
        "document_type": document_type,
        "completion_score": round(completion_score, 2),
        "score_details": {
            "required_sections_present": round(score_details["required_sections_present"], 2),
            "content_quality": round(score_details["content_quality"], 2),
            "pmbok_compliance": round(score_details["pmbok_compliance"], 2),
            "evidence_quality": round(score_details["evidence_quality"], 2),
            "metadata_completeness": round(score_details["metadata_completeness"], 2)
        },
        "migration_eligible": migration_eligible,
        "migration_status": migration_status,
        "target_stock_path": target_stock_path,
        "project_id": project_id,
        "timestamp": datetime.now().isoformat()
    }
```

## pmbok_sections.yamlとの統合

### YAML読み込みとキャッシュ

```python
import yaml

# キャッシュ（複数ドキュメント評価時の高速化）
_pmbok_sections_cache = None

def load_pmbok_sections() -> dict:
    """
    pmbok_sections.yamlをロードしてキャッシュ
    """
    global _pmbok_sections_cache

    if _pmbok_sections_cache is not None:
        return _pmbok_sections_cache

    yaml_path = "/Users/yuichi/AIPM/aipm_v0/docs/ai/pmbok_sections.yaml"
    with open(yaml_path, "r", encoding="utf-8") as f:
        _pmbok_sections_cache = yaml.safe_load(f)

    return _pmbok_sections_cache
```

### 必須セクション検証

```python
def validate_required_sections(
    content: str,
    pmbok_phase: str,
    document_type: str
) -> tuple[bool, list, list]:
    """
    必須セクションの存在を検証

    Returns:
        (is_valid, missing_sections, found_sections)
    """
    pmbok_sections = load_pmbok_sections()
    doc_spec = pmbok_sections[pmbok_phase][document_type]
    required_sections = doc_spec["required_sections"]

    missing = []
    found = []

    for section in required_sections:
        if section in content:
            found.append(section)
        else:
            missing.append(section)

    is_valid = len(missing) == 0

    return is_valid, missing, found
```

## 使用例

### 基本的な使用方法（Task tool経由）

```python
# orchestrate-auto-confirm スキル内での起動例
completion_judge_result = Task(
    description=f"完成度判定 - {file_path}",
    prompt=f"""
    @.claude/agents/completion-judge-agent.md の仕様に従い、以下のFlowドキュメントを評価してください。

    **ドキュメント情報**:
    - ファイルパス: `{file_path}`
    - プロジェクトID: `{project_id}`

    **実行手順**:
    1. ファイルを読み込む（Read tool）
    2. PMBOK Phaseを検出（トリガーワード辞書）
    3. ドキュメントタイプを特定
    4. 完成度スコアを5観点で評価
    5. メタデータJSONを生成して `{output_path}` に保存（Write tool）

    **出力ファイル**:
    - `{output_path}/completion_metadata.json`: メタデータJSON
    - `{output_path}/completion_report.md`: 詳細レポート

    **重要**: スコアが70点以上の場合のみ `migration_eligible: true` にしてください。
    """,
    subagent_type="general-purpose",
    model="sonnet",
    timeout=600000  # 10分
)
```

### 出力例: completion_metadata.json

```json
{
  "file_path": "Flow/202601/2026-01-10/project_charter_v1.md",
  "pmbok_phase": "Initiating",
  "document_type": "project_charter",
  "completion_score": 85.5,
  "score_details": {
    "required_sections_present": 28.0,
    "content_quality": 22.5,
    "pmbok_compliance": 18.0,
    "evidence_quality": 12.0,
    "metadata_completeness": 5.0
  },
  "migration_eligible": true,
  "migration_status": "auto_migrate",
  "target_stock_path": "Stock/programs/aipm-v3-project/documents/initiating/project_charter.md",
  "project_id": "aipm-v3-project",
  "timestamp": "2026-01-10T14:30:00Z"
}
```

### 出力例: completion_report.md

```markdown
# 完成度判定レポート

**ドキュメント**: Flow/202601/2026-01-10/project_charter_v1.md
**PMBOK Phase**: Initiating
**ドキュメントタイプ**: project_charter
**総合スコア**: 85.5/100点
**判定**: ✅ 自動移行対象（70点以上）

---

## スコア詳細

### 1. 必須セクション存在（28.0/30点）

**必須セクション（7/7個）**:
- ✅ プロジェクト目的
- ✅ ビジョン
- ✅ 成功基準
- ✅ ステークホルダー
- ✅ スコープ概要
- ✅ リスク概要
- ✅ マイルストーン

**任意セクション（2/4個）**:
- ✅ 予算概算
- ✅ チーム体制
- ❌ 前提条件
- ❌ 制約事項

**評価**: 必須セクション100%存在、任意セクション50%存在（+3点ボーナス）

### 2. コンテンツ品質（22.5/25点）

- ✅ 文字数: 1,234文字（5点）
- ✅ セクション見出し使用（5点）
- ✅ 箇条書き使用（5点）
- ✅ 表・コードブロック存在（5点）
- ⚠️  具体的数値・データ: 一部のみ（2.5点）

### 3. PMBOK準拠度（18.0/20点）

- ✅ Initiating固有キーワード（8点）
- ✅ PMBOK用語の正確使用（5点）
- ✅ Markdown形式フォーマット（5点）

### 4. エビデンス品質（12.0/15点）

- ✅ データソース記載（5点）
- ⚠️  引用・参照元: 一部のみ（3点）
- ✅ 根拠となる数値・統計（4点）

### 5. メタデータ完全性（5.0/10点）

- ✅ タイトル（3点）
- ❌ 作成日時記載（0点）
- ❌ バージョン情報（0点）
- ✅ 作成者情報（2点）

---

## 移行判定

**移行可否**: ✅ 自動移行対象
**移行先**: Stock/programs/aipm-v3-project/documents/initiating/project_charter.md
**次のアクション**: Phase 3（Auto Migration Agent）に引き継ぎ
```

## エッジケースと例外処理

### ケース1: 複数Phaseにまたがるドキュメント

```python
# 例: "WBS + リスク計画" 複合ドキュメント
# → 最も支配的なPhaseを採用（Planning）
```

**対処**: 最もキーワード出現頻度が高いPhaseを採用。スコア差が10%未満の場合は警告。

### ケース2: ドキュメントタイプ未検出

```python
# 例: カスタムドキュメント（pmbok_sections.yamlに未定義）
# → デフォルトスコアリング（緩和基準）
```

**対処**: `default_document_type` として評価、最小限の必須セクションで60点到達可能に設定。

### ケース3: 極端に短いドキュメント（100文字未満）

```python
# 例: "# プロジェクト憲章\n\n作成中..."
# → 自動不合格（15点未満）
```

**対処**: コンテンツ品質スコアが0点となり、自動的に60点未満で不合格。

### ケース4: ファイルパスからプロジェクトID抽出失敗

```python
# 例: "Flow/202601/2026-01-10/document.md"（プロジェクトID不明）
# → デフォルトプロジェクトID "unknown-project"
```

**対処**: メタデータJSONに警告フラグを追加し、Phase 3でHuman-in-the-Loop発火。

### ケース5: YAML読み込みエラー

```python
# pmbok_sections.yamlが破損または存在しない
```

**対処**:
```python
try:
    pmbok_sections = load_pmbok_sections()
except FileNotFoundError:
    raise RuntimeError(
        "CRITICAL: pmbok_sections.yaml not found at /Users/yuichi/AIPM/aipm_v0/docs/ai/pmbok_sections.yaml"
    )
except yaml.YAMLError as e:
    raise RuntimeError(f"CRITICAL: pmbok_sections.yaml parse error: {e}")
```

## 成功基準

Phase 2（Week 1-2）完了時の成功基準:

- [ ] 7フェーズ × 主要ドキュメントタイプでスコアリング成功
- [ ] メタデータJSON生成100%成功
- [ ] スコアリング精度90%以上（人間評価との一致率）
- [ ] 単体テスト100%成功（後述）

## 単体テスト

### テストケース設計（Week 1-2 Task 6）

```python
# tests/test_completion_judge.py

import pytest

# テストケース1: Initiating Phase - project_charter（高品質）
def test_high_quality_project_charter():
    content = """
    # プロジェクト憲章

    ## プロジェクト目的
    Flow→Stock自動確定システムの構築

    ## ビジョン
    品質70点以上のドキュメントを自動的にStockへ移行

    ## 成功基準
    - 完成度スコア70点以上で自動移行
    - ロールバック機能100%動作

    ## ステークホルダー
    - プロジェクトマネージャー: Yuichi
    - 開発チーム: Claude Code Agent

    ## スコープ概要
    Phase 2-5の実装（10週間）

    ## リスク概要
    - タイムアウト頻発（対策: 延長設定）

    ## マイルストーン
    - Week 1-2: Phase 2完了
    - Week 3-4: Phase 3完了

    ## 予算概算
    開発時間: 160-240時間

    ## チーム体制
    - PM: 1名
    - Dev: 1名（Claude Agent）

    作成日: 2026-01-10
    作成者: Yuichi
    version: 1.0
    """

    phase, doc_type = detect_pmbok_phase(content, "project_charter_v1.md")
    assert phase == "Initiating"
    assert doc_type == "project_charter"

    score = calculate_completion_score(content, phase, doc_type, load_pmbok_sections())
    assert score["total_score"] >= 70
    assert score["required_sections_present"] >= 25

# テストケース2: Discovery Phase - persona（中品質）
def test_medium_quality_persona():
    content = """
    # ペルソナ: AIプロジェクトマネージャー

    ## デモグラフィック情報
    - 年齢: 35歳
    - 職業: プロジェクトマネージャー

    ## 課題・ニーズ
    - ドキュメント管理が煩雑
    - 品質チェックに時間がかかる

    ## 行動パターン
    - 毎日複数のドキュメントをレビュー

    ## ゴール
    - ドキュメント管理を自動化
    """

    phase, doc_type = detect_pmbok_phase(content, "persona_pm.md")
    assert phase == "Discovery"
    assert doc_type == "persona"

    score = calculate_completion_score(content, phase, doc_type, load_pmbok_sections())
    assert 60 <= score["total_score"] < 70  # 警告付き移行レベル

# テストケース3: Planning Phase - wbs（低品質、不合格）
def test_low_quality_wbs():
    content = """
    # WBS

    作成中...
    """

    phase, doc_type = detect_pmbok_phase(content, "wbs.md")
    assert phase == "Planning"
    assert doc_type == "wbs"

    score = calculate_completion_score(content, phase, doc_type, load_pmbok_sections())
    assert score["total_score"] < 60  # 不合格
    assert score["content_quality"] < 5  # 極端に低い

# テストケース4: Phase検出精度
@pytest.mark.parametrize("content,expected_phase", [
    ("プロジェクト憲章を作成する", "Initiating"),
    ("ペルソナ分析を実施", "Discovery"),
    ("WBSを作成してタスク分解", "Planning"),
    ("開発計画を策定", "Executing"),
    ("ステータスレポートを作成", "Monitoring"),
    ("レッスンズラーンドを記録", "Closing"),
])
def test_phase_detection_accuracy(content, expected_phase):
    phase, _ = detect_pmbok_phase(content, "test.md")
    assert phase == expected_phase
```

## 参照

- @docs/ai/pmbok_sections.yaml - 必須セクション定義データ
- @.claude/agents/review-agent.md - Phase 4での品質評価エージェント
- @.claude/skills/orchestrate-auto-confirm/SKILL.md - Phase 2-5統合オーケストレーター（作成予定）
- @docs/ai/pmbok_workflow.md - PMBOKワークフロー詳細
