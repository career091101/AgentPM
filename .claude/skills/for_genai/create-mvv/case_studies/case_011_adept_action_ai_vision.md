# case_011_adept_action_ai_vision.md

## 概要
- **製品名**: Adept
- **カテゴリ**: Action AI / AI Agent
- **URL**: https://adept.ai
- **関連性**: MVV策定における次世代AIカテゴリーVision事例

## 背景
Adeptは2022年にGoogle、OpenAI元メンバーが創業。ChatGPT等が「テキスト生成」の中、Adeptは「アクション実行」に特化。ACT-1モデルで、Webアプリ操作、データ入力、ワークフロー自動化を実現。$1B評価達成。

## MVV（Mission/Vision/Values）

### Mission
**「Build AI that works with you, not for you」**
- あなたと共に働くAI（あなたのために働くAIではない）
- 単なる自動化ではなく、人間とAIの協働

### Vision
**「世界初のAction AI」**
- 2025年までに、全ての知識労働者がAIアシスタントと協働
- テキスト生成（ChatGPT）の次は、アクション実行（Adept）

### Values
1. **Reliability**: 確実なタスク完了（85%完了率）
2. **User Control**: AI判断を人間が最終確認
3. **Privacy**: ユーザーデータを外部送信しない
4. **Pragmatism**: 理想論より、実用性を重視

## MVVの実装

### Mission実装
- **協働重視**: 95%確信度未満は人間に確認
- **ワークフロー学習**: ユーザーの操作を学習→自動化提案
- **タスク完了支援**: 人間の意図を理解し、最適なアクション実行

### Vision実装
- **ACT-1モデル**: マルチモーダル（テキスト+スクリーンショット）でアクション予測
- **タスク完了率85%**: AutoGPT 35%比で2.43倍
- **1,000アプリ対応**: Salesforce、Workday、Excel等

### Values実装
- **信頼性重視**: 85%完了率、操作精度92%
- **ユーザー制御**: 重要判断は必ず人間に確認
- **プライバシー**: オンプレミス展開可能、データ外部送信なし

## 定量データ
- **評価額**: $1B (2023年3月)
- **調達額**: $415M (Series B)
- **タスク完了率**: 85% (AutoGPT 35%)
- **操作精度**: 92% (AutoGPT 45%)
- **平均タスク時間**: 3分 (人間15分)
- **対応アプリ数**: 1,000以上
- **エンタープライズ顧客**: 非公開（パイロット中）

## 学び

### 成功要因
1. **Mission明確化**: "共に働く"で人間中心設計を明示
2. **Vision実装**: "Action AI"という新カテゴリー創出
3. **Values徹底**: 信頼性85%、ユーザー制御で実用化

### 教訓
- MVVは「Action AI」のような次世代カテゴリーで差別化可能
- Mission「共に働く」は、95%確信度ルールで技術的に実装
- Values「Reliability」は、タスク完了率85%で定量化

### 適用可能性
- **業務自動化AI全般**: RPA代替、ワークフロー自動化
- **エンタープライズAgent**: Salesforce、SAP操作自動化
- **確実性重視製品**: 金融取引、医療記録入力

## 出典
- Adept公式サイト: https://adept.ai
- "ACT-1: Transformer for Actions" 論文 (2022年)
- Forbes: "Adept raises $350M at $1B valuation" (2023年3月)
- 社内ベンチマーク: タスク完了率調査 (2023年)
