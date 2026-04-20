using HarmonyLib;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System;
using System.Collections.Generic;
using MIU;

namespace ArchipelagoMIUU.Patches
{
    //Highscore panel modifying.
    [HarmonyPatch(typeof(HighScorePanel), "Awake")]
    class HighScorePanel_Awake_Patch
    {
        public static void Postfix(HighScorePanel __instance)
        {
            __instance.ScoreHeader.gameObject.transform.GetChild(1).gameObject.SetActive(false);
            __instance.ScoreHeader.gameObject.transform.GetChild(2).gameObject.SetActive(false);
        }
    }

    //Setup high score panel for ingame item list.
    [HarmonyPatch(typeof(HighScorePanel), "SetupScores", new Type[]{typeof(MIU.MarbleLevel), typeof(List<HighScoreRecord>)})]
    class HighScorePanel_SetupScores_Patch
    {
        public static bool Prefix(HighScorePanel __instance, MarbleLevel level)
        {
            List<HighScorePanel.HighScore> list = new List<HighScorePanel.HighScore>();
            int[] levelLogic = LocationHandler.internalLevelLogic[level.id];
            if(levelLogic[0] != -1 && levelLogic[0] <= LocationHandler.medalTypes)
            {
                list.Add(new HighScorePanel.HighScore("Super Jump", "NA_LOCAL_ID", 0.0f, "", null, false));
            }
            if(levelLogic[1] != -1 && levelLogic[1] <= LocationHandler.medalTypes)
            {
                list.Add(new HighScorePanel.HighScore("Boost", "NA_LOCAL_ID", 0.0f, "", null, false));
            }
            if(levelLogic[2] != -1 && levelLogic[2] <= LocationHandler.medalTypes)
            {
                list.Add(new HighScorePanel.HighScore("Feather Fall", "NA_LOCAL_ID", 0.0f, "", null, false));
            }
            if(levelLogic[3] != -1 && levelLogic[3] <= LocationHandler.medalTypes)
            {
                list.Add(new HighScorePanel.HighScore("Gravity Surfaces", "NA_LOCAL_ID", 0.0f, "", null, false));
            }
            if(levelLogic[4] != -1 && levelLogic[4] <= LocationHandler.medalTypes)
            {
                list.Add(new HighScorePanel.HighScore("Bounce Surfaces", "NA_LOCAL_ID", 0.0f, "", null, false));
            }
            __instance.localScores = list;
            //Perform original code delegate
            GraphicRaycaster[] componentsInChildren = __instance.GetComponentsInChildren<GraphicRaycaster>();
            for(int i = 0; i< componentsInChildren.Length; i++)
            {
                componentsInChildren[i].enabled = true;
            }
            return false;
        }
    }

    //Highscore panel header change
    [HarmonyPatch(typeof(HighScorePanel), "GetHeader")]
    class HighScorePanel_GetHeader_Patch
    {
        public static void Postfix(ref string __result)
        {
            __result = "Required Items for Completion";
        }
    }
    
    //Highscore panel stubbing.
    [HarmonyPatch(typeof(HighScorePanel), "NextHSMode")]
    class HighScorePanel_NextHSMode_Patch
    {
        public static bool Prefix()
        {
            return false;
        }
    }
    //Highscore panel stubbing.
    [HarmonyPatch(typeof(HighScorePanel), "PrevHSMode")]
    class HighScorePanel_PrevHSMode_Patch
    {
        public static bool Prefix()
        {
            return false;
        }
    }

}