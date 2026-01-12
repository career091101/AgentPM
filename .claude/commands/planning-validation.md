# Planning Validation Command

**コマンド**: `/planning-validation`

**説明**: WBS/Backlog/Roadmap整合性検証

**エージェント**: Planning Validation Agent

---

## 使用方法

```
/planning-validation
```

または

```
計画を検証してください
WBSとBacklogの整合性をチェックしてください
```

---

## 実行内容

1. **入力ファイル読み込み**: WBS、Backlog、Roadmap、リソース情報
2. **整合性チェック**: WBS ⇔ Backlogマッピング、優先度・工数確認
3. **スケジュール検証**: 期間・工数の妥当性、バッファ率確認
4. **リソース検証**: スキルギャップ、負荷分散チェック
5. **依存関係検証**: 循環依存検出（DFS）
6. **クリティカルパス特定**: CPMアルゴリズムで最短期間算出
7. **レポート生成**: 矛盾リスト、推奨対処、総合評価スコア
8. **修正提案**: 自動修正可能な矛盾の修正版生成

---

## 入力パラメータ

1. **WBSファイルパス**（必須）: 例: `Stock/programs/.../draft_wbs.md`
2. **Backlogファイルパス**（必須）: 例: `Stock/programs/.../backlog.yaml`
3. **Roadmapファイルパス**（オプション）: 例: `Stock/programs/.../draft_product_roadmap.md`
4. **リソース情報ファイルパス**（オプション）: 例: `team_members.yaml`
5. **検証モード**（オプション）: quick / standard / deep（デフォルト: standard）

---

## 実行例

```
ユーザー: /planning-validation

エージェント: WBSファイルのパスを教えてください
ユーザー: Stock/programs/.../documents/3_planning/draft_wbs.md

エージェント: Backlogファイルのパスを教えてください
ユーザー: Stock/programs/.../documents/3_planning/backlog.yaml

エージェント: 検証モードを選択してください
ユーザー: standard

エージェント: 検証を実行中...

[8分12秒後]

エージェント: ✅ 検証完了

**総合評価**: 68/100（修正推奨）

**検出された問題**:
- [高] WBSタスク「ユーザー認証実装」がBacklogに未反映
- [高] Backlogストーリー「決済機能」（優先度: High）がWBSで後半配置
- [中] WBS/Backlog工数合計の不一致（120h vs 100h）
- [高] タスク「API開発」の期間が工数と不整合
- [高] ML専門スキル不足

**クリティカルパス**:
要件定義（2週間）→ API設計（2週間）→ API実装（3週間、リスク高）→ 統合テスト（1週間）

**修正提案**:
3件の矛盾は自動修正可能です。修正版を生成しますか？
修正後の評価予測: 82/100（合格）

詳細: Flow/202601/2026-01-03/planning_validation/validation_report.md
```

---

## 成功指標

| 指標 | 目標値 |
|------|--------|
| 矛盾検出率 | > 90% |
| False Positive | < 10% |
| 検証時間 | < 10分 |

---

## 参照

- **エージェント仕様**: `@.claude/agents/planning-validation-agent.md`
- **Planning Agent**: `@.claude/agents/planning-agent.md`

---

**作成日**: 2026-01-03
**Week 5-6実装**: Planning Validation Agent（P1）
