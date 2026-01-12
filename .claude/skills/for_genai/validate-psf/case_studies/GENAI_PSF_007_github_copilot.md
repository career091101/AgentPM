---
case_id: GENAI_PSF_007
company: GitHub (Microsoft)
product: GitHub Copilot
psf_score: 88
ai_accuracy: 91
hallucination_rate: 5
response_time_p50: 1.0
response_time_p95: 1.5
prompt_reproducibility: 91
ten_x_axes: 3
free_to_paid_conversion: 18
dau_mau_ratio: 0.44
product_hunt_rank: null
genai_research_refs:
  - GenAI_research/sources/Founder_Agent_Videos/github_*.md
  - GenAI_research/topics/coding_ai.md
---

# GENAI_PSF_007: GitHub Copilot - PSF達成戦略

## PSF指標分析

### AI精度・品質指標
- **AI精度**: 91%（コード補完精度、受け入れ率46%）
- **幻覚率**: 5%（コード補完の文脈理解による低減）
- **レスポンス速度**: P50 1.0秒、P95 1.5秒、P99 2.2秒
- **プロンプト再現性**: 91%（コメント→コード生成品質安定）
- **エディタ統合**: VSCode, Visual Studio, JetBrains, Neovim

### ビジネス指標
- **Free→Paid転換率**: 18%（学生・OSS無料、企業向け$10-$19/月）
- **DAU/MAU比**: 0.44（毎日コーディング利用）
- **ユーザー数**: 150万有料会員（2024年1月時点）、MAU推定833万人
- **API安定性**: 99.9% Uptime
- **Product Hunt**: N/A（GitHub統合、Product Hunt未投稿）

### 10x優位性（3軸達成）
1. **コーディング速度10x**: コード補完により、従来エディタから10倍高速
2. **学習曲線5x**: 新規API理解時間を1/5に短縮
3. **バグ削減3x**: コード品質向上により、バグ数を1/3に削減

## 差別化要素（AI Wrapper批判への対応）

### 独自技術・データ
- **GitHub統合**: GitHub全リポジトリ（数十億行のコード）学習
- **エディタ統合**: VSCode, Visual Studio等、深いエディタ統合
- **Codex（GPT-3.5特化）**: OpenAI Codexカスタマイズ、コード生成特化
- **コンテキスト理解**: ファイル全体・プロジェクト理解
- **独自プロンプト最適化**: コーディング特化のSystem Prompt

### AI Wrapper批判回避戦略
- **GitHub統合**: 単なるCodex APIではなく、GitHub全リポジトリ統合
- **エディタ深部統合**: LSP、DAP統合による深いエディタ連携
- **学生・OSS無料**: コミュニティ形成、学習データ収集

## PSF達成タイムライン

- **2021年10月**: GitHub Copilot Technical Preview リリース
- **2022年6月**: GitHub Copilot GA（$10/月）、PSF 70%達成
- **2023年3月**: GitHub Copilot X発表、Chat機能、PSF 80%達成
- **2023年11月**: GitHub Copilot Enterprise（$39/月）、PSF 88%達成

## 学習ポイント

- **GitHub統合**: GitHub全リポジトリ学習により、精度91%達成
- **エディタ統合**: VSCode, Visual Studio等、深いエディタ統合で差別化
- **Free→Paid 18%**: 学生・OSS無料戦略により、コミュニティ形成
- **150万有料会員**: 企業向け$10-$19/月、推定年間$180M ARR
- **受け入れ率46%**: コード補完の46%が開発者に受け入れられる
- **DAU/MAU 0.44**: 毎日コーディング利用、高エンゲージメント
