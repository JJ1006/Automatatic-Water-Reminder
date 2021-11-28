import time
from plyer import notification
if __name__ == '__main__':
    notification.notify(
        title="Please Drink Water",
        message="It is very much important for your health.",
        app_icon="D:\Visual Studio Code\python projects\Automatatic-Water-Reminder\icon.ico",
        timeout=10
    )
    # time.sleep(60*60)