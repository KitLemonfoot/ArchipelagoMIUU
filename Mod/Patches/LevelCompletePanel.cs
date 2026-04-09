using HarmonyLib;
using MIU;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Stub Replay.
    [HarmonyPatch(typeof(LevelCompletePanel), "WaitForReplay")]
    class LevelCompletePanel_WaitForReplay_Patch
    {
        public static bool Prefix(LevelCompletePanel __instance, ref Replay replay, ref bool shouldSave)
        {
            Debug.Log("Hijacking replay...");
            replay=null;
            shouldSave = false;
            return true;
        }
    }

    //Stub Replay.
    [HarmonyPatch(typeof(LevelCompletePanel), "AttemptGlobalSave")]
    class LevelCompletePanel_AttemptGlobalSave_Patch
    {
        public static bool Prefix(LevelCompletePanel __instance)
        {
            Debug.Log("Refusing replay upload (AGS).");
            SaveIndicator.isSaving = false;
            __instance.canRetry = true;
            return false;
        }
    }

}