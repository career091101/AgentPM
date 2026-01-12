---
case_id: GENAI_PSF_002
company: Cursor
product: Cursor IDE
psf_score: 94
ai_accuracy: 93
hallucination_rate: 4
response_time_p50: 1.5
response_time_p95: 2.0
prompt_reproducibility: 92
ten_x_axes: 3
free_to_paid_conversion: 5.1
dau_mau_ratio: 0.42
product_hunt_rank: 1
genai_research_refs:
  - GenAI_research/sources/Founder_Agent_Videos/cursor_*.md
  - GenAI_research/topics/coding_ai.md
---

# GENAI_PSF_002: Cursor - PSF達成戦略

## PSF指標分析

### AI精度・品質指標
- **AI精度**: 93%（コード生成精度、コンパイル成功率93%）
- **幻覚率**: 4%（コード補完の文脈理解による低減）
- **レスポンス速度**: P50 1.5秒、P95 2.0秒、P99 3.2秒（コード補完最適化）
- **プロンプト再現性**: 92%（コードベース全体理解、Few-shot優秀）
- **コンテキスト長**: プロジェクト全体（数万行のコード理解）

### ビジネス指標
- **Free→Paid転換率**: 5.1%（開発者向け高転換、月額$20）
- **DAU/MAU比**: 0.42（毎日コーディング利用）
- **ユーザー数**: 推定50万MAU（2024年1月時点）、有料会員2.55万人
- **API安定性**: 99.9% Uptime
- **Product Hunt**: #1獲得（2023年3月）

### 10x優位性（3軸達成）
1. **生産性10x**: コード生成・補完により、従来エディタから生産性10倍
2. **学習曲線5x**: 新規プロジェクト理解時間を1/5に短縮
3. **デバッグ速度10x**: エラー検出・修正提案により、デバッグ速度10倍

## 差別化要素（AI Wrapper批判への対応）

### 独自技術・データ
- **IDE統合**: VSCodeフォーク、深いエディタ統合（LSP、DAP）
- **コードベース全体理解**: プロジェクト全体のコンテキスト理解（数万行）
- **マルチファイル編集**: 複数ファイルの同時編集、リファクタリング
- **Cmd+K**: 自然言語でコード編集（Cursor独自UI）
- **独自プロンプト最適化**: コーディング特化のSystem Prompt

### AI Wrapper批判回避戦略
- **IDE深部統合**: 単なるCopilot代替ではなく、IDE全体を再設計
- **コンテキスト理解**: プロジェクト全体理解により、精度93%達成
- **開発者体験**: Cmd+K、マルチファイル編集等の独自UI

## PSF達成タイムライン

- **2022年8月**: Cursor プライベートベータ開始
- **2023年3月**: Product Hunt #1獲得、PSF 70%達成
- **2023年7月**: マルチファイル編集機能、PSF 85%達成
- **2023年11月**: プロジェクト全体理解強化、PSF 94%達成

## 学習ポイント

- **IDE統合**: 深いエディタ統合により、単なるAI Wrapperから脱却
- **コンテキスト理解**: プロジェクト全体理解により、精度93%達成
- **開発者体験**: Cmd+K、マルチファイル編集等の独自UIで差別化
- **Free→Paid 5.1%**: 開発者向け高転換率、月額$20で収益化
- **Product Hunt #1**: 開発者コミュニティで初期トラクション獲得
- **生産性10x**: コード生成により、開発者の生産性10倍改善
