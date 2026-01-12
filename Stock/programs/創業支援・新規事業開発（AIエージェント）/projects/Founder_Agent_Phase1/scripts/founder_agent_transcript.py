#!/usr/bin/env python3
from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import os
import random
import re
import sys
import time
from pathlib import Path
from typing import Any, Iterable

from youtube_transcript_api import YouTubeTranscriptApi

try:
    from youtube_transcript_api._errors import IpBlocked, RequestBlocked
except Exception:  # pragma: no cover
    IpBlocked = RequestBlocked = None  # type: ignore[misc,assignment]

try:
    from youtube_transcript_api.proxies import GenericProxyConfig, WebshareProxyConfig
except Exception:  # pragma: no cover
    GenericProxyConfig = WebshareProxyConfig = None  # type: ignore[misc,assignment]


def now_iso() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    os.replace(tmp, path)


def atomic_write_json(path: Path, data: Any) -> None:
    atomic_write_text(path, json.dumps(data, ensure_ascii=False, indent=2) + "\n")


YOUTUBE_ID_RE = re.compile(
    r"(?:youtube\.com/(?:watch\?.*?v=|shorts/)|youtu\.be/)([A-Za-z0-9_-]{5,})"
)


def canonical_watch_url(video_id: str) -> str:
    return f"https://www.youtube.com/watch?v={video_id}"


@dataclasses.dataclass(frozen=True)
class VideoRef:
    video_id: str
    url: str
    title_hint: str | None
    source_file: str
    source_line: int


def extract_video_refs_from_text(text: str, source_file: str) -> list[VideoRef]:
    refs: list[VideoRef] = []
    for idx, line in enumerate(text.splitlines(), start=1):
        for match in YOUTUBE_ID_RE.finditer(line):
            video_id = match.group(1)
            url = canonical_watch_url(video_id)

            title_hint: str | None = None
            # Common formats:
            #  - "1. https://...  # title (channel_url)"
            #  - "| ... | https://... | video_id |"
            if "#" in line:
                title_hint = line.split("#", 1)[1].strip() or None
            refs.append(
                VideoRef(
                    video_id=video_id,
                    url=url,
                    title_hint=title_hint,
                    source_file=source_file,
                    source_line=idx,
                )
            )
    return refs


FILE_URI_RE = re.compile(r"file://[^)>\\s]+")


def decode_file_uri(uri: str) -> Path | None:
    # Minimal decode: only handle %XX.
    if not uri.startswith("file://"):
        return None
    from urllib.parse import unquote

    return Path(unquote(uri[len("file://") :]))


def discover_default_sources(primary_input: Path) -> list[Path]:
    sources: list[Path] = [primary_input]

    # If the current folder has a channel list, include it.
    sibling = primary_input.parent / "channel_videos_all.md"
    if sibling.exists():
        sources.append(sibling)

    # Also include the other Founder_Agent_Phase1 location (full-width parentheses),
    # because the channel-scan lists are not identical and union helps reach 680+.
    def find_repo_root(start: Path) -> Path:
        cur = start.resolve()
        for parent in [cur, *cur.parents]:
            if (parent / "aipm_v0").exists():
                return parent
        return Path.cwd()

    repo_root = find_repo_root(Path(__file__))
    candidates = [
        repo_root
        / "aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/1_initiating/project_charter_youtube_videos_from_channels_all.md",
        repo_root
        / "aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/1_initiating/project_charter_youtube_videos.md",
    ]
    sources.extend([p for p in candidates if p.exists()])
    return sources


def load_sources(sources: list[Path]) -> dict[str, str]:
    out: dict[str, str] = {}
    for p in sources:
        try:
            out[str(p)] = p.read_text(encoding="utf-8", errors="replace")
        except FileNotFoundError:
            continue
    return out


def expand_file_links(texts_by_path: dict[str, str]) -> list[Path]:
    paths: list[Path] = []
    for src_path, text in texts_by_path.items():
        for uri in FILE_URI_RE.findall(text):
            p = decode_file_uri(uri)
            if p and p.exists() and p.is_file():
                paths.append(p)
    # De-dupe while preserving order
    seen: set[str] = set()
    uniq: list[Path] = []
    for p in paths:
        sp = str(p)
        if sp in seen:
            continue
        seen.add(sp)
        uniq.append(p)
    return uniq


def gather_video_refs(primary_input: Path, extra_sources: list[Path]) -> list[VideoRef]:
    sources = [primary_input, *extra_sources]
    texts_by_path = load_sources(sources)
    linked_files = expand_file_links(texts_by_path)
    for p in linked_files:
        if str(p) not in texts_by_path:
            try:
                texts_by_path[str(p)] = p.read_text(encoding="utf-8", errors="replace")
            except FileNotFoundError:
                pass

    all_refs: list[VideoRef] = []
    for path_str, text in texts_by_path.items():
        all_refs.extend(extract_video_refs_from_text(text, source_file=path_str))
    return all_refs


def load_status(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"meta": {"created_at": now_iso()}, "videos": {}}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"meta": {"created_at": now_iso(), "status_load_error": True}, "videos": {}}


def save_status(path: Path, status: dict[str, Any]) -> None:
    status.setdefault("meta", {})["updated_at"] = now_iso()
    atomic_write_json(path, status)


def format_transcript_md(
    video_id: str,
    url: str,
    language: str | None,
    title_hint: str | None,
    segments: list[dict[str, Any]],
) -> str:
    lines: list[str] = []
    lines.append(f"# Transcript: {video_id}")
    lines.append("")
    lines.append(f"- URL: {url}")
    if title_hint:
        lines.append(f"- Title hint: {title_hint}")
    if language:
        lines.append(f"- Language: {language}")
    lines.append(f"- Retrieved at: {now_iso()}")
    lines.append("")
    lines.append("## Text")
    lines.append("")
    for seg in segments:
        start = seg.get("start")
        text = (seg.get("text") or "").strip()
        if text == "":
            continue
        # Timestamp format: mm:ss
        if isinstance(start, (int, float)):
            m, s = divmod(int(start), 60)
            ts = f"{m:02d}:{s:02d}"
            lines.append(f"- [{ts}] {text}")
        else:
            lines.append(f"- {text}")
    lines.append("")
    return "\n".join(lines)


def sleep_with_jitter(seconds: float) -> None:
    jitter = random.uniform(0.05, 0.25)
    time.sleep(max(0.0, seconds + jitter))


def parse_csv_list(value: str) -> list[str]:
    return [s.strip() for s in (value or "").split(",") if s.strip()]


def parse_int_range(value: str) -> tuple[int, int]:
    # Accept "30,180" or "30-180"
    raw = (value or "").strip()
    if "," in raw:
        a, b = raw.split(",", 1)
    elif "-" in raw:
        a, b = raw.split("-", 1)
    else:
        raise ValueError("expected 'min,max' or 'min-max'")
    return int(a.strip()), int(b.strip())


def is_blocked_error(exc: Exception) -> bool:
    if RequestBlocked is not None and isinstance(exc, RequestBlocked):
        return True
    if IpBlocked is not None and isinstance(exc, IpBlocked):
        return True
    return False


def maybe_sleep_until(iso_ts: str | None) -> None:
    if not iso_ts:
        return
    try:
        until = dt.datetime.fromisoformat(iso_ts)
    except Exception:
        return
    now = dt.datetime.now().astimezone()
    if until.tzinfo is None:
        until = until.replace(tzinfo=now.tzinfo)
    remaining = (until - now).total_seconds()
    if remaining > 1:
        print(f"cooldown active; sleeping {int(remaining)}s until {until.isoformat(timespec='seconds')}")
        time.sleep(remaining)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fetch YouTube transcripts (Founder Agent) with safe rate limiting and resume support."
    )
    parser.add_argument(
        "--input",
        default="aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/references/transcripts/video_url_list.md",
        help="Primary input file (markdown/csv) that contains YouTube URLs.",
    )
    parser.add_argument(
        "--include-default-sources",
        action="store_true",
        help="Include known project sources to reach 680+ URLs (recommended).",
    )
    parser.add_argument(
        "--extra-source",
        action="append",
        default=[],
        help="Additional file path to scan for URLs (repeatable).",
    )
    parser.add_argument(
        "--transcripts-dir",
        default="aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/references/transcripts/items",
        help="Output directory for per-video transcript markdown files.",
    )
    parser.add_argument(
        "--status",
        default="aipm_v0/Stock/programs/創業支援・新規事業開発（AIエージェント）/projects/Founder_Agent_Phase1/documents/references/transcripts/transcript_status_report.json",
        help="Progress/status JSON path.",
    )
    parser.add_argument("--languages", default="ja,ja-JP,en", help="Comma-separated languages preference.")
    parser.add_argument("--sleep-seconds", type=float, default=2.0, help="Base sleep between requests.")
    parser.add_argument("--batch-size", type=int, default=30, help="Requests per batch before resting.")
    parser.add_argument("--batch-rest-seconds", type=float, default=60.0, help="Rest after each batch.")
    parser.add_argument("--max-retries", type=int, default=3, help="Max retries per video on errors.")
    parser.add_argument(
        "--backoff-seconds",
        default="5,10,20,60",
        help="Comma-separated backoff seconds for retry (cycled).",
    )
    parser.add_argument("--limit", type=int, default=0, help="Limit number of videos to process (0=all).")
    parser.add_argument("--dry-run", action="store_true", help="Only show counts; do not fetch transcripts.")

    # Circuit breaker for IP blocks
    parser.add_argument(
        "--blocked-threshold",
        type=int,
        default=3,
        help="Trigger global cooldown after this many consecutive RequestBlocked/IpBlocked events.",
    )
    parser.add_argument(
        "--cooldown-minutes",
        default="30,180",
        help="Global cooldown range in minutes, e.g. '30,180' (randomized).",
    )
    parser.add_argument(
        "--session-rotate-every",
        type=int,
        default=20,
        help="Recreate API session after N fetch attempts to encourage proxy rotation (0=disable).",
    )
    parser.add_argument(
        "--rotate-on-block",
        dest="rotate_on_block",
        action="store_true",
        default=True,
        help="Recreate API session immediately after RequestBlocked/IpBlocked.",
    )
    parser.add_argument(
        "--no-rotate-on-block",
        dest="rotate_on_block",
        action="store_false",
        help="Disable session rotation on block events.",
    )

    # Proxy options
    parser.add_argument(
        "--proxy-http-url",
        default="",
        help="Generic HTTP proxy URL, e.g. http://user:pass@host:port",
    )
    parser.add_argument(
        "--proxy-https-url",
        default="",
        help="Generic HTTPS proxy URL, e.g. https://user:pass@host:port",
    )
    parser.add_argument("--webshare-username", default="", help="Webshare proxy username.")
    parser.add_argument("--webshare-password", default="", help="Webshare proxy password.")
    parser.add_argument(
        "--webshare-locations",
        default="",
        help="Optional comma-separated country codes for Webshare IP filtering (e.g. 'jp,us').",
    )
    args = parser.parse_args()

    if not args.webshare_username:
        args.webshare_username = os.getenv("WEBSHARE_USERNAME", "")
    if not args.webshare_password:
        args.webshare_password = os.getenv("WEBSHARE_PASSWORD", "")
    if not args.webshare_locations:
        args.webshare_locations = os.getenv("WEBSHARE_LOCATIONS", "")
    if not args.proxy_http_url:
        args.proxy_http_url = os.getenv("PROXY_HTTP_URL", "")
    if not args.proxy_https_url:
        args.proxy_https_url = os.getenv("PROXY_HTTPS_URL", "")

    primary_input = Path(args.input)
    if not primary_input.exists():
        print(f"ERROR: input not found: {primary_input}", file=sys.stderr)
        return 2

    extra_sources: list[Path] = [Path(p) for p in args.extra_source]
    if args.include_default_sources:
        extra_sources = discover_default_sources(primary_input) + extra_sources
        # Remove primary_input duplicates
        uniq: list[Path] = []
        seen: set[str] = set()
        for p in extra_sources:
            sp = str(p)
            if sp in seen:
                continue
            seen.add(sp)
            if p == primary_input:
                continue
            uniq.append(p)
        extra_sources = uniq

    refs = gather_video_refs(primary_input, extra_sources=extra_sources)
    by_id: dict[str, list[VideoRef]] = {}
    for ref in refs:
        by_id.setdefault(ref.video_id, []).append(ref)

    video_ids = sorted(by_id.keys())
    print(f"found_video_ids={len(video_ids)} from_sources={1+len(extra_sources)}")
    if args.dry_run:
        return 0

    transcripts_dir = Path(args.transcripts_dir)
    status_path = Path(args.status)
    status = load_status(status_path)
    status.setdefault("meta", {}).setdefault("started_at", now_iso())
    status["meta"]["config"] = {
        "input": str(primary_input),
        "extra_sources": [str(p) for p in extra_sources],
        "transcripts_dir": str(transcripts_dir),
        "languages": args.languages,
        "sleep_seconds": args.sleep_seconds,
        "batch_size": args.batch_size,
        "batch_rest_seconds": args.batch_rest_seconds,
        "max_retries": args.max_retries,
        "backoff_seconds": args.backoff_seconds,
        "session_rotate_every": args.session_rotate_every,
        "rotate_on_block": args.rotate_on_block,
    }
    status.setdefault("videos", {})

    languages = [s.strip() for s in args.languages.split(",") if s.strip()]
    backoffs = [float(x.strip()) for x in str(args.backoff_seconds).split(",") if x.strip()]
    if not backoffs:
        backoffs = [5.0, 10.0, 20.0, 60.0]

    processed = 0
    completed_this_run = 0
    failures_this_run = 0

    def already_done(vid: str) -> bool:
        entry = status["videos"].get(vid, {})
        return entry.get("status") == "success"

    pending = [vid for vid in video_ids if not already_done(vid)]
    if args.limit and args.limit > 0:
        pending = pending[: args.limit]

    print(f"pending={len(pending)}")
    save_status(status_path, status)

    proxy_config = None
    if args.webshare_username and args.webshare_password:
        if WebshareProxyConfig is None:
            print("ERROR: WebshareProxyConfig is not available in this youtube_transcript_api version.", file=sys.stderr)
            return 2
        locs = parse_csv_list(args.webshare_locations)
        if locs:
            proxy_config = WebshareProxyConfig(
                proxy_username=args.webshare_username,
                proxy_password=args.webshare_password,
                filter_ip_locations=locs,
            )
        else:
            proxy_config = WebshareProxyConfig(
                proxy_username=args.webshare_username,
                proxy_password=args.webshare_password,
            )
    elif args.proxy_http_url or args.proxy_https_url:
        if GenericProxyConfig is None:
            print("ERROR: GenericProxyConfig is not available in this youtube_transcript_api version.", file=sys.stderr)
            return 2
        proxy_config = GenericProxyConfig(
            http_url=args.proxy_http_url or None,
            https_url=args.proxy_https_url or None,
        )

    def new_api():
        return YouTubeTranscriptApi(proxy_config=proxy_config)

    api = new_api()
    session_requests = 0

    cb = status.setdefault("meta", {}).setdefault("circuit_breaker", {})
    cb.setdefault("consecutive_blocked", 0)
    cb.setdefault("blocked_events_total", 0)
    maybe_sleep_until(cb.get("cooldown_until"))

    try:
        cooldown_min, cooldown_max = parse_int_range(args.cooldown_minutes)
    except Exception:
        print("ERROR: --cooldown-minutes must be 'min,max' or 'min-max' (minutes).", file=sys.stderr)
        return 2

    def trigger_cooldown() -> None:
        minutes = random.randint(min(cooldown_min, cooldown_max), max(cooldown_min, cooldown_max))
        until = dt.datetime.now().astimezone() + dt.timedelta(minutes=minutes)
        cb["cooldown_until"] = until.isoformat(timespec="seconds")
        cb["cooldown_minutes_last"] = minutes
        cb["cooldown_triggered_at"] = now_iso()
        print(
            f"circuit breaker: consecutive_blocked={cb.get('consecutive_blocked')} "
            f"-> cooldown {minutes}min until {cb['cooldown_until']}"
        )
        save_status(status_path, status)
        maybe_sleep_until(cb.get("cooldown_until"))

    for idx, video_id in enumerate(pending, start=1):
        processed += 1
        url = canonical_watch_url(video_id)

        refs_for_id = by_id.get(video_id, [])
        title_hint = next((r.title_hint for r in refs_for_id if r.title_hint), None)
        sources_compact = [
            {"file": r.source_file, "line": r.source_line} for r in refs_for_id[:10]
        ]

        entry = status["videos"].setdefault(video_id, {})
        entry.setdefault("attempts", 0)
        entry["url"] = url
        entry["title_hint"] = title_hint
        entry["sources"] = sources_compact
        entry["updated_at"] = now_iso()

        if idx > 1:
            sleep_with_jitter(args.sleep_seconds)

        # Batch rest
        if args.batch_size > 0 and (idx - 1) % args.batch_size == 0 and idx != 1:
            print(f"[{idx}/{len(pending)}] batch_rest {args.batch_rest_seconds}s")
            sleep_with_jitter(args.batch_rest_seconds)

        success = False
        last_error: str | None = None
        used_lang: str | None = None
        segments: list[dict[str, Any]] | None = None

        for attempt in range(1, args.max_retries + 1):
            if args.session_rotate_every > 0 and session_requests >= args.session_rotate_every:
                api = new_api()
                session_requests = 0
            entry["attempts"] = entry.get("attempts", 0) + 1
            try:
                session_requests += 1
                fetched = api.fetch(video_id, languages=languages)
                segments = fetched.to_raw_data()
                used_lang = None  # best-effort only (package version dependent)
                success = True
                cb["consecutive_blocked"] = 0
                break
            except Exception as e:
                last_error = f"{type(e).__name__}: {e}"
                entry["last_error"] = last_error
                if is_blocked_error(e):
                    entry["status"] = "blocked"
                    cb["blocked_events_total"] = int(cb.get("blocked_events_total", 0)) + 1
                    cb["consecutive_blocked"] = int(cb.get("consecutive_blocked", 0)) + 1
                    cb["last_blocked_at"] = now_iso()
                    if args.rotate_on_block:
                        api = new_api()
                        session_requests = 0
                    save_status(status_path, status)

                    print(
                        f"[{idx}/{len(pending)}] {video_id} blocked "
                        f"(consecutive={cb['consecutive_blocked']})"
                    )
                    if args.blocked_threshold > 0 and cb["consecutive_blocked"] >= args.blocked_threshold:
                        trigger_cooldown()
                        cb["consecutive_blocked"] = 0
                        save_status(status_path, status)
                    break

                entry["status"] = "retrying"
                entry["updated_at"] = now_iso()
                save_status(status_path, status)

                backoff = backoffs[(attempt - 1) % len(backoffs)]
                print(f"[{idx}/{len(pending)}] {video_id} attempt={attempt} error={last_error} backoff={backoff}s")
                sleep_with_jitter(backoff)

        if success and segments is not None:
            out_path = transcripts_dir / f"{video_id}.md"
            md = format_transcript_md(
                video_id=video_id,
                url=url,
                language=used_lang,
                title_hint=title_hint,
                segments=segments,
            )
            atomic_write_text(out_path, md)
            entry["status"] = "success"
            entry["output"] = str(out_path)
            entry["last_error"] = None
            completed_this_run += 1
        else:
            entry["status"] = "failed"
            entry["last_error"] = last_error
            failures_this_run += 1

        entry["updated_at"] = now_iso()
        status["meta"]["progress"] = {
            "processed_this_run": processed,
            "completed_this_run": completed_this_run,
            "failed_this_run": failures_this_run,
            "pending_remaining_estimate": max(0, len(pending) - idx),
        }
        save_status(status_path, status)

        if entry["status"] == "success":
            print(f"[{idx}/{len(pending)}] success {video_id}")
        else:
            print(f"[{idx}/{len(pending)}] failed  {video_id}: {entry.get('last_error')}")

    status["meta"]["finished_at"] = now_iso()
    save_status(status_path, status)
    print(f"done completed={completed_this_run} failed={failures_this_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
