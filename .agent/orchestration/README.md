# ニュースレターオーケストレーションシステム

**バージョン**: 1.0
**作成日**: 2025-12-27

## 概要

`orchestrate_newsletter.md` ワークフローを自動実行するPythonベースのオーケストレーションシステム。
残り58記事のニュースレター調査を完全自動化し、2層品質保証を実施します。

## 実行方法

```bash
# フルオート実行
python orchestrator.py --full-auto

# ステータス確認
python orchestrator.py --status

# 次の1バッチのみ実行
python orchestrator.py --next-batch
```

## システム構成

- `orchestrator.py` - メインコーディネータ
- `progress_manager.py` - 進捗管理・バッチ化
- `batch_executor.py` - ワークフロー実行
- `quality_verifier.py` - 2層QA検証
- `progress_updater.py` - ファイル更新
- `report_generator.py` - レポート生成
- `config.py` - 設定・パス定義
- `utils.py` - ヘルパー関数
- `verification_rules.json` - QAルール定義

## 要件

- Python 3.8+
- anthropic SDK
- pathlib (標準ライブラリ)

## ログ

実行ログは `logs/` ディレクトリに保存されます。
