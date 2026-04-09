using System;
using System.Collections.Generic;
using UnityEngine;
using BepInEx.Configuration;
using MIU;

namespace ArchipelagoMIUU
{
    public static class MiscHandler
    {
        public static ConfigEntry<string> config_APip;
        public static ConfigEntry<string> config_APslot;
        public static ConfigEntry<string> config_APpassword;
        public static ConfigEntry<int> config_overrideDL;
        public static ConfigEntry<int> config_overrideDLAmnesty;
        public static bool disallowDeathlink = false;

        public static string connectString = "Not connected to Archipelago";

        public static void doTimeTravelItem()
        {
            MarbleController[] array = GameProcess.ServerProcess.FindObjectsOfType<MarbleController>();
            if (array.Length == 0)
            {
                UnityEngine.Debug.Log("Failed to find any marbles to give time travel credit to.");
                return;
            }
            foreach(MarbleController marble in array)
            {
                marble.AddTimeCredit(5f);
            }
        }

        public static void killMarbles()
        {
            MarbleController[] array = GameProcess.ServerProcess.FindObjectsOfType<MarbleController>();
            if (array.Length == 0)
            {
                UnityEngine.Debug.Log("Failed to find any marbles to kill.");
                return;
            }
            foreach(MarbleController marble in array)
            {
                disallowDeathlink = true;
                marble.ForceOutOfBounds();
            }
            disallowDeathlink = false;

        }

        //Using this for config of AP server, slot, and password fields.
        public static void setConfig(ConfigFile cfg){
            config_APip = cfg.Bind("General", "ArchipelagoIP", "archipelago.gg:", "IP address of the Archipelago server you wish to connect to.");
            config_APslot = cfg.Bind("General", "ArchipelagoSlotName", "MIUUPlayer", "Slot name of the Archipelago server you wish to connect to.");
            config_APpassword = cfg.Bind("General", "ArchipelagoPassword", "", "Password of the Archipelago server you wish to connect to, if any.");
            config_overrideDL = cfg.Bind("Overrides", "OverrideDeathLink", -1, "Override your YAML's Death Link setting. -1: No Override, 0: Disabled, 1: Enabled");
            config_overrideDLAmnesty = cfg.Bind("Overrides", "OverrideDeathLinkAmnesty", -1, "Override your YAML's Death Link Amnesty setting. Values must be between 1 and 20, or -1 to disable.");
        }

    }


}