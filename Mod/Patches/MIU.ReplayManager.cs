using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Stub replay manager.
    [HarmonyPatch(typeof(MIU.ReplayManager), "ReportReplay")]
    class MIUReplayManager_ReportReplay_Patch
    {
        public static bool Prefix()
        {
            Debug.Log("Got a replay save request, refusing.");
            return false;
        }
    }

    //Stub replay manager.
    [HarmonyPatch(typeof(MIU.ReplayManager), "SetBestReplay")]
    class MIUReplayManager_SetBestReplay_Patch
    {
        public static bool Prefix()
        {
            Debug.Log("Got a replay save request, refusing.");
            return false;
        }
    }

}