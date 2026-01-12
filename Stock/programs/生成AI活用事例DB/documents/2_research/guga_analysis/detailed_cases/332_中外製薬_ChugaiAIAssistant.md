# 事例調査：中外製薬（製薬業界）

## 1. 基本情報

| 項目 | 内容 | ソース |
|------|------|--------|
| 企業名 | 中外製薬株式会社 | [公式サイト](https://www.chugai-pharm.co.jp/) |
| 業界 | 製薬・医薬品 |  |
| 本社所在地 | 東京都中央区 |  |
| 協業先 | AWS、Preferred Networks、Google Cloud、New Relic |  |
| 公表日 | 2024年（継続発表） |  |

## 2. AI導入サマリー

| 項目 | 内容 |
|------|------|
| AIツール名 | Chugai AI Assistant、創薬AI |
| ベンダー | 自社開発（AWS協働） |
| 導入時期 | 2024年5月全社リリース |
| 対象範囲 | 全社員5,000人以上 |
| 主要技術 | RAG、マルチLLM、機械学習 |

## 3. 定量的効果

| 指標 | 数値 | 備考 |
|------|------|---------:|
| 利用社員 | 5,000人以上 | 全社展開 |
| 毎日利用 | 1,000〜1,500人 | デイリーアクティブ |
| MAU | 約3,500人 | Monthly Active Users |
| ピーク利用 | 180万トークン/時 | 最大負荷 |
| 期間短縮期待 | 13年→9年 | 創薬期間4年短縮 |
| 費用削減期待 | 約640億円 | 1,200億→560億円 |
| 成功確率 | 10倍向上 | 0.004%→0.04% |
| INNOVATION DAY | 3,000人以上 | 2024年イベント参加 |

## 4. 導入背景・課題

- 創薬プロジェクト数の拡大ニーズ
- 個々の創薬開発の短期化
- 社内文書検索の効率化
- 全社員がAIを活用できる環境整備

## 5. ソリューション詳細

### Chugai AI Assistant
- **2024年5月全社リリースの対話型生成AIアシスタント**
- AWSとのアジャイル協働開発

**特徴**:
- RAG（検索拡張生成）構成
- 社内文書検索機能
- マルチLLM対応

**対応LLM**:
- Amazon Bedrock Claude3
- Azure OpenAI GPT-4/GPT-4o
- Google Gemini Pro
- MedLM（医療特化）

### RAG SOP検索システム
- **2024年3月開発開始**
- 11月からChugai AI Assistantに統合

**機能**:
- SOPドキュメント検索
- 社内固有情報の正確な回答

### 創薬AI
- **疾患領域ターゲット探索・分子設計**
- PFN連携による深層学習活用

**機能**:
- 大量データ解析
- 最適新規分子配列の自動生成
- 抗体構造設計の効率化・高速化
- 中分子創薬への応用展開

### オブザーバビリティ基盤
- **New Relic採用**
- 2024年9月発表

## 6. 導入プロセス

| フェーズ | 時期 | 内容 |
|---------|------|------|
| PFN連携開始 | 継続中 | 創薬AI共同開発 |
| RAG開発開始 | 2024年3月 | SOP検索システム |
| AI Assistant全社リリース | 2024年5月 | 5,000人以上利用開始 |
| New Relic採用 | 2024年9月 | 可観測性基盤 |
| RAG統合 | 2024年11月 | SOP検索機能追加 |
| INNOVATION DAY | 2024年11月 | 3,000人以上参加 |

## 7. 成功要因分析

| 要因 | 詳細 |
|------|------|
| マルチクラウド | AWS/Azure/Google複数活用 |
| マルチLLM | 用途に応じたモデル選択 |
| アジャイル開発 | AWSとの協働で迅速更新 |
| 全社展開 | 5,000人以上が利用可能 |

## 8. 課題・対策

| 課題 | 対策 |
|------|------|
| 創薬期間13年 | AIで4年短縮目標 |
| 高額開発費 | 640億円削減期待 |
| 低成功確率 | AI活用で10倍向上 |
| 社内検索効率 | RAGシステム構築 |

## 9. 今後の展開

- 創薬AI活用のさらなる拡大
- Chugai AI Assistantの機能拡充
- 量子コンピューティング研究
- 個別化医療への応用

## 10. 他社への示唆

1. **全社5,000人展開**: 生成AIを全社員が利用可能な環境を短期構築
2. **マルチLLM**: Claude/GPT-4/Gemini/MedLM使い分けで最適化
3. **創薬効果試算**: 期間4年短縮・費用640億円削減・成功率10倍の定量目標

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|--------|
| 5,000人利用 | ✅ PASS | [IT Leaders](https://it.impress.co.jp/articles/-/27132) |
| 4年短縮効果 | ✅ PASS | [IT Leaders](https://it.impress.co.jp/articles/-/27132) |
| New Relic採用 | ✅ PASS | [New Relic](https://newrelic.com/jp/press-release/20240903) |

## 12. 参考リンク

- [中外製薬公式](https://www.chugai-pharm.co.jp/)
- [CHUGAI DIGITAL](https://www.chugai-pharm.co.jp/profile/digital/)
- [中外製薬note](https://note.chugai-pharm.co.jp/)
- [Google Cloud事例](https://cloud.google.com/blog/ja/topics/customers/chugai-pharm-generating-ai-to-drive-operational-efficiency-and-value-creation)

---
作成日: 2026-01-08
データソース: WebSearch, 中外製薬公式発表
Phase: 1（12セクション詳細版）
