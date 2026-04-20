using HarmonyLib;
using MIU;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Handle Death Link.
    [HarmonyPatch(typeof(MarbleController), "HandleOutOfLevelBounds")]
    class MarbleController_HandleOutOfLevelBounds_Patch
    {
        public static void Postfix(MarbleController __instance)
        {
            if(!(ConnectHandler.Authenticated && ConnectHandler.doingDeathlink))
            {
                return;
            }
            if (!__instance.isMyClientMarble())
            {
                //Prevent deathlink double jeopardy.
                if (MiscHandler.disallowDeathlink)
                {
                    return;
                }
                Debug.Log("User died, fall");
                MiscHandler.handleDeath(__instance, 0);
            }
        }
    }

    //For some reason, some levels spawn the marble out of bounds on load, which messes with Death Link.
    //As such, disallow Death Link until the marble is done respawning.
    [HarmonyPatch(typeof(MarbleController), "Respawn")]
    class MarbleController_Respawn_Patch
    {
        public static void Postfix(MarbleController __instance)
        {
            if (__instance.InMode(1))
            {
                MiscHandler.disallowDeathlink = false;
            }
        }

    }

}