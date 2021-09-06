# import GUI library - Tkinter
import tkinter as tk
import time

class Clock:
    def __init__(self):
        self.master = tk.Tk()

    def settings(self):
        # Label the window to "My Clock"
        self.master.title('My Clock')

    def widgets(self):
        #Time calculation
        def counttime(time1=''):
            time2 = time.strftime('%H:%M:%S')
            if time2 != time1:
                time1 = time2
                clock.config(text=time2)
                clock.after(200, counttime)
        # Create the clock text
        clock = tk.Label(self.master, font=('Poppins', 50, 'bold'), background='blue', foreground='white')
        clock.pack(anchor='center')
        # Clock loop
        counttime()
        tk.mainloop()

if __name__ == '__main__':
    my_clock = Clock()
    my_clock.settings()
    my_clock.widgets()
