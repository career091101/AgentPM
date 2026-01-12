#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ARCHIVE_URL = "https://note.com/ochyai/m/m41f58d360230/archive"
ARCHIVE_API_URL = "https://note.com/api/v1/layout/magazine/m41f58d360230"
ARCHIVE_START_YM = "2019-01"
ARCHIVE_END_YM = "2025-12"
EXPECTED_NOTE_COUNT = 1631


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def load_cookies(session, cookies_path):
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


def parse_netscape_cookies(txt_path):
    cookies = []
    with open(txt_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) != 7:
                continue
            domain, _flag, path, _secure, _expires, name, value = parts
            cookies.append(
                {
                    "name": name,
                    "value": value,
                    "domain": domain,
                    "path": path or "/",
                }
            )
    return cookies


def save_cookies_json(cookies, cookies_path):
    cookies_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"cookies": cookies}
    cookies_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def login_and_save_cookies(cookies_path):
    try:
        from playwright.sync_api import sync_playwright
    except Exception as exc:
        print(f"Playwright import failed: {exc}")
        print("Install with: python -m pip install playwright && python -m playwright install chromium")
        sys.exit(1)

    cookies_path.parent.mkdir(parents=True, exist_ok=True)

    done_flag = cookies_path.parent / "login_done.flag"
    if done_flag.exists():
        done_flag.unlink()

    with sync_playwright() as p:
        profile_dir = cookies_path.parent / "playwright_profile"
        # Prefer the installed Chrome if available (more stable on macOS).
        try:
            context = p.chromium.launch_persistent_context(
                user_data_dir=str(profile_dir),
                headless=False,
                channel="chrome",
            )
        except Exception:
            context = p.chromium.launch_persistent_context(
                user_data_dir=str(profile_dir),
                headless=False,
            )
        page = context.new_page()
        page.goto("https://note.com/login?redirectPath=/")
        print("Please complete X login in the browser.")
        print(f"Waiting for {done_flag} to appear...")
        # Wait for a flag file so stdin isn't required (stdin may be closed).
        while not done_flag.exists():
            time.sleep(1)
        context.storage_state(path=str(cookies_path))
        context.close()
    if done_flag.exists():
        done_flag.unlink()
    print(f"Saved cookies to {cookies_path}")


def get_session(cookies_path):
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
        }
    )
    if cookies_path.exists():
        load_cookies(session, cookies_path)
    return session


def fetch_html(session, url, sleep_s=1.0):
    resp = session.get(url, timeout=30)
    if resp.status_code != 200:
        raise RuntimeError(f"HTTP {resp.status_code} for {url}")
    time.sleep(sleep_s)
    return resp.text


def fetch_json(session, url, sleep_s=1.0, retries=3, backoff_s=2.0, log_path=None):
    last_exc = None
    for attempt in range(1, retries + 1):
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()
            payload = resp.json()
            time.sleep(sleep_s)
            return payload
        except Exception as exc:
            last_exc = exc
            if log_path:
                failure = {
                    "url": url,
                    "attempt": attempt,
                    "error": str(exc),
                    "scraped_at": now_iso(),
                }
                with log_path.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(failure, ensure_ascii=False) + "\n")
            time.sleep(backoff_s * attempt)
    raise RuntimeError(f"Failed to fetch JSON after {retries} attempts: {url}") from last_exc


def iter_months(start_ym, end_ym):
    start = datetime.strptime(start_ym, "%Y-%m")
    end = datetime.strptime(end_ym, "%Y-%m")
    cur = start
    while cur <= end:
        yield cur.strftime("%Y-%m")
        year = cur.year + (cur.month // 12)
        month = 1 if cur.month == 12 else cur.month + 1
        cur = cur.replace(year=year, month=month)


def collect_article_urls_via_api(session, start_ym, end_ym, limit=None, log_path=None):
    urls = []
    seen = set()
    note_count = None
    month_counts = []

    for ym in iter_months(start_ym, end_ym):
        page = 1
        month_added = 0
        while True:
            url = f"{ARCHIVE_API_URL}?ym={ym}-01&include_details=true&page={page}"
            payload = fetch_json(session, url, sleep_s=0.5, retries=3, backoff_s=2.0, log_path=log_path)
            magazine = payload.get("data", {}).get("magazine_layout", {})
            if note_count is None:
                note_count = magazine.get("note_count")
            section = magazine.get("page_layout", {}).get("section", {})
            contents = section.get("contents") or []
            if not contents:
                break
            for item in contents:
                note_url = item.get("note_url")
                if not note_url:
                    continue
                full = note_url if note_url.startswith("http") else urljoin(ARCHIVE_URL, note_url)
                if "/ochyai/n/" not in full:
                    continue
                if full not in seen:
                    seen.add(full)
                    urls.append(full)
                    month_added += 1
                    if limit and len(urls) >= limit:
                        month_counts.append({"ym": ym, "count": month_added})
                        return urls, note_count, month_counts
            if section.get("is_last_page") or len(contents) == 0:
                break
            page += 1
        month_counts.append({"ym": ym, "count": month_added})

    return urls, note_count, month_counts


def extract_article_id(url):
    m = re.search(r"/n/(n[0-9a-f]+)", url)
    if not m:
        return re.sub(r"\W+", "_", url)
    return m.group(1)


def normalize_filename(text, max_len=80):
    if not text:
        return "untitled"
    # Replace path separators and control chars.
    text = re.sub(r"[\\\\/\\n\\r\\t]+", "_", text)
    text = re.sub(r"[\\x00-\\x1f\\x7f]+", "", text)
    text = text.strip()
    if len(text) > max_len:
        text = text[:max_len].rstrip()
    return text or "untitled"


def build_file_stem(published_at, title, fallback_date):
    date_str = fallback_date
    if published_at:
        # Keep only date portion.
        date_str = published_at[:10]
    title_part = normalize_filename(title, max_len=80)
    return f"{date_str}_{title_part}"


def extract_content_container(soup):
    article = soup.find("article")
    if article:
        return article
    for selector in ["div.note-body", "div[class*=note-body]", "div[class*=p-article__body]"]:
        el = soup.select_one(selector)
        if el:
            return el
    return None


def detect_paid(html):
    if re.search(r"\"isPaid\"\s*:\s*true", html):
        return True
    if "paywall" in html and "続きをみる" in html:
        return True
    return False


def normalize_tags(soup):
    tags = []
    for a in soup.find_all("a", href=True):
        if "/hashtag/" in a["href"]:
            tag = a.get_text(strip=True)
            if tag and tag not in tags:
                tags.append(tag)
    return tags


def extract_published_at(soup):
    time_el = soup.find("time")
    if time_el and time_el.get("datetime"):
        return time_el.get("datetime")
    return None


def safe_ext_from_url(url):
    path = urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
        return ext
    return ".jpg"


def download_image(session, url, dest_path):
    resp = session.get(url, timeout=30)
    resp.raise_for_status()
    dest_path.write_bytes(resp.content)


def convert_article_to_markdown(session, soup, base_url, images_dir, articles_dir):
    content = extract_content_container(soup)
    if not content:
        return "", []

    image_paths = []
    img_tags = content.find_all("img")
    for idx, img in enumerate(img_tags, 1):
        src = img.get("src") or img.get("data-src")
        if not src:
            continue
        full_url = urljoin(base_url, src)
        ext = safe_ext_from_url(full_url)
        images_dir.mkdir(parents=True, exist_ok=True)
        filename = f"{idx:03d}{ext}"
        dest_path = images_dir / filename
        try:
            download_image(session, full_url, dest_path)
            rel_path = os.path.relpath(dest_path, start=articles_dir)
            img["src"] = rel_path
            image_paths.append(rel_path)
        except Exception:
            continue

    html = str(content)
    markdown = md(html, heading_style="ATX")
    return markdown, image_paths


def save_article(output_dir, article_id, metadata, markdown):
    articles_dir = output_dir / "articles"
    articles_dir.mkdir(parents=True, exist_ok=True)

    json_path = articles_dir / f"{article_id}.json"
    md_path = articles_dir / f"{article_id}.md"

    json_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(markdown, encoding="utf-8")


def process_article(session, url, output_dir):
    html = fetch_html(session, url, sleep_s=1.0)
    soup = BeautifulSoup(html, "html.parser")

    title = soup.find("title").get_text(strip=True) if soup.find("title") else ""
    published_at = extract_published_at(soup)
    tags = normalize_tags(soup)
    is_paid = detect_paid(html)

    article_id = extract_article_id(url)
    fallback_date = now_iso()[:10]
    file_stem = build_file_stem(published_at, title, fallback_date)

    images_dir = output_dir / "images" / file_stem
    articles_dir = output_dir / "articles"
    markdown, image_paths = convert_article_to_markdown(session, soup, url, images_dir, articles_dir)

    metadata = {
        "id": article_id,
        "file_stem": file_stem,
        "title": title,
        "url": url,
        "published_at": published_at,
        "tags": tags,
        "is_paid": is_paid,
        "image_paths": image_paths,
        "image_descriptions": {},
        "scraped_at": now_iso(),
    }

    save_article(output_dir, file_stem, metadata, markdown)


def main():
    parser = argparse.ArgumentParser(description="Fetch note archive articles to JSON + Markdown")
    parser.add_argument("--login", action="store_true", help="Open browser to login and save cookies")
    parser.add_argument("--limit", type=int, default=0, help="Number of articles to fetch (0=all)")
    parser.add_argument("--output", type=str, required=True, help="Output directory")
    parser.add_argument("--cookies", type=str, default="cookies/note_cookies.json", help="Cookies file path")
    parser.add_argument("--cookies-txt", type=str, help="Netscape cookies.txt path")
    args = parser.parse_args()

    output_dir = Path(args.output).expanduser().resolve()
    cookies_path = Path(args.cookies).expanduser().resolve()

    if args.cookies_txt and not cookies_path.exists():
        txt_path = Path(args.cookies_txt).expanduser().resolve()
        cookies = parse_netscape_cookies(txt_path)
        if not cookies:
            print("No cookies found in cookies.txt")
            sys.exit(1)
        save_cookies_json(cookies, cookies_path)

    if args.login or not cookies_path.exists():
        login_and_save_cookies(cookies_path)

    session = get_session(cookies_path)

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "logs").mkdir(parents=True, exist_ok=True)

    failures_path = output_dir / "logs" / "failures.jsonl"
    url_failures_path = output_dir / "logs" / "url_collection_failures.jsonl"
    metadata_dir = output_dir / "metadata"
    metadata_dir.mkdir(parents=True, exist_ok=True)

    limit = args.limit if args.limit and args.limit > 0 else None
    article_urls, note_count, month_counts = collect_article_urls_via_api(
        session,
        ARCHIVE_START_YM,
        ARCHIVE_END_YM,
        limit=limit,
        log_path=url_failures_path,
    )
    if not article_urls:
        print("No article URLs found via API.")
        sys.exit(1)

    urls_meta = {
        "source": "note_api_layout",
        "archive_url": ARCHIVE_URL,
        "magazine_key": "m41f58d360230",
        "start_ym": ARCHIVE_START_YM,
        "end_ym": ARCHIVE_END_YM,
        "note_count": note_count,
        "expected_note_count": EXPECTED_NOTE_COUNT,
        "total_urls": len(article_urls),
        "months": month_counts,
        "article_urls": article_urls,
        "collected_at": now_iso(),
    }
    urls_meta_path = metadata_dir / "archive_urls.json"
    urls_meta_path.write_text(json.dumps(urls_meta, ensure_ascii=False, indent=2), encoding="utf-8")

    if note_count is not None and note_count != len(article_urls):
        print(f"Warning: API note_count={note_count} but collected_urls={len(article_urls)}")
    if len(article_urls) != EXPECTED_NOTE_COUNT and limit is None:
        print(f"Warning: expected {EXPECTED_NOTE_COUNT} URLs but got {len(article_urls)}")

    for idx, url in enumerate(article_urls, 1):
        try:
            print(f"[{idx}/{len(article_urls)}] {url}")
            process_article(session, url, output_dir)
        except Exception as exc:
            failure = {"url": url, "error": str(exc), "scraped_at": now_iso()}
            with failures_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(failure, ensure_ascii=False) + "\n")

    print("Done.")


if __name__ == "__main__":
    main()
