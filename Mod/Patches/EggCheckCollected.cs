using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Handle texturing for collected treasureboxes.
    [HarmonyPatch(typeof(EggCheckCollected), "OnEnable")]
    class EggCheckCollected_OnEnable_Patch
    {
        public static bool Prefix(EggCheckCollected __instance)
        {
            if (!ConnectHandler.Authenticated)
            {
                return true;
            }
            if(LevelSelect.instance == null || LevelSelect.instance.level==null)
            {
                MiscHandler.Log("Can't update treasurebox textures as levelselect instance or level is null somehow");
                return true;
            }
            string locid = LevelSelect.instance.level.id + "-tb";
            if ((!LocationHandler.treasureboxsanity) || ConnectHandler.Session.Locations.AllLocationsChecked.Contains(LocationHandler.locations[locid]))
            {
                __instance.innerSphere.SetActive(false);
                __instance.caseFrame.material = __instance.caseTransparent;
            }
            else
            {
                __instance.innerSphere.SetActive(true);
                __instance.caseFrame.material = __instance.caseMetal;
            }
            return false;

        }
    }

}
