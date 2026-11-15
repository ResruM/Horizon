"""Run Horizon and publish only psychology items not delivered before.

GitHub Actions runs this several times a day (one item per batch) so the
daily reading load stays small while every batch still brings something new.
The workflow calls ``finish`` after each batch to archive the fragments.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
import json

SCORES = Path("/tmp/scores.json")
SUMMARIES = ROOT / "data" / "summaries"
POSTS = ROOT / "docs" / "_posts"
ARCHIVE = ROOT / "data" / "summaries_archive"
FRAGMENTS = ROOT / "data" / "fragments"
SEEN = ROOT / "horizon_seen.json"

# Psychological/institutional journals that publish sparsely but matter most:
# they get prioritised inside a batch when scores are close.
BOOST_SOURCES = ("PNAS", "Association for Psychological Science", "Nature Psychology")


def load_seen() -> set[str]:
    try:
        return set(json.loads(SEEN.read_text(encoding="utf-8")))
    except (OSError, ValueError):
        return set()


def norm(url: str) -> str:
    return url.split("?")[0]


def pick_batch(limit: int) -> list[dict]:
    rows = json.loads(SCORES.read_text(encoding="utf-8")) if SCORES.exists() else []
    seen = load_seen()
    ranked = []
    for row in rows:
        profile, score, source, title, url = row[:5]
        excerpt = row[5] if len(row) > 5 else ""
        if norm(url) in seen:
            continue
        boost = 1.0 if any(name in (source or "") for name in BOOST_SOURCES) else 0.0
        ranked.append((boost, score or 0, source or "", title, url, excerpt))
    ranked.sort(key=lambda r: (r[0], r[1]), reverse=True)
    return [
        {
            "source": r[2],
            "title": r[3],
            "url": r[4],
            "score": r[1],
            "content": r[5],
        }
        for r in ranked[:limit]
    ]


def _next_index(date: str) -> int:
    existing = list(FRAGMENTS.glob(f"{date}-batch*-zh.md"))
    return len(existing) + 1


def publish(batch: list[dict], date: str) -> None:
    """Append the batch to today's page and refresh the published summary."""
    FRAGMENTS.mkdir(parents=True, exist_ok=True)
    index = _next_index(date)
    for lang in ("zh", "en"):
        (FRAGMENTS / f"{date}-batch{index}-{lang}.md").write_text(
            _render(batch, lang), encoding="utf-8"
        )
    (FRAGMENTS / f"{date}-batch{index}.json").write_text(
        json.dumps(batch, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    _rebuild_today(date)
    record(batch)


def _render(batch: list[dict], lang: str) -> str:
    header = "## 心理学前沿 · 本批" if lang == "zh" else "## Psychology Frontiers · this batch"
    lines = [header, ""]
    for idx, item in enumerate(batch, start=1):
        lines.append(f"{idx}. [{item['title']}]({item['url']})")
    lines.append("")
    return "\n".join(lines)


def _rebuild_today(date: str) -> None:
    parts_all = []
    for lang, title in (("zh", "心理学前沿日报"), ("en", "Psychology Frontiers Daily")):
        parts = sorted(FRAGMENTS.glob(f"{date}-batch*-{lang}.md"))
        body = "\n\n".join(p.read_text(encoding="utf-8").strip() for p in parts)
        doc = f"# {title} - {date}\n\n{body}\n"
        (SUMMARIES / f"horizon-{date}-{lang}.md").write_text(doc, encoding="utf-8")
        # Jekyll source that the Pages workflow publishes.
        POSTS.mkdir(parents=True, exist_ok=True)
        front = (
            "---\n"
            f'layout: default\ntitle: "{"Horizon Summary"}: {date} ({"ZH" if lang == "zh" else "EN"})"\n'
            f"date: {date}\nlang: {lang}\n---\n\n"
        )
        (POSTS / f"{date}-summary-{lang}.md").write_text(front + doc, encoding="utf-8")
        parts_all.extend(parts)
    return None


def record(batch: list[dict]) -> None:
    seen = load_seen()
    seen.update(norm(item["url"]) for item in batch)
    SEEN.write_text(json.dumps(sorted(seen), ensure_ascii=False, indent=1), encoding="utf-8")


def finish(date: str) -> None:
    """Refresh today's page and keep a copy in the archive."""
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    if not list(FRAGMENTS.glob(f"{date}-batch*-zh.md")):
        return
    _rebuild_today(date)
    for lang in ("zh", "en"):
        src = SUMMARIES / f"horizon-{date}-{lang}.md"
        if src.exists():
            (ARCHIVE / f"{date}-{lang}.md").write_text(
                src.read_text(encoding="utf-8"), encoding="utf-8"
            )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("action", choices=["select", "finish"])
    ap.add_argument("--limit", type=int, default=3)
    ap.add_argument("--date", required=False)
    args = ap.parse_args()
    if args.date:
        date = args.date
    else:
        # Digests are dated by Beijing time, not the runner's UTC clock.
        from datetime import datetime as _dt, timedelta as _td, timezone as _tz
        date = _dt.now(_tz(_td(hours=8))).date().isoformat()
    if args.action == "finish":
        finish(date)
        return 0
    print(f"seen={len(load_seen())} scores={SCORES.exists()}", flush=True)
    batch = pick_batch(args.limit)
    if not batch:
        print("no unseen psychology items left in the window")
        return 0
    publish(batch, date)
    for item in batch:
        print(f"batch item: {item['score']} | {item['source']} | {item['title'][:60]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
