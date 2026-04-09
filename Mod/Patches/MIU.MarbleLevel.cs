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
            __result = LevelMedal.None;
            if (LocationHandler.isLocationChecked(__instance.id + "-c"))
            {
                __result = LevelMedal.Bronze;
            }
            if (LocationHandler.isLocationChecked(__instance.id + "-s"))
            {
                __result = LevelMedal.Silver;
            }
            if (LocationHandler.isLocationChecked(__instance.id + "-g"))
            {
                __result = LevelMedal.Gold;
            }
            if (LocationHandler.isLocationChecked(__instance.id + "-d"))
            {
                __result = LevelMedal.Diamond;
            }
            return false;
        }
    }

}