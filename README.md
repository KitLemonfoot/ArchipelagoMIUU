# Marble It Up! Ultra Archipelago Client
This is a work-in-progress BepInEx mod for [Marble It Up! Ultra](https://store.steampowered.com/app/864060/Marble_It_Up_Ultra/) that targets the [Archipelago Multiworld Randomizer](https://archipelago.gg/).

## What does Archipelago do to Marble It Up! Ultra?
- Completing levels is a check.
- Depending on YAML settings, completing a level under Silver, Gold, and Diamond times are also checks.
- The various powerups are items in the multiworld.
	- Super Jump
	- Boost (Super Speed)
	- Feather Fall
	- Gravity Surfaces
	- Bounce Surfaces
- To access chapters in the Ultra Arc, you will need Completion Medals. These can be found in the multiworld.
- Chapters in the Bonus Arc will require you play with Gold Medal completion times or higher.
	- Unlocking the chapters will require Gold Completion Medals, which can be found in the multiworld.
- An additional "5 Second Time Freeze" is available as a filler item, which will slow down time for 5 seconds when in a level.
- Death Link support: Falling out of bounds will send a Death Link. Likewise, receiving a Death Link will send you back to your last checkpoint, or the start of the level.
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
- The APWorld and patch files from our releases page
-   [BepInEx x64 5.4.23.x](https://github.com/BepInEx/BepInEx/releases)

### Installing
1. Navigate to Marble It Up! Ultra's local file directory. This can be found by right-clicking on the game in your Steam Library, selecting *Manage*, then selecting *Browse Local Files*. 
2. Install BepInEx to your copy of Marble It Up! Ultra. The guide to do so can be found [in their User Guide.](https://docs.bepinex.dev/articles/user_guide/installation/index.html)
3. Install the contents of `MIUU_Patches.zip` to the BepInEx folder. You should have two folders in the BepInEx folder: `core` and `plugins`.
4. Run the game to generate BepInEx's and the mod's config data.

### APWorld Setup
1. Install Archipelago and open the Archipelago launcher.
2. Click "Install APWorld" and select the `miuultra.apworld` file to install the Marble It Up! Ultra apworld.
3. Click on "Generate Template Options" to generate a template YAML file for Marble It Up! Ultra.
4. Modify the YAML file to your liking and place it in the `Players` folder.

All further instructions can be found in the [official Archipelago Setup Guide](https://archipelago.gg/tutorial/Archipelago/setup/en#on-your-local-installation).

### Connection
1. In the `ArchipelagoMIUU.cfg` file in the `BepInEx\config` folder, enter your Archipelago server's IP address, your slot name, and your server's password if any. 
	- You may also override your YAML's Death Link and Death Link Amnesty settings in this file if you wish .
2. Start Marble It Up! Ultra. The game should connect to the Archipelago server automatically during startup.
3. Your Archipelago server IP should be displayed in the top right corner of the main menu if the connection was successful.

## Building
You will need the latest version of the [.NET SDK](https://dotnet.microsoft.com/download) installed.
1. Place your vanilla Marble It Up! Ultra `Assembly-CSharp.dll`, `Unity.TextMeshPro.dll`, and `UnityEngine.UI.dll` files in the project's lib folder. These dll files can be obtained from the `/Marble It Up_Data/Managed/` folder in your Marble It Up! Ultra install.
2. Ensure you are building a BepInEx 5 Plugin targeting NET45 and Unity 2020.3.44.
3. Run `dotnet build`.
4. Move the resultant `ArchipelagoMIUU.dll`, as well as `Archipelago.MultiClient.Net.dll` and `Newtonsoft.Json.dll` to your BepInEx plugins folder.

## Todo
Quite a bit.
- Create a proper GUI for connecting. (Maybe repurpose the Room ID UI?)
- Implement entrance/level rando. (!!!)
- Add Treasure Boxes as locations and marble cosmetics as filler items.
- Add individual gems as locations and items (Gemsanity).
- Maybe add the Blast powerup from Multiplayer as an item?

## Special Thanks
- **Jarno** for creating their [Timespinner Archipelago implementation](https://github.com/Jarno458/TsRandomizer) that I based a lot of the APWorld code off of
- **icsharpcode** for creating [ILSpy](https://github.com/icsharpcode/ILSpy) to decompile Marble It Up! Ultra's C# code
- **The Marble Blast / Marble It Up team** for creating Marble It Up! Ultra (and for keeping the dreams of this silly marble game from my childhood alive)
- **Tim Clarke** for composing [Tim Trance](https://www.youtube.com/watch?v=gvjhZ5uqIok) which was listened to endlessly during development