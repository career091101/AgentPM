# Phase 3.5: 投稿メディア・リプライ情報取得 実装計画

## エグゼクティブサマリー

Phase 3で取得した818件の完全テキストに対し、以下の情報を追加取得：

1. **全投稿の画像/動画メタデータ**（現在は4件のみ）
2. **リプライ欄の情報**（ユーザー反応、ソースURL等）
3. **読み込み待機時間の延長**（3秒 → 8秒）

**推定実行時間**: 約6.8時間（818件 × 30秒/件）

---

## 1. 実装概要

### 新規スクリプト作成

**ファイル名**: `x_bookmark_media_replies_enricher.py`

**理由**:
- 既存の`x_bookmark_expander.py`は全文展開に特化
- メディア・リプライ取得は独立した処理フェーズ
- Phase 3完了済みデータ（v2.json）を入力とする

### データフロー

```
x_bookmarks_data_fulltext_v2.json (Phase 3完了)
    ↓
x_bookmark_media_replies_enricher.py (Phase 3.5)
    ↓
x_bookmarks_data_enriched.json (最終版)
```

---

## 2. 実装設計

### 2.1 データ構造拡張

#### 既存データ（Phase 3完了時）

```json
{
  "id": "1234567890",
  "text": "[完全な本文]",
  "url": "https://x.com/user/status/1234567890",
  "author_username": "user",
  "expanded": true,
  "expanded_at": "2025-12-31T19:15:32"
}
```

#### 拡張後データ（Phase 3.5完了時）

```json
{
  "id": "1234567890",
  "text": "[完全な本文]",
  "url": "https://x.com/user/status/1234567890",
  "author_username": "user",
  "expanded": true,
  "expanded_at": "2025-12-31T19:15:32",

  "media": {
    "images": [
      {
        "url": "https://pbs.twimg.com/media/...",
        "alt": "Image description",
        "width": 1200,
        "height": 675
      }
    ],
    "videos": [
      {
        "poster": "https://pbs.twimg.com/...",
        "aria_label": "Embedded video",
        "duration": "0:45"
      }
    ],
    "extracted_at": "2025-12-31T21:30:45"
  },

  "replies": {
    "count": 15,
    "top_replies": [
      {
        "author": "reply_user1",
        "text": "Great insight! Here's the source: https://...",
        "likes": 42,
        "posted_at": "2025-12-30T10:15:00Z",
        "urls": ["https://example.com/article"]
      },
      {
        "author": "reply_user2",
        "text": "This is similar to what was discussed here https://...",
        "likes": 28,
        "posted_at": "2025-12-30T11:20:00Z",
        "urls": ["https://another-source.com"]
      }
    ],
    "has_source_urls": true,
    "source_urls": [
      "https://example.com/article",
      "https://another-source.com"
    ],
    "extracted_at": "2025-12-31T21:30:50"
  }
}
```

### 2.2 主要関数

#### `extract_all_media(page, post_url)` - メディア情報抽出

**目的**: すべての投稿から画像/動画メタデータを取得

**実装**:

```python
async def extract_all_media(page, post_url):
    """
    投稿のメディア情報（画像/動画）を抽出

    Args:
        page: Playwright page object
        post_url: 投稿URL

    Returns:
        dict: {
            "images": [{"url", "alt", "width", "height"}],
            "videos": [{"poster", "aria_label", "duration"}],
            "extracted_at": ISO8601 timestamp
        }
    """
    logger.info(f"メディア抽出: {post_url}")

    try:
        await page.goto(post_url, wait_until="domcontentloaded", timeout=90000)
        await asyncio.sleep(8)  # 延長: 3秒 → 8秒

        article = await page.query_selector('article[data-testid="tweet"]')
        if not article:
            logger.warning(f"投稿要素が見つかりません: {post_url}")
            return None

        # 画像抽出（拡張版）
        images = []
        img_elements = await article.query_selector_all('img[alt]')
        for img in img_elements:
            alt = await img.get_attribute('alt')
            src = await img.get_attribute('src')

            # プロフィール画像を除外
            if src and 'profile' not in src.lower():
                # 画像サイズ取得（可能な場合）
                try:
                    bounding_box = await img.bounding_box()
                    width = int(bounding_box['width']) if bounding_box else None
                    height = int(bounding_box['height']) if bounding_box else None
                except:
                    width = None
                    height = None

                images.append({
                    "url": src,
                    "alt": alt or "",
                    "width": width,
                    "height": height
                })

        # 動画抽出（拡張版）
        videos = []
        video_elements = await article.query_selector_all('video')
        for video in video_elements:
            poster = await video.get_attribute('poster')
            aria_label = await video.get_attribute('aria-label')

            # 動画時間取得（可能な場合）
            try:
                duration_elem = await article.query_selector('div[aria-label*=":"]')
                duration = await duration_elem.inner_text() if duration_elem else None
            except:
                duration = None

            videos.append({
                "poster": poster or "",
                "aria_label": aria_label or "",
                "duration": duration
            })

        logger.info(f"✅ メディア抽出成功: 画像{len(images)}件、動画{len(videos)}件")

        return {
            "images": images,
            "videos": videos,
            "extracted_at": datetime.now().isoformat()
        }

    except Exception as e:
        logger.error(f"❌ メディア抽出エラー（{post_url}）: {e}")
        return None
```

#### `extract_replies_info(page, post_url, max_replies=10)` - リプライ情報抽出

**目的**: リプライ欄からユーザー反応とソースURLを取得

**実装**:

```python
async def extract_replies_info(page, post_url, max_replies=10):
    """
    リプライ欄の情報を抽出

    Args:
        page: Playwright page object
        post_url: 投稿URL
        max_replies: 取得するリプライの最大数（デフォルト10件）

    Returns:
        dict: {
            "count": リプライ総数,
            "top_replies": [リプライデータ],
            "has_source_urls": bool,
            "source_urls": [URL一覧],
            "extracted_at": ISO8601 timestamp
        }
    """
    logger.info(f"リプライ抽出: {post_url}")

    try:
        # ページはすでに読み込み済み（extract_all_media後）

        # リプライセクションまでスクロール
        await page.evaluate("window.scrollBy(0, 800)")
        await asyncio.sleep(3)

        # リプライ要素を取得（最初の投稿を除外）
        reply_articles = await page.query_selector_all('article[data-testid="tweet"]')

        if len(reply_articles) <= 1:
            logger.info("リプライが見つかりません")
            return {
                "count": 0,
                "top_replies": [],
                "has_source_urls": False,
                "source_urls": [],
                "extracted_at": datetime.now().isoformat()
            }

        # 最初の投稿を除外（元投稿）
        reply_articles = reply_articles[1:]

        top_replies = []
        all_urls = []

        for i, reply_article in enumerate(reply_articles[:max_replies]):
            try:
                # リプライ著者
                author_elem = await reply_article.query_selector('div[data-testid="User-Name"] a')
                author = await author_elem.get_attribute('href') if author_elem else "unknown"
                author = author.replace('/', '') if author else "unknown"

                # リプライテキスト
                text_elem = await reply_article.query_selector('div[data-testid="tweetText"]')
                text = await text_elem.inner_text() if text_elem else ""

                # いいね数
                like_elem = await reply_article.query_selector('div[data-testid="like"] span')
                likes_text = await like_elem.inner_text() if like_elem else "0"
                likes = parse_engagement_count(likes_text)

                # 投稿日時
                time_elem = await reply_article.query_selector('time')
                posted_at = await time_elem.get_attribute('datetime') if time_elem else None

                # URL抽出
                urls = re.findall(r'https?://[^\s]+', text)
                all_urls.extend(urls)

                top_replies.append({
                    "author": author,
                    "text": text,
                    "likes": likes,
                    "posted_at": posted_at,
                    "urls": urls
                })

                logger.debug(f"  リプライ{i+1}: @{author} - {len(text)}文字 - いいね{likes}件")

            except Exception as e:
                logger.warning(f"  リプライ{i+1}の抽出に失敗: {e}")
                continue

        # 重複URL削除
        unique_urls = list(set(all_urls))

        logger.info(f"✅ リプライ抽出成功: {len(top_replies)}件、URL {len(unique_urls)}件")

        return {
            "count": len(reply_articles),
            "top_replies": top_replies,
            "has_source_urls": len(unique_urls) > 0,
            "source_urls": unique_urls,
            "extracted_at": datetime.now().isoformat()
        }

    except Exception as e:
        logger.error(f"❌ リプライ抽出エラー（{post_url}）: {e}")
        return None


def parse_engagement_count(text):
    """
    エンゲージメント数（いいね数等）をパース

    例: "1.2万" → 12000, "345" → 345
    """
    if not text:
        return 0

    text = text.strip()

    # "万"の処理
    if '万' in text:
        num = float(text.replace('万', ''))
        return int(num * 10000)

    # "K"の処理
    if 'K' in text.upper():
        num = float(text.upper().replace('K', ''))
        return int(num * 1000)

    # 数字のみ
    try:
        return int(text.replace(',', ''))
    except:
        return 0
```

### 2.3 メイン処理フロー

```python
async def main(test_limit=None):
    """
    メイン処理

    Args:
        test_limit: テストモード時の処理件数制限
    """
    start_time = datetime.now()

    logger.info("=" * 60)
    logger.info("X Bookmark Media & Replies Enricher 起動")
    logger.info("=" * 60)

    # Phase 3完了データ読み込み
    INPUT_FILE = Path(__file__).parent.parent / "Flow" / "202512" / "2025-12-31" / "x_bookmarks_data_fulltext_v2.json"
    OUTPUT_FILE = Path(__file__).parent.parent / "Flow" / "202512" / "2025-12-31" / "x_bookmarks_data_enriched.json"

    if not INPUT_FILE.exists():
        logger.error(f"データファイルが見つかりません: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    bookmarks = data["bookmarks"]
    logger.info(f"総ブックマーク数: {len(bookmarks)}件")

    # テストモード
    if test_limit:
        bookmarks_to_process = bookmarks[:test_limit]
        logger.info(f"⚠️  テストモード: 最初の{test_limit}件のみ処理")
    else:
        bookmarks_to_process = bookmarks

    # Playwright起動
    async with async_playwright() as p:
        logger.info("ブラウザを起動中...")

        browser = await p.chromium.launch_persistent_context(
            str(USER_DATA_DIR),
            headless=False,
            slow_mo=500,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox'
            ]
        )

        page = browser.pages[0]

        # 各投稿を処理
        success_count = 0
        failed_count = 0

        for i, bookmark in enumerate(bookmarks_to_process, 1):
            logger.info(f"\n[{i}/{len(bookmarks_to_process)}] 処理中...")

            url = bookmark.get("url")
            if not url:
                logger.warning(f"URLが見つかりません（スキップ）")
                failed_count += 1
                continue

            # メディア情報抽出
            media_info = await extract_all_media(page, url)
            if media_info:
                bookmark["media"] = media_info

            # リプライ情報抽出
            replies_info = await extract_replies_info(page, url, max_replies=10)
            if replies_info:
                bookmark["replies"] = replies_info

            if media_info or replies_info:
                success_count += 1
            else:
                failed_count += 1

            # 進捗保存（10件ごと）
            if i % 10 == 0:
                logger.info(f"中間保存実行（{i}件処理完了）")
                with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                    json.dump({
                        "metadata": {
                            **data["metadata"],
                            "enriched_at": datetime.now().isoformat(),
                            "enriched_count": success_count,
                            "failed_count": failed_count
                        },
                        "bookmarks": bookmarks
                    }, f, ensure_ascii=False, indent=2)

        await browser.close()

    # 最終保存
    logger.info("\n最終データを保存中...")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "metadata": {
                **data["metadata"],
                "enriched_at": datetime.now().isoformat(),
                "enriched_count": success_count,
                "failed_count": failed_count,
                "total_processed": len(bookmarks_to_process)
            },
            "bookmarks": bookmarks
        }, f, ensure_ascii=False, indent=2)

    # 統計表示
    elapsed = (datetime.now() - start_time).total_seconds()

    logger.info("=" * 60)
    logger.info("処理完了！")
    logger.info("=" * 60)
    logger.info(f"処理対象: {len(bookmarks_to_process)}件")
    logger.info(f"成功: {success_count}件")
    logger.info(f"失敗: {failed_count}件")
    logger.info(f"実行時間: {elapsed:.1f}秒（{elapsed/60:.1f}分）")
    logger.info(f"保存先: {OUTPUT_FILE}")
    logger.info("=" * 60)
```

---

## 3. 実装手順

| ステップ | 作業内容 | 推定時間 | 累積 |
|---------|---------|---------|------|
| 1 | データ構造設計・ドキュメント化 | 20分 | 20分 |
| 2 | `extract_all_media()`実装 | 30分 | 50分 |
| 3 | `extract_replies_info()`実装 | 45分 | 95分 |
| 4 | `parse_engagement_count()`実装 | 10分 | 105分 |
| 5 | `main()`実装 | 25分 | 130分 |
| 6 | CLI引数・ログ設定 | 15分 | 145分 |
| 7 | テストモード実行（10件） | 15分 | 160分 |
| 8 | 結果検証・デバッグ | 20分 | 180分 |
| 9 | 全件実行（818件） | 409分（6.8時間） | 589分 |
| 10 | 最終検証・レポート作成 | 30分 | 619分 |
| **合計** | - | **619分（10.3時間）** | - |

### ステップ7: テストモード実行

**実行コマンド**:
```bash
cd /Users/yuichi/AIPM/aipm_v0/scripts
python3 x_bookmark_media_replies_enricher.py --test 10
```

**期待される出力**:
```
処理対象: 10件
成功: 8-10件
失敗: 0-2件
メディア抽出成功: 5-8件
リプライ抽出成功: 8-10件
```

### ステップ9: 全件実行

**実行コマンド**:
```bash
python3 x_bookmark_media_replies_enricher.py 2>&1 | tee enricher_full_run.log
```

**推定実行時間**: 約6.8時間（818件 × 30秒/件）

**内訳**:
- ページ読み込み: 8秒
- メディア抽出: 3秒
- リプライスクロール・抽出: 15秒
- DOM操作・その他: 4秒
- **合計**: 約30秒/件

---

## 4. 待機時間の設定

### 変更箇所

| 箇所 | 変更前 | 変更後 | 理由 |
|------|--------|--------|------|
| ページ読み込み後 | 3秒 | **8秒** | メディア・リプライの完全読み込み |
| リプライスクロール後 | なし | **3秒** | 追加読み込み待機 |
| 「さらに表示」クリック後 | 1秒 | **2秒** | DOM更新の確実な反映 |

### 実装

```python
# ページ読み込み後
await page.goto(post_url, wait_until="domcontentloaded", timeout=90000)
await asyncio.sleep(8)  # 延長: 3秒 → 8秒

# リプライスクロール後
await page.evaluate("window.scrollBy(0, 800)")
await asyncio.sleep(3)  # 新規追加

# 「さらに表示」クリック後
await buttons[0].click()
await asyncio.sleep(2.0)  # 延長: 1秒 → 2秒
```

---

## 5. エラーハンドリング

### 想定されるエラーと対策

| エラー | 原因 | 対策 |
|--------|------|------|
| メディア要素が見つからない | メディアなしの投稿 | 空のメディアオブジェクトを返す |
| リプライが見つからない | リプライなしの投稿 | count=0のリプライオブジェクトを返す |
| いいね数パース失敗 | 表示形式の変更 | デフォルト値0を設定 |
| ページ読み込みタイムアウト | ネットワーク遅延 | timeout=90秒、リトライなし |

### ログレベル

- **INFO**: 処理進捗、成功メッセージ
- **WARNING**: 要素が見つからない、パース失敗（処理は継続）
- **ERROR**: 致命的なエラー、投稿スキップ

---

## 6. 検証基準

### 成功基準

| 項目 | 目標 | 判定基準 |
|------|------|---------|
| メディア抽出成功率 | 80%以上 | `bookmark.media`が存在する投稿の割合 |
| リプライ抽出成功率 | 90%以上 | `bookmark.replies`が存在する投稿の割合 |
| ソースURL発見率 | 30%以上 | `replies.has_source_urls=true`の投稿の割合 |
| 処理速度 | 30秒/件以下 | 818件を7時間以内に完了 |

### 検証コマンド

**メディア抽出率の確認**:
```bash
python3 << 'EOF'
import json
with open('x_bookmarks_data_enriched.json', 'r') as f:
    data = json.load(f)
    bookmarks = data['bookmarks']

media_count = sum(1 for b in bookmarks if 'media' in b)
replies_count = sum(1 for b in bookmarks if 'replies' in b)
source_url_count = sum(1 for b in bookmarks if b.get('replies', {}).get('has_source_urls'))

print(f"メディア抽出: {media_count}/{len(bookmarks)} ({media_count/len(bookmarks)*100:.1f}%)")
print(f"リプライ抽出: {replies_count}/{len(bookmarks)} ({replies_count/len(bookmarks)*100:.1f}%)")
print(f"ソースURL発見: {source_url_count}/{len(bookmarks)} ({source_url_count/len(bookmarks)*100:.1f}%)")
EOF
```

---

## 7. 期待される成果

### 定量的成果

- ✅ メディア情報: 約650件（80%）で画像/動画メタデータ取得
- ✅ リプライ情報: 約735件（90%）でリプライ情報取得
- ✅ ソースURL: 約245件（30%）でソースURL発見
- ✅ 合計データサイズ: 1.2MB → 推定3.5MB（3倍）

### 定性的成果

- ✅ ビジュアルコンテンツの把握（画像/動画の内容）
- ✅ ユーザー反応の定量化（リプライ数、いいね数）
- ✅ 投稿のソーストラッキング（元記事URL等）
- ✅ 関連投稿のネットワーク構築（リプライ内のURL）

---

## 8. 次のアクション（Phase 4準備）

### Phase 3.5完了後の分析可能項目

1. **メディア分析**
   - 画像/動画の割合
   - 画像のalt属性による内容分類
   - 動画の長さ分布

2. **リプライ分析**
   - リプライ数と投稿エンゲージメントの相関
   - ソースURLドメインの分布
   - トップリプライの傾向

3. **ソーストラッキング**
   - 引用元記事の特定
   - 情報源の信頼性評価
   - 関連投稿のグラフ化

---

## 9. Critical Files

### 新規作成ファイル

#### `/Users/yuichi/AIPM/aipm_v0/scripts/x_bookmark_media_replies_enricher.py`
**内容**: Phase 3.5のメイン実装（約500行）

### 入力ファイル

#### `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/x_bookmarks_data_fulltext_v2.json`
**用途**: Phase 3完了データ（818件）

### 出力ファイル

#### `/Users/yuichi/AIPM/aipm_v0/Flow/202512/2025-12-31/x_bookmarks_data_enriched.json`
**用途**: Phase 3.5完了データ（メディア・リプライ情報付き）
**推定サイズ**: 3.5MB

#### `/Users/yuichi/AIPM/aipm_v0/scripts/enricher_full_run.log`
**用途**: 全件実行ログ

---

## 10. リスク管理

### 主要リスク

| リスク | 影響 | 対策 | 優先度 |
|--------|------|------|--------|
| 実行時間が予想より長い（10時間超） | 高 | 並列処理の検討、中断・再開機能 | 高 |
| リプライ構造の変化 | 中 | 複数セレクターの準備、柔軟なパース | 中 |
| レート制限 | 低 | 待機時間の延長、User-Agent設定 | 低 |
| メモリ不足 | 低 | 10件ごとの中間保存 | 低 |

---

## 11. 実装承認チェックリスト

- [ ] データ構造設計のレビュー完了
- [ ] 実装計画の承認取得
- [ ] テストモード（10件）の実行準備完了
- [ ] 全件実行（818件）の実行タイミング確認

---

**計画策定日時**: 2025-12-31 20:00
**推定完了日時**: 2026-01-01 06:00（翌朝6時）
**計画修正回数**: 0回
**次のアクション**: ユーザー承認後、実装開始
