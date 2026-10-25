# ROM Toolkit for iPhone, iPad, and LiveContainer

A practical companion list for working with legally obtained ROM dumps, patch files, emulator saves, and compressed game files. The browser tools below process files locally according to their project documentation; check each project's privacy and compatibility notes before using it.

## 1. Extract 7z and other archives

### [7zen](https://get7zen.app/) — easiest native iOS/iPadOS extractor

- Opens and extracts `.7z`, `.rar`, `.zip`, `.tar`, `.tar.gz`, `.tar.bz2`, `.tar.xz`, `.gz`, `.bz2`, `.xz`, and `.lz4`.
- Browse archive contents and preview files before extracting; extract everything or only selected files.
- The developer says it works offline, has no ads/tracking, and requires iOS/iPadOS 16+.
- **Distribution:** App Store, not a sideloadable IPA. The official website links to the App Store.

### [rom-weaver](https://rom-weaver.com/apply-patches) — archive-aware ROM workbench

- Opens ROMs and patches directly from ZIP, 7z, RAR and other supported archives; can create ZIP/7z output.
- Chains multiple patches, identifies ROMs by checksum, compares hashes, and supports a wide set of patch formats.
- Includes emulator save import/export and save trimming/editing features; some save-editing features are marked beta.
- Runs in supported mobile browsers and can work offline after caching the app and the data needed for the task.
- **Best use:** a one-stop ROM workflow in Safari when you don't want to extract a patch archive manually first.

## 2. Patch ROMs

### [Rom Patcher JS](https://www.marcrobledo.com/RomPatcher.js/)

- Applies and creates IPS, UPS, APS, BPS, RUP, PPF, Paper Mario `.mod`, and xdelta/VCDiff patches.
- Shows CRC32, MD5, and SHA-1 before patching, can remove headers, and unpacks supported patch archives automatically.
- Runs in a modern browser, including mobile Safari.

### [PatchVault](https://patchvault.app/)

- Applies IPS, BPS, UPS, and xdelta patches in the browser.
- Includes save converters for moving saves among common emulator formats, including Delta, RetroArch, Folium, and DeSmuME.
- The project states that files are processed locally and not uploaded.

### [rom-weaver patch workflow](https://rom-weaver.com/apply-patches)

Use this when the patch is itself inside a `.7z`, `.rar`, or `.zip`, when several patches must be applied in sequence, or when you want a repeatable saved patch recipe. It supports many more formats than the quick patchers; see its own format/feature documentation for exact support.

## 3. ROM identification, checksums, and preservation

### [rom-weaver](https://rom-weaver.com/)

Use the identify/checksum workflow to fingerprint a ROM, compare its hashes with known data, inspect patch requirements, and detect revision mismatches before patching. This is especially useful when a patch says it needs a particular region or revision.

### [ROMhacking.net](https://www.romhacking.net/)

A reference library for ROM-hacking utilities, patch documentation, and project information. Prefer patch files and instructions from the original project author where possible.

### [No-Intro DAT-o-MATIC](https://datomatic.no-intro.org/) and [Redump](https://redump.org/)

Reference databases for identifying and verifying cartridge-based and optical-disc dumps. A matching checksum helps establish that your dump matches a known release; it does not itself grant permission to download or distribute copyrighted game files.

## 4. Advanced format conversion

### [Final ROM source/releases](https://github.com/Yasome/FinalRom)

An offline multi-platform ROM utility project covering patching, hashing, CHD compression/decompression, and several console-image conversions. The repository includes source code and release assets, but **do not assume a ready-made IPA is available**: check the release assets or build the iOS app from source on a Mac with Xcode. This is a project reference, not currently listed as a ready-to-install SniffleShop IPA.

### [Compressatorium](https://github.com/pacnpal/compressatorium)

A self-hostable web UI for specialized game-image conversions, including CHD, RVZ/WIA, NKit, 3DS, Switch, and handheld-ROM archive workflows. It is aimed at a server/desktop environment, not a lightweight iPad-native app. Because it processes large game files, prefer a trusted self-hosted instance rather than uploading files to an unknown public server.

## 5. Suggested LiveContainer workflow

LiveContainer runs compatible iOS apps inside its own environment; it is **not** an emulator and does not replace the ROM patching/extraction tools above. Use it to keep compatible emulator and utility apps organized, while Safari handles the browser-based tools.

1. **Extract first:** open a `.7z` archive in 7zen, then save the ROM or patch file into Files. If the archive contains a patch bundle, rom-weaver may be able to open and process it directly without a separate extraction step.
2. **Patch a clean copy:** open Rom Patcher JS, PatchVault, or rom-weaver in Safari. Select the legally obtained base ROM and patch. Save the patched output as a new file; keep the original untouched.
3. **Verify the result:** check the output hash where supported, and confirm the patch's required region/revision. A patch applied to the wrong ROM revision can fail or produce a broken output.
4. **Import into an emulator:** save the output in Files, then use the emulator's file importer or the iOS share sheet. LiveContainer 3.8 added a share-to-apps flow for files and URLs; actual handoff depends on the guest app supporting the relevant file type.
5. **Handle saves carefully:** keep a backup before converting a save. Emulator save-state files and in-game battery saves are different formats; a converter for one may not support the other.
6. **For JIT-dependent guests:** check the app's compatibility notes and LiveContainer's current JIT setup guide. Not every IPA works inside LiveContainer, and a guest app may need its own configuration.

### Important boundaries

- The websites in this guide are companion tools, not IPA entries in `source.json`.
- 7zen is an App Store app, not an IPA download hosted by SniffleShop.
- Do not add random repackaged IPA mirrors just to make a tool appear sideloadable.
- This guide does not link to copyrighted ROM downloads, BIOS files, firmware keys, or pirated game collections. Use legally obtained files and follow each patch author's instructions.
- Browser file APIs and available memory vary by iOS version and browser. Very large disc images may be better handled on a desktop or trusted self-hosted conversion tool.
