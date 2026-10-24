# Upstream release sources

Last reviewed: **2026-10-24**

SniffleShop points to upstream IPA files directly; it does not rehost them. The original 34 entries remain documented below. The latest expansion adds 45 entries from AltGallery's maintained GitHub-release catalog, direct developer-maintained feeds, and official emulator releases. The upstream release links below identify the projects; source metadata has been structurally checked, but not every download URL has been live-checked yet.

| App | Tracked release | Official upstream | Notes |
| --- | --- | --- | --- |
| LiveContainer | 3.8.0 | https://github.com/LiveContainer/LiveContainer/releases | Uses the standalone `LiveContainer.ipa`, not `LiveContainer+SideStore.ipa`. |
| Feather | 2.9.0 | https://github.com/claration/Feather/releases | IPA byte size comes from the GitHub release asset; the project's source file currently carries an older size value. |
| StikDebug | 3.1.10 | https://github.com/StikDebug/StikDebug/releases | Current official debugger/JIT release; iOS 17.4+. |
| UTM | 4.7.5 | https://alt.getutm.app | Official UTM source; `UTM.ipa` is the non-jailbroken JIT sideloading build. |
| iSH | 1.3.2 | https://github.com/ish-app/ish/releases | Tracks the latest stable release rather than rolling automated prereleases. |
| Yattee | 2.0.0 build 270 | https://github.com/yattee/yattee/blob/main/altstore-source.json | Current official iOS beta from the developer-maintained AltSource. |
| iTorrent | 2.2.0 build 1 | https://github.com/XITRIX/iTorrent/releases | Official GitHub IPA; project documentation explicitly supports SideStore/AltStore sideloading. |
| Angel Aura Amethyst | 1.0.9212a18 | https://alt.crystall1ne.dev | Current official AngelAuraMC build/source; active successor to PojavLauncher. |
| Provenance | 3.3.0 | https://provenance-emu.com/apps.json | Tracks the current stable release from the official source. |
| RetroArch | 1.22.2 | https://buildbot.libretro.com/stable/1.22.2/apple/ios-arm64/ | Official Libretro stable iOS sideload IPA; current upstream release is 1.22.2. |
| Pocket8 | 1.6.2 | https://github.com/jevonlipsey/pico-ios/releases | Official iOS IPA; supports PICO-8 cartridges including Celeste Classic. |

## Deliberate exclusions

**PojavLauncher** is not included. Its current upstream source marks it discontinued, says it does not work on the latest iOS, and directs users to Amethyst instead.

**Jitterbug/Jitterbug Lite** is not included. The upstream repository is archived and its latest release is from 2022; StikDebug is the actively maintained JIT tool tracked here.

**DolphiniOS** was not added even though an official current prerelease IPA exists, because its non-jailbroken project configuration uses a replace-at-build organization identifier rather than one fixed bundle identifier. SniffleShop will not guess a bundle ID.

**Flycast** is not currently included. Its official iOS AltSource still advertises v2.5, but that AltSource's IPA URL now returns 404 and the upstream GitHub v2.5 release no longer contains an iOS IPA asset.

## Metadata rules

- `bundleIdentifier` must match the actual app identifier and is case-sensitive.
- `versions[0]` is the newest compatible version presented by the source.
- `size` is the IPA size in bytes, preferably from GitHub release asset metadata or the developer's official source.
- Stable releases are preferred when the project has a stable channel; active beta channels are used when that is the project's supported distribution.
- `appPermissions` is included only when trustworthy current entitlement/privacy metadata is available; it is never guessed.
- Icons and screenshots are included only from reliable upstream project locations.

| SideStore | 0.6.3 | https://github.com/SideStore/SideStore/releases | Official sideloading and refresh utility. |
| UTM SE | 4.7.5 | https://github.com/utmapp/UTM/releases | No-JIT UTM variant; slower than the JIT build. |
| Spotube | 5.1.2 | https://github.com/KRTirtho/spotube/releases | Open-source music client; third-party service compatibility may change. |
| BHTwitter | 4.4 | https://github.com/BandarHL/BHTwitter/releases | Modified X/Twitter client; not an official X release. |
| LBox | 1.2 | https://github.com/Lolendor/LBox/releases | LiveContainer companion utility. |
| Apollo (Patched) | 1.15.11-0.1.0 | https://github.com/ichitaso/ApolloPatcher/releases | Modified legacy Reddit client; API setup may be required. |
| Cowabunga | 10.3.2 | https://github.com/leminlimez/Cowabunga/releases | OS-version-dependent customization tool; features may be unavailable on newer iOS. |
| Misaka | 8.2.4 | https://github.com/straight-tamago/misaka/releases | OS-version-dependent customization tool; not a universal jailbreak. |
| Paperback | 0.8.11-r2 | https://github.com/Paperback-iOS/app/releases | Manga reader; extension/source availability is managed separately. |
| DebToIPA | 1.1.1 | https://github.com/sourcelocation/DebToIPA/releases | Converts compatible Debian packages to IPA format; compatibility varies. |
| ModMyIPA | 1.0.2 | https://github.com/powenn/ModMyIPA/releases | Utility for creating duplicate app bundles; older release. |
| Azula | 1.0.1 | https://github.com/Paisseon/Azula/releases | On-device dylib injection tool; compatibility and signing constraints apply. |
| AppDB | 1.1.6 | https://github.com/n3d1117/appdb/releases | Third-party appdb client; upstream release is old. |
| Mirarr | 3.3.2 | https://github.com/mirarr-app/mirarr/releases | Open-source media catalog client; use only with services you are authorized to access. |

## Expanded catalog additions

| AirCard-iOS | 1.3.2 | https://github.com/Mak5er/AirCard-iOS/releases | Minimum iOS 27.0. |
| AniBaka | 5.2.3 | https://github.com/AniBakaBaka/AniBaka/releases | Minimum iOS 13.0. |
| AnimeFlow | 2.6.4 | https://github.com/openAnimeFlow/AnimeFlow/releases | Minimum iOS 13.0. |
| Animeko | 6.4.0 | https://github.com/open-ani/animeko/releases | Minimum iOS 14.0. |
| ARMSX2 | 2.6.0-nightly.20261023.1332 | https://github.com/ARMSX2/ARMSX2/releases | Minimum iOS 17.0. Emulator/game runtime; performance and JIT needs vary by device. |
| BCD | 0.1.600 | https://github.com/thebcd69/bcd-games/releases | Minimum iOS 18.0. |
| Doer | 1.8.6 | https://github.com/moliango/doer/releases | Minimum iOS 15.0. |
| DolphiniOS | 5.0.0b6 | https://github.com/OatmealDome/dolphin-ios/releases | Minimum iOS 14.0. Emulator/game runtime; performance and JIT needs vary by device. |
| DukeX | 1.0.2 | https://github.com/MaftyManicEMU/DukeX/releases | Minimum iOS 16.0. |
| EhPanda | 2.8.1 | https://github.com/EhPanda-Team/EhPanda/releases | Minimum iOS 26.0. |
| Fathom | 1.0.0 | https://github.com/Leviidev/Fathom/releases | Minimum iOS 18.0. |
| Husk | 3.0 | https://github.com/Leviidev/Husk/releases | Minimum iOS 16.4. |
| Iridium | 0.2.0 | https://github.com/intraducine/iridium/releases | Minimum iOS 18.0. |
| Kazumi | 2.4.2 | https://github.com/Predidit/Kazumi/releases | Minimum iOS 13.0. |
| KMusic | 2.3.0 | https://github.com/Mac-XK/KMusic/releases | Minimum iOS 14.0. |
| Kumone | 0.3.21 | https://github.com/missuo/kumone/releases | Minimum iOS 16.0. |
| Madeira | 0.1.3 | https://github.com/willfaust/Madeira/releases | Minimum iOS 17.0. |
| Mangayomi | 0.9.9 | https://github.com/kodjodevf/mangayomi/releases | Upstream-hosted IPA; check release notes for compatibility. |
| ManicEMU | 2.0.1 | https://github.com/Manic-EMU/ManicEMU/releases | Minimum iOS 15.0. Emulator/game runtime; performance and JIT needs vary by device. |
| MiniWatts | 1.5.1 | https://github.com/ResistanceTo/MiniWatts/releases | Minimum iOS 17.0. |
| MoviePilotLite | 1.2.6 | https://github.com/singleton-altman/MoviePilotLite/releases | Minimum iOS 15.0. |
| Musly | 2.0.3 | https://github.com/dddevid/Musly/releases | Minimum iOS 15.0. |
| NeoStation iOS | 0.0.8 | https://github.com/TarbleFR/RewindBox/releases | Minimum iOS 18.0. |
| Novella | 2.6.0 | https://github.com/celia-sh/Novella/releases | Minimum iOS 16.4. |
| Opaline | 1.12.0 | https://github.com/verback2308/Opaline/releases | Minimum iOS 12.0. Modified client; not an original publisher build. |
| Orchard | 0.2 | https://github.com/MakrSas/orchard-ios/releases | Minimum iOS 16.0. |
| PiliPlus | 2.1.6 | https://github.com/bggRGjQaUbCoE/PiliPlus/releases | Minimum iOS 14.0. |
| Pixiv-SwiftUI | 0.16.3 | https://github.com/Eslzzyl/Pixiv-SwiftUI/releases | Minimum iOS 17.0. |
| Playport | 0.4.0 | https://github.com/playportdev/playport/releases | Minimum iOS 26.0. Emulator/game runtime; performance and JIT needs vary by device. |
| PSX3IOS | 0.2.7-beta | https://github.com/xmiguel911x/PSX3IOS/releases | Minimum iOS 15.0. |
| Roam Control | 0.9.9 | https://github.com/seanhowarthdev/Roam-Control/releases | Minimum iOS 27.0. |
| SceneBox | 1.0.4 | https://github.com/donbytyqi/scenebox/releases | Minimum iOS 18.0. Use with services/content you are authorized to access. |
| SpotiFLAC | 5.2.6 | https://github.com/mornyeapp/Mornye/releases | Minimum iOS 16.0. |
| TiebaPure | 1.4.15 | https://github.com/infinityf4p/TiebaPure-iOS/releases | Minimum iOS 16.4. |
| Tsumiru | 1.5.1 | https://github.com/Suwayomi/Suwayomi-Tsumiru/releases | Minimum iOS 14.0. |
| VeneraNext | 1.18.0 | https://github.com/CyrilPeng/Venera-Next/releases | Minimum iOS 14.0. |
| ZhihuMinusMinus | 0.9.5 | https://github.com/huamurui/zhihu-minus-minus/releases | Minimum iOS 15.1. |
| Empo | 0.8.1 | https://github.com/mateo-m/empo-app/releases | Minimum iOS 26.0. |
| Artemis | 3.0 | https://github.com/Auties00/Artemis/releases | Minimum iOS 17.0. |
| PojavLauncher | 2.2 | https://github.com/PojavLauncherTeam/PojavLauncher_iOS/releases | Minimum iOS 14.0. Emulator/game runtime; performance and JIT needs vary by device. |
| Flycast | v2.5 | https://github.com/flyinghead/flycast/releases | Emulator/game runtime; performance and JIT needs vary by device. |
| AnymeX | 3.1.8 | https://github.com/RyanYuuki/AnymeX/releases | Upstream-hosted IPA; check release notes for compatibility. |
| Winston for Reddit | 1.1.5 | https://github.com/lo-cafe/winston/releases | Upstream-hosted IPA; check release notes for compatibility. |
| VortX | 0.5.5 | https://github.com/VortXTV/VortX/releases | Minimum iOS 16.0. Emulator/game runtime; performance and JIT needs vary by device. Use with services/content you are authorized to access. |
| VortX (Apple TV) | 0.5.5 | https://github.com/VortXTV/VortX/releases | Minimum iOS 18.0. |
