# Upstream release sources

Last reviewed: **2026-09-10**

This file records where SniffleShop's metadata and downloads come from. The IPA URLs in `source.json` point to these official projects directly; SniffleShop does not rehost them.

| App | Tracked release | Official upstream | Notes |
| --- | --- | --- | --- |
| LiveContainer | 3.8.0 | https://github.com/LiveContainer/LiveContainer/releases | Uses `LiveContainer.ipa`, not the bundled `LiveContainer+SideStore.ipa`. |
| Feather | 2.9.0 | https://github.com/claration/Feather/releases | Asset byte size is taken from GitHub's release asset metadata. |
| StikDebug | 3.1.10 | https://github.com/StikDebug/StikDebug/releases | Official non-App-Store JIT/debugger release. |
| UTM | 4.7.5 | https://alt.getutm.app | Official UTM source; uses the non-jailbroken `UTM.ipa`. |
| iSH | 1.3.2 | https://github.com/ish-app/ish/releases | Tracks latest stable release (build 494), not rolling prerelease builds. |
| Angel Aura Amethyst | 1.0.9212a18 | https://alt.crystall1ne.dev | Official AngelAuraMC/crystall1ne source; active successor to PojavLauncher. |
| Provenance | 3.3.0 | https://provenance-emu.com/apps.json | Tracks stable release rather than rolling alpha. |
| Flycast | v2.5 | https://flyinghead.github.io/flycast-builds/altstore.json | Official Flycast AltStore source and GitHub release asset. |

## Deliberate exclusions

**PojavLauncher** is not included. Its upstream source now points users to Amethyst as the successor and bounds old Pojav releases to older iOS versions. SniffleShop tracks Amethyst instead.

**Jitterbug/Jitterbug Lite** is not currently included. The upstream repository is archived and the latest release is from 2022. StikDebug is the actively maintained JIT tool in this catalog.

## Metadata rules

- `bundleIdentifier` must match the upstream application identifier.
- `versions[0]` is the latest compatible version SideStore will present.
- `size` is the IPA size in bytes, preferably from GitHub release asset metadata or the developer's official source.
- Stable releases are preferred when an upstream also publishes rolling/nightly builds.
- A beta may be tracked when the upstream project itself treats that build as its active supported distribution, as with Amethyst.
- Icons and screenshots are included only when they come from a reliable upstream project location.
