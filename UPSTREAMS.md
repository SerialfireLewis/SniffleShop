# Upstream release sources

Last reviewed: **2026-10-24**

SniffleShop points to upstream IPA files directly; it does not rehost them. Release metadata is checked against official developer releases or developer-maintained source feeds.

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
