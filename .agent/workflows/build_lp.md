---
description: ランディングページを構築する
---
# LP構築ワークフロー

PSF検証のためのランディングページ（LP）を自律的に構築する。

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `lean_canvas.md`, `persona.md`, `psf_diagnosis.md` |
| **出力** | `mvp/lp/` ディレクトリ（HTML/CSS/JS/画像） |
| **次のWF** | `/deploy_mvp` |

## 前提条件

- `lean_canvas.md` が作成済み（UVP定義済み）
- `persona.md` が作成済み
- `psf_diagnosis.md` でMVPタイプ選定済み

---

## STEP 1: 入力ファイル読み込み【自動実行】

### 使用ツール
`view_file`

### 実行手順
// turbo
```
1. view_file: lean_canvas.md から以下を抽出
   - UVP（独自の価値提案）
   - 課題リスト（上位3つ）
   - ソリューション
   - ターゲット顧客

2. view_file: persona.md から以下を抽出
   - ペルソナ名・属性
   - 課題・ゴール
   - 行動特性

3. view_file: psf_diagnosis.md から以下を確認
   - 選定されたMVPタイプ
   - 推奨事項
```

---

## STEP 2: LPコンテンツ設計【自動実行】

### サービス名決定

```markdown
## サービス名候補
1. [候補1]: [理由]
2. [候補2]: [理由]
3. [候補3]: [理由]

選定: [最終決定]
```

**選定基準**:
- 覚えやすい（5文字以内推奨）
- UVPが伝わる
- ドメイン取得可能性（.comまたは.io）

### セクション設計

```markdown
## LPセクション構成

### 1. ファーストビュー（Above the Fold）
- **キャッチコピー**: [UVPを1行で]
  例: 「[課題]を[解決方法]で解決」
- **サブコピー**: [2-3行の説明]
- **CTA**: 「今すぐ無料で始める」「事前登録する」
- **ビジュアル**: [ヒーローイメージの説明]

### 2. 課題提起セクション
見出し: 「こんな悩みはありませんか？」
- ❌ [課題1]
- ❌ [課題2]
- ❌ [課題3]

### 3. ソリューション紹介セクション
見出し: 「[サービス名]が解決します」
- ✅ [機能1]: [ベネフィット]
- ✅ [機能2]: [ベネフィット]
- ✅ [機能3]: [ベネフィット]

### 4. 使い方セクション
見出し: 「3ステップで簡単」
1. [ステップ1]
2. [ステップ2]
3. [ステップ3]

### 5. ベネフィットセクション
見出し: 「[サービス名]を使うと...」
- 🎯 [ベネフィット1]
- ⏱️ [ベネフィット2]
- 💰 [ベネフィット3]

### 6. FAQ（オプション）
- Q: [よくある質問1]
  A: [回答]
- Q: [よくある質問2]
  A: [回答]

### 7. CTAセクション
見出し: 「今すぐ始めよう」
- CTA: [ボタンテキスト]
- フォーム: メールアドレス入力

### 8. フッター
- プライバシーポリシー
- お問い合わせ
- コピーライト
```

---

## STEP 3: デザイン仕様決定【自動実行】

### カラーパレット自動生成

ペルソナとサービス特性から適切なカラーを選定：

```markdown
## カラーパレット

| 用途 | カラー | 理由 |
|------|--------|------|
| プライマリ | #[XXXXXX] | [信頼/活力/etc] |
| セカンダリ | #[XXXXXX] | [補完色] |
| アクセント | #[XXXXXX] | [CTA用] |
| 背景 | #[XXXXXX] | [明るさ] |
| テキスト | #[XXXXXX] | [読みやすさ] |
```

**パレット選定ルール**:
- BtoB → 青/緑系（信頼性）
- クリエイティブ系 → 紫/オレンジ系
- 健康/環境系 → 緑系
- 金融系 → 紺/ゴールド系

### タイポグラフィ

```css
/* Google Fonts 推奨 */
見出し: 'Noto Sans JP', sans-serif (700)
本文: 'Noto Sans JP', sans-serif (400)
```

---

## STEP 4: 画像生成【自動実行】

### 使用ツール
`generate_image`

### 実行手順
// turbo
1. ヒーローイメージ生成
```
プロンプト: "Modern, clean illustration of [サービスコンセプト], 
professional, minimal design, soft gradient background, 
no text, abstract representation of [具体的な要素],
digital art style, high quality, 16:9 aspect ratio"
```

2. 機能説明用アイコン/イラスト（必要に応じて）

### 画像保存先
```
mvp/lp/images/
├── hero.webp
├── feature-1.webp (オプション)
├── feature-2.webp (オプション)
└── feature-3.webp (オプション)
```

### エラー対応
| エラー | 対応 |
|-------|------|
| 生成失敗 | プロンプト簡略化して再試行 |
| 2回失敗 | プレースホルダー画像（グラデーション背景）を使用 |

---

## STEP 5: HTML実装【自動実行】

### 使用ツール
`write_to_file`

### ファイル構成
```
mvp/lp/
├── index.html
├── css/
│   └── style.css
├── js/
│   └── main.js
└── images/
    └── hero.webp
```

### index.html テンプレート

// turbo
```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[サービス名] - [キャッチコピー短縮版]</title>
    <meta name="description" content="[UVPを60文字以内で]">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- ファーストビュー -->
    <header class="hero">
        <div class="container">
            <h1>[キャッチコピー]</h1>
            <p class="subtitle">[サブコピー]</p>
            <a href="#signup" class="cta-button">[CTAテキスト]</a>
        </div>
        <img src="images/hero.webp" alt="[サービス名]" class="hero-image">
    </header>

    <!-- 課題セクション -->
    <section class="problems">
        <div class="container">
            <h2>こんな悩みはありませんか？</h2>
            <ul class="problem-list">
                <li>❌ [課題1]</li>
                <li>❌ [課題2]</li>
                <li>❌ [課題3]</li>
            </ul>
        </div>
    </section>

    <!-- ソリューションセクション -->
    <section class="solution">
        <div class="container">
            <h2>[サービス名]が解決します</h2>
            <div class="features">
                <div class="feature">
                    <h3>✅ [機能1]</h3>
                    <p>[説明]</p>
                </div>
                <div class="feature">
                    <h3>✅ [機能2]</h3>
                    <p>[説明]</p>
                </div>
                <div class="feature">
                    <h3>✅ [機能3]</h3>
                    <p>[説明]</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ベネフィットセクション -->
    <section class="benefits">
        <div class="container">
            <h2>[サービス名]を使うと...</h2>
            <div class="benefit-list">
                <div class="benefit">
                    <span class="icon">🎯</span>
                    <p>[ベネフィット1]</p>
                </div>
                <div class="benefit">
                    <span class="icon">⏱️</span>
                    <p>[ベネフィット2]</p>
                </div>
                <div class="benefit">
                    <span class="icon">💰</span>
                    <p>[ベネフィット3]</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTAセクション -->
    <section id="signup" class="cta-section">
        <div class="container">
            <h2>今すぐ始めよう</h2>
            <form action="https://formspree.io/f/[FORM_ID]" method="POST" class="signup-form">
                <input type="email" name="email" placeholder="メールアドレス" required>
                <button type="submit" class="cta-button">[CTAテキスト]</button>
            </form>
            <p class="form-note">※ 無料でご利用いただけます</p>
        </div>
    </section>

    <!-- フッター -->
    <footer>
        <div class="container">
            <p>&copy; 2025 [サービス名]. All rights reserved.</p>
            <nav>
                <a href="privacy.html">プライバシーポリシー</a>
            </nav>
        </div>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>
```

---

## STEP 6: CSS実装【自動実行】

// turbo
```css
/* style.css */
:root {
    --primary: #[カラー];
    --secondary: #[カラー];
    --accent: #[カラー];
    --background: #[カラー];
    --text: #[カラー];
    --text-light: #[カラー];
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Noto Sans JP', sans-serif;
    color: var(--text);
    background: var(--background);
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* ヒーローセクション */
.hero {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
    padding: 80px 20px;
    text-align: center;
    min-height: 80vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.hero h1 {
    font-size: clamp(2rem, 5vw, 3.5rem);
    margin-bottom: 20px;
    font-weight: 700;
}

.hero .subtitle {
    font-size: clamp(1rem, 2vw, 1.25rem);
    margin-bottom: 40px;
    opacity: 0.9;
}

.hero-image {
    max-width: 600px;
    width: 100%;
    margin-top: 40px;
    border-radius: 12px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.2);
}

/* CTAボタン */
.cta-button {
    display: inline-block;
    background: var(--accent);
    color: white;
    padding: 16px 40px;
    font-size: 1.1rem;
    font-weight: 700;
    text-decoration: none;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
}

.cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

/* セクション共通 */
section {
    padding: 80px 20px;
}

section h2 {
    font-size: clamp(1.5rem, 4vw, 2.5rem);
    text-align: center;
    margin-bottom: 50px;
}

/* 課題セクション */
.problems {
    background: #f8f9fa;
}

.problem-list {
    list-style: none;
    max-width: 600px;
    margin: 0 auto;
}

.problem-list li {
    font-size: 1.1rem;
    padding: 15px 0;
    border-bottom: 1px solid #eee;
}

/* 機能セクション */
.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 40px;
}

.feature {
    text-align: center;
    padding: 30px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.05);
}

.feature h3 {
    font-size: 1.25rem;
    margin-bottom: 15px;
}

/* ベネフィットセクション */
.benefits {
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
}

.benefit-list {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
}

.benefit {
    text-align: center;
}

.benefit .icon {
    font-size: 3rem;
    display: block;
    margin-bottom: 15px;
}

/* CTAセクション */
.cta-section {
    text-align: center;
    background: #f8f9fa;
}

.signup-form {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 15px;
    max-width: 500px;
    margin: 0 auto;
}

.signup-form input[type="email"] {
    flex: 1;
    min-width: 250px;
    padding: 16px 20px;
    font-size: 1rem;
    border: 2px solid #ddd;
    border-radius: 50px;
}

.form-note {
    margin-top: 15px;
    color: var(--text-light);
    font-size: 0.9rem;
}

/* フッター */
footer {
    background: var(--text);
    color: white;
    padding: 30px 20px;
    text-align: center;
}

footer a {
    color: white;
    margin-left: 20px;
}

/* レスポンシブ */
@media (max-width: 768px) {
    .hero {
        padding: 60px 20px;
        min-height: auto;
    }
    
    section {
        padding: 60px 20px;
    }
}
```

---

## STEP 7: JavaScript実装【自動実行】

// turbo
```javascript
// main.js

// スムーズスクロール
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// フォーム送信処理
const form = document.querySelector('.signup-form');
if (form) {
    form.addEventListener('submit', function(e) {
        const button = form.querySelector('button');
        button.textContent = '送信中...';
        button.disabled = true;
    });
}

// 簡易アナリティクス（ページビュー記録）
console.log('Page loaded:', new Date().toISOString());
```

---

## STEP 8: ローカルプレビュー【自動実行】

### 使用ツール
`run_command`

// turbo
```bash
cd [プロジェクトパス]/mvp/lp && python3 -m http.server 8080
```

### ブラウザ確認
`browser_subagent` で以下を確認：
- ページが正常に表示される
- 画像が表示される
- レスポンシブ（画面幅変更）
- フォームが表示される

---

## STEP 9: 最終チェック【自動実行】

```markdown
## LPチェックリスト

### コンテンツ
- [ ] キャッチコピーがUVPを伝えている
- [ ] 課題→解決のストーリーが明確
- [ ] CTAが目立つ位置にある（最低2箇所）
- [ ] 誤字脱字がない

### デザイン
- [ ] カラーコントラストが適切
- [ ] モバイルで読みやすい
- [ ] 画像が表示される

### 技術
- [ ] HTMLバリデーションエラーなし
- [ ] CSSエラーなし
- [ ] フォームが動作する
```

---

## 出力

成果物パス：
```
Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/mvp/lp/
├── index.html
├── css/style.css
├── js/main.js
└── images/hero.webp
```

### 完了レポート

```markdown
# LP構築完了レポート

**作成日**: [日付]
**ステータス**: デプロイ準備完了

## サービス概要
- **名前**: [サービス名]
- **キャッチコピー**: [コピー]
- **CTA**: [ボタンテキスト]

## ファイル一覧
- index.html
- css/style.css
- js/main.js
- images/hero.webp

## チェックリスト結果
- コンテンツ: ✅
- デザイン: ✅
- 技術: ✅

## 次のステップ
→ `/deploy_mvp` でインターネットに公開
```

---

## 完了条件

- [ ] 入力ファイルを読み込んだ
- [ ] LPコンテンツを設計した
- [ ] デザイン仕様を決定した
- [ ] 画像を生成した
- [ ] HTML/CSS/JSを実装した
- [ ] ローカルで動作確認した
- [ ] mvp/lp/ ディレクトリに保存した

---

## エラーハンドリング

| ステップ | エラー | 対応 |
|---------|-------|------|
| STEP 4 | 画像生成失敗 | グラデーション背景で代替 |
| STEP 5 | HTML構文エラー | 自動修正を試行 |
| STEP 8 | サーバー起動失敗 | ポート変更（8081, 8082） |
