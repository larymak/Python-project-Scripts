from frame_alarm import AlarmsFrame
from configuration import TIME, DATE
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
        # Configure the style of time label
        self.style.configure(
                style = 'Time.TLabel',
                font = ('Helvetica', 30, 'bold'),
                anchor = 'center'
                )
        
        # Configure the style of time label
        self.style.configure(
                style = 'Data.TLabel',
                font = ('Helvetica', 30, 'bold'),
                anchor = 'center'
                )
        
        # Creating the widgets for the time and the date
        
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
                row = TIME['ROW'],
                column = TIME['COLUMN'],
                columnspan = TIME['SPAN'],
                sticky = TIME['STICKY']
                )
        self.label_date.grid(
                row = DATE['ROW'],
                column = DATE['COLUMN'],
                columnspan = DATE['SPAN'],
                sticky = DATE['STICKY']
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
        
        # set style for the button
        self.style = ttk.Style()
        self.style.configure(
                style = 'Alarm.TButton',
                font = ('Helvetica', 20, 'bold'),
                anchor = 'center'
                )
        
        # Create the button for adding alarms
        self.button = ttk.Button(
                master = self,
                text = '✚',
                command = button_function,
                style = 'Alarm.TButton',
                )
        # pack the button
        self.button.pack()
