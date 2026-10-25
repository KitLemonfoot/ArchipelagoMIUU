namespace ArchipelagoMIUU
{
    public class UpdateHandler : IUpdateManagerItem
    {
        public static UpdateHandler instance;

        public static void Init()
        {
            if (instance == null)
                instance = new UpdateHandler();

            UpdateManager.Add(instance);
        }

        public void ManagedUpdate()
        {
            HandleDisconnect();
        }

        public void HandleDisconnect()
        {
            if (MiscHandler.justDisconnected)
            {
                MiscHandler.SetConnectString("Not connected to Archipelago");
                ConnectHandler.Authenticated = false;
                ConnectHandler.ConnectInitFinished = false;
                ConnectHandler.ClearSession();
                PausePanel.ExitToMainMenuImmediate(true);
                Notification.Notify("Disconnected from Archipelago Server.", "Disconnected", icon: Assets.APIcon);
                MiscHandler.justDisconnected = false;
            }
        }
    }
}
