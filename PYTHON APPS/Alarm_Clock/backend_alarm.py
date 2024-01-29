import time
from datetime import datetime
from threading import Event
from typing import List
from configuration import TIME_RELAPSE, TIME_SPEED
from pygame import mixer

mixer.init()
sound = mixer.Sound('media/sound/alarm.mp3')


def get_date_now() -> int:
    time_now: datetime = datetime.now()
    current_hour: int = time_now.hour
    current_minutes: int = time_now.minute
    current_seconds: int = time_now.second
    current_time: int = 3600 * current_hour + 60 * current_minutes + current_seconds
    
    return current_time


class AlarmClock:
    total_time: int
    days: List[str:]
    event: Event
    clock: str
    
    def __init__(self, clock, event, days):
        self.clock = clock
        self.event = event
        self.days = days
        self.total_time = self.user_time()
        
        self.start_alarm()
    
    def user_time(self) -> int:
        """
        It take the user time and it change to seconds
        """
        user_hour_minutes = self.clock.split(':')
        hour = int(user_hour_minutes[0])
        minutes = int(user_hour_minutes[1])
        
        return 3600 * hour + 60 * minutes
    
    def check_day(self) -> None:
        """
        It check the self.days if a item from the list is the current day it will remove

        """
        initial_day = time.strftime('%a')
        for day in self.days:
            if day == initial_day:
                self.days.remove(day)
    
    def counter_timer(self) -> None:
        """
        It counts the seconds for the alarm, if the alarm is done it will start again after 60 seconds to check for
        other alarm

        """
        current_time = get_date_now()
        if current_time == self.total_time:
            sound.play()  # It start the alarm sound
            time.sleep(TIME_RELAPSE)
            self.start_alarm()
        else:
            time.sleep(TIME_SPEED)
    
    def start_alarm(self) -> None:
        while not self.event.is_set():
            if len(self.days) == 0:
                break
            else:
                self.check_day()
                while not self.event.is_set():
                    self.counter_timer()
