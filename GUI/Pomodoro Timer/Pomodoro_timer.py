import tkinter as Tk
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import messagebox
from pygame import mixer

# window geometry
HEIGTH = 700
WIDTH = 500

# palette
BUTTON_GRAPHIC = {
        'bd': 4,
        'fg': '#F0F8FF',
        'bg': 'red',
        'font': ('arial', 13),
        'width': 2,
        'height': 2,
        'relief': 'flat',
        'activebackground': 'green'
        }

WINDOW_COLOR = {'bg': 'black'}

class PomodoroTimer:

    tot_seconds = 50 * 60
    
    def __init__(self, window):
        mixer.init()
        self.window = window
        self.stop = False
        self.start = False
        self.window.title('Hocus pocus keep tha focus!')
        self.window.geometry(f"{HEIGTH}x{WIDTH}")
        self.window.configure(**WINDOW_COLOR)
        self.sound = mixer.Sound('Success.wav')

    # method containing the main logic
    def start_timer(self):
        self.start = True
        if self.start and not self.stop:
            if self.tot_seconds > 0:
                minute, seconds = divmod(self.tot_seconds, 60)
                self.min_.set(f"{minute:02d}")
                self.sec.set(f"{seconds:02d}")  
                self.tot_seconds -= 1
                self.start_button.config(state=Tk.DISABLED)
            self.window.after(1000, self.start_timer)

        elif self.stop_timer:
            self.start = True
            self.stop = False
            self.start_button.config(state=Tk.NORMAL)

        elif self.reset_timer:
            self.start_timer()
        
        if self.tot_seconds == 0:
            self.stop = True
            self.break_time()
    
    def break_time(self):
        self.start = False
        self.tot_seconds = 50 * 60
        self.sound.play(1)
        messagebox.showinfo(title='Pause', message='Time to take a 10 minutes break!')

    def stop_timer(self):
       if self.start and not self.stop:
        self.start = False
        self.stop = True

    def reset_timer(self): 
        self.stop = True 
        self.min_.set('50')
        self.sec.set('00')
        self.tot_seconds = 50 * 60

    def main(self):

        self.min_ = StringVar()
        self.sec = StringVar()
        self.min_.set('50')
        self.sec.set('00')

        # main buttons - START, RESET, STOP
        self.start_button = Button(self.window, text='START', padx=30, pady=20, **BUTTON_GRAPHIC, command=self.start_timer)
        self.reset_button = Button(self.window, text='RESET', padx=30, pady=20, **BUTTON_GRAPHIC, command=self.reset_timer)
        self.stop_button = Button(self.window, text='STOP', padx=30, pady=20, **BUTTON_GRAPHIC, command=self.stop_timer)

        # display
        self.set_minute_display = Label(self.window, textvariable=self.min_, font=('bold', 30)).place(x=100, y=120, width=200, height=100)
        self.set_seconds_display = Label(self.window, textvariable=self.sec, font=('bold', 30)).place(x=400, y=120, width=200, height=100) 

        # buttons placement
        self.start_button.place(x=300, y=390)
        self.reset_button.place(x=200, y=390)
        self.stop_button.place(x=400, y=390)

        # initialize window
        self.window.mainloop()

# Main driver
if __name__ == "__main__":
    timer = PomodoroTimer(Tk.Tk())
    timer.main()
