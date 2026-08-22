using HarmonyLib;
using MIU;
using System;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Visually show the currently obtained AP medal instead of what the savefile has.
    [HarmonyPatch(typeof(MIU.MarbleLevel), "GetMedalForScore", new Type[]{typeof(MIU.HighScoreRecord)})]
    class MIUMarbleLevel_GetMedalForScore_Patch
    {
        public static bool Prefix(MIU.MarbleLevel __instance, HighScoreRecord score, ref LevelMedal __result)
        {
            if (!ConnectHandler.Authenticated)
            {
                return true;
            }
            if (!LocationHandler.isLocationChecked(__instance.id + "-c"))
                __result = LevelMedal.None;
            else if (LocationHandler.medalTypes >= 1 && !LocationHandler.isLocationChecked(__instance.id + "-s"))
                __result = LevelMedal.Bronze;
            else if (LocationHandler.medalTypes >= 2 && !LocationHandler.isLocationChecked(__instance.id + "-g"))
                __result = LevelMedal.Silver;
            else if (LocationHandler.medalTypes >= 3 && !LocationHandler.isLocationChecked(__instance.id + "-d"))
                __result = LevelMedal.Gold;
            else
                __result = (LevelMedal)(LocationHandler.medalTypes + 1);
            return false;
        }
    }

}
