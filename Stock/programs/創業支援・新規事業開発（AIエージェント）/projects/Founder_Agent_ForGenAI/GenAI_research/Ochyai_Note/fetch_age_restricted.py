#!/usr/bin/env python3
"""Fetch 18+ age-restricted articles using Playwright browser automation."""
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# 未取得の9件
MISSING_URLS = [
    "https://note.com/ochyai/n/n32060ed41489",
    "https://note.com/ochyai/n/n49531fef376e",
    "https://note.com/ochyai/n/n495d3bb2f2d1",
    "https://note.com/ochyai/n/n5c9317872ec7",
    "https://note.com/ochyai/n/n8bc697d11adf",
    "https://note.com/ochyai/n/n981e9bb3369a",
    "https://note.com/ochyai/n/nab64d3f06c99",
    "https://note.com/ochyai/n/naca0c5f1ef2f",
    "https://note.com/ochyai/n/nf67b6c1d4d19",
]

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "full_run"
COOKIES_PATH = BASE_DIR / "cookies" / "note_cookies.json"


def now_iso():
    return datetime.now().isoformat(timespec="seconds")


def extract_article_id(url):
    import re
    m = re.search(r"/n/(n[0-9a-f]+)", url)
    if not m:
        return re.sub(r"\W+", "_", url)
    return m.group(1)


def normalize_filename(text, max_len=80):
    import re
    if not text:
        return "untitled"
    text = re.sub(r"[\\/\n\r\t]+", "_", text)
    text = re.sub(r"[\x00-\x1f\x7f]+", "", text)
    text = text.strip()
    if len(text) > max_len:
        text = text[:max_len].rstrip()
    return text or "untitled"


def build_file_stem(published_at, title, fallback_date):
    date_str = fallback_date
    if published_at:
        date_str = published_at[:10]
    title_part = normalize_filename(title, max_len=80)
    return f"{date_str}_{title_part}"


def safe_ext_from_url(url):
    from urllib.parse import urlparse
    path = urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".gif", ".webp"]:
        return ext
    return ".jpg"


def extract_content_container(soup):
    article = soup.find("article")
    if article:
        return article
    for selector in ["div.note-body", "div[class*=note-body]", "div[class*=p-article__body]"]:
        el = soup.select_one(selector)
        if el:
            return el
    return None


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


def detect_paid(html):
    import re
    if re.search(r"\"isPaid\"\s*:\s*true", html):
        return True
    if "paywall" in html and "続きをみる" in html:
        return True
    return False


def download_image_requests(url, dest_path):
    import requests
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    dest_path.write_bytes(resp.content)


def convert_article_to_markdown(html, base_url, images_dir, articles_dir):
    soup = BeautifulSoup(html, "html.parser")
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
            download_image_requests(full_url, dest_path)
            rel_path = os.path.relpath(dest_path, start=articles_dir)
            img["src"] = rel_path
            image_paths.append(rel_path)
        except Exception:
            continue

    html_str = str(content)
    markdown = md(html_str, heading_style="ATX")
    return markdown, image_paths


def save_article(output_dir, article_id, metadata, markdown):
    articles_dir = output_dir / "articles"
    articles_dir.mkdir(parents=True, exist_ok=True)
    json_path = articles_dir / f"{article_id}.json"
    md_path = articles_dir / f"{article_id}.md"
    json_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(markdown, encoding="utf-8")


def process_article_with_playwright(page, url, output_dir):
    page.goto(url, wait_until="networkidle")
    time.sleep(1)

    # 年齢確認ダイアログがあればクリック
    try:
        age_button = page.locator("text=18歳以上")
        if age_button.count() > 0:
            age_button.first.click()
            page.wait_for_load_state("networkidle")
            time.sleep(1)
    except Exception:
        pass

    html = page.content()
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
    markdown, image_paths = convert_article_to_markdown(html, url, images_dir, articles_dir)

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
        "age_restricted": True,
    }

    save_article(output_dir, file_stem, metadata, markdown)
    return file_stem


def main():
    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    failures_path = output_dir / "logs" / "age_restricted_failures.jsonl"

    print(f"Processing {len(MISSING_URLS)} age-restricted articles...")

    with sync_playwright() as p:
        # 既存のCookieがあれば使用
        context_options = {}
        if COOKIES_PATH.exists():
            context_options["storage_state"] = str(COOKIES_PATH)

        browser = p.chromium.launch(headless=True)
        context = browser.new_context(**context_options)
        page = context.new_page()

        success_count = 0
        for idx, url in enumerate(MISSING_URLS, 1):
            try:
                print(f"[{idx}/{len(MISSING_URLS)}] {url}")
                file_stem = process_article_with_playwright(page, url, output_dir)
                print(f"  -> Saved: {file_stem}")
                success_count += 1
            except Exception as exc:
                print(f"  -> Failed: {exc}")
                failure = {"url": url, "error": str(exc), "scraped_at": now_iso()}
                with failures_path.open("a", encoding="utf-8") as f:
                    f.write(json.dumps(failure, ensure_ascii=False) + "\n")

        context.close()
        browser.close()

    print(f"Done. Success: {success_count}/{len(MISSING_URLS)}")


if __name__ == "__main__":
    main()
