#!/usr/bin/env python3
"""Validate a SniffleShop source against SideStore's strict source shape.

This intentionally rejects newer AltStore-only keys that SideStore's strict
schema does not accept, such as appPermissions, category, buildVersion, and
platform.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

SOURCE_REQUIRED = {"name", "identifier", "apps"}
SOURCE_ALLOWED = SOURCE_REQUIRED | {"news", "sourceURL"}

APP_REQUIRED = {
    "name", "bundleIdentifier", "developerName", "localizedDescription",
    "iconURL", "versions",
}
APP_ALLOWED = APP_REQUIRED | {
    "beta", "downloadURL", "permissions", "screenshotURLs", "size", "subtitle",
    "tintColor", "version", "versionDate", "versionDescription",
}

VERSION_REQUIRED = {"version", "date", "downloadURL", "size"}
VERSION_ALLOWED = VERSION_REQUIRED | {
    "localizedDescription", "minOSVersion", "maxOSVersion",
}

PERMISSION_ALLOWED = {"type", "usageDescription"}
PERMISSION_TYPES = {
    "photos", "camera", "location", "contacts", "reminders", "music",
    "microphone", "speech-recognition", "background-audio",
    "background-fetch", "bluetooth", "network", "calendars", "faceid",
    "siri", "motion",
}

NEWS_REQUIRED = {"title", "identifier", "caption", "date"}
NEWS_ALLOWED = NEWS_REQUIRED | {
    "appID", "imageURL", "notify", "tintColor", "url",
}


class ValidationError(Exception):
    pass


def fail(path: str, message: str) -> None:
    raise ValidationError(f"{path}: {message}")


def require_object(value, path: str) -> dict:
    if not isinstance(value, dict):
        fail(path, "must be an object")
    return value


def require_string(value, path: str, *, nonempty: bool = True) -> str:
    if not isinstance(value, str):
        fail(path, "must be a string")
    if nonempty and not value.strip():
        fail(path, "must not be empty")
    return value


def check_keys(obj: dict, path: str, required: set[str], allowed: set[str]) -> None:
    missing = sorted(required - obj.keys())
    extra = sorted(obj.keys() - allowed)
    if missing:
        fail(path, f"missing required key(s): {', '.join(missing)}")
    if extra:
        fail(path, f"unsupported key(s): {', '.join(extra)}")


def check_https_url(value, path: str) -> None:
    value = require_string(value, path)
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        fail(path, "must be an absolute HTTPS URL")


def parse_date(value, path: str) -> datetime:
    text = require_string(value, path)
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError as exc:
        fail(path, f"invalid ISO-8601 date: {text!r}")
        raise AssertionError from exc


def validate_version(version, path: str) -> datetime:
    version = require_object(version, path)
    check_keys(version, path, VERSION_REQUIRED, VERSION_ALLOWED)
    require_string(version["version"], f"{path}.version")
    date = parse_date(version["date"], f"{path}.date")
    check_https_url(version["downloadURL"], f"{path}.downloadURL")
    size = version["size"]
    if isinstance(size, bool) or not isinstance(size, (int, float)) or size <= 0:
        fail(f"{path}.size", "must be a positive number of bytes")
    for key in ("localizedDescription", "minOSVersion", "maxOSVersion"):
        if key in version:
            require_string(version[key], f"{path}.{key}")
    return date


def validate_app(app, index: int) -> str:
    path = f"apps[{index}]"
    app = require_object(app, path)
    check_keys(app, path, APP_REQUIRED, APP_ALLOWED)

    for key in ("name", "bundleIdentifier", "developerName", "localizedDescription"):
        require_string(app[key], f"{path}.{key}")
    check_https_url(app["iconURL"], f"{path}.iconURL")

    if "beta" in app and not isinstance(app["beta"], bool):
        fail(f"{path}.beta", "must be boolean")
    if "subtitle" in app:
        require_string(app["subtitle"], f"{path}.subtitle")
    if "tintColor" in app:
        import re
        tint = require_string(app["tintColor"], f"{path}.tintColor")
        if not re.fullmatch(r"#?[0-9A-Fa-f]{6}", tint):
            fail(f"{path}.tintColor", "must be a 6-digit hex color")

    screenshots = app.get("screenshotURLs", [])
    if not isinstance(screenshots, list):
        fail(f"{path}.screenshotURLs", "must be an array")
    for i, url in enumerate(screenshots):
        check_https_url(url, f"{path}.screenshotURLs[{i}]")

    permissions = app.get("permissions", [])
    if not isinstance(permissions, list):
        fail(f"{path}.permissions", "must be an array")
    for i, permission in enumerate(permissions):
        ppath = f"{path}.permissions[{i}]"
        permission = require_object(permission, ppath)
        check_keys(permission, ppath, PERMISSION_ALLOWED, PERMISSION_ALLOWED)
        ptype = require_string(permission["type"], f"{ppath}.type")
        if ptype not in PERMISSION_TYPES:
            fail(f"{ppath}.type", f"unsupported SideStore permission type: {ptype}")
        require_string(permission["usageDescription"], f"{ppath}.usageDescription")

    versions = app["versions"]
    if not isinstance(versions, list) or not versions:
        fail(f"{path}.versions", "must be a non-empty array")

    dates = [validate_version(v, f"{path}.versions[{i}]") for i, v in enumerate(versions)]
    aware = [d.tzinfo is not None for d in dates]
    if all(aware) or not any(aware):
        for i in range(len(dates) - 1):
            if dates[i] < dates[i + 1]:
                fail(f"{path}.versions", "must be newest-first; SideStore treats the first compatible version as latest")

    return app["bundleIdentifier"]


def validate_news(item, index: int, bundle_ids: set[str]) -> None:
    path = f"news[{index}]"
    item = require_object(item, path)
    check_keys(item, path, NEWS_REQUIRED, NEWS_ALLOWED)
    for key in NEWS_REQUIRED:
        require_string(item[key], f"{path}.{key}")
    parse_date(item["date"], f"{path}.date")
    for key in ("imageURL", "url"):
        if key in item:
            check_https_url(item[key], f"{path}.{key}")
    if "appID" in item:
        app_id = require_string(item["appID"], f"{path}.appID")
        if app_id not in bundle_ids:
            fail(f"{path}.appID", "does not match any app bundleIdentifier")
    if "notify" in item and not isinstance(item["notify"], bool):
        fail(f"{path}.notify", "must be boolean")


def validate_source(data) -> None:
    data = require_object(data, "$")
    check_keys(data, "$", SOURCE_REQUIRED, SOURCE_ALLOWED)
    require_string(data["name"], "$.name")
    require_string(data["identifier"], "$.identifier")
    if "sourceURL" in data:
        check_https_url(data["sourceURL"], "$.sourceURL")

    apps = data["apps"]
    if not isinstance(apps, list) or not apps:
        fail("$.apps", "must be a non-empty array")

    ids: set[str] = set()
    names: set[str] = set()
    for i, app in enumerate(apps):
        bundle_id = validate_app(app, i)
        if bundle_id in ids:
            fail(f"apps[{i}].bundleIdentifier", f"duplicate bundle identifier {bundle_id!r}")
        ids.add(bundle_id)

        name = app["name"].casefold()
        if name in names:
            fail(f"apps[{i}].name", f"duplicate app name {app['name']!r}")
        names.add(name)

    news = data.get("news", [])
    if not isinstance(news, list):
        fail("$.news", "must be an array")
    news_ids: set[str] = set()
    for i, item in enumerate(news):
        validate_news(item, i, ids)
        identifier = item["identifier"]
        if identifier in news_ids:
            fail(f"news[{i}].identifier", f"duplicate news identifier {identifier!r}")
        news_ids.add(identifier)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?", default="source.json")
    args = parser.parse_args()

    path = Path(args.source)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        validate_source(data)
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print(f"OK: {path} is a valid strict SideStore source ({len(data['apps'])} apps)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
