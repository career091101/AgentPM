# Ralph Wiggum Rules

自律的ループ実行のルール。

## トリガー
- 「Ralph実行」「自律ループ」「無限ループ実行」

## 概要

Ralph Wiggum プラグインによる自律的ループ実行機能。`while`ループ + `--continue` + PROMPT.md による反復実行で、大量の定型タスクを自動化します。

## 基本コマンド

```bash
# ループ開始（最大イテレーション数指定必須）
/ralph-loop "<task>" --completion-promise "<promise>" --max-iterations <N>

# ループ中断
/cancel-ralph

# 完了プロミスタグ（タスク完了時にPROMPT.mdに記載）
<promise>TASK COMPLETE</promise>
```

## 安全ルール（必須遵守）

1. **`--max-iterations` を必ず設定**: 無限ループ防止
2. **Gitリポジトリで実行**: 各イテレーションで自動コミット
3. **新規ブランチで実行**: mainブランチ保護
4. **コスト監視**: 初回10イテレーションで測定

## 推奨モデル

- **Haiku**: コスト効率重視（定型タスク向け）
- **Sonnet**: 品質重視（複雑な判断が必要な場合）

## 適しているタスク

- 大量の定型ドキュメント作成
- パス統一・リファクタリング
- 翻訳タスク
- テストケース生成

## 適していないタスク

- 複雑な意思決定が必要なタスク
- ユーザー入力が必要なタスク
- 外部APIとの複雑な連携

## コア機構

```bash
while :; do
  cat PROMPT.md | claude-code --continue
done
```

## Week 5設定管理との統合

Ralph Wiggum プラグインは `.claude/project-settings.json` で有効化済み：

```json
{
  "enabledPlugins": {
    "ralph-wiggum@claude-plugins-official": true
  }
}
```

## 詳細ガイド

包括的な使用方法、実装パターン、トラブルシューティングは以下を参照：

- @docs/implementation_guides/week8_ralph_wiggum.md - 完全ガイド（Week 8実装完了）
- @.claude/rules/WEEK_IMPLEMENTATIONS.md#week-8 - クイックリファレンス

## 参照

- Week 8実装完了レポート: @Flow/202601/2026-01-10/week8_phase3_improvement_report.md
- Ralph Wiggum公式プラグイン: `ralph-wiggum@claude-plugins-official`
