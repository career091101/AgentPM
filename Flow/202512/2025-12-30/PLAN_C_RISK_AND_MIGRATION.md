# プランC: リスク管理と移行戦略 詳細ガイド

**作成日**: 2025-12-30
**対象**: プランC完全再構築プロジェクト
**バージョン**: v1.0

---

## 1. リスク管理詳細

### 1.1 リスクレジストリ

#### R1: 既存ワークフロー完全破壊 🔴

**詳細説明**:
移行時の設定ミス、参照エラー、ロジック変更により、全ツールが動作不能になるリスク。

**発生シナリオ**:
1. .cursor のパス定義が間違い、全ファイル生成先が不正
2. trigger_router.py のバグで全トリガーが無反応
3. アダプタ層の実装ミスで全ツールが SSOT を参照できない
4. 移行時に誤って本番ファイルを削除

**影響範囲**:
- ユーザー: 全員
- 機能: 全機能
- 期間: 復旧まで数時間~数日

**確率**: 中 (40%)

**影響度**: 致命的

**検知方法**:
- 自動テスト (97ケース)
- 統合テスト (各フェーズ終了時)
- カナリアデプロイ (フェーズ5)

**対策**:

1. **予防策**:
   - フェーズごとのテスト合格必須
   - コードレビュー (2名以上)
   - Git commit必須 (各フェーズ)
   - 自動テストスイート実行

2. **検知策**:
   - 統合テスト自動実行
   - Smoke Test (基本動作確認)
   - ユーザー受け入れテスト

3. **緊急対応**:
   ```bash
   # Step 1: 即座にロールバック
   git checkout pre-restructure

   # Step 2: バックアップから復元
   ./scripts/restore_backup.sh

   # Step 3: 動作確認
   ./scripts/smoke_test.sh

   # Step 4: ユーザー通知
   echo "緊急ロールバック実施。旧システムに戻しました" | ./scripts/notify_users.sh
   ```

4. **復旧手順**:
   - 所要時間: 30分
   - 責任者: DevOps Lead
   - 承認者: PM

**事後対応**:
- 根本原因分析 (RCA)
- 再発防止策の策定
- テストケース追加

---

#### R2: Cursor SPOF (Single Point of Failure) 🔴

**詳細説明**:
.cursor が唯一の真実の源となるため、.cursor の破損・削除でシステム全体が停止。

**発生シナリオ**:
1. 誤操作で .cursor/ を削除
2. Git 操作ミスで .cursor が破損
3. ディスク故障
4. マルウェア感染

**影響範囲**:
- ユーザー: 全員
- 機能: 全機能
- 期間: 復旧まで数時間

**確率**: 低 (15%)

**影響度**: 致命的

**検知方法**:
- ファイル監視ツール
- Git フック (pre-commit)
- 日次バックアップ検証

**対策**:

1. **予防策**:
   ```bash
   # 自動バックアップ (cron)
   0 2 * * * /scripts/backup_cursor.sh

   # Git フック: .cursor 削除を防止
   # .git/hooks/pre-commit
   if git diff --cached --name-only | grep -q "^.cursor/"; then
     echo "WARNING: .cursor の変更を検出。慎重に確認してください。"
     read -p "続行しますか? (y/n) " -n 1 -r
     if [[ ! $REPLY =~ ^[Yy]$ ]]; then
       exit 1
     fi
   fi
   ```

2. **検知策**:
   - ファイル監視: fswatch, inotify
   - 日次バックアップ検証
   - Git status 自動チェック

3. **冗長化**:
   - バックアップ先: 3箇所
     1. ローカル: `backup/.cursor_YYYYMMDD/`
     2. Git tag: 日次で自動タグ
     3. クラウド: Google Drive / Dropbox

4. **復旧手順**:
   ```bash
   # Step 1: 最新バックアップから復元
   cp -r backup/.cursor_20251230/ .cursor/

   # Step 2: Git から復元 (代替)
   git checkout HEAD -- .cursor/

   # Step 3: 動作確認
   ./scripts/smoke_test.sh
   ```

**復旧時間**: 15分

**事後対応**:
- バックアップ間隔を短縮 (日次 → 4時間ごと)
- 冗長化の検討 (docs/ai/lib にコアロジック分散)

---

#### R3: ツール固有カスタマイズ困難 🟡

**詳細説明**:
SSOT化により、ツール固有のカスタマイズが config.yaml とアダプタ層に限定され、柔軟性が低下。

**発生シナリオ**:
1. Antigravity固有の新機能を追加したいが、.cursor に実装する必要
2. Claude Code のエージェント特有のロジックが config.yaml で表現できない
3. ツール間の差異が大きくなり、アダプタ層が肥大化

**影響範囲**:
- ユーザー: ツール特化機能を使う一部
- 機能: 新機能追加
- 期間: 継続的

**確率**: 高 (60%)

**影響度**: 高

**検知方法**:
- ユーザーフィードバック
- 開発者からの要望

**対策**:

1. **予防策**:
   - **config.yaml の拡張性確保**:
     ```yaml
     # .agent/config.yaml
     tool: "antigravity"
     version: "v3.0"

     features:
       startup_workflows: true
       pmbok_phases: true

     custom:
       # ツール固有設定
       orchestration:
         enabled: true
         phase1_threshold: 0.8
       python_executor:
         enabled: true
         scripts_dir: ".agent/scripts/"

     extensions:
       # プラグイン機構 (将来)
       - name: "cpf_validator"
         path: ".agent/extensions/cpf_validator.py"
     ```

   - **アダプタ層の拡張**:
     ```python
     # docs/ai/lib/adapters/antigravity_adapter.py

     class AntigravityAdapter:
         def __init__(self, config):
             self.config = config
             self.custom_handlers = {}

         def register_custom_handler(self, trigger, handler):
             """ツール固有のカスタムハンドラを登録"""
             self.custom_handlers[trigger] = handler

         def execute(self, trigger, context):
             # カスタムハンドラを優先
             if trigger in self.custom_handlers:
                 return self.custom_handlers[trigger](context)
             # SSOT参照
             return self.ssot.execute(trigger, context)
     ```

2. **プラグイン機構 (Phase 2)**:
   - ツール固有ロジックを外部ファイル化
   - .agent/extensions/, .claude/extensions/
   - 動的ロード

3. **フォールバック**:
   - カスタマイズが困難な場合、ツール固有フォルダに実装を許可
   - 但し、SSOT との整合性を維持

**事後対応**:
- ユーザーフィードバックを元に config.yaml を拡張
- プラグイン機構の実装を検討

---

#### R4: 移行期間の生産性低下 🟡

**詳細説明**:
3-6ヶ月の移行期間中、新機能追加が停滞し、生産性が低下。

**発生シナリオ**:
1. 移行作業にリソースを集中し、新機能開発が停止
2. 旧システムと新システムの並行運用で混乱
3. ドキュメント不足によりユーザーが困惑

**影響範囲**:
- ユーザー: 全員
- 機能: 新機能追加の遅延
- 期間: 3-6ヶ月

**確率**: 高 (70%)

**影響度**: 中

**対策**:

1. **並行運用戦略**:
   ```yaml
   # config.yaml (全ツール共通)
   system_version: "v3"  # v2 に切り替え可能

   parallel_mode:
     enabled: true
     default_version: "v3"
     fallback_version: "v2"
   ```

2. **段階的移行**:
   - 重要度の低い機能から移行
   - クリティカルな機能は最後
   - ユーザーへの影響を最小化

3. **クイックウィン**:
   - フェーズ1完了時点で一部機能を公開
   - 早期にメリットを実感

4. **リソース配分**:
   - 移行: 70%
   - 新機能: 20%
   - バグ修正: 10%

---

#### R5: ドキュメント不足によるユーザー混乱 🟡

**詳細説明**:
移行ガイド、CHANGELOG、使い方ガイドが不十分で、ユーザーが混乱。

**対策**:

1. **必須ドキュメント**:
   - MIGRATION_GUIDE.md
   - CHANGELOG.md
   - AI_TOOLS_GUIDE.md
   - 各フォルダの README.md

2. **内容**:
   - 変更点の明示
   - 移行手順
   - トラブルシューティング
   - FAQ

3. **更新頻度**:
   - 各フェーズ完了時に更新

---

#### R6: パフォーマンス劣化 🟢

**詳細説明**:
SSOT参照により、ファイルI/Oが増加し、パフォーマンスが低下する可能性。

**対策**:

1. **キャッシング**:
   ```python
   # docs/ai/lib/core/template_engine.py

   class TemplateEngine:
       def __init__(self):
           self.cache = {}

       def load_template(self, path):
           if path in self.cache:
               return self.cache[path]

           with open(path, 'r') as f:
               template = f.read()

           self.cache[path] = template
           return template
   ```

2. **パフォーマンステスト**:
   - フェーズ4でベンチマーク
   - 目標: 現状と同等以上

---

### 1.2 リスク対応マトリックス

| リスク | 確率 | 影響 | 対応戦略 | 責任者 | 予算 |
|--------|------|------|---------|--------|------|
| R1: ワークフロー破壊 | 中(40%) | 致命的 | 回避・軽減 | Dev Lead | 高 |
| R2: Cursor SPOF | 低(15%) | 致命的 | 軽減・転嫁 | DevOps | 中 |
| R3: カスタマイズ困難 | 高(60%) | 高 | 受容・軽減 | Architect | 中 |
| R4: 生産性低下 | 高(70%) | 中 | 受容・軽減 | PM | 低 |
| R5: ドキュメント不足 | 高(60%) | 中 | 回避 | Writer | 低 |
| R6: パフォーマンス劣化 | 中(30%) | 低 | 軽減 | Dev | 低 |

**対応戦略の定義**:
- **回避**: リスクを発生させない (例: 徹底的なテスト)
- **軽減**: リスクの確率や影響を減らす (例: バックアップ)
- **転嫁**: リスクを他者に移す (例: 保険)
- **受容**: リスクを受け入れる (例: 生産性低下は一時的)

---

## 2. 移行戦略詳細

### 2.1 移行パターン

#### パターン1: Big Bang移行 (非推奨)

**方法**: 一度に全てを新システムに切り替え

**メリット**:
- 移行期間が短い
- 並行運用不要

**デメリット**:
- リスクが極めて高い
- ロールバックが困難
- ユーザーへの影響大

**判定**: ❌ **非推奨**

---

#### パターン2: 段階的移行 (推奨)

**方法**: フェーズごとに徐々に移行

**メリット**:
- リスクが管理可能
- 各フェーズでテスト可能
- ロールバックが容易

**デメリット**:
- 移行期間が長い (3-6ヶ月)
- 並行運用が必要

**判定**: ✅ **推奨**

**スケジュール**:
```
Week 1-2:   フェーズ0 (準備)
Week 3-6:   フェーズ1 (SSOT層) → 部分公開
Week 7-10:  フェーズ2 (アダプタ層) → 部分公開
Week 11-14: フェーズ3 (移行・統合) → カナリアデプロイ
Week 15-16: フェーズ4 (テスト) → フルデプロイ準備
Week 17-18: フェーズ5 (デプロイ) → フルデプロイ
```

---

#### パターン3: 並行運用移行 (推奨の補完)

**方法**: 旧システムと新システムを一時的に併存

**期間**: フェーズ3-4 (Week 11-16)

**実装**:
```yaml
# config.yaml (全ツール共通)
parallel_mode:
  enabled: true
  default_version: "v3"
  fallback_version: "v2"
  user_selectable: true
```

**ユーザー体験**:
```bash
# ユーザーが切り替え可能
export AIPM_VERSION=v2  # 旧版を使用
export AIPM_VERSION=v3  # 新版を使用 (デフォルト)
```

**メリット**:
- ユーザーが安心
- 問題発生時に即座に旧版に戻れる

**デメリット**:
- メンテナンスコストが2倍
- 混乱の可能性

---

### 2.2 移行手順詳細

#### ステップ0: バックアップ作成

```bash
#!/bin/bash
# scripts/backup_all.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backup/pre_restructure_$DATE"

echo "バックアップ作成中: $BACKUP_DIR"

# ディレクトリ作成
mkdir -p "$BACKUP_DIR"

# 全フォルダをバックアップ
cp -r .agent "$BACKUP_DIR/"
cp -r .antigravity "$BACKUP_DIR/"
cp -r .claude "$BACKUP_DIR/"
cp -r .codex "$BACKUP_DIR/"
cp -r .cursor "$BACKUP_DIR/"
cp -r docs/ai "$BACKUP_DIR/"

# Git tag作成
git tag -a "pre-restructure-$DATE" -m "バックアップ: プランC開始前"

echo "バックアップ完了: $BACKUP_DIR"
echo "Git tag: pre-restructure-$DATE"
```

---

#### ステップ1: 環境構築

```bash
#!/bin/bash
# scripts/setup_environment.sh

# Python仮想環境
python3 -m venv venv
source venv/bin/activate

# 依存パッケージ
pip install pyyaml jinja2 pytest

# ディレクトリ作成
mkdir -p docs/ai/lib/core
mkdir -p docs/ai/lib/adapters
mkdir -p docs/ai/lib/templates/shared

# .gitignore 更新
echo "venv/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore

echo "環境構築完了"
```

---

#### ステップ2: SSOT層実装 (フェーズ1)

**実装順序**:
1. `trigger_router.py` (最優先)
2. `path_resolver.py`
3. `template_engine.py`
4. `validator.py`

**trigger_router.py の骨組み**:
```python
# docs/ai/lib/core/trigger_router.py

import yaml
from pathlib import Path

class TriggerRouter:
    """トリガーワードをルーティングするコアロジック"""

    def __init__(self, ssot_root=".cursor/rules/basic"):
        self.ssot_root = Path(ssot_root)
        self.routes = self._load_routes()

    def _load_routes(self):
        """00_master_rules.mdc からルーティングテーブルをロード"""
        master_file = self.ssot_root / "00_master_rules.mdc"

        # YAMLフロントマター解析
        with open(master_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 簡易的なYAML抽出 (正式にはfrontmatterライブラリ使用)
        if content.startswith('---'):
            parts = content.split('---', 2)
            yaml_content = parts[1]
            routes = yaml.safe_load(yaml_content)
            return routes.get('trigger_routes', {})

        return {}

    def route(self, trigger_word):
        """トリガーワードから実行ファイルを決定"""
        return self.routes.get(trigger_word)

# 使用例
router = TriggerRouter()
file = router.route("プロジェクト憲章")
# -> "01_pmbok_initiating.mdc"
```

**テスト**:
```python
# tests/test_trigger_router.py

import pytest
from docs.ai.lib.core.trigger_router import TriggerRouter

def test_route_pmbok_initiating():
    router = TriggerRouter()
    result = router.route("プロジェクト憲章")
    assert result == "01_pmbok_initiating.mdc"

def test_route_task_management():
    router = TriggerRouter()
    result = router.route("タスクメモ")
    assert result == "07_task_management_v3.mdc"
```

---

#### ステップ3: アダプタ層実装 (フェーズ2)

**antigravity_adapter.py の骨組み**:
```python
# docs/ai/lib/adapters/antigravity_adapter.py

from docs.ai.lib.core.trigger_router import TriggerRouter
from docs.ai.lib.core.template_engine import TemplateEngine

class AntigravityAdapter:
    """Antigravity用のアダプタ"""

    def __init__(self, config_path=".agent/config.yaml"):
        self.config = self._load_config(config_path)
        self.router = TriggerRouter()
        self.engine = TemplateEngine()

    def _load_config(self, path):
        import yaml
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def execute(self, trigger_word, context=None):
        """トリガーワードを実行"""
        # ルーティング
        target_file = self.router.route(trigger_word)

        # SSOT参照
        ssot_path = f".cursor/rules/basic/{target_file}"

        # テンプレート適用
        output = self.engine.render(ssot_path, context)

        return output
```

---

#### ステップ4: 統合テスト (フェーズ4)

**テストケース例**:
```yaml
# tests/integration_tests.yaml

test_cases:
  - name: "PMBOK_Initiating_Antigravity"
    tool: "antigravity"
    trigger: "プロジェクト憲章"
    expected_output: "Flow/202512/2025-12-30/draft_project_charter.md"
    expected_content:
      - "# プロジェクト憲章"
      - "## プロジェクト目的"

  - name: "TaskManagement_UltraLight_Claude"
    tool: "claude"
    trigger: "タスクメモ"
    input: "企画書が進まない"
    expected_output: "Flow/202512/2025-12-30/daily_tasks.yaml"
    expected_content:
      - "inbox:"
      - "  - \"企画書が進まない\""

  # 全97ケース...
```

**自動テスト実行**:
```bash
#!/bin/bash
# scripts/run_integration_tests.sh

source venv/bin/activate

pytest tests/integration_tests.py -v --tb=short

# 成功率計算
TOTAL=$(grep "test_" tests/integration_tests.py | wc -l)
PASSED=$(pytest tests/integration_tests.py -q | grep "passed" | awk '{print $1}')
SUCCESS_RATE=$(echo "scale=2; $PASSED / $TOTAL * 100" | bc)

echo "成功率: $SUCCESS_RATE% ($PASSED/$TOTAL)"

# 合格基準: 95%以上
if (( $(echo "$SUCCESS_RATE >= 95" | bc -l) )); then
  echo "✅ 統合テスト合格"
  exit 0
else
  echo "❌ 統合テスト不合格 (95%未満)"
  exit 1
fi
```

---

### 2.3 カナリアデプロイ戦略

**対象**: フェーズ3完了後、フェーズ4開始前

**方法**:
1. **グループ分け**:
   - カナリアグループ (10%): 新システム v3
   - 通常グループ (90%): 旧システム v2

2. **設定**:
   ```yaml
   # config.yaml
   deployment:
     strategy: "canary"
     canary_percentage: 10
     canary_users:
       - "user_001"
       - "user_002"
   ```

3. **監視**:
   - エラー率
   - 実行時間
   - ユーザーフィードバック

4. **判定**:
   - 1週間問題なし → フルデプロイ
   - 問題発生 → ロールバック、修正

---

### 2.4 ロールバック手順書

#### 緊急ロールバック (即座)

```bash
#!/bin/bash
# scripts/emergency_rollback.sh

echo "🚨 緊急ロールバック開始"

# Step 1: Git tag に戻す
echo "Step 1: Git checkout"
git checkout pre-restructure

# Step 2: バックアップから復元
echo "Step 2: バックアップ復元"
LATEST_BACKUP=$(ls -t backup/pre_restructure_* | head -1)
cp -r "$LATEST_BACKUP/.agent" .agent
cp -r "$LATEST_BACKUP/.antigravity" .antigravity
cp -r "$LATEST_BACKUP/.claude" .claude
cp -r "$LATEST_BACKUP/.codex" .codex
cp -r "$LATEST_BACKUP/.cursor" .cursor

# Step 3: 動作確認
echo "Step 3: Smoke Test"
./scripts/smoke_test.sh

if [ $? -eq 0 ]; then
  echo "✅ ロールバック成功"

  # Step 4: ユーザー通知
  echo "Step 4: ユーザー通知"
  ./scripts/notify_users.sh "緊急ロールバック実施。旧システムに戻しました。"
else
  echo "❌ ロールバック失敗 - 手動介入が必要"
  exit 1
fi
```

**実行条件**:
- 重大バグ (P0) が3件以上
- システムダウン
- データ破損

**所要時間**: 30分

**責任者**: DevOps Lead

---

#### 部分ロールバック (フェーズ単位)

```bash
#!/bin/bash
# scripts/rollback_to_phase.sh

PHASE=$1  # phase1, phase2, phase3

echo "フェーズ $PHASE にロールバック"

git checkout "phase$PHASE-complete"

# 動作確認
./scripts/smoke_test.sh

if [ $? -eq 0 ]; then
  echo "✅ フェーズ $PHASE へのロールバック成功"
else
  echo "❌ ロールバック失敗"
  exit 1
fi
```

---

## 3. テスト戦略詳細

### 3.1 テストレベル

```
┌─────────────────────────────────────┐
│   E2E Test (End-to-End)             │  ← 97ケース
│   ユーザー視点の統合テスト           │
└─────────────────────────────────────┘
              ↑
┌─────────────────────────────────────┐
│   Integration Test                  │  ← 21ケース (PMBOK)
│   複数コンポーネント間のテスト       │     12ケース (タスク)
└─────────────────────────────────────┘
              ↑
┌─────────────────────────────────────┐
│   Unit Test                         │  ← 各関数ごと
│   個別関数のテスト                  │
└─────────────────────────────────────┘
```

---

### 3.2 テストケース詳細

#### Unit Test (単体テスト)

**対象**: trigger_router.py, path_resolver.py, template_engine.py, validator.py

**例**: trigger_router.py

```python
# tests/unit/test_trigger_router.py

import pytest
from docs.ai.lib.core.trigger_router import TriggerRouter

class TestTriggerRouter:
    @pytest.fixture
    def router(self):
        return TriggerRouter()

    def test_route_pmbok_initiating(self, router):
        assert router.route("プロジェクト憲章") == "01_pmbok_initiating.mdc"

    def test_route_pmbok_discovery(self, router):
        assert router.route("ペルソナ作成") == "02_pmbok_discovery.mdc"

    def test_route_task_management(self, router):
        assert router.route("タスクメモ") == "07_task_management_v3.mdc"

    def test_route_unknown_trigger(self, router):
        assert router.route("存在しないトリガー") is None

    # 全30トリガーをテスト...
```

**実行**:
```bash
pytest tests/unit/ -v --cov=docs/ai/lib/core
```

**合格基準**: カバレッジ 80%以上

---

#### Integration Test (統合テスト)

**対象**: PMBOK 7フェーズ × 3ツール = 21ケース

**例**: PMBOK Initiating

```python
# tests/integration/test_pmbok_initiating.py

import pytest
from docs.ai.lib.adapters.antigravity_adapter import AntigravityAdapter
from docs.ai.lib.adapters.claude_adapter import ClaudeAdapter
from pathlib import Path

class TestPMBOKInitiating:

    def test_antigravity_project_charter(self):
        adapter = AntigravityAdapter()
        result = adapter.execute("プロジェクト憲章", context={
            "project_name": "TestProject"
        })

        # 出力ファイル確認
        output_path = Path("Flow/202512/2025-12-30/draft_project_charter.md")
        assert output_path.exists()

        # 内容確認
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()

        assert "# プロジェクト憲章" in content
        assert "TestProject" in content

    def test_claude_project_charter(self):
        adapter = ClaudeAdapter()
        result = adapter.execute("プロジェクト憲章", context={
            "project_name": "TestProject"
        })

        # 同様の検証...

    # 全21ケース...
```

**実行**:
```bash
pytest tests/integration/ -v
```

**合格基準**: 成功率 100%

---

#### E2E Test (エンドツーエンドテスト)

**対象**: ユーザーシナリオ全体

**例**: タスク管理ワークフロー

```python
# tests/e2e/test_task_workflow.py

import pytest
from docs.ai.lib.adapters.claude_adapter import ClaudeAdapter
from pathlib import Path
import yaml

class TestTaskWorkflow:

    def test_ultra_light_full_workflow(self):
        adapter = ClaudeAdapter()

        # 1. タスクメモ
        adapter.execute("タスクメモ", context={
            "input": ["企画書が進まない", "メール返信が溜まってる"]
        })

        tasks_file = Path("Flow/202512/2025-12-30/daily_tasks.yaml")
        assert tasks_file.exists()

        with open(tasks_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        assert "企画書が進まない" in data['inbox']

        # 2. 次の一手
        adapter.execute("次の一手", context={
            "inbox_item": "企画書が進まない"
        })

        # candidates が生成されているか確認
        with open(tasks_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        assert 'candidates' in data
        assert len(data['candidates']) >= 2  # A/Bパターン

        # 3. これやる
        adapter.execute("これやる", context={
            "selected_pattern": "A"
        })

        # tasks に追加されているか確認
        with open(tasks_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        assert 'tasks' in data
        assert len(data['tasks']) >= 1

        # 4. タスクプロンプト生成
        adapter.execute("タスクプロンプト生成")

        prompts_file = Path("Flow/202512/2025-12-30/task_prompts.md")
        assert prompts_file.exists()
```

**実行**:
```bash
pytest tests/e2e/ -v --tb=short
```

**合格基準**: 成功率 95%以上

---

### 3.3 テスト自動化

**CI/CD統合** (GitHub Actions):

```yaml
# .github/workflows/test.yml

name: Test Suite

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run Unit Tests
      run: |
        pytest tests/unit/ -v --cov=docs/ai/lib/core --cov-report=xml

    - name: Run Integration Tests
      run: |
        pytest tests/integration/ -v

    - name: Run E2E Tests
      run: |
        pytest tests/e2e/ -v

    - name: Upload Coverage
      uses: codecov/codecov-action@v2
      with:
        file: ./coverage.xml
```

---

## 4. 意思決定フロー

### 4.1 Go/No-Go判定

**フェーズ4終了時に判定**:

```
┌─────────────────────────────────────┐
│  フェーズ4完了                      │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  必達条件チェック                   │
│  ✓ テスト成功率 ≥ 95%              │
│  ✓ 重大バグ (P0) = 0件             │
│  ✓ 中バグ (P1) ≤ 3件               │
│  ✓ ファイル削減率 ≥ 20%            │
│  ✓ 冗長度削減率 ≥ 60%              │
└─────────────────────────────────────┘
              ↓
        全て満たす?
           ↙  ↘
        Yes    No
         ↓      ↓
    ┌─────┐  ┌─────────────┐
    │ Go  │  │ No-Go       │
    │     │  │ フェーズ5   │
    │フェ │  │ 延期        │
    │ーズ │  │             │
    │ 5   │  │ 追加修正    │
    │実施 │  │ 後に再判定  │
    └─────┘  └─────────────┘
```

---

### 4.2 緊急判断フロー

**リスク発生時の意思決定**:

```
┌─────────────────────────────────────┐
│  リスク発生                         │
└─────────────────────────────────────┘
              ↓
      重大度評価
           ↙  ↘
    P0/致命的  P1/高
         ↓      ↓
    ┌─────┐  ┌─────────┐
    │即座に│  │1時間以内│
    │ロール│  │に判断   │
    │バック│  │         │
    └─────┘  └─────────┘
                    ↓
              修正可能?
               ↙  ↘
            Yes    No
             ↓      ↓
        ┌─────┐  ┌─────────┐
        │修正  │  │ロール    │
        │実施  │  │バック    │
        └─────┘  └─────────┘
```

---

## 5. コミュニケーション計画

### 5.1 ステークホルダー

| ステークホルダー | 役割 | 関心事 | 連絡頻度 |
|-----------------|------|--------|---------|
| **PM** | プロジェクト管理 | 進捗、リスク | 毎日 |
| **Architect** | アーキテクチャ設計 | 技術的整合性 | 週1回 |
| **Dev Team** | 実装 | タスク、技術的課題 | 毎日 |
| **QA Team** | テスト | バグ、品質 | 週2回 |
| **Users** | エンドユーザー | 使いやすさ、変更点 | 月1回 |
| **DevOps** | インフラ | デプロイ、監視 | 週1回 |

---

### 5.2 レポーティング

**週次レポート** (毎週金曜):

```markdown
# 週次レポート - Week X

## 進捗
- 完了タスク: X/Y
- フェーズ進捗: X%

## 成果物
- [成果物リスト]

## 問題・リスク
- [問題点]
- [リスク発生状況]

## 次週計画
- [予定タスク]

## KPI
- テスト成功率: X%
- ファイル削減率: X%
```

---

## 6. まとめ

プランCの成功には、**徹底的なリスク管理**と**段階的な移行戦略**が不可欠です。

**重要ポイント**:
1. ✅ フェーズごとのテスト合格必須
2. ✅ バックアップとロールバック計画の準備
3. ✅ 並行運用でユーザーへの影響を最小化
4. ✅ カナリアデプロイで問題を早期発見
5. ✅ Go/No-Go判定で品質を担保

**次のアクション**:
- 本ドキュメントをレビュー
- フェーズ0開始の承認
- リスク対策の実施

---

**作成者**: Claude Sonnet 4.5
**作成日**: 2025-12-30
**バージョン**: v1.0
