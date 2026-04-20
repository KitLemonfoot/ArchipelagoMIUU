using HarmonyLib;
using UnityEngine;
using UnityEngine.UI;

namespace ArchipelagoMIUU.Patches
{
    //Remove the Watch and Race buttons to prevent errors.
    [HarmonyPatch(typeof(LevelSelect), "SetSelected")]
    class LevelSelect_SetSelected_Patch
    {
        public static void Postfix(LevelSelect __instance)
        {
            if(JoystickUISelector.instance.CurrentSelection == __instance.ghostButton.GetComponent<Button>())
            {
                JoystickUISelector.instance.SelectSelectable(__instance.playButton);
            }
            if(JoystickUISelector.instance.CurrentSelection == __instance.replayButton.GetComponent<Button>())
            {
                JoystickUISelector.instance.SelectSelectable(__instance.playButton);
            }
            __instance.ghostButton.SetActive(false);
            __instance.replayButton.SetActive(false);
        }
    }

}