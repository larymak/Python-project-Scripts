# import GUI library - Tkinter
from tkinter import *
import time

root = Tk()

# Label the window to "My Clock"
root.title('My Clock')

#Time calculation 
def counttime(time1=''):
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        clock.after(200, counttime)

# Create the clock text 
clock = Label(root, font=('Poppins', 50, 'bold'), background='blue', foreground='white')
clock.pack(anchor='center')

# Clock loop
counttime()
mainloop()