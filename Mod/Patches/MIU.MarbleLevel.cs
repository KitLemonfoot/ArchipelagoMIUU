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
            if (LocationHandler.bronzeMedals && !LocationHandler.isLocationChecked(__instance.id + "-c"))
                __result = LevelMedal.None;
            else if (LocationHandler.silverMedals && !LocationHandler.isLocationChecked(__instance.id + "-s"))
                __result = LevelMedal.Bronze;
            else if (LocationHandler.goldMedals && !LocationHandler.isLocationChecked(__instance.id + "-g"))
                __result = LevelMedal.Silver;
            else if (LocationHandler.diamondMedals && !LocationHandler.isLocationChecked(__instance.id + "-d"))
                __result = LevelMedal.Gold;
            else
                __result = LevelMedal.Diamond;

            if (__result == LevelMedal.Diamond && !LocationHandler.diamondMedals)
                __result = LevelMedal.Gold;
            if (__result == LevelMedal.Gold && !LocationHandler.goldMedals)
                __result = LevelMedal.Silver;
            if (__result == LevelMedal.Silver && !LocationHandler.silverMedals)
                __result = LevelMedal.Bronze;
            if (__result == LevelMedal.Bronze && !LocationHandler.bronzeMedals)
                __result = LevelMedal.None;

            return false;
        }
    }

}
