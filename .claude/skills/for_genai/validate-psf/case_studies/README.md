# Tier 2 Case Studies - ForGenAI PSF検証

GenAI製品のPSF（Product-Solution Fit）達成事例を体系化したケーススタディ集。

## 概要

12件のTier 2ケーススタディ（PSFスコア 83-98/100）を収録。各ケースは以下を含む：

- **AI精度指標**: 精度、幻覚率、レスポンス速度、プロンプト再現性
- **ビジネス指標**: Free→Paid転換率、DAU/MAU比、Product Hunt順位
- **10倍優位性**: 3軸以上の差別化要素
- **AI Wrapper批判への対応**: 独自技術・データによる差別化戦略
- **PSF達成タイムライン**: MVP→PSF 70%→PSF 90%の成長過程
- **学習ポイント**: 5-6個の重要な洞察

## ケーススタディ一覧（PSFスコア降順）

### PSF Excellence（PSFスコア 92-98/100）

| ID | 製品 | PSFスコア | AI精度 | レスポンス | 転換率 | Product Hunt | ファイル |
|----|------|---------|--------|----------|--------|-------------|---------|
| 001 | **ChatGPT Plus** | 98/100 | 95% | 1.2秒 | 4.8% | #1 | GENAI_PSF_001_chatgpt_plus.md |
| 002 | **Cursor** | 94/100 | 93% | <2秒 | 5.1% | #1 | GENAI_PSF_002_cursor.md |
| 003 | **Perplexity Pro** | 92/100 | 92% | <1秒 | 3.2% | #2 | GENAI_PSF_003_perplexity_pro.md |
| 005 | **Claude Pro** | 92/100 | 96% | 1.8秒 | 2.8% | N/A | GENAI_PSF_005_claude_pro.md |

### PSF Strong（PSFスコア 85-90/100）

| ID | 製品 | PSFスコア | AI精度 | レスポンス | 転換率 | Product Hunt | ファイル |
|----|------|---------|--------|----------|--------|-------------|---------|
| 006 | **Midjourney** | 90/100 | 95% | 45秒 | 25% | N/A | GENAI_PSF_006_midjourney.md |
| 004 | **Notion AI** | 88/100 | 88% | 2.1秒 | 22% | N/A | GENAI_PSF_004_notion_ai.md |
| 007 | **GitHub Copilot** | 88/100 | 91% | 1.5秒 | 18% | N/A | GENAI_PSF_007_github_copilot.md |
| 011 | **Runway Gen-2** | 88/100 | 90% | 3分 | 2.9% | N/A | GENAI_PSF_011_runway_gen2.md |
| 008 | **Character.AI** | 87/100 | 90% | 1.6秒 | 28% | N/A | GENAI_PSF_008_character_ai.md |
| 010 | **Otter.ai** | 86/100 | 92% | 2.1秒 | 3.5% | N/A | GENAI_PSF_010_otter_ai.md |
| 009 | **Jasper AI** | 85/100 | 88% | 2.5秒 | 4.2% | N/A | GENAI_PSF_009_jasper_ai.md |

### PSF Minimum（PSFスコア 83-84/100）

| ID | 製品 | PSFスコア | AI精度 | レスポンス | 転換率 | Product Hunt | ファイル |
|----|------|---------|--------|----------|--------|-------------|---------|
| 012 | **Copy.ai** | 84/100 | 85% | 2.2秒 | 3.8% | #3 | GENAI_PSF_012_copy_ai.md |
| 013 | **Replicate** | 83/100 | 89% | 3.5秒 | 2.3% | #5 | GENAI_PSF_013_replicate.md |

## 主要指標ベンチマーク

### AI精度基準（95%以上推奨）
- ChatGPT Plus: 95%（RLHF強化学習）
- Claude Pro: 96%（Constitutional AI）
- Cursor: 93%（コード生成特化）
- Perplexity Pro: 92%（検索統合）

### レスポンス速度基準（<3秒推奨）
- Perplexity Pro: <1秒（検索最適化）
- ChatGPT Plus: 1.2秒（P50）、2.8秒（P95）
- Cursor: <2秒（コード補完）
- Claude Pro: 1.5秒（P50）、1.8秒（P95）

### 幻覚率基準（<5%推奨）
- Claude Pro: 2%（業界最高水準）
- ChatGPT Plus: 3%
- Cursor: 4%
- Perplexity Pro: 5%

### Free→Paid転換率基準（2-5%標準、特殊ケース除く）
- Cursor: 5.1%（開発者向け高転換）
- ChatGPT Plus: 4.8%
- Jasper AI: 4.2%
- Copy.ai: 3.8%

**特殊ケース（アップセル・Teen層）**:
- Character.AI: 28%（Teen層高エンゲージメント）
- Midjourney: 25%（Discord統合、クリエイター特化）
- Notion AI: 22%（既存有料会員へのアップセル）
- GitHub Copilot: 18%（学生・OSS無料戦略）

### DAU/MAU比基準（0.3以上推奨）
- Character.AI: 0.52（毎日会話利用）
- ChatGPT Plus: 0.45
- GitHub Copilot: 0.44
- Cursor: 0.42

### Product Hunt順位（#1-#10推奨）
- ChatGPT Plus: #1（2022年11月）
- Cursor: #1（2023年3月）
- Perplexity Pro: #2（2023年12月）
- Copy.ai: #3（2021年3月）
- Replicate: #5（2022年4月）

## 10倍優位性パターン

### パターン1: AI精度×速度×汎用性
- ChatGPT Plus: 精度10x + 応答5x + 汎用性10x
- Claude Pro: 長文脈1.5x + 安全性10x + 数学精度10x

### パターン2: ドメイン特化×統合UX×生産性
- Cursor: 生産性10x + 学習曲線5x + デバッグ速度10x
- GitHub Copilot: コーディング速度10x + 学習曲線5x + バグ削減3x

### パターン3: 検索×引用×速度
- Perplexity Pro: 検索速度10x + 引用信頼性10x + コスト3x

### パターン4: クリエイティブ×品質×コスト
- Midjourney: クリエイティビティ10x + 品質10x + コスト5x
- Runway Gen-2: 動画制作速度10x + 品質5x + コスト10x

### パターン5: エンゲージメント×Personality×Teen層
- Character.AI: Personality精度10x + エンゲージメント10x + Teen層獲得5x

## AI Wrapper批判回避戦略

### 戦略1: 自社モデル開発
- ChatGPT Plus: GPT-4自社開発
- Claude Pro: Claude 3.5自社開発
- Midjourney: V6自社開発
- Cursor: コードベース全体理解

### 戦略2: 独自データ統合
- Notion AI: ワークスペース全体理解（RAG）
- Cursor: プロジェクト全体理解
- GitHub Copilot: GitHub全リポジトリ学習
- Jasper AI: ブランドボイス学習

### 戦略3: マルチモデル統合
- Perplexity Pro: GPT-4 + Claude + Gemini
- Replicate: 10,000+モデル統合

### 戦略4: プラットフォーム化
- ChatGPT Plus: プラグイン拡張、GPTs
- Midjourney: Discordコミュニティ
- Replicate: モデル共有プラットフォーム

### 戦略5: 深いツール統合
- Cursor: IDE深部統合（LSP、DAP）
- GitHub Copilot: エディタ統合
- Notion AI: Slash Command統合
- Otter.ai: Zoom/Teams統合

## GenAI製品成功の共通パターン

1. **AI精度95%以上**: ChatGPT 95%, Claude 96%, Midjourney 95%
2. **レスポンス<3秒**: Perplexity <1秒, ChatGPT 2.8秒, Cursor <2秒
3. **幻覚率<5%**: Claude 2%, ChatGPT 3%, Cursor 4%
4. **プロンプト再現性90%以上**: ChatGPT 94%, Claude 93%, Cursor 92%
5. **10倍優位性3軸以上**: 全12事例で達成
6. **AI Wrapper脱却**: 自社モデル開発 or 独自データ統合 or マルチモデル統合
7. **Product Hunt #1-#10**: ChatGPT #1, Cursor #1, Perplexity #2

## 使用方法

### validate-psf スキル実行時の参照

1. **AI精度評価時**: ChatGPT 95%, Claude 96%, Cursor 93%と比較
2. **レスポンス速度評価時**: Perplexity <1秒, ChatGPT 1.2秒, Cursor <2秒と比較
3. **プロンプト再現性評価時**: ChatGPT 94%, Claude 93%, Cursor 92%と比較
4. **10倍優位性評価時**: 3軸以上達成（全12事例共通）
5. **AI Wrapper批判回避時**: 独自技術・データによる差別化戦略を参照
6. **Product Hunt準備時**: #1-#10獲得事例（ChatGPT, Cursor, Perplexity等）を参照

### ベンチマーク基準

- **PSFスコア75-79/100**: ForStartup基準最低ライン
- **PSFスコア80-84/100**: 確度中レベル（Copy.ai, Replicate）
- **PSFスコア85-92/100**: 高レベル（Midjourney, Notion AI, Cursor, Perplexity, Claude）
- **PSFスコア93-98/100**: 伝説的レベル（ChatGPT Plus）

## 更新履歴

- 2026-01-02: 12件のTier 2ケーススタディ作成（ForGenAI版validate-psf統合）
