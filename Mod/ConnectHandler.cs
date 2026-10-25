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
using System.Net.WebSockets;

namespace ArchipelagoMIUU
{
    public static class ConnectHandler
    {
        public static bool Authenticated;
        public static bool ConnectInitFinished;
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

			ItemHandler.wipeItems();
			ConnectInitFinished = false;

			try{
				Session = ArchipelagoSessionFactory.CreateSession(APserver);

				// Register handlers before connecting
				Session.Socket.ErrorReceived += HandleError;
				Session.Socket.SocketClosed += HandleSocketClosed;
				Session.Items.ItemReceived += HandleItemReceived;

				result = Session.TryConnectAndLogin(
					"Marble It Up! Ultra",
					APSlot,
					ItemsHandlingFlags.AllItems,
					version: new Version(0,6,7),
					password: MiscHandler.config_APpassword == "" ? null : MiscHandler.config_APpassword,
					requestSlotData: true
				);
			}
			catch (Exception e){
				result = new LoginFailure(e.GetBaseException().Message);
			}
			if (result is LoginSuccessful loginSuccess)
			{
				MiscHandler.Log("Successfully connected to server, setting up...");
				PausePanel.ExitToMainMenuImmediate(true);
				Authenticated = true;

				//Push locations
				LocationHandler.locations = ((JObject)loginSuccess.SlotData["locations"]).ToObject<Dictionary<string, long>>();
				long[] ids = (new List<long>(LocationHandler.locations.Values)).ToArray();

				//Scout locations
				MiscHandler.Log("Scouting locations...");
				Task<Dictionary<long, ScoutedItemInfo>> scoutTask = ConnectHandler.Session.Locations.ScoutLocationsAsync(ids);
                scoutTask.Wait();
                LocationHandler.scoutedLocations = scoutTask.Result;

				//Get final levels
				LocationHandler.finalLevels = ((JObject)loginSuccess.SlotData["finalLevels"]).ToObject<Dictionary<string, bool>>();

				//Get YAML settings.
				List<string> medals = ((JArray)loginSuccess.SlotData["MedalTypes"]).ToObject<List<string>>();
				LocationHandler.bronzeMedals = medals.Contains("Bronze");
				LocationHandler.silverMedals = medals.Contains("Silver");
				LocationHandler.goldMedals = medals.Contains("Gold");
				LocationHandler.diamondMedals = medals.Contains("Diamond");
				LocationHandler.goalArc = int.Parse(loginSuccess.SlotData["GoalArc"].ToString());
				LocationHandler.ultraArcChapters = int.Parse(loginSuccess.SlotData["UltraArcChapters"].ToString());
				LocationHandler.bonusArcChapters = int.Parse(loginSuccess.SlotData["BonusArcChapters"].ToString());
				ItemHandler.medalsPerChapter = int.Parse(loginSuccess.SlotData["MedalsPerChapter"].ToString());
				LocationHandler.treasureboxsanity = bool.Parse(loginSuccess.SlotData["Treasureboxsanity"].ToString());

				if (LocationHandler.diamondMedals)
					LocationHandler.highestMedalType = 3;
				else if (LocationHandler.goldMedals)
					LocationHandler.highestMedalType = 2;
				else if (LocationHandler.silverMedals)
					LocationHandler.highestMedalType = 1;
				else
					LocationHandler.highestMedalType = 0;

				if (LocationHandler.goalArc == 0)
					ItemHandler.bonusArcComplete = true;
				if (LocationHandler.goalArc == 1)
					ItemHandler.ultraArcComplete = true;

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

				deathLinkService.OnDeathLinkReceived += DeathLinkRecieved;
				updateDeathLinkStatus();

				MiscHandler.SetConnectString("Connected to " + APserver);
				ItemHandler.calculateRequiredMedals();

				MiscHandler.Log("Current Completion Medals: " + ItemHandler.completionMedals);
				MiscHandler.Log("Current Gold Completion Medals: " + ItemHandler.goldCompletionMedals);

				MiscHandler.Log("Successfully set up a connection to Archipelago. Let's play!");
				ConnectInitFinished = true;
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
				ClearSession();
				return;
			}
        }

		public static void updateDeathLinkStatus()
		{
			if (doingDeathlink)
			{
				deathLinkService.EnableDeathLink();
				return;
			}
			deathLinkService.DisableDeathLink();
		}

		public static void Disconnect()
		{
			if (Session != null && Session.Socket != null && Session.Socket.Connected)
				Session.Socket.DisconnectAsync();
		}

		public static void HandleError(Exception e, string message)
		{
			MiscHandler.Log($"Received error: {message}\n{e}");
			if (e is WebSocketException)
			{
				HandleSocketClosed(e.Message);
			}
		}

		public static void HandleSocketClosed(string reason)
		{
			if (!Authenticated)
				return;
			MiscHandler.Log("Socket closed" + (reason != "" ? ": " + reason : ""));
			MiscHandler.justDisconnected = true;
			Authenticated = false;
		}

		public static void HandleItemReceived(IReceivedItemsHelper helper)
		{
			while (helper.Any())
			{
				ItemInfo item = helper.DequeueItem();
				string name = item.ItemName;
				string sender = item.Player.Name;
				string colorData = MiscHandler.getItemColor(item.Flags);
				MiscHandler.Log("Got item from AP: " + name);
				ItemHandler.recieveItem(name, sender, colorData);
			}
		}

		public static void ClearSession()
		{
			if (Session != null)
			{
				Session.Socket.ErrorReceived -= HandleError;
				Session.Socket.SocketClosed -= HandleSocketClosed;
				Session.Items.ItemReceived -= HandleItemReceived;
				if (deathLinkService != null)
				{
					deathLinkService.OnDeathLinkReceived -= DeathLinkRecieved;
					deathLinkService = null;
				}
				Session = null;
			}
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
