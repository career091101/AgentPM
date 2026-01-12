---
name: analyze-sns-performance-weekly
description: |
  LinkedIn、X (Twitter)、Threads、Facebookの週次パフォーマンスを分析し、
  基本レポート（Markdown）を生成します。

  分析内容:
  - 実行日から7日遡りの投稿データ取得
  - KPI達成状況（インプレッション、エンゲージメント率）
  - プラットフォーム別パフォーマンス比較
  - トップ5投稿の特徴分析
  - Facebook Professional Dashboard統合分析（閲覧数、インタラクション、オーディエンス）

  出力: Flow/{YYYYMM}/{YYYY-MM-DD}/sns_performance_report_{YYYYMMDD}.md
  所要時間: 15-20分

trigger_keywords:
  - "SNS週次分析"
  - "SNS Performance Analysis"
  - "パフォーマンス週次レポート"
  - "Facebook分析"

stage: Analysis
dependencies:
  - Late API Analytics Addon（必須：LinkedIn, X, Threads）
  - fetch_late_analytics_optimized.py
  - collect-facebook-performance（オプション：Facebook）
  - Chrome MCP（Facebook収集時に必要）

output_file: Flow/{YYYYMM}/{YYYY-MM-DD}/sns_performance_report_{YYYYMMDD}.md
execution_time: 10-15分
priority: P1
model: claude-sonnet-4-5-20250929  # Sonnet 4.5 (2026年1月時点の最新モデル)
---

# SNS Performance Analysis - Weekly SKILL

直近1週間のSNS投稿パフォーマンスを分析し、KPI達成状況を可視化するスキルです。

## 実行フロー

### STEP 1: パラメータ設定（1分）

1. **実行日時の取得**
```bash
# スキル引数から期間を取得（オプション）
if [ -n "${START_DATE}" ]; then
    WEEK_AGO="${START_DATE}"
else
    WEEK_AGO=$(date -v-7d +%Y-%m-%d)  # macOS
    # Linux: WEEK_AGO=$(date -d '7 days ago' +%Y-%m-%d)
fi

if [ -n "${END_DATE}" ]; then
    TODAY="${END_DATE}"
else
    TODAY=$(date +%Y-%m-%d)
fi

YYYYMMDD=$(date +%Y%m%d)
YYYYMM=$(date +%Y%m)
YYYY_MM_DD=$(date +%Y-%m-%d)
```

2. **出力パスの設定**
```bash
OUTPUT_DIR="/Users/yuichi/AIPM/aipm_v0/Flow/${YYYYMM}/${YYYY_MM_DD}"
DATA_FILE="${OUTPUT_DIR}/late_api_analytics_${WEEK_AGO//\-/}-${TODAY//\-/}.json"
REPORT_FILE="${OUTPUT_DIR}/sns_performance_report_${YYYYMMDD}.md"
```

3. **ディレクトリ作成**
```bash
mkdir -p "${OUTPUT_DIR}"
```

---

### STEP 1.5: Facebookパフォーマンス収集（オプショナル）（20-30分）

**重要**: このステップはオプショナルです。Facebook収集に失敗しても、Late APIプラットフォーム（LinkedIn, X, Threads）での分析は継続されます。

#### 1-5-1. 実行条件確認

```bash
# Chrome MCP接続確認
if ! tabs_context_mcp(createIfEmpty=True); then
    echo "⚠️  Chrome MCP未接続: Facebook収集をスキップします"
    FACEBOOK_COLLECTION_ENABLED=false
fi

# Facebook最終データ確認
FACEBOOK_DATA_PATH="Stock/programs/副業/projects/SNS/data"
FACEBOOK_DATA_FILE="${FACEBOOK_DATA_PATH}/fb_performance_${YYYY_MM_DD}.json"
if [ -f "${FACEBOOK_DATA_FILE}" ]; then
    echo "✅ Facebookデータ検出: ${FACEBOOK_DATA_FILE}"
    FACEBOOK_COLLECTION_ENABLED=false  # 既存データ使用
else
    echo "⚠️  Facebookデータなし: 新規収集を試みます"
    FACEBOOK_COLLECTION_ENABLED=true
fi
```

#### 1-5-2. collect-facebook-performanceスキル実行

**実行方法**: Task tool経由

```python
if FACEBOOK_COLLECTION_ENABLED:
    try:
        facebook_result = Task(
            description="Facebook収集",
            prompt=f"""
            @.claude/skills/collect-facebook-performance/SKILL.md の仕様に従い、
            Facebookパフォーマンスデータを収集してください。

            **期間指定（重要）**:
            - 開始日（since_date）: {WEEK_AGO}
            - 終了日（until_date）: {TODAY}

            **実行手順**:
            1. STEP 1.5 で日付フィルターを設定（Professional Dashboard右上のボタン）
            2. 上記期間のデータのみ収集（デフォルト28日間ではない）
            3. 指定期間データを返すこと

            **出力先**: Stock/programs/副業/projects/SNS/data/fb_performance_{YYYY_MM_DD}.json
            **タイムアウト**: 35分

            Chrome MCPツールを使用してProfessional Dashboardから以下を収集:
            - STEP 1.5: 日付フィルター設定（"過去28日間" → "カスタム" → カレンダー選択）
            - STEP 3: Views（閲覧数）
            - STEP 4: Interactions（インタラクション）
            - STEP 5: Audience（フォロワー）
            - STEP 6: Content Library（投稿別メトリクス）
            - STEP 7: Timeline Posts（投稿全文）
            """,
            subagent_type="general-purpose",
            model="sonnet",
            timeout=2100000  # 35分（期間設定+5分）
        )
        print("✅ Facebook収集完了")
    except Exception as e:
        print(f"⚠️  Facebook収集失敗: {e}")
        print("   Late APIプラットフォームのみで分析を継続します")
        FACEBOOK_COLLECTION_ENABLED = false
```

#### 1-5-3. エラーハンドリング

| エラー | 対応 | 影響 |
|--------|------|------|
| Chrome MCP未接続 | 警告表示、スキップ | Late API継続 |
| Facebook未ログイン | 手動ログイン依頼後、スキップ | Late API継続 |
| タイムアウト（30分） | 警告表示、スキップ | Late API継続 |
| 部分データ（品質<70%） | 警告表示、データ使用スキップ | Late API継続 |

**重要**: Facebookデータ収集失敗は全体の失敗とせず、Late APIプラットフォーム（LinkedIn, X, Threads）で分析を継続します。

---

### STEP 2: Late APIデータ収集（5-8分）

#### 2-1. 環境変数確認

**必須**: LATE_API_KEY が設定されていることを確認

```bash
if [ -z "$LATE_API_KEY" ]; then
    echo "❌ エラー: LATE_API_KEY が設定されていません"
    echo "   .env ファイルを確認してください"
    exit 1
fi
```

#### 2-2. Analytics Addon契約確認

**重要**: 事前に Late API の Analytics Addon が契約されていることを確認してください。

未契約の場合:
- エラーコード: 402 (Payment Required)
- メッセージ: "Analytics Addon契約が必要です"
- 契約URL: https://app.getlate.dev/settings/billing

#### 2-3. データ収集実行

```bash
cd /Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS

python3 scripts/fetch_late_analytics_optimized.py \
  --from-date "${WEEK_AGO}" \
  --to-date "${TODAY}" \
  --output "${DATA_FILE}"
```

**実行例**:
```bash
python3 scripts/fetch_late_analytics_optimized.py \
  --from-date 2026-01-03 \
  --to-date 2026-01-10 \
  --output /Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-10/late_api_analytics_20260103-20260110.json
```

#### 2-4. エラーハンドリング

| ステータスコード | 意味 | 対応 | リトライ |
|----------------|------|------|---------|
| 200 | 成功 | 処理継続 | - |
| 202 | 処理中 | データ未準備、後で再実行 | ✅（30分後） |
| 400 | 無効なリクエスト | パラメータ確認 | ❌ |
| 401 | 認証エラー | LATE_API_KEY確認 | ❌ |
| 402 | Analytics Addon未契約 | 契約が必要 | ❌ |
| 404 | データなし | 部分的に継続 | ❌ |
| 429 | レート制限 | 1時間待機 | ✅（最大3回） |
| 500+ | サーバーエラー | 30秒待機 | ✅（最大3回） |

**リトライロジック**（既存スクリプトに実装済み）:
- タイムアウト時: 30秒待機後リトライ（最大3回）
- レート制限時: 1時間待機後リトライ（最大3回）
- サーバーエラー時: 30秒待機後リトライ（最大3回）

---

### STEP 3: データ分析（3-5分）

**重要**: このステップでは新規Pythonスクリプトを作成せず、LLMの直接推論とReadツールでデータ分析を実行します。

#### 3-1. JSONデータ読み込み

```python
# Read tool を使用してJSONファイルを読み込み
data = Read(file_path=DATA_FILE)
```

#### 3-2. KPI目標値読み込み

```python
# KPI目標値を読み込み
kpi_targets = Read(file_path="/Users/yuichi/AIPM/aipm_v0/.claude/skills/analyze-sns-performance-weekly/kpi_targets.json")
```

#### 3-3. プラットフォーム別集計（LLM推論）

以下の集計を LLM で直接実行：

**LinkedIn集計**:
```
- 投稿数: len([post for post in data["data"] if post["platform"] == "linkedin"])
- 総インプレッション: sum([post["impressions"] for post in data["data"] if post["platform"] == "linkedin"])
- 総エンゲージメント: sum([post["likes"] + post["comments"] + post["shares"] for post in data["data"] if post["platform"] == "linkedin"])
- エンゲージメント率: (総エンゲージメント / 総インプレッション) * 100
- 投稿あたり平均インプレッション: 総インプレッション / 投稿数
```

**X (Twitter)集計**:
```
- 投稿数: len([post for post in data["data"] if post["platform"] == "x"])
- 総インプレッション: sum([post["impressions"] for post in data["data"] if post["platform"] == "x"])
- 総エンゲージメント: sum([post["likes"] + post["comments"] + post["shares"] for post in data["data"] if post["platform"] == "x"])
- エンゲージメント率: (総エンゲージメント / 総インプレッション) * 100
- 投稿あたり平均インプレッション: 総インプレッション / 投稿数
```

**Threads集計**（viewsフィールド使用）:
```
- 投稿数: len([post for post in data["data"] if post["platform"] == "threads"])
- 総Views: sum([post["views"] for post in data["data"] if post["platform"] == "threads"])
- 総エンゲージメント: sum([post["likes"] + post["comments"] + post["shares"] for post in data["data"] if post["platform"] == "threads"])
- エンゲージメント率: (総エンゲージメント / 総Views) * 100 if 総Views > 0 else None
- 投稿あたり平均Views: 総Views / 投稿数 if 投稿数 > 0 else 0
```

**重要**: ThreadsはLate APIの`views`フィールドを使用します。viewsが0の場合は「計測不可」として扱い、エンゲージメント絶対数のみで評価します。

**Facebook集計**（Chrome MCP経由）:

```
データソース: Stock/programs/副業/projects/SNS/data/fb_performance_{YYYY-MM-DD}.json
（collect-facebook-performance スキルで生成）

- 総閲覧数: fb_data["views"]["total"]
- 閲覧者数: fb_data["views"]["viewers"]
- 総インタラクション: fb_data["interactions"]["total"]
  - リアクション: fb_data["interactions"]["reactions"]
  - コメント: fb_data["interactions"]["comments"]
  - シェア: fb_data["interactions"]["shares"]
- フォロワー数: fb_data["audience"]["total_followers"]
- 純フォロー数（週間）: fb_data["audience"]["net_followers"]
- エンゲージメント率: (総インタラクション / 総閲覧数) * 100
- 閲覧数変化率: fb_data["summary"]["views_change"]
- インタラクション変化率: fb_data["summary"]["interactions_change"]
```

**Facebook KPI評価**:
```
1. 週間閲覧数達成率 = (実績 / 目標100,000) * 100
2. 週間インタラクション達成率 = (実績 / 目標1,500) * 100
3. フォロワー増加達成率 = (純フォロー数 / 目標150) * 100
```

**Facebookデータ取得オプション**:
- **自動収集**: collect-facebook-performance スキルを STEP 2の前に実行
- **手動収集**: 既存の fb_performance_{YYYY-MM-DD}.json を使用
- **スキップ**: Facebookデータがない場合は警告表示し、他プラットフォームのみで分析継続

#### 3-4. 全体サマリー集計（LLM推論）

```
Late API プラットフォーム（LinkedIn, X, Threads）:
- 総投稿数: len(data["data"])
- 総インプレッション: LinkedIn総imp + X総imp（Threadsはviewsベースのため除外）
- 総Views（Threads）: Threads総views
- 総エンゲージメント: LinkedIn総eng + X総eng + Threads総eng
- 平均エンゲージメント率: (LinkedIn総imp + X総imp > 0) ? (LinkedIn総eng + X総eng) / (LinkedIn総imp + X総imp) * 100 : 0

Facebook（Chrome MCP経由）:
- 総閲覧数: fb_data["views"]["total"]（28日累計）
- 総インタラクション: fb_data["interactions"]["total"]
- フォロワー増減: fb_data["audience"]["net_followers"]

統合サマリー:
- 全プラットフォーム総リーチ: Late API総imp + Threads総views + Facebook総閲覧数
- 全プラットフォーム総エンゲージメント: Late API総eng + Threads総eng + Facebook総インタラクション
```

**注意**:
- ThreadsはViewsベースのため、インプレッション総計からは除外して別途表示
- Threads views > 0 の場合のみ、Threads独自のエンゲージメント率を計算
- エンゲージメント率はLinkedIn + Xのみで計算
- FacebookはProfessional Dashboard経由の28日間累計データを使用（週次比較は変化率で評価）

#### 3-5. KPI比較（LLM推論）

```
Late API プラットフォーム:
1. 総インプレッション達成率 = (実績 / 目標150,000) * 100
2. 平均エンゲージメント率達成率 = (実績 / 目標1.5%) * 100
3. LinkedIn投稿あたり平均imp達成率 = (実績 / 目標8,000) * 100
4. X投稿あたり平均imp達成率 = (実績 / 目標2,000) * 100

Facebook:
5. 週間閲覧数達成率 = (実績 / 目標100,000) * 100
6. 週間インタラクション達成率 = (実績 / 目標1,500) * 100
7. フォロワー増加達成率 = (純フォロー数 / 目標150) * 100
```

**評価ロジック**:
- ✅ = 達成（100%以上）
- ⚠️ = 要改善（80-99%）
- ❌ = 未達成（80%未満）

#### 3-6. トップ5投稿抽出（LLM推論）

```
1. インプレッション降順でソート
2. 上位5件を抽出
3. 各投稿の以下の情報を取得:
   - プラットフォーム
   - 投稿日時（published_at）
   - インプレッション数
   - エンゲージメント率
   - 内容プレビュー（text_preview）
```

---

### STEP 4: Markdownレポート生成（1-2分）

#### 4-1. テンプレート読み込み

```python
template = Read(file_path="/Users/yuichi/AIPM/aipm_v0/.claude/skills/analyze-sns-performance-weekly/report_template.md")
```

#### 4-2. プレースホルダー置換（LLM推論）

以下のプレースホルダーを実際の値で置換:

**期間・メタデータ**:
- `{period_start}` → 開始日（YYYY-MM-DD）
- `{period_end}` → 終了日（YYYY-MM-DD）
- `{generated_at}` → 生成日時（YYYY-MM-DD HH:MM:SS）

**エグゼクティブサマリー**:
- `{total_posts}` → 総投稿数
- `{total_impressions:,}` → 総インプレッション（カンマ区切り）
- `{total_engagement:,}` → 総エンゲージメント（カンマ区切り）
- `{engagement_rate}` → エンゲージメント率（小数点1桁）

**LinkedIn**:
- `{linkedin_posts}` → 投稿数
- `{linkedin_impressions:,}` → 総インプレッション
- `{linkedin_avg_impressions:,}` → 投稿あたり平均インプレッション
- `{linkedin_engagement:,}` → 総エンゲージメント
- `{linkedin_engagement_rate}` → エンゲージメント率

**X (Twitter)**:
- `{x_posts}` → 投稿数
- `{x_impressions:,}` → 総インプレッション
- `{x_avg_impressions:,}` → 投稿あたり平均インプレッション
- `{x_engagement:,}` → 総エンゲージメント
- `{x_engagement_rate}` → エンゲージメント率

**Threads**（viewsフィールド使用）:
- `{threads_posts}` → 投稿数
- `{threads_views:,}` → 総Views
- `{threads_avg_views:,}` → 投稿あたり平均Views
- `{threads_engagement:,}` → 総エンゲージメント
- `{threads_engagement_rate}` → エンゲージメント率（views>0の場合のみ計算）
- `{threads_views_achievement}` → Threads達成率（views_per_post目標比）
- `{threads_views_status}` → 評価（✅/⚠️/❌）

**注意**: viewsが0の場合は「計測不可」と表示し、エンゲージメント絶対数のみで評価

**Facebook**（Chrome MCP経由）:
- `{facebook_views:,}` → 総閲覧数
- `{facebook_viewers:,}` → 閲覧者数
- `{facebook_interactions:,}` → 総インタラクション
- `{facebook_reactions:,}` → リアクション数
- `{facebook_comments:,}` → コメント数
- `{facebook_shares:,}` → シェア数
- `{facebook_followers:,}` → 総フォロワー数
- `{facebook_net_followers}` → 純フォロー数（増減）
- `{facebook_engagement_rate}` → エンゲージメント率
- `{facebook_views_change}` → 閲覧数変化率（例: +220.4%）
- `{facebook_interactions_change}` → インタラクション変化率（例: +146.0%）
- `{facebook_followers_change}` → フォロワー変化率（例: +3.8%）
- `{facebook_data_source}` → "Professional Dashboard (Chrome MCP)"（固定値）

**KPI達成状況**:
- `{impressions_achievement}` → 総インプレッション達成率
- `{impressions_status}` → 評価（✅/⚠️/❌）
- `{engagement_achievement}` → エンゲージメント率達成率
- `{engagement_status}` → 評価
- `{linkedin_achievement}` → LinkedIn達成率
- `{linkedin_status}` → 評価
- `{x_achievement}` → X達成率
- `{x_status}` → 評価
- `{facebook_views_achievement}` → Facebook閲覧数達成率
- `{facebook_views_status}` → 評価
- `{facebook_interactions_achievement}` → Facebookインタラクション達成率
- `{facebook_interactions_status}` → 評価
- `{facebook_followers_achievement}` → Facebookフォロワー増加達成率
- `{facebook_followers_status}` → 評価

**トップ5投稿**（1-5位）:
- `{top1_platform}` 〜 `{top5_platform}` → プラットフォーム名
- `{top1_published_at}` 〜 `{top5_published_at}` → 投稿日時
- `{top1_impressions:,}` 〜 `{top5_impressions:,}` → インプレッション
- `{top1_engagement_rate}` 〜 `{top5_engagement_rate}` → エンゲージメント率
- `{top1_text_preview}` 〜 `{top5_text_preview}` → 内容プレビュー

#### 4-3. レポートファイル出力

```python
# Write tool を使用してMarkdownファイルを出力
Write(file_path=REPORT_FILE, content=filled_template)
```

**出力例**:
```
/Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-10/sns_performance_report_20260110.md
```

---

### STEP 5: サマリー表示（<1分）

#### 5-1. 主要インサイト表示

コンソールに以下の情報を表示:

```
================================================================================
📊 SNS Performance Analysis - Weekly Report
================================================================================
期間: {WEEK_AGO} 〜 {TODAY}
出力ファイル: {REPORT_FILE}

✅ データ収集完了
   Late API:
   - 総投稿数: {total_posts}件
   - LinkedIn: {linkedin_posts}件
   - X: {x_posts}件
   - Threads: {threads_posts}件

   Facebook (Chrome MCP):
   - 総閲覧数: {facebook_views:,}回
   - 総インタラクション: {facebook_interactions:,}回
   - フォロワー: {facebook_followers:,}人 (+{facebook_net_followers})

📈 主要KPI
   Late API:
   - 総インプレッション: {total_impressions:,}回 ({impressions_achievement}%)
   - 平均エンゲージメント率: {engagement_rate}% ({engagement_achievement}%)

   Facebook:
   - 閲覧数: {facebook_views:,}回 ({facebook_views_achievement}%)
   - インタラクション: {facebook_interactions:,}回 ({facebook_interactions_achievement}%)

🎯 KPI達成状況
   - 総インプレッション: {impressions_status}
   - エンゲージメント率: {engagement_status}
   - LinkedIn平均imp: {linkedin_status}
   - X平均imp: {x_status}
   - Facebook閲覧数: {facebook_views_status}
   - Facebookインタラクション: {facebook_interactions_status}
   - Facebookフォロワー増: {facebook_followers_status}

🏆 トップ投稿
   1位: {top1_platform} - {top1_impressions:,}回
   2位: {top2_platform} - {top2_impressions:,}回
   3位: {top3_platform} - {top3_impressions:,}回

ℹ️  Threads: viewsフィールド使用（0の場合はエンゲージメント絶対数で評価）
ℹ️  Facebook: Professional Dashboard経由で28日間累計データ

詳細レポート: {REPORT_FILE}
================================================================================
```

---

## エラーハンドリング詳細

### エラー1: Analytics Addon未契約（402）

**症状**:
```
❌ Analytics Addon契約が必要です
   https://app.getlate.dev/settings/billing で契約してください
```

**対応**:
1. Late API ダッシュボードにアクセス
2. Settings → Billing に移動
3. Analytics Addon を契約
4. 契約後、5-10分待機してから再実行

**リトライ**: なし（契約が必須）

### エラー2: レート制限（429）

**症状**:
```
⚠️  Rate limit exceeded. Retrying in 1 hour...
```

**対応**:
- 自動リトライ: 1時間待機後に再実行（最大3回）
- 手動対応: プランをアップグレード（Basic 30/min → Pro 300/min）

**リトライ**: ✅（最大3回）

### エラー3: タイムアウト

**症状**:
```
❌ タイムアウト (Page 1)
```

**対応**:
- 自動リトライ: 30秒待機後に再実行（最大3回）
- ネットワーク接続を確認
- VPN使用時は切断して再試行

**リトライ**: ✅（最大3回）

### エラー4: データ欠損（404）

**症状**:
```
⚠️  データが見つかりません (404)
```

**対応**:
- 部分的に処理継続（取得できたデータのみでレポート生成）
- 期間を調整して再実行
- プラットフォーム別にデータ取得を試行

**リトライ**: なし（部分データで継続）

### エラー5: 環境変数未設定

**症状**:
```
❌ エラー: LATE_API_KEY が設定されていません
```

**対応**:
1. `.env` ファイルを確認
2. `LATE_API_KEY=xxxxx` が設定されているか確認
3. コメント記号（#）がインラインにないか確認（Late API .env パース問題）

**正しい .env 例**:
```bash
# Late API Key
LATE_API_KEY=xxxxxxxxxxxxxxxxxxxxx
```

**間違った .env 例**（インラインコメント禁止）:
```bash
LATE_API_KEY=xxxxxxxxxxxxxxxxxxxxx # My API Key ← これは NG
```

---

## Threads 指標処理の詳細

### viewsフィールドの使用

Threadsプラットフォームでは `views` フィールドを使用してリーチを測定します。Late API の PostAnalytics スキーマにより、全投稿タイプ（テキスト、写真、動画）で `views` フィールドが利用可能です。

**Late API PostAnalytics スキーマ**:
```yaml
PostAnalytics:
  type: object
  properties:
    views:
      type: integer
      description: Number of times a post was viewed
```

### 処理方法

**データ収集時**（Late API経由）:
- Threadsの投稿も通常通り取得
- `views` フィールドを使用（impressionsではなく）
- `engagement` フィールド（likes, comments, shares）は正常に取得

**分析時**（LLM推論）:
- Threadsの投稿数をカウント
- 総Viewsを集計
- 総エンゲージメントを集計
- **views > 0 の場合**: エンゲージメント率 = (総エンゲージメント / 総Views) × 100
- **views = 0 の場合**: エンゲージメント率は「計測不可」、エンゲージメント絶対数のみで評価
- 全体のインプレッション総計にはThreads viewsを含めない（LinkedIn + Xのみ）

**レポート生成時**:
- Views: 総Views数を表示（0の場合は「計測不可」）
- エンゲージメント率: views>0の場合のみ計算・表示
- 投稿あたり平均Views: KPI目標（100 views/post）との比較

### KPI評価基準

| 指標 | 目標値 | 評価 |
|------|--------|------|
| 投稿あたりViews | 100 | ✅≧100、⚠️80-99、❌<80 |
| 投稿あたりエンゲージメント | 5 | ✅≧5、⚠️4、❌<4 |

---

## 出力例

### コンソール出力

```
================================================================================
📊 SNS Performance Analysis - Weekly Report
================================================================================
期間: 2026-01-03 〜 2026-01-10
出力ファイル: /Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-10/sns_performance_report_20260110.md

✅ データ収集完了
   - 総投稿数: 56件
   - LinkedIn: 8件
   - X: 37件
   - Threads: 8件

📈 主要KPI
   - 総インプレッション: 143,664回 (95.8%)
   - 平均エンゲージメント率: 1.42% (94.7%)

🎯 KPI達成状況
   - 総インプレッション: ⚠️ (目標: 150,000)
   - エンゲージメント率: ⚠️ (目標: 1.5%)
   - LinkedIn平均imp: ✅ (目標: 8,000)
   - X平均imp: ⚠️ (目標: 2,000)

🏆 トップ投稿
   1位: x - 18,452回
   2位: x - 15,234回
   3位: linkedin - 12,987回

ℹ️  Threads: viewsフィールド使用（0の場合はエンゲージメント絶対数で評価）

詳細レポート: /Users/yuichi/AIPM/aipm_v0/Flow/202601/2026-01-10/sns_performance_report_20260110.md
================================================================================
```

### Markdownレポート出力

レポートファイルの例は `@.claude/skills/analyze-sns-performance-weekly/report_template.md` を参照してください。

---

## 検証項目（実行前チェックリスト）

### 前提条件

- [ ] Late API Analytics Addon が契約されている
- [ ] `.env` ファイルに `LATE_API_KEY` が設定されている
- [ ] `fetch_late_analytics_optimized.py` が配置されている
- [ ] Python 3.x がインストールされている

### 実行時チェック

- [ ] 実行日時が正しく取得されている（`date` コマンド動作確認）
- [ ] 出力ディレクトリが存在するまたは作成される
- [ ] Late APIスクリプトがエラーなく実行される
- [ ] JSONファイルが正しく生成される

### 出力品質チェック

- [ ] Markdownレポートが正しく生成される
- [ ] 表形式が崩れていない
- [ ] 数値フォーマットが適切（カンマ区切り、%表記）
- [ ] Threads特例表記が適切（"計測不可"）
- [ ] KPI達成率が正しく計算されている
- [ ] トップ5投稿が正しく抽出されている

---

## トラブルシューティング

### 問題1: Late APIスクリプトが実行できない

**症状**: `python3: command not found` または `ModuleNotFoundError: No module named 'requests'`

**解決策**:
```bash
# Python 3.x インストール確認
python3 --version

# 必要なライブラリインストール
pip3 install requests
```

### 問題2: 日付計算がエラーになる

**症状**: `date: illegal option -- v` (Linux環境)

**解決策**:
```bash
# Linux環境では以下を使用
WEEK_AGO=$(date -d '7 days ago' +%Y-%m-%d)
```

### 問題3: レポートファイルが生成されない

**症状**: Write tool エラー

**解決策**:
1. 出力ディレクトリが存在するか確認
2. 書き込み権限があるか確認
3. ディスク容量を確認

---

## 参照

- Late API OpenAPI仕様: `@Flow/202601/2026-01-10/late-api-openapi.yaml`
- Late API制約: `@.claude/skills/sns-automation/LATE_API_CONSTRAINTS_AND_NOTES.md`
- 既存分析レポート: `@Flow/202601/2026-01-10/sns_performance_analysis_20260101-0110.md`
- 既存スクリプト: `@Stock/programs/副業/projects/SNS/scripts/fetch_late_analytics_optimized.py`
- KPI目標値: `@.claude/skills/analyze-sns-performance-weekly/kpi_targets.json`
- レポートテンプレート: `@.claude/skills/analyze-sns-performance-weekly/report_template.md`
- **Facebook収集スキル**: `@.claude/skills/collect-facebook-performance/SKILL.md`
- **Facebookデータ保存先**: `@Stock/programs/副業/projects/SNS/data/fb_performance_{YYYY-MM-DD}.json`

---

### STEP 6: 週次比較分析（3-5分）

**重要**: このステップは STEP 5完了後に実行し、前週データとの比較により改善トレンドを可視化します。

#### 6-1. history.json読み込み

```python
# Read tool を使用して履歴データを取得
history_path = "/Users/yuichi/AIPM/aipm_v0/Stock/programs/副業/projects/SNS/history.json"
history_data = Read(file_path=history_path)
```

**初回実行時の対応**:
- history.jsonが存在しない場合 → 初回実行として扱い、STEP 7でhistory.json新規作成
- 空のweeks配列の場合 → 今週データのみでレポート生成

#### 6-2. 前週比較計算（LLM推論）

前週データ（配列末尾から1件前）と今週データを比較:

**インプレッション増減**:
```
今週総インプレッション - 前週総インプレッション
増減率 = ((今週 - 前週) / 前週) * 100
```

**エンゲージメント率増減**:
```
今週エンゲージメント率 - 前週エンゲージメント率
（%ポイント表記、例: 0.55% → 0.62% = +0.07%ポイント）
```

**プラットフォーム別増減**:
- LinkedIn: 投稿数増減、インプレッション増減、投稿あたり平均増減
- X: 投稿数増減、インプレッション増減、投稿あたり平均増減
- Threads: Views増減、エンゲージメント増減、投稿あたり平均Views増減
  - views=0の場合はエンゲージメント絶対数のみで比較
- Facebook（28日累計）: 変化率で評価（閲覧数変化率、インタラクション変化率）

**トレンド評価**:
- ⬆️ = 改善（増加率 > 5%）
- ➡️ = 横ばい（増加率 -5% 〜 +5%）
- ⬇️ = 悪化（増加率 < -5%）

#### 6-3. トレンド分析（過去4週、LLM推論）

**4週分のデータ抽出**:
```
weeks配列の最後の4件を取得（古い順）:
- Week -3（4週前）
- Week -2（3週前）
- Week -1（2週前）
- Week 0（今週）
```

**トレンドグラフデータ生成**（Markdown表形式）:
```
| 週 | 期間 | 総インプレッション | 前週比 | 目標達成率 |
|----|------|------------------|--------|----------|
| Week -3 | {w3_period} | {w3_impressions:,}回 | - | {w3_achievement}% |
| Week -2 | {w2_period} | {w2_impressions:,}回 | {w2_delta}% | {w2_achievement}% |
| Week -1 | {w1_period} | {w1_impressions:,}回 | {w1_delta}% | {w1_achievement}% |
| Week 0 | {period_start}〜{period_end} | {total_impressions:,}回 | {w0_delta}% | {impressions_achievement}% |
```

**4週移動平均計算**:
```
avg_impressions = (w3_impressions + w2_impressions + w1_impressions + w0_impressions) / 4
avg_engagement_rate = (w3_engagement_rate + w2_engagement_rate + w1_engagement_rate + w0_engagement_rate) / 4
```

**月間達成予測**:
```
monthly_pace = 今週総インプレッション × 4.3（週平均を月換算）
monthly_gap = 1,000,000 - monthly_pace（目標月間100万回）
monthly_gap_pct = (monthly_gap / 1,000,000) * 100

達成予測 = {
  monthly_pace >= 1,000,000 ? "✅ 達成見込み" :
  monthly_pace >= 800,000 ? "⚠️ 達成可能（要努力）" :
  "❌ 達成困難（戦略見直し必要）"
}
```

---

### STEP 7: 推奨アクション生成（5-10分）

**重要**: このステップはLLM推論によるデータドリブンな改善提案を生成し、次週の具体的なアクションプランを提示します。

#### 7-1. 課題特定（LLM推論）

STEP 6の比較結果から以下を特定:

**1. 目標未達成KPI**:
```
- 総インプレッション: 実績値、目標値、ギャップ、達成率
- エンゲージメント率: 実績値、目標値、ギャップ、達成率
- LinkedIn投稿あたり平均: 実績値、目標値、ギャップ、達成率
- X投稿あたり平均: 実績値、目標値、ギャップ、達成率
```

**2. 前週比悪化項目**:
```
- インプレッション前週比が-5%以下
- エンゲージメント率前週比が-0.1%ポイント以下
- プラットフォーム別投稿数の急減
```

**3. プラットフォーム配分の歪み**:
```
LinkedIn配分効率 = LinkedIn総インプレッション / 総インプレッション
X配分効率 = X総インプレッション / 総インプレッション

LinkedIn投稿比率 = LinkedIn投稿数 / 総投稿数
X投稿比率 = X投稿数 / 総投稿数

歪み判定:
- LinkedIn: 配分効率 > 投稿比率 × 1.5 → 投資不足（増やすべき）
- X: 配分効率 < 投稿比率 × 0.7 → 投資過多（減らすべき）
```

#### 7-2. 成功パターン分析（LLM推論）

**過去4週のトップ5投稿から共通パターン抽出**:

1. history.jsonから過去4週のtop_posts配列を取得
2. 各投稿のthemeフィールドを集計
3. 頻出パターンTop 3を特定

**x_patterns_detailed.md（84パターン）と照合**:
```python
# パターンマッチング
high_performing_patterns = []
for theme in top_themes:
    # 例: "概念反転・哲学系" → Pattern #12 "概念反転"
    pattern_id = match_pattern(theme, x_patterns_detailed.md)
    high_performing_patterns.append({
        "pattern_id": pattern_id,
        "theme": theme,
        "avg_impressions": theme_avg_impressions,
        "usage_rate": theme_count / total_top_posts
    })
```

**活用率計算**:
```
現在の成功パターン活用率 = (成功パターン使用投稿数 / 総投稿数) * 100
目標活用率 = 30%
ギャップ = 目標活用率 - 現在の活用率
```

#### 7-3. アクション優先度スコアリング（LLM推論）

各改善アクション候補に対して、以下の式で優先度スコア算出:

**優先度 = (期待効果 × 0.5) + (実行容易性 × 0.3) + (成功確率 × 0.2)**

**期待効果（0-100点）**:
```
インプレッション増加予測（回数） / 1,000 = 効果点
例: +10,000回 → 10点、+50,000回 → 50点、+100,000回 → 100点
```

**実行容易性（0-100点）**:
```
- 既存リソースのみで実施可能: 100点
- 既存スキル活用で実施可能: 80点
- 新規スキル作成が必要: 50点
- 外部ツール導入が必要: 30点
- 大規模リソース投入が必要: 10点
```

**成功確率（0-100点）**:
```
- 過去データで実績あり（成功パターン）: 90-100点
- 類似事例で効果確認済み: 70-89点
- 理論的根拠あり: 50-69点
- 仮説段階: 30-49点
- 不確実性が高い: 0-29点
```

#### 7-4. 推奨アクション出力（LLM推論）

優先度順にTop 3を出力:

**テンプレート**:
```markdown
#### 🎯 優先度1: {アクション名}（優先度スコア: {score}/100）

**期待効果**: {インプレッション増加予測}回（+{増加率}%）
**根拠**: {過去データまたは成功パターン}
**実装方法**:
1. {具体的な手順ステップ1}
2. {具体的な手順ステップ2}
3. {具体的な手順ステップ3}

**実行期限**: 次週（{next_week_date}まで）
**担当スキル**: {実行すべきClaude Skill名}
```

**アクション例**:

**優先度1（プラットフォーム最適化）**:
```markdown
#### 🎯 優先度1: LinkedIn投稿数を8→12投稿/週に増やす（優先度スコア: 85/100）

**期待効果**: +40,000回（+28%）
**根拠**:
- LinkedIn投稿あたり平均9,875回（Xの4.8倍の効率）
- 投稿比率16%に対し、インプレッション貢献55%（投資不足）
- 4投稿増加 × 9,875回/投稿 = 約40,000回増加

**実装方法**:
1. generate-x-posts スキルでLinkedIn向けコンテンツを追加生成（週4投稿分）
2. 成功パターン「概念反転」「衝撃的数値」を優先的に使用
3. 投稿時間を分散（月・水・金・日の8:00 JST）

**実行期限**: 次週（2026-01-17まで）
**担当スキル**: generate-x-posts（LinkedIn専用設定）
```

**優先度2（コンテンツ品質向上）**:
```markdown
#### 🎯 優先度2: 成功パターン活用率を10%→25%に向上（優先度スコア: 78/100）

**期待効果**: +35,000回（+25%）
**根拠**:
- トップ5投稿の60%が「概念反転」パターン使用
- 平均インプレッション23,590回（全体平均2,913回の8.1倍）
- 活用率15%向上により、約35,000回増加見込み

**実装方法**:
1. x_patterns_detailed.md のPattern #12「概念反転」、#07「衝撃的数値」、#23「権威引用」を重点活用
2. 汎用的AI情報（現在40%）を15%に削減
3. generate-x-posts スキルにバズ構造パラメータを明示指定

**実行期限**: 次週（2026-01-17まで）
**担当スキル**: generate-x-posts（パターン指定モード）
```

**優先度3（Threads最適化）**:
```markdown
#### 🎯 優先度3: Threads Views指標を活用した最適化（優先度スコア: 55/100）

**期待効果**: +5,000 views（間接効果）
**根拠**:
- Threads viewsフィールドでリーチ測定可能に（Late API PostAnalytics対応）
- 目標: 100 views/post、5 engagement/post
- views>0で正確なエンゲージメント率計算が可能

**実装方法**:
1. views数上位投稿のパターン分析を実施
2. 高エンゲージメント投稿との相関を確認
3. 成功パターンをgenerate-x-posts スキルに反映

**実行期限**: 次週（2026-01-17まで）
**担当スキル**: generate-x-posts（Threads設定）
```

#### 7-5. history.json更新（LLM推論）

**今週データの追加**:

1. 今週のKPIデータを構造化
2. history.jsonのweeks配列末尾に追加
3. 5週以上の古いデータを削除（4週間ローリングウィンドウ維持）

**更新ロジック**:
```python
# 既存データを読み込み
history = Read(file_path=history_path)

# 今週データを作成
new_week = {
    "week_id": f"{YYYY}-W{week_number}",
    "period_start": WEEK_AGO,
    "period_end": TODAY,
    "kpi": {
        "total_posts": total_posts,
        "total_impressions": total_impressions,
        "total_engagement": total_engagement,
        "engagement_rate": engagement_rate,
        "platforms": {
            "linkedin": {
                "posts": linkedin_posts,
                "impressions": linkedin_impressions,
                "engagement": linkedin_engagement,
                "engagement_rate": linkedin_engagement_rate,
                "avg_impressions_per_post": linkedin_avg_impressions
            },
            "x": {
                "posts": x_posts,
                "impressions": x_impressions,
                "engagement": x_engagement,
                "engagement_rate": x_engagement_rate,
                "avg_impressions_per_post": x_avg_impressions
            },
            "threads": {
                "posts": threads_posts,
                "views": threads_views,  # impressions → views に変更
                "engagement": threads_engagement,
                "engagement_rate": threads_engagement_rate,  # views>0の場合のみ
                "avg_views_per_post": threads_avg_views,
                "note": "viewsフィールド使用。0の場合はエンゲージメント絶対数で評価"
            },
            "facebook": {  # Chrome MCP経由で収集したデータ
                "views": facebook_views,  # 28日累計
                "interactions": facebook_interactions,
                "followers": facebook_followers,
                "net_followers": facebook_net_followers,
                "engagement_rate": facebook_engagement_rate,
                "data_source": "Professional Dashboard (Chrome MCP)",
                "data_quality": fb_data_quality,
                "note": "28日間累計データ（週次比較は変化率で評価）"
            }
        }
    },
    "top_posts": [
        # トップ5投稿データ
    ],
    "success_patterns": {
        "top_themes": [
            # 成功パターン集計
        ],
        "pattern_library_reference": "x_patterns_detailed.md",
        "high_performing_patterns": [
            # 高パフォーマンスパターンID
        ]
    }
}

# weeks配列に追加
history["weeks"].append(new_week)

# 4週間を超える古いデータを削除
if len(history["weeks"]) > 4:
    history["weeks"] = history["weeks"][-4:]  # 最新4件のみ保持

# last_updated更新
history["last_updated"] = TODAY

# 保存
Write(file_path=history_path, content=json.dumps(history, ensure_ascii=False, indent=2))
```

---

### STEP 8: 拡張レポート生成（1-2分）

**重要**: このステップでは report_template.md の拡張版を使用し、前週比較・トレンド分析・推奨アクションを含む200行の詳細レポートを生成します。

#### 8-1. 拡張テンプレート読み込み

```python
# 拡張版テンプレート（200行、77プレースホルダー）
template = Read(file_path="/Users/yuichi/AIPM/aipm_v0/.claude/skills/analyze-sns-performance-weekly/report_template.md")
```

#### 8-2. 追加プレースホルダー置換（LLM推論）

**前週比較セクション**（30行）:
- `{prev_impressions:,}` → 前週総インプレッション
- `{impressions_delta:,}` → 増減数
- `{impressions_delta_pct}` → 増減率（%）
- `{impressions_trend}` → トレンド評価（⬆️/➡️/⬇️）
- （同様に前週エンゲージメント、プラットフォーム別データ）

**トレンド分析セクション**（25行）:
- `{w3_period}` 〜 `{w0_period}` → 各週の期間
- `{w3_impressions:,}` 〜 `{w0_impressions:,}` → 各週のインプレッション
- `{w3_delta}%` 〜 `{w0_delta}%` → 各週の前週比
- `{w3_achievement}%` 〜 `{w0_achievement}%` → 各週の目標達成率
- `{monthly_pace:,}` → 月間換算ペース
- `{monthly_gap:,}` → 目標までの不足
- `{monthly_gap_pct}` → 不足率（%）
- `{achievement_forecast}` → 達成予測（✅/⚠️/❌）

**推奨アクションセクション**（15行）:
- `{recommended_actions_section}` → STEP 7で生成したTop 3アクション全文

**成功パターン分析セクション**（10行）:
- `{success_patterns_section}` → トップ5投稿の共通パターン分析
- `{pattern1_name}` 〜 `{pattern3_name}` → 活用推奨パターン名
- `{pattern1_description}` 〜 `{pattern3_description}` → パターン説明

#### 8-3. 拡張レポートファイル出力

```python
# 拡張レポート（200行、8セクション）
Write(file_path=REPORT_FILE, content=filled_extended_template)
```

**出力セクション構成**:
1. 📊 エグゼクティブサマリー（既存）
2. 📈 プラットフォーム別サマリー（既存）
3. 🎯 KPI達成状況（既存）
4. 🏆 トップ5投稿（既存）
5. **🔄 前週比較**（新規）
6. **📊 トレンド分析（過去4週）**（新規）
7. **🎯 推奨アクション（優先度順）**（新規）
8. **📚 成功パターン分析（過去4週）**（新規）

---

## スキル引数

スキル実行時に期間を指定できます（オプション）:

```bash
/analyze-sns-performance-weekly --start-date 2026-01-01 --end-date 2026-01-11
```

**引数**:
- `--start-date`: 分析開始日（YYYY-MM-DD形式）
- `--end-date`: 分析終了日（YYYY-MM-DD形式）

**デフォルト動作**（引数省略時）:
- start-date: 実行日の7日前
- end-date: 実行日

**注意**:
- Facebook収集時は `since_date={start-date}`, `until_date={end-date}` として collect-facebook-performance に渡されます
- Late API収集時も同じ期間が使用されます
- 期間は最大90日（Facebook Professional Dashboard制約）

---
