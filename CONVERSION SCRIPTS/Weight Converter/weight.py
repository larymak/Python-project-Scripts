#A simple gui script to convert weight in different measurement units

#modules
import tkinter
from tkinter import Label, StringVar, Entry, Text, Button, END


#initialize window

main = tkinter.Tk()
main.title("WeightTable")
main.resizable(0, 0)
main.configure(bg='#0492C2')


def val_kg():
    #kilograms to grams
    gram = float(e2_value.get()) * 1000
    #kilograms to pound
    pound = float(e2_value.get()) * 2.20462
    #kilograms to ounce
    ounce = float(e2_value.get()) * 35.274

    #converted text to text widget
    t1.delete("1.0", END)
    t1.insert(END, gram)

    t2.delete("1.0", END)
    t2.insert(END, pound)

    t3.delete("1.0", END)
    t3.insert(END, ounce)

#label widgets
e1 = Label(main, text="Enter Weight In Kilograms")
e2_value = StringVar()
e2 = Entry(main, textvariable=e2_value)
e3 = Label(main, text="Gram")
e4 = Label(main, text="Pound")
e5 = Label(main, text="Ounce")

#Text Widgets

t1 = Text(main, height=1, width=20)
t2 = Text(main, height=1, width=20)
t3 = Text(main, height=1, width=20)

#Convert Button
convert_btn = Button(main, text='Covert', command=val_kg)

#geometry specifiers; grid method.

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
convert_btn.grid(row=0, column=2)

#run main

main.mainloop()
