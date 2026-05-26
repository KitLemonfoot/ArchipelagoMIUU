using System;
using System.Collections.Generic;
using UnityEngine;
using MIU;
using HarmonyLib;
using Archipelago.MultiClient.Net.Enums;
using System.Reflection;

namespace ArchipelagoMIUU
{
    public static class MiscHandler
    {
        public static string config_APip = "archipelago.gg:38281";
        public static string config_APslot = "MIUUPlayer";
        public static string config_APpassword = "";
        public static int config_overrideDL = -1;
        public static int config_overrideDLAmnesty = -1;
        public static bool disallowDeathlink = false;
        public static bool shuffleTrapLatch = false;

        public static string connectString = "Not connected to Archipelago";

        public static void Log(string message)
        {
            message = "[ARCHIPELAGO] " + message;
            Debug.Log(message);
        }

        public static void SetConnectString(string connectString)
        {
            MiscHandler.connectString = connectString;
            if (MainMenuPanel.instance && MainMenuPanel.instance.XBoxUserName)
            {
                string version = Assembly.GetExecutingAssembly().GetName().Version.ToString() + "-alpha";
                MainMenuPanel.instance.XBoxUserName.text = "ArchipelagoMIUU Mod " + version + "\n" + connectString;
            }
        }

        public static string getItemColor(ItemFlags flags)
        {
            switch (flags)
            {
                case ItemFlags.Advancement: return "<color=#DDA0DD>";
                case ItemFlags.NeverExclude: return "<color=#6A5ACD>";
                case ItemFlags.None: return "<color=#00FFFF>";
                case ItemFlags.Trap: return "<color=#FA8072>";
            }
            return "<color=#FFFFFF>";
        }

        public static void doGrantBlast()
        {
            MarbleController[] array = GameProcess.ServerProcess.FindObjectsOfType<MarbleController>();
            if (array.Length == 0)
            {
                Log("Failed to find any marbles to grant Blast to.");
                return;
            }
            foreach(MarbleController marble in array)
            {
                marble.physMod.CanBlast = true;
            }
        }

        public static void doTimeTravelItem()
        {
            MarbleController[] array = GameProcess.ServerProcess.FindObjectsOfType<MarbleController>();
            if (array.Length == 0)
            {
                Log("Failed to find any marbles to give time travel credit to.");
                return;
            }
            foreach(MarbleController marble in array)
            {
                marble.AddTimeCredit(5f);
            }
        }

        public static void doTimeAddTrap()
        {
            MarbleController[] array = GameProcess.ServerProcess.FindObjectsOfType<MarbleController>();
            if (array.Length == 0)
            {
                UnityEngine.Debug.Log("Failed to find any marbles to take time away from.");
                return;
            }
            foreach(MarbleController marble in array)
            {
                marble.elapsedTime = marble.elapsedTime + 5f;
            }
        }

        public static void doCosmeticShuffleTrap()
        {
            Cosmetic skin = CosmeticManager.Skins[UnityEngine.Random.Range(0, CosmeticManager.Skins.Length)];
            Cosmetic trail = CosmeticManager.Trails[UnityEngine.Random.Range(0, CosmeticManager.Trails.Length)];
            Cosmetic hat = CosmeticManager.Hats[UnityEngine.Random.Range(0, CosmeticManager.Hats.Length)];
            CosmeticManager.MySkin = skin;
            CosmeticManager.MyTrail = trail;
            CosmeticManager.MyHat = hat;
            if (GamePlayManager.Get().IsPlaying)
			{
				shuffleTrapLatch = true;
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

        public static void handleDeath(MarbleController marble, int reason)
        {
            string deathlinkMessage;
            ConnectHandler.deathAmnesty++;
            if (ConnectHandler.deathAmnesty >= ConnectHandler.deathAmnestyMax)
            {
                ConnectHandler.deathAmnesty = 0;
                deathlinkMessage = "You've died "+ConnectHandler.deathAmnestyMax+" times. Death Link sent.";
                if(ConnectHandler.deathAmnestyMax <= 1)
                {
                    deathlinkMessage = "Death Link sent.";
                }
                ConnectHandler.sendDeathLink(reason);
            }
            else
            {
                deathlinkMessage = "You've died "+ ConnectHandler.deathAmnesty +" out of "+ ConnectHandler.deathAmnestyMax +" times...";
            }
            GamePlayManager.Get().SetTutorial(deathlinkMessage, null);
            float expiry = Time.time + 3f;
            Traverse.Create(marble).Field("TutorialHideTime").SetValue(expiry);
        }
    }
}
