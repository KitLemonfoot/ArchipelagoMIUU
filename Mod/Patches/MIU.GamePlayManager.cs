using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Handle sending locations for clearing stages.
    [HarmonyPatch(typeof(MIU.GamePlayManager), "FinishPlay")]
    class MIUGamePlayManager_FinishPlay_Patch
    {
        public static void Postfix(MIU.GamePlayManager __instance, MarbleController marble)
        {
            if(LevelSelect.instance == null)
            {
                MiscHandler.Log("Unable to send checks, as LevelSelect instance is null somehow");
                return;
            }
            MIU.MarbleLevel level = LevelSelect.instance.level;
            float elapsedTime = marble.ElapsedTime;
            LocationHandler.CheckLocation(level.id+"-c");
            if(elapsedTime <= level.SilverTime)
            {
                LocationHandler.CheckLocation(level.id+"-s");
            }
            if(elapsedTime <= level.GoldTime)
            {
                LocationHandler.CheckLocation(level.id+"-g");
            }
            if(elapsedTime <= level.DiamondTime)
            {
                LocationHandler.CheckLocation(level.id+"-d");
            }
            //Send goal on last level
            if(level.id == LocationHandler.endLocations[LocationHandler.finalLevel])
            {
                ConnectHandler.SendCompletion();
            }
        }
    }

    //For some reason, some levels spawn the marble out of bounds on load, which messes with Death Link.
    //As such, disallow Death Link until the marble is done respawning.
    [HarmonyPatch(typeof(MIU.GamePlayManager), "StartPlay")]
    class MIUGamePlayManager_StartPlay_Patch
    {
        public static bool Prefix()
        {
            MiscHandler.disallowDeathlink = true;
            LevelSelect.instance.level.physModifiers.CanBlast = ItemHandler.powerupFlags["Blast"];
            return true;
        }

    }

    //Handle egg.
    [HarmonyPatch(typeof(MIU.GamePlayManager), "GotEgg")]
    class MIUGamePlayManager_GotEgg_Patch
    {
        public static bool Prefix(MIU.GamePlayManager __instance, MarbleController marble)
        {
            if(LevelSelect.instance == null)
            {
                MiscHandler.Log("Unable to send checks, as LevelSelect instance is null somehow");
                return false;
            }
            MIU.MarbleLevel level = LevelSelect.instance.level;
            string locid = level.id+"-tb";
            if (!marble.isMyClientMarble())
            {
                if (LocationHandler.treasureboxsanity)
                {
                    if (ConnectHandler.Session.Locations.AllLocationsChecked.Contains(LocationHandler.locations[locid]))
                    {
                        Notification.Notify(Localization.TryTranslate("You already found this Treasure Box.", "Unlocks"), Localization.TryTranslate("Treasure Box Found!", "Unlocks"), 3.5f, Notification.instance.FoundEgg);
                    }
                    else
                    {
                        LocationHandler.CheckLocation(locid);
                    }
                }
                else
                {
                    Notification.Notify("Treasure Boxes are not enabled in this multiworld.", Localization.TryTranslate("Treasure Box Found!", "Unlocks"), 3.5f, Assets.APIcon);
                }
            }
            return false;
        }

    }

}
