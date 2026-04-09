using System;
using System.Collections.Generic;
using UnityEngine;

using Archipelago.MultiClient.Net.Models;

namespace ArchipelagoMIUU
{
    public static class LocationHandler
    {
        public static Dictionary<string, long> locations = new Dictionary<string, long>();
        public static Dictionary<long, ScoutedItemInfo> scoutedLocations = new Dictionary<long, ScoutedItemInfo>();

        public static int finalLevel = 0;
        public static int bonusArcLevel = 0;
        public static string[] endLocations = {"overclocked_update", "citadel", "mobiusmadness_v2", "apogee_v2"};
        public static Action<bool> s => SentCheck;

        public static void CheckLocation(string loc)
        {
            if(locations.ContainsKey(loc) && ConnectHandler.Authenticated){
                if (ConnectHandler.Session.Locations.AllLocationsChecked.Contains(locations[loc]))
                {
                    return;
                }
				Debug.Log("Checking location: "+loc);
				ConnectHandler.Session.Locations.CompleteLocationChecksAsync(locations[loc]);
                //Send notification.
                if (Notification.instance != null)
                {
                    string message = "";
                    if(scoutedLocations[locations[loc]].Player.Name != ConnectHandler.APSlot)
                    {
                        message = "Sent " + scoutedLocations[locations[loc]].ItemName + " to " + scoutedLocations[locations[loc]].Player.Name; 
                        Notification.Notify(message, "Archipelago", 4f, Notification.instance.Egg);
                    }
                }
                
			}
			else Debug.Log("Location \"" + loc + "\" does not exist or you are not connected to AP.");
        }

        public static bool isLocationChecked(string loc)
        {
            if (!locations.ContainsKey(loc))
            {
                return false;
            }
            return ConnectHandler.Session.Locations.AllLocationsChecked.Contains(locations[loc]);
        }

        public static void SentCheck(bool t)
        {    
        }
    }
}