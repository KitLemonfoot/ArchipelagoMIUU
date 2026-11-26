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

    //Handle granting marbles Blast.
    [HarmonyPatch(typeof(MarbleController), "IsBlastAllowed")]
    class MarbleController_IsBlastAllowed_Patch
    {
        public static bool Prefix(MarbleController __instance, ref bool __result)
        {
            if(ConnectHandler.Authenticated){
                return true;
            }
            __result = ItemHandler.powerupFlags["Blast"];
            return false;
        }
    }

    // Handle checkpointsanity.
    [HarmonyPatch(typeof(MarbleController), "OnCheckpoint")]
    class MarbleController_OnCheckpoint_Patch
    {
        public static bool Prefix(MarbleController __instance, GameObject checkpoint)
        {
            // Do already-touched check from original game to prevent pummeling AP
            GameObject lastCheckpoint = Traverse.Create(__instance).Field("LastCheckpoint").GetValue() as GameObject;
            if(lastCheckpoint == checkpoint && __instance.LastCheckpointGemsRemaining == __instance.GemsRemaining)
            {
                return true;
            }
            // The game determines which checkpoint to send you back to based on the checkpoint object's Unity transform, meaning there isn't really 
            // a good way to ID which checkpoints exist in a level. It sucks, but this is the next best option. 
            Vector3 pos = checkpoint.transform.position;
            string posString = $"{pos.x}{pos.y}{pos.z}";
            MiscHandler.Log($"Touched a checkpoint in {GlobalContext.CurrentLevel.id} with adapted checkpoint ID of {posString}");
            LocationHandler.CheckLocation($"{GlobalContext.CurrentLevel.id}-ckpt-{posString}");
            return true;
        }
    }

    //Respawn patches.
    [HarmonyPatch(typeof(MarbleController), "Respawn")]
    class MarbleController_Respawn_Patch
    {
        //Null a checkpoint spawn if we do not have it unlocked. 
        //Ignore if Checkpointsanity items are disabled or not connected to AP.
        public static bool Prefix(MarbleController __instance)
        {
            if(!ConnectHandler.Authenticated){return true;}
            if(ItemHandler.checkpointsanity < 2){return true;}
            if(ItemHandler.allowedCheckpoints.Contains(LevelSelect.instance.level.name)){return true;}
            if(ItemHandler.allowedCheckpoints.Contains(LevelSelect.instance.chapter.name)){return true;}
            Traverse.Create(__instance).Field("LastCheckpoint").SetValue(null);
            return true;
        }

        //For some reason, some levels spawn the marble out of bounds on load, which messes with Death Link.
        //As such, disallow Death Link until the marble is done respawning.
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
