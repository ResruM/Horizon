"""Turn the last published psychology batch into a Chinese digest with summaries.

The batch publisher (``psychological_batch.py``) only keeps titles and links.
This script asks the configured model for one Chinese headline plus a short
summary per item, then rewrites the day's summary and the Jekyll post so the
published page is readable without opening every paper.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUMMARIES = ROOT / "data" / "summaries"
FRAGMENTS = ROOT / "data" / "fragments"
POSTS = ROOT / "docs" / "_posts"

SYSTEM = """你是心理学编辑。给你若干条心理学/神经科学论文条目（英文标题 + 原文链接 + 摘要片段）。
请为每一条输出：
- title: 中文标题，20 字以内，准确、不含"研究"二字堆砌，不要生造结论
- summary: 120-180 字中文摘要，说清研究对象/样本、方法、主要结果（关键数字）、以及一句结论或限制
- why: 30-60 字中文，这条对心理学读者为什么值得看

只输出 JSON：{"items":[{"index":1,"title":"...","summary":"...","why":"..."}]}
内容必须忠实于给出的材料；材料不足时宁可写得更保守，不要编造数据。
"""


def _today() -> str:
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).date().isoformat()


def _load_batch(date: str) -> list[dict]:
    files = sorted(FRAGMENTS.glob(f"{date}-batch*.json"))
    if not files:
        return []
    out: list[dict] = []
    for path in files:
        try:
            out.extend(json.loads(path.read_text(encoding="utf-8")))
        except ValueError:
            continue
    return out


async def _summarize(entries: list[dict]) -> list[dict]:
    from openai import AsyncOpenAI

    cfg = json.loads((ROOT / "data" / "config.json").read_text(encoding="utf-8"))
    ai = cfg["ai"]
    key = os.getenv(ai.get("api_key_env", "DEEPSEEK_API_KEY"), "")
    client = AsyncOpenAI(
        api_key=key,
        base_url=ai.get("base_url") or "https://api.deepseek.com",
        timeout=120,
    )
    payload = [
        {
            "index": i,
            "title": e.get("title", ""),
            "url": e.get("url", ""),
            "source": e.get("source", ""),
            "excerpt": (e.get("content") or "")[:1500],
        }
        for i, e in enumerate(entries, start=1)
    ]
    resp = await client.chat.completions.create(
        model=ai.get("model", "deepseek-chat"),
        temperature=0.2,
        max_tokens=3000,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
    )
    data = json.loads(resp.choices[0].message.content or "{}")
    return data.get("items", [])


def _render(items: list[dict], originals: list[dict], date: str) -> str:
    lines = [
        f"# 心理学前沿日报 - {date}",
        "",
        f"> 今日 {len(items)} 条，均为此前未推送过的心理学/神经科学新研究。",
        "",
        "---",
        "",
    ]
    for item in items:
        idx = int(item.get("index", 0))
        src = originals[idx - 1] if 0 < idx <= len(originals) else {}
        url = src.get("url", "")
        name = src.get("source") or src.get("feed_name") or ""
        lines.append(f"## {idx}. {item.get('title', '')}")
        lines.append("")
        if url:
            lines.append(f"[原文]({url}) · {name}")
            lines.append("")
        lines.append(item.get("summary", "").strip())
        lines.append("")
        why = (item.get("why") or "").strip()
        if why:
            lines.append(f"**为什么值得看**：{why}")
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def _write(date: str, markdown: str) -> None:
    SUMMARIES.mkdir(parents=True, exist_ok=True)
    (SUMMARIES / f"horizon-{date}-zh.md").write_text(markdown, encoding="utf-8")
    POSTS.mkdir(parents=True, exist_ok=True)
    front = (
        "---\n"
        f'layout: default\ntitle: "心理学前沿日报 {date}"\n'
        f"date: {date}\nlang: zh\n---\n\n"
    )
    (POSTS / f"{date}-summary-zh.md").write_text(front + markdown, encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None)
    args = ap.parse_args()
    date = args.date or _today()
    entries = _load_batch(date)
    if not entries:
        print(f"no batch for {date}")
        return 0
    try:
        items = asyncio.run(_summarize(entries))
    except Exception as exc:  # keep the batch visible even if the model fails
        print(f"summarize failed: {type(exc).__name__}: {exc}")
        return 1
    if not items:
        print("model returned no items")
        return 1
    md = _render(items, entries, date)
    _write(date, md)
    print(f"wrote {len(items)} item(s) for {date}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
