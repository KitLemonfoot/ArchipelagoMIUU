using System;
using System.Collections.Generic;
using UnityEngine;

namespace ArchipelagoMIUU
{
    public static class ItemHandler
    {
        //Powerup flags.
        public static Dictionary<string, bool> powerupFlags = new Dictionary<string, bool>()
        {
            {"Super Jump", false},
            {"Boost", false},
            {"Feather Fall", false},
            {"Gravity Surfaces", false},
            {"Bounce Surfaces", false},
        };

        public static int completionMedals = 0;
        public static int goldCompletionMedals = 0;
        public static int medalsPerChapter = 8;
        public static Dictionary<string, int> requiredMedals = new Dictionary<string, int>()
        {
          {"c1", 0},
          {"c2", 5},
          {"c3", 13},
          {"c4", 21},
          {"c5", 29},
          {"c6", 37},
          {"c1a", -1},
          {"c2a", -1},
          {"c3a", -1},
          {"c4a", -1},
        };

        public static void recieveItem(string itemName, string sender)
        {
            if (powerupFlags.ContainsKey(itemName))
            {
                powerupFlags[itemName] = true;
                return;
            }
            switch (itemName)
            {
                case "Completion Medal": completionMedals+=1;break;
                case "Gold Completion Medal": goldCompletionMedals+=1;break;
                case "5 Second Time Freeze": MiscHandler.doTimeTravelItem();break; 
                default: Debug.Log("Invalid item "+itemName+", ignoring.");break;
            }
            if (Notification.instance != null)
            {
                string message = "Received " + itemName + " from " + sender; 
                if(sender == ConnectHandler.APSlot)
                {
                    message = "You found your " + itemName;
                }
                Notification.Notify(message, "Archipelago", 4f, Notification.instance.FoundEgg);
            }
        }

        public static void calculateRequiredMedals()
        {
            //Calculate the required medals.
            //Bit of a messy way to do it, but it works.
            string[] chapters = {"c3", "c4", "c5", "c6"};
            for(int i = 0; i<chapters.Length; i++)
            {
                if (i > LocationHandler.finalLevel)
                {
                    requiredMedals[chapters[i]] = -1;
                    continue;
                }
                requiredMedals[chapters[i]] = 5+(medalsPerChapter*(i+1));
            }
            string[] bonusarc = {"c1a", "c2a", "c3a", "c4a"};
            for(int i = 0; i<bonusarc.Length; i++)
            {
                if (i + 1 > LocationHandler.bonusArcLevel)
                {
                    requiredMedals[bonusarc[i]] = -1;
                    continue;
                }
                requiredMedals[bonusarc[i]] = (i+1)*medalsPerChapter;
            }
        }


    }


}