# LinkedIn投稿用画像生成スキル

LinkedIn投稿の本文から、高エンゲージメント仕様のOGP画像を自動生成します。

## クイックスタート

```bash
# スキル実行
/generate-linkedin-image
```

または

```bash
# 直接実行
./.claude/skills/generate-linkedin-image/run.sh
```

## 必要な準備

### 1. APIキー取得

1. [Google AI Studio](https://aistudio.google.com/apikey) にアクセス
2. 「Get API key」をクリック
3. APIキーをコピー

### 2. 環境変数設定

```bash
export GOOGLE_GEMINI_API_KEY='your-api-key-here'
```

永続化する場合:

```bash
echo 'export GOOGLE_GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### 3. 依存ライブラリインストール

```bash
pip install google-genai pillow
```

## 使い方

### サンプルプロンプト使用

スキルを実行すると、以下の選択肢が表示されます:

```
📋 利用可能なサンプルプロンプト:
  1. AI BPO（LayerX福島氏）
  2. AGI到来予測（Google DeepMind）
  3. Claude Opus 4.5（5時間業務）
  4. AI開発工数80%削減（トランスコスモス）
  5. カスタムプロンプトを入力

選択してください (1-5): 1
```

### カスタムプロンプト使用

```
選択してください (1-5): 5

📝 カスタムプロンプトを入力してください:
> [LinkedIn投稿の本文をペースト]
```

## 生成される画像

### 仕様

- **サイズ**: 1080×1080px（正方形）
- **形式**: PNG
- **ファイルサイズ**: 通常1-2MB（5MB以下）
- **保存先**: `Stock/programs/副業/projects/SNS/output/linkedin_images/`

### 特徴

1. **フォトリアル写真**
   - 映画的ドキュメンタリースタイル
   - 8K UHD相当の高品質
   - 浅い被写界深度（背景ボケ）

2. **断定型キャッチコピー**
   - 40-60文字（2-3行）
   - 具体的数値を含む
   - 企業名・人名で信頼性向上

3. **最適化レイアウト**
   - スクリム効果（黒→透明グラデーション）
   - WCAG 2.1 AA基準（コントラスト比4.5:1以上）
   - モバイル可読性重視

## 期待される効果

- ✅ エンゲージメント率: **1.02% → 3.0%以上**（約3倍）
- ✅ 生成時間: **5分以内**
- ✅ 訴求力: **断定型+数値で強化**

## 根拠データ

### ワークスペース分析（47投稿）

| メトリクス | 改善内容 |
|-----------|---------|
| 断定型表現 | 2.1% → 100%（自動化） |
| 数値データ | 平均3.8個以上を抽出 |
| 企業名 | 平均1.2社以上を抽出 |

### Web調査（2026年版）

- 正方形画像: 30%高いエンゲージメント
- テキスト最小化: 画像の30%以下
- モバイル最適化: 必須

## トラブルシューティング

### APIキーエラー

```bash
export GOOGLE_GEMINI_API_KEY='your-api-key-here'
source ~/.zshrc
```

### ライブラリエラー

```bash
pip install google-genai pillow --upgrade
```

## 詳細ドキュメント

- [SKILL.md](./SKILL.md) - 完全な仕様書
- [skill.json](./skill.json) - メタデータ

## コスト

- **NanoBananaPro API**: 約$0.13/枚（1K解像度）
- **月間100枚**: 約$13

## 制約事項

- 実在人物の顔・肖像は生成されません（肖像権保護）
- 実在企業のロゴマークは生成されません（商標権保護）

---

**バージョン**: 1.0.0
**作成日**: 2026-01-06
