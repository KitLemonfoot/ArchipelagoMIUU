using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Packets;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.Models;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using UnityEngine;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using HarmonyLib;

namespace ArchipelagoMIUU
{
    public static class ConnectHandler
    {
        public static bool Authenticated;
        public static ArchipelagoSession Session;
        public static string APserver = null;
		public static string APSlot = null;
		public static bool doingDeathlink = false;
		public static bool doingDeathlinkYaml = false;
		public static int deathAmnesty = 0;
		public static int deathAmnestyMax = 15;
		public static int deathAmnestyMaxYaml = 15;
		public static DeathLinkService deathLinkService = null;

        public static void ConnectToAP(){
			MiscHandler.Log("Trying to connect to AP. Please wait...");
			LoginResult result;
			APSlot = MiscHandler.config_APslot;
			APserver = MiscHandler.config_APip;

			try{
				Session = ArchipelagoSessionFactory.CreateSession(APserver);

				result = Session.TryConnectAndLogin(
					"Marble It Up! Ultra",
					APSlot,
					ItemsHandlingFlags.AllItems,
					new Version(0,6,7),
					null,
					null,
					MiscHandler.config_APpassword == "" ? null : MiscHandler.config_APpassword,
					true
				);
			}
			catch (Exception e){
				result = new LoginFailure(e.GetBaseException().Message);
			}
			if (result is LoginSuccessful loginSuccess)
			{
				MiscHandler.Log("Successfully connected to server, setting up...");
				Authenticated = true;

				flushItems();
				Session.Items.ItemReceived += ItemReceived;

				//Push locations
				LocationHandler.locations = ((JObject)loginSuccess.SlotData["locations"]).ToObject<Dictionary<string, long>>();
				long[] ids = (new List<long>(LocationHandler.locations.Values)).ToArray();

				//Scout locations
				MiscHandler.Log("Scouting locations...");
				Task<Dictionary<long, ScoutedItemInfo>> scoutTask = ConnectHandler.Session.Locations.ScoutLocationsAsync(ids);
                scoutTask.Wait();
                LocationHandler.scoutedLocations = scoutTask.Result;

				//Get YAML settings.
				LocationHandler.medalTypes = int.Parse(loginSuccess.SlotData["MedalTypes"].ToString());
				LocationHandler.finalLevel = int.Parse(loginSuccess.SlotData["FinalChapter"].ToString());
				LocationHandler.bonusArcLevel = int.Parse(loginSuccess.SlotData["BonusArcChapters"].ToString());
				ItemHandler.medalsPerChapter = int.Parse(loginSuccess.SlotData["MedalsPerChapter"].ToString());
				LocationHandler.treasureboxsanity = bool.Parse(loginSuccess.SlotData["Treasureboxsanity"].ToString());

				//Setup deathlink
				doingDeathlinkYaml = bool.Parse(loginSuccess.SlotData["death_link"].ToString());
				doingDeathlink = doingDeathlinkYaml;
				deathAmnesty = 0;
				deathAmnestyMaxYaml = int.Parse(loginSuccess.SlotData["death_link_amnesty"].ToString());
				deathAmnestyMax = deathAmnestyMaxYaml;
				deathLinkService = Session.CreateDeathLinkService();
				if(MiscHandler.config_overrideDL != -1)
				{
					doingDeathlink = MiscHandler.config_overrideDL >= 1;
					MiscHandler.Log("DL overwritten with "+doingDeathlink);
				}
				if(MiscHandler.config_overrideDLAmnesty > 0)
				{
					deathAmnestyMax = Math.Min(20, MiscHandler.config_overrideDLAmnesty);
					MiscHandler.Log("DL amnesty overwritten with "+deathAmnestyMax);
				}

				if (doingDeathlink)
				{
					deathLinkService.EnableDeathLink();
					deathLinkService.OnDeathLinkReceived += DeathLinkRecieved;
				}

				MiscHandler.SetConnectString("Connected to " + APserver);
				ItemHandler.calculateRequiredMedals();

				MiscHandler.Log("Successfully set up a connection to Archipelago. Let's play!");
			}
            else if (result is LoginFailure failure)
			{
				string errorMessage = $"Failed to connect to Archipelago.\n";
				foreach (ConnectionRefusedError error in failure.ErrorCodes)
				{
					errorMessage += $"{error}: ";
				}
				foreach (string error in failure.Errors)
				{
					errorMessage += $"{error}";
				}
				MiscHandler.Log(errorMessage);
				MiscHandler.SetConnectString(errorMessage);
				Session = null;
				return;
			}
        }

		public static void flushItems()
		{
			MiscHandler.Log("Flushing items");
			while (Session.Items.Any())
			{
				ItemInfo item = Session.Items.PeekItem();
				string name = item.ItemName;
				ItemHandler.updateItem(name);
				Session.Items.DequeueItem();
			}
		}

        public static void ItemReceived(IReceivedItemsHelper helper){
			ItemInfo item = helper.PeekItem();
			string name = item.ItemName;
			string sender = item.Player.Name;
			string colorData = MiscHandler.getItemColor(item.Flags);
			MiscHandler.Log("Got item from AP: "+name);
			ItemHandler.recieveItem(name, sender, colorData);
			helper.DequeueItem();
		}

		public static void DeathLinkRecieved(DeathLink deathLink)
		{
			string message = deathLink.Source + " ";
			if(deathLink.Cause == null)
			{
				message += "died.";
			}
			else
			{
				message += deathLink.Cause;
			}
			Notification.Notify(message, "Death Link", 3f);
			MiscHandler.killMarbles();
		}

		public static void sendDeathLink(int reason){
			string msg;
			switch (reason)
			{
				case 0: msg = APSlot + " fell out of bounds.";break;
				case 1: msg = APSlot + " was crushed.";break;
				default: msg = APSlot + " died for unknown reasons.";break;
			}
			deathLinkService.SendDeathLink(new DeathLink(ConnectHandler.APSlot, msg));
			MiscHandler.Log("Deathlink sent");
		}

        public static void SendCompletion()
        {
            Session?.SetGoalAchieved();
			Action acceptAction = delegate{};
            ConfirmationWindow.instance.Open("Congratulations!", "You've completed your goal.\n\nThank you for playing!", "OK", "", acceptAction);
        }
    }
}
