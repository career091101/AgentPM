# GitHub Action Integration Guide

Claude Codeの公式GitHub App統合による自動PRレビューのガイド。

## 概要

このガイドは、Week 7で実装したGitHub Action統合の使用方法と運用ガイドラインを提供します。

### 主要機能

1. **@claudeタグによる自動レビュー起動**: PR title/body/commentに`@claude`を含めるだけでレビュー開始
2. **Claude APIによる高品質レビュー**: セキュリティ、パフォーマンス、品質、テストカバレッジ、ドキュメントの5観点評価
3. **CLAUDE.md自動更新**: PRレビューから抽出したプロジェクト全体ルールを自動追記
4. **重複検出**: 既存ルールとの類似度判定により、重複ルール追加を防止
5. **PRコメント自動投稿**: レビュー結果をMarkdown形式で自動投稿

## セットアップ手順

### 前提条件

- GitHubリポジトリへの管理者権限
- Anthropic API key（Claude API）
- Claude Code CLI（ローカル開発環境）

### Step 1: GitHub Appインストール

Claude Code CLIで公式GitHub Appをインストール：

```bash
# Claude Code CLI内で実行
/install-github-app
```

インストール後、ブラウザが開いてGitHub認証画面が表示されます。

#### 設定項目

1. **Repository access**: このリポジトリ（aipm_v0）を選択
2. **Permissions**: 以下が自動設定されます
   - Contents: Read & Write
   - Pull Requests: Read & Write
   - Issues: Read & Write

### Step 2: Anthropic API Keyの設定

GitHubリポジトリのSecretsに`ANTHROPIC_API_KEY`を追加：

1. リポジトリ → Settings → Secrets and variables → Actions
2. "New repository secret" をクリック
3. Name: `ANTHROPIC_API_KEY`
4. Secret: Anthropic APIキーを貼り付け（`sk-ant-api03-...`）
5. "Add secret" で保存

#### APIキーの取得方法

1. [Anthropic Console](https://console.anthropic.com/) にログイン
2. "API Keys" → "Create Key"
3. 名前を設定（例: "GitHub Action PR Review"）
4. キーをコピー（一度しか表示されないため注意）

### Step 3: Python依存関係のインストール（ローカル検証用）

```bash
cd /Users/yuichi/AIPM/aipm_v0
pip install -r scripts/github_actions/requirements.txt
```

インストールされるパッケージ:
- `anthropic>=0.39.0` - Anthropic API client
- `requests>=2.31.0` - GitHub API連携

### Step 4: 動作確認

1. テストブランチを作成
   ```bash
   git checkout -b test/claude-review
   ```

2. 簡単な変更をコミット
   ```bash
   echo "# Test" > test.md
   git add test.md
   git commit -m "test: Claude review test"
   git push -u origin test/claude-review
   ```

3. PRを作成し、タイトルに`@claude`を含める
   ```bash
   gh pr create --title "@claude Review this test PR" --body "Testing Claude Code review integration"
   ```

4. GitHub Actionsのログを確認
   - リポジトリ → Actions → "Claude PR Review" workflow
   - 実行中のジョブをクリックして詳細ログを確認

5. PRコメントを確認
   - PRページに戻り、Claude Codeのレビューコメントを確認

## 使用方法

### 基本的なワークフロー

#### パターン1: PR作成時に自動レビュー

PRのタイトルまたは本文に`@claude`を含める：

```markdown
## PR Title
@claude Fix authentication bug in login flow

## PR Description
This PR fixes the authentication bug reported in issue #123.

Please review:
- Security implications
- Test coverage
- Error handling
```

#### パターン2: 既存PRにレビュー依頼

PRコメントで`@claude`を含むメッセージを投稿：

```markdown
@claude このPRのセキュリティ面をレビューしてください。
特にユーザー入力のバリデーション処理を重点的にチェックお願いします。
```

#### パターン3: PR更新時に再レビュー

PR本文に`@claude`が含まれている場合、以下のイベントで自動再レビュー：
- 新規コミットのプッシュ（`synchronize`イベント）
- PR本文の編集（`edited`イベント）

### レビュー結果の読み方

Claude Codeは以下の形式でレビューコメントを投稿します：

```markdown
## 🤖 Claude Code Review

**Summary:** このPRは認証フローのバグ修正を行っています。全体的にコード品質は高いですが、いくつか改善点があります。

✅ **Recommendation:** Approve

### Issues Found

1. 🟡 **MEDIUM**: ユーザー入力バリデーションが不十分
   - **Suggestion**: email形式の正規表現チェックを追加してください

2. 🟢 **LOW**: ドキュメントコメントが不足
   - **Suggestion**: 主要関数にdocstringを追加してください

### 📝 New Rules to Add to CLAUDE.md

- 認証関連の処理では必ず入力バリデーションを実装すること
- パスワード処理時はbcryptを使用し、平文保存は禁止

---
*🤖 Generated with Claude Code*
```

#### 評価基準の理解

| 重要度 | アイコン | 意味 |
|--------|---------|------|
| **HIGH** | 🔴 | セキュリティ脆弱性、致命的バグ → 必ず修正 |
| **MEDIUM** | 🟡 | パフォーマンス問題、コード品質 → 修正推奨 |
| **LOW** | 🟢 | ドキュメント、スタイル → 時間があれば修正 |

#### Recommendationの種類

- **Approve (✅)**: 問題なし、マージ可能
- **Request Changes (⚠️)**: 重要な問題あり、修正必須
- **Comment (💬)**: 軽微な問題のみ、判断はレビュアーに委ねる

### CLAUDE.md自動更新の仕組み

#### 更新フロー

1. Claude APIがPR diffを分析
2. プロジェクト全体に適用可能なルールを抽出
   - ❌ PR固有のルール（例: "この関数名をXに変更"）
   - ✅ プロジェクト全体ルール（例: "認証処理では必ず入力バリデーション"）
3. 既存CLAUDE.mdと重複チェック
   - 正規化（小文字化、空白除去）して類似度判定
   - 部分一致も検出（例: "入力検証を実施" ⊂ "ユーザー入力は必ず検証を実施すること"）
4. 新規ルールのみをCLAUDE.mdに追記
   - セクション形式: `## Auto-Generated Rules (YYYY-MM-DD)`
   - 箇条書きで追加

#### 重複検出のロジック

`scripts/github_actions/update_claude_md.py` の `is_duplicate_rule()` 関数：

```python
def is_duplicate_rule(new_rule: str, existing_content: str) -> bool:
    """Check if rule already exists in CLAUDE.md"""
    # 正規化（小文字化、空白除去）
    new_rule_normalized = " ".join(new_rule.lower().split())

    for line in existing_content.split("\n"):
        # 箇条書き行のみチェック
        if line.strip().startswith("-") or line.strip().startswith("*"):
            existing_rule = line.strip()[1:].strip()
            existing_rule_normalized = " ".join(existing_rule.lower().split())

            # 部分一致または完全一致で重複判定
            if new_rule_normalized in existing_rule_normalized or \
               existing_rule_normalized in new_rule_normalized:
                return True

    return False
```

#### CLAUDE.md更新例

```markdown
## Auto-Generated Rules (2026-01-04)

The following rules were extracted from PR reviews:

- 認証関連の処理では必ず入力バリデーションを実装すること
- パスワード処理時はbcryptを使用し、平文保存は禁止
- API呼び出しにはタイムアウト設定を必ず含めること
```

#### 手動マージ推奨

自動追記されたルールは定期的に見直し、既存セクションに統合することを推奨：

1. 週次レビュー会議でAuto-Generated Rulesセクションを確認
2. 重要なルールは該当セクション（例: `.claude/rules/security.md`）に移動
3. 重複・不要なルールは削除
4. Auto-Generated Rulesセクションをクリーンアップ

## GitHub Actionsワークフローの詳細

### ワークフロー構成

`.github/workflows/claude_pr_review.yml` は2つのジョブで構成：

#### Job 1: check-claude-tag

**目的**: @claudeタグの検出

```yaml
check-claude-tag:
  outputs:
    should_review: ${{ steps.check.outputs.should_review }}
    pr_number: ${{ steps.check.outputs.pr_number }}
  steps:
    - name: Check for @claude mention
      uses: actions/github-script@v7
      with:
        script: |
          // PR title/body/commentで@claude検出
          if (title.includes('@claude') || body.includes('@claude')) {
            core.setOutput('should_review', 'true');
          }
```

**検出対象**:
- PR title（例: `@claude Review this PR`）
- PR body（本文）
- PR comments（コメント）

**出力**:
- `should_review`: `true` / `false`
- `pr_number`: PR番号

#### Job 2: claude-review

**目的**: Claude APIによるレビュー実行とコメント投稿

```yaml
claude-review:
  needs: check-claude-tag
  if: needs.check-claude-tag.outputs.should_review == 'true'
  steps:
    - name: Checkout repository
      uses: actions/checkout@v4
      with:
        fetch-depth: 0  # 全履歴取得（コンテキスト強化）

    - name: Checkout PR branch
      run: gh pr checkout $PR_NUMBER

    - name: Run Claude PR Review
      env:
        ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        PR_NUMBER: ${{ needs.check-claude-tag.outputs.pr_number }}
        GITHUB_TOKEN: ${{ github.token }}
      run: python scripts/github_actions/claude_pr_review.py
```

### スクリプトの動作詳細

#### `scripts/github_actions/claude_pr_review.py`

**処理フロー**:

1. **環境変数取得**
   ```python
   api_key = os.getenv("ANTHROPIC_API_KEY")
   pr_number = os.getenv("PR_NUMBER")
   github_token = os.getenv("GITHUB_TOKEN")
   repo = os.getenv("GITHUB_REPOSITORY")  # 例: "yuichi/aipm_v0"
   ```

2. **PR情報とdiffの取得**
   ```python
   # GitHub REST API v3でPR情報取得
   pr_info = get_pr_info(pr_number, github_token, repo)

   # diffフォーマットでPR変更内容を取得
   pr_diff = get_pr_diff(pr_number, github_token, repo)
   ```

3. **CLAUDE.md読み込み**
   ```python
   claude_md = read_claude_md()
   # プロジェクト固有ルールをコンテキストに含める
   ```

4. **Claude APIでレビュー実行**
   ```python
   client = anthropic.Anthropic(api_key=api_key)

   message = client.messages.create(
       model="claude-sonnet-4-20250514",
       max_tokens=4096,
       messages=[{"role": "user", "content": prompt}]
   )
   ```

5. **GitHub出力設定**
   ```python
   set_github_output("review_comment", review_comment)
   set_github_output("new_rules", json.dumps(new_rules))
   ```

#### `scripts/github_actions/update_claude_md.py`

**処理フロー**:

1. **新規ルール取得**
   ```python
   new_rules_json = os.getenv("NEW_RULES")
   new_rules = json.loads(new_rules_json)
   ```

2. **既存CLAUDE.md読み込みと重複チェック**
   ```python
   existing_content = read_claude_md()
   unique_rules = [r for r in new_rules if not is_duplicate_rule(r, existing_content)]
   ```

3. **CLAUDE.mdに追記**
   ```python
   today = datetime.now().strftime("%Y-%m-%d")
   new_section = f"\n\n## Auto-Generated Rules ({today})\n\n"

   for rule in unique_rules:
       new_section += f"- {rule}\n"

   with open("CLAUDE.md", "a", encoding="utf-8") as f:
       f.write(new_section)
   ```

4. **Git commit & push**
   ```yaml
   - name: Commit CLAUDE.md updates
     run: |
       git config user.name "claude-code-bot"
       git config user.email "claude-code-bot@users.noreply.github.com"
       git add CLAUDE.md
       git commit -m "docs: Update CLAUDE.md with new rules from PR review"
       git push
   ```

## トラブルシューティング

### よくある問題と解決策

#### 問題1: GitHub Actionが起動しない

**症状**: @claudeタグを含むPRを作成してもワークフローが実行されない

**原因チェックリスト**:
1. ✅ `.github/workflows/claude_pr_review.yml` がmainブランチにマージされているか？
2. ✅ GitHub Actionsが有効化されているか？（Settings → Actions → General）
3. ✅ PR title/body/commentに本当に`@claude`が含まれているか？（スペース・大文字小文字を確認）

**解決策**:
```bash
# ワークフローファイルの存在確認
git show main:.github/workflows/claude_pr_review.yml

# GitHub Actionsの有効化確認
# Settings → Actions → General → "Allow all actions and reusable workflows"

# PRの再編集でワークフロー再起動
# PR編集画面でタイトルに@claudeを追加して保存
```

#### 問題2: ANTHROPIC_API_KEYエラー

**症状**: GitHub Actionsログに以下のエラー：
```
Error: ANTHROPIC_API_KEY not set
```

**解決策**:
1. リポジトリ → Settings → Secrets and variables → Actions
2. `ANTHROPIC_API_KEY` が存在するか確認
3. 存在しない場合は追加、存在する場合は再作成
   ```
   Name: ANTHROPIC_API_KEY
   Secret: sk-ant-api03-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

#### 問題3: GitHub API rate limit

**症状**: GitHub Actionsログに以下のエラー：
```
Error fetching PR diff: 403 Client Error: rate limit exceeded
```

**原因**: GitHub REST APIのレート制限（認証済み: 5000リクエスト/時）

**解決策**:
1. レート制限リセット時刻の確認:
   ```bash
   curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/rate_limit
   ```

2. 一時的な回避策: 1時間待機

3. 恒久対策: GitHub Appの認証を使用（自動的に高いレート制限が適用される）

#### 問題4: Claude APIタイムアウト

**症状**: GitHub Actionsログに以下のエラー：
```
Claude API error: Connection timeout
```

**原因**: 大規模PR（1000行以上の変更）でClaude API応答時間が長い

**解決策**:

1. **diff制限の適用**（`claude_pr_review.py`を編集）:
   ```python
   # 現在: 10000文字まで
   pr_diff[:10000]

   # 変更: 5000文字に短縮
   pr_diff[:5000]
   ```

2. **モデルの変更**（コスト削減＋高速化）:
   ```python
   # 現在: claude-sonnet-4-20250514
   model="claude-sonnet-4-20250514"

   # 変更: claude-haiku（軽量・高速）
   model="claude-haiku-20250312"
   ```

3. **タイムアウト延長**（`.github/workflows/claude_pr_review.yml`）:
   ```yaml
   - name: Run Claude PR Review
     timeout-minutes: 10  # デフォルト: 6分 → 10分に延長
   ```

#### 問題5: CLAUDE.md更新のコンフリクト

**症状**: Git pushエラー:
```
! [rejected] main -> main (fetch first)
error: failed to push some refs
```

**原因**: 複数のPRレビューが同時実行され、CLAUDE.mdの更新が競合

**解決策**:

1. **concurrency制御の追加**（`.github/workflows/claude_pr_review.yml`）:
   ```yaml
   concurrency:
     group: claude-review-${{ github.ref }}
     cancel-in-progress: false  # 既存実行を中断しない
   ```

2. **リトライロジックの追加**（`update_claude_md.py`に追加）:
   ```python
   import subprocess
   import time

   def git_push_with_retry(max_retries=3):
       for i in range(max_retries):
           try:
               subprocess.run(["git", "pull", "--rebase"], check=True)
               subprocess.run(["git", "push"], check=True)
               return True
           except subprocess.CalledProcessError:
               if i == max_retries - 1:
                   raise
               time.sleep(2 ** i)  # Exponential backoff
       return False
   ```

#### 問題6: Branch protection rulesとの競合

**症状**: CLAUDE.md更新のcommitがブランチプロテクションルールでブロックされる

**解決策**:

1. **bot用のバイパス設定**（Settings → Branches → Branch protection rules）:
   - "Allow specified actors to bypass required pull requests" を有効化
   - "claude-code-bot" を追加

2. **Personal Access Token使用**（より安全な方法）:
   - GitHub Settings → Developer settings → Personal access tokens (classic)
   - "Generate new token" → `repo` スコープを選択
   - リポジトリSecrets に `CLAUDE_BOT_TOKEN` として追加
   - `.github/workflows/claude_pr_review.yml` を変更:
     ```yaml
     - name: Commit CLAUDE.md updates
       env:
         GITHUB_TOKEN: ${{ secrets.CLAUDE_BOT_TOKEN }}
       run: |
         git config user.name "claude-code-bot"
         git config user.email "claude-code-bot@users.noreply.github.com"
         git push
     ```

## コスト最適化

### Anthropic API料金体系（2026年1月時点）

| モデル | 入力料金 | 出力料金 | 1レビューあたり概算 |
|--------|---------|---------|-------------------|
| Claude Sonnet 4 | $3/MTok | $15/MTok | $0.10-0.30 |
| Claude Haiku | $0.25/MTok | $1.25/MTok | $0.01-0.03 |

**計算例**（PR 300行変更の場合）:
- 入力: PR diff (2000 tokens) + CLAUDE.md (2000 tokens) + プロンプト (500 tokens) = 4500 tokens
- 出力: レビュー結果 (1500 tokens)
- **Sonnet**: $0.0135 (入力) + $0.0225 (出力) = **$0.036/レビュー**
- **Haiku**: $0.0011 (入力) + $0.0019 (出力) = **$0.003/レビュー**

### コスト削減戦略

#### 戦略1: モデルの使い分け

小規模PR（変更行数<100）はHaikuを使用：

```python
# claude_pr_review.py に追加
def select_model(changed_files: int, additions: int, deletions: int) -> str:
    """Select optimal model based on PR size"""
    total_changes = additions + deletions

    if total_changes < 100:
        return "claude-haiku-20250312"  # 小規模: Haiku
    elif total_changes < 500:
        return "claude-sonnet-4-20250514"  # 中規模: Sonnet
    else:
        return "claude-sonnet-4-20250514"  # 大規模: Sonnet（品質重視）
```

**削減効果**: 小規模PRが全体の60%と仮定
- 従来（Sonnet全件）: $0.036 × 100レビュー/月 = $3.60/月
- 最適化後: ($0.003 × 60 + $0.036 × 40) = $1.62/月
- **削減率: 55%**

#### 戦略2: diff制限の適用

PR diffの送信サイズを制限：

```python
# 現在: 10000文字
pr_diff[:10000]

# 変更: 段階的制限
if len(pr_diff) > 15000:
    # 大規模PRは最初の5000文字のみ
    pr_diff = pr_diff[:5000] + "\n\n[... truncated for cost optimization ...]"
elif len(pr_diff) > 10000:
    pr_diff = pr_diff[:10000]
```

#### 戦略3: レビュー頻度の制御

不要なレビューを避ける：

```yaml
# .github/workflows/claude_pr_review.yml に追加
- name: Check file types
  id: file_check
  run: |
    # Markdown/ドキュメントのみの変更はスキップ
    changed_files=$(gh pr diff $PR_NUMBER --name-only)
    if echo "$changed_files" | grep -qv '\.md$'; then
      echo "has_code=true" >> $GITHUB_OUTPUT
    else
      echo "has_code=false" >> $GITHUB_OUTPUT
    fi

- name: Run Claude PR Review
  if: steps.file_check.outputs.has_code == 'true'
  run: python scripts/github_actions/claude_pr_review.py
```

#### 戦略4: 月次予算アラート

Anthropic Consoleで予算アラート設定：

1. [Anthropic Console](https://console.anthropic.com/) → Billing → Spending alerts
2. "Create alert" → 閾値設定（例: $10/月）
3. アラートメール受信 → 設定見直し

### 実運用コスト見積もり

| リポジトリ規模 | PRレビュー数/月 | 平均レビューコスト | 月額概算 |
|-------------|--------------|---------------|---------|
| 小規模（1-3人） | 20 | $0.020 | **$0.40/月** |
| 中規模（4-10人） | 80 | $0.025 | **$2.00/月** |
| 大規模（11-30人） | 200 | $0.030 | **$6.00/月** |

**削減前**（Sonnet全件 $0.036）:
- 小規模: $0.72/月 → **削減後: $0.40/月（44%削減）**
- 中規模: $2.88/月 → **削減後: $2.00/月（31%削減）**
- 大規模: $7.20/月 → **削減後: $6.00/月（17%削減）**

## セキュリティベストプラクティス

### 機密情報の保護

#### ❌ 絶対にやってはいけないこと

1. **API keyをコード内にハードコード**
   ```python
   # ❌ 絶対にダメ
   api_key = "sk-ant-api03-xxxxxxxxxxxxxxxx"
   ```

2. **API keyをコミット履歴に含める**
   ```bash
   # ❌ 絶対にダメ
   git add .env
   git commit -m "Add API key"
   ```

3. **Public repositoryでSecretsを使わずにAPI key使用**

#### ✅ 推奨される方法

1. **GitHub Secretsの使用**
   ```yaml
   env:
     ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
   ```

2. **環境変数の検証**
   ```python
   api_key = os.getenv("ANTHROPIC_API_KEY")
   if not api_key:
       print("Error: ANTHROPIC_API_KEY not set", file=sys.stderr)
       sys.exit(1)
   ```

3. **API keyのローテーション**（月次推奨）
   - Anthropic Consoleで新しいキーを作成
   - GitHub Secretsを更新
   - 古いキーを削除

### PR diffの安全性

#### 機密情報の検出と除外

```python
# claude_pr_review.py に追加
import re

def sanitize_pr_diff(pr_diff: str) -> str:
    """Remove sensitive information from PR diff"""
    # API keys (sk-xxx, api_xxx等)
    pr_diff = re.sub(r'(sk-|api_|key_)[a-zA-Z0-9\-_]{20,}', '[REDACTED]', pr_diff)

    # Passwords
    pr_diff = re.sub(r'password\s*=\s*["\'][^"\']+["\']', 'password="[REDACTED]"', pr_diff, flags=re.IGNORECASE)

    # Email addresses
    pr_diff = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', pr_diff)

    # IP addresses
    pr_diff = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', '[IP]', pr_diff)

    return pr_diff
```

### Anthropic API利用規約の遵守

1. **データ保持**: Anthropicは30日後にリクエストデータを削除
2. **データ使用**: PR diffはモデル訓練に使用されない（[Trust & Safety](https://www.anthropic.com/trust-safety) 参照）
3. **プライバシー**: 機密PRレビューは社内ポリシーに従って実施

## チーム運用ガイドライン

### 推奨ワークフロー

#### 週次レビュー会議（30分）

**議題**:
1. Auto-Generated Rulesの確認（10分）
   - 新規追加されたルールをレビュー
   - 重要なルールを既存セクションに統合
   - 重複・不要なルールを削除

2. レビュー品質の評価（10分）
   - Claudeのレビューが役立ったPR事例の共有
   - 誤検出・見逃しの報告
   - プロンプト改善の提案

3. コスト・パフォーマンスの確認（10分）
   - 月間API使用量の確認
   - コスト削減施策の検討
   - 次週のアクション決定

#### ルール統合のベストプラクティス

**Example**: Auto-Generated Rulesの統合

```markdown
## Before (CLAUDE.md)

### Security
- ユーザー入力は必ずバリデーションを実施すること

## Auto-Generated Rules (2026-01-04)
- 認証関連の処理では必ず入力バリデーションを実装すること
- パスワード処理時はbcryptを使用し、平文保存は禁止
```

**After** (週次レビュー後):

```markdown
## Security

### 入力バリデーション
- ユーザー入力は必ずバリデーションを実施すること
- 認証関連の処理では特に厳格なバリデーションを実装すること

### パスワード管理
- パスワード処理時はbcryptを使用し、平文保存は禁止
- ハッシュ化アルゴリズムは最低でもbcrypt、推奨はArgon2

## Auto-Generated Rules (2026-01-04)
[空（統合完了）]
```

### 新規メンバーのオンボーディング

1. **GitHub App権限の付与**
   - Settings → Manage access → "Add people" → 該当メンバーを追加
   - Role: Write（PRレビューコメント閲覧のため）

2. **CLAUDE.mdの読み合わせ**（30分）
   - プロジェクト全体ルールの理解
   - Auto-Generated Rulesセクションの説明
   - 週次レビュー会議への参加依頼

3. **初回PRでの動作確認**
   - 小規模なPRを作成（例: READMEの誤字修正）
   - タイトルに`@claude`を含める
   - レビューコメントを確認

## 高度な使い方

### カスタムプロンプトの調整

`scripts/github_actions/claude_pr_review.py` の `review_pr_with_claude()` 関数内のプロンプトをカスタマイズ：

#### 例1: セキュリティ重点レビュー

```python
prompt = f"""You are a senior security engineer reviewing a Pull Request.

**PR Information:**
...

**Task:**
1. Review the code changes with SECURITY as the top priority:
   - SQL injection vulnerabilities
   - XSS (Cross-Site Scripting) vulnerabilities
   - CSRF vulnerabilities
   - Authentication/Authorization issues
   - Insecure data handling
   - Dependency vulnerabilities

2. Extract security-related rules for CLAUDE.md

**Output Format:**
{{
  "review_summary": "...",
  "issues": [{{"severity": "critical|high|medium|low", "description": "...", "suggestion": "..."}}],
  "new_rules": ["Security rule 1", "Security rule 2"],
  "overall_assessment": "approve|request_changes|comment"
}}
"""
```

#### 例2: パフォーマンス重点レビュー

```python
prompt = f"""You are a senior performance engineer reviewing a Pull Request.

**Task:**
1. Review the code changes with PERFORMANCE as the top priority:
   - Algorithm complexity (O(n) vs O(n^2))
   - Database query optimization (N+1 problem)
   - Memory leaks
   - Unnecessary re-rendering (React)
   - Caching opportunities
   - Lazy loading opportunities

2. Extract performance-related rules for CLAUDE.md
"""
```

### 複数レビュアーの並列実行

大規模PRに対して、異なる観点で並列レビュー：

```yaml
# .github/workflows/claude_pr_review.yml に追加
- name: Security Review
  run: python scripts/github_actions/claude_pr_review.py --focus security

- name: Performance Review
  run: python scripts/github_actions/claude_pr_review.py --focus performance

- name: Documentation Review
  run: python scripts/github_actions/claude_pr_review.py --focus documentation
```

対応する `claude_pr_review.py` の変更：

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--focus", choices=["security", "performance", "documentation"], default="general")
args = parser.parse_args()

# プロンプトをフォーカスに応じて変更
if args.focus == "security":
    prompt = security_focused_prompt(...)
elif args.focus == "performance":
    prompt = performance_focused_prompt(...)
else:
    prompt = general_prompt(...)
```

## 参照

### 関連ドキュメント

- **GitHub App設定**: @docs/github_app_setup_guide.md
- **CLAUDE.md**: @CLAUDE.md
- **Week 5設定管理**: @.claude/rules/settings_management.md
- **Week 6 MCP統合**: @.claude/rules/mcp_integration.md

### 関連スクリプト

- **PRレビュー**: `scripts/github_actions/claude_pr_review.py`
- **CLAUDE.md更新**: `scripts/github_actions/update_claude_md.py`

### 公式ドキュメント

- [Claude Code公式ドキュメント](https://code.claude.com/docs/en/cli-reference)
- [Anthropic API Documentation](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Apps Documentation](https://docs.github.com/en/apps)
