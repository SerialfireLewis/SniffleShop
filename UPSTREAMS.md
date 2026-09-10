# Upstream release sources

Last reviewed: **2026-09-10**

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
