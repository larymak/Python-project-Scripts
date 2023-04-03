import tkinter as tk
import random
import string
import pyperclip

# Define the main function for generating the password
def generate_password():
    password_length = length_entry.get()
    if password_length.isdigit() and int(password_length) > 0:
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=int(password_length)))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    else:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Invalid password length")

# Define the function for copying the password to the clipboard
def copy_password():
    password = password_entry.get()
    pyperclip.copy(password)

# Create the main window
root = tk.Tk()
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

# Create the "Copy Password" button
copy_button = tk.Button(root, text="Copy Password", command=copy_password)
copy_button.pack(pady=10)

# Set the focus on the length entry widget
length_entry.focus()

# Run the main loop
root.mainloop()
