---
name: for-genai-validate-ai-ethics
description: GenAI製品向けAI倫理検証（Transparency、Fairness、Privacy、Accountability、Safety 5カテゴリー100点満点評価）
version: 1.0.0
---

# /for-genai-validate-ai-ethics

GenAI製品のAI倫理基準を5カテゴリー100点満点で評価します。

## 実行

```bash
/for-genai-validate-ai-ethics
```

## 詳細

- **Skill**: `/Users/yuichi/AIPM/aipm_v0/.claude/skills/for_genai/validate-ai-ethics/SKILL.md`
- **出力**: `{IDEA_FOLDER}/ai_ethics_validation/ethics_report.md`

## 評価カテゴリー（各20点満点、合計100点）

1. **Transparency（透明性）**: モデル動作説明、データソース開示、限界点明示
2. **Fairness（公平性）**: バイアステスト、公平性指標測定、多様性配慮
3. **Privacy（プライバシー）**: データ最小化、GDPR/CCPA準拠、セキュリティ対策
4. **Accountability（説明責任）**: 監査ログ、フィードバック機能、責任者明示
5. **Safety（安全性）**: ハルシネーション防止、有害コンテンツフィルタリング、Kill Switch

## 合格基準

- **総合スコア**: 70点以上/100点
- **Transparency**: 15点以上/20点
- **Fairness**: 14点以上/20点
- **Privacy**: 14点以上/20点
- **Accountability**: 14点以上/20点
- **Safety**: 13点以上/20点

## 倫理違反事例分析

- Amazon採用AI（性別バイアス）
- Microsoft Tay（ヘイトスピーチ）
- COMPAS（人種バイアス）
- Meta Galactica（ハルシネーション）
- ChatGPT Italy Ban（GDPR違反）

## ベストプラクティス参照

- OpenAI Model Card
- Anthropic Constitutional AI
- Google AI Principles
- Apple Differential Privacy
- IBM AI Fairness 360
