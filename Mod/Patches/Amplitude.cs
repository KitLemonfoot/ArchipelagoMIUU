using HarmonyLib;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Stub Amplitude.
    [HarmonyPatch(typeof(Amplitude), "SendEvent")]
    class Amplitude_ReportReplay_Patch
    {
        public static bool Prefix()
        {
            MiscHandler.Log("Got an Amplitude request, denying enqueue.");
            return false;
        }
    }

}
