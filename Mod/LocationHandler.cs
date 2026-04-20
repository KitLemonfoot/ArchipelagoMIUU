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

        /// Used for the ingame tracker. All other logic is handled by the apworld.
        /// Note: this will be expanded later to include gems and other items
        /// 
        /// Index:
        /// 0: Super Jump
        /// 1: Boost
        /// 2: Feather Fall
        /// 3: Gravity Surfaces
        /// 4: Bounce Surfaces
        /// 
        /// Value:
        /// -1: Not needed
        /// 0: Needed for base completion
        /// 1: Needed for silver+
        /// 2: Needed for gold+
        /// 3: Needed for diamond+
        /// 4: Not used (Needed only for treasure)
        public static Dictionary<string, int[]> internalLevelLogic = new Dictionary<string, int[]>()
        {
            {"learning_to_roll_update", [-1, -1, -1, -1, -1]},
            {"learning_to_turn_update", [-1, -1, -1, -1, -1]},
            {"bunny_slope", [-1, -1, -1, -1, -1]},
            {"learning_to_jump_update", [0, -1, -1, -1, -1]},
            {"fsa_update", [-1, 1, -1, -1, -1]},
            {"treasure_update", [-1, -1, -1, -1, -1]},
            {"frosty_update", [-1, -1, -1, -1, -1]},
            {"roundbend", [-1, -1, -1, 0, -1]},
            {"leaf_on_the_wind", [-1, -1, 2, -1, -1]},
            {"duality_v2", [-1, -1, -1, -1, -1]},
            {"L2bounce", [-1, -1, -1, -1, 0]},
            {"greatWall", [-1, -1, -1, -1, -1]},
            {"carom_v2", [-1, -1, -1, -1, -1]},
            {"rush_hour", [-1, -1, -1, -1, -1]},
            {"otgw_update", [0, 0, -1, -1, 0]},
            {"intothearctic_v2", [-1, -1, -1, -1, -1]},
            {"wave_pool_update", [1, 1, -1, -1, -1]},
            {"bigeasy", [-1, -1, -1, -1, -1]},
            {"transit_mayhem", [-1, -1, -1, -1, -1]},
            {"gravityknot_v2", [-1, -1, -1, 0, -1]},
            {"steppingstones_update", [0, 0, -1, 0, -1]},
            {"speedball_v2", [-1, -1, -1, -1, -1]},
            {"mountmarblius_v2", [-1, -1, -1, -1, 0]},
            {"transmission_v2", [-1, -1, -1, -1, -1]},
            {"archipelago", [-1, -1, 0, -1, -1]},
            {"sugarRush", [-1, 0, -1, -1, -1]},
            {"slalom_v2", [-1, -1, -1, -1, -1]},
            {"outskirts", [-1, -1, -1, -1, -1]},
            {"offkilter", [-1, -1, -1, 0, -1]},
            {"icyascent", [-1, 0, -1, -1, -1]},
            {"badcompany_v2", [-1, -1, -1, -1, -1]},
            {"tubular", [-1, -1, 0, -1, -1]},
            {"overclocked_update", [-1, -1, -1, -1, -1]},
            {"tether", [-1, -1, -1, 0, -1]},
            {"aqueduct", [-1, -1, -1, -1, -1]},
            {"ricochet_v2", [-1, 0, -1, -1, 0]},
            {"braid_update", [-1, 0, -1, -1, 0]},
            {"sun_spire", [-1, -1, -1, -1, -1]},
            {"thunderdrome", [-1, 0, -1, -1, -1]},
            {"hyperloop", [-1, 1, -1, -1, -1]},
            {"gearing_up", [-1, -1, -1, -1, -1]},
            {"acrophobia", [-1, -1, -1, -1, -1]},
            {"rime", [-1, -1, -1, -1, -1]},
            {"cogValley", [-1, -1, -1, -1, -1]},
            {"citadel", [0, 0, -1, -1, -1]},
            {"newtonscradle", [-1, -1, -1, -1, -1]},
            {"exmachina", [-1, -1, 0, -1, -1]},
            {"gearheart", [-1, -1, -1, -1, -1]},
            {"kleinsche", [-1, -1, -1, 0, -1]},
            {"direstraits", [0, -1, -1, -1, -1]},
            {"diamond", [-1, -1, -1, -1, -1]},
            {"glacier_v2", [-1, 1, -1, -1, -1]},
            {"shift", [-1, -1, -1, -1, -1]},
            {"conduit_v2", [-1, 0, -1, -1, 0]},
            {"flip_the_table_v2", [-1, -1, -1, 0, -1]},
            {"energy_v2", [0, -1, -1, -1, 0]},
            {"mobiusmadness_v2", [-1, 0, -1, 0, -1]},
            {"amethyst_v2", [-1, -1, -1, -1, -1]},
            {"rondure", [-1, -1, -1, 0, -1]},
            {"isaacs_apple", [-1, -1, -1, -1, -1]},
            {"penrosepass", [-1, -1, -1, 0, -1]},
            {"siege", [0, 0, 0, -1, -1]},
            {"flywheel_v2", [-1, 0, -1, -1, -1]},
            {"symbiosis", [-1, -1, -1, -1, -1]},
            {"tesseract", [-1, -1, -1, 0, -1]},
            {"leapsandbounds_v2", [0, -1, -1, -1, -1]},
            {"vertigo_mayhem", [-1, -1, -1, -1, -1]},
            {"tossedabout_v2", [-1, -1, 0, -1, 0]},
            {"apogee_v2", [0, 0, 0, 0, 0]},
            {"rosenbridge_update", [-1, -1, -1, -1, -1]},
            {"onward_and_upward_mayhem", [0, 1, -1, 0, -1]},
            {"permutation", [-1, -1, -1, -1, 0]},
            {"elevatoraction", [-1, -1, -1, -1, -1]},
            {"timecapsule", [-1, -1, -1, 0, -1]},
            {"3divide", [1, 1, -1, -1, -1]},
            {"4stairs", [0, -1, -1, -1, -1]},
            {"need_for_speed", [-1, 0, -1, -1, -1]},
            {"rivervantage", [0, 0, -1, -1, -1]},
            {"gravitycube_update", [0, -1, -1, 0, 0]},
            {"epoch", [-1, 1, -1, -1, -1]},
            {"platinum_playground_mayhem", [-1, 0, -1, -1, -1]},
            {"ribbon_v2", [-1, -1, -1, 0, -1]},
            {"castlechaos", [-1, -1, -1, -1, 0]},
            {"threadNeedle", [0, 0, -1, 0, -1]},
            {"gordian_mayhem", [0, -1, -1, 0, -1]},
            {"bumperinvasion", [-1, -1, -1, -1, -1]},
            {"bash_tion", [0, 0, 0, -1, -1]},
            {"runout", [-1, -1, -1, -1, -1]},
            {"archiarchy", [-1, -1, 0, -1, -1]},
            {"crystalmatrix", [1, 1, -1, -1, -1]},
            {"stayinalive_mayhem", [-1, -1, -1, -1, -1]},
            {"machinations_update", [0, -1, -1, -1, -1]},
            {"pitofdespair", [0, -1, -1, -1, -1]},
            {"contraption", [-1, -1, -1, -1, -1]},
            {"uphill", [0, 0, -1, 0, -1]},
            {"retro", [-1, 1, -1, -1, -1]},
            {"warpcore", [-1, -1, -1, 0, -1]},
            {"bash_faster", [-1, 0, -1, -1, -1]},
            {"prime_v2", [-1, -1, -1, -1, -1]},
            {"halfpipeheaven_v2", [-1, 0, -1, -1, -1]},
            {"wanderlust_v2", [0, -1, -1, 0, -1]},
            {"boomerang", [-1, -1, -1, -1, 0]},
            {"kendama", [-1, 0, -1, -1, -1]},
            {"cirrus_update", [-1, -1, 0, 0, -1]},
            {"zenith", [0, -1, -1, -1, 0]},
            {"alldownhill", [-1, -1, -1, 0, -1]},
            {"dangerzone", [0, -1, -1, 0, -1]},
            {"olympus", [-1, -1, -1, -1, -1]},
            {"headintheclouds_mayhem", [-1, -1, -1, -1, -1]},
            {"centripitalforce", [-1, -1, -1, -1, -1]},
            {"slickshtick", [-1, -1, -1, -1, -1]},
            {"network", [0, -1, -1, 0, -1]},
            {"radius", [0, -1, -1, 0, -1]},
            {"escalation", [0, -1, -1, -1, -1]},
            {"torque", [-1, 0, -1, -1, -1]},
            {"tangle_mayhem", [0, -1, -1, 0, -1]},
            {"stratosphere", [-1, 0, 0, 0, -1]}
        };

        public static int finalLevel = 0;
        public static int bonusArcLevel = 0;

        public static int medalTypes = 0;
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