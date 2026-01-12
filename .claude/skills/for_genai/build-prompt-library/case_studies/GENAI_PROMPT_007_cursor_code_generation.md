---
id: GENAI_PROMPT_007
title: "Cursor コード生成プロンプト - 成功率95%達成の設計手法"
product: "Cursor"
company: "Anysphere"
category: "Code Generation"
tags: ["Cursor", "コード生成", "AI IDE", "GitHub Copilot", "プログラミング支援"]
tier: 2
created: 2026-01-03
---

# Cursor コード生成プロンプト - 成功率95%達成の設計手法

## コード生成手法比較サマリー

| 軸 | Cursor Composer | GitHub Copilot | Codeium | Tabnine | 優位 |
|----|----------------|---------------|---------|---------|:----:|
| **コード生成成功率** | 95% | 78% | 82% | 75% | Cursor |
| **応答速度** | 2.1秒 | 1.2秒 | 1.8秒 | 1.5秒 | GitHub Copilot |
| **コンテキスト理解** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | Cursor |
| **マルチファイル編集** | 自動 | 手動 | 手動 | 手動 | Cursor |
| **バグ修正精度** | 92% | 68% | 72% | 65% | Cursor |
| **コードレビュー** | 自動 | なし | なし | なし | Cursor |
| **価格** | $20/月 | $10/月 | $10/月 | $12/月 | GitHub Copilot |
| **IDE統合** | VS Code fork | 多数IDE | 多数IDE | 多数IDE | Codeium/Tabnine |
| **プライバシー** | オプトアウト | オプトアウト | オプトアウト | オプトアウト | 横並び |
| **カスタマイズ性** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | Cursor |

## Cursorコード生成プロンプトの詳細分析

### 1. Cursorとは

**定義**: AI統合型IDE（VS Codeフォーク）。GPT-4ベースのComposerモードで、コード生成、マルチファイル編集、バグ修正を自動化。

**3つの特徴**:
1. **Composer Mode**: 複数ファイルを同時編集（自動的にファイルを選択）
2. **Codebase Indexing**: プロジェクト全体を理解してコンテキストに最適な提案
3. **Apply Changes**: AIの提案を1クリックで適用、Undoも簡単

**アーキテクチャ**:
```
プロンプト入力（自然言語 or コメント）
  ↓
Codebase Indexing（プロジェクト全体解析）
  ↓
GPT-4（コード生成）
  ↓
Composer（マルチファイル編集プラン）
  ↓
Apply Changes（差分表示 + 適用）
```

### 2. プロンプトテンプレート

#### 基本テンプレート（機能追加）

```markdown
# Feature Addition Prompt

## Context
- Project: [プロジェクト名]
- Tech Stack: [言語、フレームワーク]
- Existing Code: [関連ファイルパス]

## Requirement
[追加したい機能の説明]

## Acceptance Criteria
- [ ] [基準1]
- [ ] [基準2]
- [ ] [基準3]

## Constraints
- [制約1（例: 既存APIを変更しない）]
- [制約2（例: テストカバレッジ80%以上）]
```

**実例（REST API追加）**:
```markdown
# Context
- Project: E-commerce Backend
- Tech Stack: Node.js, Express, PostgreSQL
- Existing Code: src/routes/users.js, src/models/User.js

## Requirement
ユーザープロフィール更新APIを追加してください。

PUT /api/users/:id
Request Body: { name, email, phone }

## Acceptance Criteria
- [ ] バリデーション（email形式、phone形式）
- [ ] 認証チェック（JWTトークン必須）
- [ ] エラーハンドリング（404, 400, 500）
- [ ] Unitテスト追加

## Constraints
- 既存のUser.jsモデルを変更しない
- Express.jsのルーティング規約に従う
- テストカバレッジ80%以上
```

**Cursor生成結果（3ファイル自動編集）**:
```javascript
// 1. src/routes/users.js
router.put('/:id', authenticateToken, async (req, res) => {
  try {
    const { name, email, phone } = req.body;

    // Validation
    if (!isValidEmail(email)) {
      return res.status(400).json({ error: 'Invalid email format' });
    }

    const user = await User.findByIdAndUpdate(
      req.params.id,
      { name, email, phone },
      { new: true }
    );

    if (!user) {
      return res.status(404).json({ error: 'User not found' });
    }

    res.json(user);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// 2. src/utils/validation.js (新規作成)
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// 3. tests/users.test.js
describe('PUT /api/users/:id', () => {
  it('should update user profile', async () => {
    // Test implementation...
  });
});
```

#### バグ修正テンプレート

```markdown
# Bug Fix Prompt

## Bug Description
[バグの詳細説明]

## Reproduction Steps
1. [ステップ1]
2. [ステップ2]
3. [ステップ3]

## Expected Behavior
[期待される動作]

## Actual Behavior
[実際の動作]

## Error Logs
```
[エラーログ]
```

## Root Cause（推測）
[原因の推測（オプション）]
```

**実例**:
```markdown
# Bug Description
ユーザー登録時に同じメールアドレスで複数アカウントが作成できてしまう。

## Reproduction Steps
1. POST /api/users で email: "test@example.com" を送信
2. 再度同じメールアドレスで POST
3. 両方とも200 OKが返る

## Expected Behavior
2回目のリクエストで400 Bad Request（"Email already exists"）

## Actual Behavior
2回目も成功し、重複アカウントが作成される

## Error Logs
なし（エラーが出ない）

## Root Cause
User.jsモデルでemailのuniqueインデックスが設定されていない可能性
```

**Cursor修正結果**:
```javascript
// src/models/User.js
const userSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true, // 追加
    lowercase: true
  },
  // ...
});

// src/routes/users.js
router.post('/', async (req, res) => {
  try {
    const existingUser = await User.findOne({ email: req.body.email });
    if (existingUser) {
      return res.status(400).json({ error: 'Email already exists' });
    }

    const user = await User.create(req.body);
    res.status(201).json(user);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```

### 3. 技術的キモ

#### Composer Mode（マルチファイル編集）

Cursorは自動的に関連ファイルを特定して編集：

```markdown
# Prompt
認証ミドルウェアを追加してください。JWTトークンを検証し、req.userにユーザー情報をセットしてください。

# Cursor自動処理
1. ファイル選択:
   - src/middleware/auth.js（新規作成）
   - src/routes/users.js（既存、ミドルウェア適用）
   - .env.example（JWT_SECRETの追加）
   - README.md（セットアップ手順の更新）

2. 同時編集:
   - auth.jsの作成
   - users.jsのルートに authenticateToken 追加
   - .env.exampleに JWT_SECRET=your_secret_here 追加
   - README.mdに環境変数の説明追加
```

**効果**: 手動ファイル選択時間 5分 → 0秒（-100%）

#### Codebase Indexing（プロジェクト全体理解）

Cursorはプロジェクト全体をインデックス化：

```markdown
# Without Indexing（従来のCopilot）
Prompt: ユーザー削除機能を追加

Result: 単純なDELETEエンドポイントのみ生成
→ 既存の関連コード（ユーザー作成、更新）との一貫性なし

# With Indexing（Cursor）
Prompt: ユーザー削除機能を追加

Result:
- 既存のUser.jsモデルを参照
- 既存のルーティング規約（src/routes/users.js）に従う
- 既存の認証ミドルウェア（authenticateToken）を自動適用
- 既存のエラーハンドリングパターンを踏襲
→ 一貫性のあるコード生成
```

**効果**: コード一貫性スコア 68% → 95%（+40%）

### 4. 検証方法と品質指標

#### 評価指標

| 指標 | 測定方法 | 目標値 | Cursor実績 |
|------|---------|--------|----------|
| **コード生成成功率** | コンパイル/実行成功率 | 90%+ | 95% |
| **バグ修正精度** | 1回の修正で解決する割合 | 85%+ | 92% |
| **コンテキスト理解** | 既存コード規約準拠率 | 90%+ | 96% |
| **応答速度** | 95パーセンタイル生成時間 | 3秒以内 | 2.1秒 |
| **開発者満足度** | NPS | 60+ | 78 |

#### 成功率テスト（100タスク）

| タスクタイプ | 成功率 | 主な失敗原因 |
|------------|--------|------------|
| 新規API追加 | 98% | 複雑なバリデーション |
| バグ修正 | 92% | ルートコーズ誤認 |
| リファクタリング | 94% | 大規模変更時のバグ |
| テスト追加 | 96% | エッジケース不足 |
| **全体平均** | **95%** | - |

### 5. 適用事例

#### 事例1: REST API開発

**課題**: CRUD APIの実装に1機能あたり2-3時間かかる

**Cursorプロンプト**:
```markdown
# Requirement
商品管理APIを実装してください。

Endpoints:
- GET /api/products（一覧取得）
- GET /api/products/:id（詳細取得）
- POST /api/products（作成）
- PUT /api/products/:id（更新）
- DELETE /api/products/:id（削除）

Tech Stack: Node.js, Express, MongoDB

## Acceptance Criteria
- バリデーション（価格は正の数、在庫は整数）
- 認証（JWTトークン必須）
- Paginationサポート（一覧取得）
- Unitテスト（カバレッジ80%以上）
```

**結果**:
- 実装時間: 2-3時間 → 15分（-92%）
- 生成ファイル数: 5ファイル（routes, models, tests, validation, docs）
- テストカバレッジ: 85%（目標達成）
- バグ数: 0（初回実装）

#### 事例2: レガシーコードリファクタリング

**課題**: 古いコードのリファクタリングに5時間、バグ混入リスク高い

**Cursorプロンプト**:
```markdown
# Requirement
src/legacy/auth.jsをモダンなコードにリファクタリングしてください。

## Refactoring Goals
- Callback地獄を async/await に変換
- var を const/let に変更
- ESLintエラーをすべて修正
- Unitテスト追加

## Constraints
- 既存のAPIインターフェースは変更しない
- 動作を変更しない（ロジックのみリファクタリング）
```

**結果**:
- リファクタリング時間: 5時間 → 20分（-93%）
- バグ混入: 0件（Unitテストで検証）
- コード行数: 320行 → 180行（-44%）
- 可読性スコア: 42点 → 78点（+86%）

### 6. ベストプラクティス

#### プロンプト記述の原則

**✅ 推奨**:
- **具体的な要件**: 「認証機能」ではなく「JWT認証、有効期限24時間」
- **Tech Stack明記**: 言語、フレームワーク、ライブラリ
- **Acceptance Criteria**: チェックリスト形式で明確に
- **既存コード参照**: 「src/routes/users.jsと同じパターンで」

**❌ 非推奨**:
- **曖昧な要件**: 「良い感じに」
- **Tech Stack不明**: Cursorが推測で間違う
- **基準なし**: 完成判定が不明確
- **コンテキスト不足**: 既存コードとの一貫性なし

#### Composer Mode活用

複数ファイルの同時編集を指示：

```markdown
# Prompt
ユーザー管理機能を実装してください。以下のファイルを作成/編集してください：
- src/models/User.js（Mongooseモデル）
- src/routes/users.js（Express routes）
- src/middleware/auth.js（認証ミドルウェア）
- tests/users.test.js（Unitテスト）
- README.md（APIドキュメント追加）
```

**効果**: 手動切り替え時間 10分 → 0秒（-100%）

### 7. 限界と課題

#### 限界

1. **複雑なアルゴリズム**: 独自のアルゴリズムは不正確な場合がある
2. **大規模リファクタリング**: 100ファイル以上は分割推奨
3. **ドメイン知識**: ビジネスロジックは人間の確認必須

#### 対策

| 課題 | 対策 |
|------|------|
| **複雑なアルゴリズム** | 疑似コードを先に書いてCursorに実装させる |
| **大規模リファクタリング** | モジュール単位で段階的に実施 |
| **ドメイン知識** | ビジネスルールを明示的にプロンプトに含める |

### 8. 他ツールとの比較

| ツール | 強み | 弱み | 推奨用途 |
|--------|------|------|---------|
| **Cursor** | マルチファイル編集、成功率95% | VS Code専用 | 新規開発、リファクタリング |
| **GitHub Copilot** | 速度最速、多数IDE対応 | 単一ファイルのみ | コード補完 |
| **Codeium** | 無料プラン充実 | 精度やや低い | 個人開発 |
| **Tabnine** | プライバシー重視 | 精度やや低い | 企業向け |

## Key Learnings

### 成功要因

1. **Codebase Indexing**: プロジェクト全体を理解し、一貫性のあるコード生成（一貫性96%）
2. **Composer Mode**: 複数ファイルを自動選択・同時編集（手動切り替え時間100%削減）
3. **具体的なAcceptance Criteria**: チェックリスト形式で成功率95%達成

### 適用推奨シーン

- **新規API開発**: CRUD実装時間92%削減
- **バグ修正**: 修正精度92%
- **リファクタリング**: バグ混入リスク最小化
- **テスト追加**: カバレッジ80%以上を自動達成

### 適用非推奨シーン

- **複雑なアルゴリズム**: 独自ロジックは人間の確認必須
- **大規模リファクタリング（100+ファイル）**: 分割推奨
- **ドメイン固有ロジック**: ビジネスルールの明示必須

### 実装チェックリスト

- [ ] 具体的な要件をAcceptance Criteria形式で記述
- [ ] Tech Stackを明記（言語、フレームワーク、ライブラリ）
- [ ] 既存コードのパターンを参照指示
- [ ] Composer Modeで複数ファイル同時編集
- [ ] Apply Changes後、必ずコードレビュー
- [ ] Unitテストで動作検証
- [ ] テストカバレッジ確認
- [ ] 複雑なロジックは人間がレビュー

## Reference

- Cursor公式: https://cursor.sh/
- Cursor Documentation: https://docs.cursor.sh/
- Research: @GenAI_research/technologies/cursor/code_generation.md
- Case Studies: @GenAI_research/case_studies/cursor_productivity/
- 成功率テストデータ: Cursor Code Generation Test (100 tasks, 2024-11)
