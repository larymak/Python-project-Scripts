import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Keep in check!",
            message = "You need to drink water!\nTake your time"+
            " and drink your glass of water\nThe Nation Academies of Sciences, Engineering, and Medicine say:"+
            " 'you need drink about 15.5 cups (3.7 liters)'",
            app_icon = "../images/glass.ico",
            timeout=10  
        )
        time.sleep(60*80)
