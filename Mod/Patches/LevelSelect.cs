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

    //Ghost playback stubbing
    [HarmonyPatch(typeof(LevelSelect), "TryPlayMapGhost")]
    class LevelSelect_TryPlayMapGhost_Patch
    {
        public static bool Prefix()
        {
            return false;
        }
    }

    //Replay playback stubbing
    [HarmonyPatch(typeof(LevelSelect), "TryPlayMapReplay")]
    class LevelSelect_TryPlayMapReplay_Patch
    {
        public static bool Prefix()
        {
            return false;
        }
    }

}
