# スキル最適化ガイド

## 現状分析

### コンテキスト使用状況（2026-01-05時点）

```
Total: 94k/200k tokens (47%)

内訳:
- System prompt:    4.5k  (2.2%)
- System tools:    22.5k (11.3%)
- MCP tools:        5.0k  (2.5%)
- Memory files:    17.1k  (8.5%)
- Skills:        ~40-45k (20-22.5%) ← 最適化対象
- Messages:         0.01k (0.0%)
- Free space:     106k   (53.0%)
```

### 最適化による削減見込み

| カテゴリ | スキル数 | 削減tokens | 削減率 |
|---------|---------|-----------|--------|
| Trading系 | 23個 | ~3,500 tokens | 3.5% |
| ForSolo系 | 15個 | ~2,000 tokens | 2.0% |
| ForGenAI系 | 30個 | ~2,500 tokens | 2.5% |
| ForRecruit系 | 20個 | ~2,000 tokens | 2.0% |
| ForStartup系 | 30個 | ~2,500 tokens | 2.5% |
| **合計** | **118個** | **~12,500 tokens** | **12.5%** |

### 最適化後の予測

```
Total: 81.5k/200k tokens (40.75%) ← 6.25%削減
Free space: 118.5k (59.25%) ← より余裕のある運用
```

## 運用パターン

### パターン1: 常時コアスキルのみ（推奨）

**対象プロジェクト**: SNS自動化、一般的なスタートアップ検証

**有効スキル（15個程度）**:
- orchestrate-review-loop
- sns-automation
- generate-sns-posts
- research-topic
- validate-pmf
- validate-cpf
- validate-psf
- validate-10x
- build-lp
- create-mvv
- simulate-interview
- research-problem
- startup-scorecard
- discover-demand
- build-flywheel

**効果**: コンテキスト使用率 **35-38%** まで削減

### パターン2: プロジェクト別スキルセット

#### トレーディングプロジェクト

```bash
# .claudeignore で以下をコメントアウト
# .claude/skills/agent-*/
# .claude/skills/trading-*/
```

**有効スキル**: コア15個 + Trading23個 = 38個

#### ForSoloプロジェクト

```bash
# .claudeignore で以下をコメントアウト
# .claude/skills/for-solo-*/
```

**有効スキル**: コア15個 + ForSolo15個 = 30個

#### ForGenAIプロジェクト

```bash
# .claudeignore で以下をコメントアウト
# .claude/skills/for-genai-*/
```

**有効スキル**: コア15個 + ForGenAI30個 = 45個

## 実践手順

### ステップ1: 現在のコンテキストを確認

```bash
/context
```

### ステップ2: .claudeignoreを有効化

現在の設定をそのまま保存（すでに設定済み）

### ステップ3: Claude Codeを再起動

```bash
# 設定を反映させるため再起動
# VS Codeの場合: Cmd+Shift+P → "Reload Window"
# ターミナルの場合: Ctrl+C → claude code
```

### ステップ4: コンテキスト削減を確認

```bash
/context
```

**期待結果**: 47% → 35-40% に削減

### ステップ5: 特化スキルが必要な場合

```bash
# 例: トレーディングプロジェクト開始時
nano .claudeignore

# 以下の行をコメントアウト（#を追加）
# .claude/skills/agent-*/
# .claude/skills/trading-*/

# 再起動して反映
```

## トラブルシューティング

### Q: スキルが見つからないエラーが出る

**A**: `.claudeignore` で必要なスキルを誤って除外している可能性があります。

```bash
# .claudeignore を確認
cat .claudeignore | grep -A5 "スキル最適化"

# 該当スキルの行をコメントアウト
nano .claudeignore
```

### Q: コンテキスト使用率が変わらない

**A**: Claude Codeの再起動が必要です。

```bash
# VS Code: Cmd+Shift+P → "Developer: Reload Window"
# または完全再起動
```

### Q: 特定のプロジェクトで複数カテゴリが必要

**A**: `.claudeignore` で必要なカテゴリのみコメントアウト

```bash
# 例: ForGenAI + Trading を両方有効化
# .claudeignore で以下をコメントアウト
# # .claude/skills/for-genai-*/
# # .claude/skills/agent-*/
# # .claude/skills/trading-*/
```

## メンテナンス

### 月次レビュー

1. 過去1ヶ月で使用したスキルを確認
2. 未使用スキルを `.claudeignore` に追加
3. コンテキスト使用率の推移を記録

### 新規スキル追加時

新しいスキルを作成したら、`.claudeignore` の分類に追加：

```bash
# コアスキル → 除外しない
# 特化スキル → 該当カテゴリに追加
```

## 参考

- @.claude/rules/context_management.md - コンテキスト管理ルール
- @CLAUDE.md - プロジェクト概要
- Claude Code公式ドキュメント: https://code.claude.com/docs
