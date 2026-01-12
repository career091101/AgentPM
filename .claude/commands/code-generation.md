# Code Generation Command

**コマンド**: `/code-generation`

**説明**: プロジェクトコード・テスト・CI/CD設定の自動生成

**エージェント**: Code Generation Agent

---

## 使用方法

```
/code-generation
```

または

```
コード生成してください
プロジェクト初期化してください
Next.jsプロジェクトを作成してください
```

---

## 実行内容

1. **プロジェクト情報収集**: タイプ、フレームワーク、機能要件の確認
2. **テンプレート選定**: Research統合、最適パターン選択
3. **コード生成**: ディレクトリ構造、コンポーネント、API Routes生成
4. **テスト生成**: ユニット/統合/E2Eテストスケルトン
5. **CI/CD設定**: GitHub Actions/CircleCI設定生成
6. **デプロイ設定**: Vercel/Heroku/AWS設定生成
7. **Git初期化**: リポジトリ初期化、初回コミット
8. **依存関係インストール**: npm install / pip install実行
9. **検証**: ビルド成功確認、テスト実行確認
10. **レポート生成**: generated_code_report.md出力

---

## 入力パラメータ（対話形式で質問）

### 必須パラメータ

1. **プロジェクトタイプ**:
   - 質問: 「プロジェクトタイプを選択してください（frontend / backend / fullstack / ai）」
   - 例: `fullstack`
   - デフォルト: なし（必須）

2. **フレームワーク**:
   - 質問: 「使用するフレームワークを選択してください」
   - フロントエンド: `nextjs` / `react` / `vue` / `svelte`
   - バックエンド: `fastapi` / `django` / `express` / `nestjs`
   - AI特化: `langchain` / `llamaindex`
   - 例: `nextjs`（フロントエンド）、`fastapi`（バックエンド）
   - デフォルト: なし（必須）

3. **プロジェクト名**:
   - 質問: 「プロジェクト名を入力してください（kebab-case推奨）」
   - 例: `my-fitness-app`
   - デフォルト: なし（必須）

### オプションパラメータ

4. **機能要件**:
   - 質問: 「追加する機能を選択してください（複数選択可、スキップ可）」
   - 選択肢: `auth` / `payment` / `email` / `database` / `storage` / `ai`
   - 例: `auth, payment, email, database`
   - デフォルト: なし（スキップ可）

5. **デプロイ先**:
   - 質問: 「デプロイ先を選択してください」
   - 選択肢: `vercel` / `heroku` / `aws` / `docker`
   - 例: `vercel`
   - デフォルト: `vercel`

6. **CI/CDプラットフォーム**:
   - 質問: 「CI/CDプラットフォームを選択してください」
   - 選択肢: `github-actions` / `circleci` / `gitlab-ci`
   - 例: `github-actions`
   - デフォルト: `github-actions`

7. **スタイリング**（フロントエンドの場合のみ）:
   - 質問: 「スタイリング方法を選択してください」
   - 選択肢: `tailwind` / `css-modules` / `styled-components` / `emotion`
   - 例: `tailwind`
   - デフォルト: `tailwind`

8. **言語**（フロントエンドの場合のみ）:
   - 質問: 「使用言語を選択してください」
   - 選択肢: `typescript` / `javascript`
   - 例: `typescript`
   - デフォルト: `typescript`

---

## 出力結果

```
Stock/programs/[program_name]/projects/[project_name]/dev/
├── generated_code/
│   ├── frontend/              # フロントエンドコード（fullstackの場合）
│   │   ├── src/
│   │   ├── tests/
│   │   ├── public/
│   │   └── ...
│   ├── backend/               # バックエンドコード（fullstackの場合）
│   │   ├── app/
│   │   ├── tests/
│   │   └── ...
│   └── .github/workflows/     # CI/CD設定
└── generated_code_report.md  # 生成レポート
```

---

## 実行例

### 例1: Fullstack（Next.js + FastAPI）プロジェクト

```
ユーザー: /code-generation

エージェント: プロジェクトタイプを選択してください（frontend / backend / fullstack / ai）
ユーザー: fullstack

エージェント: 使用するフレームワークを選択してください
フロントエンド: nextjs / react / vue / svelte
バックエンド: fastapi / django / express / nestjs
ユーザー: nextjs (frontend), fastapi (backend)

エージェント: プロジェクト名を入力してください（kebab-case推奨）
ユーザー: my-fitness-app

エージェント: 追加する機能を選択してください（複数選択可、スキップ可）
auth / payment / email / database / storage / ai
ユーザー: auth, payment, email, database

エージェント: デプロイ先を選択してください
ユーザー: vercel

エージェント: CI/CDプラットフォームを選択してください
ユーザー: github-actions

エージェント: スタイリング方法を選択してください
ユーザー: tailwind

エージェント: 使用言語を選択してください
ユーザー: typescript

エージェント: コード生成を開始します...

[3分後]

エージェント: ✅ コード生成が完了しました

**生成されたファイル**:
- フロントエンド (Next.js 14): 45ファイル、3,200行
  - src/app/: 15ファイル（ルーティング、レイアウト）
  - src/components/: 12ファイル（UI コンポーネント）
  - src/lib/: 8ファイル（ユーティリティ、認証、決済）
  - tests/: 10ファイル（ユニットテスト）

- バックエンド (FastAPI): 38ファイル、2,850行
  - app/api/: 10ファイル（API エンドポイント）
  - app/models/: 6ファイル（データモデル）
  - app/services/: 8ファイル（ビジネスロジック）
  - tests/: 14ファイル（APIテスト）

- CI/CD: .github/workflows/ci.yml（80行）
- デプロイ: vercel.json（30行）

**機能統合**:
- ✅ 認証: Supabase Auth
- ✅ 決済: Stripe
- ✅ メール送信: Resend
- ✅ データベース: PostgreSQL (Supabase)

**次のアクション**:
1. 環境変数設定（.env.exampleを参照）
2. 依存関係インストール（npm install / pip install -r requirements.txt）
3. 開発サーバー起動（npm run dev / uvicorn main:app --reload）
4. テスト実行（npm test / pytest）

**生成レポート**: Stock/programs/.../dev/generated_code_report.md
**実行時間**: 3分12秒
```

### 例2: AI特化型（LangChain）プロジェクト

```
ユーザー: AI チャットボットのプロジェクトを作成してください

エージェント: プロジェクトタイプを選択してください（frontend / backend / fullstack / ai）
ユーザー: ai

エージェント: 使用するフレームワークを選択してください
AI特化: langchain / llamaindex
ユーザー: langchain

エージェント: プロジェクト名を入力してください
ユーザー: ai-chatbot-backend

エージェント: 追加する機能を選択してください（複数選択可、スキップ可）
auth / payment / email / database / storage / ai
ユーザー: database, ai

エージェント: デプロイ先を選択してください
ユーザー: heroku

エージェント: CI/CDプラットフォームを選択してください
ユーザー: github-actions

エージェント: コード生成を開始します...

[Research統合中...]
- ForGenAI Research: AI技術スタック選定基準を参照
- OpenAI vs Anthropic vs Google Gemini の比較表をREADME.mdに記載

[2分後]

エージェント: ✅ コード生成が完了しました

**生成されたファイル**:
- app/: 28ファイル、2,100行
  - chains/: 5ファイル（LangChainチェーン）
  - prompts/: 8ファイル（プロンプトテンプレート）
  - vectorstore/: 3ファイル（ベクトルDB統合）
  - api/: 6ファイル（FastAPI エンドポイント）
  - tests/: 6ファイル（テスト）

**AI統合**:
- ✅ OpenAI: GPT-4 Turbo
- ✅ Anthropic: Claude 3.5 Sonnet
- ✅ Google: Gemini 1.5 Pro
- ✅ ベクトルDB: Pinecone
- ✅ プロンプトテンプレート: Chain-of-Thought, Few-shot, ReAct

**Research統合結果**:
- AI技術スタック比較表をREADME.mdに記載
- プロバイダ切り替えロジック（src/lib/ai-client.ts）を自動生成
- コスト最適化戦略（キャッシング、バッチ処理）を実装

**次のアクション**:
1. 環境変数設定（OPENAI_API_KEY, ANTHROPIC_API_KEY, PINECONE_API_KEY）
2. 依存関係インストール（pip install -r requirements.txt）
3. 開発サーバー起動（uvicorn main:app --reload）
4. チャットボットテスト（curl localhost:8000/api/chat）

**生成レポート**: Stock/programs/.../dev/generated_code_report.md
**実行時間**: 2分45秒
```

### 例3: Frontend Only（React + Vite）プロジェクト

```
ユーザー: React プロジェクトを作成してください

エージェント: プロジェクトタイプを選択してください
ユーザー: frontend

エージェント: 使用するフレームワークを選択してください
フロントエンド: nextjs / react / vue / svelte
ユーザー: react

エージェント: プロジェクト名を入力してください
ユーザー: todo-app-frontend

エージェント: 追加する機能を選択してください（複数選択可、スキップ可）
ユーザー: auth

エージェント: デプロイ先を選択してください
ユーザー: vercel

エージェント: CI/CDプラットフォームを選択してください
ユーザー: [Enter]（デフォルト: github-actions）

エージェント: スタイリング方法を選択してください
ユーザー: tailwind

エージェント: 使用言語を選択してください
ユーザー: typescript

エージェント: コード生成を開始します...

[1分30秒後]

エージェント: ✅ コード生成が完了しました

**生成されたファイル**:
- src/: 25ファイル、1,800行
  - components/: 10ファイル
  - hooks/: 4ファイル
  - lib/: 5ファイル（認証ロジック）
  - pages/: 4ファイル
  - tests/: 8ファイル

**機能統合**:
- ✅ 認証: Supabase Auth

**次のアクション**:
1. 環境変数設定（.env.exampleを参照）
2. npm install
3. npm run dev
4. npm test

**生成レポート**: Stock/programs/.../dev/generated_code_report.md
**実行時間**: 1分32秒
```

### 例4: エラーハンドリング（依存関係の競合）

```
ユーザー: /code-generation

[... パラメータ入力 ...]

エージェント: コード生成を開始します...

[2分後]

エージェント: ⚠️ 依存関係のインストールでエラーが発生しました

**エラー詳細**:
```
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
npm ERR! Found: react@18.2.0
npm ERR! Could not resolve dependency: peer react@"^17.0.0" from some-package@1.0.0
```

**対処中...**:
- package.jsonのバージョンを調整中（^18.2.0 → ~18.2.0）
- 代替パッケージを検索中...

[30秒後]

エージェント: ✅ 依存関係の競合を解決しました

**解決方法**:
- `some-package`のバージョンを1.0.0 → 2.0.0に更新（React 18対応版）
- package.jsonを更新
- npm installを再実行

**結果**: 依存関係のインストールが成功しました

**次のアクション**:
1. npm run build で動作確認
2. npm test でテスト実行
```

---

## 既存エージェントとの連携

### Executing Agent完了後のコード生成

```python
# Executing Agent実行
executing_result = Task(description="開発計画作成", ...)

# 開発計画をもとにCode Generation Agent実行
Task(
    description="コード生成 - 開発計画に基づくプロジェクト初期化",
    prompt=generate_code_generation_prompt(executing_result),
    model="sonnet"
)
```

### Review Agent連携（生成コード品質チェック）

```python
# Code Generation Agent実行
code_gen_result = Task(description="コード生成", ...)

# 生成されたコードをReview Agent で品質チェック
Task(
    description="品質レビュー - 生成コード",
    prompt=generate_review_prompt(code_gen_result, doc_type="generated_code"),
    model="sonnet"
)
```

---

## エラーハンドリング

### エラー種別と推奨対処

| エラー | 対処方法 |
|--------|---------|
| **framework_not_supported** | サポート対象フレームワーク一覧を表示、最も近いフレームワークを提案 |
| **dependency_conflict** | package.jsonバージョン調整、代替パッケージ提案、再インストール |
| **build_error** | ビルドログ解析、自動修正試行、修正不可能な場合はレポートに記載 |
| **deploy_config_error** | 設定ファイルバリデーション、必須フィールド確認、.env.example更新 |

---

## 成功指標

| 指標 | 目標値 | 測定方法 |
|------|--------|---------|
| プロジェクト生成成功率 | > 90% | 成功/総実行回数 |
| ビルド成功率 | > 85% | `npm run build`成功/総生成プロジェクト |
| テスト生成カバレッジ | > 70% | テストファイル数/コードファイル数 |
| 生成時間 | < 5分/プロジェクト | 実行時間の平均値 |
| 依存関係インストール成功率 | > 95% | `npm install`成功/総実行回数 |

---

## 参照

- **エージェント仕様**: `@.claude/agents/code-generation-agent.md`
- **並列実行**: `@.claude/rules/parallel_execution.md`
- **Review Agent**: `@.claude/agents/review-agent.md`
- **Executing Agent**: `@.claude/agents/executing-agent.md`
- **Research統合**:
  - ForGenAI: `@GenAI_research/tech_stack/`
  - ForSolo: `@Solopreneur_Research/documents/01_App/case_studies/`

---

**作成日**: 2026-01-03
**Week 3-4実装**: Code Generation Agent（P1）
