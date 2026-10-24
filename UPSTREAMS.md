# Upstream release sources

Last reviewed: **2026-10-24**

SniffleShop points to upstream IPA files directly; it does not rehost them. The catalog now tracks 80 distinct apps and 102 downloadable IPA builds, including real rollback versions from the upstream NOOP and VortX feeds. The table below identifies upstream release pages and compatibility caveats. Latest CI passed both schema validation and a live link/byte-size audit: **214 URLs checked, 102 IPA sizes checked, zero failures**.

| App | Tracked release | Official upstream | Notes |
| --- | --- | --- | --- |
| LiveContainer | 3.8.0 | https://github.com/LiveContainer/LiveContainer/releases | Minimum iOS 15.0. Uses the standalone `LiveContainer.ipa`, not `LiveContainer+SideStore.ipa`. |
| Feather | 2.9.0 | https://github.com/claration/Feather/releases | IPA byte size comes from the GitHub release asset; the project's source file currently carries an older size value. |
| StikDebug | 3.1.15 | https://github.com/StikDebug/StikDebug/releases | Minimum iOS 17.4. Current official debugger/JIT release; iOS 17.4+. |
| UTM | 4.7.5 | https://alt.getutm.app | Minimum iOS 14.0. Official UTM source; `UTM.ipa` is the non-jailbroken JIT sideloading build. |
| iSH | 1.3.2 | https://github.com/ish-app/ish/releases | Minimum iOS 11.0. Tracks the latest stable release rather than rolling automated prereleases. |
| Yattee | 2.0.0 | https://github.com/yattee/yattee/blob/main/altstore-source.json | Minimum iOS 18.0. Current official iOS beta from the developer-maintained AltSource. |
| iTorrent | 2.2.0 | https://github.com/XITRIX/iTorrent/releases | Minimum iOS 16.0. Official GitHub IPA; project documentation explicitly supports SideStore/AltStore sideloading. |
| Angel Aura Amethyst | 1.0.9212a18 | https://alt.crystall1ne.dev | Minimum iOS 14.0. Current official AngelAuraMC build/source; active successor to PojavLauncher. |
| Provenance | 3.3.0 | https://provenance-emu.com/apps.json | Tracks the current stable release from the official source. |
| RetroArch | 1.22.2 | https://buildbot.libretro.com/stable/1.22.2/apple/ios-arm64/ | Minimum iOS 12.0. Official Libretro stable iOS sideload IPA; current upstream release is 1.22.2. |
| osu! | 1.0 | https://github.com/ppy/osu/releases | Minimum iOS 13.4. Upstream-hosted IPA; review release notes and compatibility before installing. |
| Aidoku | 0.9 | https://github.com/Aidoku/Aidoku/releases | Minimum iOS 15.0. Upstream-hosted IPA; review release notes and compatibility before installing. |
| NOOP | 12.0.0 | https://github.com/ryanbr/noop/releases | Minimum iOS 17.0. Official current build; 19 upstream versions retained for rollback (12.0.0 through 8.7.0). |
| Nyora | 2.7.3 | https://github.com/Nyora-Manga/nyora-ios/releases | Minimum iOS 18.0. Upstream-hosted IPA; review release notes and compatibility before installing. |
| Stremio | 2.0.7 | https://dl.strem.io/apple/2.0.7b22/ios/stremio_iOS.ipa | Minimum iOS 13.0. Upstream-hosted IPA; review release notes and compatibility before installing. |
| Sable | 1.21.0 | https://github.com/SableClient/Sable/releases | Minimum iOS 16.0. Upstream-hosted IPA; review release notes and compatibility before installing. |
| PPSSPP | 1.20.4 | https://github.com/hrydgard/ppsspp/releases | Minimum iOS 13.0. Upstream-hosted IPA; review release notes and compatibility before installing. |
| Delta | 1.6 | https://github.com/rileytestut/Delta/releases | Upstream-hosted IPA; review release notes and compatibility before installing. |
| MAME4iOS | 2022.5 | https://github.com/yoshisuga/MAME4iOS/releases | Minimum iOS 13.4. Upstream-hosted IPA; review release notes and compatibility before installing. |
| Pocket8 | 1.6.2 | https://github.com/jevonlipsey/pico-ios/releases | Minimum iOS 15.0. Official iOS IPA; supports PICO-8 cartridges including Celeste Classic. |
| SideStore | 0.6.3 | https://github.com/SideStore/SideStore/releases | Minimum iOS 14.0. Official sideloading and refresh utility. |
| UTM SE | 4.7.5 | https://github.com/utmapp/UTM/releases | Minimum iOS 14.0. No-JIT UTM variant; slower than the JIT build. |
| Spotube | 5.1.2 | https://github.com/KRTirtho/spotube/releases | Minimum iOS 14.0. Open-source music client; third-party service compatibility may change. |
| BHTwitter | 4.4 | https://github.com/BandarHL/BHTwitter/releases | Minimum iOS 14.0. Modified X/Twitter client; not an official X release. |
| LBox | 1.2 | https://github.com/Lolendor/LBox/releases | Minimum iOS 15.0. LiveContainer companion utility. |
| Apollo (Patched) | 1.15.11-0.1.0 | https://github.com/ichitaso/ApolloPatcher/releases | Minimum iOS 14.0. Modified legacy Reddit client; API setup may be required. |
| Cowabunga | 10.3.2 | https://github.com/leminlimez/Cowabunga/releases | Minimum iOS 14.0. OS-version-dependent customization tool; features may be unavailable on newer iOS. |
| Misaka | 8.2.4 | https://github.com/straight-tamago/misaka/releases | Minimum iOS 15.0. OS-version-dependent customization tool; not a universal jailbreak. |
| Paperback | 0.8.11-r2 | https://github.com/Paperback-iOS/app/releases | Minimum iOS 15.0. Manga reader; extension/source availability is managed separately. |
| DebToIPA | 1.1.1 | https://github.com/sourcelocation/DebToIPA/releases | Minimum iOS 13.0. Converts compatible Debian packages to IPA format; compatibility varies. |
| ModMyIPA | 1.0.2 | https://github.com/powenn/ModMyIPA/releases | Minimum iOS 13.0. Utility for creating duplicate app bundles; older release. |
| Azula | 1.0.1 | https://github.com/Paisseon/Azula/releases | Minimum iOS 14.0. On-device dylib injection tool; compatibility and signing constraints apply. |
| AppDB | 1.1.6 | https://github.com/n3d1117/appdb/releases | Minimum iOS 12.0. Third-party appdb client; upstream release is old. |
| Mirarr | 3.3.2 | https://github.com/mirarr-app/mirarr/releases | Minimum iOS 13.0. Open-source media catalog client; use only with services you are authorized to access. |
| AirCard-iOS | 1.3.2 | https://github.com/Mak5er/AirCard-iOS/releases | Minimum iOS 27.0. |
| AniBaka | 5.2.3 | https://github.com/AniBakaBaka/AniBaka/releases | Minimum iOS 13.0. |
| AnimeFlow | 2.6.4 | https://github.com/openAnimeFlow/AnimeFlow/releases | Minimum iOS 13.0. |
| Animeko | 6.4.0 | https://github.com/open-ani/animeko/releases | Minimum iOS 14.0. |
| ARMSX2 | 2.6.0-nightly.20261023.1332 | https://github.com/ARMSX2/ARMSX2/releases | Minimum iOS 17.0. Emulator/game runtime; performance and JIT needs vary by device. |
| BCD | 0.1.600 | https://github.com/thebcd69/bcd-games/releases | Minimum iOS 18.0. |
| Doer | 1.8.6 | https://github.com/moliango/doer/releases | Minimum iOS 15.0. |
| DolphiniOS | 5.0.0b6 | https://github.com/OatmealDome/dolphin-ios/releases | Minimum iOS 14.0. Non-jailbroken prerelease; bundle identifier follows the maintained AltGallery feed and has not been independently extracted from the IPA. |
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
| AnymeX | 3.1.8 | https://github.com/RyanYuuki/AnymeX/releases | Upstream-hosted IPA; check release notes for compatibility. |
| Winston for Reddit | 1.1.5 | https://github.com/lo-cafe/winston/releases | Upstream-hosted IPA; check release notes for compatibility. |
| VortX | 0.5.5 | https://github.com/VortXTV/VortX/releases | Minimum iOS 16.0. Emulator/game runtime; performance and JIT needs vary by device. Use with services/content you are authorized to access. |
| VortX (Apple TV) | 0.5.5 | https://github.com/VortXTV/VortX/releases | Minimum iOS 18.0. |
| Flycast | 1.0 | https://github.com/chachillie/Flycast-iOS/releases | Minimum iOS 26.0; separate community fork with its own upstream IPA. The older Flyinghead v2.5 URL was stale and is excluded. |
| Nuvio | 0.6.4 | https://github.com/NuvioMedia/NuvioMobile/releases | Open-source media client; bring your own sources; minimum iOS 16.1. |
| Reynard | 0.18.0 | https://github.com/minh-ton/reynard-browser/releases | Experimental Gecko-based browser; minimum iOS 13.0. |
| Geode | 1.5.5 | https://github.com/geode-sdk/ios-launcher/releases | Official Geometry Dash mod launcher; minimum iOS 14.0, requires the full game and an internet connection. |

## Deliberate exclusions and compatibility notes

**PojavLauncher** remains excluded. Its upstream project marks it discontinued, says it does not work on the latest iOS, and directs users to Amethyst instead.

**Jitterbug/Jitterbug Lite** remains excluded. The upstream repository is archived and its latest release is from 2022; StikDebug is the actively maintained JIT tool tracked here.

The older **Flyinghead Flycast v2.5** feed is excluded because its IPA URL is stale. SniffleShop instead tracks a separate **Flycast iOS 26** community fork with its own release artifact.

**RewindBox/NeoStation 0.0.8** was removed after its release IPA URL returned 404 during the link audit. It can be reconsidered if the upstream publishes a reachable, stable asset URL.

## Metadata rules

- `bundleIdentifier` must match the actual app identifier and is case-sensitive.
- `versions[0]` is the newest compatible version presented by the source.
- `size` is the IPA size in bytes, preferably from GitHub release asset metadata or the developer's official source.
- Stable releases are preferred when the project has a stable channel; active beta channels are used when that is the project's supported distribution.
- `appPermissions` is included only when trustworthy current entitlement/privacy metadata is available; it is never guessed.
- Icons and screenshots are included only from reliable upstream project locations.
