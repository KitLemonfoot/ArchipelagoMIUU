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
    internal class HighScorePanelItemDisplay
    {
        public static int SelectedMedalType;
        public static string SelectedLevel;

        public static void SetupPanel(HighScorePanel panel)
        {
            List<HighScorePanel.HighScore> list = [];
            int[] levelLogic = LocationHandler.internalLevelLogic[SelectedLevel];

            if ((levelLogic[SelectedMedalType] & 1) != 0)
                list.Add(new HighScorePanel.HighScore("Super Jump", "NA_LOCAL_ID", 0.0f, "", null, false));
            if ((levelLogic[SelectedMedalType] & 2) != 0)
                list.Add(new HighScorePanel.HighScore("Boost", "NA_LOCAL_ID", 0.0f, "", null, false));
            if ((levelLogic[SelectedMedalType] & 4) != 0)
                list.Add(new HighScorePanel.HighScore("Feather Fall", "NA_LOCAL_ID", 0.0f, "", null, false));
            if ((levelLogic[SelectedMedalType] & 8) != 0)
                list.Add(new HighScorePanel.HighScore("Gravity Surfaces", "NA_LOCAL_ID", 0.0f, "", null, false));
            if ((levelLogic[SelectedMedalType] & 16) != 0)
                list.Add(new HighScorePanel.HighScore("Bounce Surfaces", "NA_LOCAL_ID", 0.0f, "", null, false));
            if ((levelLogic[SelectedMedalType] & 32) != 0)
                list.Add(new HighScorePanel.HighScore("Blue Moving Platforms", "NA_LOCAL_ID", 0.0f, "", null, false));

            if (list.Count == 0)
                list.Add(new HighScorePanel.HighScore("No items required", "NA_LOCAL_ID", 0.0f, "", null, false));

            panel.localScores = list;
        }

        public static string GetMedalTypeName(int medalType = -1)
        {
            if (medalType < 0)
                medalType = SelectedMedalType;
            return medalType switch
            {
                0 => "Bronze Medal",
                1 => "Silver Medal",
                2 => "Gold Medal",
                3 => "Diamond Medal",
                4 => "Treasure Box",
                _ => "Error (please report!)",
            };
        }
    }

    //Setup high score panel for ingame item list.
    [HarmonyPatch(typeof(HighScorePanel), "SetupScores", new Type[]{typeof(MIU.MarbleLevel), typeof(List<HighScoreRecord>)})]
    class HighScorePanel_SetupScores_Patch
    {
        public static bool Prefix(HighScorePanel __instance, MarbleLevel level)
        {
            HighScorePanelItemDisplay.SelectedMedalType = ConnectHandler.Authenticated ? LocationHandler.medalTypes : 3;
            HighScorePanelItemDisplay.SelectedLevel = level.id;
            HighScorePanelItemDisplay.SetupPanel(__instance);

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
            __result = HighScorePanelItemDisplay.GetMedalTypeName();
        }
    }

    //Highscore panel stubbing.
    [HarmonyPatch(typeof(HighScorePanel), "NextHSMode")]
    class HighScorePanel_NextHSMode_Patch
    {
        public static bool Prefix(HighScorePanel __instance)
        {
            int medalType = ConnectHandler.Authenticated ? LocationHandler.medalTypes : 3;
            HighScorePanelItemDisplay.SelectedMedalType++;
            if (HighScorePanelItemDisplay.SelectedMedalType > medalType)
            {
                if ((LocationHandler.treasureboxsanity || !ConnectHandler.Authenticated) && HighScorePanelItemDisplay.SelectedMedalType <= 4)
                    HighScorePanelItemDisplay.SelectedMedalType = 4;
                else
                    HighScorePanelItemDisplay.SelectedMedalType = 0;
            }
            HighScorePanelItemDisplay.SetupPanel(__instance);
            __instance.RefreshScores();
            __instance.scoreTypeText.text = HighScorePanelItemDisplay.GetMedalTypeName();
            return false;
        }
    }
    //Highscore panel stubbing.
    [HarmonyPatch(typeof(HighScorePanel), "PrevHSMode")]
    class HighScorePanel_PrevHSMode_Patch
    {
        public static bool Prefix(HighScorePanel __instance)
        {
            int medalType = ConnectHandler.Authenticated ? LocationHandler.medalTypes : 3;
            HighScorePanelItemDisplay.SelectedMedalType--;
            if (HighScorePanelItemDisplay.SelectedMedalType > medalType)
            {
                HighScorePanelItemDisplay.SelectedMedalType = medalType;
            }
            else if (HighScorePanelItemDisplay.SelectedMedalType < 0)
            {
                if (LocationHandler.treasureboxsanity || !ConnectHandler.Authenticated)
                    HighScorePanelItemDisplay.SelectedMedalType = 4;
                else
                    HighScorePanelItemDisplay.SelectedMedalType = medalType;
            }
            HighScorePanelItemDisplay.SetupPanel(__instance);
            __instance.RefreshScores();
            __instance.scoreTypeText.text = HighScorePanelItemDisplay.GetMedalTypeName();
            return false;
        }
    }

}
