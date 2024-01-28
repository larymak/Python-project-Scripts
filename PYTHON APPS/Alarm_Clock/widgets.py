from frame_alarm import AlarmsFrame
from ttkbootstrap.scrolled import ScrolledFrame
import ttkbootstrap as ttk
import time


class ClockFrame(ttk.Frame):
    def __init__(self, parent, ):
        super().__init__(master = parent)
        # layout
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')
        
        # set data
        self.time_string = ttk.StringVar()
        self.date_string = ttk.StringVar()
        
        # start the clock
        
        self.update_time()
        
        # set set style
        self.style = ttk.Style()
        self.style.configure(
                style = 'Time.TLabel',
                font = ('Helvetica', 30, 'bold'),
                anchor = 'center'
                )
        
        self.style.configure(
                style = 'Data.TLabel',
                font = ('Helvetica', 30, 'bold'),
                anchor = 'center'
                )
        
        # set widgets
        
        self.label_time = ttk.Label(
                master = self,
                textvariable = self.time_string,
                style = 'Time.TLabel'
                )
        
        self.label_date = ttk.Label(
                master = self,
                textvariable = self.date_string,
                style = 'Data.TLabel'
                )
        
        # set layout
        
        self.label_time.grid(
                row = 0,
                column = 0,
                columnspan = 2,
                sticky = 'ns'
                )
        self.label_date.grid(
                row = 1,
                column = 0,
                columnspan = 2,
                sticky = 'n'
                )
    
    def update_time(self):
        # set time and date format
        
        time_format = "%H:%M:%S"
        date_format = "%a %B %d"
        
        # update the time for every 1 second(using a recursion func)
        
        self.time_string.set(time.strftime(time_format))
        self.after(1000, self.update_time)
        self.date_string.set(time.strftime(date_format))


class AlarmClockPanel(ScrolledFrame):
    def __init__(self, parent):
        super().__init__(master = parent)
    
    @staticmethod
    def add_alarm(alarm) -> None:
        """
        Add the alarm to be show on the panel
        """
        alarm.pack(fill = 'both', expand = True)


class AddAlarmClock(ttk.Frame):
    def __init__(self, parent, button_function):
        super().__init__(master = parent)
        
        # button
        self.button = ttk.Button(
                master = self,
                text = '+',
                command = button_function,
                style = 'Alarm.TButton',
                )
        self.button.pack(expand = True, fill = 'both')
