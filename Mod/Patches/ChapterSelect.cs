using HarmonyLib;
using UnityEngine;
using System.Collections.Generic;
using TMPro;

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

    //Glitter the medal icons and change the text color if they are needed for goaling.
    [HarmonyPatch(typeof(ChapterSelect), "CheckLevelScores")]
    class ChapterSelect_CheckLevelScores_Patch
    {
        public static void Postfix(ChapterSelect __instance)
        {
            if (!ConnectHandler.Authenticated)
            {
                return;
            }
            //ughhh this is ugly
            List<GameObject> medals = Traverse.Create(__instance).Field("medals").GetValue() as List<GameObject>;
            List<MIU.MarbleLevel> chapterLevels = GlobalContext.LevelData.GetChapter(__instance.ChapterID).levels;
            for(int i = 0; i < chapterLevels.Count; i++)
            {
                string levelID = chapterLevels[i].id;
                if (LocationHandler.finalLevels.ContainsKey(levelID))
                {
                    medals[i].GetComponentInChildren<ParticleSystem>().Play();
                    medals[i].GetComponentInChildren<TextMeshProUGUI>().color = Color.cyan;
                }
                else
                {
                    medals[i].GetComponentInChildren<ParticleSystem>().Stop();
                    medals[i].GetComponentInChildren<TextMeshProUGUI>().color = Color.white;
                }
            }

        }
    }

}
