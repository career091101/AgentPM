# DeNA AI活用100本ノック - データセット

## 概要

DeNA社員による生成AI活用事例を100件収集した構造化データセット。

**公開日**: 2025年12月23日
**公式URL**: https://fullswing.dena.com/pdf/AI_100tips_slide.pdf

## ファイル構成

### dena_100knock_raw.json
完全な100件のAI活用事例を含むメインデータセット。

**スキーマ**:
```json
{
  "case_id": "dena_100knock_001",
  "number": 1,
  "title": "事例タイトル",
  "job_category": "エンジニア|ビジネス職|クリエイター|全職種",
  "category": "カテゴリ分類",
  "difficulty": "★☆☆|★★☆|★★★",
  "what": "解決したい課題",
  "how": "AI活用による解決策",
  "result": "得られた成果",
  "voice": "利用者の声",
  "ai_tool": "使用AIツール",
  "time_savings": "時間削減効果",
  "quality_improvement": "品質向上効果"
}
```

## データ特性

### 職種別分類
- **エンジニア職**: 32件（32%）
  - 開発・コーディング
  - テスト自動化
  - インフラ構築

- **ビジネス職**: 40件（40%）
  - 業務自動化
  - 資料・ドキュメント作成
  - データ分析
  - リサーチ

- **クリエイター職**: 18件（18%）
  - 画像生成
  - UI/UXデザイン
  - コンテンツ制作

- **全職種対応**: 10件（10%）
  - 情報収集
  - ナレッジ共有
  - 業務自動化

### カテゴリ別分類
1. **情報収集・リサーチ** (12件)
   - NotebookLM、Gemini Deep Research活用

2. **資料・ドキュメント作成** (15件)
   - Gemini Canvas、ChatGPT活用

3. **開発・コーディング** (18件)
   - GitHub Copilot、Cursor活用

4. **学習・ナレッジ共有** (10件)
   - NotebookLM、Gemini活用

5. **業務自動化** (20件)
   - GAS、Gemini CLI活用

6. **データ分析** (10件)
   - Gemini Deep Research、NotebookLM活用

7. **クリエイティブ** (10件)
   - Adobe Firefly、Figma活用

8. **その他** (5件)

### 使用されたAIツール（上位15）
1. **Gemini** - 30件以上
2. **NotebookLM** - 15件以上
3. **GitHub Copilot** - 15件以上
4. **ChatGPT** - 12件以上
5. **Claude** - 8件以上
6. **Cursor** - 12件以上
7. **Adobe Firefly** - 8件以上
8. **Google Apps Script** - 8件以上
9. **Gemini Deep Research** - 5件以上
10. **Gemini Canvas** - 8件以上
11. **Claude Code** - 3件以上
12. **Google Meet** - 3件以上
13. **Figma** - 4件以上
14. **JIRA** - 2件以上
15. **その他** - 複数

## 時間削減効果

- **平均削減率**: 73%
- **最大削減**: 100%削減（完全自動化）
- **最小削減**: 40-50%削減（補助効果）

**削減効果別集計**:
- 80%以上削減: 45件
- 60-79%削減: 35件
- 40-59%削減: 15件
- 明記なし: 5件

## 品質向上効果

主要な品質向上の形態:
1. **誤字脱字ゼロ化** - 校正・レビュー自動化
2. **品質向上** - AI による高品質補完
3. **精度向上** - 分析・検出精度の改善
4. **網羅性向上** - 漏れのない検査・分析
5. **視点の多面化** - 多角的な分析実施
6. **記録の完全性** - 漏れのない記録化

## データ収集方法

複数の情報源から集約:

1. **DeNA公式スライド**
   - https://fullswing.dena.com/pdf/AI_100tips_slide.pdf
   - https://downloads.ctfassets.net/...

2. **分析記事・ドキュメント化サイト**
   - [DeNA AI活用100本ノック事例集](https://dena-100-ai.akirafunakoshi.com/)
   - [DeNA AI活用100本ノック全解析](https://gai.workstyle-evolution.co.jp/2025/12/31/dena-ai-100-use-cases-systematic-classification-enterprise-implementation-guide/)
   - [AI速報ドットコム](https://aisokuho.com/2025/12/25/dena-employees-100-ai-utilization-slides-released/)
   - [IT中小企業診断士村上知也](https://london3.jp/2025/12/dena-ai-100/)

3. **メディア報道**
   - INTERNET Watch
   - ITmedia
   - Note.com 記事群
   - その他複数の報道メディア

## データ品質

### 完全性
- **100%**: 全100件を収集
- **詳細度**: ケースにより異なる
  - 詳細記載: 約60件
  - 部分記載: 約30件
  - 簡潔記載: 約10件

### 正確性
- **情報源**: 複数の独立した情報源から相互検証
- **信頼度**: 高（DeNA公式資料と複数の分析記事の一貫性あり）

### 更新頻度
- **初版作成日**: 2026年1月8日
- **基準日**: 2025年12月23日（DeNA公開日）

## 利用ガイド

### クエリ例

```python
import json

with open('dena_100knock_raw.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# エンジニア向け事例のみ抽出
engineer_cases = [c for c in data['cases']
                  if 'エンジニア' in c['job_category']]

# 時間削減効果が大きい事例をランキング
high_impact = sorted(data['cases'],
                     key=lambda x: x.get('time_savings', '').count('%'),
                     reverse=True)[:10]

# 特定のAIツール活用例を検索
gemini_cases = [c for c in data['cases']
                if 'Gemini' in c['ai_tool']]
```

### フィルタリング条件

- **職種**: job_category
- **カテゴリ**: category
- **難易度**: difficulty
- **AIツール**: ai_tool
- **時間削減効果**: time_savings の %削減率

## 関連リソース

- [CLAUDE.md](../../../CLAUDE.md) - プロジェクト基本ルール
- [PMBOKワークフロー](../../../docs/ai/pmbok_workflow.md)
- [ResearchフェーズWBS](../../README.md)

## ライセンス

このデータセットはDeNA公開の「AI活用100本ノック」から集約したもの。
- **原著作権**: DeNA株式会社
- **公開日**: 2025年12月23日
- **配布形式**: 無料（ユーザー登録不要）

## 更新履歴

| 日付 | 版 | 変更内容 |
|------|-----|---------|
| 2026-01-08 | 1.0 | 初版作成（100件全収集） |

## 問い合わせ

データに関する質問や追加情報は、以下の情報源にご確認ください:

- DeNA公式: https://fullswing.dena.com/
- Xアカウント: @DeNA_fullswing
- ドキュメント化サイト: https://dena-100-ai.akirafunakoshi.com/
