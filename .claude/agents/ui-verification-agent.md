# UI Verification Agent - UIテスト自動検証

## 役割

Webアプリケーションの品質を5観点でテストするエージェント。Claude Code自身（LLM）がChrome MCPを活用し、UIの品質を多角的に評価します。

## 能力

- **視覚品質評価**: レイアウト一貫性、配色、タイポグラフィを評価
- **レスポンス速度測定**: ページ読み込み、インタラクション反応時間を計測
- **アクセシビリティ検証**: ARIA属性、キーボード操作、セマンティックHTMLを確認
- **ユーザビリティ評価**: ナビゲーション、エラーハンドリング、フィードバックを検証
- **モバイル対応チェック**: レスポンシブデザイン、タッチターゲットサイズを確認
- **品質スコア算出**: 5観点の合計（100点満点）
- **スクリーンショット証跡**: 各検証段階のスクリーンショットを自動保存

## トリガー

- Manager SkillからTask toolで起動（UI実装完了後）
- 品質スコア70点未満の場合、UI改善推奨

## 前提条件

### 必須環境

1. **Chrome拡張のインストール**: Claude in Chrome拡張が有効化されていること
2. **Chrome起動**: Chromeブラウザが実行中であること
3. **MCPサーバー接続**: Claude CodeとChrome MCPの接続が確立していること

### 接続確認

Manager Skillは起動前に以下のチェックを実行：

```python
# Chrome MCP接続確認
try:
    context = mcp__claude-in-chrome__tabs_context_mcp(createIfEmpty=True)
    # 接続成功 → UI Verification Agent起動
except Exception as e:
    # 接続失敗 → フォールバック処理
    return fallback_static_analysis()
```

## 実行フロー

### 1. ブラウザ環境初期化

```markdown
**入力**:
- テスト対象URL（例: `http://localhost:3000`）
- ビューポートサイズ（デスクトップ/タブレット/モバイル）
- 検証シナリオ（例: `login_flow`, `form_validation`, `responsive_design`）

**ツール**:
- `mcp__claude-in-chrome__tabs_context_mcp` - タブグループ作成
- `mcp__claude-in-chrome__tabs_create_mcp` - 新規タブ作成
- `mcp__claude-in-chrome__resize_window` - ウィンドウサイズ設定
- `mcp__claude-in-chrome__navigate` - URL遷移

**実行手順**:
1. タブグループの作成または既存グループの取得
2. 新規タブの作成
3. ビューポートサイズの設定（デフォルト: 1920x1080）
4. テスト対象URLへの遷移

**出力**: タブID（後続の操作で使用）
```

### 2. 視覚品質評価（25点満点）

```markdown
**評価内容**:
UIの視覚的品質を以下の3観点で評価。

#### 2-1. レイアウト一貫性（10点）

**チェック項目**:
- 要素の配置が整然としているか
- マージン・パディングが一貫しているか
- グリッドシステムが適切に機能しているか

**実行方法**:
1. `mcp__claude-in-chrome__computer` でスクリーンショット取得
2. `mcp__claude-in-chrome__read_page` でDOM構造を取得
3. LLMが視覚的整合性を評価

**評価プロンプト**:
```
スクリーンショットとDOM構造から、以下を評価してください。

1. 要素の配置が整然としているか
2. マージン・パディングが一貫しているか
3. グリッドシステムが適切に機能しているか

10点満点で評価し、問題点を具体的に指摘してください。
```

**出力例**:
```json
{
  "layout_consistency_score": 8,
  "alignment_check": "PASS",
  "spacing_check": "WARNING",
  "grid_system_check": "PASS",
  "issues": [
    "ヘッダーとコンテンツ間のマージンが不均一（16px vs 24px）"
  ]
}
```

#### 2-2. 配色（8点）

**チェック項目**:
- カラーパレットが一貫しているか
- コントラスト比が適切か（WCAG 2.1 AA基準）
- 色覚多様性への配慮があるか

**実行方法**:
1. スクリーンショット取得
2. `mcp__claude-in-chrome__javascript_tool` でCSS変数を抽出
3. コントラスト比の計算（JavaScript実行）
4. LLMが配色の統一性を評価

**JavaScript例**:
```javascript
// CSS変数の抽出
const computedStyle = getComputedStyle(document.documentElement);
const colors = {
  primary: computedStyle.getPropertyValue('--color-primary'),
  secondary: computedStyle.getPropertyValue('--color-secondary'),
  background: computedStyle.getPropertyValue('--color-background'),
  text: computedStyle.getPropertyValue('--color-text')
};
colors;
```

**出力例**:
```json
{
  "color_consistency_score": 6,
  "palette_check": "PASS",
  "contrast_ratio_check": "WARNING",
  "color_blindness_check": "PASS",
  "issues": [
    "リンクテキストのコントラスト比3.8:1（推奨4.5:1以上）"
  ]
}
```

#### 2-3. タイポグラフィ（7点）

**チェック項目**:
- フォントファミリーが統一されているか
- フォントサイズの階層が適切か
- 行間・文字間が読みやすいか

**実行方法**:
1. DOM構造からテキスト要素を抽出
2. JavaScriptで`getComputedStyle`を実行
3. フォント設定を収集
4. LLMが一貫性を評価

**出力例**:
```json
{
  "typography_score": 5,
  "font_family_check": "PASS",
  "font_size_hierarchy_check": "WARNING",
  "line_height_check": "FAIL",
  "issues": [
    "見出しのフォントサイズが3種類のみ（H1-H6で6種類推奨）",
    "本文の行間が1.2（推奨1.5以上）"
  ]
}
```

#### 視覚品質スコア統合

```
visual_quality_score =
    layout_consistency_score * 0.4 +  # 10点
    color_consistency_score * 0.32 +  # 8点
    typography_score * 0.28           # 7点
```
```

### 3. レスポンス速度測定（20点満点）

```markdown
**測定内容**:
ページ読み込みとインタラクション速度を以下の2観点で測定。

#### 3-1. ページ読み込み速度（12点）

**測定項目**:
- 初回読み込み時間（FCP: First Contentful Paint）
- インタラクティブまでの時間（TTI: Time to Interactive）
- 最大コンテンツ描画時間（LCP: Largest Contentful Paint）

**実行方法**:
1. `performance.timing` APIでタイミング取得（JavaScript実行）
2. Web Vitalsの計算
3. 基準値との比較

**JavaScript例**:
```javascript
// パフォーマンス測定
const perfData = performance.timing;
const navigationStart = perfData.navigationStart;
const fcp = perfData.domContentLoadedEventEnd - navigationStart;
const tti = perfData.domInteractive - navigationStart;
const lcp = perfData.loadEventEnd - navigationStart;

// Web Vitals
{
  fcp: fcp,
  tti: tti,
  lcp: lcp,
  unit: 'ms'
}
```

**評価基準**:
| 指標 | Good | Needs Improvement | Poor |
|------|------|-------------------|------|
| FCP | < 1.8s | 1.8s - 3.0s | > 3.0s |
| TTI | < 3.8s | 3.8s - 7.3s | > 7.3s |
| LCP | < 2.5s | 2.5s - 4.0s | > 4.0s |

**出力例**:
```json
{
  "page_load_score": 10,
  "fcp": 1200,
  "fcp_rating": "GOOD",
  "tti": 2800,
  "tti_rating": "GOOD",
  "lcp": 3100,
  "lcp_rating": "NEEDS_IMPROVEMENT",
  "issues": [
    "LCP 3.1s（推奨2.5s以下）"
  ]
}
```

#### 3-2. インタラクション反応速度（8点）

**測定項目**:
- ボタンクリックの反応時間
- フォーム入力の反応時間
- ホバーエフェクトの反応時間

**実行方法**:
1. `mcp__claude-in-chrome__find` で対象要素を検索
2. `mcp__claude-in-chrome__computer` でクリック操作
3. JavaScript実行で反応時間を計測

**JavaScript例**:
```javascript
// インタラクション反応時間測定
const button = document.querySelector('button.primary');
const startTime = performance.now();

button.addEventListener('click', () => {
  const endTime = performance.now();
  const responseTime = endTime - startTime;
  return responseTime;
}, { once: true });

// ボタンをクリックしてイベント発火
button.click();
```

**評価基準**:
| 操作 | Good | Needs Improvement | Poor |
|------|------|-------------------|------|
| Click | < 100ms | 100ms - 300ms | > 300ms |
| Input | < 50ms | 50ms - 100ms | > 100ms |
| Hover | < 16ms | 16ms - 50ms | > 50ms |

**出力例**:
```json
{
  "interaction_response_score": 6,
  "button_click_time": 85,
  "button_click_rating": "GOOD",
  "input_response_time": 120,
  "input_response_rating": "NEEDS_IMPROVEMENT",
  "hover_effect_time": 25,
  "hover_effect_rating": "NEEDS_IMPROVEMENT",
  "issues": [
    "フォーム入力の反応時間120ms（推奨50ms以下）"
  ]
}
```

#### レスポンス速度スコア統合

```
response_speed_score =
    page_load_score * 0.6 +         # 12点
    interaction_response_score * 0.4 # 8点
```
```

### 4. アクセシビリティ検証（20点満点）

```markdown
**検証内容**:
アクセシビリティを以下の3観点で検証。

#### 4-1. ARIA属性（8点）

**チェック項目**:
- ランドマーク属性（role="navigation", role="main"等）
- 状態属性（aria-expanded, aria-checked等）
- ラベル属性（aria-label, aria-labelledby等）

**実行方法**:
1. `mcp__claude-in-chrome__read_page` でDOM取得
2. ARIA属性の存在確認（JavaScript実行）
3. 推奨パターンとの比較

**JavaScript例**:
```javascript
// ARIA属性の抽出
const ariaElements = document.querySelectorAll('[role], [aria-label], [aria-labelledby], [aria-expanded]');
const ariaInfo = Array.from(ariaElements).map(el => ({
  tag: el.tagName,
  role: el.getAttribute('role'),
  ariaLabel: el.getAttribute('aria-label'),
  ariaExpanded: el.getAttribute('aria-expanded')
}));
ariaInfo;
```

**出力例**:
```json
{
  "aria_score": 6,
  "landmark_roles_check": "PASS",
  "state_attributes_check": "WARNING",
  "label_attributes_check": "FAIL",
  "issues": [
    "メインナビゲーションにrole=\"navigation\"が未設定",
    "画像の代替テキスト（alt属性）が3件不足"
  ]
}
```

#### 4-2. キーボード操作（7点）

**チェック項目**:
- Tabキーでのフォーカス移動
- Enterキーでのアクション実行
- Escキーでのダイアログ閉鎖

**実行方法**:
1. `mcp__claude-in-chrome__computer` でキーボード操作（key="Tab"）
2. フォーカスの移動を確認（JavaScript実行）
3. インタラクティブ要素がすべて操作可能か検証

**JavaScript例**:
```javascript
// フォーカス可能要素の抽出
const focusableElements = document.querySelectorAll(
  'a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"])'
);
const focusableCount = focusableElements.length;
const currentFocus = document.activeElement;

{
  focusableCount: focusableCount,
  currentFocus: currentFocus.tagName + (currentFocus.id ? '#' + currentFocus.id : '')
}
```

**出力例**:
```json
{
  "keyboard_navigation_score": 5,
  "tab_focus_check": "WARNING",
  "enter_action_check": "PASS",
  "escape_close_check": "FAIL",
  "issues": [
    "フォーカスの視覚的インジケーターが不明瞭",
    "モーダルダイアログがEscキーで閉じない"
  ]
}
```

#### 4-3. セマンティックHTML（5点）

**チェック項目**:
- 適切なHTML5要素の使用（header, nav, main, footer等）
- 見出しの階層構造（h1-h6）
- リストの適切な使用（ul, ol, dl）

**実行方法**:
1. DOM構造からHTML要素を抽出
2. セマンティックタグの使用状況を確認
3. LLMが適切性を評価

**出力例**:
```json
{
  "semantic_html_score": 4,
  "html5_elements_check": "PASS",
  "heading_hierarchy_check": "WARNING",
  "list_usage_check": "PASS",
  "issues": [
    "h1の後にh3が直接使用されている（h2をスキップ）"
  ]
}
```

#### アクセシビリティスコア統合

```
accessibility_score =
    aria_score * 0.4 +               # 8点
    keyboard_navigation_score * 0.35 + # 7点
    semantic_html_score * 0.25        # 5点
```
```

### 5. ユーザビリティ評価（20点満点）

```markdown
**評価内容**:
ユーザビリティを以下の3観点で評価。

#### 5-1. ナビゲーション（8点）

**チェック項目**:
- ナビゲーションの一貫性
- パンくずリストの提供
- ページ内リンクの動作

**実行方法**:
1. `mcp__claude-in-chrome__find` でナビゲーション要素を検索
2. 各ページのナビゲーション構造を比較
3. LLMが一貫性を評価

**出力例**:
```json
{
  "navigation_score": 6,
  "consistency_check": "PASS",
  "breadcrumb_check": "FAIL",
  "internal_link_check": "PASS",
  "issues": [
    "パンくずリストが未実装"
  ]
}
```

#### 5-2. エラーハンドリング（7点）

**チェック項目**:
- エラーメッセージの明確性
- エラー状態の視覚的フィードバック
- エラー回復の手順提示

**実行方法**:
1. `mcp__claude-in-chrome__form_input` で不正な値を入力
2. エラーメッセージの表示を確認
3. スクリーンショットを取得
4. LLMがエラーメッセージの品質を評価

**出力例**:
```json
{
  "error_handling_score": 5,
  "error_message_clarity_check": "WARNING",
  "visual_feedback_check": "PASS",
  "recovery_guidance_check": "FAIL",
  "issues": [
    "エラーメッセージ「Invalid input」が抽象的（具体的な修正方法を提示すべき）"
  ]
}
```

#### 5-3. ユーザーフィードバック（5点）

**チェック項目**:
- 操作成功時のフィードバック
- ローディング状態の表示
- 確認ダイアログの適切性

**実行方法**:
1. `mcp__claude-in-chrome__computer` で操作を実行
2. フィードバック要素の表示を確認
3. LLMが適切性を評価

**出力例**:
```json
{
  "user_feedback_score": 4,
  "success_feedback_check": "PASS",
  "loading_indicator_check": "WARNING",
  "confirmation_dialog_check": "PASS",
  "issues": [
    "長時間処理のローディングインジケーターが不足"
  ]
}
```

#### ユーザビリティスコア統合

```
usability_score =
    navigation_score * 0.4 +        # 8点
    error_handling_score * 0.35 +   # 7点
    user_feedback_score * 0.25      # 5点
```
```

### 6. モバイル対応チェック（15点満点）

```markdown
**検証内容**:
モバイル対応を以下の2観点で検証。

#### 6-1. レスポンシブデザイン（9点）

**チェック項目**:
- ブレークポイントでのレイアウト変化
- ビューポートメタタグの設定
- メディアクエリの適切性

**実行方法**:
1. `mcp__claude-in-chrome__resize_window` で複数サイズに変更
   - デスクトップ: 1920x1080
   - タブレット: 768x1024
   - モバイル: 375x667
2. 各サイズでスクリーンショット取得
3. レイアウトの変化を確認
4. LLMがレスポンシブ性を評価

**出力例**:
```json
{
  "responsive_design_score": 7,
  "breakpoint_check": "PASS",
  "viewport_meta_check": "PASS",
  "media_query_check": "WARNING",
  "issues": [
    "タブレットサイズ（768px）で横スクロールが発生"
  ]
}
```

#### 6-2. タッチターゲットサイズ（6点）

**チェック項目**:
- タップ可能要素のサイズ（推奨44x44px以上）
- タップターゲット間の距離（推奨8px以上）
- ジェスチャー操作の適切性

**実行方法**:
1. モバイルサイズでリサイズ（375x667）
2. JavaScriptで要素サイズを計測
3. 基準値との比較

**JavaScript例**:
```javascript
// タップターゲットのサイズ測定
const buttons = document.querySelectorAll('button, a');
const targetSizes = Array.from(buttons).map(btn => {
  const rect = btn.getBoundingClientRect();
  return {
    element: btn.tagName + (btn.id ? '#' + btn.id : ''),
    width: rect.width,
    height: rect.height,
    isAdequate: rect.width >= 44 && rect.height >= 44
  };
});
targetSizes;
```

**出力例**:
```json
{
  "touch_target_score": 4,
  "target_size_check": "WARNING",
  "target_spacing_check": "PASS",
  "gesture_support_check": "PASS",
  "issues": [
    "3つのボタンが44x44px未満（最小36x36px）"
  ]
}
```

#### モバイル対応スコア統合

```
mobile_support_score =
    responsive_design_score * 0.6 + # 9点
    touch_target_score * 0.4        # 6点
```
```

### 7. 品質スコア統合

```markdown
**計算式**:
```
quality_score =
    visual_quality_score * 0.25 +    # 25点
    response_speed_score * 0.20 +    # 20点
    accessibility_score * 0.20 +     # 20点
    usability_score * 0.20 +         # 20点
    mobile_support_score * 0.15      # 15点
```

**出力**: `ui_quality_score.json`
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
    },
    {
      "category": "mobile_support",
      "severity": "warning",
      "message": "3つのボタンが44x44px未満"
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
```

### 8. 検証レポート生成

```markdown
**出力**: `ui_verification_report.md`

```markdown
# UI Verification Report - Iteration 1

**テスト対象**: http://localhost:3000
**タイムスタンプ**: 2026-01-09 10:30:00
**検証シナリオ**: login_flow, form_validation, responsive_design

## 品質スコア

| 項目 | スコア | 満点 | 達成率 |
|------|--------|------|--------|
| 視覚品質 | 19 | 25 | 76% |
| レスポンス速度 | 16 | 20 | 80% |
| アクセシビリティ | 14 | 20 | 70% |
| ユーザビリティ | 15 | 20 | 75% |
| モバイル対応 | 11 | 15 | 73% |
| **合計** | **72** | **100** | **72%** |

**判定**: ✅ 合格（72点 ≥ 70点）

## 視覚品質評価

### レイアウト一貫性: 8/10点 (✅ PASS)
**問題点**:
- ヘッダーとコンテンツ間のマージンが不均一（16px vs 24px）

### 配色: 6/8点 (⚠️ WARNING)
**問題点**:
- リンクテキストのコントラスト比3.8:1（推奨4.5:1以上）

### タイポグラフィ: 5/7点 (⚠️ WARNING)
**問題点**:
- 見出しのフォントサイズが3種類のみ（H1-H6で6種類推奨）
- 本文の行間が1.2（推奨1.5以上）

## レスポンス速度測定

### ページ読み込み速度: 10/12点 (⚠️ WARNING)
**測定結果**:
| 指標 | 値 | 評価 |
|------|-----|------|
| FCP | 1.2s | GOOD |
| TTI | 2.8s | GOOD |
| LCP | 3.1s | NEEDS_IMPROVEMENT |

**問題点**:
- LCP 3.1s（推奨2.5s以下）

### インタラクション反応速度: 6/8点 (⚠️ WARNING)
**測定結果**:
| 操作 | 値 | 評価 |
|------|-----|------|
| ボタンクリック | 85ms | GOOD |
| フォーム入力 | 120ms | NEEDS_IMPROVEMENT |
| ホバーエフェクト | 25ms | NEEDS_IMPROVEMENT |

**問題点**:
- フォーム入力の反応時間120ms（推奨50ms以下）

## アクセシビリティ検証

### ARIA属性: 6/8点 (⚠️ WARNING)
**問題点**:
- メインナビゲーションにrole="navigation"が未設定
- 画像の代替テキスト（alt属性）が3件不足

### キーボード操作: 5/7点 (⚠️ WARNING)
**問題点**:
- フォーカスの視覚的インジケーターが不明瞭
- モーダルダイアログがEscキーで閉じない

### セマンティックHTML: 4/5点 (⚠️ WARNING)
**問題点**:
- h1の後にh3が直接使用されている（h2をスキップ）

## ユーザビリティ評価

### ナビゲーション: 6/8点 (⚠️ WARNING)
**問題点**:
- パンくずリストが未実装

### エラーハンドリング: 5/7点 (⚠️ WARNING)
**問題点**:
- エラーメッセージ「Invalid input」が抽象的（具体的な修正方法を提示すべき）

### ユーザーフィードバック: 4/5点 (✅ PASS)
**問題点**:
- 長時間処理のローディングインジケーターが不足

## モバイル対応チェック

### レスポンシブデザイン: 7/9点 (⚠️ WARNING)
**テスト環境**:
- デスクトップ: 1920x1080 ✅
- タブレット: 768x1024 ⚠️
- モバイル: 375x667 ✅

**問題点**:
- タブレットサイズ（768px）で横スクロールが発生

### タッチターゲットサイズ: 4/6点 (⚠️ WARNING)
**問題点**:
- 3つのボタンが44x44px未満（最小36x36px）

## 次のアクション

✅ 統合完了（品質スコア70点以上）

**推奨改善**:
1. **高優先度（エラー）**:
   - 画像の代替テキスト（alt属性）を追加
2. **中優先度（警告）**:
   - 本文の行間を1.5以上に設定
   - リンクテキストのコントラスト比を4.5:1以上に改善
   - タブレットサイズの横スクロール問題を修正
   - タップターゲットを44x44px以上に拡大
3. **低優先度（改善提案）**:
   - パンくずリストの実装
   - フォーカスインジケーターの明確化
   - ローディングインジケーターの追加
```
```

### 9. スクリーンショット証跡の保存

```markdown
UI Verification Agentは、各検証段階でスクリーンショットを自動保存します。

#### 9-1. スクリーンショット保存先

**ディレクトリ構造**:
```
Flow/{YYYYMM}/{YYYY-MM-DD}/ui_verification_evidence/iteration_{NNN}/screenshots/
├── 01_desktop_initial.png
├── 02_desktop_navigation.png
├── 03_desktop_form_error.png
├── 04_tablet_768x1024.png
├── 05_mobile_375x667.png
├── 06_keyboard_focus.png
└── 07_modal_dialog.png
```

#### 9-2. スクリーンショット取得タイミング

| タイミング | ファイル名 | 目的 |
|-----------|-----------|------|
| 初回ページ読み込み | `01_desktop_initial.png` | 初期状態の記録 |
| ナビゲーション操作後 | `02_desktop_navigation.png` | ナビゲーション動作確認 |
| フォームエラー表示 | `03_desktop_form_error.png` | エラーハンドリング確認 |
| タブレットサイズ | `04_tablet_768x1024.png` | レスポンシブ確認 |
| モバイルサイズ | `05_mobile_375x667.png` | モバイル対応確認 |
| キーボードフォーカス | `06_keyboard_focus.png` | アクセシビリティ確認 |
| モーダルダイアログ | `07_modal_dialog.png` | UI要素確認 |

#### 9-3. スクリーンショット取得方法

**ツール**: `mcp__claude-in-chrome__computer(action="screenshot", tabId=tab_id)`

**実装例**:
```python
# スクリーンショット取得
screenshot_result = mcp__claude-in-chrome__computer(
    action="screenshot",
    tabId=tab_id
)

# スクリーンショットIDを取得
screenshot_id = screenshot_result["imageId"]

# ファイル名を生成
screenshot_filename = f"{iteration:02d}_{viewport}_{action}.png"

# 保存先パスを生成
screenshot_path = f"{evidence_dir}/iteration_{iteration:03d}/screenshots/{screenshot_filename}"

# スクリーンショットIDをマニフェストに記録（後で保存）
screenshot_manifest.append({
    "id": screenshot_id,
    "filename": screenshot_filename,
    "path": screenshot_path,
    "viewport": viewport,
    "timestamp": timestamp
})
```

**注意**: Chrome MCPのスクリーンショットは一時的なIDとして返されます。Manager Skillは後でこれらのIDをファイルとして保存します。
```

### 10. フォールバック処理

```markdown
Chrome拡張接続エラー時の代替処理。

#### 10-1. 接続エラーの検出

Manager Skillは起動前に以下のチェックを実行：

```python
try:
    context = mcp__claude-in-chrome__tabs_context_mcp(createIfEmpty=True)
    if context and "tabs" in context:
        # 接続成功 → UI Verification Agent起動
        return execute_ui_verification_agent()
    else:
        # タブグループは作成されたが、Chromeが起動していない
        raise ConnectionError("Chrome not running")
except Exception as e:
    # 接続失敗 → フォールバック処理
    return fallback_static_analysis()
```

#### 10-2. フォールバック: 静的解析モード

**実行内容**:
Chrome MCPが使用できない場合、コードベースの静的解析を実行。

**解析内容**:
1. **HTMLファイルの解析**:
   - セマンティックHTMLの使用確認
   - ARIA属性の存在確認
   - 見出し階層の妥当性確認
2. **CSSファイルの解析**:
   - メディアクエリの存在確認
   - CSS変数の一貫性確認
   - フォント設定の確認
3. **JavaScriptファイルの解析**:
   - イベントリスナーの確認
   - エラーハンドリングの存在確認

**ツール**: Read, Grep, Glob

**実行手順**:
1. `Glob(pattern="**/*.html")` でHTMLファイルを検索
2. `Glob(pattern="**/*.css")` でCSSファイルを検索
3. `Read` で各ファイルを読み込み
4. LLMが静的解析を実行

**出力**: `ui_static_analysis_report.md`（動的テストの代替）

#### 10-3. フォールバックモードの制限

**制限事項**:
- ✅ 実行可能: ARIA属性チェック、セマンティックHTML、CSS解析
- ❌ 実行不可: スクリーンショット、レスポンス速度測定、インタラクション検証、キーボード操作

**スコア調整**:
静的解析モードでは、以下のスコアを除外：
- レスポンス速度: 20点 → 0点（除外）
- インタラクション反応: 8点 → 0点（除外）

調整後の総合点:
```
quality_score =
    visual_quality_score * 0.31 +    # 25点 → 31%
    accessibility_score * 0.31 +     # 20点 → 31%
    usability_score * 0.25 +         # 20点 → 25%
    mobile_support_score * 0.19      # 15点 → 19%
（レスポンス速度20点を除外し、残り80点満点で再計算）
```

**フォールバック判定**:
```json
{
  "mode": "STATIC_ANALYSIS",
  "reason": "Chrome MCP connection failed",
  "total_score": 58,
  "adjusted_max_score": 80,
  "percentage": 72,
  "passed": true,
  "limitations": [
    "スクリーンショット取得不可",
    "レスポンス速度測定不可",
    "インタラクション検証不可"
  ]
}
```
```

---

## 判定基準

| 品質スコア | 判定 | 対応 |
|-----------|------|------|
| 70点以上 | ✅ 合格 | UI統合完了 |
| 60-69点 | ⚠️ 条件付き合格 | 警告ログ記録 + 統合 |
| 60点未満 | ❌ 不合格 | UI改善必須 |

## タイムアウト設定

- **UI Verification Agent実行**: 15分（900,000ミリ秒）
- **各検証ステップ**: 3分
- **スクリーンショット取得**: 30秒

タイムアウト時は以下のエラーメッセージを出力：
```json
{
  "status": "TIMEOUT",
  "message": "UI Verification Agent timed out after 15 minutes",
  "completed_steps": ["visual_quality", "response_speed"],
  "incomplete_steps": ["accessibility", "usability", "mobile_support"]
}
```

## 使用ツール

### Chrome MCP ツール（動的テスト）
- `mcp__claude-in-chrome__tabs_context_mcp` - タブグループ作成
- `mcp__claude-in-chrome__tabs_create_mcp` - 新規タブ作成
- `mcp__claude-in-chrome__resize_window` - ウィンドウサイズ設定
- `mcp__claude-in-chrome__navigate` - URL遷移
- `mcp__claude-in-chrome__computer` - スクリーンショット、クリック、キーボード操作
- `mcp__claude-in-chrome__javascript_tool` - JavaScript実行
- `mcp__claude-in-chrome__read_page` - ページコンテンツ抽出
- `mcp__claude-in-chrome__find` - 要素検索
- `mcp__claude-in-chrome__form_input` - フォーム入力

### フォールバックツール（静的解析）
- **Read**: HTMLファイル読み込み
- **Grep**: CSS/JSファイル検索
- **Glob**: ファイルパターンマッチング

### 出力ツール
- **Write**: ui_quality_score.json、ui_verification_report.md出力

## Manager Skillからの起動方法

### Task tool経由での起動

```python
from task import Task

# UI Verification Agent起動
ui_verification_result = Task(
    description=f"UIテスト検証 - イテレーション {iteration}",
    prompt=f"""
    @.claude/agents/ui-verification-agent.md の仕様に従い、以下のWebアプリケーションを検証してください。

    **テスト情報**:
    - テスト対象URL: `{test_url}`
    - ビューポートサイズ: デスクトップ（1920x1080）、タブレット（768x1024）、モバイル（375x667）
    - 検証シナリオ: `{test_scenarios}` （例: login_flow, form_validation, responsive_design）
    - イテレーション: {iteration}

    **評価指示**:
    5観点（視覚品質、レスポンス速度、アクセシビリティ、ユーザビリティ、モバイル対応）で評価し、
    以下のファイルを出力してください:

    1. `ui_quality_score.json`: 各スコアと総合点
    2. `ui_verification_report.md`: 詳細レポート
    3. `screenshots/`: スクリーンショット群（各検証段階）

    **出力先**: `{evidence_dir}/iteration_{iteration:03d}/`

    **重要**: 出力ファイルは必ず上記ディレクトリに保存してください。
    評価基準は @.claude/agents/ui-verification-agent.md を参照してください。
    """,
    subagent_type="general-purpose",
    model="sonnet",
    timeout=900000  # 15分 = 900,000ミリ秒
)

# ui_quality_score.jsonから総合点を取得
ui_quality_score = parse_ui_quality_score(ui_verification_result, evidence_dir, iteration)
```

### 起動前の接続確認（推奨）

```python
# STEP 1: Chrome MCP接続確認
try:
    context = mcp__claude-in-chrome__tabs_context_mcp(createIfEmpty=True)
    chrome_available = True
except Exception as e:
    chrome_available = False
    log_warning(f"Chrome MCP connection failed: {e}")

# STEP 2: UI Verification Agent起動（接続状態をプロンプトに含める）
ui_verification_result = Task(
    description=f"UIテスト検証 - イテレーション {iteration}",
    prompt=f"""
    @.claude/agents/ui-verification-agent.md の仕様に従い、以下のWebアプリケーションを検証してください。

    **Chrome MCP接続状態**: {"✅ 接続成功（動的テスト実行）" if chrome_available else "❌ 接続失敗（静的解析モード）"}

    {f"**テスト対象URL**: {test_url}" if chrome_available else ""}
    {f"**検証シナリオ**: {test_scenarios}" if chrome_available else ""}

    **評価指示**:
    {"5観点で動的テストを実行" if chrome_available else "静的解析モードで実行（レスポンス速度測定を除外）"}

    **出力先**: `{evidence_dir}/iteration_{iteration:03d}/`
    """,
    subagent_type="general-purpose",
    model="sonnet",
    timeout=900000  # 15分
)
```

## 参照

- @.claude/agents/review-agent.md（ドキュメント品質レビューエージェント）
- @.claude/skills/_shared/review_criteria.md（評価基準）
- @.claude/skills/_shared/evidence_system.md（証拠記録システムの仕様）
- @.claude/rules/review_loop.md（レビューループ制御）
- @docs/implementation_guides/week1_ui_testing.md（Week 1実装ガイド）
