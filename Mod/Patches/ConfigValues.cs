using HarmonyLib;
using MIU;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Lock levels if AP does not have enough completion medals.
    [HarmonyPatch(typeof(ConfigValues), "isChapterUnlocked")]
    class ConfigValues_isChapterUnlocked_Patch
    {
        public static bool Prefix(ConfigValues __instance, string chapterID, ref bool __result)
        {
            if (!ConnectHandler.Authenticated)
            {
                return true;
            }
            MarbleChapter chapter = __instance.GetChapter(chapterID);
            if (chapter == null)
            {
                __result = false;
                return false;
            }
            if(chapter != null && ItemHandler.requiredMedals.ContainsKey(chapterID))
            {
                if(ItemHandler.requiredMedals[chapterID] == -1)
                {
                    __result = false;
                    return false;
                }
                //Bonus arc
                if (chapter.chapterSet == "Bonus" && ItemHandler.goldCompletionMedals >= ItemHandler.requiredMedals[chapterID])
                {
                    __result = true;
                    return false;
                }
                if (chapter.chapterSet != "Bonus" && ItemHandler.completionMedals >= ItemHandler.requiredMedals[chapterID])
                {
                    __result = true;
                    return false;
                }
            }
            __result = false;
            return false;
        }

    }

    //Return AP lock text.
    [HarmonyPatch(typeof(ConfigValues), "GetLockText")]
    class ConfigValues_GetLockText_Patch
    {
        public static bool Prefix(ConfigValues __instance, string chapterID, ref string __result)
        {
            if (!ConnectHandler.Authenticated)
            {
                return true;
            }
            string result = "";
            if (!ItemHandler.requiredMedals.ContainsKey(chapterID) || ItemHandler.requiredMedals[chapterID]<0)
            {
                result = "This chapter is not available in this multiworld...";
            }
            else
            {
                if (chapterID.EndsWith("a")){
                    int remaining = ItemHandler.requiredMedals[chapterID] - ItemHandler.goldCompletionMedals;
                    result = "Receive "+remaining+" more Gold Completion Medals from the multiworld to unlock!";
                }
                else
                {
                    int remaining = ItemHandler.requiredMedals[chapterID] - ItemHandler.completionMedals;
                    result = "Receive "+remaining+" more Completion Medals from the multiworld to unlock!";
                }
            }
            __result = result;
            return false;
        }
    }

}