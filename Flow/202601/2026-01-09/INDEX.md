# Chrome拡張UIテスト検証シナリオ - ファイルインデックス

**プロジェクト**: AIPM v0 - UIテスト自動化
**作成日**: 2026-01-09
**対象ツール**: Chrome拡張 MCP（Model Context Protocol）

---

## ファイル構成概観

```
Flow/202601/2026-01-09/
│
├── 📋 INDEX.md (このファイル)
│   └─ 全体のナビゲーション＆ファイル関係図
│
├── 📑 UI_TEST_SUMMARY.md ← 🟢 ここから始める
│   ├─ 5シナリオの概要
│   ├─ 成功配点の説明
│   ├─ 実行フロー図
│   ├─ 品質ゲート判定基準
│   └─ FAQ＆トラブルシューティング
│
├── 📘 ui_verification_implementation_guide.md
│   ├─ 詳細な実装方法
│   ├─ 各シナリオのコード例
│   ├─ Chrome MCPツール使用方法
│   ├─ エラーハンドリング戦略
│   └─ ベストプラクティス
│
├── 📦 ui_verification_scenarios.json (800+ 行)
│   ├─ Scenario 1: ログインフロー (14 steps)
│   ├─ Scenario 2: フォーム送信 (16 steps)
│   ├─ Scenario 3: ページ遷移 (17 steps)
│   ├─ Scenario 4: Ajax/非同期 (15 steps)
│   ├─ Scenario 5: エラーハンドリング (20 steps)
│   └─ メタデータ＆設定
│
└── 📁 ui_verification/ (テスト実行後に生成)
    ├── screenshots/ (15-18枚)
    │   └─ {scenario}_{step}_{description}.jpeg
    ├── ui_verification_report.md
    └── ui_verification_scores.json
```

---

## ファイル詳細ガイド

### 1️⃣ UI_TEST_SUMMARY.md（全体図）

**推奨読破時間**: 5-10分 ✨

**含まれる内容**:
- 各シナリオの概要（1ページ/シナリオ）
- 成功配点の内訳（視覚品質、パフォーマンス等）
- 実行フロー図＆タイムアウト設定
- 品質ゲート判定基準
- Chrome MCPツール使用マトリックス
- エラーハンドリング戦略

**このファイルを読むべき人**:
- [ ] UIテスト全体の構図を理解したい
- [ ] 各シナリオの成功基準を知りたい
- [ ] 所要時間を見積もりたい
- [ ] 品質判定基準を確認したい

**主な図表**:
```
┌─ 5シナリオの概要表
├─ Chrome MCPツール使用マトリックス（5x12）
├─ 実行フロー図（Phase 1-3）
├─ 並列実行による時間短縮図
├─ 品質ゲート判定フロー
└─ 依存関係＆実行順序図
```

---

### 2️⃣ ui_verification_implementation_guide.md（実装手引き）

**推奨読破時間**: 15-20分 📚

**含まれる内容**:
- Phase 1: 環境セットアップ（詳細手順＆コード例）
- Phase 2: 各シナリオの実装方法
  - Scenario 1: ログイン（Python/疑似コード）
  - Scenario 2: フォーム（フィールド入力＆バリデーション）
  - Scenario 3: ページ遷移（URL検証チェックリスト）
  - Scenario 4: Ajax（ネットワークリクエスト確認）
  - Scenario 5: エラー（APIエラーシミュレーション）
- Phase 3: レポート生成＆品質判定
- トラブルシューティング（4パターン）
- ベストプラクティス＆並列実行

**このファイルを読むべき人**:
- [ ] 実際にテストを実装・実行する
- [ ] コード例を参照したい
- [ ] テスト失敗時の対応方法を知りたい
- [ ] パフォーマンス最適化を検討している

**コード例の数**: 15+ 個

**トラブルシューティング**:
- 問題1: "Failed to find element: 401"
- 問題2: スクリーンショットが空白
- 問題3: 要素が見つからない
- 問題4: JavaScript実行が失敗

---

### 3️⃣ ui_verification_scenarios.json（仕様書）

**推奨読破時間**: 20-30分 📖

**構造**（JSON形式）:

```json
{
  "metadata": {
    "version": "1.0",
    "total_scenarios": 5,
    "execution_time_estimate_minutes": 10
  },
  "scenarios": [
    {
      "id": "scenario_001",
      "name": "ログインフロー検証",
      "steps": [
        {
          "step_number": 1,
          "action": "tabs_context_mcp",
          "parameters": {...},
          "expected_output": {...},
          "timeout_seconds": 5
        },
        ...（14ステップ）
      ],
      "success_criteria": {
        "required_checks": [
          {"name": "...", "points": 20, "failure_mode": "..."}
        ],
        "total_points": 100,
        "passing_score": 70
      },
      "error_handling": {...}
    }
  ]
}
```

**含まれる情報**:
- 各Scenario の詳細定義
- ステップバイステップの仕様
- 使用ツール＆パラメータ
- 期待出力＆タイムアウト
- 成功基準＆配点
- エラーハンドリング戦略

**このファイルを読むべき人**:
- [ ] Scenario の仕様を参照したい
- [ ] ステップ-by-ステップの詳細を確認したい
- [ ] APIエンドポイント＆パラメータを知りたい
- [ ] 成功基準を確認したい

**ファイルサイズ**: 約 800行

---

## 読破フロー図

### パターンA: 全体理解（初回）

```
┌─────────────────────────────────────┐
│ UI_TEST_SUMMARY.md                  │ ← ここから開始
│ (全体図＆概要)                       │ 5-10分
│ • シナリオ概要                       │
│ • 成功配点                           │
│ • 実行フロー                         │
└─────────┬───────────────────────────┘
          ↓ 理解できた
┌─────────────────────────────────────┐
│ ui_verification_scenarios.json       │ 20-30分
│ (詳細仕様＆ステップ定義)            │
│ • 各Scenario の仕様                 │
│ • ステップ定義                       │
│ • エラーハンドリング                 │
└─────────────────────────────────────┘
```

### パターンB: 実装＆実行（2回目以降）

```
┌─────────────────────────────────────┐
│ ui_verification_implementation_guide.md  │ ← ここから開始
│ (実装手順＆コード例)                 │ 15-20分
│ • Phase 1-3 の実行手順              │
│ • Scenario 別コード例                │
│ • トラブルシューティング             │
└─────────┬───────────────────────────┘
          ↓ 参照しながら実装
┌─────────────────────────────────────┐
│ ui_verification_scenarios.json       │ 必要時参照
│ (ステップ参照＆値の確認)            │
│ • 各ステップの詳細                   │
│ • テストデータ                       │
│ • 期待出力                           │
└─────────────────────────────────────┘
```

### パターンC: トラブル対応

```
┌─────────────────────────────────────┐
│ UI_TEST_SUMMARY.md                  │ ← FAQ & チェックリスト
│ (FAQ＆トラブルシューティング)       │
│ • Q&A (Q1-Q5)                       │
│ • 一般的なエラーと対応表            │
└─────────┬───────────────────────────┘
          ↓ 詳細が必要な場合
┌─────────────────────────────────────┐
│ ui_verification_implementation_guide.md  │
│ (詳細なエラーハンドリング)           │
│ • 4パターンのトラブル対応            │
│ • リトライ戦略                       │
│ • コード例                           │
└─────────────────────────────────────┘
```

---

## ドキュメント相互参照マップ

```
ui_verification_scenarios.json
    ├─ metadata.version
    ├─ metadata.total_scenarios ──────────→ UI_TEST_SUMMARY.md
    │                                       [シナリオ詳細ガイド]
    │
    ├─ scenarios[0].name
    │  scenarios[0].steps[].action
    │       ↓
    │  "navigate" ───────────────→ implementation_guide.md
    │  "find"                      [各ツールの使用方法]
    │  "form_input"
    │  "computer"
    │  "read_page"
    │  "javascript_tool"
    │  etc.
    │
    ├─ scenarios[].success_criteria
    │       ↓
    │  points, failure_mode ─────→ UI_TEST_SUMMARY.md
    │                              [成功配点の内訳]
    │
    └─ scenarios[].error_handling
            ↓
       recovery_actions ──────────→ implementation_guide.md
                                   [エラーハンドリング戦略]
```

---

## 実行方法別の参照ファイル

### ケース1: 初めてテストする

```
① UI_TEST_SUMMARY.md を読む (全体理解)
   ↓
② scenarios.json を軽く参照 (各Scenario の概要)
   ↓
③ implementation_guide.md で環境セットアップ (Phase 1)
   ↓
④ implementation_guide.md で Scenario 1 を実装 (Phase 2-1)
   ↓
⑤ scenarios.json で ステップ詳細を確認しながら実装
   ↓
⑥ 残り Scenario 2-5 を同様に実装
   ↓
⑦ implementation_guide.md で レポート生成 (Phase 3)
```

### ケース2: 2回目以降のテスト実行

```
① implementation_guide.md の実行手順を参照
   ↓
② scenarios.json でパラメータ確認
   ↓
③ 各Scenario を順序実行
   ↓
④ UI_TEST_SUMMARY.md で結果を解釈
```

### ケース3: 結果が 70 点未満

```
① UI_TEST_SUMMARY.md で品質ゲート基準を確認
   ↓
② implementation_guide.md で該当 Scenario のトラブル対応を参照
   ↓
③ scenarios.json でステップ詳細を再確認
   ↓
④ UI修正 → 再テスト実行
```

---

## 各ドキュメントのハイライト

### 📑 UI_TEST_SUMMARY.md

**ここだけは絶対読むべき**:
- ✅ 実行フロー図（Phase 1-3）
- ✅ 品質ゲート判定基準（420/350/未満）
- ✅ Chrome MCPツール使用マトリックス
- ✅ 依存関係＆実行順序
- ✅ FAQ（Q1-Q5）

**スキップできる部分**:
- 詳細なコード例
- 全ステップの説明
- エラーハンドリングの実装詳細

---

### 📘 implementation_guide.md

**ここだけは絶対読むべき**:
- ✅ Phase 1: 環境セットアップ
- ✅ Scenario 1: ログインフロー（コード例付き）
- ✅ トラブルシューティング（4パターン）
- ✅ ベストプラクティス

**詳しく読むべき**:
- 実装中のシナリオのコード例
- エラー発生時の対応方法

**軽く見る程度**:
- 他のシナリオの詳細（scenarios.json で確認）

---

### 📦 scenarios.json

**ここだけは絶対参照すべき**:
- ✅ 実装中の Scenario のステップ定義
- ✅ テストデータ（test@example.com 等）
- ✅ 期待出力＆タイムアウト
- ✅ 成功基準＆配点

**軽く参照する程度**:
- 全体構造（UI_TEST_SUMMARY.md で理解）
- 他の Scenario（必要時のみ）

---

## ナビゲーション例

### 「Scenario 2 の実装方法が知りたい」

```
① UI_TEST_SUMMARY.md
   → Scenario 2 セクション
      "複数フィールドのフォーム入力 → 送信 → バックエンド検証"
   ↓
② scenarios.json
   → scenarios[1] (Scenario 2)
      → steps 配列 (16ステップ)
      → success_criteria (6つのチェック項目, 100点)
   ↓
③ implementation_guide.md
   → "パターン2: フォーム送信検証" セクション
      → Python/疑似コード例
      → テストデータ（name: 田中太郎）
      → バリデーションテスト
```

---

### 「テストが失敗した。対応方法は？」

```
① UI_TEST_SUMMARY.md
   → "エラーハンドリング戦略" セクション
      → 標準リトライポリシー
      → 一般的なエラーと対応表
   ↓
② scenarios.json
   → 失敗したScenarioのセクション
      → error_handling セクション
      → recovery_actions 配列
   ↓
③ implementation_guide.md
   → "トラブルシューティング" セクション
      → 問題別の解決方法
      → コード例
```

---

### 「並列実行で高速化したい」

```
① UI_TEST_SUMMARY.md
   → "実行フロー図" セクション
      → グループA/B/C の構成
      → 並列可能なシナリオ
      → 依存関係＆実行順序
   ↓
② implementation_guide.md
   → "ベストプラクティス" セクション
      → "1. 並列実行による高速化" サブセクション
      → サブエージェント並列実行コード例
```

---

## ファイル用語集

| 用語 | 説明 | 参照ファイル |
|------|------|-----------|
| **Scenario** | テストの大カテゴリー（5個） | summary.md |
| **Step** | Scenario内の単位操作（14-20個/Scenario） | scenarios.json |
| **Action** | Chrome MCPツール（navigate, find等） | implementation_guide.md |
| **Success Criteria** | テスト合格条件（6個/Scenario） | scenarios.json |
| **Points** | 各チェック項目の配点 | scenarios.json, summary.md |
| **Timeout** | 操作の最大待機時間 | scenarios.json |
| **Retry** | 失敗時の再試行（最大2回）| scenarios.json |
| **Error Handling** | エラー発生時の対応戦略 | scenarios.json, implementation_guide.md |

---

## チェックシート

### 初回セットアップ時

- [ ] UI_TEST_SUMMARY.md を読んだ（全体理解）
- [ ] scenarios.json の構造を理解した
- [ ] implementation_guide.md の Phase 1 を実施した
- [ ] テスト環境（localhost:3000）が起動している
- [ ] テストアカウントが存在する

### テスト実行前

- [ ] implementation_guide.md で該当 Scenario のコード例を確認
- [ ] scenarios.json でテストデータを確認
- [ ] 期待出力とタイムアウトを理解した
- [ ] エラーハンドリング戦略を確認した

### テスト実行後

- [ ] レポート（.md + .json）が生成された
- [ ] スコアが 100-500 の範囲内
- [ ] 品質ゲート判定を確認した（🟢/🟡/🔴）
- [ ] 結果を関係者に共有した

---

## よくある質問への回答

**Q: どのファイルから始めるべき？**
A: `UI_TEST_SUMMARY.md` から始めてください。5-10分で全体像が理解できます。

**Q: 実装方法が分からない場合は？**
A: `ui_verification_implementation_guide.md` を参照。コード例が豊富です。

**Q: 各ステップの詳細な定義は？**
A: `ui_verification_scenarios.json` を参照。JSON形式で完全に定義されています。

**Q: テスト失敗時の対応は？**
A: `UI_TEST_SUMMARY.md` のFAQ + `implementation_guide.md` のトラブルシューティング を参照。

**Q: 実行時間を短縮できる？**
A: `UI_TEST_SUMMARY.md` の実行フロー図で並列実行パターンを確認。3並列で 60% 短縮可能。

---

## ドキュメント更新方針

| 更新項目 | 更新ファイル | 頻度 |
|---------|-----------|------|
| テスト結果 | `ui_verification_report.md` (生成) | 毎回実行後 |
| シナリオ追加 | `scenarios.json` | 必要時 |
| コード例更新 | `implementation_guide.md` | 月1回 |
| UI変更の反映 | `scenarios.json` + `implementation_guide.md` | 該当時 |
| FAQ更新 | `UI_TEST_SUMMARY.md` | 月1回 |

---

## 参考リンク

- Chrome拡張MCPツール: `@docs/implementation_guides/week1_ui_testing.md`
- LLM優先実行: `@.claude/rules/execution_preference.md`
- 並列実行: `@.claude/rules/parallel_execution.md`
- CLAUDE.md (プロジェクト定義): `@CLAUDE.md`

---

**Created**: 2026-01-09
**Version**: 1.0
**Maintainer**: Claude Code UI Testing Automation

このインデックスをブックマークして、テスト実行時に参照してください！
