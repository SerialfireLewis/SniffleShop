#!/usr/bin/env python3
"""Lightweight reachability checker for external URLs in a SideStore source."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


def collect_urls(source: dict) -> list[tuple[str, str]]:
    urls: list[tuple[str, str]] = []
    for app in source.get("apps", []):
        name = app.get("name", "<unknown>")
        if app.get("iconURL"):
            urls.append((f"{name} icon", app["iconURL"]))
        for i, url in enumerate(app.get("screenshotURLs", []), 1):
            urls.append((f"{name} screenshot {i}", url))
        for version in app.get("versions", []):
            urls.append((f"{name} {version.get('version', '?')} IPA", version["downloadURL"]))
    for item in source.get("news", []):
        if item.get("imageURL"):
            urls.append((f"news {item.get('identifier', '?')} image", item["imageURL"]))
        if item.get("url"):
            urls.append((f"news {item.get('identifier', '?')} link", item["url"]))
    return urls


def check(url: str, timeout: float) -> tuple[int, str, str | None]:
    headers = {"User-Agent": "SniffleShop-link-check/1.0", "Accept": "*/*"}
    try:
        req = urllib.request.Request(url, headers=headers, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.geturl(), response.headers.get("Content-Length")
    except urllib.error.HTTPError as exc:
        if exc.code not in (403, 405):
            raise

    headers["Range"] = "bytes=0-0"
    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return response.status, response.geturl(), response.headers.get("Content-Length")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?", default="source.json")
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args()

    data = json.loads(Path(args.source).read_text(encoding="utf-8"))
    urls = collect_urls(data)
    failures = 0

    for label, url in urls:
        try:
            status, final_url, content_length = check(url, args.timeout)
            if status < 200 or status >= 400:
                raise RuntimeError(f"HTTP {status}")
            suffix = f" ({content_length} bytes reported)" if content_length else ""
            print(f"OK   {label}: HTTP {status}{suffix}")
        except Exception as exc:
            failures += 1
            print(f"FAIL {label}: {url} -> {exc}", file=sys.stderr)

    print(f"Checked {len(urls)} URLs; {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
