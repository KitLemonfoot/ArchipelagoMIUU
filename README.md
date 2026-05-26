# Marble It Up! Ultra Archipelago Client
This is a work-in-progress mod for [Marble It Up! Ultra](https://store.steampowered.com/app/864060/Marble_It_Up_Ultra/) that targets the [Archipelago Multiworld Randomizer](https://archipelago.gg/).

## What does Archipelago do to Marble It Up! Ultra?
- Completing levels is a check.
	- Depending on YAML settings, completing a level under Silver, Gold, and Diamond times are also checks.
	- Depending on YAML settings, collecting a level's Treasure Box can also be a check.
- Various powerups and level elements are items in the multiworld.
	- Super Jump
	- Boost (Super Speed)
	- Feather Fall
	- Gravity Surfaces
	- Bounce Surfaces
	- Blue Moving Platforms
- To access chapters in the Ultra Arc, you will need Completion Medals. These can be found in the multiworld.
- Chapters in the Bonus Arc will require you play with Gold Medal completion times or higher.
	- Unlocking the chapters will require Gold Completion Medals, which can be found in the multiworld.
- Several traps are enableable:
	- Time Add Trap: Adds 5 seconds to your current in-game time.
	- Cosmetic Shuffle Trap: Shuffles your marble's current cosmetics.
- An additional "5 Second Time Freeze" is available as a filler item, which will slow down time for 5 seconds when in a level.
- Death Link support: Falling out of bounds or being crushed will send a Death Link. Likewise, receiving a Death Link will send you back to your last checkpoint, or the start of the level.
	- There is also Death Link Amnesty, where you will not send a Death Link until you have died a certain amount of times.

Additionally, the following features will be *disabled* while playing Archipelago:
- Multiplayer
- Weekly Challenges
- Custom Levels
- Saving high scores
- Saving replays
- Amplitude telemetry

You will need to obtain enough Completion Medals to unlock your goal level, then complete it to goal.

## Setup
You will need the following:
- The latest version of [Marble It Up! Ultra, downloaded from Steam](https://store.steampowered.com/app/864060/Marble_It_Up_Ultra/)
- The Archipelago software from [their Releases page](https://github.com/ArchipelagoMW/Archipelago/releases/)
- The APWorld and mod files from our releases page
- MIUU Mod Loader from [their Releases page](https://git.thearst3rd.com/thearst3rd/miuu-mod-loader/releases/latest)
- MIUU Console Unlocker from [their Releases page](https://git.thearst3rd.com/thearst3rd/miuu-console-unlocker/releases/latest)

### Installing
1. Navigate to Marble It Up! Ultra's local file directory. This can be found by right-clicking on the game in your Steam Library, selecting *Manage*, then selecting *Browse Local Files*.
2. Install [MIUU Mod Loader](https://git.thearst3rd.com/thearst3rd/miuu-mod-loader) to your copy of Marble It Up! Ultra if it's not already installed.
3. Extract the contents of `ArchipelagoMIUU-vX.Y.Z.zip` to the `Mods` folder.
4. Also install [Console Unlocker](https://git.thearst3rd.com/thearst3rd/miuu-console-unlocker) if it's not already installed.

### APWorld Setup
1. Install Archipelago and open the Archipelago launcher.
2. Click "Install APWorld" and select the `miuultra.apworld` file to install the Marble It Up! Ultra apworld.
3. Click on "Generate Template Options" to generate a template YAML file for Marble It Up! Ultra.
4. Modify the YAML file to your liking and place it in the `Players` folder.

All further instructions can be found in the [official Archipelago Setup Guide](https://archipelago.gg/tutorial/Archipelago/setup/en#on-your-local-installation).

### Connection
1. Start Marble It Up! Ultra and press `~` to access the in-game console.
2. In the console, use the `apConnect` command to connect to the archipelago server.
3. Your Archipelago server IP should be displayed in the top right corner of the main menu if the connection was successful.
4. **Optional**: Use the `apOverrideDl` and `apOverrideDlAmnesty` commands to override the YAML's Death Link settings. Examples:
	- `apOverrideDl 0` or `apOverrideDl 1` to forcably disable or enable Death Link
	- `apOverrideDlAmnesty 10` to forcably set the Death Link amnesty to 10 deaths (for when Death Link is enabled)
	- `apOverride -1` and `apOverrideDlAmnesty -1` to disable the overrides (it will use the values in the YAML)

## Building
You will need the latest version of the [.NET SDK](https://dotnet.microsoft.com/download) installed.
1. In the `Mod` folder, copy the file `UserProperties.xml.template` as `UserProperties.xml` and edit it as following:
	- Set `GameDir` to be a path pointing to your Marble It Up! Ultra game installation
	- If necessary, change `GameDataDir` to point to the `_Data` folder in your Marble It Up! Ultra installation. Required on Linux
2. Ensure [MIUU Mod Loader](https://git.thearst3rd.com/thearst3rd/miuu-mod-loader) is installed so that the Harmony dll can be found.
3. Build the project with `dotnet build --configuration Release`. This will build the mod and copy it and its dependencies into the `Mods` folder of your MIUU install!

## Todo
Quite a bit.
- Add individual gems as locations and items (Gemsanity).
- Create a proper GUI for connecting.
- Implement entrance/level rando. (!!!)
- Code cleanup and eventual 1.0 release; my plan is to PR this game to Core once it's 100% ready!

## Special Thanks
- **Jarno** for creating their [Timespinner Archipelago implementation](https://github.com/Jarno458/TsRandomizer) that I based a lot of the APWorld code off of
- **icsharpcode** for creating [ILSpy](https://github.com/icsharpcode/ILSpy) to decompile Marble It Up! Ultra's C# code
- **The Marble Blast / Marble It Up team** for creating Marble It Up! Ultra (and for keeping the dreams of this silly marble game from my childhood alive)
- **Tim Clarke** for composing [Tim Trance](https://www.youtube.com/watch?v=gvjhZ5uqIok) which was listened to endlessly during development
