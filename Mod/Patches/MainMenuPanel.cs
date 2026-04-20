using HarmonyLib;
using UnityEngine;
using TMPro;
using System;

namespace ArchipelagoMIUU.Patches
{
    //Hijack the Xbox username and display our stuff.
    [HarmonyPatch(typeof(MainMenuPanel), "Start")]
    class MainMenuPanel_Start_Patch
    {
        public static void Postfix(MainMenuPanel __instance)
        {
            __instance.XBoxUserName.text = "ArchipelagoMIUU Mod v"+MyPluginInfo.PLUGIN_VERSION+"-alpha\n"+MiscHandler.connectString;
            __instance.XBoxUserName.gameObject.SetActive(value:true);
            //Remove UI panels
            GameObject coreUI = __instance.gameObject.transform.GetChild(1).gameObject;
            GameObject right = coreUI.transform.GetChild(4).gameObject;
            right.transform.GetChild(1).gameObject.SetActive(false);
            right.transform.GetChild(2).gameObject.SetActive(false);
            //GameObject bottom = coreUI.transform.GetChild(3).gameObject;
            //GameObject demoButton = bottom.transform.GetChild(0).gameObject;
            //TextMeshProUGUI demoButtonLabel = demoButton.transform.GetChild(0).gameObject.GetComponent<TextMeshProUGUI>();
            //demoButtonLabel.text = "Archipelago";
            //demoButton.SetActive(true);
        }
    }

    //Force Xbox username to visible.
    //A little haphazard but it should work
    [HarmonyPatch(typeof(MainMenuPanel), "Update")]
    class MainMenuPanel_Update_Patch
    {
        public static void Postfix(MainMenuPanel __instance)
        {
            __instance.XBoxUserName.gameObject.SetActive(value:true);
        }
    }

    //Prevent entry to weekly challenges.
    [HarmonyPatch(typeof(MainMenuPanel), "ChallengeButton")]
    class MainMenuPanel_ChallengeButton_Patch
    {
        public static bool Prefix(MainMenuPanel __instance)
        {
            Action acceptAction = delegate
			{
			};
            ConfirmationWindow.instance.Open("Sorry", "Weekly Challenges are disabled while using the Archipelago mod.", "OK", "", acceptAction);
            return false;
        }
    }

    //Prevent entry to multiplayer.
    [HarmonyPatch(typeof(MainMenuPanel), "TryEnterMPUI")]
    class MainMenuPanel_TryEnterMPUI_Patch
    {
        public static bool Prefix(MainMenuPanel __instance)
        {
            Action acceptAction = delegate
			{
			};
            ConfirmationWindow.instance.Open("Sorry", "Multiplayer mode is disabled while using the Archipelago mod.", "OK", "", acceptAction);
            return false;
        }
    }

    //Prevent entry to weekly challenges.
    [HarmonyPatch(typeof(MainMenuPanel), "CustomLevelsButton")]
    class MainMenuPanel_CustomLevelsButton_Patch
    {
        public static bool Prefix(MainMenuPanel __instance)
        {
            Action acceptAction = delegate
			{
			};
            ConfirmationWindow.instance.Open("Sorry", "Custom levels are disabled while using the Archipelago mod.", "OK", "", acceptAction);
            return false;
        }
    }

    //Send demo button to AP menu.
    [HarmonyPatch(typeof(MainMenuPanel), "DemoButton")]
    class MainMenuPanel_DemoButton_Patch
    {
        public static void Postfix()
        {
            PanelManager.instance.GoToPanel(PanelType.Multiplayer);
            MultiplayerPanel.instance.GoToCreatePanel();
            MultiplayerPanel.instance.curMode = MultiplayerPanel.PanelMode.Base;
        }
    }
}