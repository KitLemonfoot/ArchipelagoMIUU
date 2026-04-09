using HarmonyLib;
using MIU;
using UnityEngine;

namespace ArchipelagoMIUU.Patches
{
    //Handle bounce and gravity surfaces.
    [HarmonyPatch(typeof(MaterialFlags), "ApplyTriangleMaterial")]
    class MaterialFlags_ApplyTriangleMaterial_Patch
    {
        public static void Postfix(Material m, BumperController bumper, TriangleGrid.TriangleSurfaceData tri)
        {
            if (!ConnectHandler.Authenticated)
            {
                return;
            }
            if(tri.materialLabels.HasFlag(MaterialLabel.Bounce))
            {
                if(!ItemHandler.powerupFlags["Bounce Surfaces"])
                {
                    tri.materialLabels = MaterialLabel.None;
                    tri.restitution = 1f;
			        tri.force = 0f;
			        tri.friction = 1f;
			        tri.noBounceFx = true;
                }
            }
            if (tri.materialLabels.HasFlag(MaterialLabel.Gravity))
            {
                if(!ItemHandler.powerupFlags["Gravity Surfaces"])
                {
                    tri.materialLabels = MaterialLabel.None;
                    tri.localGravity = 0f;
                }
            }
        }
    }

}