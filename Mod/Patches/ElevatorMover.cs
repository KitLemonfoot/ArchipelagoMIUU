using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Determine whether to move or not.
    [HarmonyPatch(typeof(ElevatorMover), "Advance")]
    class ElevatorMover_Advance_Patch
    {
        public static bool Prefix(ElevatorMover __instance)
        {
            if((!ItemHandler.powerupFlags["Blue Moving Platforms"]) && __instance.CollapseTriggered)
            {
                return false;
            }
            return true;
        }
    }

}
