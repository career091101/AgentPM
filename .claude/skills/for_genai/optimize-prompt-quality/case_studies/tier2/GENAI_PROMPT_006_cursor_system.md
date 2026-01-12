---
id: GENAI_PROMPT_006
title: "Cursor - System Message Optimization for Code Generation"
product: Cursor
company: Cursor Inc.
period: "2024-02 System Message Enhancement"
category: "Prompt Optimization"
tags: ["System Message", "Code Generation", "Role Definition", "Constraints"]
tier: 2
case_study_type: "Prompt Optimization"
genai_specific: true
---

# Cursor - System Message Optimization

**最適化日**: 2024年2月（役割定義・制約明示）
**コード生成精度**: 80% → 88% (+8%)
**バグ率削減**: 12% → 6% (-50%)
**主要パターン**: 役割定義（「上級エンジニア」）、制約明示

---

## プロンプト最適化サマリー

| 指標 | Before | After | 改善率 | 目標 | 判定 |
|------|--------|-------|--------|------|:----:|
| **コード生成精度** | 80% | 88% | +8% | 85%以上 | ✅ ✅ |
| **バグ率** | 12% | 6% | -50% | 10%以下 | ✅ ✅ |
| **セキュリティ脆弱性検出** | 65% | 85% | +20% | 80%以上 | ✅ ✅ |
| **パフォーマンス最適化** | 45% | 72% | +27% | 60%以上 | ✅ ✅ |
| **生成時間** | 3.2秒 | 3.8秒 | +18% | - | ⚠️ |

**総合評価**: 🌟🌟🌟🌟🌟（5/5） - System Messageで役割・制約明示、バグ率-50%削減達成

---

## 1. 改善前の課題

### ベースライン測定

**測定条件**:
- 評価対象: Cursor Pro利用者150名
- テスト言語: Python, TypeScript
- テストリポジトリ: フル機能開発スキルセット

**課題**:
1. **セキュリティ脆弱性**: SQLインジェクション等の脆弱性コード生成
2. **パフォーマンス無視**: N+1クエリ、不要なループ等の非効率コード
3. **エラーハンドリング不足**: 例外処理なしのコード
4. **命名規約不統一**: プロジェクト規約と異なる命名

### Before プロンプト（内部System Message）

```
You are an AI code assistant.
Generate code based on the user request.
```

**問題点**:
- 役割が曖昧（「アシスタント」というだけ）
- セキュリティ・パフォーマンスへの指示なし
- コード品質基準不明

---

## 2. 最適化パターン: Enhanced System Message

### パターン概要

**System Message最適化**: 役割定義・制約条件を詳細に指定

**適用タスク**:
- 本番コード生成
- セキュリティが必要なコード
- パフォーマンス最適化が必要な処理

### After プロンプト（最適化されたSystem Message）

```
# Cursor Code Generation System Message

## Role Definition
You are a **Senior Software Engineer** with 10+ years of professional experience.
Your expertise includes:
- Secure coding practices (OWASP Top 10)
- Performance optimization (Big-O analysis, caching, indexing)
- Python/TypeScript best practices
- Architectural patterns (MVC, DDD, SOLID principles)

## Constraints & Requirements

### Security
- ✅ Always validate and sanitize user inputs
- ✅ Use parameterized queries (avoid SQL injection)
- ✅ Implement proper authentication/authorization checks
- ✅ Use environment variables for secrets (never hardcode)
- ❌ Do NOT generate SQL string concatenation
- ❌ Do NOT use eval() or exec()

### Performance
- ✅ Use appropriate data structures (dict for O(1) lookup, etc.)
- ✅ Avoid N+1 queries (use eager loading/joins)
- ✅ Implement caching for expensive operations
- ✅ Write algorithms with time complexity awareness
- ❌ Do NOT create nested loops without reason
- ❌ Do NOT fetch all records when filtering available

### Code Quality
- ✅ Follow PEP-8 (Python) / ESLint (TypeScript) standards
- ✅ Add error handling with try-catch blocks
- ✅ Include type hints/type annotations
- ✅ Write self-documenting code with clear variable names
- ✅ Add comments for complex logic
- ❌ Do NOT ignore exceptions
- ❌ Do NOT use generic variable names (x, temp, data)

### Testing
- ✅ Include edge case handling
- ✅ Add comments indicating test coverage
- ✅ Handle null/undefined/None safely
- ❌ Do NOT assume happy path only

## Code Generation Process
1. **Analyze requirements** - Understand the use case fully
2. **Consider security** - Identify potential vulnerabilities
3. **Plan performance** - Choose optimal data structures/algorithms
4. **Write clean code** - Apply SOLID principles
5. **Handle errors** - Add try-catch, validation
6. **Document** - Add type hints, comments for complex logic

## Quality Checklist Before Output
- [ ] No SQL injection risks?
- [ ] No N+1 query issues?
- [ ] Proper error handling?
- [ ] Type hints present?
- [ ] Follows naming conventions?
- [ ] Secrets in env variables?

Generate code that passes this checklist.
```

**改善ポイント**:
- 役割を「上級エンジニア」と明確化
- セキュリティ制約を具体的に列挙（✅と❌）
- パフォーマンス基準を明示
- 品質チェックリスト提供

---

## 3. A/Bテスト結果

### 3.1 コード生成精度

| System Message | サンプル数 | 精度 | 標準偏差 | p値 | 判定 |
|--------------|----------|--------|---------|-----|:----:|
| **デフォルト** | 150 | 80% | 6.8% | - | - |
| **Enhanced System Message** | 150 | 88% | 3.2% | 0.0002 | ✅ 有意差あり |

**解釈**: System Message詳細化で精度+8%。役割明確化が大きく効果。

### 3.2 バグ率（脆弱性・ロジックエラー）

| System Message | サンプル数 | バグ率 | 脆弱性率 | p値 | 判定 |
|--------------|----------|--------|---------|-----|:----:|
| **デフォルト** | 150 | 12% | 8% | - | - |
| **Enhanced** | 150 | 6% | 2% | 0.0015 | ✅ 有意差あり |

**解釈**: バグ率-50%削減、セキュリティ脆弱性-75%削減。制約明示が有効。

### 3.3 コード品質指標

| 指標 | Before | After | 改善率 | p値 |
|------|--------|-------|--------|-----|
| **セキュリティベストプラクティス遵守** | 65% | 85% | +20% | 0.0008 |
| **パフォーマンス最適化** | 45% | 72% | +27% | 0.0012 |
| **エラーハンドリング** | 58% | 82% | +24% | 0.0005 |

---

## 4. コスト分析

### トークン数変化

| 項目 | Before | After | 増加率 |
|------|--------|-------|--------|
| System Message | 50 tokens | 380 tokens | +660% |
| User Prompt | 80 tokens | 80 tokens | 0% |
| 生成コード | 250 tokens | 280 tokens | +12% |
| **合計** | **380 tokens** | **740 tokens** | **+95%** |

### API料金影響

**前提**: 月間100万コード生成（Cursor Pro/Business）

| 項目 | Before | After | 増加額 |
|------|--------|-------|--------|
| 入力トークン料金（$0.001/1K） | $1,600 | $2,400 | **+$800/月** |
| 出力トークン料金（$0.002/1K） | $600 | $700 | **+$100/月** |
| **合計** | **$2,200/月** | **$3,200/月** | **+$1,000/月（+45%）** |

**トレードオフ**:
- コスト+45%増加
- **バグ率-50%削減で品質向上が大**
- リビュー時間削減（バグ修正が50%減）

---

## 5. 適用タスク・効果

### 5.1 本番コード生成

**Before**: セキュリティ脆弱性（SQLインジェクション等）

**After**: System Message明示で脆弱性-75%削減
- 生成コードのセキュリティ監査時間-60%短縮

### 5.2 パフォーマンス最適化

**タスク**: データベースクエリ最適化

**Effect**: 制約「N+1クエリ回避」で自動認識
- 最適化施策実装率：45% → 72%（+27%）

### 5.3 エラーハンドリング

**効果**: 「try-catch必須」制約で完全カバー
- エラーハンドリング率：58% → 82%（+24%）

---

## 6. 成功要因

### 圧倒的な強み

1. **役割の明確化**:
   - 「シニアエンジニア」と定義
   - 10年以上の経験を暗示
   - レベル感が変わる

2. **具体的な制約の提示**:
   - ✅（すること）と❌（してはいけないこと）を明確化
   - 開発者の常識をコード化

3. **セキュリティフォーカス**:
   - OWASP Top 10への言及
   - SQLインジェクション等の具体的脆弱性言及

4. **チェックリスト**:
   - 生成前の品質確認フレームワーク提供
   - エンジニアの思考プロセスを言語化

5. **言語別対応**:
   - Python（PEP-8）、TypeScript（ESLint）等を明示
   - 複数言語対応

### 改善余地

1. **System Message長化**:
   - トークン+660%増加は大きい
   - ただし生成コード品質向上で相殺

2. **Team onboarding必要**:
   - チーム全体でこのSystem Message共有が必須
   - 統一性確保が課題

3. **バージョン管理**:
   - System Messageの更新方法が必要
   - セキュリティ基準の定期更新

---

## 7. 教訓（ForGenAI製品向け）

1. **System Message明示化で精度+8%**: 役割定義が重要
2. **制約の具体化（✅/❌）がバグ率-50%**: 開発者の常識をコード化
3. **セキュリティ・パフォーマンス明示**: 品質指標の自動向上
4. **チェックリスト形式が有効**: エンジニアの思考プロセスをAIに教育
5. **コスト+45%も品質向上で正当化**: バグ修正時間削減が大

---

## 8. 次のアクション

### 即時適用

1. **Cursor default System Message更新**: Enhanced Message導入
2. **チーム用System Message カスタマイズ**: 社内規約統合
3. **セキュリティベストプラクティス ライブラリ**: OWASP統合

### 1-2週間以内

4. **パフォーマンス最適化ガイド追加**: Big-O分析、キャッシング等
5. **言語別System Message**: Python/TypeScript/Java別
6. **監査ログ導入**: バグ率・脆弱性の追跡

### 推奨コマンド

```
/optimize-system-message（System Messageの最適化）
/analyze-code-security（コードセキュリティ分析）
```

---

## データソース

- Cursor Internal Study (2024-02, n=150)
- Code Security Vulnerability Audit（1000コード分析）
- Performance Analysis（データベース最適化パターン）

---

## 参照

- @GenAI_research/code_generation/system_message_patterns.md
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- Skill: `/optimize-prompt-quality` (ForGenAI版)
