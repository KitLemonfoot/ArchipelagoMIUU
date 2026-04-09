using HarmonyLib;

namespace ArchipelagoMIUU.Patches
{
    //Connect to AP on startup.
    [HarmonyPatch(typeof(USplashScreen), "Start")]
    class USplashScreen_Start_Patch
    {
        public static bool Prefix()
        {
            ConnectHandler.ConnectToAP();
            return true;
        }
    }

}