# SniffleShop

SniffleShop is a SideStore-compatible source for sideloadable iOS software. It tracks a curated set of useful open-source apps, emulators, developer utilities, JIT tools, and Linux/terminal software using official upstream downloads.

## Add SniffleShop to SideStore

Use this source URL:

```text
https://raw.githubusercontent.com/SerialfireLewis/SniffleShop/main/source.json
```

In SideStore:

1. Open **Sources**.
2. Tap **+** / **Add Source**.
3. Paste the URL above.
4. Add the source, then browse **SniffleShop**.

The repository must be **public** for `raw.githubusercontent.com` to serve `source.json` without authentication.

## Catalog

Current tracked apps:

- **LiveContainer** — runs guest iOS apps in a container; the listed standalone build is the SideStore-compatible IPA.
- **Feather** — on-device signing and IPA/source management.
- **StikDebug** — on-device debugger and JIT enabler for iOS 17.4+.
- **UTM** — QEMU-based virtual machines for Linux, Windows, and other operating systems; JIT build.
- **iSH** — local Alpine/Linux shell using x86 userspace emulation.
- **Angel Aura Amethyst** — actively maintained Minecraft: Java Edition launcher for iOS; requires JIT.
- **Provenance** — multi-system retro emulator.
- **Flycast** — Dreamcast, Naomi, Naomi 2, and Atomiswave emulator.

Downloads are intentionally limited to official developer release assets or official project-hosted IPA URLs. SniffleShop does not mirror IPAs.

## Compatibility notes

Some apps need capabilities beyond ordinary sideloading:

- JIT-dependent apps may require a JIT enabler, pairing file, loopback VPN, or another setup appropriate to your iOS version.
- LiveContainer 3.8.0's standalone IPA requires SideStore 0.6.2+ (or a compatible AltStore release).
- StikDebug requires iOS 17.4 or newer.
- Amethyst requires JIT for normal operation.
- UTM's non-SE build requires JIT for fast emulation.

SniffleShop uses the strict SideStore source schema. That schema supports the high-level `permissions` array but does **not** allow AltStore's newer `appPermissions`/entitlement object, so unsupported entitlement fields are deliberately not inserted into `source.json`.

## Repository layout

```text
source.json                  SideStore source consumed by clients
README.md                    Installation and catalog documentation
UPSTREAMS.md                 Release provenance and maintenance notes
scripts/validate_source.py   Strict schema/metadata validator
scripts/check_links.py       External icon/screenshot/IPA reachability checker
.github/workflows/validate.yml
                             CI validation + scheduled link checks
```

## Validate locally

No third-party Python packages are required.

```bash
python3 scripts/validate_source.py source.json
python3 scripts/check_links.py source.json
```

`validate_source.py` enforces the current strict SideStore source shape: supported keys only, required fields, unique bundle identifiers, valid dates/URLs, positive byte sizes, supported permission values, and newest-first version ordering.

`check_links.py` performs lightweight HTTP checks against every external icon, screenshot, and IPA URL without downloading full IPA files.

## Updating an app

1. Check the app's official upstream release/source listed in [UPSTREAMS.md](UPSTREAMS.md).
2. Confirm the exact IPA asset, bundle identifier, release date, and byte size.
3. Add the release at the **front** of that app's `versions` array.
4. Keep only fields accepted by SideStore's source schema.
5. Run both validation scripts.
6. Commit the update.

SideStore treats the first compatible entry in `versions` as the latest version, so version arrays must stay newest-first.

## Source policy

SniffleShop favors:

- official developer GitHub releases,
- official developer-hosted source feeds and IPA downloads,
- open-source projects,
- current non-jailbroken/sideloadable builds.

It avoids random IPA mirrors, piracy repositories, jailbreak-only/TrollStore-only packages presented as SideStore builds, placeholder metadata, and releases known to be incompatible with current iOS without a clear compatibility bound.
