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
		public static int deathAmnesty = 0;
		public static int deathAmnestyMax = 15;
		public static DeathLinkService deathLinkService = null;

        public static void ConnectToAP(){
			Debug.Log("Trying to connect to AP. Please wait...");
			LoginResult result;
			APSlot = MiscHandler.config_APslot.Value;
			APserver = MiscHandler.config_APip.Value;
			
			try{
				Session = ArchipelagoSessionFactory.CreateSession(APserver);
				
				result = Session.TryConnectAndLogin(
					"Marble It Up! Ultra", 
					APSlot, 
					ItemsHandlingFlags.AllItems,
					new Version(0,6,7),
					null,
					null,
					MiscHandler.config_APpassword.Value == "" ? null : MiscHandler.config_APpassword.Value,
					true
				);
			}
			catch (Exception e){
				result = new LoginFailure(e.GetBaseException().Message);
			}
			if (result is LoginSuccessful loginSuccess)
			{
				Debug.Log("Successfully connected to server, setting up...");
				Authenticated = true;
				
				Session.Items.ItemReceived += ItemReceived;

				//Push locations
				LocationHandler.locations = ((JObject)loginSuccess.SlotData["locations"]).ToObject<Dictionary<string, long>>();
				long[] ids = (new List<long>(LocationHandler.locations.Values)).ToArray();

				//Scout locations
				Debug.Log("Scouting locations...");
				Task<Dictionary<long, ScoutedItemInfo>> scoutTask = ConnectHandler.Session.Locations.ScoutLocationsAsync(ids);
                scoutTask.Wait();
                LocationHandler.scoutedLocations = scoutTask.Result;

				//Get YAML settings.
				LocationHandler.finalLevel = int.Parse(loginSuccess.SlotData["FinalChapter"].ToString());
				LocationHandler.bonusArcLevel = int.Parse(loginSuccess.SlotData["BonusArcChapters"].ToString());
				ItemHandler.medalsPerChapter = int.Parse(loginSuccess.SlotData["MedalsPerChapter"].ToString());

				//Setup deathlink
				doingDeathlink = bool.Parse(loginSuccess.SlotData["death_link"].ToString());
				deathAmnesty = 0;
				deathAmnestyMax = int.Parse(loginSuccess.SlotData["death_link_amnesty"].ToString());
				deathLinkService = Session.CreateDeathLinkService();
				if(MiscHandler.config_overrideDL.Value != -1)
				{
					doingDeathlink = MiscHandler.config_overrideDL.Value>=1;
					Debug.Log("DL overwritten with "+doingDeathlink);
				}
				if(MiscHandler.config_overrideDLAmnesty.Value > 0)
				{
					deathAmnestyMax = Math.Min(20, MiscHandler.config_overrideDLAmnesty.Value);
					Debug.Log("DL amnesty overwritten with "+deathAmnestyMax);
				}

				if (doingDeathlink)
				{
					deathLinkService.EnableDeathLink();
					deathLinkService.OnDeathLinkReceived += DeathLinkRecieved;
				}

				MiscHandler.connectString = "Connected to "+APserver;
				ItemHandler.calculateRequiredMedals();

				Debug.Log("Successfully set up a connection to Archipelago. Let's play!");
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
				Debug.Log(errorMessage);
				Session = null;
				return;
			}
        }

        public static void ItemReceived(IReceivedItemsHelper helper){
			ItemInfo item = helper.PeekItem();
			string name = item.ItemName;
			string sender = item.Player.Name;
			Debug.Log("Got item from AP: "+name);
			ItemHandler.recieveItem(name, sender);
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

		public static void sendDeathLink(){
			string msg = APSlot + " fell out of bounds.";
			deathLinkService.SendDeathLink(new DeathLink(ConnectHandler.APSlot, msg));
			Debug.Log("Deathlink sent");
		}

        public static void SendCompletion()
        {
            Session?.SetGoalAchieved();
			Action acceptAction = delegate{};
            ConfirmationWindow.instance.Open("Congratulations!", "You've completed your goal.\n\nThank you for playing!", "OK", "", acceptAction);
        }
    }
}