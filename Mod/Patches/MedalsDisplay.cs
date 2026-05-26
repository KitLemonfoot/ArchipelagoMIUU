using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Handle medal time icons for Treasureboxsanity.
    [HarmonyPatch(typeof(MedalsDisplay), "Setup")]
    class MedalsDisplay_Setup_Patch
    {
        public static void Postfix(MedalsDisplay __instance)
        {
            if (!ConnectHandler.Authenticated)
                return;
            bool flag = LocationHandler.isLocationChecked(LevelSelect.instance.level.id + "-tb");
            if (flag && __instance.MedalTimes.text.Contains("<sprite=8>"))
                __instance.MedalTimes.text = __instance.MedalTimes.text.Replace("<sprite=8>", "<sprite=9>");
            if (!flag && __instance.MedalTimes.text.Contains("<sprite=9>"))
                __instance.MedalTimes.text = __instance.MedalTimes.text.Replace("<sprite=9>", "<sprite=8>");
        }
    }

}
