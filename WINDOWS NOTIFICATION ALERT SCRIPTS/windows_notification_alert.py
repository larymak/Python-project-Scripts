from plyer import notification
import time

if __name__ == "__main__":

    try:
        message = "NOTIFICATION"
        title = "SET UP YOU TIME"
        while True:
            notification.notify(title=title, message=message, timeout=10)
            time.sleep(3600)
    except KeyboardInterrupt:
        print("Keyboard Interrupt the Program")
