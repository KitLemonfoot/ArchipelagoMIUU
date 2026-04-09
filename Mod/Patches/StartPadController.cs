using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Re-enable deathlinking after player spawns.
    [HarmonyPatch(typeof(StartPadController), "SetCountdownTime")]
    class StartPadController_SetCountdownTime_Patch
    {
        public static void Postfix(StartPadController __instance, float time)
        {
            if(time>=0f && time < __instance.CountdownTime)
            {
                MiscHandler.disallowDeathlink = false;
            }
        }
    }

}