# schedule-linkedin-3-cases

---
name: schedule-linkedin-3-cases
description: |
  LinkedIn投稿3案を自動生成し、Late API経由で翌日8:00 JSTに一括予約投稿するスキル（高野メソッド準拠）。
  ユーザーはLate APIコンソールで3案を確認し、最適な1案を選択して投稿を実行。
  所要時間: 3-5分、出力: post_result_scheduled_{YYYYMMDD}.json
version: 1.0.0
trigger_keywords:
  - "LinkedIn 3案自動予約"
  - "LinkedIn予約投稿"
  - "schedule-linkedin-3-cases"
stage: Phase 3b - LinkedIn Scheduling
dependencies:
  - research-topic (最新リサーチデータ使用)
output_file: "Stock/programs/副業/projects/SNS/data/post_result_scheduled_{YYYYMMDD}.json"
execution_time: "3-5分"
priority: P1
model: sonnet
thinking: false
---

## Overview

最新のAIリサーチデータから高野メソッド準拠のLinkedIn投稿3案を自動生成し、Late API経由で**翌日8:00 JST**に一括予約投稿します。

**実行フロー**:
1. 最新リサーチデータ（`research_findings_*_v2_*.json`）を読み込み
2. Claude API経由で3案を生成（数字インパクト型、衝撃発言型、問題提起型）
3. Late API経由で翌日8:00 JSTに全3案を予約投稿
4. ユーザーはLate APIコンソール（https://getlate.dev/dashboard）で3案を確認
5. 最適な1案を選択し、残り2案を削除してから投稿実行

**Late API失敗時のフォールバック**:
- 手動投稿用Markdownファイルを `data/manual_posts/linkedin_{YYYYMMDD}.md` に自動生成

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│              LinkedIn 3-Case Auto Scheduling Flow                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ research_findings │ → │ Claude API       │                  │
│  │ (最新AIリサーチ)  │    │ (3案生成)        │                  │
│  └──────────────────┘    └──────────────────┘                  │
│                                    │                            │
│                                    ▼                            │
│                          ┌──────────────────┐                  │
│                          │ 高野メソッド7要素 │                  │
│                          │ ①引き込み        │                  │
│                          │ ②データ/事例    │                  │
│                          │ ③共感           │                  │
│                          │ ④洞察           │                  │
│                          │ ⑤アドバイス     │                  │
│                          │ ⑥問いかけ       │                  │
│                          │ ⑦固有名詞       │                  │
│                          └──────────────────┘                  │
│                                    │                            │
│                                    ▼                            │
│                          ┌──────────────────┐                  │
│                          │ 3案同時生成      │                  │
│                          │ ・数字インパクト型│                  │
│                          │ ・衝撃発言型     │                  │
│                          │ ・問題提起型     │                  │
│                          └──────────────────┘                  │
│                                    │                            │
│                                    ▼                            │
│                          ┌──────────────────┐                  │
│                          │ Late API         │                  │
│                          │ (翌日8:00 JST)   │                  │
│                          └──────────────────┘                  │
│                                    │                            │
│                ┌───────────────────┴───────────────────┐        │
│                ▼                                       ▼        │
│      ┌──────────────────┐                 ┌──────────────────┐ │
│      │ Late API Console │                 │ Markdown File    │ │
│      │ (ユーザー選択)   │                 │ (失敗時)         │ │
│      └──────────────────┘                 └──────────────────┘ │
│                │                                                │
│                ▼                                                │
│      ┌──────────────────┐                                      │
│      │ 1案のみ投稿実行  │                                      │
│      └──────────────────┘                                      │
└─────────────────────────────────────────────────────────────────┘
```

---

## Success Criteria

- [ ] リサーチデータ読み込み成功率 100%
- [ ] 3案生成成功率 100%（各案700字以上）
- [ ] Late API予約投稿成功率 95%以上
- [ ] 失敗時のMarkdownファイル生成 100%
- [ ] 翌日8:00 JST計算の正確性 100%
- [ ] ログファイル保存 100%

---

## Prerequisites

### 環境変数設定（`.env`ファイル）

```bash
# Late API
LATE_API_KEY=sk_your-late-api-key-here
LATE_LINKEDIN_ACCOUNT_ID=your-linkedin-account-id

# Anthropic API
ANTHROPIC_API_KEY=sk-ant-api03-your-api-key-here
```

### 必要なPythonパッケージ

```bash
pip3 install anthropic requests python-dotenv pytz
```

---

## Instructions

### STEP 1: スキル実行

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

# Claude Code CLIでスキル実行
/schedule-linkedin-3-cases
```

**または直接Pythonスクリプト実行**:
```bash
python3 scripts/schedule_linkedin_post.py
```

---

### STEP 2: 実行フロー

1. **次の予約投稿日を取得**
   - `data/post_result_scheduled_*.json` から最新ファイルを検索
   - 最新日付の**翌日8:00 JST**を計算
   - ファイルがない場合は**明日8:00 JST**

2. **コンテンツ生成（3案）**
   - `data/research_findings_*_v2_*.json` から最新リサーチデータを読み込み
   - Claude API経由で3案を生成:
     - 案1: 数字インパクト型（具体的数値・倍率・金額を最優先）
     - 案2: 衝撃発言型（著名人の発言や強い表現）
     - 案3: 問題提起型（読者の課題や業界の変化を問いかけ）

3. **Late API予約投稿**
   - 全3案を同じ時刻（翌日8:00 JST → UTC変換）に予約投稿
   - 成功時: `post_id` をログに記録
   - 失敗時: Markdownファイル生成 + エラーログ記録

4. **ログ保存**
   - `data/post_result_scheduled_{YYYYMMDD}.json` に保存
   - 内容: 予約日時、各案のステータス（成功/失敗）、post_id

---

### STEP 3: Late APIコンソールで確認・選択

1. **Late APIダッシュボードにアクセス**:
   - URL: https://getlate.dev/dashboard
   - Late APIアカウントでログイン

2. **予約投稿一覧を確認**:
   - 翌日8:00 JSTに予約された3案が表示される
   - 各案のプレビューを確認

3. **最適な1案を選択**:
   - エンゲージメントが高そうな案を1つ選択
   - 残り2案を削除（Late APIコンソールの削除ボタン）

4. **投稿実行**:
   - 選択した1案が翌日8:00に自動投稿される

---

### STEP 4: エラー時のフォールバック

Late API失敗時、以下のMarkdownファイルが自動生成されます:

**ファイルパス**: `data/manual_posts/linkedin_{YYYYMMDD}.md`

**ファイル内容例**:
```markdown
# LinkedIn 手動投稿（Late API 失敗時）

**日付**: 2026-01-05
**予定時刻**: 08:00 JST

---

## 案1（数字インパクト型）

AI投資額が2025年に前年比3.2倍の$2,400億に達した。

... (投稿本文700-900字) ...

**ハッシュタグ**: #AI #スタートアップ

---

## 案2（衝撃発言型）

「AIは仕事を奪うのではなく、仕事の質を変える」― Marc Andreessen

... (投稿本文700-900字) ...

**ハッシュタグ**: #AI #経営

---

## 案3（問題提起型）

あなたの会社はAI導入で本当に生産性が上がりましたか？

... (投稿本文700-900字) ...

**ハッシュタグ**: #AI #テクノロジー

---

**エラー理由**: Late API Error: 401 - Unauthorized

**手動投稿方法**:
1. Late APIダッシュボード (https://getlate.dev/dashboard) にアクセス
2. 上記3案から1案を選択
3. LinkedInに手動投稿
```

---

## Output Files

### 成功時

**ファイル**: `data/post_result_scheduled_20260105.json`

```json
{
  "scheduled_date": "2026-01-05T08:00:00+09:00",
  "scheduled_time_jst": "2026-01-05 08:00:00 JST",
  "results": [
    {
      "case": 1,
      "type": "数字インパクト型",
      "post_id": "post_abc123",
      "content": "AI投資額が2025年に前年比3.2倍の$2,400億に達した。\n\n...\n\n#AI #スタートアップ",
      "status": "success"
    },
    {
      "case": 2,
      "type": "衝撃発言型",
      "post_id": "post_def456",
      "status": "success"
    },
    {
      "case": 3,
      "type": "問題提起型",
      "post_id": "post_ghi789",
      "status": "success"
    }
  ]
}
```

### 失敗時

**ファイル**: `data/manual_posts/linkedin_20260105.md`（上記参照）

---

## Cost Estimation

### Claude API料金（Sonnet 4）

- **入力**: 4,500 tokens（リサーチデータ2,000 + プロンプト2,500）
- **出力**: 1,500 tokens（3案 × 500 tokens）
- **コスト**: $0.0135（入力）+ $0.0225（出力）= **$0.036/回**

**月間コスト**（毎日実行）:
- $0.036 × 30日 = **$1.08/月**

### Late API料金

- 無料プラン: 100投稿/月まで無料
- 月間投稿数: 30日 × 3案 = 90投稿 → **無料範囲内**

---

## Troubleshooting

### 問題1: "No research_findings found"

**原因**: リサーチデータファイルが存在しない

**解決策**:
```bash
# research-topic スキルを実行してリサーチデータを生成
/research-topic
```

---

### 問題2: Late API "401 Unauthorized"

**原因**: Late API keyが無効または期限切れ

**解決策**:
1. Late API Console → Settings → API Keys
2. 新しいAPI keyを生成
3. `.env` ファイルの `LATE_API_KEY` を更新

---

### 問題3: LinkedIn Account ID不明

**原因**: `LATE_LINKEDIN_ACCOUNT_ID` が設定されていない

**解決策**:
```bash
# Late API経由でアカウント情報取得
python3 scripts/get_late_accounts.py

# 出力からLinkedIn Account IDをコピー
# .envに設定
LATE_LINKEDIN_ACCOUNT_ID=your-linkedin-account-id
```

---

### 問題4: Claude API "rate_limit_error"

**原因**: Claude API レート制限到達（5リクエスト/分）

**解決策**:
- 1分待機後に再実行
- または実行頻度を調整（毎日 → 週3回）

---

## Dependencies

### Python Scripts

| スクリプト | 役割 |
|----------|------|
| `scripts/late_api_client.py` | Late API統合（スケジューリング） |
| `scripts/generate_linkedin_3_cases.py` | Claude API経由でコンテンツ生成 |
| `scripts/schedule_linkedin_post.py` | メイン実行スクリプト |

### External APIs

| API | 用途 | レート制限 |
|-----|------|----------|
| **Claude API** | 3案コンテンツ生成 | 5リクエスト/分 |
| **Late API** | LinkedIn予約投稿 | 100リクエスト/分 |

---

## Related Skills

- **research-topic**: 最新リサーチデータ生成（前提条件）
- **generate-sns-posts**: 汎用SNS投稿生成（参考実装）
- **approve-and-schedule**: Web UI承認フロー（別アプローチ）

---

## Version History

### v1.0.0 (2026-01-04)
- 初版リリース
- Late API統合
- Claude API経由で3案生成（高野メソッド準拠）
- 翌日8:00 JST自動計算
- Markdownフォールバック実装
