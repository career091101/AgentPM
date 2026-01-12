# ForStartup Skills CI/CD ガイド

## 概要

このプロジェクトには自動検証ワークフローが統合されています。ForStartupスキルを変更する際には、このガイドに従ってください。

## CI/CD パイプライン

### 1. ローカル開発

スキルファイル (`SKILL.md`) を編集した後、プッシュ前に検証を実行します:

```bash
# ローカル検証
python3 scripts/validate_skills.py

# 結果確認
cat validation_report.json
```

### 2. Push時の自動検証

`.claude/skills/for_startup/` 配下の変更を push すると、自動的に GitHub Actions ワークフローが実行されます:

- YAMLフロントマター検証
- ForRecruit残骸チェック
- ファイル構造検証

### 3. Pull Request時の検証結果投稿

PR作成時に、検証結果が自動的に PR コメントとして投稿されます:

```
## ForStartup Skills Validation Report

### Validation Results

✅ **All validations passed!**

### Summary

- Total files scanned: 30
- Valid files: 30
- Invalid files: 0
```

## スキルファイルの標準フォーマット

### YAML フロントマター（必須）

```yaml
---
name: スキルの一意な識別子
description: |
  スキルの説明。複数行対応。
  起業の科学やビジネスモデルの観点を記述。

trigger_keywords:
  - "キーワード1"
  - "キーワード2"
  - "キーワード3"

stage: Phase2（CPF検証）

dependencies:
  - 依存スキル1
  - 依存スキル2
  - 依存スキル3

output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/...
---
```

### ファイル構造（推奨）

```markdown
---
[YAMLフロントマター]
---

# スキル名

スキルの概要説明。

---

## このSkillでできること

1. **機能1**: 説明
2. **機能2**: 説明
3. **機能3**: 説明

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 説明 |
| **出力** | ファイルパス |
| **次のSkill** | 後続スキル |
| **ステージ** | フェーズ |

---

## 使用方法

詳細な使用手順。

---

## 評価基準

定量・定性評価基準の詳細。

---

## Domain-Specific Knowledge

参考資料、参照ドキュメント。
```

## よくあるエラーと対処方法

### 1. YAML フロントマター構文エラー

**エラー:**
```
Invalid YAML frontmatter: while parsing a block mapping...
```

**原因:**
```yaml
output_file: {OUTPUT_DIR}/output.md  # 中括弧がYAML辞書と解釈される
```

**修正:**
```yaml
output_file: Stock/programs/.../output.md  # 完全パスを記述
```

### 2. 必須フィールド不足

**エラー:**
```
Missing required fields: trigger_keywords, stage
```

**修正:** 以下の4フィールドを必ず含める:
- `trigger_keywords` (配列)
- `stage` (文字列)
- `output_file` (文字列)
- `dependencies` (配列)

### 3. stage値が非標準形式

**警告:**
```
stage 'Phase5（Monitoring）' may not be in standard format.
```

**標準値リスト:**
- `Phase1` （需要発見）
- `Phase2` （CPF検証）
- `Phase3` （PSF検証）
- `Phase4` （実装）
- `planning`, `discovery`, `research`

**拡張値:**
- `Phase1（需要発見）` ✅
- `Phase2（CPF検証）` ✅
- `Phase3（PSF検証）` ✅
- `Phase4（実装）` ✅

### 4. ForRecruit残骸が見つかった

**警告:**
```
ForRecruit reference found: forrecruit
```

**対処:**
```bash
# 対象ファイルを確認
grep -r "ForRecruit" .claude/skills/for_startup/

# テキストを置換
# ForRecruit → for_startup (またはコンテキストに応じて修正)
```

### 5. 括弧の混在（パス規約違反）

**エラー:**
```
output_file contains half-width parentheses. Use full-width: （AIエージェント）
```

**修正:**
```yaml
# ❌ 誤り（半角括弧）
output_file: Stock/programs/創業支援・新規事業開発(AIエージェント)/...

# ✅ 正しい（全角括弧）
output_file: Stock/programs/創業支援・新規事業開発（AIエージェント）/...
```

## パス規約（重要）

### 括弧の使用ルール

- **全角括弧（）のみ** を使用すること
- 半角括弧()は使用禁止
- フォルダ名: `創業支援・新規事業開発（AIエージェント）`

### Unicode正規化

すべてのパスは Unicode NFC正規化を使用:

```python
import unicodedata
path = unicodedata.normalize('NFC', path_string)
```

## チェックリスト

スキルを作成・修正する際は、以下をチェック:

- [ ] YAML フロントマターが正しい形式か
- [ ] 4つの必須フィールドが存在するか
  - [ ] `trigger_keywords` （配列）
  - [ ] `stage` （文字列）
  - [ ] `output_file` （文字列）
  - [ ] `dependencies` （配列）
- [ ] フィールドの型が正しいか
- [ ] `output_file` に全角括弧を使用しているか
- [ ] ForRecruit参照が含まれていないか
- [ ] Markdown見出し（# Title）が存在するか
- [ ] 本文が十分な長さか（100文字以上）
- [ ] ローカルで `python3 scripts/validate_skills.py` を実行したか
- [ ] エラーがすべて修正されたか

## PR作成時の流れ

1. **ローカルで編集**
   ```bash
   # スキルファイルを編集
   vim .claude/skills/for_startup/[skill-name]/SKILL.md
   ```

2. **ローカル検証を実行**
   ```bash
   python3 scripts/validate_skills.py
   cat validation_report.json
   ```

3. **エラーを修正**
   - `validation_report.json` の `errors` セクションを確認
   - YAML フロントマターを修正

4. **コミット**
   ```bash
   git add .claude/skills/for_startup/[skill-name]/SKILL.md
   git commit -m "Fix: Skill validation errors in [skill-name]"
   ```

5. **Push**
   ```bash
   git push origin feature/[description]
   ```

6. **PR作成**
   - GitHub で PR を作成
   - 自動検証ワークフローが実行される
   - PR コメントで検証結果を確認

7. **マージ**
   - すべてのチェックが ✅ になったら マージ

## 高度なカスタマイズ

### 検証ルールの追加

新しい検証ルールを追加する場合:

1. `scripts/validate_skills.py` の `SkillValidator` クラスを拡張
2. 新しいメソッドを実装
3. ローカルでテスト
4. PR で提案

例:
```python
def _validate_custom_rule(self, file_path: Path, frontmatter: Dict) -> None:
    """カスタム検証ルール"""
    if 'custom_field' in frontmatter:
        # 検証ロジック
        pass
```

### ワークフロー条件の変更

`.github/workflows/validate-skills.yml` で以下を調整可能:

```yaml
on:
  push:
    paths:
      - '.claude/skills/for_startup/**'  # トリガーパスの変更
  pull_request:
    paths:
      - '.claude/skills/for_startup/**'
```

## サポート

質問や問題がある場合:

1. `validation_report.json` を確認
2. このドキュメントの「よくあるエラー」を参照
3. スクリプト出力で詳細なエラーメッセージを確認
4. プロジェクト管理者に報告

## 参考資料

- [PMBOK ワークフロー](../../docs/ai/pmbok_workflow.md)
- [パス規約](../../.claude/rules/path_conventions.md)
- [検証スクリプト](../../scripts/validate_skills.py)
- [ワークフロー定義](./.github/workflows/validate-skills.yml)
