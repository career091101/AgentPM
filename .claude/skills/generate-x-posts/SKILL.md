---
name: generate-x-posts
description: |
  X（旧Twitter）投稿を自動生成するスキル。
  **デフォルトはスレッド形式**（インプレッション+63%、エンゲージメント+54%）。
  バズ構文84パターン、A/Bテスト、シャドウバン回避、Late API投稿。
trigger_keywords:
  - "X投稿生成"
  - "ツイート作成"
  - "Xスレッド作成"
stage: Development
dependencies:
  - sns-automation
priority: P1
model: claude-opus-4-5-20251101  # Opus 4.5 (2026年1月時点の最新モデル)
thinking: true
context_optimization:
  external_files:
    - x_patterns_detailed.md
    - x_config.json
  estimated_reduction: 70%
---

# X投稿生成スキル（generate-x-posts）

## 概要

このスキルは、X（旧Twitter）向けの高エンゲージメント投稿を自動生成し、Late API経由で予約投稿します。

### 主要機能

1. **スレッド形式がデフォルト**（v0.4.1で変更）
   - 根拠: algorithm.md（486-505行目）によるとスレッドは単一ツイート比較で：
     - インプレッション +63%
     - エンゲージメント +54%
     - フォロワー成長率 3.2倍
   - 最適スレッド数: 5-10ツイート（最適7ツイート）
   - 単一ツイートは`format: "single"`で明示的に指定した場合のみ

2. **280半角文字制限対応**（日本語140文字）
   - Unicode正規化による正確な文字数カウント
   - 半角・全角文字の区別
   - 絵文字・URL考慮

3. **バズ構文84パターン完全版**（Phase 4完了）
   - 実証済みフック文言84パターン
   - カテゴリ別最適化（有益性強調、権威性、逆張り、感情型等10カテゴリ）

4. **Late API自動投稿**
   - スレッド投稿（デフォルト）
   - 単一ツイート投稿（例外ケース）
   - エラーハンドリング＋Markdownフォールバック

5. **エンゲージメント予測**（Phase 3完了）
   - X公式アルゴリズム実装（Reply +13.5, RT +1.0, Like +0.5）
   - Recency factor（半減期360分）
   - Premium優遇（3.0倍平均）

6. **A/Bテスト**（Phase 4完了）
   - 2パターン生成＋7観点比較
   - 勝ちパターンの自動選択

7. **シャドウバン回避**（Phase 4完了）
   - 投稿間隔監視（1時間5ツイート、1日50ツイート制限）
   - 4段階警告システム

8. **最適投稿時刻推薦**（Phase 4完了）
   - 履歴分析による時間帯推薦
   - 信頼性評価（サンプル数ベース）

### 制約事項

- **文字数**: 280半角文字（日本語140文字）厳格
- **ハッシュタグ**: 一切使用しない（Xのアルゴリズムで不要、かつSNS横断使用を避けるため）
- **トーン**: カジュアル・衝撃型
- **投稿間隔**: シャドウバン回避のため1時間5ツイート以内
- **エンゲージメント指標除外**: 他のSNS投稿のいいね数・リツイート数・ビュー数・インプレッション数は記載しない（スパム判定回避、独立性確保）

---

## 入力仕様

### 必須パラメータ

| パラメータ | 型 | 説明 | 例 |
|-----------|---|------|---|
| `input_type` | string | 入力タイプ | `"topic"`, `"article_url"`, `"keyword"` |
| `input_value` | string | 入力値 | トピック文、URL、キーワード |
| `account_id` | string | XアカウントID | Late API設定から取得 |

### オプションパラメータ

| パラメータ | 型 | デフォルト | 説明 |
|-----------|---|----------|------|
| `scheduled_for` | string | `null` | 予約投稿時刻（ISO 8601形式） |
| `tone` | string | `"casual"` | トーン（`"casual"`, `"professional"`, `"humorous"`） |
| `format` | string | `"thread"` | フォーマット（`"thread"`, `"single"`） |
| `source_tweet_url` | string | `null` | 元となるX投稿のURL（引用リポスト形式で1ツイート目に追加） |

### 入力タイプ詳細

#### 1. `input_type: "topic"`
```json
{
  "input_type": "topic",
  "input_value": "AI活用で生産性を3倍にする方法",
  "account_id": "xxx"
}
```

#### 2. `input_type: "article_url"`
```json
{
  "input_type": "article_url",
  "input_value": "https://example.com/article",
  "account_id": "xxx"
}
```

#### 3. `input_type`: "keyword"`
```json
{
  "input_type": "keyword",
  "input_value": "ChatGPT プロンプトエンジニアリング",
  "account_id": "xxx"
}
```

#### 4. 引用リポスト形式（`source_tweet_url`指定）
```json
{
  "input_type": "topic",
  "input_value": "OpenAI GPT-5.2の7つの落とし穴について解説",
  "account_id": "xxx",
  "source_tweet_url": "https://x.com/SuguruKun_ai/status/1234567890"
}
```

**効果**:
- 元投稿へのクレジット明示
- 引用元の権威性を活用
- Xの引用ツイートカードが自動表示され、視認性向上
- エンゲージメント率が通常投稿比で約1.3倍向上（algorithm.md データ）

---

## 処理フロー

### STEP 1: コンテンツ準備

#### 1-A. トピック型（`input_type: "topic"`）
LLMが直接推論で以下を実行：
1. トピックを分析し、核心メッセージを抽出
2. 数値データ・固有名詞を特定
3. インパクトキーワードを洗い出し

#### 1-B. URL型（`input_type: "article_url"`）
```markdown
1. WebFetch toolでURLコンテンツ取得
2. LLMが要約（日本語120文字以内）
3. 核心メッセージ抽出
```

#### 1-C. キーワード型（`input_type: "keyword"`）
```markdown
1. WebSearch toolでトレンド情報収集
2. Top 3結果を統合
3. LLMが核心メッセージ作成
```

---

### STEP 2: スレッド生成（デフォルト、format: "thread"）

**重要**: スレッド生成は全てLLMの自然言語理解能力を活用します。スクリプトは使用しません。

**根拠**: X algorithm.md（486-505行目）によると、スレッドは単一ツイートと比較して：
- インプレッション +63%
- エンゲージメント +54%
- フォロワー成長率 3.2倍

**最適スレッド数**: 5-10ツイート（最適7ツイート）

#### 2-1. バズ構文選択

LLMへの指示：
```
1. Read toolで `x_patterns_detailed.md` を読み込み
2. コンテンツのトーンに最適なパターンを3つ選択
   - ビジネス系: 警告型、強調型
   - ライフスタイル系: 感情型、お願い型
   - 副業・稼ぐ系: 実績型、秘密型
3. 最も効果的な1パターンを決定
```

#### 2-2. コンテンツ長の判定

LLMへの指示：
```
1. コンテンツの文字数をカウント
   - 280カウント以下でユーザーが明示的に単一ツイート要求: STEP 2-A（単一ツイート）へ
   - 281-1400カウント: スレッド最適 → 続行
   - 1400カウント超: 警告「長すぎます。要約推奨」

2. デフォルトはスレッド生成（5-10ツイート）
```

#### 2-3. セマンティック分割（LLM自然言語理解）

LLMへの指示：
```
コンテンツを3-5個のツイートに分割する際、以下の優先順位で分割点を選択：

1. **セマンティックブレーク検出**（意味の区切りを最優先）
   - 段落区切り（\n\n）- 最優先
   - 見出し・サブセクション（## や ### で始まる行）
   - リスト項目の区切り
   - 句点（。）による文の終わり
   - 読点（、）- 最終手段（文が長すぎる場合のみ）

2. **各セクションの重要度を評価**
   LLMが以下の基準でスコアリング：
   - 数値データ含有度: +3点/個（例: 「売上3倍」「時間80%削減」）
     - **注意**: ビジネス指標（売上、成長率、削減率など）はOK
     - **禁止**: 他のSNS投稿のエンゲージメント指標（いいね数、リツイート数、ビュー数、インプレッション数）
   - 固有名詞の有無: +2点/個（企業名、人名、製品名）
   - インパクト語彙: +1点/個（「衝撃」「革命」「劇的」など）
   - 具体的事例: +2点（「〇〇の場合」「〇〇さんは」）

   重要度スコアが高いセクションを優先配置

   **禁止事項（エンゲージメント指標の除外）**:
   元のLinkedIn投稿に以下が含まれていても、X投稿には**絶対に含めない**：
   - 「いいね6,349」「リツイート491」「163,736ビュー」「1,124いいね」
   - 「SuguruKun_aiのスレッドが〇〇ビューを記録」
   - その他、他のSNS投稿のエンゲージメント数値

   **理由**: スパム判定回避、X投稿の独立性確保

3. **目標ツイート数（5-10個、最適7個）にグループ化**
   - 根拠: algorithm.md（486-505行目）- 5-10ツイートが最も成功しやすい
   - 1ツイート目: フック + 核心の導入（重要度トップ）
   - 2-N-1ツイート目: 核心内容の展開（重要度順）
   - 最終ツイート: まとめ + CTA

4. **各ツイートの文字数調整**
   - 日本語120-135文字（240-270カウント）に調整
   - 最大140文字（280カウント）厳守
   - 超過時は以下の優先順位で削減:
     a) 修飾語（形容詞・副詞）
     b) 補足説明
     c) 冗長な表現
     d) 重複内容

5. **スレッド番号付与**
   - 各ツイートの先頭に番号を付与: (1/5), (2/5), ..., (5/5)
   - 番号は文字数カウントに含める
```

#### 2-4. スレッド構成の最適化

LLMへの指示：
```
各ツイートの役割を明確化：

1. **1ツイート目（フック + 導入）**
   - バズ構文パターンを使用（x_patterns_detailed.mdから選択）
   - 核心メッセージの予告
   - **ハッシュタグは使用しない**（Xのアルゴリズムで不要）
   - **`source_tweet_url`が指定されている場合**: URLを核心メッセージの直後、CTA（「以下で解説します👇」）の直前に配置（引用リポスト形式）

   **例1: 通常形式（source_tweet_urlなし）**
     ```
     (1/4)

     これあんまり知ってる人少ないんですが

     AI活用で生産性が3倍になる方法、実は5つしかありません。

     以下で解説します👇
     ```

   **例2: 引用リポスト形式（source_tweet_url指定あり）**
     ```
     (1/4)

     これあんまり知ってる人少ないんですが

     AI活用で生産性が3倍になる方法、実は5つしかありません。

     https://x.com/username/status/1234567890

     以下で解説します👇
     ```

   **注意**:
   - URLは「核心メッセージ」と「以下で解説します👇」の間に配置
   - これにより、引用元を明示しつつ、スレッドへの誘導を最後に配置
   - URL追加後も280カウント以内に収まるよう調整
   - URLは23カウントとして計算

2. **中間ツイート（2-N-1番目）**
   - 核心内容を展開
   - 数値データ・具体例を優先
   - 箇条書きで読みやすく
   - 例:
     ```
     (2/4)

     1. タスク自動化（30%削減）
     - 定型業務をChatGPTで自動化
     - 週10時間の時間創出

     2. 情報収集効率化（50%削減）
     - Web記事を3分で要約
     - リサーチ時間が半減
     ```

3. **最終ツイート（N/N番目）**
   - まとめ + 問いかけ終結
   - CTA（行動喚起）を含める
   - 例:
     ```
     (4/4)

     この5つを実践すれば、誰でも生産性3倍は達成可能です。

     あなたはどの方法から試しますか？

     参考になった人はいいねしてね👍
     ```

4. **スレッド全体の一貫性チェック**
   - ストーリーが自然に流れるか
   - 重複内容がないか
   - 各ツイートが独立して読めるか（途中から読んでも理解可能か）
```

#### 2-5. 各ツイートの文字数検証

LLMへの指示：
```
スレッド内の各ツイートに対して、STEP 2-3の文字数カウントを実行：

for each tweet in thread:
  1. Unicode正規化（NFC形式）
  2. 半角・全角・絵文字・URLを区別してカウント
  3. 総カウント数 = (半角 × 1) + (全角 × 2) + (絵文字 × 2) + (URL × 23)
  4. 検証:
     - 280カウント以下: ✅ OK
     - 280カウント超: ❌ NG → 削減して再検証

  5. 全ツイートが280カウント以下になるまで調整を繰り返す
```

---

### STEP 2-A: 単一ツイート生成（format: "single"の場合のみ、例外ケース）

**注意**: 単一ツイートはスレッドと比較してインプレッション-63%、エンゲージメント-54%のため、推奨されません。
ユーザーが明示的に`format: "single"`を指定した場合のみ実行します。

#### 2-A-1. ツイート構成（単一）

LLMへの指示：
```
以下の3部構成でツイートを作成：

1. **フック（1行目）**: バズ構文パターンを使用（x_patterns_detailed.mdから選択）
   - 例: "これあんまり知ってる人少ないんですが"
   - 目的: 最初の1秒で注意を引く

2. **核心内容（2-5行）**: 主要メッセージ
   - 数値データ優先（3つ以上推奨）
   - 固有名詞挿入（企業名、人名）
   - 箇条書き形式（読みやすさ重視）

3. **CTA（最終行）**: 行動喚起
   - 例: "参考になった人はいいねしてね"
   - 控えめ（3日に1回程度使用）
```

#### 2-A-2. 文字数カウント（LLM直接計算）

LLMへの指示：
```
1. テキストのUnicode正規化（NFC形式）を適用

2. 文字種別を区別してカウント:
   - **半角文字（ASCII、英数字、記号）**: 1文字 = 1カウント
   - **全角文字（日本語ひらがな、カタカナ、漢字）**: 1文字 = 2カウント
   - **絵文字**: 1絵文字 = 2カウント
   - **URL**: すべてt.co形式の23カウントに換算

3. 総カウント数を計算:
   - total_count = (半角文字数 × 1) + (全角文字数 × 2) + (絵文字数 × 2) + (URL数 × 23)
   - 最大値: 280カウント（日本語のみの場合は140文字相当）

4. 調整目標:
   - 日本語主体の場合: 135文字以下（270カウント以下）に調整
   - 英語主体の場合: 270文字以下（270カウント以下）に調整
   - 280カウントを超える場合は必ず警告

5. 検証:
   - 280カウントを1でも超えたら投稿失敗となるため厳格にチェック
   - 超過時は文末から削減（CTA → 核心内容 → フックの優先順位）

**注意**: ハッシュタグは追加しない（Xのアルゴリズムで不要、スパム判定リスクあり）
```

---

### STEP 3: バリデーション（LLM直接チェック）

LLMへの指示：
```
以下の11項目の禁止事項をチェック：

1. ❌ 誇大広告（実績の嘘）
2. ❌ 他者誹謗中傷
3. ❌ 差別的表現
4. ❌ 個人情報漏洩
5. ❌ 著作権侵害
6. ❌ スパム行為
7. ❌ 投資助言（無資格）
8. ❌ 医療アドバイス（無資格）
9. ❌ 違法行為助長
10. ❌ 政治的偏向（過度）
11. ❌ 成人向けコンテンツ

違反検出時:
- 該当箇所を指摘
- 修正案を提示
- 再生成して再チェック

全項目クリア後のみSTEP 4へ進む
```

---

### STEP 4: エンゲージメント予測（LLM直接計算）

**重要**: このステップは全てLLMの直接計算で実行します。スクリプトは使用しません。

#### 4-1. ベースER（エンゲージメント率）推定

LLMへの指示：
```
コンテンツ品質から基準エンゲージメント率を推定：

1. **ベースER開始値**: 3.0%

2. **コンテンツ品質による加算**:
   - 数値データ3つ以上含有: +0.5%
     例: 「300万imp」「3倍」「50%削減」

   - 問いかけ終結: +1.0%
     例: 「あなたはどう思いますか？」「どの方法から試しますか？」

   - 衝撃フック（バズ構文100選から）: +0.8%
     x_patterns_detailed.mdから選択したパターンがあれば加算

   - 権威性引用: +0.6%
     例: 「〇〇氏によると」「研究結果では」「データによれば」

   - 具体的事例: +0.4%
     例: 「Aさんの場合」「実際に〇〇したら」

3. **最終ベースER計算**:
   base_er = 3.0% + (該当項目の合計)

   例: 数値データあり(+0.5%) + 問いかけあり(+1.0%) + バズ構文あり(+0.8%)
       = 3.0% + 2.3% = 5.3%
```

#### 4-2. 予測エンゲージメント数の計算

LLMへの指示：
```
1. **Read toolで x_config.json からフォロワー数を取得**
   デフォルト値: 1000（設定がない場合）

2. **予測いいね数**:
   predicted_likes = followers × base_er × 0.5

   例: フォロワー1000人、ベースER 5.3%
       = 1000 × 0.053 × 0.5 = 26.5 ≒ 27いいね

3. **予測リツイート数**:
   predicted_retweets = predicted_likes × 0.15

   例: 27 × 0.15 = 4.05 ≒ 4リツイート

4. **予測リプライ数**:
   predicted_replies = predicted_likes × 0.08

   例: 27 × 0.08 = 2.16 ≒ 2リプライ
```

#### 4-3. X公式アルゴリズムスコア計算

LLMへの指示：
```
GitHub検証済みの公式重み数値を使用：

engagement_score = (replies × 13.5) + (retweets × 1.0) + (likes × 0.5)

**重み数値の意味**:
- Reply（リプライ）: 13.5倍 - 最も価値が高い（会話を生む）
- Retweet（リツイート）: 1.0倍 - 拡散効果
- Like（いいね）: 0.5倍 - 最も軽いエンゲージメント

例: 2リプライ、4リツイート、27いいね
    = (2 × 13.5) + (4 × 1.0) + (27 × 0.5)
    = 27 + 4 + 13.5
    = 44.5
```

#### 4-4. Recency Factor（時間減衰）計算

LLMへの指示：
```
X公式アルゴリズムの時間減衰を計算：

1. **半減期**: 360分（6時間）
   360分後にスコアが半分になる

2. **投稿後経過時間**: 30分（デフォルト想定）
   ※予約投稿の場合は、scheduled_forから計算

3. **Recency factor計算**:
   recency_factor = exp(-elapsed_minutes / 360)

   例: 投稿後30分
       = exp(-30 / 360)
       = exp(-0.0833)
       = 0.920（約92%維持）

   参考値:
   - 30分後: 0.920（92%）
   - 60分後: 0.846（85%）
   - 180分後: 0.606（61%）
   - 360分後: 0.368（37%、半減期）
   - 720分後: 0.135（14%）
```

#### 4-5. Premium優遇計算

LLMへの指示：
```
1. **Read toolで x_config.json からPremium設定を取得**
   デフォルト値: true（Premium加入想定）

2. **Premium multiplier**:
   - Premium加入: 3.0倍（平均値）
     実測値では2-4倍の範囲、中央値3.0倍を使用

   - Premium未加入: 1.0倍

3. **Premiumの効果**:
   - フォロワー外へのリーチが6倍（600 vs 100）
   - アルゴリズムスコアが3倍優遇
   - For Youタイムラインでの露出増加
```

#### 4-6. 時間帯補正

LLMへの指示：
```
投稿時刻（scheduled_for）から時間帯を判定し、補正倍率を適用：

1. **時間帯別補正倍率**:
   - 朝8時-9時: 1.3倍（通勤・始業前の高活動時間）
   - 昼12時-13時: 1.1倍（昼休み）
   - 夜21時-22時: 1.2倍（帰宅後のリラックス時間）
   - その他: 1.0倍（補正なし）

2. **scheduled_forがnullの場合**:
   - 即時投稿と判定
   - 現在時刻で時間帯補正を計算

3. **例**:
   scheduled_for = "2026-01-07T08:00:00+09:00"
   → 朝8時 → time_multiplier = 1.3
```

#### 4-7. 最終スコアとリーチ予測

LLMへの指示：
```
1. **最終エンゲージメントスコア**:
   final_score = engagement_score × recency_factor × premium_multiplier × time_multiplier

   例: 44.5 × 0.920 × 3.0 × 1.3
       = 159.6

2. **推定リーチ（インプレッション数）**:
   estimated_reach = followers × premium_multiplier × time_multiplier × (1 + base_er)

   例: 1000 × 3.0 × 1.3 × (1 + 0.053)
       = 1000 × 3.0 × 1.3 × 1.053
       = 4,107インプレッション

3. **スレッドの場合の追加補正**:
   thread_multiplier = 1.63（63%増加）

   スレッド最終スコア = final_score × thread_multiplier
   スレッド推定リーチ = estimated_reach × thread_multiplier

4. **出力JSON形式**:
   {
     "predicted_likes": 27,
     "predicted_retweets": 4,
     "predicted_replies": 2,
     "base_er": 5.3,
     "engagement_score": 44.5,
     "recency_factor": 0.920,
     "premium_multiplier": 3.0,
     "time_multiplier": 1.3,
     "final_score": 159.6,
     "estimated_reach": 4107,
     "thread_multiplier": 1.0
   }
```

---

### STEP 5: シャドウバン回避（投稿間隔監視・警告）

**目的**: X APIのシャドウバンリスクを回避するため、投稿頻度を監視して警告を発出。

**シャドウバンとは**: Xが過度な投稿をスパムと判定し、投稿がフォロワーのタイムラインに表示されなくなる状態。

#### 5-1. x_config.jsonから投稿履歴読み込み

LLMがRead toolで以下を取得：

```json
{
  "shadowban_prevention": {
    "hourly_limit": 5,
    "daily_limit": 50,
    "recent_posts": [
      {"timestamp": "2026-01-06T14:00:00+09:00", "post_id": "xxx"},
      {"timestamp": "2026-01-06T13:30:00+09:00", "post_id": "yyy"},
      {"timestamp": "2026-01-06T13:00:00+09:00", "post_id": "zzz"}
    ]
  }
}
```

#### 5-2. 投稿間隔チェック（LLM直接計算）

LLMが以下を実行：

```markdown
1. **現在時刻取得**:
   current_time = "2026-01-06T14:30:00+09:00"

2. **過去1時間の投稿数カウント**:
   recent_posts内で、current_timeから60分以内の投稿を抽出
   hourly_count = 3（例）

3. **過去24時間の投稿数カウント**:
   recent_posts内で、current_timeから24時間以内の投稿を抽出
   daily_count = 12（例）

4. **制限値との比較**:
   - hourly_count >= hourly_limit（5）？ → 警告レベル1
   - daily_count >= daily_limit（50）？ → 警告レベル2
```

#### 5-3. 警告レベル判定

LLMが以下の3段階で判定：

**警告レベル**:
- **レベル0（安全）**: hourly_count < 3 かつ daily_count < 30
  - メッセージ: 「投稿間隔は安全です。」
  - アクション: そのまま投稿継続

- **レベル1（注意）**: hourly_count >= 3 かつ hourly_count < 5
  - メッセージ: 「⚠️ 過去1時間に3回投稿済み。あと2回で1時間制限（5回）に達します。」
  - アクション: 投稿は許可、但し警告表示

- **レベル2（危険）**: hourly_count >= 5 または daily_count >= 40
  - メッセージ: 「🚫 シャドウバンリスク高！過去1時間に5回以上投稿済み。投稿を1時間延期することを強く推奨します。」
  - アクション: ユーザーに延期を推薦（強制停止はしない）

- **レベル3（緊急停止）**: daily_count >= 50
  - メッセージ: 「🛑 1日の投稿上限（50回）に達しました。24時間経過後に再投稿してください。」
  - アクション: Late API投稿をスキップ、Markdownフォールバックのみ

#### 5-4. 推奨待機時間計算（LLM直接計算）

レベル2の場合、LLMが最適な待機時間を計算：

```markdown
1. **最新投稿からの経過時間**:
   latest_post_time = recent_posts[0]["timestamp"]
   elapsed_minutes = (current_time - latest_post_time) / 60

2. **推奨待機時間**:
   recommended_wait = 60 - elapsed_minutes

   例: 最新投稿が30分前 → あと30分待機推奨

3. **Late API予約投稿時刻提案**:
   scheduled_time = current_time + recommended_wait

   例: 現在14:30、最新投稿14:00 → 15:00に予約投稿を提案
```

#### 5-5. x_config.json更新（Edit tool）

投稿実行後、LLMがEdit toolで履歴を更新：

```json
{
  "shadowban_prevention": {
    "recent_posts": [
      {"timestamp": "2026-01-06T14:30:00+09:00", "post_id": "new_post_id"},
      {"timestamp": "2026-01-06T14:00:00+09:00", "post_id": "xxx"},
      {"timestamp": "2026-01-06T13:30:00+09:00", "post_id": "yyy"}
      // 24時間以上前の投稿は削除
    ]
  }
}
```

#### 5-6. 出力例

```json
{
  "shadowban_check": {
    "status": "warning_level_1",
    "hourly_count": 3,
    "daily_count": 12,
    "hourly_limit": 5,
    "daily_limit": 50,
    "message": "⚠️ 過去1時間に3回投稿済み。あと2回で1時間制限（5回）に達します。",
    "recommended_action": "投稿可能ですが、投稿間隔を広げることを推奨します。",
    "next_safe_posting_time": "2026-01-06T15:00:00+09:00"
  }
}
```

---

### STEP 6: A/Bテスト（2パターン生成、LLM比較）

**目的**: 2つの異なるバズ構文パターンでツイートを生成し、LLMがエンゲージメント予測を比較して最適なパターンを選択。

#### 6-1. A/Bテスト実行判定

LLMが以下の条件をチェック：

**A/Bテスト実行条件**:
1. ユーザーが明示的に「A/Bテスト」をリクエスト
2. または、コンテンツが特に重要（週次レポート、新製品発表など）
3. または、前回投稿のER（エンゲージメント率）が目標未達（< 3.0%）

**実行フラグ**: `ab_test_enabled`（デフォルト: false）

#### 6-2. パターンA生成（フック1）

LLMが以下を実行：

```markdown
1. **バズ構文選択**:
   x_patterns_detailed.mdから最適なカテゴリを選択：
   - ビジネス系: カテゴリ1（警告型）、カテゴリ5（デメリット）、カテゴリ7（数字）
   - ライフスタイル系: カテゴリ1（感情型）、カテゴリ9（喜怒哀楽）
   - 副業・稼ぐ系: カテゴリ2（権威性）、カテゴリ7（数字）

2. **パターンA構築**:
   - フック: カテゴリ内からランダム選択（例: 「これあんまり知ってる人少ないんですが」）
   - 本文: コンテンツ核心部分を120-135文字に調整
   - CTA: カテゴリ10から選択（例: 「参考になった人はいいねしてね」）

3. **エンゲージメント予測**:
   STEP 4のロジックを適用してパターンAのスコアを算出
```

出力例:
```
パターンA:
これあんまり知ってる人少ないんですが

AI活用で生産性が3倍になる方法、実は5つしかありません。

①プロンプトテンプレート化
②タスク自動化（API連携）
③コンテキスト最適化
④エージェント分業
⑤継続的学習ループ

詳細はコメント欄で👇

#AI活用 #生産性向上

予測ER: 5.8%、推定リーチ: 4,800インプレッション
```

#### 6-3. パターンB生成（フック2）

LLMが以下を実行：

```markdown
1. **異なるカテゴリから選択**:
   パターンAと異なるカテゴリを選択（多様性確保）

2. **パターンB構築**:
   - フック: 別カテゴリから選択（例: 「批判覚悟で本音を言います」）
   - 本文: 同じ核心内容、異なる表現・順序
   - CTA: 異なるCTA（例: 「いいね/リツイート多いと続き書くね」）

3. **エンゲージメント予測**:
   STEP 4のロジックを適用してパターンBのスコアを算出
```

出力例:
```
パターンB:
批判覚悟で本音を言います

生産性を3倍にする方法、実はAI活用の5つの型だけです。

大半の人がこれを知らずに非効率な使い方をしています。

①テンプレート化
②自動化設計
③コンテキスト管理
④分業設計
⑤改善サイクル

いいね/リツイート多いと続き書くね👇

#AI活用 #生産性向上

予測ER: 6.2%、推定リーチ: 5,100インプレッション
```

#### 6-4. LLM比較分析

LLMが以下の7つの観点で比較：

**比較観点**:
1. **エンゲージメント予測スコア**（X公式アルゴリズム）
2. **推定リーチ**（インプレッション数）
3. **フックの衝撃度**（1-10点）
4. **本文の読みやすさ**（1-10点）
5. **CTAの明確さ**（1-10点）
6. **ハッシュタグ適切性**（1-10点）
7. **文字数最適性**（280半角文字制限への近さ）

LLMの分析出力:
```json
{
  "pattern_a": {
    "engagement_score": 44.5,
    "estimated_reach": 4800,
    "hook_impact": 7,
    "readability": 8,
    "cta_clarity": 6,
    "hashtag_fit": 8,
    "character_optimization": 9,
    "total_score": 88.5
  },
  "pattern_b": {
    "engagement_score": 48.2,
    "estimated_reach": 5100,
    "hook_impact": 9,
    "readability": 7,
    "cta_clarity": 8,
    "hashtag_fit": 8,
    "character_optimization": 9,
    "total_score": 93.2
  },
  "recommendation": "pattern_b",
  "reason": "フックの衝撃度が2点高く、CTAがより明確。予測ERも6.2%で目標（3.5%）を大きく上回る。"
}
```

#### 6-5. 最終選択

LLMが以下を実行：

```markdown
1. **総合スコア比較**:
   total_score = engagement_score + (hook_impact × 5) + (readability × 3) + (cta_clarity × 4) + (hashtag_fit × 2) + character_optimization

2. **推薦パターン決定**:
   - 総合スコアが高い方を推薦
   - スコア差が5点未満の場合は両方提示、ユーザー選択

3. **出力**:
   推薦パターンのみを出力、または両パターンを提示
```

#### 6-6. A/Bテスト結果記録（Phase 4）

x_config.jsonの`pattern_performance`セクションに記録：

```json
{
  "ab_test_history": [
    {
      "test_id": "ab_20260106_001",
      "pattern_a": {
        "category": "category_1_pattern_12",
        "predicted_er": 5.8,
        "total_score": 88.5
      },
      "pattern_b": {
        "category": "category_1_pattern_9",
        "predicted_er": 6.2,
        "total_score": 93.2
      },
      "selected": "pattern_b",
      "actual_er": null,
      "test_date": "2026-01-06T14:30:00+09:00"
    }
  ]
}
```

**重要**: 実際のER（actual_er）は後日Late APIダッシュボードから手動更新。

---

### STEP 6: Late API投稿（スレッド対応、実証済み）

**重要**: このセクションは2026-01-06に実証済みの動作確認済み形式です。

#### 6-A. Late API設定読み込み

LLMがRead toolで以下を取得：

```python
# Stock/programs/副業/projects/SNS/scripts/late_api_post.py から抽出
api_key = config["api_key"]  # Bearer認証トークン
base_url = config["base_url"]  # https://api.late.so/api/v1
account_id = get_account_id("twitter")  # Xアカウント識別子
```

#### 6-B. Late APIスレッド投稿の正しい形式（実証済み）

**成功実績**: 2026-01-06 20:10投稿成功（post_id: `695ceb1e8247cf816ba753b6`）

**参照実装**: `@Stock/programs/副業/projects/SNS/scripts/schedule_x_threads_post.py` (126-141行目)

**正しいペイロード形式**:

```python
{
    'content': tweets[0],  # ← 1ツイート目は必須（トップレベル）
    'scheduledFor': '2026-01-06T20:10:00+09:00',  # ISO 8601形式
    'timezone': 'Asia/Tokyo',
    'platforms': [{
        'platform': 'twitter',
        'accountId': account_id,
        'platformSpecificData': {
            'threadItems': [{'content': tweet} for tweet in tweets[1:]]  # ← 2ツイート目以降
        }
    }],
    'publishNow': False,
    'crosspostingEnabled': False
}
```

**重要ポイント**:
1. **`content`フィールドは必須**: 1ツイート目をトップレベルに配置
2. **`threadItems`は2ツイート目以降**: `platforms[].platformSpecificData.threadItems`配列に格納
3. **各アイテムは`{"content": "text"}`形式**: `{"text": "..."}`ではなく`{"content": "..."}`
4. **`platformSpecificData`は`platforms[]`配列内**: トップレベルではない

#### 6-C. よくあるエラーと解決策（実証済み）

**エラー1: "Content is required for selected platforms"**

❌ **誤った形式** (v3, v5で発生):
```python
{
    "platforms": [{
        "platformSpecificData": {
            "threadItems": [{"content": tweet} for tweet in tweets]  # 全ツイート
        }
    }]
    # contentフィールドがない → エラー
}
```

✅ **正しい形式**:
```python
{
    'content': tweets[0],  # ← 1ツイート目を追加
    'platforms': [{
        'platformSpecificData': {
            'threadItems': [{'content': tweet} for tweet in tweets[1:]]
        }
    }]
}
```

**エラー2: Late APIダッシュボードで2ツイート目以降が表示されない**

❌ **誤った形式** (v4で発生):
```python
"threadItems": [{"text": tweet} for tweet in tweets[1:]]  # ← "text"キーは無効
```

✅ **正しい形式**:
```python
"threadItems": [{"content": tweet} for tweet in tweets[1:]]  # ← "content"キーを使用
```

**エラー3: platformSpecificDataの配置ミス**

❌ **誤った形式** (v2で発生):
```python
{
    "content": tweets[0],
    "platformSpecificData": {  # ← トップレベルに配置（誤り）
        "threadItems": [...]
    },
    "platforms": [{
        "platform": "twitter",
        "accountId": account_id
    }]
}
```

✅ **正しい形式**:
```python
{
    'content': tweets[0],
    'platforms': [{
        'platform': 'twitter',
        'accountId': account_id,
        'platformSpecificData': {  # ← platforms[]内に配置（正解）
            'threadItems': [...]
        }
    }]
}
```

#### 6-D. Python実装例（最小限、実証済み）

LLMが以下のコードを生成（スクリプトファイル作成、単発実行）:

```python
#!/usr/bin/env python3
import sys
import requests
from datetime import datetime
from zoneinfo import ZoneInfo

sys.path.insert(0, '/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/scripts')
from late_api_post import get_account_id, load_config

# ツイート内容（7ツイート例）
tweets = [
    "1ツイート目...",
    "2ツイート目...",
    "3ツイート目...",
    "4ツイート目...",
    "5ツイート目...",
    "6ツイート目...",
    "7ツイート目..."
]

# Late API設定読み込み
config = load_config()
api_key = config["api_key"]
base_url = config["base_url"]
account_id = get_account_id("twitter")

# 予約投稿時刻（ISO 8601）
scheduled_time = datetime(2026, 1, 6, 20, 10, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
scheduled_time_iso = scheduled_time.isoformat()

# リクエストボディ構築（実証済み形式）
request_body = {
    'content': tweets[0],  # 1ツイート目
    'scheduledFor': scheduled_time_iso,
    'timezone': 'Asia/Tokyo',
    'platforms': [{
        'platform': 'twitter',
        'accountId': account_id,
        'platformSpecificData': {
            'threadItems': [{'content': tweet} for tweet in tweets[1:]]  # 2-7ツイート目
        }
    }],
    'publishNow': False,
    'crosspostingEnabled': False
}

# Late API投稿
response = requests.post(
    f"{base_url}/posts",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json=request_body,
    timeout=30
)

if response.status_code in [200, 201]:
    result = response.json()
    post_id = result.get('post', {}).get('_id', result.get('id', 'N/A'))
    print(f"✅ 投稿成功！ 投稿ID: {post_id}")
else:
    print(f"❌ 投稿失敗 ステータスコード: {response.status_code}")
    print(f"レスポンス: {response.text}")
```

#### 6-E. エラーハンドリング

LLMが以下を判定：
```
レスポンスコード別処理:

200/201: ✅ 投稿成功
  → 成功JSONを出力

400: ❌ リクエストエラー
  → 文字数再チェック
  → JSON形式確認
  → 修正して再試行（1回のみ）

401: ❌ 認証エラー
  → APIキー確認を促す
  → Markdownフォールバックへ

429: ❌ レート制限
  → 1時間待機を促す
  → Markdownフォールバックへ

500+: ❌ サーバーエラー
  → Late API障害と判定
  → Markdownフォールバックへ

Timeout: ❌ タイムアウト
  → 3回リトライ（指数バックオフ: 1秒→2秒→4秒）
  → 失敗時Markdownフォールバック
```

---

### STEP 7: シャドウバン回避（投稿間隔監視・警告）

**注意**: このセクションは元のSTEP 5から移動しました（STEP 6追加に伴う番号変更）。

（内容は変更なし、元のSTEP 5の内容をそのまま維持）

---

### STEP 8: A/Bテスト（2パターン生成、LLM比較）

**注意**: このセクションは元のSTEP 6から移動しました（STEP 6追加に伴う番号変更）。

（内容は変更なし、元のSTEP 6の内容をそのまま維持）

---

### STEP 9: 最適投稿時刻推薦（履歴分析）

**目的**: 過去の投稿エンゲージメント履歴を分析して、最もパフォーマンスが高い時間帯を推薦。

#### 8-1. x_config.jsonからエンゲージメント履歴読み込み

LLMがRead toolで以下を取得：

```json
{
  "optimal_posting_times": {
    "weekday": {
      "morning": {
        "time": "08:00-09:00",
        "avg_engagement_rate": 4.2,
        "sample_count": 15
      },
      "noon": {
        "time": "12:00-13:00",
        "avg_engagement_rate": 3.8,
        "sample_count": 20
      },
      "evening": {
        "time": "21:00-22:00",
        "avg_engagement_rate": 5.1,
        "sample_count": 18
      }
    },
    "weekend": {
      "morning": {
        "time": "10:00-11:00",
        "avg_engagement_rate": 3.5,
        "sample_count": 8
      },
      "afternoon": {
        "time": "15:00-16:00",
        "avg_engagement_rate": 4.0,
        "sample_count": 10
      },
      "evening": {
        "time": "20:00-21:00",
        "avg_engagement_rate": 4.8,
        "sample_count": 12
      }
    }
  }
}
```

#### 8-2. 曜日・時間帯判定（LLM直接計算）

LLMが以下を実行：

```markdown
1. **現在時刻取得**:
   current_time = "2026-01-06T14:30:00+09:00"（月曜日）

2. **曜日判定**:
   - 月〜金曜日 → "weekday"
   - 土・日曜日 → "weekend"

3. **時間帯分類**:
   - 07:00-10:00 → "morning"
   - 11:00-14:00 → "noon"（weekdayのみ）
   - 15:00-17:00 → "afternoon"（weekendのみ）
   - 20:00-23:00 → "evening"
```

#### 8-3. 最適時刻推薦（LLM分析）

LLMが以下の3段階で分析：

**ステップ1: 現在の曜日・時間帯のER取得**

```markdown
例: 月曜14:30の場合
- 曜日: weekday
- 時間帯: noon
- avg_engagement_rate: 3.8%
- sample_count: 20
```

**ステップ2: 同曜日カテゴリ内での最適時刻特定**

```markdown
weekday内のすべての時間帯を比較：
- morning: 4.2%（15サンプル）
- noon: 3.8%（20サンプル）
- evening: 5.1%（18サンプル）← 最高ER

**推薦**: weekday evening（21:00-22:00）が5.1%で最適
```

**ステップ3: サンプル数による信頼性評価**

```markdown
サンプル数が少ない場合（< 10）は信頼性が低いため警告：

- sample_count >= 15: 高信頼度（★★★）
- sample_count 10-14: 中信頼度（★★☆）
- sample_count 5-9: 低信頼度（★☆☆）
- sample_count < 5: データ不足（☆☆☆）
```

#### 8-4. Late API予約投稿時刻提案

LLMが以下を実行：

```markdown
1. **最適時刻の中央値を算出**:
   evening: 21:00-22:00 → 中央値 = 21:30

2. **次回最適投稿時刻を計算**:
   - 現在時刻: 2026-01-06T14:30:00
   - 最適時刻: 21:30
   - 次回投稿時刻: 2026-01-06T21:30:00+09:00

3. **Late API scheduledTime設定**:
   "scheduledTime": "2026-01-06T21:30:00+09:00"
```

#### 8-5. 代替案提示（即時投稿vs予約投稿）

LLMが2つのオプションを提示：

**オプションA: 即時投稿（現在時刻）**
```json
{
  "option": "immediate",
  "scheduled_time": "2026-01-06T14:30:00+09:00",
  "expected_er": 3.8,
  "confidence": "★★★（20サンプル）",
  "advantage": "すぐに投稿できる",
  "disadvantage": "ERが最適時刻より1.3%低い"
}
```

**オプションB: 予約投稿（最適時刻）**
```json
{
  "option": "scheduled",
  "scheduled_time": "2026-01-06T21:30:00+09:00",
  "expected_er": 5.1,
  "confidence": "★★★（18サンプル）",
  "advantage": "ERが34%高い（5.1% vs 3.8%）",
  "disadvantage": "投稿まで7時間待機"
}
```

**推薦**: LLMがER差が1.0%以上の場合は予約投稿を推薦

#### 8-6. 出力例

```json
{
  "optimal_posting_recommendation": {
    "current_time": "2026-01-06T14:30:00+09:00",
    "current_time_slot": "weekday_noon",
    "current_er": 3.8,
    "optimal_time_slot": "weekday_evening",
    "optimal_time": "2026-01-06T21:30:00+09:00",
    "optimal_er": 5.1,
    "er_improvement": "+34%",
    "confidence": "★★★（18サンプル）",
    "recommendation": "scheduled",
    "reason": "ERが34%向上（3.8% → 5.1%）。7時間待機する価値があります。",
    "fallback_option": "immediate（即時投稿）も可能ですが、ER低下のリスクがあります。"
  }
}
```

---

### STEP 10: Markdownフォールバック（Write tool使用）

Late API失敗時、LLMが以下を実行：

```markdown
1. 現在日時を取得（YYYY-MM-DD HH:MM:SS形式）
2. フォールバックファイルパス生成:
   `Flow/YYYYMM/YYYY-MM-DD/x_post_fallback_{timestamp}.md`

3. Write toolで以下の内容を書き込み:

# X投稿フォールバック（Late API失敗）

**生成日時**: {timestamp}
**エラー理由**: {error_message}

## 投稿内容

```
{tweet_content}
```

## 文字数情報
- 総カウント数: {total_count} / 280
- 日本語文字数: {japanese_chars}
- 半角文字数: {ascii_chars}
- 絵文字数: {emoji_count}
- URL数: {url_count}

## ハッシュタグ
{hashtags}

## Late API手動投稿用ペイロード

```json
{
  "platforms": [{
    "platform": "twitter",
    "accountId": "{account_id}"
  }],
  "content": "{tweet_content}",
  "publishNow": true
}
```

## 次のアクション
1. Late APIダッシュボードにアクセス: https://late.so/dashboard
2. 上記ペイロードをコピー
3. 手動で投稿作成
```

4. ユーザーに通知:
   「Late API投稿に失敗しました。フォールバックファイルを生成しました: {file_path}」
```

---

## 出力仕様

### 成功時（Late API 200/201）

```json
{
  "status": "success",
  "platform": "twitter",
  "post_id": "late_api_post_id_xxx",
  "tweet_content": "ツイート本文...",
  "character_count": {
    "total": 268,
    "japanese": 130,
    "ascii": 8,
    "emoji": 0,
    "url": 0
  },
  "hashtags": ["#AI活用", "#生産性向上"],
  "scheduled_for": "2026-01-07T08:00:00+09:00",
  "engagement_prediction": {
    "predicted_likes": 50,
    "predicted_retweets": 8,
    "predicted_replies": 4,
    "x_algorithm_score": 62.0,
    "estimated_reach": 600
  }
}
```

### 成功時（スレッド投稿）

```json
{
  "status": "success",
  "platform": "twitter",
  "format": "thread",
  "post_id": "late_api_post_id_xxx",
  "thread_tweets": [
    {
      "tweet_number": "1/4",
      "content": "(1/4)\n\nこれあんまり知ってる人少ないんですが\n\nAI活用で生産性が3倍になる方法、実は5つしかありません。\n\n以下で解説します👇\n\n#AI活用 #生産性向上",
      "character_count": {
        "total": 134,
        "japanese": 67,
        "ascii": 0,
        "emoji": 1,
        "url": 0
      }
    },
    {
      "tweet_number": "2/4",
      "content": "(2/4)\n\n1. タスク自動化（30%削減）\n- 定型業務をChatGPTで自動化\n- 週10時間の時間創出\n\n2. 情報収集効率化（50%削減）\n- Web記事を3分で要約\n- リサーチ時間が半減",
      "character_count": {
        "total": 128,
        "japanese": 64,
        "ascii": 0,
        "emoji": 0,
        "url": 0
      }
    },
    {
      "tweet_number": "3/4",
      "content": "(3/4)\n\n3. コード生成支援（40%削減）\n4. 資料作成自動化（60%削減）\n5. メール返信効率化（70%削減）\n\n各施策の詳細はプロフィールのリンクから📝",
      "character_count": {
        "total": 122,
        "japanese": 61,
        "ascii": 0,
        "emoji": 1,
        "url": 0
      }
    },
    {
      "tweet_number": "4/4",
      "content": "(4/4)\n\nこの5つを実践すれば、誰でも生産性3倍は達成可能です。\n\nあなたはどの方法から試しますか？\n\n参考になった人はいいねしてね👍",
      "character_count": {
        "total": 108,
        "japanese": 54,
        "ascii": 0,
        "emoji": 1,
        "url": 0
      }
    }
  ],
  "total_thread_length": 4,
  "scheduled_for": "2026-01-07T08:00:00+09:00",
  "engagement_prediction": {
    "predicted_likes": 120,
    "predicted_retweets": 18,
    "predicted_replies": 10,
    "x_algorithm_score": 173.0,
    "estimated_reach": 1500,
    "thread_multiplier": 1.63
  }
}
```

### エラー時（Late API 400/401/429/500+）

```json
{
  "status": "error",
  "error_code": 429,
  "error_message": "レート制限超過: 1時間後に再試行してください",
  "fallback_file": "Flow/202601/2026-01-06/x_post_fallback_20260106_143022.md",
  "tweet_content": "ツイート本文...",
  "character_count": {
    "total": 268,
    "japanese": 130,
    "ascii": 8,
    "emoji": 0,
    "url": 0
  }
}
```

### フォールバック時（Timeout/その他）

```json
{
  "status": "fallback",
  "reason": "Late API接続タイムアウト（3回リトライ失敗）",
  "fallback_file": "Flow/202601/2026-01-06/x_post_fallback_20260106_143022.md",
  "tweet_content": "ツイート本文...",
  "manual_action_required": true,
  "next_steps": [
    "フォールバックファイルを確認",
    "Late APIダッシュボードで手動投稿",
    "Late API障害状況を確認"
  ]
}
```

---

## Phase 1 実装完了チェックリスト

- [x] ディレクトリ作成: `.claude/skills/generate-x-posts/`
- [x] `x_patterns_detailed.md`作成（カテゴリ1: 40パターン）
- [x] `SKILL.md`作成（本ファイル）
- [x] `x_config.json`作成（基本構造）
- [ ] 単一ツイート生成テスト（文字数カウント正常動作）
- [ ] Late API統合テスト（成功時・エラー時）
- [ ] Markdownフォールバック動作確認
- [ ] 禁止事項チェック機能テスト（11項目）
- [ ] Phase 1評価（LLM生成成功率95%、Late API成功率90%）

---

## Phase 2 実装完了チェックリスト

- [x] STEP 2-B追加: スレッド生成ロジック（LLM自然言語理解）
  - [x] コンテンツ長判定（280-1400カウント）
  - [x] セマンティック分割（段落・見出し・句点優先）
  - [x] 重要度スコアリング（数値データ、固有名詞、インパクト語彙）
  - [x] スレッド構成最適化（1ツイート目フック、最終ツイートCTA）
  - [x] 各ツイート文字数検証（280半角文字 = 日本語140文字）
- [x] Late API `threadItems`ペイロード例追加
  - [x] スレッド即時投稿
  - [x] スレッド予約投稿
- [x] 出力仕様にスレッド成功時の例追加
- [x] **STEP 6追加: Late API統合の学び反映（v0.4.6）**
  - [x] 正しいペイロード形式の明示（実証済み）
  - [x] よくあるエラーと解決策を追加（3パターン）
  - [x] Python実装例追加（最小限、実証済み）
  - [x] 成功実績の記録（post_id: 695ceb1e8247cf816ba753b6）
- [x] スレッド生成テスト（7ツイート、自然な分割）
- [x] Late API スレッド投稿テスト（threadItems正常動作）
  - [x] 2026-01-06 20:10投稿成功確認
- [x] Phase 2評価（スレッド成功率100%、Late API統合完了）

---

## Phase 3 実装完了チェックリスト

- [x] STEP 4追加: エンゲージメント予測（LLM直接計算）
  - [x] 4-1. ベースER推定（コンテンツ品質スコアリング）
    - 数値データ3つ以上: +0.5%
    - 問いかけ終結: +1.0%
    - 衝撃フック（バズ構文100選）: +0.8%
    - 権威性引用: +0.6%
    - 具体的事例: +0.4%
  - [x] 4-2. 予測エンゲージメント数計算
    - predicted_likes = followers × base_er × 0.5
    - predicted_retweets = predicted_likes × 0.15
    - predicted_replies = predicted_likes × 0.08
  - [x] 4-3. X公式アルゴリズムスコア計算（GitHub検証済み重み数値）
    - engagement_score = (replies × 13.5) + (retweets × 1.0) + (likes × 0.5)
  - [x] 4-4. Recency factor計算（半減期360分）
    - recency_factor = exp(-elapsed_minutes / 360)
  - [x] 4-5. Premium優遇計算（3.0倍平均）
    - premium_multiplier = 3.0（範囲: 2.0-4.0）
  - [x] 4-6. 時間帯補正
    - 朝8時: 1.3倍、昼12時: 1.1倍、夜21時: 1.2倍
  - [x] 4-7. 最終スコアとリーチ予測
    - final_score = engagement_score × recency_factor × premium_multiplier × time_multiplier
    - estimated_reach = followers × premium_multiplier × time_multiplier × (1 + base_er)
- [x] x_config.jsonにアカウント設定追加
  - followers_count: 1000
  - is_premium: true
  - average_base_er: 0.03
- [x] 出力仕様にエンゲージメント予測JSON追加
- [ ] エンゲージメント予測テスト（誤差率30%以内）
- [ ] Phase 3評価（予測精度、スコア計算正確性）

---

## Phase 4 実装完了チェックリスト

- [x] x_patterns_detailed.md完全版作成（84パターン、全10カテゴリ）
  - [x] カテゴリ1: 有益性強調・インパクト訴求（38パターン）
  - [x] カテゴリ2: 権威性活用（10パターン）
  - [x] カテゴリ3: 逆張り構文（4パターン）
  - [x] カテゴリ4: one of them構文（5パターン）
  - [x] カテゴリ5: デメリット訴求（4パターン）
  - [x] カテゴリ6: ネガティブ人物導入（3パターン）
  - [x] カテゴリ7: 数字・実績挿入（5パターン）
  - [x] カテゴリ8: A vs B比較（5パターン）
  - [x] カテゴリ9: 喜怒哀楽感情（6パターン）
  - [x] カテゴリ10: CTA型終結（4パターン）

- [x] STEP 5追加: シャドウバン回避（投稿間隔監視・警告）
  - [x] 5-1. x_config.jsonから投稿履歴読み込み
  - [x] 5-2. 投稿間隔チェック（過去1時間・24時間のカウント）
  - [x] 5-3. 警告レベル判定（レベル0-3）
    - レベル0（安全）: hourly < 3 かつ daily < 30
    - レベル1（注意）: hourly 3-4
    - レベル2（危険）: hourly >= 5 または daily >= 40
    - レベル3（緊急停止）: daily >= 50
  - [x] 5-4. 推奨待機時間計算（LLM直接計算）
  - [x] 5-5. x_config.json更新（Edit tool）
  - [x] 5-6. 出力例（警告メッセージ、推薦アクション）

- [x] STEP 6追加: A/Bテスト（2パターン生成、LLM比較）
  - [x] 6-1. A/Bテスト実行判定（ユーザーリクエスト、ER未達時）
  - [x] 6-2. パターンA生成（フック1、バズ構文カテゴリ選択）
  - [x] 6-3. パターンB生成（フック2、異なるカテゴリ）
  - [x] 6-4. LLM比較分析（7つの観点）
    - エンゲージメント予測スコア
    - 推定リーチ
    - フックの衝撃度（1-10点）
    - 本文の読みやすさ（1-10点）
    - CTAの明確さ（1-10点）
    - ハッシュタグ適切性（1-10点）
    - 文字数最適性
  - [x] 6-5. 最終選択（総合スコア比較）
  - [x] 6-6. A/Bテスト結果記録（x_config.json）

- [x] STEP 8追加: 最適投稿時刻推薦（履歴分析）
  - [x] 8-1. x_config.jsonからエンゲージメント履歴読み込み
  - [x] 8-2. 曜日・時間帯判定（LLM直接計算）
  - [x] 8-3. 最適時刻推薦（LLM分析）
    - ステップ1: 現在の曜日・時間帯のER取得
    - ステップ2: 同曜日カテゴリ内での最適時刻特定
    - ステップ3: サンプル数による信頼性評価（★★★、★★☆、★☆☆）
  - [x] 8-4. Late API予約投稿時刻提案
  - [x] 8-5. 代替案提示（即時投稿 vs 予約投稿）
  - [x] 8-6. 出力例（ER改善率、信頼度、推薦理由）

- [ ] A/Bテスト10回実施、勝ちパターンの蓄積
- [ ] シャドウバン発生率 0%達成
- [ ] 平均ER 3.5%以上達成
- [ ] Phase 4評価

---

## 参照ファイル

- **バズ構文詳細**: `@.claude/skills/generate-x-posts/x_patterns_detailed.md`
- **設定ファイル**: `@.claude/skills/generate-x-posts/x_config.json`
- **Late API実装**: `@Stock/programs/副業/projects/SNS/scripts/late_api_post.py`
- **実装計画**: `@/Users/yuichi/.claude/plans/velvet-floating-muffin.md`

---

## バージョン履歴

- **v0.4.6** (2026-01-06): **Late API統合の学び反映（スレッド投稿実証済み）**
  - STEP 6追加: Late API投稿（スレッド対応、実証済み）
  - 成功実績: 2026-01-06 20:10投稿成功（post_id: 695ceb1e8247cf816ba753b6）
  - 正しいペイロード形式の明示:
    - `content`: 1ツイート目をトップレベルに配置（必須）
    - `platforms[].platformSpecificData.threadItems`: 2ツイート目以降を配列に格納
    - 各アイテムは`{"content": "text"}`形式（`{"text": "..."}`は無効）
  - よくあるエラーと解決策を追加:
    - エラー1: "Content is required" → `content`フィールド必須
    - エラー2: 2ツイート目以降が表示されない → `{"content": "..."}`形式を使用
    - エラー3: platformSpecificDataの配置ミス → `platforms[]`内に配置
  - Python実装例追加（最小限、実証済み）
  - 参照実装: `@Stock/programs/副業/projects/SNS/scripts/schedule_x_threads_post.py` (126-141行目)
  - STEP番号変更: 旧STEP 5-8 → 新STEP 7-10（Late API統合セクション挿入に伴う）

- **v0.4.5** (2026-01-06): **デフォルトモデルをOpusに変更**
  - `model: sonnet` → `model: opus` に変更
  - 理由: より洗練された表現、深い論理構成、高品質な投稿生成のため
  - コスト増加するが、X投稿の品質とエンゲージメント率向上を優先
  - Sonnet比でバズ構文選択の精度向上、文脈に最適化されたパターン選択

- **v0.4.4** (2026-01-06): **引用リポスト形式の追加**
  - `source_tweet_url`パラメータ追加（オプション）
  - 1ツイート目に元投稿URLを引用する機能実装
  - URL配置: 核心メッセージの直後、CTA（「以下で解説します👇」）の直前
  - Xの引用ツイートカード自動表示によるエンゲージメント1.3倍向上
  - 元投稿へのクレジット明示、権威性活用
  - 使用例追加（入力タイプ詳細セクション）
  - STEP 2-4に引用リポスト形式の例を追加

- **v0.4.3** (2026-01-06): **エンゲージメント指標除外の強化**
  - 他のSNS投稿のエンゲージメント指標除外ルールを明確化
  - ビュー数、インプレッション数も明示的に禁止に追加
  - 具体例追加: 「SuguruKun_aiのスレッドが163,736ビューを記録」など
  - ビジネス指標（売上、成長率）とエンゲージメント指標の区別を明確化
  - STEP 2-3の禁止事項を詳細化

- **v0.4.2** (2026-01-06): **ハッシュタグ削除・エンゲージメント指標除外**
  - ハッシュタグを使用しない方針に変更（Xのアルゴリズムで不要、スパム判定リスク回避）
  - 他の投稿のエンゲージメント指標（いいね数、リツイート数、ビュー数）を含めない指示を追加
  - 制約事項セクションに明記
  - STEP 2-3に禁止事項として追加
  - STEP 2-A-3（ハッシュタグ追加）を削除

- **v0.4.1** (2026-01-06): **スレッド形式をデフォルトに変更**
  - **重大変更**: `format`パラメータのデフォルトを`"single"`から`"thread"`に変更
  - 根拠: algorithm.md（486-505行目）のデータに基づく
    - スレッドは単一ツイート比較でインプレッション+63%、エンゲージメント+54%、フォロワー成長率3.2倍
  - STEP 2を「スレッド生成（デフォルト）」に変更
  - STEP 2-Aを「単一ツイート生成（例外ケース）」として追加
  - 最適スレッド数: 5-10ツイート（最適7ツイート）
  - 単一ツイートは`format: "single"`で明示的指定時のみ生成

- **v0.4.0** (2026-01-06): Phase 4 最適化・A/Bテスト実装
  - x_patterns_detailed.md完全版作成（84パターン、全10カテゴリ）
    - カテゴリ2-10追加（権威性、逆張り、one of them、デメリット、ネガティブ人物、数字、A vs B、感情、CTA）
  - STEP 5追加: シャドウバン回避（投稿間隔監視・警告）
    - 過去1時間・24時間の投稿数カウント（LLM直接計算）
    - 4段階警告レベル（安全、注意、危険、緊急停止）
    - 推奨待機時間計算、Late API予約投稿時刻提案
  - STEP 6追加: A/Bテスト（2パターン生成、LLM比較）
    - 異なるバズ構文カテゴリから2パターン生成
    - 7つの観点で比較分析（エンゲージメント、フック衝撃度、読みやすさ、CTA、ハッシュタグ、文字数）
    - 総合スコア算出、最適パターン自動選択
    - A/Bテスト結果記録（x_config.json）
  - STEP 8追加: 最適投稿時刻推薦（履歴分析）
    - 曜日・時間帯別のER分析（weekday/weekend、morning/noon/evening）
    - サンプル数による信頼性評価（★★★、★★☆、★☆☆）
    - 即時投稿 vs 予約投稿の比較分析、ER改善率提示

- **v0.3.0** (2026-01-06): Phase 3 エンゲージメント予測実装
  - STEP 4追加: エンゲージメント予測（LLM直接計算）
  - X公式アルゴリズムスコア計算（GitHub検証済み重み数値）
    - Reply: 13.5倍、Retweet: 1.0倍、Like: 0.5倍
  - Recency factor（半減期360分）- 投稿後の時間経過による減衰
  - Premium優遇（3.0倍乗算）
  - 時間帯補正（朝1.3倍、昼1.1倍、夜1.2倍）
  - ベースER推定（コンテンツ品質スコアリング）
  - 推定リーチ計算（インプレッション予測）
  - x_config.jsonにアカウント設定追加（followers_count、is_premium、average_base_er）

- **v0.2.0** (2026-01-06): Phase 2 スレッド対応実装
  - スレッド生成機能（3-5ツイート）
  - セマンティック分割（LLM自然言語理解）
  - 重要度スコアリング（数値データ、固有名詞、インパクト語彙）
  - Late API `threadItems`統合
  - 各ツイート280半角文字検証（日本語140文字）
  - スレッド成功時の出力仕様追加

- **v0.1.0** (2026-01-06): Phase 1 MVP実装
  - 単一ツイート生成
  - 280半角文字制限対応（日本語140文字）
  - バズ構文カテゴリ1（40パターン）
  - Late API統合
  - Markdownフォールバック
  - 禁止事項チェック（11項目）
