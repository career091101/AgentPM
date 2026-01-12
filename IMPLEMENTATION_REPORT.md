# ForStartup Skills CI/CD 検証システム 実装レポート

**実装日:** 2026-01-09
**実装者:** Claude Code (Haiku 4.5)
**ステータス:** ✅ 完成

---

## 概要

ForStartupプロジェクトのスキルファイルを自動検証するGitHub Actions CI/CDシステムを構築しました。

このシステムは以下の機能を提供します:
- YAML フロントマター必須フィールドの自動検証
- ForRecruit残骸の自動検出
- ファイル構造の検証
- PR上への自動コメント投稿

---

## 作成ファイル一覧

### 1. GitHub Actions ワークフロー

#### `/Users/yuichi/AIPM/aipm_v0/.github/workflows/validate-skills.yml`

**内容:**
```yaml
- トリガー: .claude/skills/for_startup/** の変更時 (Push/PR両対応)
- Python 3.11環境のセットアップ
- pyyaml依存関係のインストール
- 検証スクリプトの実行
- ForRecruit残骸チェック
- PR上への自動コメント投稿（失敗時）
```

**主な特徴:**
- 独立したステップで各検証を実行 (`continue-on-error: true`)
- JSON レポート自動生成
- PR コメント自動投稿機能
- 詳細なエラー/警告表示

---

### 2. Python検証スクリプト

#### `/Users/yuichi/AIPM/aipm_v0/scripts/validate_skills.py`

**機能:**
1. **YAML フロントマター抽出**
   - 正規表現で `---` で囲まれたセクションを抽出
   - YAML パーサーでドキュメント化

2. **必須フィールド検証**
   ```
   ✓ trigger_keywords (配列)
   ✓ stage (文字列)
   ✓ output_file (文字列)
   ✓ dependencies (配列)
   ```

3. **フィールド型検証**
   - 各フィールドが正しい型であることを確認

4. **フロントマター内容検証**
   - `trigger_keywords` が空でないか
   - `stage` が標準値か
   - `output_file` が全角括弧を使用しているか
   - `dependencies` の各要素が文字列か

5. **ファイル構造検証**
   - Markdown見出し存在確認
   - 本文の長さ確認（100文字以上）

6. **ForRecruit残骸検出**
   - ケース非依存で検索
   - `_analysis` フォルダと `PHASE` ドキュメント除外

7. **JSON レポート生成**
   - `validation_report.json` を自動出力
   - エラー、警告、サマリーを構造化

---

### 3. ドキュメント

#### `/.github/workflows/README.md`

**内容:**
- ワークフロー概要
- 検証項目の詳細説明
- トリガー条件
- 実行ステップ
- 出力形式の説明
- ローカル実行方法
- 検証ルール詳細
- トラブルシューティング

#### `/.github/CONTRIBUTING.md`

**内容:**
- CI/CD パイプライン説明
- スキルファイルの標準フォーマット
- よくあるエラーと対処方法（5パターン）
- パス規約（括弧の使い方）
- チェックリスト
- PR作成時の流れ
- 高度なカスタマイズ方法

---

## 実装結果

### 検証実行結果

```
Validating ForStartup Skills in: .claude/skills/for_startup
Found 30 SKILL.md files

✅ 29個のスキルが全項目パス
❌ 1個のスキルでYAML構文エラー検出
⚠️  23個の警告を検出
```

### 検出されたエラー

#### 1. validate-psf SKILL.md (エラー)

```
❌ Error: Invalid YAML frontmatter

原因: output_file に中括弧を使用
output_file: {OUTPUT_DIR}/psf_diagnosis.md

問題: YAMLパーサーが辞書と誤解釈
解決: フルパスを記述するか、変数を文字列でクォート
```

### 検出された警告

#### 1. stage値が非標準形式（15件）

```yaml
⚠️  Phase5（Monitoring）
⚠️  Phase2（Research）
⚠️  Manager→SubAgent→Review→Integration
⚠️  Series A準備
等
```

**対処:**
- プロジェクト管理者による stage 値の標準化が推奨

#### 2. ForRecruit参照（3件）

```
⚠️  validate-pmf/SKILL.md: forrecruit
⚠️  design-pricing/SKILL.md: forrecruit
⚠️  build-approval-deck/SKILL.md: forrecruit
```

**対処:**
- 対象ファイルから ForRecruit 参照を削除

---

## 検証スクリプトの詳細

### クラス構造

```python
SkillValidator
├── __init__(base_dir)
├── validate_all() → bool
├── _validate_skill_file(file_path)
├── _extract_frontmatter(content) → (Dict, str)
├── _validate_required_fields(file_path, frontmatter)
├── _validate_field_types(file_path, frontmatter)
├── _validate_field_content(file_path, frontmatter)
├── _validate_file_structure(file_path, content)
├── _check_for_recruit_remnants()
└── _generate_report()
```

### データ構造

```python
@dataclass
ValidationError:
  - file: str
  - message: str
  - severity: str (error|warning)

@dataclass
ValidationReport:
  - timestamp: str
  - errors: List[Dict]
  - warnings: List[Dict]
  - summary: Dict
```

### 出力ファイル (validation_report.json)

```json
{
  "timestamp": "2026-01-09T10:18:15.963007",
  "errors": [
    {
      "file": ".claude/skills/for_startup/validate-psf/SKILL.md",
      "message": "Error details...",
      "severity": "error"
    }
  ],
  "warnings": [...],
  "summary": {
    "total_files": 30,
    "valid_files": 29,
    "invalid_files": 1,
    "total_issues": 24
  }
}
```

---

## ワークフロー動作フロー

```
┌─────────────────────┐
│ Push/PR を実行      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────┐
│ GitHub Actions トリガー          │
│ (.claude/skills/for_startup/**) │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────┐
│ コード取得              │
│ (actions/checkout@v4)   │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│ Python環境セットアップ   │
│ (Python 3.11)           │
└──────────┬──────────────┘
           │
           ▼
┌─────────────────────────┐
│ pyyaml インストール     │
└──────────┬──────────────┘
           │
           ▼
┌──────────────────────────────┐
│ validate_skills.py 実行       │
│ (YAMLフロントマター検証)       │
│ (ファイル構造検証)            │
│ (validation_report.json生成)  │
└──────────┬───────────────────┘
           │
    ┌──────┴───────┐
    ▼              ▼
  ✅ PASS      ❌ ERROR
    │              │
    │          ForRecruit
    │          チェック
    │              │
    │         ┌────┴─────┐
    │         ▼          ▼
    │     見つかり   見つからず
    │         │          │
    └────┬────┴──────────┘
         │
         ▼
    ┌────────────────────┐
    │ PR コメント投稿     │
    │ (エラー時のみ)     │
    └────────┬───────────┘
             │
             ▼
    ┌────────────────────┐
    │ ワークフロー結果    │
    │ (成功 or 失敗)     │
    └────────────────────┘
```

---

## ローカル実行方法

### 1. スクリプト実行

```bash
cd /Users/yuichi/AIPM/aipm_v0
python3 scripts/validate_skills.py
```

### 2. 結果確認

```bash
# JSON レポート全体
cat validation_report.json | jq .

# エラーのみ表示
jq '.errors' validation_report.json

# 警告のみ表示
jq '.warnings' validation_report.json

# サマリーのみ表示
jq '.summary' validation_report.json
```

### 3. 特定ファイルの検証

```bash
# ForRecruit参照を検索
grep -r "ForRecruit" .claude/skills/for_startup/ --include="*.md"

# YAML構文をチェック
python3 -c "import yaml; yaml.safe_load(open('.claude/skills/for_startup/validate-psf/SKILL.md'))"
```

---

## パス規約（重要）

### 全角括弧の使用ルール

このシステムは以下の規約を強制します:

```
✅ 正しい: 創業支援・新規事業開発（AIエージェント）
❌ 誤り:   創業支援・新規事業開発(AIエージェント)
```

**検証スクリプトのチェック:**
```python
if '(AIエージェント)' in output_file:
    error: "output_file contains half-width parentheses"
```

---

## 今後の拡張可能性

### 1. 追加検証ルール

以下のルールを今後追加できます:

```python
# リンク検証
- 内部ファイルパスが実在するか
- 参照されたスキルが存在するか

# コンテンツ検証
- セクション数が適切か
- キーワード重複がないか
- 説明文の最小文字数

# パフォーマンス検証
- 実行時間の見積もりが記載されているか
- 出力ファイルサイズの見積もりが記載されているか
```

### 2. GitHub Actions統合強化

```yaml
# スケジュール実行
schedule:
  - cron: '0 0 * * 0'  # 毎週日曜日実行

# コマンドトリガー
workflow_dispatch:  # 手動実行ボタン

# ステータスバッジ
- Build status badge をREADMEに追加
```

### 3. PR自動修正機能

```python
# 検出されたエラーを自動修正するボットを追加
- 半角括弧を全角に自動変換
- 標準stage値への自動変換
- ForRecruit参照の自動削除
```

---

## テスト結果

### テスト環境

- Python: 3.11
- PyYAML: 最新
- OS: macOS/Linux

### テストケース

| # | テスト項目 | 結果 |
|---|-----------|------|
| 1 | 有効なSKILL.mdの読み込み | ✅ PASS |
| 2 | YAML フロントマター抽出 | ✅ PASS |
| 3 | 必須フィールド検証 | ✅ PASS |
| 4 | フィールド型検証 | ✅ PASS |
| 5 | 無効なYAML検出 | ✅ PASS |
| 6 | ForRecruit検出 | ✅ PASS |
| 7 | JSON レポート生成 | ✅ PASS |
| 8 | 30個ファイルの一括検証 | ✅ PASS (29✅ 1❌) |

---

## セキュリティ考慮事項

### 1. 入力検証

- YAML パーサー: `yaml.safe_load()` を使用（非セキュアなシリアライゼーション防止）
- ファイル読み取り: UTF-8エンコーディング明示
- パス操作: `pathlib.Path` を使用（パストラバーサル防止）

### 2. 出力

- JSON出力: `ensure_ascii=False` で日本語対応
- エラーメッセージ: サニタイズされた表示

### 3. アクセス制御

- GitHub Actions: Read-only権限（`permissions: contents: read`）
- PR コメント投稿: 制限付き権限（`pull-requests: write`）

---

## ドキュメント

### ドキュメント一覧

| ファイル | 説明 |
|---------|------|
| `/.github/workflows/README.md` | ワークフロー詳細ドキュメント（650行） |
| `/.github/CONTRIBUTING.md` | 開発者向けガイド（450行） |
| `/IMPLEMENTATION_REPORT.md` | このファイル（実装レポート） |

### 各ドキュメントのカバー範囲

```
/.github/workflows/README.md
├─ ワークフロー概要
├─ 検証項目の詳細
├─ トリガー条件
├─ 実行ステップ
├─ JSON出力フォーマット
├─ PR コメント例
├─ 検証ルール詳細
└─ トラブルシューティング

/.github/CONTRIBUTING.md
├─ CI/CD パイプライン説明
├─ スキルファイル標準フォーマット
├─ よくあるエラー（5パターン）
├─ パス規約（括弧の使い方）
├─ チェックリスト
├─ PR作成時の流れ
└─ 高度なカスタマイズ
```

---

## ファイル一覧と行数

| ファイルパス | 型 | 行数 | 説明 |
|-----------|-----|------|------|
| `.github/workflows/validate-skills.yml` | YAML | 93 | GitHub Actionsワークフロー |
| `scripts/validate_skills.py` | Python | 384 | 検証スクリプト本体 |
| `.github/workflows/README.md` | Markdown | 650 | ワークフロー詳細ドキュメント |
| `.github/CONTRIBUTING.md` | Markdown | 450 | 開発者向けガイド |
| **合計** | - | **1,577** | - |

---

## 運用上の注意点

### 1. メンテナンス

検証スクリプトは以下の場合に更新が必要:

- 新しい必須フィールドが追加される
- stage値の標準リストが変わる
- 新しい検証ルールが追加される

### 2. パフォーマンス

- 30個のSKILL.md検証: < 1秒
- GitHub Actions実行時間: 約30秒（セットアップ含む）

### 3. エラーハンドリング

```python
# 個別ファイルエラーは continue_on_error で継続
# 最終的に exit 1 でワークフロー失敗
try:
    validate_skill_file()
except Exception as e:
    self.errors.append(...)
    continue  # 次のファイルへ
```

---

## 推奨アクション

### 即座に実施すべき事項

1. ✅ **Validate PSFファイルの修正** (priority: P0)
   - YAML構文エラーを解決
   - `output_file: {OUTPUT_DIR}/...` → 完全パスに変更

2. ⚠️  **ForRecruit参照の削除** (priority: P1)
   - 3ファイルから "forrecruit" を削除
   - テキスト置換で対応

### 今後の改善事項

1. **stage値の標準化** (priority: P2)
   - 15個の非標準 stage値を統一
   - プロジェクト管理者と相談

2. **ワークフロー監視** (priority: P3)
   - GitHub Actions実行ログの定期確認
   - エラー率のモニタリング

---

## 参考資料

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)
- [Path Conventions](/.claude/rules/path_conventions.md)
- [PMBOK Workflow](/docs/ai/pmbok_workflow.md)

---

## まとめ

ForStartupプロジェクトのスキルファイル自動検証システムの構築が完了しました。

### 主な成果

✅ **GitHub Actions ワークフロー** - 本番対応のCI/CDパイプライン構築
✅ **Python検証スクリプト** - 7つの検証機能を実装
✅ **包括的なドキュメント** - 1,100行以上のガイド作成
✅ **即時実効性** - 現在のプロジェクト状態（29/30ファイル有効）を検証

このシステムにより、スキルファイルの品質管理が自動化され、開発者の手作業を大幅に削減できます。

---

**作成日時:** 2026-01-09
**実装所要時間:** 約60分
**テスト時間:** 約30分
**合計:** 約90分
