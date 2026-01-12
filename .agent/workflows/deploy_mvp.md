---
description: MVPをインターネットに公開する
---
# MVPデプロイワークフロー

構築したMVP（LP/Webアプリ）をインターネットに公開する。

## 前提条件
- `mvp/lp/` または `mvp/webapp/` に成果物が完成済み
- GitHubアカウントが利用可能
- デプロイ先のプラットフォームを選定済み

## ステップ

### 1. デプロイ先の選定

```markdown
## デプロイプラットフォーム比較

| プラットフォーム | 無料枠 | 難易度 | 適用ケース |
|----------------|-------|-------|-----------|
| **GitHub Pages** | ✅無制限 | 簡単 | 静的サイト（LP） |
| **Vercel** | ✅月100GB | 簡単 | Next.js / React |
| **Netlify** | ✅月100GB | 簡単 | 静的サイト + Forms |
| **Cloudflare Pages** | ✅無制限 | 簡単 | 静的サイト |

**推奨**: LP単体の場合は **GitHub Pages** または **Netlify**
```

### 2. GitHub Pages デプロイ（推奨）

#### 2.1 リポジトリ作成

// turbo
```bash
# プロジェクトディレクトリに移動
cd [mvpディレクトリ]

# Git初期化
git init
git add .
git commit -m "Initial MVP commit"
```

#### 2.2 GitHubリポジトリ作成

```markdown
## GitHub リポジトリ設定
- リポジトリ名: [founder-agent-mvp]
- 公開設定: Public（無料でPages利用のため）
- README: 不要
```

// turbo
```bash
# リモート追加とプッシュ
git remote add origin https://github.com/[username]/[repo-name].git
git branch -M main
git push -u origin main
```

#### 2.3 GitHub Pages有効化

```markdown
## GitHub Pages設定手順
1. リポジトリの Settings を開く
2. 左メニューから Pages を選択
3. Source: Deploy from a branch を選択
4. Branch: main、フォルダ: / (root) を選択
5. Save をクリック
```

#### 2.4 公開URL確認

```markdown
## 公開URL
https://[username].github.io/[repo-name]/
```

### 3. Vercel デプロイ（代替）

#### 3.1 Vercel CLIインストール

// turbo
```bash
npm i -g vercel
```

#### 3.2 デプロイ実行

// turbo
```bash
cd [mvpディレクトリ]
vercel
```

対話式プロンプトに回答：
- Set up and deploy: Y
- Scope: [アカウント選択]
- Link to existing project: N
- Project name: [プロジェクト名]
- Directory: ./

#### 3.3 本番デプロイ

// turbo
```bash
vercel --prod
```

### 4. 公開確認

```markdown
## 公開確認チェックリスト

### 基本確認
- [ ] URLにアクセスできる
- [ ] ページが正しく表示される
- [ ] 画像が表示される
- [ ] リンクが動作する

### フォーム確認
- [ ] フォーム送信が動作する
- [ ] 送信完了メッセージが表示される
- [ ] 送信データを受信できる（Formspree/メール等）

### モバイル確認
- [ ] スマートフォンで表示確認
- [ ] タップターゲットが適切なサイズ

### パフォーマンス確認
- [ ] ページ読み込みが3秒以内
```

### 5. 分析設定（オプション）

```markdown
## 分析ツール設定

### Google Analytics
1. GA4プロパティを作成
2. Measurement IDを取得
3. index.htmlに以下を追加:

<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXX');
</script>

### 代替: Plausible（プライバシー重視）
<script defer data-domain="[ドメイン]" src="https://plausible.io/js/script.js"></script>
```

### 6. DNSカスタムドメイン設定（オプション）

```markdown
## カスタムドメイン設定
独自ドメインを使用する場合:

1. ドメインレジストラでDNS設定
2. CNAME: www → [username].github.io
3. A: @ → GitHub Pages IP
4. リポジトリ Settings > Pages > Custom domain に設定
5. HTTPS強制を有効化
```

## 出力

### デプロイ完了レポート

```markdown
# MVPデプロイ完了レポート

**デプロイ日**: [日付]
**プラットフォーム**: [GitHub Pages / Vercel / Netlify]

## 公開URL
🌐 **[URL]**

## リポジトリ
📁 [GitHubリポジトリURL]

## 確認結果
| 項目 | 結果 |
|------|------|
| アクセス可能 | ✅ |
| 表示正常 | ✅ |
| フォーム動作 | ✅ |
| モバイル対応 | ✅ |

## 分析設定
- [ ] Google Analytics: [設定済み/未設定]
- [ ] Measurement ID: [G-XXXXXXX]

## 次のステップ
→ `/create_sns_content` でSNS投稿を作成
→ ユーザー獲得を開始
```

成果物を以下のパスに保存：
```
Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/4_executing/deploy_report.md
```

## 完了条件
- [ ] デプロイプラットフォームを選定した
- [ ] リポジトリを作成・プッシュした
- [ ] デプロイを実行した
- [ ] 公開URLでアクセス確認した
- [ ] `deploy_report.md` を保存した
