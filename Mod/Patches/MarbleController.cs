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
                MiscHandler.Log("User died, fall");
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

    //Handle cosmetic shuffle trap on the main Unity thread.
    //TODO: I hate doing this. It was fine in holo8 but not so much here. Learn how to actually make this sort of thing threadsafe.
    [HarmonyPatch(typeof(MarbleController), "Update")]
    class MarbleController_Update_Patch
    {
        public static void Postfix(MarbleController __instance)
        {
            if (MiscHandler.shuffleTrapLatch)
            {
                __instance.ApplyMyCosmetics(runtimeUpdate: true);
                CameraController.instance.player.ApplyMyCosmetics(runtimeUpdate: true);
                MiscHandler.shuffleTrapLatch = false;
            }
        }
    }

}
