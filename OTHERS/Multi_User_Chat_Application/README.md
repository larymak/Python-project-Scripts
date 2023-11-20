# Overview
The **Multi-User Chat Application** is a Python-based chat application designed to provide real-time text-based communication among multiple users.

# Features
The chat application includes the following key features:
* **User Nicknames:** Users can set and display personalized nicknames within the chat.
* **Private Messaging:** Users can send private messages to specific recipients.
* **Message Logging:** All chat messages are logged on the server for historical reference.
* **Error Handling:** The application handles various error scenarios for a stable user experience.

# Technologies Used
The project was implemented using the following technologies:
* **Python:** The primary programming language used for both the server and client applications.
* **Python's socket library:** Utilized for network communication between the server and clients.
* **Threading:** Implemented to enable concurrent handling of multiple client connections on the server.

# Installation and Usage
To install and use the chat application, follow these steps:
* Clone the project repository from [GitHub URL](https://github.com/AHNAF14924/Multi-User-Chat-Application.git)
* Open the terminal/command prompt.
* Navigate to the project directory.
* Start the server by running python `server.py`
* Run the client by executing python `client.py`
 ## Server Setup
 * Choose one of the computers to act as the server. This computer will run the server code.
 * Modify the server code to use the computer's local IP address (e.g., '192.168.x.x' or '10.0.x.x') in the host variable. This allows other computers to connect to the server.
 * Run the server code on the chosen computer.
 
 Example server code (change 'host' to the local IP address):

 ```
 host = '192.168.x.x'  # Use the local IP address of the server computer
port = 12345  # You can keep the same port
 ```
Start the server:
```
python3 server.py
```
## Client Setup
* On each of the other computers, you will run the client code.
* Modify the client code to use the IP address of the computer running the server in the server_host variable.
* Run the client code on each computer.

Example client code (change 'server_host' to the server's IP address):
```
server_host = '192.168.x.x'  # Use the server's local IP address
server_port = 12345  # Keep the same port as the server
```
Start the client on each computer:

```
python3 client.py
```
## Join the Chat

* After starting the client on each computer, you will be prompted to set a nickname. Enter a unique nickname for each user.
* Once the nickname is set, you can start sending messages by typing in the terminal of each client. Messages will be sent to the server and broadcast to all connected clients.

## Sending Messages

* To send a regular message, type your message and press Enter. It will be broadcast to all connected clients.
* To send a private message to a specific user, use the "@" symbol followed by the recipient's nickname, a space, and your message. For example: `@JohnDoe Hi, John!`

## Exiting the Application
To exit the chat application:
* Type `exit` in the terminal and press Enter. This will disconnect you from the chat and close the client application.
