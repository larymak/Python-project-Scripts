from tkinter import *
from morse import MorseCode

# translate object
translate = MorseCode()

# --------------------------------BUTTON FUNCTIONS------------------------------
# Button function morse
def code():
    text = e.get().strip()
    print(text)
    e.delete(0, END)
    text = translate.to_morse(text)
    e.insert(0, text)

# Button function english
def decode():
    text = e.get().strip()
    print(text)
    e.delete(0, END)
    e.insert(0, translate.to_english(text))

# Button function clear
def on_clear():
    e.delete(0, END)

# -----------------------------------UI SETUP-----------------------------------
root = Tk()
root.title("Morse Code Converter")

# Entry field
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
e.focus()

code = Button(root, text="Code", command=code).grid(row=1, column=0)
clear = Button(root, text="Clear", command=on_clear).grid(row=1, column=1)
decode = Button(root, text="Decode", command=decode).grid(row=1, column=2)
exit = Button(root, text="EXIT", command=root.quit).grid(row=2, column=0, columnspan=3)

root.mainloop()