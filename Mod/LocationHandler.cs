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
        /// Bit:
        /// 1:  Super Jump
        /// 2:  Boost
        /// 4:  Feather Fall
        /// 8:  Gravity Surfaces
        /// 16: Bounce Surfaces
        /// 32: Blue Moving Platforms
        ///
        /// Index:
        /// 0: Needed for base completion
        /// 1: Needed for silver
        /// 2: Needed for gold
        /// 3: Needed for diamond
        public static Dictionary<string, int[]> internalLevelLogic = new Dictionary<string, int[]>()
        {
            {"learning_to_roll_update", [0, 0, 0, 0]},
            {"learning_to_turn_update", [0, 0, 0, 0]},
            {"bunny_slope", [0, 0, 0, 0]},
            {"learning_to_jump_update", [1, 1, 1, 1]},
            {"fsa_update", [0, 2, 2, 2]},
            {"treasure_update", [0, 0, 0, 0]},
            {"frosty_update", [0, 0, 0, 0]},
            {"roundbend", [8, 8, 8, 8]},
            {"leaf_on_the_wind", [0, 0, 4, 4]},
            {"duality_v2", [0, 0, 0, 0]},
            {"L2bounce", [16, 16, 16, 16]},
            {"greatWall", [0, 0, 0, 0]},
            {"carom_v2", [0, 0, 0, 0]},
            {"rush_hour", [0, 0, 0, 0]},
            {"otgw_update", [19, 19, 19, 19]},
            {"intothearctic_v2", [0, 0, 0, 0]},
            {"wave_pool_update", [0, 3, 3, 3]},
            {"bigeasy", [0, 0, 0, 0]},
            {"transit_mayhem", [32, 32, 32, 32]},
            {"gravityknot_v2", [8, 8, 8, 8]},
            {"steppingstones_update", [43, 43, 43, 43]},
            {"speedball_v2", [0, 0, 0, 0]},
            {"mountmarblius_v2", [16, 16, 16, 16]},
            {"transmission_v2", [32, 32, 32, 32]},
            {"archipelago", [4, 4, 4, 4]},
            {"sugarRush", [2, 2, 2, 2]},
            {"slalom_v2", [32, 32, 32, 32]},
            {"outskirts", [0, 0, 0, 0]},
            {"offkilter", [8, 8, 8, 8]},
            {"icyascent", [34, 34, 34, 34]},
            {"badcompany_v2", [32, 32, 32, 32]},
            {"tubular", [4, 4, 4, 4]},
            {"overclocked_update", [32, 32, 32, 32]},
            {"tether", [8, 8, 8, 8]},
            {"aqueduct", [0, 0, 0, 0]},
            {"ricochet_v2", [18, 18, 18, 18]},
            {"braid_update", [18, 18, 18, 18]},
            {"sun_spire", [32, 32, 32, 32]},
            {"thunderdrome", [2, 2, 2, 2]},
            {"hyperloop", [0, 2, 2, 2]},
            {"gearing_up", [0, 0, 0, 0]},
            {"acrophobia", [0, 0, 0, 0]},
            {"rime", [0, 0, 0, 0]},
            {"cogValley", [0, 0, 0, 0]},
            {"citadel", [35, 35, 35, 35]},
            {"newtonscradle", [0, 0, 0, 0]},
            {"exmachina", [4, 4, 4, 4]},
            {"gearheart", [0, 0, 0, 0]},
            {"kleinsche", [8, 8, 8, 8]},
            {"direstraits", [1, 1, 1, 1]},
            {"diamond", [0, 0, 0, 0]},
            {"glacier_v2", [0, 2, 2, 2]},
            {"shift", [0, 0, 0, 0]},
            {"conduit_v2", [18, 18, 18, 18]},
            {"flip_the_table_v2", [8, 8, 8, 8]},
            {"energy_v2", [17, 17, 17, 17]},
            {"mobiusmadness_v2", [10, 10, 10, 10]},
            {"amethyst_v2", [0, 0, 0, 0]},
            {"rondure", [8, 8, 8, 8]},
            {"isaacs_apple", [0, 0, 0, 0]},
            {"penrosepass", [8, 8, 8, 8]},
            {"siege", [7, 7, 7, 7]},
            {"flywheel_v2", [2, 2, 2, 2]},
            {"symbiosis", [32, 32, 32, 32]},
            {"tesseract", [8, 8, 8, 8]},
            {"leapsandbounds_v2", [33, 33, 33, 33]},
            {"vertigo_mayhem", [0, 0, 0, 0]},
            {"tossedabout_v2", [20, 20, 20, 20]},
            {"apogee_v2", [31, 31, 31, 31]},
            {"rosenbridge_update", [0, 0, 0, 0]},
            {"onward_and_upward_mayhem", [9, 11, 11, 11]},
            {"permutation", [16, 16, 16, 16]},
            {"elevatoraction", [0, 0, 0, 0]},
            {"timecapsule", [8, 8, 8, 8]},
            {"3divide", [0, 3, 3, 3]},
            {"4stairs", [1, 1, 1, 1]},
            {"need_for_speed", [2, 2, 2, 2]},
            {"rivervantage", [3, 3, 3, 3]},
            {"gravitycube_update", [25, 25, 25, 25]},
            {"epoch", [0, 2, 2, 2]},
            {"platinum_playground_mayhem", [2, 2, 2, 2]},
            {"ribbon_v2", [8, 8, 8, 8]},
            {"castlechaos", [16, 16, 16, 16]},
            {"threadNeedle", [43, 43, 43, 43]},
            {"gordian_mayhem", [9, 9, 9, 9]},
            {"bumperinvasion", [0, 0, 0, 0]},
            {"bash_tion", [7, 7, 7, 7]},
            {"runout", [0, 0, 0, 0]},
            {"archiarchy", [36, 36, 36, 36]},
            {"crystalmatrix", [0, 3, 3, 3]},
            {"stayinalive_mayhem", [32, 32, 32, 32]},
            {"machinations_update", [1, 1, 1, 1]},
            {"pitofdespair", [1, 1, 1, 1]},
            {"contraption", [0, 0, 0, 0]},
            {"uphill", [11, 11, 11, 11]},
            {"retro", [0, 2, 2, 2]},
            {"warpcore", [8, 8, 8, 8]},
            {"bash_faster", [2, 2, 2, 2]},
            {"prime_v2", [0, 0, 0, 0]},
            {"halfpipeheaven_v2", [2, 2, 2, 2]},
            {"wanderlust_v2", [9, 9, 9, 9]},
            {"boomerang", [16, 16, 16, 16]},
            {"kendama", [2, 2, 2, 2]},
            {"cirrus_update", [44, 44, 44, 44]},
            {"zenith", [49, 49, 49, 49]},
            {"alldownhill", [8, 8, 8, 8]},
            {"dangerzone", [9, 9, 9, 9]},
            {"olympus", [0, 0, 0, 0]},
            {"headintheclouds_mayhem", [0, 0, 0, 0]},
            {"centripitalforce", [0, 0, 0, 0]},
            {"slickshtick", [0, 0, 0, 0]},
            {"network", [9, 9, 9, 9]},
            {"radius", [9, 9, 9, 9]},
            {"escalation", [33, 33, 33, 33]},
            {"torque", [2, 2, 2, 2]},
            {"tangle_mayhem", [9, 9, 9, 9]},
            {"stratosphere", [46, 46, 46, 46]},
        };

        public static int finalLevel = 0;
        public static int bonusArcLevel = 0;

        public static int medalTypes = 0;

        public static bool treasureboxsanity = false;
        public static string[] endLocations = {"overclocked_update", "citadel", "mobiusmadness_v2", "apogee_v2"};
        public static Action<bool> s => SentCheck;

        public static void CheckLocation(string loc)
        {
            if(locations.ContainsKey(loc) && ConnectHandler.Authenticated){
                if (ConnectHandler.Session.Locations.AllLocationsChecked.Contains(locations[loc]))
                {
                    return;
                }
				MiscHandler.Log("Checking location: "+loc);
				ConnectHandler.Session.Locations.CompleteLocationChecksAsync(locations[loc]);
                //Send notification.
                if (Notification.instance != null)
                {
                    string message = "";
                    if(scoutedLocations[locations[loc]].Player.Name != ConnectHandler.APSlot)
                    {
                        message = "Sent " + MiscHandler.getItemColor(scoutedLocations[locations[loc]].Flags) + scoutedLocations[locations[loc]].ItemName + "</color> to " + scoutedLocations[locations[loc]].Player.Name;
                        Notification.Notify(message, "Archipelago", 4f, Assets.APIcon);
                    }
                }

			}
			else MiscHandler.Log("Location \"" + loc + "\" does not exist or you are not connected to AP.");
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
