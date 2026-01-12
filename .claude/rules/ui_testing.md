# UI Testing Rules

Chrome拡張（claude-in-chrome）を使用したUIテスト自動化のガイド。

## 概要

UIテスティングはPhase 2.5（Review Loop統合）で、ドキュメント品質評価と並行してWeb UI品質を検証するプロセス。

@.claude/agents/ui-verification-agent.md との連携により、ビジュアルテスト、レスポンス速度、アクセシビリティを5観点で自動評価。

## 前提条件

### Chrome MCP接続設定

1. **タブコンテキスト初期化**
```python
# 初回実行時に必ず実行
tabs_context_mcp(createIfEmpty=True)
```

2. **新規タブ作成**
```python
# テスト環境のタブを作成
tab_id = tabs_create_mcp()
```

3. **接続確認**
```python
# Tab IDが取得できることを確認
navigate(url="https://example.com", tabId=tab_id)
screenshot(tabId=tab_id)
```

## 使用可能なChrome MCPツール一覧

| ツール | 用途 | 主な関数 |
|--------|------|--------|
| **computer** | マウス・キーボード・スクリーンショット | left_click, type, screenshot, scroll |
| **read_page** | アクセシビリティツリー取得 | depth, filter, ref_id指定 |
| **find** | 自然言語要素検索 | query, tabId |
| **navigate** | URL遷移・履歴操作 | url, "forward", "back" |
| **form_input** | フォーム値入力 | ref, value, tabId |
| **javascript_tool** | JavaScript実行 | action="javascript_exec", text |
| **get_page_text** | テキスト抽出 | tabId |
| **upload_image** | スクリーンショット・ファイルアップロード | imageId, ref または coordinate |

## テストシナリオ例

### 1. ログインフロー検証
```markdown
1. navigate(url="https://app.example.com/login", tabId=tab_id)
2. screenshot() でログインページを確認
3. form_input(ref="email_field", value="test@example.com", tabId=tab_id)
4. form_input(ref="password_field", value="password123", tabId=tab_id)
5. left_click(ref="login_button", tabId=tab_id)
6. wait(duration=2) でページロード待機
7. screenshot() でダッシュボード表示を確認
```

### 2. フォームバリデーション
```markdown
1. find(query="email input field", tabId=tab_id)
2. form_input(ref=ref_email, value="invalid-email", tabId=tab_id)
3. left_click(ref="submit_button", tabId=tab_id)
4. screenshot() でエラーメッセージを確認
```

### 3. レスポンシブデザイン
```markdown
1. resize_window(width=375, height=667, tabId=tab_id)  # iPhone
2. screenshot()
3. resize_window(width=768, height=1024, tabId=tab_id) # iPad
4. screenshot()
5. resize_window(width=1920, height=1080, tabId=tab_id) # Desktop
6. screenshot()
```

### 4. キーボードナビゲーション
```markdown
1. read_page(filter="interactive", tabId=tab_id)
2. key(text="Tab", repeat=5, tabId=tab_id)  # フォーカス移動確認
3. screenshot() で各ステップのフォーカス状態を確認
4. key(text="Enter", tabId=tab_id) でアクション実行
```

### 5. エラーハンドリング
```markdown
1. navigate(url="https://app.example.com/nonexistent", tabId=tab_id)
2. screenshot() で404ページを確認
3. find(query="error message", tabId=tab_id)
4. screenshot() で適切なエラー表示を確認
```

## UI検証エージェント連携

### Task tool経由での起動

```python
# UI検証エージェント起動
ui_verification_result = Task(
    description=f"UI品質検証 - イテレーション {iteration}",
    prompt=f"""
    @.claude/agents/ui-verification-agent.md の仕様に従い、以下のWebアプリケーションをテストしてください。

    **アプリケーション情報**:
    - URL: `{app_url}`
    - 対象ページ: {target_pages}
    - イテレーション: {iteration}

    **評価指示**:
    5観点（視覚的品質、レスポンス速度、アクセシビリティ、ユーザビリティ、モバイル対応）で評価し、
    以下のファイルを出力してください:

    1. `ui_quality_score.json`: 各スコアと総合点
    2. `ui_test_report.md`: 詳細テストレポート
    3. `ui_screenshots/`: テスト時のスクリーンショット保存

    **出力先**: `{evidence_dir}/iteration_{iteration:03d}/ui_test/`

    **重要**: Chrome MCPツールを使用してブラウザを自動操作し、各テストシナリオを実行してください。
    評価基準は @.claude/skills/_shared/ui_evaluation_criteria.md を参照してください。
    """,
    subagent_type="general-purpose",
    model="sonnet",
    timeout=900000  # 15分 = 900,000ミリ秒
)
```

## Review Loop統合（Phase 2.5）

### ドキュメント品質 + UI品質の複合判定

```python
# Step 1: ドキュメント品質評価（既存フロー）
doc_review = Task(
    description=f"ドキュメント品質レビュー",
    prompt=f"@.claude/agents/review-agent.md に従い評価...",
    subagent_type="general-purpose",
    model="sonnet",
    timeout=600000  # 10分
)
doc_quality_score = parse_quality_score(doc_review)

# Step 2: UI品質評価（Phase 2.5 新機能）
ui_review = Task(
    description=f"UI品質テスト",
    prompt=f"@.claude/agents/ui-verification-agent.md に従い評価...",
    subagent_type="general-purpose",
    model="sonnet",
    timeout=900000  # 15分
)
ui_quality_score = parse_quality_score(ui_review)

# Step 3: 複合判定
combined_score = (doc_quality_score * 0.6) + (ui_quality_score * 0.4)

if combined_score >= 70:
    integrate_and_finalize(results)
    return "SUCCESS"
else:
    return trigger_replan(doc_review, ui_review)
```

## 評価基準（100点満点）

| 観点 | 配点 | 評価項目 | 合格基準 |
|------|------|--------|--------|
| **視覚的品質** | 25点 | レイアウト整合性、色彩再現、タイポ無し | ≧20点 |
| **レスポンス速度** | 20点 | ページロード時間、インタラクション遅延 | ≧15点 |
| **アクセシビリティ** | 20点 | WCAG 2.1 AA準拠、スクリーンリーダー対応 | ≧15点 |
| **ユーザビリティ** | 20点 | ナビゲーション、エラーハンドリング、確認ダイアログ | ≧15点 |
| **モバイル対応** | 15点 | レスポンシブ、タッチターゲット(44×44px)、ビューポート設定 | ≧11点 |
| **総合合格基準** | - | 総合点≧70点、かつ各観点≧最低基準 | **70点以上** |

## トラブルシューティング

### Chrome MCP接続エラー

**エラー**: "Tab context not found"
```markdown
解決策:
1. tabs_context_mcp(createIfEmpty=True) を再実行
2. Chrome再起動
3. エージェント再起動
```

### タブID無効エラー

**エラー**: "Tab ID 999 is invalid"
```markdown
解決策:
1. tabs_context_mcp() で現在のTab IDを確認
2. 無効なTab IDの使用を避ける
3. 新規タブが必要な場合は tabs_create_mcp() を実行
```

### タイムアウト対策

```markdown
- 画像多用ページ: timeout = 1200000（20分）に延長
- APIヘビーページ: 事前データ準備で高速化
- 長期バックグラウンド: run_in_background=True で非同期実行
```

### スクリーンショット取得失敗

```markdown
1. wait(duration=1) でページロード完了を待機
2. read_page() でDOM確認
3. javascript_tool で動的要素ロード待機
```

## チェックリスト

テスト実行前に以下を確認：

- [ ] Chrome MCP接続が確立されているか？ (tabs_context_mcp)
- [ ] テスト対象URLが正しいか？
- [ ] 各テストシナリオが明確か？
- [ ] スクリーンショット保存先が指定されているか？
- [ ] タイムアウト設定は適切か？
- [ ] モバイル・デスクトップ両方のテストが含まれているか？
- [ ] アクセシビリティ評価が含まれているか？
- [ ] エラーケースのテストが含まれているか？

## 参照

- @.claude/agents/ui-verification-agent.md - UI検証エージェント仕様
- @.claude/agents/review-agent.md - レビューエージェント（ドキュメント品質）
- @.claude/skills/_shared/ui_evaluation_criteria.md - UI評価基準詳細
- @.claude/rules/review_loop.md - Review Loop統合ルール
- [Claude in Chrome MCP ドキュメント](https://anthropic.com/claude-in-chrome)
