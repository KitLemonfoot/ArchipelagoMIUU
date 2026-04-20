using HarmonyLib;
using UnityEngine;
using MIU;

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
                if (!ConnectHandler.Authenticated)
                {
                    return;
                }
                if (!ItemHandler.canLogicallyCompleteLevel(GlobalContext.CurrentLevel.id))
                {
                    MarbleController[] array = GameProcess.ServerProcess.FindObjectsOfType<MarbleController>();
                    if (array.Length == 0)
                    {
                        Debug.Log("Failed to find any marbles to tell about no logic.");
                        return;
                    }
                    GamePlayManager.Get().SetTutorial("You may not have all the required items to beat this level...", null);
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