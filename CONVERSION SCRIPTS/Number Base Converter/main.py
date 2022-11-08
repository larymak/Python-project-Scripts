from tobinary import decimalToBinary, octalToBinary, hexToBinary
from tooctal import decimalToOctal, binaryToOctal, hexToOctal
from tohex import decimalToHex, binaryToHex, octalToHex
from todecimal import binaryToDecimal, octalToDecimal, hexToDecimal

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Number Base Conversion")
root.state('zoomed')
root.configure(background="#011")

# variables-----------------------------------------------------------------------------------------------------------
global decimal_ip, binary_ip, octal_ip, hexadecimal_ip
decimal_ip = StringVar()
binary_ip = StringVar()
octal_ip = StringVar()
hexadecimal_ip = StringVar()

# functions-----------------------------------------------------------------------------------------------------------
def convert():
    decimal = decimal_ip.get()
    binary = binary_ip.get()
    octal = octal_ip.get()
    hex = hexadecimal_ip.get()

    result = False

    if decimal:
        try:
            float(decimal)
            result = True
        except:
            messagebox.showerror("Error", "Invalid Decimal Value", parent=root)
            decimal_ip.set('')

        if result:
            b = decimalToBinary(decimal)
            o = decimalToOctal(decimal)
            h = decimalToHex(decimal)

            binary_ip.set(b)
            octal_ip.set(o)
            hexadecimal_ip.set(h)
        
    if binary:
        s = set(binary)
        if '.' in s or '0' in s or '1' in s:
            result = True
        else:
            messagebox.showerror("Error", "Invalid Binary Value", parent=root)
            binary_ip.set('')
        
        if result:
            try:
                d = binaryToDecimal(binary)
                o = binaryToOctal(binary)
                h = binaryToHex(binary)

                decimal_ip.set(d)
                octal_ip.set(o)
                hexadecimal_ip.set(h)

            except:
                messagebox.showerror("Error", "Invalid Binary Value", parent=root)
                binary_ip.set('')

    if octal:
        try:
            o = float(octal)
            if '8' in str(o) or '9' in str(o):
                messagebox.showerror("Error", "Invalid Octal Value", parent=root)
                octal_ip.set('')
            else:
                result = True
        except:
            messagebox.showerror("Error", "Invalid Octal Value", parent=root)
            octal_ip.set('')

        if result:
            try:
                d = octalToDecimal(octal)
                b = octalToBinary(octal)
                h = octalToHex(octal)

                decimal_ip.set(d)
                binary_ip.set(b)
                hexadecimal_ip.set(h)

            except:
                messagebox.showerror("Error", "Invalid Octal Value", parent=root)
                octal_ip.set('')

    if hex:
        result = True
        for h in hex.upper():
            if h == '.':
                pass
            elif ((h < '0' or h > '9') and (h < 'A' or h > 'F')):
                result = False
                break

        if result:
            try:
                d = hexToDecimal(hex)
                b = hexToBinary(hex)
                o = hexToOctal(hex)

                decimal_ip.set(d)
                binary_ip.set(b)
                octal_ip.set(o)

            except:
                messagebox.showerror("Error", "Invalid Hexadecimal Value", parent=root)
                hexadecimal_ip.set('')
        
        else:
            messagebox.showerror("Error", "Invalid Hexadecimal Value", parent=root)
            hexadecimal_ip.set('')

def clear():
    decimal_ip.set('')
    binary_ip.set('')
    octal_ip.set('')
    hexadecimal_ip.set('')

# widgets-------------------------------------------------------------------------------------------------------------
title = Label(
    root,
    text="Number Base Conversion",
    fg="#0c0",
    bg="#011",
    font=("verdana", 30, "bold"),
    pady=20,
).pack(fill=X)

F1 = LabelFrame(
    root,
    bd=0,
    font=("verdana", 15, "bold"),
    bg="#011",
)
F1.place(relx=0.5, rely=0.5, anchor=CENTER)

decimal_lbl = Label(
    F1,
    text="Decimal No. :",
    font=("verdana", 20, "bold"),
    bg="#011",
    fg="#fff",
).grid(sticky=E, row=0, column=0, padx=20, pady=20, ipadx=10, ipady=10)

decimal_txt = Entry(
    F1, 
    width=25,
    textvariable=decimal_ip,
    font="arial 15",
    bd=7,
    relief=SUNKEN
).grid(row=0, column=1, padx=20, pady=20, ipadx=10, ipady=10)

binary_lbl = Label(
    F1,
    text="Binary No. :",
    font=("verdana", 20, "bold"),
    bg="#011",
    fg="#fff",
).grid(sticky=E, row=1, column=0, padx=20, pady=20, ipadx=10, ipady=10)

binary_txt = Entry(
    F1, 
    width=25,
    textvariable=binary_ip,
    font="arial 15",
    bd=7,
    relief=SUNKEN
).grid(row=1, column=1, padx=20, pady=20, ipadx=10, ipady=10)

octal_lbl = Label(
    F1,
    text="Octal No. :",
    font=("verdana", 20, "bold"),
    bg="#011",
    fg="#fff",
).grid(sticky=E, row=2, column=0, padx=20, pady=20, ipadx=10, ipady=10)

octal_txt = Entry(
    F1, 
    width=25,
    textvariable=octal_ip,
    font="arial 15",
    bd=7,
    relief=SUNKEN
).grid(row=2, column=1, padx=20, pady=20, ipadx=10, ipady=10)

hexadecimal_lbl = Label(
    F1,
    text="Hexadecimal No. :",
    font=("verdana", 20, "bold"),
    bg="#011",
    fg="#fff",
).grid(sticky=E, row=3, column=0, padx=20, pady=20, ipadx=10, ipady=10)

hexadecimal_txt = Entry(
    F1, 
    width=25,
    textvariable=hexadecimal_ip,
    font="arial 15",
    bd=7,
    relief=SUNKEN
).grid(row=3, column=1, padx=20, pady=20, ipadx=10, ipady=10)

convert_btn = Button(
    F1,
    text="Convert",
    command=convert,
    width=10,
    bd=7,
    font="verdana 20 bold",
).grid(row=1, column=4, columnspan=2, padx=20, pady=20, ipadx=5, ipady=5)

clear_btn = Button(
    F1,
    text="Clear",
    command=clear,
    width=10,
    bd=7,
    font="verdana 20 bold",
).grid(row=2, column=4, columnspan=2, padx=20, pady=20, ipadx=5, ipady=5)

quit_btn = Button(
    F1,
    text="Quit",
    command=root.quit,
    width=10,
    bd=7,
    font="verdana 20 bold",
).grid(row=3, column=4, columnspan=2, padx=20, pady=20, ipadx=5, ipady=5)

root.mainloop()