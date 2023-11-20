import socket
import threading

# Create a socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '192.168.0.11'  # Listen on all available network interfaces
port = 12345

# Bind the socket to the host and port
server.bind((host, port))

# Listen for incoming connections
server.listen()

print(f"Server listening on {host}:{port}")

# Store client connections and nicknames in dictionaries
clients = {}
nicknames = {}

# Function to broadcast messages to all connected clients
def broadcast(message, sender=None):
    for client_socket, nickname in zip(clients, nicknames):
        if client_socket != sender:
            try:
                client_socket.send(message.encode('utf-8'))
            except:
                remove_client(client_socket)

# Function to handle client connections
def handle_client(client_socket):
    try:
        # Request and store the user's nickname
        client_socket.send("Enter your nickname: ".encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        nicknames[client_socket] = nickname
        print(f"Nickname of {nickname} is set.")

        # Welcome message
        welcome_message = f"Welcome, {nickname}!"
        client_socket.send(welcome_message.encode('utf-8'))

        while True:
            message = client_socket.recv(1024)
            if not message:
                remove_client(client_socket)
                break
            elif message.decode('utf-8').lower() == 'exit':
                remove_client(client_socket)
            elif message.decode('utf-8').startswith('@'):
                # Private message
                recipient = message.decode('utf-8').split(' ')[0][1:]
                if recipient in nicknames.values():
                    recipient_socket = list(nicknames.keys())[list(nicknames.values()).index(recipient)]
                    recipient_socket.send(f"(Private) {nickname}: {message.decode('utf-8')[len(recipient) + 2:]}".encode('utf-8'))
                else:
                    client_socket.send("Recipient not found.".encode('utf-8'))
            else:
                # Broadcast regular message
                broadcast(f"{nickname}: {message.decode('utf-8')}", sender=client_socket)
    except:
        remove_client(client_socket)

# Function to remove a client from the server
def remove_client(client_socket):
    if client_socket in clients:
        print(f"Connection closed with {nicknames[client_socket]}")
        del nicknames[client_socket]
        clients.pop(client_socket)
        client_socket.close()

# Main server loop
while True:
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address}")
    clients[client_socket] = client_address

    # Start a thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

