# /post-multiplatform

LinkedIn/X/Threadsへのマルチプラットフォーム予約投稿を実行します（Option C対応、6投稿/日）。

## 実行内容

1. 環境変数チェック（Late APIキー、各プラットフォームのアカウントID）
2. 最新の投稿ファイル（`posts_generated_takano_{date}.md`）を検索
3. 6投稿のコンテンツを抽出
4. Late APIから既存予約を取得し、競合を回避
5. 投稿計画を表示してユーザー確認
6. Late API経由で6投稿を予約

## 投稿スケジュール

| 時刻 | プラットフォーム | タイプ |
|------|----------------|--------|
| 7:30 | X | 派生（フック変更） |
| 7:30 | Threads | 派生（フック変更） |
| 8:00 | LinkedIn | 高野式メイン |
| 12:00 | X | スレッド深掘り |
| 20:00 | X | スレッド深掘り |
| 20:00 | Threads | 新規 |

## 引数

- `--auto`: 確認プロンプトをスキップ
- `--date YYYY-MM-DD`: 特定日付の投稿ファイルを使用

## 使用例

```
/post-multiplatform
/post-multiplatform --auto
/post-multiplatform --date 2026-01-06
```

## 前提条件

1. `.env`に以下の環境変数が設定されていること：
   - `LATE_API_KEY`
   - `LATE_LINKEDIN_ACCOUNT_ID`
   - `LATE_TWITTER_ACCOUNT_ID`
   - `LATE_THREADS_ACCOUNT_ID`

2. `posts_generated_takano_{date}.md`が存在すること
   - なければ先に`/generate-sns-posts-takano`を実行

## 実行スクリプト

```bash
cd Stock/programs/副業/projects/SNS
python3 scripts/late_api_multi_post_v2.py
```

## 詳細

詳細は `.claude/skills/post-multiplatform/SKILL.md` を参照してください。
