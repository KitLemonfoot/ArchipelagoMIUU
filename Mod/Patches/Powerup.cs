using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Stub powerups when we don't have the AP item.
    [HarmonyPatch(typeof(Powerup), "ProcessTick")]
    class Powerup_ProcessTick_Patch
    {
        public static bool Prefix(Powerup __instance)
        {
            if (!ConnectHandler.Authenticated)
            {
                return true;
            }
            //Jump
            if(__instance.Effect.name == "Super Jump Pickup" && !ItemHandler.powerupFlags["Super Jump"])
            {
                __instance._availableForPickup = false;
            }
            //Boost
            if(__instance.Effect.name == "Super Speed Pickup" && !ItemHandler.powerupFlags["Boost"])
            {
                __instance._availableForPickup = false;
            }
            //Featherfall
            if(__instance.Effect.name == "Helicopter Pickup" && !ItemHandler.powerupFlags["Feather Fall"])
            {
                __instance._availableForPickup = false;
            }
            return true;
        }
    }

}