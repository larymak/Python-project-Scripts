from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk
import random
import string
import pyperclip
import re

crack_speed = 400000000000
format = {'Uppercase characters': 0,
            'Lowercase characters': 0,
            'Special characters': 0,
            'Numbers': 0}

entropies = {'Uppercase characters': 26,
             'Lowercase characters': 26,
             'Special characters': 33,
             'Numbers': 10}

# Define the main function for generating the password
def generate_password():
    password_length = length_entry.get()
    if password_length.isdigit() and int(password_length) > 0:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(password_length)))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_ckeck = password_strength(password)
        passwordStrength.config(text=password_ckeck)
    else:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Invalid password length")

# Define the function for copying the password to the clipboard
def copy_password():
    password = password_entry.get()
    pyperclip.copy(password)

#Define the function to ckeck the password strength
def password_strength(password):
    password_len = len(password) 
    if(len(password) < 7):
        strength = "very weak"
    else:
        if( len(password) < 9 ):
            strength = "weak"
        else:
            if(len(password) < 11):
                strength = "good"
            else:
                strength = "strong"
    for char in password:
        if re.match("[0-9]", char):
            format["Numbers"] += 1
        elif re.match("[a-z]", char):
            format["Lowercase characters"] += 1
        elif re.match("[A-Z]", char):
            format["Uppercase characters"] += 1
        else:  
            format["Special characters"] += 1
    entropy = 0
    for frm in format.keys():
        if format[frm] > 0:
            entropy += entropies[frm]
    
    time_ = "hours"
    cracked = ((entropy**password_len) / crack_speed) / 3600 # Hours in seconds

    if cracked > 24:
        cracked = cracked / 24
        time_ = "days"

    if cracked > 365:
        cracked = cracked / 365
        time_ = "years"

    if time_ == "years" and cracked > 100:
        cracked = cracked / 100
        time_ = "centuries"

    if time_ == "centuries" and cracked > 1000:
        cracked = cracked / 1000
        time_ = "millennia"
    cracked = "\nTime to crack password:   {:,.2f} {}".format(cracked, time_)
    text = strength + cracked
    return text


# Create the main window
root = tk.Tk()
root.geometry("350x350")
root.title("Password Generator")

# Create the password length label and entry widget
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)
length_entry = tk.Entry(root, width=5)
length_entry.pack()

# Create the "Generate Password" button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Create the password entry widget
password_label = tk.Label(root, text="Generated Password:")
password_label.pack()
password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=10)

passwordStrength = tk.Label(root, text = "")
passwordStrength.pack()

# Create the "Copy Password" button
copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack(pady=10)

# Set the focus on the length entry widget
length_entry.focus()

# Run the main loop
root.mainloop()
