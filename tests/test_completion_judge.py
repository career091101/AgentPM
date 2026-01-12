"""
Completion Judge Agent 単体テスト

Week 1-2 Phase 2 実装の検証用テスト。
7フェーズ × 主要ドキュメントタイプでスコアリング成功を確認。

実行方法:
    pytest tests/test_completion_judge.py -v

成功基準:
    - 全テストケース成功
    - Phase検出精度 100%
    - スコアリング精度 90%以上（人間評価との一致率）
"""

import pytest
import json
import yaml
from pathlib import Path


# ========================================
# ヘルパー関数（仕様書からの参照実装）
# ========================================

def load_pmbok_sections():
    """pmbok_sections.yamlをロード"""
    yaml_path = Path("/Users/yuichi/AIPM/aipm_v0/docs/ai/pmbok_sections.yaml")
    with open(yaml_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# ========================================
# フィクスチャ（テストデータ）
# ========================================

@pytest.fixture
def pmbok_sections():
    """pmbok_sections.yamlデータ"""
    return load_pmbok_sections()


@pytest.fixture
def high_quality_project_charter():
    """高品質プロジェクト憲章サンプル（70点以上期待）"""
    return """
# プロジェクト憲章

## プロジェクト目的
Flow→Stock自動確定システムの構築により、ドキュメント管理を完全自動化する。

## ビジョン
品質70点以上のドキュメントを自動的にStockへ移行し、プロジェクト管理を効率化する。

## 成功基準
- 完成度スコア70点以上で自動移行
- ロールバック機能100%動作
- 並列実行で92%時間短縮達成

## ステークホルダー
- プロジェクトマネージャー: Yuichi
- 開発チーム: Claude Code Agent
- レビュアー: Review Agent

## スコープ概要
Phase 2-5の実装（10週間）
- Phase 2: Completion Judge Agent
- Phase 3: Auto Migration Agent
- Phase 4: Quality Assurance Integration
- Phase 5: Stakeholder Notification

## リスク概要
- タイムアウト頻発（対策: タイムアウト延長設定）
- Gitコンフリクト（対策: バージョン管理自動化）

## マイルストーン
- Week 1-2: Phase 2完了
- Week 3-4: Phase 3完了
- Week 5-6: Phase 4完了
- Week 7-8: Phase 5完了

## 予算概算
開発時間: 160-240時間
コスト削減: 年間378-756時間（ROI 1.15-2.62x）

## チーム体制
- PM: 1名
- Dev: 1名（Claude Agent）
- Reviewer: 1名（Review Agent）

## 前提条件
- Git 2.5以上
- tmux 3.6a以上
- Claude Code CLI

## 制約事項
- 開発期間: 10週間
- 並列実行: 最大25タスク

---
作成日: 2026-01-10
作成者: Yuichi
version: 1.0
"""


@pytest.fixture
def medium_quality_persona():
    """中品質ペルソナサンプル（60-70点期待）"""
    return """
# ペルソナ: AIプロジェクトマネージャー

## ペルソナ名
田中太郎（Tanaka Taro）

## デモグラフィック情報
- 年齢: 35歳
- 職業: プロジェクトマネージャー
- 勤務先: IT企業
- 経験年数: 10年

## 課題・ニーズ
- ドキュメント管理が煩雑で時間がかかる
- 品質チェックに毎日2時間以上費やす
- 複数プロジェクト同時進行で混乱

## 行動パターン
- 毎日複数のドキュメントをレビュー
- 週次でステータスレポート作成
- チームとの定例ミーティング実施

## ゴール
- ドキュメント管理を自動化して時間削減
- 品質を維持しつつ効率向上
- プロジェクト全体の可視化

## 技術スキル
- PMBOK基礎知識あり
- Git基本操作可能
"""


@pytest.fixture
def low_quality_wbs():
    """低品質WBSサンプル（60点未満期待）"""
    return """
# WBS

作成中...

## プロジェクト概要
詳細は後で追加します。
"""


# ========================================
# テストケース1: Phase検出精度
# ========================================

@pytest.mark.parametrize(
    "content,expected_phase",
    [
        ("プロジェクト憲章を作成する", "Initiating"),
        ("ステークホルダー登録簿を更新", "Initiating"),
        ("ペルソナ分析を実施", "Discovery"),
        ("ユーザージャーニーマップを作成", "Discovery"),
        ("仮説マップを構築", "Discovery"),
        ("競合調査を実施", "Research"),
        ("市場規模推定を行う", "Research"),
        ("WBSを作成してタスク分解", "Planning"),
        ("PRDを作成", "Planning"),
        ("プロダクトバックログを初期化", "Planning"),
        ("開発計画を策定", "Executing"),
        ("スプリントゴールを設定", "Executing"),
        ("ストーリー実装を開始", "Executing"),
        ("ステータスレポートを作成", "Monitoring"),
        ("変更要求を記録", "Monitoring"),
        ("レッスンズラーンドを記録", "Closing"),
        ("移行文書を作成", "Closing"),
    ],
)
def test_phase_detection_accuracy(content, expected_phase):
    """
    Phase検出精度テスト（17ケース）

    成功基準: 100%正確にPhase検出
    """
    # NOTE: detect_pmbok_phase関数は実装後にimport
    # from completion_judge import detect_pmbok_phase
    # phase, _ = detect_pmbok_phase(content, "test.md")
    # assert phase == expected_phase

    # 仕様書に基づくアサーション（実装後に有効化）
    pytest.skip("Implementation pending: detect_pmbok_phase function")


# ========================================
# テストケース2: ドキュメントタイプ検出
# ========================================

@pytest.mark.parametrize(
    "filename,pmbok_phase,expected_doc_type",
    [
        # Initiating
        ("project_charter.md", "Initiating", "project_charter"),
        ("stakeholder_analysis.md", "Initiating", "stakeholder_analysis"),
        # Discovery
        ("persona_pm.md", "Discovery", "persona"),
        ("user_journey_map.md", "Discovery", "user_journey_map"),
        ("assumption_map.md", "Discovery", "assumption_map"),
        # Research
        ("competitor_research.md", "Research", "competitor_research"),
        ("market_size_estimation.md", "Research", "market_size_estimation"),
        # Planning
        ("wbs.md", "Planning", "wbs"),
        ("prd.md", "Planning", "prd"),
        ("product_backlog.md", "Planning", "product_backlog"),
        # Executing
        ("development_plan.md", "Executing", "development_plan"),
        ("sprint_goal.md", "Executing", "sprint_goal"),
        # Monitoring
        ("status_report.md", "Monitoring", "status_report"),
        # Closing
        ("lessons_learned.md", "Closing", "lessons_learned"),
    ],
)
def test_document_type_detection(filename, pmbok_phase, expected_doc_type):
    """
    ドキュメントタイプ検出テスト（14ケース）

    成功基準: 主要ドキュメントタイプ90%以上正確検出
    """
    pytest.skip("Implementation pending: document type detection")


# ========================================
# テストケース3: 高品質ドキュメントスコアリング
# ========================================

def test_high_quality_project_charter(high_quality_project_charter, pmbok_sections):
    """
    高品質プロジェクト憲章のスコアリングテスト

    成功基準:
    - 総合スコア 70点以上
    - 必須セクション存在 25点以上
    - migration_eligible = true
    """
    pytest.skip("Implementation pending: calculate_completion_score function")

    # 期待される動作（実装後に有効化）
    # from completion_judge import detect_pmbok_phase, calculate_completion_score
    #
    # phase, doc_type = detect_pmbok_phase(high_quality_project_charter, "project_charter.md")
    # assert phase == "Initiating"
    # assert doc_type == "project_charter"
    #
    # score = calculate_completion_score(
    #     high_quality_project_charter, phase, doc_type, pmbok_sections
    # )
    #
    # assert score["total_score"] >= 70, f"Expected >= 70, got {score['total_score']}"
    # assert score["required_sections_present"] >= 25
    # assert score["content_quality"] >= 15
    # assert score["pmbok_compliance"] >= 10


# ========================================
# テストケース4: 中品質ドキュメントスコアリング
# ========================================

def test_medium_quality_persona(medium_quality_persona, pmbok_sections):
    """
    中品質ペルソナのスコアリングテスト

    成功基準:
    - 総合スコア 60-70点（警告付き移行）
    - migration_status = "migrate_with_warning"
    """
    pytest.skip("Implementation pending: calculate_completion_score function")


# ========================================
# テストケース5: 低品質ドキュメントスコアリング
# ========================================

def test_low_quality_wbs(low_quality_wbs, pmbok_sections):
    """
    低品質WBSのスコアリングテスト

    成功基準:
    - 総合スコア 60点未満（不合格）
    - migration_eligible = false
    - migration_status = "improve_required"
    """
    pytest.skip("Implementation pending: calculate_completion_score function")


# ========================================
# テストケース6: メタデータJSON生成
# ========================================

def test_metadata_json_generation():
    """
    メタデータJSON生成フォーマットテスト

    成功基準:
    - 必須フィールド全て存在
    - timestampがISO8601形式
    - target_stock_pathが正しいPMBOK構造
    """
    pytest.skip("Implementation pending: generate_metadata_json function")

    # 期待される出力形式（実装後に有効化）
    # metadata = {
    #     "file_path": "Flow/202601/2026-01-10/project_charter_v1.md",
    #     "pmbok_phase": "Initiating",
    #     "document_type": "project_charter",
    #     "completion_score": 85.5,
    #     "score_details": {
    #         "required_sections_present": 28.0,
    #         "content_quality": 22.5,
    #         "pmbok_compliance": 18.0,
    #         "evidence_quality": 12.0,
    #         "metadata_completeness": 5.0
    #     },
    #     "migration_eligible": True,
    #     "migration_status": "auto_migrate",
    #     "target_stock_path": "Stock/programs/test-project/documents/initiating/project_charter.md",
    #     "project_id": "test-project",
    #     "timestamp": "2026-01-10T14:30:00Z"
    # }
    #
    # # 必須フィールド確認
    # required_fields = [
    #     "file_path", "pmbok_phase", "document_type", "completion_score",
    #     "migration_eligible", "target_stock_path", "timestamp"
    # ]
    # for field in required_fields:
    #     assert field in metadata
    #
    # # timestamp形式確認（ISO8601）
    # from datetime import datetime
    # datetime.fromisoformat(metadata["timestamp"].replace("Z", "+00:00"))
    #
    # # target_stock_path構造確認
    # assert "Stock/programs/" in metadata["target_stock_path"]
    # assert "/documents/" in metadata["target_stock_path"]
    # assert metadata["pmbok_phase"].lower() in metadata["target_stock_path"]


# ========================================
# テストケース7: 必須セクション検証
# ========================================

@pytest.mark.parametrize(
    "pmbok_phase,document_type,expected_required_count",
    [
        ("Initiating", "project_charter", 7),
        ("Discovery", "persona", 5),
        ("Planning", "wbs", 5),
        ("Planning", "prd", 5),
        ("Executing", "development_plan", 5),
    ],
)
def test_required_sections_validation(
    pmbok_phase, document_type, expected_required_count, pmbok_sections
):
    """
    pmbok_sections.yamlとの整合性テスト

    成功基準:
    - 各ドキュメントタイプの必須セクション数が正確
    - min_completion_scoreが適切に設定されている
    """
    doc_spec = pmbok_sections[pmbok_phase][document_type]

    # 必須セクション数確認
    assert len(doc_spec["required_sections"]) == expected_required_count

    # min_completion_score確認（60-80の範囲）
    assert 60 <= doc_spec["min_completion_score"] <= 80


# ========================================
# テストケース8: エッジケース処理
# ========================================

def test_edge_case_empty_document():
    """
    エッジケース: 空ドキュメント

    成功基準:
    - スコア 0点
    - migration_eligible = false
    """
    pytest.skip("Implementation pending: edge case handling")


def test_edge_case_extremely_short_document():
    """
    エッジケース: 極端に短いドキュメント（100文字未満）

    成功基準:
    - スコア 15点未満
    - migration_eligible = false
    """
    pytest.skip("Implementation pending: edge case handling")


def test_edge_case_multiple_phases():
    """
    エッジケース: 複数Phaseにまたがるドキュメント

    成功基準:
    - 最も支配的なPhaseを採用
    - スコア差10%未満の場合は警告
    """
    pytest.skip("Implementation pending: edge case handling")


def test_edge_case_unknown_document_type():
    """
    エッジケース: ドキュメントタイプ未検出

    成功基準:
    - デフォルトスコアリング適用
    - 最小限の必須セクションで60点到達可能
    """
    pytest.skip("Implementation pending: edge case handling")


# ========================================
# テストケース9: YAML読み込みエラー
# ========================================

def test_yaml_loading_error_handling(tmp_path):
    """
    YAML読み込みエラーハンドリング

    成功基準:
    - FileNotFoundError時に適切なエラーメッセージ
    - YAMLError時に適切なエラーメッセージ
    """
    pytest.skip("Implementation pending: error handling")


# ========================================
# テストケース10: パフォーマンステスト
# ========================================

def test_performance_single_document():
    """
    パフォーマンステスト: 単一ドキュメント

    成功基準:
    - 1ドキュメントの評価が10秒以内
    """
    pytest.skip("Implementation pending: performance testing")


def test_performance_parallel_evaluation():
    """
    パフォーマンステスト: 並列評価

    成功基準:
    - 5ドキュメント並列評価が30秒以内
    """
    pytest.skip("Implementation pending: performance testing")


# ========================================
# 統合テスト: Week 1-2完了基準
# ========================================

def test_week_1_2_success_criteria():
    """
    Week 1-2 成功基準統合テスト

    成功基準:
    - 7フェーズ × 主要ドキュメントタイプでスコアリング成功
    - メタデータJSON生成100%成功
    - スコアリング精度90%以上（人間評価との一致率）
    """
    pytest.skip("Implementation pending: Week 1-2 integration test")

    # 検証項目:
    # 1. 全7フェーズの Phase検出成功
    # 2. 主要30+ドキュメントタイプの検出成功
    # 3. スコアリング精度 >= 90%
    # 4. メタデータJSON生成成功率 = 100%


# ========================================
# 実行サマリー
# ========================================

if __name__ == "__main__":
    print("""
    ========================================
    Completion Judge Agent 単体テスト
    ========================================

    実行方法:
        pytest tests/test_completion_judge.py -v

    テストケース概要:
        - Phase検出精度: 17ケース
        - ドキュメントタイプ検出: 14ケース
        - スコアリング: 3品質レベル
        - メタデータJSON生成: 1ケース
        - 必須セクション検証: 5ケース
        - エッジケース: 4ケース
        - エラーハンドリング: 1ケース
        - パフォーマンス: 2ケース
        - 統合テスト: 1ケース

    合計: 48テストケース

    成功基準:
        - 全テストケース成功
        - Phase検出精度 100%
        - スコアリング精度 90%以上

    注意:
        現在は仕様書として機能。実装後にテストを有効化。
    """)
