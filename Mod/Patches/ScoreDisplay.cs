using HarmonyLib;

namespace ArchipelagoMIUU.Patches
{
    //Modify score display to show tracker.
    [HarmonyPatch(typeof(ScoreDisplay), "Setup")]
    class ScoreDisplay_Setup_Patch
    {
        public static void Postfix(ScoreDisplay __instance, HighScorePanel.HighScore score)
        {
            __instance.DiamondEffect.Stop();
            __instance.numText.text = "";
            __instance.scoreText.text = "";
            if (score.username == "No items required")
            {
                __instance.img.enabled = false;
            }
            else
            {
                __instance.img.enabled = true;
                __instance.img.sprite = ItemHandler.powerupFlags[score.username] ? Notification.instance.FoundEgg : Notification.instance.Egg;
            }
        }
    }
}
