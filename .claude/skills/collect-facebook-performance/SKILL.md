---
name: collect-facebook-performance
description: |
  Facebook個人アカウント（プロフェッショナルモード）のProfessional Dashboardから
  投稿パフォーマンス（閲覧数、インタラクション、オーディエンス）を収集するスキル。
  Claude in Chrome MCPを使用したブラウザ自動化で、インサイトデータを構造化して取得します。

  **NEW**: タイムラインから投稿の全文テキストを抽出する機能を追加。
  「さらに表示」ボタンをクリックして省略されていない完全なテキストを取得します。

  使用タイミング：
  - 週次SNSパフォーマンス分析時
  - Facebook投稿の効果測定時
  - オーディエンス分析時
  - 投稿コンテンツの全文分析時

  所要時間：20-30分
  出力：fb_performance_{YYYY-MM-DD}.json（インサイトデータ + 投稿詳細 + Content Library + 全文テキスト）
trigger_keywords:
  - "Facebookパフォーマンス収集"
  - "Facebook分析"
  - "FBインサイト収集"
  - "Facebookダッシュボード"
stage: Data Collection
dependencies: []
output_file: Stock/programs/副業/projects/SNS/data/fb_performance_{YYYY-MM-DD}.json
execution_time: 20-30分
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
6. **投稿全文抽出（NEW）**: タイムラインから「さらに表示」をクリックして投稿の完全なテキストを取得

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
| **入力** | 開始日（since_date: YYYY-MM-DD）、終了日（until_date: YYYY-MM-DD）、Chromeログインセッション |
| **出力** | fb_performance_{YYYY-MM-DD}.json（インサイト + 投稿詳細） |
| **次のアクション** | 週次分析、SNS戦略立案、投稿最適化 |
| **注意** | since_date/until_date未指定時はデフォルト28日間 |

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

### STEP 1.5: 期間フィルター設定（2-3分）【NEW】

**目的**: Professional Dashboardで指定期間のデータのみ取得するため、日付フィルターを設定

**アクセスURL**: `https://www.facebook.com/professional_dashboard/profile_insights/views`

**Chrome MCPツール使用**:
```
1. navigate(url="https://www.facebook.com/professional_dashboard/profile_insights/views", tabId=tab_id)
   → Views ページへ遷移

2. wait(duration=3)
   → ダッシュボードロード待機

3. screenshot(tabId=tab_id)
   → 初期状態確認（28日間表示）

4. find(query="過去28日間", tabId=tab_id)
   → 右上の日付選択ボタンを検索（例: "過去28日間: 12月15日 ～ 1月11日"）

5. left_click(ref=date_button_ref, tabId=tab_id)
   → ドロップダウンメニュー展開

6. wait(duration=1)
   → メニュー展開待機

7. find(query="カスタム", tabId=tab_id)
   → "カスタム" オプションを検索

8. left_click(ref=custom_option_ref, tabId=tab_id)
   → カスタム期間選択

9. wait(duration=1)
   → カレンダーUI表示待機

10. JavaScript tool で日付選択:
    ```javascript
    // since_date（例: 2026-01-01）から until_date（例: 2026-01-11）を選択
    // カレンダーグリッドから該当日をクリック
    const startDate = new Date('{since_date}');
    const endDate = new Date('{until_date}');

    // グリッドセルを検索してクリック
    const cells = document.querySelectorAll('[role="gridcell"]');
    // 実装は日付に応じて動的にクリック
    ```

11. find(query="適用", tabId=tab_id)
    → "適用" ボタンを検索

12. left_click(ref=apply_button_ref, tabId=tab_id)
    → フィルター適用

13. wait(duration=3)
    → データ再読み込み待機

14. screenshot(tabId=tab_id)
    → フィルター適用後の状態確認
```

**DOM構造（2026年1月時点、実機確認済み）**:
```
button "過去28日間: 12月15日 ～ 1月11日"  ← 日付フィルターボタン
  → ドロップダウンメニュー展開
    menuitem "今日"
    menuitem "過去7日間: 1月5日 ～ 1月11日"
    menuitem "過去14日間: 12月29日 ～ 1月11日"
    menuitem "過去28日間: 12月15日 ～ 1月11日"（デフォルト選択）
    menuitem "過去60日間: 11月13日 ～ 1月11日"
    menuitem "過去90日間: 10月14日 ～ 1月11日"
    menuitem "カスタム"  ← これをクリック
      → カレンダーダイアログ表示
        button "前月"
        button "翌月"
        grid [role="grid"] "日付を選択"
          gridcell × 35（日付セル）
        button "戻る"
        button "適用"
```

**エラーハンドリング**:

| エラー | 対応 |
|--------|------|
| 日付ボタンが見つからない | スクリーンショット撮影 → 手動確認依頼 |
| カスタム期間オプションがない | プリセット（7日/60日）で代替 |
| カレンダーUI操作失敗 | JavaScript tool で直接DOM操作 |
| フィルター適用失敗 | 3回リトライ後、28日間データで継続 |

**制約事項**:
- 最大期間: 90日間（Facebook Professional Dashboard制限）
- 過去データのみ（未来日付は指定不可）
- 最小期間: 1日間

---

### STEP 3: 閲覧数（Views）データ収集（2-3分）

**前提**: STEP 1.5で設定した期間フィルターが適用済み

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

**前提**: STEP 1.5で設定した期間フィルターが適用済み

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

**前提**: STEP 1.5で設定した期間フィルターが適用済み

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

**前提**: STEP 1.5で設定した期間フィルターが適用済み

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

**ストーリーズ除外ルール**:
- `content_type: "story"` の投稿は収集対象から**除外**
- ストーリーズは24時間で消える一時的なコンテンツのため、長期分析に不向き
- Content Library上で「ストーリーズ」タブや「Story」ラベルがある場合はスキップ
- フィルタリング: 投稿タイプが「写真」「動画」「テキスト」「リール」のみを対象

---

### STEP 7: タイムライン全文抽出（5-8分）【NEW】

**前提**: STEP 1.5で設定した期間フィルターが適用済み（プロフィールタイムラインでは表示される投稿が指定期間に限定）

**目的**: Content Libraryでは投稿タイトルのみ取得可能なため、タイムラインから投稿の完全なテキストを抽出する。

**アクセスURL**: `https://www.facebook.com/me` または `https://www.facebook.com/{ユーザーID}`

**Chrome MCPツール使用**:
```
1. navigate(url="https://www.facebook.com/me", tabId=tab_id)
   → 自分のプロフィールページへ遷移（/ユーザーID/にリダイレクト）

2. wait(duration=3)
   → ページロード待機

3. screenshot(tabId=tab_id)
   → プロフィールページ確認

4. scroll(direction="down", amount=3, tabId=tab_id)
   → 投稿セクションまでスクロール

5. 「さらに表示」ボタンのクリック（各投稿ごと）:
   a. find(query="さらに表示", tabId=tab_id)
      → 「さらに表示」ボタンを検索（複数見つかる場合あり）

   b. left_click(ref=button_ref, tabId=tab_id)
      → ボタンをクリックして全文展開

   c. wait(duration=2)
      → 展開待機

6. javascript_tool でテキスト抽出:
   ```javascript
   const articles = document.querySelectorAll('[role="article"]');
   const posts = [];
   articles.forEach((article, index) => {
     if (index >= 10) return; // 最大10投稿
     const textElements = article.querySelectorAll('[dir="auto"]');
     let fullText = '';
     textElements.forEach(el => {
       if (el.textContent && el.textContent.length > 100
           && el.textContent.length > fullText.length) {
         fullText = el.textContent;
       }
     });
     if (fullText) {
       posts.push({
         index: index,
         text_preview: fullText.substring(0, 100),
         text_length: fullText.length,
         has_see_more: fullText.includes('さらに表示')
       });
     }
   });
   JSON.stringify(posts, null, 2);
   ```

7. スクロール + 繰り返し（最大10-15投稿）:
   a. scroll(direction="down", amount=3, tabId=tab_id)
   b. wait(duration=2)
   c. find(query="さらに表示", tabId=tab_id) で新しいボタンを検索
   d. 次の投稿の「さらに表示」をクリック
   e. javascript_tool で投稿テキストを抽出
```

**DOM構造（2026年1月時点、動作確認済み）**:
```
[role="article"]              ← 各投稿のコンテナ
  heading "投稿者名"           ← 投稿者
  link "日時"                 ← 投稿日時・詳細リンク（/posts/pfbid...）
  [dir="auto"]                ← 本文テキスト（複数存在）
    button "さらに表示"        ← 全文展開ボタン（省略されている場合のみ）

※ [dir="auto"] 要素のうち、textContent.length が最大のものが投稿本文
※ 「さらに表示」クリック後は、同じ [dir="auto"] 内に全文が展開される
```

**セレクタ**:
- 投稿コンテナ: `document.querySelectorAll('[role="article"]')`
- テキスト要素: `article.querySelectorAll('[dir="auto"]')`
- 展開ボタン: `find(query="さらに表示")` で検索

**「さらに表示」クリック後の全文取得**:
```
クリック前: "「ホワイトカラーの仕事は真っ先に消える」。イーロン・マスクが放ったこの一言..."

クリック後: "「ホワイトカラーの仕事は真っ先に消える」。
イーロン・マスクが放ったこの一言、マジで背筋が凍る件。
最新のインタビューで彼は、「原子（アトム）を動かさない仕事なら、
AIは今すぐにでも半分以上代替できる」と断言した。

これ、脅しでも何でもない。ただの未来予測だ。
..." (完全なテキスト)
```

**取得データ**:
```json
{
  "timeline_posts": [
    {
      "post_id": "pfbid02xxxxx",
      "published_at": "2026-01-11T19:32:00+09:00",
      "full_text": "「ホワイトカラーの仕事は真っ先に消える」。\nイーロン・マスクが放ったこの一言、マジで背筋が凍る件。\n\n最新のインタビューで彼は、「原子（アトム）を動かさない仕事なら、AIは今すぐにでも半分以上代替できる」と断言した。\n\nこれ、脅しでも何でもない。ただの未来予測だ。\n\nただ、私たちは今、「シンギュラリティ（技術的特異点）」の真っ只中にいる。\nこれまでの常識だった「良い大学を出て、オフィスでPCを叩く仕事」が、最も価値のないスキルになろうとしている。\n\nなぜ？\n答えは単純だ。PC上の操作はすべてデジタル情報処理であり、AIが最も得意とする領域だからだ。\n...",
      "text_length": 1247,
      "has_media": true,
      "reactions_count": 55,
      "comments_count": 2,
      "shares_count": 10
    }
  ]
}
```

**抽出戦略**:

| 項目 | 設定 |
|------|------|
| **最大投稿数** | 10-15件（過去7日分程度） |
| **スクロール回数** | 最大5回 |
| **各投稿間の待機** | 2-3秒（人間的な操作パターン） |
| **「さらに表示」クリック後待機** | 2秒 |
| **タイムアウト** | 投稿あたり最大10秒 |
| **ストーリーズ除外** | ストーリーズセクションはスキップ（通常投稿のみ対象） |

**Content Libraryとの紐付け**:
```
Content Library: title = "ホワイトカラーの仕事は真っ..."
Timeline:        full_text = "「ホワイトカラーの仕事は真っ先に消える」。イーロン・マスクが..."

→ titleの先頭部分でマッチングし、full_textを紐付け
```

**エラーハンドリング**:

| エラー | 対応 |
|--------|------|
| 「さらに表示」ボタンが見つからない | 現在表示されているテキストをそのまま使用 |
| クリック失敗 | 3回リトライ後スキップ |
| DOM構造変更 | スクリーンショット + LLM推論でフォールバック |
| 投稿が画像/動画のみ | full_text = null として記録 |

---

### STEP 8: データ統合・出力（1分）

**統合データフォーマット**:
```json
{
  "collected_at": "2026-01-12T10:30:00+09:00",
  "platform": "facebook",
  "account_type": "personal_professional",
  "period": "{since_date} ~ {until_date}",
  "period_days": "{計算された日数: (until - since).days + 1}",

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

  "timeline_posts": {
    "posts_count": 10,
    "extraction_method": "timeline_see_more_click",
    "posts": [
      {
        "post_id": "pfbid02xxxxx",
        "published_at": "2026-01-11T19:32:00+09:00",
        "title_preview": "ホワイトカラーの仕事は真っ...",
        "full_text": "「ホワイトカラーの仕事は真っ先に消える」。\nイーロン・マスクが放ったこの一言、マジで背筋が凍る件。\n\n最新のインタビューで彼は、「原子（アトム）を動かさない仕事なら、AIは今すぐにでも半分以上代替できる」と断言した。\n\nこれ、脅しでも何でもない。ただの未来予測だ。\n\nただ、私たちは今、「シンギュラリティ（技術的特異点）」の真っ只中にいる。\nこれまでの常識だった「良い大学を出て、オフィスでPCを叩く仕事」が、最も価値のないスキルになろうとしている。\n\nなぜ？\n答えは単純だ。PC上の操作はすべてデジタル情報処理であり、AIが最も得意とする領域だからだ。\n\n一方で、物理的な世界で動く「人型ロボット（Optimus）」の進化も異常だ。\nイーロンは「3年以内に、ロボットは人間の外科医よりも上手く手術できるようになる」と予言している。\n\nつまり、知的労働も肉体労働も、AIとロボットが「人間超え」するのは時間の問題ということだ。\n\nポイントは、これが「10年後」の話ではなく、「来年」「3年後」の話だという点にある。\nAGI（汎用人工知能）は、早ければ2026年にも登場する。\n\nこの変化のスピードは、企業や政府の対応能力を遥かに超えている。\nイーロン自身も「次の3〜7年はバンピー（でこぼこ）な道のりになる」と警告している。\n\nしかし、ここからが本当の話だ。\nこの変化は、圧倒的な「豊かさ」への入り口でもある。\n労働コストがゼロに近づけば、商品やサービスは限りなく無料に近づく。\n\n問題は立ち止まるか、新しいツールを使い倒して「拡張された人間」になるか。",
        "text_length": 892,
        "has_media": false,
        "reactions_count": 55,
        "comments_count": 2,
        "shares_count": 10,
        "content_library_match": true
      }
    ],
    "match_rate": 0.85
  },

  "quality_score": {
    "data_completeness": 98.0,
    "views_captured": true,
    "interactions_captured": true,
    "audience_captured": true,
    "content_library_captured": true,
    "timeline_posts_captured": true,
    "posts_count": 20,
    "full_text_count": 10,
    "full_text_match_rate": 0.85,
    "stories_excluded": true
  },

  "filter_settings": {
    "exclude_stories": true,
    "included_content_types": ["photo", "text", "multi_photo", "reels", "video"],
    "excluded_content_types": ["story"]
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
- 2026-01-12: Content Library対応追加（投稿別詳細データ収集）
  - 各投稿の閲覧数、閲覧者数、インタラクション、収益、インプレッション、コメント、新フォロー数を取得
  - STEP 6としてContent Library収集ステップを追加
  - 出力JSONにcontent_libraryセクションを追加
- 2026-01-12: **タイムライン全文抽出機能追加**
  - STEP 7としてタイムラインからの投稿全文抽出ステップを追加
  - `https://www.facebook.com/me` にアクセスし、各投稿の「さらに表示」ボタンをクリックして全文を取得
  - DOM構造: `[role="article"] > [dir="auto"] > button "さらに表示"`
  - Content Libraryのtitleと紐付けて完全なテキストデータを提供
  - 出力JSONに`timeline_posts`セクションを追加（full_text, text_length, content_library_match等）
  - 所要時間: 15-20分 → 20-30分に更新
- 2026-01-12: **STEP 7にJavaScript抽出コード追加**
  - 動作確認テストで検証済みのDOM構造とセレクタを反映
  - `document.querySelectorAll('[role="article"]')` で投稿コンテナを取得
  - `article.querySelectorAll('[dir="auto"]')` でテキスト要素を取得
  - textContent.length が最大の要素を投稿本文として抽出
  - テスト結果: 828文字、652文字の全文抽出に成功
- 調査結果: Professional Dashboardで閲覧数・インタラクション・オーディエンス取得可能を確認
- 調査結果: Content Library（/content/content_library）で投稿別詳細データ取得可能を確認
- 調査結果: タイムライン（/me）で「さらに表示」クリックにより投稿全文取得可能を確認
- 2026-01-12: **ストーリーズ除外機能追加**
  - Content Library収集時に`content_type: "story"`を除外
  - タイムライン抽出時もストーリーズセクションをスキップ
  - 出力JSONに`filter_settings`セクションを追加（除外設定の明示化）
  - 対象コンテンツタイプ: photo, text, multi_photo, reels, video のみ
- 2026-01-12: **カスタム期間指定機能追加（STEP 1.5）**
  - Professional Dashboardの日付フィルターUI操作により、指定期間のデータ収集を実現
  - STEP 1.5を追加: 日付フィルターボタン → ドロップダウン → "カスタム" → カレンダー選択 → "適用"
  - 入力仕様変更: since_date（開始日）、until_date（終了日）パラメータ追加
  - データ構造変更: period と period_days を動的計算（`{since_date} ~ {until_date}`, `(until - since).days + 1`）
  - STEP 3〜7に前提条件追加: "STEP 1.5で設定した期間フィルターが適用済み"
  - 最大期間制限: 90日（Facebook Professional Dashboard制約）
  - デフォルト動作: since_date/until_date未指定時は従来通り28日間
  - 調査結果: Facebook Professional Dashboard実機でUI構造確認（button "過去28日間" → menuitem "カスタム" → grid[role="grid"]）
