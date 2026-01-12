# トリガーワード クイックリファレンス

**作成日**: 2025-12-30
**バージョン**: 1.0
**対応ツール**: Claude Code, Antigravity, Cursor, Codex

---

## 📋 トリガーワード一覧

### 日次タスク管理トリガー（Ultra Light 4コマンド運用）

| トリガー | 目的 | 対応ツール |
|----------|------|-----------|
| **タスクメモ** | inbox に気がかりを追記（何行でもOK） | 全ツール |
| **次の一手** | inbox から1件選択して完了までのTodoパターン生成（2〜5個） | 全ツール |
| **全部の一手** | inbox 全件のTodoパターンを一括表示（柔軟な数） | 全ツール |
| **これやる** | candidates から tasks へ確定 | 全ツール |
| **タスクプロンプト生成** | tasksをClaude Code実行可能なプロンプト形式に変換 | Claude Code |
| **今日のタスク** | 日次タスク開始 | 全ツール |
| **作業開始** | 日次タスク開始 | 全ツール |

---

### PMBOKフェーズ系トリガー

#### 1. Initiating（立ち上げ）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| プロジェクト憲章 | draft_project_charter.md | Flow/YYYYMM/YYYY-MM-DD/ |
| ステークホルダー分析 | draft_stakeholder_analysis.md | Flow/YYYYMM/YYYY-MM-DD/ |
| プロダクト定義 | draft_program_definition.md | Flow/YYYYMM/YYYY-MM-DD/ |

---

#### 2. Discovery（発見）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| ペルソナ作成 | draft_persona.md | Flow/YYYYMM/YYYY-MM-DD/ |
| ジャーニーマップ | draft_user_journey_map.md | Flow/YYYYMM/YYYY-MM-DD/ |
| 仮説マップ | draft_assumption_map.md | Flow/YYYYMM/YYYY-MM-DD/ |
| 課題定義 | draft_problem_statement.md | Flow/YYYYMM/YYYY-MM-DD/ |
| ソリューション定義 | draft_solution_definition.md | Flow/YYYYMM/YYYY-MM-DD/ |
| 検証計画 | draft_validation_plan.md | Flow/YYYYMM/YYYY-MM-DD/ |
| UXリサーチ | draft_ux_research_overview.md | Flow/YYYYMM/YYYY-MM-DD/ |
| インタビュー設計 | draft_interview_guide.md | Flow/YYYYMM/YYYY-MM-DD/ |

---

#### 3. Research（調査）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| 競合調査 | draft_competitor_research.md | Flow/YYYYMM/YYYY-MM-DD/ |
| 市場規模推定 | draft_market_size_estimation.md | Flow/YYYYMM/YYYY-MM-DD/ |
| デスクリサーチ | draft_desk_research.md | Flow/YYYYMM/YYYY-MM-DD/ |
| 顧客調査 | draft_customer_research.md | Flow/YYYYMM/YYYY-MM-DD/ |

---

#### 4. Planning（計画）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| WBS作成 | draft_wbs.md | Flow/YYYYMM/YYYY-MM-DD/ |
| プロダクトバックログ初期化 | backlog.yaml | Flow/YYYYMM/YYYY-MM-DD/ |
| リスク計画 | draft_risk_plan.md | Flow/YYYYMM/YYYY-MM-DD/ |
| プロジェクトスコープ記述書 | draft_project_scope.md | Flow/YYYYMM/YYYY-MM-DD/ |
| プロダクト要求仕様書 | draft_prd.md | Flow/YYYYMM/YYYY-MM-DD/ |
| ロードマップ作成 | draft_product_roadmap.md | Flow/YYYYMM/YYYY-MM-DD/ |

---

#### 5. Executing（実行）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| Development | 開発メニュー表示 | - |
| 開発環境初期化 | draft_setup.md | Flow/YYYYMM/YYYY-MM-DD/ |
| 開発計画作成 | draft_development_plan.md | Flow/YYYYMM/YYYY-MM-DD/ |
| ストーリー実装 | draft_story_implementation.md | Flow/YYYYMM/YYYY-MM-DD/ |
| スプリントゴール | sprint_goal.md | Flow/YYYYMM/YYYY-MM-DD/ |

---

#### 6. Monitoring（監視）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| ステータスレポート | status_report.md | Flow/YYYYMM/YYYY-MM-DD/ |
| 変更要求 | change_request.md | Flow/YYYYMM/YYYY-MM-DD/ |

---

#### 7. Closing（終結）

| トリガー | 生成物 | 保存先 |
|----------|--------|--------|
| レッスンズラーンド | lessons_learned.md | Flow/YYYYMM/YYYY-MM-DD/ |
| 移行文書 | transition_document.md | Flow/YYYYMM/YYYY-MM-DD/ |

---

## 🔄 確定反映フロー

ドラフトを確定版に移動する場合：

| トリガー | 処理 |
|----------|------|
| 確定反映して | Flow/YYYYMM/YYYY-MM-DD/draft_*.md → Stock/programs/.../documents/[phase]/*.md |

---

## 💡 使い方例

### 日次タスク管理の典型的な流れ

```
朝（9:00）:
ユーザー: タスクメモ
AI: 何が気がかりですか？何行でも入力できます。

    【入力例】
    ・[inbox項目1]
    ・[inbox項目2]
    ・[inbox項目3]

ユーザー: [inbox項目1] / [inbox項目2] / [inbox項目3] / [inbox項目4] / [inbox項目5]
AI: ✅ inboxに追加しました

朝（9:05）- パターン1: 次の一手（1件選択）:
ユーザー: 次の一手
AI: inboxから1件選んでください：
    1. [inbox項目1]
    2. [inbox項目2]
    3. [inbox項目3]
ユーザー: 1
AI: 「[inbox項目1]」の完了までのTodo候補：

    【パターンA: [アプローチ名]】
    1. [Todo1]
    2. [Todo2]
    3. [Todo3]
    → 完了: [最終成果物]

    【パターンB: [アプローチ名]】
    1. [Todo1]
    2. [Todo2]
    3. [Todo3]
    4. [Todo4]
    → 完了: [最終成果物]

    💡 おすすめ: パターンA（1→2→3の順で実行）
    理由: [このTodo組み合わせを推奨する理由を1-2行で説明]

    どのパターンで進めますか？(A/B/C...)

朝（9:05）- パターン2: 全部の一手（全件一括）:
ユーザー: 全部の一手
AI: inbox全件の完了までのTodo候補：

    【例1: [inbox項目1]】
    パターンA: [アプローチ名]
      1. [Todo1]
      2. [Todo2]
      3. [Todo3]
      → 完了: [最終成果物]

    パターンB: [アプローチ名]
      1. [Todo1]
      2. [Todo2]
      3. [Todo3]
      4. [Todo4]
      → 完了: [最終成果物]

    💡 おすすめ: パターンA（1→2→3の順で実行）
    理由: [このTodo組み合わせを推奨する理由を1-2行で説明]

    【例2: [inbox項目2]】
    パターンA: [アプローチ名]
      1. [Todo1]
      2. [Todo2]
      3. [Todo3]
      → 完了: [最終成果物]

    💡 おすすめ: パターンA（1→2→3の順で実行）
    理由: [このTodo組み合わせを推奨する理由を1-2行で説明]

    どの項目について作業しますか？番号で指定:
    1. [inbox項目1]
    2. [inbox項目2]
ユーザー: 1
AI: どのパターンで進めますか？(A/B/C...)
ユーザー: A

朝（9:10）:
ユーザー: これやる
AI: どれをやりますか？(A/B/C、複数選択可、例: A,C または 全部)
ユーザー: A,C
AI: 各パターンのDone定義を選んでください：

    パターンA: [アプローチ名]
    1. [A用完了基準1]
    2. [A用完了基準2]
    3. [A用完了基準3]

    パターンC: [アプローチ名]
    1. [C用完了基準1]
    2. [C用完了基準2]

    💡 おすすめ: A=1または2, C=1
    理由: パターンAは1と2のどちらも適切（1は早期完了重視、2は品質重視）。パターンCは1が最適。

    入力形式: A=1, C=2（カンマ区切りで指定）
ユーザー: A=1, C=2
AI: ✅ tasksに追加しました（2個追加）
```

---

### PMBOKフェーズの典型的な流れ

```
プロジェクト開始時:
ユーザー: プロジェクト憲章
AI: プロジェクト名を教えてください
ユーザー: [プロジェクト名を入力]
AI: [質問応答を繰り返し]
AI: ✅ draft_project_charter.md を作成しました

発見フェーズ:
ユーザー: ペルソナ作成
AI: ペルソナ名を教えてください
ユーザー: [ペルソナ名を入力]
AI: [質問応答を繰り返し]
AI: ✅ draft_persona.md を作成しました

確定反映:
ユーザー: 確定反映して
AI: draft_persona.md を Stock/programs/.../documents/discovery/ に移動しました
```

---


## 📚 関連ドキュメント

- **統合ガイド**: `docs/ai/AI_TOOLS_GUIDE.md`
- **PMBOKワークフロー**: `docs/ai/pmbok_workflow.md`
- **システム概要**: `docs/ai/overview.md`
- **プロジェクトコンテキスト**: `CLAUDE.md`

---


**更新履歴**:
- 2025-12-30 v1.1: Ultra Light 4コマンド運用（タスクプロンプト生成追加）
- 2025-12-30 v1.0: 初版リリース（トリガーワード一覧）

**作成者**: Claude Sonnet 4.5
**設計方針**: 競合回避、明確な分類、使い方例の提示
