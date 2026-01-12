---
command: /for-genai-build-prompt-library
skill: for_genai/build-prompt-library
description: |
  GenAI製品向け高品質プロンプトテンプレートライブラリ構築スキルを実行。
  5パターン（Zero-shot、Few-shot、Chain-of-Thought、ReAct、Tree-of-Thought）×5ユースケース（要約、生成、分析、変換、コード）＝25テンプレート自動生成。
  精度改善率+15-30%、A/Bテスト方法論、品質指標（精度、一貫性、速度）を提供。
---

# /for-genai-build-prompt-library

GenAI製品向け高品質プロンプトテンプレートライブラリ構築スキルを実行。

## 使用タイミング

- PSF検証完了後、プロンプト設計開始前
- MVP開発開始前
- プロンプト品質改善が必要なとき
- AI精度・一貫性向上が必要なとき

## 実行内容

1. ユースケース分類（5カテゴリ）
2. プロンプトパターン選定テーブル作成（精度改善率付き）
3. ベストプラクティス統合（役割指定、思考プロセス、Few-shot examples）
4. テンプレートライブラリ構造作成（5階層）
5. 品質指標測定（精度、一貫性、速度）
6. A/Bテスト方法論策定
7. GenAI_research統合（実プロダクト事例15件）
8. テンプレート自動生成（25個）
9. 品質評価・A/Bテスト実施
10. 成果物出力

## 出力

```
{IDEA_FOLDER}/prompt_library/
├── README.md
├── library_report.md
├── quality_metrics.md
├── ab_test_methodology.md
├── templates/
│   ├── 01_summarization/
│   ├── 02_generation/
│   ├── 03_analysis/
│   ├── 04_transformation/
│   └── 05_code/
├── pattern_selection_table.md
├── best_practices.md
├── evaluation/
└── examples/
```

## 次のステップ

```
/optimize-prompt-quality（テンプレートライブラリを基にプロンプト品質最適化）
/measure-aarrr（プロンプトライブラリ導入後のActivation/Retention改善効果測定）
/validate-pmf（プロンプト品質向上によるPMF達成検証）
```

## 期待効果

- 精度改善率: +15-30%（Zero-shot基準比）
- テンプレート数: 25個（5カテゴリ×5パターン）
- 品質指標達成: 精度90%以上、一貫性85%以上、速度3秒以下
- A/Bテスト信頼性: p<0.05（統計的有意性確認）

## 関連スキル

- `/optimize-prompt-quality` - プロンプト品質最適化（このライブラリを基に実行）
- `/select-ai-tech-stack` - AI技術スタック選定（LLMプロバイダー選定と連携）
- `/monitor-model-updates` - モデル更新監視（テンプレート再評価が必要）

## Prerequisites
- ForGenAI Edition プロジェクト構造作成済み
- ユースケース分類が明確

## Estimated Time
40-60分（自律実行）
