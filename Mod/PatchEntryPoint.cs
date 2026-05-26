using HarmonyLib;
using UnityEngine.SceneManagement;

namespace ArchipelagoMIUU;

public static class PatchEntryPoint
{
    private static bool IsPatched = false;

    public static void Start()
    {
        SceneManager.sceneLoaded += BeginPatch;
    }

    private static void BeginPatch(Scene scene, LoadSceneMode mode)
    {
        if (!IsPatched)
        {
            IsPatched = true;
            SceneManager.sceneLoaded -= BeginPatch;
            new Harmony("archipelago").PatchAll();
            Assets.LoadAPIcon();
            MiscHandler.Log("Archipelago Loaded!");
        }
    }
}
