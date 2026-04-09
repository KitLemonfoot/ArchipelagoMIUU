using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Always bring up chapter select so player can tell how many medals they need for each chapter.
    [HarmonyPatch(typeof(ChapterSelect), "isChapterSelectUnlocked")]
    class ChapterSelect_isChapterSelectUnlocked_Patch
    {
        public static bool Prefix(ChapterSelect __instance, ref bool __result)
        {
            if (!ConnectHandler.Authenticated)
            {
                return true;
            }
            __result = true;
            return false;
        }
    }

}