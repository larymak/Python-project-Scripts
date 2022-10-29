# the calculator
from tkinter import Tk, Button, Label, Grid, Entry, END

root = Tk()
root.title("CALCULATOR")
e = Entry(
    root,
    width=35,
    borderwidth=10,
)
e.grid(row=0, column=0, columnspan=4, padx=8, pady=8)


def joker(number):
    now = e.get()
    e.delete(0, END)
    e.insert(0, str(now) + str(number))


def addd():
    n1 = e.get()
    global num1
    global cal
    cal = "add"
    num1 = float(n1)
    e.delete(0, END)


def sub():
    n1 = e.get()
    global num1
    global cal
    cal = "sub"
    num1 = float(n1)
    e.delete(0, END)


def mul():
    n1 = e.get()
    global num1
    global cal
    cal = "mul"
    num1 = float(n1)
    e.delete(0, END)


def div():
    n1 = e.get()
    global num1
    global cal
    cal = "div"
    num1 = float(n1)
    e.delete(0, END)


def equ():
    if cal == "add":
        n2 = e.get()
        e.delete(0, END)
        e.insert(0, num1 + float(n2))
    elif cal == "sub":
        n2 = e.get()
        e.delete(0, END)
        e.insert(0, num1 - float(n2))
    elif cal == "mul":
        n2 = e.get()
        e.delete(0, END)
        e.insert(0, num1 * float(n2))
    elif cal == "div":
        n2 = e.get()
        e.delete(0, END)
        e.insert(0, num1 / float(n2))
    else:
        pass


def clr():
    e.delete(0, END)


# bottons
btn1 = Button(root, text="1", padx=20, pady=5, command=lambda: joker("1"))
btn2 = Button(root, text="2", padx=20, pady=5, command=lambda: joker("2"))
btn3 = Button(root, text="3", padx=20, pady=5, command=lambda: joker("3"))
btn4 = Button(root, text="4", padx=20, pady=5, command=lambda: joker("4"))
btn5 = Button(root, text="5", padx=20, pady=5, command=lambda: joker("5"))
btn6 = Button(root, text="6", padx=20, pady=5, command=lambda: joker("6"))
btn7 = Button(root, text="7", padx=20, pady=5, command=lambda: joker("7"))
btn8 = Button(root, text="8", padx=20, pady=5, command=lambda: joker("8"))
btn9 = Button(root, text="9", padx=20, pady=5, command=lambda: joker("9"))
btn0 = Button(root, text="0", padx=20, pady=5, command=lambda: joker("0"))
btnadd = Button(root, text="+", padx=20, pady=5, command=addd)
btnsub = Button(root, text="-", padx=20, pady=5, command=sub)
btnmul = Button(root, text="*", padx=20, pady=5, command=mul)
btndiv = Button(root, text="/", padx=20, pady=5, command=div)
btnequ = Button(root, text="=", padx=20, pady=5, command=equ)
btndot = Button(root, text=".", padx=20, pady=5, command=lambda: joker("."))
btnclr = Button(root, text="clear", padx=20, pady=5, command=clr)


btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)
btn0.grid(row=4, column=1)
btnadd.grid(row=1, column=3)
btnsub.grid(row=2, column=3)
btnmul.grid(row=3, column=3)
btndiv.grid(row=4, column=3)
btnequ.grid(row=4, column=0)
btndot.grid(row=4, column=2)
btnclr.grid(row=5, column=1)

root.mainloop()
