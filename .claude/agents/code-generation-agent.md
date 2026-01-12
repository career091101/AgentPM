# Code Generation Agent

**役割**: Executingフェーズにおけるコード生成・テスト作成・リポジトリ初期化を自動化

**優先度**: P1（Week 3-4実装）

**年間削減時間**: 20時間（プロジェクト初期セットアップ、ボイラープレート作成の自動化）

---

## 1. エージェント概要

### 1.1 目的

Executingフェーズにおける以下の作業を自動化し、開発開始までのリードタイムを短縮：

1. **テンプレートベースのコード生成**: React/Next.js/FastAPI/Django等のプロジェクト構造を自動生成
2. **テスト自動生成**: Jest/pytest/RSpec等のテストスケルトンを自動作成
3. **リポジトリ初期化**: .gitignore、README.md、package.json/requirements.txt等の設定ファイルを自動生成
4. **CI/CDパイプライン設定**: GitHub Actions/CircleCI/GitLab CI等の設定ファイルを自動生成
5. **デプロイスクリプト生成**: Vercel/Heroku/AWS等のデプロイ設定を自動生成

### 1.2 年間削減時間の根拠

| 作業内容 | 従来の所要時間 | 自動化後 | 削減時間 |
|---------|--------------|---------|---------|
| プロジェクト初期化 | 2-3時間/プロジェクト | 10分 | 2.5時間 |
| テストスケルトン作成 | 1-2時間/プロジェクト | 5分 | 1.5時間 |
| CI/CD設定 | 2-4時間/プロジェクト | 15分 | 3時間 |
| デプロイ設定 | 1-2時間/プロジェクト | 10分 | 1.5時間 |

**年間想定プロジェクト数**: 2-3プロジェクト
**年間削減時間**: (2.5 + 1.5 + 3 + 1.5) × 2.5 = **21.25時間**

### 1.3 Research統合

#### ForGenAI Research統合

**参照**: `GenAI_research/tech_stack/`

- **AI技術スタック選定基準**: OpenAI vs Anthropic vs Google Gemini vs Cohere
- **プロンプトエンジニアリングパターン**: Chain-of-Thought、Few-shot、ReAct等のテンプレート
- **モデル選定フロー**: タスク別の最適モデル選定（GPT-4 Turbo vs Claude 3.5 Sonnet vs Gemini 1.5 Pro）
- **コスト最適化**: 入力トークン削減、キャッシング戦略、バッチ処理

**統合方法**:
- コード生成時にAI技術スタック選定基準を自動適用
- プロンプトテンプレートを`src/prompts/`ディレクトリに自動生成
- `.env.example`にAPI Key設定例を記載

#### ForSolo Research統合

**参照**: `Solopreneur_Research/documents/01_App/case_studies/`

- **Boilerplate/Templateビジネスモデル**: ShipFast、Superstarter、Nextless.js等の成功パターン
- **Micro-SaaS技術スタック**: Next.js + Supabase + Stripe + Resendの組み合わせ
- **1人開発効率化**: GitHub Copilot、Cursor、v0.devの活用パターン

**統合方法**:
- ShipFastライクなボイラープレートテンプレート提供
- Supabase認証、Stripe決済、Resendメール送信のコードスニペット自動生成
- Solo運用に最適化された軽量CI/CD設定（GitHub Actions + Vercel自動デプロイ）

---

## 2. 能力と実行フロー

### 2.1 主要能力

#### 能力1: テンプレートベースのコード生成

**対応フレームワーク**:

| カテゴリ | フレームワーク | 生成内容 |
|---------|-------------|---------|
| **フロントエンド** | React, Next.js, Vue.js, Svelte | コンポーネント構造、ルーティング、状態管理 |
| **バックエンド** | FastAPI, Django, Express.js, NestJS | API構造、ORM設定、認証ミドルウェア |
| **フルスタック** | Next.js (App Router), SvelteKit, Remix | SSR/SSG設定、API Routes、DB統合 |
| **AI特化** | LangChain, LlamaIndex, Haystack | プロンプトテンプレート、ベクトルDB統合 |

**生成されるファイル構造例（Next.js App Router）**:
```
project-root/
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── api/
│   │   │   └── hello/route.ts
│   │   └── (auth)/
│   │       ├── login/page.tsx
│   │       └── register/page.tsx
│   ├── components/
│   │   ├── ui/
│   │   │   ├── Button.tsx
│   │   │   └── Card.tsx
│   │   └── layout/
│   │       ├── Header.tsx
│   │       └── Footer.tsx
│   ├── lib/
│   │   ├── db.ts
│   │   ├── auth.ts
│   │   └── utils.ts
│   └── types/
│       └── index.ts
├── public/
│   └── images/
├── tests/
│   ├── unit/
│   └── integration/
├── .env.example
├── .gitignore
├── next.config.js
├── package.json
├── tsconfig.json
└── README.md
```

#### 能力2: テスト自動生成

**対応テストフレームワーク**:

| 言語/フレームワーク | テストツール | 生成内容 |
|------------------|------------|---------|
| JavaScript/TypeScript | Jest, Vitest | ユニットテスト、スナップショットテスト |
| React | React Testing Library | コンポーネントテスト |
| Python | pytest | ユニットテスト、フィクスチャ |
| Ruby | RSpec | ユニットテスト、リクエストスペック |

**生成されるテストファイル例（React Component）**:
```typescript
// tests/unit/components/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react'
import { Button } from '@/components/ui/Button'

describe('Button Component', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>)
    expect(screen.getByText('Click me')).toBeInTheDocument()
  })

  it('calls onClick handler when clicked', () => {
    const handleClick = jest.fn()
    render(<Button onClick={handleClick}>Click me</Button>)
    fireEvent.click(screen.getByText('Click me'))
    expect(handleClick).toHaveBeenCalledTimes(1)
  })

  it('applies variant styles correctly', () => {
    const { container } = render(<Button variant="primary">Primary</Button>)
    expect(container.firstChild).toHaveClass('btn-primary')
  })
})
```

#### 能力3: リポジトリ初期化

**自動生成される設定ファイル**:

1. **.gitignore** (言語/フレームワーク別テンプレート)
```gitignore
# Node.js
node_modules/
.env
.env.local
dist/
build/

# Next.js
.next/
out/

# Python
__pycache__/
*.pyc
.venv/
venv/

# IDEs
.vscode/
.idea/
```

2. **README.md** (プロジェクト情報、セットアップ手順)
```markdown
# Project Name

## Overview
[プロジェクトの概要を自動記載]

## Tech Stack
- Frontend: Next.js 14 (App Router)
- Backend: FastAPI
- Database: PostgreSQL
- Auth: Supabase Auth
- Styling: Tailwind CSS

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.11+
- PostgreSQL 15+

### Installation
\`\`\`bash
# フロントエンド
cd frontend
npm install
npm run dev

# バックエンド
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`

## Environment Variables
See `.env.example` for required environment variables.

## Testing
\`\`\`bash
npm test        # フロントエンド
pytest          # バックエンド
\`\`\`

## Deployment
[デプロイ手順を自動記載]
```

3. **package.json / requirements.txt** (依存関係管理)

#### 能力4: CI/CDパイプライン設定

**対応CI/CDプラットフォーム**:

| プラットフォーム | 設定ファイル | 生成内容 |
|----------------|------------|---------|
| GitHub Actions | `.github/workflows/ci.yml` | テスト、ビルド、デプロイ |
| CircleCI | `.circleci/config.yml` | テスト、ビルド、デプロイ |
| GitLab CI | `.gitlab-ci.yml` | テスト、ビルド、デプロイ |

**生成されるGitHub Actions設定例**:
```yaml
# .github/workflows/ci.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'
      - run: npm ci
      - run: npm test
      - run: npm run build

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
```

#### 能力5: デプロイスクリプト生成

**対応デプロイ先**:

| プラットフォーム | 設定ファイル | 自動化内容 |
|----------------|------------|----------|
| Vercel | `vercel.json` | ビルド設定、環境変数、リダイレクト |
| Heroku | `Procfile`, `app.json` | Dyno設定、アドオン設定 |
| AWS (CDK) | `cdk/lib/stack.ts` | インフラコード、デプロイスクリプト |
| Docker | `Dockerfile`, `docker-compose.yml` | コンテナ設定、マルチステージビルド |

**生成されるVercel設定例**:
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "devCommand": "npm run dev",
  "installCommand": "npm install",
  "framework": "nextjs",
  "env": {
    "DATABASE_URL": "@database-url",
    "OPENAI_API_KEY": "@openai-api-key"
  },
  "redirects": [
    {
      "source": "/old-path",
      "destination": "/new-path",
      "permanent": true
    }
  ]
}
```

### 2.2 実行フロー

```
STEP 1: プロジェクト情報収集
├─ プロジェクトタイプ選択（Frontend/Backend/Fullstack/AI）
├─ フレームワーク選択（Next.js/FastAPI/Django等）
├─ 機能要件確認（認証/決済/メール送信等）
└─ デプロイ先選択（Vercel/Heroku/AWS等）

STEP 2: テンプレート選定
├─ Research統合（ForGenAI: AI技術スタック、ForSolo: Boilerplate）
├─ テンプレートライブラリから最適パターン選択
├─ カスタマイズポイント特定（ドメイン固有ロジック）
└─ 依存関係リスト生成

STEP 3: ディレクトリ構造生成
├─ プロジェクトルート作成（/Users/yuichi/AIPM/aipm_v0/Stock/programs/.../dev/）
├─ サブディレクトリ生成（src/, tests/, public/）
├─ 設定ファイル配置（.gitignore, README.md, package.json等）
└─ 空ファイル生成（後のSTEPで内容を埋める）

STEP 4: コード生成
├─ コンポーネント/モジュールファイル生成
├─ API Routes生成
├─ ユーティリティ関数生成
└─ 型定義ファイル生成（TypeScript）

STEP 5: テスト生成
├─ ユニットテストスケルトン生成
├─ 統合テストスケルトン生成
├─ E2Eテスト設定生成（Playwright/Cypress）
└─ モックデータ生成

STEP 6: CI/CD設定
├─ GitHub Actions / CircleCI / GitLab CI設定生成
├─ テストジョブ定義
├─ ビルドジョブ定義
└─ デプロイジョブ定義

STEP 7: デプロイ設定
├─ Vercel / Heroku / AWS設定生成
├─ 環境変数テンプレート生成（.env.example）
├─ デプロイスクリプト生成
└─ インフラコード生成（必要に応じて）

STEP 8: Git初期化
├─ `git init`実行
├─ 初回コミット作成
├─ ブランチ戦略設定（main, develop）
└─ リモートリポジトリ設定（GitHub/GitLab）

STEP 9: 依存関係インストール
├─ `npm install` / `pip install -r requirements.txt`実行
├─ インストールエラーチェック
└─ lockファイル生成（package-lock.json / poetry.lock）

STEP 10: 検証・レポート生成
├─ 生成されたファイルリストの確認
├─ ビルド成功確認（`npm run build` / `python -m build`）
├─ テスト実行確認（`npm test` / `pytest`）
└─ 生成レポート出力（generated_code_report.md）
```

---

## 3. 入力パラメータ

### 3.1 必須パラメータ

#### 1. プロジェクトタイプ

**質問**: 「プロジェクトタイプを選択してください」

**選択肢**:
- `frontend`: フロントエンドのみ（React/Next.js/Vue.js等）
- `backend`: バックエンドのみ（FastAPI/Django/Express.js等）
- `fullstack`: フロントエンド+バックエンド統合
- `ai`: AI特化型（LangChain/LlamaIndex統合）

**デフォルト**: なし（必須）

#### 2. フレームワーク

**質問**: 「使用するフレームワークを選択してください」

**フロントエンド選択肢**:
- `nextjs`: Next.js 14 (App Router)
- `react`: React 18 (Vite)
- `vue`: Vue.js 3
- `svelte`: SvelteKit

**バックエンド選択肢**:
- `fastapi`: FastAPI (Python)
- `django`: Django (Python)
- `express`: Express.js (Node.js)
- `nestjs`: NestJS (Node.js)

**AI特化選択肢**:
- `langchain`: LangChain (Python)
- `llamaindex`: LlamaIndex (Python)

**デフォルト**: なし（必須）

#### 3. プロジェクト名

**質問**: 「プロジェクト名を入力してください（kebab-case推奨）」

**例**: `my-fitness-app`, `ai-chatbot-backend`

**デフォルト**: なし（必須）

### 3.2 オプションパラメータ

#### 4. 機能要件

**質問**: 「追加する機能を選択してください（複数選択可）」

**選択肢**:
- `auth`: 認証機能（Supabase Auth / NextAuth.js）
- `payment`: 決済機能（Stripe統合）
- `email`: メール送信（Resend / SendGrid）
- `database`: データベース（PostgreSQL / MongoDB）
- `storage`: ファイルストレージ（Supabase Storage / AWS S3）
- `ai`: AI機能（OpenAI / Anthropic統合）

**デフォルト**: なし（スキップ可）

#### 5. デプロイ先

**質問**: 「デプロイ先を選択してください」

**選択肢**:
- `vercel`: Vercel（推奨: Next.js）
- `heroku`: Heroku（推奨: Django/FastAPI）
- `aws`: AWS（CDKでインフラコード生成）
- `docker`: Docker（Dockerfileとdocker-compose.yml生成）

**デフォルト**: `vercel`

#### 6. CI/CDプラットフォーム

**質問**: 「CI/CDプラットフォームを選択してください」

**選択肢**:
- `github-actions`: GitHub Actions
- `circleci`: CircleCI
- `gitlab-ci`: GitLab CI

**デフォルト**: `github-actions`

#### 7. スタイリング

**質問**: 「スタイリング方法を選択してください」

**選択肢**:
- `tailwind`: Tailwind CSS
- `css-modules`: CSS Modules
- `styled-components`: styled-components
- `emotion`: Emotion

**デフォルト**: `tailwind`（フロントエンドの場合）

#### 8. 言語

**質問**: 「使用言語を選択してください」

**選択肢**:
- `typescript`: TypeScript
- `javascript`: JavaScript

**デフォルト**: `typescript`（フロントエンドの場合）

---

## 4. 出力ファイル

### 4.1 出力先

```
Stock/programs/[program_name]/projects/[project_name]/dev/
├── generated_code/          # 生成されたコード
│   ├── src/
│   ├── tests/
│   ├── public/
│   ├── .github/workflows/
│   ├── .gitignore
│   ├── README.md
│   ├── package.json / requirements.txt
│   └── ...
└── generated_code_report.md # 生成レポート
```

### 4.2 生成レポート形式

```markdown
# Code Generation Report

**生成日時**: 2026-01-03 15:30:45
**プロジェクト名**: my-fitness-app
**プロジェクトタイプ**: fullstack
**フレームワーク**: Next.js 14 (App Router) + FastAPI

---

## 生成されたファイル一覧

### フロントエンド (Next.js)

**ディレクトリ構造**:
```
frontend/
├── src/
│   ├── app/              # 15 files
│   ├── components/       # 8 files
│   ├── lib/              # 5 files
│   └── types/            # 3 files
├── tests/                # 12 files
├── public/               # 2 files
└── 設定ファイル          # 8 files
```

**主要ファイル**:
- `src/app/layout.tsx` (120 lines) - ルートレイアウト、メタデータ設定
- `src/app/page.tsx` (80 lines) - ホームページ
- `src/components/ui/Button.tsx` (60 lines) - Buttonコンポーネント
- `tests/unit/components/Button.test.tsx` (45 lines) - Buttonテスト

### バックエンド (FastAPI)

**ディレクトリ構造**:
```
backend/
├── app/
│   ├── api/              # 10 files
│   ├── models/           # 5 files
│   ├── services/         # 8 files
│   └── utils/            # 4 files
├── tests/                # 15 files
└── 設定ファイル          # 6 files
```

**主要ファイル**:
- `app/main.py` (100 lines) - FastAPIアプリケーションエントリポイント
- `app/api/users.py` (150 lines) - ユーザーAPI
- `app/models/user.py` (80 lines) - ユーザーモデル
- `tests/test_users.py` (120 lines) - ユーザーAPIテスト

### CI/CD設定

- `.github/workflows/ci.yml` (80 lines) - GitHub Actions設定

### デプロイ設定

- `vercel.json` (30 lines) - Vercel設定

---

## 機能統合状況

| 機能 | 統合状況 | 備考 |
|------|---------|------|
| 認証 | ✅ 統合済み | Supabase Auth |
| 決済 | ✅ 統合済み | Stripe |
| メール送信 | ✅ 統合済み | Resend |
| データベース | ✅ 統合済み | PostgreSQL (Supabase) |

---

## 次のアクション

### 1. 環境変数設定

`.env.example`をコピーして`.env`を作成し、以下の環境変数を設定してください：

```bash
# フロントエンド (.env.local)
NEXT_PUBLIC_SUPABASE_URL=your-supabase-url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
STRIPE_SECRET_KEY=your-stripe-secret-key

# バックエンド (.env)
DATABASE_URL=postgresql://user:password@localhost:5432/mydb
OPENAI_API_KEY=your-openai-api-key
RESEND_API_KEY=your-resend-api-key
```

### 2. 依存関係インストール

```bash
# フロントエンド
cd frontend
npm install

# バックエンド
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. 開発サーバー起動

```bash
# フロントエンド
npm run dev  # http://localhost:3000

# バックエンド
uvicorn main:app --reload  # http://localhost:8000
```

### 4. テスト実行

```bash
# フロントエンド
npm test

# バックエンド
pytest
```

### 5. デプロイ

```bash
# Vercelへのデプロイ
vercel --prod
```

---

## 生成統計

- **総ファイル数**: 120
- **総行数**: 8,540
- **生成時間**: 3分12秒
- **使用モデル**: sonnet
```

---

## 5. Task tool統合

### 5.1 Manager Skillからの呼び出しパターン

```python
result = Task(
    description="コード生成 - Next.js + FastAPI プロジェクト初期化",
    prompt="""
    @.claude/agents/code-generation-agent.md の仕様に従い、以下のプロジェクトを生成してください。

    **プロジェクト情報**:
    - プロジェクトタイプ: fullstack
    - フレームワーク: Next.js 14 (App Router) + FastAPI
    - プロジェクト名: my-fitness-app
    - 機能要件: auth, payment, email, database
    - デプロイ先: vercel
    - CI/CD: github-actions
    - スタイリング: tailwind
    - 言語: typescript

    **Research統合**:
    - ForGenAI: AI技術スタック選定（OpenAI vs Anthropic）
    - ForSolo: ShipFastボイラープレート参考

    以下を生成してください:
    1. ディレクトリ構造（frontend/ + backend/）
    2. コンポーネント・APIファイル
    3. テストスケルトン
    4. CI/CD設定（GitHub Actions）
    5. デプロイ設定（Vercel）
    6. generated_code_report.md
    """,
    subagent_type="general-purpose",
    model="sonnet",  # バランス重視（opus: 高品質が必要な場合）
    timeout=1200000  # 20分
)
```

### 5.2 モデル選択ガイド

| モデル | 用途 | 生成品質 | 速度 | コスト |
|--------|------|---------|------|--------|
| **haiku** | 単純なボイラープレート生成 | 標準 | 最速 | 低 |
| **sonnet** | 標準的なプロジェクト生成（推奨デフォルト） | 高 | 中速 | 中 |
| **opus** | 複雑なアーキテクチャ、カスタムロジック | 最高 | 低速 | 高 |

**推奨**:
- 初回プロジェクト生成: **sonnet**（バランス重視）
- AI特化型プロジェクト: **opus**（プロンプトエンジニアリング品質重視）
- 既存テンプレートの複製: **haiku**（高速生成）

---

## 6. Research統合

### 6.1 ForGenAI Research統合

**参照**: `@GenAI_research/tech_stack/ai_framework_comparison.md`

#### AI技術スタック選定基準

| プロバイダ | 推奨モデル | ユースケース | コスト（$/1M tokens） |
|-----------|-----------|-------------|---------------------|
| **OpenAI** | GPT-4 Turbo | 汎用タスク、高品質出力 | Input: $10, Output: $30 |
| **Anthropic** | Claude 3.5 Sonnet | 長文処理、コード生成 | Input: $3, Output: $15 |
| **Google** | Gemini 1.5 Pro | マルチモーダル、動画解析 | Input: $1.25, Output: $5 |
| **Cohere** | Command R+ | エンタープライズRAG | Input: $3, Output: $15 |

**統合方法**:
- プロジェクトタイプ`ai`の場合、上記比較表を`README.md`に自動記載
- `.env.example`に複数プロバイダのAPI Key設定例を記載
- `src/lib/ai-client.ts`にプロバイダ切り替えロジックを自動生成

#### プロンプトエンジニアリングパターン

**参照**: `@GenAI_research/prompt_patterns/`

**自動生成されるテンプレート**:
```typescript
// src/prompts/templates.ts

export const PROMPT_TEMPLATES = {
  chainOfThought: `あなたは{role}です。以下のタスクを段階的に考えて実行してください。

タスク: {task}

ステップ1: ...
ステップ2: ...
最終回答: ...`,

  fewShot: `以下の例を参考に、同様のタスクを実行してください。

例1: {example1}
例2: {example2}

タスク: {task}`,

  reAct: `Thought: 現在の状況を分析
Action: 次に取るべき行動
Observation: 行動の結果観察
... (繰り返し)
Answer: 最終的な回答`
}
```

### 6.2 ForSolo Research統合

**参照**: `@Solopreneur_Research/documents/01_App/case_studies/marc_lou_shipfast.md`

#### ShipFastボイラープレート統合

**統合内容**:
- Next.js 14 (App Router) + Supabase + Stripe + Resendの組み合わせ
- Marc LouのShipFast成功パターン（初月100 MRR達成）を参考
- 1人開発に最適化された軽量設定

**自動生成されるコード例**:
```typescript
// src/lib/stripe.ts
import Stripe from 'stripe'

export const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!, {
  apiVersion: '2023-10-16',
})

export const createCheckoutSession = async (priceId: string, userId: string) => {
  const session = await stripe.checkout.sessions.create({
    mode: 'subscription',
    payment_method_types: ['card'],
    line_items: [{ price: priceId, quantity: 1 }],
    success_url: `${process.env.NEXT_PUBLIC_URL}/dashboard?session_id={CHECKOUT_SESSION_ID}`,
    cancel_url: `${process.env.NEXT_PUBLIC_URL}/pricing`,
    client_reference_id: userId,
  })
  return session
}
```

#### Solo運用最適化CI/CD

**GitHub Actions設定（軽量版）**:
```yaml
name: Deploy to Vercel

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
```

**特徴**:
- テストステップを省略（Solo開発ではローカルテストで十分）
- ビルドステップを省略（Vercelが自動ビルド）
- デプロイのみに特化（3分以内でデプロイ完了）

---

## 7. エラーハンドリング

### Pattern 1: フレームワーク未対応

**エラー**: 選択されたフレームワークのテンプレートが存在しない

**対処**:
1. サポート対象フレームワークリストを表示
2. 最も近いフレームワークを提案（例: Remix → Next.js）
3. 汎用テンプレートで代替生成を提案

### Pattern 2: 依存関係の競合

**エラー**: `npm install`または`pip install`でエラー発生

**対処**:
1. エラーログを解析（バージョン競合、パッケージ未発見等）
2. 依存関係バージョンを調整（`package.json`の`^`を`~`に変更等）
3. 代替パッケージを提案（例: `node-sass` → `sass`）
4. 再インストール実行

### Pattern 3: ビルドエラー

**エラー**: `npm run build`または`python -m build`で失敗

**対処**:
1. ビルドログを解析（型エラー、インポートエラー等）
2. 自動修正を試行（型定義追加、インポートパス修正）
3. 修正不可能な場合はエラー箇所を`generated_code_report.md`に記載
4. ユーザーに手動修正を依頼

### Pattern 4: デプロイ設定エラー

**エラー**: Vercel/Heroku/AWSデプロイ設定が不正

**対処**:
1. 設定ファイルのバリデーション実行
2. 必須フィールドの欠落をチェック（`VERCEL_TOKEN`等）
3. `.env.example`に不足している環境変数を追加
4. 修正後に再生成

---

## 8. 成功指標

| 指標 | 目標値 | 測定方法 |
|------|--------|---------|
| プロジェクト生成成功率 | > 90% | 生成成功/総実行回数 |
| ビルド成功率 | > 85% | `npm run build`成功/総生成プロジェクト数 |
| テスト生成カバレッジ | > 70% | テストファイル数/コードファイル数 |
| 生成時間 | < 5分/プロジェクト | 実行時間の平均値 |
| 依存関係インストール成功率 | > 95% | `npm install`成功/総実行回数 |

---

## 9. 参照

- **エージェント仕様**: `@.claude/agents/code-generation-agent.md`（本ファイル）
- **並列実行**: `@.claude/rules/parallel_execution.md`
- **Review Agent**: `@.claude/agents/review-agent.md`
- **Executing Agent**: `@.claude/agents/executing-agent.md`
- **Research統合**:
  - ForGenAI: `@GenAI_research/tech_stack/`
  - ForSolo: `@Solopreneur_Research/documents/01_App/case_studies/`

---

**作成日**: 2026-01-03
**Week 3-4実装**: Code Generation Agent（P1）
