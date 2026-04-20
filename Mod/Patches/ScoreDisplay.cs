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
            __instance.img.sprite = Notification.instance.Egg;
            if (ItemHandler.powerupFlags[score.username])
            {
                __instance.img.sprite = Notification.instance.FoundEgg;
            }
        }
    }
}