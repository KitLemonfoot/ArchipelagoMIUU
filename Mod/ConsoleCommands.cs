using System;
using System.Collections.Generic;
using MIU;

namespace ArchipelagoMIUU
{
    internal class ConsoleCommands
    {
        [ConsoleCommand(description = "Connects to an Archipelago server", paramsDescription = "[ip:port, name, optional password]")]
        public static string apConnect(params string[] args)
        {
            if (args.Length < 2 || args.Length > 3)
                return "Please provide exactly 2 or 3 arguments.\n\nUsage:\n  apConnect address:port slotName [password]\n\nExamples:\n\n  apConnect archipelago.gg:12345 MyUsername\n  apConnect localhost:38281 MyUsername password123";

            MiscHandler.config_APip = args[0];
            MiscHandler.config_APslot = args[1];
            MiscHandler.config_APpassword = args.Length > 2 ? args[2] : "";
            MIU.Console.print("Attempting to connect to Archipelago server:");
            MIU.Console.print("Address and port: " + MiscHandler.config_APip);
            MIU.Console.print("Slot name: " + MiscHandler.config_APslot);
            MIU.Console.print("Password: " + (MiscHandler.config_APpassword != "" ? MiscHandler.config_APpassword : "(none)"));
            MIU.Console.print("Death link override: " + MiscHandler.config_overrideDL);
            MIU.Console.print("Death link amnesty override: " + MiscHandler.config_overrideDLAmnesty);
            ConnectHandler.ConnectToAP();
            return "";
        }

        [ConsoleCommand(description = "Override your YAML's Death Link setting", paramsDescription = "-1: no override, 0: disabled, 1: enabled")]
        public static string apOverrideDl(params string[] args)
        {
            string usage = "Possible values:\n  -1: No override\n   0: Disable\n   1: Enable";
            if (args.Length < 1)
            {
                string output = "";
                if (ConnectHandler.Authenticated)
                    output += "YAML value: " + ConnectHandler.doingDeathlinkYaml + "\n";
                if (MiscHandler.config_overrideDL == -1)
                    output += "Override:   -\n";
                else
                    output += "Override:   " + (MiscHandler.config_overrideDL == 1) + "\n";
                output += usage;
                return output;
            }
            if (!ConnectHandler.Authenticated)
            {
                return "You are not currently connected to an Archipelago server.";
            }

            switch (args[0])
            {
                case "-1":
                    MiscHandler.config_overrideDL = -1;
                    ConnectHandler.doingDeathlink = ConnectHandler.doingDeathlinkYaml;
                    ConnectHandler.updateDeathLinkStatus();
                    return "Death Link override is disabled";
                case "0":
                    MiscHandler.config_overrideDL = 0;
                    ConnectHandler.doingDeathlink = false;
                    ConnectHandler.updateDeathLinkStatus();
                    return "Death Link is now overridden to disabled";
                case "1":
                    MiscHandler.config_overrideDL = 1;
                    ConnectHandler.doingDeathlink = true;
                    ConnectHandler.updateDeathLinkStatus();
                    return "Death Link is now overridden to ENABLED";
                default:
                    return "Unknown value " + args[0] + "\n" + usage;
            }
        }

        [ConsoleCommand(description = "Override your YAML's Death Link Amnesty setting", paramsDescription = "[-1: no override, 1-20: override]")]
        public static string apOverrideDlAmnesty(params string[] args)
        {
            string usage = "Possible values:\n  -1: No override\n  1-20: Override to that many deaths";
            if (args.Length < 1)
            {
                string output = "";
                if (ConnectHandler.Authenticated)
                    output += "YAML value: " + ConnectHandler.deathAmnestyMaxYaml + "\n";
                if (MiscHandler.config_overrideDLAmnesty == -1)
                    output += "Override:   -\n";
                else
                    output += "Override:   " + MiscHandler.config_overrideDLAmnesty + "\n";
                output += usage;
                return output;
            }

            bool success = Int32.TryParse(args[0], out int value);
            if (!success || value < -1 || value == 0 || value > 20)
                return "Invalid value " + args[0] + "\n" + usage;

            MiscHandler.config_overrideDLAmnesty = value;

            if (value == -1)
            {
                ConnectHandler.deathAmnestyMax = ConnectHandler.deathAmnestyMaxYaml;
                return "Death Link Amnesty override is disabled";
            }

            ConnectHandler.deathAmnestyMax = value;
            return "Death Link Amnesty is now " + value;
        }

        [ConsoleCommand(description = "Enables or disables various AP elements when not connected to an Archipelago server", paramsDescription = "[\"element\"]")]
        public static string apToggleElement(params string[] args)
        {
            if (ConnectHandler.Authenticated)
            {
                return "You may not use this command at this time as you are currently connected to an Archipelago server.";
            }
            if (args.Length < 1)
            {
                string output = "Current values: \n";
                foreach(KeyValuePair<string, bool> kvp in ItemHandler.powerupFlags)
                {
                    output+= kvp.Key + ": " + kvp.Value.ToString() + "\n";
                }
                return output;
            }
            string element = args[0];
            if (!ItemHandler.powerupFlags.ContainsKey(element))
            {
                return "Item " + element + " is not a valid MIUU item.";
            }
            ItemHandler.powerupFlags[element] = !ItemHandler.powerupFlags[element];
            return "Element " + element + " availability has been set to " + ItemHandler.powerupFlags[element].ToString();
            
        }
    }
}
