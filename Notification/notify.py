from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

# Show notification when needed
toaster.show_toast("Notification!", "Alert! Yes", threaded=True,
                   icon_path=None, duration=3) # duration is in seconds

# To check if we have any active notification
# we will use 'toaster.notification_active()'
while toaster.notification_active():
    time.sleep(0.1)