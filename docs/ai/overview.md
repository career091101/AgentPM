# aipm_v0 プロダクト概要

## システム概要

**aipm_v0** は、PMBOK × Lean UX × Agile のハイブリッドプロジェクト管理システムです。

LLM（大規模言語モデル）の支援を受けながら、プロジェクト管理における文書作成から確定・アーカイブまでの流れを自動化します。

## 主な特徴

1. **PMBOK × Lean UX × Agileハイブリッド**
   - 上流工程: PMBOK準拠の文書管理
   - 中流: Lean UXの発見と検証
   - 実装フェーズ: アジャイル手法

2. **3層フォルダ構造**
   - `Flow/` - ドラフト・作業中ファイル
   - `Stock/` - 確定版ドキュメント
   - `Archived/` - 完了プロジェクト格納

3. **トリガーワードによる文書生成**
   - 例: 「プロジェクト憲章」→ 質問応答 → ドラフト生成
   - 「確定反映して」→ Flow から Stock へ移動

## ディレクトリ構造

```
aipm_v0/
├── Flow/           # ドラフト・WIP（年月/日付で階層化）
├── Stock/          # 確定版ドキュメント
│   └── programs/   # プログラム/プロジェクト構造
├── Archived/       # 完了・旧バージョン格納
├── scripts/        # ユーティリティスクリプト
├── .cursor/rules/  # Cursor用PMBOKルール
├── .agent/         # Antigravity用ルール/ワークフロー
├── .codex/         # Codex用Skills
├── .claude/        # Claude Code用ルール/Subagents
└── docs/ai/        # 共通コアドキュメント（本ディレクトリ）
```

## PMBOKフェーズ

| フェーズ | 主な成果物 |
|----------|-----------|
| Initiating | プロジェクト憲章、ステークホルダー分析 |
| Discovery | ペルソナ、ジャーニーマップ、仮説マップ |
| Research | 競合調査、市場規模推定、デスクリサーチ |
| Planning | WBS、PRD、バックログ初期化 |
| Executing | 開発計画、ストーリー実装、スプリント |
| Monitoring | ステータスレポート、リスクログ |
| Closing | レッスンズラーンド、移行文書 |

## マルチエージェント対応

このリポジトリは以下のAIツールで共通運用できます：

- **Antigravity** - 主軸ツール
- **Cursor** - 既存.mdcルール活用
- **Codex** - Skills経由
- **Claude Code** - Subagents経由

詳細は各ツール固有の設定ファイルを参照してください。
