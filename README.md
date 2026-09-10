# SniffleShop

SniffleShop is a SideStore-compatible AltSource for sideloadable iOS software. It tracks a curated set of useful open-source apps, emulators, developer utilities, JIT tools, Linux/terminal software, and other sideloading-friendly projects using official upstream downloads.

## Add SniffleShop to SideStore

Paste this source URL into SideStore:

```text
https://raw.githubusercontent.com/SerialfireLewis/SniffleShop/main/source.json
```

In SideStore, open **Sources**, tap **+ / Add Source**, paste the URL, and add **SniffleShop**.

You can also use SideStore's source URL scheme once the repository is public:

```text
sidestore://source?url=https%3A%2F%2Fraw.githubusercontent.com%2FSerialfireLewis%2FSniffleShop%2Fmain%2Fsource.json
```

> **Important:** the repository must be public for `raw.githubusercontent.com` to serve `source.json` to SideStore without GitHub authentication.

## Catalog

Current tracked apps:

- **LiveContainer** — run guest iOS apps inside a container; the listed standalone IPA is intended for SideStore.
- **Feather** — on-device signing and IPA/source management.
- **StikDebug** — on-device debugger and JIT enabler for iOS 17.4+.
- **UTM** — QEMU-based virtual machines for Linux, Windows, and other operating systems; JIT build.
- **iSH** — local Alpine/Linux shell using x86 userspace emulation.
- **Yattee** — open-source privacy-focused video client with Invidious/Piped/self-hosted support.
- **iTorrent** — open-source native torrent client with Files integration and background transfers.
- **Angel Aura Amethyst** — actively maintained Minecraft: Java Edition launcher for iOS; requires JIT.
- **Provenance** — multi-system retro emulator.
- **Flycast** — Dreamcast, Naomi, Naomi 2, and Atomiswave emulator.

Downloads are intentionally limited to official developer GitHub release assets or official project-hosted IPA URLs. SniffleShop does not mirror IPAs.

## Source format

SideStore is compatible with AltStore Sources. SniffleShop uses current AltSource metadata where useful while retaining SideStore-compatible fields used by existing SideStore sources. It includes source metadata, app categories, bundle IDs, versions, dates, sizes, OS bounds, and reliable screenshots. `appPermissions` is included only where trustworthy current upstream metadata is available; those values are never guessed.

## Compatibility notes

- **LiveContainer 3.8.0** standalone requires SideStore 0.6.2+ or a compatible AltStore release.
- **StikDebug** requires iOS 17.4 or newer.
- **Amethyst** requires JIT for normal operation.
- **UTM** is the non-SE JIT build and needs JIT for fast emulation.
- **Yattee 2.0 build 270** requires iOS 18 or newer.
- **iTorrent 2.2.0** requires iOS 16 or newer.

## Repository layout

```text
source.json                  Source consumed by SideStore/AltStore
README.md                    Installation and catalog documentation
UPSTREAMS.md                 Release provenance and maintenance notes
scripts/validate_source.py   Current AltSource/SideStore metadata validator
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

The validator checks required metadata, categories, URL/date syntax, version ordering, bundle-ID uniqueness, byte sizes, screenshots, `appPermissions`, SideStore permission values, and featured-app references. The link checker performs lightweight HTTP checks without intentionally downloading full IPA files.

## Updating an app

1. Check the official upstream in [UPSTREAMS.md](UPSTREAMS.md).
2. Confirm the exact IPA asset, case-sensitive bundle identifier, release date, byte size, and OS requirement.
3. Add the release at the front of the app's `versions` array.
4. Copy security-sensitive `appPermissions` only from trustworthy current upstream metadata or verified IPA metadata.
5. Run both validation scripts and commit.

## Source policy

SniffleShop favors official developer GitHub releases, official developer-hosted source feeds, open-source projects, and current sideloadable/non-jailbroken builds. It avoids random IPA mirrors, piracy repositories, placeholder metadata, jailbreak-only/TrollStore-only packages presented as ordinary SideStore builds, and releases known to be incompatible without a clear compatibility bound.
