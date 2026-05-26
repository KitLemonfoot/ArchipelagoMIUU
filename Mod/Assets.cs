using System;
using System.IO;
using System.Reflection;
using UnityEngine;

namespace ArchipelagoMIUU;

public static class Assets
{
    public static Sprite APIcon;

    public static void LoadAPIcon()
    {
        try
        {
            var iconData = File.ReadAllBytes(Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "Archipelago.png"));
            Texture2D iconTexture = new(2,2,TextureFormat.RGBA32, false);
            ImageConversion.LoadImage(iconTexture, iconData);
            APIcon = Sprite.Create(iconTexture, new(0, 0, iconTexture.width, iconTexture.height), new());
        }
        catch (Exception e)
        {
            MiscHandler.Log("Could not load APIcon! " + e);
        }
    }
}
