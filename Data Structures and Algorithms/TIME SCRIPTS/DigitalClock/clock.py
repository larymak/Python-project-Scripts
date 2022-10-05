# import GUI library - Tkinter
import tkinter as tk
import time
import random


class Clock:
    colors = ['red', 'blue', 'green', 'black', 'orange', 'purple', 'brown', 'yellow', 'pink']

    def __init__(self):
        # instance of Tkinter window
        self.master = tk.Tk()
        self.color = random.choice(Clock.colors)

    def settings(self):
        # Label the window to "My Clock"
        self.master.title('My Clock')

    def widgets(self):
        # Time calculation
        def count_time(time1=''):
            time2 = time.strftime('%H:%M:%S')
            if time2 != time1:
                time1 = time2
                clock.config(text=time2)
                clock.after(200, count_time)
        # Create the clock text
        clock = tk.Label(self.master, font=('Poppins', 50, 'bold'), background=self.color, foreground='white')
        clock.pack(anchor='center')
        # Clock loop
        count_time()
        tk.mainloop()


if __name__ == '__main__':
    my_clock = Clock()
    my_clock.settings()
    my_clock.widgets()
