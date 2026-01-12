# Research Index Command

**コマンド**: `/research-index`

**説明**: Research Database検索・事例参照提案

**エージェント**: Research Index Agent

---

## 使用方法

```
/research-index
```

または

```
成功事例を検索してください
関連事例を探してください
```

---

## 実行内容

1. **クエリ入力**: 自然言語で検索内容を入力
2. **セマンティック検索**: ベクトルDB（Pinecone/Supabase pgvector）で類似事例検索
3. **リランキング**: ドメイン一致優先、日付新しい順、多様性確保
4. **要約生成**: 各事例の3行要約（課題、ソリューション、結果）
5. **クロスドメインインサイト**: 複数ドメイン横断時の統合戦略提示
6. **結果返却**: search_results.md（人間可読）、search_results.json（機械可読）

---

## 入力パラメータ

1. **検索クエリ**（必須）: 例: 「AIフィットネスアプリの成功事例」
2. **ドメイン指定**（オプション）: for_genai / for_recruit / for_solo / for_startup / all（デフォルト: all）
3. **検索モード**（オプション）: quick / standard / deep（デフォルト: standard）
4. **Top N件**（オプション）: 1-20（デフォルト: 5）
5. **類似度閾値**（オプション）: 0.0-1.0（デフォルト: 0.7）

---

## 実行例

```
ユーザー: /research-index

エージェント: 検索したい内容を自然言語で入力してください
ユーザー: AIフィットネスアプリの成功事例

エージェント: 検索対象のドメインを選択してください（複数選択可）
ユーザー: for_solo, for_genai

エージェント: 検索を実行中...

[4.2秒後]

エージェント: ✅ 検索完了（5件）

1. [92%] Marc Lou - ShipFast
   - 初月100 MRR達成、6ヶ月で$50K売上
   - ドメイン: ForSolo

2. [88%] Tony Dinh - Black Magic
   - ローンチ初日$1K売上、3ヶ月で$10K MRR
   - ドメイン: ForSolo

3. [85%] Product Hunt #1獲得戦略
   - #1獲得で初日500-1000ユーザー獲得
   - ドメイン: ForGenAI

クロスドメインインサイト:
- ShipFastボイラープレートでAI機能を高速実装
- Build in Public戦略でフォロワー獲得
- Product Hunt #1を狙い、初期ユーザー500-1000獲得

詳細: Flow/202601/2026-01-03/research_search/search_results.md
```

---

## 成功指標

| 指標 | 目標値 |
|------|--------|
| 検索精度 | > 80% |
| 検索速度 | < 10秒 |
| 事例提案の採用率 | > 50% |

---

## 参照

- **エージェント仕様**: `@.claude/agents/research-index-agent.md`
- **Research統合**:
  - ForGenAI: `@GenAI_research/`
  - ForSolo: `@Solopreneur_Research/`
  - ForRecruit: `@Recruit_Product_Research/`
  - ForStartup: `@Recruit_Product_Research/`

---

**作成日**: 2026-01-03
**Week 4-5実装**: Research Index Agent（P1）
