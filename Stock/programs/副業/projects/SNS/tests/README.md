# テストスイート

X & Threads同時投稿スキルのテストスイートです。

## テストファイル一覧

| ファイル | 種類 | 対象 | 実行時間 |
|---------|------|------|---------|
| `test_threads_adapter.py` | ユニットテスト | Threads Adapter | 5秒 |
| `test_late_api_scheduler.py` | ユニットテスト | Late API Scheduler | 5秒 |
| `test_integration.py` | 統合テスト | エンドツーエンド | 30秒-5分 |

## テスト実行方法

### 1. 環境準備

```bash
# 必要なパッケージをインストール
pip install pytest pytest-mock

# 環境変数を設定（統合テストのみ）
export LATE_API_KEY=sk_your_api_key_here
export LATE_TWITTER_ACCOUNT_ID=your_twitter_account_id
export LATE_THREADS_ACCOUNT_ID=your_threads_account_id
```

### 2. ユニットテスト実行

```bash
cd Stock/programs/副業/projects/SNS/tests

# すべてのユニットテストを実行
pytest test_threads_adapter.py test_late_api_scheduler.py -v

# 特定のテストクラスのみ実行
pytest test_threads_adapter.py::TestThreadsAdapter -v

# 特定のテストメソッドのみ実行
pytest test_threads_adapter.py::TestThreadsAdapter::test_merge_thread -v
```

### 3. 統合テスト実行

#### 3-1. ドライラン（Late API投稿なし）

```bash
# Late API呼び出しのみ、実際の投稿はしない
RUN_INTEGRATION_TESTS=1 pytest test_integration.py::TestIntegration::test_full_flow_dry_run -v -s
```

#### 3-2. 本番API投稿テスト（注意！）

⚠️  **警告**: このテストは実際にLate APIに投稿します。

```bash
# Sandbox環境を使用していることを確認してから実行
RUN_INTEGRATION_TESTS=1 RUN_LIVE_TESTS=1 pytest test_integration.py::TestIntegration::test_full_flow_with_live_api -v -s
```

### 4. すべてのテストを実行

```bash
# ユニットテストのみ（統合テストはスキップ）
pytest -v

# すべてのテスト（統合テスト含む）
RUN_INTEGRATION_TESTS=1 pytest -v
```

## テストカバレッジ

### Threads Adapter

| 機能 | テスト | ステータス |
|------|--------|-----------|
| スレッド結合 | ✅ | 実装済み |
| 絵文字カウント | ✅ | 実装済み |
| 口語体抽出 | ✅ | 実装済み |
| 基本的な変換 | ✅ | 実装済み |
| 文字数検証エラー | ✅ | 実装済み |
| 絵文字数検証エラー | ✅ | 実装済み |
| 空白2行検証エラー | ✅ | 実装済み |
| ハッシュタグ検証エラー | ✅ | 実装済み |

### Late API Scheduler

| 機能 | テスト | ステータス |
|------|--------|-----------|
| 環境変数初期化 | ✅ | 実装済み |
| APIキー未設定エラー | ✅ | 実装済み |
| 既存予約取得 | ✅ | 実装済み（モック） |
| 空き日検索（自動） | ✅ | 実装済み（モック） |
| 空き日検索（指定日） | ✅ | 実装済み（モック） |
| 指定日競合エラー | ✅ | 実装済み（モック） |
| 空き日なしエラー | ✅ | 実装済み（モック） |
| 401認証エラー | ✅ | 実装済み（モック） |
| 429レート制限エラー | ✅ | 実装済み（モック） |
| 予約投稿成功 | ✅ | 実装済み（モック） |
| タイムアウトリトライ | ✅ | 実装済み（モック） |

### 統合テスト

| シナリオ | テスト | ステータス |
|---------|--------|-----------|
| ドライラン（投稿なし） | ✅ | 実装済み |
| 本番API投稿 | ✅ | 実装済み（オプション） |

## トラブルシューティング

### エラー: "LATE_API_KEY not found"

**原因**: 統合テストの環境変数が設定されていません。

**対応**:
```bash
export LATE_API_KEY=sk_your_api_key_here
```

### エラー: "ModuleNotFoundError: No module named 'pytest'"

**原因**: pytestがインストールされていません。

**対応**:
```bash
pip install pytest pytest-mock
```

### エラー: "ImportError: cannot import name 'ThreadsAdapter'"

**原因**: プロジェクトルートがパスに含まれていません。

**対応**:
```bash
# testsディレクトリから実行してください
cd Stock/programs/副業/projects/SNS/tests
pytest -v
```

## CI/CD統合

GitHub Actionsでの自動テスト実行例:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install pytest pytest-mock
      - run: cd Stock/programs/副業/projects/SNS/tests && pytest test_threads_adapter.py test_late_api_scheduler.py -v
```

## ベストプラクティス

1. **ユニットテストは毎回実行**: コード変更時は必ずユニットテストを実行
2. **統合テストは慎重に**: 本番API投稿テストは Sandbox環境で実行
3. **モックを活用**: 外部API呼び出しはモックで代替（速度向上）
4. **カバレッジ測定**: `pytest --cov` でカバレッジを確認

---

**最終更新**: 2026-01-06
