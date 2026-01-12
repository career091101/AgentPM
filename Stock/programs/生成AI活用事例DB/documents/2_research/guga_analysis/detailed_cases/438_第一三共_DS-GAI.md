# 事例調査：第一三共（製薬業界）

## 1. 基本情報

| 項目 | 内容 | ソース |
|------|------|--------|
| 企業名 | 第一三共株式会社 | [公式サイト](https://www.daiichisankyo.co.jp/) |
| 業界 | 製薬 |  |
| 本社所在地 | 東京都中央区 |  |
| 協業先 | Microsoft（Azure OpenAI）、アバナード、AWS、エクサウィザーズ、FRONTEO |  |
| 公表日 | 2024年4月〜（継続発表） |  |

## 2. AI導入サマリー

| 項目 | 内容 |
|------|------|
| AIツール名 | DS-GAI（ディーエス・ガイ）、Amazon Bedrock、SageMaker |
| ベンダー | Microsoft（Azure OpenAI）、アバナード、AWS |
| 導入時期 | 2024年4月〜 |
| 対象範囲 | 国内グループ会社全従業員約9,300人 |
| 主要技術 | 生成AI、Azure OpenAI、Amazon Bedrock、AIエージェント |

## 3. 定量的効果

| 指標 | 数値 | 備考 |
|------|------|---------:|
| 対象従業員 | 約9,300人 | 国内グループ全社 |
| 初期開発期間 | 約1カ月 | 本番リリースまで |
| 機能拡張期間 | 半年間 | フェーズ2 |

## 4. 導入背景・課題

- 全社的な生成AI活用の推進
- 業務効率化の要請
- 創薬研究プロセスの効率化
- AIフレンドリーな企業文化醸成

## 5. ソリューション詳細

### DS-GAI（2024年4月〜）
- **Azure OpenAI Service活用**
- アバナードが開発・導入支援
- 約1カ月で本番リリース完了

**段階的機能拡張**:
- リリース当初: シンプルなAI対話インターフェース
- 2024年10月: 第一三共仕様にリニューアル
- 2024年11月: GPT-4実装
- 2024年12月: 社内ドキュメントアップロード・解析機能
- 2025年1月: 画像生成機能（マルチモーダル対応）
- 2025年2月: 社内データセット解析、Code Interpreter機能

**開発アプローチ**:
- フェーズ1（1ヶ月）: 基本機能の全社リリース
- フェーズ2（半年間）: 次々と機能拡張

### AI創薬基盤（AWS協業）
- **AIエージェント統合型創薬基盤**
- Cloud Center of Excellence（CCoE）設置（2023年）

**技術構成**:
- Amazon SageMaker Unified Studio
- データメッシュアーキテクチャ
- Amazon Bedrock（AIエージェント開発）

**進展**:
- 2024年: セルフサービス方式でAWS基盤を研究利用可能に

### エクサウィザーズ協業（2019年〜）
- **データ駆動型創薬共同開発**
- 2023年からヒット化合物創出プロジェクト

**成果**:
- 難易度の高い標的タンパク質のヒット化合物を短期同定

### FRONTEO協業（2024年11月）
- **Drug Discovery AI Factory（DDAIF）活用**
- 毒性試験データベース・報告書テキスト解析

## 6. 導入プロセス

| フェーズ | 時期 | 内容 |
|---------|------|------|
| エクサウィザーズ協業開始 | 2019年 | データ駆動型創薬 |
| CCoE設置 | 2023年 | クラウド推進体制 |
| DS-GAIリリース | 2024年4月 | 約1カ月で本番化 |
| AWS基盤整備 | 2024年 | セルフサービス化 |
| GPT-4実装 | 2024年11月 | DS-GAI機能拡張 |
| FRONTEO協業 | 2024年11月 | DDAIF活用開始 |
| マルチモーダル対応 | 2025年1月 | 画像生成機能追加 |

## 7. 成功要因分析

| 要因 | 詳細 |
|------|------|
| アジャイル開発 | 約1カ月で本番リリース |
| 継続的機能拡張 | 週次ペースで機能リリース |
| パートナー協業 | アバナード、AWS、エクサウィザーズ等 |
| CCoE設置 | クラウド推進の専門組織 |

## 8. 課題・対策

| 課題 | 対策 |
|------|------|
| 迅速な導入要請 | アジャイル開発で1カ月リリース |
| 機能拡充ニーズ | 週次ペースでの継続的改善 |
| 創薬研究効率化 | AIエージェント統合型基盤構築 |

## 9. 今後の展開

- DS-GAIの機能継続拡張
- AIエージェント統合型創薬基盤の本格稼働
- データメッシュアーキテクチャの完成
- Tokyo-1プロジェクトでの協業拡大

## 10. 他社への示唆

1. **約9,300人対象のDS-GAIを約1カ月で本番リリース**: アジャイル開発と継続的機能拡張（週次リリース）の組み合わせ
2. **フェーズ1（1カ月）→フェーズ2（半年）の段階的展開**: シンプルな対話から画像生成・データ解析まで機能拡充
3. **AWS/Azure/エクサウィザーズ等マルチパートナー協業**: 創薬AI、全社生成AI、毒性解析それぞれに最適パートナー選定

## 11. ファクトチェック結果

| 項目 | 判定 | ソース |
|------|------|--------|
| DS-GAI約1カ月導入 | ✅ PASS | [日経クロステック](https://xtech.nikkei.com/atcl/nxt/news/24/00531/) |
| Azure OpenAI採用 | ✅ PASS | [Microsoft事例](https://www.microsoft.com/ja-jp/customers/story/1782137615034628342-daiichisankyo-azure-openai-service-pharmaceuticals-ja-japan) |
| AWS AIエージェント基盤 | ✅ PASS | [AWSブログ](https://aws.amazon.com/jp/blogs/news/daiichi-sankyo-ai-agent-integrated-drug-discovery/) |

## 12. 参考リンク

- [第一三共公式](https://www.daiichisankyo.co.jp/)
- [DS-GAI導入（日経クロステック）](https://xtech.nikkei.com/atcl/nxt/news/24/00531/)
- [Microsoft事例](https://www.microsoft.com/ja-jp/customers/story/1782137615034628342-daiichisankyo-azure-openai-service-pharmaceuticals-ja-japan)
- [アバナード事例](https://www.avanade.com/ja-jp/insights/clients/daiichisankyo-generative-ai)
- [AWS創薬基盤](https://aws.amazon.com/jp/blogs/news/daiichi-sankyo-ai-agent-integrated-drug-discovery/)

---
作成日: 2026-01-08
データソース: WebSearch, 第一三共公式発表
Phase: 1（12セクション詳細版）
