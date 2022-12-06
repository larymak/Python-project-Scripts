from datetime import datetime
import pytz
from pytz import UnknownTimeZoneError

# Get time zone name from user
user_entered_time_zone = input('Enter your time zone: ')


def get_current_time(time_zone_name):
    # It will get the time zone of the user location
    time_zone_name = pytz.timezone(time_zone_name)

    # Print the date and time in specified format
    current_time = datetime.now(time_zone_name)
    print(f"Current time in this timezone: {current_time.strftime('%Y:%m:%d %H:%M:%S %Z')}")


try:
    get_current_time(user_entered_time_zone)
except UnknownTimeZoneError:
    print('UnknownTimeZoneError... \nPlease try again with correct time zone.')
