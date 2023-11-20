import tkinter as tk
from tkinter import scrolledtext
import threading
import socket

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server's host and port
server_host = '192.168.0.11'  # Change this to the server's IP or hostname
server_port = 12345

# Connect to the server
client.connect((server_host, server_port))

# Function to send a message
def send_message():
    message = message_entry.get()
    client.send(message.encode('utf-8'))
    message_entry.delete(0, tk.END)
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, "You: " + message + "\n")
    chat_text.config(state=tk.DISABLED)

# Function to receive and display messages from the server
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            chat_text.config(state=tk.NORMAL)
            if message.startswith("Server: "):
                chat_text.insert(tk.END, message + "\n")
            else:
                chat_text.insert(tk.END, message + "\n")
            chat_text.config(state=tk.DISABLED)
        except:
            print("Connection closed.")
            client.close()
            break

# Create a GUI for the client
client_gui = tk.Tk()
client_gui.title("Chat Client")

chat_text = scrolledtext.ScrolledText(client_gui, wrap=tk.WORD)
chat_text.config(state=tk.DISABLED)
chat_text.pack()

message_entry = tk.Entry(client_gui)
message_entry.pack()

send_button = tk.Button(client_gui, text="Send", command=send_message)
send_button.pack()

# Create a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main GUI loop
client_gui.mainloop()

