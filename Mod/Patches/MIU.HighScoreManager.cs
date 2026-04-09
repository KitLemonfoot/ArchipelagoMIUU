using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Stub highscore manager.
    [HarmonyPatch(typeof(MIU.HighScoreManager), "ReportLevelScore")]
    class MIUHighScoreManager_ReportLevelScore_Patch
    {
        public static bool Prefix()
        {
            Debug.Log("Got a highscore save request, refusing.");
            return false;
        }
    }

}