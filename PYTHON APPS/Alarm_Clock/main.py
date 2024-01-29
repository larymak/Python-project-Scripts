from tkinter import IntVar

from toplevel import TopLevel
import ttkbootstrap as ttk
from configuration import (
    WIDTH, HEIGHT,
    ICON_PATH, TITLE_APP,
    THEME, CLOCK, BUTTON, PANEL,
    )
from widgets import (
    ClockFrame, AlarmClockPanel,
    AddAlarmClock, AlarmsFrame,
    )

# Import the libraries for changing the title bar color, it works only on windows :/
try:
    from ctypes import windll, byref, sizeof, c_int
except ImportError:
    pass


class App(ttk.Window):
    hour_int: IntVar
    minute_int: IntVar
    
    alarm_panel: AlarmClockPanel
    button_top_level: AddAlarmClock
    clock_frame: ClockFrame
    
    def __init__(self):
        super().__init__(themename = THEME)
        self.bind('<Alt-s>', lambda even: self.destroy())
        self.set_geometry(height = HEIGHT, width = WIDTH)
        self.title(TITLE_APP)
        self.set_icon(path_image = ICON_PATH)
        self.set_title_color()
        
        # set data
        
        self.hour_int = ttk.IntVar(value = 0)
        self.minute_int = ttk.IntVar(value = 0)
        self.top_level = None
        
        # create widgets
        self.clock_frame = ClockFrame(self)
        self.alarm_panel = AlarmClockPanel(parent = self)
        self.button_top_level = AddAlarmClock(parent = self, button_function = self.start_top_level)
        
        # set layout for widgets(place method)
        self.clock_frame.place(
                relx = CLOCK['X'],
                rely = CLOCK['Y'],
                relwidth = CLOCK['WIDTH'],
                relheight = CLOCK['HEIGHT'],
                anchor = 'nw'
                )
        self.alarm_panel.place(
                relx = PANEL['X'],
                rely = PANEL['Y'],
                relwidth = PANEL['WIDTH'],
                relheight = PANEL['HEIGHT'],
                anchor = 'nw',
                )
        self.button_top_level.place(
                relx = BUTTON['X'],
                rely = BUTTON['Y'],
                anchor = 'center'
                )
        
        # Set a model for the alarm :), you can eliminate if you don t like it
        # Start here
        alarm = AlarmsFrame(
                parent = self.alarm_panel,
                text = '12:00',
                )
        self.alarm_panel.add_alarm(alarm)
        # Stop here
        
        # run the window
        self.mainloop()
    
    def set_icon(self, path_image: str) -> None:
        try:
            self.iconbitmap(path_image)
        except Exception:
            pass
    
    def set_geometry(self, width: int, height: int) -> None:
        """
         It make the windows to be in the center of your desktop.
         The formula is down and you could found on the internet explained very well :)
        """
        desktop_height = self.winfo_screenheight()  # it take your desktop height
        desktop_width = self.winfo_screenwidth()  # it take your desktop width
        window_top = int((desktop_height - height) / 2)
        window_left = int((desktop_width - width) / 2)
        self.geometry(f'{width}x{height}+{window_left}+{window_top}')
    
    def set_title_color(self) -> None:
        try:
            HWND: int = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE: int = 35
            color: int = 0x00000000
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(color)), sizeof(c_int))
        
        except Exception:
            pass
    
    def start_top_level(self) -> None:
        """
        It show the windows to set your alarm
        """
        self.top_level = TopLevel(
                parent = self,
                hour_int = self.hour_int,
                minute_int = self.minute_int,
                ok_function = self.ok_button,
                cancel_function = self.cancel_button
                )
    
    def ok_button(self) -> None:
        """
        It take to input from the top level and paste the time of the alarm

        """
        if self.hour_int.get() or self.minute_int.get():
            
            hour, minute = self.hour_int.get(), self.minute_int.get()
            hour_str = str(hour) if hour >= 10 else f'0{hour}'
            minutes_str = str(minute) if minute >= 10 else f'0{minute}'
            
            text_label = f'{hour_str}:{minutes_str}'
            alarm_frame = AlarmsFrame(parent = self.alarm_panel, text = text_label)
            
            self.alarm_panel.add_alarm(alarm_frame)
            self.hour_int.set(value = 0)
            self.minute_int.set(value = 0)
            self.top_level.destroy()
    
    def cancel_button(self) -> None:
        
        self.hour_int.set(value = 0)
        self.minute_int.set(value = 0)
        self.top_level.destroy()


if __name__ == '__main__':
    App()
