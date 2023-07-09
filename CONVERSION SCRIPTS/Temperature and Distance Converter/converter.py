from fractions import Fraction
import tkinter as tk

convert = {"Distance": {"Inches to Centimeters": lambda x: x * 2.54,
           "Centimeters to Inches": lambda x: x / 2.54,
           "Feet to Inches": lambda x: x * 12,
           "Inches to Feet": lambda x: x / 12,
           "Meters to Feet": lambda x: ((100 / 2.54) / 12) * x,
           "Feet to Meters": lambda x: x / ((100 / 2.54) / 12),
           "Inches to Meters": lambda x: (x * 2.54) / 100,
           "Meters to Inches": lambda x: (100 / 2.54) * x,
           "Miles to Feet": lambda x: x * 5280,
           "Feet to Miles": lambda x: x / 5280,
           "Miles to Yards": lambda x: x * 1760,
           "Yards to Miles": lambda x: x / 1760,
           "Miles to Kilometers": lambda x: x * 1.609,
           "Kilometers to Miles": lambda x: x / 1.609},
           "Temperature": {"Fahrenheit to Celsius": lambda x: (x - 32) * (5/9),
           "Celsius to Fahrenheit": lambda x: x * (9/5) + 32}}
    
window = tk.Tk()
window.title("Converter")
window.geometry("400x400")
bg_color, fg_color = "white", "black"
window.configure(bg = bg_color)

entry_frame = tk.Frame(window, bg = bg_color)
lbl = tk.Label(window, bg = bg_color, fg = fg_color)
lbl.pack()
for i in 'entry_lbl1', 'entry_lbl2', 'error_lbl', 'entry2':
    globals()[i] = tk.Label(entry_frame, bg = bg_color, fg = fg_color)
entry1 = tk.Entry(entry_frame)
def conversion(event):
    try:
        entry2['text'] = convert[category][choice](float(entry1.get()))
        error_lbl['text'] = ''
    except:
        error_lbl['text'] = "Sorry, please input a number."
        entry1.delete(0, tk.END); entry2['text'] = ''

entry1.bind("<Return>", conversion)

def go_back():
    for i in window.children:
        if '!radiobutton' in i:
            window.children[i].pack_forget()
    entry_frame.pack_forget(); back_btn.pack_forget()
    start()
back_btn = tk.Button(window, text = 'BACK', command = go_back)

def make_rbtns(List):
    rbtns = {}
    w = max([len(i) for i in List]) + 2
    for i in List:
        rbtns[i] = {}
        rbtns[i]['var'] = tk.StringVar()
        rbtns[i]['button'] = tk.Radiobutton(window, text = i, value = i, var = rbtns[i]['var'], fg = fg_color, bg = bg_color, width = w, anchor = 'w')
        rbtns[i]['button'].pack()
    if step != 1:
        back_btn.pack()
    return rbtns

def chosen(rbtns):
    for i in rbtns:
        rbtns[i]['button'].pack_forget()
        if rbtns[i]['var'].get() != '':
            choice = i
    return choice

def entered():
    global choice
    choice = chosen(choices)
    lbl['text'] = "Enter your conversions below:"
    entry_lbl1['text'] = choice.split("to")[0]; entry_lbl2['text'] = choice.split('to')[1]
    entry_lbl1.grid(row = 1, column = 0); entry_lbl2.grid(row = 2, column = 0)
    entry1.grid(row = 1, column = 1); entry2.grid(row = 2, column = 1)
    entry1.focus()
    error_lbl.grid(row = 3, column = 1)
    entry_frame.pack()
    back_btn.pack_forget(); back_btn.pack()

def init():
    global choices, category, step
    step = 2
    category = chosen(categories)
    choices = make_rbtns(convert[category])
    for i in choices:
        choices[i]['button']['command'] = entered

def start():
    global categories, step
    step = 1
    categories = make_rbtns(["Distance", "Temperature"])
    for i in categories:
        categories[i]['button']['command'] = init
    lbl['text'] = "What would you like to convert?"

start()
