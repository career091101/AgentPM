#!/usr/bin/env python3
"""Retry failed articles from failures.jsonl"""
import json
import sys
from pathlib import Path

# Add parent dir to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from note_archive_fetcher import get_session, process_article, now_iso

def main():
    output_dir = Path(__file__).parent / "full_run"
    failures_path = output_dir / "logs" / "failures.jsonl"
    cookies_path = Path(__file__).parent / "cookies" / "note_cookies.json"
    retry_failures_path = output_dir / "logs" / "retry_failures.jsonl"

    if not failures_path.exists():
        print("No failures.jsonl found")
        return

    failed_urls = []
    with failures_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
                if "url" in data:
                    failed_urls.append(data["url"])
            except:
                continue

    if not failed_urls:
        print("No failed URLs found")
        return

    print(f"Found {len(failed_urls)} failed URLs to retry")

    session = get_session(cookies_path)

    success_count = 0
    for idx, url in enumerate(failed_urls, 1):
        try:
            print(f"[{idx}/{len(failed_urls)}] Retrying: {url}")
            process_article(session, url, output_dir)
            success_count += 1
        except Exception as exc:
            failure = {"url": url, "error": str(exc), "scraped_at": now_iso()}
            with retry_failures_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(failure, ensure_ascii=False) + "\n")
            print(f"  Failed again: {exc}")

    print(f"Done. Successfully retried: {success_count}/{len(failed_urls)}")

if __name__ == "__main__":
    main()
