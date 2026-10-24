# SniffleShop

SniffleShop is a SideStore-compatible AltSource for sideloadable iOS software. It tracks a curated set of useful open-source apps, emulators, developer utilities, JIT tools, Linux/terminal software, and other sideloading-friendly projects using official upstream downloads.

## Add SniffleShop to SideStore

Paste this source URL into SideStore:

```text
https://raw.githubusercontent.com/SerialfireLewis/SniffleShop/main/source.json
```

In SideStore, open **Sources**, tap **+ / Add Source**, paste the URL, and add **SniffleShop**.

You can also use SideStore's source URL scheme:

```text
sidestore://source?url=https%3A%2F%2Fraw.githubusercontent.com%2FSerialfireLewis%2FSniffleShop%2Fmain%2Fsource.json
```

## Catalog

Current tracked apps (79 entries):

- **LiveContainer** — run guest iOS apps inside a container; the listed standalone IPA is intended for SideStore.
- **Feather** — on-device signing and IPA/source management.
- **StikDebug** — on-device debugger and JIT enabler for iOS 17.4+.
- **UTM** — QEMU-based virtual machines for Linux, Windows, and other operating systems; JIT build.
- **iSH** — local Alpine/Linux shell using x86 userspace emulation.
- **Yattee** — open-source privacy-focused video client with Invidious/Piped/self-hosted support.
- **iTorrent** — open-source native torrent client with Files integration and background transfers.
- **Angel Aura Amethyst** — actively maintained Minecraft: Java Edition launcher for iOS; requires JIT.
- **Provenance** — multi-system retro emulator.
- **RetroArch** — multi-system emulation frontend using Libretro cores; official stable sideload IPA.
- **osu!** — official open-source osu! lazer iOS build for rhythm-game play.
- **Aidoku** — open-source manga reader with external sources, downloads, OCR support, and reader customization.
- **NOOP** — open-source offline companion for supported WHOOP straps.
- **Nyora** — native open-source manga and comics reader.
- **Stremio** — extensible media center using the official iOS sideload IPA.
- **Sable** — native open-source Matrix client.
- **PPSSPP** — fast, configurable PlayStation Portable emulator with save states, speed controls, and controller support.
- **Delta** — Nintendo-focused multi-system emulator with save states, cheats, skins, fast-forward, and controller support.
- **MAME4iOS** — arcade emulator with deterministic input recording/playback and single-step support for TAS-style work.
- **Pocket8** — native PICO-8 emulator for iPhone and iPad; runs `.p8`/`.p8.png` cartridges including Celeste Classic and Celeste Classic 2.
- **SideStore** — AltStore fork - no AltServer required. See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **UTM SE** — UTM Slow Edition — no JIT required, App Store compliant. See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **Spotube** — Open-source Spotify client — no premium needed (SwiftUI/Flutter). See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **BHTwitter** — Tweaked Twitter/X — ad block, download, premium unlock (tweaked). See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **LBox** — SwiftUI repo manager for LiveContainer (NEW 2025). See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **Apollo (Patched)** — Reddit's Apollo — revived with custom API key (tweaked). See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **Cowabunga** — iOS 14-16.1.2 MacDirtyCow toolbox — themes, tweaks, no jailbreak. See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **Misaka** — iOS & tvOS customisation for KFD & MDC — successor to Cowabunga. See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **Paperback** — Manga reader — extensions, tracking & downloads. See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **DebToIPA** — Convert .deb tweaks to .ipa on-device (SwiftUI). See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **ModMyIPA** — Duplicate any IPA — install multiple copies side-by-side. See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **Azula** — Inject dylibs into IPAs on-device (SwiftUI + ElleKit). See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **AppDB** — Full client for appdb.to — sideloaded apps database. See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.
- **Mirarr** — FOSS movie & TV app — watch movies and TV shows. See [UPSTREAMS.md](UPSTREAMS.md) for source and compatibility notes.

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
- **RetroArch** can use JIT/dynamic recompilation for supported cores when JIT is available.
- **PPSSPP 1.20.4** requires iOS 13.0 or newer.
- **MAME4iOS 2022.5** uses the MAME 0.250 core and requires iOS 13.4 or newer.
- **Delta 1.6** is the latest official sideload IPA published in Delta's GitHub releases.

### Expanded catalog: additional apps

These 45 additions were imported from maintained developer releases and compatible AltStore/SideStore feeds. Direct download URLs remain upstream-hosted; this repository does not rehost IPA binaries.

- **AirCard-iOS 1.3.2** — Apple Wallet card skins, passcode themes and wallpapers (minimum iOS 27.0).
- **AniBaka 5.2.3** — 跨平台番剧聚合、媒体播放与弹幕客户端 (minimum iOS 13.0).
- **AnimeFlow 2.6.4** — 跨平台动漫视频播放器，支持多数据源、实时 4K 超分辨率与弹幕 (minimum iOS 13.0).
- **Animeko 6.4.0** — 一站式弹幕追番平台 (minimum iOS 14.0).
- **ARMSX2 2.6.0-nightly.20261023.1332** — PlayStation 2 emulator for ARM64 (minimum iOS 17.0).
- **BCD 0.1.600** — Windows games on iPhone and iPad (minimum iOS 18.0).
- **Doer 1.8.6** — A native iOS client for Linux.do (minimum iOS 15.0).
- **DolphiniOS 5.0.0b6** — GameCube and Wii emulator for iOS/iPadOS (minimum iOS 14.0).
- **DukeX 1.0.2** — Original Xbox emulation for iOS (minimum iOS 16.0).
- **EhPanda 2.8.1** — An unofficial E-Hentai App for iOS built with SwiftUI & TCA (minimum iOS 26.0).
- **Fathom 1.0.0** — x86-64 PC emulator for iOS (minimum iOS 18.0).
- **Husk 3.0** — Android app launcher for iOS (minimum iOS 16.4).
- **Iridium 0.2.0** — Experimental Windows-game runtime for iPhone and iPad (minimum iOS 18.0).
- **Kazumi 2.4.2** — 基于自定义规则的番剧采集APP，支持流媒体在线观看，支持弹幕，支持实时超分辨率。 (minimum iOS 13.0).
- **KMusic 2.3.0** — 基于 SwiftUI 的多源音乐聚合播放器 (minimum iOS 14.0).
- **Kumone 0.3.21** — 原生 NetEase Cloud Music iOS 客户端（雲の音） (minimum iOS 16.0).
- **Madeira 0.1.3** — Windows PC games on your iPhone (minimum iOS 17.0).
- **Mangayomi 0.9.9** — Read manga, novels, and watch anime.
- **ManicEMU 2.0.1** — All-in-one retro game emulator for iOS (minimum iOS 15.0).
- **MiniWatts 1.5.1** — Battery, charging and thermal instrument (minimum iOS 17.0).
- **MoviePilotLite 1.2.6** — MoviePilot 移动端，基于 Flutter 实现 (minimum iOS 15.0).
- **Musly 2.0.3** — Free Navidrome client & Subsonic music player (minimum iOS 15.0).
- **NeoStation iOS 0.0.8** — Emulation frontend for iPhone and iPad (minimum iOS 18.0).
- **Novella 2.6.0** — 轻书架第三方客户端 (minimum iOS 16.4).
- **Opaline 1.12.0** — YouTube client for iOS 12+ (minimum iOS 12.0).
- **Orchard 0.2** — Apple Silicon macOS Ventura running inside an iPhone app (minimum iOS 16.0).
- **PiliPlus 2.1.6** — 使用Flutter开发的BiliBili第三方客户端 (minimum iOS 14.0).
- **Pixiv-SwiftUI 0.16.3** — 基于 SwiftUI 的 Pixiv 第三方客户端 (minimum iOS 17.0).
- **Playport 0.4.0** — PC games on your iPhone. Natively, no streaming. (minimum iOS 26.0).
- **PSX3IOS 0.2.7-beta** — PlayStation 3 emulator for iPhone and iPad (minimum iOS 15.0).
- **Roam Control 0.9.9** — Choose, test and move your iPhone's reported location (minimum iOS 27.0).
- **SceneBox 1.0.4** — Torrent streaming client (minimum iOS 18.0).
- **SpotiFLAC 5.2.6** — FLAC Downloader for iOS (minimum iOS 16.0).
- **TiebaPure 1.4.15** — 基于 SwiftUI 的第三方百度贴吧客户端 (minimum iOS 16.4).
- **Tsumiru 1.5.1** — Native manga & manhwa reader for Suwayomi-Server (minimum iOS 14.0).
- **VeneraNext 1.18.0** — 跨平台漫画阅读器 (minimum iOS 14.0).
- **ZhihuMinusMinus 0.9.5** — 轻量、纯净的第三方知乎客户端 (minimum iOS 15.1).
- **Empo 0.8.1** — Run RPG Maker and PSDK games on iPhone and iPad. (minimum iOS 26.0).
- **Artemis 3.0** — Alternative client for HIDIVE (minimum iOS 17.0).
- **PojavLauncher 2.2** — Minecraft: Java Edition on iOS (Swift/ObjC + Java) (minimum iOS 14.0).
- **Flycast v2.5** — Dreamcast, Naomi and Atomiswave emulator..
- **AnymeX 3.1.8** — Multiservice tracking client.
- **Winston for Reddit 1.1.5** — Winston, a beautiful and native Reddit client for iOS.
- **VortX 0.5.5** — Stream movies and shows on iPhone and iPad. (minimum iOS 16.0).
- **VortX (Apple TV) 0.5.5** — Stream movies and shows on Apple TV. (minimum iOS 18.0).

Some newer entries require iOS 26 or 27, and some emulators or game runtimes need JIT, user-supplied game files, or compatible source content. Check each entry's version metadata before installing. Modified clients are identified as such in their descriptions; an upstream release link does not imply endorsement by the original service.

## Repository layout

```text
source.json                  Source consumed by SideStore/AltStore
README.md                    Installation and catalog documentation
UPSTREAMS.md                 Release provenance and maintenance notes
scripts/validate_source.py   Current AltSource/SideStore metadata validator
scripts/check_links.py       External icon/screenshot/IPA reachability checker
.github/workflows/validate.yml
                             CI validation + link checks on updates and weekly
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

## Compatibility and modified apps

Some entries are legacy utilities or only work on specific iOS releases. **BHTwitter and Apollo (Patched) are modified third-party builds, not official releases from the original app developers.** Cowabunga and Misaka are OS-version-dependent customization tools. Read each entry's upstream release notes before installing; the catalog does not imply every app works on every iOS version.
