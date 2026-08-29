using HarmonyLib;
using UnityEngine;
using MIU;
using System.Collections.Generic;

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
                //Handle logical complete message
                int medalType = ConnectHandler.Authenticated ? LocationHandler.medalTypes : 3;
                int hardestUnachievableMedal = -1;
                bool canGetMedal = true;
                for (int i = 0; i <= medalType; i++) {
                    canGetMedal = ItemHandler.canLogicallyCompleteLevel(GlobalContext.CurrentLevel.id, i);
                    if (!canGetMedal)
                    {
                        hardestUnachievableMedal = i;
                        break;
                    }
                }
                bool canGetTreasure;
                if (!LocationHandler.treasureboxsanity && ConnectHandler.Authenticated)
                    canGetTreasure = true;
                else
                    canGetTreasure = ItemHandler.canLogicallyCompleteLevel(GlobalContext.CurrentLevel.id, 4);
                if (!canGetMedal || !canGetTreasure)
                {
                    MarbleController[] array = GameProcess.ServerProcess.FindObjectsOfType<MarbleController>();
                    if (array.Length == 0)
                    {
                        MiscHandler.Log("Failed to find any marbles to tell about no logic.");
                        return;
                    }
                    List<string> cantGet = [];
                    if (!canGetMedal)
                        cantGet.Add(HighScorePanelItemDisplay.GetMedalTypeName(hardestUnachievableMedal));
                    if (!canGetTreasure)
                        cantGet.Add("treasure box");

                    GamePlayManager.Get().SetTutorial("You may not have all the required items to get the " + string.Join(" or ", cantGet) + "...", null);
                    foreach(MarbleController marble in array)
                    {
                        float expiry = Time.time + 5f;
                        Traverse.Create(marble).Field("TutorialHideTime").SetValue(expiry);
                    }
                }
            }

        }
    }

}
