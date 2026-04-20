using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Handle crushing deathlink.
    [HarmonyPatch(typeof(MarbleGrinderEffectController), "TriggerCrush")]
    class MarbleGrinderEffectController_TriggerCrush_Patch
    {
        public static void Postfix(MarbleGrinderEffectController __instance, MarbleController marble)
        {
            if(!(ConnectHandler.Authenticated && ConnectHandler.doingDeathlink))
            {
                return;
            }
            if (!marble.isMyClientMarble())
            {
                Debug.Log("User died, crush");
                MiscHandler.handleDeath(marble, 1);
            }
            return;
        }
    }

}