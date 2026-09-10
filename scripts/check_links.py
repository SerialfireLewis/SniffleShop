#!/usr/bin/env python3
"""Check every external URL in a SideStore source and verify declared IPA sizes."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


def collect_urls(source: dict) -> list[tuple[str, str, int | None]]:
    urls: list[tuple[str, str, int | None]] = []
    for app in source.get("apps", []):
        name = app.get("name", "<unknown>")
        if app.get("iconURL"):
            urls.append((f"{name} icon", app["iconURL"], None))
        for i, url in enumerate(app.get("screenshotURLs", []), 1):
            urls.append((f"{name} screenshot {i}", url, None))
        for version in app.get("versions", []):
            expected = version.get("size")
            if isinstance(expected, float) and expected.is_integer():
                expected = int(expected)
            urls.append((
                f"{name} {version.get('version', '?')} IPA",
                version["downloadURL"],
                expected if isinstance(expected, int) and not isinstance(expected, bool) else None,
            ))
    for item in source.get("news", []):
        if item.get("imageURL"):
            urls.append((f"news {item.get('identifier', '?')} image", item["imageURL"], None))
        if item.get("url"):
            urls.append((f"news {item.get('identifier', '?')} link", item["url"], None))
    return urls


def response_size(headers) -> int | None:
    """Return total object size, preferring Content-Range when a ranged GET was used."""
    content_range = headers.get("Content-Range")
    if content_range:
        match = re.search(r"/(\d+)$", content_range)
        if match:
            return int(match.group(1))
    content_length = headers.get("Content-Length")
    if content_length and content_length.isdigit():
        return int(content_length)
    return None


def check(url: str, timeout: float) -> tuple[int, str, int | None]:
    headers = {"User-Agent": "SniffleShop-link-check/2.0", "Accept": "*/*"}
    try:
        req = urllib.request.Request(url, headers=headers, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status, response.geturl(), response_size(response.headers)
    except urllib.error.HTTPError as exc:
        if exc.code not in (403, 405):
            raise

    # Some CDNs reject HEAD. Ask for one byte and use Content-Range's total size.
    headers["Range"] = "bytes=0-0"
    req = urllib.request.Request(url, headers=headers, method="GET")
    with urllib.request.urlopen(req, timeout=timeout) as response:
        size = response_size(response.headers)
        # A server that ignored Range may report the full Content-Length, which is fine.
        return response.status, response.geturl(), size


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?", default="source.json")
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args()

    data = json.loads(Path(args.source).read_text(encoding="utf-8"))
    urls = collect_urls(data)
    failures = 0
    size_checks = 0

    for label, url, expected_size in urls:
        try:
            status, final_url, remote_size = check(url, args.timeout)
            if status < 200 or status >= 400:
                raise RuntimeError(f"HTTP {status}")
            if expected_size is not None and remote_size is not None:
                size_checks += 1
                if remote_size != expected_size:
                    raise RuntimeError(
                        f"size mismatch: source={expected_size} bytes, upstream={remote_size} bytes"
                    )
            suffix = f" ({remote_size} bytes reported)" if remote_size is not None else ""
            print(f"OK   {label}: HTTP {status}{suffix}")
        except Exception as exc:
            failures += 1
            print(f"FAIL {label}: {url} -> {exc}", file=sys.stderr)

    print(f"Checked {len(urls)} URLs and {size_checks} declared IPA sizes; {failures} failure(s).")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
