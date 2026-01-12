# Post Multiplatform Skill

LinkedIn/X/Threadsへのマルチプラットフォーム予約投稿スキル（Option C対応）。

**Version**: 1.0.0

---

## このSkillでできること

1. **6投稿同時予約**: LinkedIn 1案 + X 3投稿 + Threads 2投稿を一括予約
2. **競合回避**: 4時間帯（7:30, 8:00, 12:00, 20:00）の既存予約を自動検出・回避
3. **Xスレッド対応**: 5-7ツイートのスレッド形式投稿
4. **Late API統合**: 全プラットフォームをLate API経由で自動投稿

---

## 投稿スケジュール（Option C）

| 時刻 | プラットフォーム | タイプ | トピック | 文字数 |
|------|----------------|--------|---------|--------|
| 7:30 | X | 派生（フック変更） | Top 1 | 280文字 |
| 7:30 | Threads | 派生（フック変更） | Top 1 | 500文字 |
| 8:00 | LinkedIn | 高野式メイン | Top 1 | 1,150-1,300文字 |
| 12:00 | X | スレッド深掘り | Top 2 | 5-7ツイート |
| 20:00 | X | スレッド深掘り | Top 3 | 5-7ツイート |
| 20:00 | Threads | 新規（LinkedIn似） | Top 2 | 500文字 |

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | `posts_generated_takano_{date}.md`（Phase 3出力） |
| **出力** | `late_api_multiplatform_{timestamp}.json`（予約結果） |
| **前提スキル** | generate-sns-posts-takano（投稿生成） |

---

## 必要な環境変数

`.env`ファイルに以下を設定：

```bash
LATE_API_KEY=sk_...
LATE_LINKEDIN_ACCOUNT_ID=...
LATE_TWITTER_ACCOUNT_ID=...
LATE_THREADS_ACCOUNT_ID=...
```

---

## Instructions

**実行モード**: Bashスクリプト実行
**推定所要時間**: 2-5分

### STEP 1: 環境確認（30秒）

**実行前チェック**:

```bash
# 環境変数の存在確認
cd Stock/programs/副業/projects/SNS
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv()

required = ['LATE_API_KEY', 'LATE_LINKEDIN_ACCOUNT_ID', 'LATE_TWITTER_ACCOUNT_ID', 'LATE_THREADS_ACCOUNT_ID']
missing = [k for k in required if not os.getenv(k)]
if missing:
    print(f'❌ 未設定: {missing}')
else:
    print('✅ 全環境変数設定済み')
"
```

**環境変数が未設定の場合**:
1. Late APIダッシュボード（https://getlate.dev/dashboard）でアカウントIDを確認
2. `.env`ファイルに追記

---

### STEP 2: 投稿ファイル確認（30秒）

**最新の投稿ファイルを確認**:

```bash
ls -la Stock/programs/副業/projects/SNS/data/posts_generated_takano_*.md | tail -1
```

**ファイルが存在しない場合**:
- `generate-sns-posts-takano`スキルを先に実行

---

### STEP 3: マルチプラットフォーム投稿実行（1-3分）

**対話モード実行**:

```bash
cd Stock/programs/副業/projects/SNS
python3 scripts/late_api_multi_post_v2.py
```

**自動実行（確認スキップ）**:

```bash
cd Stock/programs/副業/projects/SNS
echo "y" | python3 scripts/late_api_multi_post_v2.py
```

---

### STEP 4: 結果確認（30秒）

**結果ファイルを確認**:

```bash
ls -la Stock/programs/副業/projects/SNS/data/late_api_multiplatform_*.json | tail -1
```

**Late APIダッシュボードで確認**:
- https://getlate.dev/dashboard

---

## 対話フロー

スクリプト実行時の対話フロー：

```
============================================================
SNS Multi-Platform Posting v2.0 (Option C)
============================================================

📋 環境チェック中...
   ✅ LATE_API_KEY: 設定済み
   ✅ LATE_LINKEDIN_ACCOUNT_ID: 設定済み
   ✅ LATE_TWITTER_ACCOUNT_ID: 設定済み
   ✅ LATE_THREADS_ACCOUNT_ID: 設定済み

📁 投稿ファイル検索中...
   ✅ 入力ファイル: posts_generated_takano_20260107.md

📄 コンテンツを抽出中...
   ✅ LinkedIn: 1,280文字
   ✅ X派生: 280文字
   ✅ Xスレッド1: 7ツイート
   ✅ Xスレッド2: 5ツイート
   ✅ Threads派生: 480文字
   ✅ Threads新規: 520文字

🔍 既存予約投稿をチェック中...
   既存予約投稿: 3件
✅ 投稿日: 2026-01-08

============================================================
投稿計画（競合回避済み）
============================================================
💼 2026-01-08 08:00 JST - LINKEDIN
   タイプ: main
   内容: OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」...

🐦 2026-01-08 07:30 JST - TWITTER
   タイプ: derived
   内容: X派生（Top1）...

🐦 2026-01-08 12:00 JST - TWITTER
   タイプ: thread
   スレッド: 7ツイート

🐦 2026-01-08 20:00 JST - TWITTER
   タイプ: thread
   スレッド: 5ツイート

🧵 2026-01-08 07:30 JST - THREADS
   タイプ: derived
   内容: Threads派生（Top1）...

🧵 2026-01-08 20:00 JST - THREADS
   タイプ: new
   内容: Threads新規（Top2）...

合計: 6投稿

============================================================
上記の計画で投稿を実行しますか？ (y/n): y

============================================================
Late API投稿実行中...
============================================================

💼 LINKEDIN (08:00) を投稿中...
   ✅ 成功! Post ID: 695b47753c923022a7af9074

🐦 TWITTER (07:30) を投稿中...
   ✅ 成功! Post ID: 695b47763c923022a7af908b

🐦 TWITTER (12:00) を投稿中...
   ✅ 成功! Post ID: 695b47773c923022a7af909c

🐦 TWITTER (20:00) を投稿中...
   ✅ 成功! Post ID: 695b47783c923022a7af90a4

🧵 THREADS (07:30) を投稿中...
   ✅ 成功! Post ID: 695b47793c923022a7af90b5

🧵 THREADS (20:00) を投稿中...
   ✅ 成功! Post ID: 695b47803c923022a7af90c6

============================================================
実行完了
============================================================
💾 結果保存: late_api_multiplatform_20260107_143022.json

✅ 成功: 6/6投稿
❌ 失敗: 0/6投稿

プラットフォーム別:
  💼 LINKEDIN: 1/1
  🐦 TWITTER: 3/3
  🧵 THREADS: 2/2

🎉 全投稿が成功しました！
Late APIダッシュボードで確認してください:
https://getlate.dev/dashboard
============================================================
```

---

## コンテンツ抽出ロジック

スクリプトは`posts_generated_takano_{date}.md`から以下を自動抽出：

| セクション | 抽出パターン | 出力先 |
|-----------|-------------|--------|
| `## LinkedIn投稿` | 高野式本文 | linkedin |
| `## X派生投稿` | フック変更版 | x_derived |
| `## Xスレッド1` | 5-7ツイート | x_thread1 |
| `## Xスレッド2` | 5-7ツイート | x_thread2 |
| `## Threads派生投稿` | フック変更版 | threads_derived |
| `## Threads新規投稿` | LinkedIn似 | threads_new |

**フォールバック**:
- セクションが見つからない場合、案1/案2/案3から自動生成
- LinkedIn案をベースにX/Threads用に文字数調整

---

## エラーハンドリング

### 環境変数未設定

```
❌ 未設定: ['LATE_TWITTER_ACCOUNT_ID', 'LATE_THREADS_ACCOUNT_ID']
```

**対応**: `.env`ファイルにアカウントIDを追加

### 投稿ファイル未検出

```
❌ 投稿ファイルが見つかりません
   Stock/programs/副業/projects/SNS/data/posts_generated_takano_*.md
```

**対応**: `generate-sns-posts-takano`スキルを先に実行

### Late API認証エラー

```
❌ 失敗: 401 Unauthorized
```

**対応**: `LATE_API_KEY`が正しいか確認

### 部分成功

```
⚠️  一部の投稿が失敗しました
   - twitter (thread): Rate limit exceeded
```

**対応**: 失敗した投稿のみ手動で再実行、またはしばらく待ってから再実行

---

## 出力ファイル形式

**ファイル名**: `late_api_multiplatform_{YYYYMMDD_HHMMSS}.json`

```json
{
  "executed_at": "2026-01-07T14:30:22+09:00",
  "target_date": "2026-01-08",
  "posting_schedule": {
    "linkedin": [{"time": "08:00", "type": "main", "topic": "top1"}],
    "twitter": [
      {"time": "07:30", "type": "derived", "topic": "top1"},
      {"time": "12:00", "type": "thread", "topic": "top2"},
      {"time": "20:00", "type": "thread", "topic": "top3"}
    ],
    "threads": [
      {"time": "07:30", "type": "derived", "topic": "top1"},
      {"time": "20:00", "type": "new", "topic": "top2"}
    ]
  },
  "results": [
    {
      "platform": "linkedin",
      "type": "main",
      "status": "success",
      "post_id": "695b47753c923022a7af9074",
      "scheduled_for": "2026-01-08T08:00:00+09:00",
      "title": "OpenAIとNVIDIAが仕掛けた「200兆円の循環投資」..."
    },
    {
      "platform": "twitter",
      "type": "derived",
      "status": "success",
      "post_id": "695b47763c923022a7af908b",
      "scheduled_for": "2026-01-08T07:30:00+09:00",
      "title": "X派生（Top1）"
    }
    // ... 残り4投稿
  ]
}
```

---

## 関連スキル

| スキル | 役割 | 実行順序 |
|--------|------|---------|
| `collect-x-timeline` | Xタイムライン収集 | Phase 1 |
| `extract-content` | コンテンツ抽出 | Phase 2 |
| `research-topic` | トピック調査 | Phase 2 |
| `generate-sns-posts-takano` | 投稿生成 | Phase 3 |
| **`post-multiplatform`** | **マルチプラットフォーム投稿** | **Phase 4** |

---

## 使用例

### 基本的な使用

```
User: /post-multiplatform
```

システムが自動的に：
1. 環境変数をチェック
2. 最新の投稿ファイルを検索
3. 6投稿のコンテンツを抽出
4. 既存予約との競合をチェック
5. 投稿計画を表示
6. ユーザー確認後、6投稿を実行
7. 結果をJSONに保存

### 自動実行モード

```
User: /post-multiplatform --auto
```

確認プロンプトをスキップして自動実行。

### 特定日付の投稿ファイルを指定

```
User: /post-multiplatform --date 2026-01-06
```

指定日付の投稿ファイルを使用。

---

## 依存関係

**Pythonパッケージ**:
- `requests`
- `python-dotenv`

**設定ファイル**:
- `.env`（環境変数）

**入力ファイル**:
- `posts_generated_takano_{date}.md`

---

## 更新履歴

| 日時 | バージョン | 変更内容 |
|------|----------|---------|
| 2026-01-07 | 1.0.0 | 初版作成（Option C対応、6投稿マルチプラットフォーム） |

---

## 参照

- **投稿スクリプト**: `Stock/programs/副業/projects/SNS/scripts/late_api_multi_post_v2.py`
- **共有コンテキスト**: `.claude/skills/sns-automation/sns_automation_shared_context.md`
- **Late API統合ガイド**: `.claude/skills/sns-automation/late_api_integration_guide.md`
- **Late APIダッシュボード**: https://getlate.dev/dashboard
