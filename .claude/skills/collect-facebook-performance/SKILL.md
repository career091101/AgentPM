---
name: collect-facebook-performance
description: |
  Facebook個人アカウント（プロフェッショナルモード）のProfessional Dashboardから
  投稿パフォーマンス（閲覧数、インタラクション、オーディエンス）を収集するスキル。
  Claude in Chrome MCPを使用したブラウザ自動化で、インサイトデータを構造化して取得します。

  使用タイミング：
  - 週次SNSパフォーマンス分析時
  - Facebook投稿の効果測定時
  - オーディエンス分析時

  所要時間：15-20分
  出力：fb_performance_{YYYY-MM-DD}.json（インサイトデータ + 投稿詳細 + Content Library）
trigger_keywords:
  - "Facebookパフォーマンス収集"
  - "Facebook分析"
  - "FBインサイト収集"
  - "Facebookダッシュボード"
stage: Data Collection
dependencies: []
output_file: Stock/programs/副業/projects/SNS/data/fb_performance_{YYYY-MM-DD}.json
execution_time: 15-20分
framework_reference: Stock/programs/副業/projects/SNS/
priority: P2
---

# Collect Facebook Performance Skill

Facebook Professional Dashboardからのパフォーマンスデータ収集スキル。

---

## このSkillでできること

1. **閲覧数（インプレッション）収集**: 総閲覧数、閲覧者数、3秒/1分再生数
2. **インタラクション収集**: リアクション、コメント、シェア数（投稿別）
3. **オーディエンス分析**: フォロワー数、年齢/性別/地域分布
4. **投稿別詳細（Content Library）**: 各投稿の閲覧数・閲覧者数・インタラクション・収益・インプレッション・コメント・新フォロー数
5. **トレンド分析**: 過去28日間の推移データ

---

## 前提条件

| 項目 | 要件 |
|------|------|
| **アカウントタイプ** | 個人アカウント（プロフェッショナルモードON） |
| **ブラウザ** | Chrome（Facebookにログイン済み） |
| **Chrome MCP** | claude-in-chrome 拡張機能が有効 |

### プロフェッショナルモード確認方法
1. Facebook → 設定 → プロフィール設定
2. 「プロフェッショナルモード」がONになっていることを確認
3. ONでない場合は有効化が必要（インサイトデータが表示されない）

---

## 入力・出力

| 項目 | 内容 |
|------|------|
| **入力** | 期間（デフォルト: 過去28日間）、Chromeログインセッション |
| **出力** | fb_performance_{YYYY-MM-DD}.json（インサイト + 投稿詳細） |
| **次のアクション** | 週次分析、SNS戦略立案、投稿最適化 |

---

## Instructions

**実行モード**: 半自動（ログイン確認が必要）
**推定所要時間**: 10-15分

### STEP 1: Chrome MCP接続確認（1分）

**Chrome MCPツール使用**:
```
1. tabs_context_mcp(createIfEmpty=True)
   → タブコンテキスト初期化

2. tabs_create_mcp()
   → 新規タブ作成、tab_id取得

3. navigate(url="https://www.facebook.com", tabId=tab_id)
   → Facebookトップへ遷移

4. wait(duration=3)
   → ページロード待機

5. screenshot(tabId=tab_id)
   → ログイン状態確認
```

**ログイン状態判定**:
- プロフィールアイコン表示 → ログイン済み（続行）
- ログインフォーム表示 → 未ログイン（ユーザーに手動ログイン依頼）

**未ログイン時の対応**:
```markdown
Facebookにログインされていません。
以下の手順でログインしてください：

1. 開いたChromeタブでFacebookにログイン
2. ログイン完了後、こちらに戻ってください
3. 「続行」と入力してデータ収集を再開します

※ セキュリティ上、自動ログインは行いません
```

---

### STEP 2: Professional Dashboard遷移（1分）

**Chrome MCPツール使用**:
```
1. navigate(url="https://www.facebook.com/professional_dashboard", tabId=tab_id)
   → Professional Dashboardへ遷移

2. wait(duration=3)
   → ページロード待機

3. screenshot(tabId=tab_id)
   → ダッシュボード表示確認
```

**Professional Dashboard確認項目**:
- 「インサイト」セクション表示あり → 続行
- 「プロフェッショナルモードをオンにする」表示 → ユーザーに有効化依頼

---

### STEP 3: 閲覧数（Views）データ収集（2-3分）

**アクセスURL**: `https://www.facebook.com/professional_dashboard/profile_insights/views`

**Chrome MCPツール使用**:
```
1. navigate(url="https://www.facebook.com/professional_dashboard/profile_insights/views", tabId=tab_id)

2. wait(duration=2)

3. screenshot(tabId=tab_id)
   → 閲覧数ページ確認

4. read_page(tabId=tab_id, depth=15)
   → アクセシビリティツリーでDOM構造取得

5. LLM推論でデータ抽出
   → スクリーンショット + アクセシビリティツリーから数値を抽出
```

**取得データ**:
```json
{
  "total_views": 302261,
  "change_percent": "+220.4%",
  "viewers": 91572,
  "video_3s_plays": 1835,
  "video_1m_plays": 0,
  "by_content_type": {
    "photo": 71.8,
    "text": 23.6,
    "multi_photo": 2.6,
    "reels": 1.9,
    "other": 0.2
  },
  "audience_split": {
    "followers": 22.8,
    "non_followers": 77.2
  },
  "posts": [
    {"date": "2026-01-11", "time": "19:42", "views": 4413},
    {"date": "2026-01-10", "time": "19:00", "views": 23928}
  ]
}
```

---

### STEP 4: インタラクションデータ収集（2-3分）

**アクセスURL**: `https://www.facebook.com/professional_dashboard/profile_insights/interactions`

**Chrome MCPツール使用**:
```
1. navigate(url="https://www.facebook.com/professional_dashboard/profile_insights/interactions", tabId=tab_id)

2. wait(duration=2)

3. screenshot(tabId=tab_id)
   → インタラクションページ確認

4. read_page(tabId=tab_id, depth=15)
   → DOM構造取得

5. LLM推論でデータ抽出
```

**取得データ**:
```json
{
  "total_interactions": 2295,
  "change_percent": "+146.0%",
  "breakdown": {
    "reactions": 1893,
    "comments": 210,
    "shares": 192
  },
  "by_type_percent": {
    "reactions": 82.5,
    "comments": 9.2,
    "shares": 8.4
  },
  "audience_split": {
    "followers": 55.4,
    "non_followers": 44.6
  },
  "posts": [
    {"date": "2026-01-11", "time": "19:32", "interactions": 73},
    {"date": "2026-01-10", "time": "19:06", "interactions": 163}
  ]
}
```

---

### STEP 5: オーディエンスデータ収集（2-3分）

**アクセスURL**: `https://www.facebook.com/professional_dashboard/profile_insights/audience`

**Chrome MCPツール使用**:
```
1. navigate(url="https://www.facebook.com/professional_dashboard/profile_insights/audience", tabId=tab_id)

2. wait(duration=2)

3. screenshot(tabId=tab_id)
   → オーディエンスページ確認

4. read_page(tabId=tab_id, depth=15)
   → DOM構造取得

5. LLM推論でデータ抽出
```

**取得データ**:
```json
{
  "total_followers": 6647,
  "change_percent": "+3.8%",
  "net_followers": 236,
  "unfollows": 37,
  "demographics": {
    "age": {
      "35-44": 28.2,
      "45-54": 26.7,
      "25-34": 17.7,
      "55-64": 17.3,
      "65+": 8.2,
      "18-24": 1.9
    },
    "top_cities": [
      {"city": "横浜市", "percent": 20.4},
      {"city": "渋谷区", "percent": 17.6},
      {"city": "川崎市", "percent": 10.2},
      {"city": "港区", "percent": 10.2},
      {"city": "目黒区", "percent": 8.3},
      {"city": "大阪市", "percent": 7.4}
    ],
    "top_countries": [
      {"country": "日本", "percent": 92.7},
      {"country": "米国", "percent": 1.7},
      {"country": "インドネシア", "percent": 1.4},
      {"country": "中国", "percent": 1.1},
      {"country": "ガーナ", "percent": 0.6},
      {"country": "シンガポール", "percent": 0.6}
    ]
  }
}
```

---

### STEP 6: Content Libraryデータ収集（3-5分）【メイン】

**アクセスURL**: `https://www.facebook.com/professional_dashboard/content/content_library`

**Chrome MCPツール使用**:
```
1. navigate(url="https://www.facebook.com/professional_dashboard/content/content_library", tabId=tab_id)

2. wait(duration=3)

3. screenshot(tabId=tab_id)
   → Content Libraryページ確認

4. read_page(tabId=tab_id, depth=20)
   → 投稿一覧テーブルのDOM構造取得

5. LLM推論で投稿データ抽出
   → 各行のデータをパース

6. scroll(direction="down", amount=5, tabId=tab_id)
   → 追加の投稿を読み込み

7. 必要に応じてスクロール + read_page を繰り返し
   → 最大50件または7日分まで取得
```

**取得データ（各投稿ごと）**:
```json
{
  "posts": [
    {
      "post_id": "pfbid_xxxxx",
      "title": "ホワイトカラーの仕事は真っ...",
      "published_at": "2026-01-11 19:32",
      "content_type": "text",
      "metrics": {
        "views": 4492,
        "viewers": 2658,
        "interactions": 73,
        "revenue": 0.51,
        "new_followers": 0,
        "impressions": 3005,
        "comments": 3
      }
    },
    {
      "post_id": "pfbid_yyyyy",
      "title": "OpenAIが「ひっそり公開」した...",
      "published_at": "2026-01-10 18:58",
      "content_type": "photo",
      "metrics": {
        "views": 24039,
        "viewers": 16071,
        "interactions": 163,
        "revenue": 1.59,
        "new_followers": 13,
        "impressions": 16984,
        "comments": 1
      }
    }
  ]
}
```

**Content Libraryカラム定義**:

| カラム | 説明 | 用途 |
|--------|------|------|
| **プレビュー** | サムネイル + タイトル + 公開日時 | 投稿特定 |
| **閲覧数** | 総閲覧回数 | リーチ評価 |
| **閲覧者数** | ユニーク閲覧者数 | 実質リーチ |
| **インタラクション** | 総インタラクション数 | エンゲージメント |
| **収益** | 推定収益（USD） | 収益化評価 |
| **新フォロー数** | 投稿経由の新規フォロワー | 成長寄与 |
| **インプレッション** | 表示回数 | 配信効率 |
| **コメント** | コメント数 | 会話指標 |

**スクロール戦略**:
```
初回読み込み: 約15-20件表示
スクロール1回: +10-15件追加
最大スクロール: 5回（約50件）
待機時間: 各スクロール後2秒
```

**データ検証**:
- 閲覧数 ≥ 閲覧者数（必須）
- インプレッション ≥ インタラクション（必須）
- 公開日時が期間内（28日以内）

---

### STEP 7: データ統合・出力（1分）

**統合データフォーマット**:
```json
{
  "collected_at": "2026-01-12T10:30:00+09:00",
  "platform": "facebook",
  "account_type": "personal_professional",
  "period": "2025-12-15 ~ 2026-01-11",
  "period_days": 28,

  "summary": {
    "total_views": 302261,
    "total_interactions": 2295,
    "total_followers": 6647,
    "total_revenue": 30.01,
    "views_change": "+220.4%",
    "interactions_change": "+146.0%",
    "followers_change": "+3.8%"
  },

  "views": {
    "total": 302261,
    "viewers": 91572,
    "video_3s_plays": 1835,
    "video_1m_plays": 0,
    "by_content_type": {
      "photo": 71.8,
      "text": 23.6,
      "multi_photo": 2.6,
      "reels": 1.9,
      "other": 0.2
    },
    "audience_split": {
      "followers": 22.8,
      "non_followers": 77.2
    }
  },

  "interactions": {
    "total": 2295,
    "reactions": 1893,
    "comments": 210,
    "shares": 192,
    "audience_split": {
      "followers": 55.4,
      "non_followers": 44.6
    }
  },

  "audience": {
    "total_followers": 6647,
    "net_followers": 236,
    "unfollows": 37,
    "demographics": {
      "age": {
        "35-44": 28.2,
        "45-54": 26.7,
        "25-34": 17.7,
        "55-64": 17.3,
        "65+": 8.2,
        "18-24": 1.9
      },
      "top_cities": [],
      "top_countries": []
    }
  },

  "content_library": {
    "posts_count": 20,
    "total_views": 152847,
    "total_viewers": 98234,
    "total_interactions": 1456,
    "total_revenue": 18.52,
    "total_impressions": 125678,
    "total_comments": 89,
    "total_new_followers": 78,
    "posts": [
      {
        "post_id": "pfbid_xxxxx",
        "title": "ホワイトカラーの仕事は真っ...",
        "published_at": "2026-01-11T19:32:00+09:00",
        "content_type": "text",
        "metrics": {
          "views": 4492,
          "viewers": 2658,
          "interactions": 73,
          "revenue": 0.51,
          "new_followers": 0,
          "impressions": 3005,
          "comments": 3
        },
        "engagement_rate": 1.63
      }
    ],
    "top_posts": [
      {
        "rank": 1,
        "post_id": "pfbid_top1",
        "title": "6年後、プログラマーは1人も...",
        "views": 51409,
        "interactions": 221,
        "revenue": 3.32,
        "new_followers": 29
      }
    ]
  },

  "quality_score": {
    "data_completeness": 98.0,
    "views_captured": true,
    "interactions_captured": true,
    "audience_captured": true,
    "content_library_captured": true,
    "posts_count": 20
  }
}
```

**保存先**: `Stock/programs/副業/projects/SNS/data/fb_performance_{YYYY-MM-DD}.json`

---

## エラーハンドリング

### 未ログイン
- **検出**: スクリーンショットでログインフォーム表示
- **対応**: ユーザーに手動ログイン依頼、ログイン後に再実行

### プロフェッショナルモード未有効
- **検出**: Professional Dashboard非表示
- **対応**: ユーザーにプロフェッショナルモード有効化を依頼
- **手順案内**:
  ```
  プロフェッショナルモードが有効になっていません。
  以下の手順で有効化してください：

  1. Facebook → 自分のプロフィール
  2. 「...」メニュー → 「プロフェッショナルモードをオンにする」
  3. 指示に従って設定完了
  4. 完了後、このスキルを再実行
  ```

### DOM構造変更
- **検出**: read_page() でデータ取得失敗
- **対応**: スクリーンショット + LLM推論でフォールバック

### レート制限
- **検出**: ページ読み込みエラー
- **対応**: 5分待機後にリトライ（最大3回）

### 部分データ
- **検出**: 一部セクションのデータ取得失敗
- **対応**: 取得成功したデータのみ保存、警告付きで続行

---

## ToS違反リスク軽減策

### 人間的な操作パターン
- **ページ遷移間隔**: 2-3秒
- **スクロール**: scroll_amount=3-5
- **セッション上限**: 15分/回

### 実行頻度制限
- **推奨**: 週1回
- **最大**: 1日1回

### 対象限定
- 自己アカウントのみ
- 公開されているインサイトデータのみ取得

---

## 既存スキルとの統合

### analyze-sns-performance-weekly への統合

`analyze-sns-performance-weekly/SKILL.md` に以下を追加：

```markdown
### Facebook集計

**データソース**: `fb_performance_{YYYY-MM-DD}.json`

**集計項目**:
- 総閲覧数: summary.total_views
- 総インタラクション: summary.total_interactions
- フォロワー増減: audience.net_followers
- 平均インタラクション/投稿: interactions.total / posts.length
```

### sns-automation への統合

Phase 1 のデータ収集ステップにオプションとして追加：

```markdown
### STEP 1.5: Facebookパフォーマンス収集（オプション）

**実行条件**: 前回実行から7日以上経過
**実行モード**: 並列（X収集と同時実行可能）
**失敗時**: 警告のみ
```

---

## 使用例

### 基本的な使用

```
User: Facebookパフォーマンス収集
```

システムが自動的に：
1. Chrome MCP接続確認
2. Facebookログイン状態確認
3. Professional Dashboard遷移
4. 閲覧数データ収集
5. インタラクションデータ収集
6. オーディエンスデータ収集
7. JSON出力生成

---

## 調査結果（2026-01-12）

Professional Dashboardで確認した実際のデータ：

| メトリクス | 値 |
|-----------|-----|
| 総閲覧数 | 302,261 (+220.4%) |
| 閲覧者 | 91,572 |
| 総インタラクション | 2,295 (+146.0%) |
| リアクション | 1,893 |
| コメント | 210 |
| シェア | 192 |
| フォロワー | 6,647 (+3.8%) |
| 純フォロー | 236 |

---

## 更新履歴

- 2026-01-12: 初版作成（Chrome MCP対応）
- 調査結果: Professional Dashboardで閲覧数・インタラクション・オーディエンス取得可能を確認
