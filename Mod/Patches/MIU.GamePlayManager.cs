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
                Debug.Log("Unable to send checks, as LevelSelect instance is null somehow");
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
            return true;
        }

    }

}