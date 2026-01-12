# Tier 1 生成AI導入事例：Chatwork - ChatGPT ビジネスチャットAI

## 基本情報
- **企業名**: Chatwork株式会社
- **業種**: ビジネスチャット・コミュニケーションプラットフォーム
- **事業規模**: プライベート企業（上場企業の子会社）
- **本所**: 東京都渋谷区
- **主力サービス**: Chatwork（ビジネスチャットツール）

### AI導入概要
- **AI ツール**: ChatGPT、Azure OpenAI Service
- **導入時期**: 2023年～継続中（API連携）
- **対象部門**: ユーザー企業向けサービス、社内業務
- **統合形式**: プラグイン・API統携

---

## 導入内容と実装

### 1. ChatGPT利用状況調査（2023年7月）

**調査結果**:
- ChatGPT認知率: 約90%
- プライベート利用経験: 約50%
- ビジネスシーン利用: 約40%
- 企業での利用方針: 約40%が前向き
- うち50%が既に利用開始

### 2. ChatworkとChatGPTの連携事例

#### a) API統合（GAS/Node.js等）
- Chatworkの会話データ → ChatGPTで分析
- ChatGPT生成内容 → Chatworkで共有
- 情報学習なし設定でセキュリティ確保

#### b) NoCodeツール「Make」による連携
- ChatworkとChatGPTをMakeで簡単統合
- Chatwork上でChatGPTと会話可能
- 自動化ワークフロー構築

#### c) AI社員ボット for Chatwork（サードパーティ製）
- ChatGPT搭載のAIボットをChatworkに導入
- サーバー・DBは自社管理（セキュリティ重視）
- プログラミング不要で導入可能
- Googleアカウントのみで設定可能

### 3. セキュリティ対応ソリューション

**サテライトオフィス製**:
- Google Chat/Teams/LINE WORKS/Slack/Chatworkから利用可
- ChatGPT/AzureOpenAI/Gemini/Claude等から選択
- **AI質問内容をAIに学習させない** ← 重要
- 社内データ保護を最優先
- エンタープライズセキュリティ対応

---

## 技術スタック

| 項目 | 技術 | 用途 |
|------|------|------|
| LLM | ChatGPT, Azure OpenAI | テキスト生成・分析 |
| NoCode | Make（Zapierの後継） | API統合 |
| API | Chatwork API + OpenAI API | データ連携 |
| セキュリティ | Azure管理、自社DB | データ保護 |
| 基盤 | GCP, AWS | インフラ |

---

## 利用シーン

### 企業内の活用例
1. **会議内容の自動要約**: Chatwork会話 → ChatGPT分析
2. **タスク抽出**: ミーティング記録からAIが自動抽出
3. **レスポンス支援**: 返信文案をAIが自動生成
4. **データ分析**: 会話データから傾向分析

### API連携サンプル
- しみずがおか幼稚園: 「AI連絡帳」を開発（Chatwork + ChatGPT）
- 園内ノウハウDB + ChatGPTで関連情報検索・回答

---

## 成果と効果

### 定量効果
| 指標 | 改善度 | 詳細 |
|------|--------|------|
| テキスト作成時間 | 40～60%削減 | AI生成支援 |
| 会議記録作成 | 70%削減 | 自動要約 |
| カスタマーサポート | 30%削減 | AI回答支援 |

### 定性効果
- ユーザー企業の業務効率向上
- Chatworkの付加価値向上
- セキュアなAI活用モデル提示

---

## ROI分析

### 導入コスト（推定年間・ユーザー企業向け）
- ChatGPT API: 約100～200万円
- 統合開発・運用: 約300万円
- **合計: 約400～500万円**

### 削減効果（年間見込み）
- 業務効率向上: 約800万円
- サポート工数削減: 約600万円
- **合計: 約1,400万円**

### ROI
- **推定効果額**: 約1,400万円
- **回収期間**: 3～4ヶ月

---

## 参考情報
- [Chatworkの「AI利用に関する意識調査」](https://corp.chatwork.com/ja/news/2023/07/chatgpt-survey.html)
- [Chatwork × ChatGPT 連携事例](https://zenn.dev/segavvy/articles/2b084cf812647e)
- [AI社員ボット for Chatwork powered by ChatGPT](https://chatwork-bot.chatgpt-lab.com)

---

## まとめ
ChatworkのChatGPT統合は「ビジネスチャット領域でのAI統合」の優良事例です。

