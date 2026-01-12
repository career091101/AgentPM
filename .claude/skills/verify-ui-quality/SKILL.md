---
name: verify-ui-quality
description: |
  UI Verification Agentを起動してWebアプリケーションの品質を検証するスキル。

  Chrome MCPを活用し、視覚品質、レスポンス速度、アクセシビリティ、ユーザビリティ、モバイル対応の5観点でUIを評価。
  品質スコア70点以上で統合完了、未達の場合は改善推奨を提示します。

  使用タイミング:
  - UI実装完了後の品質検証
  - リリース前の最終チェック
  - UIリファクタリング後の確認

  所要時間: 15分（動的テスト） or 10分（静的解析フォールバック）
  出力: ui_quality_score.json + ui_verification_report.md + screenshots/

trigger_keywords:
  - "UI品質検証"
  - "UIテスト実行"
  - "UI検証開始"
  - "Webアプリテスト"
  - "UIチェック"

stage: UI Testing
dependencies:
  - Chrome拡張MCPの接続
  - テスト対象URLの起動
output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/ui_verification/ui_quality_score.json
execution_time: 15分（動的テスト） or 10分（静的解析）
priority: P1
---

# Verify UI Quality Skill - UI品質自動検証

UI Verification Agentを起動してWebアプリケーションの品質を自動検証するスキル。

**Version**: 1.0（Week 1完成版 - 2026-01-09）

---

## このSkillでできること

1. **Chrome MCP統合**: Claude in Chrome拡張経由でブラウザ操作
2. **5観点評価**: 視覚品質（25点）、レスポンス速度（20点）、アクセシビリティ（20点）、ユーザビリティ（20点）、モバイル対応（15点）
3. **動的テスト**: スクリーンショット、パフォーマンス測定、インタラクション検証
4. **静的解析フォールバック**: Chrome MCP未接続時の代替処理
5. **スクリーンショット証跡**: 各検証段階のスクリーンショット自動保存
6. **品質ゲート**: 70点以上で統合完了、未達の場合は改善推奨

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | テスト対象URL、プロジェクト名、検証シナリオ（オプション） |
| **出力** | ui_quality_score.json + ui_verification_report.md + screenshots/ |
| **次のSkill** | 統合完了 or UI改善 |

---

## Instructions

**実行モード**: 自律実行（品質ゲートで停止）
**推定所要時間**: 15分（動的テスト） or 10分（静的解析フォールバック）

### Phase 1: 入力バリデーション

#### STEP 1: パラメータ確認

```markdown
## 必須パラメータ
- **target_url**: テスト対象URL（例: `http://localhost:3000`）
- **project_name**: プロジェクト名（例: `創業支援・新規事業開発（AIエージェント）`）

## オプションパラメータ
- **scenarios**: 実行するシナリオ（省略時は全5シナリオ）
  - `login_flow`: ログインフロー検証
  - `form_validation`: フォームバリデーション検証
  - `responsive_design`: レスポンシブデザイン検証
  - `keyboard_navigation`: キーボードナビゲーション検証
  - `error_handling`: エラーハンドリング検証

## 検証例

**入力例**:
```json
{
  "target_url": "http://localhost:3000",
  "project_name": "創業支援・新規事業開発（AIエージェント）",
  "scenarios": ["login_flow", "form_validation", "responsive_design"]
}
```
```

#### STEP 2: 出力ディレクトリ作成

```python
import os
from pathlib import Path
from datetime import datetime

# 日付ベースのディレクトリ構造
today = datetime.now()
year_month = today.strftime("%Y%m")
date = today.strftime("%Y-%m-%d")

# 出力ディレクトリ
base_dir = Path(f"/Users/yuichi/AIPM/aipm_v0/Flow/{year_month}/{date}")
evidence_dir = base_dir / "ui_verification_evidence"
screenshots_dir = evidence_dir / "screenshots"

# ディレクトリ作成
os.makedirs(screenshots_dir, exist_ok=True)

print(f"✅ 出力ディレクトリ作成完了: {evidence_dir}")
```

**出力構造**:
```
Flow/{YYYYMM}/{YYYY-MM-DD}/ui_verification_evidence/
├── ui_quality_score.json
├── ui_verification_report.md
└── screenshots/
    ├── 01_desktop_initial.png
    ├── 02_desktop_navigation.png
    ├── 03_desktop_form_error.png
    ├── 04_tablet_768x1024.png
    ├── 05_mobile_375x667.png
    └── ...
```

---

### Phase 2: Chrome MCP接続確認

#### STEP 3: Chrome拡張接続チェック

```python
# Chrome MCP接続確認
try:
    # MCP接続テスト
    context = mcp__claude_in_chrome__tabs_context_mcp(createIfEmpty=True)

    if context and "tabs" in context:
        chrome_available = True
        print("✅ Chrome MCP接続成功（動的テスト実行）")
    else:
        chrome_available = False
        print("⚠️ Chromeが起動していません（静的解析モードで実行）")

except Exception as e:
    chrome_available = False
    print(f"❌ Chrome MCP接続失敗: {e}")
    print("→ 静的解析モードで実行します")
```

**接続確認の重要性**:
- Chrome拡張が有効化されていない場合、動的テストは実行不可
- フォールバックモードでは静的解析のみ実行（スコア調整あり）
- Manager Skillは起動前に必ずこのチェックを実行すること

---

### Phase 3: UI Verification Agent起動

#### STEP 4: Task tool経由でエージェント起動

```python
from task import Task

# 検証シナリオのデフォルト設定
if not scenarios:
    scenarios = ["login_flow", "form_validation", "responsive_design",
                 "keyboard_navigation", "error_handling"]

# UI Verification Agent起動（Task tool）
ui_verification_result = Task(
    description=f"UIテスト検証 - {project_name}",
    prompt=f"""
    @.claude/agents/ui-verification-agent.md の仕様に従い、以下のWebアプリケーションを検証してください。

    **Chrome MCP接続状態**: {"✅ 接続成功（動的テスト実行）" if chrome_available else "❌ 接続失敗（静的解析モード）"}

    **テスト情報**:
    - テスト対象URL: `{target_url}`
    - プロジェクト名: `{project_name}`
    - ビューポートサイズ: デスクトップ（1920x1080）、タブレット（768x1024）、モバイル（375x667）
    - 検証シナリオ: {', '.join(scenarios)}

    **評価指示**:
    {"5観点（視覚品質、レスポンス速度、アクセシビリティ、ユーザビリティ、モバイル対応）で動的テストを実行" if chrome_available else "静的解析モード（レスポンス速度測定を除外）"}

    以下のファイルを出力してください:
    1. `ui_quality_score.json`: 各スコアと総合点
    2. `ui_verification_report.md`: 詳細レポート
    3. `screenshots/`: スクリーンショット群（各検証段階）

    **出力先**: `{evidence_dir}/`

    **重要**:
    - 出力ファイルは必ず上記ディレクトリに保存してください。
    - 評価基準は @.claude/agents/ui-verification-agent.md を参照してください。
    - 検証シナリオは @.claude/config/ui_verification.json を参照してください。
    """,
    subagent_type="general-purpose",
    model="sonnet",
    timeout=900000  # 15分 = 900,000ミリ秒
)

print("✅ UI Verification Agent起動完了")
```

**設定パラメータ**:
- `subagent_type="general-purpose"`: 汎用エージェント（Chrome MCPツール使用可能）
- `model="sonnet"`: バランス重視（推奨）
- `timeout=900000`: 15分タイムアウト（動的テスト想定）

---

### Phase 4: 検証結果取得

#### STEP 5: ui_quality_score.json読み込み

```python
import json
from pathlib import Path

# スコアファイル読み込み
score_file = evidence_dir / "ui_quality_score.json"

if not score_file.exists():
    print("❌ ui_quality_score.json が見つかりません")
    print("→ UI Verification Agentの実行に失敗した可能性があります")
    return {"status": "ERROR", "message": "Score file not found"}

with open(score_file, 'r', encoding='utf-8') as f:
    quality_data = json.load(f)

# 品質スコア取得
total_score = quality_data.get("total_score", 0)
passed = quality_data.get("passed", False)
threshold = quality_data.get("threshold", 70)

print(f"✅ 品質スコア取得完了: {total_score}点 / 100点満点")
print(f"   - 視覚品質: {quality_data.get('visual_quality_score', 0)}点")
print(f"   - レスポンス速度: {quality_data.get('response_speed_score', 0)}点")
print(f"   - アクセシビリティ: {quality_data.get('accessibility_score', 0)}点")
print(f"   - ユーザビリティ: {quality_data.get('usability_score', 0)}点")
print(f"   - モバイル対応: {quality_data.get('mobile_support_score', 0)}点")
```

**スコア構造（ui_quality_score.json）**:
```json
{
  "total_score": 72,
  "visual_quality_score": 19,
  "response_speed_score": 16,
  "accessibility_score": 14,
  "usability_score": 15,
  "mobile_support_score": 11,
  "passed": true,
  "threshold": 70,
  "issues": [
    {
      "category": "visual_quality",
      "severity": "warning",
      "message": "本文の行間が1.2（推奨1.5以上）"
    },
    {
      "category": "accessibility",
      "severity": "error",
      "message": "画像の代替テキスト（alt属性）が3件不足"
    }
  ],
  "breakdown": {
    "visual_quality": {
      "score": 19,
      "max": 25,
      "weight": 0.25,
      "percentage": 76
    },
    "response_speed": {
      "score": 16,
      "max": 20,
      "weight": 0.20,
      "percentage": 80
    },
    "accessibility": {
      "score": 14,
      "max": 20,
      "weight": 0.20,
      "percentage": 70
    },
    "usability": {
      "score": 15,
      "max": 20,
      "weight": 0.20,
      "percentage": 75
    },
    "mobile_support": {
      "score": 11,
      "max": 15,
      "weight": 0.15,
      "percentage": 73
    }
  }
}
```

---

### Phase 5: 品質ゲート判定

#### STEP 6: 合否判定

```python
# 品質ゲート判定
if total_score >= threshold:
    judgment = "✅ 合格"
    action = "統合完了"
    print(f"{judgment}（{total_score}点 ≥ {threshold}点）")
    print(f"次のアクション: {action}")

elif total_score >= (threshold - 10):
    judgment = "⚠️ 条件付き合格"
    action = "警告ログ記録 + 統合"
    print(f"{judgment}（{total_score}点 ≥ {threshold - 10}点）")
    print(f"次のアクション: {action}")

else:
    judgment = "❌ 不合格"
    action = "UI改善必須"
    print(f"{judgment}（{total_score}点 < {threshold - 10}点）")
    print(f"次のアクション: {action}")
```

**判定基準**:
| 品質スコア | 判定 | 対応 |
|-----------|------|------|
| 70点以上 | ✅ 合格 | UI統合完了 |
| 60-69点 | ⚠️ 条件付き合格 | 警告ログ記録 + 統合 |
| 60点未満 | ❌ 不合格 | UI改善必須 |

---

### Phase 6: レポート生成

#### STEP 7: 改善推奨の抽出

```python
# issuesから改善推奨を抽出
issues = quality_data.get("issues", [])

# 優先度別に分類
high_priority = [issue for issue in issues if issue.get("severity") == "error"]
medium_priority = [issue for issue in issues if issue.get("severity") == "warning"]
low_priority = [issue for issue in issues if issue.get("severity") == "info"]

# 改善推奨レポート生成
improvement_report = f"""
## 改善推奨

### 高優先度（エラー）
{chr(10).join([f"- {issue['message']}" for issue in high_priority]) if high_priority else "なし"}

### 中優先度（警告）
{chr(10).join([f"- {issue['message']}" for issue in medium_priority]) if medium_priority else "なし"}

### 低優先度（改善提案）
{chr(10).join([f"- {issue['message']}" for issue in low_priority]) if low_priority else "なし"}
"""

print(improvement_report)
```

---

### Phase 7: スクリーンショット確認

#### STEP 8: スクリーンショット存在確認

```python
import os

# スクリーンショットディレクトリ確認
screenshot_files = list(screenshots_dir.glob("*.png"))

if screenshot_files:
    print(f"✅ スクリーンショット {len(screenshot_files)}件保存完了")
    for screenshot in sorted(screenshot_files):
        print(f"   - {screenshot.name}")
else:
    print("⚠️ スクリーンショットが保存されていません")
    print("   → Chrome MCP接続失敗の可能性があります")
```

**スクリーンショット命名規則**:
```
01_desktop_initial.png           # 初回ページ読み込み
02_desktop_navigation.png        # ナビゲーション操作後
03_desktop_form_error.png        # フォームエラー表示
04_tablet_768x1024.png           # タブレットサイズ
05_mobile_375x667.png            # モバイルサイズ
06_keyboard_focus.png            # キーボードフォーカス
07_modal_dialog.png              # モーダルダイアログ
```

---

### Phase 8: 最終サマリー出力

#### STEP 9: サマリーレポート生成

```python
from datetime import datetime

# サマリーレポート作成
summary = {
    "timestamp": datetime.now().isoformat(),
    "project_name": project_name,
    "target_url": target_url,
    "scenarios": scenarios,
    "chrome_mcp_available": chrome_available,
    "total_score": total_score,
    "judgment": judgment,
    "action": action,
    "high_priority_issues": len(high_priority),
    "medium_priority_issues": len(medium_priority),
    "low_priority_issues": len(low_priority),
    "screenshot_count": len(screenshot_files),
    "output_directory": str(evidence_dir)
}

# サマリーファイル出力
summary_file = evidence_dir / "verification_summary.json"
with open(summary_file, 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"✅ サマリーレポート保存完了: {summary_file}")
```

**サマリー出力例（verification_summary.json）**:
```json
{
  "timestamp": "2026-01-09T10:30:00",
  "project_name": "創業支援・新規事業開発（AIエージェント）",
  "target_url": "http://localhost:3000",
  "scenarios": ["login_flow", "form_validation", "responsive_design"],
  "chrome_mcp_available": true,
  "total_score": 72,
  "judgment": "✅ 合格",
  "action": "統合完了",
  "high_priority_issues": 1,
  "medium_priority_issues": 3,
  "low_priority_issues": 2,
  "screenshot_count": 7,
  "output_directory": "/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-09/ui_verification_evidence"
}
```

---

## フォールバック処理（静的解析モード）

### Chrome MCP未接続時の対応

#### STEP 10: 静的解析モードの実行

```python
if not chrome_available:
    print("⚠️ Chrome MCP未接続のため、静的解析モードで実行")

    # HTMLファイルの検索
    html_files = list(Path(".").rglob("*.html"))
    css_files = list(Path(".").rglob("*.css"))
    js_files = list(Path(".").rglob("*.js"))

    print(f"検出ファイル: HTML {len(html_files)}件、CSS {len(css_files)}件、JS {len(js_files)}件")

    # UI Verification Agent起動（静的解析モード）
    ui_verification_result = Task(
        description=f"UIテスト検証（静的解析） - {project_name}",
        prompt=f"""
        @.claude/agents/ui-verification-agent.md の仕様に従い、以下のWebアプリケーションを**静的解析モード**で検証してください。

        **Chrome MCP接続状態**: ❌ 接続失敗（静的解析モードで実行）

        **テスト情報**:
        - プロジェクト名: `{project_name}`
        - 検出ファイル: HTML {len(html_files)}件、CSS {len(css_files)}件、JS {len(js_files)}件

        **評価指示**:
        静的解析モードで以下を実行:
        1. HTMLファイル解析（セマンティックHTML、ARIA属性、見出し階層）
        2. CSSファイル解析（メディアクエリ、CSS変数、フォント設定）
        3. JavaScriptファイル解析（イベントリスナー、エラーハンドリング）

        **制限事項**:
        - レスポンス速度測定: 実行不可（20点除外）
        - スクリーンショット取得: 実行不可
        - インタラクション検証: 実行不可

        **スコア調整**:
        残り80点満点で再計算（視覚品質31%、アクセシビリティ31%、ユーザビリティ25%、モバイル対応19%）

        以下のファイルを出力してください:
        1. `ui_quality_score.json`: 各スコアと総合点（adjusted_max_score: 80）
        2. `ui_static_analysis_report.md`: 静的解析レポート

        **出力先**: `{evidence_dir}/`
        """,
        subagent_type="general-purpose",
        model="sonnet",
        timeout=600000  # 10分
    )

    print("✅ UI Verification Agent起動完了（静的解析モード）")
```

**静的解析モードの制限**:
- ✅ 実行可能: ARIA属性チェック、セマンティックHTML、CSS解析
- ❌ 実行不可: スクリーンショット、レスポンス速度測定、インタラクション検証

---

## エラーハンドリング

### タイムアウト処理

```python
try:
    ui_verification_result = Task(
        description=f"UIテスト検証 - {project_name}",
        prompt=f"...",
        subagent_type="general-purpose",
        model="sonnet",
        timeout=900000  # 15分
    )
except TimeoutError:
    print("❌ UI Verification Agent タイムアウト（15分）")

    # 部分的な結果を確認
    if score_file.exists():
        print("⚠️ 部分的な結果が出力されています")
        # 既存スコアを読み込み
    else:
        print("❌ 結果ファイルが生成されませんでした")
        return {"status": "TIMEOUT", "message": "No output generated"}
```

### 出力ファイル不在時の処理

```python
if not score_file.exists():
    print("❌ ui_quality_score.json が見つかりません")

    # フォールバック: デフォルトスコア生成
    default_score = {
        "total_score": 0,
        "passed": False,
        "threshold": 70,
        "mode": "ERROR",
        "message": "UI Verification Agent failed to generate output"
    }

    with open(score_file, 'w', encoding='utf-8') as f:
        json.dump(default_score, f, ensure_ascii=False, indent=2)

    return default_score
```

---

## 検証シナリオ設定

### ui_verification.json参照

検証シナリオは `@.claude/config/ui_verification.json` で定義：

```json
{
  "scenarios": [
    {
      "id": "login_flow",
      "name": "ログインフロー検証",
      "test_steps": [ /* ... */ ],
      "score_weight": 20
    },
    {
      "id": "form_validation",
      "name": "フォームバリデーション検証",
      "test_steps": [ /* ... */ ],
      "score_weight": 20
    },
    {
      "id": "responsive_design",
      "name": "レスポンシブデザイン検証",
      "test_steps": [ /* ... */ ],
      "score_weight": 20
    },
    {
      "id": "keyboard_navigation",
      "name": "キーボードナビゲーション検証",
      "test_steps": [ /* ... */ ],
      "score_weight": 20
    },
    {
      "id": "error_handling",
      "name": "エラーハンドリング検証",
      "test_steps": [ /* ... */ ],
      "score_weight": 20
    }
  ]
}
```

---

## 参照

- @.claude/agents/ui-verification-agent.md - UI Verification Agent仕様書（1092行）
- @.claude/config/ui_verification.json - 検証シナリオ設定（697行）
- @.claude/rules/review_loop.md - レビューループ制御
- @docs/implementation_guides/week1_ui_testing.md - Week 1実装ガイド
- @.claude/skills/orchestrate-review-loop/SKILL.md - ドキュメント品質レビュー版

---

## Week 1 実装完了状況（2026-01-09）

### 検証済み項目
- ✅ Chrome MCP接続確認機能
- ✅ 静的解析フォールバックモード
- ✅ Task tool経由でのエージェント起動
- ✅ 品質スコア取得（ui_quality_score.json）
- ✅ 改善推奨抽出（issues配列）
- ✅ スクリーンショット保存機能

### 実装済み機能
1. **入力バリデーション**: 必須パラメータ確認
2. **Chrome MCP接続確認**: 接続失敗時の静的解析フォールバック
3. **Task tool統合**: `Task(subagent_type="general-purpose", model="sonnet")`
4. **品質ゲート判定**: 70点基準、条件付き合格（60-69点）
5. **スクリーンショット証跡**: screenshots/ディレクトリへの自動保存
6. **サマリーレポート**: verification_summary.json生成

### 次のステップ（Week 2以降）
- Manager Skillへの統合
- 複数プロジェクトの並列検証
- カスタム検証シナリオの追加
