from threading import Thread, Event
from configuration import LIST_DAY
import ttkbootstrap as ttk
from backend_alarm import AlarmClock


def start_alarm(clock: str, event: Event, days: str) -> None:
    AlarmClock(clock = clock, event = event, days = days).start_alarm()


class AlarmsFrame(ttk.Frame):
    def __init__(self, parent, text):
        super().__init__(master = parent, )
        
        # set style
        self.style = ttk.Style()
        # styling the delete button
        self.style.configure(
                style = 'Delete.TButton',
                background = '#e74c3c',
                anchor = 'center',
                font = ('Helvetica', 14, 'bold')
                )
        
        self.style.map(
                style = 'Delete.TButton',
                background = [('active', '#e74c3c')],
                bordercolor = '#e74c3c',
                )
        
        # styling the time label for the alarm
        self.style.configure(
                style = 'Alarm_Set.TLabel',
                anchor = 'center',
                font = ('Helvetica', 18, 'bold')
                )
        
        # set grid layout
        self.event = Event()
        self.rowconfigure((0, 1), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(0, 7)), weight = 1, uniform = 'a')
        
        #  set data
        self.day_label = list(range(7))
        self.days_on = list()
        self.time_str = text
        self.variable_checkbutton = ttk.BooleanVar()
        
        # set widgets
        self.time_label = ttk.Label(
                style = 'Alarm_Set.TLabel',
                master = self,
                text = self.time_str,
                )
        
        self.checkbutton = ttk.Checkbutton(
                master = self,
                variable = self.variable_checkbutton,
                command = self.set_alarm
                )
        
        self.delete_button = ttk.Button(
                master = self,
                style = 'Delete.TButton',
                text = 'Delete',
                command = self.delete_alarm
                )
        
        # set layout
        self.time_label.grid(row = 0, column = 0, sticky = 'news')
        self.checkbutton.grid(row = 0, column = 5, sticky = 'nse')
        self.delete_button.grid(row = 0, column = 6, sticky = 'news')
        
        # add the layer of day
        for index, day in enumerate(LIST_DAY):
            self.day_label[index] = DayButton(
                    parent = self,
                    day_name = day,
                    row = 1,
                    column = index,
                    )
    
    def set_alarm(self):
        
        self.select_days()
        alarm_test = Thread(
                target = start_alarm,
                args = (self.time_str, self.event, self.days_on),
                daemon = True
                )
        
        if self.variable_checkbutton.get():
            self.event.clear()
            alarm_test.start()
        else:
            self.event.set()
    
    def delete_alarm(self):
        self.event.set()
        self.destroy()
    
    def select_days(self):
        
        self.days_on.clear()
        for i in range(7):
            if not self.day_label[i].state.get():
                self.days_on.append(self.day_label[i]['text'])


class DayButton(ttk.Label):
    
    def __init__(self, parent, day_name, row, column):
        self.style = ttk.Style()
        self.style.configure(
                style = 'Day.TLabel',
                font = ('Helvetica', 16),
                )
        super().__init__(
                master = parent,
                text = day_name,
                style = 'Day.TLabel',
                anchor = 'center',
                background = '#303030'
                )
        self.state = ttk.BooleanVar(value = True)
        self.grid(
                row = row,
                column = column,
                sticky = 'news',
                padx = 2,
                pady = 2
                )
        self.bind('<Enter>', self.enter_alarm)
        self.bind('<Leave>', self.leave_alarm)
        self.bind('<Button-1>', self.select_alarm)
    
    def enter_alarm(self, event = None):
        if self.state.get():
            self.configure(background = '#526170')
    
    def leave_alarm(self, event = None):
        if self.state.get():
            self.configure(background = '#303030')
    
    def select_alarm(self, event = None):
        if self.state.get():
            self.configure(background = '#00bc8c')
            self.state.set(False)
        else:
            self.configure(background = '#303030')
            self.state.set(True)
