#!/usr/bin/env python3
"""
Note記事ベンチマーク収集スクリプト

3ジャンル（テクノロジー・AI、ビジネス・起業、クリエイター・副業）から
高品質な記事を収集し、AI学習データセットを構築する。

Usage:
    python note_benchmark_collector.py --genre tech_ai --limit 40
    python note_benchmark_collector.py --genre business --limit 40
    python note_benchmark_collector.py --genre creator --limit 40
    python note_benchmark_collector.py --all --limit 120
"""
import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ベンチマーク出力ディレクトリ
BENCHMARK_DIR = Path(__file__).parent.parent / "Stock/programs/副業/projects/SNS/knowledge/Note/benchmark"

# ジャンル定義（クリエイターIDはnote.comで確認済み - 2026年1月更新）
GENRES = {
    "tech_ai": {
        "name": "テクノロジー・AI",
        "hashtags": ["AI", "ChatGPT", "プログラミング", "エンジニア", "機械学習", "LLM", "生成AI", "Python", "開発"],
        "creators": [
            "ochyai",       # 落合陽一
            "norinity1103", # のりにてぃ
            "takahiroanno", # 安野貴博
            "fladdict",     # 深津貴之（THE GUILD）
            "shi3z",        # shi3z（清水亮）
            "mizchi",       # mizchi
            "aiconsulting", # inoue_AI
            "belnon",       # あべむつき（AI活用マガジン）
            "ai_freelancer", # 自由人@フリーランス
            "mori_mori_ta",  # 森々田
        ],
        "keywords": ["AI活用", "ChatGPT", "Claude", "プロンプト", "自動化"],
    },
    "business": {
        "name": "ビジネス・起業",
        "hashtags": ["スタートアップ", "起業", "マーケティング", "SaaS", "経営", "ビジネス", "事業開発"],
        "creators": [
            "kensuu",       # けんすう（アル）
            "tamesue",      # 為末大
            "kishidanami",  # 岸田奈美
            "kajiken0630",  # 梶谷健人
            "ikedanoriyuki", # 池田紀行
            "osamu_fujitani", # 藤谷治
            "juninagao",     # 永尾準一
            "dada696",       # 世良陽一
            "suadd",         # suadd
            "shota_y",       # 横山翔太
        ],
        "keywords": ["起業", "スタートアップ", "マーケティング", "成長戦略"],
    },
    "creator": {
        "name": "クリエイター・副業",
        "hashtags": ["副業", "SNS運用", "マネタイズ", "個人ブランディング", "フリーランス", "クリエイター"],
        "creators": [
            "golddust",      # もえぎ（写真・旅行）
            "fujiwarahana",  # 藤原華（文章術）
            "harunoyuki0906", # はるのゆき
            "yuki_note_writer", # ゆき
            "okeydon",       # おけいどん
            "mayumi_tanaka", # 田中真弓
            "hiroyuki_note", # ひろゆき（副業系）
            "sachiyo",       # さちよ
            "yurufuwa_life", # ゆるふわライフ
            "freelance_hero", # フリーランスヒーロー
        ],
        "keywords": ["副業", "収益化", "フォロワー", "note収益"],
    },
}

# 収集期間（過去1年）
COLLECT_START_DATE = datetime.now() - timedelta(days=365)
COLLECT_END_DATE = datetime.now()


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def load_cookies(session, cookies_path):
    """Cookieファイルを読み込んでセッションに設定"""
    if not cookies_path.exists():
        return False
    with open(cookies_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    cookies = data.get("cookies", data)
    for c in cookies:
        session.cookies.set(
            c.get("name"),
            c.get("value"),
            domain=c.get("domain"),
            path=c.get("path", "/"),
        )
    return True


def get_session(cookies_path=None):
    """認証済みセッションを取得"""
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
    })
    if cookies_path and cookies_path.exists():
        load_cookies(session, cookies_path)
    return session


def fetch_json(session, url, sleep_s=1.0, retries=3):
    """JSON APIを取得"""
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()
            time.sleep(sleep_s)
            return resp.json()
        except Exception as e:
            if attempt == retries - 1:
                raise
            time.sleep(2 ** attempt)
    return None


def fetch_html(session, url, sleep_s=1.0):
    """HTMLページを取得"""
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    time.sleep(sleep_s)
    return resp.text


def fetch_creator_articles(session, creator_id, limit=20):
    """クリエイターの記事一覧を取得"""
    articles = []
    page = 1

    while len(articles) < limit:
        # クリエイター記事一覧API
        url = f"https://note.com/api/v2/creators/{creator_id}/contents?kind=note&page={page}"
        try:
            data = fetch_json(session, url, sleep_s=0.5)
            if not data:
                break

            notes = data.get("data", {}).get("contents", [])
            if not notes:
                break

            for note in notes:
                # 過去1年以内の記事のみ
                published = note.get("publishAt", "")
                if published:
                    try:
                        pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
                        if pub_date.replace(tzinfo=None) < COLLECT_START_DATE:
                            continue
                    except:
                        pass

                articles.append({
                    "id": note.get("key", ""),
                    "title": note.get("name", ""),
                    "url": f"https://note.com/{creator_id}/n/{note.get('key', '')}",
                    "author": note.get("user", {}).get("name", creator_id),
                    "author_id": creator_id,
                    "published_at": published,
                    "like_count": note.get("likeCount", 0),
                    "comment_count": note.get("commentCount", 0),
                    "is_paid": note.get("price", 0) > 0,
                    "price": note.get("price", 0),
                    "creator_source": creator_id,
                })

                if len(articles) >= limit:
                    break

            page += 1
            if page > 10:  # 最大10ページ
                break

        except Exception as e:
            print(f"  Warning: Failed to fetch from {creator_id}: {e}")
            break

    return articles


def collect_genre_articles(session, genre_key, limit=40):
    """ジャンル別に記事を収集（クリエイターAPIベース）"""
    genre = GENRES.get(genre_key)
    if not genre:
        raise ValueError(f"Unknown genre: {genre_key}")

    print(f"\n📂 {genre['name']}ジャンルの記事収集開始...")

    all_articles = []
    seen_ids = set()

    # クリエイターごとに収集
    articles_per_creator = max(5, limit // len(genre["creators"]))

    for creator_id in genre["creators"]:
        print(f"  👤 {creator_id} の記事を取得中...")
        articles = fetch_creator_articles(session, creator_id, limit=articles_per_creator)

        for article in articles:
            if article["id"] not in seen_ids:
                seen_ids.add(article["id"])
                article["genre"] = genre_key
                all_articles.append(article)

        print(f"     → {len(articles)}件取得（累計: {len(all_articles)}件）")

        if len(all_articles) >= limit:
            break

    # スキ数でソートして上位を選択
    all_articles.sort(key=lambda x: x.get("like_count", 0), reverse=True)
    selected = all_articles[:limit]

    print(f"  ✓ {len(selected)}件を選択（スキ数上位）")
    return selected


def extract_article_content(session, url):
    """記事本文を抽出"""
    try:
        html = fetch_html(session, url, sleep_s=1.0)
        soup = BeautifulSoup(html, "html.parser")

        # タイトル
        title_el = soup.find("h1")
        title = title_el.get_text(strip=True) if title_el else ""

        # 本文
        article = soup.find("article")
        if article:
            # 不要な要素を削除
            for el in article.find_all(["script", "style", "nav", "footer"]):
                el.decompose()

            body_html = str(article)
            body_text = article.get_text(separator="\n", strip=True)
            body_md = md(body_html, heading_style="ATX")
        else:
            body_html = ""
            body_text = ""
            body_md = ""

        # ハッシュタグ
        hashtags = []
        for a in soup.find_all("a", href=True):
            if "/hashtag/" in a["href"]:
                tag = a.get_text(strip=True)
                if tag and tag not in hashtags:
                    hashtags.append(tag)

        # 文字数
        word_count = len(body_text)

        # 見出し数
        heading_count = len(soup.find_all(["h2", "h3"]))

        return {
            "title": title,
            "body_text": body_text,
            "body_markdown": body_md,
            "hashtags": hashtags,
            "word_count": word_count,
            "heading_count": heading_count,
        }

    except Exception as e:
        print(f"    Warning: Failed to extract content: {e}")
        return None


def calculate_quality_score(article, content):
    """品質スコアを計算"""
    score = 0
    details = {}

    # 文字数 (2000-5000字が最適) - 20点
    wc = content.get("word_count", 0)
    if 2000 <= wc <= 5000:
        score += 20
        details["word_count"] = {"score": 20, "value": wc, "status": "optimal"}
    elif 1000 <= wc < 2000 or 5000 < wc <= 8000:
        score += 15
        details["word_count"] = {"score": 15, "value": wc, "status": "acceptable"}
    elif wc > 500:
        score += 10
        details["word_count"] = {"score": 10, "value": wc, "status": "short"}
    else:
        details["word_count"] = {"score": 0, "value": wc, "status": "too_short"}

    # ハッシュタグ数 (3-5個が最適) - 15点
    tag_count = len(content.get("hashtags", []))
    if 3 <= tag_count <= 5:
        score += 15
        details["hashtags"] = {"score": 15, "count": tag_count, "status": "optimal"}
    elif 1 <= tag_count <= 7:
        score += 10
        details["hashtags"] = {"score": 10, "count": tag_count, "status": "acceptable"}
    else:
        details["hashtags"] = {"score": 0, "count": tag_count, "status": "suboptimal"}

    # スキ数（相対評価）- 25点
    likes = article.get("like_count", 0)
    if likes >= 100:
        score += 25
        details["likes"] = {"score": 25, "count": likes, "status": "high"}
    elif likes >= 50:
        score += 20
        details["likes"] = {"score": 20, "count": likes, "status": "good"}
    elif likes >= 20:
        score += 15
        details["likes"] = {"score": 15, "count": likes, "status": "moderate"}
    elif likes >= 5:
        score += 10
        details["likes"] = {"score": 10, "count": likes, "status": "low"}
    else:
        details["likes"] = {"score": 0, "count": likes, "status": "very_low"}

    # コメント数 - 10点
    comments = article.get("comment_count", 0)
    if comments >= 1:
        score += 10
        details["comments"] = {"score": 10, "count": comments, "status": "has_comments"}
    else:
        details["comments"] = {"score": 0, "count": comments, "status": "no_comments"}

    # 見出し構造 (3個以上が最適) - 20点
    headings = content.get("heading_count", 0)
    if headings >= 3:
        score += 20
        details["structure"] = {"score": 20, "headings": headings, "status": "well_structured"}
    elif headings >= 1:
        score += 10
        details["structure"] = {"score": 10, "headings": headings, "status": "has_structure"}
    else:
        details["structure"] = {"score": 0, "headings": headings, "status": "flat"}

    # 投稿時刻（19時前後が最適）- 10点
    published = article.get("published_at", "")
    if published:
        try:
            pub_dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
            hour = pub_dt.hour
            if 18 <= hour <= 20:
                score += 10
                details["timing"] = {"score": 10, "hour": hour, "status": "golden_hour"}
            elif 17 <= hour <= 21:
                score += 5
                details["timing"] = {"score": 5, "hour": hour, "status": "good_time"}
            else:
                details["timing"] = {"score": 0, "hour": hour, "status": "off_peak"}
        except Exception:
            details["timing"] = {"score": 0, "status": "unknown"}

    return score, details


def save_article(article, content, quality_score, quality_details, output_dir):
    """記事を保存"""
    genre_dir = output_dir / "raw" / article["genre"]
    genre_dir.mkdir(parents=True, exist_ok=True)

    # ファイル名生成
    article_id = article["id"]
    published = article.get("published_at", "")[:10] or "unknown"
    safe_title = re.sub(r"[^\w\s-]", "", article.get("title", "untitled"))[:50]
    filename = f"{published}_{article_id}_{safe_title}"

    # メタデータ
    metadata = {
        **article,
        "content": {
            "word_count": content.get("word_count", 0),
            "heading_count": content.get("heading_count", 0),
            "hashtags": content.get("hashtags", []),
        },
        "quality": {
            "score": quality_score,
            "tier": "A" if quality_score >= 80 else "B" if quality_score >= 60 else "C" if quality_score >= 40 else "D",
            "details": quality_details,
        },
        "collected_at": now_iso(),
    }

    # JSON保存
    json_path = genre_dir / f"{filename}.json"
    json_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    # Markdown保存（無料記事のみ本文）
    if not article.get("is_paid", False):
        md_path = genre_dir / f"{filename}.md"
        md_content = f"# {article.get('title', 'Untitled')}\n\n"
        md_content += f"> Author: {article.get('author', 'Unknown')}\n"
        md_content += f"> Published: {published}\n"
        md_content += f"> Likes: {article.get('like_count', 0)}\n"
        md_content += f"> Quality Score: {quality_score}/100\n\n"
        md_content += "---\n\n"
        md_content += content.get("body_markdown", "")
        md_path.write_text(md_content, encoding="utf-8")

    return filename


def main():
    parser = argparse.ArgumentParser(description="Note記事ベンチマーク収集ツール")
    parser.add_argument("--genre", type=str, choices=["tech_ai", "business", "creator"],
                        help="収集するジャンル")
    parser.add_argument("--all", action="store_true", help="全ジャンルを収集")
    parser.add_argument("--limit", type=int, default=40, help="ジャンルあたりの記事数")
    parser.add_argument("--cookies", type=str,
                        default="Stock/programs/副業/projects/月刊アプリマーケティング/data/cookies/note_cookies.json",
                        help="Cookiesファイルパス")
    parser.add_argument("--output", type=str, default=str(BENCHMARK_DIR), help="出力ディレクトリ")
    parser.add_argument("--skip-content", action="store_true", help="本文取得をスキップ")
    args = parser.parse_args()

    output_dir = Path(args.output).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Cookie設定
    cookies_path = Path(args.cookies).expanduser().resolve()
    if not cookies_path.is_absolute():
        cookies_path = Path(__file__).parent.parent / args.cookies

    session = get_session(cookies_path if cookies_path.exists() else None)

    print("=" * 60)
    print("📚 Note記事ベンチマーク収集")
    print("=" * 60)
    print(f"期間: {COLLECT_START_DATE.strftime('%Y-%m-%d')} ～ {COLLECT_END_DATE.strftime('%Y-%m-%d')}")
    print(f"出力先: {output_dir}")
    print()

    # 収集対象ジャンル
    if args.all:
        genres_to_collect = list(GENRES.keys())
    elif args.genre:
        genres_to_collect = [args.genre]
    else:
        print("Error: --genre または --all を指定してください")
        sys.exit(1)

    all_results = []

    for genre_key in genres_to_collect:
        articles = collect_genre_articles(session, genre_key, limit=args.limit)

        print(f"\n  📥 本文取得中...")
        for idx, article in enumerate(articles, 1):
            print(f"    [{idx}/{len(articles)}] {article['title'][:40]}...")

            if args.skip_content:
                content = {"word_count": 0, "heading_count": 0, "hashtags": []}
            else:
                content = extract_article_content(session, article["url"])
                if not content:
                    content = {"word_count": 0, "heading_count": 0, "hashtags": []}

            # 品質スコア計算
            score, details = calculate_quality_score(article, content)

            # 保存
            filename = save_article(article, content, score, details, output_dir)

            all_results.append({
                "genre": genre_key,
                "article_id": article["id"],
                "title": article["title"],
                "quality_score": score,
                "filename": filename,
            })

            print(f"      → Score: {score}/100 ({details.get('likes', {}).get('status', 'unknown')})")

    # サマリー保存
    summary = {
        "collected_at": now_iso(),
        "total_articles": len(all_results),
        "by_genre": {},
        "articles": all_results,
    }

    for genre_key in genres_to_collect:
        genre_articles = [a for a in all_results if a["genre"] == genre_key]
        avg_score = sum(a["quality_score"] for a in genre_articles) / len(genre_articles) if genre_articles else 0
        summary["by_genre"][genre_key] = {
            "count": len(genre_articles),
            "avg_quality_score": round(avg_score, 1),
        }

    summary_path = output_dir / "metadata" / "collection_summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n" + "=" * 60)
    print("✅ 収集完了!")
    print("=" * 60)
    print(f"総記事数: {len(all_results)}件")
    for genre_key, stats in summary["by_genre"].items():
        print(f"  {GENRES[genre_key]['name']}: {stats['count']}件 (平均スコア: {stats['avg_quality_score']})")
    print(f"\n出力先: {output_dir}")


if __name__ == "__main__":
    main()
