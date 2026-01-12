# Knowledge Base

Compounding Engineering ナレッジベース

## 概要

このディレクトリは、週次品質レポートから自動抽出されたナレッジを蓄積するための領域です。

### ディレクトリ構造

```
.claude/knowledge/
├── README.md (このファイル)
├── success_patterns/ - 成功パターン
├── failure_patterns/ - 失敗パターン
└── best_practices/ - ベストプラクティス
```

## 自動抽出ルール

### success_patterns/ - 成功パターン

以下の条件で自動抽出：
- カテゴリスコアが **10点以上改善** した場合
- 総合スコアが **90点以上** (優秀レベル) に到達した場合

**ファイル形式**: `success_YYYYMMDD.json`

**内容例**:
```json
{
  "date": "2026-01-04T10:00:00",
  "improvements": [
    {
      "category": "code_quality",
      "previous": 75.5,
      "current": 87.2,
      "improvement": 11.7
    }
  ],
  "best_practices": [
    "週次品質スコアが92点を達成（優秀レベル）",
    "code_quality/コードカバレッジが95点達成"
  ]
}
```

### failure_patterns/ - 失敗パターン

以下の条件で自動抽出：
- カテゴリスコアが **10点以上低下** した場合
- 2週連続でスコアが低下した場合

**ファイル形式**: `failure_YYYYMMDD.json`

**内容例**:
```json
{
  "date": "2026-01-04T10:00:00",
  "degradations": [
    {
      "category": "test_quality",
      "previous": 85.0,
      "current": 72.5,
      "degradation": -12.5
    }
  ]
}
```

### best_practices/ - ベストプラクティス

週次レポートから抽出されたベストプラクティスを手動でまとめたMarkdownファイルを格納。

**ファイル形式**: `{topic}.md`

**トピック例**:
- `code_coverage.md` - コードカバレッジ向上手法
- `cyclomatic_complexity.md` - 循環的複雑度削減手法
- `documentation.md` - ドキュメント品質向上手法
- `security.md` - セキュリティ改善手法
- `git_workflow.md` - Gitワークフロー改善手法

## 活用方法

### 1. 週次レビュー会議での活用

```bash
# 直近1ヶ月の成功パターンを確認
ls -lt .claude/knowledge/success_patterns/ | head -5

# 成功パターンの内容確認
cat .claude/knowledge/success_patterns/success_20260104.json | jq
```

### 2. 改善計画策定時の参照

過去の成功パターンを参照して、効果的な改善策を立案。

```bash
# code_quality改善の成功例を検索
grep -r "code_quality" .claude/knowledge/success_patterns/
```

### 3. CLAUDE.mdへの統合

優れたベストプラクティスは、定期的にCLAUDE.mdに統合。

```bash
# 週次更新スクリプト実行
bash scripts/update_claude_md.sh
```

## メンテナンス

### 定期クリーンアップ

90日以上経過したナレッジファイルは定期的にアーカイブ：

```bash
# 90日以上経過したファイルを削除
find .claude/knowledge/ -name "*.json" -mtime +90 -delete
```

### ベストプラクティス統合

月次レビュー会議で、成功パターンから共通要素を抽出し、`best_practices/`に統合。

## 参照

- 週次品質レポート: `scripts/weekly_quality_report.py`
- 品質測定: `scripts/measure_quality.py`
- 品質指標定義: `.claude/config/quality_metrics.json`
