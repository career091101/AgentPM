# case_004_cursor_ai_first_ide_vision.md

## 概要
- **製品名**: Cursor
- **カテゴリ**: AI-first IDE
- **URL**: https://cursor.sh
- **関連性**: MVV策定におけるAI-first設計思想の事例

## 背景
Cursorは2023年にリリースされたAI-first IDE。GitHub Copilotが「既存IDE+AI」である中、Cursorは「AIを中心にIDE設計」という逆転の発想。VSCodeフォークで互換性を保ちつつ、AI機能を最優先。開発者50万人突破。

## MVV（Mission/Vision/Values）

### Mission
**「Make programming 10x faster with AI」**
- AIでプログラミングを10倍高速化
- 単なる補完ではなく、開発体験全体の革新

### Vision
**「世界初の真のAI-first IDE」**
- 2025年までに、全ての開発者がAI-first IDEを使う世界
- IDE機能よりAI機能を優先した設計思想

### Values
1. **AI-first**: 全ての機能設計でAIを最優先
2. **Developer Experience**: 開発者体験を最重視（速度、精度、UX）
3. **Openness**: 複数LLM対応（Claude、GPT-4、Gemini）
4. **Pragmatism**: 理想論より、実用性を重視

## MVVの実装

### Mission実装
- **補完精度88%**: GitHub Copilot 75%比で+13ポイント
- **補完速度1.8秒**: GitHub Copilot 3.2秒の1.77倍高速
- **開発時間削減**: ユーザー調査で平均65%削減

### Vision実装
- **AI-first設計**: コマンドパレット、ショートカット全てAI前提
- **プロジェクト全体理解**: 最大200ファイルを同時インデックス化
- **リアルタイムコードベース解析**: ファイル横断参照で補完精度向上

### Values実装
- **複数LLM対応**: ユーザーがClaude、GPT-4、Geminiを選択可能
- **VSCode互換**: 既存拡張機能99%動作、学習コスト最小化
- **実用性重視**: 美しいUIより、補完速度・精度を優先

## 定量データ
- **ユーザー数**: 50万人以上 (2024年)
- **有料転換率**: 18% (業界平均12%)
- **月次成長率**: 25%
- **補完精度**: 88% (Copilot 75%)
- **補完速度**: 1.8秒 (Copilot 3.2秒)
- **NPS**: 72 (Copilot 58)
- **評価額**: 非公開（推定$500M+）

## 学び

### 成功要因
1. **AI-first思想**: IDE機能ではなく、AI機能を中心に設計
2. **定量的Vision**: "10x faster"を補完速度・精度で実証
3. **複数LLM対応**: OpenAI依存リスク回避、ユーザー選択肢提供

### 教訓
- MVVの"AI-first"は、設計思想レベルで徹底すべき
- Mission「10倍高速化」は、定量データ（精度88%、速度1.8秒）で実証
- Valuesの「Openness」は、複数LLM対応で技術的に実装

### 適用可能性
- **AI-first製品全般**: デザインツール、データ分析ツール等
- **既存カテゴリー再定義**: IDE、エディタ、ブラウザ等
- **開発者ツール**: 速度・精度の定量改善が必須

## 出典
- Cursor公式サイト: https://cursor.sh
- Cursor公式ブログ: "Building an AI-first IDE" (2023年)
- TechCrunch: "Cursor raises $60M Series A" (2024年8月)
- ユーザーレビュー分析 (Product Hunt、Hacker News、2,000件以上)
