# Ralph Loop (Ralph Wiggum Plugin) セットアップドキュメント

## 📋 製品概要

### 正式名称
**Ralph Wiggum Plugin for Claude Code**（通称: Ralph Loop）

### バージョン
- **Claude Code**: v2.0.76（2025年12月最新版）
- **プラグイン**: Anthropic公式プラグイン

### 用途・目的
Ralph Wiggum は、**Claude Code のための自律的な反復開発ループ技術**を実装する公式プラグインです。

**核心概念**:
- Claude Code を永続的な `while true` ループとして動作させる
- 同じプロンプトを繰り返しフィードバック
- タスクが完了するまで（または最大反復回数に達するまで）自動的に反復実行
- **Stop フック**を使用して終了を検知し、完了シグナルがない限りループ継続

**名称の由来**: The Simpsons の Ralph Wiggum にちなんで命名。「失敗しても粘り強く反復し続ける」という哲学を体現。

### 公式リソース
- **公式マーケットプレイス**: `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/ralph-wiggum/`
- **オリジナル技術**: https://ghuntley.com/ralph/
- **Ralph Orchestrator**: https://github.com/mikeyobrien/ralph-orchestrator
- **Awesome Claude**: https://awesomeclaude.ai/ralph-wiggum
- **GitHub（公式）**: https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum
- **GitHub（コミュニティ）**: https://github.com/frankbria/ralph-claude-code

---

## 🖥️ 環境情報

### インストール日時
2025-12-31

### OS環境
- **OS**: macOS (Darwin 25.1.0)
- **プラットフォーム**: darwin
- **作業ディレクトリ**: /Users/yuichi/AIPM

### 前提条件（すべて満たしています ✅）
| 要件 | バージョン | 状態 |
|------|-----------|------|
| **Claude Code** | v2.0.76 | ✅ インストール済み |
| **Node.js** | v25.2.1 | ✅ インストール済み |
| **npm** | 11.6.2 | ✅ インストール済み |
| **公式マーケットプレイス** | 2025-12-31更新 | ✅ ダウンロード済み |
| **ralph-wiggum プラグイン** | マーケットプレイス内 | ✅ 利用可能 |

---

## 📦 インストール手順

### ステップ1: Claude Code の起動

プロジェクトディレクトリに移動して Claude Code を起動します。

```bash
cd /Users/yuichi/AIPM/aipm_v0
claude
```

### ステップ2: プラグインのインストール

Claude Code の対話シェル内で以下のコマンドを実行します。

```bash
/plugin install ralph-wiggum@claude-plugin-directory
```

**代替方法**: GUI経由でのインストール

```bash
/plugin
# メニューから "Discover" を選択
# "ralph-wiggum" を検索してインストール
```

### ステップ3: インストールの確認

プラグインが正常にインストールされたか確認します。

```bash
/help
```

出力に以下のコマンドが含まれていれば成功です：
- `/ralph-loop` - 自律的な反復ループを開始
- `/cancel-ralph` - ループを停止
- `/help` - Ralph Wiggum のヘルプ表示

---

## ✅ 動作確認

### Level 1: 基本動作テスト

#### テスト1: ヘルプコマンド

```bash
/help
```

**期待される結果**: Ralph Wiggum のコマンド一覧とオプションが表示される

#### テスト2: 簡単なループ実行

```bash
/ralph-loop "Hello world を3回表示してください。完了したら<promise>COMPLETE</promise>を出力してください。" --completion-promise "COMPLETE" --max-iterations 5
```

**期待される結果**:
1. Claude が "Hello world" を3回表示
2. `<promise>COMPLETE</promise>` を出力
3. ループが自動的に終了

#### テスト3: ループのキャンセル

長時間実行中のループをキャンセルする場合：

```bash
/cancel-ralph
```

**期待される結果**: ループが即座に停止

### Level 2: 実践的な機能確認

#### テスト4: テスト駆動開発（TDD）ループ

```bash
/ralph-loop "簡単な加算関数 add(a, b) を作成し、テストを書いてください。すべてのテストが通過したら<promise>DONE</promise>を出力してください。" --completion-promise "DONE" --max-iterations 10
```

**期待される結果**:
1. 関数の作成
2. テストコードの生成
3. テスト実行
4. エラーがあれば修正
5. すべてのテストが通過したら `<promise>DONE</promise>` を出力

---

## 📖 基本的な使用方法

### コマンド一覧

| コマンド | 機能 |
|---------|------|
| `/ralph-loop "<prompt>"` | 自律的な反復ループを開始 |
| `/cancel-ralph` | 実行中のループを停止 |
| `/help` | コマンドとオプションのヘルプ表示 |

### /ralph-loop コマンドのオプション

```bash
/ralph-loop "<prompt>" --max-iterations <n> --completion-promise "<text>"
```

| オプション | 説明 | デフォルト | 推奨値 |
|-----------|------|-----------|--------|
| `--max-iterations <n>` | 最大反復回数（安全対策） | 無制限 | **20-50** |
| `--completion-promise "<text>"` | 完了を示すフレーズ（完全一致） | なし | `"COMPLETE"` |

**重要**: `--max-iterations` は必ず設定してください。無限ループを防ぐための安全機構です。

### 使用例

#### 例1: REST API の構築

```bash
/ralph-loop "Build a REST API for todos. Requirements: CRUD operations, input validation, tests. Output <promise>COMPLETE</promise> when done." --completion-promise "COMPLETE" --max-iterations 50
```

#### 例2: 段階的な機能開発

```bash
/ralph-loop "Phase 1: User authentication (JWT, tests)
Phase 2: Product catalog (list/search, tests)
Phase 3: Shopping cart (add/remove, tests)

Output <promise>COMPLETE</promise> when all phases done." --completion-promise "COMPLETE" --max-iterations 100
```

#### 例3: テスト駆動開発（TDD）

```bash
/ralph-loop "Implement feature X following TDD:
1. Write failing tests
2. Implement feature
3. Run tests
4. If any fail, debug and fix
5. Refactor if needed
6. Repeat until all green
7. Output: <promise>COMPLETE</promise>" --completion-promise "COMPLETE" --max-iterations 30
```

---

## 💡 プロンプト作成のベストプラクティス

### ✅ 良いプロンプトの特徴

1. **明確な完了基準**
   ```markdown
   Build a REST API for todos.

   When complete:
   - All CRUD endpoints working
   - Input validation in place
   - Tests passing (coverage > 80%)
   - README with API docs
   - Output: <promise>COMPLETE</promise>
   ```

2. **段階的なゴール設定**
   ```markdown
   Phase 1: User authentication (JWT, tests)
   Phase 2: Product catalog (list/search, tests)
   Phase 3: Shopping cart (add/remove, tests)

   Output <promise>COMPLETE</promise> when all phases done.
   ```

3. **自己修正パターンの組み込み**
   ```markdown
   Implement feature X following TDD:
   1. Write failing tests
   2. Implement feature
   3. Run tests
   4. If any fail, debug and fix
   5. Refactor if needed
   6. Repeat until all green
   7. Output: <promise>COMPLETE</promise>
   ```

4. **エスケープハッチの設定**
   ```markdown
   After 15 iterations, if not complete:
   - Document what's blocking progress
   - List what was attempted
   - Suggest alternative approaches
   ```

### ❌ 避けるべきプロンプト

- **曖昧な完了基準**: "Build a todo API and make it good."
- **過度に大きなスコープ**: "Create a complete e-commerce platform."
- **検証不可能なタスク**: "Write code for feature X."（テストや基準がない）
- **主観的な判断が必要**: "デザインを良くして"

---

## 🛠️ トラブルシューティング

### 問題1: プラグインがインストールできない

**症状**: `/plugin install ralph-wiggum@claude-plugin-directory` が失敗する

**解決策**:
1. Claude Code のバージョンを確認: `claude --version`（v2.0以上が必要）
2. マーケットプレイスの更新: Claude Code を再起動
3. 手動確認: `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/ralph-wiggum/` が存在するか確認

### 問題2: コマンドが認識されない

**症状**: `/ralph-loop` を実行しても "Unknown command" エラー

**解決策**:
1. プラグインが正常にインストールされているか確認: `/plugin list`
2. Claude Code を再起動
3. プロジェクトディレクトリで再度 `claude` を起動

### 問題3: ループが無限に継続する

**症状**: `--completion-promise` を設定したのにループが止まらない

**原因**: 完了プロミスの文字列が完全一致しない（大文字小文字、スペース、括弧等）

**解決策**:
1. 完了プロミスの形式を統一: `<promise>COMPLETE</promise>`
2. プロンプトに明示的に記載: "Output <promise>COMPLETE</promise> when done."
3. `--max-iterations` を必ず設定して安全弁を確保

### 問題4: API コストが高くなる

**症状**: 長時間のループで API 使用量が増加

**解決策**:
1. `--max-iterations` を適切に設定（20-50程度）
2. プロンプトをより具体的に記述（無駄な反復を減らす）
3. 段階的なゴール設定で早期終了を促進
4. 一晩実行する場合は事前にコスト見積もりを確認

---

## 🧠 Ralph Loop の哲学

### 1. 反復 > 完璧
最初から完璧を目指さない。ループに任せて段階的に改善。

### 2. 失敗はデータ
「決定論的に悪い」= 失敗は予測可能で情報豊富。プロンプト調整に活用。

### 3. オペレーターのスキルが重要
成功はモデルの性能ではなく、**プロンプトの品質**に依存。

### 4. 粘り強さが勝つ
失敗しても諦めず、成功するまで反復。ループが自動的にリトライを処理。

---

## 📊 適用シーンと非推奨シーン

### ✅ Ralph Loop に適したタスク

| シーン | 理由 |
|--------|------|
| **明確な成功基準があるタスク** | テストや検証が自動化可能 |
| **反復改善が必要なタスク** | テストが通るまで修正を繰り返す |
| **グリーンフィールドプロジェクト** | 一晩放置して完成させる |
| **自動検証可能なタスク** | テスト、リンター、ビルド成功 |

### ❌ Ralph Loop に不向きなタスク

| シーン | 理由 |
|--------|------|
| **人間の判断が必要なタスク** | デザイン決定、主観的評価 |
| **ワンショット操作** | 反復の必要がない |
| **曖昧な成功基準** | 完了判定が不可能 |
| **本番環境デバッグ** | ターゲット絞り込みデバッグの方が効率的 |

---

## 🎯 実績・事例

Ralph Loop 技術を使用した実績：

- **Y Combinator ハッカソン**: 一晩で6つのリポジトリを自動生成
- **商業プロジェクト**: $50,000 の契約を $297 の API コストで完了
- **プログラミング言語開発**: "cursed" という言語を3ヶ月かけて作成

---

## 📚 参考リソース

### 公式ドキュメント
- [Claude Code プラグインドキュメント](https://code.claude.com/docs/en/plugins)
- [Claude Code 公式リポジトリ](https://github.com/anthropics/claude-code)

### コミュニティリソース
- [Original Ralph technique by Geoffrey Huntley](https://ghuntley.com/ralph/)
- [Ralph Orchestrator (improved implementation)](https://github.com/mikeyobrien/ralph-orchestrator)
- [ralph-claude-code (community fork)](https://github.com/frankbria/ralph-claude-code)
- [Awesome Claude - Ralph Wiggum](https://awesomeclaude.ai/ralph-wiggum)

### GitHub Issues
- [Ralph Wiggum プラグインの Issue](https://github.com/anthropics/claude-code/labels/ralph-wiggum)
- [Feature Request: File-Based Prompts](https://github.com/anthropics/claude-code/issues/15824)
- [BUG: newline characters issue](https://github.com/anthropics/claude-code/issues/12170)

---

## 🚀 次のステップ

### 推奨される学習パス

1. **基本的な使用法を習得** (1-2時間)
   - 簡単なループで動作確認
   - コマンドとオプションの理解

2. **プロンプトライティングの練習** (3-5時間)
   - 良いプロンプトと悪いプロンプトの比較
   - 完了基準の設定練習
   - 段階的なゴール設定

3. **実践プロジェクトで使用** (数日〜数週間)
   - TDD ワークフローでの活用
   - API 開発
   - テストカバレッジ改善

4. **高度なテクニック** (継続的)
   - 複数フェーズのプロジェクト
   - エスケープハッチの活用
   - コスト最適化

---

**作成日時**: 2025-12-31
**作成者**: Claude Code (Sonnet 4.5)
**環境**: macOS (Darwin 25.1.0), Claude Code v2.0.76
