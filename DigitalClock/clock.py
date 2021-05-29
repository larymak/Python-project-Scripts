from tkinter import *
import time

root = Tk()
root.title('My Clock')

def counttime(time1=''):
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
        clock.after(200, counttime)

clock = Label(root, font=('Poppins', 50, 'bold'), background='blue', foreground='white')
clock.pack(anchor='center')

counttime()
mainloop()