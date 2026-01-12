---
name: collect-x-timeline
description: |
  X (Twitter) のホームタイムラインから高エンゲージメント投稿を効率的に収集するスキル。
  Playwrightカーソルベース API傍受方式により、GraphQL APIのHomeTimelineエンドポイントを
  ネットワークレスポンスで傍受し、重複率0%でツイートデータを収集します。

  使用タイミング：
  - SNS投稿分析・トレンド調査時
  - インフルエンサー発掘時
  - コンテンツ戦略立案時

  所要時間：5-10分
  出力：x_timeline_{YYYY-MM-DD}.json（ツイートデータ + エンゲージメント統計）
trigger_keywords:
  - "Xタイムライン収集"
  - "X収集"
  - "Twitterタイムライン収集"
  - "ツイート収集"
  - "SNSデータ収集"
stage: Data Collection
dependencies: []
output_file: Stock/programs/副業/projects/SNS/data/x_timeline_{YYYY-MM-DD}.json
execution_time: 5-10分
framework_reference: Stock/programs/副業/projects/SNS/
priority: P1
---

# Collect X Timeline Skill

X (Twitter) のホームタイムライン収集スキル。

---

## このSkillでできること

1. **GraphQL API傍受**: Playwrightでホームタイムライン APIをネットワークインターセプション
2. **カーソルベースページネーション**: 重複率0%の完璧なデータ品質
3. **高エンゲージメント抽出**: ユーザー名、テキスト、いいね、リツイート、リプライ数を構造化
4. **自動認証**: Cookieファイルから自動ログイン
5. **デバッグモード**: APIレスポンス保存で詳細分析可能

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 目標収集件数（デフォルト: 200件）、Cookie認証ファイル |
| **出力** | x_timeline_{YYYY-MM-DD}.json（ツイートデータ + メタデータ） |
| **次のアクション** | トレンド分析、インフルエンサー分析、コンテンツ戦略立案 |

---

## Instructions

**実行モード**: 自律実行
**推定所要時間**: 5-10分

### STEP 1: Cookie認証ファイル確認（30秒）

**確認項目**:
```bash
# Cookieファイルの存在確認
ls -lh Stock/programs/副業/projects/SNS/data/x_cookies.json
```

**Cookieファイルが存在しない場合**:
1. ユーザーに通知
2. Cookie取得手順を案内:
   - X.com にブラウザでログイン
   - 開発者ツール → Application → Cookies
   - `x.com` ドメインのクッキーをエクスポート
   - JSON形式で `data/x_cookies.json` に保存

**Cookieフォーマット例**:
```json
[
  {
    "name": "auth_token",
    "value": "xxxxx",
    "domain": "x.com",
    "path": "/",
    "secure": true,
    "httpOnly": true
  }
]
```

---

### STEP 2: 収集パラメータ設定（30秒）

**ユーザーに確認**:
```
以下のパラメータで収集を開始します：
- 目標収集件数: 200件
- 出力パス: data/x_timeline_{YYYY-MM-DD}.json
- デバッグモード: OFF（ONにする場合は --debug を指定）

よろしければ実行します。パラメータを変更する場合はお知らせください。
```

**カスタマイズ可能なパラメータ**:
- `--target`: 目標収集件数（デフォルト: 200）
- `--output`: 出力ファイルパス（デフォルト: `data/x_timeline_{YYYY-MM-DD}.json`）
- `--url`: 収集URL（デフォルト: `https://x.com/home`）
- `--cookies`: クッキーファイルパス（デフォルト: `data/x_cookies.json`）
- `--debug`: デバッグモード（APIレスポンス保存）

---

### STEP 3: Playwright スクリプト実行（4-8分）

**Bashツール使用**:
```bash
cd Stock/programs/副業/projects/SNS

# 基本実行（200件収集）
python3 scripts/collect_x_timeline_cursor.py \
  --target 200 \
  --output "data/x_timeline_$(date +%Y%m%d).json" \
  --cookies data/x_cookies.json

# デバッグモード実行（APIレスポンス保存）
python3 scripts/collect_x_timeline_cursor.py \
  --target 200 \
  --output "data/x_timeline_$(date +%Y%m%d).json" \
  --cookies data/x_cookies.json \
  --debug
```

**実行プロセス**:
1. **ブラウザ起動**: Playwright Chromium ヘッドレスモード
2. **Cookie認証**: `x_cookies.json` から認証情報ロード
3. **ホームタイムラインナビゲート**: `https://x.com/home` へアクセス
4. **ネットワークインターセプション**: GraphQL API `HomeTimeline` レスポンス傍受
5. **データ抽出**: ツイートID、ユーザー名、テキスト、エンゲージメント指標を抽出
6. **カーソルベースページネーション**: `cursor-bottom-XXX` から次のカーソル値を取得
7. **スクロール&待機**: 2000pxスクロール、3-6秒ランダム待機（レート制限回避）
8. **重複除外**: `seen_tweet_ids` セットで自動フィルタ
9. **目標達成確認**: 200件到達またはmax_iterations（150回）で終了

**技術的特徴**:
- **GraphQL構造解析**: `data.home.home_timeline_urt.instructions[].entries[]` から抽出
- **ユーザー情報パス**: `result.core.user_results.result.core.screen_name`
- **ツイートテキスト**: `legacy.full_text`
- **エンゲージメント**: `legacy.favorite_count`, `legacy.retweet_count`, `legacy.reply_count`

---

### STEP 4: データ品質検証（1分）

**検証項目**:
```python
# 擬似コード（LLM内計算）

# 1. 収集件数確認
actual_count = len(tweets)
target_count = 200
achievement_rate = (actual_count / target_count) * 100

# 2. 重複率確認
unique_ids = set([tweet['tweet_id'] for tweet in tweets])
duplicate_rate = (1 - len(unique_ids) / actual_count) * 100

# 3. エンゲージメントデータ完全性
tweets_with_engagement = [t for t in tweets if t['likes'] > 0 or t['retweets'] > 0]
engagement_completeness = (len(tweets_with_engagement) / actual_count) * 100

# 判定
if achievement_rate >= 95 and duplicate_rate < 1 and engagement_completeness >= 80:
    status = "success"
elif achievement_rate >= 80:
    status = "warning"  # 警告付きで続行
else:
    status = "failure"  # データ不足で停止
```

**品質基準**:
| 指標 | 成功 | 警告 | 失敗 |
|------|------|------|------|
| **目標達成率** | ≥95% | 80-95% | <80% |
| **重複率** | <1% | 1-5% | >5% |
| **エンゲージメント完全性** | ≥80% | 60-80% | <60% |

---

### STEP 5: 成果物生成（30秒）

**出力フォーマット**:
```json
{
  "collected_at": "2026-01-01T22:30:00",
  "total_tweets": 211,
  "unique_tweets": 211,
  "duplicate_rate": 0.0,
  "cursors_collected": 7,
  "quality_score": {
    "achievement_rate": 105.5,
    "duplicate_rate": 0.0,
    "engagement_completeness": 95.2
  },
  "tweets": [
    {
      "tweet_id": "1234567890",
      "username": "@elonmusk",
      "text": "Tweet content...",
      "likes": 103049,
      "retweets": 25000,
      "replies": 8500,
      "timestamp_text": "Mon Jan 01 22:20:00 +0000 2026",
      "collected_at": "2026-01-01T22:30:00"
    }
  ]
}
```

**保存先**: `Stock/programs/副業/projects/SNS/data/x_timeline_{YYYY-MM-DD}.json`

**サマリーレポート生成** (オプション):
```markdown
# Xタイムライン収集レポート

収集日時: 2026-01-01 22:30:00

## 実行サマリー
- ステータス: 成功
- 総収集数: 211件
- ユニーク: 211件
- 重複率: 0%
- 目標達成率: 105.5%
- カーソル数: 7個
- 実行時間: 約5分

## データ品質
- エンゲージメント完全性: 95.2%
- Username抽出率: 100%
- テキスト抽出率: 100%

## Top 5 高エンゲージメント
1. @username1: 103,049 likes
2. @username2: 89,532 likes
3. @username3: 75,210 likes
4. @username4: 62,803 likes
5. @username5: 58,441 likes

## 次のアクション
- トレンド分析
- インフルエンサー分析
- コンテンツ戦略立案
```

---

## パフォーマンス比較

### カーソルベースAPI vs Scroll方式

| 指標 | カーソルベースAPI | Scroll方式 | 改善率 |
|------|-----------------|-----------|--------|
| **収集件数** | 211件 | 8件 | **26.4倍** |
| **重複率** | 0% | 52.9% | **-100%** |
| **実行時間** | 約5分 | 約5分 | 同等 |
| **スケーラビリティ** | 400件/10分 | 16件/10分 | **25倍** |

---

## エラーハンドリング

### Cookie認証失敗
- **原因**: auth_token 期限切れ、Cookie形式エラー
- **対応**: ユーザーに再ログイン＆Cookie再取得を依頼
- **ログ**: `status: "auth_failure"` 記録

### Username抽出が"unknown"になる場合
- **原因**: GraphQL レスポンス構造変更
- **対応**: フォールバックパスで再抽出
  ```python
  # パターン1: core.user_results.result.core.screen_name
  # パターン2: core.user_results.result.legacy.screen_name
  ```
- **ログ**: username="unknown" のツイートを検出し、パターン2で再処理

### エンゲージメント指標が0になる場合
- **原因**: DOM変更、aria-label フォーマット変更
- **対応**: GraphQL APIから直接抽出（DOM非依存）
- **ログ**: `engagement_completeness` スコアが80%未満の場合は警告

### ネットワークタイムアウト
- **タイムアウト設定**:
  - 各イテレーション: 60秒
  - 全体: 10分
- **対応**: タイムアウト時は現在までのデータを保存し、部分成功として報告

---

## データ品質保証

| 品質指標 | 目標 | 実績（2026-01-01） |
|---------|------|------------------|
| **収集件数** | 200件 | 211件（105.5%） |
| **重複率** | <1% | 0% |
| **Username抽出率** | ≥95% | 100% |
| **エンゲージメント完全性** | ≥80% | 95.2% |

---

## Knowledge Base参照

- **実装ガイド**: `Stock/programs/副業/projects/SNS/X_COLLECTION_INSTRUCTIONS.md`
- **修正版ガイド**: `Stock/programs/副業/projects/SNS/docs/x_timeline_collection_fixed_guide.md`
- **成功レポート**: `Stock/programs/副業/projects/SNS/data/x_timeline_20260101_final/FINAL_SUCCESS_REPORT.md`
- **比較レポート**: `Stock/programs/副業/projects/SNS/data/cursor_vs_scroll_comparison_report.md`

---

## 使用例

### 基本的な使用

```
User: Xタイムライン収集
```

システムが自動的に：
1. Cookie認証ファイル確認
2. パラメータ確認（目標200件）
3. Playwrightスクリプト実行
4. データ品質検証（目標達成率、重複率）
5. JSON出力生成
6. サマリーレポート生成

### カスタムパラメータ使用

```
User: Xタイムライン収集 500件
```

システムが自動的に：
- `--target 500` でスクリプト実行
- 約10分で500件収集
- データ品質検証
- JSON出力生成

### デバッグモード使用

```
User: Xタイムライン収集（デバッグモード）
```

システムが自動的に：
- `--debug` フラグでスクリプト実行
- APIレスポンスを `data/x_timeline_cursor_test_debug/` に保存
- 詳細なログ出力

---

## 実行時の注意事項

1. **Cookie有効期限**: 約30日で期限切れ、再ログインが必要
2. **レート制限**: 1時間に約500件が上限（スクロール待機時間で調整）
3. **市場時間**: 24時間実行可能だが、トレンドは平日昼間が活発
4. **データ鮮度**: 毎日実行でトレンド追跡、週1回実行で週次分析

---

## 依存パッケージ

**必須**:
```bash
pip install playwright asyncio
playwright install chromium
```

**オプション（分析用）**:
```bash
pip install pandas numpy matplotlib
```

---

## 次のアクション提案

収集完了後、以下のアクションを提案します：

1. **トレンド分析**: いいね・リツイート数Top 50を抽出
2. **インフルエンサー分析**: 高エンゲージメントユーザーTop 10を特定
3. **コンテンツ戦略**: 人気トピック・キーワードを抽出
4. **時系列分析**: 日次・週次のトレンド推移を可視化

---

## 更新履歴

- 2026-01-02: 初版作成（Claude Code Skill対応）
- 2026-01-01: 211件収集成功（目標達成率105.5%）
- 2025-12-31: Playwrightカーソルベース実装完成
